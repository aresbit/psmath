---
layout: default
---

# 第39章: Banach 代数与 C\* 代数·上：预备与直觉 (Banach Algebras and C\*-Algebras · Part I: Warm-up and Intuition)

> 配套深化: 见 第40章 Banach 代数与 C\* 代数·下（完整推导），本章是它的具体铺垫，建议先读本章
> 对应原专栏: MP53–MP54
> 专家依据: `_experts/analysis/functional-analysis.md`（主）+ `_experts/analysis/spectral-theory.md`
> 知识库依据: `opc2/knowledge/math/泛函分析/`（21 篇）
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

第40章要证明的核心结果——Gelfand 表示定理与 Arens 引理——建立在四步抽象之上：把"代数"从具体的矩阵/函数集合抽象成公理化对象；把"级数展开"抽象成 Neumann 级数；把"点"抽象成"特征 (character)"与"极大理想 (maximal ideal)"；把"自伴矩阵的特征值是实数"这件线性代数里司空见惯的事实，抽象成 C\* 代数公理的一条推论。对认真的自学者来说，每一步抽象背后都压着好几行具体计算，第40章为了不显得啰嗦，常常把这些计算压成"直接验证""归纳可得"这类字眼一带而过。

本章的任务，就是先在 $$2\times2$$ 矩阵、$$\mathbb C^3$$ 这类最朴素的有限维对象上，把这些计算逐一手算一遍。读完本章，你会已经亲手做过：验证一个次乘性范数、用幂级数直接求出一个矩阵的逆、算出一个具体交换代数的全部"特征"、验证一个具体对称矩阵的特征值为什么必须是实数。第40章要做的，只是把这几件"具体的事"升级成"任意 Banach 代数、任意 C\* 代数"上的一般陈述——升级的方式，只是把矩阵换成抽象元素、把"坐标"换成"特征"，算法本身不变。

## 二、入口：一道具体的问题 (Entry Problem)

把第40章入口题里的"紧 Hausdorff 空间 $$X$$"与"Hilbert 空间 $$H$$"都换成最小号的有限版本。

**代数甲（有限版）.** 取 $$X = \{1,2,3\}$$（三个点，离散空间自动紧 Hausdorff），$$\mathcal A = \mathbb C^3$$：元素是三元组 $$f=(f_1,f_2,f_3)$$，加法与乘法逐分量进行，范数取 $$\lVert f\rVert_\infty = \max(\lvert f_1\rvert,\lvert f_2\rvert,\lvert f_3\rvert)$$，单位元是 $$\mathbf 1=(1,1,1)$$。这正是 $$C(X)$$ 在 $$X$$ 只有三个点时的样子。

**代数乙（有限版）.** 取 $$H=\mathbb C^3$$（标准内积），$$\mathcal B=M_3(\mathbb C)$$，装备矩阵乘法与算子范数。这正是 $$\mathcal B(H)$$ 在 $$H$$ 有限维时的样子。

**入口题（简化版）**

**(a)【函数的谱，三个点】** 在 $$\mathcal A=\mathbb C^3$$ 中，$$f=(2,0,-1)$$ 是否可逆（即是否存在 $$g$$ 使 $$f_ig_i=1$$ 对 $$i=1,2,3$$ 都成立）？直接检验：$$f_2=0$$，而 $$0\cdot g_2=1$$ 无解，所以 $$f$$ 不可逆。反过来，只要每个 $$f_i\ne0$$，取 $$g_i=1/f_i$$ 就够了。于是
$$f\text{ 不可逆} \iff \text{存在 } i\in\{1,2,3\}\text{ 使 } f_i=0 .$$
这正是第40章入口题 (a) 在三个点上的样子：不可逆（代数条件）$$\iff$$ 某一"坐标"取零（几何条件）。

**(b)【算子的谱，三个点】** 取 $$M=\operatorname{diag}(1,2,3)\in M_3(\mathbb C)$$（对角矩阵，可以看成"在坐标 $$i$$ 处乘以 $$i$$"这个乘法算子的有限版本）。直接算：$$\lambda I - M=\operatorname{diag}(\lambda-1,\lambda-2,\lambda-3)$$ 是对角矩阵，可逆 $$\iff$$ 每个对角元非零 $$\iff$$ $$\lambda\notin\{1,2,3\}$$。于是
$$\sigma(M)=\{1,2,3\}.$$

**(c)【统一的形状】** 并排写：
$$\sigma(f)=\{f_1,f_2,f_3\}=\{2,0,-1\}, \qquad \sigma(M)=\{1,2,3\}.$$
两边都是"某个东西在三个坐标上的取值集合"。在这个有限例子里，$$K=\{1,2,3\}$$ 本身就是那个"能测出谱"的空间，"$$\Gamma$$"就是"直接读出第 $$i$$ 个坐标"这个动作——$$\Gamma(f)(i)=f_i$$。这看起来近乎废话，但请记住这句废话：第40章要证明的，就是**对任意交换 Banach 代数，都能造出一个类似 $$\{1,2,3\}$$ 那样的"坐标集合" $$\Delta(\mathcal A)$$，使 $$\Gamma$$ 同样只是"读坐标"**——哪怕原来的代数长得完全不像 $$\mathbb C^3$$（比如是无穷维的连续函数代数）。

**(d)【交换与否的边界，预热】** 取 $$M_2(\mathbb C)$$ 中两个矩阵单位
$$E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix}, \qquad E_{21}=\begin{pmatrix}0&0\\1&0\end{pmatrix}.$$
直接算：$$E_{12}E_{21}=\begin{pmatrix}1&0\\0&0\end{pmatrix}\ne\begin{pmatrix}0&0\\0&1\end{pmatrix}=E_{21}E_{12}$$，乘法不交换。(c) 里"读坐标"的想法，还能在 $$M_2(\mathbb C)$$ 上重演一遍吗？先记下这个疑问——三节会用两个幂等元和两个幂零元的算术，直接算出答案是"不能"。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 从矩阵的次乘性开始

