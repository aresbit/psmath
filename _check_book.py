#!/usr/bin/env python3
"""全书级检查：导航链接 ↔ 实际文件、各章自查、进度统计。"""
import re, subprocess, pathlib, sys

D = pathlib.Path(__file__).resolve().parent / "docs"
actual = {p.name for p in D.glob("ch*.md")}

links = {}
for nav in ("index.md", "_sidebar.md"):
    f = D / nav
    if not f.exists(): continue
    links[nav] = [l for l in re.findall(r"\]\(([^)]*\.md)\)", f.read_text(encoding="utf-8"))
                  if l.startswith("ch")]

print("== 导航链接 ==")
broken_now, pending = [], 0
plan = []
for nav, ls in links.items():
    b = [l for l in ls if l not in actual]
    broken_now += b
    print("  %-12s 链 %d 断链 %d" % (nav, len(ls), len(b)))
    if not plan: plan = ls
pending = len(broken_now)
missing = [l for l in plan if l not in actual]
if missing:
    print("  未写章节 %d 个（预期）：%s…" % (len(missing), missing[0]))

# 断链里如果有"已写的号"却对不上，就是真断链
nums_written = {n[:5] for n in actual}
real_broken = [l for l in missing if l[:5] in nums_written]
print("  ⚠️ 真断链（该章已存在但链接对不上）: %d %s" % (len(real_broken), real_broken or "✓"))

# ── 各章章末导航块的邻居链接也要核 ──
planned = set(re.findall(r"\]\((ch[^)]*\.md)\)", (D / "index.md").read_text(encoding="utf-8")))
nav_bad = []
for p_ in sorted(D.glob("ch*.md")):
    txt = p_.read_text(encoding="utf-8")
    if "chapter-nav" not in txt: continue
    for t in re.findall(r'href="(ch[^"]*\.md)"', txt[txt.find("chapter-nav"):]):
        if t not in planned:
            nav_bad.append((p_.name, t))
print("\n== 章末导航块 ==")
if nav_bad:
    for a, t in nav_bad: print("  ✗ %-44s → %s" % (a[:44], t))
else:
    print("  邻居链接全部指向计划内文件名 ✓")

incomplete = []
# ── 悬空引用审计 ──
#    判据：引用 X.Y 若不在本章陈述里，且**其前 150 字符内出现过「第 NN 章」**，
#    则视为跨章引用（不算悬空）。第一版直接删「第 NN 章」→ 剩下的引用又变"无章号"，
#    导致 ch06 的 ch05 引用被反复误报。改为按距离判断。
print("\n== 悬空引用 ==")
_dang = 0
for p_ in sorted(D.glob("ch*.md")):
    txt = p_.read_text(encoding="utf-8")
    stmts = {m.group(2) for m in re.finditer(
        r"^\*\*((?:定义|定理|引理|推论|命题)(?:\s*/\s*(?:定义|定理|引理|推论|命题))*) (\d+\.\d+)",
        txt, re.M)}
    if len(stmts) < 3:
        continue
    bad = []
    for m in re.finditer(r"(定义|定理|引理|推论|命题)\s+(\d+\.\d+)", txt):
        num = m.group(2)
        if num in stmts:
            continue
        before = txt[max(0, m.start() - 150):m.start()]
        if re.search(r"第\s*\d+\s*章", before):
            continue                       # 跨章引用
        bad.append(num)
    bad = sorted(set(bad))
    if bad:
        _dang += len(bad)
        print("  ⚠️ %-44s 悬空 %s" % (p_.name[:44], bad[:8]))
print("  悬空引用合计: %d" % _dang)
print("\n== 各章自查 ==")
ok = fail = 0
total = 0
for p in sorted(D.glob("ch*.md")):
    r = subprocess.run([sys.executable, str(D.parent / "_check.py"), str(p)],
                       capture_output=True, text=True)
    s = p.read_text(encoding="utf-8")
    cn = len(re.findall(r"[\u4e00-\u9fff]", s))
    # 识别"骨架已建但没填完"：七节齐全却字数很低
    nsec = len(re.findall(r"^## ", s, re.M))
    if nsec >= 7 and cn < 3000:
        print("  ⏳ %-44s 七节骨架已建但只填了 %d 字 —— 需续写" % (p.name[:44], cn))
        incomplete.append(p.name)
    elif nsec < 7:
        print("  ⏳ %-44s 只有 %d 节（<7）—— 骨架未完成" % (p.name[:44], nsec))
        incomplete.append(p.name)
    if cn > 3000: total += cn
    good = "全过" in r.stdout
    ok += good; fail += (not good)
    if not good:
        last = [l for l in r.stdout.splitlines() if l.startswith("结果")]
        print("  ✗ %-44s %s" % (p.name[:44], last[0] if last else "?"))
print("  %d 过 / %d 未过" % (ok, fail))
print("\n== 规模 ==")
print("  已写章节 %d / 40   完成章合计 %s 中文字" % (len(actual), format(total, ",")))
