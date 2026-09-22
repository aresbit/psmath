---
layout: default
---

# 第30章: Hilbert 空间与内积结构·下：完整推导 (Hilbert Spaces and Inner Product Structure · Part II: Full Derivation)

> 专家依据: `_experts/analysis/functional-analysis.md` + `_experts/analysis/_SKILL.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）
> 配套预备: 见 第29章 Hilbert 空间与内积结构·上（同一主题的具体铺垫，建议先读）

## 一、本章概要 (Overview)

读完第29章的具体例子后——你已经亲手验证过 Cauchy–Schwarz、算出过平行四边形法则的成立与失效、构造过一个真正"走不出多项式空间"的柯西列、也解过一次具体的 Gram 矩阵——这里把同样的构造写成对任意内积空间都成立的一般定义，并给出完整证明。

**从哪来**：第 08 章的 定理 3.6 证明了「内积给出 $$V\to V^*$$ 的自然同构 $$g^\flat$$」，第 06 章的 定理 3.21 又证明了「$$V\cong V^*$$ 不自然」。这两个结论在有限维里说得通：内积一次选定，之后的指标升降就只是"把向量搬成泛函"。但第 06 章的问题 3 已经埋了地雷——$$V=\mathbb{R}[x]$$ 时 $$\dim V=\aleph_0$$ 而 $$\dim V^*=\mathfrak{c}$$，$$V$$ 与 $$V^*$$ 之间连**同构**都不存在，更不必谈"自然"。本章要回答的就是：**$$g^\flat$$ 在无穷维里什么时候还是同构？**

**到哪去**：答案是——当且仅当空间**完备**且范数**来自内积**，即空间是 **Hilbert 空间**。这时 $$g^\flat$$ 被 Riesz 表示定理救活，$$H\cong H^*$$ 成为内积的免费赠品，而 Banach 空间一般不享有。这一章同时把第 08 章的正交概念从有限维搬到无穷维：正交补、正交投影、正交规范基。下一章（第 32 章）将把这套语言直接翻译成量子力学的态、可观测量与测量。

**核心问题**：$$L^2$$ 上的 Fourier 级数为什么"能收敛到函数"却又"逐点常常不收敛"？本章给出的解释是：Fourier 级数的收敛是**范数收敛**（正交基展开），而逐点收敛是另一件事——两者的差别正是"内积几何"与"点态分析"的差别。

## 二、入口：一道具体的问题 (Entry Problem)

> 题目来源：自编。母题是 MP38（泛函分析与量子力学）里 "Riesz 引理" 那一段，以及线性代数教材中「多项式空间在 $$L^2$$ 范数下不完备」的经典例题。

**问题 2.1.** 取向量空间 $$V=\mathbb{R}[x]$$（实系数多项式全体），在 $$V$$ 上定义

$$\langle f,g\rangle=\int_0^1 f(x)g(x)\,dx .$$

记 $$\lVert f\rVert=\sqrt{\langle f,f\rangle}$$。回答下列四问：

**(i)** 验证 $$\langle\cdot,\cdot\rangle$$ 满足内积的三条公理，从而 $$V$$ 是一个**内积空间**。

**(ii)** $$(V,\lVert\cdot\rVert)$$ 完备吗？也就是说，$$V$$ 中的每个柯西列都收敛到 $$V$$ 中的一个元素吗？

**(iii)** 定义泛函 $$\ell(f)=\displaystyle\int_0^1 f(x)e^x\,dx$$（$$e^x$$ 是那个超越函数，不是多项式）。先证 $$\ell$$ 是 $$V$$ 上的**连续**线性泛函，即 $$\ell\in V^*$$。再问：**存在**多项式 $$g\in V$$ 使

$$\ell(f)=\langle f,g\rangle\qquad\text{对一切 }f\in V$$

成立吗？

**(iv)**（预告，本章末尾回来）在 $$L^2([-\pi,\pi])$$ 上，三角系 $$\lbrace e^{inx}/\sqrt{2\pi}\rbrace_{n\in\mathbb{Z}}$$ 是正交规范集。我们将证明：对任何 $$f\in L^2$$，

$$\Bigg\lVert f-\sum_{\lvert n\rvert\le N}\hat f(n)e^{inx}\Bigg\rVert_2\xrightarrow[\ N\to\infty\ ]{}0 .$$

可是历史上，连续函数的 Fourier 级数确实有在某点发散的例子。**范数收敛与逐点发散如何共存？**

**为什么这道题是全章的引子。** (ii)(iii) 两问合起来说明一件事：第 08 章 定理 3.6 里那个"免费"的 $$g^\flat:V\to V^*$$，在无穷维里可能**不是满射**——$$V$$ 里根本没有向量能代表 $$\ell$$。而 (iii) 的失败不是因为我们选的泛函太怪异，恰恰因为它太自然（$$e^x$$ 是 $$[0,1]$$ 上最规矩的函数之一）。本章第三节给治病的手段（完备化，定理 3.6）并把失败定位到"不完备"上（定理 3.14），第六节的练习研究题 1 会把 (ii)(iii) 彻底收尾；(iv) 则由注 3.19 回答。

## 三、结构：定义与完整推导 (Structure & Proof)

本节把内积从有限维搬到无穷维。搬运分三步：先立内积（3.1–3.5），再补完备性（3.6），最后看完备性到底买来了什么（3.9–3.14），末了把正交基这条线铺完（3.15–3.19）。

### 3.1 内积、范数、以及三条不等式

**定义 3.1（内积空间, inner product space）。** 设 $$H$$ 是域 $$\mathbb{F}$$（$$\mathbb{R}$$ 或 $$\mathbb{C}$$）上的线性空间。映射 $$\langle\cdot,\cdot\rangle:H\times H\to\mathbb{F}$$ 称为**内积 (inner product)**，若对一切 $$x,y,z\in H$$ 与 $$\alpha,\beta\in\mathbb{F}$$：

1. **对第一变元线性**：$$\langle\alpha x+\beta y,z\rangle=\alpha\langle x,z\rangle+\beta\langle y,z\rangle$$；
2. **共轭对称**：$$\langle x,y\rangle=\overline{\langle y,x\rangle}$$；
3. **正定**：$$\langle x,x\rangle\ge0$$，且 $$\langle x,x\rangle=0\iff x=0$$。

带内积的线性空间称为**内积空间 (inner product space)**，又称 **pre-Hilbert 空间 (pre-Hilbert space)**。

由 1、2 立刻得到**对第二变元共轭线性**：$$\langle x,\alpha y+\beta z\rangle=\overline{\alpha}\langle x,y\rangle+\overline{\beta}\langle x,z\rangle$$（先交换再取共轭即可）。实情形下 $$\overline{\alpha}=\alpha$$，共轭线性退化为线性。

**注 3.1（谁是"第一变元"是个约定）。** 本书取"第一变元线性、第二变元共轭线性"。物理文献常反过来（把共轭放在第一变元）。**哪个变元带共轭不影响任何定理的内容**，只影响公式里共轭出现的位置；读者看别的书时先确认约定即可。

**定理 3.2（Cauchy–Schwarz 不等式）。** 对一切 $$x,y$$，

$$\lvert\langle x,y\rangle\rvert\le\lVert x\rVert\,\lVert y\rVert ,$$

等号成立当且仅当 $$x,y$$ 线性相关。

*证明。* 若 $$y=0$$，两边都是 $$0$$，且 $$x,y$$ 线性相关，结论成立。设 $$y\ne0$$，则 $$\lVert y\rVert^2=\langle y,y\rangle>0$$。令

$$z=x-\frac{\langle x,y\rangle}{\lVert y\rVert^{2}}\,y .$$

直接计算 $$\lVert z\rVert^2$$：由第一变元线性与第二变元共轭线性，

$$\lVert z\rVert^{2}=\langle z,z\rangle=\Big\langle x-\tfrac{\langle x,y\rangle}{\lVert y\rVert^{2}}y,\ x-\tfrac{\langle x,y\rangle}{\lVert y\rVert^{2}}y\Big\rangle$$

$$=\lVert x\rVert^{2}-\frac{\langle x,y\rangle}{\lVert y\rVert^{2}}\overline{\langle x,y\rangle}-\frac{\overline{\langle x,y\rangle}}{\lVert y\rVert^{2}}\langle x,y\rangle+\frac{\langle x,y\rangle\,\overline{\langle x,y\rangle}}{\lVert y\rVert^{4}}\lVert y\rVert^{2}$$

$$=\lVert x\rVert^{2}-\frac{\lvert\langle x,y\rangle\rvert^{2}}{\lVert y\rVert^{2}}-\frac{\lvert\langle x,y\rangle\rvert^{2}}{\lVert y\rVert^{2}}+\frac{\lvert\langle x,y\rangle\rvert^{2}}{\lVert y\rVert^{2}}=\lVert x\rVert^{2}-\frac{\lvert\langle x,y\rangle\rvert^{2}}{\lVert y\rVert^{2}} .$$

由正定性 $$\lVert z\rVert^2\ge0$$，移项得 $$\lvert\langle x,y\rangle\rvert^{2}\le\lVert x\rVert^{2}\lVert y\rVert^{2}$$，开方即得所求。

**等号情形。** 若 $$\lvert\langle x,y\rangle\rvert=\lVert x\rVert\lVert y\rVert$$，上面的等式链给出 $$\lVert z\rVert^2=0$$，由正定性 $$z=0$$，即 $$x=\frac{\langle x,y\rangle}{\lVert y\rVert^2}y$$，二者线性相关。反之若 $$x=cy$$，则 $$\lvert\langle cy,y\rangle\rvert=\lvert c\rvert\,\lVert y\rVert^2=\lVert cy\rVert\lVert y\rVert$$，等号成立。$$\blacksquare$$

**定理 3.3（内积诱导的范数）。** 令 $$\lVert x\rVert:=\sqrt{\langle x,x\rangle}$$。则 $$\lVert\cdot\rVert$$ 是 $$H$$ 上的范数，且

$$\lVert x+y\rVert^{2}=\lVert x\rVert^{2}+2\operatorname{Re}\langle x,y\rangle+\lVert y\rVert^{2}. \tag{3.1}$$

*证明。* **正定性与齐次性**：由内积公理 3，$$\lVert x\rVert\ge0$$ 且 $$\lVert x\rVert=0\iff x=0$$；由第一变元线性，

$$\lVert\alpha x\rVert^{2}=\langle\alpha x,\alpha x\rangle=\alpha\overline{\alpha}\,\langle x,x\rangle=\lvert\alpha\rvert^{2}\lVert x\rVert^{2}.$$

**三角不等式**：展开 $$\lVert x+y\rVert^2$$，用共轭对称 $$\langle y,x\rangle=\overline{\langle x,y\rangle}$$ 得

$$\lVert x+y\rVert^{2}=\lVert x\rVert^{2}+\langle x,y\rangle+\langle y,x\rangle+\lVert y\rVert^{2}=\lVert x\rVert^{2}+2\operatorname{Re}\langle x,y\rangle+\lVert y\rVert^{2},$$

这正是 (3.1)。又 $$\operatorname{Re}\langle x,y\rangle\le\lvert\langle x,y\rangle\rvert$$，由定理 3.2 得

$$\lVert x+y\rVert^{2}\le\lVert x\rVert^{2}+2\lVert x\rVert\lVert y\rVert+\lVert y\rVert^{2}=(\lVert x\rVert+\lVert y\rVert)^{2}.$$

开方即得三角不等式。$$\blacksquare$$

于是每个内积空间自动是一个**赋范空间**；$$\lVert x-y\rVert$$ 就是两点距离 $$d(x,y)$$，可以谈收敛：$$x_n\to x$$ 意味着 $$\lVert x_n-x\rVert\to0$$。

**定义 3.4（Hilbert 空间, Hilbert space）。** 若内积空间 $$H$$ 在范数 $$\lVert\cdot\rVert$$ 下**完备**（每个柯西列都收敛），则称 $$H$$ 为 **Hilbert 空间**。

（glossary 里记录的译名是「Hilbert 空间」；本书正文统一写 "Hilbert 空间"，与第 08 章、第 28 章的写法保持一致。）

**定理 3.5（平行四边形法则与"范数来自内积"的判别）。**

(i) 内积空间中恒有

$$\lVert x+y\rVert^{2}+\lVert x-y\rVert^{2}=2\lVert x\rVert^{2}+2\lVert y\rVert^{2}. \tag{3.2}$$

(ii) 反之，设 $$\lVert\cdot\rVert$$ 是线性空间 $$X$$ 上的范数，若它满足 (3.2)，则 $$X$$ 上的内积可由范数还原：

$$\langle x,y\rangle=\tfrac14\Big(\lVert x+y\rVert^{2}-\lVert x-y\rVert^{2}\Big)\quad(\mathbb{F}=\mathbb{R}\ \text{情形}), \tag{3.3}$$

复情形则用**极化恒等式 (polarization identity)**

$$\langle x,y\rangle=\tfrac14\Big(\lVert x+y\rVert^{2}-\lVert x-y\rVert^{2}+i\lVert x+iy\rVert^{2}-i\lVert x-iy\rVert^{2}\Big). \tag{3.4}$$

于是：**一个 Banach 空间是 Hilbert 空间，当且仅当它的范数满足平行四边形法则。**

*证明。* **(i)** 由 (3.1) 分别写 $$x+y$$ 与 $$x-y$$（注意 $$\operatorname{Re}\langle x,-y\rangle=-\operatorname{Re}\langle x,y\rangle$$）：

$$\lVert x+y\rVert^{2}=\lVert x\rVert^{2}+\lVert y\rVert^{2}+2\operatorname{Re}\langle x,y\rangle,$$

$$\lVert x-y\rVert^{2}=\lVert x\rVert^{2}+\lVert y\rVert^{2}-2\operatorname{Re}\langle x,y\rangle .$$

两式相加即得 (3.2)。

**(ii)** 只对实情形验证 (3.3) 给出的 $$\langle\cdot,\cdot\rangle$$ 确实是内积，复情形把每个等式逐项核对即可（差异只在第四项多因子 $$i$$，且需用 $$\lVert iy\rVert=\lVert y\rVert$$）。记 $$S(x,y)=\frac14(\lVert x+y\rVert^2-\lVert x-y\rVert^2)$$。

*对称性*：$$\lVert x-y\rVert=\lVert y-x\rVert$$ 直接给出 $$S(x,y)=S(y,x)$$。

*正定性与 $$\langle x,x\rangle=\lVert x\rVert^2$$*：取 $$y=x$$，得 $$S(x,x)=\frac14(\lVert 2x\rVert^2-0)=\frac14\cdot 4\lVert x\rVert^2=\lVert x\rVert^{2}\ge0$$，且等号只在 $$x=0$$。

*加性*：需证 $$S(x+y,z)=S(x,z)+S(y,z)$$，等价于（两边同乘 4，记 $$Q(a)=\lVert a\rVert^{2}$$）

$$Q(x+y+z)-Q(x+y-z)=\big[Q(x+z)-Q(x-z)\big]+\big[Q(y+z)-Q(y-z)\big]. \tag{3.5}$$

我们只用平行四边形法则证明 (3.5)。把 (3.2) 用在两对向量上：

$$\underbrace{Q(x+y+z)+Q(x-y+z)}_{u=x+z,\ v=y}=2Q(x+z)+2Q(y), \tag{A}$$

$$\underbrace{Q(x+y-z)+Q(x-y-z)}_{u=x-z,\ v=y}=2Q(x-z)+2Q(y). \tag{B}$$

(A) 减 (B)。注意 $$x-y+z=-\big((y-x)-z\big)$$、$$x-y-z=-\big((y-x)+z\big)$$，而 $$Q(-w)=Q(w)$$，故

$$Q(x+y+z)-Q(x+y-z)-\big[Q(y-x+z)-Q(y-x-z)\big]=2\big[Q(x+z)-Q(x-z)\big]. \tag{C}$$

再把 $$x$$ 与 $$y$$ 的角色互换，重做同一步骤（把 (A)(B) 里的 $$x,y$$ 对调）。**（展开）** 把 (C) 里的 $$x$$ 换成 $$y$$、$$y$$ 换成 $$x$$，得到

$$Q(y+x+z)-Q(y+x-z)-\big[Q(x-y+z)-Q(x-y-z)\big]=2\big[Q(y+z)-Q(y-z)\big].$$

现在逐项对照回 (C) 里已经出现过的量：加法交换律给出 $$Q(y+x+z)=Q(x+y+z)$$、$$Q(y+x-z)=Q(x+y-z)$$；而 $$x-y+z=-\big((y-x)-z\big)$$、$$x-y-z=-\big((y-x)+z\big)$$ 与 $$Q(-w)=Q(w)$$ 给出 $$Q(x-y+z)=Q(y-x-z)$$、$$Q(x-y-z)=Q(y-x+z)$$，所以方括号里的量翻了个符号：

$$Q(x-y+z)-Q(x-y-z)=Q(y-x-z)-Q(y-x+z)=-\big[Q(y-x+z)-Q(y-x-z)\big].$$

代回上式，中括号前的负号与这里的负号相乘抵消成正号，就得到

$$Q(x+y+z)-Q(x+y-z)+\big[Q(y-x+z)-Q(y-x-z)\big]=2\big[Q(y+z)-Q(y-z)\big]. \tag{D}$$

(C) 与 (D) 相加，带方括号的两项正好抵消；两边除以 2 即得 (3.5)。加性证毕。

*齐次性*：由加性，对正整数 $$n$$ 有 $$S(nx,z)=nS(x,z)$$（对 $$n$$ 归纳）；又 $$S(-x,z)+S(x,z)=S(0,z)=0$$，故 $$S(-x,z)=-S(x,z)$$，于是对一切整数 $$n$$ 成立。把 $$x$$ 换成 $$x/n$$ 得 $$S(x/n,z)=\frac1nS(x,z)$$，故对一切有理数 $$q$$ 有 $$S(qx,z)=qS(x,z)$$。最后固定 $$z$$，映射 $$x\mapsto S(x,z)=\frac14\big(Q(x+z)-Q(x-z)\big)$$ 是范数的复合，因而连续（因为 $$\big\lvert Q(a)-Q(b)\big\rvert\le\lVert a-b\rVert(\lVert a\rVert+\lVert b\rVert)$$）；取有理数列 $$q_n\to\alpha$$，则

$$S(\alpha x,z)=\lim_n S(q_nx,z)=\lim_n q_nS(x,z)=\alpha S(x,z).$$

于是 $$S$$ 对第一变元线性，在实情形下由对称性对第二变元也线性。

*复情形*：沿用实情形中的那个泛函 $$S$$，即 $$S(x,y)=\frac14\big(\lVert x+y\rVert^{2}-\lVert x-y\rVert^{2}\big)$$（它正是 (3.4) 的实部）。则 (3.4) 可以读作

$$\langle x,y\rangle=S(x,y)+i\,S(x,iy).$$

上面的加性与齐次性论证**只用到了平行四边形法则**，所以对 $$S$$ 一字不改地成立：$$S$$ 对第一变元实线性、对第二变元实线性（由 $$S(x,y)=S(y,x)$$），且 $$S(x,x)=\lVert x\rVert^{2}$$。复内积的三条公理逐条落地：

- **对第一变元的加性与实齐次性**：$$S(x,y)$$ 有，$$S(x,iy)$$ 也有（把 $$y$$ 换成 $$iy$$ 再用一次同样的论证），两者相加即得。
- **对虚单位 $$i$$ 的齐次性**：由范数的齐次性与 $$\lVert iw\rVert=\lVert w\rVert$$，

$$S(x,iy)=\tfrac14\big(Q(x+iy)-Q(x-iy)\big),\qquad S(ix,y)=\tfrac14\big(Q(ix+y)-Q(ix-y)\big)=\tfrac14\big(Q(x-iy)-Q(x+iy)\big)=-S(x,iy),$$

$$S(ix,iy)=\tfrac14\big(Q(i(x+y))-Q(i(x-y))\big)=S(x,y) .$$

于是 $$\langle ix,y\rangle=S(ix,y)+iS(ix,iy)=-S(x,iy)+iS(x,y)=i\big(S(x,y)+iS(x,iy)\big)=i\langle x,y\rangle$$。结合实齐次性，得到对一切复标量 $$\alpha=a+bi$$ 的齐次性。

- **共轭对称**：$$\overline{\langle y,x\rangle}=S(y,x)-iS(y,ix)=S(x,y)+iS(x,iy)=\langle x,y\rangle$$（第一与第三个等号用了上面两条恒等式）。

- **正定与范数**：见下面的验证。

最后验证这个 $$S$$ 诱导的正是原来的范数。实情形 $$S(x,x)=\frac14\big(\lVert2x\rVert^{2}-0\big)=\lVert x\rVert^{2}$$。复情形直接代 (3.4)（并注意 $$\lVert x-x\rVert^{2}=0$$）：

$$4S(x,x)=\lVert2x\rVert^{2}+i\lVert(1+i)x\rVert^{2}-i\lVert(1-i)x\rVert^{2}=4\lVert x\rVert^{2}+i\cdot2\lVert x\rVert^{2}-i\cdot2\lVert x\rVert^{2}=4\lVert x\rVert^{2},$$

故 $$S(x,x)=\lVert x\rVert^{2}\ge0$$，且等号只在 $$x=0$$。于是 $$S$$ 是内积且诱导范数 $$\lVert\cdot\rVert$$。$$\blacksquare$$

**定理 3.5 的应用（$$\ell^p$$ 与 $$L^p$$ 中只有 $$p=2$$ 是 Hilbert 空间）。** 在 $$\ell^p$$ 中取

$$x=(1,1,0,0,\dots),\qquad y=(1,-1,0,0,\dots).$$

则 $$x+y=(2,0,\dots)$$、$$x-y=(0,2,\dots)$$，于是

$$\lVert x\rVert_p=\lVert y\rVert_p=2^{1/p},\qquad \lVert x+y\rVert_p=\lVert x-y\rVert_p=2 .$$

平行四边形的左边是 $$2^{2}+2^{2}=8$$，右边是 $$2\cdot 2^{2/p}+2\cdot 2^{2/p}=4\cdot 2^{2/p}$$。两边相等要求 $$2^{2/p}=2$$，即 $$p=2$$。所以 **$$p\ne2$$ 时 $$\ell^p$$ 的范数不可能由任何内积诱导**（否则 (3.2) 必须成立，而它不成立）。$$L^p([0,1])$$ 同理：取 $$f=\chi_{[0,1/2]}$$、$$g=\chi_{[1/2,1]}$$，则 $$\lvert f+g\rvert=1$$ 在 $$[0,1]$$ 上处处成立、$$\lvert f-g\rvert=1$$ 也处处成立，而 $$\lVert f\rVert_p=\lVert g\rVert_p=(1/2)^{1/p}$$。代入 (3.2)：左边 $$=1+1=2$$，右边 $$=2(1/2)^{2/p}+2(1/2)^{2/p}=4\cdot2^{-2/p}=2^{2-2/p}$$。两边相等要求 $$2-\frac2p=1$$，仍得 $$p=2$$。**这就是 $$L^2$$ 在 $$L^p$$ 家族里地位特殊的代数理由。**

### 3.2 完备化：把柯西列当成新向量

内积空间未必完备（入口题 (ii) 正是如此）。完备化的思想是**缺什么就把什么添进去**：把每个"该收敛而没处可收敛的极限"直接规定成一个新元素。实现这个想法的唯一干净手段是把柯西列本身当作候选新元素。

**定理 3.6（完备化的存在与唯一性）。** 设 $$(V,\langle\cdot,\cdot\rangle)$$ 是内积空间。则存在 Hilbert 空间 $$(H,\langle\cdot,\cdot\rangle_H)$$ 与线性映射 $$\iota:V\to H$$，使得

(i) $$\iota$$ 保内积（因而是单射），且 $$\iota(V)$$ 在 $$H$$ 中稠密；
(ii) $$H$$ 完备。
并且这样的 $$(H,\iota)$$ 在"固定 $$V$$ 上"的意义下唯一：若 $$(H',\iota')$$ 也满足 (i)(ii)，则存在等距同构 $$\Phi:H\to H'$$ 使 $$\Phi\circ\iota=\iota'$$。

*证明（构造）。* 记 $$\mathcal{C}$$ 为 $$V$$ 中全体柯西列 $$(x_n)$$ 的集合，$$\mathcal{N}$$ 为零列（$$\lVert x_n\rVert\to0$$）的集合。

**第一步：$$\mathcal{C}$$ 是线性空间，$$\mathcal{N}$$ 是其子空间。** 两个柯西列之和、数乘仍是柯西列（三角不等式与齐次性）；零列对加法与数乘封闭，且零列加零列仍是零列。

**第二步：极限 $$\lim_n\langle x_n,y_n\rangle$$ 存在。** 由 Cauchy–Schwarz（定理 3.2）与双线性，

$$\big\lvert\langle x_n,y_n\rangle-\langle x_m,y_m\rangle\big\rvert=\big\lvert\langle x_n-x_m,y_n\rangle+\langle x_m,y_n-y_m\rangle\big\rvert\le\lVert x_n-x_m\rVert\lVert y_n\rVert+\lVert x_m\rVert\lVert y_n-y_m\rVert .$$

$$(x_n)$$ 柯西故有界（取 $$\varepsilon=1$$：$$\lVert x_n\rVert\le\lVert x_{n_0}\rVert+1$$），$$(y_n)$$ 同理。于是右端当 $$n,m$$ 大时任意小，$$\langle x_n,y_n\rangle$$ 是 $$\mathbb{F}$$ 中的柯西列，在完备域 $$\mathbb{F}$$ 中收敛。

**第三步：定义 $$H=\mathcal{C}/\mathcal{N}$$。** 若 $$(x_n),(y_n)\in\mathcal{C}$$、$$(u_n),(v_n)\in\mathcal{N}$$，则

$$\big\lvert\langle x_n+u_n,y_n+v_n\rangle-\langle x_n,y_n\rangle\big\rvert\le\lVert u_n\rVert\lVert y_n+v_n\rVert+\lVert x_n\rVert\lVert v_n\rVert\xrightarrow[\ n\to\infty\ ]{}0,$$

所以 $$\lim\langle x_n,y_n\rangle$$ 只依赖两个陪类，与代表元的选取无关。于是

$$\big\langle[x_n],[y_n]\big\rangle_H:=\lim_{n\to\infty}\langle x_n,y_n\rangle$$

是良定义的。**（展开）** 对第一变元的线性：若 $$[x_n]=[x_n']$$ 代表元相同这件事已在上面处理过，故只需在固定代表元的层面验证——设 $$(u_n)\in\mathcal C$$ 是第三个柯西列，则

$$\big\langle\alpha[x_n]+\beta[u_n],[y_n]\big\rangle_H=\lim_n\langle\alpha x_n+\beta u_n,y_n\rangle=\lim_n\big(\alpha\langle x_n,y_n\rangle+\beta\langle u_n,y_n\rangle\big)=\alpha\lim_n\langle x_n,y_n\rangle+\beta\lim_n\langle u_n,y_n\rangle,$$

这里用了 $$V$$ 上内积对第一变元的线性（逐项成立，再取极限；极限对加法、数乘的可加性是数列极限的基本性质），最后一式正是 $$\alpha\langle[x_n],[y_n]\rangle_H+\beta\langle[u_n],[y_n]\rangle_H$$。共轭对称同理：$$\langle[y_n],[x_n]\rangle_H=\lim_n\langle y_n,x_n\rangle=\lim_n\overline{\langle x_n,y_n\rangle}=\overline{\lim_n\langle x_n,y_n\rangle}=\overline{\langle[x_n],[y_n]\rangle_H}$$（共轭运算与取极限可交换，因为共轭是连续映射）。正定性：$$\big\langle[x_n],[x_n]\big\rangle_H=\lim\lVert x_n\rVert^2\ge0$$，且若此极限为 $$0$$，则 $$\lVert x_n\rVert\to0$$，按定义 $$(x_n)\in\mathcal{N}$$，故 $$[x_n]=0$$。故 $$H$$ 是内积空间。

**第四步：$$H$$ 完备。** 设 $$\big(\xi^{(m)}\big)_{m}$$ 是 $$H$$ 中柯西列。对每个 $$m$$ 取代表元 $$(x^{(m)}_n)_n\in\mathcal{C}$$。由于 $$\lVert\xi^{(m)}\rVert_H=\lim_n\lVert x^{(m)}_n\rVert$$，除有限多个 $$n$$ 外都有 $$\lVert x^{(m)}_n\rVert\le\lVert\xi^{(m)}\rVert_H+1$$；把那有限多个"坏项"改成 $$0$$（改动有限多项既保持柯西性也不改变陪类，故仍取到原来的 $$\xi^{(m)}$$），就使取对角列 $$z_n:=x^{(n)}_n$$。由

$$\lVert z_n-z_m\rVert\le\lVert x^{(n)}_n-x^{(n)}_m\rVert+\lVert x^{(n)}_m-x^{(m)}_m\rVert,$$

第一项由 $$(x^{(n)}_k)_k$$ 是柯西列而小，第二项由 $$\big(\xi^{(m)}\big)$$ 是 $$H$$ 中柯西列（即 $$\lim_k\lVert x^{(n)}_k-x^{(m)}_k\rVert$$ 小）而小，故 $$(z_n)$$ 是 $$V$$ 中柯西列，即 $$(z_n)\in\mathcal{C}$$。记 $$\xi=[z_n]\in H$$。则

$$\big\lVert\xi-\xi^{(m)}\big\rVert_H^{2}=\lim_n\lVert z_n-x^{(m)}_n\rVert^{2}\le\limsup_n\big(\lVert z_n-x^{(n)}_n\rVert+\lVert x^{(n)}_n-x^{(m)}_n\rVert\big)^{2}\xrightarrow[\ m\to\infty\ ]{}0,$$

（第一项当 $$n$$ 大时小，第二项当 $$m,n$$ 大时小）故 $$\xi^{(m)}\to\xi$$。$$H$$ 完备。

**第五步：嵌入与稠密。** 定义 $$\iota(x)=[(x,x,x,\dots)]$$（常列）。则 $$\langle\iota(x),\iota(y)\rangle_H=\lim\langle x,y\rangle=\langle x,y\rangle$$，故 $$\iota$$ 保内积，特别地保范数、是单射。稠密性：对 $$[x_n]\in H$$ 与 $$\varepsilon>0$$，取 $$N$$ 使 $$m,n\ge N$$ 时 $$\lVert x_n-x_m\rVert<\varepsilon$$，则 $$\lVert[x_n]-\iota(x_N)\rVert_H=\lim_n\lVert x_n-x_N\rVert\le\varepsilon$$（取 $$n\ge N$$）。故 $$\iota(V)$$ 稠密。

**第六步：唯一性。** 设 $$(H',\iota')$$ 也满足 (i)(ii)。在 $$\iota(V)$$ 上定义 $$\Phi_0(\iota(x)):=\iota'(x)$$；保内积使 $$\Phi_0$$ 良定义且等距。$$H'$$ 完备、$$\iota(V)$$ 稠密，故 $$\Phi_0$$ 唯一地延拓成等距同构 $$\Phi:H\to H'$$（延拓手续：对 $$\xi\in H$$ 取 $$\iota(x_n)\to\xi$$，则 $$\iota'(x_n)$$ 在 $$H'$$ 中柯西、有极限，规定为 $$\Phi(\xi)$$；极限唯一性与等距性由范数的连续性给出）。$$\blacksquare$$

**注 3.6（完备化不改变任何"极限早已存在"的结论）。** 上面最后一步的延拓论证是通用的：**稠密子空间上的等距映射、只要值域空间完备，就唯一延拓到全空间。** 这条"稠密延拓"手法在泛函分析里反复出现（连续函数延拓、算子延拓、测度延拓）。记住它的形状：稠密 + 完备 = 延拓。

**例 3.6（本书后面要用的三个完备化）。**

1. $$V=\mathbb{R}[x]$$ 带 $$\langle f,g\rangle=\int_0^1fg$$ 的完备化是 $$L^2([0,1])$$（这一点在练习研究题 1 里证明）。
2. $$C([0,1])$$ 带 $$\langle f,g\rangle=\int_0^1fg$$ 的完备化同样是 $$L^2([0,1])$$：连续函数在 $$L^2$$ 中稠密。
3. $$c_{00}$$（只有有限多个非零项的数列）带 $$\ell^2$$ 内积的完备化是 $$\ell^2$$。它给出了入口题 (iii) 在数列情形的对照：在 $$c_{00}$$ 里泛函 $$\phi(x)=\sum_n x_n/n$$ 也是"没有表示向量"的（表示向量应是 $$(1/n)_n\notin c_{00}$$）。

### 3.3 正交、投影定理与 Riesz 表示

现在把第 08 章的"正交"搬到无穷维。全部论证只用到 Cauchy–Schwarz 与**完备性**——这就是完备性买来的东西。

**定义 3.7（正交与正交补）。** 设 $$H$$ 是内积空间。称 $$x\perp y$$ 若 $$\langle x,y\rangle=0$$。对子集 $$S\subset H$$，其**正交补 (orthogonal complement)** 为

$$S^{\perp}=\lbrace x\in H:\ \langle x,s\rangle=0\ \text{对一切 } s\in S\rbrace .$$

**命题 3.8（正交补是闭子空间）。** $$S^\perp$$ 是 $$H$$ 的闭线性子空间，且 $$S^\perp=\big(\overline{\operatorname{span}S}\big)^\perp$$。

*证明。* 对每个 $$s\in S$$，$$\langle\cdot,s\rangle:H\to\mathbb{F}$$ 是连续线性泛函（由 Cauchy–Schwarz，$$x_n\to x$$ 时 $$\lvert\langle x_n,s\rangle-\langle x,s\rangle\rvert\le\lVert x_n-x\rVert\lVert s\rVert\to0$$），故核 $$\lbrace s\rbrace^{\perp}=\ker\langle\cdot,s\rangle$$ 是闭线性子空间。于是

$$S^{\perp}=\bigcap_{s\in S}\lbrace s\rbrace^{\perp}$$

是闭子空间的交，因而是闭线性子空间。

再证第二个陈述。因为 $$\operatorname{span}S\subset\overline{\operatorname{span}S}$$，任何与 $$\overline{\operatorname{span}S}$$ 正交的元素都与 $$\operatorname{span}S$$ 正交，故 $$\big(\overline{\operatorname{span}S}\big)^{\perp}\subset S^{\perp}$$。反过来，设 $$x\in S^\perp$$，即 $$\langle x,s\rangle=0$$ 对一切 $$s\in S$$。任取 $$y\in\operatorname{span}S$$，写 $$y=\sum_{k=1}^{N}\alpha_ks_k$$（$$s_k\in S$$），则由内积对第二变元的共轭线性，

$$\langle x,y\rangle=\sum_{k=1}^{N}\overline{\alpha_k}\langle x,s_k\rangle=0 .$$

于是 $$S^{\perp}\subset(\operatorname{span}S)^{\perp}$$。最后若 $$y\in\overline{\operatorname{span}S}$$，取 $$y_k\in\operatorname{span}S$$ 使 $$y_k\to y$$；由 $$\langle\cdot,\cdot\rangle$$ 的连续性（$$y_k\to y$$ 时 $$\lvert\langle x,y_k\rangle-\langle x,y\rangle\rvert\le\lVert x\rVert\lVert y_k-y\rVert\to0$$），$$\langle x,y\rangle=\lim_k\langle x,y_k\rangle=0$$，故 $$x\perp\overline{\operatorname{span}S}$$，即 $$S^{\perp}\subset\big(\overline{\operatorname{span}S}\big)^{\perp}$$。两向包含合起来给出等号。$$\blacksquare$$

**定理 3.9（闭凸集的极小元存在唯一）。** 设 $$C\subset H$$ 是 Hilbert 空间 $$H$$ 的非空**闭凸**子集（凸：$$u,v\in C\Rightarrow tu+(1-t)v\in C$$ 对一切 $$t\in[0,1]$$）。则存在唯一 $$v\in C$$ 使

$$\lVert v\rVert=\inf_{u\in C}\lVert u\rVert .$$

*证明（存在性）。* 记 $$d=\inf_{u\in C}\lVert u\rVert<\infty$$（$$C$$ 非空）。取极小化序列 $$(u_n)\subset C$$ 使 $$\lVert u_n\rVert\to d$$。由平行四边形法则 (3.2) 与**中点属于 $$C$$**（凸性），

$$\lVert u_m-u_n\rVert^{2}=2\lVert u_m\rVert^{2}+2\lVert u_n\rVert^{2}-4\Big\lVert\tfrac{u_m+u_n}{2}\Big\rVert^{2}\le2\lVert u_m\rVert^{2}+2\lVert u_n\rVert^{2}-4d^{2}\xrightarrow[\ m,n\to\infty\ ]{}0 .$$

（用了 $$\big\lVert\frac{u_m+u_n}{2}\big\rVert\ge d$$，因为中点在 $$C$$ 中。）故 $$(u_n)$$ 是柯西列；$$H$$ 完备故 $$u_n\to v$$；$$C$$ 闭故 $$v\in C$$；范数连续故 $$\lVert v\rVert=\lim\lVert u_n\rVert=d$$。存在性成立。

*唯一性。* 若 $$\lVert v\rVert=\lVert v'\rVert=d$$，对 $$v,v'$$ 用平行四边形法则：

$$\lVert v-v'\rVert^{2}=2d^{2}+2d^{2}-4\Big\lVert\tfrac{v+v'}{2}\Big\rVert^{2}\le4d^{2}-4d^{2}=0,$$

故 $$v=v'$$。$$\blacksquare$$

**注 3.9（两个假设都不能去）。** 不闭：在 $$\mathbb{R}^2$$ 中取开单位圆盘，$$\inf\lVert u\rVert=0$$ 但 $$0\notin C$$。不凸：在 $$\mathbb{R}^2$$ 中取单位圆周（闭集），$$\inf=1$$ 却在圆周一整圈上取到，不唯一。

**定理 3.10（正交分解 / 投影定理, projection theorem）。** 设 $$M$$ 是 Hilbert 空间 $$H$$ 的**闭线性子空间**。则每个 $$x\in H$$ 唯一地写成

$$x=Px+(I-P)x,\qquad Px\in M,\quad (I-P)x\in M^{\perp},$$

即 $$H=M\oplus M^{\perp}$$。并且 $$Px$$ 由两条性质唯一刻画：$$Px\in M$$、$$x-Px\perp M$$。

*证明（存在性）。* 若 $$x\in M$$，取 $$Px=x$$、$$(I-P)x=0$$，成立。设 $$x\notin M$$。集合

$$C:=x-M=\lbrace x-m:\ m\in M\rbrace$$

是闭凸集（$$M$$ 是子空间故凸，$$M$$ 闭故 $$C$$ 闭；平移不改变凸闭性），且 $$0\notin C$$（否则 $$x\in M$$），故 $$d:=\inf_{u\in C}\lVert u\rVert>0$$。由定理 3.9 取唯一极小元 $$v\in C$$，写 $$v=x-m_0$$、$$m_0\in M$$。下面证明 $$v\perp M$$。

对任意 $$w\in M$$、$$w\ne0$$，考察实变量函数

$$g(t)=\big\lVert v-tw\big\rVert^{2}=\lVert v\rVert^{2}-2t\operatorname{Re}\langle v,w\rangle+t^{2}\lVert w\rVert^{2}.$$

因为 $$m_0+tw\in M$$，所以 $$v-tw=x-(m_0+tw)\in C$$，于是 $$g(t)\ge\lVert v\rVert^{2}=g(0)$$ 对一切 $$t\in\mathbb{R}$$；故 $$t=0$$ 是 $$g$$ 的最小点，$$g'(0)=-2\operatorname{Re}\langle v,w\rangle=0$$，即 $$\operatorname{Re}\langle v,w\rangle=0$$。再把 $$w$$ 换成 $$iw$$（$$M$$ 是复线性子空间故 $$iw\in M$$），得 $$\operatorname{Re}\langle v,iw\rangle=\operatorname{Re}\big(\,\overline{i}\langle v,w\rangle\big)=\operatorname{Re}\big(-i\langle v,w\rangle\big)=\operatorname{Im}\langle v,w\rangle=0$$。于是 $$\langle v,w\rangle=0$$ 对一切 $$w\in M$$，即 $$v\perp M$$。取 $$Px:=m_0$$，则 $$x=Px+v$$ 就是所求分解。

*唯一性。* 设 $$x=m+v=m'+v'$$，$$m,m'\in M$$、$$v,v'\perp M$$。则 $$m-m'=v'-v\in M\cap M^{\perp}$$。但若 $$z\in M\cap M^\perp$$ 则 $$\langle z,z\rangle=0$$，故 $$z=0$$。于是 $$m=m'$$、$$v=v'$$。$$\blacksquare$$

**定义 3.11（正交投影, orthogonal projection）。** 定理 3.10 中的映射 $$P=P_M:H\to H$$，$$x\mapsto Px$$，称为到 $$M$$ 上的**正交投影**。它满足

$$P^{2}=P,\qquad \langle Px,y\rangle=\langle x,Py\rangle\ \ \forall x,y,\qquad \lVert Px\rVert\le\lVert x\rVert .$$

*证明。* $$Px\in M$$ 故 $$P(Px)=Px$$（$$M$$ 中元素自己就是到自己的投影）。共轭对称性：写 $$x=Px+v$$、$$y=Py+w$$（$$v,w\perp M$$），则

$$\langle Px,y\rangle=\langle Px,Py\rangle+\langle Px,w\rangle=\langle Px,Py\rangle,\qquad \langle x,Py\rangle=\langle Px,Py\rangle+\langle v,Py\rangle=\langle Px,Py\rangle,$$

两者相等（用了 $$Px,w\in M$$ 的正交性与 $$v\perp M$$）。保范不等式：由勾股关系 $$\lVert x\rVert^{2}=\lVert Px\rVert^{2}+\lVert v\rVert^{2}\ge\lVert Px\rVert^{2}$$（这一等式见下面的注 3.10）。$$\blacksquare$$

**注 3.10（勾股定理在无穷维成立）。** 若 $$x\perp y$$，则 $$\lVert x+y\rVert^{2}=\lVert x\rVert^{2}+\lVert y\rVert^{2}$$——这是 (3.1) 里 $$\operatorname{Re}\langle x,y\rangle=0$$ 的直接结果。更一般地，若 $$x_1,\dots,x_N$$ 两两正交，则 $$\big\lVert\sum_k x_k\big\rVert^{2}=\sum_k\lVert x_k\rVert^{2}$$（展开后交叉项全为 $$0$$）。**这就是投影保范不等式的来源，也是 Bessel 不等式的来源。**

**定理 3.12（Riesz 表示定理, Riesz representation theorem）。** 设 $$H$$ 是 Hilbert 空间，$$f\in H^*$$（连续线性泛函）。则存在**唯一**的 $$y\in H$$ 使

$$f(x)=\langle x,y\rangle\qquad\text{对一切 } x\in H ,$$

且 $$\lVert f\rVert_{H^*}=\lVert y\rVert$$。

*证明（存在性）。* 若 $$f=0$$，取 $$y=0$$。设 $$f\ne0$$，记 $$N=\ker f$$（闭真子空间，因为 $$f$$ 连续、$$f\ne0$$）。

*关键一步：$$N^{\perp}\ne\lbrace0\rbrace$$。* 取 $$z\notin N$$。由定理 3.10 写 $$z=n+z^{\perp}$$，$$n\in N$$、$$z^\perp\in N^\perp$$。若 $$z^\perp=0$$ 则 $$z=n\in N$$，矛盾；故 $$z^{\perp}\ne0$$。

*再把 $$f$$ 限制在 $$N^\perp$$ 上。* 若 $$w\in N^{\perp}$$ 且 $$f(w)=0$$，则 $$w\in N$$，故 $$w\in N\cap N^{\perp}=\lbrace0\rbrace$$，即 $$w=0$$。于是 $$f\vert_{N^{\perp}}$$ 是单射；取 $$w_0\in N^\perp$$、$$w_0\ne0$$，则 $$f(w_0)\ne0$$，令

$$z_0:=\frac{w_0}{f(w_0)}\in N^{\perp},\qquad f(z_0)=1 .$$

*验证 $$y=z_0/\lVert z_0\rVert^{2}$$ 即为所求。* 对任意 $$x\in H$$，由 $$f$$ 线性，

$$f\big(x-f(x)z_0\big)=f(x)-f(x)f(z_0)=0,$$

故 $$x-f(x)z_0\in N\perp z_0$$，即 $$\big\langle x-f(x)z_0,\ z_0\big\rangle=0$$。展开并用 $$\langle z_0,z_0\rangle=\lVert z_0\rVert^{2}$$：

$$\langle x,z_0\rangle=f(x)\lVert z_0\rVert^{2}\ \Longrightarrow\ f(x)=\Big\langle x,\ \frac{z_0}{\lVert z_0\rVert^{2}}\Big\rangle .$$

*唯一性。* 若 $$\langle x,y\rangle=\langle x,y'\rangle$$ 对一切 $$x$$，则 $$\langle x,y-y'\rangle=0$$ 对一切 $$x$$；取 $$x=y-y'$$ 得 $$\lVert y-y'\rVert^{2}=0$$，故 $$y=y'$$。

*范数。* 一方面由 Cauchy–Schwarz，$$\lvert f(x)\rvert=\lvert\langle x,y\rangle\rvert\le\lVert x\rVert\lVert y\rVert$$，故 $$\lVert f\rVert\le\lVert y\rVert$$。另一方面取 $$x=y$$（若 $$y\ne0$$）：

$$f(y)=\langle y,y\rangle=\lVert y\rVert^{2}\ \Longrightarrow\ \lVert f\rVert\ge\frac{\lvert f(y)\rvert}{\lVert y\rVert}=\lVert y\rVert .$$

（$$y=0$$ 时 $$f=0$$，两边都是 $$0$$。）两向不等号合起来给出 $$\lVert f\rVert=\lVert y\rVert$$。$$\blacksquare$$

**定理 3.13（Riesz 等距同构：$$H\cong H^*$$）。** 映射

$$\Phi:H\to H^*,\qquad \Phi(y)=\langle\cdot,y\rangle$$

是**共轭线性**（$$\Phi(\alpha y+\beta z)=\overline{\alpha}\Phi(y)+\overline{\beta}\Phi(z)$$）的双射，且是等距：$$\lVert\Phi(y)\rVert_{H^*}=\lVert y\rVert$$。特别地，$$H$$ 是自反的（$$H\cong H^*\cong H^{**}$$），且 $$H$$ 上的弱拓扑与弱\*拓扑重合。

*证明。* 定理 3.12 说 $$\Phi$$ 是满射且是单射（唯一性），等距性就是 $$\lVert f\rVert=\lVert y\rVert$$。共轭线性来自内积对第二变元的共轭线性：

$$\Phi(\alpha y+\beta z)(x)=\langle x,\alpha y+\beta z\rangle=\overline{\alpha}\langle x,y\rangle+\overline{\beta}\langle x,z\rangle .$$

**自反性（展开）。** 先说明 $$H^*$$ 本身也是 Hilbert 空间：$$\Phi:H\to H^*$$ 是等距（保范），而等距同构把柯西列送到柯西列、把收敛送到收敛，所以完备性沿着 $$\Phi$$ 从 $$H$$ 搬到 $$H^*$$；又因为 $$\Phi$$ 保范，$$H^*$$ 的范数自动继承 $$H$$ 的平行四边形法则（定理 3.5 的必要性方向），故由定理 3.5(ii) 可用极化恒等式在 $$H^*$$ 上还原出一个内积。**具体取法是**：

$$\langle f,g\rangle_{H^*}:=\big\langle\Phi^{-1}(g),\ \Phi^{-1}(f)\big\rangle_H\qquad(f,g\in H^*)$$

（这里把变元顺序对调，是为了抵消 $$\Phi^{-1}$$ 的共轭线性——$$\Phi^{-1}$$ 与 $$\Phi$$ 一样是共轭线性双射，把它放进 $$H$$ 的内积的第二变元、同时把参与对调的那个变元放进第一变元，两次共轭恰好抵消，使 $$\langle\cdot,\cdot\rangle_{H^*}$$ 对第一变元线性；这与定理 3.5(ii) 由极化恒等式还原出的内积是同一个，逐条核对内积公理是常规展开，此处从略）。于是可以对 $$H^*$$ 重新套用定理 3.12/3.13：存在共轭线性等距同构 $$\Psi:H^*\to H^{**}$$，$$\Psi(g)=\langle\cdot,g\rangle_{H^*}$$。要检查的是复合 $$\Psi\circ\Phi:H\to H^{**}$$ 是否就是"自然嵌入" $$J:H\to H^{**}$$，$$(Jx)(f):=f(x)$$（$$f\in H^*$$）。取 $$x\in H$$、$$f\in H^*$$ 任意，直接算：

$$\big(\Psi(\Phi(x))\big)(f)=\big\langle f,\Phi(x)\big\rangle_{H^*}=\big\langle\Phi^{-1}(\Phi(x)),\ \Phi^{-1}(f)\big\rangle_H=\big\langle x,\ \Phi^{-1}(f)\big\rangle_H$$

（第一个等号是 $$\Psi$$ 的定义，第二个等号是 $$\langle\cdot,\cdot\rangle_{H^*}$$ 的定义，第三个等号用了 $$\Phi^{-1}(\Phi(x))=x$$）。而按 $$\Phi$$ 的定义，$$f=\Phi\big(\Phi^{-1}(f)\big)=\big\langle\cdot,\ \Phi^{-1}(f)\big\rangle$$，把它作用在 $$x$$ 上正是 $$f(x)=\langle x,\Phi^{-1}(f)\rangle_H$$——与上式右端逐字相同。于是 $$\big(\Psi(\Phi(x))\big)(f)=f(x)=(Jx)(f)$$ 对一切 $$f$$ 成立，即 $$\Psi\circ\Phi=J$$：$$J$$ 本身就是一个（等距）同构，这正是"$$H$$ 自反"的定义。弱拓扑与弱\*拓扑重合，是因为在自反空间上两者都是"使 $$H^*$$ 的元素连续"的最粗拓扑。$$\blacksquare$$

**注 3.13（Riesz 表示把"泛函"换成了"向量"）。** 定理 3.12 可以一句话记住：**Hilbert 空间上的连续线性泛函就是"与某个固定向量做内积"。** 它的第一个用处是让**伴随算子** $$A^*$$ 能被定义成 $$A^*:H\to H$$ 而不是 $$H^*\to H^*$$：固定 $$y$$ 时 $$x\mapsto\langle Ax,y\rangle$$ 是连续线性泛函，由定理 3.12 它等于 $$\langle x,A^*y\rangle$$，这就定出了 $$A^*y\in H$$（第 32 章会用到；更系统的展开见知识库 `泛函分析/ch06.md` 与 `mit-18-102/ch10.md`）。第二个用处是让 **Dirac 符号**合法化：$$\langle\phi\mid\psi\rangle$$ 里的 $$\langle\phi\mid$$ 被理解为"$$H^*$$ 里的泛函"，而由 Riesz，它同时也就是 $$H$$ 里的一个向量——左矢与右矢可以互相搬运（见 MP39 与本章练习竞赛题 1）。

**定理 3.14（与第 08 章的接口：$$g^\flat$$ 到底什么时候是同构？）。** 设 $$(V,\langle\cdot,\cdot\rangle)$$ 是内积空间，定义

$$g^{\flat}:V\to V^{*},\qquad g^{\flat}(v):=\langle v,\cdot\rangle\quad\big(\text{即 } g^{\flat}(v)(w)=\langle v,w\rangle\big).$$

则：

(i) $$g^\flat$$ 恒为线性映射；

(ii) $$\ker g^{\flat}=\lbrace0\rbrace$$，即 $$g^\flat$$ 恒为单射；

(iii) 若 $$V$$ **完备**（即 $$V$$ 是 Hilbert 空间），则 $$g^{\flat}$$ 还是满射，从而是等距同构（这就是定理 3.12、3.13 的内容，此时 $$g^{\flat}$$ 与 $$\Phi$$ 只差一次共轭约定）；

(iv) 若 $$V$$ **不完备**，则 $$g^\flat$$ 一般**不是**满射：存在内积空间 $$V$$ 与 $$f\in V^{*}$$，使 $$f$$ 不等于任何 $$g^{\flat}(v)$$。

*证明。* **(i)** 由内积对第一变元的线性：$$g^\flat(\alpha v+\beta w)(x)=\langle\alpha v+\beta w,x\rangle=\alpha\langle v,x\rangle+\beta\langle w,x\rangle$$。

**(ii)** 设 $$g^\flat(v)=0$$，即 $$\langle v,w\rangle=0$$ 对一切 $$w$$。取 $$w=v$$ 得 $$\lVert v\rVert^{2}=0$$，由正定性 $$v=0$$。所以核是 $$\lbrace0\rbrace$$——注意这一步**只用正定性**，与完备性无关。但无穷维里"单射 $$\Rightarrow$$ 满射"不成立（秩—零化度定理要有限维，见第 06 章的 问题 3）。

**(iii)** 即定理 3.12（每个 $$f\in V^*$$ 都由某个向量表示）。

**(iv)** 取入口题的 $$V=\mathbb{R}[x]$$、$$\langle f,g\rangle=\int_0^1 fg$$，以及

$$\ell(f)=\int_0^1 f(x)e^{x}\,dx .$$

先证 $$\ell\in V^*$$：由 Cauchy–Schwarz（定理 3.2），

$$\lvert\ell(f)\rvert=\lvert\langle f,e^{x}\rangle\rvert\le\lVert f\rVert\cdot\lVert e^{x}\rVert,\qquad \lVert e^{x}\rVert^{2}=\int_0^1e^{2x}dx=\frac{e^{2}-1}{2}<\infty ,$$

故 $$\ell$$ 连续（且 $$\lVert\ell\rVert\le\sqrt{(e^{2}-1)/2}$$）。再证它没有表示向量。设存在 $$g\in\mathbb{R}[x]$$ 使 $$\ell(f)=\langle f,g\rangle$$ 对一切 $$f\in\mathbb{R}[x]$$，即

$$\int_0^1 f(x)\big(e^{x}-g(x)\big)\,dx=0\qquad\text{对一切 } f\in\mathbb{R}[x] . \tag{3.6}$$

记 $$h(x)=e^{x}-g(x)$$，它是 $$[0,1]$$ 上的连续函数。由 **Weierstrass 逼近定理**（$$[0,1]$$ 上的连续函数可被多项式在 $$\lVert\cdot\rVert_\infty$$ 下任意逼近；其证明见数学分析教材的逼近论部分，本书不重复），存在多项式列 $$f_n$$ 使 $$\lVert f_n-h\rVert_\infty\to0$$。把 $$f=f_n$$ 代入 (3.6)：

$$0=\int_0^1 f_nh=\int_0^1 h^{2}+\int_0^1 (f_n-h)h ,$$

于是

$$\int_0^1h^{2}=-\int_0^1(f_n-h)h\le\lVert f_n-h\rVert_\infty\int_0^1\lvert h\rvert\xrightarrow[\ n\to\infty\ ]{}0 .$$

故 $$\int_0^1h^{2}=0$$；被积函数 $$h^2$$ 连续且非负，故 $$h\equiv0$$，即 $$g\equiv e^{x}$$ 在 $$[0,1]$$ 上。但 $$e^x$$ 不是多项式（它的 $$n$$ 阶导数 $$e^x$$ 在 $$0$$ 处值为 $$1$$，而任何 $$n$$ 次多项式的 $$n+1$$ 阶导数恒为 $$0$$；若 $$e^x$$ 是多项式则其某阶导数为零，矛盾）。这与 $$g\in\mathbb{R}[x]$$ 冲突。故这样的 $$g$$ 不存在，$$g^{\flat}$$ 不是满射。$$\blacksquare$$

**定理 3.14 的另一面：Banach 空间上"$$V\cong V^{*}$$"也不是免费的。** 定理 3.14 (iv) 的病是"不完备"，那么补上完备性（改用 Banach 空间）是否就万事大吉？不是。反例是

$$L^{1}([0,1])\qquad\text{与}\qquad L^{\infty}([0,1]) .$$

由 $$(L^{p})^{*}\cong L^{q}$$（$$\frac1p+\frac1q=1$$，见知识库 `泛函分析/ch02.md`），$$(L^{1})^{*}\cong L^{\infty}$$。但 $$L^{1}([0,1])$$ 是**可分**的（多项式在 $$L^1$$ 中稠密），而 $$L^{\infty}([0,1])$$ 是**不可分**的：对每个 $$t\in[0,1]$$，函数 $$\chi_{[0,t]}$$ 的等价类两两距离为 $$1$$（$$t\ne s$$ 时$$\lVert\chi_{[0,t]}-\chi_{[0,s]}\rVert_\infty=1$$），给出一个不可数的 $$1$$-分离集，故不存在可数稠密子集。**可分性在等距同构下保持**，所以不存在从 $$L^{1}$$ 到 $$(L^{1})^{*}$$ 的等距同构——$$\lVert\cdot\rVert_{L^1}$$ 无法由任何内积诱导（定理 3.5 已经说明 $$p\ne2$$ 时范数不满足平行四边形法则），连"同构"这一步都过不去。

**结论（本章最重要的一句话）。**

> 第 08 章 定理 3.6 说"内积给出 $$V\to V^{*}$$ 的自然同构"。在**有限维**，这句话对任何内积空间成立——但那里的关键是"$$\dim V=\dim V^{*}$$，单射即满射"（秩—零化度定理），内积其实只提供了单射那半边。到了**无穷维**，维数不再能保证满射（$$\mathbb{R}[x]$$：$$\dim V=\aleph_0$$，而由第 06 章的 问题 3，$$\dim V^{*}=\mathfrak{c}$$），此时唯一的补救是**同时要求内积与完备性**——即 $$V$$ 是 Hilbert 空间。**所以在无穷维里，$$V\cong V^{*}$$ 靠的不是维数巧合，而是内积加完备性；这正是第 06 章研究题 1 与问题 3 问的那件事的答案，也说明 Riesz 表示定理不是"显然的内积性质"，而是一条真正用掉了完备性的定理。**

### 3.4 正交规范基与 Fourier 展开

**定义 3.15（正交规范集、极大、正交规范基）。** 设 $$H$$ 是内积空间。族 $$\lbrace e_\alpha\rbrace_{\alpha\in A}$$ 称为**正交规范集 (orthonormal set)**，若

$$\langle e_\alpha,e_\beta\rangle=\delta_{\alpha\beta}=\begin{cases}1,&\alpha=\beta,\\0,&\alpha\ne\beta.\end{cases}$$

称它**极大 (maximal)**，若唯一与所有 $$e_\alpha$$ 正交的向量是 $$0$$。若 $$H$$ 是 Hilbert 空间且 $$\lbrace e_\alpha\rbrace$$ 是极大正交规范集，则称它为 $$H$$ 的**正交规范基 (orthonormal basis, ONB)**。

（**（展开）为什么"极大"等价于"张成稠密"。** 记 $$M=\overline{\operatorname{span}\lbrace e_\alpha\rbrace}$$（张成的闭包，这是 $$H$$ 的闭子空间）。

**"不稠密 $$\Rightarrow$$ 不极大"：** 若 $$M\ne H$$，取 $$x_0\in H\setminus M$$。由定理 3.10（$$M$$ 闭），$$x_0=Px_0+v$$，$$Px_0\in M$$、$$v\perp M$$。因为 $$x_0\notin M$$，必有 $$v\ne0$$（否则 $$x_0=Px_0\in M$$）。又 $$v\perp M\supset\lbrace e_\alpha\rbrace$$，故 $$v$$ 是一个非零的、与全体 $$e_\alpha$$ 正交的向量，与"极大"（唯一与所有 $$e_\alpha$$ 正交的向量是 $$0$$）矛盾。

**"稠密 $$\Rightarrow$$ 极大"：** 反之设 $$M=H$$，并设 $$x\perp$$ 全体 $$e_\alpha$$。由命题 3.8（正交补对张成取闭包不变），$$x\in\lbrace e_\alpha\rbrace^\perp=M^\perp=H^\perp=\lbrace0\rbrace$$，即 $$x=0$$，故极大性成立——只有零向量能同时与所有 $$e_\alpha$$ 正交。两个方向合起来，"极大"与"张成稠密"等价。）

**例 3.15。** $$\mathbb{F}^n$$ 的标准基；$$\ell^2$$ 中的 $$\lbrace e_n\rbrace$$（$$e_n$$ 是第 $$n$$ 位为 $$1$$、其余为 $$0$$ 的数列）；$$L^2([-\pi,\pi])$$ 中的 $$\lbrace e^{inx}/\sqrt{2\pi}\rbrace_{n\in\mathbb{Z}}$$（由 $$\frac1{2\pi}\int_{-\pi}^{\pi}e^{i(n-m)x}dx=\delta_{nm}$$ 验证）。最后这个就是我们熟悉的 Fourier 系。

**为什么先证 Bessel、再证 Parseval。** 我们最终想说"$$x$$ 能展开成正交基的无穷级数"，但"无穷级数收敛"这件事本身要先有保证——下面的 Bessel 不等式正是这份保证的雏形：它说部分和的长度平方**不会超过** $$\lVert x\rVert^2$$，对任意正交规范列都成立（不需要"基"、不需要完备性）；有了这个一致的上界，级数才有资格谈论收敛。

**定理 3.16（Bessel 不等式）。** 设 $$\lbrace e_n\rbrace_{n\ge1}$$ 是正交规范列，则对一切 $$x\in H$$

$$\sum_{n=1}^{\infty}\big\lvert\langle x,e_n\rangle\big\rvert^{2}\le\lVert x\rVert^{2}.$$

*证明。* 记 $$s_N=\sum_{n=1}^{N}\langle x,e_n\rangle e_n$$。先算 $$\lVert x-s_N\rVert^{2}$$。由注 3.10 的勾股定理（$$s_N$$ 与 $$x-s_N$$ 正交，见下），

$$\lVert x\rVert^{2}=\lVert x-s_N\rVert^{2}+\lVert s_N\rVert^{2}=\lVert x-s_N\rVert^{2}+\sum_{n=1}^{N}\big\lvert\langle x,e_n\rangle\big\rvert^{2}, \tag{3.7}$$

其中第二步用了 $$e_n$$ 两两正交与 $$\lVert e_n\rVert=1$$。正交性 $$\langle x-s_N,e_m\rangle=\langle x,e_m\rangle-\sum_{n=1}^{N}\overline{\langle x,e_n\rangle}\langle e_n,e_m\rangle=\langle x,e_m\rangle-\langle x,e_m\rangle=0$$ 对 $$1\le m\le N$$ 成立，故 $$\langle x-s_N,s_N\rangle=\sum_m\langle x,e_m\rangle\langle x-s_N,e_m\rangle=0$$。于是由 (3.7)，$$\lVert x-s_N\rVert^{2}\ge0$$ 给出部分和 $$\sum_{n=1}^{N}\lvert\langle x,e_n\rangle\rvert^{2}\le\lVert x\rVert^{2}$$。左侧随 $$N$$ 单调不减、有上界，故收敛且极限 $$\le\lVert x\rVert^{2}$$。$$\blacksquare$$

**从"有界"到"收敛"还差一步。** Bessel 只保证了部分和 $$s_N=\sum_{n\le N}\langle x,e_n\rangle e_n$$ 的长度不失控，并没有说 $$s_N$$ 本身收敛到某个向量——这一步恰好要用上完备性（否则 $$s_N$$ 可能又是一列"该收敛却无处可去"的柯西列，正是第29章 3.3 节遇到的麻烦）；而"极大"这条条件保证了即便 $$s_N$$ 收敛，极限也一定是 $$x$$ 本身，不多不少。

**定理 3.17（Fourier 展开与 Parseval 恒等式）。** 设 $$\lbrace e_n\rbrace_{n\ge1}$$ 是 Hilbert 空间 $$H$$ 的正交规范**基**。则对一切 $$x\in H$$

$$x=\sum_{n=1}^{\infty}\langle x,e_n\rangle e_n\qquad\text{（在 }\lVert\cdot\rVert\text{ 意义下收敛）}, \tag{3.8}$$

$$\lVert x\rVert^{2}=\sum_{n=1}^{\infty}\big\lvert\langle x,e_n\rangle\big\rvert^{2}\qquad\text{（Parseval 恒等式）}. \tag{3.9}$$

*证明。* 由 (3.7)，$$\big\lVert s_M-s_N\big\rVert^{2}=\sum_{n=N+1}^{M}\lvert\langle x,e_n\rangle\rvert^{2}$$（$$M>N$$）。由 Bessel 不等式，右侧随 $$N,M$$ 增大而任意小（级数收敛的必要条件），故 $$(s_N)$$ 是柯西列。$$H$$ 完备，故 $$s_N\to s$$ 对某个 $$s\in H$$。

再证 $$s=x$$。对每个固定的 $$m$$，由内积的连续性（命题 3.8 的证明里用过的那条：$$u_n\to u,v_n\to v\Rightarrow\langle u_n,v_n\rangle\to\langle u,v\rangle$$），

$$\langle s,e_m\rangle=\lim_{N}\langle s_N,e_m\rangle=\lim_{N}\Big\langle\sum_{n=1}^{N}\langle x,e_n\rangle e_n,\ e_m\Big\rangle=\langle x,e_m\rangle ;$$

（当 $$N\ge m$$ 时右端那个内积恒等于 $$\langle x,e_m\rangle$$。）于是 $$\langle x-s,e_m\rangle=0$$ 对一切 $$m$$。由基的极大性（定义 3.15 的等价刻画），$$x-s=0$$。这就证明了 (3.8)。

(3.9)：在 (3.7) 中令 $$N\to\infty$$。左端是常数，右端第一项 $$\lVert x-s_N\rVert^{2}\to\lVert x-s\rVert^{2}=0$$，第二项收敛到 $$\sum_n\lvert\langle x,e_n\rangle\rvert^{2}$$，故两者相等。$$\blacksquare$$

**注 3.17（Bessel 与 Parseval 的差别就是"极大性"）。** Bessel 只说"部分信息不超过全部信息"，它对任意正交规范列成立；Parseval 把不等号升级为等号，用掉了极大性。**这就是正交规范"列"与正交规范"基"的分水岭。**

**定理 3.18（可分 Hilbert 空间都等距同构于 $$\ell^2$$）。** 设 $$H$$ 是无限维可分的 Hilbert 空间，$$\lbrace e_n\rbrace_{n\ge1}$$ 是它的正交规范基（可分性保证基可取为可数族：对可数稠密集做 Gram–Schmidt）。定义

$$T:H\to\ell^{2},\qquad Tx=\big(\langle x,e_1\rangle,\langle x,e_2\rangle,\dots\big).$$

则 $$T$$ 是线性等距同构，保持内积：$$\langle Tx,Ty\rangle_{\ell^{2}}=\langle x,y\rangle$$。

*证明。* **良定义与等距**：由 Parseval (3.9)，$$\lVert Tx\rVert_{\ell^2}^{2}=\sum_n\lvert\langle x,e_n\rangle\rvert^{2}=\lVert x\rVert^{2}<\infty$$，故 $$Tx\in\ell^2$$，且 $$T$$ 保范。保内积由极化恒等式 (3.4) 与保范性得到（复情形），实情形由 (3.3)。

**线性**：内积对第一变元线性，逐分量线性。

**满射**：任取 $$c=(c_n)\in\ell^{2}$$。由 $$\sum_{n=N+1}^{M}\lvert c_n\rvert^{2}\to0$$ 知部分和 $$t_N=\sum_{n=1}^{N}c_ne_n$$ 是柯西列，故 $$t_N\to x$$ 对某个 $$x\in H$$。由内积的连续性，$$\langle x,e_m\rangle=\lim_N\langle t_N,e_m\rangle=c_m$$（当 $$N\ge m$$ 时那个内积就是 $$c_m$$），故 $$Tx=c$$。

**单射**：保范映射零核。于是 $$T$$ 是等距同构。$$\blacksquare$$

**注 3.18（为什么这条定理重要）。** 它说：**所有无限维可分 Hilbert 空间在几何上是同一个空间。** 研究 $$\ell^2$$ 就等于研究 $$L^2$$、研究 Sobolev 空间 $$H^1$$、研究一切可分量子力学态空间。这是泛函分析里最省力的一条事实——第 32 章会直接受益。

**定理 3.19（$$L^2$$ 是 Hilbert 空间；三角系是它的正交规范基）。** 设 $$\langle f,g\rangle=\int_{-\pi}^{\pi}f(x)\overline{g(x)}\,dx$$，$$\lVert f\rVert_2=\sqrt{\langle f,f\rangle}$$。

(i) $$L^{2}([-\pi,\pi])$$ 在 $$\lVert\cdot\rVert_2$$ 下完备（Riesz–Fischer 定理），因而是 Hilbert 空间。

(ii) 记 $$\hat f(n)=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(t)e^{-int}dt$$、$$S_Nf(x)=\sum_{\lvert n\rvert\le N}\hat f(n)e^{inx}$$。则对一切 $$f\in L^{2}([-\pi,\pi])$$

$$\big\lVert f-S_Nf\big\rVert_{2}\xrightarrow[\ N\to\infty\ ]{}0 ,$$

即 $$\lbrace e^{inx}/\sqrt{2\pi}\rbrace_{n\in\mathbb{Z}}$$ 是正交规范基，且对有列展开 $$\lVert f\rVert_2^{2}=2\pi\sum_{n\in\mathbb{Z}}\lvert\hat f(n)\rvert^{2}$$。

*证明思路与关键步骤。* **(i)** 是测度论的标准结论（Riesz–Fischer：$$L^p$$ 完备），本书按知识库 `泛函分析/ch01.md` 的立场直接引用。

**(ii)** 只需证极大性：若 $$\hat f(n)=0$$ 对一切 $$n$$，则 $$f=0$$（定义 3.15 的等价刻画）。直接证明 $$S_Nf\to f$$ 需要估计 Dirichlet 核 $$D_N(x)=\frac{\sin((N+\frac12)x)}{2\pi\sin(x/2)}$$，而 $$\lVert D_N\rVert_{L^1}\sim\log N$$ 无界——这正是逐点收敛无法从范数收敛推出的原因（注 3.19）。可行之路是绕道 **Cesàro 平均**。记

$$\sigma_Nf=\frac{1}{N+1}\sum_{k=0}^{N}S_kf ,$$

则由几何级数求和，$$\sigma_Nf(x)=\int_{-\pi}^{\pi}K_N(x-t)f(t)dt$$，其中 **Fejér 核 (Fejér kernel)**

$$K_N(x)=\frac{1}{2\pi(N+1)}\left(\frac{\sin\frac{(N+1)x}{2}}{\sin\frac x2}\right)^{2}\quad(x\ne0),\qquad K_N(0)=\frac{N+1}{2\pi},$$

满足四条性质：(a) $$K_N\ge0$$ 且偶；(b) $$2\pi$$-周期；(c) $$\int_{-\pi}^{\pi}K_N=1$$；(d) 对 $$\delta\in(0,\pi)$$，在 $$\delta\le\lvert x\rvert\le\pi$$ 上 $$\lvert K_N(x)\rvert\le\frac{1}{2\pi(N+1)\sin^{2}(\delta/2)}$$。由 (a)(c) 与 $$f$$ 的一致连续性，把积分拆成 $$\lvert t\rvert\le\delta$$ 与 $$\delta\le\lvert t\rvert\le\pi$$ 两段并用 (d)，得：**对 $$2\pi$$-周期连续函数 $$f$$，$$\sigma_Nf\to f$$ 一致**（Fejér 定理）。

再对一般 $$f\in L^2$$ 做 $$\varepsilon/3$$ 论证：取 $$2\pi$$-周期连续 $$g$$ 使 $$\lVert f-g\rVert_2<\varepsilon/3$$（连续函数在 $$L^2$$ 中稠密），并注意由 (a)(c) 与 Cauchy–Schwarz 有 $$\lVert\sigma_Nh\rVert_2\le\lVert h\rVert_2$$（$$h\in L^2$$），于是

$$\lVert\sigma_Nf-f\rVert_2\le\lVert\sigma_N(f-g)\rVert_2+\lVert\sigma_Ng-g\rVert_2+\lVert g-f\rVert_2<\frac\varepsilon3+\lVert\sigma_Ng-g\rVert_2+\frac\varepsilon3 ,$$

取 $$N$$ 大使中间项 $$<\varepsilon/3$$（Fejér 定理 + 一致收敛给 $$L^2$$ 收敛）。故 $$\sigma_Nf\to f$$ 于 $$L^2$$。

最后：若 $$\hat f(n)=0$$ 对一切 $$n$$，则 $$S_kf=0$$ 对一切 $$k$$，故 $$\sigma_Nf=0$$，于是 $$\lVert f\rVert_2=\lim\lVert\sigma_Nf-f\rVert_2=0$$，$$f=0$$。极大性成立，$$\lbrace e^{inx}/\sqrt{2\pi}\rbrace$$ 是正交规范基。$$\blacksquare$$

**注 3.19（范数收敛与逐点发散如何共存——入口题 (iv) 的解答）。** 定理 3.19 (ii) 的收敛是**范数收敛**：$$\lVert f-S_Nf\rVert_2\to0$$，意思是"平均平方误差趋于零"。它允许误差在一个越来越小、越来越分散的集合上变得很大。而**逐点收敛**要求每个固定的 $$x$$ 上 $$S_Nf(x)\to f(x)$$，这是一个更强的、逐点的要求。两者的桥梁是 Dirichlet 核的 $$L^1$$ 范数：由 $$S_Nf(x)=f*D_N(x)$$ 与 $$K_N$$ 的四条性质对比可见，$$D_N$$ **不非负**，因而没有 (a)(c) 联合给出的"平均化"效果，$$\lVert D_N\rVert_{L^1}\sim\log N$$ 无界——这正好对应着"逐点收敛不稳定"：存在连续函数（du Bois-Reymond 反例）其 Fourier 级数在某点发散。用今日的语言：$$L^2$$ 收敛是**几何的**（正交基展开），逐点收敛是**点态的**；前者由 Hilbert 空间结构免费给出，后者要请出更深的结果（Carleson 定理断言 $$L^2$$ 函数的 Fourier 级数几乎处处收敛）。**这就是"能收敛到函数"与"逐点不收敛"共存的机制。**

**注 3.20（Hermite 内积为什么必须带共轭）。** 复内积 $$\langle\phi,\psi\rangle=\int\overline{\phi}\psi$$ 的共轭不是装饰。把复数写成极形式 $$\phi=\lvert\phi\rvert e^{i\alpha}$$、$$\psi=\lvert\psi\rvert e^{i\beta}$$，则 $$\overline{\phi}\psi=\lvert\phi\rvert\lvert\psi\rvert e^{i(\beta-\alpha)}$$：**两个复数直接相乘是相位相加，一个乘另一个的共轭是相位相减。** 相减得到的是**相位差**——也就是"夹角"，它不依赖 $$\alpha,\beta$$ 各自的绝对值。物理上，这意味着内积（以及一切由它导出的物理量）**与波函数的绝对相位无关**，只依赖相对相位；这正是量子力学里"整体相位不可观测"这条实验事实的代数形式。若把内积取成不带共轭的 $$\int\phi\psi$$，相位差就会变成相位和，几何立刻失真。

## 四、几何与物理直觉 (Intuition)

**几何侧：无穷维里的"直角"仍然是全部几何的来源。** 本章每一条定理都能画成一张有限维的图：

| 定理 | 有限维的画面 | 无穷维新增的困难 | 补救用的假设 |
|---|---|---|---|
| 定理 3.2 Cauchy–Schwarz | 夹角 $$\cos\theta=\frac{\langle x,y\rangle}{\lVert x\rVert\lVert y\rVert}$$ | 无（不等式与维数无关） | 无 |
| 定理 3.9 极小元 | "垂足"是点到集合的最近点 | 极小化序列未必收敛 | **完备 + 闭 + 凸** |
| 定理 3.10 正交分解 | $$x$$ 拆成"水平 + 竖直"两支 | 只有 $$\lVert x-y\rVert\to d$$ 不够，要走柯西 | **闭子空间 + 完备** |
| 定理 3.12 Riesz | 泛函 = 与某向量配对 | 泛函是"抽象的"，不知是哪个向量 | **完备（满射那半边）** |
| 定理 3.17 Parseval | 勾股定理：$$\lVert x\rVert^2=\sum\lvert x_i\rvert^2$$ | 无穷多项，需要级数收敛的机制 | **Bessel + 极大性 + 完备** |

一句话：**无穷维把这些定理的"结论"原样保留，把"证明"全部改道经过完备性。** 这也解释了为什么定理 3.14 的反例发生在 $$V$$ 不完备或 $$V$$ 不是 Hilbert 空间时——病不在内积，病在"极限无处可去"。

**正交基就是坐标系。** 定理 3.17 说：只要 $$H$$ 有正交规范基，每个向量都唯一地写成 $$\sum_n\langle x,e_n\rangle e_n$$。这与有限维的"坐标分解 $$x=\sum_ix_ie_i$$"逐字相同，无非多加了一个收敛要求。$$\langle x,e_n\rangle$$ 是**坐标**，$$\lVert x\rVert^2=\sum_n\lvert\langle x,e_n\rangle\rvert^2$$ 是**勾股定理的无穷版本**，而 $$\lbrace\langle x,e_n\rangle\rbrace_n\in\ell^2$$ 是说"坐标序列本身就是一个 $$\ell^2$$ 向量"。定理 3.18 把这个观察升级成结论：**无限维可分 Hilbert 空间全是同一个空间，只是坐标用得不同。**

**物理侧：为什么量子力学必须住在 Hilbert 空间里。** 把 $$L^2(\Omega)$$ 里的 $$\psi$$ 看作"状态"，内积结构给出三件事：

1. **归一化与概率。** $$\langle\psi,\psi\rangle=\int\lvert\psi\rvert^2=1$$ 是概率归一化；$$\lvert\psi(x)\rvert^2$$ 是概率密度。注意被积项 $$\overline{\psi}\psi=\lvert\psi\rvert^2$$ 处处取实——这正是注 3.20 的共轭机制：**只有取共轭，"与自己做内积"才给出实数**。
2. **相位无关性。** 注 3.20 说 $$\overline{\phi}\psi$$ 只依赖相位差。物理语言：$$\psi$$ 与 $$e^{i\alpha}\psi$$ 描述同一个态（整体相位不可观测）。数学语言：态是 $$L^2$$ 中**单位球面模掉 $$U(1)$$ 作用**的元素——这条线索在第 48 章会以射影表示的面貌回来。
3. **叠加原理就是线性。** 态的线性组合还是态（$$\lVert\alpha\phi+\beta\psi\rVert$$ 由内积算出），正交的态互不"干涉"（$$\lVert\phi+\psi\rVert^2=\lVert\phi\rVert^2+\lVert\psi\rVert^2$$）。

**测量就是正交投影。** 定理 3.10 的分解 $$x=P_Mx+(I-P_M)x$$ 在物理里的读法是：把一个态"投影到某个子空间上"，$$\lVert P_Mx\rVert^2$$ 就是"落在该子空间里的概率"。这一读法在第 32 章会被系统化成投影算子值测度与谱定理。**Riesz 表示定理则是 Dirac 符号的合法性证明**：$$\langle\phi\mid A\mid\psi\rangle$$ 这个写法把左矢、算子、右矢三种东西自由搬动，靠的正是 $$H\cong H^*$$。

**三者对应的这一章版本**：

| 几何 | 代数 | 物理 |
|---|---|---|
| 正交分解 $$H=M\oplus M^\perp$$ | 正交投影 $$P^2=P=P^*$$ | 测量投影，概率 $$\lVert Px\rVert^2$$ |
| 完备化（柯西列取商） | $$\mathcal{C}/\mathcal{N}$$ | "理想实验极限"的补全 |
| Riesz $$H\cong H^*$$ | 共轭线性等距同构 | bra–ket 互转，$$\langle\phi\mid\leftrightarrow\mid\phi\rangle$$ |
| 正交规范基 $$x=\sum\langle x,e_n\rangle e_n$$ | 等距同构 $$H\cong\ell^2$$ | 态按可观测量的本征态展开 |
| 平行四边形法则 | 范数来自内积的判据 | 强调"只有 $$L^2$$ 有相位几何" |

## 五、经典问题精讲 (Classical Problems)

> 每题标注**考点**（它检查什么）与**位置**（它在本章结构里的坐标）。

### 经典题 1（考点：投影定理的计算形态——Gram 矩阵；位置：3.3 定理 3.10）

**题。** 在 $$L^{2}([-1,1])$$（$$\langle f,g\rangle=\int_{-1}^{1}fg$$）中，求 $$f(x)=x^{2}$$ 到子空间 $$M=\operatorname{span}\lbrace1,x\rbrace$$ 的最佳逼近元（即最小二乘一次逼近），并验证勾股关系。

**解。** $$M$$ 是有限维子空间，从而是闭的（有限维子空间在赋范空间里恒闭），故定理 3.10 适用：最佳逼近元就是正交投影 $$Pf$$，且由 $$f-Pf\perp M$$ 刻画。

先算 $$M$$ 的 Gram 矩阵 $$G=\big(\langle e_i,e_j\rangle\big)$$（$$e_1=1$$，$$e_2=x$$）：

$$\langle1,1\rangle=\int_{-1}^{1}1\,dx=2,\qquad \langle1,x\rangle=\int_{-1}^{1}x\,dx=0,\qquad \langle x,x\rangle=\int_{-1}^{1}x^{2}dx=\frac23 .$$

（$$\langle1,x\rangle=0$$ 因为 $$x$$ 是奇函数。）再算右端：

$$\langle f,1\rangle=\int_{-1}^{1}x^{2}dx=\frac23,\qquad \langle f,x\rangle=\int_{-1}^{1}x^{3}dx=0 .$$

把 $$Pf=a\cdot1+b\cdot x$$ 代入正交条件 $$\langle f-Pf,e_i\rangle=0$$，得线性方程组

$$\begin{pmatrix}2&0\\0&\frac23\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}\frac23\\0\end{pmatrix}\ \Longrightarrow\ a=\frac{2/3}{2}=\frac13,\qquad b=0 .$$

故

$$Pf(x)=\frac13,\qquad f-Pf=x^{2}-\frac13 .$$

**验证正交性**：$$\langle x^{2}-\frac13,1\rangle=\frac23-\frac13\cdot2=0$$；$$\langle x^{2}-\frac13,x\rangle=\int_{-1}^{1}(x^{3}-\frac{x}{3})dx=0-0=0$$（奇函数积分为零）。两条都成立。

**验证勾股关系**：

$$\lVert f\rVert^{2}=\int_{-1}^{1}x^{4}dx=\frac25,\qquad \lVert Pf\rVert^{2}=\Big(\frac13\Big)^{2}\cdot2=\frac29,$$

$$\lVert f-Pf\rVert^{2}=\int_{-1}^{1}\Big(x^{2}-\frac13\Big)^{2}dx=\int_{-1}^{1}x^{4}dx-\frac23\int_{-1}^{1}x^{2}dx+\frac19\int_{-1}^{1}dx=\frac25-\frac49+\frac29=\frac{18-10}{45}=\frac{8}{45}.$$

而 $$\frac29+\frac{8}{45}=\frac{10+8}{45}=\frac{18}{45}=\frac25$$，与 $$\lVert f\rVert^{2}$$ 一致，勾股关系成立。$$\blacksquare$$

**注释。** 有限维时"正交条件"就是一个线性方程组，系数矩阵是 Gram 矩阵 $$G$$——**这就是最小二乘法的全部数学内容**：把 $$G$$ 解出来就得到投影。若把 $$x^{2}$$ 换成一般的 $$f$$，一切照旧，只是涉及 $$L^2$$ 上的三阶矩。$$\langle f,x\rangle=0$$ 导致 $$b=0$$，这不是巧合：$$x^2$$ 与 $$x$$ 的正交性来自对称性（偶函数与奇函数）。

### 经典题 2（考点：Riesz 表示的显式构造与范数计算；位置：3.3 定理 3.12）

**题。** (a) 在 $$\ell^{2}$$ 上定义 $$f(x)=\sum_{n\ge1}\frac{x_n}{n}$$。证明 $$f\in(\ell^{2})^{*}$$，写出它的 Riesz 表示向量，并求 $$\lVert f\rVert$$。

(b) 在 $$L^{2}([0,1])$$ 上定义 $$\ell(g)=\int_{0}^{1/2}g(x)\,dx$$。同样写出表示向量并求 $$\lVert\ell\rVert$$。

**解。** **(a)** 由 Cauchy–Schwarz（定理 3.2），

$$\lvert f(x)\rvert=\Big\lvert\sum_{n\ge1}\frac1n x_n\Big\rvert\le\Big(\sum_{n\ge1}\frac1{n^{2}}\Big)^{1/2}\Big(\sum_{n\ge1}\lvert x_n\rvert^{2}\Big)^{1/2}=\lVert y\rVert\,\lVert x\rVert ,$$

其中 $$y=(1,1/2,1/3,\dots)$$。因 $$\sum_n1/n^{2}=\pi^{2}/6<\infty$$（这个数在经典题 3 已算出），$$y\in\ell^{2}$$，故 $$f$$ 连续且 $$\lVert f\rVert\le\lVert y\rVert=\pi/\sqrt6$$。

由定理 3.12 的**唯一性**，表示向量只能是 $$y$$：解法是验证 $$f(x)=\langle x,y\rangle$$：

$$\langle x,y\rangle_{\ell^{2}}=\sum_{n}\overline{x_n}y_n=\sum_n\frac{x_n}{n}=f(x) .$$

再求范数：一方面 $$\lVert f\rVert\le\lVert y\rVert$$（上面的估计）；另一方面取 $$x=y$$：

$$f(y)=\sum_n\frac{1}{n^{2}}=\lVert y\rVert^{2}\ \Longrightarrow\ \lVert f\rVert\ge\frac{\lvert f(y)\rvert}{\lVert y\rVert}=\lVert y\rVert .$$

（这符合定理 3.12 的一般事实：$$\lVert f\rVert=\lVert y\rVert$$。）故

$$\lVert f\rVert=\lVert y\rVert=\Big(\frac{\pi^{2}}{6}\Big)^{1/2}=\frac{\pi}{\sqrt6} .$$

**(b)** 由 Cauchy–Schwarz，

$$\lvert\ell(g)\rvert=\Big\lvert\int_0^1 g(x)\chi_{[0,1/2]}(x)\,dx\Big\rvert\le\lVert g\rVert_{2}\cdot\Big(\int_0^{1/2}1\,dx\Big)^{1/2}=\frac{1}{\sqrt2}\lVert g\rVert_2 ,$$

故 $$\ell\in(L^{2})^{*}$$，且表示向量就是 $$y=\chi_{[0,1/2]}$$（$$\langle g,y\rangle=\int_0^{1/2}g$$，逐字符合定义）。保范性同样用 $$g=y$$ 兑现：$$\ell(y)=\int_0^{1/2}1=\frac12=\lVert y\rVert^{2}$$，故

$$\lVert\ell\rVert=\lVert y\rVert=\frac{1}{\sqrt2} . \blacksquare$$

**注释。** 两道小题说明了 Riesz 表示定理的用法：**先猜到那个向量，验证配对，再取 $$x=y$$ 兑现范数。** 范数的上界来自 Cauchy–Schwarz，下界来自"取 $$x=y$$"，这是 Riesz 表示的标准"双向估计"。

### 经典题 3（考点：Parseval 恒等式算级数；位置：3.4 定理 3.17）

**题。** 用 $$\lbrace e^{inx}/\sqrt{2\pi}\rbrace_{n\in\mathbb{Z}}$$ 是 $$L^{2}([-\pi,\pi])$$ 的正交规范基这一事实，计算 $$\sum_{n\ge1}\frac1{n^{2}}$$。

**解。** 取 $$f(x)=x$$（在 $$[-\pi,\pi]$$ 上，端点值不影响 $$L^2$$ 的元素）。由定理 3.17，Parseval 恒等式

$$\int_{-\pi}^{\pi}\lvert f\rvert^{2}dx=2\pi\sum_{n\in\mathbb{Z}}\lvert\hat f(n)\rvert^{2},\qquad \hat f(n)=\frac{1}{2\pi}\int_{-\pi}^{\pi}x e^{-inx}dx .$$

**左边**：$$\int_{-\pi}^{\pi}x^{2}dx=\frac{2\pi^{3}}{3}$$。

**右边**：对 $$n\ne0$$ 分部积分，

$$\int_{-\pi}^{\pi}x e^{-inx}dx=\Big[\frac{x e^{-inx}}{-in}\Big]_{-\pi}^{\pi}-\int_{-\pi}^{\pi}\frac{e^{-inx}}{-in}dx .$$

先算第一项：$$e^{-in\pi}=e^{in\pi}=(-1)^{n}$$，故

$$\Big[\frac{x e^{-inx}}{-in}\Big]_{-\pi}^{\pi}=\frac{\pi(-1)^{n}-(-\pi)(-1)^{n}}{-in}=\frac{2\pi(-1)^{n}}{-in}=\frac{2\pi i(-1)^{n}}{n}.$$

再算第二项：$$\int_{-\pi}^{\pi}e^{-inx}dx=\Big[\frac{e^{-inx}}{-in}\Big]_{-\pi}^{\pi}=\frac{(-1)^n-(-1)^n}{-in}=0$$（$$n\ne0$$）。所以

$$\hat f(n)=\frac{1}{2\pi}\cdot\frac{2\pi i(-1)^{n}}{n}=\frac{i(-1)^{n}}{n},\qquad \lvert\hat f(n)\rvert^{2}=\frac{1}{n^{2}} .$$

$$n=0$$ 时 $$\hat f(0)=\frac{1}{2\pi}\int_{-\pi}^{\pi}x\,dx=0$$。于是 Parseval 给出

$$\frac{2\pi^{3}}{3}=2\pi\sum_{n\ne0}\frac{1}{n^{2}}=2\pi\cdot2\sum_{n\ge1}\frac1{n^{2}}=4\pi\sum_{n\ge1}\frac1{n^{2}} ,$$

故

$$\sum_{n\ge1}\frac1{n^{2}}=\frac{2\pi^{3}}{3\cdot4\pi}=\frac{\pi^{2}}{6} . \blacksquare$$

**注释。** 这条计算是 Euler 1735 年的结果，此处不必用任何解析技巧，**它是 Parseval 恒等式的机械推论**：正交基把"函数的大小"换成"系数的大小"，而左端是初等的积分。用 $$f(x)=x^2$$ 同样可算 $$\sum 1/n^4=\pi^4/90$$（见本章练习竞赛题 1）。

### 经典题 4（考点：投影定理中"闭"不可去；位置：3.3 定理 3.10 的必要性）

**题。** 在 $$L^{2}([0,1])$$ 中取 $$M=\mathbb{R}[x]$$（多项式全体）。证明：$$M$$ 是子空间但**不是闭子空间**；对 $$f(x)=e^{x}$$，$$\operatorname{dist}(f,M)=0$$ 但**不存在** $$p\in M$$ 使 $$\lVert f-p\rVert=\operatorname{dist}(f,M)$$。由此说明定理 3.10 中"$$M$$ 闭"不可省。

**解。** **$$M$$ 不是闭的。** 由 Weierstrass 逼近定理，多项式在 $$\lVert\cdot\rVert_\infty$$ 下在 $$C([0,1])$$ 中稠密；又 $$\lVert g\rVert_2\le\lVert g\rVert_\infty$$，故稠密性对 $$\lVert\cdot\rVert_2$$ 也成立，即 $$M$$ 在 $$L^{2}([0,1])$$ 中稠密。若 $$M$$ 闭则 $$M=\overline M=L^{2}([0,1])$$，但 $$M\ne L^{2}$$（例如常数函数 $$\frac12\cdot\chi$$ 型的台阶函数不在 $$M$$ 中——更干净的理由：$$e^{x}\notin M$$，见下）。故 $$M$$ 不闭。

**距离为零。** 由稠密性，存在多项式列 $$p_n$$ 使 $$\lVert e^{x}-p_n\rVert_2\to0$$，故 $$\operatorname{dist}(e^{x},M)=0$$。

**但达不到。** 若存在 $$p\in M$$ 使 $$\lVert e^{x}-p\rVert_2=0$$，则 $$\int_0^1(e^{x}-p(x))^{2}dx=0$$；被积函数连续且非负，故 $$e^{x}=p(x)$$ 对一切 $$x\in[0,1]$$。但 $$e^{x}$$ 不是多项式：若它是次数为 $$N$$ 的多项式，则它的 $$N+1$$ 阶导数恒为 $$0$$；而 $$\frac{d^{N+1}}{dx^{N+1}}e^{x}=e^{x}>0$$，矛盾。（这也是入口题 (iii) 里用过的那条论证。）故最佳的 $$p$$ 不存在。

**结论。** $$\operatorname{dist}(e^{x},M)=0$$ 却无元素取到它，正交投影不存在。若改用 $$\overline M=L^{2}([0,1])$$，则 $$\overline M^{\perp}=\lbrace0\rbrace$$、投影是恒等映射，题目变得平凡——**病根就在"$$M$$ 不闭"这一点上**。$$\blacksquare$$

**注释。** 这道题把入口题 (ii)(iii) 的两种失败统一了：定理 3.10 要求 $$M$$ 闭，定理 3.12 要求整个空间完备；两者都指向同一件事——**逼近问题要有解，必须让极限点留在空间里。** 完备化的作用正是"把缺的极限点补进去"（定理 3.6）。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 在 $$\mathbb{C}^{n}$$ 上定义 $$\langle z,w\rangle=\sum_{j=1}^{n}z_j\overline{w_j}$$。验证它是内积；写出 $$n=1$$ 时 Cauchy–Schwarz 不等式的具体形式，并说明此时等号恒成立。

**基2.** 设 $$\lbrace e_1,\dots,e_n\rbrace$$ 是内积空间 $$H$$ 中的正交规范组，$$x\in H$$。证明 $$x-\sum_{k=1}^{n}\langle x,e_k\rangle e_k$$ 与每个 $$e_j$$ 正交，并由此推出有限版 Bessel 不等式 $$\sum_{k=1}^{n}\lvert\langle x,e_k\rangle\rvert^{2}\le\lVert x\rVert^{2}$$。

**基3.** 证明内积对第二变元共轭线性；再证明内积是连续二元函数：若 $$x_n\to x$$、$$y_n\to y$$，则 $$\langle x_n,y_n\rangle\to\langle x,y\rangle$$。

**基4.** 在 $$L^{2}([0,1])$$ 中取 $$y=\chi_{[0,1/2]}$$、$$z=\chi_{[1/2,1]}$$。验证 $$y\perp z$$，计算 $$\lVert y\rVert^{2}$$、$$\lVert z\rVert^{2}$$、$$\lVert y+z\rVert^{2}$$、$$\lVert y-z\rVert^{2}$$，并检查平行四边形法则 (3.2) 成立；再用同样的 $$y,z$$ 检查 $$L^{1}$$-范数下 (3.2) 是否成立。

### 竞赛（本课目标难度）

**竞1.** 用 Parseval 恒等式与 $$f(x)=x^{2}$$ 计算 $$\sum_{n\ge1}\frac{1}{n^{4}}$$。

**竞2.** 设 $$\lbrace e_n\rbrace_{n\ge1}$$ 是 Hilbert 空间 $$H$$ 中的正交规范**列**，$$x\in H$$。证明 $$\langle x,e_n\rangle\to0$$。再说明：尽管 $$\langle x,e_n\rangle\to0$$，"$$e_n$$ 在范数意义下收敛到 $$0$$"是**错误**的。把这两句话与本节的 Bessel 不等式放在一起，解释为什么它们不矛盾。

**竞3.** 设 $$M$$ 是 Hilbert 空间 $$H$$ 的闭子空间，$$P=P_M$$ 是正交投影，记 $$Q=I-P$$。证明：

(i) $$Q$$ 是到 $$M^{\perp}$$ 上的正交投影（即 $$Q^{2}=Q$$、$$\langle Qx,y\rangle=\langle x,Qy\rangle$$、$$Qx\in M^{\perp}$$）；

(ii) $$\lVert x\rVert^{2}=\lVert Px\rVert^{2}+\lVert Qx\rVert^{2}$$；

(iii) $$\big(M^{\perp}\big)^{\perp}=M$$。

**竞4.** 设 $$M,N$$ 是 Hilbert 空间 $$H$$ 的闭子空间。证明

$$\big(M+N\big)^{\perp}=M^{\perp}\cap N^{\perp},\qquad \big(M\cap N\big)^{\perp}=\overline{M^{\perp}+N^{\perp}} .$$

（第二个等式里为什么必须有闭包？在 $$\ell^{2}$$ 里举例说明。）

### 研究（通向下一章）

**研1.** 设 $$V=\mathbb{R}[x]$$ 带 $$\langle f,g\rangle=\int_{0}^{1}f g$$，$$\ell(f)=\int_{0}^{1}f e^{x}dx$$（即入口题的空间与泛函）。

(i) 证明 $$V$$ 的完备化（定理 3.6 意义下）等距同构于 $$L^{2}([0,1])$$。

(ii) 在该完备化中写出 $$\ell$$ 的 Riesz 表示向量，并计算 $$\lVert\ell\rVert$$。

(iii) 用一句话解释：入口题 (iii) 的失败到底是"定理错了"还是"空间缺了点东西"。

**研2.** 设 $$H=L^{2}(\mathbb{R})$$，$$\langle\phi,\psi\rangle=\int_{\mathbb{R}}\overline{\phi(x)}\psi(x)\,dx$$。

(i) 证明：对一切 $$\alpha\in\mathbb{R}$$，$$\psi\mapsto e^{i\alpha}\psi$$ 保持一切内积不变，因而 $$\psi$$ 与 $$e^{i\alpha}\psi$$ 无法由内积区分。

(ii) 举一个具体的 $$\phi,\psi$$，使 $$\langle\phi,\psi\rangle$$ 是纯虚数（即 $$\operatorname{Re}\langle\phi,\psi\rangle=0$$ 而 $$\operatorname{Im}\langle\phi,\psi\rangle\ne0$$）。

(iii) 说明 $$\operatorname{Re}\langle\phi,\psi\rangle$$ 与 $$\operatorname{Im}\langle\phi,\psi\rangle$$ 分别可能承担什么物理角色。

### 解答 (Solutions)

**解 基1.** **内积公理。** 对第一变元线性：$$\langle\alpha z+\beta z',w\rangle=\sum_j(\alpha z_j+\beta z'_j)\overline{w_j}=\alpha\sum_jz_j\overline{w_j}+\beta\sum_jz'_j\overline{w_j}=\alpha\langle z,w\rangle+\beta\langle z',w\rangle$$。

共轭对称：$$\overline{\langle w,z\rangle}=\overline{\sum_jw_j\overline{z_j}}=\sum_j\overline{w_j}z_j=\langle z,w\rangle$$（注意 $$\overline{\overline{z_j}}=z_j$$）。

正定：$$\langle z,z\rangle=\sum_jz_j\overline{z_j}=\sum_j\lvert z_j\rvert^{2}\ge0$$，且等号成立当且仅当每个 $$\lvert z_j\rvert^{2}=0$$，即 $$z=0$$。

**$$n=1$$ 时的 Cauchy–Schwarz。** 此时 $$\lvert\langle z,w\rangle\rvert=\lvert z\overline w\rvert=\lvert z\rvert\lvert w\rvert=\lVert z\rVert\lVert w\rVert$$——不等号**恒取等号**。这与定理 3.2 的等号条件（$$z,w$$ 线性相关）一致：在 $$\mathbb{C}$$ 这一维空间里，任何两个向量都线性相关。$$\blacksquare$$

**解 基2.** 记 $$s_n=\sum_{k=1}^{n}\langle x,e_k\rangle e_k$$。对固定的 $$j\in\lbrace1,\dots,n\rbrace$$，由内积对第二变元的共轭线性与 $$\langle e_k,e_j\rangle=\delta_{kj}$$，

$$\Big\langle\sum_{k=1}^{n}\langle x,e_k\rangle e_k,\ e_j\Big\rangle=\sum_{k=1}^{n}\overline{\langle x,e_k\rangle}\,\delta_{kj}=\overline{\langle x,e_j\rangle} .$$

于是

$$\langle x-s_n,e_j\rangle=\langle x,e_j\rangle-\overline{\langle x,e_j\rangle} .$$

这里就要小心约定的陷阱：我们的内积对**第一**变元线性、对**第二**变元共轭线性，所以 $$\langle x,e_j\rangle-\overline{\langle x,e_j\rangle}$$ 一般不为零。正确的算法是把 $$s_n$$ 写进**第一**变元：

$$\langle s_n,e_j\rangle=\Big\langle\sum_{k=1}^{n}\langle x,e_k\rangle e_k,\ e_j\Big\rangle=\sum_{k=1}^{n}\langle x,e_k\rangle\langle e_k,e_j\rangle=\langle x,e_j\rangle ,$$

（第一个等号用了对第一变元的线性，第二个用了 $$\langle e_k,e_j\rangle=\delta_{kj}$$ 与共轭对称在一个变元上取值的直接计算）。故 $$\langle x-s_n,e_j\rangle=0$$ 对一切 $$j$$。

**推 Bessel。** 由勾股定理（注 3.10，$$s_n$$ 是 $$n$$ 个两两正交向量之和）、$$\lVert e_k\rVert=1$$ 与 $$s_n\perp x-s_n$$，

$$\lVert x\rVert^{2}=\lVert x-s_n\rVert^{2}+\lVert s_n\rVert^{2}=\lVert x-s_n\rVert^{2}+\sum_{k=1}^{n}\big\lvert\langle x,e_k\rangle\big\rvert^{2}\ge\sum_{k=1}^{n}\big\lvert\langle x,e_k\rangle\big\rvert^{2} . \blacksquare$$

**注。** 这道题的关键 leap 不在计算，而在**约定的辨识**：一旦把 $$s_n$$ 错放进第二变元，就会得到 $$\langle x,e_j\rangle-\overline{\langle x,e_j\rangle}$$ 这种"看起来不为零"的假象。**凡是内积里出现 $$\sum c_k e_k$$，先想清楚它待在哪个变元里。**

**解 基3.** **共轭线性。** 由共轭对称与对第一变元的线性（$$\alpha=\overline{\overline\alpha}$$），

$$\langle x,\alpha y+\beta z\rangle=\overline{\langle\alpha y+\beta z,x\rangle}=\overline{\alpha\langle y,x\rangle+\beta\langle z,x\rangle}=\overline{\alpha}\,\overline{\langle y,x\rangle}+\overline{\beta}\,\overline{\langle z,x\rangle}=\overline{\alpha}\langle x,y\rangle+\overline{\beta}\langle x,z\rangle .$$

**连续性。** 先由定理 3.2 把两个差拆开：

$$\big\lvert\langle x_n,y_n\rangle-\langle x,y\rangle\big\rvert=\big\lvert\langle x_n-x,y_n\rangle+\langle x,y_n-y\rangle\big\rvert\le\lVert x_n-x\rVert\lVert y_n\rVert+\lVert x\rVert\lVert y_n-y\rVert .$$

收敛数列有界：存在 $$C$$ 使 $$\lVert y_n\rVert\le C$$、$$\lVert x\rVert\le C$$（取 $$C=\lVert x\rVert+\sup_n\lVert y_n\rVert$$，$$\sup$$ 有限由 $$y_n$$ 柯西）。于是右端 $$\le C\lVert x_n-x\rVert+C\lVert y_n-y\rVert\to0$$。$$\blacksquare$$

**解 基4.** **正交性**：$$y$$ 与 $$z$$ 的支集只交于一点 $$\lbrace1/2\rbrace$$（零测集），故

$$\langle y,z\rangle=\int_0^1y(x)z(x)dx=0 .$$

**范数**：$$\lVert y\rVert^{2}=\int_0^{1/2}1\,dx=\frac12$$；同理 $$\lVert z\rVert^{2}=\frac12$$。又 $$y+z=\chi_{[0,1]}$$，$$y-z$$ 在 $$[0,1/2)$$ 上为 $$1$$、在 $$(1/2,1]$$ 上为 $$-1$$，故

$$\lVert y+z\rVert^{2}=\int_0^1 1\,dx=1,\qquad \lVert y-z\rVert^{2}=\int_0^1 1\,dx=1 .$$

**平行四边形法则 (3.2)**：左边 $$=1+1=2$$，右边 $$=2\cdot\frac12+2\cdot\frac12=2$$，成立。

**改到 $$L^{1}$$-范数**：$$\lVert y\rVert_1=\lVert z\rVert_1=\frac12$$、$$\lVert y+z\rVert_1=1$$（$$y+z=\chi_{[0,1]}$$）、$$\lVert y-z\rVert_1=1$$。于是 (3.2) 的**左边** $$=\lVert y+z\rVert_1^{2}+\lVert y-z\rVert_1^{2}=1+1=2$$，**右边** $$=2\lVert y\rVert_1^{2}+2\lVert z\rVert_1^{2}=2\cdot\frac14+2\cdot\frac14=1$$。左 $$\ne$$ 右，法则失效。

（提醒：平行四边形法则里出现的是**范数的平方**。上面的两个范数都是 $$\frac12$$，平方后是 $$\frac14$$，"范数之和为 $$1$$"与"平方之和为 $$1$$"是两回事，混用会得出错误的等式。这个陷阱在 $$\ell^p$$ 的反例里同样存在：那里 $$\lVert x\rVert_p=2^{1/p}$$ 要平方成 $$2^{2/p}$$ 才能入式。）$$\blacksquare$$

**注（为什么取 $$y=\chi_{[0,1/2]}$$、$$z=\chi_{[1/2,1]}$$ 就能一次成功）。** 平行四边形法则把 $$y,z,y+z,y-z$$ 四者的范数绑在一起；要让 $$\lVert\cdot\rVert_1$$ 暴露它与 $$L^2$$ 的差别，必须让 $$y$$ 与 $$z$$ **处处同号**（对 $$y+z$$）同时又**处处反号**（对 $$y-z$$）——只有支集不相交的非负函数能做到。这就是定理 3.5 里 $$\ell^p$$ 反例用 $$(1,1,0,\dots)$$ 与 $$(1,-1,0,\dots)$$ 的原因：它们的"同号/反号"由坐标 $$1,1$$ 与 $$1,-1$$ 分别实现。

**解 竞1.** 用 $$f(x)=x^{2}$$ 在 $$[-\pi,\pi]$$ 上的**余弦级数**配合 Parseval 最省事——因为 $$x^{2}$$ 是偶函数，正弦项自动消失，少一半符号要记。

**第一步：实形式三角系的正交性与范数。** 族 $$\lbrace1,\ \cos nx,\ \sin nx\ (n\ge1)\rbrace$$ 两两正交（同频率的 $$\cos nx$$ 与 $$\sin nx$$ 也在一个周期上正交，因为 $$\sin(2nx)$$ 是奇函数），且

$$\int_{-\pi}^{\pi}1^{2}dx=2\pi,\qquad \int_{-\pi}^{\pi}\cos^{2}(nx)\,dx=\pi,\qquad \int_{-\pi}^{\pi}\sin^{2}(nx)\,dx=\pi .$$

**第二步：$$x^{2}$$ 的 Fourier 系数。** 记

$$a_0=\frac{1}{2\pi}\int_{-\pi}^{\pi}x^{2}dx=\frac{1}{2\pi}\cdot\frac{2\pi^{3}}{3}=\frac{\pi^{2}}{3},\qquad a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}x^{2}\cos(nx)\,dx,\qquad b_n=0 .$$

（$$b_n=0$$ 因为 $$x^{2}\sin nx$$ 是奇函数，在对称区间上积分为零。）算 $$a_n$$：先由偶性

$$\int_{-\pi}^{\pi}x^{2}\cos(nx)\,dx=2\int_{0}^{\pi}x^{2}\cos(nx)\,dx .$$

对 $$J:=\int_{0}^{\pi}x^{2}\cos(nx)\,dx$$ 分部积分。取 $$u=x^{2}$$、$$dv=\cos(nx)dx$$、$$v=\frac{\sin(nx)}{n}$$：

$$J=\Big[\frac{x^{2}\sin(nx)}{n}\Big]_{0}^{\pi}-\frac{2}{n}\int_{0}^{\pi}x\sin(nx)\,dx=0-\frac{2}{n}\int_{0}^{\pi}x\sin(nx)\,dx .$$

（边界项为 $$0$$：$$x=0$$ 与 $$x=\pi$$ 处 $$\sin(nx)=0$$，因为 $$\sin(n\pi)=0$$。）再对 $$\int_{0}^{\pi}x\sin(nx)dx$$ 分部积分，取 $$u=x$$、$$dv=\sin(nx)dx$$、$$v=-\frac{\cos(nx)}{n}$$：

$$\int_{0}^{\pi}x\sin(nx)\,dx=\Big[-\frac{x\cos(nx)}{n}\Big]_{0}^{\pi}+\frac{1}{n}\int_{0}^{\pi}\cos(nx)\,dx=-\frac{\pi\cos(n\pi)}{n}+\frac{1}{n}\Big[\frac{\sin(nx)}{n}\Big]_{0}^{\pi}=-\frac{\pi(-1)^{n}}{n}+0 .$$

（用了 $$\cos(n\pi)=(-1)^{n}$$ 与 $$\sin(n\pi)=0$$。）代回：

$$J=-\frac{2}{n}\cdot\Big(-\frac{\pi(-1)^{n}}{n}\Big)=\frac{2\pi(-1)^{n}}{n^{2}},\qquad a_n=\frac{1}{\pi}\cdot 2J=\frac{1}{\pi}\cdot\frac{4\pi(-1)^{n}}{n^{2}}=\frac{4(-1)^{n}}{n^{2}} .$$

于是

$$x^{2}=\frac{\pi^{2}}{3}+4\sum_{n\ge1}\frac{(-1)^{n}}{n^{2}}\cos(nx)\qquad(-\pi\le x\le\pi) .$$

（自检：令 $$x=0$$，得 $$0=\frac{\pi^{2}}{3}+4\sum_{n\ge1}\frac{(-1)^{n}}{n^{2}}$$，即 $$\sum_{n\ge1}\frac{(-1)^{n}}{n^{2}}=-\frac{\pi^{2}}{12}$$，这正是熟知的交错级数和，说明系数没有错。）

**第三步：Parseval。** 对正交系 $$\lbrace1,\cos nx,\sin nx\rbrace$$，Parseval 恒等式（定理 3.17 的实形式）是

$$\int_{-\pi}^{\pi}f^{2}=2\pi a_0^{2}+\pi\sum_{n\ge1}\big(a_n^{2}+b_n^{2}\big).$$

（右端每一项都是"系数 $$=$$ 内积 $$/$$ 基的范数平方"，再乘基的范数平方。）代入 $$f=x^{2}$$、$$a_0=\frac{\pi^{2}}{3}$$、$$a_n=\frac{4(-1)^{n}}{n^{2}}$$、$$b_n=0$$：

$$\int_{-\pi}^{\pi}x^{4}dx=\frac{2\pi^{5}}{5},\qquad \text{右端}=2\pi\Big(\frac{\pi^{2}}{3}\Big)^{2}+\pi\sum_{n\ge1}\frac{16}{n^{4}}=\frac{2\pi^{5}}{9}+16\pi\sum_{n\ge1}\frac{1}{n^{4}} .$$

于是

$$16\pi\sum_{n\ge1}\frac{1}{n^{4}}=\frac{2\pi^{5}}{5}-\frac{2\pi^{5}}{9}=2\pi^{5}\cdot\frac{9-5}{45}=\frac{8\pi^{5}}{45},$$

$$\sum_{n\ge1}\frac{1}{n^{4}}=\frac{8\pi^{5}}{45\cdot16\pi}=\frac{\pi^{4}}{90} . \blacksquare$$

**关键 leap。** 一是**选实形式（余弦级数）而不是复指数形式**：复形式要在 $$e^{inx}$$、$$\hat f(n)$$、共轭、以及 $$n$$ 与 $$-n$$ 两个方向上同时记账，符号出错的面积大得多；而实形式里偶函数只有余弦项，一步就砍掉一半。二是**先用低阶情形自检**：第二步末尾用 $$x=0$$ 对出了 $$\sum(-1)^{n}/n^{2}=-\pi^{2}/12$$，这只用了几秒钟，却能在继续算 $$x^{4}$$ 之前发现系数符号错误——这正是 `_experts/analysis/_SKILL.md` 打法 B（先估计、再精确）在符号计算里的用法：**每算完一个系数，都找一个后来只用到一个数字的地方兑它。** 最后一步的 $$\frac{\pi^{4}}{90}$$ 也可以反过来验证：它与经典题 3 的 $$\frac{\pi^{2}}{6}$$ 之比为 $$\frac{\pi^{4}/90}{\pi^{2}/6}=\frac{\pi^{2}}{15}$$，而 $$\zeta(4)=\frac{\pi^{2}}{15}\zeta(2)$$ 正是 Euler 的递推关系，数目对得上。

**解 竞2.** **第一句：$$\langle x,e_n\rangle\to0$$。** 由 Bessel（定理 3.16），$$\sum_{n}\lvert\langle x,e_n\rangle\rvert^{2}\le\lVert x\rVert^{2}<\infty$$。收敛级数的通项趋于零，故 $$\langle x,e_n\rangle\to0$$。**注意这只需 Bessel，不需要 $$H$$ 完备，也不需要 $$\lbrace e_n\rbrace$$ 是基。**

**第二句：$$\lVert e_n-0\rVert=1\not\to0$$。** 因为 $$\lVert e_n\rVert=\sqrt{\langle e_n,e_n\rangle}=1$$ 对一切 $$n$$。

**为什么不矛盾。** "$$\langle x,e_n\rangle\to0$$ 对每个 $$x$$"说的是：把 $$e_n$$ 用**每一个**固定向量去量，量出来的数趋于零。这是**逐向量（弱）**的收敛，等价于说 $$e_n$$ 在**弱拓扑**下趋于 $$0$$。而"$$e_n\to0$$ 于范数"要求 $$\lVert e_n\rVert\to0$$，即**一致地**小。Bessel 不等式给出的界 $$\lVert x\rVert^{2}$$ 依赖于 $$x$$，且**没有任何先验理由**让这个界随 $$n$$ 缩小。换个说法：$$x=\sum_n\langle x,e_n\rangle e_n$$（若 $$\lbrace e_n\rbrace$$ 是基）里每一项的系数趋于零，但每项的**长度**始终是 $$1$$——把无穷多个"长度为 $$1$$ 的成分"按系数衰减的方式叠加，整体仍然收敛。这就是"范数收敛严格强于弱收敛"的最简例子，也是第 08 章练习研究题 2 里"无穷维让 $$V\ne V^*$$"的同一条断层线。$$\blacksquare$$

（补一句：由定理 3.13，Hilbert 空间自反，弱拓扑与弱\*拓扑重合，这个例子里 $$e_n\xrightarrow{w}0$$ 但 $$\lVert e_n\rVert=1$$，说明**弱收敛不保范数**。）

**解 竞3.** **(i)** $$Q=I-P$$。由 $$P^{2}=P$$，$$Q^{2}=(I-P)^{2}=I-2P+P^{2}=I-P=Q$$。共轭对称：由定义 3.11 里 $$P$$ 的共轭对称性，$$\langle Qx,y\rangle=\langle x,y\rangle-\langle Px,y\rangle=\langle x,y\rangle-\langle x,Py\rangle=\langle x,Qy\rangle$$。值域：由定理 3.10 的分解 $$x=Px+Qx$$、$$Px\in M$$、$$Qx\in M^{\perp}$$，故 $$Qx\in M^{\perp}$$。再由 $$Q=M^{\perp}$$ 上投影的定义即得。

**(ii)** 由 $$x=Px+Qx$$ 且 $$Px\perp Qx$$（$$Px\in M$$、$$Qx\in M^{\perp}$$），用勾股定理（注 3.10）：

$$\lVert x\rVert^{2}=\lVert Px+Qx\rVert^{2}=\lVert Px\rVert^{2}+\lVert Qx\rVert^{2} .$$

**(iii)** 一方面 $$M\subset(M^{\perp})^{\perp}$$：若 $$m\in M$$，则对一切 $$u\in M^{\perp}$$ 有 $$\langle m,u\rangle=0$$（由 $$u\perp M$$ 的定义），故 $$m\in(M^{\perp})^{\perp}$$。反之设 $$x\in(M^{\perp})^{\perp}$$。由定理 3.10 写 $$x=Px+Qx$$；$$Qx\in M^{\perp}$$，故 $$\langle x,Qx\rangle=0$$；又 $$\langle x,Qx\rangle=\langle Px+Qx,Qx\rangle=\lVert Qx\rVert^{2}$$（用了 $$Px\perp Qx$$）。于是 $$\lVert Qx\rVert^{2}=0$$，$$Qx=0$$，$$x=Px\in M$$。故 $$(M^{\perp})^{\perp}=M$$。$$\blacksquare$$

（对比命题 3.8 的一般结论 $$(S^{\perp})^{\perp}=\overline{\operatorname{span}S}$$：对闭子空间才有 $$=M$$。这正是"闭"在下标里出现两次的原因。）

**解 竞4.** **第一个等式。** 对任意 $$x\in H$$，逐步等价：

$$x\in(M+N)^{\perp}\iff\langle x,m+n\rangle=0\ \text{对一切 } m\in M,\ n\in N$$

$$\iff\langle x,m\rangle=0\ \forall m\in M\ \text{且}\ \langle x,n\rangle=0\ \forall n\in N\iff x\in M^{\perp}\cap N^{\perp} .$$

（"$$\Leftarrow$$"用 $$\langle x,m+n\rangle=\langle x,m\rangle+\langle x,n\rangle$$；"$$\Rightarrow$$"分别取 $$(m,n)=(m,0)$$ 与 $$(0,n)$$。）

**第二个等式。** 把已证的第一个等式用在 $$M^{\perp}$$、$$N^{\perp}$$ 上，并利用竞3(iii) 的 $$(M^{\perp})^{\perp}=M$$：

$$\big(M^{\perp}+N^{\perp}\big)^{\perp}=(M^{\perp})^{\perp}\cap(N^{\perp})^{\perp}=M\cap N . \tag{3.11}$$

**两边同时取 $$\perp$$**。左边取 $$\perp$$ 得 $$\big((M^{\perp}+N^{\perp})^{\perp}\big)^{\perp}$$，而对任何子空间 $$A$$ 有 $$(A^{\perp})^{\perp}=\overline{A}$$（命题 3.8 的推论），故它等于 $$\overline{M^{\perp}+N^{\perp}}$$；右边取 $$\perp$$ 得 $$(M\cap N)^{\perp}$$。于是

$$(M\cap N)^{\perp}=\overline{M^{\perp}+N^{\perp}} .$$

（顺带得到包含关系 $$M^{\perp}+N^{\perp}\subset(M\cap N)^{\perp}$$。）

**闭包不可去：一个例子。** 取 $$H=\ell^{2}\oplus\ell^{2}$$（向量写成配对 $$(a,b)$$，$$a,b\in\ell^{2}$$，内积是两分量内积之和），并取

$$M=\big\lbrace(x,0):\ x\in\ell^{2}\big\rbrace,\qquad N=\big\lbrace(x,Tx):\ x\in\ell^{2}\big\rbrace,\qquad T=\operatorname{diag}\Big(1,\tfrac12,\tfrac13,\dots\Big).$$

$$M$$ 显然闭。$$N$$ 是有界算子 $$T$$ 的**图像 (graph)**，而图像必闭：若 $$(x_k,Tx_k)\to(a,b)$$，则 $$x_k\to a$$（第一分量收敛）且 $$Tx_k\to b$$；由 $$T$$ 连续，$$Tx_k\to Ta$$，故 $$b=Ta$$，即 $$(a,b)=(a,Ta)\in N$$。又

$$M\cap N=\big\lbrace(x,0):\ Tx=0\big\rbrace=\lbrace0\rbrace$$

（$$T$$ 的对角元 $$1,1/2,1/3,\dots$$ 全不为零，故 $$\ker T=\lbrace0\rbrace$$），于是 $$(M\cap N)^{\perp}=H=\ell^{2}\oplus\ell^{2}$$。

再直接算两个正交补。对 $$(u,v)\in H$$：

$$(u,v)\in M^{\perp}\iff u=0;\qquad (u,v)\in N^{\perp}\iff\big\langle(x,Tx),(u,v)\big\rangle=\langle x,u\rangle+\langle x,Tv\rangle=0\ \ \forall x\iff u=-Tv .$$

（第二个等价：把 $$x=e_n$$ 逐个代入，读出每个坐标的等式；其中用了 $$T$$ 自伴，即 $$\langle Tx,v\rangle=\langle x,Tv\rangle$$。）于是

$$M^{\perp}+N^{\perp}=\big\lbrace(0,w)+(-Tv,v):\ v,w\in\ell^{2}\big\rbrace=\big\lbrace(-Tv,\ w+v):\ v,w\in\ell^{2}\big\rbrace=\operatorname{ran}(T)\oplus\ell^{2}$$

（第二分量随 $$w$$ 遍历整个 $$\ell^{2}$$，第一分量随 $$v$$ 遍历 $$\operatorname{ran}(T)$$）。而

$$\operatorname{ran}(T)=\Big\lbrace b\in\ell^{2}:\ \sum_{n}n^{2}\lvert b_n\rvert^{2}<\infty\Big\rbrace$$

在 $$\ell^{2}$$ 中**稠密但不闭**：它包含一切有限支集向量（故稠密），却不含 $$b=(1,\tfrac12,\tfrac13,\dots)\in\ell^{2}$$（因为 $$\sum_n n^{2}\cdot\frac1{n^{2}}=\sum_n1=\infty$$），而 $$b$$ 正是那些有限支集向量的范数极限。所以

$$M^{\perp}+N^{\perp}=\operatorname{ran}(T)\oplus\ell^{2}\ \subsetneq\ \ell^{2}\oplus\ell^{2}=(M\cap N)^{\perp} .$$

**闭包确实不能去掉。**（几何读法：$$M\cap N=\lbrace0\rbrace$$ 时 $$(M\cap N)^{\perp}$$ 是整个空间，但 $$M^{\perp}+N^{\perp}$$ 会漏掉一条稠密的"裂缝"。这就是无穷维里"两个闭子空间之和未必闭"的现象，也是"闭值域定理"要处理的同一类麻烦；见知识库 `泛函分析/ch06.md`。）$$\blacksquare$$

**解 研1.** **(i)** 记 $$\iota:V\to L^{2}([0,1])$$ 为包含映射。对 $$f,g\in V$$，

$$\langle f,g\rangle=\int_{0}^{1}fg=\langle\iota f,\iota g\rangle_{L^{2}} ,$$

故 $$\iota$$ 保内积（因而是单射，由定理 3.14(ii) 的论证）。又 $$L^{2}([0,1])$$ 完备，且由 Weierstrass 逼近定理，多项式（即 $$\iota(V)$$）在 $$\lVert\cdot\rVert_\infty$$ 下稠密于 $$C([0,1])$$，而 $$C([0,1])$$ 在 $$L^{2}$$ 中稠密，故 $$\iota(V)$$ 在 $$L^{2}([0,1])$$ 中稠密。于是 $$\big(L^{2}([0,1]),\iota\big)$$ 满足定理 3.6 的 (i)(ii)，**是** $$V$$ 的一个完备化；由该定理的**唯一性**部分，$$V$$ 的完备化等距同构于 $$L^{2}([0,1])$$。

**(ii)** $$\ell(f)=\int_{0}^{1}f(x)e^{x}dx=\langle\iota f,\ e^{x}\rangle_{L^{2}}$$（实数情形共轭无用），故在完备化里 $$\ell$$ 的 Riesz 表示向量就是 $$y=e^{x}\in L^{2}([0,1])$$。范数

$$\lVert\ell\rVert=\lVert y\rVert_{L^{2}}=\Big(\int_0^{1}e^{2x}dx\Big)^{1/2}=\sqrt{\frac{e^{2}-1}{2}} .$$

与定理 3.14 (iv) 的估计 $$\sqrt{(e^{2}-1)/2}$$ 一致。

**(iii)** 不是定理错了，是**空间缺了那个向量**。$$V=\mathbb{R}[x]$$ 不全，$$e^{x}$$ 这个"应该存在的极限"没有落脚处；把它补进去（完备化）之后，Riesz 表示立刻成立，$$y=e^{x}$$ 只是恰好在补进来的那部分里。**这正是第 08 章的 $$g^\flat$$ 从"单射"升格为"同构"的代价：不是换一个定理，而是换一个空间。** 换句话说，完备化就是"让泛函有资格被向量表示"这件事的收费口。$$\blacksquare$$

**（接下一章）** 到这里 $$\mathbb{R}[x]$$ 的缺口被 $$L^{2}$$ 补上，Hilbert 空间的几何（投影、正交基、Riesz）全部到位——**下一章（第 32 章：从 Hamilton 到量子）就把这套几何交给物理：态是 $$L^{2}$$ 里的单位向量，可观测量是自伴算子，投影 $$P_M$$ 就是"测量落在 $$M$$ 里"的事件，而 Riesz 表示定理正是 Dirac 符号 $$\langle\phi\mid\psi\rangle$$ 得以自由搬运左右矢的原因。**

**解 研2.** **(i)** 对 $$\alpha\in\mathbb{R}$$，

$$\big\langle e^{i\alpha}\phi,\ e^{i\alpha}\psi\big\rangle=\int_{\mathbb{R}}\overline{e^{i\alpha}\phi(x)}\,e^{i\alpha}\psi(x)\,dx=\int_{\mathbb{R}}e^{-i\alpha}\overline{\phi(x)}\,e^{i\alpha}\psi(x)\,dx=\int_{\mathbb{R}}\overline{\phi(x)}\psi(x)\,dx=\langle\phi,\psi\rangle ,$$

（用了 $$\overline{e^{i\alpha}}=e^{-i\alpha}$$ 与 $$e^{-i\alpha}e^{i\alpha}=1$$）。故乘 $$e^{i\alpha}$$ 保一切内积，特别地保范数：$$\lVert e^{i\alpha}\psi\rVert=\lVert\psi\rVert$$。由注 3.20，$$\overline{\phi}\psi=\lvert\phi\rvert\lvert\psi\rvert e^{i(\arg\psi-\arg\phi)}$$ 只依赖相位**差**，整体相位 $$\alpha$$ 在差里抵消。**于是内积无法区分 $$\psi$$ 与 $$e^{i\alpha}\psi$$**——在物理上这意味着"态"不是 $$L^{2}$$ 的单个向量，而是它的一个 $$U(1)$$ 轨道（这一点在第 48 章的射影表示里会正式化）。

**(ii)** 取 $$\phi=\chi_{[0,1]}$$、$$\psi=i\chi_{[2,3]}$$（分别支在不相交区间 $$[0,1]$$ 与 $$[2,3]$$ 上）。则

$$\langle\phi,\psi\rangle=\int_{\mathbb{R}}\overline{\chi_{[0,1]}(x)}\,i\chi_{[2,3]}(x)\,dx=0 ,$$

这是 $$0$$，不是纯虚数——因为支集不相交。改用支集相交的例子：取 $$\phi=\chi_{[0,2]}$$、$$\psi=i\chi_{[1,3]}$$，则

$$\langle\phi,\psi\rangle=\int_{1}^{2}i\,dx=i .$$

于是 $$\operatorname{Re}\langle\phi,\psi\rangle=0$$ 而 $$\operatorname{Im}\langle\phi,\psi\rangle=1\ne0$$。

**(iii)** 由注 3.20 与经典题 2 的读法：$$\operatorname{Re}\langle\phi,\psi\rangle$$ 是**实数、对称**的部分（$$\overline{\operatorname{Re}\langle\phi,\psi\rangle}=\operatorname{Re}\langle\psi,\phi\rangle$$），它承担"概率与期望值"这类**可观测的实数**——$$\lvert\langle\phi,\psi\rangle\rvert^{2}$$ 给出"在态 $$\phi$$ 中测得态 $$\psi$$"的概率；$$\operatorname{Im}\langle\phi,\psi\rangle$$ 是**反对称**的部分（$$\operatorname{Im}\langle\phi,\psi\rangle=-\operatorname{Im}\langle\psi,\phi\rangle$$，是一个**辛形式**，与第 08 章 3.5 节、3.6 节的结构同源），它承担**正则对易关系 $$[q,p]=i\hbar$$ 那一侧**的代数信息：相位差的方向性（顺时针/逆时针）在虚部里，而量子力学的非交换性正来自这个反对称结构。$$\blacksquare$$

**（接下一章）** 到这一步，"Hilbert 空间 + 复 Hermite 内积的实部/虚部"已经把几何与代数都铺好了：**第 32 章（从 Hamilton 到量子：可观测量与本征态）会把 $$\operatorname{Re}$$ 的部分变成测量概率、把 $$\operatorname{Im}$$ 的部分变成 $$[q,p]=i\hbar$$，并把自伴算子搬上舞台——这正是本章定理 3.12、定理 3.13 与注 3.20 三件事合起来的物理面目。**

## 七、Takeaway 与延伸 (Takeaways)

**1. 从有限维到无穷维，活的结论与死的结论各有哪些。** 活下来的：Cauchy–Schwarz（定理 3.2，与维数无关）、正交性与正交补（定义 3.7、命题 3.8）、勾股定理（注 3.10）、内积诱导范数（定理 3.3）。死掉或需要附加条件的：**"单射即满射"**（秩—零化度定理失效，$$g^\flat$$ 只保住单射）、**"有界闭集紧"**（Heine–Borel 失效，故极小化序列未必收敛）、**"$$V\cong V^*$$"**（需要内积 + 完备）。补上完备性后，死掉的那三条里前两条复活：极小元存在唯一（定理 3.9）、正交分解成立（定理 3.10）、Riesz 表示成立（定理 3.12）。

**2. 完备性是唯一的收费口。** 本章所有"$$=$$"最终都被某条 $$\varepsilon$$ 论证兑现：投影要用柯西列取极限，Riesz 要用闭凸集的极小元，Fourier 展开要用部分和柯西。**只要有人问"这一步为什么能取极限"，答案永远是完备性。** 这也是为什么 $$L^p$$、$$C(K)$$、$$\ell^p$$ 都被先做成 Banach 空间再谈别的。

**3. 第 08 章的 $$g^\flat$$ 是本章的主题曲。** 有限维时它是同构，但那靠的是"$$\dim V=\dim V^{*}$$"这个维数巧合（第 08 章 定理 3.6 的证明里"满射"那一步用到了有限维），内积只贡献了单射。无穷维里维数不再相等（$$\mathbb{R}[x]$$：$$\aleph_0$$ 对 $$\mathfrak{c}$$），于是 $$g^\flat$$ 的地位必须被重新谈判：**它在 Hilbert 空间上是等距同构（定理 3.12、3.13），在不完备的内积空间上不是满射（定理 3.14），在非 Hilbert 的 Banach 空间上一般也不行（$$L^1$$ 与 $$L^\infty$$ 的可分性反例）。** 第 06 章的问题 3 问"$$V\cong V^*$$ 为什么在无穷维会崩"，本章的回答是：**崩的不是内积，是"维数保证同构"这条捷径；修好它的唯一办法是要求空间完备。**

**4. 正交规范基把"函数"变成"数列"。** 定理 3.18 说所有无限维可分 Hilbert 空间都等距同构于 $$\ell^2$$，这句话是省力的极致：算 $$L^2$$ 里的几何等于算 $$\ell^2$$ 里的几何。定理 3.17 给出换算公式（Fourier 展开 + Parseval），经典题 3 与练习竞赛题 1 演示了它如何把难以手算的级数变成机械的积分。**注意区分"几何收敛"与"点态收敛"**：注 3.19 说明 Fourier 级数的 $$L^2$$ 收敛是正交基给的，而逐点发散是 Dirichlet 核 $$L^1$$ 范数无界（$$\sim\log N$$）造成的——这是本章最容易被误读的一点。

**5. 平行四边形的判别力。** 定理 3.5 的 (3.2) 是一条**代数指纹**：它把"范数来自内积"变成可检验的恒等式，并一举把 $$\ell^p,\ L^p\ (p\ne2)$$ 从 Hilbert 家族里踢出去。练习基础题 4 提醒了一个容易犯的错：入式的是**范数的平方**，不是范数本身。这条判据在后续章节还会以别的面貌出现（如 Hilbert 空间的自反性、弱拓扑与弱\*拓扑重合都依赖它）。

**下一章的悬念（第 32 章：从 Hamilton 到量子——可观测量与本征态）。** 本章把舞台搭好了：$$H$$ 是 Hilbert 空间，$$H\cong H^*$$ 由 Riesz 给出，正交投影 $$P_M$$ 是"到子空间的最短距离"。但真正的物理还没上场。下一章做三件事：第一，把 $$L^2(\mathbb{R})$$ 上的**复 Hermite 内积**的实部与虚部分开读——实部给概率与期望值，虚部给正则对易关系 $$[q,p]=i\hbar$$（这正是第 08 章练习研究题 2 留下的那句话）；第二，把**自伴算子**定义为"内积对称"的算子（$$\langle Tx,y\rangle=\langle x,Ty\rangle$$），并用本章的定理 3.12 说明为什么在 Hilbert 空间上"自伴 $$=$$ 可以搬来搬去"，而在 Banach 空间上只能谈对偶空间之间的 $$A^{*}:Y^{*}\to X^{*}$$（MP39 的起点）；第三，把第 04 章的"$$J^2=-I$$、谱为 $$\pm i$$"与本章的 $$L^2$$ 正交基合起来，得到量子力学最早的那批本征值问题（谐振子、氢原子）。**一句话：本章给的是**几何**，下一章给的是**物理**——同一个 Hilbert 空间的两副面孔。**

**延伸阅读。**

- W. Rudin, *Functional Analysis*, 2nd ed.（Ch. 4 Hilbert 空间、Ch. 12 测度与积分）：Riesz 表示定理与正交基的标准处理，即知识库 `泛函分析/ch05.md` 的来源。
- J. B. Conway, *A Course in Functional Analysis*, GTM 96（Ch. 1）：几何视角下的 Hilbert 空间，投影定理的强形式（闭凸集）。
- MIT OCW 18.102 *Introduction to Functional Analysis*（第 14–17 讲）：Melrose 讲义路径，即知识库 `泛函分析/mit-18-102/ch08.md–ch10.md` 的来源；Fejér 绕道与 $$L^2$$ 收敛在这份讲义里讲得最清楚。
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics*, Vol. I（Ch. II）：把本章内容直接作为量子力学的地基来使用——原专栏 MP38 推荐的就是这套书。
- R. Vershynin, *Lectures in Functional Analysis*（第 4–5 章）：从紧算子与谱理论回头看 Hilbert 空间，是第 32 章之后的路。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch29_Hilbert空间与内积结构_上.md">← 第29章 Hilbert 空间与内积结构·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch31_从Hamilton到量子_可观测量与本征态_上.md">第31章 从 Hamilton 到量子：可观测量与本征态·上 →</a></div>
</div>