**手算.** 取
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}2&0\\1&1\end{pmatrix},$$
范数取**行和范数** $$\lVert C\rVert_\infty=\max_i\sum_j\lvert C_{ij}\rvert$$（比矩阵的算子范数好手算，而且同样满足次乘性，这是线性代数里的标准事实）。逐行加：$$A$$ 的两行绝对值和是 $$2,1$$，故 $$\lVert A\rVert_\infty=2$$；$$B$$ 的两行绝对值和是 $$2,2$$，故 $$\lVert B\rVert_\infty=2$$。直接相乘：
$$AB=\begin{pmatrix}1\cdot2+1\cdot1 & 1\cdot0+1\cdot1\\ 0\cdot2+1\cdot1 & 0\cdot0+1\cdot1\end{pmatrix}=\begin{pmatrix}3&1\\1&1\end{pmatrix}.$$
$$AB$$ 两行绝对值和是 $$4,2$$，故 $$\lVert AB\rVert_\infty=4$$。核对：
$$\lVert AB\rVert_\infty=4 \le 4 = \lVert A\rVert_\infty\lVert B\rVert_\infty ,$$
这一次恰好取等。这条不等式——**乘积的范数不超过范数的乘积**——就是"次乘性 (submultiplicativity)"，它对任何一对矩阵、任何一种"由向量范数诱导出的矩阵范数"都成立，不是 $$A,B$$ 这两个特定矩阵的巧合。

**定义 3.1（代数与次乘性，手算版）** 一个**代数 (algebra)** 就是一个既能加、又能乘（乘法满足结合律与分配律）的复线性空间；有单位元 $$e$$（满足 $$ea=ae=a$$）就叫**含单位的 (unital)**；乘法可交换就叫**交换的 (commutative)**。如果代数上还有一个范数 $$\lVert\cdot\rVert$$，使空间完备（柯西列都收敛），并且满足**次乘性 (submultiplicativity)** $$\lVert ab\rVert\le\lVert a\rVert\lVert b\rVert$$，就叫 **Banach 代数 (Banach algebra)**。$$M_n(\mathbb C)$$（矩阵乘法）、$$\mathbb C^n$$（逐分量乘法）都是这样的对象，而且都含单位、都完备（有限维空间自动完备）。

### 3.2 一次具体的幂级数求逆：谱的雏形

**手算（标量情形）.** 先问一个熟悉的问题：$$1/(1-0.5)$$ 等于多少？按等比级数展开，$$\sum_{n=0}^\infty (0.5)^n$$ 的部分和是
$$s_1=1,\quad s_2=1.5,\quad s_3=1.75,\quad s_4=1.875,\ \dots$$
逐项逼近 $$1/(1-0.5)=2$$，误差 $$2-s_N=(0.5)^N/(1-0.5)$$ 随 $$N$$ 指数缩小。

**手算（矩阵情形，对角）.** 把上面这件事搬到矩阵上：取 $$a=\operatorname{diag}(1/2,\,1/3)$$。逐分量用等比级数：
$$(I-a)^{-1}=\operatorname{diag}\Big(\frac{1}{1-1/2},\ \frac{1}{1-1/3}\Big)=\operatorname{diag}(2,\ 3/2).$$
直接求逆核对：$$I-a=\operatorname{diag}(1/2,2/3)$$，逆矩阵就是把每个对角元取倒数，正是 $$\operatorname{diag}(2,3/2)$$——两种算法吻合。

**手算（矩阵情形，幂零，精确有限和）.** 更进一步，取
$$a=\begin{pmatrix}0&1/2\\0&0\end{pmatrix}, \qquad a^2=\begin{pmatrix}0&1/2\\0&0\end{pmatrix}\begin{pmatrix}0&1/2\\0&0\end{pmatrix}=\begin{pmatrix}0&0\\0&0\end{pmatrix}=0.$$
因为 $$a^2=0$$，"级数" $$\sum_{n\ge0}a^n=I+a$$ 只有两项，直接相乘验证：
$$(I-a)(I+a)=I+a-a-a^2=I-a^2=I. \tag{39.1}$$
同样 $$(I+a)(I-a)=I$$，所以
$$(I-a)^{-1}=I+a=\begin{pmatrix}1&1/2\\0&1\end{pmatrix}.$$
这个例子比对角情形更有代表性：它告诉我们**"$$I-a$$ 可逆、逆是幂级数和"这件事不需要 $$a$$ 可对角化**，只需要级数本身收敛（这里甚至提前截断为零）。

**命题 3.2（Neumann 级数，手算版）** 上面三个例子的公共模式是：只要 $$a$$ "足够小"（标量情形 $$\lvert a\rvert<1$$；矩阵情形用范数 $$\lVert a\rVert<1$$ 衡量"小"），$$e-a$$ 就可逆，逆由幂级数 $$\sum_{n\ge0}a^n$$ 给出，而且这个级数按 $$\lVert a^n\rVert\le\lVert a\rVert^n$$ 绝对收敛（次乘性保证了这条估计——上面 3.1 节手算过的那条不等式）。第40章命题 3.3 会把这件事写成任意 Banach 代数上的一般定理，并补上完整的分析证明（核心还是同一个技巧：截断和 $$s_N=e+a+\dots+a^{N-1}$$ 满足 $$(e-a)s_N=e-a^N$$，让 $$N\to\infty$$）。

**从这里看"谱"从哪里来.** 上面三个例子都在回答"$$e-a$$（或更一般的 $$\lambda e-a$$）什么时候可逆"这个问题。把入口题 (b) 里的 $$M=\operatorname{diag}(1,2,3)$$ 拿来做同样的事：$$\lambda I-M$$ 什么时候不可逆？直接看对角元，$$\lambda I - M=\operatorname{diag}(\lambda-1,\lambda-2,\lambda-3)$$ 不可逆 $$\iff$$ 某个对角元为零 $$\iff$$ $$\lambda\in\{1,2,3\}$$。

**定义 3.3（谱，有限维手算版）** 使 $$\lambda I-M$$（或抽象地，$$\lambda e-a$$）不可逆的 $$\lambda$$ 全体，称为 $$M$$（或 $$a$$）的**谱 (spectrum)**，记 $$\sigma(M)$$。上面算出 $$\sigma(M)=\{1,2,3\}$$。第40章定义 3.2 会在任意含单位的 Banach 代数 $$\mathcal A$$ 上重写这个定义（把 $$I$$ 换成 $$e$$），命题 3.3 到命题 3.4 会证明 $$\sigma(a)$$ 总是 $$\mathbb C$$ 的一个非空紧子集——"非空"这一条在有限维矩阵上是显然的（特征多项式总有根），但对无穷维的抽象代数，需要 Liouville 定理这样的分析工具才能补上。

### 3.3 有限维交换代数的"点"：手算全部特征

三点空间上的函数 $$f\in\mathbb C^3$$ 天然有"在第 $$i$$ 个点取值"这个操作 $$f\mapsto f_i$$。下面直接验证：这个操作恰好把 $$\mathbb C^3$$ 里能"读出一个数"的全部方式都列尽了，不多不少。

