---
layout: default
---

# 第54章: Lie 代数与指数映射·下：完整推导 (Lie Algebras and the Exponential Map · Part II: Full Derivation)

> 专家依据: algebra/lie-algebra-root-systems.md（主）；方法论见 algebra/_SKILL.md
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）
> 配套预备: 见 第53章 Lie 代数与指数映射·上（同一主题的具体铺垫，建议先读）

## 一、本章概要 (Overview)

读完第 53 章的具体例子后——矩阵指数在对角矩阵与幂零矩阵上怎么算、$$e^{tA}e^{tB}$$ 与 $$e^{t(A+B)}$$ 差多少、怎样对约束方程求导得到 $$\mathfrak{so}(2)$$ 与 $$\mathfrak{so}(3)$$、$$\exp$$ 为什么会"撞车"——这里把同样的构造写成一般定义，并给出完整证明。

第 48 章已经把骨架搭好：Lie 群是「群 + 光滑流形 + 相容性」，在单位元处求导得到它的 Lie 代数 $$\mathfrak{g}=T_eG$$，括号是左不变向量场的对易子，矩阵情形就是换位子 $$[A,B]=AB-BA$$。本章要让这条链**动起来**——把 $$\mathfrak{g}$$ 里的直线积分成 $$G$$ 上的曲线，即给出指数映射 $$\exp:\mathfrak{g}\to G$$，并说清它什么时候是「群与代数之间的桥」、什么时候不是。

三个问题串起全章。**第一，求导丢掉了什么？** 把 $$G$$ 在单位元处线性化，得到的只是一个向量空间；第 48 章的定理 3.22 说每个切向量都唯一地积分成一条单参数子群，于是每个 $$X\in\mathfrak{g}$$ 都给出 $$G$$ 上的一整条曲线 $$t\mapsto\exp(tX)$$。**第二，丢掉的东西能不能补回来？** BCH 公式给出 $$e^Xe^Y=e^{\,X+Y+\frac12[X,Y]+\cdots}$$，它说明括号 $$[X,Y]$$ 恰是「指数映射与加法之间的失配」；于是 Lie 代数决定群的**局部**结构，一点不多也一点不少。**第三，局部够不够用？** 不够：$$\mathfrak{su}(2)\cong\mathfrak{so}(3)$$ 是同构的 Lie 代数，可 $$SU(2)$$ 与 $$SO(3)$$ 是覆叠比为二的不同的群（第 52 章），而且 $$\exp$$ 连满射都不一定成立。局部与整体之间隔着一层拓扑。

本章同时收两条旧账。第 04 章那句「对 $$\theta J$$ 求导得 $$i$$」是本章最小、最完整的例子；第 44 章的 $$[x,p]=i\hbar$$ 在这里第一次有了名字——它是 **Heisenberg 代数 (Heisenberg algebra)**（第 44 章的 定义 3.3 写作"Heisenberg代数"，本章统一记作 Heisenberg 代数），而指数化之后是 Heisenberg 群，第 44 章的整个 Stone–von Neumann 定理在那时会被重新读成「一个幂零 Lie 群的不可约酉表示唯一」。第 56 章要把实 Lie 代数复化，把这里的「谱」升级成「权」与「根」。

## 二、入口：一道具体的问题 (Entry Problem)

> 题目来源：**自编**。母题是「两个无穷小变换叠在一起，为什么会多出一点东西」。它同时是第 44 章 Heisenberg 代数的最小具体化身，也是下一节 BCH 公式的最短验证。

**入口题。** 记 $$E_{ij}$$ 为 $$3\times3$$ 矩阵中第 $$i$$ 行第 $$j$$ 列位置为 $$1$$、其余位置为 $$0$$ 的矩阵。取

$$X=E_{12}=\begin{bmatrix}0&1&0\\0&0&0\\0&0&0\end{bmatrix},\qquad Y=E_{23}=\begin{bmatrix}0&0&0\\0&0&1\\0&0&0\end{bmatrix},$$

并记 $$Z:=[X,Y]=XY-YX$$。

**(a)** 算出 $$X^2,\ Y^2,\ XY,\ YX,\ Z$$。验证：在四个乘积 $$X^2,Y^2,XY,YX$$ 中，除 $$XY$$ 之外全部为零，而 $$XY=Z$$。

**(b)** 算出 $$\exp(X)$$、$$\exp(Y)$$ 与 $$\exp(X)\exp(Y)$$（注意 $$X^2=Y^2=0$$，幂级数只剩两项）。再算出 $$\exp\!\bigl(X+Y+\tfrac12 Z\bigr)$$，并验证

$$\exp(X)\exp(Y)=\exp\!\Bigl(X+Y+\tfrac12[X,Y]\Bigr).$$

**(c)** 承 (b)：证明上式右边**不能**简化成 $$\exp(X+Y)$$。再算出四条曲线的换位子 $$e^{X}e^{Y}e^{-X}e^{-Y}$$，证明它等于 $$e^{Z}$$ 而**不是**单位矩阵。

**(d)**（真正的问题）现在把 $$X,Y$$ 换成任意两个 $$n\times n$$ 矩阵 $$A,B$$。既然 $$e^Ae^B$$ 一般不等于 $$e^{A+B}$$，那么 $$\log\!\bigl(e^Ae^B\bigr)$$ 究竟等于什么？先猜出它除 $$A+B$$ 之外的头一项，再回答：**在单位元处求导（取 Lie 代数）到底丢掉了哪些信息？丢掉的信息够不够还原整个群 $$G$$？**

**为什么这道题必须用本章的工具才能真正解掉。** (a)(b)(c) 三问都能手算到底，答案却指向一件一般的事：$$e^Xe^Y$$ 与 $$e^{X+Y}$$ 的差由一个**二阶项** $$[X,Y]$$ 掌管。 (d) 问的就是这个二阶项在一般情形下的确切形状——这正是 BCH 公式（定理 3.8），而要证明它、并且解释它为什么恰好把「丢掉的二阶信息」补回来，需要先有单参数子群（§3.1）、指数映射与对数映射（§3.2）、矩阵 Lie 群的代数刻画（§3.3）这一整套机器。 (a) 里的 $$X,Y,Z$$ 还会在本章最后以名字出现：它们张成 Heisenberg 代数 $$\mathfrak{h}_3$$（定理 3.14），而第 44 章那条 $$[x,p]=i\hbar$$ 就是它在量子力学里的表示。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 出发点：第 48 章留下的零件

本章不重新定义 Lie 群与 Lie 代数，而是直接接着第 48 章往下走。把要用的东西列在这里，便于回查：

**(R1) 单参数子群**（第 48 章的 定义 3.21）。$$G$$ 的**单参数子群 (one-parameter subgroup)** 是光滑同态 $$c:(\mathbb R,+)\to G$$，即光滑曲线满足 $$c(s+t)=c(s)c(t)$$ 对一切 $$s,t\in\mathbb R$$。

**(R2) 切向量与单参数子群的对应**（第 48 章的 定理 3.22）。对每个 $$v\in\mathfrak g=T_eG$$，存在**唯一**的单参数子群 $$c_v$$ 使 $$c_v'(0)=v$$；反之任一单参数子群的 $$c'(0)$$ 都落在 $$\mathfrak g$$ 中。存在性由左不变向量场的积分曲线给出，唯一性由常微分方程解的唯一性给出。

**(R3) 指数映射**（第 48 章的 定义 3.23）。$$\exp:\mathfrak g\to G$$，$$\exp(v):=c_v(1)$$。

**(R4) $$\exp$$ 的基本性质**（第 48 章的 定理 3.24）。(i) $$c_v(t)=\exp(tv)$$；(ii) $$\exp((s+t)v)=\exp(sv)\exp(tv)$$、$$\exp(-v)=\exp(v)^{-1}$$、$$\exp(0)=e$$；(iii) $$\exp$$ 光滑且 $$(d\exp)_0=\mathrm{id}_{\mathfrak g}$$，故 $$\exp$$ 在 $$0$$ 附近是到 $$e$$ 附近的微分同胚；(iv) 自然性：$$\rho(\exp_G v)=\exp_H\bigl((d\rho)_e v\bigr)$$ 对 Lie 群同态 $$\rho:G\to H$$ 成立；(v) 矩阵情形 $$\exp(A)=\sum_{k\ge0}A^k/k!$$。

**(R5) 矩阵群的括号**（第 48 章的 定理 3.20）。对闭子群 $$G\subseteq GL(n,\mathbb R)$$，$$\mathfrak g=T_IG$$ 是 $$M_n(\mathbb R)$$ 的子空间，且括号就是换位子 $$[A,B]=AB-BA$$。

**本章要补的四件事。** (R1)–(R5) 已经说明「求导得到代数」，但留下了四个洞：(1) 求导是个单方向的、不可逆的操作，它的**反函数**——对数映射——在哪里？ (2) 具体到矩阵群，$$\mathfrak g$$ 里到底有哪些矩阵，有没有统一的算法？ (3) 反过来，$$\mathfrak g$$ 的括号能不能唯一决定 $$G$$ 的乘法？ (4) $$\exp$$ 能覆盖多少 $$G$$？ 依次对应下面的 §3.2、§3.3、§3.4、§3.5。

### 3.2 对数映射与指数坐标

**定义 3.1（对数映射, logarithm map）**。由 (R4)(iii)，存在 $$\mathfrak g$$ 中含 $$0$$ 的开集 $$U$$ 与 $$G$$ 中含 $$e$$ 的开集 $$V$$，使 $$\exp:U\to V$$ 是微分同胚。定义

$$\log:=\bigl(\exp\vert_U\bigr)^{-1}:V\to U\subseteq\mathfrak g.$$

$$\log$$ 依赖 $$U,V$$ 的取法，但这不影响它在 $$e$$ 附近的局部性质；下面定理 3.2 说明在重叠区域上它唯一。

**定理 3.2（对数映射的基本性质）**。

(i) $$\log$$ 光滑，$$\log(e)=0$$，且 $$(d\log)_e=\mathrm{id}_{\mathfrak g}$$；

(ii) 对 $$X\in U$$ 有 $$\log(\exp X)=X$$，对 $$g\in V$$ 有 $$\exp(\log g)=g$$；

(iii) **矩阵情形**：若 $$\lVert A-I\rVert<1$$，则

$$\log A=\sum_{k\ge1}\frac{(-1)^{k+1}}{k}(A-I)^k=(A-I)-\frac{(A-I)^2}{2}+\frac{(A-I)^3}{3}-\cdots,$$

且在此条件下 $$\exp(\log A)=A$$；

(iv) $$\log$$ **不是**加法同态：一般地 $$\log(gh)\ne\log g+\log h$$，其偏差由 BCH 公式（定理 3.8）给出；入口题 (c) 的一对 $$X,Y$$ 就是反例。

*证明*。(i) $$\log$$ 是微分同胚的逆映射，故光滑；$$\log(e)=\log(\exp 0)=0$$；再取微分，$$(d\log)_e=\bigl((d\exp)_0\bigr)^{-1}=\mathrm{id}_{\mathfrak g}$$。

(ii) 这就是互为逆映射的定义。

(iii) 记 $$N=A-I$$。设 $$\lVert N\rVert<1$$，则幂级数 $$S(N)=\sum_{k\ge1}(-1)^{k+1}N^k/k$$ 绝对收敛（$$\lVert N^k\rVert\le\lVert N\rVert^k$$，与 $$-\log(1-\lVert N\rVert)$$ 比较）。把标量恒等式 $$\exp(\log(1+x))=1+x$$ 看成两个幂级数的复合：它有正的收敛半径 $$1$$，且复合后仍是一个整幂级数。矩阵 $$\lVert N\rVert<1$$ 落在收敛圆内，故把 $$N$$ 代入复合级数是合法的，得 $$\exp\bigl(S(N)\bigr)=I+N=A$$。

(iv) 取入口题的 $$X,Y$$：由 (iii)（或直接算，见 §6 解 基1），$$\log(e^{X})=\log(I+X)=X$$、$$\log(e^{Y})=Y$$，而 $$e^{X}e^{Y}=I+X+Y+Z$$（$$Z=[X,Y]$$），故

$$\log\bigl(e^{X}e^{Y}\bigr)=X+Y+Z\ne X+Y=\log e^{X}+\log e^{Y}.$$

(顺带看到：$$I+X+Y+Z$$ 比 $$I$$ 远，但 $$\log$$ 依然可用级数算，因为 $$N=X+Y+Z$$ 满足 $$N^2=Z$$、$$N^3=0$$，级数只有两项有效。) $$\blacksquare$$

**推论 3.3（指数坐标, exponential coordinates）**。取 $$\mathfrak g$$ 的一组基 $$X_1,\dots,X_n$$（$$n=\dim G$$），并把 $$U$$ 取得足够小。则 $$V$$ 中每个 $$g$$ 唯一地写成

$$g=\exp\Bigl(\sum_{i=1}^n x_iX_i\Bigr),\qquad (x_1,\dots,x_n)\in U'\subseteq\mathbb R^n,$$

映射 $$g\mapsto(x_1,\dots,x_n)$$ 是 $$G$$ 在 $$e$$ 附近的一张光滑坐标卡（**指数坐标**）。在这套坐标下，群乘法由 BCH 公式以迭代括号的幂级数给出，特别地它以 $$e$$ 为中心是**实解析**的。

*说明*：坐标卡的结论来自定义 3.1 的 $$\log$$ 与线性同构 $$\mathbb R^n\to\mathfrak g$$ 的复合。群乘法解析性的结论来自 BCH（定理 3.8）；这条性质在几何上很重要——它说明 Lie 群在单位元附近"没有除括号之外的结构"，一切局部信息都被有限的括号表 $$c_{ij}^k$$ 决定。

### 3.3 矩阵 Lie 群：把代数算出来

本课程遇到的群几乎都是矩阵群（第 48 章已算出 $$SO(n),SU(n),\mathrm{Aff}(n)$$ 三个），因为矩阵群上所有运算都可以直接手算。本小节给出把 $$\mathfrak g$$ 算出来的**通用算法**，并把第 48 章的推论 3.20 补全成一张完整的表。

**定理 3.4（矩阵 Lie 群的 Lie 代数：指数刻画）**。设 $$G\subseteq GL(n,\mathbb R)$$ 是**闭子群**。由 Cartan 闭子群定理，$$G$$ 自动是嵌入子流形，从而是以 $$\mathfrak g=T_IG$$ 为 Lie 代数的 Lie 群。此时

