---
layout: default
---

# 第52章: 四元数、SO(3)≅RP³、SU(2)≅S³·下：完整推导 (Quaternions, SO(3)≅RP³, SU(2)≅S³ · Part II: Full Derivation)

> 对应原专栏: MP69
> 专家依据: `_experts/algebra/representation-theory.md` + `_experts/algebra/lie-algebra-root-systems.md`
> 知识库依据: `opc2/knowledge/math/李群/lie-groups/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）
> 配套预备: 见 第51章 四元数、SO(3)≅RP³、SU(2)≅S³·上（同一主题的具体铺垫，建议先读）

## 一、本章概要 (Overview)

**从哪来**：第 02 章把「复数乘法就是平面旋转」讲成了一条**定理**，不是一句直观。第 04 章把同一个几何事实换了个说法：平面旋转全体构成群 $$SO(2)$$，它作为拓扑空间就是圆 $$S^1$$，而 $$\mathbb{R}$$ 沿整数点卷到圆上的那个覆叠结构（$$\pi_1(S^1)=\mathbb{Z}$$）解释了幅角的多值性。第 24、25 章开始问三维：$$SO(3)$$ 是什么形状？第 50 章给出了抽象答案——它是个连通紧 Lie 群，它的拓扑可以利用覆叠空间来读。但抽象的答案需要一个**拿在手里能转**的模型。

**本章干什么**：把 $$SO(3)$$ 装进一个具体的代数对象——**单位四元数**。四元数不是"复数加了两个虚数"这种记号把戏；它是第 02 章那个构造**再走一遍**的产物：从 $$\mathbb{R}$$ 到 $$\mathbb{C}$$ 是走第一步，从 $$\mathbb{C}$$ 到 $$\mathbb{H}$$ 是走第二步，规则完全一样。走完之后我们发现单位四元数全体是一个**三维球面** $$S^3$$，它到 $$SO(3)$$ 有一个二对一的满同态 $$\rho$$，核是 $$\{\pm1\}$$。于是

$$SO(3)\cong S^3/\{\pm 1\}\cong \mathbb{RP}^3,\qquad SU(2)\cong S^3 .$$

**代价**：第 01、02 章里 「旋转 $$\leftrightarrow$$ 复数」是一一对应的（$$SO(2)\cong S^1$$）。到了三维，这个对应**多出一层**：同一个旋转对应两个四元数 $$q$$ 与 $$-q$$。这不是缺陷，而是一个新现象——「转 360° 与恒等不同，转 720° 才是恒等」的严格版本就是它。这层多出来的东西在第 60 章（Möbius 群、双重覆盖与射影表示）会以「射影表示」的名义再次出现：电子这类自旋 $$1/2$$ 的对象，其波函数只在这种"多出一层"的意义下才承载 $$SO(3)$$ 的作用。

**到哪去**：本章末尾（研究题 1）会算出 $$\pi_1(SO(3))=\mathbb{Z}/2$$，并把「转圈」这件事化为 $$S^3$$ 上提升曲线的端点问题。第 54 章（Lie 代数与指数映射）将把这套整体拓扑换成无穷小版本：对 $$SO(3)$$ 求导得到 $$\mathfrak{so}(3)$$，四元数的指数映射 $$\theta\mapsto\cos\frac\theta2+n\sin\frac\theta2$$ 里的因子 $$\frac12$$ 就是本章的二重覆盖在无穷小层面的印记。

## 二、入口：一道具体的问题 (Entry Problem)

> 题目来源：**自编**。母题有二：一是刚体运动学中的经典现象「Dirac 绳戏 (belt trick)」，二是 Lie 群理论里「$$S^3$$ 双重覆盖 $$SO(3)$$」的标准例子。把两者并成一道题、并要求其答案用本章的两套语言各说一遍，是本章的设计。

**入口题。**

**(a)** 把 $$SO(3)$$ 看成拓扑空间（第 24、25 章）。固定 $$z$$ 轴，记 $$\gamma(t)$$ 为「绕 $$z$$ 轴逆时针转 $$t$$ 弧度」这个旋转，$$0\le t\le 2\pi$$。于是 $$\gamma(0)=\gamma(2\pi)=I$$，即 $$\gamma$$ 是 $$SO(3)$$ 中以 $$I$$ 为基点的**闭路 (loop)**。

**问**：这条闭路能否在 $$SO(3)$$ 内**连续地收缩**为常值回路（即：是否存在一个把 $$\gamma$$ 与"停在 $$I$$ 不动的常值回路"连通起来的连续形变）？

**(b)** 把 (a) 中的「转 $$t$$」换成「转 $$2t$$」（$$0\le t\le 2\pi$$），也就是从 $$0$$ 一直转到 $$4\pi$$，物体转两整圈。这条闭路能收缩吗？

> 先动手做：取一根皮带或一根绳子，一端踩住（或夹住），另一端用手捏住。把手腕转一整圈——带子中间出现的扭结，能在**不转动手**的前提下解开吗？再试手腕转两整圈。(a)(b) 就是这个问题去掉物理外衣的样子。

**(c)** 下面是一道**纯代数计算**，乘法规则直接给出，不需要几何背景。给四个符号 $$1,i,j,k$$，规定 $$1$$ 是乘法单位且与全体可交换，其余乘法由下式确定（乘法对加法与实数倍双线性）：

$$i^2=j^2=k^2=-1,\qquad ij=k,\qquad jk=i,\qquad ki=j .$$

（没有写出来的乘积，如 $$ji$$，暂不假设；本章 §3 会证明它们被上式**唯一确定**，且 $$ji=-k$$。）

记

$$S^3=\{\,x_0+x_1i+x_2j+x_3k\ :\ x_0,x_1,x_2,x_3\in\mathbb{R},\ x_0^2+x_1^2+x_2^2+x_3^2=1\,\}.$$

**(i)** 证明实部为 $$-1$$ 的元素（记作 $$-1$$）以及 $$1$$ 都在 $$S^3$$ 中；再证明：若 $$q\in S^3$$，则存在 $$q^{-1}\in S^3$$ 使 $$qq^{-1}=q^{-1}q=1$$。

**(ii)** 对实数 $$\theta$$ 记 $$q_\theta=\cos\dfrac{\theta}{2}+k\sin\dfrac{\theta}{2}$$。用乘法规则算出 $$q_\theta\, i\, q_\theta^{-1}$$ 与 $$q_\theta\, j\, q_\theta^{-1}$$，把结果写成 $$1,i,j,k$$ 的实系数线性组合。特别地，$$\theta=2\pi$$ 时 $$q_\theta$$ 等于什么？$$\theta=4\pi$$ 呢？

**(iii)** 把 (ii) 中「取 $$q\in S^3$$、做 $$x\mapsto qxq^{-1}$$」看成 $$S^3$$ 的一个操作，那么 (ii) 说明 $$q_\theta$$ 对 $$i,j$$ 做了某一件事。把这件事与 (a)(b) 对上：找出 (a)、(b) 两条闭路在 $$S^3$$ 中「抬起来」（成为 $$q$$ 随 $$t$$ 变化的曲线）分别长什么样，从而解释为什么 (a) 缩不了而 (b) 能缩。

**为什么这是同一道题。** (a)(b) 是拓扑问题，(c) 是代数问题，但它们的答案是同一句话的两面。读完本章你会看到：(c)(ii) 给出的是「绕 $$k$$ 轴转 $$\theta$$」的四元数，而 $$\theta=2\pi$$ 时它落在 $$-1$$ 处、$$\theta=4\pi$$ 时才回到 $$1$$——**转一整圈的旋转对应四元数从 $$1$$ 走到 $$-1$$，转两整圈才回到 $$1$$**。把这条 $$S^3$$ 里的曲线"压"到 $$SO(3)$$ 上，(a) 那条闭路的提升是一条从 $$1$$ 到 $$-1$$ 的**非闭合**道路，所以它缩不了；(b) 的提升是 $$S^3$$ 中一条真正的闭路，而 $$S^3$$ 单连通（第 16 章），所以它缩得了。结论：

$$\text{「转一整圈不是恒等，转两整圈才是」}\ \Longleftrightarrow\ \pi_1(SO(3))\cong\mathbb{Z}/2 .$$

四元数不是描述旋转的一种"方便记号"，它是把 $$SO(3)$$ 拆成两半的那层空间 $$S^3$$。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 复数：一个可以复制的构造模板

第 02 章的 定理 3.4 说的是：$$i^2=-1$$ **不是公理，是定理**。回顾它的做法——不是"规定"一个平方为 $$-1$$ 的数，而是先在 $$\mathbb{R}^2$$ 上要求一个乘法，使它实现"模相乘、幅角相加"（第 02 章的 定理 3.5），然后证明这样得到的乘法恰好把 $$(0,1)\cdot(0,1)$$ 送到 $$(-1,0)$$。把那个构造抽出来看，它的骨架是：

> **构造模板。** 取一个 $$\mathbb{R}$$-代数 $$A$$（对加法、实数倍、乘法封闭且乘法结合），外加一个元素 $$\iota$$，要求
> $$\iota^2=-1,$$
> 并要求 $$\iota$$ 与 $$A$$ 中所有元素可交换；然后取这个结构"最小"的实现。

对 $$A=\mathbb{R}$$ 走一遍这个模板，得到的正是 $$\mathbb{C}=\{a+bi\}$$，也正如第 02 章所证，它作为"乘法算子"就是平面旋转。**本章要做的事，是把同一个模板对 $$A=\mathbb{C}$$ 再走一遍。** 唯一的改动是：第二遍里我们**放弃**"新元素与旧元素可交换"这一条——因为放弃它，得到的才是三维旋转的代数。

### 3.2 从 $$\mathbb{C}$$ 到 $$\mathbb{H}$$：同一步走第二遍

模板的第二遍走法有一个经典的落点：$$\mathbb{C}$$ 上的 $$2\times2$$ 矩阵。我们先把这个落点写出来，再证明它确实是模板的产物。

**定义 3.1（四元数代数, quaternion algebra）** 记 $$\sigma_1,\sigma_2,\sigma_3$$ 为 **Pauli 矩阵 (Pauli matrices)**

$$\sigma_1=\begin{bmatrix}0&1\\1&0\end{bmatrix},\qquad
\sigma_2=\begin{bmatrix}0&-i\\ i&0\end{bmatrix},\qquad
\sigma_3=\begin{bmatrix}1&0\\0&-1\end{bmatrix},$$

（这里右边出现的 $$i$$ 是 $$\mathbb{C}$$ 的虚数单位，不要与下面的大写 $$\mathbb I$$ 混淆）。令

$$\mathbb I:=-i\sigma_1=\begin{bmatrix}0&-i\\-i&0\end{bmatrix},\qquad
\mathbb J:=-i\sigma_2=\begin{bmatrix}0&-1\\1&0\end{bmatrix},\qquad
\mathbb K:=-i\sigma_3=\begin{bmatrix}-i&0\\0&i\end{bmatrix},$$

并定义

$$\mathbb{H}:=\operatorname{span}_\mathbb{R}\{\,I_2,\ \mathbb I,\ \mathbb J,\ \mathbb K\,\}\ \subset\ M_2(\mathbb{C}).$$

$$\mathbb{H}$$ 中的元素称为**四元数 (quaternion)**。

注意 $$\mathbb I,\mathbb J,\mathbb K$$ 里都带因子 $$-i$$：$$\sigma_1,\sigma_2,\sigma_3$$ 都是 Hermite 矩阵（$$\sigma_k^*=\sigma_k$$），乘上 $$-i$$ 之后 $$\mathbb I,\mathbb J,\mathbb K$$ 变成**反 Hermite** 的（$$\mathbb I^*=-\mathbb I$$，其余同理）。这正是"纯虚"在矩阵里的对应物：下面的定理 3.3 会证明映射 $$q\mapsto q^*$$ 恰好就是矩阵的共轭转置，于是"纯虚四元数"（$$q^*=-q$$）恰好对应反 Hermite 矩阵。

**定理 3.1（乘法表）** $$\mathbb{H}$$ 对矩阵乘法封闭，从而是 $$M_2(\mathbb{C})$$ 的 $$4$$ 维子代数；$$\{I_2,\mathbb I,\mathbb J,\mathbb K\}$$ 是它的一组基。在这组基下，乘法由下式完全决定：

$$\mathbb I^2=\mathbb J^2=\mathbb K^2=-I_2,\qquad
\mathbb I\mathbb J=\mathbb K,\quad \mathbb J\mathbb K=\mathbb I,\quad \mathbb K\mathbb I=\mathbb J,$$
$$\mathbb J\mathbb I=-\mathbb K,\quad \mathbb K\mathbb J=-\mathbb I,\quad \mathbb I\mathbb K=-\mathbb J,\qquad
\mathbb I\mathbb J\mathbb K=-I_2 .$$

把 $$I_2,\mathbb I,\mathbb J,\mathbb K$$ 依次记作 $$1,i,j,k$$，上表就是入口题 (c) 给出的那套规则，并顺带补全了未写出的 $$ji=-k$$ 等三条。特别地 $$\mathbb{H}$$ **不交换**：$$ij\neq ji$$。

*证明*：只需逐对计算三个矩阵的乘积，都是 $$2\times2$$ 的直接乘法。我们算三组，其余完全类似。

$$\mathbb I^2=\begin{bmatrix}0&-i\\-i&0\end{bmatrix}\begin{bmatrix}0&-i\\-i&0\end{bmatrix}
=\begin{bmatrix}(-i)(-i)&0\\0&(-i)(-i)\end{bmatrix}=\begin{bmatrix}-1&0\\0&-1\end{bmatrix}=-I_2,$$
$$\mathbb J^2=\begin{bmatrix}0&-1\\1&0\end{bmatrix}\begin{bmatrix}0&-1\\1&0\end{bmatrix}
=\begin{bmatrix}-1&0\\0&-1\end{bmatrix}=-I_2,$$
$$\mathbb I\mathbb J=\begin{bmatrix}0&-i\\-i&0\end{bmatrix}\begin{bmatrix}0&-1\\1&0\end{bmatrix}
=\begin{bmatrix}-i&0\\0&i\end{bmatrix}=\mathbb K,$$
$$\mathbb J\mathbb I=\begin{bmatrix}0&-1\\1&0\end{bmatrix}\begin{bmatrix}0&-i\\-i&0\end{bmatrix}
=\begin{bmatrix}i&0\\0&-i\end{bmatrix}=-\mathbb K .$$

用 $$\mathbb K^2=-I_2$$ 与已算出的 $$\mathbb I\mathbb J=\mathbb K$$ 得 $$\mathbb I\mathbb J\mathbb K=\mathbb K^2=-I_2$$。剩下三条从 $$\mathbb I\mathbb J=\mathbb K$$ 派生：两边左乘 $$\mathbb I$$ 得 $$\mathbb I^2\mathbb J=\mathbb I\mathbb K$$，即 $$\mathbb I\mathbb K=-\mathbb J$$；两边右乘 $$\mathbb J$$ 得 $$\mathbb I\mathbb J^2=\mathbb K\mathbb J$$，即 $$\mathbb K\mathbb J=-\mathbb I$$；再把两边左乘 $$\mathbb J$$ 得 $$\mathbb J\mathbb I\mathbb J=\mathbb J\mathbb K$$，即 $$(-\mathbb K)\mathbb J=\mathbb J\mathbb K$$，配合 $$\mathbb K\mathbb J=-\mathbb I$$ 得 $$\mathbb J\mathbb K=\mathbb I$$；最后把 $$\mathbb I\mathbb J=\mathbb K$$ 右乘 $$\mathbb I$$，用 $$\mathbb J\mathbb I=-\mathbb K$$ 与 $$\mathbb I\mathbb K=-\mathbb J$$ 得 $$\mathbb K\mathbb I=\mathbb J$$。所有乘积都落在 $$\{I_2,\mathbb I,\mathbb J,\mathbb K\}$$ 的 $$\mathbb R$$-张成里，所以对乘法封闭。

$$\{I_2,\mathbb I,\mathbb J,\mathbb K\}$$ 线性无关：设 $$x_0I_2+x_1\mathbb I+x_2\mathbb J+x_3\mathbb K=0$$，看 $$(1,1)$$ 元得 $$x_0-ix_3=0$$，看 $$(1,2)$$ 元得 $$-ix_1-x_2=0$$，虚部实部分离即得 $$x_0=x_1=x_2=x_3=0$$。故 $$\dim_\mathbb{R}\mathbb{H}=4$$。$$\blacksquare$$

**定理 3.2（$$\mathbb{H}$$ 就是"模板的第二遍"：Cayley–Dickson 描述）** 每个 $$q\in\mathbb{H}$$ 可**唯一**地写成

$$q=a+bj,\qquad a,b\in\mathbb{C},$$

其中 $$\mathbb{C}$$ 指 $$\operatorname{span}_\mathbb{R}\{I_2,\mathbb I\}$$。并且对每个 $$z\in\mathbb{C}$$，

$$jz=\bar z\,j\qquad(\bar z\ \text{是}\ z\ \text{的复共轭}).$$

等价地：$$ji=-ij$$。因此 $$\mathbb{H}$$ 正是"取 $$A=\mathbb{C}$$、加一个满足 $$\iota^2=-1$$ 的元素 $$j$$、放弃交换性"的产物。

*证明*：把 $$i=\mathbb I$$ 视为 $$\mathbb C$$ 的虚单位，记 $$a=x_0+x_1 i,\ b=x_2+x_3 i$$（$$x_\nu\in\mathbb R$$）。则

$$a+bj=(x_0+x_1 i)+(x_2+x_3 i)j=x_0+x_1i+x_2j+x_3\underbrace{ij}_{=k},$$

与定理 3.1 的基表示一致，唯一性来自基的线性无关。又对 $$z=x+iy$$：

$$jz=j(xI_2+y\mathbb I)=xj+y\,j i,\qquad \bar z\, j=(x-iy)j=xj-y\,ij .$$

两者相等当且仅当 $$ji=-ij$$，这正是定理 3.1 已算出的。最后由双线性，$$jz=\bar zj$$ 对一切 $$z\in\mathbb C$$ 成立。$$\blacksquare$$

### 3.3 共轭、模与可除性

**定义 3.2（共轭与模, conjugate and modulus）** 对 $$q=x_0+x_1i+x_2j+x_3k\in\mathbb{H}$$，定义它的**共轭 (conjugate)**

$$q^*:=x_0-x_1i-x_2j-x_3k,$$

以及**模 (modulus)**

$$\lvert q\rvert:=\sqrt{x_0^2+x_1^2+x_2^2+x_3^2}.$$

注意 $$\lvert q\rvert^2=qq^*$$（下面证明）。矩阵地看，若

$$\phi(q)=\begin{bmatrix}a&b\\-\bar b&\bar a\end{bmatrix}\qquad(a=x_0-ix_3,\ b=-x_2-ix_1),$$

则 $$q^*$$ 对应 $$\phi(q)$$ 的**共轭转置 (conjugate transpose)**。这个形式上的对应不是巧合，它是下面 (i) 的来源——也因此 $$\mathbb{H}$$ 里"共轭"的记法与复数的完全兼容。

**定理 3.3（$$\mathbb{H}$$ 是可除环, division ring）**

(i) 对一切 $$p,q\in\mathbb{H}$$：$$(pq)^*=q^*p^*$$；

(ii) $$qq^*=q^*q=\lvert q\rvert^2\in\mathbb{R}_{\ge0}$$，且 $$q q^*=0\iff q=0$$；

(iii) 模是乘性的：$$\lvert pq\rvert=\lvert p\rvert\cdot\lvert q\rvert$$；

(iv) 每个非零 $$q$$ 有逆 $$q^{-1}=q^*/\lvert q\rvert^2\in\mathbb{H}$$。因此 $$\mathbb{H}$$ 是一个**除环**：每个非零元可逆，但乘法不交换。

*证明思路*：把 $$\mathbb{H}$$ 实现为 $$2\times2$$ 复矩阵的子代数，然后"共轭 $$\leftrightarrow$$ 共轭转置"、"模的平方 $$\leftrightarrow$$ 行列式"。行列式是乘性的，于是 (iii) 立得。

*证明*：先写出矩阵实现。对 $$q=x_0+x_1i+x_2j+x_3k$$ 有

$$\phi(q)=x_0I_2+x_1\mathbb I+x_2\mathbb J+x_3\mathbb K
=\begin{bmatrix}x_0-ix_3&-ix_1-x_2\\-ix_1+x_2&x_0+ix_3\end{bmatrix}
=\begin{bmatrix}a&b\\-\bar b&\bar a\end{bmatrix},\qquad
\begin{aligned}a&=x_0-ix_3,\\ b&=-x_2-ix_1.\end{aligned}$$

$$\phi$$ 是线性同构（定理 3.1 的线性无关），且由定理 3.1 保持乘法并送 $$1\mapsto I_2$$：$$\phi(pq)=\phi(p)\phi(q)$$。

(i) 对上述 $$\phi(q)$$，其共轭转置为

$$\phi(q)^*=\begin{bmatrix}\bar a&-\bar b\\ b&a\end{bmatrix}
=\begin{bmatrix}x_0+ix_3&ix_1+x_2\\-ix_1+x_2&x_0-ix_3\end{bmatrix}
=\phi(q^*),$$

末一等式是把 $$q^*$$ 的各项符号代入 $$\phi$$ 的定义直接得到。于是 $$\phi((pq)^*)=\phi(pq)^*=\big(\phi(p)\phi(q)\big)^*=\phi(q)^*\phi(p)^*=\phi(q^*p^*)$$，两边用 $$\phi$$ 单射去 $$\phi$$，得 (i)。

(ii) 对任何 $$2\times2$$ 矩阵 $$M$$，由伴随矩阵公式 $$M\cdot\operatorname{adj}(M)=\det(M)I_2$$，而 $$\operatorname{adj}\!\begin{bmatrix}a&b\\-\bar b&\bar a\end{bmatrix}=\begin{bmatrix}\bar a&-b\\ \bar b&a\end{bmatrix}=\phi(q)^*$$（与 (i) 中算出的 $$\phi(q)^*$$ 逐项相同）。故

$$\phi(q)\phi(q)^*=\det\phi(q)\cdot I_2,\qquad \det\phi(q)=a\bar a+b\bar b=x_0^2+x_3^2+x_1^2+x_2^2 .$$

这就是 $$qq^*=\lvert q\rvert^2$$。(i) 的式子取 $$p=q^*$$ 并再用一次 (i)（注意 $$q^{**}=q$$）得 $$q^*q=(q^*q)^{**}=(q q^*)^*=\lvert q\rvert^2$$（实数共轭是自身）。$$qq^*=0$$ 当且仅当 $$\lvert q\rvert^2=0$$，当且仅当四个分量全零。

(iii) 由 (ii) 与 (i)：$$(pq)(pq)^*=p\,q\,q^*\,p^*=\lvert q\rvert^2\,p\,p^*=\lvert q\rvert^2\lvert p\rvert^2$$（第二步把实标量 $$\lvert q\rvert^2$$ 移到前面）。两边开方得 $$\lvert pq\rvert=\lvert p\rvert\lvert q\rvert$$。

(iv) 由 (ii)(iii)：$$q\cdot\big(q^*/\lvert q\rvert^2\big)=\lvert q\rvert^2/\lvert q\rvert^2=1$$，同法左乘亦然。$$\blacksquare$$

（顺带解释定理 3.3 的"除环"一词：$$\mathbb{H}$$ 几乎是一个域，唯一缺的是交换性。由经典的 Frobenius 定理，有限维实结合可除代数只有 $$\mathbb{R}$$（一维）、$$\mathbb{C}$$（二维）、$$\mathbb{H}$$（四维）三个，$$\mathbb{H}$$ 是其中唯一**非交换**的。八维的 Cayley 八元数已不满足结合律——模板走到第三步就出事了。）

### 3.4 单位四元数、$$S^3$$ 与 $$SU(2)$$

**定理 3.4（$$S^3\cong SU(2)$$）** 记

$$S^3=\{\,q\in\mathbb{H}\ :\ \lvert q\rvert=1\,\}.$$

则 $$\phi$$ 限制在 $$S^3$$ 上是到**二维特殊酉群 (special unitary group)**

$$SU(2)=\{\,Q\in M_2(\mathbb{C})\ :\ Q^*Q=I_2,\ \det Q=1\,\}$$

的群同构。特别地，$$S^3$$ 按四元数乘法成群，且作为拓扑空间就是 $$\mathbb{R}^4$$ 中的单位球面。

*证明*：设 $$\lvert q\rvert=1$$。由定理 3.3(ii)，$$\phi(q)\phi(q)^*=I_2$$；由定理 3.3 的证明，$$\det\phi(q)=\lvert q\rvert^2=1$$。故 $$\phi(q)\in SU(2)$$。

反过来设 $$Q\in SU(2)$$，写成 $$Q=\begin{bmatrix}a&b\\ c&d\end{bmatrix}$$。由 $$Q^*Q=I_2$$ 得 $$Q^*=Q^{-1}$$，由 $$\det Q=1$$ 得 $$Q^{-1}=\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$$。逐项比对 $$Q^*=\begin{bmatrix}\bar a&\bar c\\ \bar b&\bar d\end{bmatrix}$$ 与 $$Q^{-1}$$：

$$\bar a=d,\qquad \bar b=-c,\qquad \bar c=-b,\qquad \bar d=a .$$

第二、三式等价（互相取共轭），于是 $$c=-\bar b,\ d=\bar a$$，即

$$Q=\begin{bmatrix}a&b\\-\bar b&\bar a\end{bmatrix}=\phi(q),\qquad q \text{ 由 } a=x_0-ix_3,\ b=-x_2-ix_1 \text{ 反解}.$$

（反解明确写出来：$$x_0=\operatorname{Re}a,\ x_3=-\operatorname{Im}a,\ x_2=-\operatorname{Re}b,\ x_1=-\operatorname{Im}b$$。）并且 $$\det Q=\lvert a\rvert^2+\lvert b\rvert^2=1$$，正是 $$\lvert q\rvert=1$$。所以 $$\phi:S^3\to SU(2)$$ 是双射；它是群同态是因为 $$\phi$$ 保乘法；它是同胚是因为 $$\phi$$ 的四个矩阵元是 $$(x_0,x_1,x_2,x_3)$$ 的实线性（连续）函数，其反解同样连续。$$\blacksquare$$

**必须显式点出的一步。** 定理 3.4 是第 04 章的升级：那里是 $$SO(2)\cong S^1$$（一维圆），这里是 $$SU(2)\cong S^3$$（三维球面）。同一件事实——"旋转全体是一个球面"——在两个维度上分别成立，但**球面的维度不同、性质也不同**：$$S^1$$ 有 $$\pi_1=\mathbb{Z}$$（可以绕无穷多次），$$S^3$$ 有 $$\pi_1=0$$（绕不过去）。这个差别正是下一节二重覆盖的全部内容。

### 3.5 共轭作用给出的旋转 $$\rho:S^3\to SO(3)$$

现在让四元数"作用"起来。关键的想法来自入口题 (c)：$$q\,i\,q^{-1}$$ 仍是纯虚的四元数，而 $$i,j,k$$ 三个纯虚元恰好可以读作 $$\mathbb{R}^3$$ 的一组坐标。

记 $$\operatorname{Im}\mathbb{H}=\operatorname{span}_\mathbb{R}\{i,j,k\}$$（**纯虚四元数 (pure quaternion)**，其特征是 $$x^*=-x$$），并通过

$$x_1i+x_2j+x_3k\ \longleftrightarrow\ (x_1,x_2,x_3)\in\mathbb{R}^3$$

把 $$\operatorname{Im}\mathbb{H}$$ 与 $$\mathbb{R}^3$$ 等同。由定理 3.3(ii)，$$\lvert x\rvert=\sqrt{x_1^2+x_2^2+x_3^2}$$ 就是通常的欧氏长度。

**定理 3.5（$$\rho$$ 是到 $$SO(3)$$ 的同态）** 对 $$q\in S^3$$、$$x\in\operatorname{Im}\mathbb{H}$$，定义

$$\rho(q)\,x:=q\,x\,q^{-1}=q\,x\,q^{*}.$$

则

(i) $$\rho(q)x\in\operatorname{Im}\mathbb{H}$$；

(ii) $$\rho(q)$$ 是 $$\operatorname{Im}\mathbb{H}$$ 上的线性变换，且

$$\langle \rho(q)x,\rho(q)y\rangle=\langle x,y\rangle$$

对一切 $$x,y\in\operatorname{Im}\mathbb{H}$$ 成立（$$\langle\cdot,\cdot\rangle$$ 是 $$\mathbb{R}^3$$ 的标准内积）；

(iii) $$\rho(q_1q_2)=\rho(q_1)\rho(q_2)$$、$$\rho(1)=\operatorname{id}$$，即 $$\rho$$ 是群同态 $$S^3\to GL(\operatorname{Im}\mathbb{H})\cong GL(3,\mathbb{R})$$；

(iv) 每个 $$\rho(q)$$ 是正交矩阵，且 $$\det\rho(q)=1$$。因此

$$\rho:S^3\longrightarrow SO(3)$$

是群同态。

*证明思路*：(i) 用"纯虚"的判据 $$x^*=-x$$ 与定理 3.3(i)；(ii) 把模的乘性翻译成内积的保持（极化）；(iii) 直接代入结合律；(iv) 正交性是 (ii) 的改写，行列式为正靠连续性 + 连通性。

*证明*：(i) $$\big(\rho(q)x\big)^*=q\,x^*\,q^*=q(-x)q^*=-\rho(q)x$$（第一、三步用定理 3.3(i) 与 $$(q^*)^*=q$$），故纯虚。

(ii) 线性：$$x\mapsto qxq^*$$ 对 $$x$$ 是左乘与右乘的复合，是线性的。内积保持：由定理 3.3(ii)(iii) 的模乘性（$$\lvert q\rvert=1$$，故 $$\lvert q x q^*\rvert=\lvert x\rvert$$），再用**极化恒等式**把模还原成内积：

$$\langle x,y\rangle=\frac{\lvert x+y\rvert^2-\lvert x\rvert^2-\lvert y\rvert^2}{2}.$$

（对纯虚元，$$\lvert x\rvert^2=x_1^2+x_2^2+x_3^2$$，右端确实算得 $$x_1y_1+x_2y_2+x_3y_3$$。）因 $$\rho(q)$$ 保 $$\lvert\cdot\rvert^2$$ 且线性，它保内积。

(iii) $$\rho(q_1q_2)x=(q_1q_2)x(q_1q_2)^{-1}=q_1(q_2xq_2^{-1})q_1^{-1}=\rho(q_1)\big(\rho(q_2)x\big)$$；$$\rho(1)x=x$$。

(iv) (ii) 说 $$\rho(q)$$ 保内积，即 $$\rho(q)^{\mathsf T}\rho(q)=I$$，故 $$\rho(q)\in O(3)$$。要证明行列式为 $$+1$$：矩阵元是 $$q=(x_0,x_1,x_2,x_3)$$ 的多项式，故 $$\det\circ\rho:S^3\to\{\pm1\}$$ 连续；而 $$S^3$$ 连通（它是球面），连续函数把连通集送到连通集，$$\{\pm1\}$$ 的连通子集只有单点集，故 $$\det\rho$$ 是常数；由 $$\rho(1)=\operatorname{id}$$ 得该常数为 $$\det I=1$$。所以 $$\rho(q)\in SO(3)$$。$$\blacksquare$$

**定理 3.6（$$\rho$$ 是满射：每个旋转都是某个四元数的共轭）**

**(Euler 旋转定理)** 每个 $$R\in SO(3)$$ 都存在**单位**向量 $$n\in\mathbb{R}^3$$ 与角 $$\theta\in[0,2\pi)$$，使 $$R$$ 是"绕 $$n$$ 逆时针转 $$\theta$$"的旋转。

对这样的 $$R$$，取 $$q=\cos\dfrac{\theta}{2}+n\sin\dfrac{\theta}{2}\in S^3$$（把 $$n=n_1i+n_2j+n_3k$$ 读作纯虚元），则 $$\rho(q)=R$$。特别地 $$\rho$$ 满射。

*证明思路*：先证 $$R$$ 必有特征值 $$1$$（转轴），再用正交基把它分块对角化，在垂直于轴的平面上读出转角，最后**直接计算**罗德里格斯式的公式验证 $$\rho(q)$$ 就是它。

*证明*：（Euler 定理）记 $$I_3$$ 为 $$3\times3$$ 单位阵。用 $$\det(R^{\mathsf T})=\det R=1$$：

$$\det(R-I_3)=\det\big(R(I_3-R^{\mathsf T})\big)=\det R\cdot\det(I_3-R^{\mathsf T})=\det\big((I_3-R)^{\mathsf T}\big)=\det(I_3-R).$$

另一方面对 $$3\times3$$ 矩阵有 $$\det(-M)=(-1)^3\det M=-\det M$$，故 $$\det(I_3-R)=-\det(R-I_3)$$。于是 $$\det(R-I_3)=-\det(R-I_3)$$，即 $$\det(R-I_3)=0$$，$$R$$ 有实特征值 $$1$$。取对应的单位向量 $$n$$。

把 $$n$$ 扩充为 $$\mathbb{R}^3$$ 的标准正交基 $$(n,u,w)$$，注意 $$w=u\times n$$ 使定向一致。在此基下，$$R$$ 的矩阵形如 $$\begin{bmatrix}1&0\\0&A\end{bmatrix}$$，其中 $$A\in O(2)$$（$$R$$ 保内积、且把 $$n^\perp$$ 映到自身），且 $$\det A=\det R=1$$，所以 $$A\in SO(2)$$，由第 04 章的 定理 3.1 存在 $$\theta$$ 使 $$A=R_\theta$$ 是转角 $$\theta$$ 的平面旋转。这就证明了 Euler 定理。

（$$\rho(q)=R$$）设 $$q=\cos\frac\theta2+\sin\frac\theta2\,n$$。先看轴：因为 $$n^2=-1$$，有 $$qn=\cos\frac\theta2\,n+\sin\frac\theta2\,n^2=\cos\frac\theta2\,n-\sin\frac\theta2$$，而 $$nq$$ 算出同一式子，故 $$qn=nq$$，于是

$$\rho(q)n=qnq^{-1}=nqq^{-1}=n .$$

$$n$$ 被固定。再看垂直平面上的作用。对纯虚单位向量 $$u\perp n$$，用纯虚元乘积公式

$$xy=-\langle x,y\rangle+x\times y\qquad(x,y\in\operatorname{Im}\mathbb{H})$$

（把两边分别展开 $$(x_1i+x_2j+x_3k)(y_1i+y_2j+y_3k)$$ 即得，这是四元数乘法与 $$\mathbb{R}^3$$ 的点积、叉积之间的桥梁）。由 $$u\perp n$$、$$\lvert u\rvert=\lvert n\rvert=1$$ 得 $$nu=n\times u=:v$$，且 $$v\perp n,\ v\perp u,\ \lvert v\rvert=1$$。直接展开 $$q\,u\,q^{*}$$：

$$q\,u\,q^*=\Big(\cos\tfrac\theta2+\sin\tfrac\theta2\,n\Big)u\Big(\cos\tfrac\theta2-\sin\tfrac\theta2\,n\Big)
=\cos^2\tfrac\theta2\,u+\cos\tfrac\theta2\sin\tfrac\theta2\,(nu-un)+\sin^2\tfrac\theta2\,(-nun).$$

逐项化简：$$nu=v$$，$$un=-v$$，而 $$nun=n(n\times u)=n\langle n,u\rangle-u\lvert n\rvert^2=-u$$（叉积恒等式 $$a\times(a\times b)=a\langle a,b\rangle-b\lvert a\rvert^2$$）。代回：

$$q\,u\,q^*=\big(\cos^2\tfrac\theta2-\sin^2\tfrac\theta2\big)u+2\sin\tfrac\theta2\cos\tfrac\theta2\,v=\cos\theta\,u+\sin\theta\,(n\times u).$$

右端正是"把 $$u$$ 绕 $$n$$ 逆时针转 $$\theta$$"（$$n\times u$$ 是 $$u$$ 转 $$+90^\circ$$ 的方向）。把它与 $$\rho(q)n=n$$ 合起来，$$\rho(q)$$ 与"绕 $$n$$ 转 $$\theta$$"这个旋转在 $$\{n,u,v\}$$（$$\mathbb R^3$$ 的一组基）上取值相同，故 $$\rho(q)=R$$。$$\blacksquare$$

（**注**：上式 $$q\,u\,q^*=\cos\theta\,u+\sin\theta\,(n\times u)$$ 就是四元数版的 Rodrigues 公式；第 54 章会对 $$\rho$$ 求导得到 $$\mathfrak{so}(3)$$，那里会从另一个方向再遇见它。）

### 3.6 核与像：$$SO(3)\cong S^3/\{\pm1\}\cong\mathbb{RP}^3$$

**定理 3.7（核）** $$\ker\rho=\{\pm1\}=\{1,-1\}$$。也就是说，方程 $$\rho(q)=\operatorname{id}$$ 只有两个解 $$q=1$$ 和 $$q=-1$$；于是**每个旋转恰好对应两个四元数** $$q$$ 与 $$-q$$。

*证明思路*：$$\rho(q)=\operatorname{id}$$ 等价于 $$q$$ 与所有纯虚元对易；再加上 $$q$$ 与 $$1$$ 当然对易，就是 $$q$$ 落在 $$\mathbb{H}$$ 的**中心 (center)** 里。算出中心只有实数，再配合 $$\lvert q\rvert=1$$ 即得。

*证明*：设 $$q\in S^3$$ 且 $$\rho(q)=\operatorname{id}$$，即 $$qxq^*=x$$ 对一切纯虚 $$x$$，右乘 $$q$$ 得

$$qx=xq\qquad\text{对一切纯虚 }x.$$

又 $$q\cdot 1=1\cdot q$$ 平凡地成立，而 $$\mathbb{H}=\mathbb{R}\cdot1\oplus\operatorname{Im}\mathbb{H}$$，故上式对一切 $$x\in\mathbb{H}$$ 成立，即 $$q\in Z(\mathbb{H})$$（中心）。

求中心：写 $$q=x_0+x_1i+x_2j+x_3k$$。由 $$qi=iq$$ 展开：

$$qi=x_0i-x_1-x_2k+x_3j,\qquad iq=x_0i-x_1+x_2k-x_3j .$$

比较 $$k$$、$$j$$ 的系数得 $$x_2=x_3=0$$（一次得到两个等式 $$-x_2=x_2$$，$$x_3=-x_3$$）。再对 $$qj=jq$$ 展开（此时 $$q=x_0+x_1i$$）：

$$qj=x_0j+x_1\underbrace{ij}_{k},\qquad jq=x_0j+x_1\underbrace{ji}_{-k},$$

比较得 $$x_1=0$$。于是 $$q=x_0\in\mathbb{R}$$。再由 $$\lvert q\rvert=1$$ 得 $$x_0=\pm1$$。

反之 $$q=\pm1$$ 显然在核中。$$\blacksquare$$

**推论 3.8（$$SO(3)\cong\mathbb{RP}^3$$）** 有拓扑群同构

$$SO(3)\cong S^3/\{\pm1\}\cong\mathbb{RP}^3 .$$

其中 $$S^3/\{\pm1\}$$ 是把每对对径点 $$\{q,-q\}$$ 粘成一点得到的商空间，$$\mathbb{RP}^3$$ 是三维实射影空间（$$\mathbb{R}^4$$ 中过原点的直线全体）。

*证明思路*：第一步用群同态基本定理（配合紧性把"同构"从群升级为拓扑群）；第二步证明 $$\mathbb{RP}^3$$ 就是 $$S^3/\{\pm 1\}$$——每一条过原点的直线恰好穿过球面两次，穿过的两个点是反向的。

*证明*：由定理 3.5 与 3.6，$$\rho:S^3\to SO(3)$$ 是连续满同态，由定理 3.7，$$\ker\rho=\{\pm1\}$$。群同态基本定理给出群同构 $$\bar\rho:S^3/\{\pm1\}\to SO(3)$$。这是连续双射；$$S^3$$ 紧致，故商 $$S^3/\{\pm1\}$$ 紧致，而 $$SO(3)$$ 作为 $$\mathbb{R}^9$$ 的闭有界子集是 Hausdorff 紧空间；紧空间之间的连续双射是同胚。于是 $$\bar\rho$$ 是同胚，也就是拓扑群同构。

再证 $$\mathbb{RP}^3\cong S^3/\{\pm1\}$$。记 $$\mathbb{R}^4\setminus\{0\}$$ 中过原点的直线全体为 $$\mathbb{RP}^3$$。每条直线 $$\ell$$ 与单位球面 $$S^3$$ 恰好交于两点：取 $$\ell$$ 上任意非零 $$v$$，则 $$\pm v/\lvert v\rvert$$ 是两个交点，且它们是 $$\ell\cap S^3$$ 的全部（若 $$\lvert x\rvert=\lvert y\rvert=1$$ 且 $$x,y$$ 在同一直线上，则 $$x=\pm y$$）。于是映射

$$\ell\ \longmapsto\ \{q,-q\}=\ell\cap S^3$$

是 $$\mathbb{RP}^3\to S^3/\{\pm1\}$$ 的连续双射，紧空间之间故为同胚。合并两步即得结论。$$\blacksquare$$

**这条同构的读法**（与入口题 (c) 对照）：定理 3.6 说每个旋转都得到，定理 3.7 说每个旋转得到**两次**。所以 $$SO(3)$$ 是 $$S^3$$ 的"两倍"。但这"两倍"不是把 $$S^3$$ 放大成两个球面——它是把 $$S^3$$ 沿着 $$q\leftrightarrow-q$$ 这层自由对合**折叠**起来。折完之后，$$S^3$$ 上两个不同的点 $$q,-q$$ 变成了 $$SO(3)$$ 的同一个点，这就是"多出一层"的精确含义。

### 3.7 「转 360° 不是恒等、转 720° 才是」的严格表述

入口题 (a)(b) 现在可以彻底清算了。先精确说明"提升"是什么意思。

**定理 3.9（$$\rho$$ 是覆叠映射）** $$\rho:S^3\to SO(3)$$ 是**覆叠映射 (covering map)**，其覆叠变换群是 $$\mathbb{Z}/2=\{1,-1\}$$（即 $$\rho(q)=\rho(-q)$$，且这两点局部上是 $$\rho^{-1}\big(\rho(q)\big)$$ 的全部）。

*证明思路*：$$\rho$$ 是"折叠对径点"的商映射，除这一处折叠外处处可逆。最省力的做法是**用群结构**：一个群同态只要在单位元处"无穷小可逆"，左平移就把这件事搬到每一点；再配合纤维恰有两点（定理 3.7）即得覆叠。单位元处的无穷小可逆性用定理 3.6 已经算出的显式公式直接核验。

*证明*：先核验纤维，这是定理 3.7 已给的：$$\rho(q)=\rho(q')\iff q'=\pm q$$，且 $$q\neq-q$$，所以每条纤维恰含两个点。

再核验"无穷小可逆"。由定理 3.6 的计算，对单位向量 $$n$$ 与角 $$\theta$$，

$$\rho\Big(\cos\tfrac\theta2+n\sin\tfrac\theta2\Big)=\text{绕 }n\text{ 转 }\theta .$$

取 $$n=i$$、$$\theta=2t$$，得 $$\rho(\cos t+i\sin t)=$$ 绕 $$i$$ 轴转 $$2t$$ 的旋转。把这条曲线在 $$t=0$$ 处逐项求导（旋转矩阵的元是 $$t$$ 的光滑函数，逐元求导即可）：

$$\frac{d}{dt}\Bigr\rvert_{t=0}\rho(\cos t+i\sin t)=\begin{bmatrix}0&0&0\\0&0&-2\\0&2&0\end{bmatrix}\in\mathfrak{so}(3),$$

一个非零的反对称矩阵。对 $$n=j$$、$$n=k$$ 同理（把 $$i\to j\to k\to i$$ 轮换，定理 3.1 的乘法表在轮换下不变，而 $$\rho$$ 完全由乘法表决定），得到另外两个非零反对称矩阵。这三个矩阵线性无关（它们分别是绕三根坐标轴的无穷小旋转，非零元落在不同的位置）。所以 $$\rho$$ 在单位元处的"求导"把 $$\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$$ 的一组基送到 $$\mathfrak{so}(3)$$ 的线性无关三元组，从而是线性同构。（切映射的正式定义见第 54 章；本章只用"逐项求导"这个具体操作。）

最后从单位元推广到任意点。$$\rho$$ 是群同态，故有恒等式 $$\rho\circ L_q=L_{\rho(q)}\circ\rho$$（$$L$$ 表示左乘）。两边在单位元处求导，得

$$d\rho_q=(dL_{\rho(q)})_1\circ d\rho_1\circ (dL_q)_1^{-1},$$

即"$$\rho$$ 在 $$q$$ 处的可逆性"由"$$\rho$$ 在 $$1$$ 处的可逆性"经左右乘固定元素（它们都是微分同胚，可逆）换算得到。单位元处已可逆，故 $$\rho$$ 处处是局部微分同胚；一个有局部逆的光滑映射配上每点纤维恰两点，就是覆叠映射，覆叠变换群为将 $$q$$ 送到 $$-q$$ 的 $$\mathbb{Z}/2$$。$$\blacksquare$$

（若不想用"切映射"这套语言，这里还有一条纯拓扑的退路：由定理 3.6 的显式公式，对每条坐标轴方向的旋转都写得出局部逆——给定"绕 $$i$$ 转小角 $$2t$$"解出 $$q=\cos t+i\sin t$$，且 $$t\mapsto q$$ 光滑；三根轴拼起来覆盖 $$SO(3)$$ 的一个单位邻域，再用群乘法平移到任意点，即得局部平凡化。这条退路与上面的切映射论证是同一件事的两种写法。）

现在给出本章的正题。

**定理 3.10（转 360° 与转 720°）** 对 $$t\in[0,1]$$ 记

$$q(t):=\cos(\pi t)+k\sin(\pi t)\in S^3,\qquad \gamma(t):=\rho\big(q(t)\big)\in SO(3).$$

于是 $$\gamma$$ 是"绕 $$k$$ 轴转 $$2\pi t$$"，$$q$$ 是它的一条提升。

(i) $$\gamma$$ 是 $$SO(3)$$ 中基点为 $$I$$ 的闭路，但**它不是零伦的**（不能连续收缩为常值回路）。等价地：**"转一整圈"不等于"停在原地"**。

(ii) 把 $$\gamma$$ 与自身首尾相接得到 $$\gamma^2$$（绕 $$k$$ 转 $$4\pi t$$）。$$\gamma^2$$ 是**零伦的**：它可以连续收缩为常值回路。这就是"转两整圈回到自己"。

(iii) 因此 $$\pi_1\big(SO(3),I\big)\cong\mathbb{Z}/2$$，非平凡元是 $$[\gamma]$$。

*证明思路*：全部用覆叠空间的两条基本性质——**道路提升**与**同伦提升**。要点是：闭路的提升**未必**是闭路；而闭路零伦 $$\iff$$ 它的提升（自基点起）回到同一基点。

*证明*：(i) 提升的显式计算。由定理 3.6 中已经算过的结论（取 $$n=k,\ \theta=2\pi t$$），$$\rho\big(\cos(\pi t)+k\sin(\pi t)\big)$$ 是绕 $$k$$ 转 $$2\pi t$$ 的旋转，故 $$\gamma(t)=\rho(q(t))$$，且 $$\gamma(0)=\gamma(1)=I$$，是闭路。

断言它非零伦。反设存在连续 $$H:[0,1]\times[0,1]\to SO(3)$$ 使

$$H(t,0)=\gamma(t),\qquad H(t,1)=I,\qquad H(0,s)=H(1,s)=I\quad(\forall t,s).$$

由定理 3.9，$$\rho$$ 是覆叠映射，满足**同伦提升性质**。由**道路提升**，$$\gamma$$ 有唯一提升 $$\tilde\gamma$$ 使 $$\tilde\gamma(0)=1$$；而 $$q(t)$$ 是一条满足 $$\rho(q(t))=\gamma(t)$$、$$q(0)=1$$ 的道路，故

$$\tilde\gamma(t)=q(t),\qquad \tilde\gamma(1)=q(1)=\cos\pi+k\sin\pi=-1 .$$

（这里用到 $$\rho\circ q=\gamma$$ 与提升唯一性。）由同伦提升性质，$$H$$ 提升为 $$\tilde H:[0,1]\times[0,1]\to S^3$$ 使 $$\rho\circ\tilde H=H$$ 且 $$\tilde H(t,0)=q(t)$$。

对每个固定的 $$s$$，$$t\mapsto\tilde H(t,s)$$ 是闭路 $$H(\cdot,s)$$ 的提升；其起点 $$\tilde H(0,s)$$ 满足 $$\rho\big(\tilde H(0,s)\big)=H(0,s)=I$$，故 $$\tilde H(0,s)\in\{1,-1\}$$。函数 $$s\mapsto\tilde H(0,s)$$ 连续，取值在离散集 $$\{1,-1\}$$ 中，故为常数；在 $$s=0$$ 处它等于 $$\tilde H(0,0)=q(0)=1$$，所以 $$\tilde H(0,s)\equiv1$$。

同理 $$s\mapsto\tilde H(1,s)$$ 连续且取值在 $$\rho^{-1}(I)=\{1,-1\}$$ 中，故为常数。在 $$s=0$$ 处该常数为 $$\tilde H(1,0)=q(1)=-1$$。但 $$H(\cdot,1)$$ 是常值回路 $$\equiv I$$，其从 $$1$$ 出发的提升必是常值 $$1$$，故 $$\tilde H(1,1)=1$$。同一常量既等于 $$-1$$ 又等于 $$1$$，矛盾。所以 $$\gamma$$ 非零伦。

(ii) 先写出 $$\gamma^2$$。首尾相接的闭路 $$\gamma^2$$ 在参数下等于"绕 $$k$$ 转 $$4\pi t$$"，即

$$\gamma^2(t)=\rho\big(q_2(t)\big),\qquad q_2(t):=\cos(2\pi t)+k\sin(2\pi t),\quad t\in[0,1] .$$

（验证：$$t\le\frac12$$ 时 $$\gamma^2(t)=\gamma(2t)$$ 是转 $$4\pi t$$；$$t\ge\frac12$$ 时 $$\gamma^2(t)=\gamma(2t-1)$$ 是先转 $$2\pi$$ 再转 $$2\pi(2t-1)$$，合计 $$4\pi t$$。两端在 $$t=\frac12$$ 处都给出转 $$2\pi=I$$，连续。）注意 $$q_2(0)=1$$、$$q_2(1)=\cos2\pi+k\sin2\pi=1$$，所以 $$q_2$$ 是 $$S^3$$ 中基点为 $$1$$ 的**闭路**。

$$q_2$$ 零伦：由第 16 章，$$S^3$$ 单连通，即 $$\pi_1(S^3,1)=0$$。故存在连续 $$Q:[0,1]\times[0,1]\to S^3$$ 使

$$Q(t,0)=q_2(t),\qquad Q(t,1)=1,\qquad Q(0,s)=Q(1,s)=1 .$$

令 $$G:=\rho\circ Q$$。则

$$G(t,0)=\rho(q_2(t))=\gamma^2(t),\qquad G(t,1)=\rho(1)=I,\qquad G(0,s)=G(1,s)=\rho(1)=I,$$

即 $$G$$ 是 $$\gamma^2$$ 到常值回路的零伦。故 $$\gamma^2$$ 零伦。

(iii) 已证 $$[\gamma]\neq1$$、$$[\gamma]^2=[\gamma^2]=1$$，所以 $$\pi_1(SO(3),I)$$ 含有二阶元。再看它没有别的：由定理 3.9，$$\rho:S^3\to SO(3)$$ 是覆叠映射而 $$S^3$$ 单连通，故它是**万有覆叠 (universal cover)**，由覆叠空间理论（覆叠变换群 $$\cong$$ 基本群，当底空间的覆叠为万有覆叠时）得

$$\pi_1\big(SO(3),I\big)\cong\{\pm1\}\cong\mathbb{Z}/2 .$$

（这一步的覆叠空间理论一般形式属于第 50 章的取材范围；本章只用它的结论，且 (i)(ii) 已经把结论的两个具体内容——"$$\gamma$$ 绕不过去"与"$$\gamma^2$$ 绕得过去"——各证了一遍。）$$\blacksquare$$

**把定理 3.10 说人话。**

- $$\gamma$$ 是一条**非零伦闭路**：从单位旋转开始，连续地"绕 $$k$$ 轴转一整圈"回到单位旋转，但这个"回来"不是把出发时的状态原样带回来——它的提升从 $$1$$ 走到了 $$-1$$。所以你没法把"转过一整圈"这件事连续地抹掉。
- $$\gamma^2$$（转两整圈）**零伦**：提升从 $$1$$ 出发回到 $$1$$，这是 $$S^3$$ 中一条真正的闭路，而 $$S^3$$ 里没有洞，它缩得掉。
- 这正是皮带实验：手腕转一整圈，带子上的扭结解不开（除非你把手腕跟着倒回去）；手腕转两整圈，带子在自己的"肚子里"滑一圈就解开了。

**与第 50 章的接口**：第 50 章把 "$$SO(3)$$ 的拓扑" 提成了一个待办；本章把它算清楚了——$$\pi_1=\mathbb{Z}/2$$、万有覆叠是 $$S^3$$、覆叠的层数 $$2$$。第 54 章会把这个**整体**信息换成**无穷小**信息：对 $$\rho$$ 在单位元处求导，四元数上"转 $$\theta$$ 的一半"会显形为 $$\mathfrak{so}(3)\cong\mathbb{R}^3$$ 与四元数切空间之间的一个因子 $$2$$。

## 四、几何与物理直觉 (Intuition)

### 4.1 旋转的空间是一个"对径粘合的实心球"

三维旋转由**轴**与**角**两个数据决定。轴是 $$\mathbb{R}^3$$ 中的一条**无向直线**，角在 $$[0,\pi]$$ 里取（大于 $$\pi$$ 的转角可以改用它反向轴的补角，是一样的旋转）。于是可以这样画所有旋转：

> 取 $$\mathbb{R}^3$$ 中半径为 $$\pi$$ 的**闭实心球**。球内每一点 $$p$$ 代表一个旋转：从球心指向 $$p$$ 的方向是**转轴**，$$\lvert p\rvert$$ 是**转角**（单位长度对应 $$1$$ 弧度）。球心代表恒等（转角 $$0$$）。

这个模型几乎是双射，只有边界多余了一点：球面上的点 $$p$$（$$\lvert p\rvert=\pi$$）与对径点 $$-p$$ 代表同一个旋转——绕同一直线的两个相反方向各转 $$\pi$$，效果完全相同。球心那个"退化"点不参与这个粘合（$$p=0$$ 时 $$-p=p$$）。因此

$$SO(3)\ \cong\ \big(\text{半径 }\pi\text{ 的闭球}\big)\big/\ (p\sim-p\ \text{当}\ \lvert p\rvert=\pi),\ \text{且}\ 0\ \text{不动}.$$

这就是 $$\mathbb{RP}^3$$ 的实心球模型（练习里会让你把它与推论 3.8 的 $$S^3/\{\pm1\}$$ 对起来）。它与四元数模型的区别很直观：

- **实心球模型**：每个旋转**一个**点，但边界被粘合，拓扑不平凡；
- **$$S^3$$ 模型**：每个旋转**两个**点（$$q$$ 与 $$-q$$），但 $$S^3$$ 本身是简单的球面，没有粘合。

两种模型各有各的"贵"：前者牺牲了局部干净（要粘合），后者牺牲了唯一性（多出一层）。定理 3.6、3.7 与推论 3.8 说的就是这两笔账之间的换算率是 $$2:1$$。

### 4.2 与第 04 章的对照：一维圆到三维球面

第 04 章的 $$SO(2)\cong S^1$$ 与本章的 $$SU(2)\cong S^3$$ 是同一句话在两个维度上的两次落地。把两处放在一起看，差别一目了然：

| | 平面（第 04 章） | 空间（本章） |
|---|---|---|
| 旋转群 | $$SO(2)$$ | $$SO(3)$$ |
| "旋转全体"的模型 | 圆 $$S^1$$ | 球面 $$S^3$$ |
| 一一对应？ | 是（$$SO(2)\cong S^1$$） | 否（二对一，$$SO(3)\cong S^3/\{\pm1\}$$） |
| 万有覆叠 | $$\mathbb{R}\to S^1$$ | $$S^3\to SO(3)$$ |
| 基本群 | $$\pi_1(S^1)=\mathbb{Z}$$ | $$\pi_1(SO(3))=\mathbb{Z}/2$$ |
| 覆叠层数 | 无穷（$$\mathbb{R}$$ 卷成圆） | 两层（$$S^3$$ 折成 $$\mathbb{RP}^3$$） |
| 多值性表现 | 幅角定到模 $$2\pi$$ | 同一旋转有两个四元数 $$q,-q$$ |

一句话概括这一行的升级：平面旋转的"多值性"是**无穷重**的（转角可以差任意个 $$2\pi$$），所以 $$\mathbb{R}$$ 要卷无穷多圈才绕回自己；空间旋转的"多值性"只有**两重**，因为绕一根轴转 $$2\pi$$ 虽然回到了同一个旋转，但四元数只走了一半，得转 $$4\pi$$（走两圈）才回到起点。这就是为什么 $$\mathbb{Z}$$ 掉到了 $$\mathbb{Z}/2$$。

### 4.3 物理：自旋 $$1/2$$、中子干涉与皮带戏法

量子力学把 $$\pi_1(SO(3))=\mathbb{Z}/2$$ 从"数学趣闻"变成了可测量的预言。一个自旋 $$1/2$$ 的粒子的**态**不是由 $$SO(3)$$ 的旋转来变换的，而是由它的二重覆盖 $$SU(2)$$ 来变换的：对空间旋转 $$\rho(q)$$，态的变换是乘以 $$q$$（在某个表示里）。这意味着

> 把一个自旋 $$1/2$$ 的粒子**绕任意轴空间旋转 $$2\pi$$**，它的波函数变成**原来的负号**；再转 $$2\pi$$（共 $$4\pi$$）才完全复原。

"变成负号"是可观测的：把一束自旋 $$1/2$$ 的粒子（例如中子）分成两束，让其中一束经历转角为 $$\theta$$ 的自旋旋转、另一束不动，则两束的相位差是 $$\frac\theta2$$ 而不是 $$\theta$$（这正是半角在起作用）。于是干涉强度随 $$\theta$$ **以 $$4\pi$$ 为周期**变化：$$\theta=2\pi$$ 时相位差为 $$\pi$$，出现相消干涉——**"转一整圈"在干涉图样上留下了实实在在的痕迹**；要到 $$\theta=4\pi$$ 才完全复原。中子干涉实验（1975 年，Rauch 等人）测到的正是这个 $$4\pi$$ 周期和 $$\theta=2\pi$$ 处的相消，直接"看见"了 $$\pi_1(SO(3))=\mathbb{Z}/2$$。**这是把纯拓扑当作物理量测出来的著名例子**，也是本课"几何 $$\leftrightarrow$$ 代数 $$\leftrightarrow$$ 物理"这条主线在 Lie 群一章的最强回响。

皮带戏法是同一个定理在宏观世界的版本，不需要量子力学：手腕转 $$2\pi$$，手与手臂的相对姿态复原了，但带子上的扭结还在（$$\gamma$$ 非零伦）；手腕转 $$4\pi$$，带子可以在自己身上滑一圈把扭结消掉（$$\gamma^2$$ 零伦）。**"绕了两圈的信息"藏在了带子里，正如它藏在自旋态的符号里。**

物理要的一般原则是：**当群的拓扑不平凡时，它的"表示"可能必须允许相差一个相位或符号——这就是射影表示**。本章给出的是最小的例子（$$\mathbb{Z}/2$$），第 60 章会把这件事一般化，并给出射影表示与"覆盖群的真表示"之间的一一对应。

### 4.4 一条必须记住的几何事实

$$\rho(q)$$ 保持**轴**不动这件事，在四元数语言里只有一行：$$q=\cos\frac\theta2+\sin\frac\theta2 n$$ 与 $$n$$ 可交换（因为 $$n^2=-1$$），于是 $$\rho(q)n=q n q^{-1}=n$$。一般地，$$\rho(q)$$ 的不动点集就是 $$q$$ 的虚部（作为轴）张成的那条直线——**旋转的轴，就是对应四元数的虚部方向**。这个观察让"由 $$q$$ 读出旋转轴与转角"变成两步计算：

$$n=\frac{\operatorname{Im}q}{\lvert\operatorname{Im}q\rvert},\qquad \theta=2\arctan\frac{\lvert\operatorname{Im}q\rvert}{\operatorname{Re}q}\quad(\operatorname{Re}q>0\ \text{时}).$$

因子 $$2$$ 与 $$\arctan$$ 的出现，都是"$$q$$ 只走半角"的直接后果。

## 五、经典问题精讲 (Classical Problems)

### 题 1：由四元数写旋转矩阵（四元数版 Rodrigues 公式）

**考点**：定理 3.5 中 $$\rho(q)x=qxq^*$$ 的显式化；四元数乘法与点积、叉积的桥梁公式。**在本章结构里的位置**：3.5 节的具体化，也是后面所有"从 $$q$$ 读出旋转"的计算基础。

**题目**：设 $$q=w+xi+yj+zk\in S^3$$。求 $$\rho(q)$$ 在基 $$(i,j,k)$$ 下的矩阵 $$R(q)$$。

**解**：先用纯虚元乘积公式化简。对纯虚元 $$u$$（可等同于 $$\mathbb{R}^3$$ 中的向量），

$$q\,u\,q^*=(w^{2}-\lvert v\rvert^{2})u+2\langle v,u\rangle v+2w\,(v\times u),\qquad v:=(x,y,z) .$$

*这个公式的来历*：把 $$q=w+v$$、$$q^*=w-v$$ 展开，

$$q u q^*=(wu+vu)(w-v)=w^{2}u-wuv+wvu-vuv .$$

逐项处理。由 $$uv=-\langle u,v\rangle+u\times v$$ 得

$$-wuv=w\langle u,v\rangle-w\,(u\times v),\qquad wvu=-w\langle u,v\rangle+w\,(v\times u),$$

两项相加为 $$2w(v\times u)$$（用了 $$u\times v=-v\times u$$）。又

$$vuv=v\big({-\langle u,v\rangle+u\times v}\big)=-\langle u,v\rangle v+v(u\times v)=-\langle u,v\rangle v+\Big(u\lvert v\rvert^{2}-v\langle v,u\rangle\Big)=2\langle u,v\rangle v-\lvert v\rvert^{2}u,$$

其中用了 $$\langle u,v\rangle=\langle v,u\rangle$$、$$v\cdot(u\times v)=0$$，以及三重积公式 $$v\times(u\times v)=u\lvert v\rvert^{2}-v\langle v,u\rangle$$。合并三项即得公式。$$\square$$

现在取 $$u=e_1=i$$。由 $$v\times i=(x,y,z)\times(1,0,0)=(0,z,-y)$$：

$$\rho(q)i=(w^{2}-x^{2}-y^{2}-z^{2}+2x^{2})i+2z\,j-2y\,k
=\big(1-2(y^{2}+z^{2})\big)i+2(xy+wz)j+2(xz-wy)k,$$

末一步用了 $$w^{2}+x^{2}+y^{2}+z^{2}=1$$ 与 $$(w^{2}-x^{2}-y^{2}-z^{2}+2x^{2})=(1-2y^{2}-2z^{2})$$。这是 $$R(q)$$ 的**第一列**。

同法，取 $$u=j$$（此时 $$v\times j=(-z,0,x)$$）：

$$\rho(q)j=2(xy-wz)i+\big(1-2(x^{2}+z^{2})\big)j+2(yz+wx)k .$$

取 $$u=k$$（此时 $$v\times k=(y,-x,0)$$）：

$$\rho(q)k=2(xz+wy)i+2(yz-wx)j+\big(1-2(x^{2}+y^{2})\big)k .$$

把这三列排好：

$$R(q)=\begin{bmatrix}
1-2(y^{2}+z^{2}) & 2(xy-wz) & 2(xz+wy)\\
2(xy+wz) & 1-2(x^{2}+z^{2}) & 2(yz-wx)\\
2(xz-wy) & 2(yz+wx) & 1-2(x^{2}+y^{2})
\end{bmatrix}.$$

**自检**（三个必查的极端值）：$$q=i$$（$$w=0,x=1$$）给出 $$\operatorname{diag}(1,-1,-1)$$，即绕 $$i$$ 转 $$\pi$$，对；$$q=1$$ 给出 $$I_3$$，对；$$q=\cos\frac\theta2+k\sin\frac\theta2$$ 给出 $$\begin{bmatrix}\cos\theta&-\sin\theta&0\\ \sin\theta&\cos\theta&0\\0&0&1\end{bmatrix}$$，即绕 $$k$$ 转 $$\theta$$，对。取迹得

$$\operatorname{tr}R(q)=3-4(x^{2}+y^{2}+z^{2})=4w^{2}-1,$$

这个量只与 $$w$$ 有关——它是后面题 5 的关键。$$\blacksquare$$

### 题 2：从旋转矩阵反解四元数

**考点**：二重覆盖的"计算后果"——反解时必然出现"选哪一支"；定理 3.7 的算法版。**在本章结构里的位置**：3.6 节在工程计算中的形象。

**题目**：给定 $$R\in SO(3)$$ 且 $$\operatorname{tr}R\neq-1$$，求所有 $$q\in S^3$$ 使 $$R(q)=R$$。

**解**：由题 1，$$\operatorname{tr}R=4w^{2}-1$$，故

$$w=\pm\frac12\sqrt{1+\operatorname{tr}R}.$$

$$w$$ 的符号待定（这正是二重覆盖）。又由题 1 的矩阵，非对角元之差给出

$$R_{32}-R_{23}=4wx,\qquad R_{13}-R_{31}=4wy,\qquad R_{21}-R_{12}=4wz .$$

（逐项相减即可验证，例如 $$R_{32}=2(yz+wx)$$、$$R_{23}=2(yz-wx)$$。）于是当 $$w\neq0$$——

$$x=\frac{R_{32}-R_{23}}{4w},\qquad y=\frac{R_{13}-R_{31}}{4w},\qquad z=\frac{R_{21}-R_{12}}{4w}.$$

先取 $$w=+\frac12\sqrt{1+\operatorname{tr}R}$$ 得到一支解 $$q_+=(w,x,y,z)$$；另一支解就是 $$q_-=-q_+$$（定理 3.7）。**验证公式给出的确实是解**：由定理 3.6，$$R$$ 有某个 $$q_0=(w_0,x_0,y_0,z_0)\in S^3$$ 使 $$R(q_0)=R$$。由题 1 的迹公式，$$\operatorname{tr}R=4w_0^{2}-1$$，所以 $$\sqrt{1+\operatorname{tr}R}=2\lvert w_0\rvert$$，从而 $$w=\pm w_0$$——注意 $$\operatorname{tr}R\neq-1$$ 恰好保证 $$w_0\neq0$$（否则 $$4w_0^2-1=-1$$），分母不为零。对 $$w=w_0$$ 那一支，由 $$R_{32}-R_{23}=4w_0x_0$$ 得 $$x=\dfrac{4w_0x_0}{4w_0}=x_0$$，同理 $$y=y_0$$、$$z=z_0$$，于是 $$q_+=q_0\in S^3$$ 且 $$R(q_+)=R$$；取 $$w=-w_0$$ 则得 $$q_-=-q_+=(-w_0,-x_0,-y_0,-z_0)$$。所以这两支就是全部解（定理 3.7 说至多两支）。

**退化情形**：$$\operatorname{tr}R=-1$$，即 $$w=0$$（转角 $$\pi$$）。此时上面三个式子的分母为 $$0$$，公式失效；但从题 1 的对角元读出

$$x^{2}=\frac{1+R_{11}}{2},\qquad y^{2}=\frac{1+R_{22}}{2},\qquad z^{2}=\frac{1+R_{33}}{2},$$

符号由非对角元的一致性（$$R_{12}=2xy$$ 等）定出，仍然恰好两支解。

**结论**：反解总有两支，且它们相差一个整体符号——这就是"用四元数做姿态插值时必须先选定一支（例如强制 $$w\ge0$$）"这句话的数学内容。若不选，插值会在某处突然反向：因为 $$q$$ 与 $$-q$$ 在 $$S^3$$ 里是对径的**远**点，而在 $$SO(3)$$ 里是同一点。$$\blacksquare$$

### 题 3：旋转的空间是"对径粘合的实心球"

**考点**：推论 3.8 的球模型版本。**在本章结构里的位置**：4.1 节直觉的严格化，也是"轴-角"参数化的拓扑代价。

**题目**：设 $$B=\{\,p\in\mathbb{R}^3:\lvert p\rvert\le\pi\,\}$$，在 $$B$$ 上定义等价关系：当 $$\lvert p\rvert=\pi$$ 时令 $$p\sim-p$$，其余点只与自己等价。证明 $$B/{\sim}\ \cong\ SO(3)$$。

**解**：构造函数 $$\Psi:B/{\sim}\to SO(3)$$。

- 对 $$p\in B$$，$$p\neq0$$：令 $$n=p/\lvert p\rvert$$，$$\theta=\lvert p\rvert$$，把 $$p$$ 送到"绕 $$n$$ 转 $$\theta$$"的旋转。
- $$\Psi(0)=I$$。

**良定义**：若 $$p\neq0$$ 且 $$p\sim -p$$，则 $$\lvert p\rvert=\pi$$。"绕 $$n$$ 转 $$\pi$$"与"绕 $$-n$$ 转 $$\pi$$"是同一个旋转（把 $$n$$ 换成 $$-n$$，转角 $$\pi$$ 换成 $$-\pi$$，在模 $$2\pi$$ 下是同一元素；也可直接算：绕 $$-n$$ 的 Rodrigues 公式在两个角度上取值相同）。在内部（$$\lvert p\rvert<\pi$$）等价类是单点，无冲突。

**满射**：任给 $$R\in SO(3)$$，由定理 3.6（Euler 定理）存在单位 $$n$$ 与 $$\theta\in[0,2\pi)$$ 使 $$R=$$ 绕 $$n$$ 转 $$\theta$$。若 $$\theta\le\pi$$，取 $$p=\theta n\in B$$，$$\Psi(p)=R$$。若 $$\theta>\pi$$，则 $$\theta':=2\pi-\theta\in(0,\pi)$$；"绕 $$n$$ 转 $$\theta$$"等于"绕 $$-n$$ 转 $$\theta'$$"（绕 $$n$$ 转 $$\theta$$ 与绕 $$n$$ 转 $$\theta-2\pi=-\theta'$$ 是同一个旋转，而绕 $$n$$ 转 $$-\theta'$$ 就是绕 $$-n$$ 转 $$\theta'$$），取 $$p=\theta'(-n)\in B$$，$$\Psi(p)=R$$。

**单射**：设 $$\Psi(p)=\Psi(p')=R\neq I$$。写 $$p=\theta n$$、$$p'=\theta' n'$$，其中 $$\theta=\lvert p\rvert,\ \theta'=\lvert p'\rvert\in(0,\pi]$$，$$n,n'$$ 是单位向量。

**轴唯一**：由定理 3.6 的证明，$$R$$ 的转轴是特征值 $$1$$ 的特征空间；$$R\neq I$$ 时这个特征空间是**一维**的（绕轴转 $$\theta\neq0$$ 在轴上有特征值 $$1$$，在垂直平面上是转 $$\theta$$ 的平面旋转，特征值 $$e^{\pm i\theta}\neq1$$），所以转轴的直线 $$\mathbb{R}n=\mathbb{R}n'$$ 唯一确定，即 $$n'=\pm n$$。

**转角唯一**：在轴的两种定向里选使转角落在 $$(0,\pi]$$ 的那一个，转角随之唯一（$$\theta$$ 与 $$2\pi-\theta$$ 中恰有一个落在 $$(0,\pi]$$）。

分两种情形。若 $$n'=n$$，则 $$\theta'=\theta$$，于是 $$p'=\theta' n'=\theta n=p$$，本就是同一个点。若 $$n'=-n$$，则"绕 $$n$$ 转 $$\theta$$"$$=$$"绕 $$-n$$ 转 $$\theta'$$"，而绕 $$-n$$ 转 $$\theta'$$ 就是绕 $$n$$ 转 $$-\theta'$$（把轴反向等于把角取负），故 $$-\theta'\equiv\theta\pmod{2\pi}$$，即 $$\theta'=2\pi-\theta$$；与 $$0<\theta,\theta'\le\pi$$ 一并看，只能 $$\theta=\theta'=\pi$$（否则 $$\theta'=2\pi-\theta>\pi$$）。于是 $$\lvert p\rvert=\lvert p'\rvert=\pi$$ 且 $$p=-p'$$，即 $$p\sim p'$$。

两情形都给出 $$p\sim p'$$，故 $$\Psi$$ 单射。

$$\Psi$$ 连续（在 $$p\neq0$$ 处由 Rodrigues 公式光滑，在 $$0$$ 处邻域内的旋转都趋于 $$I$$），$$B/{\sim}$$ 紧、$$SO(3)$$ Hausdorff，故 $$\Psi$$ 是同胚：$$B/{\sim}\cong SO(3)$$。

**与 $$\mathbb{RP}^3$$ 的对接**：把球体换成单位球 $$D^3$$ 并把半径方向的坐标当作 $$S^3$$ 的第四坐标，则 $$D^3/{\sim}$$ 就是 $$S^3/\{\pm1\}$$（上半球 $$x_0\ge0$$ 已是每条 $$\pm$$ 对的代表元系，边界 $$x_0=0$$ 的赤道 $$S^2$$ 上才需要粘对径点），也就是 $$\mathbb{RP}^3$$（推论 3.8）。$$\blacksquare$$

### 题 4：二重覆盖不能拆开——不存在连续截面

**考点**：定理 3.10 的直接应用，也是"自旋 $$1/2$$ 不可能是 $$SO(3)$$ 的普通表示"的几何根源。**在本章结构里的位置**：把 3.7 节的拓扑结论转成一句"不可能性"定理。

**题目**：证明不存在连续映射 $$s:SO(3)\to S^3$$ 使 $$\rho\circ s=\operatorname{id}_{SO(3)}$$（这样的 $$s$$ 称为这个覆叠的一个**连续截面 (continuous section)**）。

**解**：反设这样的 $$s$$ 存在。取定理 3.10 中的闭路

$$\gamma(t)=\rho\big(\cos(\pi t)+k\sin(\pi t)\big),\qquad 0\le t\le1,\qquad \gamma(0)=\gamma(1)=I .$$

**第一步**：$$s\circ\gamma$$ 是 $$S^3$$ 中的闭路。因为 $$\gamma(0)=\gamma(1)=I$$，且 $$s(I)$$ 是一个固定点，所以

$$s(\gamma(0))=s(\gamma(1))=s(I),$$

即 $$s\circ\gamma$$ 是以 $$s(I)$$ 为基点的闭路。

**第二步**：$$s\circ\gamma$$ 是 $$\gamma$$ 的提升。由 $$\rho\circ s=\operatorname{id}$$ 得

$$\rho\big(s(\gamma(t))\big)=\gamma(t)\qquad(\forall t).$$

所以 $$s\circ\gamma$$ 是一条满足 $$\rho\circ(s\circ\gamma)=\gamma$$ 的道路，即 $$\gamma$$ 的一条提升。

**第三步**：由定理 3.9（覆叠）道路提升唯一。$$\gamma$$ 从 $$s(I)$$ 出发的提升只有一条，就是 $$s\circ\gamma$$；另一方面，从 $$s(I)$$ 出发我们也可以直接把定理 3.10 里的 $$q(t)$$ 改写：设 $$s(I)=q_0\in\{1,-1\}$$，则 $$t\mapsto q_0 q(t)$$ 也是 $$\gamma$$ 的一条提升（因为 $$\rho(q_0 q)=\rho(q_0)\rho(q)=\rho(q)$$，且 $$(q_0q)(0)=q_0$$）。由唯一性，

$$s\circ\gamma=q_0\cdot q .$$

但由定理 3.10(i)（或直接算）$$q(1)=-1$$，故 $$s(\gamma(1))=q_0\cdot(-1)\neq q_0=s(\gamma(0))$$，与 $$s\circ\gamma$$ 是闭路（第一步）矛盾。故 $$s$$ 不存在。$$\blacksquare$$

**这条不可能性说明什么**：二重覆盖 $$S^3\to SO(3)$$ **不能**在"连续"的意义下拆开——你没法在所有旋转上一致地、连续地选出 $$q$$ 而不是 $$-q$$。这就是量子力学里"$$SO(3)$$ 的表示只能出现整数自旋、半整数自旋必须允许相差一个符号"的几何原因；第 60 章 的射影表示会把这句话提升为一条一般定理。

### 题 5：共轭类只由转角决定

**考点**：题 1 的迹公式 + 定理 3.6 的轴角唯一性。**在本章结构里的位置**：$$SO(3)$$ 的共轭类，是第 56 章"紧 Lie 群的表示由极大环面与特征标决定"的最小组件。

**题目**：设 $$R,R'\in SO(3)$$。证明：存在 $$S\in SO(3)$$ 使 $$R'=SRS^{-1}$$，当且仅当 $$\operatorname{tr}R=\operatorname{tr}R'$$。

**解**：**必要性**。迹在相似变换下不变：$$\operatorname{tr}(SRS^{-1})=\operatorname{tr}(RSS^{-1})=\operatorname{tr}R$$。

**充分性**。先说明 $$\operatorname{tr}R$$ 决定转角。由定理 3.6 写 $$R=\rho(q)$$，$$q=\cos\frac\theta2+n\sin\frac\theta2$$，取 $$\theta\in[0,\pi]$$（转轴定向与转角一并选取，使角落在这一区间；题 3 的单射性证明说明了这种取法唯一）。由题 1 的迹公式，

$$\operatorname{tr}R=4w^{2}-1=4\cos^{2}\frac\theta2-1=1+2\cos\theta ,$$

（末一步用 $$\cos\theta=2\cos^{2}\frac\theta2-1$$），故 $$\operatorname{tr}R$$ 与 $$\theta\in[0,\pi]$$ 一一对应。

现设 $$\operatorname{tr}R=\operatorname{tr}R'$$，则两者转角同为 $$\theta$$。设转轴分别为单位向量 $$n,n'$$。取 $$S\in SO(3)$$ 使 $$Sn=n'$$：这样的 $$S$$ 存在，因为把 $$n$$ 与 $$n'$$ 各自扩充成**右手**标准正交基 $$(n,u,w)$$、$$(n',u',w')$$ 后，令 $$S$$ 依次把 $$n\mapsto n'$$、$$u\mapsto u'$$、$$w\mapsto w'$$ 即可（它把标准正交基送到标准正交基且保定向，故属于 $$SO(3)$$）。

于是 $$S R S^{-1}$$ 是转角 $$\theta$$、转轴 $$Sn=n'$$ 的旋转。而 $$R'$$ 也是转角 $$\theta$$、转轴 $$n'$$ 的旋转；由定理 3.6（轴角在 $$\theta\in[0,\pi]$$ 时唯一确定旋转），$$SRS^{-1}=R'$$。$$\blacksquare$$

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 设 $$p=1+i$$、$$q=j+k$$。计算 $$pq$$、$$qp$$、$$p^*$$、$$\lvert p\rvert$$、$$p^{-1}$$，并验证 $$\lvert pq\rvert=\lvert p\rvert\lvert q\rvert$$。由此说明 $$\mathbb{H}$$ 不交换。

**基2.** 设 $$q=\dfrac{1+i+j+k}{2}$$。验证 $$q\in S^3$$，求 $$q^*$$、$$q^{-1}$$，写出对应的 $$SU(2)$$ 矩阵 $$\phi(q)$$，并求 $$\rho(q)$$ 的转轴与转角。

**基3.** 只用 $$i^2=j^2=k^2=-1$$ 与 $$ij=k,\ jk=i,\ ki=j$$，推出 $$ji=-k,\ kj=-i,\ ik=-j$$。

**基4.** 证明：当 $$\lvert q\rvert=1$$ 时 $$q^{-1}=q^*$$；并且映射 $$\iota:q\mapsto q^*$$ 是 $$S^3$$ 的对合（$$\iota^2=\operatorname{id}$$），其不动点集恰为 $$\{1,-1\}$$。

### 竞赛（本课目标难度）

**竞1.** 设 $$R$$ 是绕 $$n=\frac{1}{\sqrt3}(1,1,1)$$ 转 $$\frac{2\pi}{3}$$（即把坐标循环置换 $$x\mapsto y\mapsto z\mapsto x$$）的旋转。求**全部** $$q\in S^3$$ 使 $$\rho(q)=R$$。

**竞2.** 求集合 $$\{\,q\in S^3\ :\ q^2=-1\,\}$$，并证明 $$\rho$$ 把它映到「转角为 $$\pi$$ 的旋转全体」，后者同胚于 $$\mathbb{RP}^2$$。

**竞3.** 证明：不存在群同态 $$\phi:SO(3)\to S^3$$ 使 $$\rho\circ\phi=\operatorname{id}_{SO(3)}$$。（注意：这里**不假设** $$\phi$$ 连续。）

**竞4.** 设 $$q_\nu=\cos\frac{\theta_\nu}{2}+n_\nu\sin\frac{\theta_\nu}{2}$$（$$\nu=1,2$$，$$n_\nu$$ 为单位向量）。证明合成旋转 $$q=q_2q_1$$ 的转角 $$\theta$$ 满足

$$\cos\frac\theta2=\cos\frac{\theta_1}{2}\cos\frac{\theta_2}{2}-\sin\frac{\theta_1}{2}\sin\frac{\theta_2}{2}\langle n_1,n_2\rangle,$$

并说明为什么 $$q_2q_1$$ 一般**不是**绕 $$n_1$$ 或 $$n_2$$ 的旋转。

### 研究（通向下一章）

**研1.** 对纯虚的四元数 $$u$$（$$\lvert u\rvert=1$$，即 $$u^2=-1$$）定义 $$\exp(\theta u):=\sum_{m\ge0}\frac{(\theta u)^m}{m!}$$。证明 $$\exp(\theta u)=\cos\theta+u\sin\theta$$，并推出 $$\rho\big(\exp(\theta u)\big)$$ 是绕 $$u$$ 转 $$2\theta$$ 的旋转。解释：为什么这里出现的是 $$2\theta$$（"半角"从哪来）。

**研2.** 设 $$V_\lambda=\operatorname{Sym}^\lambda\mathbb{C}^2$$（$$\lambda\ge0$$）是 $$SU(2)$$ 的不可约复表示（维数 $$\lambda+1$$，即自旋 $$j=\lambda/2$$；分类见第 56 章）。证明：$$V_\lambda$$ 能"下降"为 $$SO(3)$$ 的表示（即存在表示 $$\Pi:SO(3)\to GL(V_\lambda)$$ 使 $$\Pi\circ\rho$$ 就是 $$SU(2)$$ 的作用）当且仅当 $$\lambda$$ 是偶数。并解释 $$\lambda$$ 奇数时 $$V_\lambda$$ 是什么。

### 解答 (Solutions)

**解 基1.** 用乘法表逐项展开。

$$pq=(1+i)(j+k)=j+k+ij+ik=j+k+k+(-j)=2k,$$
$$qp=(j+k)(1+i)=j+ji+k+ki=j+(-k)+k+j=2j .$$

故 $$pq=2k\neq 2j=qp$$。共轭 $$p^*=1-i$$。模 $$\lvert p\rvert=\sqrt{pp^*}=\sqrt{(1+i)(1-i)}=\sqrt{1+1}=\sqrt2$$。逆 $$p^{-1}=p^*/\lvert p\rvert^2=\frac{1-i}{2}$$（验算：$$(1+i)\frac{1-i}{2}=\frac{1+1}{2}=1$$）。

乘性：$$\lvert pq\rvert=\lvert 2k\rvert=\sqrt{4}=2$$，而 $$\lvert p\rvert\lvert q\rvert=\sqrt2\cdot\sqrt2=2$$，相等。$$\blacksquare$$

**解 基2.** $$\lvert q\rvert^2=\frac14(1+1+1+1)=1$$，故 $$q\in S^3$$。$$q^*=\frac{1-i-j-k}{2}$$，且由题 基4（或 $$\lvert q\rvert=1$$）得 $$q^{-1}=q^*$$。

对应 $$SU(2)$$ 矩阵：用 $$\phi(q)=\begin{bmatrix}a&b\\-\bar b&\bar a\end{bmatrix}$$，其中 $$a=x_0-ix_3=\frac{1-i}{2}$$、$$b=-x_2-ix_1=\frac{-1-i}{2}$$，于是

$$\phi(q)=\begin{bmatrix}\dfrac{1-i}{2}&\dfrac{-1-i}{2}\\[2mm] \dfrac{1-i}{2}&\dfrac{1+i}{2}\end{bmatrix}.$$

（自检：$$-\bar b=-\frac{-1+i}{2}=\frac{1-i}{2}$$，$$\bar a=\frac{1+i}{2}$$，两列标准正交，行列式 $$=\lvert a\rvert^2+\lvert b\rvert^2=\frac12+\frac12=1$$，确在 $$SU(2)$$。）

转轴与转角：$$\operatorname{Im}q=\frac12(i+j+k)$$，故轴 $$n=\frac{1}{\sqrt3}(1,1,1)$$；$$\operatorname{Re}q=\frac12=\cos\frac\theta2$$ 得 $$\frac\theta2=\frac\pi3$$，即 $$\theta=\frac{2\pi}{3}$$。所以 $$\rho(q)$$ 是绕 $$(1,1,1)$$ 方向转 $$120^\circ$$——与竞1 是同一个旋转。$$\blacksquare$$

**解 基3.** 关键是把"求逆"变成直接的结合律计算，不预设"逆唯一"（此时还没证明 $$\mathbb{H}$$ 是除环）。先用 $$i^2=j^2=k^2=-1$$ 算出三对乘积：

$$(ij)(ji)=i(jj)i=i(-1)i=-i^2=1,$$
$$(jk)(kj)=j(kk)j=j(-1)j=-j^2=1,$$
$$(ki)(ik)=k(ii)k=k(-1)k=-k^2=1 .$$

第一式说明 $$ji$$ 是 $$ij=k$$ 的右逆。又 $$k\cdot(-k)=-k^2=1$$，即 $$-k$$ 是 $$k$$ 的（双向）逆。用结合律把两者接起来：

$$ji=ji\cdot 1=ji\cdot\big(k\cdot(-k)\big)=(ji\cdot k)\cdot(-k)=\big(ji\cdot(ij)\big)\cdot(-k)=1\cdot(-k)=-k .$$

第二式同法，注意 $$i=jk$$，故 $$kj\cdot i=kj\cdot(jk)=(kj)(jk)=1$$，而 $$i\cdot(-i)=-i^2=1$$：

$$kj=kj\cdot 1=kj\cdot\big(i\cdot(-i)\big)=(kj\cdot i)\cdot(-i)=1\cdot(-i)=-i .$$

第三式同法，注意 $$j=ki$$，故 $$ik\cdot j=ik\cdot(ki)=(ik)(ki)=1$$，而 $$j\cdot(-j)=-j^2=1$$：

$$ik=ik\cdot 1=ik\cdot\big(j\cdot(-j)\big)=(ik\cdot j)\cdot(-j)=1\cdot(-j)=-j .$$

三式即所求。$$\blacksquare$$

三式即所求（$$(ij)^{-1}=j^{-1}i^{-1}$$ 与上面的配对一致，无需额外假设）。$$\blacksquare$$

**解 基4.** 由定理 3.3(ii)，$$qq^*=\lvert q\rvert^2=1$$，故 $$q^{-1}=q^*/\lvert q\rvert^2=q^*$$。

对合：$$\iota(\iota(q))=(q^*)^*=q$$。光滑：$$\iota$$ 在基 $$(1,i,j,k)$$ 上是线性映射 $$\operatorname{diag}(1,-1,-1,-1)$$，当然光滑。

不动点：$$q^*=q\iff x_1i+x_2j+x_3k=-(x_1i+x_2j+x_3k)\iff x_1=x_2=x_3=0$$，即 $$q=x_0$$ 是实数；再由 $$\lvert q\rvert=\lvert x_0\rvert=1$$ 得 $$q=\pm1$$。$$\blacksquare$$

**解 竞1.** **关键 leap**：先把"轴 $$n$$、角 $$\theta$$"翻成四元数公式 $$q_\theta=\cos\frac\theta2+n\sin\frac\theta2$$（定理 3.6），再意识到二重覆盖使答案正好是两个。

由 $$\theta=\frac{2\pi}{3}$$：$$\cos\frac\theta2=\cos\frac\pi3=\frac12$$，$$\sin\frac\theta2=\sin\frac\pi3=\frac{\sqrt3}{2}$$。于是

$$q=\frac12+\frac{1}{\sqrt3}(1,1,1)\cdot\frac{\sqrt3}{2}=\frac{1+i+j+k}{2}.$$

验算它给出 $$R$$（绕 $$(1,1,1)$$ 转 $$120^\circ$$ 即坐标循环置换）：用 §五 题 1 的矩阵公式，$$w=x=y=z=\frac12$$，

$$R_{11}=1-2\Big(\frac14+\frac14\Big)=0,\quad R_{13}=2\Big(\frac14+\frac14\Big)=1,\quad R_{21}=2\Big(\frac14+\frac14\Big)=1,$$

其余元同法，得 $$R=\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix}$$，正是 $$e_1\mapsto e_2\mapsto e_3\mapsto e_1$$ 的循环置换。

由定理 3.7（二重覆盖），$$\rho(q)=\rho(-q)$$，故全部解是

$$q=\pm\frac{1+i+j+k}{2}.\qquad\blacksquare$$

**解 竞2.** 设 $$q=w+v$$（$$v=x i+y j+z k$$ 为虚部）。展开

$$q^2=w^2+2wv+v^2=(w^2-\lvert v\rvert^2)+2wv,$$

其中用了纯虚元的平方 $$v^2=-\lvert v\rvert^2$$（由乘积公式 $$vv=-\langle v,v\rangle+v\times v=-\lvert v\rvert^2$$）。要求 $$q^2=-1$$，即实部虚部分别相等：

$$w^2-\lvert v\rvert^2=-1,\qquad 2wv=0 .$$

第二式（$$v\neq0$$ 时）给出 $$w=0$$；若 $$v=0$$ 则第一式给 $$w^2=-1$$，无实解。故必有 $$w=0$$，再由 $$\lvert q\rvert^2=w^2+\lvert v\rvert^2=1$$ 得 $$\lvert v\rvert=1$$。所以

$$\{\,q\in S^3:q^2=-1\,\}=\{\text{纯虚单位四元数}\}\cong S^2 .$$

它们的像是：$$q=v$$ 是纯虚单位元，可写成 $$q=\cos\frac\pi2+v\sin\frac\pi2$$，由定理 3.6，$$\rho(q)$$ 是**绕 $$v$$ 转 $$\pi$$** 的旋转。由于 $$\rho(q)=\rho(-q)$$，而 $$-v$$ 与 $$v$$ 是 $$S^2$$ 上的对径点，像空间就是

$$S^2/\{\pm1\}=\mathbb{RP}^2\ \subset\ SO(3)=\mathbb{RP}^3 .$$

在题 3 的实心球模型里，这正是"边界球面粘对径点"那一层，即转角恰为 $$\pi$$ 的旋转全体。$$\blacksquare$$

**解 竞3.** **关键 leap**：不要试图构造 $$\phi$$，而是数"阶为 $$2$$ 的元素"——$$SO(3)$$ 有无穷多个，$$S^3$$ 只有一个。

设 $$\phi$$ 是这样的同态。先注意 $$\phi$$ **必是单射**：若 $$\phi(x)=\phi(y)$$，两边作用 $$\rho$$ 得 $$x=(\rho\circ\phi)(x)=(\rho\circ\phi)(y)=y$$。

现在看阶为 $$2$$ 的元素。$$S^3$$ 中满足 $$g^2=1$$ 的元素：由 竞2 的计算（把 $$-1$$ 换成 $$1$$），$$w^2-\lvert v\rvert^2=1$$、$$2wv=0$$、$$w^2+\lvert v\rvert^2=1$$，解得 $$v=0,\ w=\pm1$$，即

$$\{g\in S^3:g^2=1\}=\{1,-1\},$$

故 $$S^3$$ 中唯一的二阶元是 $$-1$$。

而 $$SO(3)$$ 中二阶元有无穷多个：任取单位向量 $$n$$，"绕 $$n$$ 转 $$\pi$$"的旋转 $$R_n$$ 满足 $$R_n^2=I$$ 且 $$R_n\neq I$$（它把 $$n^\perp$$ 上的向量取反），不同的轴给出不同的 $$R_n$$（因为 $$R_n$$ 的不动直线恰是 $$\mathbb{R}n$$）。

对每个这样的 $$R_n$$：$$\phi(R_n)^2=\phi(R_n^2)=\phi(I)=1$$，且由单射 $$\phi(R_n)\neq1$$，故 $$\phi(R_n)=-1$$。于是无穷多个不同的 $$R_n$$ 都被送到同一个 $$-1$$，与 $$\phi$$ 单射矛盾。$$\blacksquare$$

**解 竞4.** 记 $$c_\nu=\cos\frac{\theta_\nu}{2}$$、$$s_\nu=\sin\frac{\theta_\nu}{2}$$。展开

$$q_2q_1=(c_2+s_2n_2)(c_1+s_1n_1)=c_2c_1+c_2s_1n_1+s_2c_1n_2+s_2s_1\,n_2n_1 .$$

用纯虚元乘积公式 $$n_2n_1=-\langle n_2,n_1\rangle+n_2\times n_1$$，其中第二项是纯虚的、第一项是实数：

$$q_2q_1=\underbrace{\big(c_2c_1-s_2s_1\langle n_1,n_2\rangle\big)}_{\text{实部}}+\underbrace{\big(c_2s_1n_1+s_2c_1n_2+s_2s_1\,n_2\times n_1\big)}_{\text{虚部}} .$$

另一方面 $$q=q_2q_1$$ 作为单位四元数总可写成 $$q=\cos\frac\theta2+n\sin\frac\theta2$$（$$\theta\in[0,\pi]$$ 时唯一，见 §五 题 5），故实部就是 $$\cos\frac\theta2$$，即第一式。

**为什么一般不是绕 $$n_1$$ 或 $$n_2$$**：$$q$$ 的虚部里出现了 $$n_2\times n_1$$ 这一项，它一般与 $$n_1,n_2$$ 都不平行。当 $$n_1\perp n_2$$ 时它非零（$$\lvert n_1\times n_2\rvert=1$$），此时转轴由三项合成，既不是 $$n_1$$ 也不是 $$n_2$$——所以"绕固定轴的旋转全体"对复合**不封闭**，$$SO(3)$$ 比 $$SO(2)$$ 复杂的根源就在这里（对比第 04 章：平面旋转的复合还是平面旋转，一条轴管到底）。$$\blacksquare$$

**解 研1.** 思路：$$u^2=-1$$ 使幂次以周期 $$4$$ 循环，按奇偶把级数拆成两半，认出 $$\cos$$ 与 $$\sin$$ 的 Taylor 级数——这与第 04 章 定理 3.6 的 $$\exp(\theta J)=R_\theta$$ 是**同一个计算**，只是把 $$J$$ 换成了 $$u$$。

$$u^{2m}=(-1)^m,\qquad u^{2m+1}=(-1)^m u,$$

于是

$$\exp(\theta u)=\sum_{m\ge0}\frac{\theta^{2m}u^{2m}}{(2m)!}+\sum_{m\ge0}\frac{\theta^{2m+1}u^{2m+1}}{(2m+1)!}
=\sum_{m\ge0}\frac{(-1)^m\theta^{2m}}{(2m)!}+u\sum_{m\ge0}\frac{(-1)^m\theta^{2m+1}}{(2m+1)!}=\cos\theta+u\sin\theta .$$

（级数绝对收敛，可如此重排。）

由定理 3.6，$$\rho\big(\cos\theta+u\sin\theta\big)$$ 是"绕 $$u$$ 转 $$2\theta$$"（把定理 3.6 里的 $$\frac\theta2$$ 换成现在的 $$\theta$$，即 $$\theta_{\text{转}}=2\theta$$）。

**"半角"从哪来**：$$\exp(\theta u)$$ 里的 $$\theta$$ 是四元数侧的参数，而它对应**半个**旋转角。根源是 $$\rho$$ 是二重覆盖下"先作用再折半"：$$\exp(\theta u)$$ 与 $$\exp((\theta+\pi)u)=-\exp(\theta u)$$ 给出**同一个**旋转，所以四元数参数的有效周期是 $$2\pi$$ 而旋转角的周期是 $$4\pi$$——两者的比值 $$2$$ 就是那个 $$\frac12$$。

这与 3.7 节的定理 3.10 是同一件事的无穷小版本：整体上，$$t\mapsto q(t)=e^{\pi t\,k}$$ 在 $$t=1$$ 时给 $$-1$$（走了半个周期）；无穷小地，$$q$$ 的"角速度"是旋转角速度的一半。**把这个计算一般化，就是第 54 章的指数映射**：对一般 Lie 群，$$\exp:\mathfrak{g}\to G$$ 正是这里 $$\theta\mapsto e^{\theta u}$$ 的推广，而"是覆叠还是同构"要看 $$\mathfrak{g}$$ 如何卷绕。第一章的 $$e^{i\theta}$$、第 04 章的 $$e^{\theta J}$$、本章的 $$e^{\theta u}$$ 是同一个定理的三个影子。$$\blacksquare$$

**解 研2.** 设 $$V$$ 是不可约复表示。方法：先看"$$-I$$ 作用是什么"，再用这个标量判断能否下降。

**第一步：$$-I$$ 在不可约表示上必是标量。** $$-I_2=\operatorname{diag}(-1,-1)$$ 是 $$SU(2)$$ 的**中心元**（与每个 $$Q$$ 交换：$$(-I)Q=Q(-I)$$）。故它给出的线性算子与整个 $$SU(2)$$ 作用交换；由 Schur 引理（不可约表示的自同态是标量，第 56 章），$$-I$$ 在 $$V_\lambda$$ 上作用为某个标量 $$\varepsilon_\lambda I$$。

**第二步：标量由最高权空间读出。** 取极大环面 $$T=\{t_\theta=\operatorname{diag}(e^{i\theta},e^{-i\theta})\}\subset SU(2)$$，它是圆的同态像。$$T$$ 交换，故 $$V_\lambda$$ 同时对角化：$$V_\lambda=\bigoplus_\mu (V_\lambda)_\mu$$，$$t_\theta$$ 在 $$(V_\lambda)_\mu$$ 上作用为 $$e^{i\mu\theta}$$。权重 $$\mu$$ 是整数，因为 $$\theta\mapsto t_\theta$$ 是圆到 $$T$$ 的同态、其单值性给出的正是整数（这就是第 04 章 定理 3.10 里 $$\pi_1(S^1)=\mathbb{Z}$$ 的又一次现身）。

对 $$SU(2)$$ 的不可约表示，权重是 $$\mu=\lambda,\lambda-2,\dots,-\lambda$$，最高权空间 $$(V_\lambda)_\lambda$$ 一维（最高权理论，第 56 章）。取 $$t_\theta$$ 中 $$\theta=\pi$$，则 $$t_\pi=\operatorname{diag}(-1,-1)=-I_2$$。它在最高权空间上作用为

$$e^{i\lambda\pi}=(-1)^\lambda .$$

因为 $$-I_2$$ 的作用是标量（第一步），这个值就是 $$\varepsilon_\lambda=(-1)^\lambda$$。

**第三步：下降条件。**

（必要性）设 $$V_\lambda$$ 能下降，即存在表示 $$\Pi:SO(3)\to GL(V_\lambda)$$，使手头的 $$SU(2)$$ 作用 $$\Lambda:SU(2)\to GL(V_\lambda)$$ 恰等于 $$\Pi\circ\rho$$。由定理 3.7，$$\rho(-1)=\rho(1)=I$$，故

$$\Lambda(-I_2)=\Pi\big(\rho(-I_2)\big)=\Pi(I)=\operatorname{id},$$

即 $$\varepsilon_\lambda=1$$，也就是 $$(-1)^\lambda=1$$。

（充分性）反之设 $$\varepsilon_\lambda=1$$，即 $$\Lambda(-I_2)=\operatorname{id}$$。则 $$\Lambda$$ 在核 $$\{\pm I_2\}$$ 上平凡（$$I_2$$ 当然平凡，$$-I_2$$ 由假设），故由群同态基本定理，$$\Lambda$$ 下降为 $$SO(3)\cong SU(2)/\{\pm I_2\}$$ 的表示 $$\Pi$$，且自动满足 $$\Pi\circ\rho=\Lambda$$。

于是

$$V_\lambda\ \text{能下降}\iff (-1)^\lambda=1\iff\lambda\ \text{偶}\iff j=\frac\lambda2\in\mathbb{Z} .$$

$$\lambda=2j$$ 偶对应维数 $$2j+1$$ 的**整数自旋**表示（$$j=0,1,2,\dots$$ 给出维数 $$1,3,5,7,\dots$$，正是球面调和函数 $$l=0,1,2,\dots$$ 的维数）；$$\lambda$$ 奇（半整数自旋 $$j=\frac12,\frac32,\dots$$）时 $$-I_2$$ 作用为 $$-1$$，$$V_\lambda$$ **不能**下降。

**半整数情形是什么**：它仍是 $$SU(2)$$ 的（完全合法的、单值的）表示，但投到 $$SO(3)$$ 后只是"相差一个符号"的表示——即 $$SO(3)$$ 的**射影表示 (projective representation)**。物理上的自旋 $$1/2$$ 电子就活在这里：它的态在 $$SU(2)$$ 上单值，在 $$SO(3)$$ 上只能定义到相差符号。**把"相差一个符号"的表示理论一般化——为什么它总由某个覆盖群的真表示给出、以及如何分类——正是第 60 章的起点。**$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

1. **四元数不是"复数多两个虚数"，是同一个构造的第二步。** 第 02 章从 $$\mathbb{R}$$ 走了一遍"加一个平方为 $$-1$$ 的符号"，得到 $$\mathbb{C}$$；本章对 $$\mathbb{C}$$ 走了第二遍，得到 $$\mathbb{H}$$。唯一的改动是**放弃交换性**（$$jz=\bar zj$$），而正是这个放弃换来了它在 $$\mathbb{R}^3$$ 上的旋转作用。模板的第三步（八元数）会连**结合律**也一起丢掉——书里不再往下走。

2. **单位四元数 $$=S^3=SU(2)$$，它是 $$SO(3)$$ 的二重覆盖。** 每个旋转对应两个四元数 $$q,-q$$（定理 3.7），覆叠层数是 $$2$$。与之对照，第 04 章的平面情形是一一对应（$$SO(2)\cong S^1$$）——"多出一层"是三维才出现的新现象，不是记号问题。

3. **$$\rho(q)x=qxq^*$$ 是本章的心脏。** 它把"轴-角"翻译成"共轭"，把"复合旋转"翻译成"四元数乘法"，把"转轴"翻译成"$$q$$ 的虚部方向"。全部具体计算（Rodrigues 公式、反解四元数、轴角复合）都是它的展开。

4. **"转 360° 不是恒等、转 720° 才是"有精确含义：$$\pi_1(SO(3))=\mathbb{Z}/2$$。** 严格表述是定理 3.10：360° 回路非零伦、其平方零伦；证明靠 $$S^3$$ 单连通 + 覆叠的道路提升与同伦提升。物理版本是中子干涉实验（自旋 $$1/2$$ 转 $$2\pi$$ 变号）与皮带戏法。

5. **$$SO(3)\cong S^3/\{\pm1\}\cong\mathbb{RP}^3$$，并且 $$S^3\to SO(3)$$ 没有连续截面（题 4）。** 这决定了 $$SO(3)$$ 的表示论只能出现整数自旋；半整数自旋是 $$SU(2)$$ 的表示、是 $$SO(3)$$ 的**射影表示**（研究题 2）。这条线在第 60 章变成一般理论。

**下一章悬念**：本章做的全是**整体**的事——覆叠、基本群、二重覆盖。但 $$\rho$$ 在单位元处"取无穷小"时会发生什么？把 $$\rho\big(\cos t+i\sin t\big)$$ 对 $$t$$ 求导（定理 3.9 的证明里已经算过一次），得到的是一批 $$\mathfrak{so}(3)$$ 的反对称矩阵；这些矩阵配上换位子 $$[X,Y]=XY-YX$$ 就构成 $$SO(3)$$ 的 **Lie 代数**，并且 $$\mathfrak{so}(3)\cong\mathfrak{su}(2)\cong\mathbb{R}^3$$ 是**同构**的——尽管 $$SO(3)$$ 与 $$SU(2)=S^3$$ 本身不同胚。整体拓扑与无穷小结构为什么会"失配"，四元数的"半角"在无穷小层面又表现为哪个因子，是下一章的主题。

**延伸阅读**：

- John Stillwell,《Naive Lie Theory》第 8 章。以四元数与 $$SU(2)$$ 为主线讲 $$SO(3)$$，与本章的组织方式最接近。
- Brian Hall,《Lie Groups, Lie Algebras, and Representations》第 1、2 章。$$SU(2)$$ 与 $$SO(3)$$ 的二重覆盖、Pauli 矩阵与四元数对应，写法严格。
- Michael Artin,《Algebra》第 5 章。四元数作为除环与矩阵代数的处理，含 "Hamilton 的发现" 的历史注记。
- Квант 杂志关于四元数与旋转的专题；以及任何一本刚体动力学的开篇（轴角、欧拉角、四元数的三角关系），看工程文献怎样使用本章的定理 3.6 与题 2。
- 原专栏：MP67（典型群(1)：拓扑性质）、MP69（典型群(3)：三维空间的旋转、Pauli 矩阵、四元数、$$SO(3)$$、$$\mathbb{RP}^3$$、$$SU(2)$$、$$S^3$$）。本章的矩阵实现与 $$S^3\cong SU(2)$$ 的论证直接取自 MP69。
- 中子干涉实验的原始文献：H. Rauch 等, *Phys. Lett. A* **54** (1975) 425；科普叙述见 Feynman《QED》与 Susskind 的量子力学讲义中关于 "旋转 $$2\pi$$" 的讨论。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch51_四元数_SO_3_RP³_SU_2_S³_上.md">← 第51章 四元数、SO(3)≅RP³、SU(2)≅S³·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch53_Lie代数与指数映射_上.md">第53章 Lie 代数与指数映射·上 →</a></div>
</div>