**手算.** 记 $$e_1=(1,0,0)$$、$$e_2=(0,1,0)$$、$$e_3=(0,0,1)$$。逐分量乘法给出两条关键的算术事实：
$$e_i\cdot e_i=e_i\ (\text{幂等}),\qquad e_i\cdot e_j=0\ (i\ne j),\qquad e_1+e_2+e_3=\mathbf 1 .$$
设 $$\varphi:\mathbb C^3\to\mathbb C$$ 是线性的、保乘法的（$$\varphi(fg)=\varphi(f)\varphi(g)$$）、且 $$\varphi(\mathbf 1)=1$$（这正是第40章定义 3.9 里"特征"的三条要求）。把 $$e_i\cdot e_i=e_i$$ 代入乘性：
$$\varphi(e_i)^2=\varphi(e_i\cdot e_i)=\varphi(e_i) \quad\Longrightarrow\quad \varphi(e_i)\big(\varphi(e_i)-1\big)=0 \quad\Longrightarrow\quad \varphi(e_i)\in\{0,1\}.$$
把 $$e_i\cdot e_j=0$$（$$i\ne j$$）代入乘性：$$\varphi(e_i)\varphi(e_j)=\varphi(0)=0$$，所以 $$\varphi(e_i),\varphi(e_j)$$ 不能同时是 $$1$$。再把 $$e_1+e_2+e_3=\mathbf 1$$ 代入线性性：$$\varphi(e_1)+\varphi(e_2)+\varphi(e_3)=\varphi(\mathbf 1)=1$$。三个数各取 $$0$$ 或 $$1$$、两两不同时为 $$1$$、加起来等于 $$1$$——唯一的可能是**恰好一个 $$\varphi(e_k)=1$$，其余为 $$0$$**。任意 $$f=(f_1,f_2,f_3)=f_1e_1+f_2e_2+f_3e_3$$，由线性性
$$\varphi(f)=f_1\varphi(e_1)+f_2\varphi(e_2)+f_3\varphi(e_3)=f_k ,$$
即 $$\varphi$$ 就是"读第 $$k$$ 个坐标"这个操作。反过来，对每个 $$k\in\{1,2,3\}$$，$$\varphi_k(f)=f_k$$ 确实线性、保乘法（逐分量乘法下 $$(fg)_k=f_kg_k$$）、且 $$\varphi_k(\mathbf 1)=1$$，是合法的特征。

**定义 3.4（特征，手算版）** 满足"线性 + 保乘法 + $$\varphi(\mathbf 1)=1$$"的映射 $$\varphi:\mathcal A\to\mathbb C$$ 称为 $$\mathcal A$$ 的**特征 (character)**。

**命题 3.5（$$\mathbb C^3$$ 的全部特征）** $$\mathbb C^3$$ 恰有三个特征 $$\varphi_1,\varphi_2,\varphi_3$$，$$\varphi_k(f)=f_k$$，一一对应三个坐标。

**$$M_2(\mathbb C)$$ 没有特征——直接算.** 回到入口题 (d)。除了 $$E_{12},E_{21}$$，再取 $$E_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix}$$、$$E_{22}=\begin{pmatrix}0&0\\0&1\end{pmatrix}$$。直接算：$$E_{11}^2=E_{11}$$、$$E_{22}^2=E_{22}$$（幂等）；$$E_{12}^2=\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix}=0$$、同理 $$E_{21}^2=0$$（幂零）；而
$$E_{12}E_{21}=\begin{pmatrix}1&0\\0&0\end{pmatrix}=E_{11}, \qquad E_{21}E_{12}=\begin{pmatrix}0&0\\0&1\end{pmatrix}=E_{22}$$
（这正是(d)里算过的那两个乘积）。设 $$\varphi\in\Delta(M_2(\mathbb C))$$ 存在。幂零元给出 $$\varphi(E_{12})^2=\varphi(E_{12}^2)=\varphi(0)=0$$，故 $$\varphi(E_{12})=0$$；同理 $$\varphi(E_{21})=0$$。于是
$$\varphi(E_{11})=\varphi(E_{12}E_{21})=\varphi(E_{12})\varphi(E_{21})=0, \qquad \varphi(E_{22})=\varphi(E_{21}E_{12})=\varphi(E_{21})\varphi(E_{12})=0 .$$
但 $$E_{11}+E_{22}=I$$ 给出 $$\varphi(E_{11})+\varphi(E_{22})=\varphi(I)=1$$，即 $$0+0=1$$，矛盾！所以 $$M_2(\mathbb C)$$ 不存在特征：$$\Delta(M_2(\mathbb C))=\varnothing$$。

这与 $$\mathbb C^3$$ 的算法唯一的差别，就是"读坐标"这条路要求乘法交换——$$\mathbb C^3$$ 里 $$e_ie_j=e_je_i$$ 自动成立，但 $$M_2(\mathbb C)$$ 里 $$E_{12}E_{21}\ne E_{21}E_{12}$$，"点"就消失了。第40章经典问题 2 会用理想论重新给出这个结论（对一般的 $$M_n(\mathbb C)$$，$$n\ge2$$），但上面这个幂等元/幂零元的直接算法已经把要点摆在了台面上。

### 3.4 自伴矩阵的谱为什么是实数：一次具体验证

**手算（对照组：会转的矩阵）.** 取
$$B=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\ (\text{逆时针旋转 } 90^\circ).$$
特征方程 $$\det(B-\lambda I)=\lambda^2+1=0$$，特征值是 $$\lambda=\pm i$$——**不是实数**。注意 $$B^*=B^{\mathsf T}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=-B$$，$$B$$ 不自伴。

**手算（主角：会拉伸的矩阵）.** 取
$$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}.$$
$$A$$ 是实对称矩阵，故 $$A^*=A^{\mathsf T}=A$$，自伴。特征方程 $$\det(A-\lambda I)=(2-\lambda)^2-1=\lambda^2-4\lambda+3=(\lambda-1)(\lambda-3)=0$$，特征值 $$\lambda=1,3$$——**都是实数**。