$$\mathfrak g=\bigl\{X\in M_n(\mathbb R)\ :\ \exp(tX)\in G\ \text{对一切 }t\in\mathbb R\bigr\}.$$

*证明*。($$\subseteq$$) 设 $$X\in\mathfrak g$$。由 (R4)(i)，$$\exp(tX)=c_X(t)$$。在第 48 章的定理 3.20 的证明里已经算出：矩阵群上的左不变向量场是 $$X^A(g)=gA$$，而 $$e^{tA}$$ 满足 $$\frac{d}{dt}e^{tA}=e^{tA}A$$，故 $$t\mapsto\exp(tX)$$ 是左不变向量场 $$X^X$$ 过 $$e$$ 的积分曲线，整条落在 $$G$$ 内。

($$\supseteq$$) 反之，若 $$\exp(tX)\in G$$ 对一切 $$t$$ 成立，则 $$t\mapsto\exp(tX)$$ 是 $$G$$ 内一条光滑曲线，在 $$t=0$$ 处的切向量是

$$\frac{d}{dt}\Big\vert_{t=0}\exp(tX)=X,$$

故 $$X\in T_IG=\mathfrak g$$。$$\blacksquare$$

**定理 3.5（$$\det\exp X=\exp\operatorname{tr}X$$）**。对任意 $$X\in M_n(\mathbb R)$$，

$$\det\bigl(\exp X\bigr)=\exp(\operatorname{tr}X).$$

*证明*。把 $$X$$ 看成复矩阵不影响 $$\det$$ 与 $$\operatorname{tr}$$，故在 $$\mathbb C$$ 上作。复方阵必可上三角化：存在可逆 $$P$$ 与上三角 $$T$$，使 $$X=PTP^{-1}$$，而 $$T$$ 的对角元恰是 $$X$$ 的特征值 $$\lambda_1,\dots,\lambda_n$$（含代数重数）。

由 (R4)(v)，$$\exp(X)=\sum_kX^k/k!$$。因为 $$X^k=PT^kP^{-1}$$，级数逐项共轭，得 $$\exp(X)=P\exp(T)P^{-1}$$。上三角矩阵的幂仍上三角，故 $$\exp(T)$$ 上三角，其对角元是 $$\sum_k(\lambda_i)^k/k!=e^{\lambda_i}$$。于是

$$\det\exp(X)=\det\exp(T)=\prod_{i=1}^ne^{\lambda_i}=\exp\Bigl(\sum_{i=1}^n\lambda_i\Bigr)=\exp(\operatorname{tr}X).$$

（右边两个等式的依据分别是：三角阵的行列式等于对角元之积；$$\operatorname{tr}$$ 是特征值之和。）$$\blacksquare$$

**定理 3.6（经典矩阵 Lie 群一览）**。下表中 $$\Omega=\begin{bmatrix}0&I_n\\-I_n&0\end{bmatrix}$$：

| 群 $$G$$ | 定义条件 | $$\mathfrak g$$ | $$\dim\mathfrak g$$ |
|---|---|---|---|
| $$GL(n,\mathbb R)$$ | 可逆 | $$M_n(\mathbb R)$$ | $$n^2$$ |
| $$SL(n,\mathbb R)$$ | $$\det=1$$ | $$\mathfrak{sl}(n,\mathbb R)=\{X:\operatorname{tr}X=0\}$$ | $$n^2-1$$ |
| $$O(n)$$ | $$R^{\mathsf T}R=I$$ | $$\mathfrak{so}(n)=\{X:X^{\mathsf T}=-X\}$$ | $$\frac{n(n-1)}2$$ |
| $$SO(n)$$ | $$R^{\mathsf T}R=I,\ \det R=1$$ | $$\mathfrak{so}(n)$$ | $$\frac{n(n-1)}2$$ |
| $$U(n)$$ | $$U^*U=I$$ | $$\mathfrak u(n)=\{X:X^*=-X\}$$ | $$n^2$$ |
| $$SU(n)$$ | $$U^*U=I,\ \det U=1$$ | $$\mathfrak{su}(n)=\{X:X^*=-X,\ \operatorname{tr}X=0\}$$ | $$n^2-1$$ |
| $$Sp(2n,\mathbb R)$$ | $$M^{\mathsf T}\Omega M=\Omega$$ | $$\mathfrak{sp}(2n,\mathbb R)=\{X:X^{\mathsf T}\Omega+\Omega X=0\}$$ | $$n(2n+1)$$ |

*算法*：对定义条件中的每一条恒等式在 $$t=0$$ 处求导，得到 $$\mathfrak g$$ 必须满足的**线性**条件（这是必要性）；再对满足线性条件的 $$X$$ 验证 $$\exp(tX)$$ 确实落回 $$G$$（这是充分性，用定理 3.4）。这条算法在第 48 章的推论 3.20 里已经对 $$\mathfrak{gl},\mathfrak{so},\mathfrak u,\mathfrak{su},\mathfrak{aff}$$ 跑过一遍，下面只补新的两行，并统一给出维数。

*$$\mathfrak{sl}(n,\mathbb R)$$ 一行*。由定理 3.5，$$\det\exp(tX)=e^{t\operatorname{tr}X}$$；它对一切 $$t$$ 等于 $$1$$ 当且仅当 $$\operatorname{tr}X=0$$。维数：$$\operatorname{tr}$$ 是 $$M_n$$ 上非零线性泛函，其核的维数是 $$n^2-1$$。

*$$\mathfrak{sp}(2n,\mathbb R)$$ 一行*。对 $$M(t)^{\mathsf T}\Omega M(t)=\Omega$$（$$M(0)=I$$）在 $$t=0$$ 求导，得 $$X^{\mathsf T}\Omega+\Omega X=0$$。把这条条件改写：由 $$\Omega^{\mathsf T}=-\Omega$$，

$$X^{\mathsf T}\Omega+\Omega X=0\iff X^{\mathsf T}\Omega=-\Omega X\iff (\Omega X)^{\mathsf T}=X^{\mathsf T}\Omega^{\mathsf T}=-X^{\mathsf T}\Omega=\Omega X,$$

末一式正是「$$S:=\Omega X$$ 是对称矩阵」。$$\Omega$$ 可逆，故 $$X\mapsto\Omega X$$ 是 $$M_{2n}(\mathbb R)$$ 上的可逆线性映射，且上式说明它把 $$\mathfrak{sp}(2n,\mathbb R)$$ 双射到全体对称矩阵上。于是

$$\dim\mathfrak{sp}(2n,\mathbb R)=\frac{2n(2n+1)}2=n(2n+1).$$

反向：若 $$S=\Omega X$$ 对称，则 $$S^{\mathsf T}=S$$，即 $$(\Omega X)^{\mathsf T}=\Omega X$$；展开左边 $$(\Omega X)^{\mathsf T}=X^{\mathsf T}\Omega^{\mathsf T}=-X^{\mathsf T}\Omega$$，于是 $$-X^{\mathsf T}\Omega=\Omega X$$，即 $$\Omega X=-X^{\mathsf T}\Omega$$（**注意符号**：不是 $$\Omega X=X^{\mathsf T}\Omega$$）。代入即得 $$X^{\mathsf T}\Omega+\Omega X=X^{\mathsf T}\Omega+(-X^{\mathsf T}\Omega)=0$$。取 $$X=\Omega^{-1}S$$，对 $$\Phi(t)=\exp(tX)^{\mathsf T}\Omega\exp(tX)$$ 求导（用 $$\frac{d}{dt}\exp(tX)^{\mathsf T}=\exp(tX)^{\mathsf T}X^{\mathsf T}$$）：

$$\Phi'(t)=\exp(tX)^{\mathsf T}\bigl(X^{\mathsf T}\Omega+\Omega X\bigr)\exp(tX)=0,$$

故 $$\Phi$$ 恒为常数，$$\Phi(t)=\Phi(0)=\Omega$$，即 $$\exp(tX)\in Sp(2n,\mathbb R)$$ 对一切 $$t$$。由定理 3.4，$$X\in\mathfrak{sp}(2n,\mathbb R)$$。$$\blacksquare$$

*其余各行的维数*：$$\mathfrak u(n)$$ 由 $$n$$ 个纯虚对角元（$$n$$ 个实数参数）与 $$\frac{n(n-1)}2$$ 个自由复元（$$n(n-1)$$ 个实数参数）决定，共 $$n^2$$；$$\mathfrak{su}(n)$$ 是在 $$\mathfrak u(n)$$ 上加一个实条件 $$\operatorname{tr}X=0$$（反厄米矩阵的对角元纯虚，故迹纯虚，"迹为零"是 $$1$$ 个实条件），得 $$n^2-1$$；$$\mathfrak{so}(n)$$ 由严格上三角的 $$\frac{n(n-1)}2$$ 个元素自由决定。

**推论 3.7（$$\mathfrak{so}(3)\cong\mathfrak{su}(2)\cong\mathbb R^3$$：第 52 章那个失配的代数解释）**。取

$$J_1=\begin{bmatrix}0&0&0\\0&0&-1\\0&1&0\end{bmatrix},\quad J_2=\begin{bmatrix}0&0&1\\0&0&0\\-1&0&0\end{bmatrix},\quad J_3=\begin{bmatrix}0&-1&0\\1&0&0\\0&0&0\end{bmatrix},$$

则 $$\{J_1,J_2,J_3\}$$ 是 $$\mathfrak{so}(3)$$ 的一组基，且

$$[J_j,J_k]=\varepsilon_{jkl}J_l\qquad(\varepsilon\ \text{为 Levi-Civita 符号，重复指标求和}).$$

在 $$\mathfrak{su}(2)$$ 一侧取 $$S_k=\dfrac{1}{2i}\sigma_k=-\dfrac i2\sigma_k$$（$$\sigma_1,\sigma_2,\sigma_3$$ 为 Pauli 矩阵）。每个 $$\sigma_k$$ 厄米且迹零，故 $$S_k^*=-S_k$$、$$\operatorname{tr}S_k=0$$，即 $$S_k\in\mathfrak{su}(2)$$；由 $$\sigma_j\sigma_k=\delta_{jk}I+i\varepsilon_{jkl}\sigma_l$$ 得

$$[S_j,S_k]=\frac{-1}{4}\bigl(\sigma_j\sigma_k-\sigma_k\sigma_j\bigr)=\frac{-1}{4}\cdot2i\varepsilon_{jkl}\sigma_l=\varepsilon_{jkl}S_l.$$

于是 $$S_k\mapsto J_k$$ 线性延拓后是 Lie 代数同构 $$\mathfrak{su}(2)\to\mathfrak{so}(3)$$。

**但这个同构不能提升为群的同构。** 取同一个代数元素的两个实现：在 $$\mathfrak{so}(3)$$ 里是 $$J_3$$，在 $$\mathfrak{su}(2)$$ 里是 $$S_3$$。由 $$J_3^2=\operatorname{diag}(-1,-1,0)$$、$$J_3^3=-J_3$$ 得

$$\exp(tJ_3)=\cos t\,I+\sin t\,J_3+(1-\cos t)J_3^2=\begin{bmatrix}\cos t&-\sin t&0\\ \sin t&\cos t&0\\ 0&0&1\end{bmatrix}=R_z(t),$$

故 $$\exp(2\pi J_3)=I$$。而 $$S_3=-\frac i2\sigma_3$$，$$\exp(tS_3)=e^{-it\sigma_3/2}=\operatorname{diag}\bigl(e^{-it/2},e^{it/2}\bigr)$$，故 $$\exp(2\pi S_3)=\operatorname{diag}(-1,-1)=-I\ne I$$。

**同一个 Lie 代数里的同一个元素，在 $$SO(3)$$ 里走一整圈回到单位元，在 $$SU(2)$$ 里只走到 $$-I$$。** 第 52 章那条「转 $$360^\circ$$ 不是恒等、转 $$720^\circ$$ 才是」的二重覆盖，在 Lie 代数层面**完全不可见**——因为线性化（求导）把 $$SU(2)\to SO(3)$$ 这个二对一的覆叠映射压成了二对二的恒等映射。这就是 §一 中「局部够不够用」的答案：$$\exp$$ 不是单射，覆叠信息在求导时被抹平。

### 3.4 BCH：指数映射什么时候是桥

§3.3 说明 $$\mathfrak g$$ 可以算；现在回答反方向的问题：$$\mathfrak g$$ **够不够**决定 $$G$$？

**定理 3.8（Baker–Campbell–Hausdorff 公式）**。存在 $$\mathfrak g$$ 中含 $$0$$ 的开邻域 $$U$$，使对一切 $$X,Y\in U$$ 有

$$\log\bigl(e^{X}e^{Y}\bigr)=X+Y+\frac12[X,Y]+\frac1{12}\Bigl([X,[X,Y]]+[Y,[Y,X]]\Bigr)+\cdots,$$

其中 $$\cdots$$ 里每一项都是 $$X,Y$$ 的**迭代括号**（反复取 $$[\cdot,\cdot]$$ 得到的式子），系数是与 $$\mathfrak g$$ 无关的普适有理数。特别地：$$\log(e^Xe^Y)$$ 只依赖 $$\mathfrak g$$ 的括号运算，不依赖 $$X,Y$$ 的矩阵形状（把它们放进任何别的实现里，结果一样）。

*证明思路*（本课程引用结论与前三阶系数；完整证明需要幂级数解的存在唯一性与 Dynkin 的组合公式）。记 $$Z(t)=\log\bigl(e^{tX}e^{Y}\bigr)$$，它在 $$t=0$$ 附近有定义，且 $$e^{Z(t)}=e^{tX}e^{Y}$$。两边对 $$t$$ 求导：左边用矩阵求导公式

$$\frac{d}{dt}e^{Z(t)}=\int_0^1e^{sZ}\dot Ze^{(1-s)Z}\,ds=\Bigl(\frac{e^{\operatorname{ad}Z}-1}{\operatorname{ad}Z}\Bigr)(\dot Z)\cdot e^{Z},$$

右边等于 $$Xe^{tX}e^{Y}=Xe^{Z}$$。两边约去 $$e^{Z}$$ 并解出 $$\dot Z$$：

$$\dot Z(t)=\sum_{n\ge0}\frac{B_n}{n!}\bigl(\operatorname{ad}Z(t)\bigr)^nX,\qquad Z(0)=Y,$$

