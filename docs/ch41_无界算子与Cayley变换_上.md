---
layout: default
---

# 第41章: 无界算子与 Cayley 变换·上：预备与直觉 (Unbounded Operators and the Cayley Transform · Part I: Warm-up and Intuition)

> 配套深化: 见 第42章 无界算子与 Cayley 变换·下（完整推导），本章是它的具体铺垫，建议先读本章
> 专家依据: `_experts/analysis/functional-analysis.md`（主）+ `_experts/analysis/spectral-theory.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

本章要打磨的，是第42章开篇就迎面撞上的四个"跳跃点"：（1）一个算子除了公式，还要不要写出"对哪些向量适用"这件事——第42章的 定义 3.1 把这写成"定义域"，但这个概念第一次出现时容易被当成技术性的枝节；（2）"对称"与"自伴"两个词在有限维里从不分家，为什么到了无穷维就分了家、而且伴随的定义域会真的变大；（3）第42章 定理 3.3（Hellinger–Toeplitz）与 命题 3.21、定理 3.22 里反复出现的"无界"，具体是怎么个无界法，能不能在纸上亲手算出一个范数发散的例子；（4）第42章 3.6 节的 Cayley 变换 $$U=(T-i)(T+i)^{-1}$$ 与半角公式 $$x=\tan\frac\theta2$$ 的关系写得很快，本章要先用两组具体数字把这条关系算穿。

做法是：把第42章里"位置算子在 $$L^2(\mathbb R)$$ 上"这类需要 Fourier 变换和 Sobolev 空间的例子，换成一个只需要数列求和的玩具版本——序列空间 $$\ell^2(\mathbb N)$$ 上的对角算子；把 Cayley 变换换成实数域上的旋转矩阵和标量算例。读完本章，你应该已经**亲手验证**过：一个具体向量不在某个算子的定义域里、一个具体算子无界、一个具体的旋转矩阵确实是 $$(I-B)(I+B)^{-1}$$ 的样子、以及一个具体的一阶算子在有限区间上确实留有"亏口"。第42章要做的，只是把这些手算过程写成一般定义和一般证明。

## 二、入口：一道具体的问题 (Entry Problem)

**问题（对角算子的定义域之谜：动量算子问题的离散预演）。** 取 $$H=\ell^2(\mathbb N)=\Bigl\lbrace c=(c_1,c_2,c_3,\dots)\ :\ \sum_{n=1}^\infty\lvert c_n\rvert^2<\infty\Bigr\rbrace$$，标准正交基记作 $$e_1,e_2,e_3,\dots$$（$$e_n$$ 第 $$n$$ 位是 1，其余是 0）。定义一个"数索引"的对角算子：

$$T_0e_n=n\,e_n,\qquad n=1,2,3,\dots$$

并把它线性延拓到**有限支集**序列（即只有有限多项非零的序列，记这个子空间为 $$c_c(\mathbb N)$$）：若 $$c=\sum_{n=1}^N c_ne_n$$，则 $$T_0c=\sum_{n=1}^N n\,c_n e_n$$。

**(i)** 能不能对**任意** $$g=(g_n)\in\ell^2(\mathbb N)$$ 都定义 $$(ng_n)_n$$ 并指望它还在 $$\ell^2$$ 里？请给出一个**具体的** $$g\in\ell^2(\mathbb N)$$，使 $$(ng_n)_n\notin\ell^2(\mathbb N)$$。

**(ii)** 取 $$c,d\in c_c(\mathbb N)$$（比如 $$c=(1,2,0,0,\dots)$$，$$d=(0,3,1,0,\dots)$$），直接算出 $$\langle T_0c,d\rangle$$ 与 $$\langle c,T_0d\rangle$$，看它们是否相等。猜一猜：对**任意**有限支集的 $$c,d$$，这个等式是不是总成立？

**(iii)** 找一个具体的 $$g\in\ell^2(\mathbb N)\setminus c_c(\mathbb N)$$（无穷多项非零），使得"$$c\mapsto\langle T_0c,g\rangle$$ 作为 $$c_c(\mathbb N)$$ 上的线性泛函"仍然连续（换句话说 $$(ng_n)_n\in\ell^2$$）。这说明什么？

**(iv)** 单位向量 $$e_N$$ 满足 $$\lVert e_N\rVert=1$$、$$T_0e_N=Ne_N$$。当 $$N$$ 变大时，$$\lVert T_0e_N\rVert$$ 会怎样？由此能不能判断 $$T_0$$（哪怕只限制在 $$c_c(\mathbb N)$$ 上）有没有可能被延拓成一个**处处有定义、还对称**的有界算子？

**本题与第42章的对应。** (i) 是第42章入口题 (i) 的离散版——那里问的是 $$\hat p\psi=-i\psi'$$ 对任意 $$\psi\in L^2(\mathbb R)$$ 是否有意义。(ii)–(iii) 逼出"定义域"与"伴随的定义域可能更大"这两个概念，对应第42章 定义 3.13、经典问题 2。(iv) 是第42章 定理 3.3（Hellinger–Toeplitz）的具体导火索。三、四节会把这四问逐一算完，并延伸出 Cayley 变换与亏指数两条线。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 算子＝映射＋定义域：一个能亲手算的反例

回答入口题 (i)。取

$$g_n=\frac1n,\qquad n=1,2,3,\dots$$

**第一步，$$g\in\ell^2(\mathbb N)$$ 吗？** 需要 $$\sum_n\lvert g_n\rvert^2=\sum_n\frac1{n^2}$$ 收敛。这是熟知的 $$p$$-级数（$$p=2>1$$），收敛（和是 $$\pi^2/6$$，这里只需要"收敛"这一点）。故 $$g\in\ell^2(\mathbb N)$$。

**第二步，$$(ng_n)_n$$ 呢？** $$ng_n=n\cdot\frac1n=1$$ 对每个 $$n$$ 都成立，于是 $$\sum_n\lvert ng_n\rvert^2=\sum_n1=\infty$$。故 $$(ng_n)_n\notin\ell^2(\mathbb N)$$——公式 $$T_0g=(ng_n)_n$$ 在这个 $$g$$ 上给出的不是 $$\ell^2$$ 里的元素，**根本不是一个合法的输出**。

这就是入口题 (i) 的答案：不能对任意 $$g\in\ell^2$$ 定义 $$T_0g$$。于是需要一个记号，专门标出"公式 $$T_0$$ 对哪些向量真正有意义"——这正是第42章 定义 3.1 引入"定义域"这个词的原因。搬到本章的语境：

**定义 3.1（对角算子的定义域，warm-up 版）。** 记

$$\mathrm{Dom}(T_0)=\Bigl\lbrace c=(c_n)\in\ell^2(\mathbb N)\ :\ \sum_n n^2\lvert c_n\rvert^2<\infty\Bigr\rbrace,$$

在 $$\mathrm{Dom}(T_0)$$ 上规定 $$T_0c=(nc_n)_n$$。这是"公式 + 只在公式真正有意义的地方使用它"的最直接写法——第42章 定义 3.1 对一般 Hilbert 空间做的就是同一件事，只是把"$$\sum n^2\lvert c_n\rvert^2<\infty$$"换成了更抽象的条件。

$$c_c(\mathbb N)$$（有限支集序列）显然满足这个条件（求和只有有限项），故 $$c_c(\mathbb N)\subseteq\mathrm{Dom}(T_0)$$；而 $$g=(1/n)$$ 不满足，故 $$g\notin\mathrm{Dom}(T_0)$$，与上面的计算一致。

**为什么用 $$\ell^2(\mathbb N)$$ 而不是直接用第42章的 $$L^2(\mathbb R)$$。** 两者都是无穷维 Hilbert 空间，但 $$\ell^2(\mathbb N)$$ 的元素是一列数字，"求和"就是普通的数列求和；$$L^2(\mathbb R)$$ 的元素是一个函数，"求和"要换成积分，还要先弄清楚什么是"弱导数"。本章的每一个计算——判断某个向量在不在某个集合里、级数收不收敛——用 $$\ell^2(\mathbb N)$$ 都可以直接动笔算出数字；换成 $$L^2(\mathbb R)$$ 就要先掌握 Fourier 变换和 Sobolev 空间（第42章 引理 3.20）才能算。这就是"先具体、后抽象"的意思：先在 $$\ell^2(\mathbb N)$$ 里把"定义域为什么重要"这件事算穿，第42章再把同一套逻辑套到 $$L^2(\mathbb R)$$ 上，读者到时候只需要多学一层 Fourier 变换的"翻译"，逻辑本身已经熟悉了。

**命题 3.2（$$T_0$$ 在 $$c_c(\mathbb N)$$ 上对称）。** 对任意 $$c,d\in c_c(\mathbb N)$$，$$\langle T_0c,d\rangle=\langle c,T_0d\rangle$$。

*手算*：取入口题 (ii) 的 $$c=(1,2,0,0,\dots)$$，$$d=(0,3,1,0,\dots)$$。$$T_0c=(1\cdot1,\,2\cdot2,\,0,\dots)=(1,4,0,\dots)$$，$$T_0d=(0,\,2\cdot3,\,3\cdot1,0,\dots)=(0,6,3,0,\dots)$$。于是

$$\langle T_0c,d\rangle=1\cdot0+4\cdot3+0\cdot1=12,\qquad \langle c,T_0d\rangle=1\cdot0+2\cdot6+0\cdot3=12 .$$

两者相等。

*一般证明*：设 $$c=\sum_{n\le N}c_ne_n$$，$$d=\sum_{n\le N}d_ne_n$$（把两者的支集都塞进同一个有限范围 $$N$$ 里）。则

$$\langle T_0c,d\rangle=\sum_{n\le N}(nc_n)\overline{d_n}=\sum_{n\le N}n\,c_n\overline{d_n},\qquad \langle c,T_0d\rangle=\sum_{n\le N}c_n\overline{(nd_n)}=\sum_{n\le N}n\,c_n\overline{d_n}$$

（第二个等式用了 $$n$$ 是实数，故 $$\overline{nd_n}=n\overline{d_n}$$）。两式是同一个和，故相等。$$\blacksquare$$

这条证明比第42章 定理 3.22（动量算子对称）里的分部积分简单得多——因为求和只有有限项，没有"边界项"要处理。这不是巧合：第42章那里靠分部积分让边界项因**紧支集**而消失，这里"和只有有限项"就是紧支集在离散世界里的样子；**没有边界可谈**，是因为压根没有"边界"这一说。等到 3.3 节把区间搬回连续情形，"边界项消失"就要靠函数本身在端点为零来保证——这条对照就是理解第42章 定理 3.22 证明的钥匙。

**命题 3.3（$$T_0$$ 无界）。** 不存在常数 $$C$$ 使 $$\lVert T_0c\rVert\le C\lVert c\rVert$$ 对一切 $$c\in c_c(\mathbb N)$$ 成立。

*手算*：入口题 (iv) 已经算过：$$\lVert e_N\rVert=1$$，$$\lVert T_0e_N\rVert=\lVert Ne_N\rVert=N$$。取 $$N=10,100,10^6,\dots$$，比值 $$\lVert T_0e_N\rVert/\lVert e_N\rVert=N$$ 没有上界。故任何常数 $$C$$ 都会被某个 $$N>C$$ 的 $$e_N$$ 击穿。$$\blacksquare$$

这就是第42章 定义 3.1"无界"这个词最朴素的样子：不是"算出来的值很大"，而是**输入的范数固定为 1，输出的范数却没有上界**。

**命题 3.4（伴随的定义域比原定义域大：入口题 (iii) 的具体解）。** 取

$$g_n=\frac1{n^2},\qquad n=1,2,3,\dots .$$

则 $$g\in\ell^2(\mathbb N)\setminus c_c(\mathbb N)$$（无穷多项非零），且泛函 $$c\mapsto\langle T_0c,g\rangle$$（$$c\in c_c(\mathbb N)$$）在 $$\ell^2$$ 范数下连续。

*手算*：$$\sum_n\lvert g_n\rvert^2=\sum_n n^{-4}$$ 收敛（$$p=4>1$$），故 $$g\in\ell^2$$；每一项都非零，故 $$g\notin c_c(\mathbb N)$$。再看 $$(ng_n)_n$$：$$ng_n=n\cdot n^{-2}=n^{-1}$$，

$$\sum_n\lvert ng_n\rvert^2=\sum_n n^{-2}$$

同样是收敛的 $$p$$-级数（与 命题 3.2 前算过的那个级数一样）。由 Cauchy–Schwarz，对任意 $$c\in c_c(\mathbb N)$$，

$$\lvert\langle T_0c,g\rangle\rvert=\Bigl\lvert\sum_n(nc_n)\overline{g_n}\Bigr\rvert=\Bigl\lvert\sum_nc_n\overline{(ng_n)}\Bigr\rvert\le\lVert c\rVert\cdot\lVert(ng_n)_n\rVert,$$

右边是个有限常数乘 $$\lVert c\rVert$$，故连续。$$\blacksquare$$

**这回答了入口题 (iii)：存在向量 $$g$$，它不在 $$c_c(\mathbb N)$$ 里，却仍然让"$$T_0$$ 与 $$g$$ 配对"这件事有意义。** 第42章 定义 3.13 把这类 $$g$$ 的全体叫作 $$T_0^*$$ 的**定义域**——它可以比 $$T_0$$ 自己的定义域**更大**。仿照 命题 3.4 的算法逐一检验可得

$$\mathrm{Dom}(T_0^*)=\Bigl\lbrace g\in\ell^2\ :\ \sum_nn^2\lvert g_n\rvert^2<\infty\Bigr\rbrace=\mathrm{Dom}(T_0)\ \supsetneq\ c_c(\mathbb N),$$

即：把 $$T_0$$ 的定义域从 $$c_c(\mathbb N)$$ 换成"最大"的 $$\mathrm{Dom}(T_0)$$（命题 3.4 里 $$g=(1/n^2)$$ 正落在这个更大的集合里，$$g=(1/n)$$ 则连这个更大的集合都进不去），伴随的定义域就与原定义域重新相等——这正是第42章 定义 3.16"自伴"的意思：**定义域恰好等于伴随的定义域**。$$c_c(\mathbb N)$$ 上的 $$T_0$$ 对称但不自伴；补到 $$\mathrm{Dom}(T_0)$$ 上的 $$T_0$$ 自伴。第42章 经典问题 2 对动量算子做的就是同一件事，只是 $$c_c(\mathbb N)\to C_c^\infty(\mathbb R)$$、级数换成积分。

### 3.2 从旋转矩阵到 Cayley 变换：两组数字算穿半角公式

第42章 3.6 节的 Cayley 变换 $$U=(T-i)(T+i)^{-1}$$ 来自一句"三角函数万能公式 $$x=\tan\frac\theta2$$ 把直线铺到圆上"。这句话本身也需要先用数字验证。

**命题 3.5（实反对称矩阵的 Cayley 变换是旋转，两组数值）。** 对 $$B=\begin{pmatrix}0&x\\-x&0\end{pmatrix}$$，$$(I-B)(I+B)^{-1}$$ 是转角为 $$\theta=2\arctan x$$ 的旋转矩阵。

*第一组数字，$$x=1$$*：

$$I-B=\begin{pmatrix}1&-1\\1&1\end{pmatrix},\qquad I+B=\begin{pmatrix}1&1\\-1&1\end{pmatrix},\qquad \det(I+B)=1\cdot1-1\cdot(-1)=2 .$$

$$(I+B)^{-1}=\frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix}$$（$$2\times2$$ 矩阵求逆：交换对角、变号副对角、除以行列式）。于是

$$(I-B)(I+B)^{-1}=\begin{pmatrix}1&-1\\1&1\end{pmatrix}\cdot\frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix}=\frac12\begin{pmatrix}0&-2\\2&0\end{pmatrix}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.$$

这正是 $$\theta=90°$$ 的旋转矩阵 $$\begin{pmatrix}\cos90°&-\sin90°\\\sin90°&\cos90°\end{pmatrix}$$。核对公式：$$\theta=2\arctan1=2\times45°=90°$$，吻合。

*第二组数字，$$x=1/\sqrt3$$*：这次直接用倍角公式核对，不重算矩阵逆（读者可仿第一组的步骤自行验证）。$$x^2=1/3$$，

$$\frac{1-x^2}{1+x^2}=\frac{1-1/3}{1+1/3}=\frac{2/3}{4/3}=\frac12,\qquad \frac{2x}{1+x^2}=\frac{2/\sqrt3}{4/3}=\frac{2}{\sqrt3}\cdot\frac34=\frac{\sqrt3}{2}.$$

而 $$\cos60°=1/2$$、$$\sin60°=\sqrt3/2$$，且 $$2\arctan(1/\sqrt3)=2\times30°=60°$$——又一次吻合。

*一般证明*：由半角公式，$$x=\tan\frac\theta2$$ 时 $$\dfrac{1-x^2}{1+x^2}=\cos\theta$$、$$\dfrac{2x}{1+x^2}=\sin\theta$$（三角学的标准恒等式，两组数值已各验证一次）。而对一般 $$x$$，仿第一组数字的矩阵计算，

$$(I-B)(I+B)^{-1}=\frac1{1+x^2}\begin{pmatrix}1-x^2&-2x\\2x&1-x^2\end{pmatrix}=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},\qquad \theta=2\arctan x .$$

$$\blacksquare$$

**命题 3.6（标量 Cayley 变换落在单位圆上，数值验证）。** 对实数 $$t$$，令 $$\mu(t)=\dfrac{t-i}{t+i}$$。则 $$\lvert\mu(t)\rvert=1$$。

*手算，$$t=\sqrt3$$*：

$$\mu(\sqrt3)=\frac{\sqrt3-i}{\sqrt3+i}=\frac{(\sqrt3-i)^2}{(\sqrt3+i)(\sqrt3-i)}=\frac{3-2\sqrt3\,i-1}{3+1}=\frac{2-2\sqrt3\,i}{4}=\frac12-\frac{\sqrt3}2i$$

（分母用 $$(\sqrt3+i)(\sqrt3-i)=3-i^2=4$$；分子展开 $$(\sqrt3-i)^2=3-2\sqrt3i+i^2=2-2\sqrt3i$$）。模长：

$$\lvert\mu(\sqrt3)\rvert=\sqrt{\Bigl(\frac12\Bigr)^2+\Bigl(\frac{\sqrt3}2\Bigr)^2}=\sqrt{\frac14+\frac34}=1 .$$

且 $$\mu(\sqrt3)=\cos(-60°)+i\sin(-60°)$$，幅角 $$-60°=2\arctan\sqrt3-180°$$（$$\arctan\sqrt3=60°$$）——这与第42章 定理 3.29 给出的公式 $$\mu(p)=e^{i(2\arctan p-\pi)}$$（那里 $$p$$ 是动量算子的谱参数）完全对应：**这里的 $$t$$ 就是位置或动量取值为一个具体实数时的玩具模型**，第42章 经典问题 3(b) 与 竞4 对动量、位置算子做的，正是把 $$t$$ 换成变量 $$p$$ 或 $$x$$、把"标量乘法"换成"乘法算子"后的同一件事。

*一般证明*：$$\lvert\mu(t)\rvert^2=\dfrac{(t-i)\overline{(t-i)}}{(t+i)\overline{(t+i)}}=\dfrac{(t-i)(t+i)}{(t+i)(t-i)}=1$$（$$t$$ 是实数，$$\overline{t\mp i}=t\pm i$$，分子分母是同一对共轭因子的乘积）。$$\blacksquare$$

**为什么需要这两个记号。** $$B\mapsto(I-B)(I+B)^{-1}$$ 与 $$t\mapsto\mu(t)$$ 看起来是两件事，其实是同一件事的两幅面孔：把"反对称"（$$B^T=-B$$，对应复数情形的"反自伴"，$$T^*=-T$$）换成"正交/酉"（长度不变），核心都是同一个 Möbius 型公式 $$\lambda\mapsto\dfrac{1-\lambda}{1+\lambda}$$，只是自变量前面差一个 $$i$$。第42章 定义 3.26 直接对无界的 $$T$$（可能是矩阵、可能是微分算子）写 $$U=(T-i)(T+i)^{-1}$$，此刻你已经在 $$2\times2$$ 矩阵和标量两种最简单的情形下各验证过两次数值、证过一次一般公式——第42章 定理 3.27–3.29 要做的，只是把"矩阵求逆"换成"算子的 $$(T+i)^{-1}$$"，把"三角恒等式"换成"内积展开"。

### 3.3 亏口：一阶算子在有限区间上留下多少自由度

第42章 3.5 节用**二阶**算子 $$-\dfrac{d^2}{dt^2}$$ 在 $$(0,1)$$ 上演示"定义域＝边界条件"，解空间是二维的，算起来稍显吃力。这里先用**一阶**算子把同一件事算穿——它正是第42章 竞3 的题目，这里给出完整的手算过程。

**命题 3.7（一阶算子在 $$(0,1)$$ 上的亏子空间是一维的）。** 取 $$H=L^2(0,1)$$，先只考虑"最大"算子 $$P_0^*$$（不加边界条件，定义域取一切 $$g$$ 使 $$g,g'\in L^2(0,1)$$，$$P_0^*g=-ig'$$；第42章的记法里，这个最大算子恰是"$$-i\frac{d}{dt}$$ 限制在紧支集光滑函数上"那个算子 $$P_0$$ 的伴随）。解方程

$$-ig'=\pm ig .$$

*手算，取 "$$+i$$" 情形*：$$-ig'=ig\iff g'=-g$$。这是最简单的一阶线性 ODE，通解 $$g(t)=Ce^{-t}$$（$$C\in\mathbb C$$ 任意常数）。验证：$$g'(t)=-Ce^{-t}=-g(t)$$，代回 $$-ig'=-i(-g)=ig$$，成立。这个解空间由**一个**函数 $$e^{-t}$$ 张成，是一维的。它在 $$L^2(0,1)$$ 里吗？

$$\int_0^1\lvert e^{-t}\rvert^2\,dt=\int_0^1e^{-2t}\,dt=\Bigl[-\frac12e^{-2t}\Bigr]_0^1=\frac{1-e^{-2}}2\approx0.432,$$

有限，故 $$e^{-t}\in L^2(0,1)$$。

*"$$-i$$" 情形*：同样 $$g'=g$$，通解 $$g(t)=Ce^t$$，一维解空间，且

$$\int_0^1\lvert e^t\rvert^2\,dt=\int_0^1e^{2t}\,dt=\frac{e^2-1}2\approx3.19<\infty,$$

也在 $$L^2(0,1)$$ 里。

**结论**：两个"亏子空间"（第42章 定义 3.24 的 $$\mathscr K_+=\ker(P_0^*-i)$$、$$\mathscr K_-=\ker(P_0^*+i)$$）分别由 $$e^{-t}$$、$$e^t$$ 张成，维数都是 $$1$$：

$$n_+=n_-=1 .$$

$$\blacksquare$$

**这和区间上"墙"的类比是一回事，只是墙变简单了。** 二阶算子（第42章 3.5 节）在两端各留一个方程，解空间二维；一阶算子只在"一个方向"上传播，每个方程只留一维解空间。第42章 竞3 会请你验证：把 $$n_+=n_-=1$$ 代入第42章 定理 3.25（von Neumann 自伴扩张定理），自伴扩张构成**一个**实参数（对应 $$U(1)$$，即一个相位 $$e^{i\theta}$$）的族，形如"$$g(1)=e^{i\theta}g(0)$$"——这正是 3.2 节"单位圆"的再次出现：**决定自伴扩张的参数，本身就活在单位圆上**，与 Cayley 变换把谱送上单位圆是同一个几何。

**猜一猜（留给六节练习）**：如果把区间 $$(0,1)$$ 换成半无穷区间 $$(0,\infty)$$，$$e^{-t}$$ 和 $$e^{t}$$ 还都在对应的 $$L^2$$ 空间里吗？亏指数会不会变？这是第42章之后（动量算子在半线上）会遇到的情形，这里先猜，六节练习验证。

## 四、几何与物理直觉 (Intuition)

**1. 定义域像"仪器的量程"。** $$T_0e_n=ne_n$$ 就像一台"读数放大 $$n$$ 倍"的仪器：读数越高的通道，被放大得越厉害。如果输入本身在高读数通道上衰减得不够快（比如 $$g=(1/n)$$），放大后就爆表——这正是"定义域"的直觉意思：**不是仪器坏了，是有些输入超出了它的量程。**

**2. 对称而不自伴，像一台"只按最初几个读数标定过"的仪表。** $$c_c(\mathbb N)$$ 上的 $$T_0$$ 用有限的读数就能验证对称性；但世界上还有很多"看起来能配对"的读数（比如 $$g=(1/n^2)$$），它们没有被囊括进最初的标定范围。把标定范围扩大到"所有能配对的"，才是这台仪器的完整版——自伴，就是标定范围已经开到不能再开、再开就要超界。

**3. Cayley 变换像座钟的指针。** 半角公式 $$x=\tan\frac\theta2$$ 把一条无穷长的直线（钟摆能达到的所有偏角的正切值）卷成一个圆周（指针实际指向的角度）。第42章的 $$U=(T-i)(T+i)^{-1}$$ 做的是同一件事：把"谱"这条可以跑到无穷远的直线，卷成一个有界的圆。物理上（第42章 3.4、3.6 节的相移、S 矩阵）圆周上的角度就是"相位"——一个永远只能落在 $$[0,2\pi)$$ 里的量。

**4. 亏指数像"门口的进出平衡"。** $$n_+$$ 数的是"往 $$+i$$ 方向跑出去还留在空间里的自由度"，$$n_-$$ 是反方向的。一阶算子只有一个"方向"，进出各一个自由度，$$n_+=n_-=1$$；二阶算子有两个方向（第42章 3.5 节），进出各两个。自伴扩张存在，要求进出的自由度数目相等——就像一扇门，进来多少人，最终也得让多少人出去，账才能平；6 节研2 会看到一个"账平不了"的例子。

## 五、经典问题精讲 (Classical Problems)

**问题 1（$$T_0$$ 的一个边界情形：$$g_n=1/n^{1.5}$$）。** 判断 $$g=(n^{-1.5})_{n\ge1}$$ 是否属于 $$\ell^2(\mathbb N)$$，是否属于 $$\mathrm{Dom}(T_0)$$（3.1 节 定义 3.1）。

*解*：$$\sum_n\lvert g_n\rvert^2=\sum_n n^{-3}$$，$$p=3>1$$，收敛，故 $$g\in\ell^2(\mathbb N)$$。再看 $$n^2\lvert g_n\rvert^2=n^2\cdot n^{-3}=n^{-1}$$，$$\sum_n n^{-1}$$ 是调和级数，**发散**。故 $$g\notin\mathrm{Dom}(T_0)$$。这个例子恰好卡在 $$g=(1/n)$$（3.1 节，连 $$\ell^2$$ 都进不去）与 $$g=(1/n^2)$$（3.1 节，落在 $$\mathrm{Dom}(T_0)$$ 里）中间：指数取 $$1.5$$ 时，向量还在 $$\ell^2$$ 里，却没能进入 $$T_0$$ 的定义域——说明 $$\mathrm{Dom}(T_0)$$ 是 $$\ell^2(\mathbb N)$$ 的一个**真子空间**，而不是靠近边缘才有的一点点差别。$$\blacksquare$$

**问题 2（由旋转矩阵反推 $$x$$）。** 已知某个 $$(I-B)(I+B)^{-1}$$ 算出来是 $$\begin{pmatrix}0&1\\-1&0\end{pmatrix}$$（转角 $$-90°$$），求 $$x$$，并验证。

*解*：由 命题 3.5，$$\theta=2\arctan x$$。这里 $$\cos\theta=0,\sin\theta=-1$$ 给 $$\theta=-90°$$，故 $$\arctan x=-45°$$，$$x=\tan(-45°)=-1$$。核对：$$B=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$$，$$I-B=\begin{pmatrix}1&1\\-1&1\end{pmatrix}$$，$$I+B=\begin{pmatrix}1&-1\\1&1\end{pmatrix}$$，$$\det(I+B)=2$$，$$(I+B)^{-1}=\frac12\begin{pmatrix}1&1\\-1&1\end{pmatrix}$$；

$$(I-B)(I+B)^{-1}=\begin{pmatrix}1&1\\-1&1\end{pmatrix}\cdot\frac12\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\frac12\begin{pmatrix}0&2\\-2&0\end{pmatrix}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},$$

与题设吻合。$$\blacksquare$$

**问题 3（标量 Cayley 变换的幅角公式，$$t=2$$）。** 算出 $$\mu(2)=\dfrac{2-i}{2+i}$$ 的模与幅角，并与 $$2\arctan2-\pi$$ 核对。

*解*：$$\mu(2)=\dfrac{(2-i)^2}{(2+i)(2-i)}=\dfrac{4-4i-1}{4+1}=\dfrac{3-4i}5=\dfrac35-\dfrac45i$$。模：$$\sqrt{(3/5)^2+(4/5)^2}=\sqrt{9/25+16/25}=1$$。幅角 $$\varphi$$ 满足 $$\cos\varphi=3/5,\sin\varphi=-4/5$$，即 $$\varphi=-\arctan(4/3)\approx-53.13°$$。核对公式：$$\arctan2\approx63.43°$$，$$2\times63.43°-180°=-53.13°$$，在数值精度内吻合。$$\blacksquare$$

**问题 4（半无穷区间上的一维亏子空间，预告 6 节研2）。** 只考虑"$$+i$$"方程 $$g'=-g$$：它的解 $$g(t)=Ce^{-t}$$ 在 $$(0,1)$$ 与 $$(0,\infty)$$ 上是否都属于对应的 $$L^2$$ 空间？

*解*：$$(0,1)$$ 上已在 命题 3.7 算过，属于（值约 $$0.432$$）。$$(0,\infty)$$ 上：

$$\int_0^\infty e^{-2t}\,dt=\Bigl[-\frac12e^{-2t}\Bigr]_0^\infty=0-\Bigl(-\frac12\Bigr)=\frac12<\infty,$$

也属于——指数衰减函数在半无穷区间上依然可积。这一半（"$$+i$$"这一支）不受区间是否有限影响；6 节研2 会看另一半（"$$-i$$"，$$e^t$$）在半无穷区间上会不会同样幸运。$$\blacksquare$$

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 取 $$c=(2,0,1,0,0,\dots)$$（第 1、3 位非零）、$$d=(1,1,0,0,\dots)$$（第 1、2 位非零），两者都在 $$c_c(\mathbb N)$$ 里。直接算出 $$T_0c$$、$$T_0d$$，并验证 $$\langle T_0c,d\rangle=\langle c,T_0d\rangle$$。

**基2.** 判断 $$g=(n^{-3})_{n\ge1}$$ 是否属于 $$\ell^2(\mathbb N)$$；是否属于 $$\mathrm{Dom}(T_0)$$（定义 3.1）。

**基3.** 取单位向量 $$c=\bigl(\tfrac1{\sqrt2},\tfrac1{\sqrt2},0,0,\dots\bigr)$$（第 1、2 位各为 $$1/\sqrt2$$）。验证 $$\lVert c\rVert=1$$，并算出 $$\lVert T_0c\rVert$$。

### 竞赛（本课目标难度）

**竞1.** 取 $$x=2$$。按 命题 3.5 的方法，直接算出 $$2\times2$$ 矩阵 $$B=\begin{pmatrix}0&2\\-2&0\end{pmatrix}$$ 的 Cayley 变换 $$(I-B)(I+B)^{-1}$$，并用 $$\theta=2\arctan2$$ 核对其 $$\cos\theta,\sin\theta$$（数值到两位小数即可）。

**竞2.** 对 命题 3.6 的 $$\mu(t)=\dfrac{t-i}{t+i}$$，算出 $$\mu(0)$$ 与 $$t\to+\infty$$、$$t\to-\infty$$ 时 $$\mu(t)$$ 的极限。说明为什么两个方向的极限是同一个复数，这个复数是谁。

**竞3.** 把 命题 3.7 里的区间从 $$(0,1)$$ 换成 $$(0,2)$$，重新算出 $$\ker(P_0^*\mp i)$$ 的具体解、验证它们仍在 $$L^2(0,2)$$ 中，从而说明 $$n_+=n_-=1$$ 与区间长度无关。

### 研究（通向下一章）

**研1.** 一般地取 $$g_n=n^{-\alpha}$$（$$\alpha>0$$）。求使 $$g\in\ell^2(\mathbb N)$$ 的 $$\alpha$$ 范围；再求使 $$g\in\mathrm{Dom}(T_0)$$ 的 $$\alpha$$ 范围。指出"在 $$\ell^2$$ 里但不在 $$\mathrm{Dom}(T_0)$$ 里"对应哪一段 $$\alpha$$，并核对 五节问题 1（$$\alpha=1.5$$）落在这一段里。

**研2.** 把 命题 3.7 的区间换成半无穷区间 $$(0,\infty)$$。分别判断 $$e^{-t}$$ 与 $$e^{t}$$ 是否属于 $$L^2(0,\infty)$$，由此猜测这时的 $$n_+,n_-$$ 分别是多少。它们还相等吗？这对"自伴扩张是否存在"意味着什么（提示：第42章 定理 3.25）？

### 解答 (Solutions)

**解 基1.** $$T_0c$$：第 1 位 $$1\cdot2=2$$，第 3 位 $$3\cdot1=3$$，其余 0，即 $$T_0c=(2,0,3,0,\dots)$$。$$T_0d$$：第 1 位 $$1\cdot1=1$$，第 2 位 $$2\cdot1=2$$，即 $$T_0d=(1,2,0,\dots)$$。

$$\langle T_0c,d\rangle=2\cdot1+0\cdot1+3\cdot0=2,\qquad \langle c,T_0d\rangle=2\cdot1+0\cdot2+1\cdot0=2 .$$

两者相等，与 命题 3.2 一致。$$\blacksquare$$

**解 基2.** $$\sum_n\lvert g_n\rvert^2=\sum_n n^{-6}$$，$$p=6>1$$，收敛，故 $$g\in\ell^2(\mathbb N)$$。$$n^2\lvert g_n\rvert^2=n^2\cdot n^{-6}=n^{-4}$$，$$\sum_n n^{-4}$$ 同样是收敛的 $$p$$-级数（$$p=4>1$$），故 $$g\in\mathrm{Dom}(T_0)$$。（对比 五节问题 1 的 $$\alpha=1.5$$：那里 $$n^2g_n^2=n^{-1}$$ 发散；这里指数大得多，两次检验都收敛。）$$\blacksquare$$

**解 基3.** $$\lVert c\rVert^2=\bigl(\tfrac1{\sqrt2}\bigr)^2+\bigl(\tfrac1{\sqrt2}\bigr)^2=\tfrac12+\tfrac12=1$$，故 $$\lVert c\rVert=1$$。$$T_0c$$：第 1 位 $$1\cdot\tfrac1{\sqrt2}=\tfrac1{\sqrt2}$$，第 2 位 $$2\cdot\tfrac1{\sqrt2}=\tfrac2{\sqrt2}=\sqrt2$$。

$$\lVert T_0c\rVert^2=\Bigl(\frac1{\sqrt2}\Bigr)^2+(\sqrt2)^2=\frac12+2=\frac52,\qquad \lVert T_0c\rVert=\sqrt{5/2}=\frac{\sqrt{10}}2\approx1.58 .$$

（对照 命题 3.3：单个 $$e_N$$ 给出 $$\lVert T_0e_N\rVert=N$$ 可以任意大；这里两个通道混合，$$\lVert T_0c\rVert$$ 介于 $$1$$ 和 $$2$$ 之间，符合直觉。）$$\blacksquare$$

**解 竞1.** $$I-B=\begin{pmatrix}1&-2\\2&1\end{pmatrix}$$，$$I+B=\begin{pmatrix}1&2\\-2&1\end{pmatrix}$$，$$\det(I+B)=1+4=5$$，$$(I+B)^{-1}=\frac15\begin{pmatrix}1&-2\\2&1\end{pmatrix}$$。

$$(I-B)(I+B)^{-1}=\begin{pmatrix}1&-2\\2&1\end{pmatrix}\cdot\frac15\begin{pmatrix}1&-2\\2&1\end{pmatrix}=\frac15\begin{pmatrix}1-4&-2-2\\2+2&-4+1\end{pmatrix}=\frac15\begin{pmatrix}-3&-4\\4&-3\end{pmatrix}=\begin{pmatrix}-0.6&-0.8\\0.8&-0.6\end{pmatrix}.$$

核对：$$\theta=2\arctan2\approx2\times63.43°=126.87°$$，$$\cos126.87°\approx-0.60$$，$$\sin126.87°\approx0.80$$，与矩阵吻合。$$\blacksquare$$

**解 竞2.** $$\mu(0)=\dfrac{0-i}{0+i}=\dfrac{-i}{i}=-1$$。$$t\to\pm\infty$$ 时，$$\mu(t)=\dfrac{t-i}{t+i}=\dfrac{1-i/t}{1+i/t}\to\dfrac{1-0}{1+0}=1$$（分子分母同除以 $$t$$，$$i/t\to0$$）。两个方向的极限相同，都是复数 $$1$$——由幅角公式 $$\varphi(t)=2\arctan t-\pi$$：$$t\to+\infty$$ 时 $$\arctan t\to\pi/2$$，$$\varphi\to0$$；$$t\to-\infty$$ 时 $$\arctan t\to-\pi/2$$，$$\varphi\to-2\pi\equiv0$$（模 $$2\pi$$）。两条路径绕过单位圆的两侧，最终都汇合在 $$\mu=1$$ 这一点。这正是第42章 定理 3.29"$$T$$ 无界 $$\Rightarrow1\in\sigma(U)$$"的数值影子：谱跑到无穷远，Cayley 像上就变成了逼近（但取不到）$$1$$ 这一点。$$\blacksquare$$

**解 竞3.** 方程不变，仍是 $$g'=\mp g$$，通解 $$g(t)=Ce^{\mp t}$$，在任何区间上都是一维解空间（区间长度不影响 ODE 解空间的维数，只影响解是否可积）。可积性：

$$\int_0^2e^{-2t}\,dt=\Bigl[-\frac12e^{-2t}\Bigr]_0^2=\frac{1-e^{-4}}2\approx0.491<\infty,\qquad \int_0^2e^{2t}\,dt=\frac{e^4-1}2\approx26.8<\infty,$$

两个积分都有限（只是比 命题 3.7 里 $$(0,1)$$ 上的值大一些），故 $$e^{-t},e^{t}\in L^2(0,2)$$，$$n_+=n_-=1$$ 依然成立。**结论**：只要区间**有限**，亏指数就不受区间长度影响——真正决定亏指数的是区间"有没有边界"，不是边界隔多远。$$\blacksquare$$

**解 研1.** $$g\in\ell^2(\mathbb N)$$ 要求 $$\sum_n n^{-2\alpha}<\infty$$，即 $$2\alpha>1$$，$$\alpha>\tfrac12$$。$$g\in\mathrm{Dom}(T_0)$$ 要求 $$\sum_n n^2\cdot n^{-2\alpha}=\sum_n n^{2-2\alpha}<\infty$$，即 $$2\alpha-2>1$$，$$\alpha>\tfrac32$$。故"在 $$\ell^2$$ 里但不在 $$\mathrm{Dom}(T_0)$$ 里"对应 $$\tfrac12<\alpha\le\tfrac32$$。五节问题 1 取 $$\alpha=1.5=\tfrac32$$，恰好卡在这段区间的右端点（$$\alpha=3/2$$ 时 $$\sum n^{-1}$$ 仍发散，故仍不在 $$\mathrm{Dom}(T_0)$$ 里），与那里直接算出的"$$g\in\ell^2$$ 但 $$g\notin\mathrm{Dom}(T_0)$$"一致。$$\blacksquare$$

**解 研2.** $$\displaystyle\int_0^\infty e^{-2t}\,dt=\Bigl[-\frac12e^{-2t}\Bigr]_0^\infty=\frac12<\infty$$，故 $$e^{-t}\in L^2(0,\infty)$$；而 $$\displaystyle\int_0^\infty e^{2t}\,dt=\infty$$（被积函数不衰减反而增长），故 $$e^{t}\notin L^2(0,\infty)$$。于是 $$\ker(P_0^*-i)$$（由 $$e^{-t}$$ 张成）仍是一维，$$n_+=1$$；但 $$\ker(P_0^*+i)$$（本该由 $$e^{t}$$ 张成）现在是**零维**，$$n_-=0$$。两者不相等。由第42章 定理 3.25（von Neumann 自伴扩张定理），**自伴扩张存在当且仅当 $$n_+=n_-$$**——这里 $$1\ne0$$，故 $$P_0$$ 在半无穷区间 $$(0,\infty)$$ 上**没有自伴扩张**：它对称、甚至"极大对称"（不能再扩大而不破坏对称性），却永远成不了自伴算子。这正是"半线上的动量算子"这一经典病态例子，与第42章 3.3 节末尾提到的"极大对称但非自伴"的单侧移位反例同根同源。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

1. **定义域是算子的一部分，不是技术细节。** $$T_0e_n=ne_n$$ 在 $$\ell^2(\mathbb N)$$ 上不能对每个向量都有意义（$$g=(1/n)$$ 就是反例）；一旦写清楚"对哪些向量有意义"，一切才谈得上。

2. **对称与自伴的区别，就是"原定义域"与"伴随定义域"是否相等。** $$c_c(\mathbb N)$$ 上的 $$T_0$$ 对称，但伴随的定义域 $$\mathrm{Dom}(T_0^*)$$ 严格更大（$$g=(1/n^2)$$ 就在其中却不在 $$c_c(\mathbb N)$$ 里）；把定义域补到最大（$$\mathrm{Dom}(T_0)$$），两者才相等，才自伴。

3. **无界就是"输入范数固定为 1，输出范数没有上界"，可以亲手用 $$e_N$$ 这样的向量演示，不需要任何抽象理论。**

4. **Cayley 变换把直线卷成圆，半角公式 $$x=\tan\frac\theta2$$ 是它最初等的样子。** 两组具体数值（$$x=1$$ 给 $$90°$$，$$x=1/\sqrt3$$ 给 $$60°$$）和一个标量算例（$$\mu(t)=\frac{t-i}{t+i}$$ 恒在单位圆上）已经把这套机制完全跑通了一遍。

5. **亏指数数的是"进出是否平衡"，决定自伴扩张是否存在。** 一阶算子在有限区间上 $$n_+=n_-=1$$，账平了，自伴扩张构成单位圆上的一个相位族；换到半无穷区间，$$n_+=1\ne0=n_-$$，账平不了，自伴扩张干脆不存在——这就是研 2 提前遇到的"病态"情形，第42章之后的章节会正面处理它。

**交棒给第42章。** 现在你已经能手算出：哪些向量掉出定义域、伴随的定义域确实更大、旋转矩阵与标量情形下 Cayley 变换的具体数值、以及一阶算子在区间上亏指数为 $$1$$（以及为什么换到半线上会失衡）。第42章要做的，是把这些手算过程搬到 $$L^2(\mathbb R)$$ 上真正的位置算子 $$X$$、动量算子 $$P$$、能量算子 $$-\frac{d^2}{dx^2}$$ 和区间上的 $$-\frac{d^2}{dt^2}$$ 上，证明它们对任意情形都成立，并给出严格的一般结构——包括 Hellinger–Toeplitz 定理（定理 3.3）、伴随的一般定义（定义 3.13）、von Neumann 自伴扩张定理（定理 3.25）和完整的 Cayley 变换、谱定理（定理 3.28–3.30）。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch40_Banach代数与C_代数_下.md">← 第40章 Banach 代数与 C\* 代数·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch42_无界算子与Cayley变换_下.md">第42章 无界算子与 Cayley 变换·下 →</a></div>
</div>