**验证 C\* 恒等式.** 由自伴算子的谱定理（第 38 章），实对称矩阵的算子范数等于最大特征值的绝对值，故 $$\lVert A\rVert=3$$。直接算 $$A^2$$（因为 $$A$$ 自伴，$$A^*A=A^2$$）：
$$A^2=\begin{pmatrix}2&1\\1&2\end{pmatrix}\begin{pmatrix}2&1\\1&2\end{pmatrix}=\begin{pmatrix}5&4\\4&5\end{pmatrix}.$$
$$A^2$$ 的特征值是 $$A$$ 的特征值的平方：$$1^2=1$$、$$3^2=9$$，故 $$\lVert A^2\rVert=9$$。核对
$$\lVert A^*A\rVert=\lVert A^2\rVert=9=3^2=\lVert A\rVert^2 ,$$
**C\* 恒等式**（第40章定义 3.16）在这个例子上精确成立。

**命题 3.6（自伴 $$\Rightarrow$$ 特征值实，手算版）** 上面的对照说明了什么："旋转"（$$B^*=-B$$）把实向量转成不共线的方向，特征值只能是虚数；"拉伸"（$$A^*=A$$）沿着两条互相垂直的实方向各自伸缩，特征值必须是实数。这不是巧合：第40章的 **Arens 引理**（定理 3.18）会证明，只要一个代数满足 C\* 恒等式 $$\lVert x^*x\rVert=\lVert x\rVert^2$$，自伴元在"特征"上的取值就必须是实数——证明的核心技巧是对 $$t\in\mathbb R$$ 考察 $$b=a+ite$$，用 C\* 恒等式把 $$\lvert\varphi(b)\rvert^2\le\lVert a\rVert^2+t^2$$ 这条不等式的 $$t^2$$ 消掉，逼出一次不等式必须斜率为零。这条论证完全不需要知道矩阵长什么样，只用到"对合"与"范数"这两条代数信息——这正是它能从 $$2\times2$$ 矩阵一路推广到无穷维算子代数的原因。

## 四、几何与物理直觉 (Intuition)

**特征就是"探针".** 三节里，$$\mathbb C^3$$ 的特征 $$\varphi_k$$ 无非是"在第 $$k$$ 个位置读数"。可以把它想成往一块布景里插一根温度计：每根温度计（每个 $$\varphi$$）在每个时刻只报告一个数（$$\varphi(a)$$），把所有温度计的读数拼起来，就重建出了整块布景（$$\hat a$$ 这个函数）。$$M_2(\mathbb C)$$ 没有特征，说的是这块"布景"根本插不进温度计——$$E_{12}E_{21}\ne E_{21}E_{12}$$ 意味着"先测这个再测那个"和"先测那个再测这个"给出不同的答案，任何单一读数都概括不了整个代数。这正是第40章 §4.5、以及量子力学"不可对易的可观测量无法同时精确测量"这条原理的最朴素版本。

**拉伸与旋转：为什么"自伴"对应"实数".** $$A=\begin{pmatrix}2&1\\1&2\end{pmatrix}$$ 沿两条互相垂直的方向（$$(1,1)$$ 与 $$(1,-1)$$）分别拉伸 $$3$$ 倍和 $$1$$ 倍——这是纯粹的伸缩，没有"转向"，伸缩比例（特征值）当然是实数，就像一把尺子量出的长度不会是虚数。$$B=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$$ 则是纯旋转，没有任何实方向被它映回自己的倍数（除了零向量），"伸缩比例"这个概念对旋转失效，代数上体现为特征值变成非实数。物理上，可观测量（能量、位置、动量……）对应自伴算子，测量结果对应特征值——正因为可观测量是"拉伸型"而不是"旋转型"的，测量结果才总是实数。第40章 §4.3 会把这条对应写成完整的物理论证链。

**交换性：能否同时读出所有坐标.** $$\mathbb C^3$$ 的三个特征互不冲突，可以同时问"$$f$$ 在 1、2、3 处分别是多少"；但对 $$M_2(\mathbb C)$$，$$E_{12}$$ 与 $$E_{21}$$ 的乘积顺序会改变答案，无法赋予它们各自独立、互不干扰的"读数"。这就是"交换代数才有点"这件事最直白的含义：交换性等价于"所有测量可以同时、无冲突地进行"。

## 五、经典问题精讲 (Classical Problems)

### 问题 1（幂零矩阵：范数与谱半径可以差很远）

取 $$a=\begin{pmatrix}0&1\\0&0\end{pmatrix}$$（与第40章练习 基3 是同一个矩阵，那里会用谱半径公式重新算一遍）。

**(i)** 求 $$\sigma(a)$$；**(ii)** 求算子范数 $$\lVert a\rVert$$（标准正交基下）；**(iii)** 比较 $$r(a)=\sup_{\lambda\in\sigma(a)}\lvert\lambda\rvert$$ 与 $$\lVert a\rVert$$。

**解.** (i) $$\det a=0$$，$$a$$ 本身不可逆，故 $$0\in\sigma(a)$$。对 $$\lambda\ne0$$，$$\lambda I-a=\begin{pmatrix}\lambda&-1\\0&\lambda\end{pmatrix}$$，行列式 $$\lambda^2\ne0$$，可逆。故 $$\sigma(a)=\{0\}$$。

(ii) $$a$$ 把标准正交基向量 $$e_2=(0,1)$$ 送到 $$e_1=(1,0)$$，把 $$e_1$$ 送到 $$0$$；对一般单位向量 $$x=(x_1,x_2)$$（$$x_1^2+x_2^2=1$$），$$ax=(x_2,0)$$，$$\lVert ax\rVert=\lvert x_2\rvert\le1$$，且 $$x=e_2$$ 时取到 $$1$$。故 $$\lVert a\rVert=1$$。

(iii) $$r(a)=0<1=\lVert a\rVert$$。**谱半径可以严格小于范数**——这正是第40章谱半径公式（定理 3.5）要精确刻画的现象：谱的大小由 $$\lVert a^n\rVert^{1/n}$$ 的极限决定，而这里 $$a^2=0$$，幂立刻死掉，谱半径塌成零，与 $$\lVert a\rVert=1$$ 无关。$$\blacksquare$$

### 问题 2（$$M_2(\mathbb C)$$ 没有特征：完整重述）

用 3.3 节的幂等元/幂零元算法，独立写出 $$M_2(\mathbb C)$$ 不存在特征的完整论证（不许直接抄 3.3 节，重新写一遍每一步的理由）。