其中 $$B_n$$ 是 Bernoulli 数（$$B_0=1,\ B_1=-\frac12,\ B_2=\frac16,\dots$$），而 $$\operatorname{ad}Z=[Z,\cdot]$$。这是一条关于 $$Z$$ 的（无穷维）常微分方程，右端的解析性保证它有唯一解析解。把 $$Z(t)=Y+tW_1+t^2W_2+\cdots$$ 代入逐阶比较系数：一阶给出 $$W_1=X-\frac12[Y,X]=X+\frac12[X,Y]$$，继续解下去，在 $$t=1$$ 处的前几项即定理中的展开式。

*为什么幂零时会截断*：Dynkin 的显式公式表明，$$n$$ 阶项是 $$\operatorname{ad}X$$ 与 $$\operatorname{ad}Y$$ 的 $$n-1$$ 重复合作用在某个元素上的结果。若 $$\mathfrak g$$ 幂零（下中心列 $$L^{c+1}=0$$），则 $$\operatorname{ad}X$$ 是幂零算子，每个因子至多出现 $$c$$ 次，故 $$n-1\le2(c-1)$$ 之后的项全为零——**幂零情形的 BCH 是有限多项式**（见定理 3.14）。

**推论 3.9（括号 = $$\exp$$ 与加法的"二阶失配"）**。

(i) 对 $$X,Y\in U$$，$$\log(e^Xe^Y)-(X+Y)=\frac12[X,Y]+(\text{三阶及以上})$$；

(ii) $$[X,Y]=\displaystyle\lim_{t\to0}\frac1{t^2}\log\Bigl(e^{tX}e^{tY}e^{-tX}e^{-tY}\Bigr)$$；

(iii) $$e^Xe^Y=e^{X+Y}$$ 在 $$\lVert X\rVert,\lVert Y\rVert$$ 充分小时成立，当且仅当 $$[X,Y]=0$$；整体地，若 $$[X,Y]=0$$，则对一切 $$X,Y$$ 都有 $$e^Xe^Y=e^{X+Y}$$。

*证明*。(i) 是定理 3.8 的改写。

(ii) 由 (i)，对小的 $$t$$，

$$e^{tX}e^{tY}=e^{\,t(X+Y)+\frac12t^2[X,Y]+O(t^3)},\qquad e^{-tX}e^{-tY}=e^{-t(X+Y)+\frac12t^2[X,Y]+O(t^3)}.$$

记 $$U=t(X+Y)+\frac12t^2[X,Y]+O(t^3)$$，$$V=-t(X+Y)+\frac12t^2[X,Y]+O(t^3)$$。由定理 3.8，

$$\log\bigl(e^{U}e^{V}\bigr)=U+V+\frac12[U,V]+\cdots.$$

其中 $$U+V=t^2[X,Y]+O(t^3)$$；而 $$[U,V]=O(t^3)$$——因为 $$U,V$$ 的首项是 $$t(X+Y)$$ 与 $$-t(X+Y)$$，二者交换，故 $$t$$ 阶与 $$t^2$$ 阶的贡献全部抵消。于是 $$\log(\cdots)=t^2[X,Y]+O(t^3)$$，除以 $$t^2$$ 令 $$t\to0$$ 即得。

(iii) 若 $$[X,Y]=0$$，则 $$\operatorname{ad}X$$ 与 $$\operatorname{ad}Y$$ 交换，级数可用二项式定理重排：$$e^{X}e^{Y}=\sum_{k,l}\frac{X^kY^l}{k!\,l!}=\sum_{m}\frac{(X+Y)^m}{m!}=e^{X+Y}$$（$$\frac{(X+Y)^m}{m!}$$ 的展开正是 $$\sum_{k+l=m}\frac{X^kY^l}{k!l!}$$，这里用到 $$X,Y$$ 交换，故绝对收敛的级数可以任意重排）。反之，若在 $$U$$ 内 $$e^Xe^Y=e^{X+Y}$$，把 $$X,Y$$ 换成 $$tX,tY$$（$$t$$ 小）：由 (i) 得 $$\frac{t^2}{2}[X,Y]+O(t^3)=0$$，除以 $$t^2$$ 令 $$t\to0$$，得 $$[X,Y]=0$$。$$\blacksquare$$

**这就是入口题 (d) 的答案。** 在单位元处求导，丢掉的是群的**全部乘法信息**，留下的只有向量空间 $$\mathfrak g$$。但 (ii) 表明：丢掉的二阶信息没有被扔掉，它被完整地编码进了括号 $$[X,Y]$$——括号就是"两个无穷小变换先后次序不同"所产生的那一点残余。至于三阶及以上的信息，定理 3.8 说它们**也由括号生成**（都是迭代括号），所以什么也没丢。于是：

**定理 3.10（BCH 的结果：局部由代数决定）**。

(a) **局部同构**。若 $$\mathfrak g\cong\mathfrak h$$ 分别是 Lie 群 $$G,H$$ 的 Lie 代数，则存在 $$e\in G$$、$$e\in H$$ 的邻域之间的微分同胚 $$\phi$$，满足 $$\phi(g_1g_2)=\phi(g_1)\phi(g_2)$$（只要两边都在邻域内），且 $$\phi\circ\exp_G=\exp_H\circ\varphi$$，其中 $$\varphi:\mathfrak g\to\mathfrak h$$ 是给定的 Lie 代数同构。这样的局部同构在重叠区域上唯一。

(b) **整体结论（Lie 第二定理，此处引用）**。设 $$G$$ 连通单连通、$$H$$ 任意 Lie 群。则每个 Lie 代数同态 $$\varphi:\operatorname{Lie}(G)\to\operatorname{Lie}(H)$$ 都是唯一一个 Lie 群同态 $$\Phi:G\to H$$ 的微分。推论：**连通单连通的 Lie 群若 Lie 代数同构，则自身同构**。

(c) **存在性（Lie 第三定理，此处引用）**。每个有限维实 Lie 代数都是某个连通单连通 Lie 群的 Lie 代数。证明路线：由 Ado 定理先把它实现为矩阵李代数 $$\mathfrak g\subseteq\mathfrak{gl}(n,\mathbb R)$$，取它在 $$GL(n,\mathbb R)$$ 中对应的连通子群 $$G_0$$，再取 $$G_0$$ 的万有覆叠群。

*证明* (a)。在指数坐标（推论 3.3）下定义 $$\phi=\exp_H\circ\varphi\circ\log_G$$。要证它保乘法。设 $$g_1,g_2$$ 都在 $$e$$ 附近，写 $$g_i=\exp_G X_i$$（$$X_i\in\mathfrak g$$ 小）。则由定理 3.8，

$$g_1g_2=\exp_G\Bigl(X_1+X_2+\frac12[X_1,X_2]+\cdots\Bigr),$$

其中每一项都是迭代括号。把 $$\log_G$$ 作用上去，即得 $$\log_G(g_1g_2)$$ 的 BCH 展开式；再作用 $$\varphi$$——因为 $$\varphi$$ 是 Lie 代数同态（保线性、保括号），迭代括号被逐项送到对应位置，于是

$$\varphi\bigl(\log_G(g_1g_2)\bigr)=\log_H\bigl(\exp_H\varphi(X_1)\cdot\exp_H\varphi(X_2)\bigr).$$

两边同时作用 $$\exp_H$$，左端是 $$\phi(g_1g_2)$$，右端是 $$\phi(g_1)\phi(g_2)$$。唯一性来自 $$\log$$ 在重叠区域上由 $$\exp$$ 唯一确定（定义 3.1 之后的说明）。$$\blacksquare$$

*(b)(c) 的完整证明超出本章（需要覆叠空间理论与 Frobenius 定理的配合，见第 50 章的覆叠空间部分与知识库 `李群/lie-groups/ch03`）。本章只使用它们的结论，并明确标记为引用——它们是"Lie 代数决定单连通 Lie 群"这一事实的全部依据。*

### 3.5 指数映射的像：它到底覆盖了多少 $$G$$

定理 3.10 说的是"局部由代数决定"。那么**整体**呢？最直接的追问是：$$\exp$$ 能覆盖整个 $$G$$ 吗？答案分两半——紧的时候能，不紧的时候未必。

**定理 3.11（$$\exp:\mathfrak{sl}(2,\mathbb R)\to SL(2,\mathbb R)$$ 不是满射）**。设 $$X\in\mathfrak{sl}(2,\mathbb R)$$，即 $$X$$ 是实 $$2\times2$$ 矩阵且 $$\operatorname{tr}X=0$$。则

$$\operatorname{tr}\bigl(\exp X\bigr)\ge-2,$$

且等号成立时必有 $$\exp X=-I$$。特别地，矩阵

$$A=\begin{bmatrix}-1&1\\0&-1\end{bmatrix}\in SL(2,\mathbb R)$$

满足 $$\operatorname{tr}A=-2$$ 而 $$A\ne-I$$，故 $$A$$ **不在** $$\exp$$ 的像中。

*证明*。$$\operatorname{tr}X=0$$ 时 $$X$$ 的特征多项式是 $$\lambda^2+\det X$$，故两个特征值之和为零，记为 $$\alpha,-\alpha$$。$$X$$ 是实矩阵：若 $$\alpha\notin\mathbb R$$，则两个特征值必须互为共轭，即 $$-\alpha=\overline\alpha$$，也就是 $$\operatorname{Re}\alpha=0$$。于是只剩两种可能。

**情形一：$$\alpha\in\mathbb R$$。** 把 $$X$$ 复化后上三角化（定理 3.5 证明里用过的论证）：$$\exp X$$ 的特征值恰为 $$X$$ 的特征值的指数，即 $$e^{\alpha}$$ 与 $$e^{-\alpha}$$。故

$$\operatorname{tr}\exp X=e^{\alpha}+e^{-\alpha}=2\cosh\alpha\ge2.$$

**情形二：$$\alpha=i\beta$$，$$\beta\in\mathbb R$$。** 同理 $$\operatorname{tr}\exp X=e^{i\beta}+e^{-i\beta}=2\cos\beta\ge-2$$。

两种情形都给出 $$\operatorname{tr}\exp X\ge-2$$。若等号成立，则只可能是情形二且 $$\cos\beta=-1$$，即 $$\beta=\pi(2k+1)$$。此时 $$X$$ 的两个特征值 $$\pm i\pi(2k+1)$$ 互不相同，$$X$$ 在 $$\mathbb C$$ 上可对角化，$$\exp X$$ 也可对角化，而它的两个特征值都是 $$e^{\pm i\pi(2k+1)}=-1$$，故 $$\exp X=-I$$。

最后核对 $$A$$：$$\det A=(-1)\cdot(-1)-1\cdot0=1$$，故 $$A\in SL(2,\mathbb R)$$；$$\operatorname{tr}A=-2$$；但 $$A+I=\begin{bmatrix}0&1\\0&0\end{bmatrix}\ne0$$，故 $$A\ne-I$$。由已证的必要条件，$$A$$ 不在 $$\exp$$ 的像中。$$\blacksquare$$

**注**。这个定理说明 $$\exp$$ 的像被 $$\operatorname{tr}\ge-2$$ 这张半平面挡住。$$SL(2,\mathbb R)$$ 是连通的（由极分解 $$K\exp(\mathfrak p)$$ 可见），所以这不是连通性的障碍，而是 $$\log$$ 远离 $$I$$ 时的多值与 $$\exp$$ 的折叠造成的。它还说明：生成连通群必须用"有限个指数之积"，一个指数不够。

**定理 3.12（指数映射的像：生成性与满射性）**。

(a) 若 $$G$$ 连通，则 $$G$$ 中**每个**元素都是有限个指数映射值的乘积：

$$g=\exp X_1\exp X_2\cdots\exp X_k,\qquad X_i\in\mathfrak g.$$

(b) 若 $$G$$ 连通**紧**（如 $$U(n)$$、$$SU(n)$$、$$SO(n)$$），则 $$\exp:\mathfrak g\to G$$ 是**满射**。

*证明*。(a) 记

$$H=\{\exp X_1\cdots\exp X_k\ :\ k\ge0,\ X_i\in\mathfrak g\},$$

其中 $$k=0$$ 的空乘积理解为 $$e$$。$$H$$ 是子群：乘法封闭是定义本身；逆元由 $$\exp(X)^{-1}=\exp(-X)$$（(R4)(ii)）仍在同一形式内。

$$H$$ 是**开**子群。由 (R4)(iii)，$$\exp$$ 把 $$\mathfrak g$$ 中含 $$0$$ 的某个邻域 $$W$$ 微分同胚地映到 $$G$$ 中含 $$e$$ 的邻域，而 $$\exp(W)\subseteq H$$，故 $$H$$ 含 $$e$$ 的一个开邻域；对任意 $$h\in H$$，$$h\exp(W)\subseteq H$$ 是 $$h$$ 的开邻域。于是 $$H$$ 开。

拓扑群的**开子群必闭**：其余陪集 $$gH$$ 是 $$H$$ 的左平移，因而是开的，补集 $$G\setminus H=\bigcup_{g\notin H}gH$$ 是开集之并，故 $$H$$ 闭。

$$H$$ 既开又闭，$$G$$ 连通且 $$H\ne\varnothing$$（含 $$e$$），故 $$H=G$$。

(b) 对 $$SU(n)$$ 证（$$U(n)$$、$$SO(n)$$ 同理）。设 $$U\in SU(n)$$。$$U$$ 正规，由谱定理可酉对角化：存在酉矩阵 $$P$$ 与实数 $$\theta_1,\dots,\theta_n$$，使

$$U=P\operatorname{diag}\bigl(e^{i\theta_1},\dots,e^{i\theta_n}\bigr)P^{-1}.$$

$$\det U=1$$ 即 $$e^{i(\theta_1+\cdots+\theta_n)}=1$$，故 $$\sum_j\theta_j\in2\pi\mathbb Z$$。把其中一个角改成 $$\theta_j-2\pi$$（这不改变 $$e^{i\theta_j}$$，因而不改变 $$U$$），可使 $$\sum_j\theta_j=0$$ 精确成立。令

$$X=P\operatorname{diag}(i\theta_1,\dots,i\theta_n)P^{-1}.$$

$$i\theta_j$$ 是纯虚数，故 $$X^*=P\operatorname{diag}\bigl(\overline{i\theta_j}\bigr)P^{-1}=P\operatorname{diag}(-i\theta_j)P^{-1}=-X$$；又 $$\operatorname{tr}X=i\sum_j\theta_j=0$$。于是 $$X\in\mathfrak{su}(n)$$，而

$$\exp X=P\operatorname{diag}\bigl(e^{i\theta_1},\dots,e^{i\theta_n}\bigr)P^{-1}=U.$$

