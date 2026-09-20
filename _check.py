#!/usr/bin/env python3
"""章节交付前自查 —— 所有写章 agent 统一跑这一个。

用法: python3 _check.py docs/chXX_xxx.md
退出码 0 = 全过；1 = 有不过项。
"""
import re
import sys
import pathlib

def main():
    if len(sys.argv) < 2:
        print("用法: python3 _check.py <章节文件>"); return 2
    f = sys.argv[1]
    t = pathlib.Path(f).read_text(encoding="utf-8")
    raw = t
    t_nocode = re.sub(r"```.*?```", "", t, flags=re.S)

    fails = []

    # 1) 单美元：数学里不能出现单个 $（代码块已剥离）
    single = [i for i, l in enumerate(t_nocode.splitlines(), 1)
              if re.search(r"(?<!\$)\$(?!\$)", l)]
    print("1) 单美元（数学里）: %d 行%s" % (len(single), ("  " + str(single[:6])) if single else ""))
    if single: fails.append("单美元")

    # 2) 数学跨度内的裸竖线
    #    ★ 只看 $$...$$ 之间；表格的 | 是单元格分隔符，不算
    # ★ 必须跨行匹配：display 公式常写成 $$ 换行 内容 换行 $$，
    #   按行匹配会整段漏掉（ch13 的 agent 指出了这个盲区）。
    bad = []
    _lines = t_nocode.split("\n")
    for m in re.finditer(r"\$\$(.+?)\$\$", t_nocode, re.S):
        if "|" in m.group(1):
            _ln = t_nocode[:m.start()].count("\n") + 1
            bad.append((_ln, m.group(1).strip().replace("\n", " ")[:60]))
    print("2) 数学跨度内裸竖线: %d 处%s" % (len(bad), ("  " + str(bad[:4])) if bad else ""))
    if bad: fails.append("裸竖线")

    # 3) Liquid 冲突
    liq = [(i, l[:60]) for i, l in enumerate(raw.splitlines(), 1)
           if ("{{" in l or "{%" in l) and "{% raw %}" not in l and "{% endraw %}" not in l]
    print("3) Liquid {{ / {%%: %d 行%s" % (len(liq), ("  " + str(liq[:4])) if liq else ""))
    if liq: fails.append("Liquid")

    # 4) 首行不能是 ---
    _ls = raw.splitlines()
    # 允许「有效的最小 front matter」：首行 --- 且 3 行内出现第二个 ---
    _fm = (_ls and _ls[0].strip() == "---"
           and any(x.strip() == "---" for x in _ls[1:6]))
    first = _ls[0] if _ls else ""
    ok4 = _fm or not first.strip().startswith("---")
    print("4) 首行: %r  %s" % (first[:50], "OK" + ("（合法 front matter）" if _fm else "") if ok4 else "✗ 无效 front matter"))
    if not ok4: fails.append("首行---")

    # 5) 七节齐全
    nsec = len(re.findall(r"^## ", t, re.M))
    print("5) ## 节数: %d  %s" % (nsec, "OK" if nsec >= 7 else "✗ 少于 7"))
    if nsec < 7: fails.append("节数")

    # 附加：$$ 成对 + 中文字数
    nd = len(re.findall(r"\$\$", t))
    print("   附) $$ 总数 %d（%s）" % (nd, "成对" if nd % 2 == 0 else "✗ 奇数，有未闭合"))
    if nd % 2: fails.append("$$未闭合")
    cn = len(re.findall(r"[\u4e00-\u9fff]", t))
    print("   附) 中文字数 %d  %s" % (cn, "OK" if 3000 <= cn <= 12000 else "⚠ 不在 4000–8000 附近"))

    # 6) 编号单调性与重号（只认真正的"陈述行"：**定理 3.1** 或 **定理 3.1（…）**）
    #    ⚠️ 不能写松，否则正文里的回指（"**定理 3.31 说**：…"）会被当成重复陈述
    import collections
    # 允许：数字后接 **（（。）都可；类型词补上 约定/例；否则会漏计
    # 编号后必须紧跟 ** / （ / 。 —— 否则会把正文回指（"**定理 3.8 的立即推论**"）
    # 误当成第二条陈述（这已是本式第 4 次迭代，两个方向都踩过）
    # 编号后必须紧跟 ** / （ / 。 / .** —— 否则会把正文回指（"**定理 3.8 的立即推论**"）当成第二条
    # 定义/定理/引理/推论/命题/约定 共享一个计数器；例、注 各自独立（教科书惯例）
    _stmt = re.findall(r"^\*\*(定义|定理|引理|推论|命题|约定|例|注)\s+(\d+\.\d+)(?:\*\*|（|。|\.\*\*)", t, re.M)
    _G = {"A": {"定义","定理","引理","推论","命题","约定"}, "B": {"例"}, "C": {"注"}}
    _rev, _dup = [], {}
    for gname, types in _G.items():
        seq = [(ty, n) for ty, n in _stmt if ty in types]
        nums = [tuple(int(x) for x in n.split(".")) for _, n in seq]
        _rev += [(seq[i], seq[i+1]) for i in range(len(nums)-1) if nums[i+1] < nums[i]]
        import collections as _c
        _dup.update({k: v for k, v in _c.Counter(seq).items() if v > 1})
    stmts = _stmt

    print("6) 编号: %d 条  单调性 %s  重号 %s" % (len(stmts), "OK" if not _rev else "✗ 逆序 %s" % _rev[:2], _dup or "无"))
    if _rev: fails.append("编号逆序")
    if _dup: fails.append("编号重复")

    # 7) 控制字符 —— Python 写文件时字符串没加 raw 前缀，\t \b \f \v 会被真的解释掉，
    #    把 LaTeX 的 \times/\to/\big/\blacksquare 变成不可见控制符。肉眼看不出来，必须机器查。
    import unicodedata as _ud
    _ctrl = {chr(x): _ud.name(chr(x), "?") for x in
             list(range(0, 9)) + list(range(11, 13)) + list(range(14, 32)) + [127]}
    _hits = {}
    for _i, _ch in enumerate(t):
        if _ch in _ctrl:
            _hits[_ctrl[_ch]] = _hits.get(_ctrl[_ch], 0) + 1
    print("7) 控制字符: %d %s" % (sum(_hits.values()), _hits or ""))
    if _hits: fails.append("控制字符")

    # 8) 练习完整性 —— 这是最容易"看着写完了其实没写"的一节
    #    有 agent 把 `## 六、练习` 留成「（待填）」就交付了
    _q = len(re.findall(r"^\*\*[基竞研][0-9]+\.", t, re.M))   # 宽式：题面可带标题 **研1.（…）**
    _a = len(re.findall(r"^\*\*解 [基竞研][0-9]+\.\*\*", t, re.M))
    _sol_sec = "### 解答 (Solutions)" in t or "### 解答(Solutions)" in t
    _stub = bool(re.search(r"^\s*[（(]待填[）)]\s*$", t, re.M))
    _ok8 = (_q >= 8) and (_a == _q) and _sol_sec and not _stub
    print("8) 练习: 题面 %d  解答 %d  解答节 %s%s  %s"
          % (_q, _a, "有" if _sol_sec else "✗无",
             "  ⚠️有『（待填）』占位" if _stub else "",
             "OK" if _ok8 else "✗ 不完整"))
    if not _ok8: fails.append("练习不完整")

    print("\n结果: " + ("全过 ✓" if not fails else "✗ 未过: " + "、".join(fails)))
    return 0 if not fails else 1

if __name__ == "__main__":
    sys.exit(main())