**解.** 设 $$\varphi:M_2(\mathbb C)\to\mathbb C$$ 是特征。由 $$E_{12}^2=0$$（直接相乘验证：$$E_{12}$$ 只有第 $$1$$ 行第 $$2$$ 列非零，$$E_{12}$$ 的第 $$2$$ 行全为零，故 $$E_{12}\cdot E_{12}$$ 的每一项都要用到 $$E_{12}$$ 第 $$2$$ 行，结果为零），乘性给出 $$\varphi(E_{12})^2=\varphi(0)=0$$，故 $$\varphi(E_{12})=0$$（复数的平方为零只能它本身为零）。同理由 $$E_{21}^2=0$$ 得 $$\varphi(E_{21})=0$$。由 $$E_{12}E_{21}=E_{11}$$（直接相乘核对）与乘性，$$\varphi(E_{11})=\varphi(E_{12})\varphi(E_{21})=0\cdot0=0$$；由 $$E_{21}E_{12}=E_{22}$$ 同理 $$\varphi(E_{22})=0$$。但 $$E_{11}+E_{22}=I$$，线性性给出 $$\varphi(E_{11})+\varphi(E_{22})=\varphi(I)=1$$（特征的定义要求 $$\varphi(I)=1$$），即 $$0=1$$，矛盾。故不存在这样的 $$\varphi$$。$$\blacksquare$$

### 问题 3（Gelfand 变换在有限维就是"读坐标"）

在 $$\mathcal A=\mathbb C^3$$ 上，取 $$f=(1,-1,2)$$。写出 $$\Gamma(f)$$ 在三个特征 $$\varphi_1,\varphi_2,\varphi_3$$ 上的取值，并核对 $$\sigma(f)=\{\Gamma(f)(\varphi_k):k=1,2,3\}$$ 与 (a)(c) 直接算出的 $$\sigma(f)=\{f_1,f_2,f_3\}$$ 是同一个集合。

**解.** 由命题 3.5，$$\varphi_k(f)=f_k$$，即 $$\Gamma(f)(\varphi_1)=1$$、$$\Gamma(f)(\varphi_2)=-1$$、$$\Gamma(f)(\varphi_3)=2$$。于是
$$\{\Gamma(f)(\varphi_k):k=1,2,3\}=\{1,-1,2\}.$$
另一方面，仿照入口题 (a)，$$\lambda\mathbf1-f=(\lambda-1,\lambda+1,\lambda-2)$$ 不可逆 $$\iff$$ 某一分量为零 $$\iff$$ $$\lambda\in\{1,-1,2\}$$，故 $$\sigma(f)=\{1,-1,2\}$$，与上面吻合。**"元素就是函数"在这里完全不神秘**：$$f$$ 本来就是 $$\{1,2,3\}$$ 上的一个函数，$$\Gamma(f)$$ 只是把它原样搬到 $$\Delta(\mathcal A)=\{\varphi_1,\varphi_2,\varphi_3\}\cong\{1,2,3\}$$ 上。这件"平凡"的事，在第40章的 $$C(X)$$（$$X$$ 是一般紧 Hausdorff 空间）上仍然需要证明——因为那时 $$\Delta(C(X))$$ 是不是"恰好等于 $$X$$"、"没有多出别的怪点"，不再是数有限个坐标就能看出来的，需要一条公共零点引理（第40章经典问题 3）配合紧性才能保证。$$\blacksquare$$

### 问题 4（一般自伴 $$2\times2$$ 矩阵：符号化重做一遍问题 4 的验证）

设 $$A=\begin{pmatrix}\alpha&\beta\\\bar\beta&\delta\end{pmatrix}$$，$$\alpha,\delta\in\mathbb R$$，$$\beta\in\mathbb C$$（这是最一般的 $$2\times2$$ 自伴矩阵）。证明 $$A$$ 的两个特征值都是实数。

**解.** $$A^*=A^{\mathsf T}$$ 取共轭：$$\begin{pmatrix}\bar\alpha&\overline{\bar\beta}\\\bar\beta_{\phantom{)}}^{\phantom{)}}\!\!\!&\bar\delta\end{pmatrix}=\begin{pmatrix}\alpha&\beta\\\bar\beta&\delta\end{pmatrix}=A$$（用了 $$\alpha,\delta$$ 是实数），验证 $$A$$ 确实自伴。特征方程：
$$\det(A-\lambda I)=(\alpha-\lambda)(\delta-\lambda)-\beta\bar\beta=\lambda^2-(\alpha+\delta)\lambda+(\alpha\delta-\lvert\beta\rvert^2)=0 .$$
判别式
$$\Delta=(\alpha+\delta)^2-4(\alpha\delta-\lvert\beta\rvert^2)=(\alpha-\delta)^2+4\lvert\beta\rvert^2 ,$$
是两个非负实数之和，故 $$\Delta\ge0$$ 对任意 $$\alpha,\delta\in\mathbb R$$、$$\beta\in\mathbb C$$ 恒成立。于是
$$\lambda=\frac{(\alpha+\delta)\pm\sqrt\Delta}{2}$$
永远是实数（判别式非负，根号内非负，整个表达式是实数的四则运算）。**这就是问题 4 的一般版本**：不再依赖具体数字，任何自伴 $$2\times2$$ 矩阵的特征值都被这条判别式恒等式钉死在实轴上。$$\blacksquare$$

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.**（次乘性的另一次数值核对）设 $$A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$$，$$B=\begin{pmatrix}1&0\\1&1\end{pmatrix}$$，范数取行和范数。(i) 分别算出 $$\lVert A\rVert$$、$$\lVert B\rVert$$；(ii) 算出 $$AB$$ 与 $$\lVert AB\rVert$$；(iii) 核对次乘性，并说明这一次是否取等。

**基2.**（对角自伴矩阵的谱与范数）设 $$M=\operatorname{diag}(-1,0,2)$$ 作用在 $$\mathbb C^3$$ 上。(i) 直接算出 $$\sigma(M)$$；(ii) 算出谱半径 $$r(M)$$ 与算子范数 $$\lVert M\rVert$$；(iii) 说明为什么这里 $$r(M)=\lVert M\rVert$$。

**基3.**（Neumann 级数：又一组数字）设 $$a=\operatorname{diag}(1/4,\,-1/5)$$。(i) 直接算出 $$(I-a)^{-1}$$；(ii) 用等比级数逐项核对 $$\sum_{n=0}^\infty a^n$$ 收敛到同一个矩阵；(iii) 说明 $$\lVert a\rVert<1$$ 在哪里起了作用。

### 竞赛（本课目标难度）