$$SO(n)$$ 同理：任一 $$R\in SO(n)$$ 正交相似于旋转块的直和 $$\operatorname{diag}(R_{t_1},\dots,R_{t_m})\oplus[1]$$（$$n$$ 为奇数时末尾是 $$1\times1$$ 的块），把二维块 $$R_{t_j}$$ 换成 $$\exp(t_jJ)$$、一维块换成 $$\exp(0)$$，所得 $$X$$ 反对称且 $$\exp X=R$$。$$U(n)$$ 情形省去"把 $$\sum_j\theta_j$$ 调成 $$0$$"这一步。$$\blacksquare$$

**对照**：定理 3.11 说非紧时 $$\exp$$ 可能不满，定理 3.12(b) 说紧时一定满。$$\mathrm{Aff}(n)$$、Galileo 群、$$SE(3)$$ 等非紧群属于前者。

### 3.6 两个必须回头的接口

本章有两处旧账要还：第 04 章"求导得 $$i$$"，第 44 章"$$[x,p]=i\hbar$$"。前者是本章最小、最完整的例子；后者在这里第一次有了名字。

**定理 3.13（最小例子：$$\mathfrak{so}(2)$$、$$J$$ 与 $$i$$）**。

(i) 记 $$J=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$$。则 $$\mathfrak{so}(2)=\mathbb RJ$$，且

$$\exp(\theta J)=\cos\theta\,I+\sin\theta\,J=R_\theta.$$

映射 $$a+bi\mapsto aI+bJ$$ 是 $$\mathbb C\to M_2(\mathbb R)$$ 的单代数同态，其像为 $$\{aI+bJ\}$$；在这个同构下 $$J$$ 对应 $$i$$。

(ii) 设 $$\rho:\mathfrak g\to\mathfrak{gl}(V)$$ 是实 Lie 代数到一个**反自伴**算子空间的表示，即 $$\rho(X)^*=-\rho(X)$$ 对一切 $$X$$ 成立。则 $$\rho(X)$$ 的每个特征值都是纯虚数。

(iii) 第 04 章的算子 $$D=\dfrac{d}{d\theta}$$ 是 $$\mathfrak{so}(2)$$ 的生成元在 $$L^2(S^1)$$ 上的表示像，其谱为 $$i\mathbb Z$$。

*证明*。(i) 第 48 章的推论 3.20(ii) 已给出 $$\mathfrak{so}(2)=\{X:X^{\mathsf T}=-X\}$$，而 $$2\times2$$ 实反对称矩阵恰有 $$\theta J$$ 的形状，故 $$\mathfrak{so}(2)=\mathbb RJ$$。由 $$J^2=-I$$ 得 $$J^{2m}=(-1)^mI$$、$$J^{2m+1}=(-1)^mJ$$；代入 (R4)(v) 的级数并按奇偶分组，

$$\exp(\theta J)=\Bigl(\sum_{m\ge0}\frac{(-1)^m\theta^{2m}}{(2m)!}\Bigr)I+\Bigl(\sum_{m\ge0}\frac{(-1)^m\theta^{2m+1}}{(2m+1)!}\Bigr)J=\cos\theta\,I+\sin\theta\,J.$$

（这就是第 04 章的定理 3.6，这里用 $$J^2=-I$$ 把它重新组织了一遍。）代数同态部分直接相乘：

$$(aI+bJ)(cI+dJ)=ac\,I+(ad+bc)J+bd\,J^2=(ac-bd)I+(ad+bc)J,$$

与复数乘法 $$(a+bi)(c+di)=(ac-bd)+(ad+bc)i$$ 逐项一致；又 $$aI+bJ=0$$ 迫使 $$a=b=0$$，故是单同态。

**第 04 章那句"对 $$\theta J$$ 求导得 $$i$$"，准确含义是**：$$\frac{d}{d\theta}\big\vert_{\theta=0}\exp(\theta J)=J$$，而 $$J$$ 在上述同构下**就是** $$i$$。求导把旋转群 $$SO(2)$$ 压成了一维代数 $$\mathbb RJ$$，而这个代数配上同构之后就是复数的虚轴。

(ii) 设 $$\rho(X)v=\lambda v$$，$$v\ne0$$。两边与 $$v$$ 取内积：

$$\lambda\lVert v\rVert^2=\langle\rho(X)v,v\rangle=-\langle v,\rho(X)v\rangle=-\overline\lambda\lVert v\rVert^2,$$

故 $$\lambda=-\overline\lambda$$，即 $$\operatorname{Re}\lambda=0$$。

(iii) 第 04 章已算出 $$De^{ik\theta}=ik\,e^{ik\theta}$$，且 $$D$$ 的谱恰为 $$i\mathbb Z$$。要把它纳入本定理的框架，只需说明 $$D$$ 确实是 $$\mathfrak{so}(2)$$ 的生成元在一个表示下的像：规定 $$\rho(J)=D$$。这不是任意的人为对应，因为 (R4)(iv)（自然性）要求它与群表示相容——

$$\rho\bigl(\exp(tJ)\bigr)=e^{t\rho(J)}=e^{tD}.$$

左边是圆周上的旋转 $$R_t$$，右边作用在函数上正是平移：$$(e^{tD}f)(\theta)=f(\theta+t)$$。两边一致，故 $$\rho$$ 合法。$$e^{tD}$$ 保 $$L^2(S^1)$$ 的范数（平移不改变积分），是酉算子，由分部积分它的生成元 $$D$$ 反自伴。于是由 (ii)，$$D$$ 的谱必落在虚轴上——**这就是 $$ik$$ 里那个 $$i$$ 的代数来源**。

第 04 章给出的解释（整数性来自 $$e^{2\pi\lambda}=1$$ 的单值性）是**拓扑**来源：它决定谱是离散的格 $$i\mathbb Z$$ 而不是整条虚轴。两个来源互相独立、结论相容：**代数管"落在虚轴上"，拓扑管"落在哪些点"。**

**定理 3.14（Heisenberg 代数与 Heisenberg 群：第 44 章的回读）**。

设 $$\mathfrak h_3=\operatorname{span}_{\mathbb R}\{x,p,z\}$$，括号由

$$[x,p]=z,\qquad [z,x]=[z,p]=0$$

双线性延拓给出（这正是第 44 章的 定义 3.3 的Heisenberg代数，本章记作 Heisenberg 代数）。

(i) $$\mathfrak h_3$$ 幂零：下中心列 $$\mathfrak h_3^{1}=\mathfrak h_3$$、$$\mathfrak h_3^{2}=[\mathfrak h_3,\mathfrak h_3]=\mathbb Rz$$、$$\mathfrak h_3^{3}=0$$。

(ii) 因此 BCH 在二阶**精确**截断：对一切 $$A,B\in\mathfrak h_3$$，

$$\log\bigl(e^{A}e^{B}\bigr)=A+B+\frac12[A,B].$$

(iii) 于是 $$\exp:\mathfrak h_3\to H_3(\mathbb R)$$ 是整体微分同胚（有全局定义的光滑逆），群律在指数坐标 $$a=xX+pP+zZ$$ 下是

$$(x,p,z)\cdot(x',p',z')=\Bigl(x+x',\ p+p',\ z+z'+\frac12\bigl(xp'-px'\bigr)\Bigr).$$

(iv) 第 44 章的 Weyl 关系就是这条群律在量子力学表示下的样子。

*证明*。(i) 由括号表直接读出：$$[\mathfrak h_3,\mathfrak h_3]$$ 由 $$[x,p]=z$$ 张成，为 $$\mathbb Rz$$；再取一次括号落入 $$[\mathfrak h_3,\mathbb Rz]=0$$。

(ii) 由定理 3.8 与其后的"截断"论证：任取 $$A,B\in\mathfrak h_3$$，$$\operatorname{ad}A,\operatorname{ad}B$$ 的像都落在中心子代数 $$\mathbb Rz$$ 里，故它们的复合只要"两次相撞"就为零。Dynkin 公式中每一阶项都是 $$\operatorname{ad}A,\operatorname{ad}B$$ 的复合作用，故三阶及以上全为零。入口题 (b) 已把这件事实在 $$3\times3$$ 矩阵上算穿：$$e^{X}e^{Y}=I+X+Y+Z=e^{\,X+Y+\frac12Z}$$。

(iii) 给出矩阵实现：把 $$x,p,z$$ 分别送到

$$X=E_{12}=\begin{bmatrix}0&1&0\\0&0&0\\0&0&0\end{bmatrix},\quad P=E_{23}=\begin{bmatrix}0&0&0\\0&0&1\\0&0&0\end{bmatrix},\quad Z=E_{13}=\begin{bmatrix}0&0&1\\0&0&0\\0&0&0\end{bmatrix},$$

这确实保持括号（$$[E_{12},E_{23}]=E_{13}$$）。对 $$a=xX+pP+zZ$$，由 $$a^2=xp\,Z$$、$$a^3=0$$ 得

$$\exp(a)=I+xE_{12}+pE_{23}+\bigl(z+\tfrac12xp\bigr)E_{13}.$$

反过来，任一 $$M(\xi,\pi,\zeta)=I+\xi E_{12}+\pi E_{23}+\zeta E_{13}$$ 都等于 $$\exp\bigl(\xi X+\pi P+(\zeta-\tfrac12\xi\pi)Z\bigr)$$。故 $$\exp$$ 是 $$\mathfrak h_3$$ 到上单位三角群

$$H_3(\mathbb R)=\bigl\{I+\xi E_{12}+\pi E_{23}+\zeta E_{13}\bigr\}$$

