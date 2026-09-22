---
layout: default
---

# 第32章: 从 Hamilton 到量子：可观测量与本征态·下：完整推导 (From Hamilton to Quantum Mechanics: Observables and Eigenstates · Part II: Full Derivation)

> 配套预备: 见 第31章 从 Hamilton 到量子：可观测量与本征态·上（同一主题的具体铺垫，建议先读）

> 专家依据: `_experts/analysis/spectral-theory.md`（主）+ `_experts/analysis/_SKILL.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

本章要回答一个具体的问题：**把经典力学改造成量子力学，到底动的是经典力学的哪一个结构？**

流行说法是"把数换成算子"。这句话不算错，但它没指出动手的位置，于是位置算符为什么是"乘 $$x$$"、动量算符为什么是"$$-i\hbar\frac{d}{dx}$$"，就都成了要背下来的约定。本章要说明：真正被换掉的是**括号**——量子力学保存了相空间上光滑函数全体所带的整个括号代数，只把 Poisson 括号 $$\{F,G\}$$ 换成了对易子的 $$\frac{1}{i\hbar}[\hat F,\hat G]$$。位置与动量两个算符之所以必须长成那样，是这条要求逼出来的，不是灵感。

**从哪来**：第 03、04 章造出了对偶与辛结构，相空间 $$T^*M$$ 上的典范二形式 $$\omega=dq\wedge dp$$ 在那里露面；本章要从堆里重新读出 Hamilton 方程与 Poisson 括号。第 30 章把波函数装进了 Hilbert 空间 $$L^2\langle\cdot,\cdot\rangle$$，但那个空间上还什么都没有发生——本章把算子放到它上面去。第 04 章那句"求导给出谱"，当时只是 $$SO(2)$$ 上的一个小例子；本章里它长成了量子力学的核心：动量算符就是求导算符乘上 $$-i\hbar$$，它的谱就是全部允许的动量读数。

**到哪去**：第 34 章会把这些算子组装成一条演化方程，即 Schrödinger 方程。

## 二、入口：一道具体的问题 (Entry Problem)

本节先给题，不给定义。四问都不会在本节解答：(a) 的答案在 3.4，(b) 在 3.5，(c) 在 3.7（还会在例题 5.3 里再算一遍），(d) 在 3.8 与 3.9。

**入口题（自编；风格取自教材经典例题与 Квант 口径，(b)(c) 取自 [Hall 2013] 第一章习题）。**

一根无重力、无阻尼、悬浮的橡皮筋被拉成一个周长 $$2\pi$$ 的圆环，环上可以驻留频率唯一的单色波。用 $$x\in[0,2\pi)$$ 表示环上一点的弧长坐标，设环上的光滑复值函数全体为一个函数空间 $$\mathscr X$$（本章后面会说明，再加上一个内积它就是第 30 章的 Hilbert 空间）。

**(a) 求导给出的谱。** 把求导算子 $$D=\dfrac{d}{dx}$$ 作用在单色波 $$\psi_k(x)=e^{ikx}$$ 上：

$$D\psi_k=\frac{d}{dx}e^{ikx}=ik\,e^{ikx}.$$

要使 $$\psi_k$$ 是环上良定义的函数（即周期为 $$2\pi$$ 的 $$C^\infty$$ 函数），$$k$$ 必须取哪些值？在这些函数上，$$D$$ 的全部特征值是什么？它们都是实数吗？

**(b) 实数谱的代价。** 实验物理学家告诉你一条铁律：凡是能被仪器读到的量，读数都是实数。既然 $$D$$ 的特征值带上了一个虚部，$$D$$ 自己就不能代表任何可观测量。但 (a) 里那组单色波是好的，不该丢掉。请你构造一个新算子 $$P$$，使下面两条同时成立：

- (i) 特征函数不变，还是全体 $$e^{ikx}$$；
- (ii) 特征值全部是实数，且与频率 $$k$$ 成正比。

把 $$P$$ 显式写出来，并指明那个比例系数是由什么定下来的。

**(c) 两个算子的差。** 再引入一个算子 $$X$$，它的作用是"乘 $$x$$"：$$(X\psi)(x)=x\psi(x)$$。取任意一个光滑的检验函数 $$\psi$$，分别算出 $$(XP)\psi$$ 与 $$(PX)\psi$$，再求差 $$(XP-PX)\psi$$。这个差等于 $$0$$ 吗？如果不等于 $$0$$，它等于什么？它会随 $$\psi$$ 改变吗？

**(d) 为什么是这个差。** 设 $$A,B,C$$ 分别是两个这样的算子（先把它们想成"求导"与"乘函数"这种具体对象就够了）。记

$$[A,B]=AB-BA.$$

先做一个纯代数的小证明：

$$[AB,C]=A[B,C]+[A,C]B.$$

再回答：经典力学里有没有一个二元运算，它和 $$[\,,\,]$$ 具有完全相同的三条代数性质——双线性、反对称、以及满足上面的 Leibniz 律与 Jacobi 恒等式？如果有，它是谁？它在 (c) 里那对具体算子上取值多少？

本章会让你看到一件比"数换成算子"更准确的事：**(b) 里被迫乘上的那个 $$-i\hbar$$ 不是灵感，是 (d) 逼出来的**——只有在它之下，量子力学的括号与经典力学的 Poisson 括号才遵守同一套代数律。

## 三、结构：定义与完整推导 (Structure & Proof)

本节分两半。前半（3.1–3.6）是经典那一侧：把第 08 章的辛结构翻译成 Hamilton 方程与 Poisson 括号，看清"经典可观测量"到底是什么对象。后半（3.7–3.15）是量子那一侧：造出两个算子，算清它们的括号，然后论证为什么量子可观测量必须是**自伴**算子。

### 3.1 经典一侧：相空间、Hamilton 方程与 Poisson 括号

**定义 3.1（相空间与 Hamilton 量, phase space and Hamiltonian）**。设 $$M$$ 是 $$n$$ 维光滑流形，称它为**位形空间 (configuration space)**——在本课程后面的物理章节里它取 $$\mathbb{R}^3$$ 或 $$\mathbb{R}^{3N}$$。它的**余切丛 (cotangent bundle, 见第 12 章)** $$T^*M$$ 上的点写作

$$(q,p)=\bigl(q^1,\dots,q^n,\,p_1,\dots,p_n\bigr),\qquad q\in M,\ \ p\in T_q^*M,$$

称 $$q$$ 为**广义坐标 (generalized coordinates)**、$$p$$ 为**广义动量 (generalized momenta)**，称 $$T^*M$$ 为**相空间 (phase space)**。

设保守系统的 Lagrange 量是 $$L(q,\dot q)=T(\dot q)-V(q)$$，其中 $$T,\ V$$ 分别是动能与势能。定义**共轭动量 (conjugate momenta)**

$$p_i=\frac{\partial L}{\partial \dot q^i},\qquad i=1,\dots,n.$$

（这一步是把切丛上的速度换成余切丛上的动量，正是第 06 章"对偶"在物理里的实例。）对 $$L$$ 作 **Legendre 变换 (Legendre transform)**，得到相空间上的实值光滑函数

$$H(q,p)=\sum_{i=1}^n p_i\dot q^i-L(q,\dot q)
=\frac{1}{2m}\sum_{i=1}^n p_i^2+V(q),$$

称为 **Hamilton 量 (Hamiltonian)**。最后一步用了 $$T=\frac{m}{2}\sum_i(\dot q^i)^2$$ 与 $$p_i=m\dot q^i$$，于是 $$\sum_ip_i\dot q^i=m\sum_i(\dot q^i)^2=2T$$，故 $$H=2T-(T-V)=T+V$$：Hamilton 量就是总能量。

**定理 3.1（Hamilton 方程）**。运动轨迹满足 Euler–Lagrange 方程 $$\dfrac{d}{dt}\dfrac{\partial L}{\partial \dot q^i}=\dfrac{\partial L}{\partial q^i}$$ 当且仅当

$$\dot q^i=\frac{\partial H}{\partial p_i},\qquad \dot p_i=-\frac{\partial H}{\partial q^i},\qquad i=1,\dots,n.$$

*证明*：只需对上式两边做 Legendre 变换的逆运算。先算两个偏导。对 $$\dot q$$ 求偏导：由 $$p_j=\partial L/\partial\dot q^j$$ 得

$$\frac{\partial H}{\partial \dot q^i}=\frac{\partial}{\partial \dot q^i}\Bigl(\sum_j p_j\dot q^j-L\Bigr)=p_i-\frac{\partial L}{\partial \dot q^i}=p_i-p_i=0.$$

所以 $$H$$ 作为 $$(q,p)$$ 的函数与 $$\dot q$$ 无关（这正是 Legendre 变换消掉 $$\dot q$$ 的意思）。记 $$H(q,p)$$，则把 $$H=\sum_jp_j\dot q^j-L$$ 对 $$p_i$$ 求偏导时，$$\dot q$$ 被看作 $$(q,p)$$ 的函数，于是

$$\frac{\partial H}{\partial p_i}=\dot q^i+\sum_jp_j\frac{\partial \dot q^j}{\partial p_i}-\frac{\partial L}{\partial \dot q^j}\frac{\partial \dot q^j}{\partial p_i}
=\dot q^i+\sum_j\Bigl(p_j-\frac{\partial L}{\partial \dot q^j}\Bigr)\frac{\partial \dot q^j}{\partial p_i}=\dot q^i,$$

因为括号里每项都等于零。这就给出第一组方程。对 $$q^i$$ 求偏导时 $$p$$ 固定：

$$\frac{\partial H}{\partial q^i}=\sum_j p_j\frac{\partial \dot q^j}{\partial q^i}-\frac{\partial L}{\partial q^i}-\sum_j\frac{\partial L}{\partial \dot q^j}\frac{\partial \dot q^j}{\partial q^i}
=-\frac{\partial L}{\partial q^i},$$

再次用了 $$p_j=\partial L/\partial\dot q^j$$ 消掉两串。另一方面 Euler–Lagrange 方程说 $$\dot p_i=\dfrac{d}{dt}\dfrac{\partial L}{\partial \dot q^i}=\dfrac{\partial L}{\partial q^i}$$。代入即得 $$\dot p_i=-\partial H/\partial q^i$$。

反过来，若 Hamilton 方程成立，把第一式写成 $$p_i=m\dot q^i$$ 代入第二式并对时间求导，就回到 Euler–Lagrange 方程。$$\blacksquare$$

**定义 3.2（Poisson 括号, Poisson bracket）**。对相空间上任两个光滑函数 $$F,G\in C^\infty(T^*M)$$，定义

$$\{F,G\}=\sum_{i=1}^n\Bigl(\frac{\partial F}{\partial q^i}\frac{\partial G}{\partial p_i}-\frac{\partial F}{\partial p_i}\frac{\partial G}{\partial q^i}\Bigr).$$

**定理 3.2（Poisson 括号的代数性质与典范关系）**。对任意 $$F,G,K\in C^\infty(T^*M)$$ 与 $$\alpha,\beta\in\mathbb{R}$$：

- **(i) 双线性 (bilinear)**：$$\{\alpha F+\beta G,K\}=\alpha\{F,K\}+\beta\{G,K\}$$，第二个变量同理；
- **(ii) 反对称 (antisymmetric)**：$$\{F,G\}=-\{G,F\}$$，特别地 $$\{F,F\}=0$$；
- **(iii) Leibniz 律**：$$\{FG,K\}=F\{G,K\}+\{F,K\}G$$；
- **(iv) Jacobi 恒等式**：$$\{F,\{G,K\}\}+\{G,\{K,F\}\}+\{K,\{F,G\}\}=0$$；
- **(v) 典范关系**：$$\{q^i,q^j\}=0$$、$$\{p_i,p_j\}=0$$、$$\{q^i,p_j\}=\delta^i_j$$。

*证明*：(i)(ii) 逐项看 (定义 3.2) 的表达式：每一项都是两个一阶偏导的乘积，偏导算子本身对两个变量分别线性、且两个变量上下对称只差一个符号，所以双线性与反对称立得。

(iii)：固定一个分量 $$i$$，记 $$u=\partial/\partial q^i,\ v=\partial/\partial p_i$$，则第 $$i$$ 项是 $$uF\cdot vG-u_pF\cdots$$ 这样的组合；写成 $$\{F,K\}=\sum_i[u_i(F)v_i(K)-v_i(F)u_i(K)]$$。由乘积求导法则 $$u(FG)=u(F)G+Fu(G)$$：

$$\{FG,K\}=\sum_i\bigl[u_i(F)G\,v_i(K)+F\,u_i(G)v_i(K)-v_i(F)G\,u_i(K)-F\,v_i(G)u_i(K)\bigr]$$
$$=G\sum_i[u_i(F)v_i(K)-v_i(F)u_i(K)]+F\sum_i[u_i(G)v_i(K)-v_i(G)u_i(K)]
=G\{F,K\}+F\{G,K\}.$$

(iv)：这是唯一需要真算的一条。先在 $$n=1$$ 的情形算完，再说明一般情形。把 $$x=(q,p)$$ 简写成两个坐标，下标表示偏导，则 $$\{F,G\}=F_qG_p-F_pG_q$$。先算里层：

$$(\{F,G\})_p=F_{qp}G_p+F_qG_{pp}-F_{pp}G_q-F_pG_{qp},$$
$$(\{F,G\})_q=F_{qq}G_p+F_qG_{pq}-F_{pq}G_q-F_pG_{qq}.$$

于是

$$\{H,\{F,G\}\}=H_q\bigl[F_{qp}G_p+F_qG_{pp}-F_{pp}G_q-F_pG_{qp}\bigr]-H_p\bigl[F_{qq}G_p+F_qG_{pq}-F_{pq}G_q-F_pG_{qq}\bigr].$$

把 $$\{F,\{G,H\}\}$$ 与 $$\{G,\{H,F\}\}$$ 按把字母循环替换 $$H\mapsto F\mapsto G\mapsto H$$ 得到。三式相加，按"哪个函数被求了二阶导"分类。以 $$G$$ 的二阶导项为例：上式里含 $$G_{qp}$$ 的系数是 $$-H_qF_p$$，含 $$G_{pq}$$ 的系数是 $$-H_pF_q$$；而在 $$\{F,\{G,H\}\}$$ 里，含 $$G_{qp}$$ 的系数是 $$F_qH_p$$，含 $$G_{pq}$$ 的系数是 $$F_pH_q$$。注意 $$G_{pq}$$ 与 $$G_{qp}$$ 数值相等，但位置不同、系数不同，必须分开收拢后再相加：

$$G_{qp}\text{ 项系数}:\ -H_qF_p+F_qH_p=0,\qquad G_{pq}\text{ 项系数}:\ -H_pF_q+F_pH_q=0.$$

同理，二阶导落在 $$F$$ 上的项与落在 $$H$$ 上的项，也就是把上式中的字母两两循环置换后的同一批式子，系数也都成对相消。故三项之和为 $$0$$，这就是 (iv)。（每个函数都不产生别的二阶导，且 $$F_{qp}=F_{pq}$$ 一类的交换性已用上。）

一般 $$n$$：把 $$\{F,G\}$$ 的求和写成 $$\sum_i[u_i(F)v_i(G)-v_i(F)u_i(G)]$$，展开后出现的二阶导是 $$u_iu_j,\ u_iv_j,\ v_iv_j$$ 三类。$$i=j$$ 的项就是上面的 $$n=1$$ 计算，逐 $$i$$ 重复即可；$$i\ne j$$ 的项在把指标 $$(i,j)$$ 与 $$(j,i)$$ 配对后，因 $$u_iu_j=u_ju_i$$ 与括号的反对称性成对抵消（已用程序按 $$n=2$$ 的例子核验）。$$\blacksquare$$

(v)：$$q,p$$ 是相空间的独立坐标，故 $$\partial q^i/\partial q^j=\delta^i_j$$、$$\partial q^i/\partial p_j=0$$、$$\partial p_i/\partial q^j=0$$、$$\partial p_i/\partial p_j=\delta^j_i$$。代入 (定义 3.2)：$$\{q^i,p_j\}=\delta^i_j\delta^i_j$$ 型的两项相减得 $$\delta^i_j$$；而 $$\{q^i,q^j\}$$ 的两项里都含因子 $$\partial q^j/\partial p_k=0$$，故为零；$$\{p_i,p_j\}$$ 同理。$$\blacksquare$$

$$\{q^i,p_j\}=\delta^i_j$$ 这一条是整章的种子：它说"位置与动量这对共轭变量，在括号下的取值恰好是 $$1$$"。量子力学要做的事，就是让同一个 $$1$$ 以另一种代数形式重新出现。

### 3.2 经典可观测量：相空间上的实函数

**定义 3.3（经典可观测量, classical observable）**。把相空间上光滑实值函数全体记作

$$\mathscr X=C^\infty(T^*M;\mathbb{R}).$$

$$A\in\mathscr X$$ 称为一个**经典可观测量**：给定系统的一个状态 $$(q,p)\in T^*M$$，它就给出一个确定的实读数 $$A(q,p)$$。

"实读数"三个字是定义的一部分，不是修辞：$$A$$ 取实值，是因为它要对应仪器上的一个刻度。请把这一条记牢，第三节 3.11 整节的论证都建立在它上面——到了量子那一侧，这条要求会逼出一个很强的条件。

**定理 3.3（Hamilton 量生成时间演化）**。设系统沿 Hamilton 方程的轨迹 $$t\mapsto(q(t),p(t))$$ 运动，$$A\in\mathscr X$$。则沿轨迹

$$\frac{dA}{dt}=\{H,A\}=\bigl(\text{定义 3.2 的 Poisson 括号}\bigr).$$

*证明*：由链式法则与 Hamilton 方程 (定理 3.1)，

$$\frac{dA}{dt}=\sum_i\Bigl(\frac{\partial A}{\partial q^i}\dot q^i+\frac{\partial A}{\partial p_i}\dot p_i\Bigr)
=\sum_i\Bigl(\frac{\partial A}{\partial q^i}\frac{\partial H}{\partial p_i}-\frac{\partial A}{\partial p_i}\frac{\partial H}{\partial q^i}\Bigr)=\{H,A\}.$$

（最后一式与定义 3.2 里 $$F=H,G=A$$ 的写法逐项对齐；由反对称性也等于 $$-\{A,H\}$$，两种写法在文献里都常见，本书统一用 $$\{H,A\}$$。）$$\blacksquare$$

定理 3.3 值得多读一遍。它说：Hamilton 量 $$H$$ 单独一个函数，就决定了**所有**可观测量的时间变化率——**每一个 $$A$$ 的演化都是它与 $$H$$ 的括号**。换句话说，$$H$$ 的作用方式是"与它作括号"，这是一种纯代数的描述，完全没有用到坐标。这句话是本章后半段最关键的线索：量子化要保留的，正是"用一个算子对另一个算子作括号来生成演化"这个模式。

由定义 3.2 的典范关系 (v) 立刻得到 Hamilton 方程本身的括号写法，把它和定理 3.1 对照：

$$\dot q^i=\{q^i,H\},\qquad \dot p_i=\{p_i,H\}.$$

### 3.3 量子一侧：状态与可观测量的替换

第 30 章把波函数装进了复 Hilbert 空间 $$L^2\langle\cdot,\cdot\rangle$$：内积由 Hermite 共轭的积分给出，

$$\langle\phi,\psi\rangle=\int_\Omega\overline{\phi(x)}\,\psi(x)\,dx,$$

其中 $$\Omega\subseteq\mathbb{R}^n$$ 是粒子可能出现的区域，$$\overline{\phi}$$ 表示复共轭。本章全程用 Dirac 记号 $$\lvert\psi\rangle$$ 表示向量（右矢, ket），$$\langle\psi\rvert$$ 表示它的对偶（左矢, bra，"左矢—右矢"配对即是内积）。

**定义 3.4（量子态与量子可观测量, quantum state and quantum observable）**

- **量子态**就是 $$L^2\langle\cdot,\cdot\rangle$$ 中的一个单位向量 $$\lvert\psi\rangle$$（$$\langle\psi\vert\psi\rangle=1$$，归一化使得后面要定义的"概率"真的加起来是 $$1$$）。量子态全体记作

$$\mathscr H=L^2\langle\cdot,\cdot\rangle .$$

- **量子可观测量**是 $$\mathscr H$$ 上的一个**自伴算子 (self-adjoint operator)** $$\hat A:\mathscr H\to\mathscr H$$，即满足

$$\langle\phi,\hat A\psi\rangle=\langle\hat A\phi,\psi\rangle\qquad\text{对一切 }\phi,\psi\in\mathscr H .$$

（严格地说自伴还要求定义域与共轭算子的定义域相同，见 3.15 与第 42 章；本章先用上面这条"对称性"条件，它已经足够承载全部物理论证。）

经典与量子两侧的对象就这样一一对上：

| 经典力学 | 量子力学 |
|---|---|
| 状态：相空间中的点 $$(q,p)\in T^*M$$ | 状态：单位向量 $$\lvert\psi\rangle\in\mathscr H$$ |
| 状态空间：相空间 $$T^*M$$ | 状态空间：Hilbert 空间 $$\mathscr H=L^2$$ |
| 可观测量：实函数 $$A\in C^\infty(T^*M)$$ | 可观测量：自伴算子 $$\hat A=\hat A^{*}$$ |
| 括号：Poisson 括号 $$\{F,G\}$$ | 括号：对易子 $$\frac{1}{i\hbar}[\hat F,\hat G]$$ |

**这张表里只有第四行是"真的定义"，前三行都是类比**。本章的全部力气都花在第四行：它是唯一能同时解释"为什么是 $$-i\hbar$$"和"为什么必须自伴"的那一条。下一小节起，我们从最具体的驻波问题开始，看它怎样逼出这些替换。

### 3.4 求导给出谱：第 04 章线索的升级

现在正式解入口题 (a)。

**定理 3.4（求导算子的谱）**。设 $$\mathscr H_{\mathrm{per}}=C^\infty_{2\pi}(\mathbb{R};\mathbb{C})$$ 是 $$\mathbb{R}$$ 上以 $$2\pi$$ 为周期的光滑复值函数全体，$$D=\dfrac{d}{dx}$$ 按 $$\psi\mapsto\psi'$$ 作用。则对每个整数 $$k\in\mathbb{Z}$$，

$$D e^{ikx}=ik\,e^{ikx},$$

并且 $$\{\psi_k=e^{ikx}\}_{k\in\mathbb{Z}}$$ 是 $$\mathscr H_{\mathrm{per}}$$ 的一组特征函数，对应的特征值恰为 $$\{ik\}_{k\in\mathbb{Z}}$$，一个不多一个不少。

*证明*：良定义性先做。$$e^{ik(x+2\pi)}=e^{ikx}e^{2\pi ik}$$，它等于 $$e^{ikx}$$ 当且仅当 $$e^{2\pi ik}=1$$，即 $$k\in\mathbb{Z}$$。所以"周期 $$2\pi$$"这个环条件恰好把 $$k$$ 限制为整数——这就是入口题 (a) 的答案，也是"量子化"在纯经典框架里唯一的来源：**不是谁规定了 $$k$$ 要离散，是环的拓扑规定了它**。（把环换成长 $$\mathbb{R}$$，$$k$$ 就连续取值，见 3.14。）

再算特征值：$$\dfrac{d}{dx}e^{ikx}=ik\,e^{ikx}$$，故 $$\psi_k$$ 是特征函数、特征值 $$ik\in i\mathbb{Z}$$。"一个不多一个不少"用的是 Fourier 展开：任何 $$\psi\in\mathscr H_{\mathrm{per}}$$ 都能写成 $$\sum_k c_k\psi_k$$（一致收敛），而 $$D\psi=\lambda\psi$$ 意味着按特征函数展开后每个分量都满足 $$c_k(ik-\lambda)=0$$，故只允许 $$\lambda=ik$$ 对某个使 $$c_k\ne0$$ 的 $$k$$ 成立。$$\blacksquare$$

特征值全是**纯虚数** $$ik$$（$$k\ne0$$ 时虚部非零，$$k=0$$ 时等于 $$0$$）。按定义 3.3 的精神——可观测量的读数必须是实数——$$D$$ 不能代表任何可观测量。

但请停在这里看一眼这个尴尬处的"来源"。$$D$$ 本身没有任何毛病，它是这座函数空间上最自然的算子；有毛病的是"$$D$$ 的特征值恰好是纯虚的"。而在第 04 章我们恰恰见过这套结构：那里 $$SO(2)$$ 的生成元 $$J$$ 是反对称矩阵，其特征值也是纯虚的 $$\{\pm i\}$$，并且 $$i$$ 在那里从"一个被假设存在的数"变成了"求导算子谱上的一条线"。本章要做的，是把那条线再往下推一步：**给纯虚的谱乘一个数，让它落到实轴上**。这件事一旦做成，代价就是那个乘数，而那个乘数就是 $$\hbar$$ 与 $$-i$$。

### 3.5 动量算子

接着解入口题 (b)。

**定义 3.5（动量算子, momentum operator）**。在 $$\mathscr H=L^2(\mathbb{R})$$ 上定义

$$P=-i\hbar\frac{d}{dx},\qquad\text{即}\quad (P\psi)(x)=-i\hbar\frac{d\psi}{dx},$$

其中 $$\hbar$$ 是 Planck 常数（除以 $$2\pi$$）。$$P$$ 称为**动量算子**。

**定理 3.5（动量算子的特征值与量子化条件）**。对任意 $$k\in\mathbb{R}$$，

$$P e^{ikx}=-i\hbar\cdot ik\,e^{ikx}=\hbar k\,e^{ikx}.$$

于是 $$P$$ 在单色波上有特征值 $$\hbar k\in\mathbb{R}$$（当 $$k\in\mathbb{Z}$$ 时它们是离散的），并且

$$p=\hbar k$$

正是 de Broglie 物质波假设。换言之：**入口题 (b) 的唯一解（在"特征函数不变、特征值实且正比于 $$k$$"的要求下）就是 $$P=-i\hbar\dfrac{d}{dx}$$**，比例系数是 $$\hbar$$；乘上 $$-i$$ 是为了把 $$D$$ 的 $$ik$$ 搬成实数，乘上 $$\hbar$$ 是为了让读数带上能量的量纲。

*证明*：前半是直接计算 $$-i\hbar\dfrac{d}{dx}e^{ikx}=-i\hbar(ik)e^{ikx}=\hbar k\,e^{ikx}$$。唯一性：设算子 $$P$$ 满足 $$Pe^{ikx}=\lambda(k)e^{ikx}$$ 对一切 $$k$$ 成立，且 $$\lambda(k)=ck$$ 为实数。$$P$$ 是形如 $$a\dfrac{d}{dx}+b$$ 的一阶线性算子（因为它在每个 $$e^{ikx}$$ 上是乘常数，而在这些波的有限线性组合上必须保持线性），于是

$$P e^{ikx}=a(ik)e^{ikx}+b\,e^{ikx}=(iak+b)e^{ikx},$$

故 $$\lambda(k)=iak+b$$。要求它对一切实数 $$k$$ 取实值，得 $$a$$ 纯虚、$$b=0$$，写成 $$a=-i\hbar$$ 即固定了比例 $$\hbar$$。$$\blacksquare$$

定理 3.5 就是原专栏 MP41 所说的"经典驻波的量子化"：环上的驻波本来是经典现象，一旦要求它的每个模式都携带一个实数、且与整数频率成正比的量，这个量就只能是 $$\hbar k$$。量子化不是外加的假设，它是"要求谱落在实轴上"的副产品。

### 3.6 位置算子

接着解入口题 (c) 的一半：把"位置"也变成算子。

**定义 3.6（位置算子与高阶矩, position operator）**。在 $$\mathscr H=L^2(\Omega)$$ 上定义

$$(X\psi)(x)=x\psi(x).$$

更一般地，对正整数 $$m$$ 定义 $$(X^m\psi)(x)=x^m\psi(x)$$。$$X$$ 称为**位置算子**。

**定理 3.6（位置算子给出各阶矩）**。设 $$\lvert\psi\rangle\in\mathscr H$$ 已归一化，$$\langle\psi\vert\psi\rangle=1$$。则对一切正整数 $$m$$，

$$\langle\psi\vertX^m\psi\rangle=\int_\Omega \overline{\psi(x)}\,x^m\,\psi(x)\,dx=E(x^m),$$

右边正是位置 $$x$$ 的第 $$m$$ 阶**矩 (moment)**；$$m=1$$ 时即为位置的**期望 (expectation value)** $$E(x)$$。特别地 $$E(x)=\langle\psi\vertX\psi\rangle$$ 是实数。

*证明*：由定义 3.6 直接代入内积定义：

$$\langle\psi\vertX^m\psi\rangle=\int_\Omega\overline{\psi(x)}\,(X^m\psi)(x)\,dx=\int_\Omega\overline{\psi(x)}\,x^m\psi(x)\,dx=\int_\Omega x^m\lvert\psi(x)\rvert^2dx,$$

最后一式就是按概率密度 $$\lvert\psi(x)\rvert^2$$（由 $$\langle\psi\vert\psi\rangle=1$$ 归一）对 $$x^m$$ 加权平均，即 $$E(x^m)$$。实性：$$x^m$$ 实、$$\lvert\psi\rvert^2$$ 非负实，积分是实的。$$\blacksquare$$

于是经典的"位置函数" $$Q(q,p)=q$$ 对应到了 $$X$$，"动量函数" $$P(q,p)=p$$ 对应到了 $$-i\hbar\dfrac{d}{dx}$$。两个算子的作用方式截然不同——一个乘 $$x$$，一个求导——但它们在 3.14 里会被证明是**同一件事在两种表象下的样子**，中间的桥就是 Fourier 变换。

### 3.7 正则对易关系

这是入口题 (c) 的答案，也是本章的心脏。

**定理 3.7（正则对易关系, canonical commutation relation）**。设 $$X$$、$$P$$ 如定义 3.5、3.6，作用在适当光滑、衰减足够快的函数 $$\psi$$ 上（例如 Schwartz 函数，见 3.15）。则

$$[X,P]:=XP-PX=i\hbar\,I,$$

其中 $$I$$ 是恒等算子。更明确地：$$(XP-PX)\psi=i\hbar\,\psi$$ 对一切这样的 $$\psi$$ 成立。

*证明*：不必算两次，只算一个方向再相减即可。

$$(XP\psi)(x)=X\bigl(-i\hbar\,\psi'(x)\bigr)=-i\hbar\,x\,\psi'(x),$$

$$(PX\psi)(x)=P\bigl(x\,\psi(x)\bigr)=-i\hbar\,\frac{d}{dx}\bigl(x\psi(x)\bigr)=-i\hbar\bigl(\psi(x)+x\,\psi'(x)\bigr),$$

第二式用了乘积求导法则。两式相减：

$$(XP-PX)\psi=-i\hbar x\psi'+i\hbar\psi+i\hbar x\psi'=i\hbar\,\psi.$$

$$\blacksquare$$

请注意这个证明里真正干活的只有一件事：**Leibniz 律**。$$P$$ 是求导，$$X$$ 是乘 $$x$$，而求导作用在乘积上会多吐出一项 $$\psi$$；如果 $$X$$ 只是"乘一个常数"，这一项就不会出现，两个算子就会交换。所以 $$[X,P]=i\hbar$$ 的根源不是"量子力学很神秘"，而是"求导与乘法不对易"这件初等事实。入口题 (c) 的答案就是：差不为零，它恒等于 $$i\hbar\psi$$，与 $$\psi$$ 无关——它是一个**算子**，而不是一个数。

$$[X,P]=i\hbar$$ 与经典关系 $$\{q,p\}=1$$ 长得像，这不是巧合；3.9 会把这件事说清楚。

### 3.8 对易子：一个与 Poisson 括号同构的括号

**定义 3.7（对易子, commutator）**。设 $$\mathcal L(\mathscr H)$$ 是 $$\mathscr H$$ 上线性算子全体（各自带定义域）。定义二元运算

$$[\,\cdot\,,\cdot\,]:\mathcal L(\mathscr H)\times\mathcal L(\mathscr H)\to\mathcal L(\mathscr H),\qquad [\hat A,\hat B]=\hat A\hat B-\hat B\hat A.$$

称 $$[\hat A,\hat B]$$ 为 $$\hat A,\hat B$$ 的**对易子**（物理文献也称"不对易子"，因为它度量的正是两者交换失败的程度）。若 $$[\hat A,\hat B]=0$$，称两算子**对易 (commute)**。

**定理 3.8（对易子的代数性质）**。对任意算子 $$\hat A,\hat B,\hat C$$ 与 $$\alpha,\beta\in\mathbb{C}$$：

- **(i) 双线性**：$$[\alpha\hat A+\beta\hat B,\hat C]=\alpha[\hat A,\hat C]+\beta[\hat B,\hat C]$$，第二变量同理；
- **(ii) 反对称**：$$[\hat A,\hat B]=-[\hat B,\hat A]$$，特别地 $$[\hat A,\hat A]=0$$；
- **(iii) Leibniz 律**：$$[\hat A\hat B,\hat C]=\hat A[\hat B,\hat C]+[\hat A,\hat C]\hat B$$；
- **(iv) Jacobi 恒等式**：$$[\hat A,[\hat B,\hat C]]+[\hat B,[\hat C,\hat A]]+[\hat C,[\hat A,\hat B]]=0$$；
- **(v) 自伴算子的对易子是反自伴的**：若 $$\hat A=\hat A^{*}$$、$$\hat B=\hat B^{*}$$，则 $$[\hat A,\hat B]^{*}=-[\hat A,\hat B]$$。

*证明*：(i)(ii) 直接把 $$[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$$ 代入，用算子加法的线性与乘积的分配律，逐项相加即得；两个变量分别线性、上下互换变号，都是"减号两边对称"的直接后果。

(iii)：把定义写开，

$$[\hat A\hat B,\hat C]=\hat A\hat B\hat C-\hat C\hat A\hat B,$$
$$\hat A[\hat B,\hat C]+[\hat A,\hat C]\hat B=\hat A\hat B\hat C-\hat A\hat C\hat B+\hat A\hat C\hat B-\hat C\hat A\hat B=\hat A\hat B\hat C-\hat C\hat A\hat B .$$

两式相等（中间两项 $$\pm\hat A\hat C\hat B$$ 相消）。(iii) 证完。注意这里**不需要**任何"算子可交换"的假设——恰恰相反，正因为不交换，这个恒等式才有内容。

(iv)：直接展开 $$[\hat A,[\hat B,\hat C]]=\hat A\hat B\hat C-\hat A\hat C\hat B-\hat B\hat C\hat A+\hat C\hat B\hat A$$。把三次循环的同类项合并：展开式中每个"交错积"（如 $$\hat A\hat B\hat C$$ 与 $$\hat B\hat A\hat C$$）都会以相反的符号出现两次。以 $$\hat A\hat B\hat C$$ 为例，它出现在第一项的 $$+$$ 号处，而 $$\hat C\hat A\hat B$$ 出现在别的项中；逐步核对六个排列 $$\{ABC,ACB,BAC,BCA,CAB,CBA\}$$，正负各三个且两两配对：$$+ABC-\cancel{ACB}-\cancel{BAC}+\cancel{BCA}+\cancel{CAB}-CBA$$ 中的交错项，加上第二、三项贡献的其余交错项，六项的和恰为 $$ABC+BCA+CAB-ACB-CBA-BAC$$。再代入 $$[\,\cdot\,,\cdot\,]$$ 的定义式核对：这些正是 $$\hat A\hat B\hat C+\hat B\hat C\hat A+\hat C\hat A\hat B-\hat A\hat C\hat B-\hat B\hat A\hat C-\hat C\hat B\hat A=0$$。$$\blacksquare$$

（对 (iv) 更省力的读法：定义"求交换子"映射 $$\mathrm{ad}_{\hat A}(\hat B)=[\hat A,\hat B]$$，则 (iii) 说 $$\mathrm{ad}_{\hat A}$$ 是一个**导子 (derivation)**；而 (iv) 说 $$\mathrm{ad}_{\hat A}$$ 本身也满足 Leibniz 律：$$\mathrm{ad}_{\hat A}([\hat B,\hat C])=[\mathrm{ad}_{\hat A}\hat B,\hat C]+[\hat B,\mathrm{ad}_{\hat A}\hat C]$$。把这条展开就是 (iv)。这说明"两个求导的代换失败"仍然是"求导"。）

(v)：用自伴的定义 $$\langle\phi,\hat A\psi\rangle=\langle\hat A\phi,\psi\rangle$$。对任意 $$\phi,\psi$$，

$$\langle\phi,[\hat A,\hat B]\psi\rangle=\langle\phi,\hat A\hat B\psi\rangle-\langle\phi,\hat B\hat A\psi\rangle
=\langle\hat A\phi,\hat B\psi\rangle-\langle\hat B\phi,\hat A\psi\rangle,$$
$$\langle[\hat A,\hat B]\phi,\psi\rangle=\langle\hat A\hat B\phi,\psi\rangle-\langle\hat B\hat A\phi,\psi\rangle
=\langle\hat B\phi,\hat A\psi\rangle-\langle\hat A\phi,\hat B\psi\rangle=-\langle\phi,[\hat A,\hat B]\psi\rangle .$$

于是 $$[\hat A,\hat B]^{*}=-[\hat A,\hat B]$$，即对易子是**反自伴**的。这条性质马上会解释那个 $$i$$。$$\blacksquare$$

### 3.9 Dirac 对应：为什么偏偏是这个替换

现在把两侧合起来看。对照 (定理 3.2) 与 (定理 3.8)，会发现一件整齐的事：**Poisson 括号与 $$\frac{1}{i\hbar}$$ 倍的对易子，满足完全相同的四条代数律**。

| | Poisson 括号 | $$\dfrac{1}{i\hbar}$$ 倍对易子 |
|---|---|---|
| 双线性 | 是 | 是 |
| 反对称 | 是 | 是 |
| Leibniz 律 | 是 | 是 |
| Jacobi 恒等式 | 是 | 是 |

**定理 3.9（Dirac 对应）**。设 $$\hbar>0$$，$$\hat 1=I$$。要求一个对应 $$F\mapsto\hat F$$ 把相空间函数送到 $$\mathscr H$$ 上的算子，满足：

- (a) $$\hat q^i=X^i$$（乘 $$x^i$$）、$$\hat p_i=-i\hbar\,\partial_{x^i}$$；
- (b) 对应是 $$\mathbb{C}$$-线性的；
- (c) **保括号**：$$\widehat{\{F,G\}}=\frac{1}{i\hbar}[\hat F,\hat G]$$ 对一切 $$F,G$$ 成立。

则 (c) 里的系数 $$\frac{1}{i\hbar}$$ 是唯一能让左边配上自伴算子的取法；换句话说，如下两条等价，且它们互相决定：

$$[X,P]=i\hbar\,I\quad\Longleftrightarrow\quad\{q,p\}=1 .$$

*证明*：分三步，前两步定"形状"，第三步定"尺度"。

**第一步：为什么系数必须是纯虚数。** 左边 $$\widehat{\{F,G\}}$$ 是 $$\widehat{F,G}$$ 对应到的算子；如果 $$F,G$$ 都是可观测量（自伴），那么它们的 Poisson 括号也是可观测量（相空间上的实函数），所以左边应当是**自伴**算子。右边 $$[\hat F,\hat G]$$ 是反自伴的 (定理 3.8 (v))。而算子 $$\alpha[\hat F,\hat G]$$（$$\alpha$$ 是复数）自伴当且仅当

$$\bigl(\alpha[\hat F,\hat G]\bigr)^{*}=\bar\alpha\,[\hat F,\hat G]^{*}=\bar\alpha\bigl(-[\hat F,\hat G]\bigr)=-\bar\alpha[\hat F,\hat G]$$

要等于 $$\alpha[\hat F,\hat G]$$，即 $$-\bar\alpha=\alpha$$，即 $$\alpha$$ 是纯虚数。所以系数只能取 $$\alpha=\dfrac{1}{i\hbar}$$ 这种形状（$$\dfrac{1}{i}=\dfrac{i}{i\cdot i}=-i$$ 也是纯虚的），绝不能是 $$1$$ 或 $$\hbar$$ 这类实数。**这就是那个 $$i$$ 的全部来源**：它不来自任何物理假设，它是"对易子反自伴"这一代数事实的必然推论。

**第二步：为什么两侧的代数律必须匹配。** 保括号对应 (c) 若成立，则由于 $$\{,\}$$ 与 $$\frac{1}{i\hbar}[\,,\,]$$ 都满足双线性、反对称、Leibniz、Jacobi，这套对应至少在最基本的结构上是自洽的：任何用 $$\{,\}$$ 写出的经典等式（例如定理 3.3 的演化方程、定理 3.1 的 Hamilton 方程）都会被自动翻译成用 $$\frac{1}{i\hbar}[\,,\,]$$ 写出的量子等式。这解释了原专栏 MP43 的那三行对应：

$$\dot q^i=\{q^i,H\}\ \longleftrightarrow\ \frac{d\hat q^i}{dt}=\frac{1}{i\hbar}[\hat q^i,\hat H],\qquad
\dot p_i=\{p_i,H\}\ \longleftrightarrow\ \frac{d\hat p_i}{dt}=\frac{1}{i\hbar}[\hat p_i,\hat H].$$

右边两个方程即 **Heisenberg 运动方程**（第 34 章展开）。若系数不匹配（比如取实数系数），两侧的反对称性与 Jacobi 律就会打架，翻译出来的等式不再自洽。所以 (c) 不是"一种选择"，是**唯一**能让经典—量子两侧代数同步的取法。

**第三步：尺度由典范关系锁定。** 把 $$F=q^i,G=p_j$$ 代入 (c)：左边是 $$\widehat{\{q^i,p_j\}}=\widehat{\delta^i_j}=\delta^i_j I$$（常数函数对应标量算子）；右边是 $$\frac{1}{i\hbar}[X^i,\hat p_j]$$。于是

$$[X^i,\hat p_j]=i\hbar\,\delta^i_j\,I .$$

$$i=j=1$$ 时即 (定理 3.7)。这就同时定下了 $$\hbar$$ 出现的位置与符号。若改用别的单位使 $$\hbar=1$$，等式变成 $$[X,P]=iI$$——那只是单位约定，代数内容没有变。$$\blacksquare$$

**这就是入口题 (d) 的答案**：经典力学里那个和 $$[\,,\,]$$ 性质相同的运算是 Poisson 括号；在 $$(X,P)$$ 这对具体算子上，它取值为 $$\{q,p\}=1$$，而对易子取值为 $$[X,P]=i\hbar$$。两侧的 $$1$$ 是同一个 $$1$$。

### 3.10 为什么必须是自伴算子

到这里，"为什么要换成算子"已经清楚了；还剩一个更尖锐的问题：为什么必须是**自伴**算子，随便一个算子不行吗？

**定理 3.10（自伴性的三条等价功能）**。

- **(a) 期望恒为实**：若 $$\hat A=\hat A^{*}$$，则对一切 $$\psi\in\mathscr H$$，$$\langle\psi\vert\hat A\psi\rangle\in\mathbb{R}$$。
- **(b) 反之亦真**：若 $$\hat A$$ 是线性算子且 $$\langle\psi\vert\hat A\psi\rangle\in\mathbb{R}$$ 对一切 $$\psi\in\mathscr H$$ 成立，则 $$\langle\phi,\hat A\psi\rangle=\langle\hat A\phi,\psi\rangle$$ 对一切 $$\phi,\psi$$ 成立，即 $$\hat A$$ 对称。
- **(c) 本征值恒为实**：若 $$\hat A=\hat A^{*}$$ 且 $$\hat A\psi=\lambda\psi$$、$$\psi\ne0$$，则 $$\lambda\in\mathbb{R}$$。

*证明* (a)：由内积的共轭对称性 $$\langle u,v\rangle=\overline{\langle v,u\rangle}$$ 与自伴性 $$\langle\hat A\psi,\psi\rangle=\langle\psi,\hat A\psi\rangle$$（把自伴定义里的 $$\phi,\psi$$ 都取成 $$\psi$$）：

$$\langle\psi,\hat A\psi\rangle=\langle\hat A\psi,\psi\rangle=\overline{\langle\psi,\hat A\psi\rangle},$$

一个数等于自己的共轭，故它是实数。$$\blacksquare$$

*证明* (b)：思路是**极化 (polarization)**——把"对角元 $$\langle\psi,A\psi\rangle$$ 实"这条较弱的信息放大成"所有非对角元对称"这条较强的信息。记

$$f(\phi,\psi)=\langle\phi,\hat A\psi\rangle-\langle\hat A\phi,\psi\rangle .$$

$$f$$ 对第二变量线性、对第一变量共轭线性（sesquilinear）。由 (a) 的对偶条件，对一切 $$\psi$$ 有 $$f(\psi,\psi)=\langle\psi,\hat A\psi\rangle-\overline{\langle\psi,\hat A\psi\rangle}=0$$。

取 $$\phi,\psi$$ 任意、$$\lambda\in\mathbb{C}$$，把第二个变量换成 $$\psi+\lambda\phi$$：

$$0=f(\psi+\lambda\phi,\psi+\lambda\phi)=f(\psi,\psi)+\bar\lambda f(\phi,\psi)+\lambda f(\psi,\phi)+\lvert\lambda\rvert^2f(\phi,\phi)
=\bar\lambda f(\phi,\psi)+\lambda f(\psi,\phi).$$

注意 $$f(\psi,\phi)=-\overline{f(\phi,\psi)}$$（直接把定义取共轭并交换内积的两个变量可得）。记 $$g=f(\phi,\psi)$$，则上式成为 $$\bar\lambda g-\lambda\bar g=0$$ 对一切 $$\lambda\in\mathbb{C}$$。

- 取 $$\lambda=1$$：$$g-\bar g=2i\,\mathrm{Im}\,g=0$$，故 $$\mathrm{Im}\,g=0$$；
- 取 $$\lambda=i$$：$$-ig-i\bar g=-i(g+\bar g)=-2i\,\mathrm{Re}\,g=0$$，故 $$\mathrm{Re}\,g=0$$。

于是 $$g=0$$，即 $$f(\phi,\psi)=0$$，也就是 $$\langle\phi,\hat A\psi\rangle=\langle\hat A\phi,\psi\rangle$$。$$\blacksquare$$

*证明* (c)：这是三条里最短的一条，也最要紧。

$$\lambda\langle\psi\vert\psi\rangle=\langle\psi\vert\lambda\psi\rangle=\langle\psi\vert\hat A\psi\rangle\overset{(a)}{=}\overline{\langle\psi\vert\hat A\psi\rangle}=\overline{\langle\hat A\psi\vert\psi\rangle}=\overline{\langle\lambda\psi\vert\psi\rangle}=\overline{\lambda}\,\langle\psi\vert\psi\rangle .$$

因为 $$\psi\ne0$$ 且内积是正定的，$$\langle\psi\vert\psi\rangle>0$$，可以两边约掉，得 $$\lambda=\overline{\lambda}$$，即 $$\lambda\in\mathbb{R}$$。$$\blacksquare$$

**这三条合起来说清了一件物理上不可让步的事**：一个量要能被"测量"、要能给出数值结果，它的谱就必须落在实轴上（(c)），它的期望就必须是实数（(a)）；而 (b) 说这两条要求反过来把"自伴"完全锁死了。所以"可观测量 = 自伴算子"不是约定，而是被逼出来的结论。原专栏 MP42 说 X、P "在有界性上出问题、只能在稠定子空间上谈对称"，说的正是同一件事的另一面：**自伴性是要争来的，不是免费的**（见 3.15）。

### 3.11 本征态展开与统计诠释

**定义 3.11（本征态展开与概率幅, eigenstate expansion and probability amplitude）**。设 $$\hat A=\hat A^{*}$$ 是可观测量，并设它的归一化特征向量 $$\{\lvert e_i\rangle\}_{i}$$ 构成 $$\mathscr H$$ 的一组**正交归一基 (orthonormal basis)**：

$$\hat A\lvert e_i\rangle=\lambda_i\lvert e_i\rangle,\qquad \langle e_i\verte_j\rangle=\delta_{ij}.$$

（"存在这样一组基"正是**谱定理 (spectral theorem)** 的内容；有限维情形总有，无限维情形要加条件，见第 38 章。）于是任一量子态 $$\lvert\psi\rangle$$ 可唯一展开为

$$\lvert\psi\rangle=\sum_i c_i\lvert e_i\rangle,\qquad c_i=\langle e_i\vert\psi\rangle .$$

$$c_i$$ 称为 $$\lvert\psi\rangle$$ 在 $$\lvert e_i\rangle$$ 上的**概率幅 (probability amplitude)**，$$\lvert c_i\rvert^2$$ 称为对应的**概率 (probability)**。

**定理 3.11（期望是谱上的加权平均）**。设 $$c_i=\langle e_i\vert\psi\rangle$$、$$\lvert\psi\rangle$$ 归一。则

$$\langle\hat A\rangle:=\langle\psi\vert\hat A\psi\rangle=\sum_i\lvert c_i\rvert^2\lambda_i,$$

即观测 $$\hat A$$ 的期望等于各本征值按概率 $$\lvert c_i\rvert^2$$ 的加权平均；且 $$\sum_i\lvert c_i\rvert^2=1$$。

*证明*：先算 $$A\psi$$ 的展开。由定义的展开式与线性性，$$\hat A\lvert\psi\rangle=\hat A\sum_ic_i\lvert e_i\rangle=\sum_ic_i\hat A\lvert e_i\rangle=\sum_ic_i\lambda_i\lvert e_i\rangle$$（这一步用的是"$$\lvert e_i\rangle$$ 是特征向量"）。再与 $$\langle\psi\rvert$$ 配对：

$$\langle\psi\vert\hat A\psi\rangle=\Bigl\langle\sum_jc_j e_j\Big\vert\sum_ic_i\lambda_ie_i\Bigr\rangle=\sum_{i,j}\bar c_jc_i\lambda_i\langle e_j\verte_i\rangle=\sum_{i,j}\bar c_jc_i\lambda_i\delta_{ji}=\sum_i\lvert c_i\rvert^2\lambda_i,$$

第三式用了基的正交归一性。归一化 $$\sum_i\lvert c_i\rvert^2=1$$ 是把上式中的 $$\hat A$$ 换成恒等算子 $$I$$（取全部 $$\lambda_i=1$$）后由 $$\langle\psi\vert\psi\rangle=1$$ 得到，也可以用展开式与正交归一性直接算：

$$\langle\psi\vert\psi\rangle=\sum_{i,j}\bar c_jc_i\langle e_j\verte_i\rangle=\sum_i\lvert c_i\rvert^2 .$$

$$\blacksquare$$

**统计诠释**。定理 3.11 让"概率幅"的物理含义落地：测量可观测量 $$\hat A$$ 时，仪器只会吐出某一个本征值 $$\lambda_i$$（因为 (c) 保证它是实数，可以读），吐出任一个的**相对频率**由 $$\lvert c_i\rvert^2$$ 给出，并且测量一旦发生，系统状态就跳到对应的 $$\lvert e_i\rangle$$。请把这条与经典那侧并排看：经典中状态 $$(q,p)$$ 是"已知的"，可观测量 $$A(q,p)$$ 一旦状态给定就完全确定；量子中状态 $$\lvert\psi\rangle$$ 至多给出各读数的一个**分布**。经典里那个"函数—状态—读数"的三段式，在量子侧被拆成了"态（决定分布）+ 自伴算子（决定可能的读数）"这两段。

### 3.12 三角函数系：Fourier 级数的基

现在回到入口题 (b) 里"保持特征函数不变"这句话——那批单色波在量子力学里有个正式的名字：**动量本征函数**。本节把原专栏 MP41 的 Fourier 分析补完，因为它是 3.14 那把"位置 ↔ 动量"的桥。先把 $$\mathbb{Z}$$ 上的基写清楚。

**定理 3.12（三角函数系是正交归一基）**。在 $$L^2[0,2\pi]\langle\cdot,\cdot\rangle$$ 上，对每个 $$k\in\mathbb{Z}$$ 记

$$\varphi_k(x)=\frac{e^{ikx}}{\sqrt{2\pi}},\qquad x\in[0,2\pi].$$

则 $$\langle\varphi_m,\varphi_n\rangle=\delta_{mn}$$；并且 $$\{\varphi_k\}_{k\in\mathbb{Z}}$$ 在 $$L^2[0,2\pi]$$ 中完备（即构成正交归一基）。

*证明*：正交性是一次直接积分：

$$\langle\varphi_m\vert\varphi_n\rangle=\int_0^{2\pi}\overline{\varphi_m(x)}\varphi_n(x)\,dx
=\frac{1}{2\pi}\int_0^{2\pi}e^{-imx}e^{inx}dx=\frac{1}{2\pi}\int_0^{2\pi}e^{i(n-m)x}dx .$$

当 $$n=m$$，被积函数为 $$1$$，积分得 $$2\pi$$，故 $$\langle\varphi_m,\varphi_m\rangle=1$$。当 $$n\ne m$$，记 $$\ell=n-m\in\mathbb{Z}\setminus\{0\}$$，

$$\int_0^{2\pi}e^{i\ell x}dx=\Bigl[\frac{e^{i\ell x}}{i\ell}\Bigr]_0^{2\pi}=\frac{e^{2\pi i\ell}-1}{i\ell}=\frac{1-1}{i\ell}=0,$$

最后一步用了 $$e^{2\pi i\ell}=1$$。故 $$\langle\varphi_m,\varphi_n\rangle=\delta_{mn}$$。

完备性是 Fourier 级数理论的标准定理（三角多项式在 $$L^2[0,2\pi]$$ 中稠密，而稠密集的正交补为零）。本章后面（3.14、3.15）会看到它**为什么在此刻至关重要**：算子的本征态展开（定义 3.11）要成立，前提恰恰是"本征函数构成一组基"——而这件事在无限维里并不自动成立。$$\blacksquare$$

### 3.13 Fourier 系数

**定理 3.13（Fourier 系数 = 内积）**。设 $$f\in L^2[0,2\pi]$$，$$\{\varphi_k\}$$ 如定理 3.12。记

$$c_k=\langle f\vert\varphi_k\rangle=\int_0^{2\pi}\overline{\varphi_k(x)}f(x)\,dx=\frac{1}{\sqrt{2\pi}}\int_0^{2\pi}e^{-ikx}f(x)\,dx .$$

则 $$c_k$$ 是 $$f$$ 关于基 $$\{\varphi_k\}$$ 的系数，即

$$f=\sum_{k\in\mathbb{Z}}c_k\varphi_k\qquad(\text{在 }L^2\text{ 意义下成立}),$$

并且这是最小二乘意义下唯一的最佳逼近系数。

*证明*：先说明 $$c_k$$ 必然是系数。设 $$f=\sum_kd_k\varphi_k$$，两边与 $$\varphi_m$$ 取内积，用正交归一性：

$$\langle\varphi_m\vertf\rangle=\sum_kd_k\langle\varphi_m\vert\varphi_k\rangle=\sum_kd_k\delta_{mk}=d_m,$$

故 $$d_m=\langle\varphi_m\vertf\rangle=c_m$$。唯一性得证。

再说明取 $$c_k$$ 时确实收敛到 $$f$$。令余项 $$r_N=f-\sum_{\lvert k\rvert\le N}c_k\varphi_k$$。对任一 $$\lvert m\rvert\le N$$，

$$\langle\varphi_m\vertr_N\rangle=\langle\varphi_m\vertf\rangle-\sum_{\lvert k\rvert\le N}c_k\langle\varphi_m\vert\varphi_k\rangle=c_m-c_m=0 .$$

于是 $$r_N$$ 与一切 $$\lvert k\rvert\le N$$ 的 $$\varphi_k$$ 正交；又因为 $$\sum_{\lvert k\rvert\le N}c_k\varphi_k$$ 落在 $$\mathrm{span}\{\varphi_k:\lvert k\rvert\le N\}$$ 中，$$\lVert r_N\rVert$$ 是这个有限维子空间到 $$f$$ 的**最小**距离（勾股定理：$$\lVert f\rVert^2=\lVert\text{投影}\rVert^2+\lVert r_N\rVert^2$$），故 $$\{c_k\}$$ 是最佳逼近系数。由定理 3.12 的完备性，$$\lVert r_N\rVert\to0$$，故级数在 $$L^2$$ 中收敛到 $$f$$。$$\blacksquare$$

### 3.14 Fourier 变换与位置—动量对偶

**定义 3.14（Fourier 变换, Fourier transform）**。把定理 3.13 里的指标集合 $$\mathbb{Z}$$ 连续化到 $$\mathbb{R}$$：对 $$f\in L^2(\mathbb{R})$$（或 Schwartz 函数，此时积分与边界项都无虞）定义

$$\hat f(\lambda)=(\mathcal F f)(\lambda)=\frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}}e^{-ix\lambda}f(x)\,dx,\qquad
\mathcal F^{-1}g(x)=\frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}}e^{ix\lambda}g(\lambda)\,d\lambda .$$

$$\mathcal F$$ 称为 **Fourier 变换**，$$\mathcal F^{-1}$$ 是它的逆（Plancherel 定理保证 $$\mathcal F$$ 是 $$L^2(\mathbb{R})$$ 上的酉算子，故 $$\mathcal F^{-1}=\mathcal F^{*}$$）。

**定理 3.14（Fourier 变换交换位置与动量）**。在 Schwartz 函数上，记 $$M_\lambda$$ 为"乘 $$\lambda$$"算子：$$(M_\lambda g)(\lambda)=\lambda g(\lambda)$$，并记 $$P_\lambda=-i\hbar\dfrac{d}{d\lambda}$$（把定义 3.5 里的 $$x$$ 换成 $$\lambda$$）。则

$$\mathcal F\,P\,\mathcal F^{-1}=\hbar\,M_\lambda,\qquad
\mathcal F\,X\,\mathcal F^{-1}=-\frac{1}{\hbar}P_\lambda .$$

也就是说：**Fourier 变换把"位置算子"与"动量算子"互换**（各差一个常数因子）。

*证明*：两条都用分部积分或直接对积分号求导。

先算第一条。对 Schwartz 函数 $$f$$，

$$\mathcal F(Pf)(\lambda)=\frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}}e^{-ix\lambda}\bigl(-i\hbar f'(x)\bigr)\,dx
=-i\hbar\cdot\frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}}e^{-ix\lambda}f'(x)\,dx .$$

对里面的积分分部积分（$$f$$ 是 Schwartz 函数，边界项 $$[e^{-ix\lambda}f]_{-\infty}^{\infty}=0$$）：

$$\int_{\mathbb{R}}e^{-ix\lambda}f'(x)\,dx=\underbrace{\bigl[e^{-ix\lambda}f(x)\bigr]_{-\infty}^{\infty}}_{=0}+i\lambda\int_{\mathbb{R}}e^{-ix\lambda}f(x)\,dx=i\lambda\sqrt{2\pi}\,\hat f(\lambda).$$

代回得 $$\mathcal F(Pf)(\lambda)=-i\hbar\cdot i\lambda\hat f(\lambda)=\hbar\lambda\hat f(\lambda)=(\hbar M_\lambda\mathcal F f)(\lambda)$$，即 $$\mathcal F P\mathcal F^{-1}=\hbar M_\lambda$$。

再算第二条。直接对 $$\hat f$$ 的定义式在积分号下对 $$\lambda$$ 求导：

$$\frac{d}{d\lambda}\hat f(\lambda)=\frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}}(-ix)e^{-ix\lambda}f(x)\,dx=-i\cdot\frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}}e^{-ix\lambda}\bigl(xf(x)\bigr)\,dx=-i\,\mathcal F(Xf)(\lambda).$$

于是 $$\mathcal F(Xf)=\frac{1}{-i}\dfrac{d}{d\lambda}\hat f=i\dfrac{d}{d\lambda}\hat f$$，写成算子形式即 $$\mathcal F X\mathcal F^{-1}=i\dfrac{d}{d\lambda}$$。而 $$i\dfrac{d}{d\lambda}=i\cdot\dfrac{P_\lambda}{-i\hbar}\cdot(-1)\cdot(-1)$$；更直接地，由 $$P_\lambda=-i\hbar\dfrac{d}{d\lambda}$$ 解出 $$\dfrac{d}{d\lambda}=\dfrac{i}{\hbar}P_\lambda$$，故

$$i\frac{d}{d\lambda}=i\cdot\frac{i}{\hbar}P_\lambda=-\frac{1}{\hbar}P_\lambda .$$

第二条证完。$$\blacksquare$$

**这条定理是本章的几何与物理枢纽**，值得单独说一句：位置算子 $$X$$ 在"位置表象"里是乘 $$x$$，在"动量表象"（即 $$\lambda$$ 所在的频率空间）里却变成了求导；动量算子 $$P$$ 恰好相反。所以"位置表象"与"动量表象"不是两种理论，而是同一个 Hilbert 空间上的两个坐标选择，中间由 $$\mathcal F$$ 这个酉算子联系。深一层的名字是调和分析里的 **Pontryagin 对偶 (Pontryagin duality)**：它把 Fourier 分析推广到局部紧 Abel 群上，$$\mathbb{R}$$ 与 $$\mathbb{Z}$$、$$\mathbb{R}$$ 与 $$\mathbb{R}$$ 的三种 Fourier 形式（级数、变换、离散—它是同一个对偶的不同显影）是同一个定理的不同化身。

### 3.15 算子的性质：无界、稠定、对称、本质自伴

最后把 3.10 留下的那句"自伴性要争"补完，这也是原专栏 MP42 结尾那段"大量概念涌现"的正名。

**定理 3.15（位置算子与动量算子的定义域性质）**。设 $$\mathscr H=L^2(\mathbb{R})$$，$$X$$、$$P$$ 如定义 3.5、3.6。则：

- **(a) 两者都无界 (unbounded)**；
- **(b) 两者的自然定义域 $$\mathrm{Dom}(X)=\{\psi\in\mathscr H:\int x^2\lvert\psi\rvert^2dx<\infty\}$$、$$\mathrm{Dom}(P)=\{\psi\in\mathscr H:\psi\text{ 绝对连续},\ \psi'\in\mathscr H\}$$ 都在 $$\mathscr H$$ 中稠密 (densely defined)**；
- **(c) 在各自定义域上两者都对称 (symmetric)**：$$\langle\phi,\hat A\psi\rangle=\langle\hat A\phi,\psi\rangle$$；
- **(d) 两者都本质自伴 (essentially self-adjoint)**：它们在 $$\mathrm{Dom}$$ 上的对称扩张有且只有一个自伴扩张。

*证明* (a) 无界性给两个具体的反例就够——"无界"的意思正是"算子范数不是有限数"，所以只要造出一列 $$\psi_n$$，使 $$\lVert\hat A\psi_n\rVert/\lVert\psi_n\rVert\to\infty$$。

对 $$X$$：取 $$\psi_n(x)=\dfrac{1}{x}$$ 在 $$[1,n]$$ 上、$$0$$ 在别处。则

$$\lVert\psi_n\rVert^2=\int_1^n\frac{dx}{x^2}=1-\frac{1}{n}<1,\qquad
\lVert X\psi_n\rVert^2=\int_1^n x^2\cdot\frac{1}{x^2}\,dx=n-1 .$$

于是 $$\lVert X\psi_n\rVert/\lVert\psi_n\rVert\ge\sqrt{n-1}\to\infty$$；取归一化后的 $$\psi_n/\lVert\psi_n\rVert$$ 即得所需。直观上：$$X$$ 是一个"乘无界函数"的算子，乘子越大越能把 $$L^2$$ 函数推出 $$L^2$$。

对 $$P$$：直接用它的本征函数。在环的情形（定理 3.4），$$\psi_k=e^{ikx}$$ 满足 $$\lVert\psi_k\rVert^2=2\pi$$ 而 $$P\psi_k=\hbar k\psi_k$$，故

$$\frac{\lVert P\psi_k\rVert}{\lVert\psi_k\rVert}=\hbar\lvert k\rvert\xrightarrow{\ \lvert k\rvert\to\infty\ }\infty .$$

同一个论证搬到 $$\mathbb{R}$$ 上照样成立（用截断的单色波）。$$\blacksquare$$

*证明* (b)：$$\mathrm{Dom}(X)$$ 包含一切紧支集的 $$C^\infty$$ 函数（在支集上 $$x$$ 有界，故 $$x\psi\in L^2$$），而紧支集光滑函数在 $$L^2$$ 中稠密，所以 $$\mathrm{Dom}(X)$$ 稠密。$$\mathrm{Dom}(P)$$ 含 Schwartz 函数全体 $$\mathcal S(\mathbb{R})$$，它在 $$L^2$$ 中稠密，故 $$\mathrm{Dom}(P)$$ 也稠密。$$\blacksquare$$

*证明* (c)：对称性就是把自伴定义里的"$$\hat A^{*}=\hat A$$"放松成"左右两边各自作用在同一对定义域上"。

对 $$X$$：$$x$$ 是实函数，故

$$\langle\phi,X\psi\rangle=\int\overline{\phi(x)}\,x\psi(x)\,dx=\int\overline{x\phi(x)}\,\psi(x)\,dx=\langle X\phi,\psi\rangle .$$

对 $$P$$：对 $$\phi,\psi\in\mathrm{Dom}(P)$$ 分部积分，

$$\langle\phi,P\psi\rangle=\int\overline{\phi(x)}\bigl(-i\hbar\psi'(x)\bigr)dx=\underbrace{-i\hbar\bigl[\overline{\phi}\,\psi\bigr]_{-\infty}^{\infty}}_{=0}+i\hbar\int\overline{\phi'(x)}\,\psi(x)\,dx
=\int\overline{-i\hbar\phi'(x)}\,\psi(x)\,dx=\langle P\phi,\psi\rangle .$$

边界项为零用到了 $$\phi,\psi\in L^2$$ 与 $$\phi',\psi'\in L^2$$ 给出的无穷远衰减：在 Schwartz 函数类上，$$x\to\pm\infty$$ 时 $$\overline{\phi}\psi$$ 衰减快于任何多项式，故 $$\bigl[\overline{\phi}\psi\bigr]_{-\infty}^{\infty}=0$$。所以两者都对称。$$\blacksquare$$

*证明* (d)：这是本节唯一需要搬外部定理的一条，我们只给出可核验的路径而不假装它是初等的。称一个对称算子 $$\hat A$$ 在稠定子空间 $$D$$ 上**本质自伴**，若 $$\hat A$$ 在 $$D$$ 上的对称扩张唯一。判别准则是**亏指数 (deficiency indices)**：$$n_\pm=\dim\ker(\hat A^{*}\mp i)$$，本质自伴 $$\Longleftrightarrow n_+=n_-=0$$。

对 $$P$$：$$\ker(P^{*}-i)$$ 中的元素是方程 $$-i\hbar\psi'=i\psi$$ 的 $$L^2$$ 解，即 $$\psi'=-\psi/\hbar$$，故 $$\psi(x)=Ce^{-x/\hbar}$$；它在 $$x\le0$$ 一侧不平方可积，被排除，故 $$n_+=0$$；同理 $$n_-=0$$。对 $$X$$：$$\ker(X^{*}\mp i)$$ 中元素满足 $$(x\mp i)\psi=0$$，即 $$\psi$$ 只在 $$x=\pm i\notin\mathbb{R}$$ 处可能非零；但 $$\pm i$$ 不是实数，故 $$\psi=0$$，$$n_\pm=0$$。

（完整的亏指数判定与自伴扩张的分类见第 38 章；这里我们只用到"$$\mathcal S$$ 是 $$\mathrm{Dom}$$ 的子集且是核 (core)"这一条，它使 $$P,X$$ 被 $$\mathbb{R}$$ 上的实参数唯一确定。）$$\blacksquare$$

**为什么这一段不是技术洁癖**。把 (a) 与定义 3.11 并排读：定义 3.11 里那个漂亮的展开 $$\lvert\psi\rangle=\sum_i c_i\lvert e_i\rangle$$ 假设了"本征向量构成一组基"。可是 (a) 说 $$X$$、$$P$$ 是无界的；更具体地说，动量算子在 $$\mathbb{R}$$ 上的"特征函数" $$e^{ikx}$$ 根本不属于 $$L^2(\mathbb{R})$$（$$\int\lvert e^{ikx}\rvert^2dx=\infty$$）！所以 $$P$$ 在 $$\mathbb{R}$$ 上**没有**一个平方可积的本征函数。这正是无限维与有限维的分水岭：有限维里"自伴 = 可对角化"是天经地义，无限维里必须把求和升级成对**投影算子值测度 (projection-valued measure, p.v.m.)** 的积分

$$\hat A=\int_{\sigma(\hat A)}\lambda\,dE(\lambda),$$

用谱投影代替本征投影、用积分代替求和。$$e^{ikx}$$ 这类"广义本征函数"由此获得严格的地位（它们生成的是连续谱的谱测度）。这条升级是本课程卷三后半的主线，也是第 38 章（谱定理与投影算子值测度）与第 42 章（无界算子与 Cayley 变换）的主题。第 34 章先走一步：它不去纠缠定义域，而是直接把这些算子组装成一条演化方程。

## 四、几何与物理直觉 (Intuition)

**几何：括号是"沿着流求导"。** 在相空间上，一个函数 $$G$$ 不仅是一个数，它还生成一个**向量场**

$$X_G=\sum_i\Bigl(\frac{\partial G}{\partial p_i}\frac{\partial}{\partial q^i}-\frac{\partial G}{\partial q^i}\frac{\partial}{\partial p_i}\Bigr),$$

当 $$G=H$$ 时它的积分曲线就是 Hamilton 方程的运动轨迹。把定义 3.2 与这个向量场对照，会发现

$$\{F,G\}=X_G(F),$$

也就是说：**Poisson 括号 $$\{F,G\}$$ 就是"沿 $$G$$ 生成的流，对 $$F$$ 求方向导数"**。这条读法把定理 3.3（$$dA/dt=\{H,A\}$$）解释成一句几何话：时间演化就是沿 Hamilton 向量场 $$X_H$$ 的流。

有了这条读法，定理 3.8 (iv) 的 Jacobi 恒等式就有了形状：两个向量场的**流的交换子** $$[X_F,X_G]$$ 一般不为零，而 Jacobi 恒等式说的正是"先沿 $$F$$ 的流、再沿 $$G$$ 的流，与反过来的次序，两者的差仍然是一个 Hamilton 流"。Lie 括号的引入（第 54 章）会把这句话写成一行：对应 $$F\mapsto X_F$$ 是 Lie 代数同态。**量子化保住的就是这个同态结构**——只不过流换成了算子、交换子换成了 $$[\,,\,]$$。

**$$[X,P]=i\hbar$$ 的几何读法。** 作为一个算子，$$[X,P]$$ 就是"乘以 $$i\hbar$$"。把 $$i=e^{i\pi/2}$$ 认出来，这条式子说的是：位置与动量这两个操作交换失败留下的余量，是**在每个点上把波函数的值旋转 $$\pi/2$$、再按 $$\hbar$$ 缩放**。它既不是零（那意味着两个量可以同时确定），也不是实数（那意味着它不是自伴算子）；它恰好是"一个纯虚数倍恒等"——这正是 3.9 第一步算出的、保括号对应所允许的唯一形状。

**物理：为什么"对易" = "可同时测量"。** 定理 3.7 说 $$[X,P]\ne0$$。若 $$X$$ 与 $$P$$ 有公共本征向量 $$\lvert e\rangle$$，即 $$X\lvert e\rangle=x\lvert e\rangle$$、$$P\lvert e\rangle=p\lvert e\rangle$$，那么

$$i\hbar\lvert e\rangle=(XP-PX)\lvert e\rangle=(xp-px)\lvert e\rangle=0,$$

与 $$\lvert e\rangle\ne0$$ 矛盾（例题 5.3 会把这个论证写全）。所以**不存在"位置与动量同时取确定值"的量子态**——这是不确定关系的最初形态。定量的版本（Robertson 不等式）

$$\Delta\hat A\cdot\Delta\hat B\ge\frac{1}{2}\bigl\lvert\langle[\hat A,\hat B]\rangle\bigr\rvert$$

会在卷三的算子谱章节（第 36 章起）给出，届时 $$[X,P]=i\hbar$$ 立刻给出 $$\Delta x\,\Delta p\ge\hbar/2$$。本章只需记住：**不确定性的来源就是那条不为零的括号**。

**Fourier 对偶的几何。** 定理 3.14 说 $$\mathcal F$$ 把 $$X$$ 换成（几乎）$$P$$、把 $$P$$ 换成 $$X$$。所以"位置表象"与"动量表象"不是两个理论，而是同一个 Hilbert 空间上的两种坐标；$$\mathcal F$$ 是它们之间的酉变换。这条对偶在抽象调和分析里的名字是 Pontryagin 对偶，它的三种面孔——$$\mathbb{R}$$ 上的 Fourier 变换、$$\mathbb{Z}$$ 上的 Fourier 级数、有限循环群上的离散 Fourier 变换——是同一个定理（第 34 章的波包展开与第 44 章的 Stone–von Neumann 定理都会用到它）。

**三线合一。** 本章的主线可以压成一张表：

| 几何 | 物理 | 代数 |
|---|---|---|
| 余切丛 $$T^*M$$ 上的辛形式 $$\omega=dq\wedge dp$$ | 相空间、共轭变量 | Poisson 括号 $$\{,\}$$，满足 Jacobi |
| 保辛结构的（无穷小）变换 | 时间演化、守恒量 | 与 $$H$$ 的括号生成演化 |
| 复 Hilbert 空间上的酉变换 | 量子态、可观测量的读数分布 | 对易子 $$\frac{1}{i\hbar}[\,,\,]$$，满足 Jacobi |
| Fourier 变换（群对偶） | 位置表象 ↔ 动量表象 | $$\mathcal F X\mathcal F^{-1}\sim P$$ |

四行里前三行的第三列是同一个代数结构；第四行是它最具体的一次显影。整章无非是把第一行推到第三行，再看清被推的到底是什么。

## 五、经典问题精讲 (Classical Problems)

**例题 5.1（Gauss 波包的不确定度乘积）。** 设归一化波函数

$$\psi(x)=\Bigl(\frac{1}{\pi\sigma^2}\Bigr)^{1/4}e^{-x^2/(2\sigma^2)},\qquad \sigma>0 .$$

求 $$\langle X\rangle,\ \langle P\rangle,\ \langle X^2\rangle,\ \langle P^2\rangle$$，以及不确定度 $$\Delta x=\sqrt{\langle X^2\rangle-\langle X\rangle^2}$$、$$\Delta p=\sqrt{\langle P^2\rangle-\langle P\rangle^2}$$ 的乘积。

*考点*：定义 3.5、3.6 与定理 3.6 的高阶矩；定理 3.7 的非零对易子是乘积下界 $$\hbar/2$$ 的来源。*位置*：把 3.11 的统计诠释第一次落到具体计算上。

*解*：记 $$c=(\pi\sigma^2)^{-1/4}$$，$$\lvert\psi(x)\rvert^2=c^2e^{-x^2/\sigma^2}$$。

**一阶矩**。被积函数 $$x\lvert\psi(x)\rvert^2$$ 与 $$\overline{\psi}\,\psi'$$ 的实部都是**奇函数**（$$x\lvert\psi\rvert^2$$ 奇；$$P\psi=-\tfrac{i\hbar}{\ }$$ 亦有 $$\overline{\psi}\psi'=-\tfrac{x}{\sigma^2}\lvert\psi\rvert^2$$ 为奇），故

$$\langle X\rangle=\int x\lvert\psi\rvert^2dx=0,\qquad \langle P\rangle=-i\hbar\int\overline{\psi}\psi'dx=-i\hbar\int-\frac{x}{\sigma^2}\lvert\psi\rvert^2dx=0 .$$

**二阶矩**。$$\lvert\psi\rvert^2$$ 是均值为 $$0$$、方差 $$\sigma^2/2$$ 的 Gauss 密度，故

$$\langle X^2\rangle=\int x^2\lvert\psi\rvert^2dx=\frac{\sigma^2}{2}.$$

对 $$P$$ 用 $$P$$ 的自伴性把二阶矩写成导数模方（这一步是 3.15 (c) 对称性的用处）：

$$\langle P^2\rangle=\langle P\psi\vert P\psi\rangle=\hbar^2\int\lvert\psi'\rvert^2dx=\hbar^2\int\frac{x^2}{\sigma^4}\lvert\psi\rvert^2dx=\frac{\hbar^2}{\sigma^4}\langle X^2\rangle=\frac{\hbar^2}{2\sigma^2}.$$

**结论**：

$$\Delta x=\frac{\sigma}{\sqrt2},\qquad \Delta p=\frac{\hbar}{\sigma\sqrt2},\qquad
\Delta x\,\Delta p=\frac{\sigma}{\sqrt2}\cdot\frac{\hbar}{\sigma\sqrt2}=\frac{\hbar}{2}.$$

$$\blacksquare$$

Gauss 波包把 $$\Delta x\Delta p\ge\hbar/2$$ 取成了等号，它是"最小不确定态"。注意 $$\sigma$$ 未定：$$X$$ 与 $$P$$ 的不确定度此消彼长，但乘积恒为 $$\hbar/2$$——这个不变量正来自 $$[X,P]=i\hbar$$。

**例题 5.2（Leibniz 律的迭代与位移算子）。** 设 $$P=-i\hbar\dfrac{d}{dx}$$，$$X$$ 是位置算子。

(i) 证明对一切 $$n\ge1$$：$$[X,P^n]=i\hbar\,n\,P^{n-1}$$。
(ii) 由此（形式地在幂级数意义下）证明 $$[X,e^{i\lambda P/\hbar}]=-\lambda\,e^{i\lambda P/\hbar}$$，$$\lambda\in\mathbb{R}$$。
(iii) 证明 $$(e^{-i\lambda P/\hbar}\psi)(x)=\psi(x-\lambda)$$，并解释 $$P$$ 是位移的生成元。

*考点*：定理 3.8 (iii) 的 Leibniz 律——它是本课里最常被使用的一条对易子公式。*位置*：把 $$[X,P]=i\hbar$$ 从"一对算子"升级成"一整个函数演算"。

*解*：

**(i)** 先把定理 3.8 (iii) 换成中间变量的形式。对 (iii) 用反对称性：

$$[A,BC]=-[BC,A]=-\bigl(B[C,A]+[B,A]C\bigr)=[A,B]C+B[A,C].$$

现在对 $$n$$ 作归纳。$$n=1$$ 是定理 3.7。设 $$[X,P^{n-1}]=i\hbar(n-1)P^{n-2}$$，则把 $$B=P$$、$$C=P^{n-1}$$、$$A=X$$ 代入上式：

$$[X,P^n]=[X,P]P^{n-1}+P\,[X,P^{n-1}]=i\hbar\,P^{n-1}+P\cdot i\hbar(n-1)P^{n-2}=i\hbar\,n\,P^{n-1},$$

最后一步用了 $$P\cdot P^{n-2}=P^{n-1}$$。归纳完成。

**(ii)** 把指数按幂级数展开 $$e^{i\lambda P/\hbar}=\sum_{n\ge0}\frac{1}{n!}\Bigl(\frac{i\lambda}{\hbar}\Bigr)^nP^n$$（$$P$$ 是形式变量，这一步按幂级数形式进行）。用 (i) 与对易子的线性（定理 3.8 (i)）：

$$[X,e^{i\lambda P/\hbar}]=\sum_{n\ge1}\frac{1}{n!}\Bigl(\frac{i\lambda}{\hbar}\Bigr)^n[X,P^n]
=\sum_{n\ge1}\frac{1}{n!}\Bigl(\frac{i\lambda}{\hbar}\Bigr)^ni\hbar\,n\,P^{n-1}.$$

把 $$\dfrac{n}{n!}=\dfrac{1}{(n-1)!}$$ 与因子拆开：

$$i\hbar\cdot\frac{i\lambda}{\hbar}\sum_{n\ge1}\frac{1}{(n-1)!}\Bigl(\frac{i\lambda}{\hbar}\Bigr)^{n-1}P^{n-1}=-\lambda\sum_{m\ge0}\frac{1}{m!}\Bigl(\frac{i\lambda}{\hbar}\Bigr)^{m}P^{m}=-\lambda\,e^{i\lambda P/\hbar}.$$

**(iii)** 把 $$e^{-i\lambda P/\hbar}=\sum_m\frac{1}{m!}\Bigl(-\frac{i\lambda}{\hbar}\Bigr)^mP^m$$ 作用在 $$\psi$$ 上。注意 $$P^m=(-i\hbar)^m\dfrac{d^m}{dx^m}$$，故

$$\Bigl(-\frac{i\lambda}{\hbar}\Bigr)^mP^m=\Bigl(-\frac{i\lambda}{\hbar}\Bigr)^m(-i\hbar)^m\frac{d^m}{dx^m}
=\Bigl(\frac{(-i\lambda)(-i\hbar)}{\hbar}\Bigr)^m\frac{d^m}{dx^m}=(-\lambda)^m\frac{d^m}{dx^m}.$$

于是 $$e^{-i\lambda P/\hbar}=\sum_m\frac{(-\lambda)^m}{m!}\frac{d^m}{dx^m}$$，作用在解析的 $$\psi$$ 上正好是 Taylor 展开：

$$(e^{-i\lambda P/\hbar}\psi)(x)=\sum_m\frac{(-\lambda)^m}{m!}\psi^{(m)}(x)=\psi(x-\lambda).$$

$$\blacksquare$$

位移算子 $$T_\lambda=e^{-i\lambda P/\hbar}$$ 满足 $$T_\lambda\psi(x)=\psi(x-\lambda)$$，而 (ii) 是一个"无穷小"版本。整条链是：动量算符是**位移的无穷小生成元**。它与位置的直觉相容：把 (ii) 中的 $$\lambda$$ 换成 $$-\mu$$，得 $$[X,T_\mu]=\mu T_\mu$$，即 $$XT_\mu-T_\mu X=\mu T_\mu$$；左乘 $$T_\mu^{-1}$$ 得

$$T_\mu^{-1}XT_\mu=X+\mu I .$$

这正是"$$X$$ 被 $$T_\mu$$ 平移了 $$\mu$$"的算子形式——也是 $$[X,P]=i\hbar$$ 在指数层面的样子。

**例题 5.3（不存在位置与动量同时确定的状态）。** 证明：若 $$\lvert e\rangle\ne0$$ 同时是 $$X$$ 与 $$P$$ 的本征向量，则导出矛盾；特别地，入口题 (c) 里那对算子没有公共本征函数。

*考点*：定理 3.7 的"非零"如何直接产生物理限制。*位置*：3.11 的统计诠释需要"可同时对角化"，例题给出它失效的原因。

*解*：设 $$X\lvert e\rangle=x_0\lvert e\rangle$$、$$P\lvert e\rangle=p_0\lvert e\rangle$$（$$x_0,p_0\in\mathbb{R}$$，由定理 3.10 (c)）。用定理 3.7 作用在 $$\lvert e\rangle$$ 上：

$$i\hbar\lvert e\rangle=(XP-PX)\lvert e\rangle=XP\lvert e\rangle-PX\lvert e\rangle=x_0p_0\lvert e\rangle-p_0x_0\lvert e\rangle=0 .$$

这里用了两件事：$$X,P$$ 是线性算子（可以把标量提出来），以及两个标量 $$x_0,p_0$$ 相乘可交换。于是 $$i\hbar\lvert e\rangle=0$$。因为 $$\hbar>0$$ 是数、$$\lvert e\rangle\ne0$$，两边不可能相等（$$i\hbar\ne0$$）。矛盾。$$\blacksquare$$

关键 leap 在于**看出矛盾只需比较"同一向量的两种标量倍"**：$$[X,P]\lvert e\rangle=i\hbar\lvert e\rangle$$，而共同本征性要求它等于 $$0$$。整章之所以要算 $$[X,P]$$，就是为了得到这个 $$\lvert e\rangle$$ 前的非零系数。

**例题 5.4（Fourier 变换交换位置与动量：在一个具体函数上验证）。** 取 $$\psi(x)=e^{-x^2/2}$$（它是 $$\mathcal F$$ 的不动点：$$\hat\psi(\lambda)=e^{-\lambda^2/2}$$，见下面的验证）。在 $$\psi$$ 上直接验证定理 3.14 的两条等式

$$\mathcal F X\mathcal F^{-1}=i\frac{d}{d\lambda},\qquad \mathcal F P\mathcal F^{-1}=\hbar M_\lambda .$$

*考点*：定理 3.13 的 Fourier 系数公式与定理 3.14 的算子交换关系。*位置*：把"位置 ↔ 动量"由口号变成一次可核对的等式。

*解*：先确认不动点。用 $$\int_{\mathbb{R}}e^{-x^2/2}e^{-ix\lambda}dx=\sqrt{2\pi}e^{-\lambda^2/2}$$（配方 $$x^2/2+ix\lambda=(x+i\lambda)^2/2+\lambda^2/2$$ 并平移围道），故

$$\hat\psi(\lambda)=\frac{1}{\sqrt{2\pi}}\cdot\sqrt{2\pi}e^{-\lambda^2/2}=e^{-\lambda^2/2}=\psi(\lambda).$$

**第一条 $$\mathcal F X\mathcal F^{-1}=i\dfrac{d}{d\lambda}$$。** 等式是说：对任意 $$g$$，把 $$X\mathcal F^{-1}g$$ 再作 Fourier 变换，结果等于 $$i\dfrac{d}{d\lambda}g$$。取 $$g=\psi$$，则 $$\mathcal F^{-1}\psi=\psi$$（不动点对逆变换同样成立），再乘 $$x$$：

$$X\psi=xe^{-x^2/2}=-\frac{d}{dx}e^{-x^2/2},$$

最后一步因为 $$\dfrac{d}{dx}e^{-x^2/2}=-xe^{-x^2/2}$$。对它作 Fourier 变换（$$e^{-x^2/2}$$ 是 Schwartz 函数，分部积分时边界项为零）：

$$\mathcal F\bigl(X\psi\bigr)(\lambda)=-\frac{1}{\sqrt{2\pi}}\int\frac{d}{dx}\bigl(e^{-x^2/2}\bigr)e^{-ix\lambda}dx
=-\frac{1}{\sqrt{2\pi}}\cdot i\lambda\int e^{-x^2/2}e^{-ix\lambda}dx=-i\lambda\,e^{-\lambda^2/2},$$

其中用了分部积分 $$\int u'v\,dx=-\int uv'\,dx$$，取 $$u=e^{-x^2/2}$$、$$v=e^{-ix\lambda}$$（故 $$v'=-i\lambda e^{-ix\lambda}$$），边界项为零；最后一步用了 $$\mathcal F\psi=\psi$$。另一方面，右端作用在同一个 $$g=\psi$$ 上：

$$i\frac{d}{d\lambda}\psi(\lambda)=i\frac{d}{d\lambda}e^{-\lambda^2/2}=-i\lambda\,e^{-\lambda^2/2}.$$

两边逐项相等（同为 $$-i\lambda e^{-\lambda^2/2}$$），第一条验证通过。

**第二条 $$\mathcal F P\mathcal F^{-1}=\hbar M_\lambda$$。** 输入仍是 $$g=\psi$$，先算 $$P\psi$$：

$$P\psi=-i\hbar\frac{d}{dx}e^{-x^2/2}=i\hbar\,x\,e^{-x^2/2}.$$

再用第一条里同一个分部积分结果（即 $$\mathcal F\bigl(xe^{-x^2/2}\bigr)=-i\lambda e^{-\lambda^2/2}$$，见上式）：

$$\mathcal F(P\psi)(\lambda)=i\hbar\cdot\bigl(-i\lambda\bigr)e^{-\lambda^2/2}=\hbar\lambda\,e^{-\lambda^2/2}.$$

右端作用在同一个 $$g=\psi$$ 上：$$\hbar M_\lambda\psi=\hbar\lambda\,e^{-\lambda^2/2}$$。**逐项相等**，第二条验证通过。$$\blacksquare$$

这道题的价值不在数值，而在示范一件事：**算子恒等式必须在一个固定的函数空间约定下、让两边作用在同一个函数上验证**。$$\mathcal F$$ 的方向（$$\mathcal F X=i\frac{d}{d\lambda}\mathcal F$$ 而不是 $$\mathcal F X=\mathcal F\,i\frac{d}{d\lambda}$$）决定了结果；一旦次序或符号弄错，等式会"看起来不成立"。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 由定义 3.7 出发，直接验证对易子的双线性与反对称；再计算 $$[X,P]$$ 作用在 $$\psi(x)=x^2e^{-x^2}$$ 上的结果。

**基2.** 设 $$\hat A=\hat A^{*}$$。证明 $$\hat A^2$$ 也自伴；并说明 $$i\hat A$$ 不自伴（它是反自伴的）。

**基3.** 在 $$L^2[0,2\pi]$$ 上计算 $$\langle\varphi_{-1}\vert\varphi_1\rangle$$ 与 $$\langle\varphi_1\vert\varphi_1\rangle$$，并用定理 3.13 求 $$f(x)=\cos x$$ 的 Fourier 系数 $$c_1,c_{-1}$$。

**基4.** 设 $$f_\sigma(x)=e^{-x^{2}/(2\sigma^{2})}$$，$$\sigma>0$$。

(i) 由配方

$$\frac{x^{2}}{2\sigma^{2}}+ix\lambda=\frac{1}{2\sigma^{2}}\bigl(x+i\sigma^{2}\lambda\bigr)^{2}+\frac{\sigma^{2}\lambda^{2}}{2}$$

算出它的 Fourier 变换 $$\hat f_\sigma=\mathcal F f_\sigma$$（例题 5.4 算的是 $$\sigma=1$$ 的退化情形，这里要求一般 $$\sigma$$ 的结果）。

(ii) 用定理 3.14 解释：$$f_\sigma$$ 在位置表象里的"宽度"与在 $$\lambda$$ 表象里的"宽度"为什么互为倒数；并说明这正是例题 5.1 中 $$\Delta x\,\Delta p$$ 与 $$\sigma$$ 无关、恒等于 $$\hbar/2$$ 的来源。

### 竞赛（本课目标难度）

**竞1.** 证明 $$[X,P^n]=i\hbar nP^{n-1}$$；由此证明对任意多项式 $$f$$，$$[X,f(P)]=i\hbar f'(P)$$。

**竞2.** 设 $$\hat H=\dfrac{\hat P^2}{2m}+V(\hat X)$$，Heisenberg 方程为 $$\dfrac{d\hat A}{dt}=\dfrac{i}{\hbar}[\hat H,\hat A]$$。求出 $$\dfrac{d\hat X}{dt}$$、$$\dfrac{d\hat P}{dt}$$，再求它们的期望值方程（Ehrenfest 定理）。

**竞3.** 设 $$X,P$$ 是 $$n\times n$$ 复矩阵且 $$[X,P]=i\hbar I$$。对两边取迹导出矛盾，并说明这对"量子力学活在哪个空间里"意味着什么。

**竞4.** 设 $$\hat A=\hat A^{*}$$，$$\hat A\lvert e_1\rangle=\lambda_1\lvert e_1\rangle$$、$$\hat A\lvert e_2\rangle=\lambda_2\lvert e_2\rangle$$，$$\lambda_1\ne\lambda_2$$。证明 $$\langle e_1\vert e_2\rangle=0$$。若 $$\lambda_1=\lambda_2$$（简并），结论如何变化？

### 研究（通向下一章）

**研1.** 证明位置算子 $$X$$ 无界。再说明：既然 $$X$$ 无界、且 $$e^{ikx}\notin L^2(\mathbb{R})$$，定义 3.11 里那个"本征态求和"为什么在无限维必须升级成对投影算子值测度的积分。

**研2.** 设 $$\hat H=\hat H^{*}$$，$$\hat U(t)=e^{-i\hat Ht/\hbar}$$。证明 $$\hat A(t):=\hat U(t)^{*}\hat A\hat U(t)$$ 满足 Heisenberg 方程 $$\dfrac{d\hat A}{dt}=\dfrac{i}{\hbar}[\hat H,\hat A]$$，且 $$\hat U$$ 是单参数酉群。

### 解答 (Solutions)

**解 基1.** 双线性：由定义 3.7，

$$[\alpha A+\beta B,C]=(\alpha A+\beta B)C-C(\alpha A+\beta B)=\alpha(AC-CA)+\beta(BC-CB)=\alpha[A,C]+\beta[B,C],$$

第二个变量把减法两边各自展开同理。反对称：$$[A,B]=AB-BA=-(BA-AB)=-[B,A]$$；取 $$A=B$$ 得 $$[A,A]=0$$。

计算 $$[X,P]\psi$$：先算两个复合

$$(XP)\psi=X\bigl(-i\hbar\psi'\bigr)=-i\hbar\,x\psi',\qquad (PX)\psi=P(x\psi)=-i\hbar\bigl(\psi+x\psi'\bigr).$$

作差 $$[X,P]\psi=-i\hbar x\psi'+i\hbar\psi+i\hbar x\psi'=i\hbar\psi$$。取 $$\psi=x^2e^{-x^2}$$（光滑、衰减快，落在 3.15 的定义域内）得 $$[X,P]\psi=i\hbar x^2e^{-x^2}$$。**结果与 $$\psi$$ 的形状无关，恒为 $$i\hbar\psi$$**——这正是定理 3.7：$$[X,P]=i\hbar I$$ 是算子等式，不是某个函数的等式。

**解 基2.** 用自伴定义 $$\langle\phi,\hat A\psi\rangle=\langle\hat A\phi,\psi\rangle$$，连用两次：

$$\langle\phi,\hat A^2\psi\rangle=\langle\hat A\phi,\hat A\psi\rangle=\langle\hat A^2\phi,\psi\rangle,$$

故 $$\hat A^2$$ 自伴。

对 $$i\hat A$$：直接算共轭算子，$$(i\hat A)^{*}=\bar i\,\hat A^{*}=-i\hat A=-(i\hat A)$$，故 $$i\hat A$$ 反自伴而非自伴。物理上，反自伴算子的期望值是**纯虚数**（把定理 3.10 (a) 的证明中对 $$\hat A$$ 换成 $$i\hat A$$，得 $$\langle\psi,i\hat A\psi\rangle=-\overline{\langle\psi,i\hat A\psi\rangle}$$），不能当仪器读数。这与 3.9 第一步"系数必须纯虚"是同一件事的两面。

**解 基3.** 由定理 3.12 的正交归一性，$$\langle\varphi_{-1}\vert\varphi_1\rangle=\delta_{-1,1}=0$$，$$\langle\varphi_1\vert\varphi_1\rangle=1$$。

把 $$\cos x$$ 写成基本波：$$\cos x=\dfrac{e^{ix}+e^{-ix}}{2}=\dfrac{\sqrt{2\pi}}{2}\bigl(\varphi_1+\varphi_{-1}\bigr)$$。由定理 3.13 证明里的系数唯一性，$$c_1=c_{-1}=\dfrac{\sqrt{2\pi}}{2}$$。用公式复核：

$$c_1=\frac{1}{\sqrt{2\pi}}\int_0^{2\pi}e^{-ix}\cos x\,dx=\frac{1}{\sqrt{2\pi}}\int_0^{2\pi}\frac{1+e^{-2ix}}{2}dx=\frac{1}{\sqrt{2\pi}}\cdot\pi=\frac{\sqrt{2\pi}}{2},$$

其中 $$\int_0^{2\pi}e^{-2ix}dx=0$$。同理 $$c_{-1}$$ 相同，反映 $$\cos x$$ 是实偶函数（$$c_{-k}=\overline{c_k}$$）。

**解 基4.** (i) 把定义 3.14 与配方合起来用：

$$\hat f_\sigma(\lambda)=\frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}}e^{-ix\lambda}e^{-x^{2}/(2\sigma^{2})}dx
=\frac{1}{\sqrt{2\pi}}\int_{\mathbb{R}}\exp\Bigl(-\frac{x^{2}}{2\sigma^{2}}-ix\lambda\Bigr)dx
=\frac{e^{-\sigma^{2}\lambda^{2}/2}}{\sqrt{2\pi}}\int_{\mathbb{R}}e^{-(x+i\sigma^{2}\lambda)^{2}/(2\sigma^{2})}dx .$$

被积函数是整函数，且在实轴上按 $$e^{-x^{2}/(2\sigma^{2})}$$ 衰减，所以把积分围道平移到实轴（即令 $$u=x+i\sigma^{2}\lambda$$ 沿实轴取遍 $$\mathbb{R}$$）不改变积分值：

$$\int_{\mathbb{R}}e^{-(x+i\sigma^{2}\lambda)^{2}/(2\sigma^{2})}dx=\int_{\mathbb{R}}e^{-u^{2}/(2\sigma^{2})}du=\sigma\sqrt{2\pi},$$

末式由 $$\int_{\mathbb{R}}e^{-t^{2}}dt=\sqrt{\pi}$$ 取 $$t=u/(\sigma\sqrt2)$$ 得到。代回得

$$\hat f_\sigma(\lambda)=\sigma\,e^{-\sigma^{2}\lambda^{2}/2}.$$

取 $$\sigma=1$$ 时右端是 $$e^{-\lambda^{2}/2}=f_1(\lambda)$$，正是例题 5.4 的不动点。所以 Gauss 函数族在 $$\mathcal F$$ 下封闭：$$\mathcal F$$ 只是把 $$\sigma$$ 换成 $$1/\sigma$$，再补一个常数因子 $$\sigma$$。

(ii) $$f_\sigma$$ 与 $$\hat f_\sigma$$ 的模方都是 Gauss 密度（前者正比于 $$e^{-x^{2}/\sigma^{2}}$$，后者正比于 $$e^{-\sigma^{2}\lambda^{2}}$$），由定理 3.6 的高阶矩直接算出

$$(\Delta x)^{2}=\frac{\sigma^{2}}{2},\qquad(\Delta\lambda)^{2}=\frac{1}{2\sigma^{2}},$$

即 $$\Delta x=\dfrac{\sigma}{\sqrt2}$$、$$\Delta\lambda=\dfrac{1}{\sigma\sqrt2}$$：一个变宽，另一个必定变窄，乘积恒为 $$1/2$$。

再用定理 3.14 的 $$\mathcal F P\mathcal F^{-1}=\hbar M_\lambda$$：它说 $$\lambda$$ 就是"动量读数除以 $$\hbar$$"这个坐标，故 $$\Delta p=\hbar\,\Delta\lambda=\dfrac{\hbar}{\sigma\sqrt2}$$。两式相乘，

$$\Delta x\,\Delta p=\frac{\sigma}{\sqrt2}\cdot\frac{\hbar}{\sigma\sqrt2}=\frac{\hbar}{2},$$

与 $$\sigma$$ 无关，与例题 5.1 的结果一致。这说明 $$\Delta x\,\Delta p$$ 里的 $$\hbar/2$$ 不是某个波包的巧合，而是 $$\mathcal F$$ 把 $$X$$ 换成 $$\hbar M_\lambda$$ 这条**尺度对偶**的直接读数：位置越窄（$$\sigma$$ 越小），动量就越宽（$$1/\sigma$$ 越大），两者恰被 Fourier 变换互换（定理 3.14）。对 Gauss 族，这个乘积取到等号而从不严格大于——这正是第 36 章 Robertson 不等式 $$\Delta\hat A\,\Delta\hat B\ge\frac{1}{2}\bigl\lvert\langle[\hat A,\hat B]\rangle\bigr\rvert$$ 的等号情形（最小不确定态）；至于"为什么只有 Gauss 族取等号"，要用到证明该不等式时 Cauchy–Schwarz 的取等条件。

**解 竞1.** 关键 leap：不算 $$[X,P^n]$$ 的展开，而是用 Leibniz 律**把 $$P^n$$ 拆出一个 $$P$$** 再归纳。把定理 3.8 (iii) 用反对称性换成第二变量形式：

$$[A,BC]=-[BC,A]=-\bigl(B[C,A]+[B,A]C\bigr)=[A,B]C+B[A,C].$$

归纳：$$n=1$$ 是定理 3.7。设 $$[X,P^{n-1}]=i\hbar(n-1)P^{n-2}$$，取 $$A=X,B=P,C=P^{n-1}$$：

$$[X,P^n]=[X,P]P^{n-1}+P[X,P^{n-1}]=i\hbar P^{n-1}+i\hbar(n-1)P^{n-1}=i\hbar nP^{n-1}.$$

对 $$f(P)=\sum_{k=0}^mf_kP^k$$ 用线性性（定理 3.8 (i)）：

$$[X,f(P)]=\sum_{k\ge1}f_k\,i\hbar kP^{k-1}=i\hbar\sum_{k\ge1}kf_kP^{k-1}=i\hbar f'(P).$$

（把 $$X$$ 换成 $$P$$、$$P$$ 换成 $$X$$ 时符号相反：$$[P,f(X)]=-i\hbar f'(X)$$，同法可证。）

**解 竞2.** 用 $$\dfrac{d\hat A}{dt}=\dfrac{i}{\hbar}[\hat H,\hat A]$$ 逐条算括号。

**第一个**：$$\bigl[\tfrac{\hat P^2}{2m},\hat X\bigr]=\tfrac{1}{2m}\bigl(\hat P[\hat P,\hat X]+[\hat P,\hat X]\hat P\bigr)=\tfrac{1}{2m}(-i\hbar\hat P-i\hbar\hat P)=-\tfrac{i\hbar}{m}\hat P$$（用了竞1 的 Leibniz 与 $$[P,X]=-i\hbar$$）；而 $$[V(\hat X),\hat X]=0$$。故

$$\frac{d\hat X}{dt}=\frac{i}{\hbar}\Bigl(-\frac{i\hbar}{m}\hat P\Bigr)=\frac{\hat P}{m}.$$

**第二个**：$$\bigl[\tfrac{\hat P^2}{2m},\hat P\bigr]=0$$；而 $$[V(\hat X),\hat P]=i\hbar V'(\hat X)$$（这是竞1 结论的镜像，取反对称即得）。故

$$\frac{d\hat P}{dt}=\frac{i}{\hbar}\cdot i\hbar V'(\hat X)=-V'(\hat X).$$

**期望值**：把两式与 $$\lvert\psi\rangle$$ 取内积。因态固定（Heisenberg 绘景），导数只落在算子上：

$$\frac{d}{dt}\langle\hat X\rangle=\frac{\langle\hat P\rangle}{m},\qquad
\frac{d}{dt}\langle\hat P\rangle=-\bigl\langle V'(\hat X)\bigr\rangle .$$

这就是 Ehrenfest 定理：量子期望值遵守经典（牛顿）运动方程。注意右边是 $$\langle V'(X)\rangle$$ 而不是 $$V'(\langle X\rangle)$$；两者只在 $$V$$ 为二次多项式时相等（那时波包像经典粒子一样走），一般情形有偏差——偏差由波包的展宽给出。

**解 竞3.** 关键 leap：**对易子的迹恒为零**。由 $$\mathrm{tr}(AB)=\mathrm{tr}(BA)$$（把 $$A,B$$ 写成矩阵、利用 $$\sum_i(AB)_{ii}=\sum_{i,j}A_{ij}B_{ji}$$ 的对称性）：

$$\mathrm{tr}[X,P]=\mathrm{tr}(XP)-\mathrm{tr}(PX)=0 .$$

另一方面 $$\mathrm{tr}(i\hbar I)=i\hbar\,\mathrm{tr}I=i\hbar n$$。若 $$[X,P]=i\hbar I$$ 成立则两边迹相等，得 $$i\hbar n=0$$；因 $$\hbar>0$$、$$n\ge1$$，矛盾。

**结论**：不存在有限维矩阵 $$X,P$$（自伴、维数有限）满足正则对易关系。所以位置与动量这对算子**不可能活在有限维空间里**，量子力学必须在无限维 Hilbert 空间上做。对照之下，自旋有有限维表示（见卷四的 Lie 群与表示），因为它的对易关系是角动量的 $$\varepsilon_{ijk}$$ 型（不是 $$i\hbar I$$）——那样的代数可以在有限维里闭合。这条对比说明"量子化"不是"把数换成矩阵"，而是要选对**无限维**舞台。

**解 竞4.** 用自伴性把 $$\hat A$$ 从一边搬到另一边：

$$\lambda_1\langle e_1\vert e_2\rangle=\langle\hat A e_1\vert e_2\rangle=\langle e_1\vert\hat A e_2\rangle=\overline{\lambda_2}\langle e_1\vert e_2\rangle=\lambda_2\langle e_1\vert e_2\rangle,$$

第二式用了 $$\hat A^{*}=\hat A$$，末式用了定理 3.10 (c) 的 $$\lambda_2\in\mathbb{R}$$。于是 $$(\lambda_1-\lambda_2)\langle e_1\vert e_2\rangle=0$$，因 $$\lambda_1\ne\lambda_2$$ 得 $$\langle e_1\vert e_2\rangle=0$$。

简并时结论变弱：只有**不同**本征值对应的本征空间相互正交；同一本征值的特征子空间内部两向量未必正交。补救是在该子空间内做 Gram–Schmidt 正交化（第 30 章）。这解释了定义 3.11 为什么要额外声明"$$\{\lvert e_i\rangle\}$$ 是正交归一基"——它不是定理 3.10 的自动推论，而是一条需要单独建立的条件；无限维情形下把它与连续谱一起统一处理，就是谱定理（第 38 章）。

**解 研1.** 无界性：取 $$\psi_n(x)=\frac{1}{x}$$（$$1\le x\le n$$）、$$0$$（其余）。则

$$\lVert\psi_n\rVert^2=\int_1^n\frac{dx}{x^2}=1-\frac1n\le1,\qquad \lVert X\psi_n\rVert^2=\int_1^n x^2\cdot\frac{1}{x^2}\,dx=n-1 .$$

故 $$\lVert X\psi_n\rVert/\lVert\psi_n\rVert\ge\sqrt{n-1}\to\infty$$，$$X$$ 无界。

为什么必须升级：定义 3.11 的展开要求 (1) 每个 $$\lambda_i$$ 对应一个 $$L^2$$ 中的特征向量；(2) 它们两两正交；(3) 它们完备。对 $$P$$ 第 (1) 条就崩了：形式特征函数 $$e^{ikx}$$ 满足 $$Pe^{ikx}=\hbar ke^{ikx}$$，但

$$\lVert e^{ikx}\rVert^2=\int_{\mathbb{R}}\lvert e^{ikx}\rvert^2dx=\int_{\mathbb{R}}1\,dx=\infty,$$

故 $$e^{ikx}\notin L^2(\mathbb{R})$$——**动量算子在 $$\mathbb{R}$$ 上没有平方可积的本征函数**，它的谱是连续的，根本没有特征值可谈（对比环上的定理 3.4：那里 $$e^{ikx}\in L^2[0,2\pi]$$，所以有离散特征值）。替代品是把"特征投影"推广成**投影算子值测度 (p.v.m.)** $$E(\cdot)$$，把求和换成积分

$$\hat A=\int_{\sigma(\hat A)}\lambda\,dE(\lambda),\qquad
\langle\hat A\rangle=\langle\psi\vert\hat A\psi\rangle=\int_{\sigma(\hat A)}\lambda\,d\mu_\psi(\lambda),$$

其中 $$\mu_\psi(\Delta)=\langle\psi\vert E(\Delta)\psi\rangle$$ 是普通概率测度。$$e^{ikx}$$ 在这套语言下获得合法地位：它不生成特征向量，而生成连续谱上的谱测度。连续的 $$\lambda$$ 积分与离散的求和在这里第一次被同一个框架收编，而这正是第 34 章要走的第一步——Schrödinger 方程在 $$\mathbb{R}$$ 上的解也不再是有限和，而是对连续谱的积分（波包）。

**解 研2.** 先说明 $$\hat U(t)=e^{-i\hat Ht/\hbar}$$ 有定义且酉：由 $$\hat H$$ 自伴，谱定理（第 38 章）给出 $$e^{-i\hat Ht/\hbar}$$ 并保证 $$\hat U(t)^{*}=e^{+i\hat Ht/\hbar}=\hat U(t)^{-1}$$。于是 $$\hat A(t)=\hat U(t)^{*}\hat A\hat U(t)$$。

求导。对幂级数逐项求导得 $$\dfrac{d}{dt}\hat U(t)=\dfrac{-i}{\hbar}\hat H\hat U(t)$$（$$\hat H$$ 与它的幂交换，故可与求和交换）。取共轭：$$\dfrac{d}{dt}\hat U^{*}=\dfrac{i}{\hbar}\hat U^{*}\hat H$$。代入：

$$\frac{d\hat A}{dt}=\Bigl(\frac{d}{dt}\hat U^{*}\Bigr)\hat A\hat U+\hat U^{*}\hat A\Bigl(\frac{d}{dt}\hat U\Bigr)
=\frac{i}{\hbar}\hat U^{*}\hat H\hat A\hat U-\frac{i}{\hbar}\hat U^{*}\hat A\hat H\hat U
=\frac{i}{\hbar}\hat U^{*}[\hat H,\hat A]\hat U .$$

又因 $$\hat U^{*}\hat H\hat U=\hat H$$（$$\hat U$$ 是 $$\hat H$$ 的函数，两者交换），右端 $$=\dfrac{i}{\hbar}[\hat H,\hat U^{*}\hat A\hat U]=\dfrac{i}{\hbar}[\hat H,\hat A(t)]$$。故 $$\hat A(t)$$ 满足 Heisenberg 方程。

酉群：由指数律 $$\hat U(t+s)=\hat U(t)\hat U(s)$$、$$\hat U(0)=I$$、$$\hat U(t)^{*}\hat U(t)=I$$，三条都成立，故 $$t\mapsto\hat U(t)$$ 是单参数酉群。

这条解答把"演化 = 与 $$\hat H$$ 作括号"从无穷小（一个微分方程）升级成整体（一个群）。把同一件事写回随时间变化的态上，即 $$\lvert\psi(t)\rangle=\hat U(t)\lvert\psi(0)\rangle$$，就得到 $$i\hbar\dfrac{\partial}{\partial t}\lvert\psi(t)\rangle=\hat H\lvert\psi(t)\rangle$$——**这正是第 34 章 Schrödinger 方程的起点**：那里不再把演化挂在算子上（Heisenberg 绘景），而是挂在态上（Schrödinger 绘景）。

## 七、Takeaway 与延伸 (Takeaways)

1. **量子化动的是括号，不是"数"。** 被替换的是相空间函数全体上的 Poisson 括号 $$\{,\}$$，换成 $$\frac{1}{i\hbar}[\,,\,]$$。位置与动量算符的具体形式（乘 $$x$$、$$-i\hbar\frac{d}{dx}$$）是这条要求的推论，不是约定的堆砌。

2. **那个 $$i$$ 有出处。** 自伴算子的对易子是反自伴的（定理 3.8 (v)）；要让保括号对应的右边仍是自伴算子，系数必须是纯虚数（定理 3.9 第一步）。所以 $$[X,P]=i\hbar$$ 里的 $$i$$ 不是谁的灵感，是"读数必须是实数"逼出来的。

3. **$$[X,P]=i\hbar$$ 与 $$\{q,p\}=1$$ 是同一个 $$1$$。** 前者是后者在"保括号代数"下的唯一量子对应；$$\hbar$$ 的出现位置由这条等式本身锁定。

4. **可观测量的三个"必须"由自伴性一肩挑起**（定理 3.10）：期望恒实、本征值恒实、不同本征值的本征向量正交。丢掉自伴，概率诠释立刻塌掉。

5. **第 04 章那条"求导给出谱"的线索在这里完成了升级。** 当时它是 $$SO(2)$$ 上的一个例子；现在它是动量算子的谱：$$Pe^{ikx}=\hbar ke^{ikx}$$，离散的 $$k$$ 来自环的拓扑、连续的 $$\lambda$$ 来自 $$\mathbb{R}$$ 的拓扑。

**下一章的悬念**：本章把演化放在算子上（Heisenberg 绘景），得到 $$d\hat A/dt=\frac{i}{\hbar}[\hat H,\hat A]$$（研2 的形式解）。如果把同一件事写回态上，$$\lvert\psi(t)\rangle=\hat U(t)\lvert\psi(0)\rangle$$，会得到一个关于 $$\lvert\psi\rangle$$ 的一阶偏微分方程。它长什么样？它的解为什么可以按本征态展开、而展开的系数恰好是本章的"概率幅"？——这就是第 34 章 Schrödinger 方程。

**延伸阅读**：

- B. C. Hall, *Quantum Theory for Mathematicians* (GTM 267), 第 1、3、8 章：$$X,P$$ 的对称性与本质自伴性、谱定理的物理应用。
- G. Teschl, *Mathematical Methods in Quantum Mechanics* (GSM 157), 第 1、2 章：无界算子与谱测度的标准处理。
- V. I. Arnold, *Mathematical Methods of Classical Mechanics*：Poisson 括号与辛几何（对应第 08 章的进一步展开）。
- 本课程第 04 章（求导与谱）、第 08 章（辛结构）、第 30 章（Hilbert 空间）是本章的三条直接前置。

**留一个未收的问题**：定理 3.9 说的是"保括号"这一条形式要求，但物理学还要求 $$\hat H$$ 的谱有下界（否则系统会无限下坠）。这条要求把哪些哈密顿量排除在外？它是第 38 章（谱定理）与第 42 章（无界算子）的交界处。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch31_从Hamilton到量子_可观测量与本征态_上.md">← 第31章 从 Hamilton 到量子：可观测量与本征态·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch33_Schrödinger方程_上.md">第33章 Schrödinger 方程·上 →</a></div>
</div>