**竞1.**（$$n$$ 个点的推广）设 $$X=\{1,\dots,n\}$$，$$\mathcal A=\mathbb C^n$$（逐分量运算，上确界范数）。仿照 3.3 节对 $$\mathbb C^3$$ 的论证，证明 $$\mathcal A$$ 恰有 $$n$$ 个特征 $$\varphi_1,\dots,\varphi_n$$，$$\varphi_k(f)=f_k$$，再没有别的特征。

**竞2.**（$$M_n(\mathbb C)$$（$$n\ge2$$）没有特征：一般化）仿照问题 2 的论证，证明对任意 $$n\ge2$$，$$M_n(\mathbb C)$$ 没有特征。（提示：只需要 $$E_{12},E_{21},E_{11},E_{22}$$ 这四个矩阵单位参与论证，其余下标不出场；把它们看成嵌在 $$n\times n$$ 矩阵左上角的 $$2\times2$$ 块即可。）

**竞3.**（一般自伴 $$2\times2$$ 矩阵与 C\* 恒等式）沿用问题 4 的记号 $$A=\begin{pmatrix}\alpha&\beta\\\bar\beta&\delta\end{pmatrix}$$。取 $$\alpha=1,\delta=3,\beta=2i$$。(i) 验证 $$A^*=A$$；(ii) 具体算出两个特征值；(iii) 算出 $$\lVert A\rVert$$（最大特征值的绝对值）与 $$\lVert A^2\rVert$$，核对 C\* 恒等式 $$\lVert A^*A\rVert=\lVert A\rVert^2$$。

### 研究（通向下一章）

**研1.**（Neumann 级数的误差估计）设 $$a=\operatorname{diag}(0.4,\,0.4)$$，$$s_N=\sum_{n=0}^{N-1}a^n$$。(i) 算出精确值 $$(I-a)^{-1}$$；(ii) 算出 $$s_1,s_2,s_3,s_4$$ 并算出误差 $$\lVert(I-a)^{-1}-s_N\rVert$$（行和范数）；(iii) 猜一个关于 $$N$$ 与 $$\lVert a\rVert$$ 的误差公式，并用等比级数余项核对。

**研2.**（旋转 + 伸缩：正规但不自伴的矩阵，$$\lVert b^2\rVert=\lVert b\rVert^2$$ 需要绕道）设 $$b=\begin{pmatrix}1&-2\\2&1\end{pmatrix}$$。(i) 验证 $$b^*b=bb^*$$（$$b$$ 正规），但 $$b^*\ne b$$（$$b$$ 不自伴）；(ii) 直接算出 $$b^2$$，并核对 $$\lVert b^2\rVert=\lVert b\rVert^2$$ 这条等式在数值上成立（提示：可以先算 $$b^*b$$，它是自伴的对角矩阵，比直接对 $$b^2$$ 算算子范数容易）；(iii) 说明为什么这里不能像自伴矩阵那样"直接"套用命题 3.6 的论证。

### 解答 (Solutions)

**解 基1.** (i) $$A$$ 两行绝对值和是 $$1+2=3$$、$$0+1=1$$，故 $$\lVert A\rVert=3$$；$$B$$ 两行是 $$1+0=1$$、$$1+1=2$$，故 $$\lVert B\rVert=2$$。

(ii) $$AB=\begin{pmatrix}1\cdot1+2\cdot1&1\cdot0+2\cdot1\\0\cdot1+1\cdot1&0\cdot0+1\cdot1\end{pmatrix}=\begin{pmatrix}3&2\\1&1\end{pmatrix}$$。两行绝对值和是 $$3+2=5$$、$$1+1=2$$，故 $$\lVert AB\rVert=5$$。

(iii) $$\lVert A\rVert\lVert B\rVert=3\times2=6\ge5=\lVert AB\rVert$$，次乘性成立，这一次是**严格**不等号，没有取等。$$\blacksquare$$

**解 基2.** (i) $$M$$ 是实对角矩阵，故自伴。$$\lambda I-M=\operatorname{diag}(\lambda+1,\lambda,\lambda-2)$$ 不可逆 $$\iff$$ 某个对角元为零 $$\iff$$ $$\lambda\in\{-1,0,2\}$$，故 $$\sigma(M)=\{-1,0,2\}$$。

(ii) $$r(M)=\max(\lvert-1\rvert,\lvert0\rvert,\lvert2\rvert)=2$$。对角矩阵作用在标准正交基下，算子范数等于对角元绝对值的最大值（每个标准基向量都是它自己的特征向量，取范数最大的那个方向即达到上确界），故 $$\lVert M\rVert=2$$。

(iii) $$r(M)=\lVert M\rVert=2$$：因为 $$M$$ 自伴（进而正规），命题 3.6 后面提到的第40章命题 3.17 (iii) 保证了正规元的谱半径恒等于范数；这里 $$M$$ 是对角矩阵，两者相等在(i)(ii)里已经直接验证过了。$$\blacksquare$$

**解 基3.** (i) $$I-a=\operatorname{diag}(3/4,\,6/5)$$，逐分量取倒数：$$(I-a)^{-1}=\operatorname{diag}(4/3,\,5/6)$$。

(ii) 逐分量按等比级数求和：$$\sum_{n\ge0}(1/4)^n=\dfrac{1}{1-1/4}=\dfrac43$$；$$\sum_{n\ge0}(-1/5)^n=\dfrac{1}{1-(-1/5)}=\dfrac{1}{6/5}=\dfrac56$$。两个分量分别与(i)吻合。

(iii) $$\lVert a\rVert=\max(1/4,1/5)=1/4<1$$，这保证了两条几何级数（$$\sum(1/4)^n$$ 与 $$\sum(1/5)^n$$，后者甚至交错、收敛更快）都绝对收敛；若某个对角元的绝对值 $$\ge1$$，级数就不收敛，$$(I-a)^{-1}$$ 也可能不存在（例如对角元恰为 $$1$$ 时 $$I-a$$ 直接奇异）。$$\blacksquare$$