的双射，且 $$\xi,\pi,\zeta$$ 给出全局光滑坐标（预像坐标为 $$\xi,\pi,\zeta-\tfrac12\xi\pi$$，是多项式因而光滑），逆也是多项式的。同一条计算给出群律 $$M(\xi,\pi,\zeta)M(\xi',\pi',\zeta')=M(\xi+\xi',\pi+\pi',\zeta+\zeta'+\xi\pi')$$；换回指数坐标 $$x=\xi,\ p=\pi,\ z=\zeta-\tfrac12\xi\pi$$，即得 (iii) 中那条式子。

(iv) 取 $$\mathfrak h_3$$ 的一个表示 $$\rho$$，使 $$\rho(x)=i\mathsf X$$、$$\rho(p)=i\mathsf P$$（$$\mathsf X,\mathsf P$$ 为位置与动量算子，自伴，故 $$\rho(x),\rho(p)$$ 反自伴，$$e^{s\rho(x)}=e^{is\mathsf X}$$ 是酉算子）。由 $$[\mathsf X,\mathsf P]=i\hbar I$$（第 44 章的 定义 3.2），

$$[\rho(x),\rho(p)]=[i\mathsf X,i\mathsf P]=-[\mathsf X,\mathsf P]=-i\hbar I=\rho(z),$$

即 $$\rho$$ 把中心元 $$z$$ 送到 $$-i\hbar I$$。注意 $$[\rho(x),\rho(p)]$$ 是中心元、与 $$\rho(x),\rho(p)$$ 都交换，故由 (ii) 可连续用两次：

$$e^{s\rho(x)}e^{t\rho(p)}e^{-s\rho(x)}e^{-t\rho(p)}=e^{\,st[\rho(x),\rho(p)]}=e^{-ist\hbar}I.$$

记 $$U(s)=e^{is\mathsf X}$$、$$V(t)=e^{it\mathsf P}$$，上式即

$$U(s)V(t)=e^{-i\hbar st}\,V(t)U(s),$$

正是第 44 章的 定义 3.5（Weyl 关系）。$$\blacksquare$$

**第 44 章的整条链在这里被重新组织了一遍。** $$[x,p]=z$$ 是维数最小的非交换幂零 Lie 代数（第 44 章的 命题 3.3）；它的指数化是 Heisenberg 群 $$H_3(\mathbb R)$$，而 $$\exp$$ 在这里是**整体**微分同胚——因为幂零使 BCH 变成有限多项式，没有收敛半径的麻烦；Weyl 关系是群律的酉表示；Stone–von Neumann 定理读作「这个 Lie 代数在中心元取 $$-i\hbar I$$ 的不可约酉表示，在同构意义下唯一」。第 44 章那条 $$[x,p]=i\hbar$$ 里的 $$i$$，与定理 3.13 里第 04 章的 $$i$$ 是**同一个** $$i$$：反自伴算子的谱落在虚轴上（定理 3.13(ii)），而指数化把谱点 $$\lambda$$ 送到 $$e^{\lambda}$$；于是"谱落在单位圆上"与"生成元自带一个 $$i$$"是同一件事的两种说法。

**本节收束。** 把 §3.3–§3.6 合起来看：**局部**完全由括号决定（定理 3.8、3.10）；**整体**分两层——连通群中每个元素是有限个指数之积（定理 3.12(a)），而覆叠、基本群、$$\exp$$ 是否满射完全不受代数控制（定理 3.11、推论 3.7）。第 25、26 章已经算过整体那一层；第 56 章要回到代数这一层，把实 Lie 代数复化，把这里的"谱"升级成"权"与"根"——那时 Cartan 子代数扮演的角色，正是"一族可以同时对角化的生成元"。

## 四、几何与物理直觉 (Intuition)

### 4.1 几何图像：把切平面"卷"到群上

$$\exp:\mathfrak g\to G$$ 在 $$0$$ 附近是微分同胚（(R4)(iii)），意思很具体：$$\mathfrak g$$ 是 $$G$$ 在 $$e$$ 处的切平面，$$\exp$$ 把这张平面（的一个小圆盘）**盖**到 $$G$$ 在 $$e$$ 附近的那一片上，而且是双射。整体上，$$\exp$$ 把 $$\mathfrak g$$ 里的每条直线 $$t\mapsto tX$$ 卷成 $$G$$ 上一条单参数子群；直线越走越远，卷上去的曲线可能绕回来、可能与别的曲线相撞。

三种典型形状，值得分别记住：

| 群 | $$\exp$$ 的形状 | 障碍 |
|---|---|---|
| $$U(1)=SO(2)$$ | $$\mathbb R$$ 螺旋地卷到圆上，核是 $$2\pi\mathbb Z$$ | 覆叠，$$\exp$$ 不单射 |
| $$SL(2,\mathbb R)$$ | 覆盖不满，像被 $$\operatorname{tr}\ge-2$$ 挡住（定理 3.11） | 对数不可解，$$\exp$$ 不满射 |
| $$H_3(\mathbb R)$$ | 整体微分同胚，$$\mathfrak h_3$$ 与群是同一片 $$\mathbb R^3$$（定理 3.14） | 无——幂零使 BCH 变成多项式 |

第一行是第 04 章的图：直线卷到圆上，卷了无限多层；这说明了为什么单靠 $$\exp$$ 处理**整体**问题不够用。第二行是本章新看到的：直线甚至卷不满。第三行是最舒服的情形——幂零群上 $$\exp$$ 是一张全局坐标卡，矩阵指数与矩阵对数互为逆，没有收敛半径的顾虑。

### 4.2 括号的几何：一个"四步小方块"

推论 3.9(ii) 有一个完全几何的读法。取 $$X,Y\in\mathfrak g$$ 与小的 $$t$$，依次做四件事：沿 $$X$$ 的流走 $$t$$，沿 $$Y$$ 的流走 $$t$$，沿 $$X$$ 的流走 $$-t$$，沿 $$Y$$ 的流走 $$-t$$。四步走完**不**回到出发点，偏差是

$$\log\bigl(e^{tX}e^{tY}e^{-tX}e^{-tY}\bigr)=t^2[X,Y]+O(t^3),$$

即偏差是二阶的，方向恰是 $$[X,Y]$$。**Lie 括号就是"两条流先后次序不同"的残余。** 若两条流对易（$$[X,Y]=0$$），这个方块闭合，$$e^{tX}$$ 与 $$e^{tY}$$ 生成一片二维的交换面。

由此可以看清 Jacobi 恒等式的两个独立来源——它们说的是同一件事：

1. **分析来源**（本课程采用的定义，第 48 章的 定理 3.17）。括号是向量场的对易子 $$[X,Y]f=X(Yf)-Y(Xf)$$，Jacobi 恒等式是两次应用 Leibniz 律的直接后果。
2. **代数来源**。定理 3.8 的级数必须满足结合律——$$(e^{X}e^{Y})e^{Z}$$ 与 $$e^{X}(e^{Y}e^{Z})$$ 是同一个东西。把 BCH 代入并逐阶比较系数，会得到一族恒等式；其中第一个不被反交换性自动满足的，正是 Jacobi 恒等式。反过来，若括号不满足 Jacobi，BCH 级数就定义不出群。这条"群律的结合性 $$\leftrightarrow$$ 括号的 Jacobi"的对偶，才是"Lie 代数"这个概念必须把 Jacobi 写进公理的深层原因（本章不展开证明）。

顺带看一个可以当场验证的实例：**反交换性是"逆元存在"的无穷小影子**。取 $$Y=-X$$，由 (R4)(ii) 有 $$e^{X}e^{-X}=I$$，于是

$$0=\log\bigl(e^{X}e^{-X}\bigr)=X+(-X)+\frac12[X,-X]+(\text{三阶及以上})=\frac12\bigl(-[X,X]\bigr)+(\text{三阶及以上})$$

对所有小的 $$X$$ 成立，故 $$[X,X]=0$$；再由双线性得 $$[X,Y]=-[Y,X]$$。

### 4.3 物理：生成元、守恒量与那个 $$i$$

连续对称性在物理里的标准语言就是单参数变换群：一个连续参数（时间、转角、平移量）对应一族变换，它们构成单参数子群，而"无穷小变换"就是它的 Lie 代数元素——**生成元 (generator)**。

- 空间平移的生成元是动量；转动的生成元是角动量；时间演化的生成元是 Hamiltonian（第 32 章）。
- 定理 3.13(ii) 给出了量子力学里那个绕不开的 $$i$$ 的代数来源：量子力学要求变换是**酉**的，而酉群的 Lie 代数由**反自伴**算子组成，反自伴算子的特征值必然纯虚。于是每个"可观测量"（自伴算子）都要配一个反自伴的生成元，二者差一个 $$i$$。第 44 章的 $$[X,P]=i\hbar I$$ 就是这个 $$i$$ 的具体化身：它不是约定的产物，而是"酉表示 + 自伴可观测量"这条要求的必然后果。
- 第 46 章的 Stone 定理是同一件事的算子版本：自伴的 $$H$$ 生成单参数酉群 $$e^{-itH}$$，而 $$-iH$$ 才是（反自伴的）Lie 代数元素。
- 更精细的一层：相空间平移群 $$\mathbb R^2$$ 本身交换，可量子化后两个平移复合会"差一个相位"（Weyl 关系）。交换群要变成非交换，只能"往上加一个中心"——这是中心扩张，物理上叫反常，数学上就是定理 3.14 里的 Heisenberg 群。第 60 章的射影表示会把它讲成一般的机制。

### 4.4 三条主线在这里合流

- **几何**：切空间、局部微分同胚、覆叠、$$\exp$$ 的单射范围（§4.1）。
- **代数**：括号、迭代括号、BCH 的普适有理系数（§4.2）。
- **物理**：生成元、守恒量、量子化带来的 $$i$$ 与相位（§4.3）。

三者的交点是 BCH 公式：它说的是"群律完全由括号生成"，几何上即"局部由切空间决定"，物理上即"连续对称性完全由它的无穷小生成元决定"。本章的技术内容只有一条主线——**给"求导"这个单向操作配一台反向机器，再测量它在哪里失效**：在 $$0$$ 附近它完美（定理 3.10），在整体上它漏掉覆叠（推论 3.7），甚至漏掉一部分群（定理 3.11）。

## 五、经典问题精讲 (Classical Problems)

### 题 1：$$\exp:\mathfrak{so}(3)\to SO(3)$$ 的像与单射范围

**考点**：定理 3.12(b)（紧连通群上 $$\exp$$ 满射）与推论 3.7（覆叠在代数层不可见）。**位置**：§3.5，本章"整体 vs 局部"主线的最短实例。

**题**。证明：(a) $$\exp:\mathfrak{so}(3)\to SO(3)$$ 是满射；(b) 它**不是**单射，并求出全部碰撞点；(c) 它在开球 $$B_\pi=\{X\in\mathfrak{so}(3):\lVert X\rVert<\pi\}$$ 上是单射。

**解**。

(a) 给出一个不依赖定理 3.12 的直接论证（两者都对，直接论证还顺带给出轴角表示）。设 $$R\in SO(3)$$。它的特征多项式是三次实系数多项式，故至少有一个实特征值；由于 $$R$$ 正交，特征值的模都是 $$1$$，实特征值只能是 $$\pm1$$。又 $$\det R=1$$ 是三个特征值之积，而三个特征值的乘积也等于（实特征值）$$\,\times\,$$（一对共轭复特征值的积）。复特征值成共轭对时其积为模的平方，是正数；若实特征值是 $$-1$$，则另两个特征值之积必须为 $$-1$$，与"共轭对之积为正"矛盾。故实特征值是 $$1$$。

取单位向量 $$n$$ 使 $$Rn=n$$。在 $$n^\perp$$ 上，$$R$$ 限制为 $$n^\perp$$ 的一个保向正交变换（因为 $$\det R=1$$ 且 $$Rn=n$$），而 $$n^\perp$$ 是二维的，故它是旋转 $$R_{n,\theta}$$。于是

$$R=R_{n,\theta}=\exp\bigl(\theta(n_1J_1+n_2J_2+n_3J_3)\bigr),$$

最后一步是推论 3.7 里 $$\exp(tJ_3)=R_z(t)$$ 的共轭版本（把 $$e_3$$ 方向旋转到 $$n$$）。所以 $$\exp$$ 满射。

(b) 由推论 3.7，$$\exp(2\pi J_3)=R_z(2\pi)=I=\exp(0)$$，故 $$\exp$$ 不是单射。一般地，对 $$X=\theta(n_1J_1+n_2J_2+n_3J_3)$$（$$\lVert n\rVert=1$$），

$$\exp\bigl(X+2\pi k\,(n_1J_1+n_2J_2+n_3J_3)\bigr)=\exp(X)\qquad(k\in\mathbb Z),$$

因为 $$\exp$$ 把沿 $$n$$ 方向的直线送到单参数子群 $$t\mapsto R_{n,t}$$，而它是 $$2\pi$$ 周期的。故 $$\exp$$ 的每条纤维至少含一个无穷等差数列；$$\exp^{-1}(I)=\{2\pi k\,(n_1J_1+n_2J_2+n_3J_3):k\in\mathbb Z,\ \lVert n\rVert=1\}$$ 就是所有半径是 $$2\pi$$ 的整数倍的"球面"之并。

(c) 设 $$\exp(X)=\exp(Y)=R$$ 且 $$\lVert X\rVert,\lVert Y\rVert<\pi$$。写 $$X=\theta n\cdot J$$，其中 $$\theta=\lVert X\rVert\in[0,\pi)$$、$$n$$ 是单位向量（$$X=0$$ 时取 $$\theta=0$$，任意 $$n$$）。由 (a) 的论证，$$R=R_{n,\theta}$$ 是绕 $$n$$ 转 $$\theta$$ 的旋转。类似地 $$R=R_{m,\varphi}$$，$$\varphi=\lVert Y\rVert\in[0,\pi)$$。

若 $$\theta=0$$ 则 $$R=I$$，此时 $$R$$ 的特征值 $$1$$ 重数为 $$3$$，故 $$\varphi=0$$，即 $$X=Y=0$$。若 $$\theta\in(0,\pi)$$，则 $$\sin\theta>0$$，$$R$$ 的特征值 $$1$$ 的重数为 $$1$$，其单位特征向量是 $$\pm n$$。从 $$R-R^{\mathsf T}=2\sin\theta\,[n]_\times$$ 读出 $$n$$ 的定向，再用 $$\operatorname{tr}R=1+2\cos\theta$$ 解出 $$\theta\in(0,\pi)$$。于是 $$(n,\theta)$$ 被 $$R$$ 唯一决定，同理 $$(m,\varphi)$$ 被 $$R$$ 唯一决定，两者相同，$$X=Y$$。$$\blacksquare$$

**注**：半径 $$\pi$$ 是精确的边界——$$\exp(\pi J_3)=\exp(-\pi J_3)$$，两侧在边界上撞在一起。这就是"单射球"的半径不能扩大的原因，也是 $$\mathbb{RP}^3$$ 要把 $$S^3$$ 的对径点粘起来的无穷小影子（第 52 章）。

### 题 2：什么时候 $$e^{A}e^{B}$$ 精确等于 $$e^{A+B+\frac12[A,B]}$$

**考点**：定理 3.8 的 BCH 级数与"截断"条件。**位置**：§3.4；这题同时是第 44 章 命题 3.6（对易关系 $$\Rightarrow$$ Weyl 关系）的核心引理。

**题**。设 $$A,B\in M_n(\mathbb R)$$，记 $$C=[A,B]$$，并设 $$[C,A]=[C,B]=0$$（即 $$C$$ 与 $$A,B$$ 都交换）。证明

$$e^{A}e^{B}=e^{\,A+B+\frac12C},\qquad\text{以及}\qquad e^{A}e^{B}e^{-A}e^{-B}=e^{C}.$$

**解**。思路：BCH 的每一项都是迭代括号；只要每个三阶及以上的迭代括号都含一格"$$[\cdot,C]$$"，它们就全为零，级数便在二阶截断。

**第一步：$$e^{A}e^{B}=e^{A+B+\frac12C}$$。** 由定理 3.8，

$$\log\bigl(e^{A}e^{B}\bigr)=A+B+\frac12C+\sum_{n\ge3}(\text{含 }A,B\text{ 的 }n\text{ 重迭代括号}).$$

每个 $$n\ge3$$ 的迭代括号都不是裸的 $$[A,B]$$，而是把 $$[A,B]=C$$ 再与某个东西括一次以上。由 Dynkin 公式，$$n$$ 阶项可写成 $$\operatorname{ad}$$ 的复合作用在 $$A$$ 或 $$B$$ 上，形如

$$(\operatorname{ad}U_1)(\operatorname{ad}U_2)\cdots(\operatorname{ad}U_{n-1})(V),\qquad U_i,V\in\{A,B\},\ n-1\ge2.$$

这里至少有两层 $$\operatorname{ad}$$，故展开后每一项都含一格把已经产生的中间括号（其中必有一个是 $$C$$，或 $$C$$ 的倍数）再括一次的动作，于是都等于 $$0$$（$$[C,A]=[C,B]=0$$）。故三阶及以上全消失，得 $$e^{A}e^{B}=e^{A+B+\frac12C}$$。

（一个更贴近计算的验证：把 $$A,B$$ 换成 $$tA,tB$$，对 $$F(t)=e^{tA}e^{tB}$$ 有 $$F^{-1}F'=e^{-tB}Ae^{tB}+B$$。因为 $$\frac{d}{ds}\big\vert_se^{-sB}Ae^{sB}=e^{-sB}[A,B]e^{sB}=C$$ 与 $$s$$ 无关，积分得 $$e^{-tB}Ae^{tB}=A+t[A,B]$$，故

$$F^{-1}F'=A+B+t[A,B],$$

右端对不同的 $$t$$ 相互交换（都是 $$A+B$$ 与中心元 $$C=[A,B]$$ 的多项式），故可直接积分 $$F(t)=\exp\bigl(t(A+B)+\frac{t^2}{2}[A,B]\bigr)$$；取 $$t=1$$ 即得。）

**第二步：$$e^{A}e^{B}e^{-A}e^{-B}=e^{C}$$。** 由第一步，

$$e^{A}e^{B}=e^{A+B+\frac12C},\qquad e^{-A}e^{-B}=e^{-(A+B)+\frac12C}.$$

注意 $$[-A,-B]=[A,B]=C$$，故第二个指数的修正项也是 $$+\frac12C$$。记 $$U=A+B+\frac12C$$、$$V=-(A+B)+\frac12C$$。因为 $$C$$ 与 $$A,B$$ 都交换，$$U,V$$ 都是 $$A+B$$ 与 $$C$$ 的多项式，故 $$[U,V]=0$$；于是由 (R4)(ii) 的加法性（或把第一步再用一次），

$$e^{A}e^{B}e^{-A}e^{-B}=e^{U}e^{V}=e^{U+V}=e^{C}.$$

$$\blacksquare$$

**关键 leap**：不要去展开两边的级数逐项对消，而是**先判断 BCH 截断在哪一阶**。判据是"是否还有非线性独立的迭代括号"：一旦 $$[A,B]$$ 是中心元，所有更高阶项都死掉。

### 题 3：闭子群的 Lie 代数与 $$SU(2)$$ 的极大环面

**考点**：定理 3.4 的一般化（从矩阵群推广到任意闭子群）。**位置**：§3.3，把"求导 $$+$$ 反向验证"这套算法搬到抽象群上。

**题**。(a) 设 $$G$$ 是 Lie 群，$$H\subseteq G$$ 是闭子群。证明

$$\operatorname{Lie}(H)=\bigl\{X\in\operatorname{Lie}(G)\ :\ \exp_G(tX)\in H\ \text{对一切 }t\in\mathbb R\bigr\}.$$

(b) 取 $$T=\{D_\theta:\theta\in\mathbb R\}\subseteq SU(2)$$，其中 $$D_\theta=\begin{bmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{bmatrix}$$。证明 $$T\cong U(1)$$，并算出 $$\operatorname{Lie}(T)$$ 在 $$\mathfrak{su}(2)$$ 的基 $$\{S_1,S_2,S_3\}$$ 下的表达式。

**解**。

(a) **($$\subseteq$$)** 设 $$X\in\operatorname{Lie}(H)=T_eH$$。由 (R2)（即第 48 章的 定理 3.22），$$H$$ 上以 $$X$$ 为初速度的单参数子群是 $$\exp_H(tX)$$；而 $$H$$ 的单参数子群也是 $$G$$ 的单参数子群（同一条曲线，同一个初速度），由 $$G$$ 中单参数子群的唯一性，$$\exp_H(tX)=\exp_G(tX)$$。曲线整条在 $$H$$ 内，故 $$\exp_G(tX)\in H$$。

**($$\supseteq$$)** 反之，若 $$\exp_G(tX)\in H$$ 对一切 $$t$$，则 $$t\mapsto\exp_G(tX)$$ 是 $$H$$ 内一条光滑曲线（$$H$$ 是闭子群，由 Cartan 闭子群定理它是嵌入子流形），在 $$t=0$$ 处切向量为 $$\frac{d}{dt}\big\vert_0\exp_G(tX)=X$$，故 $$X\in T_eH=\operatorname{Lie}(H)$$。

(b) 先验证 $$D_\theta\in SU(2)$$：$$\overline{D_\theta}^{\mathsf T}D_\theta=\operatorname{diag}(e^{-i\theta},e^{i\theta})\operatorname{diag}(e^{i\theta},e^{-i\theta})=I$$，且 $$\det D_\theta=e^{i\theta}e^{-i\theta}=1$$。又 $$D_\theta D_\phi=D_{\theta+\phi}$$、$$D_0=I$$、$$D_\theta^{-1}=D_{-\theta}$$，故 $$T\cong U(1)$$。

再算 $$\operatorname{Lie}(T)$$：取 $$\theta$$ 的一次项，

$$\frac{d}{d\theta}\Big\vert_{\theta=0}D_\theta=\begin{bmatrix}i&0\\0&-i\end{bmatrix}=i\sigma_3.$$

$$i\sigma_3$$ 反厄米（$$\overline{i\sigma_3}^{\mathsf T}=\overline{i\sigma_3}=-i\sigma_3$$）、迹零，故属于 $$\mathfrak{su}(2)$$；由 (a)，$$\operatorname{Lie}(T)=\mathbb R\cdot i\sigma_3$$，一维。用 $$S_3=-\frac i2\sigma_3$$ 即 $$\sigma_3=2iS_3$$ 换算：

$$i\sigma_3=i\cdot2iS_3=-2S_3,$$

故 $$\operatorname{Lie}(T)=\mathbb R S_3$$——它正是 $$\mathfrak{su}(2)$$ 里与第三方向对应的那条直线。$$\blacksquare$$

**注**：$$T$$ 是 $$SU(2)$$ 的**极大环面**（能把 $$\mathfrak{su}(2)$$ 同时对角化的那一族元素），商 $$SU(2)/T\cong S^2$$ 正是第 52 章 Hopf 纤维化的底空间。$$\operatorname{Lie}(T)$$ 这条直线就是把 $$\mathfrak{su}(2)$$ 分成"对角部分"与"非对角部分"的起点——这个分解在复化以后就长成 Cartan 子代数与根空间（第 56 章）。

### 题 4：局部同构并不蕴含整体同构

**考点**：定理 3.10(a) 与覆叠的关系。**位置**：§3.4/§3.5，这是"局部 vs 整体"这条主线的正面靶子。

**题**。设 $$G,H$$ 是连通 Lie 群，$$\rho:G\to H$$ 是满射的 Lie 群同态，且 $$\rho$$ 是局部微分同胚（即每点附近都是到像的局部微分同胚）。证明 $$\rho_*:=(d\rho)_e:\mathfrak g\to\mathfrak h$$ 是 Lie 代数同构。再举两个例子说明**逆命题不成立**。

**解**。**第一步：$$\rho_*$$ 是线性同构。** $$\rho$$ 是局部微分同胚，故在每一点 $$(d\rho)_g:T_gG\to T_{\rho(g)}H$$ 都是线性同构，特别地 $$(d\rho)_e$$ 是线性同构；又 $$\dim\mathfrak g=\dim G=\dim H=\dim\mathfrak h$$（由逆函数定理，$$\rho$$ 的两边维数相同）。

**第二步：$$\rho_*$$ 保括号。** 对 $$X,Y\in\mathfrak g$$，取 $$G$$ 中对应的左不变向量场 $$X^X,Y^Y$$。由第 48 章的定理 3.16 的论证，$$\rho$$ 把 $$X^X$$ 推到 $$H$$ 上以 $$\rho_*X$$ 为初速度的左不变向量场（因为 $$\rho\circ L_g=L_{\rho(g)}\circ\rho$$），而对易子在推前下保持：$$\rho_*([X,Y])=[\rho_*X,\rho_*Y]$$。故 $$\rho_*$$ 是 Lie 代数同态，从而是 Lie 代数同构。

**逆命题不成立，两个反例。**

**例一：$$SU(2)\to SO(3)$$。** 由推论 3.7，$$\mathfrak{su}(2)\cong\mathfrak{so}(3)$$；但 $$SU(2)\cong S^3$$ 与 $$SO(3)\cong\mathbb{RP}^3$$ 不同胚（$$S^3$$ 单连通，$$\mathbb{RP}^3$$ 的基本群是 $$\mathbb Z/2$$，第 25、26 章），故不同构。障碍是覆叠：核是离散的 $$\{\pm I\}$$。

**例二：$$\mathbb R\to U(1)$$，$$\rho(t)=e^{2\pi it}$$。** 两者都是一维连通 Lie 群，Lie 代数都是一维交换的，故同构（一维交换 Lie 代数只有一种）。但 $$\mathbb R$$ 不是圆的同构：$$\rho$$ 的核是 $$\mathbb Z$$，而 $$\mathbb R$$ 中唯一有限子群是 $$\{0\}$$。障碍同样是覆叠。

**结论**：要得到整体同构，必须在定理 3.10(b) 的条件下补上**单连通性**这一条。（顺带注意：两个反例的障碍都是"核非平凡"，这正是覆叠空间理论的核心——局部同构给出的差一个离散中心的商，第 50 章已算过它的基本群。）$$\blacksquare$$

**关键 leap**：验证"保括号"时不必去碰抽象的对易子，用**左不变向量场**把一切都变成立即的：同态把左不变向量场推到左不变向量场，而推前与对易子交换。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.**（入口题的收尾）承入口题的 $$X=E_{12},\ Y=E_{23},\ Z=[X,Y]$$：(a) 算出 $$X^2,Y^2,XY,YX,Z$$；(b) 写出 $$\exp(X)$$、$$\exp(Y)$$、$$\exp(X)\exp(Y)$$ 与 $$\exp\bigl(X+Y+\frac12Z\bigr)$$；(c) 写出 $$e^{X}e^{Y}e^{-X}e^{-Y}$$。

**基2.** 求 $$\mathfrak{sl}(2,\mathbb R)$$、$$\mathfrak{so}(3)$$、$$\mathfrak{su}(2)$$ 各一组基与维数。

**基3.** 证明：(a) 若 $$\operatorname{tr}X=0$$ 则 $$\det(\exp X)=1$$；(b) $$\exp X$$ 总可逆，且 $$(\exp X)^{-1}=\exp(-X)$$。(b) 中不要引用 (R4)(ii)，改用推论 3.9(iii) 之外的另一种方式说说理由。

**基4.** 写出 $$\mathfrak h_3=\operatorname{span}\{x,p,z\}$$（$$[x,p]=z$$，$$z$$ 中心）的下中心列，说明它幂零；再算出 $$\exp(xX+pP+zZ)$$ 的矩阵（用入口题的 $$X,P,Z$$），并核对定理 3.14(iii) 的群律。

### 竞赛（本课目标难度）

**竞1.** 设 $$G$$ 是连通 Lie 群，$$H\subseteq G$$ 是**开**子群。证明 $$H$$ 是闭的，并且 $$H=G$$。

**竞2.** 求 $$\mathfrak{sp}(2n,\mathbb R)$$ 的维数；当 $$n=1$$ 时写出显式基，并证明 $$\mathfrak{sp}(2,\mathbb R)\cong\mathfrak{sl}(2,\mathbb R)$$。

**竞3.** 设 Lie 代数 $$\mathfrak g$$ 幂零，且下中心列满足 $$\mathfrak g^{c+1}=0$$（即幂零类为 $$c$$）。证明 BCH 级数在 $$n\le2c-1$$ 阶之后截断，即 $$\log(e^Xe^Y)$$ 是 $$X,Y$$ 的有限多项式。

**竞4.** 设 $$\rho:G\to H$$ 是 Lie 群同态，$$G$$ 连通。证明 $$\operatorname{Lie}(\ker\rho)=\ker\bigl(\rho_*:\mathfrak g\to\mathfrak h\bigr)$$。

**竞5.** 设 $$G$$ 是 Lie 群。证明：若 $$e^{X}e^{Y}=e^{Y}e^{X}$$ 对一切足够小的 $$X,Y\in\mathfrak g$$ 成立，则 $$\mathfrak g$$ 是交换 Lie 代数；反之亦然。

### 研究（通向下一章）

**研1.** 证明：若 $$G$$ 是连通紧 Lie 群，则 $$\exp:\mathfrak g\to G$$ 是满射。对 $$SU(n)$$ 与 $$SO(n)$$ 写出完整证明，并指出论证的哪一步在 $$SL(2,\mathbb R)$$ 上会失效。

**研2.** 设 $$\rho:\mathfrak g\to\mathfrak{gl}(V)$$ 是实 Lie 代数到反自伴算子的表示。证明 $$\rho(X)$$ 的谱落在虚轴上；再把 $$\mathfrak g$$ 复化，说明"虚谱"如何转化为"实谱"，并指出这与下一章的"权"和"根"是什么关系。

### 解答 (Solutions)

**解 基1.** 逐个算。$$E_{12}E_{12}=0$$（第 1 行第 2 列乘第 1 行全为零），$$E_{23}E_{23}=0$$，
$$E_{12}E_{23}=E_{13},\qquad E_{23}E_{12}=0.$$
(a) 于是 $$X^2=Y^2=YX=0$$，$$XY=E_{13}$$，$$Z=XY-YX=E_{13}$$。顺带记下后面要用的：$$Z^2=0$$，且 $$XZ=ZX=YZ=ZY=0$$（因为 $$E_{13}$$ 左乘任何 $$E_{1j}$$、右乘任何 $$E_{3j}$$ 都为零，而 $$X,Y,Z$$ 的列指标都 $$\le3$$、行指标都 $$\ge1$$，逐项核对即得）。

(b) 由 $$X^2=Y^2=0$$，幂级数只剩两项：$$\exp(X)=I+X$$、$$\exp(Y)=I+Y$$。于是
$$\exp(X)\exp(Y)=(I+X)(I+Y)=I+X+Y+XY=I+X+Y+Z.$$
再算 $$\exp\bigl(X+Y+\frac12Z\bigr)$$：记 $$W=X+Y+\frac12Z$$。由 (a)，
$$W^2=(X+Y)^2+\bigl(X+Y\bigr)\tfrac12Z+\tfrac12Z(X+Y)+\tfrac14Z^2=\bigl(XY+YX\bigr)+0+0+0=Z,$$
$$W^3=W\cdot W^2=WZ=XZ+YZ+\tfrac12Z^2=0.$$
故 $$\exp(W)=I+W+\frac12W^2=I+X+Y+\frac12Z+\frac12Z=I+X+Y+Z$$，与 $$\exp(X)\exp(Y)$$ 完全相等。

(c) 由 $$(X+Y)^2=Z$$、$$(X+Y)^3=0$$，
$$e^{X+Y}=I+(X+Y)+\tfrac12(X+Y)^2=I+X+Y+\tfrac12Z\ne I+X+Y+Z.$$
而
$$e^{-X}e^{-Y}=(I-X)(I-Y)=I-X-Y+XY=I-(X+Y)+Z,$$
故
$$e^{X}e^{Y}e^{-X}e^{-Y}=(I+X+Y+Z)\bigl(I-(X+Y)+Z\bigr).$$
设 $$A=X+Y$$，用 $$A^2=Z$$、$$AZ=ZA=0$$：
$$(I+A+Z)(I-A+Z)=(I+A)(I-A)+(I+A)Z+Z(I-A)+Z^2=(I-Z)+(Z)+(Z)+0=I+Z=e^{Z}.$$
（末一步用了 $$Z^2=0$$，故 $$e^{Z}=I+Z$$。）这正是推论 3.9(ii) 的 $$t=1$$ 情形：四步走完回到出发点差 $$[X,Y]=Z$$。

**解 基2.** 用定理 3.6 的算法，逐个在定义条件上求导。

$$\mathfrak{sl}(2,\mathbb R)=\Bigl\{\begin{bmatrix}a&b\\ c&-a\end{bmatrix}\Bigr\}$$：条件 $$\operatorname{tr}X=0$$ 就是 $$d=-a$$，故自由参数 $$a,b,c$$ 三个。取
$$H=\begin{bmatrix}1&0\\0&-1\end{bmatrix},\quad X_+=\begin{bmatrix}0&1\\0&0\end{bmatrix},\quad X_-=\begin{bmatrix}0&0\\1&0\end{bmatrix},$$
则 $$[H,X_+]=2X_+$$、$$[H,X_-]=-2X_-$$、$$[X_+,X_-]=H$$。（这组关系是 $$\mathfrak{sl}(2)$$ 表示论的标准记号，第 56 章会用到。）

$$\mathfrak{so}(3)=\{X:X^{\mathsf T}=-X\}$$：反对称实 $$3\times3$$ 矩阵由严格上三角的 $$\frac{3\cdot2}2=3$$ 个元素决定，基就是推论 3.7 的 $$J_1,J_2,J_3$$，维数 $$3$$。

$$\mathfrak{su}(2)=\{X:X^*=-X,\ \operatorname{tr}X=0\}$$：反厄米 $$2\times2$$ 复矩阵的复自由度为 $$2^2=4$$（实维数 $$4$$），再减去迹零的 $$1$$ 个实条件，实维数 $$3$$。Pauli 矩阵 $$\sigma_1,\sigma_2,\sigma_3$$ 厄米、迹零，故 $$S_k=\frac{1}{2i}\sigma_k$$ 反厄米、迹零，构成一组基。

三个都是 $$3$$ 维（$$\mathfrak{sl}(2,\mathbb R)$$ 与 $$\mathfrak{su}(2)$$ 复化后同构，见第 56 章）。

**解 基3.** (a) 由定理 3.5，$$\det(\exp X)=\exp(\operatorname{tr}X)=\exp(0)=1$$。

(b) 思路一（幂级数直接算）：记 $$S_N=\sum_{k=0}^{N}X^k/k!$$ 为部分和。在**交换**代数 $$\mathbb R[X]$$（$$X$$ 的多项式全体）里，标量恒等式 $$e^{x}e^{-x}=1$$ 逐次截断给出 $$S_N\cdot S'_N=I+O(\lVert X\rVert^{N+1})$$，其中 $$S'_N=\sum_{k=0}^N(-X)^k/k!$$。令 $$N\to\infty$$：因为两个级数都绝对收敛（$$\lVert X^k\rVert\le\lVert X\rVert^k$$，与 $$e^{\lVert X\rVert}$$ 比较），乘积的极限是 $$e^{X}e^{-X}=I$$，故 $$e^{-X}$$ 是 $$e^{X}$$ 的逆，$$e^{X}$$ 可逆。

思路二（用 (R4)(ii)）：$$[X,-X]=-[X,X]=0$$，故由推论 3.9(iii) 的"$$[A,B]=0\Rightarrow e^{A}e^{B}=e^{A+B}$$"，取 $$A=X$$、$$B=-X$$ 得 $$e^{X}e^{-X}=e^{0}=I$$。

两种思路的差别值得留意：思路一是一路纯级数运算，思路二把结论挂在括号上——后者正是本章的一般框架。

**解 基4.** 下中心列：$$\mathfrak h_3^{1}=\mathfrak h_3$$；由括号表 $$[x,p]=z$$、$$[z,\cdot]=0$$ 得
$$\mathfrak h_3^{2}=[\mathfrak h_3,\mathfrak h_3]=\mathbb Rz,\qquad \mathfrak h_3^{3}=[\mathfrak h_3,\mathfrak h_3^{2}]=[\mathfrak h_3,\mathbb Rz]=0.$$
故幂零类为 $$2$$（$$\mathfrak h_3^{3}=0$$）。

矩阵实现取入口题的 $$X=E_{12},\ P=E_{23},\ Z=E_{13}$$（$$[E_{12},E_{23}]=E_{13}$$）。设 $$a=xX+pP+zZ$$。由 $$E_{12}^2=E_{23}^2=E_{13}^2=0$$、$$E_{12}E_{23}=E_{13}$$、$$E_{23}E_{12}=0$$、$$E_{13}$$ 与其余相乘为零，
$$a^2=xp\,E_{13}=xp\,Z,\qquad a^3=0,$$
故
$$\exp(a)=I+a+\tfrac12a^2=I+xE_{12}+pE_{23}+\Bigl(z+\tfrac12xp\Bigr)E_{13}.$$
群律核对：记 $$M(\xi,\pi,\zeta)=I+\xi E_{12}+\pi E_{23}+\zeta E_{13}$$。直接相乘，
$$M(\xi,\pi,\zeta)M(\xi',\pi',\zeta')=M\bigl(\xi+\xi',\ \pi+\pi',\ \zeta+\zeta'+\xi\pi'\bigr).$$
而 $$\exp(a)=M\bigl(x,p,z+\frac12xp\bigr)$$，即 $$\zeta=z+\frac12xp$$。把 $$\zeta=z+\frac12xp$$、$$\zeta'=z'+\frac12x'p'$$ 代入：
$$\zeta''=z+\tfrac12xp+z'+\tfrac12x'p'+xp',$$
再换回 $$z''=\zeta''-\frac12x''p''$$（其中 $$x''=x+x'$$、$$p''=p+p'$$）：
$$z''=z+z'+\tfrac12xp+\tfrac12x'p'+xp'-\tfrac12(x+x')(p+p')=z+z'+\tfrac12\bigl(xp'-px'\bigr).$$
正是定理 3.14(iii)。

**解 竞1.** **思路**：连通性只用来排除"多个陪集并存"，所以先证开子群必闭，再说连通群只有一个陪集。

**第一步：$$H$$ 闭。** 对任意 $$g\in G$$，$$gH=L_g(H)$$ 是 $$H$$ 在微分同胚 $$L_g$$ 下的像，因而也是开集。于是
$$G\setminus H=\bigcup_{g\notin H}gH$$
是开集之并（每个 $$g\notin H$$ 的陪集 $$gH$$ 与 $$H$$ 不交，且这些陪集覆盖补集），故 $$G\setminus H$$ 开，即 $$H$$ 闭。

**第二步：$$H=G$$。** 用 $$H$$ 开 + $$G$$ 连通。$$G=H\cup(G\setminus H)$$ 是两个不相交开集之并；$$G$$ 连通且 $$H\ne\varnothing$$（含 $$e$$），故 $$G\setminus H=\varnothing$$，即 $$H=G$$。$$\blacksquare$$

**关键 leap**：把"开子群"与"闭"联系起来的那一步是 $$gH$$ 的开性——左平移是微分同胚，因而把开集送到开集。这条结论是定理 3.12(a) 证明的核心。

**解 竞2.** 记 $$\Omega=\begin{bmatrix}0&I_n\\-I_n&0\end{bmatrix}$$，则 $$\Omega^{\mathsf T}=-\Omega$$。由 §3.3 的计算，
$$X^{\mathsf T}\Omega+\Omega X=0\iff\Omega X=(X^{\mathsf T}\Omega^{\mathsf T})^{\mathsf T}=(\Omega X)^{\mathsf T}\iff\Omega X\ \text{对称}.$$
$$X\mapsto\Omega X$$ 可逆，故 $$\mathfrak{sp}(2n,\mathbb R)$$ 与 $$2n\times2n$$ 对称矩阵空间线性同构，维数
$$\dim\mathfrak{sp}(2n,\mathbb R)=\frac{2n(2n+1)}2=n(2n+1).$$

$$n=1$$ 时 $$\Omega=J=\begin{bmatrix}0&1\\-1&0\end{bmatrix}$$。设 $$X=\begin{bmatrix}a&b\\ c&d\end{bmatrix}$$，则
$$X^{\mathsf T}J+JX=\begin{bmatrix}a&c\\ b&d\end{bmatrix}\begin{bmatrix}0&1\\-1&0\end{bmatrix}+\begin{bmatrix}0&1\\-1&0\end{bmatrix}\begin{bmatrix}a&b\\ c&d\end{bmatrix}=\begin{bmatrix}-c&a\\ -d&b\end{bmatrix}+\begin{bmatrix}c&d\\ -a&-b\end{bmatrix}=\begin{bmatrix}0&a+d\\ -(a+d)&0\end{bmatrix}.$$
故条件等价于 $$a+d=\operatorname{tr}X=0$$，即 $$\mathfrak{sp}(2,\mathbb R)=\mathfrak{sl}(2,\mathbb R)$$，维数 $$3=1\cdot(2\cdot1+1)$$，与公式一致。这组基就取解 基2 中的 $$H,X_+,X_-$$。$$\blacksquare$$

**关键 leap**：不去数"条件个数"（那样容易漏掉约束间的相关性），而是把 $$\mathfrak{sp}$$ **线性同构**到对称矩阵空间——维数随即一目了然。$$n=1$$ 时两个小矩阵的加法只是一个自检。

**解 竞3.** **思路**：把 BCH 的每一项写成 $$\operatorname{ad}$$ 的复合，然后数一数"某个因子被重复了多少次"。

由定理 3.8 之后的说明（Dynkin 公式），BCH 展开中每个 $$n$$ 阶项都具有形状
$$(\operatorname{ad}U_1)(\operatorname{ad}U_2)\cdots(\operatorname{ad}U_{n-1})(V),\qquad U_i,V\in\{X,Y\}.$$
这里共 $$n-1$$ 个因子 $$U_1,\dots,U_{n-1}$$，每个是 $$X$$ 或 $$Y$$。

**关键观察**：$$\mathfrak g^{c+1}=0$$ 等价于说，对任何 $$Z_0\in\mathfrak g$$，
$$(\operatorname{ad}W_1)(\operatorname{ad}W_2)\cdots(\operatorname{ad}W_c)(Z_0)=[W_1,[W_2,[\cdots[W_c,Z_0]\cdots]]]\in\mathfrak g^{c+1}=0.$$
也就是说：**任一 $$\operatorname{ad}$$ 因子只要连续（不要求同一个）出现 $$c$$ 次，复合就是零**（每个中间括号都落在 $$\mathfrak g^{2},\mathfrak g^{3},\dots$$ 里）。

现在设 $$n-1\ge2c-1$$。若 $$X$$ 在 $$\{U_1,\dots,U_{n-1}\}$$ 中出现至多 $$c-1$$ 次，$$Y$$ 也至多 $$c-1$$ 次，则总数 $$n-1\le2(c-1)=2c-2<2c-1$$，矛盾。故 $$X$$ 出现至少 $$c$$ 次，或 $$Y$$ 出现至少 $$c$$ 次；由上面的观察，该 $$n$$ 阶项为 $$0$$。

于是级数在 $$n\le2c-1$$ 处截断，$$\log(e^{X}e^{Y})$$ 是 $$X,Y$$ 的有限多项式。取 $$\mathfrak h_3$$（$$c=2$$）得截断阶数 $$3$$；实际只需到 $$2$$ 阶（入口题 (b) 已验证）。$$\blacksquare$$

**关键 leap**：把"幂零"翻译成"$$\operatorname{ad}$$ 因子的重复次数上限"，而不是去分析展开式里括号的嵌套深度。

**解 竞4.** **思路**：把两个子空间都用"对一切 $$t$$ 的指数"刻画（题 3(a) 的一般化），再逐项对上。

**第一步：$$\operatorname{Lie}(\ker\rho)\subseteq\ker\rho_*$$。** 设 $$X\in\operatorname{Lie}(\ker\rho)=T_e(\ker\rho)$$。由题 3(a)，$$\exp_G(tX)\in\ker\rho$$ 对一切 $$t$$，即
$$\rho\bigl(\exp_G(tX)\bigr)=e_H\qquad\text{对一切 }t.$$
由 (R4)(iv)（自然性），左端 $$\rho(\exp_G(tX))=\exp_H\bigl(t\,\rho_*X\bigr)$$。两边在 $$t=0$$ 处求导：
$$\rho_*X=\frac{d}{dt}\Big\vert_{t=0}\exp_H(t\,\rho_*X)=\frac{d}{dt}\Big\vert_{t=0}e_H=0.$$
故 $$X\in\ker\rho_*$$。

**第二步：$$\ker\rho_*\subseteq\operatorname{Lie}(\ker\rho)$$。** 设 $$\rho_*X=0$$。则对一切 $$t$$，
$$\rho\bigl(\exp_G(tX)\bigr)=\exp_H(t\cdot0)=e_H,$$
即 $$\exp_G(tX)\in\ker\rho$$ 对一切 $$t$$。由题 3(a) 的另一半，$$X\in\operatorname{Lie}(\ker\rho)$$。

两步合起来即所求。顺带看到：$$\ker\rho_*$$ 是 $$\mathfrak g$$ 的一个 Lie 理想（同态的核），故它一定是某个闭子群的 Lie 代数——那个闭子群就是 $$\ker\rho$$。$$\blacksquare$$

**关键 leap**：两边都用"$$\exp(tX)\in K$$ 对一切 $$t$$"这把尺子去量，而不是去构造 $$\ker\rho$$ 的局部坐标。

**解 竞5.** **思路**：把 $$X,Y$$ 换成 $$tX,tY$$，让"小范围"这件事变成可以令 $$t\to0$$ 的极限。

**正向。** 设 $$X,Y\in\mathfrak g$$ 任意。则对一切充分小的 $$t$$，$$tX,tY$$ 都落在定理 3.8 的邻域里，且由假设 $$e^{tX}e^{tY}=e^{tY}e^{tX}$$。两边取 $$\log$$（定义 3.1，在 $$e$$ 附近有定义且唯一）：

$$\log\bigl(e^{tX}e^{tY}\bigr)=\log\bigl(e^{tY}e^{tX}\bigr).$$

由定理 3.8 把两边展开到二阶：

$$tX+tY+\frac12t^2[X,Y]+O(t^3)=tY+tX+\frac12t^2[Y,X]+O(t^3).$$

$$tX+tY$$ 被消去（向量加法交换），$$[Y,X]=-[X,Y]$$，故

$$t^2[X,Y]+O(t^3)=0.$$

除以 $$t^2$$ 并令 $$t\to0$$，得 $$[X,Y]=0$$。由于 $$X,Y$$ 任意，$$\mathfrak g$$ 交换。

**反向。** 设 $$\mathfrak g$$ 交换，即 $$[X,Y]=0$$ 对一切 $$X,Y$$。则由推论 3.9(iii)（$$[A,B]=0\Rightarrow e^{A}e^{B}=e^{A+B}$$），

$$e^{X}e^{Y}=e^{X+Y}=e^{Y+X}=e^{Y}e^{X}$$

对一切 $$X,Y\in\mathfrak g$$ 成立。$$\blacksquare$$

（更强的事实：若 $$\mathfrak g$$ 交换，则 $$G$$ 的单位连通分支是交换群——因为由定理 3.12(a)，该分支中每个元素是有限个 $$e^{X_i}$$ 之积，而它们两两交换。）

**关键 leap**：把"充分小"用**缩放参数** $$t$$ 显式写出来，好让 $$t^2$$ 项的系数被极限逼出来。这一步是与 BCH 打交道时的常用手法。

**解 研1.** **思路**：紧性的作用是把"矩阵"变成"可以用谱定理对角化的东西"，于是 $$\log$$ 可以在每个特征值上逐点取——**不需要**任何收敛半径。

**$$SU(n)$$ 的情形。** 设 $$U\in SU(n)$$。$$U$$ 正规（$$U^*U=UU^*=I$$），由谱定理存在酉矩阵 $$P$$ 使
$$U=P\operatorname{diag}\bigl(e^{i\theta_1},\dots,e^{i\theta_n}\bigr)P^{-1},\qquad\theta_j\in\mathbb R.$$
$$\det U=1$$ 即 $$e^{i(\theta_1+\cdots+\theta_n)}=1$$，故 $$\sum_j\theta_j\in2\pi\mathbb Z$$。取整数 $$k$$ 使 $$\sum_j\theta_j-2\pi k=0$$，把 $$\theta_1$$ 换成 $$\theta_1-2\pi k$$（$$e^{i\theta_1}$$ 不变）；重命名后不妨设 $$\sum_j\theta_j=0$$。令
$$X=P\operatorname{diag}(i\theta_1,\dots,i\theta_n)P^{-1}.$$
$$X^*=P\operatorname{diag}(\overline{i\theta_j})P^{-1}=P\operatorname{diag}(-i\theta_j)P^{-1}=-X$$，$$\operatorname{tr}X=i\sum_j\theta_j=0$$，故 $$X\in\mathfrak{su}(n)$$；而
$$\exp X=P\operatorname{diag}\bigl(e^{i\theta_j}\bigr)P^{-1}=U.$$

**$$SO(n)$$ 的情形。** 设 $$R\in SO(n)$$。实正交矩阵的特征值模为 $$1$$ 且成共轭对出现；由实 Schur 分解，$$R$$ 正交相似于若干二维旋转块与若干 $$1\times1$$ 块（对角元为 $$\pm1$$）的直和：

$$R=Q\operatorname{diag}(R_{t_1},\dots,R_{t_m},\ 1,\dots,1,\ -1,\dots,-1)Q^{\mathsf T}.$$

$$\det R=1$$ 迫使 $$-1$$ 的个数为**偶数**；把每两个 $$-1$$ 换成一块 $$R_\pi$$（$$=\operatorname{diag}(-1,-1)$$，正是转角 $$\pi$$ 的旋转块），便得到无 $$-1$$ 块的形式

$$R=Q\operatorname{diag}(R_{t_1},\dots,R_{t_m},1,\dots,1)Q^{\mathsf T}.$$

令 $$X=Q\operatorname{diag}(t_1J,\dots,t_mJ,0,\dots,0)Q^{\mathsf T}$$（$$J$$ 为解 基2 中的 $$\begin{bmatrix}0&-1\\1&0\end{bmatrix}$$）。每个 $$t_jJ$$ 反对称，末尾的零块也反对称，共轭不改变反对称性，故 $$X\in\mathfrak{so}(n)$$；而由推论 3.7 的 $$\exp(tJ)=R_t$$ 与分块指数的性质，
$$\exp X=Q\operatorname{diag}\bigl(\exp(t_1J),\dots,\exp(t_mJ),1,\dots,1\bigr)Q^{\mathsf T}=R.$$

**哪一步在 $$SL(2,\mathbb R)$$ 上失效。** 全部失效于"可**酉**（或正交）对角化"这一步：上面两个证明都把 $$U$$（或 $$R$$）化成了**正规**形式，而 $$\log$$ 在每一块上可以逐点取（$$R_{t}$$ 的 $$\log$$ 是 $$tJ$$，$$e^{i\theta}$$ 的 $$\log$$ 是 $$i\theta$$），完全不需要幂级数收敛。$$SL(2,\mathbb R)$$ 中的矩阵一般**不是**正规的，不能这样对角化；一旦改用 Jordan 形，就会出现 $$\log(\lambda I+N)=\log\lambda\cdot I+\sum_k(-1)^{k+1}N^k/(k\lambda^k)$$ 这样的级数，而它在 $$\lambda=-1$$ 且 $$N\ne0$$ 处发散——这正是定理 3.11 的算术内容。

**接下一章**：上面用到的关键工具是"把一族运算**同时**对角化"。在这套证明里它是谱定理；在一般紧 Lie 群上它变成**极大环面**定理（每个元素含于某个极大环面，而环面上的 $$\exp$$ 显然满射）。一旦把实 Lie 代数复化，这个"同时对角化"就长成了**Cartan 子代数 + 根空间分解**——那正是第 56 章的起点。

**解 研2.** **思路**：先用"取内积"把虚谱逼出来（核心是 $$\lambda=-\overline\lambda$$），再把 $$i$$ 从算子里搬到谱上，看它怎样把虚数变成实数。

**第一步：虚谱。** 设 $$\rho(X)v=\lambda v$$，$$v\ne0$$。由 $$\rho(X)^*=-\rho(X)$$，
$$\lambda\lVert v\rVert^2=\langle\rho(X)v,v\rangle=-\langle v,\rho(X)v\rangle=-\overline{\lambda}\lVert v\rVert^2,$$
故 $$\lambda=-\overline\lambda$$，即 $$\operatorname{Re}\lambda=0$$。于是 $$\sigma(\rho(X))\subseteq i\mathbb R$$。

**第二步：复化把虚谱变成实谱。** 令 $$\mathfrak g_{\mathbb C}=\mathfrak g\otimes_{\mathbb R}\mathbb C$$，并把 $$\rho$$ 复线性延拓为 $$\rho_{\mathbb C}$$。取元素 $$iX$$（严格说是 $$X\otimes i$$）：由复线性，
$$\rho_{\mathbb C}(iX)=i\,\rho(X).$$
而 $$\bigl(i\rho(X)\bigr)^*=-i\,\rho(X)^*=-i\cdot\bigl(-\rho(X)\bigr)=i\rho(X)$$，故 **$$i\rho(X)$$ 自伴**，它的特征值是**实数**：若 $$\rho(X)v=\lambda v$$ 且 $$\lambda=i\beta$$（$$\beta\in\mathbb R$$），则 $$i\rho(X)v=i\lambda v=-\beta v$$。

所以"虚谱变实谱"的换算就是乘一个 $$i$$：**把反自伴算子乘 $$i$$ 得自伴算子，谱从 $$i\mathbb R$$ 移到 $$\mathbb R$$。** $$-i\rho(X)$$ 的特征值就是那些 $$\beta$$。

**第三步：这与"权"和"根"的关系。** 之所以要费这一趟，是因为**实谱可以比较大小、可以排序、可以做整数运算**，而虚谱不行。第 56 章要做的正是这件事：

- 取一个**极大的两两交换**的（反自伴算子）族 $$\mathfrak t\subseteq\mathfrak g$$。复化后 $$\{i\rho(H):H\in\mathfrak t\}$$ 是一族两两交换的**自伴**算子，由线性代数可以**同时对角化**。
- 同时对角化之后，每个共同特征向量 $$v$$ 给出一族实数 $$\bigl(h\mapsto\beta(h)\bigr)$$，使 $$i\rho(H)v=\beta(H)v$$，即 $$\rho(H)v=i\beta(H)v$$。这条线性泛函
$$\lambda:\mathfrak t_{\mathbb C}\to\mathbb C,\qquad \lambda(H)=i\beta(H)$$
就是所谓的**权 (weight)**。
- 把 $$\rho$$ 取成**伴随表示** $$\operatorname{ad}:\mathfrak g\to\mathfrak{gl}(\mathfrak g)$$，则非零的权就是**根 (root)**，而 $$\mathfrak t$$ 的复化就是 **Cartan 子代数**。根空间分解 $$\mathfrak g_{\mathbb C}=\mathfrak h\oplus\bigoplus_{\alpha}\mathfrak g_\alpha$$ 说的就是"把 $$\mathfrak g_{\mathbb C}$$ 按这族实谱拆开"。

顺带解释一个本章出现过的现象：$$SL(2,\mathbb R)$$ 的情形（定理 3.11）里出现的 $$2\cos\beta$$、$$2\cosh\alpha$$，正是 $$\operatorname{ad}$$ 的"谱"在紧/非紧两种情况下落在虚轴/实轴上的差别——紧的时候取 $$\cos$$，非紧的时候取 $$\cosh$$。

**接下一章**：把实 Lie 代数复化、把"反自伴算子的虚谱"翻译成"自伴算子的实谱"、再把这套谱账整理成权与根——这就是第 56 章要做的全部事情。复半单 Lie 代数由它的根系完全决定，而根系又压缩成一张 Dynkin 图；本章建立的 $$\exp$$、BCH、$$\mathfrak{sl}(2)$$ 那组关系 $$[H,X_+]=2X_+,\ [H,X_-]=-2X_-,\ [X_+,X_-]=H$$（解 基2），在那里会成为整个分类理论的原子模型。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**1. $$\exp$$ 不是记号，是一个自然操作。** 它由单参数子群定义（定义 3.1 之前的 (R1)–(R3)），与一切 Lie 群同态交换（(R4)(iv)），在矩阵群上退化为矩阵指数级数（(R4)(v)）。第 02 章的 $$e^{i\theta}$$、第 46 章的 $$e^{-itH}$$（算子群）、本章的 $$\exp(\theta J)=R_\theta$$，都是同一个操作的不同实现。一旦有了它，"Lie 代数决定 Lie 群吗"才成为一个可以问的问题。

**2. 求导丢掉的是乘法，但乘法没被丢掉——它被括号接管了。** BCH 公式（定理 3.8）说 $$e^{X}e^{Y}=e^{\,X+Y+\frac12[X,Y]+\cdots}$$，而 $$\cdots$$ 里全是迭代括号。于是：局部范围内 $$G$$ 的乘法被 $$\mathfrak g$$ 的括号**完全**决定（定理 3.10）。这也是"Lie 代数"必须带 Jacobi 公理的原因——Jacobi 是结合律在无穷小层面的影子（§4.2）。$$[X,X]=0$$ 则更直接：它是 $$e^{X}e^{-X}=I$$ 的影子。

**3. 整体信息与代数无关，必须另算。** 三条证据：$$\mathfrak{su}(2)\cong\mathfrak{so}(3)$$ 但 $$SU(2)\ne SO(3)$$（推论 3.7）；$$\exp:\mathfrak{sl}(2,\mathbb R)\to SL(2,\mathbb R)$$ 不是满射（定理 3.11）；$$\mathbb R$$ 与 $$U(1)$$ 的 Lie 代数同构而群不同构（题 4）。能给的正向结论只有两条：连通群中每个元素是**有限个指数之积**，紧连通群上 $$\exp$$ 是满射（定理 3.12）。第 25、26 章算过的那层拓扑（覆叠、基本群），在本章找到了它在代数里的"盲点"的确切位置。

**4. 量子力学里那个 $$i$$ 有了统一的代数解释。** 酉表示把实 Lie 代数送到**反自伴**算子，反自伴算子的特征值必为纯虚（定理 3.13(ii)）。第 04 章 $$D$$ 的谱是 $$i\mathbb Z$$，第 44 章的关系是 $$[x,p]=i\hbar$$——两个 $$i$$ 是同一个 $$i$$，它不是约定的产物，而是"酉 + 自伴"这条要求的必然结果。

**5. 幂零是"顺利"与"麻烦"的分水岭。** 幂零时 BCH 有限截断，$$\exp$$ 是整体微分同胚，矩阵指数与对数互逆而不必担心收敛半径（定理 3.14）。Heisenberg 群 $$H_3(\mathbb R)$$ 就是这个现象的最小范例，而它同时就是第 44 章那个 Lie 代数——第 44 章的整条链（CCR $$\to$$ Weyl 关系 $$\to$$ Stone–von Neumann）在这里被重新读成：一个幂零 Lie 群的唯一不可约酉表示。

### 下一章的悬念

本章把实 Lie 代数当**一个**对象处理：括号、迭代括号、谱。但**谱**这件事只在"反自伴算子"上做了一半——我们知道谱落在虚轴上（定理 3.13(ii)），却没能像线性代数那样把它**算出来**。第 56 章要做两件事：把 $$\mathfrak g$$ 复化，让虚谱变成实谱；然后取一族**极大的两两交换**的元素（Cartan 子代数），把它们同时对角化。对角化之后：

- 共同特征值给出一族线性泛函，叫做**权 (weight)**；
- 把表示取成伴随表示 $$\operatorname{ad}$$，非零的权就是**根 (root)**；
- $$\mathfrak g_{\mathbb C}$$ 因此被拆成 Cartan 子代数加上一族根空间，而每一对根配上一条 $$\mathfrak{sl}(2)$$ 子代数（解 基2 里那组 $$[H,X_+]=2X_+$$、$$[H,X_-]=-2X_-$$、$$[X_+,X_-]=H$$ 就是它的原子模型）；
- 根系再压缩成 Cartan 矩阵与 Dynkin 图，复半单 Lie 代数由此**分类**：$$A_n,B_n,C_n,D_n,E_6,E_7,E_8,F_4,G_2$$。

本章的定理 3.12(b) 与研 1 用到的"谱定理"，在那里会被替换成"极大环面 + 同时对角化"这条一般机制。

### 延伸阅读

- **原专栏**：MP70（典型群(4)：Lie 群的同伦、旋量群）、MP71（典型群(5)：流形的 Lie 代数和 Lie 群的左不变向量场）、MP72（典型群(6)：单参数子群与指数映射）。本章 §3.1–§3.2 的结构直接取自 MP71–MP72；MP70 里提到的旋量群 $$\mathrm{Spin}(n)$$ 的构造要用 Clifford 代数，那是第 58 章。
- **John Stillwell,《Naive Lie Theory》** 第 6–9 章。矩阵群路线，BCH 与指数映射讲得最平易，与本章的层次最接近。
- **Brian Hall,《Lie Groups, Lie Algebras, and Representations》(GTM 222)** 第 2–3 章。矩阵 Lie 群、矩阵指数、闭子群定理、李的三条定理的完整证明，以及 $$\exp$$ 不满射的反例。
- **Bonfiglioli–Fulci,《Topics in Noncommutative Algebra: The Theorem of Campbell, Baker, Hausdorff and Dynkin》**。想要 BCH 的完整证明与历史，看这本；本章只用到它的前三阶系数与"幂零时截断"这条推论。
- **回看两条旧账**：第 04 章（$$SO(2)$$ 与 $$D$$ 的谱）的定理 3.6、3.8 在本章被收进定理 3.13；第 44 章（正则对易关系）的定义 3.2、3.3、3.5 与 命题 3.6 在本章被收进定理 3.14。重读那两章时，可以把本章的编号当作"一般框架"去对照。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch53_Lie代数与指数映射_上.md">← 第53章 Lie 代数与指数映射·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch55_复半单Lie代数与根系_上.md">第55章 复半单 Lie 代数与根系·上 →</a></div>
</div>
