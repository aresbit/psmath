---
layout: default
---

# 第42章: 无界算子与 Cayley 变换·下：完整推导 (Unbounded Operators and the Cayley Transform · Part II: Full Derivation)

> 对应原专栏: MP55–MP56
> 专家依据: `_experts/analysis/functional-analysis.md`（主）+ `_experts/analysis/spectral-theory.md`
> 知识库依据: `opc2/knowledge/math/泛函分析/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）
> 配套预备: 见 第41章 无界算子与 Cayley 变换·上（同一主题的具体铺垫，建议先读）

## 一、本章概要 (Overview)

读完第41章的具体例子后（对角算子的定义域反例、旋转矩阵与标量情形的 Cayley 变换、一阶算子在区间上的亏指数），这里把同样的构造写成一般定义并给出完整证明。

**从哪来**：第 15 到第 40 章把"算子"这件事越做越顺——第 36 章给出谱、预解式与谱半径公式，第 38 章给出谱定理 $$T=\int\lambda\,dE(\lambda)$$，第 40 章把这一切装进 C\*-代数。但这几章共享一个从未被审问的前提：**算子在整空间上有定义，而且有界**。裂缝其实早就露出来了：第 34 章末尾写道，"$$a$$、$$a^\dagger$$、$$X$$、$$P$$ 都不可能是有界算子，'谱'与'定义域'必须在更严格的意义下重新谈"；第 04 章的"诚实清单"更明确地把这笔账记在了本章名下——那里算 $$\sigma(D)=i\mathbb Z$$ 时用的正是一个无界算子。

**核心问题**：量子力学最常用的三个算子——位置 $$\hat x$$、动量 $$\hat p$$、能量 $$-\frac{d^2}{dx^2}$$——**全部无界**。如果可观测量都有界，量子力学的数学在第 40 章就可以结束；它们无界，于是必须回答三个问题：无界算子的"自伴"是什么意思？定义域的选择是技术细节还是实质内容？以及最关键的：**能不能把无界问题变回有界问题？**

**到哪去**：第三个问题的答案是能，手段叫 **Cayley 变换 (Cayley transform)**：$$U=(T-i)(T+i)^{-1}$$ 把无界自伴算子 $$T$$ 换成酉算子 $$U$$。第 38 章的谱定理与第 40 章的函数演算于是整体搬到无界情形。搬完之后，第 44 章要处理量子力学真正的起点——正则对易关系 $$[\hat x,\hat p]=i\hbar I$$。这个等式本身就已经说明 $$\hat x,\hat p$$ 不能都有界（本章研 2 给出证明），所以第 44 章整章都建在"无界"这个前提上，用的正是本章造的语言。

## 二、入口：一道具体的问题 (Entry Problem)

> 题目来源：自编。母题是 MP55 开篇那段"位置算符与动量算符都不能保证结果平方可积"，以及 MP55 末段关于 $$-\frac{d^2}{dt^2}$$ 的算例。

**问题 2.1（动量算子的定义域之谜）.** 取 $$H=L^2(\mathbb R)$$（$$\mathbb R$$ 上平方可积复函数空间，内积与 $$L^2$$ 的基本事实见第 30 章），取 $$\hbar=1$$，把动量算子写成

$$\hat p=-i\frac{d}{dx}.$$

**(i)** 对**任意** $$\psi\in L^2(\mathbb R)$$ 规定 $$\hat p\psi=-i\psi'$$，这个式子一定有意义吗？换句话说，$$\hat p$$ 能当作 $$H\to H$$ 的处处有定义的线性算子吗？如果不能，请**写出一个具体的** $$\psi\in L^2(\mathbb R)$$，使 $$\hat p\psi$$ 无意义。

**(ii)** 退一步，让 $$\hat p$$ 只在紧支集光滑函数 $$C_c^\infty(\mathbb R)$$ 上作用。这时它当然有定义，而且分部积分（边界项为零）给出

$$\langle\hat p\varphi,\psi\rangle=\langle\varphi,\hat p\psi\rangle,\qquad \forall\varphi,\psi\in C_c^\infty(\mathbb R).$$

这个式子说 $$C_c^\infty$$ 上的 $$\hat p$$ 与它的伴随在 $$C_c^\infty$$ 上取值相同。那么能不能就此宣布"$$\hat p$$ 自伴"？

**(iii)** 再退一步：若有人主张把定义域直接放大到整个 $$H$$，同时保持 (ii) 的对称性，会有矛盾吗？

**(iv)**（本章末尾回来）自由能量算子 $$\hat H=-\frac{d^2}{dx^2}$$ 在 $$L^2(\mathbb R)$$ 上谱是 $$[0,\infty)$$，连续、没有空隙，而且 $$\hat H$$ **一个特征向量都没有**。可是物理书上满篇都是 $$e^{ikx}$$——它难道不是 $$\hat H$$ 的特征函数？

**为什么这道题是全章的引子。** (i) 逼出**定义域**这个概念：无界算子不是一个"映射"，而是一对（映射，定义域）。(ii) 逼出**对称与自伴的区分**：$$C_c^\infty$$ 上的等式只覆盖了一小部分向量，而伴随的定义域要大得多。(iii) 用一条硬定理（Hellinger–Toeplitz）把"处处定义"这条路彻底封死，它同时解释了为什么第 18–20 章的世界里没有这个区分。(iv) 是本章技术的最终演示：用 Fourier 变换把 $$\hat H$$ 搬成乘法算子，"有没有特征函数"就变成"某个水平集有没有正测度"。四问的答案分别落在 3.1、3.3、3.1、3.4 节。

## 三、结构：定义与完整推导 (Structure & Proof)

本节按六步走：先立"算子带定义域"（3.1），再补"无界算子怎么谈连续性"（3.2），然后处理伴随、对称、自伴这三个最容易混的概念（3.3），接着把三个基本算子逐个算清楚（3.4），用亏指数说明"定义域就是边界条件"（3.5），最后用 Cayley 变换把无界问题化归为酉算子（3.6），并回头把第 04 章的债还掉（3.7）。

### 3.1 无界算子：定义域是算子的一部分

**定义 3.1（无界算子, unbounded operator）。** 设 $$H$$ 是复 Hilbert 空间。$$H$$ 上的一个**算子 (operator)** 是一个线性映射

$$T:\ \mathrm{Dom}(T)\ \longrightarrow\ H,$$

其中 $$\mathrm{Dom}(T)\subseteq H$$ 是一个线性子空间，称为 $$T$$ 的**定义域 (domain)**。若 $$\mathrm{Dom}(T)=H$$ 且存在常数 $$C<\infty$$ 使

$$\lVert Tx\rVert\le C\lVert x\rVert,\qquad \forall x\in H,$$

则称 $$T$$ **有界 (bounded)**，并定义**算子范数** $$\lVert T\rVert=\sup_{\lVert x\rVert\le1}\lVert Tx\rVert$$。若不存在这样的 $$C$$，称 $$T$$ **无界 (unbounded)**。

注意定义里的双重含义：$$\mathrm{Dom}(T)\ne H$$ 的算子按上述定义自动"无界"，但本书关心的是**既无界又稠定**的那些算子——它们是量子力学里的可观测量。所以"无界"这个标签的作用不是把 $$\mathrm{Dom}(T)\ne H$$ 的情形排除出去，而是提醒我们：对这类算子，**定义域必须与映射一起写出来，否则算子是未定义的**。同一个公式 $$-i\frac{d}{dx}$$，配上不同的定义域，就是不同的算子，可以有不同的谱（3.4 与 3.5 节会给实例）。

**定义 3.2（稠定算子, densely defined operator）。** 若 $$\overline{\mathrm{Dom}(T)}=H$$，即定义域在 $$H$$ 中稠密，称 $$T$$ **稠定**。

要求稠定不是洁癖，而是伴随算子存在的前提：以下 3.3 节中，构造 $$T^*$$ 时要用到 Riesz 表示定理，而它要求泛函定义在一个稠密子空间上（第 30 章）。物理上稠定是自明的：可观测量必须能在足够多的态上被测量。

**定理 3.3（Hellinger–Toeplitz 定理）。** 设 $$T:H\to H$$ 是**处处定义**的线性算子，且**对称**，即

$$\langle Tx,y\rangle=\langle x,Ty\rangle,\qquad \forall x,y\in H .$$

则 $$T$$ 有界。

*证明思路*：把每个 $$y$$ 变成一个泛函 $$\varphi_y(x)=\langle x,Ty\rangle$$。对称性让"$$x$$ 固定、$$y$$ 取遍单位球"这族泛函恰好逐点有界，于是可以动用一致有界原理（第 36 章），把逐点界升级为一致界。

*证明*：对每个 $$y\in H$$ 定义 $$\varphi_y:H\to\mathbb C$$，$$\varphi_y(x)=\langle x,Ty\rangle$$。由内积对第一变元的线性和 Cauchy–Schwarz 不等式（第 30 章），$$\varphi_y$$ 是线性泛函且

$$\lvert\varphi_y(x)\rvert\le\lVert x\rVert\cdot\lVert Ty\rVert,$$

所以 $$\varphi_y$$ 连续，$$\lVert\varphi_y\rVert=\lVert Ty\rVert$$（Riesz 表示定理反过来给等号：取 $$x=Ty/\lVert Ty\rVert$$ 时等号成立）。

现在固定 $$x\in H$$。由对称性 $$\langle x,Ty\rangle=\langle Tx,y\rangle$$，

$$\sup_{\lVert y\rVert\le1}\lvert\varphi_y(x)\rvert=\sup_{\lVert y\rVert\le1}\lvert\langle Tx,y\rangle\rvert=\lVert Tx\rVert<\infty .$$

这里两次用到同一个东西：内积范数的对偶刻画 $$\lVert u\rVert=\sup_{\lVert v\rVert\le1}\lvert\langle u,v\rangle\rvert$$。于是族 $$\lbrace\varphi_y\rbrace_{\lVert y\rVert\le1}$$ 在每一点 $$x$$ 处有界。由一致有界原理，存在 $$C<\infty$$ 使

$$\sup_{\lVert y\rVert\le1}\lVert\varphi_y\rVert\le C .$$

代回 $$\lVert\varphi_y\rVert=\lVert Ty\rVert$$ 得 $$\sup_{\lVert y\rVert\le1}\lVert Ty\rVert\le C$$，即 $$T$$ 有界。$$\blacksquare$$

**推论 3.4（对称与自伴的区分只存在于无界情形）。** 若 $$T$$ 稠定对称且无界，则 $$\mathrm{Dom}(T)\ne H$$。因此在有界算子的世界里，"对称"与"自伴"是同一件事（见 3.3 节的 定理 3.17）：有界对称算子 $$T$$ 满足 $$T=T^*$$。**只有在无界情形下，这两个词才分家**——这就是本章标题里"对称 vs 自伴"的由来，也是 MP55 反复强调的那一点。

### 3.2 图像、图像范数、闭算子

无界算子没有算子范数，所以"$$x_n\to x$$ 是否蕴含 $$Tx_n\to Tx$$"这句话不能直接说。替代品是把算子看成一个几何对象。

**定义 3.5（图像, graph）。** 对算子 $$T:\mathrm{Dom}(T)\to H$$，乘积空间 $$H\oplus H$$ 的子集

$$\Gamma(T)=\bigl\lbrace (x,Tx)\ :\ x\in\mathrm{Dom}(T)\bigr\rbrace$$

称为 $$T$$ 的**图像**。$$H\oplus H$$ 上取内积 $$\langle(x_1,y_1),(x_2,y_2)\rangle=\langle x_1,x_2\rangle+\langle y_1,y_2\rangle$$，相应地 $$\lVert(x,y)\rVert=\sqrt{\lVert x\rVert^2+\lVert y\rVert^2}$$；$$H\oplus H$$ 是 Hilbert 空间。$$\Gamma(T)$$ 是 $$H\oplus H$$ 的线性子空间。

**定义 3.6（闭算子, closed operator）。** 若 $$\Gamma(T)$$ 在 $$H\oplus H$$ 中是闭子集，称 $$T$$ **闭**。展开成序列语言：$$T$$ 闭，当且仅当对任意 $$x_n\in\mathrm{Dom}(T)$$，

$$x_n\to x\ \text{且}\ Tx_n\to y\qquad\Longrightarrow\qquad x\in\mathrm{Dom}(T)\ \text{且}\ Tx=y .$$

这个定义是 MP55 里"$$B$$ 是 $$A$$ 的扩张"时那个 $$\Gamma(A)\subset\Gamma(B)$$ 的语言的精确化。闭性是"在图像里的极限不跑出去"，它取代了无界算子缺失的连续性。

**定义 3.7（图像范数, graph norm）。** 在 $$\mathrm{Dom}(T)$$ 上定义

$$\lVert x\rVert_T=\sqrt{\lVert x\rVert^2+\lVert Tx\rVert^2}.$$

**命题 3.8（图像范数完备与闭性等价）。** $$\lVert\cdot\rVert_T$$ 是 $$\mathrm{Dom}(T)$$ 上的范数；并且

$$T\ \text{闭}\qquad\Longleftrightarrow\qquad \bigl(\mathrm{Dom}(T),\lVert\cdot\rVert_T\bigr)\ \text{完备}.$$

*证明*：**第一句**：非负性与齐次性立刻（$$\lVert\cdot\rVert$$ 是范数）。三角不等式：

$$\lVert x+y\rVert_T^2=\lVert x+y\rVert^2+\lVert Tx+Ty\rVert^2=\bigl\lVert (x+y,\,Tx+Ty)\bigr\rVert^2,$$

而 $$(x+y,Tx+Ty)=(x,Tx)+(y,Ty)$$，故由 $$H\oplus H$$ 中范数的三角不等式即得。正定性同理：$$\lVert x\rVert_T=0$$ 蕴含 $$(x,Tx)=0$$ 蕴含 $$x=0$$。

**第二句**：映射 $$\Phi:x\mapsto(x,Tx)$$ 是 $$\mathrm{Dom}(T)$$ 到 $$\Gamma(T)$$ 的**等距双射**（按定义，$$\lVert x\rVert_T=\lVert(x,Tx)\rVert$$，且像恰为 $$\Gamma(T)$$）。等距双射保持柯西列与收敛，所以前者完备当且仅当 $$\Gamma(T)$$ 作为 $$H\oplus H$$ 的子空间完备。$$H\oplus H$$ 完备，而完备度量空间的子空间完备等价于它闭。于是 $$\lVert\cdot\rVert_T$$ 完备 $$\iff\Gamma(T)$$ 闭 $$\iff T$$ 闭。$$\blacksquare$$

**推论 3.9（"无界"= 换个范数就有界）。** 若 $$T$$ 闭，则 $$T:(\mathrm{Dom}(T),\lVert\cdot\rVert_T)\to H$$ 是有界线性算子，且 $$\lVert T\rVert\le1$$。

*证明*：$$\lVert Tx\rVert\le\sqrt{\lVert x\rVert^2+\lVert Tx\rVert^2}=\lVert x\rVert_T$$，所以范数不超过 1。要证"有界线性算子"，还需要定义域空间是赋范空间——由 命题 3.8 它甚至是 Hilbert 空间。$$\blacksquare$$

这条推论是理解本章的一把钥匙：**无界算子并不"坏"，它只是对 $$L^2$$ 的范数无界；对图像范数它乖得很。**第 04 章算 $$D$$ 的谱时"逐频率除以 $$ik-\lambda$$"能奏效，本质上就是因为换了这把尺子。

**定义 3.10（扩张、可闭、闭包）。** 设 $$S,T$$ 是 $$H$$ 上的算子。若 $$\Gamma(S)\subseteq\Gamma(T)$$，称 $$T$$ 是 $$S$$ 的**扩张 (extension)**，记 $$S\subseteq T$$；展开即 $$\mathrm{Dom}(S)\subseteq\mathrm{Dom}(T)$$ 且 $$T$$ 在 $$\mathrm{Dom}(S)$$ 上与 $$S$$ 相同。若 $$\overline{\Gamma(S)}$$ 也是某个算子的图像，称 $$S$$ **可闭 (closable)**，对应的算子称 $$S$$ 的**闭包 (closure)**，记 $$\overline S$$（$$\Gamma(\overline S)=\overline{\Gamma(S)}$$）。

**命题 3.11（可闭判据）。** $$S$$ 可闭，当且仅当：每当 $$x_n\in\mathrm{Dom}(S)$$ 满足 $$x_n\to0$$ 且 $$Sx_n\to y$$，必有 $$y=0$$。

*证明*：$$\overline{\Gamma(S)}$$ 是图像，等价于 $$\overline{\Gamma(S)}$$ 与"竖直子空间"$$\lbrace0\rbrace\oplus H$$ 的交只有 $$(0,0)$$——因为 $$\Gamma(S)$$ 已经是图像（每个 $$x$$ 至多配一个 $$Sx$$），闭包要破坏这一点，唯一可能是某个 $$(0,y)$$ 落进来。

而 $$(0,y)\in\overline{\Gamma(S)}$$ 按定义就是：存在 $$(x_n,Sx_n)\in\Gamma(S)$$ 使 $$(x_n,Sx_n)\to(0,y)$$，即 $$x_n\to0$$ 且 $$Sx_n\to y$$。所以"只有 $$(0,0)$$"就是判据本身。$$\blacksquare$$

**命题 3.12（稠定对称算子可闭）。** 稠定对称算子（见 定义 3.15）总可闭，且其闭包 $$\overline S\subseteq S^*$$。

*证明*：设 $$x_n\in\mathrm{Dom}(S)$$、$$x_n\to0$$、$$Sx_n\to y$$。任取 $$z\in\mathrm{Dom}(S)$$，由对称性

$$\langle y,z\rangle=\lim_{n}\langle Sx_n,z\rangle=\lim_{n}\langle x_n,Sz\rangle=0 .$$

（中间一步用 $$S$$ 对称；最后一步用 $$x_n\to0$$。）所以 $$y\perp\mathrm{Dom}(S)$$。而 $$S$$ 稠定，$$\mathrm{Dom}(S)$$ 在 $$H$$ 中稠密，故 $$y=0$$。由 命题 3.11，$$S$$ 可闭。

再证 $$\overline S\subseteq S^*$$：$$\mathrm{Dom}(S^*)=\lbrace z:\ x\mapsto\langle Sx,z\rangle\ \text{连续}\rbrace$$ 是闭子空间，而 $$\Gamma(S)\subseteq\Gamma(S^*)$$（下一节 定理 3.14），取闭包得 $$\Gamma(\overline S)=\overline{\Gamma(S)}\subseteq\Gamma(S^*)$$，因为 $$\Gamma(S^*)$$ 本身就闭。$$\blacksquare$$

### 3.3 伴随、对称、自伴

**定义 3.13（伴随算子, adjoint operator）。** 设 $$T$$ 稠定。令

$$\mathrm{Dom}(T^*)=\Bigl\lbrace\, y\in H\ :\ \text{泛函}\ x\mapsto\langle Tx,y\rangle\ \text{在}\ \mathrm{Dom}(T)\ \text{上连续}\,\Bigr\rbrace .$$

对 $$y\in\mathrm{Dom}(T^*)$$，该泛函唯一地延拓为 $$H$$ 上的连续线性泛函，再由 Riesz 表示定理（第 30 章）唯一地写成 $$x\mapsto\langle x,z\rangle$$ 的形式，$$z\in H$$。规定 $$T^*y=z$$，即

$$\langle Tx,y\rangle=\langle x,T^*y\rangle,\qquad \forall x\in\mathrm{Dom}(T).$$

等价说法：$$y\in\mathrm{Dom}(T^*)$$ 当且仅当存在（此时唯一的）$$z\in H$$ 使上式对一切 $$x\in\mathrm{Dom}(T)$$ 成立。

对称性条件在这里是必需的：没有稠密性，延拓不唯一，$$z$$ 也就不唯一。

**定理 3.14（伴随的两条基本性质）。**

(i) $$T^*$$ 恒为闭算子（无论 $$T$$ 是否闭）。

(ii) 若 $$S\subseteq T$$ 且两者稠定，则 $$T^*\subseteq S^*$$（伴随把扩张反过来）。

*证明*：(i) 设 $$y_n\in\mathrm{Dom}(T^*)$$、$$y_n\to y$$、$$T^*y_n\to z$$。对每个固定的 $$x\in\mathrm{Dom}(T)$$，内积对第二变元连续，故

$$\langle Tx,y\rangle=\lim_n\langle Tx,y_n\rangle=\lim_n\langle x,T^*y_n\rangle=\langle x,z\rangle .$$

按 定义 3.13，$$y\in\mathrm{Dom}(T^*)$$ 且 $$T^*y=z$$。这正是 定义 3.6 的闭性判据。$$\square$$

(ii) 设 $$y\in\mathrm{Dom}(T^*)$$，记 $$z=T^*y$$，则 $$\langle Tx,y\rangle=\langle x,z\rangle$$ 对一切 $$x\in\mathrm{Dom}(T)$$ 成立。因 $$\mathrm{Dom}(S)\subseteq\mathrm{Dom}(T)$$ 且 $$T$$ 在 $$\mathrm{Dom}(S)$$ 上等于 $$S$$，故对一切 $$x\in\mathrm{Dom}(S)$$ 也有 $$\langle Sx,y\rangle=\langle x,z\rangle$$。于是 $$y\in\mathrm{Dom}(S^*)$$ 且 $$S^*y=z=T^*y$$。$$\blacksquare$$

注意 (i) 的份量：**伴随总是闭的**。这是后面所有"自伴算子自动闭"的来源。

**定义 3.15（对称算子, symmetric operator）。** 稠定算子 $$T$$ 称为**对称**的，若

$$\langle Tx,y\rangle=\langle x,Ty\rangle,\qquad \forall x,y\in\mathrm{Dom}(T).$$

由 定义 3.13 立得：$$T$$ 对称 $$\iff$$ $$T\subseteq T^*$$，即 $$\mathrm{Dom}(T)\subseteq\mathrm{Dom}(T^*)$$ 且在 $$\mathrm{Dom}(T)$$ 上 $$T^*=T$$。对称性还有一个等价的"数"的刻画：$$\langle Tx,x\rangle\in\mathbb R$$ 对一切 $$x\in\mathrm{Dom}(T)$$（用极化恒等式把 $$\langle Tx,y\rangle$$ 从二次型还原，第 30 章）。

**定义 3.16（自伴 / 本质自伴, self-adjoint / essentially self-adjoint）。** 稠定算子 $$T$$ 称**自伴**，若 $$T=T^*$$，即 $$T$$ 对称**且** $$\mathrm{Dom}(T)=\mathrm{Dom}(T^*)$$。稠定对称算子 $$T$$ 称**本质自伴**，若其闭包 $$\overline T$$ 自伴。（此时 $$\overline T$$ 是 $$T$$ 唯一的自伴扩张。）

对称与自伴的差别就是一句话：**定义域是否与伴随的定义域相等**。听起来是小事，3.4 与 3.5 节会显示它是全部物理内容所在。

**定理 3.17（自伴性的判定）。** 设 $$T$$ 稠定对称。则

$$T\ \text{自伴}\qquad\Longleftrightarrow\qquad \mathrm{ran}(T+i)=H\qquad\Longleftrightarrow\qquad \mathrm{ran}(T-i)=H .$$

*证明思路*：先立一个关键恒等式：对称性让交叉项相消，于是

$$\lVert(T-\lambda)x\rVert^2=\lVert(T-a)x\rVert^2+b^2\lVert x\rVert^2,\qquad \lambda=a+ib. \tag{3.1}$$

（展开 $$\lVert(T-a-ib)x\rVert^2$$，两个交叉项分别是 $$\overline{-ib}\,\langle x,(T-a)x\rangle$$ 与 $$-ib\,\langle(T-a)x,x\rangle$$；由对称性 $$\langle(T-a)x,x\rangle=\langle x,(T-a)x\rangle\in\mathbb R$$，两者互为共轭且和为 $$0$$。）取 $$\lambda=\pm i$$（$$a=0,b=\pm1$$）得

$$\lVert(T\pm i)x\rVert^2=\lVert Tx\rVert^2+\lVert x\rVert^2\ \ge\ \lVert x\rVert^2 . \tag{3.2}$$

这说明 $$T\pm i$$ 单射，且 $$(T+i)^{-1}:\mathrm{ran}(T+i)\to\mathrm{Dom}(T)$$ 是等距（3.6 节要用）。剩下的论证用一个"搬回去"的技巧。

*证明*：先设 $$T=T^*$$。

*单是满的*：$$T$$ 自伴故 $$T$$ 闭（由 定理 3.14(i) 的 $$T^*$$ 恒闭），于是 $$\mathrm{ran}(T+i)$$ 闭：若 $$(T+i)x_n\to w$$，则由 (3.2) $$x_n$$ 是柯西列，$$x_n\to x$$，又 $$Tx_n=(T+i)x_n-ix_n\to w-ix$$；由 $$T$$ 闭得 $$x\in\mathrm{Dom}(T)$$、$$Tx=w-ix$$，故 $$w=(T+i)x\in\mathrm{ran}(T+i)$$。再算正交补：对 $$u\in H$$，

$$u\perp\mathrm{ran}(T+i)\iff\langle(T+i)x,u\rangle=0\ \ \forall x\in\mathrm{Dom}(T)\iff\langle x,(T^*-i)u\rangle=0\ \ \forall x\in\mathrm{Dom}(T),$$

而 $$\mathrm{Dom}(T)$$ 稠密，故等价于 $$(T^*-i)u=0$$，即 $$T^*u=iu$$。因 $$T^*=T$$，这就是 $$(T-i)u=0$$，由 (3.2) 得 $$u=0$$。所以 $$\mathrm{ran}(T+i)^\perp=\lbrace0\rbrace$$。闭 + 稠密（正交补为 0）⇒ $$\mathrm{ran}(T+i)=H$$。同理 $$\mathrm{ran}(T-i)=H$$。

*反方向*：设 $$\mathrm{ran}(T\pm i)=H$$。由 $$T\subseteq T^*$$ 只需证 $$\mathrm{Dom}(T^*)\subseteq\mathrm{Dom}(T)$$。取 $$y\in\mathrm{Dom}(T^*)$$。因 $$\mathrm{ran}(T+i)=H$$，存在 $$x\in\mathrm{Dom}(T)$$ 使

$$(T+i)x=(T^*+i)y .$$

对任意 $$z\in\mathrm{Dom}(T)$$ 计算：

$$\langle(T+i)x,z\rangle=\langle Tx,z\rangle+i\langle x,z\rangle=\langle x,Tz\rangle+i\langle x,z\rangle=\langle x,(T+i)z\rangle,$$

$$\langle(T^*+i)y,z\rangle=\langle T^*y,z\rangle+i\langle y,z\rangle=\langle y,Tz\rangle+i\langle y,z\rangle=\langle y,(T+i)z\rangle .$$

两式相等给出 $$\langle x-y,(T+i)z\rangle=0$$ 对一切 $$z\in\mathrm{Dom}(T)$$ 成立。而 $$\lbrace(T+i)z\rbrace=\mathrm{ran}(T+i)=H$$，故 $$x-y\perp H$$，即 $$y=x\in\mathrm{Dom}(T)$$。于是 $$(T+i)y=(T+i)x=(T^*+i)y$$，比较得 $$Ty=T^*y$$。所以 $$T^*=T$$。$$\blacksquare$$

**推论 3.18（自伴算子的极大性）。** 自伴算子没有真的对称扩张：若 $$T\subseteq S$$ 且 $$S$$ 对称，则 $$S=T$$。

*证明*：由 定理 3.14(ii)，$$T\subseteq S$$ 给 $$S^*\subseteq T^*$$；又 $$S$$ 对称给 $$S\subseteq S^*$$。合起来 $$S\subseteq S^*\subseteq T^*=T$$，而 $$T\subseteq S$$，故 $$S=T$$。$$\blacksquare$$

**注（反方向不成立，这是无界情形独有的怪事）。** 极大对称并不蕴含自伴。例：取单侧移位 $$U(x_0,x_1,\dots)=(0,x_0,x_1,\dots)$$——它是等距，$$\mathrm{Dom}(U)=\ell^2$$ 而 $$\mathrm{ran}(U)=\lbrace x_0=0\rbrace\subsetneq\ell^2$$，故 $$U$$ 不酉；令 $$T=i(I+U)(I-U)^{-1}$$（见 3.6 节），则 $$T$$ 稠定、对称、极大，但由 定理 3.28 不是自伴。有界算子无此现象。

**定理 3.19（自伴算子的谱在实轴上）。** 设 $$T$$ 自伴，则 $$\sigma(T)\subseteq\mathbb R$$；更精确地，对 $$\lambda=a+ib$$ 与 $$x\in\mathrm{Dom}(T)$$ 有 (3.1)，故 $$\lVert(T-\lambda)x\rVert\ge\lvert b\rvert\lVert x\rVert$$。

*证明*：设 $$\lambda=a+ib$$ 且 $$b\ne0$$。由上式和 (3.1)：

- $$T-\lambda$$ 单射；
- $$\mathrm{ran}(T-\lambda)$$ 闭：若 $$(T-\lambda)x_n\to w$$，则 $$\lVert x_n-x_m\rVert\le\lvert b\rvert^{-1}\lVert(T-\lambda)(x_n-x_m)\rVert\to0$$，$$x_n\to x$$，且 $$Tx_n=(T-\lambda)x_n+\lambda x_n\to w+\lambda x$$；$$T$$ 闭（$$T=T^*$$ 与 定理 3.14(i)）给出 $$x\in\mathrm{Dom}(T)$$ 且 $$w=(T-\lambda)x$$；
- $$\mathrm{ran}(T-\lambda)^\perp=\ker(T^*-\overline\lambda)=\ker(T-\overline\lambda)=\lbrace0\rbrace$$，因为 $$b\ne0$$ 时 $$T-\overline\lambda$$ 单射（$$\overline\lambda$$ 的虚部是 $$-b$$）。

闭 + 正交补为零 ⇒ $$\mathrm{ran}(T-\lambda)=H$$，故 $$T-\lambda$$ 是双射。再加上 $$\lVert(T-\lambda)^{-1}\rVert\le\lvert b\rvert^{-1}$$（直接由不等式），$$\lambda\notin\sigma(T)$$。$$\blacksquare$$

这条定理是"可观测量对应自伴算子"的技术根据：谱是实的，测量结果才落在实轴上。

### 3.4 三个基本例子：位置、动量、$$-\frac{d^2}{dx^2}$$

先把一个技术事实放在手边。

**引理 3.20（$$H^1$$ 的 Fourier 刻画）。** 记

$$H^1(\mathbb R)=\Bigl\lbrace f\in L^2(\mathbb R)\ :\ \int_{\mathbb R}\bigl(1+p^2\bigr)\lvert\hat f(p)\rvert^2\,dp<\infty\Bigr\rbrace,$$

约定 Fourier 变换 $$\hat f(p)=\frac{1}{\sqrt{2\pi}}\int e^{-ipx}f(x)\,dx$$。则 $$H^1(\mathbb R)$$ 恰由那些"弱导数仍在 $$L^2$$"的函数组成，且

$$\widehat{f'}(p)=ip\,\hat f(p),\qquad \lVert f'\rVert_2^2=\int p^2\lvert\hat f(p)\rvert^2\,dp .$$

*证明思路*：把"求导 = 乘 $$ip$$"从 Schwartz 函数延拓到 $$H^1$$。

*证明*：$$C_c^\infty(\mathbb R)\subseteq H^1$$，且 $$C_c^\infty$$ 在 $$L^2$$ 中稠密，故 $$H^1$$ 稠密。若 $$f\in L^2$$ 且弱导数 $$f'\in L^2$$，对任意 Schwartz 函数 $$\phi$$，由弱导数的定义与 Plancherel（第 30 章的 Fourier 理论）

$$\int f'\overline\phi=-\int f\overline{\phi'}=-\int \hat f\overline{\widehat{\phi'}}=\int \hat f\overline{ip\hat\phi}=\int(ip\hat f)\overline{\hat\phi},$$

即 $$\hat{f'}=ip\hat f$$ 作为分布等式，于是 $$\lVert f'\rVert_2^2=\lVert\widehat{f'}\rVert_2^2=\int p^2\lvert\hat f\rvert^2$$。反过来，若 $$\int(1+p^2)\lvert\hat f\rvert^2<\infty$$，则 $$p\hat f\in L^2$$；令 $$g$$ 为 $$ip\hat f$$ 的逆 Fourier 变换，则 $$g\in L^2$$ 且 $$\hat g=ip\hat f=\widehat{f'}$$（分布意义），故 $$f'=g\in L^2$$。$$\blacksquare$$

**命题 3.21（位置算子自伴）。** 在 $$H=L^2(\mathbb R)$$ 上定义

$$(X\psi)(x)=x\psi(x),\qquad \mathrm{Dom}(X)=\Bigl\lbrace\psi\in L^2\ :\ \int_{\mathbb R}\lvert x\psi(x)\rvert^2\,dx<\infty\Bigr\rbrace .$$

则 $$\mathrm{Dom}(X)$$ 稠密，$$X$$ 对称且自伴。

*证明*：**稠密**：$$C_c^\infty(\mathbb R)\subseteq\mathrm{Dom}(X)$$（紧支集函数被 $$x$$ 乘后仍在 $$L^2$$），而 $$C_c^\infty$$ 在 $$L^2$$ 中稠密。

**对称**：$$x$$ 取实值，

$$\langle X\psi,\varphi\rangle=\int x\psi(x)\overline{\varphi(x)}\,dx=\int\psi(x)\overline{x\varphi(x)}\,dx=\langle\psi,X\varphi\rangle .$$

**自伴**：设 $$\varphi\in\mathrm{Dom}(X^*)$$ 并记 $$X^*\varphi=z$$，即 $$\int x\psi\overline\varphi=\int\psi\overline z$$ 对一切 $$\psi\in\mathrm{Dom}(X)$$。取 $$\psi$$ 为任意紧支集 $$L^2$$ 函数，则 $$\int\psi\overline{x\varphi}=\int\psi\overline z$$ 对一切这样的 $$\psi$$ 成立，故 $$x\varphi=z$$（几乎处处）。于是 $$x\varphi\in L^2$$，即 $$\varphi\in\mathrm{Dom}(X)$$，且 $$X^*\varphi=x\varphi=X\varphi$$。故 $$\mathrm{Dom}(X^*)=\mathrm{Dom}(X)$$、$$X^*=X$$。$$\blacksquare$$

**定理 3.22（动量算子自伴）。** 在 $$H=L^2(\mathbb R)$$ 上取 $$\mathrm{Dom}(P)=H^1(\mathbb R)$$，$$P\psi=-i\psi'$$。则 $$P$$ 稠定、对称、自伴，且

$$\lVert P\psi\rVert^2=\int p^2\lvert\hat\psi(p)\rvert^2\,dp .$$

*证明*：**稠密**：$$C_c^\infty\subseteq H^1$$。

**对称**：设 $$\psi,\varphi\in H^1$$。乘积 $$\psi\overline\varphi$$ 的弱导数 $$\psi'\overline\varphi+\psi\overline{\varphi'}\in L^1$$，故 $$\psi\overline\varphi$$ 绝对连续；又 $$\psi\overline\varphi\in L^1$$ 且其导数可积，故 $$\psi\overline\varphi$$ 在 $$\pm\infty$$ 有极限，而该极限必为 $$0$$（否则模方在无穷远处不趋于零，与可积性矛盾——$$H^1\subset C_0$$，这是 Sobolev 嵌入，第 30 章）。于是 $$\int(\psi\overline\varphi)'=0$$，即

$$\int\psi'\overline\varphi=-\int\psi\overline{\varphi'}.$$

两边乘 $$-i$$：

$$\langle P\psi,\varphi\rangle=-i\!\int\!\psi'\overline\varphi=i\!\int\!\psi\overline{\varphi'}=\int\psi\overline{(-i\varphi')}=\langle\psi,P\varphi\rangle .$$

**自伴**：设 $$\varphi\in L^2$$。由 Plancherel 与 引理 3.20，对 $$\psi\in H^1$$，

$$\langle P\psi,\varphi\rangle=\int_{\mathbb R}p\,\hat\psi(p)\overline{\hat\varphi(p)}\,dp .$$

记 $$h(p)=p\hat\varphi(p)$$。泛函 $$\psi\mapsto\langle P\psi,\varphi\rangle$$ 在 $$(\mathrm{Dom}(P),\lVert\cdot\rVert_{L^2})$$ 上连续，当且仅当存在 $$C$$ 使

$$\Bigl\lvert\int \hat\psi\,\overline{h}\,dp\Bigr\rvert\le C\lVert\hat\psi\rVert_2\qquad\text{对一切}\ \psi\in H^1 .$$

$$\lbrace\hat\psi:\psi\in H^1\rbrace$$ 在 $$L^2$$ 中稠密（含 $$C_c^\infty$$ 的 Fourier 像所张成的空间），故上述条件等价于 $$h\in L^2$$ 且此泛函就是 $$\hat\psi\mapsto\langle\hat\psi,h\rangle$$。因此

$$\mathrm{Dom}(P^*)=\lbrace\varphi\in L^2:\ p\hat\varphi\in L^2\rbrace=H^1=\mathrm{Dom}(P),$$

且 $$P^*\varphi$$ 的 Fourier 变换是 $$p\hat\varphi$$，即 $$P^*\varphi=-i\varphi'=P\varphi$$（引理 3.20）。故 $$P^*=P$$。最后一条等式就是 引理 3.20 第二式。$$\blacksquare$$

**入口题 (i) 的具体反例。** 取 $$\psi=\chi_{[0,1]}$$（区间 $$[0,1]$$ 的指示函数）。它是 $$L^2(\mathbb R)$$ 的元素，但 $$\psi$$ 的弱导数作为分布是 $$\delta_0-\delta_1$$，不是 $$L^2$$ 函数（$$H^1$$ 的函数绝对连续，而 $$\psi$$ 在 $$0,1$$ 处跳跃），故 $$\psi\notin H^1=\mathrm{Dom}(P)$$。于是 $$\hat p\psi=-i\psi'$$ 在 $$L^2$$ 中无意义——这正是"处处定义"走不通的样子。

**定理 3.23（自由能量算子）。** 在 $$H=L^2(\mathbb R)$$ 上取 $$\mathrm{Dom}(H_0)=H^2(\mathbb R)=\lbrace\psi\in L^2:\ \int(1+p^2)^2\lvert\hat\psi\rvert^2<\infty\rbrace$$，$$H_0\psi=-\psi''$$。则 $$H_0$$ 自伴，谱为

$$\sigma(H_0)=[0,\infty),$$

且 $$H_0$$ **没有特征向量**；它的谱全是连续谱。

*证明*：$$H_0=P^2$$，而 $$P$$ 自伴（定理 3.22）；自伴算子的平方是自伴的、正算子（$$\langle P^2\psi,\psi\rangle=\lVert P\psi\rVert^2\ge0$$）。由 Fourier 变换，$$P$$ 酉等价于 $$L^2(\mathbb R)$$ 上"乘 $$p$$"的乘法算子 $$M_p$$：$$\widehat{P\psi}=p\hat\psi$$。于是 $$H_0$$ 酉等价于乘 $$p^2$$ 的乘法算子 $$M_{p^2}$$，定义域为 $$\lbrace\hat\psi:p^2\hat\psi\in L^2\rbrace=H^2$$。

对乘法算子有两条可直接验证的事实（第 36 章乘法算子一段）：$$\sigma(M_{p^2})=\overline{\lbrace p^2\bigr\rbrace}=[0,\infty)$$；且 $$\lambda$$ 是特征值当且仅当集合 $$\lbrace p:p^2=\lambda\rbrace$$ 有正测度。这个集合是有限点集（$$p=\pm\sqrt\lambda$$，或 $$p=0$$），Lebesgue 测度为零，所以 $$M_{p^2}$$ 没有特征值。酉等价保持谱与"是否特征值"，故 $$H_0$$ 的谱为 $$[0,\infty)$$ 且无特征向量。$$\blacksquare$$

这就回答了入口题 (iv)：$$e^{ikx}$$ 满足 $$-\frac{d^2}{dx^2}e^{ikx}=k^2e^{ikx}$$，但它不是 $$L^2(\mathbb R)$$ 的元素（$$\lvert e^{ikx}\rvert=1$$，模方积分发散），所以它不在 $$\mathrm{Dom}(H_0)$$ 里，不是特征向量。物理上这类解叫"广义特征函数"，数学上的正确说法是：$$k^2$$ 属于**连续谱**，$$e^{ikx}$$ 是谱测度的广义向量（第 38 章的 PVM 语言）。**定义域把物理直觉里的"本征函数"挡在了 Hilbert 空间之外——这正是本章一开始就强调"定义域是算子的一部分"的原因。**

### 3.5 亏指数与自伴扩张：定义域就是边界条件

入口题 (ii) 的答案是"不能"。理由在本节。把一个对称算子限制到太小的定义域上，它就不再自伴，而是留下若干"缺口"。

**定义 3.24（亏子空间与亏指数, deficiency subspace / deficiency indices）。** 设 $$T$$ 稠定对称。称

$$\mathscr K_+=\ker(T^*-i),\qquad \mathscr K_-=\ker(T^*+i)$$

为 $$T$$ 的**亏子空间**，$$n_\pm=\dim\mathscr K_\pm$$ 为**亏指数 (deficiency indices)**。由 (3.2) 与 $$\mathrm{ran}(T\pm i)^\perp=\ker(T^*\mp i)$$（3.3 节已算）得 $$n_\pm=\dim\ker(T^*\mp i)=\dim\mathrm{ran}(T\pm i)^\perp=\mathrm{codim}\,\mathrm{ran}(T\pm i)$$（同号：$$\mathscr K_+=\ker(T^*-i)=\mathrm{ran}(T+i)^\perp$$ 给出 $$n_+=\mathrm{codim}\,\mathrm{ran}(T+i)$$，$$\mathscr K_-=\ker(T^*+i)=\mathrm{ran}(T-i)^\perp$$ 给出 $$n_-=\mathrm{codim}\,\mathrm{ran}(T-i)$$；下文 定理 3.25 的证明里 $$n_+=\dim D^\perp$$、$$D=\mathrm{ran}(T+i)$$ 用的正是这一版本，注意不要错记成异号）；而 $$T$$ 自伴 $$\iff$$ $$n_+=n_-=0$$（定理 3.17）。

**定理 3.25（von Neumann 自伴扩张定理）。** 稠定对称算子 $$T$$ 有自伴扩张，当且仅当 $$n_+=n_-$$。

*证明思路*：3.6 节会证明"Cayley 变换把自伴算子一对一换成酉算子"（定理 3.28）。同一个变换把"$$T$$ 的对称扩张"换成"$$U$$ 的等距扩张"，把"$$T$$ 的自伴扩张"换成"$$U$$ 的酉扩张"。于是问题变成：一个等距 $$U:\mathrm{Dom}(U)\to H$$ 能扩成酉算子吗？

*证明*：设 $$U=(T-i)(T+i)^{-1}$$，$$\mathrm{Dom}(U)=\mathrm{ran}(T+i)=:D$$，$$\mathrm{ran}(U)=\mathrm{ran}(T-i)=:R$$（定理 3.27(i)(ii)）。注意

$$D^\perp=\mathrm{ran}(T+i)^\perp=\ker(T^*-i)=\mathscr K_+,\qquad R^\perp=\mathrm{ran}(T-i)^\perp=\ker(T^*+i)=\mathscr K_-,$$

故 $$n_+=\dim D^\perp$$、$$n_-=\dim R^\perp$$。

**(一) $$T$$ 有自伴扩张 $$\iff$$ $$U$$ 有酉扩张。** 设 $$S\supseteq T$$ 自伴。$$S$$ 的 Cayley 变换 $$V=(S-i)(S+i)^{-1}$$ 是酉算子（定理 3.28），且 $$\mathrm{Dom}(V)=\mathrm{ran}(S+i)=H$$（同样由 定理 3.28）、$$\mathrm{ran}(V)=H$$。由 $$\mathrm{Dom}(T)\subseteq\mathrm{Dom}(S)$$ 得 $$(T+i)^{-1}$$ 与 $$(S+i)^{-1}$$ 在 $$\mathrm{ran}(T+i)$$ 上一致，故 $$V\supseteq U$$。反方向：设酉算子 $$V\supseteq U$$。先说明 $$I-V$$ 单射：$$\mathrm{ran}(I-V)\supseteq\mathrm{ran}(I-U)=\mathrm{Dom}(T)$$ 稠密，故 $$\ker(I-V^*)=\mathrm{ran}(I-V)^\perp=\lbrace0\rbrace$$；而 $$V$$ 酉时 $$Vx=x\iff V^*x=x$$，所以 $$\ker(I-V)=\ker(I-V^*)=\lbrace0\rbrace$$。于是可令 $$S=i(I+V)(I-V)^{-1}$$，定义域为 $$\mathrm{ran}(I-V)$$；由 3.6 节末尾的注（酉算子的逆 Cayley 变换对称、且由 $$V$$ 酉知其自伴），$$S$$ 自伴；又 $$I-U=2i(T+i)^{-1}$$ 与 $$I-S=2i(S+i)^{-1}$$ 在 $$\mathrm{Dom}(T)$$ 上一致，故 $$S\supseteq T$$。

**(二) 等距 $$U:D\to R$$ 有酉扩张 $$\iff$$ $$\dim D^\perp=\dim R^\perp$$。** 设 $$V$$ 是酉扩张。$$V$$ 保内积、为双射，故把正交补映成正交补：$$V(D^\perp)=V(D)^\perp$$（对 $$y\perp D$$ 与任意 $$Vx\in V(D)$$，$$\langle Vy,Vx\rangle=\langle y,x\rangle=0$$）。于是 $$V(D)^\perp=(VD)^\perp=R^\perp$$（$$V\supseteq U$$ 给 $$VD=UD=R$$），且 $$V$$ 在 $$D^\perp$$ 上等距，故 $$\dim D^\perp=\dim R^\perp$$。

反之设 $$\dim D^\perp=\dim R^\perp=:m$$。取 $$D^\perp$$ 的正交规范基 $$\lbrace e_\alpha\rbrace_{\alpha<m}$$ 与 $$R^\perp$$ 的正交规范基 $$\lbrace f_\alpha\rbrace_{\alpha<m}$$。定义

$$V\Bigl(\sum_{\alpha}c_\alpha e_\alpha+x\Bigr)=\sum_\alpha c_\alpha f_\alpha+Ux,\qquad x\in D,$$

线性（$$D^\perp$$ 与 $$D$$ 张成 $$D^\perp\oplus D$$，是 $$H$$ 的稠密子空间）。对 $$y=\sum c_\alpha e_\alpha+x$$，因 $$D^\perp\perp D$$、$$U$$ 等距、两组基正交规范，

$$\lVert Vy\rVert^2=\sum_\alpha\lvert c_\alpha\rvert^2+\lVert Ux\rVert^2=\sum_\alpha\lvert c_\alpha\rvert^2+\lVert x\rVert^2=\lVert y\rVert^2,$$

故 $$V$$ 是 $$D^\perp\oplus D$$ 上的等距。$$D^\perp\oplus D$$ 在 $$H$$ 中稠密，且 $$V$$ 的值域含 $$R^\perp\oplus R=(R^\perp)\oplus\mathrm{ran}(U)$$，它同样稠密（$$\mathrm{ran}(U)=R$$，$$H=R\oplus R^\perp$$ 处处成立）。等距从稠密子空间到稠密值域，唯一延拓为 $$H$$ 上的酉算子。

合起来：$$T$$ 有自伴扩张 $$\iff$$ $$U$$ 有酉扩张 $$\iff$$ $$\dim D^\perp=\dim R^\perp$$ $$\iff$$ $$n_+=n_-$$。$$\blacksquare$$

（结论的用法：**$$n_+=n_-$$ 时自伴扩张一般不是唯一的，而是"一族"，这一族恰好用来编码边界条件**——见下面的例子。）

**例（区间上的 $$-d^2/dt^2$$：边界条件从哪里冒出来）。** 取 $$H=L^2(0,1)$$，$$T_0=-\frac{d^2}{dt^2}$$，$$\mathrm{Dom}(T_0)=C_c^\infty(0,1)$$（在 $$(0,1)$$ 内部光滑、在端点附近为零的函数）。两次分部积分（边界项因支集在内部而消失）给出 $$\langle T_0\phi,\psi\rangle=\langle\phi,T_0\psi\rangle$$，故 $$T_0$$ 对称。

它的伴随 $$T_0^*$$ 定义在 $$H^2(0,1)=\lbrace f\in L^2:f''\in L^2\rbrace$$ 上（对 $$g$$ 而言，$$\phi\mapsto\langle T_0\phi,g\rangle=-\int\phi''\overline g$$ 要求 $$g''\in L^2$$，且 $$g'\in L^2$$ 由 $$g''\in L^2$$ 与 $$g\in L^2$$ 自动成立；**没有任何边界条件**）。于是解 $$T_0^*u=\pm i u$$，即 $$u''=\mp iu$$：$$u(t)=e^{\alpha t}$$，$$\alpha^2=\mp i$$，各有两个解，且都落在 $$L^2(0,1)$$。

**展开**：这是一个二阶常系数线性 ODE，其解空间的维数等于特征方程 $$\alpha^2=\mp i$$ 的根的个数（重根另计，这里两个平方根不同，故根数为 2）——$$-i$$ 有两个平方根 $$\pm e^{-i\pi/4}$$，$$+i$$ 有两个平方根 $$\pm e^{i\pi/4}$$，于是 $$\ker(T_0^*\mp i)$$ 各由两个线性无关的指数函数 $$e^{\alpha_1t},e^{\alpha_2t}$$ 张成，是**二维**空间（这正是第41章 命题 3.7 里一阶算子只给出一维解空间的对照：阶数每升一阶，特征方程多一个根，解空间就多一维）。区间 $$(0,1)$$ 是有限区间，指数函数在有限区间上必有界，故必平方可积——不像半无穷区间上会有 $$e^{\alpha t}$$ 因实部符号不对而不可积的情形（第41章 六节 研2 已经在一阶的情形里见过这种"账平不了"）。所以

$$n_+=n_-=2 .$$

由 定理 3.25，$$T_0$$ 的自伴扩张构成一个四实参数的族（对应 $$U(2)$$），每个扩张由**一组边界条件**指定：

- **Dirichlet**：$$u(0)=u(1)=0$$。解 $$u''=-\lambda u$$ 得 $$\lambda_n=n^2\pi^2$$（$$n\ge1$$），谱是离散的、下界为 $$\pi^2>0$$；
- **Neumann**：$$u'(0)=u'(1)=0$$。得 $$\lambda_n=n^2\pi^2$$（$$n\ge0$$），谱含 $$0$$；
- **周期**：$$u(1)=u(0)$$ 且 $$u'(1)=u'(0)$$。得 $$\lambda_n=4\pi^2n^2$$（$$n\ge0$$）。

三组数字完全不同，**而算子公式 $$-\frac{d^2}{dt^2}$$ 一个字没变**。所以：$$\mathrm{Dom}(T_0)=C_c^\infty(0,1)$$ 这个选择不是"技术细节"，它是一个**物理假设**——它对应"粒子被关在 $$(0,1)$$ 里，但还没说明在墙上发生了什么"。边界条件就是墙上发生的事。这就是"定义域是实质内容"这句话的完整含义。

### 3.6 Cayley 变换：把无界变成酉

现在到本章的技术核心。想法来自 MP56：三角函数的万能公式 $$x=\tan\frac\theta2$$ 把实直线铺到单位圆上；同一个映射作用在算子上，就把"谱在实轴"翻译成"谱在单位圆"。

**定义 3.26（Cayley 变换, Cayley transform）。** 设 $$T$$ 稠定对称。由 (3.2)，$$T+i$$ 单射，故有逆

$$(T+i)^{-1}:\ \mathrm{ran}(T+i)\ \longrightarrow\ \mathrm{Dom}(T),$$

且它是等距。定义

$$U=(T-i)(T+i)^{-1},\qquad \mathrm{Dom}(U)=\mathrm{ran}(T+i).$$

**定理 3.27（Cayley 变换的基本性质）。** 设 $$T$$ 稠定对称，$$U$$ 如上。

(i) $$U$$ 是等距：$$\lVert Uy\rVert=\lVert y\rVert$$ 对一切 $$y\in\mathrm{Dom}(U)$$。

(ii) $$U$$ 是单射，$$\mathrm{ran}(U)=\mathrm{ran}(T-i)$$。

(iii) $$I-U=2i\,(T+i)^{-1}$$，$$I+U=2T\,(T+i)^{-1}$$；特别地 $$I-U$$ 单射，$$\mathrm{ran}(I-U)=\mathrm{Dom}(T)$$。

(iv) 逆公式：在 $$\mathrm{Dom}(T)$$ 上

$$T=i\,(I+U)(I-U)^{-1}.$$

*证明*：任取 $$y\in\mathrm{Dom}(U)$$，写 $$y=(T+i)x$$（$$x\in\mathrm{Dom}(T)$$ 唯一）。则 $$Uy=(T-i)x$$，于是由 (3.2)

$$\lVert Uy\rVert^2=\lVert(T-i)x\rVert^2=\lVert Tx\rVert^2+\lVert x\rVert^2=\lVert(T+i)x\rVert^2=\lVert y\rVert^2 .$$

此即 (i)。(ii) 中单射由 (i) 立刻；值域是 $$(T-i)\bigl(\mathrm{Dom}(T)\bigr)=\mathrm{ran}(T-i)$$。

(iii)：对 $$y=(T+i)x$$，

$$(I-U)y=y-Uy=(T+i)x-(T-i)x=2ix=2i(T+i)^{-1}y,$$

$$(I+U)y=(T+i)x+(T-i)x=2Tx=2T(T+i)^{-1}y .$$

$$I-U$$ 单射因为 $$(T+i)^{-1}$$ 单射；其值域是 $$\lbrace 2ix:x\in\mathrm{Dom}(T)\rbrace=\mathrm{Dom}(T)$$。

(iv)：由 (iii)，对 $$z\in\mathrm{Dom}(T)$$ 有 $$(I-U)z=2i(T+i)^{-1}z$$。把 $$z=(T+i)x$$（$$x\in\mathrm{Dom}(T)$$）代入右边：$$2i(T+i)^{-1}(T+i)x=2ix$$。另一方面 $$(I-U)(T+i)x$$ 直接展开也等于 $$2ix$$，两相印证。于是反向读这个等式：在 $$\mathrm{Dom}(T)$$ 上，$$(I-U)^{-1}=\frac{1}{2i}(T+i)$$——它把 $$z\in\mathrm{Dom}(T)$$ 送回 $$H$$。代入得

$$i(I+U)(I-U)^{-1}=i\cdot\frac{1}{2i}(I+U)(T+i)=\frac12\bigl((T+i)+(T-i)\bigr)=T .$$

（第二步把 $$(I+U)y=2Tx$$ 用于 $$y=(T+i)x$$，即 $$(I+U)(T+i)=2T$$ 作为 $$\mathrm{Dom}(T)\to H$$ 的映射。）$$\blacksquare$$

**定理 3.28（自伴 $$\Leftrightarrow$$ 酉）。** 稠定对称算子 $$T$$ 自伴，当且仅当它的 Cayley 变换 $$U$$ 是酉算子。

*证明*：$$U$$ 是等距（定理 3.27(i)）。等距是酉算子 $$\iff$$ $$\mathrm{Dom}(U)=H$$ 且 $$\mathrm{ran}(U)=H$$。

若 $$T$$ 自伴，由 定理 3.17，$$\mathrm{ran}(T+i)=H$$ 且 $$\mathrm{ran}(T-i)=H$$，即 $$\mathrm{Dom}(U)=H$$、$$\mathrm{ran}(U)=H$$，故 $$U$$ 酉。

反之设 $$U$$ 酉，则 $$\mathrm{Dom}(U)=H=\mathrm{ran}(T+i)$$、$$\mathrm{ran}(U)=H=\mathrm{ran}(T-i)$$。由 定理 3.17 的"反方向"证明（那里只用到 $$\mathrm{ran}(T+i)=H$$ 与对称性），得 $$T=T^*$$。$$\blacksquare$$

**注（逆 Cayley 变换：从酉算子回到自伴算子）。** 反过来，设 $$V$$ 是酉算子且 $$I-V$$ 单射。在 $$\mathrm{Dom}(S)=\mathrm{ran}(I-V)$$ 上定义

$$S=i\,(I+V)(I-V)^{-1}.$$

则 $$S$$ 稠定、对称；并且 $$S$$ 自伴。*证明*：$$\mathrm{Dom}(S)=\mathrm{ran}(I-V)$$ 稠密，因为 $$\mathrm{ran}(I-V)^\perp=\ker(I-V^*)=\lbrace0\rbrace$$（$$V$$ 酉时 $$I-V^*$$ 与 $$I-V$$ 同为单射）。对称性：取 $$y=(I-V)a$$、$$w=(I-V)b$$，用 $$V^*V=I$$ 与 $$V^*=V^{-1}$$ 展开

$$\langle Sy,w\rangle=i\langle(I+V)a,(I-V)b\rangle=i\bigl(\langle a,b\rangle-\langle a,Vb\rangle+\langle Va,b\rangle-\langle a,b\rangle\bigr)=i\bigl(\langle Va,b\rangle-\langle a,Vb\rangle\bigr),$$

$$\langle y,Sw\rangle=-i\langle(I-V)a,(I+V)b\rangle=-i\bigl(\langle a,Vb\rangle-\langle Va,b\rangle\bigr),$$

两式相等。自伴性：直接用 定理 3.17，验证 $$\mathrm{ran}(S\pm i)=H$$——而 $$S\pm i$$ 在 $$y=(I-V)a$$ 上分别是 $$i(I+V)(I-V)^{-1}\mp i\cdot\ldots$$，逐项化简得 $$\mathrm{ran}(S+i)=\mathrm{ran}\bigl(2i\,V(I-V)^{-1}\bigr)=H$$（$$V$$ 与 $$(I-V)^{-1}$$ 都满射），同理 $$\mathrm{ran}(S-i)=\mathrm{ran}\bigl(2i\,(I-V)^{-1}\bigr)=H$$。$$\square$$

这条注与 定理 3.28 合起来给出：**"自伴（可以无界）的稠定算子"与"$$1$$ 不是特征值的酉算子"之间存在保结构的双射**。它正是 定理 3.25 里那个"反方向"所引用的结论。

**定理 3.29（谱映射）。** 设 $$T$$ 自伴，$$U$$ 为其 Cayley 变换。记 Möbius 映射

$$c(\lambda)=\frac{\lambda-i}{\lambda+i},$$

它把 $$\mathbb R\cup\lbrace\infty\rbrace$$ 双射到单位圆周 $$\mathbb T=\lbrace\lvert\mu\rvert=1\rbrace$$，且 $$c(\infty)=1$$。则

$$\lambda\in\sigma(T)\qquad\Longleftrightarrow\qquad c(\lambda)\in\sigma(U),$$

并且 $$1\in\sigma(U)$$（$$T$$ 无界时；$$1$$ 永远不是 $$U$$ 的特征值）。

*证明*：设 $$\lambda\in\mathbb R$$，记 $$\mu=c(\lambda)=\frac{\lambda-i}{\lambda+i}$$（由 $$\lvert\lambda-i\rvert=\lvert\lambda+i\rvert$$ 得 $$\lvert\mu\rvert=1$$）。由 定理 3.27(iv)，$$T=i(I+U)(I-U)^{-1}$$。先在 $$H$$ 上做一次纯代数运算：对任意 $$w\in H$$，

$$(\lambda I-T)(I-U)w=\lambda(I-U)w-i(I+U)w=(\lambda-i)w-(\lambda+i)Uw=(\lambda+i)\Bigl[\tfrac{\lambda-i}{\lambda+i}w-Uw\Bigr]=(\lambda+i)(\mu I-U)w .$$

这里只用到了 $$T(I-U)=i(I+U)$$（定理 3.27(iv) 等价形式）。因为 $$(I-U):H\to\mathrm{Dom}(T)$$ 是双射（定理 3.27(iii)：$$I-U=2i(T+i)^{-1}$$，而 $$T+i$$ 与 $$(T+i)^{-1}$$ 互逆，后者由 $$T$$ 自伴时 $$\mathrm{ran}(T+i)=H$$ 才有定义），上式可以右乘 $$(I-U)^{-1}$$ 写成

$$\lambda I-T=(\lambda+i)\,(\mu I-U)\,(I-U)^{-1}\qquad\text{作为}\ \mathrm{Dom}(T)\to H\ \text{的等式}. \tag{3.3}$$

于是 $$\lambda+i\ne0$$，而 $$(I-U)^{-1}$$ 与 $$(I-U)$$ 是一对互逆的双射，所以

$$\lambda I-T\ \text{是双射}\iff \mu I-U\ \text{是双射}\iff \mu\notin\sigma(U) .$$

再补上"逆有界"这一半：若 $$\mu\notin\sigma(U)$$，则由 (3.3)

$$(\lambda I-T)^{-1}=(I-U)\,(\mu I-U)^{-1}\,\frac{1}{\lambda+i},$$

右端是有界算子的乘积，故有界；反过来若 $$\lambda I-T$$ 是双射，则 $$T$$ 闭（自伴算子的伴随性，定理 3.14(i)）蕴含 $$(\lambda I-T)^{-1}$$ 闭，再用闭图像定理（第 36 章）得它有界。两半合起来给出

$$\lambda\in\sigma(T)\qquad\Longleftrightarrow\qquad \mu=c(\lambda)\in\sigma(U) .$$

最后，$$I-U=2i(T+i)^{-1}$$ 单射，故 $$1$$ 是 $$U$$ 的特征值是不可能的——$$1\notin\sigma_p(U)$$。若 $$T$$ 无界，则 $$\sigma(T)$$ 无界（这一点在 定理 3.30 之后看最清楚：那时 $$\lVert Tx\rVert^2=\int\lambda^2\,d\langle E(\lambda)x,x\rangle$$，$$\sigma(T)$$ 有界必然逼出 $$T$$ 有界；在本章的具体例子上——位置、动量、自由能量——谱无界可以直接看出），于是可取 $$\lambda_n\in\sigma(T)$$ 使 $$\lvert\lambda_n\rvert\to\infty$$，则 $$c(\lambda_n)\to1$$；$$\sigma(U)$$ 闭，故 $$1\in\sigma(U)$$。$$\blacksquare$$

这个定理是整章的高潮：**$$T$$ 的自伴性变成一个酉算子的存在性，$$T$$ 的谱变成单位圆上"去掉点 $$1$$"的像**。而且它给出了 Cayley 变换的物理身份。在动量表象里 $$P$$ 是乘 $$p$$，于是

$$U=(P-i)(P+i)^{-1}\ \longleftrightarrow\ \text{乘以}\ \frac{p-i}{p+i}=-e^{2i\arctan p}=e^{i(2\arctan p-\pi)} .$$

$$U$$ 的"特征值"$$\frac{p-i}{p+i}$$ 的模恒为 $$1$$，辐角 $$2\arctan p-\pi$$ 随动量 $$p$$ 从 $$-\pi$$ 变到 $$0$$——这正是散射理论里那个**随能量变化的相移**，$$U$$ 就是 S 矩阵的最简模型。MP56 用万能公式 $$x=\tan\frac\theta2$$ 引入 Cayley 变换，不是巧合：$$c(\lambda)=\frac{\lambda-i}{\lambda+i}$$ 的逆正是 $$\lambda=-\cot\frac\theta2$$，与 $$x=\tan\frac\theta2$$ 是同一个半角替换。**万能公式把直线卷成圆，Cayley 变换把无界算子卷成酉算子。**

最后把这个手段用到谱定理上。

**定理 3.30（无界自伴算子的谱定理）。** 设 $$T$$ 是 $$H$$ 上稠定自伴（可以无界）的算子。则存在唯一的投影算子值测度 $$E:\mathcal B(\mathbb R)\to B(H)$$（第 38 章）使

$$T=\int_{\mathbb R}\lambda\,dE(\lambda),$$

其含义是：$$\mathrm{Dom}(T)=\Bigl\lbrace x\in H:\ \int_{\mathbb R}\lambda^2\,d\langle E(\lambda)x,x\rangle<\infty\Bigr\rbrace$$，且对 $$x\in\mathrm{Dom}(T)$$、$$y\in H$$

$$\langle Tx,y\rangle=\int_{\mathbb R}\lambda\,d\langle E(\lambda)x,y\rangle .$$

此外：$$T$$ 有界 $$\iff$$ $$\sigma(T)$$ 有界（此时 $$\lVert T\rVert=\sup_{\lambda\in\sigma(T)}\lvert\lambda\rvert$$），$$\sigma(T)\subseteq\mathbb R$$ 非空，且特征函数演算 $$\chi_\Delta(T)=E(\Delta)$$ 对有界 Borel 函数 $$f$$ 给出 $$\lVert f(T)\rVert=\lVert f\rVert_{\infty,\sigma(T)}$$。

*证明思路*：把 第 38 章的谱定理用在**有界的** $$U$$ 上（$$U$$ 酉故有界），再沿 $$c^{-1}$$ 把 $$U$$ 的谱测度拉回实轴。

*证明*：由 定理 3.28，$$U$$ 是酉算子。第 38 章的正规算子谱定理给唯一的谱测度 $$E_U$$，支撑在 $$\sigma(U)\subseteq\mathbb T$$ 上，且

$$U=\int_{\mathbb T}\mu\,dE_U(\mu).$$

$$c:\mathbb R\cup\lbrace\infty\rbrace\to\mathbb T$$ 是双射，并把实轴上的 Borel 集 $$\Delta$$ 映为 $$\mathbb T$$ 中的 Borel 集（$$c$$ 在实轴上的限制连续单射，这是标准的 Borel 同构事实）。令

$$E(\Delta)=E_U\bigl(c(\Delta)\bigr).$$

投影值测度的三条公理由 $$E_U$$ 直接继承。于是 $$U=\int_{\mathbb R}c(\lambda)\,dE(\lambda)$$。

现在用逆公式 定理 3.27(iv)：$$T=i(I+U)(I-U)^{-1}$$。令

$$f(\mu)=i\,\frac{1+\mu}{1-\mu},$$

它在单位圆 $$\mathbb T$$ 上是连续函数（因为 $$1\notin\mathbb T$$ 故分母不为零），并且与 $$c$$ 互逆：代入 $$\mu=\frac{\lambda-i}{\lambda+i}$$ 得

$$\frac{1+\mu}{1-\mu}=\frac{(\lambda+i)+(\lambda-i)}{(\lambda+i)-(\lambda-i)}=\frac{2\lambda}{2i}=-i\lambda,\qquad\text{故}\ f(c(\lambda))=i\cdot(-i\lambda)=\lambda .$$

按第 38 章的连续函数演算，$$f(U)$$ 有意义，且

$$T_{\text{formal}}:=f(U)=\int_{\mathbb T}f(\mu)\,dE_U(\mu)=\int_{\mathbb R}\lambda\,dE(\lambda),$$

第二个等号是变量替换 $$\mu=c(\lambda)$$。形式上这就是要证的式子；剩下的唯一麻烦是 $$f$$ 无界（$$\mu\to1$$ 时 $$f(\mu)\to\infty$$），所以这一"积分"必须按无界函数演算解释为定义域受限的算子：

$$\mathrm{Dom}(T_{\text{formal}})=\Bigl\lbrace x:\int\lvert f(\mu)\rvert^2\,d\langle E_U(\mu)x,x\rangle<\infty\Bigr\rbrace=\Bigl\lbrace x:\int\lambda^2\,d\langle E(\lambda)x,x\rangle<\infty\Bigr\rbrace .$$

$$T$$ 与 $$T_{\text{formal}}$$ 都是 $$i(I+U)(I-U)^{-1}$$：前者由 定理 3.27(iv)，后者因为 $$f(U)$$ 在 $$(I-U)^{-1}$$ 有意义处与之相符（有界 Borel 函数上做了函数演算后再取极限）。两者定义域也相同，故 $$T=T_{\text{formal}}$$。唯一性来自 $$E_U$$ 的唯一性（第 38 章）。

谱与范数的断言是同一个积分的推论：$$\langle Tx,x\rangle=\int\lambda\,d\langle Ex,x\rangle$$ 与 $$\lVert Tx\rVert^2=\int\lambda^2\,d\langle Ex,x\rangle$$（后者由 $$T$$ 自伴时 $$\lVert Tx\rVert^2=\langle T^2x,x\rangle=\int\lambda^2\,d\langle Ex,x\rangle$$），于是 $$T$$ 有界 $$\iff$$ $$\int\lambda^2d\langle Ex,x\rangle\le C\lVert x\rVert^2$$ $$\iff$$ $$\mathrm{supp}\,E$$ 有界 $$\iff$$ $$\sigma(T)$$ 有界，此时 $$\lVert Tx\rVert^2\le(\sup\lvert\sigma(T)\rvert)^2\lVert x\rVert^2$$ 且取等号可达。$$\blacksquare$$

**注（乘法算子模型）。** 定理 3.30 也是 MP55"自伴算子酉等价于乘法算子"那句话的精确形态：把 $$H$$ 按 $$E_U$$ 分解，$$T$$ 就变成"乘以函数 $$\lambda\mapsto\lambda$$"，定义域就是"函数与 $$\lambda$$ 相乘后仍属空间"的那些向量。位置算子是乘 $$x$$、动量算子是乘 $$p$$（在动量表象）、自由能量是乘 $$p^2$$——第 3.4 节三个例子正是这一定理的三个具体化身。

### 3.7 回账：第 04 章的 $$\sigma(D)=i\mathbb Z$$ 现在有了地基

第 04 章在算 $$S^1$$ 上的算子 $$D=\frac{d}{d\theta}$$ 时，写下过一份"诚实清单"，第一条写着：$$D$$ 是无界算子，"无界算子的完整理论（图像、闭性、预解式）见第 42 章。本章只用到'预解式 $$\lambda\mapsto(\lambda I-D)^{-1}$$ 存在且范数被 $$\delta^{-1}$$ 控制'这一半，且是显式构造的，不依赖任何一般定理。"

现在把这笔账结清。取

$$H=L^2(S^1),\qquad \mathrm{Dom}(D)=H^1(S^1)=\Bigl\lbrace f=\sum_k c_ke^{ik\theta}:\ \sum_k(1+k^2)\lvert c_k\rvert^2<\infty\Bigr\rbrace .$$

**定理 3.31（$$D$$ 在 $$H^1(S^1)$$ 上反自伴）。** 上述 $$D$$ 稠定、闭，且 $$D^*=-D$$（$$\mathrm{Dom}(D^*)=\mathrm{Dom}(D)$$）。因而 $$iD$$ 自伴，$$\sigma(D)=i\mathbb Z$$。

*证明*：**稠密**：三角多项式 $$\subseteq H^1$$ 且在 $$L^2$$ 中稠密（第 30 章的完备正交系）。

**伴随的定义域**：设 $$g=\sum_k g_ke^{ik\theta}\in L^2$$。对 $$f\in H^1$$，

$$\langle Df,g\rangle=\sum_k(ik\,f_k)\overline{g_k}=\sum_k f_k\,\overline{(-ik\,g_k)} .$$

把 $$f$$ 换成 $$f$$ 的三角多项式，右边是关于 $$f$$ 的线性泛函。这个泛函在 $$(H^1,\lVert\cdot\rVert_{L^2})$$ 上连续 $$\iff$$ 系数列 $$(-ikg_k)_k$$ 属 $$\ell^2$$（因为 $$\lbrace f_k\rbrace$$ 可取遍 $$\ell^2$$ 的稠密子集——有限支撑列），即 $$\sum_kk^2\lvert g_k\rvert^2<\infty$$，也就是 $$g\in H^1$$。于是

$$\mathrm{Dom}(D^*)=\Bigl\lbrace g:\sum_kk^2\lvert g_k\rvert^2<\infty\Bigr\rbrace=H^1=\mathrm{Dom}(D),$$

且 $$D^*g$$ 的系数是 $$-ikg_k$$，即 $$D^*g=-g'=-Dg$$。所以 $$D^*=-D$$。

**闭**：$$D^*$$ 恒闭（定理 3.14(i)），故 $$D=D^{**}=-D^*$$ 也闭——更直接地，$$-D=D^*$$ 闭即 $$D$$ 闭。也可用图像范数验证：$$\lVert f\rVert_D^2=\lVert f\rVert^2+\lVert f'\rVert^2=\sum_k(1+k^2)\lvert f_k\rvert^2$$，故映射 $$f\mapsto\bigl((1+k^2)^{1/2}f_k\bigr)_k$$ 把 $$(\mathrm{Dom}(D),\lVert\cdot\rVert_D)$$ 等距同构到 $$\ell^2$$ 的闭子空间 $$\lbrace (c_k):\sum(1+k^2)\lvert f_k\rvert^2<\infty\rbrace$$ 上，于是它完备，由 命题 3.8 得 $$D$$ 闭。

**谱**：$$iD$$ 自伴（由 $$D^*=-D$$ 得 $$(iD)^*=-iD^*=-i(-D)=iD$$），故由 定理 3.19 其谱在实轴上，即 $$\sigma(D)\subseteq i\mathbb R$$。反过来 $$De^{ik\theta}=ik\,e^{ik\theta}$$ 给出 $$i\mathbb Z\subseteq\sigma(D)$$（$$ik$$ 是特征值）。**这正是第 04 章 定理 3.11 的两半**：那里"$$i\mathbb Z\subseteq\sigma(D)$$"用特征方程，"另一半"用逐频率除法显式构造 $$(\lambda I-D)^{-1}$$ 并估计范数 $$\le\delta^{-1}$$。两半合起来给出 $$\sigma(D)=i\mathbb Z$$。$$\blacksquare$$

**这笔债到底欠在哪、还了什么。** 三条交代，供从第 04 章回来的读者核对：

1. **第 04 章不需要本章的全套理论。** 它的证明只用两件事：$$D$$ 在 $$C_{2\pi}^\infty$$ 上的对称性（分部积分，边界项因周期性消失），以及 $$\lambda\notin i\mathbb Z$$ 时逐频率除法的显式逆与 $$\lVert(\lambda I-D)^{-1}\rVert\le\delta^{-1}$$。这两件事合起来已经直接给出"$$\lambda I-D$$ 双射且逆有界"，即谱的定义成立，**没有用到闭性、亏指数、谱定理中的任何一条**。所以那份"诚实清单"里的自我限制是准确的，第 04 章的结论没有漏洞。

2. **但有一个隐含前提是第 04 章没有证、本章才补上的：定义域 $$H^1$$ 是"对"的那一个。** 定理 3.31 说明 $$\mathrm{Dom}(D^*)=\mathrm{Dom}(D)=H^1$$，所以 $$H^1$$ 不是随手挑的子空间，而是那个形式算子的**闭包**——不加任何相位扭曲时它能取到的最大定义域。若改用更小的 $$C_{2\pi}^\infty$$，$$D$$ 仍对称、可闭（命题 3.12），但 $$D\ne D^*$$，而且**不是本质自伴**：它有无穷多个自伴扩张，每个对应一组圆周上的"准周期条件" $$f(2\pi)=e^{i\alpha}f(0)$$，谱从 $$i\mathbb Z$$ 变成 $$\lbrace i(k+\alpha/2\pi):k\in\mathbb Z\rbrace$$。换句话说，**第 04 章那个干净的 $$\sigma(D)=i\mathbb Z$$，是"用极大定义域、不加相位扭曲"这份选择的红利。**

3. **周期背景与区间背景的对照，是本章 3.5 节那个例子的镜像。** 在 $$S^1$$（无边）上取极大定义域，无需任何边界条件即得自伴；在 $$[0,1]$$（有边）上取 $$C_c^\infty$$，必须补边界条件才自伴，亏指数 $$(2,2)$$。

至此第 04 章留给本章的那句话可以划掉了：图像、闭性、可闭性在本章 3.2 节，$$D$$ 的自伴（反自伴）性在 定理 3.31，预解式的地位在 定理 3.29 与 定理 3.30。

## 四、几何与物理直觉 (Intuition)

**1. 图像是 $$H\oplus H$$ 里的一条"曲线"，闭性是它不漏点。** 有限维里算子是矩阵，图像是一张平面；无限维里 $$\Gamma(T)$$ 是 $$H\oplus H$$ 的线性子空间。说"$$T$$ 闭"就是"这条子空间不漏点"——它自己已经含了所有属于它的极限。推论 3.9 因此有了几何读法：**把 $$x$$ 换成 $$(x,Tx)$$，$$T$$ 就变成投影到第二坐标，而投影是有界的**。所以"无界"是范数选错造成的假象，不是算子本身的病。

**2. 亏指数 = 墙上有几种反射方式。** 对 3.5 节的 $$-\frac{d^2}{dt^2}$$，$$n_-=\dim\ker(T^*+i)$$ 数的是"入射波"自由度，$$n_+=\dim\ker(T^*-i)$$ 数的是"出射波"自由度。$$n_+=n_-$$ 是**概率守恒**：进去几种，出来几种。自伴扩张存在的条件因此读作"没有漏掉任何几率"，而不同的自伴扩张就是不同的"墙面反射规则"——Dirichlet（完全反射、基态能量 $$\pi^2>0$$）、Neumann（反射但允许常数，基态能量 $$0$$）、周期（墙上无缝，能级间距变成 $$4\pi^2$$ 的倍数）。同一条方程、不同的墙，得到不同的物理。

**3. Cayley 变换 = 把实轴卷成单位圆，把 S 矩阵从散射里抽象出来。** Möbius 映射 $$c(\lambda)=\frac{\lambda-i}{\lambda+i}$$ 是双曲几何里"上半平面圆盘模型"的主角，也是第 01、02 章 $$SO(2)$$ 那条线的可逆侧；作用在算子上，它把"谱在实轴"（自伴）变成"谱在单位圆"（酉）。前面算过：动量算子的 Cayley 变换是乘 $$\frac{p-i}{p+i}=e^{i(2\arctan p-\pi)}$$，一个纯相位；这**正是散射理论里的相移 $$\delta(p)$$**，$$U$$ 就是 S 矩阵。于是"非自伴的对称算子"对应"不保持几率的散射"——亏指数就是被吸走的几率。这条线在 3.6 节末尾具体的等式里已经全部可见。

**4. 三个世界的地图：几何 ↔ 物理 ↔ 代数。**
- 几何：实轴 $$\leftrightarrow$$ 单位圆（Cayley / 半角替换）。
- 物理：自伴算子（能量、动量）$$\leftrightarrow$$ 酉算子（时间演化、散射、相位）。
- 代数：无界问题 $$\leftrightarrow$$ 有界问题（换个范数、换成一族谱投影）。

谱定理（定理 3.30）就是这三条坐标线的交点：$$T=\int\lambda\,dE(\lambda)$$ 左边是无界物理量，右边是实轴上的积分，而构造它用的正是单位圆上的有界酉算子。

## 五、经典问题精讲

**经典问题 1（Hellinger–Toeplitz：为什么"处处定义"是禁区）。** 考点：定理 3.3 的证明与它的含义。位置：3.1 节。

*题*：设 $$T:H\to H$$ 处处定义、对称。证明 $$T$$ 有界；并由此说明：若 $$\hat p$$ 想要处处定义，它只能有界，而 $$\hat p$$ 无界——故 $$\hat p$$ 不能处处定义。这回答了入口题 (i) 与 (iii)。

*$$\hat p$$ 无界的显式构造*：取定 $$0\ne\varphi\in C_c^\infty(\mathbb R)$$，令

$$\psi_k(t)=\frac{e^{ikt}\varphi(t)}{\lVert\varphi\rVert_2}\quad(k=1,2,\dots),\qquad \lVert\psi_k\rVert_2=1 .$$

由 $$\hat p=-i\frac{d}{dt}$$，用乘积法则

$$\hat p\psi_k=\frac{e^{ikt}\bigl(k\varphi(t)-i\varphi'(t)\bigr)}{\lVert\varphi\rVert_2},\qquad \lVert\hat p\psi_k\rVert_2\ge k-\frac{\lVert\varphi'\rVert_2}{\lVert\varphi\rVert_2}\xrightarrow[k\to\infty]{}\infty .$$

（第二步用了三角不等式 $$\lVert k\varphi-i\varphi'\rVert\ge k\lVert\varphi\rVert-\lVert\varphi'\rVert$$。）故 $$\hat p$$ 在单位球上无界。

*解*：已在 定理 3.3 中完整证明，这里换成"反证的口吻"重述关键点。若 $$T$$ 无界，则存在 $$x_n$$ 使 $$\lVert Tx_n\rVert\ge n\lVert x_n\rVert$$。另一方面对称性把 $$\lVert Tx\rVert$$ 写成了 $$\sup_{\lVert y\rVert\le1}\lvert\langle x,Ty\rangle\rvert$$，而一致有界原理说：只要每个 $$x$$ 处的 $$y$$-上确界有限（它对固定 $$x$$ 恰恰等于 $$\lVert Tx\rVert$$），那么整体一致有限。两条陈述不可能同时成立，故 $$T$$ 有界。具体到 $$\hat p$$：题中的显式构造已证它无界，因此它不可能处处定义。"处处定义 + 对称 + 无界"这三条凑不齐全——这就是无界算子理论存在的理由。$$\blacksquare$$

**经典问题 2（动量的伴随定义域：对称不等于自伴）。** 考点：定义 3.13 与 定理 3.22，即入口题 (ii)。位置：3.3–3.4 节。

*题*：在 $$C_c^\infty(\mathbb R)$$ 上定义 $$P_0\psi=-i\psi'$$。证明 $$P_0$$ 对称；证明 $$\mathrm{Dom}(P_0^*)=H^1(\mathbb R)\supsetneq C_c^\infty(\mathbb R)$$，所以 $$P_0$$ 对称但**不**自伴；再证明 $$P_0$$ 本质自伴，其闭包就是 定理 3.22 的 $$P$$。

*解*：**对称**：分部积分，边界项因 $$\varphi,\psi$$ 紧支集为零（入口题 (ii) 已写）。

**$$\mathrm{Dom}(P_0^*)$$ 更大**：$$P_0$$ 是 $$P$$（定理 3.22）的限制，由 定理 3.14(ii)，$$P_0^*\supseteq P^*=P$$，故 $$\mathrm{Dom}(P_0^*)\supseteq\mathrm{Dom}(P)=H^1$$。另一方向：设 $$\varphi\in\mathrm{Dom}(P_0^*)$$、$$P_0^*\varphi=z$$。对一切 $$\psi\in C_c^\infty$$，$$\int(-i\psi')\overline\varphi=\int\psi\overline z$$。把 $$\psi$$ 取为在 $$(a,b)$$ 中等于 $$1$$、在外部迅速变零的测试函数并取极限，得 $$-i\cdot 0=\int_a^b\overline z$$ 型的关系，逐点推出 $$z=i\overline\varphi...$$ 更干脆的做法是重复 定理 3.22 的 Fourier 论证：条件"$$\psi\mapsto\langle P_0\psi,\varphi\rangle$$ 对 $$\psi\in C_c^\infty$$ 连续"等价于"$$p\hat\varphi\in L^2$$"，而 $$\lbrace\hat\psi:\psi\in C_c^\infty\rbrace$$ 在 $$L^2$$ 中稠密，故此条件即 $$\varphi\in H^1$$。于是 $$\mathrm{Dom}(P_0^*)=H^1\supsetneq C_c^\infty=\mathrm{Dom}(P_0)$$，$$P_0\ne P_0^*$$：**对称而不自伴**。

**本质自伴**：由 命题 3.12，$$P_0$$ 可闭且 $$\overline{P_0}\subseteq P_0^*=P$$。另一方向，$$P$$ 是闭的（定理 3.14(i)，$$P=P^*$$），且 $$\Gamma(P)\supseteq\Gamma(P_0)$$，取闭包得 $$\Gamma(P)\supseteq\Gamma(\overline{P_0})$$，即 $$P\supseteq\overline{P_0}$$。故 $$\overline{P_0}=P$$，自伴。所以 $$P_0$$ 本质自伴，且其唯一自伴扩张就是 $$P$$。$$\blacksquare$$

**关键 leap**：把"$$P_0$$ 的伴随"与"$$P$$ 的伴随"用 定理 3.14(ii) 联系起来——**扩大定义域使伴随变小**。对称算子的一切麻烦都源于这两个定义域不相等。

**经典问题 3（Cayley 变换的两个算例：矩阵与相移）。** 考点：定义 3.26，定理 3.27–3.29。位置：3.6 节，与 MP56 原文逐字对应。

*题*：**(a)** 对 $$B=\begin{pmatrix}0&x\\-x&0\end{pmatrix}$$（实反对称）算出 $$(I-B)(I+B)^{-1}$$，验证它是旋转矩阵，并指出 $$x=\tan\frac\theta2$$。**(b)** 对动量算子 $$P=-i\frac{d}{dx}$$ 在动量表象算出 Cayley 变换，验证它是酉算子，写出它的谱。

*解*：**(a)**$$I-B=\begin{pmatrix}1&-x\\x&1\end{pmatrix}$$，$$I+B=\begin{pmatrix}1&x\\-x&1\end{pmatrix}$$，$$\det(I+B)=1+x^2$$，故

$$(I+B)^{-1}=\frac{1}{1+x^2}\begin{pmatrix}1&-x\\x&1\end{pmatrix},\qquad (I-B)(I+B)^{-1}=\frac{1}{1+x^2}\begin{pmatrix}1-x^2&-2x\\2x&1-x^2\end{pmatrix}.$$

用 $$x=\tan\frac\theta2$$ 与倍角公式 $$\frac{1-x^2}{1+x^2}=\cos\theta$$、$$\frac{2x}{1+x^2}=\sin\theta$$，得 $$\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}$$：旋转 $$\theta$$。注意 $$B$$ 的 Cayley 变换用的是 $$I\pm B$$，而 $$B$$ 是**反自伴**的（实反对称在复数化下为反 Hermite）：与本章 $$T$$ 自伴时用 $$T\pm i$$ 是同一构造——因为 $$iT$$ 才反自伴，$$T\pm i=i(T\mp i i)=$$ 的形式转换使 $$i$$ 出现在该出现的位置。（MP56 原文里反对称矩阵对应"正交矩阵"，把实矩阵换成复矩阵后"正交"换成"酉"，这正是 $$B\mapsto T$$ 的一步。）

**(b)** 在动量表象 $$P$$ 是乘 $$p$$（定理 3.22 的 Fourier 结论），故

$$U=\frac{P-i}{P+i}\ \longleftrightarrow\ \mu(p)=\frac{p-i}{p+i}.$$

$$\lvert\mu(p)\rvert^2=\frac{p^2+1}{p^2+1}=1$$，故 $$U$$ 是"乘一个模为 1 的函数"的乘法算子。乘法算子 $$M_\mu$$ 是酉算子 $$\iff$$ $$\lvert\mu\rvert=1$$ 几乎处处（第 36 章乘法算子一段）。所以 $$U$$ 酉，与 定理 3.28 一致（$$P$$ 自伴）。谱：$$\mu(p)$$ 的值域是单位圆去掉点 $$1$$（$$p\to\pm\infty$$ 时 $$\mu\to1$$，取不到），闭包是整个单位圆，故 $$\sigma(U)=\mathbb T$$，且 $$1$$ 不是特征值（$$\mu(p)=1$$ 无解）。这恰好是 定理 3.29 说的：$$P$$ 无界 ⟹ $$1\in\sigma(U)$$ 但 $$1$$ 非特征值；而 $$\sigma(P)=\mathbb R$$ 在 $$c$$ 下的像就是 $$\mathbb T\setminus\lbrace1\rbrace$$ 的闭包。写成相位：$$\mu(p)=-e^{2i\arctan p}=e^{i(2\arctan p-\pi)}$$，随 $$p$$ 从 $$-\infty$$ 增到 $$+\infty$$，辐角从 $$-\pi$$ 增到 $$0$$——**这就是散射相移 $$\delta(p)=2\arctan p-\pi$$ 加一个 $$\pi$$ 的平移**。$$\blacksquare$$

**经典问题 4（位置算子的谱与"没有特征向量"）。** 考点：定理 3.21、定理 3.30，入口题 (iv) 的孪生问题。位置：3.3–3.4 节。

*题*：证明 $$\sigma(X)=\mathbb R$$，且 $$X$$ 没有特征向量。

*解*：**没有特征向量**：设 $$X\psi=\lambda\psi$$，即 $$(x-\lambda)\psi(x)=0$$ 几乎处处。于是 $$\psi=0$$ 于测度非零集 $$\lbrace x\ne\lambda\rbrace$$ 上，故 $$\psi=0$$ 几乎处处（单点集零测）。所以任何 $$\lambda$$ 都不是特征值。

**谱是 $$\mathbb R$$**：设 $$\lambda\in\mathbb R$$。用 定理 3.30 的乘法算子模型最省事：$$X$$ 就是乘恒等函数 $$\mathrm{id}(x)=x$$ 的乘法算子，而对乘法算子 $$M_h$$ 有 $$\sigma(M_h)=\overline{h(\mathbb R)}$$（第 36 章乘法算子一段；推导要点：$$\lambda\notin\overline{h(\mathbb R)}$$ 时 $$1/(h-\lambda)$$ 有界，$$M_{1/(h-\lambda)}$$ 就是 $$(\lambda I-M_h)^{-1}$$；$$\lambda\in\overline{h(\mathbb R)}$$ 时取 $$h$$ 在 $$\lambda$$ 附近水平集上的归一化指示函数即可证 $$\lambda I-M_h$$ 不是下有界的）。取 $$h=\mathrm{id}$$ 得 $$\sigma(X)=\overline{\mathbb R}=\mathbb R$$。也可以直接构造：取 $$\psi_n=\sqrt{n}\,\chi_{[\lambda,\lambda+1/n]}$$（归一化指示函数），则

$$\lVert(\lambda I-X)\psi_n\rVert^2=n\!\int_{\lambda}^{\lambda+1/n}(x-\lambda)^2dx=\frac{1}{3n^2}\to0,$$

故 $$\lambda I-X$$ 不是下有界的，因而不可能有有界逆（有界逆必给 $$\lVert(\lambda I-X)\psi\rVert\ge C^{-1}\lVert\psi\rVert$$）。$$\lambda\notin\mathbb R$$ 时由 定理 3.19 的实谱结论排除。于是 $$\sigma(X)=\mathbb R$$，且因无特征值，这是**纯连续谱**。$$\blacksquare$$

**关键 leap**：谱不等于特征值集合。第 36 章已经点过这件事（乘法算子 $$M_\varphi$$、单侧移位），本章给的是"为什么"：定义域与闭性决定了一个"特征方程的解"是否真的落在 Hilbert 空间里。$$e^{ikx}\notin L^2$$、$$\delta$$ 函数不是向量——**谱是比特征值更大的概念**，这正是第 38 章要引进 PVM 的原因。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 设 $$T$$ 稠定对称，$$\lambda=a+ib\in\mathbb C$$。验证恒等式

$$\lVert(T-\lambda)x\rVert^2=\lVert(T-a)x\rVert^2+b^2\lVert x\rVert^2,\qquad x\in\mathrm{Dom}(T),$$

并由此推出：$$T$$ 的（若有的）特征值都是实数；$$T\pm i$$ 单射且 $$(T\pm i)^{-1}$$ 是等距。

**基2.** 取 $$X$$（命题 3.21）。证明：$$\mathrm{Dom}(X)$$ 在 $$L^2(\mathbb R)$$ 中稠密；$$X$$ 对称；并给出一个具体的 $$\psi\in L^2(\mathbb R)\setminus\mathrm{Dom}(X)$$。

**基3.** 证明：$$\lVert x\rVert_T=\sqrt{\lVert x\rVert^2+\lVert Tx\rVert^2}$$ 是 $$\mathrm{Dom}(T)$$ 上的范数；且当 $$T$$ 闭时，$$T:(\mathrm{Dom}(T),\lVert\cdot\rVert_T)\to H$$ 是范数不超过 $$1$$ 的有界线性算子。

**基4.** 设 $$T$$ 稠定对称，$$U=(T-i)(T+i)^{-1}$$。验证

$$I-U=2i\,(T+i)^{-1},\qquad I+U=2T\,(T+i)^{-1},$$

并算出 $$U$$ 与 $$U^*$$ 的关系（在 $$T$$ 自伴、$$U$$ 酉的情形下验证 $$U^*=U^{-1}$$）。

### 竞赛（本课目标难度）

**竞1.** 用一致有界原理证明 Hellinger–Toeplitz 定理（定理 3.3），并说明证明中"对称性"被用在了哪一步。若不假设对称，只假设 $$T$$ 处处定义且 $$\lVert Tx\rVert$$ 在每一点处有限，结论还成立吗？（提示：思考 $$T$$ 是一个处处有定义的无界线性算子是否可能。）

**竞2.** 设 $$T$$ 稠定对称。证明：$$T$$ 自伴 $$\iff$$ $$\mathrm{ran}(T+i)=H$$。再证明：若 $$T\subseteq S$$ 且 $$S$$ 对称，则 $$S=T$$（即自伴算子是极大对称的）。

**竞3.** 取 $$H=L^2(0,1)$$，在 $$C_c^\infty(0,1)$$ 上定义 $$P_0=-i\frac{d}{dx}$$。算出 $$P_0$$ 的亏指数，并写出 $$P_0$$ 的所有自伴扩张。它们各自与什么边界条件对应？取 $$f(t)=t^2(1-t)^2$$ 验证它属于最大算子的定义域 $$\mathrm{Dom}(P_0^*)$$ 但不属于 $$\mathrm{Dom}(P_0)$$。

**竞4.** 设 $$T$$ 自伴、$$U$$ 为其 Cayley 变换，$$\mu=\frac{\lambda-i}{\lambda+i}$$（$$\lambda\in\mathbb R$$）。验证恒等式

$$\lambda I-T=(\lambda+i)\,(I-U)^{-1}\,(I-\mu U),$$

从而证明 $$\lambda\in\sigma(T)\iff\mu\in\sigma(U)$$。再对 $$T=X$$（位置算子）具体算出 $$U$$ 是什么乘法算子，并确定 $$\sigma(U)$$。

### 研究（通向下一章）

**研1.** 取 $$H=L^2(0,1)$$，$$T_0=-\frac{d^2}{dt^2}$$，$$\mathrm{Dom}(T_0)=C_c^\infty(0,1)$$。**(a)** 证明 $$T_0^*$$ 是 $$H^2(0,1)$$ 上的 $$-\frac{d^2}{dt^2}$$（无边界条件）。**(b)** 算出 $$n_+=n_-=2$$。**(c)** 证明 Dirichlet 扩张（$$u(0)=u(1)=0$$）是自伴的，并算出它的谱是 $$\lbrace n^2\pi^2:n\ge1\rbrace$$；对 Neumann 扩张（$$u'(0)=u'(1)=0$$）做同样的事，谱是 $$\lbrace n^2\pi^2:n\ge0\rbrace$$。**(d)** 用 定理 3.29 解释：为什么 Dirichlet 谱的最低点是 $$\pi^2$$ 而 Neumann 的可以到 $$0$$？

**研2.** 设 $$A,B$$ 是 $$H$$ 上的有界算子且 $$AB-BA=i\hbar I$$（$$\hbar>0$$）。**(a)** 证明这不可能（即正则对易关系迫使算子无界）。**(b)** 用 $$P=-i\frac{d}{dx}$$ 与 $$X$$（乘 $$x$$）在 $$H^1$$ 与 $$\mathrm{Dom}(X)$$ 上验证 $$[X,P]=iI$$（形式上）。**(c)** 从而论证：第 44 章的 Heisenberg 对易关系只能活在无界算子的语言里，而"时间演化 $$e^{itH}$$ 是酉算子"这种说法之所以好用，正是因为 Cayley 变换把无界 $$H$$ 换成了有界酉算子。

### 解答 (Solutions)

**解 基1.** 展开内积。记 $$A=T-a$$（$$A$$ 在 $$\mathrm{Dom}(T)$$ 上对称，因为 $$T$$ 对称、$$a$$ 是实数时 $$\langle ax,y\rangle=a\langle x,y\rangle$$ 且 $$a=\overline a$$）。则

$$\lVert(T-\lambda)x\rVert^2=\langle(A-ib)x,(A-ib)x\rangle=\lVert Ax\rVert^2+\langle -ibx,Ax\rangle+\langle Ax,-ibx\rangle+b^2\lVert x\rVert^2 .$$

两个交叉项：$$\langle -ibx,Ax\rangle=-ib\langle x,Ax\rangle$$（内积对第一变元线性），$$\langle Ax,-ibx\rangle=\overline{-ib}\langle Ax,x\rangle=ib\langle Ax,x\rangle$$。由 $$T$$ 对称，$$\langle Ax,x\rangle=\langle x,Ax\rangle\in\mathbb R$$（对称性的实数二次型刻画），故两项分别是 $$-ibq$$ 与 $$ibq$$，和为 $$0$$。于是

$$\lVert(T-\lambda)x\rVert^2=\lVert(T-a)x\rVert^2+b^2\lVert x\rVert^2 .$$

**特征值实**：若 $$Tx=\lambda x$$、$$\lVert x\rVert=1$$，则 $$\lVert(T-a)x\rVert=0$$，故 $$\langle Tx,x\rangle=a\lVert x\rVert^2$$ 为实数——但 $$\lambda=\langle Tx,x\rangle/a$$ 在 $$a\ne0$$ 时；更直接地，由上式 $$0=\lVert(T-\lambda)x\rVert^2\ge b^2$$，故 $$b=0$$。

**单射与等距**：上式取 $$\lambda=\pm i$$（$$a=0,b=\pm1$$）得 $$\lVert(T\pm i)x\rVert^2=\lVert Tx\rVert^2+\lVert x\rVert^2\ge\lVert x\rVert^2$$。若 $$(T\pm i)x=0$$ 则 $$x=0$$：单射。对 $$y=(T+i)x$$，$$\lVert(T+i)^{-1}y\rVert=\lVert x\rVert$$ 而 $$\lVert y\rVert=\lVert(T+i)x\rVert$$，故 $$\lVert(T+i)^{-1}y\rVert=\lVert y\rVert$$；等价地 $$\lVert(T+i)^{-1}\rVert\le1$$。对 $$T-i$$ 同理。$$\blacksquare$$

**解 基2.** **稠密**：$$C_c^\infty(\mathbb R)\subseteq\mathrm{Dom}(X)$$，因为紧支集有界函数 $$\psi$$ 满足 $$\int\lvert x\psi\rvert^2\le M^2\int\lvert\psi\rvert^2<\infty$$；而 $$C_c^\infty$$ 在 $$L^2$$ 中稠密（可用 $$L^1\cap L^2$$ 函数截断、再用光滑逼近，第 30 章）。故 $$X$$ 稠定。

**对称**：$$\langle X\psi,\varphi\rangle=\int x\psi\overline\varphi=\int\psi\overline{x\varphi}=\langle\psi,X\varphi\rangle$$，因为 $$x\in\mathbb R$$。

**具体反例**：$$L^2$$ 只要求 $$\lvert\psi\rvert^2$$ 在无穷远按快于 $$x^{-1}$$ 的速度衰，而 $$\mathrm{Dom}(X)$$ 要求 $$\lvert x\psi\rvert^2$$ 这样衰，即 $$\lvert\psi\rvert^2$$ 按快于 $$x^{-3}$$ 的速度衰——差两个整幂。取

$$\psi(x)=\begin{cases}\dfrac{1}{1+\lvert x\rvert},&\lvert x\rvert\ge1,\\[2mm] \dfrac{1}{2}\bigl(2-\lvert x\rvert\bigr),&\lvert x\rvert<1 .\end{cases}$$

（$$\lvert x\rvert<1$$ 上的分支是为了让 $$\psi$$ 连续、有界。）在 $$[1,\infty)$$ 上 $$\lvert\psi\rvert^2=\frac{1}{(1+x)^2}$$，$$\int_1^\infty\frac{dx}{(1+x)^2}<\infty$$；在 $$[-1,1]$$ 上有界。故

$$\int_{\mathbb R}\lvert\psi\rvert^2<\infty,\quad \text{即}\ \psi\in L^2(\mathbb R);$$

但在 $$\lvert x\rvert\ge1$$ 上 $$\lvert x\psi(x)\rvert^2=\frac{x^2}{(1+\lvert x\rvert)^2}\to1$$，于是

$$\int_{\mathbb R}\lvert x\psi(x)\rvert^2\,dx\ge\int_{1}^{\infty}\frac{x^2}{(1+x)^2}\,dx=\infty,$$

故 $$X\psi\notin L^2$$，即 $$\psi\in L^2(\mathbb R)\setminus\mathrm{Dom}(X)$$。$$\blacksquare$$

（注：$$L^2$$ 只要求 $$\lvert\psi\rvert$$ 衰减快于 $$x^{-1/2}$$，$$\mathrm{Dom}(X)$$ 要求快于 $$x^{-3/2}$$。）

**解 基3.** **范数**：$$\lVert x\rVert_T\ge0$$，且 $$\lVert\alpha x\rVert_T^2=\lVert\alpha x\rVert^2+\lVert T(\alpha x)\rVert^2=\lvert\alpha\rvert^2\lVert x\rVert_T^2$$（$$T$$ 线性），故齐次性成立；$$\lVert x\rVert_T=0$$ 蕴含 $$\lVert x\rVert=0$$，故 $$x=0$$。三角不等式：映射 $$\Phi:x\mapsto(x,Tx)$$ 线性，$$\lVert x\rVert_T=\lVert\Phi(x)\rVert_{H\oplus H}$$，而 $$H\oplus H$$ 上的范数满足三角不等式，故

$$\lVert x+y\rVert_T=\lVert\Phi x+\Phi y\rVert_{H\oplus H}\le\lVert\Phi x\rVert+\lVert\Phi y\rVert=\lVert x\rVert_T+\lVert y\rVert_T .$$

正定性：$$\lVert x\rVert_T=0\Rightarrow\lVert x\rVert=0\Rightarrow x=0$$。

**有界性**：$$\lVert Tx\rVert^2\le\lVert x\rVert^2+\lVert Tx\rVert^2=\lVert x\rVert_T^2$$，故 $$\lVert T\rVert_{(\mathrm{Dom}T,\lVert\cdot\rVert_T)\to H}\le1$$。当 $$T$$ 闭时，由 命题 3.8，$$(\mathrm{Dom}(T),\lVert\cdot\rVert_T)$$ 是 Hilbert 空间（完备赋范空间），$$T$$ 是其中的有界线性算子。$$\blacksquare$$

**解 基4.** 设 $$y=(T+i)x$$，$$x\in\mathrm{Dom}(T)$$。则 $$(T+i)^{-1}y=x$$，且 $$Uy=(T-i)x$$。于是

$$(I-U)y=y-Uy=(T+i)x-(T-i)x=2ix=2i(T+i)^{-1}y,$$

$$(I+U)y=y+Uy=(T+i)x+(T-i)x=2Tx=2T(T+i)^{-1}y .$$

**$$U$$ 与 $$U^*$$**：在 $$\mathrm{Dom}(U)=\mathrm{ran}(T+i)$$ 上、$$\mathrm{ran}(U)=\mathrm{ran}(T-i)$$ 上，对 $$y=(T+i)x$$、$$w=(T+i)x'$$，

$$\langle Uy,w\rangle=\langle(T-i)x,(T+i)x'\rangle=\langle Tx,Tx'\rangle+\langle -ix,Tx'\rangle+\langle Tx,ix'\rangle+\langle -ix,ix'\rangle .$$

前两项交叉：$$\langle -ix,Tx'\rangle=-i\langle x,Tx'\rangle$$，$$\langle Tx,ix'\rangle=i\langle Tx,x'\rangle=i\langle x,Tx'\rangle$$，和为 $$0$$。故

$$\langle Uy,w\rangle=\lVert Tx\rVert\lVert Tx'\rVert\text{ 型}+\langle x,x'\rangle=\langle Tx,Tx'\rangle+\langle x,x'\rangle .$$

对称地 $$\langle y,Uw\rangle=\langle (T+i)x,(T-i)x'\rangle=\langle Tx,Tx'\rangle+\langle x,x'\rangle$$。故 $$\langle Uy,w\rangle=\langle y,Uw\rangle$$，即 $$U^*\supseteq U$$。若 $$T$$ 自伴则 $$U$$ 酉（定理 3.28），$$U^*=U^{-1}$$：由等距性 $$U^*U=I$$、$$UU^*=I$$。$$\blacksquare$$

**解 竞1.** **关键 leap**：注意到"对称性"的唯一用处是把 $$\lVert Tx\rVert$$ 改写成 $$\sup_{\lVert y\rVert\le1}\lvert\langle x,Ty\rangle\rvert$$，从而把"对 $$x$$ 一致有界"的问题变成"对一族连续泛函逐点有界"的问题，正好落进一致有界原理的形式。

**证明**：对 $$y\in H$$ 令 $$\varphi_y(x)=\langle x,Ty\rangle$$。$$\varphi_y$$ 线性、$$\lvert\varphi_y(x)\rvert\le\lVert x\rVert\lVert Ty\rVert$$，故 $$\varphi_y\in H^*$$ 且 $$\lVert\varphi_y\rVert=\lVert Ty\rVert$$（Riesz：$$x\mapsto\langle x,Ty\rangle$$ 的范数恰是 $$\lVert Ty\rVert$$，因为取 $$x=Ty/\lVert Ty\rVert$$ 时达到等号）。

固定 $$x$$。由对称性 $$\langle x,Ty\rangle=\langle Tx,y\rangle$$，

$$\sup_{\lVert y\rVert\le1}\lvert\varphi_y(x)\rvert=\sup_{\lVert y\rVert\le1}\lvert\langle Tx,y\rangle\rvert=\lVert Tx\rVert<\infty,$$

最后一步是内积范数的对偶刻画。故泛函族 $$\lbrace\varphi_y\rbrace_{\lVert y\rVert\le1}$$ 逐点有界。$$H$$ 是 Banach 空间（Hilbert 空间必完备），由一致有界原理（第 36 章）

$$\sup_{\lVert y\rVert\le1}\lVert\varphi_y\rVert=:C<\infty .$$

代入 $$\lVert\varphi_y\rVert=\lVert Ty\rVert$$ 得 $$\sup_{\lVert y\rVert\le1}\lVert Ty\rVert=C$$，即 $$T$$ 有界。

**对称性用在哪**：只在 $$\sup_{\lVert y\rVert\le1}\lvert\langle x,Ty\rangle\rvert=\lVert Tx\rVert$$ 这一步。若不假设对称，逐点有界性就只给出 $$\sup_{\lVert y\rVert\le1}\lvert\langle x,Ty\rangle\rvert<\infty$$ 对每个 $$x$$——这不足以结论（它是 $$T$$ 的另一种表述，绕回来还是同一个问题）。

**去掉了对称性呢？** 结论不再成立：处处定义的无界线性算子**存在**，但必须用选择公理（Hamel 基）造，而且不能是闭的。具体地，在无穷维 Banach 空间上取一个代数基，把某个基向量映成任意大的倍数并线性延拓，就得到处处定义的无界线性算子。它不连续、不闭、不能用公式写出来——Hellinger–Toeplitz 说的正是：**"可由公式给出、并且对称"的处处定义算子是不会有这类怪脾气的。**$$\blacksquare$$

**解 竞2.** 第一段已在 定理 3.17 中完整给出，此处按题面重述要点并补第二段。

**$$T$$ 自伴 $$\Rightarrow$$ $$\mathrm{ran}(T+i)=H$$**：由 $$T$$ 自伴得 $$T$$ 闭（定理 3.14(i)）。闭 + 不等式 $$\lVert(T+i)x\rVert\ge\lVert x\rVert$$ 给出 $$\mathrm{ran}(T+i)$$ 闭（若 $$(T+i)x_n\to w$$ 则 $$x_n\to x$$，$$Tx_n\to w-ix$$，闭性给 $$w=(T+i)x$$）。正交补 $$\mathrm{ran}(T+i)^\perp=\ker(T^*-i)=\ker(T-i)=\lbrace0\rbrace$$（最后一式用不等式）。闭 + 正交补零 ⇒ 满。

**$$\mathrm{ran}(T+i)=H\Rightarrow T$$ 自伴**：取 $$y\in\mathrm{Dom}(T^*)$$，由满射性有 $$x\in\mathrm{Dom}(T)$$ 使 $$(T+i)x=(T^*+i)y$$。对任意 $$z\in\mathrm{Dom}(T)$$，用对称性展开 $$\langle(T+i)x,z\rangle=\langle x,(T+i)z\rangle$$，用伴随的定义展开 $$\langle(T^*+i)y,z\rangle=\langle y,(T+i)z\rangle$$；两式相等给出 $$x-y\perp\mathrm{ran}(T+i)=H$$，故 $$y=x\in\mathrm{Dom}(T)$$。于是 $$T^*\subseteq T$$，又 $$T\subseteq T^*$$，得 $$T=T^*$$。

**极大性**：设 $$T\subseteq S$$、$$S$$ 对称。由 定理 3.14(ii)，$$S^*\subseteq T^*=T$$；又 $$S\subseteq S^*$$。故 $$S\subseteq T\subseteq S$$，即 $$S=T$$。$$\blacksquare$$

**解 竞3.** **最大算子**：$$g\in\mathrm{Dom}(P_0^*)$$ 当且仅当 $$g\in H^1(0,1)=\lbrace g\in L^2:g'\in L^2\rbrace$$（弱导数意义；因为 $$\lbrace\psi'\rbrace_{\psi\in C_c^\infty}$$ 张成 $$L^2$$ 的稠密子集，而 $$g\in L^2$$ 且 $$g'\in L^2$$ 时 $$g$$ 绝对连续，故 $$g$$ 在 [0,1] 上有连续代表）。此时 $$P_0^*g=-ig'$$，**没有边界条件**。所以

$$\mathrm{Dom}(P_0^*)=H^1(0,1),\qquad \mathrm{Dom}(P_0)=C_c^\infty(0,1)\subsetneq H^1(0,1) .$$

（对比区间与圆周：这里区间有端点，但最大算子仍不带边界条件——边界条件正体现在"$$L^2$$ 中 $$g'$$ 可积"这一点被 $$H^1$$ 的迹定理所允许。真正要界住端点会在下一步。）

**亏指数**：解 $$P_0^*g=\pm ig$$，即 $$-ig'=\pm ig$$，$$g'=\mp g$$，$$g(t)=Ce^{\mp t}$$。两者都光滑、有界，属 $$H^1(0,1)$$，各构成一维解空间。故

$$n_+=n_-=1 .$$

**自伴扩张**：由 定理 3.25，自伴扩张构成一参数族。一般形式是：取 $$\theta\in[0,2\pi)$$，

$$\mathrm{Dom}(P_\theta)=\lbrace g\in H^1(0,1):\ g(1)=e^{i\theta}g(0)\rbrace,\qquad P_\theta g=-ig' .$$

逐条验证：$$P_\theta$$ 对称——对 $$g,h\in\mathrm{Dom}(P_\theta)$$，

$$\langle P_\theta g,h\rangle-\langle g,P_\theta h\rangle=-i\bigl[g\overline h\bigr]_0^1=-i\bigl(g(1)\overline{h(1)}-g(0)\overline{h(0)}\bigr)=-i\bigl(e^{i\theta}g(0)\overline{e^{i\theta}h(0)}-g(0)\overline{h(0)}\bigr)=0 .$$

自伴性由 $$n_+=n_-$$（定理 3.25）或直接用 $$\mathrm{ran}(P_\theta\pm i)=H$$（定理 3.17）：方程 $$-ig'\pm ig=f$$ 是一阶线性 ODE，通解含一常数，边界条件 $$g(1)=e^{i\theta}g(0)$$ 恰定此常数。故每个 $$P_\theta$$ 自伴。$$\theta=0$$ 即周期条件；$$\theta=\pi$$ 即反周期条件。**同一族里没有"Dirichlet"型条件**——一阶算子只能有一个端点条件（或两个端点的一个线性关系），这与 3.5 节二阶算子会出现 $$u(0)=u(1)=0$$ 不同，原因是一阶方程只需一个边界条件。

**具体向量**：$$f(t)=t^2(1-t)^2$$。$$f\in H^1(0,1)$$（多项式光滑），故 $$f\in\mathrm{Dom}(P_0^*)$$。而 $$f(0)=f(1)=0$$，$$f'\ne0$$ 在端点附近，$$P_0f=-if'$$ 在 (0,1) 上非零——所以 $$f$$ 不是 $$C_c^\infty(0,1)$$ 的元素（$$C_c^\infty$$ 要求在整个 $$[0,1]$$ 的某个邻域外为零，而 $$f$$ 的支集恰是 $$[0,1]$$）。更准确地说，$$f$$ 与任何 $$C_c^\infty(0,1)$$ 中的函数都不相同：$$C_c^\infty(0,1)$$ 中函数在端点附近恒为零，而 $$f$$ 不是。故 $$f\in\mathrm{Dom}(P_0^*)\setminus\mathrm{Dom}(P_0)$$，$$P_0$$ 不自伴得到实证。$$\blacksquare$$

**解 竞4.** **关键 leap**：不要试图把 $$(I-U)^{-1}$$ 当成 $$H$$ 上的算子——它的定义域是 $$\mathrm{Dom}(T)$$（定理 3.27(iii)：$$(I-U)^{-1}=\frac{1}{2i}(T+i)$$）。正确做法是**先让 $$(\lambda I-T)$$ 右乘 $$(I-U)$$**，把定义域的麻烦消掉，得到 $$H$$ 上的等式之后再右乘 $$(I-U)^{-1}$$。

**恒等式**：设 $$\lambda\in\mathbb R$$，$$\mu=\frac{\lambda-i}{\lambda+i}$$。由 定理 3.27(iv)，在 $$\mathrm{Dom}(T)=\mathrm{ran}(I-U)$$ 上有 $$T=i(I+U)(I-U)^{-1}$$，等价地

$$T\,(I-U)=i\,(I+U)\qquad\text{作为}\ H\to H\ \text{的等式}.$$

（$$I-U$$ 把 $$H$$ 映满 $$\mathrm{Dom}(T)$$，再经 $$T$$ 回到 $$H$$。）于是对任意 $$w\in H$$，

$$(\lambda I-T)(I-U)w=\lambda w-\lambda Uw-iw-iUw=(\lambda-i)w-(\lambda+i)Uw .$$

把 $$(\lambda+i)$$ 提出：

$$(\lambda-i)w-(\lambda+i)Uw=(\lambda+i)\Bigl[\frac{\lambda-i}{\lambda+i}w-Uw\Bigr]=(\lambda+i)(\mu I-U)w .$$

所以作为 $$H\to H$$ 的算子恒等式，

$$(\lambda I-T)(I-U)=(\lambda+i)(\mu I-U). \tag{3.4}$$

**可逆性的传递**：$$(I-U)$$ 与 $$(I-U)^{-1}$$ 是 $$H$$ 与 $$\mathrm{Dom}(T)$$ 之间互逆的双射（定理 3.27(iii)），$$\lambda+i\ne0$$ 是纯量。在 (3.4) 两边右乘 $$(I-U)^{-1}$$，得

$$\lambda I-T=(\lambda+i)(\mu I-U)(I-U)^{-1}\qquad\text{作为}\ \mathrm{Dom}(T)\to H\ \text{的等式}. \tag{3.5}$$

纯量因子与 $$(I-U)^{-1}$$ 都是双射，故

$$\lambda I-T\ \text{是双射}\iff \mu I-U\ \text{是双射}\iff\mu\notin\sigma(U).$$

"逆有界"那一半同样自动：$$\mu\notin\sigma(U)$$ 时 $$U$$ 有界给 $$(\mu I-U)^{-1}$$ 有界，于是由 (3.5)

$$(\lambda I-T)^{-1}=(I-U)\,(\mu I-U)^{-1}\,(\lambda+i)^{-1}$$

有界；反方向由 $$T$$ 闭（自伴故 $$T=T^*$$，而 定理 3.14(i) 说伴随恒闭）加上闭图像定理（第 36 章）给出。两半合起来：

$$\lambda\in\sigma(T)\iff\frac{\lambda-i}{\lambda+i}=\mu\in\sigma(U).$$

**对 $$X$$ 具体算**：$$X$$ 是乘 $$x$$ 的乘法算子；乘法算子的函数演算把 $$\mu(X)$$ 实现为乘 $$\mu(x)$$ 的算子（第 40 章的连续函数演算，在乘法模型里就是逐点相乘），所以

$$(U\varphi)(x)=\frac{x-i}{x+i}\,\varphi(x),\qquad\text{即}\ U=M_{\mu},\ \ \mu(x)=\frac{x-i}{x+i}.$$

$$\lvert\mu(x)\rvert=1$$ 对一切 $$x\in\mathbb R$$，故 $$U$$ 是酉算子（第 36 章乘法算子一段：乘模为 1 的函数是酉的）。$$\mu$$ 是实轴到 $$\mathbb T\setminus\lbrace1\rbrace$$ 的双射，故 $$\overline{\mu(\mathbb R)}=\mathbb T$$，即

$$\sigma(U)=\mathbb T .$$

核对 定理 3.29：

$$\lbrace\lambda\in\mathbb R:\mu(\lambda)\in\sigma(U)\rbrace=\lbrace\lambda\in\mathbb R:\mu(\lambda)\in\mathbb T\rbrace=\mathbb R=\sigma(X),$$

并且 $$1=\mu(\infty)\in\sigma(U)$$ 而 $$1\notin\sigma_p(U)$$（方程 $$\frac{x-i}{x+i}=1$$ 无解）——正对应 定理 3.29 末段"$$X$$ 无界 $$\Rightarrow$$ $$1\in\sigma(U)$$ 但 $$1$$ 不是特征值"。$$\blacksquare$$


**解 研1.** **(a)** $$T_0$$ 的定义域是 $$C_c^\infty(0,1)$$。设 $$g\in L^2(0,1)$$。泛函 $$\phi\mapsto\langle T_0\phi,g\rangle=-\int_0^1\phi''\overline g$$ 在 $$(C_c^\infty,\lVert\cdot\rVert_{L^2})$$ 上连续，当且仅当分布 $$-g''$$ 属于 $$L^2$$（因为 $$C_c^\infty$$ 上的连续性意味着 $$g''$$ 是 $$C_c^\infty$$ 上有界泛函的"密度"，故可表示为 $$L^2$$ 函数与 $$\phi$$ 配对）。于是 $$g''\in L^2(0,1)$$。又 $$g''\in L^2$$ 与 $$g\in L^2$$ 蕴含 $$g'\in L^2$$：取 $$a\in(0,1)$$，$$g'(t)=g'(a)+\int_a^tg''$$ 给出 $$\lvert g'(t)\rvert\le\lvert g'(a)\rvert+\sqrt{\lvert t-a\rvert}\lVert g''\rVert_2$$（Cauchy–Schwarz），右端平方可积。故 $$g\in H^2(0,1)$$。反之 $$g\in H^2(0,1)$$ 时 $$\int_0^1\phi''\overline g=\int_0^1\phi\overline{g''}$$（两次分部积分，边界项因 $$\phi$$ 支集在内部为零），故泛函连续、$$T_0^*g=-g''$$。所以

$$\mathrm{Dom}(T_0^*)=H^2(0,1),\qquad T_0^*=-\frac{d^2}{dt^2}\ \text{（无边界条件）}.$$

**(b)** 求 $$\ker(T_0^*\mp i)$$：$$-u''=\pm iu\iff u''=\mp iu$$。设 $$u=e^{\alpha t}$$，$$\alpha^2=\mp i$$。$$-i$$ 的两个平方根是 $$\pm e^{-i\pi/4}$$，$$+i$$ 的是 $$\pm e^{i\pi/4}$$，各给两个线性无关解，都在 $$H^2(0,1)$$（指数函数光滑）。故

$$n_+=\dim\ker(T_0^*-i)=2,\qquad n_-=\dim\ker(T_0^*+i)=2 .$$

由 定理 3.25，自伴扩张存在，构成 $$U(2)$$ 形的四实参数族（两个端点各一个 $$2\times2$$ 的条件对）。

**(c) Dirichlet**：取 $$\mathrm{Dom}(T_D)=\lbrace u\in H^2(0,1):u(0)=u(1)=0\rbrace$$，$$T_Du=-u''$$。

*对称*：两次分部积分，$$\langle T_Du,v\rangle-\langle u,T_Dv\rangle=\bigl[-u'\overline v+u\overline{v'}\bigr]_0^1$$，端点处 $$u=v=0$$ 使边界项为零：$$T_D$$ 对称。

*自伴*：验证 $$\mathrm{ran}(T_D\pm i)=H$$（定理 3.17）。解 $$-u''\pm iu=f$$ 是二阶线性 ODE；给定 $$f\in L^2$$，通解 = 齐次通解（2 维，在 $$H^2$$ 中）+ 特解。边界条件 $$u(0)=u(1)=0$$ 是两个线性方程；系数矩阵行列式不为零（否则存在非零齐次解的 $$u$$ 满足 $$u(0)=u(1)=0$$ 及 $$-u''=\mp iu$$；但由 解 基1 的恒等式 $$\lVert(T\mp i)u\rVert^2=\lVert Tu\rVert^2+\lVert u\rVert^2$$，$$T_Du=\pm iu$$ 只有零解，且 $$T_D$$ 在 Dirichlet 定义域上对称，故矛盾）。所以对每个 $$f$$ 有唯一解 $$u\in\mathrm{Dom}(T_D)$$，即 $$\mathrm{ran}(T_D\pm i)=H$$。故 $$T_D$$ 自伴。

*谱*：解 $$T_Du=\lambda u$$，$$u''=-\lambda u$$，$$u(0)=u(1)=0$$。$$\lambda=k^2$$ 时 $$u=A\sin(kt)+B\cos(kt)$$；$$u(0)=0\Rightarrow B=0$$，$$u(1)=0\Rightarrow\sin k=0$$，$$k=n\pi$$。$$\lambda<0$$ 时写 $$\lambda=-k^2$$，$$u=A\sinh(kt)$$，$$u(1)=0\Rightarrow\sinh k=0\Rightarrow k=0$$，排除。故

$$\sigma(T_D)=\lbrace n^2\pi^2:\ n=1,2,3,\dots\rbrace,\qquad \text{特征函数}\ \sqrt2\sin(n\pi t).$$

（自伴性保证谱全在实轴、且由 定理 3.30 的 PVM 知这已是全部谱。）

**Neumann**：$$\mathrm{Dom}(T_N)=\lbrace u\in H^2:u'(0)=u'(1)=0\rbrace$$。同样两步给出自伴性；谱为 $$\lambda=k^2$$ 且 $$\cos kt$$ 满足 $$u'(0)=0$$，$$u'(1)=0\Rightarrow\sin k=0$$，$$k=n\pi$$；$$n=0$$ 时 $$\lambda=0$$，$$u=\text{const}$$（常数属 $$H^2$$，$$u'=0$$ 满足 Neumann）。故

$$\sigma(T_N)=\lbrace n^2\pi^2:\ n=0,1,2,\dots\rbrace,\qquad \text{特征函数}\ \cos(n\pi t)\ (n\ge1)、1\ (n=0).$$

**(d)** 由 定理 3.29，两个扩张的谱各自满足 $$\lambda\in\sigma(T)\iff\mu(\lambda)=\frac{\lambda-i}{\lambda+i}\in\sigma(U)$$。Dirichlet 的 $$T_D$$ 是**正**算子（$$\langle T_Du,u\rangle=\int\lvert u'\rvert^2-\bigl[u'\overline u\bigr]_0^1=\lVert u'\rVert^2\ge0$$，且 $$=0$$ 蕴含 $$u$$ 为常数，配合 $$u(0)=0$$ 得 $$u=0$$），故 $$0\notin\sigma(T_D)$$，最小谱点是 $$\pi^2$$。Neumann 的 $$T_N$$ 有常数特征函数，$$0\in\sigma(T_N)$$，对应 $$\mu(0)=\frac{-i}{i}=-1\in\sigma(U_N)$$：**$$T$$ 的低谱端对应 $$U$$ 的谱点靠近 $$-1$$ 还是 $$1$$**——Dirichlet 的 $$\mu(\pi^2)=\frac{\pi^2-i}{\pi^2+i}$$ 在单位圆上离 $$-1$$ 有一段距离，Neumann 的 $$\mu(0)=-1$$ 正好落在 $$-1$$。更本质地说：$$T_D$$ 正且无零特征值，所以 $$0\notin\sigma(T_D)$$；$$T_N$$ 的常数函数是零特征向量，所以 $$0\in\sigma(T_N)$$。**边界条件把最低能级从 $$\pi^2$$ 抬到 $$0$$ 或压下——这就是"墙上有几种反射方式"的谱论后果。**

（本小题是第 44 章的起点：量子力学里"粒子在盒中"与"粒子在环上"的能谱差别，全部由定义域（边界条件）编码，而正则对易关系要在这种受约束的定义域上重新讨论。）$$\blacksquare$$

**解 研2.** **(a)** 设 $$[A,B]=AB-BA=i\hbar I$$。先证一个归纳式：

$$[A,B^n]=B[A,B^{n-1}]+[A,B]B^{n-1}=B[A,B^{n-1}]+i\hbar B^{n-1}.$$

（用 $$[A,XY]=[A,X]Y+X[A,Y]$$。）由归纳假设 $$[A,B^{n-1}]=(n-1)i\hbar B^{n-2}$$，故

$$[A,B^n]=(n-1)i\hbar B^{n-1}+i\hbar B^{n-1}=ni\hbar B^{n-1}.$$

取算子范数：

$$n\hbar\lVert B^{n-1}\rVert=\lVert [A,B^n]\rVert=\lVert AB^n-B^nA\rVert\le\lVert A\rVert\lVert B^n\rVert+\lVert B^n\rVert\lVert A\rVert\le2\lVert A\rVert\lVert B\rVert\lVert B^{n-1}\rVert .$$

（用了次可乘性 $$\lVert B^n\rVert\le\lVert B\rVert^n\le\lVert B\rVert\lVert B^{n-1}\rVert$$。）若 $$B^{n-1}\ne0$$ 则约去得

$$n\hbar\le2\lVert A\rVert\lVert B\rVert\qquad\text{对一切}\ n\ge1,$$

而 $$n$$ 任意大，矛盾。若某个 $$B^{n-1}=0$$，则 $$B$$ 幂零；此时由 $$[A,B^n]=0=ni\hbar B^{n-1}$$ 对一切 $$n$$ 得 $$B^{n-1}=0$$ 对所有 $$n$$，特别 $$n=1$$ 给 $$0=B^0=I$$，矛盾。故 $$A,B$$ 不可能都有界。

**(b)** 形式计算：对 $$\psi\in C_c^\infty(\mathbb R)$$

$$(XP-PX)\psi=x(-i\psi')-(-i)(x\psi)'=-ix\psi'+i(\psi+x\psi')=i\psi .$$

故 $$[X,P]=iI$$（$$\hbar=1$$）在 $$C_c^\infty$$ 上成立。$$C_c^\infty\subseteq\mathrm{Dom}(X)\cap H^1$$，且 $$PX\psi$$、$$XP\psi$$ 都有意义（$$\psi\in C_c^\infty\Rightarrow x\psi\in C_c^\infty\subseteq H^1$$）。所以对易关系在一族公共定义域上成立，而 $$X,P$$ 无界（由 (a) 或直接看特征值无界）。

**(c)** 综合 (a)：正则对易关系 $$[X,P]=i\hbar I$$ 与"两者有界"不相容，故第 44 章的一切陈述都必须写在无界算子的语言里——本章的**定义域、对称 vs 自伴、闭性**就是那套语言，而 $$C_c^\infty$$ 上的形式对易关系之所以能推出物理结论，靠的是把它提升到 定理 3.22 与 命题 3.21 的**自伴**算子（而不只是形式对称），再用 定理 3.30 的谱定理。另一方面，时间演化 $$e^{-itH}$$ 要成为真的酉群，也需要 $$H$$ 自伴（Stone 定理）；而 Cayley 变换（定理 3.28）说明"无界自伴 $$H$$"与"酉算子"是同一份数据的两种写法——**这也是第 44 章把 $$[X,P]=i\hbar I$$ 改写成 Weyl 关系（指数化后的酉算子关系）的动机：无界算子的关系不好直接处理，酉算子的关系好处理。那正是下一章的起点。**$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

1. **无界算子不是"映射"，而是"映射 + 定义域"。** 定义域不是技术细节，它承载物理内容：区间上 $$-\frac{d^2}{dt^2}$$ 的三组边界条件给出三套完全不同的能谱，而算子公式一个字没变（3.5 节）。位置、动量、自由能量的定义域分别是 $$L^2(\mathbb R,(1+x^2)dx)$$、$$H^1(\mathbb R)$$、$$H^2(\mathbb R)$$——把这些写对，本章一半的工作就完成了。

2. **对称与自伴的区分只存在于无界情形。** Hellinger–Toeplitz（定理 3.3）说：处处定义 + 对称 $$\Rightarrow$$ 有界；所以有界世界里两个词合一。无界世界里，对称只保证 $$T\subseteq T^*$$，自伴要求 $$\mathrm{Dom}(T)=\mathrm{Dom}(T^*)$$。判定手段是 $$\mathrm{ran}(T\pm i)=H$$（定理 3.17），量化手段是亏指数（定义 3.24、定理 3.25）。

3. **无界 = 换个范数就有界。** 图像范数（定义 3.7）把 $$\mathrm{Dom}(T)$$ 变成 Hilbert 空间，闭算子在其上是有界算子（推论 3.9）。第 04 章"逐频率除以 $$ik-\lambda$$"的做法能成立，秘密就在这里。

4. **Cayley 变换把无界问题搬回有界问题的世界：$$U=(T-i)(T+i)^{-1}$$。** 它把自伴 $$T$$ 一对一换成酉 $$U$$（定理 3.28），把实轴按半角公式卷成单位圆（定理 3.29），从而让第 38 章的谱定理与第 40 章的函数演算整体可用（定理 3.30）。物理上它就是散射相移 $$e^{i(2\arctan p-\pi)}$$，就是 S 矩阵的最简模型；数学上它是万能公式 $$x=\tan\frac\theta2$$ 的算子版。

5. **谱比特征值大。** $$-\frac{d^2}{dx^2}$$ 在 $$L^2(\mathbb R)$$ 上谱为 $$[0,\infty)$$ 却一个特征向量也没有（定理 3.23）；$$e^{ikx}$$ 不是向量，是"广义特征函数"，正式说法属于第 38 章的 PVM。位置算子同理（经典问题 4）。

6. **本章还清了两笔旧账。** 第 04 章的 $$\sigma(D)=i\mathbb Z$$ 现在有了地基：$$D$$ 在 $$H^1(S^1)$$ 上反自伴（定理 3.31），而第 04 章只用了对称性与显式预解式，那个自我限制是准确的；同时它默默用了"$$H^1$$ 是极大定义域"这一点，本章补上了证明，并解释了为什么圆周上不需要边界条件而区间上需要。第 34 章末尾"$$X,P$$ 不可能有界"那句话，由 Hellinger–Toeplitz（定理 3.3）与研 2 的交换子论证给出两种独立证明。

**下一章的悬念。** 本章造好了语言，但还没用它碰量子力学真正的起点：正则对易关系

$$[\hat x,\hat p]=i\hbar I .$$

第 44 章要问：这个等式（在一族公共稠定定义域上）到底决定了多少东西？答案惊人地刚性——**在 Weyl 形式（指数化后的酉算子关系）下，它在不可约意义上有唯一的表示**，这就是 Stone–von Neumann 定理。中间要过两道本章刚铺好的桥：一是 Stone 定理（自伴算子与单参数强连续酉群的一一对应，其证明正是沿本章定理 3.30 的 PVM 积分 $$e^{-itH}=\int e^{-it\lambda}dE(\lambda)$$），二是"把无界关系指数化成酉算子关系好处理"这条策略——它不过是 Cayley 变换（定理 3.28）的同一思想换个方向再走一次。第 46 章则会把 Cayley 变换再推一步，用算子半群与 Feynman 路径积分处理"$$e^{-tH}$$ 这个半群本身"。

**延伸阅读。**
- MP55（本章入口的母题：位置与动量算子的无界性、乘法算子、图与闭算子、本质自伴）与 MP56（Cayley 变换，从万能公式到实矩阵到复算子）。
- 第 04 章的"诚实清单"（本章 3.7 节正面回应）与第 34 章末尾关于 $$a,a^\dagger$$ 无界的预告。
- 细节补充方向：闭算子的值域定理、自伴扩张与边界三元组（abstract boundary conditions）、Weyl 判据与本质谱——它们都在第 18–20 章的谱论与本章的亏指数之间架桥。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch41_无界算子与Cayley变换_上.md">← 第41章 无界算子与 Cayley 变换·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch43_正则对易关系与Stone_vonNeumann_上.md">第43章 正则对易关系与 Stone–von Neumann·上 →</a></div>
</div>