**解 竞1.** 记 $$e_k\in\mathbb C^n$$ 为第 $$k$$ 个坐标向量（第 $$k$$ 位是 $$1$$，其余为 $$0$$）。与 3.3 节一致：$$e_k^2=e_k$$（幂等），$$e_ke_j=0$$（$$k\ne j$$），$$\sum_{k=1}^ne_k=\mathbf1$$。设 $$\varphi\in\Delta(\mathcal A)$$。由幂等性与乘性，$$\varphi(e_k)^2=\varphi(e_k)$$，故 $$\varphi(e_k)\in\{0,1\}$$ 对每个 $$k$$ 成立；由 $$e_ke_j=0$$（$$k\ne j$$）与乘性，$$\varphi(e_k)\varphi(e_j)=0$$，故至多一个 $$\varphi(e_k)$$ 为 $$1$$；由线性性与 $$\sum_ke_k=\mathbf1$$，$$\sum_k\varphi(e_k)=\varphi(\mathbf1)=1$$，故恰好一个 $$\varphi(e_k)=1$$，记这个下标为 $$m$$。对任意 $$f=\sum_kf_ke_k$$，$$\varphi(f)=\sum_kf_k\varphi(e_k)=f_m$$，即 $$\varphi=\varphi_m$$。反过来每个 $$\varphi_k(f)=f_k$$ 都合法（同 $$n=3$$ 时的验证，逐分量乘法保证乘性）。故 $$\Delta(\mathcal A)=\{\varphi_1,\dots,\varphi_n\}$$，恰 $$n$$ 个。$$\blacksquare$$

**解 竞2.** 把 $$M_2(\mathbb C)$$ 里用到的四个矩阵单位 $$E_{11},E_{12},E_{21},E_{22}$$ 嵌入 $$M_n(\mathbb C)$$ 左上角 $$2\times2$$ 块（其余位置补零）。矩阵单位乘法法则 $$E_{ab}E_{cd}=\delta_{bc}E_{ad}$$ 在 $$n\times n$$ 里同样成立（与 $$n=2$$ 时逐项核对完全一致，因为非零元都落在同一个 $$2\times2$$ 块里，块外的零不参与运算），故仍有 $$E_{12}^2=E_{21}^2=0$$、$$E_{12}E_{21}=E_{11}$$、$$E_{21}E_{12}=E_{22}$$，以及 $$E_{11}+E_{22}\ne I_n$$（$$n\ge3$$ 时还差 $$E_{33}+\dots+E_{nn}$$）——但这不影响论证：设 $$\varphi$$ 是特征，同问题 2 的推理得 $$\varphi(E_{12})=\varphi(E_{21})=0$$，从而 $$\varphi(E_{11})=\varphi(E_{22})=0$$。再取 $$E_{33},\dots,E_{nn}$$（$$n\ge3$$ 时），它们两两正交幂等（$$E_{kk}^2=E_{kk}$$、$$E_{kk}E_{jj}=0$$，$$k\ne j$$），同 3.3 节的论证，$$\varphi(E_{kk})\in\{0,1\}$$ 且至多一个为 $$1$$；但 $$\sum_{k=1}^nE_{kk}=I$$，故 $$\sum_k\varphi(E_{kk})=1$$。这与已经算出的 $$\varphi(E_{11})=\varphi(E_{22})=0$$ 相容（可以是某个 $$k\ge3$$ 使 $$\varphi(E_{kk})=1$$）——但再用一次 $$E_{1k}E_{k1}=E_{11}$$ 型的关系（$$k\ne1$$）：由 $$E_{1k}^2=0$$（$$k\ne1$$，同样的幂零论证）得 $$\varphi(E_{1k})=0$$，从而 $$\varphi(E_{kk})=\varphi(E_{k1}E_{1k})=\varphi(E_{k1})\varphi(E_{1k})=0$$ 对**每个** $$k$$ 成立（$$k=1$$ 时就是已经算出的 $$\varphi(E_{11})=0$$）。于是 $$\sum_k\varphi(E_{kk})=0\ne1$$，矛盾。故 $$n\ge2$$ 时 $$M_n(\mathbb C)$$ 没有特征。（$$n=2$$ 时上面第二段不需要，问题 2 的论证已经够用。）$$\blacksquare$$

**解 竞3.** (i) $$A=\begin{pmatrix}1&2i\\-2i&3\end{pmatrix}$$（因为 $$\bar\beta=\overline{2i}=-2i$$）。$$A^*=A^{\mathsf T}$$ 取共轭 $$=\begin{pmatrix}1&\overline{-2i}\\\overline{2i}&3\end{pmatrix}=\begin{pmatrix}1&2i\\-2i&3\end{pmatrix}=A$$，自伴。

(ii) 特征方程 $$\lambda^2-(1+3)\lambda+(1\times3-\lvert2i\rvert^2)=\lambda^2-4\lambda+(3-4)=\lambda^2-4\lambda-1=0$$。判别式 $$16+4=20$$，$$\lambda=\dfrac{4\pm\sqrt{20}}{2}=2\pm\sqrt5$$。两个特征值都是实数：$$\lambda_1=2+\sqrt5\approx4.236$$，$$\lambda_2=2-\sqrt5\approx-0.236$$。

(iii) $$\lVert A\rVert=\max(\lvert2+\sqrt5\rvert,\lvert2-\sqrt5\rvert)=2+\sqrt5$$（因为 $$\sqrt5\approx2.236<4$$，故 $$2-\sqrt5\approx-0.236$$，绝对值小于 $$2+\sqrt5$$）。$$A^2$$ 的特征值是 $$(2+\sqrt5)^2=9+4\sqrt5$$ 与 $$(2-\sqrt5)^2=9-4\sqrt5$$；因为 $$9-4\sqrt5\approx0.056>0$$，两者都非负，$$\lVert A^2\rVert=\max(9+4\sqrt5,\,9-4\sqrt5)=9+4\sqrt5$$。核对：$$\lVert A\rVert^2=(2+\sqrt5)^2=9+4\sqrt5=\lVert A^2\rVert=\lVert A^*A\rVert$$（自伴时 $$A^*A=A^2$$）。C\* 恒等式精确成立。$$\blacksquare$$

**解 研1.** (i) $$I-a=\operatorname{diag}(0.6,0.6)=0.6\,I$$，故 $$(I-a)^{-1}=\dfrac{1}{0.6}I=\dfrac53I\approx1.6667\,I$$。

(ii) $$s_1=I$$（只有 $$n=0$$ 一项）；$$s_2=I+0.4I=1.4\,I$$；$$s_3=s_2+0.16I=1.56\,I$$；$$s_4=s_3+0.064I=1.624\,I$$。误差（行和范数，对角矩阵就是对角元绝对值）：
$$\lVert(I-a)^{-1}-s_1\rVert=1.6667-1=0.6667,\quad \lVert(I-a)^{-1}-s_2\rVert=1.6667-1.4=0.2667,$$
$$\lVert(I-a)^{-1}-s_3\rVert=1.6667-1.56=0.1067,\quad \lVert(I-a)^{-1}-s_4\rVert=1.6667-1.624=0.0427.$$

(iii) 猜测 $$\lVert(I-a)^{-1}-s_N\rVert=\dfrac{\lVert a\rVert^N}{1-\lVert a\rVert}$$。核对：$$N=1$$，$$0.4/0.6=0.6\overline6$$，与上面一致；$$N=2$$，$$0.16/0.6=0.2\overline6$$，一致；$$N=3$$，$$0.064/0.6\approx0.1067$$，一致；$$N=4$$，$$0.0256/0.6\approx0.0427$$，一致。一般地，$$(I-a)^{-1}-s_N=\sum_{n=N}^\infty a^n=a^N\sum_{n=0}^\infty a^n=a^N(I-a)^{-1}$$（对角情形逐分量算等比级数余项即可），取范数得 $$\lVert a\rVert^N/(1-\lVert a\rVert)$$。**这正是第40章命题 3.3 证明里"$$\lVert a^N\rVert\to0$$，故截断和收敛到真值"这一步的具体数值版本**——那里只证了极限为零，这里进一步算出了收敛速度。$$\blacksquare$$

**解 研2.** (i) $$b^{\mathsf T}=\begin{pmatrix}1&2\\-2&1\end{pmatrix}$$，因 $$b$$ 是实矩阵，$$b^*=b^{\mathsf T}$$。直接算：
$$b^*b=\begin{pmatrix}1&2\\-2&1\end{pmatrix}\begin{pmatrix}1&-2\\2&1\end{pmatrix}=\begin{pmatrix}1+4&-2+2\\-2+2&4+1\end{pmatrix}=\begin{pmatrix}5&0\\0&5\end{pmatrix},$$
$$bb^*=\begin{pmatrix}1&-2\\2&1\end{pmatrix}\begin{pmatrix}1&2\\-2&1\end{pmatrix}=\begin{pmatrix}1+4&2-2\\2-2&4+1\end{pmatrix}=\begin{pmatrix}5&0\\0&5\end{pmatrix}.$$
两者相等，$$b$$ 正规；但 $$b^*=\begin{pmatrix}1&2\\-2&1\end{pmatrix}\ne\begin{pmatrix}1&-2\\2&1\end{pmatrix}=b$$，$$b$$ 不自伴。

(ii) $$b^2=\begin{pmatrix}1&-2\\2&1\end{pmatrix}\begin{pmatrix}1&-2\\2&1\end{pmatrix}=\begin{pmatrix}1-4&-2-2\\2+2&-4+1\end{pmatrix}=\begin{pmatrix}-3&-4\\4&-3\end{pmatrix}$$。由(i)，$$b^*b=5I$$，故 $$\lVert b\rVert^2=\lVert b^*b\rVert=5$$（用了第40章 C\* 恒等式，或者直接：$$b/\sqrt5$$ 是正交矩阵，$$\lVert b\rVert=\sqrt5$$），于是 $$\lVert b\rVert^2=5$$。另一方面，$$(b^2)^*(b^2)=(b^*)^2b^2$$；因为 $$b$$ 正规，$$(b^*)^2b^2=b^*(b^*b)b=b^*(bb^*)b=(b^*b)(b^*b)=(5I)(5I)=25I$$，故 $$\lVert b^2\rVert^2=\lVert(b^2)^*b^2\rVert=25$$，即 $$\lVert b^2\rVert=5$$。核对：$$\lVert b^2\rVert=5=\lVert b\rVert^2$$，等式成立。

(iii) 不能直接套用命题 3.6（那里的自伴论证）：命题 3.6 与第40章命题 3.17 (ii) 的公式 $$\lVert s^2\rVert=\lVert s\rVert^2$$ 只对**自伴**元 $$s$$ 证明过（直接用 $$s^*s=s^2$$ 代入 C\* 恒等式）；$$b$$ 只是正规，$$b^*\ne b$$，所以 $$b^*b\ne b^2$$，不能把 C\* 恒等式 $$\lVert b^*b\rVert=\lVert b\rVert^2$$ 直接读成 $$\lVert b^2\rVert=\lVert b\rVert^2$$。上面(ii)的正确算法是**绕道 $$b^*b$$**：先用正规性把 $$(b^2)^*(b^2)$$ 重排成 $$(b^*b)^2$$（这一步需要 $$b^*b=bb^*$$），$$b^*b$$ 是自伴的（对任何 $$b$$ 都自伴），这时才合法调用"自伴元的平方"公式。第40章命题 3.17 (iii) 的证明正是这条绕道的一般版本。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**T1.** 谱、可逆性是纯代数概念，在 $$\mathbb C^3$$、$$M_n(\mathbb C)$$ 这类你已经很熟悉的对象上就能完整定义与手算，不需要"算子""希尔伯特空间"这些无穷维背景。

**T2.** Neumann 级数把"等比级数求和"这件事从标量搬到矩阵、再搬到抽象代数：只要 $$\lVert a\rVert<1$$，$$e-a$$ 就可逆，逆由幂级数给出；收敛速度由 $$\lVert a\rVert^N/(1-\lVert a\rVert)$$ 控制（研1）。

**T3.** "特征"就是"读坐标"的代数化身：交换代数（如 $$\mathbb C^n$$）里，特征由幂等元与乘法关系直接解出，恰好一一对应"坐标"；一旦代数不交换（如 $$M_n(\mathbb C)$$，$$n\ge2$$），两个不对易的元素立刻用幂零性逼出矛盾，特征集合整体消失。

**T4.** 自伴（$$A^*=A$$）对应"纯拉伸"，特征值必为实数；正规但不自伴（如研2 的旋转伸缩矩阵）则需要绕道 $$b^*b$$ 才能算清楚 $$\lVert b^2\rVert=\lVert b\rVert^2$$——直接套用"自伴"的公式是最容易踩的坑。

**T5（交棒）.** 现在你已经能手算出：小矩阵的可逆性与谱、有限维交换代数的全部特征、自伴矩阵特征值为实数的具体验证、以及"正规但不自伴"时公式为什么不能照搬。下一章（第40章）会证明这一切对**任意**（可能无穷维的）Banach 代数与 C\* 代数都成立，给出一般的 Gelfand 表示定理与 Arens 引理，并回答第36章留下的悬念：自伴算子的谱为什么必须落在实轴上。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch38_谱定理与投影算子值测度_下.md">← 第38章 谱定理与投影算子值测度·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch40_Banach代数与C_代数_下.md">第40章 Banach 代数与 C\* 代数·下 →</a></div>
</div>
