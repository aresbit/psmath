---
layout: default
---

# 第79章: 尾声：从 Galois 到现代数学·上：预备与直觉 (Epilogue: From Galois to Modern Mathematics · Part I: Warm-up and Intuition)

> 配套深化: 见 第80章 尾声：从 Galois 到现代数学·下（完整推导），本章是它的具体铺垫，建议先读本章
> 专家依据: `_experts/algebra/algebraic-geometry-topology-k.md` + `_experts/algebra/category-universal-properties.md` + `_experts/numbertheory/analytic-number-theory.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

第 80 章要把全书 39 章里反复出现的"巧合"归并成四条**共同定理**：对偶与反变、$$D^2=0$$ 的两副面孔、谱、Galois 连接。这四条定理各自都在"用一句话概括一大类现象"，而正因为它们概括得多，第一次读到定义时最容易觉得"符号一大堆，但不知道为什么要这样写"。

本章要打磨的正是这四个跳跃点，每个都用**具体数字**先手算一遍：

1. **对偶**——用一个具体的 $$2\times3$$ 矩阵算"箭头反过来"是什么意思，代替直接讲抽象的"对偶范畴"；
2. **$$D^2=0$$**——用一个三角形的顶点、边、面手算"边界的边界为零"，代替直接讲一般环上模的链复形；
3. **谱**——用一个 $$2\times2$$ 矩阵手算特征值、预解式、预解恒等式，代替直接证无穷维 Banach 空间上"谱非空"；
4. **Galois 连接**——用 $$\mathbb Q(\sqrt2)/\mathbb Q$$ 这个只有两个子群、两个中间域的最小例子，代替直接讲一般偏序集上的反序映射。

读完本章，你应该已经**用手**算出这四件事在最小例子里长什么样；第 80 章要做的，只是把这些手算步骤逐字符号化，换成对"任意范畴""任意环上模""任意 Banach 空间""任意偏序集"都成立的一般陈述与证明。

## 二、入口：一道具体的问题 (Entry Problem)

下面四小题各自只要求**算出答案**，不要求你写出一般证明——那是第 80 章的事。

**(a)（箭头反过来）** 取
$$A=\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix}\ (2\times3),\qquad B=\begin{pmatrix}1&0\\-1&1\\0&2\end{pmatrix}\ (3\times2).$$
写出 $$A^T$$、$$B^T$$，算出 $$AB$$（$$2\times2$$）与 $$(AB)^T$$，再算出 $$B^TA^T$$。它们相等吗？

**(b)（边界的边界）** 一个三角形有三个顶点 $$v_1,v_2,v_3$$、三条有向边 $$e_1=v_1v_2$$、$$e_2=v_2v_3$$、$$e_3=v_1v_3$$，和一个面 $$\sigma=v_1v_2v_3$$。规定"面的边界"是
$$\partial_2\sigma=e_1+e_2-e_3,$$
"边的边界"是"终点减起点"：$$\partial_1e_1=v_2-v_1$$，$$\partial_1e_2=v_3-v_2$$，$$\partial_1e_3=v_3-v_1$$。算出 $$\partial_1(\partial_2\sigma)$$。

**(c)（谱与预解式）** 取
$$T=\begin{pmatrix}2&1\\0&3\end{pmatrix}.$$
求 $$T$$ 的特征值。再取 $$\lambda=5$$，算出 $$(\lambda I-T)^{-1}$$（写成具体矩阵）。

**(d)（域越大，群越小）** 设 $$K=\mathbb Q(\sqrt2)=\{a+b\sqrt2:a,b\in\mathbb Q\}$$。$$\mathbb Q$$-自同构 $$\sigma:K\to K$$ 只能把 $$\sqrt2$$ 送到 $$x^2-2=0$$ 的另一个根，即 $$\pm\sqrt2$$。写出 $$\operatorname{Gal}(K/\mathbb Q)$$ 的全部元素、全部子群，以及每个子群对应的"被它固定住的元素全体"（固定域）。

**题面为什么这样设计。** 这四小题分别是第 80 章定义 3.1、定义 3.2、定义 3.3、定义 3.4 的最小实例——你算完之后会发现：(a) 的两个答案永远相等（这是"反变"的雏形）；(b) 的答案永远是零（这是 $$\partial^2=0$$ 的雏形）；(c) 里 $$5I-T$$ 恰好可逆，因为 $$5$$ 不是特征值（这是"谱＝不可逆的点"的雏形）；(d) 里子群越大，固定域越小（这是 Galois 连接的雏形）。第三节会把这四个"永远"背后的原因说清楚。

## 三、结构：定义与完整推导 (Structure & Proof)

这一节把入口题的四小题逐个做完：先手算，再抽象出一般陈述。

### 3.1 转置：把箭头倒过来的具体算法

先把入口题 (a) 算完整。

$$A^T=\begin{pmatrix}1&0\\2&1\\0&1\end{pmatrix},\qquad B^T=\begin{pmatrix}1&-1&0\\0&1&2\end{pmatrix}.$$

$$AB$$ 逐项算：第 1 行第 1 列 $$=1\cdot1+2\cdot(-1)+0\cdot0=-1$$；第 1 行第 2 列 $$=1\cdot0+2\cdot1+0\cdot2=2$$；第 2 行第 1 列 $$=0\cdot1+1\cdot(-1)+1\cdot0=-1$$；第 2 行第 2 列 $$=0\cdot0+1\cdot1+1\cdot2=3$$。故
$$AB=\begin{pmatrix}-1&2\\-1&3\end{pmatrix},\qquad (AB)^T=\begin{pmatrix}-1&-1\\2&3\end{pmatrix}.$$

再算 $$B^TA^T$$（$$2\times3$$ 乘 $$3\times2$$）：第 1 行第 1 列 $$=1\cdot1+(-1)\cdot2+0\cdot0=-1$$；第 1 行第 2 列 $$=1\cdot0+(-1)\cdot1+0\cdot1=-1$$；第 2 行第 1 列 $$=0\cdot1+1\cdot2+2\cdot0=2$$；第 2 行第 2 列 $$=0\cdot0+1\cdot1+2\cdot1=3$$。故
$$B^TA^T=\begin{pmatrix}-1&-1\\2&3\end{pmatrix}=(AB)^T.$$

两者逐项相等，**顺序被倒过来了**：先 $$A$$ 后 $$B$$（即 $$AB$$）转置之后，变成先 $$B^T$$ 后 $$A^T$$（即 $$B^TA^T$$）。这不是这两个具体矩阵的巧合——换任意一对形状匹配的矩阵重算一遍都成立，原因纯粹是下标求和的对称性：

**命题 3.1（转置反转合成顺序）** 设 $$A$$ 是 $$m\times n$$ 矩阵，$$B$$ 是 $$n\times k$$ 矩阵。则 $$(AB)^T=B^TA^T$$。

**证明**：记 $$A=(a_{ij})$$、$$B=(b_{jl})$$。按定义，$$AB$$ 的 $$(i,l)$$ 元是 $$\sum_{j=1}^na_{ij}b_{jl}$$，所以 $$(AB)^T$$ 的 $$(l,i)$$ 元就是
$$\big((AB)^T\big)_{li}=(AB)_{il}=\sum_{j=1}^na_{ij}b_{jl}.$$
另一边，$$A^T$$ 的 $$(j,i)$$ 元是 $$a_{ij}$$，$$B^T$$ 的 $$(l,j)$$ 元是 $$b_{jl}$$，所以 $$B^TA^T$$ 的 $$(l,i)$$ 元是
$$(B^TA^T)_{li}=\sum_{j=1}^n(B^T)_{lj}(A^T)_{ji}=\sum_{j=1}^nb_{jl}\,a_{ij}.$$
两式右边只差乘法顺序，而数的乘法可交换，故对每个 $$(l,i)$$ 都有 $$\big((AB)^T\big)_{li}=(B^TA^T)_{li}$$，即 $$(AB)^T=B^TA^T$$。$$\blacksquare$$

**这为什么是"反变"的雏形。** 把矩阵 $$A$$ 看成线性映射 $$f:\mathbb R^n\to\mathbb R^m$$、$$B$$ 看成 $$g:\mathbb R^k\to\mathbb R^n$$，则 $$AB$$ 对应"先 $$g$$ 后 $$f$$"的复合 $$f\circ g$$。命题 3.1 说：把这个复合"转置"（第 80 章会说"送进对偶空间"），得到的箭头方向、复合顺序都反过来了——$$(f\circ g)^T=g^T\circ f^T$$。第 80 章的定义 3.1 要做的，就是把"转置"这个具体操作换成对**任意**范畴都有意义的"把每个箭头方向倒过来"，而命题 3.1 的证明思路（拆开定义、逐项核对、发现只是乘法顺序变了）会原样变成定理 3.1 证明里"逐条核对范畴公理"的那一步。

### 3.2 边界的边界为零：一个三角形算两遍

先把入口题 (b) 算完整。把 $$v_1,v_2,v_3$$、$$e_1,e_2,e_3$$ 都当成自由交换群 $$\mathbb Z^3$$ 的基向量，$$\partial_1,\partial_2$$ 按线性延拓：
$$\partial_1(\partial_2\sigma)=\partial_1(e_1+e_2-e_3)=\partial_1e_1+\partial_1e_2-\partial_1e_3$$
$$=(v_2-v_1)+(v_3-v_2)-(v_3-v_1)=(v_2-v_1)+(v_3-v_2)+(v_1-v_3).$$
把三项加起来：$$v_2$$ 出现 $$+1-1=0$$ 次，$$v_1$$ 出现 $$-1+1=0$$ 次，$$v_3$$ 出现 $$+1-1=0$$ 次。所以
$$\partial_1(\partial_2\sigma)=0.$$
这不是巧合：$$\partial_2\sigma$$ 把三角形的边界拆成三条边，每条边又被 $$\partial_1$$ 拆成"终点减起点"，而三角形的边首尾相接绕一圈，每个顶点被经过一次"进"、一次"出"，符号自动抵消。

**定义 3.2（有限自由链复形，具体版）** 一列有限秩自由交换群与群同态
$$C_2\xrightarrow{\ \partial_2\ }C_1\xrightarrow{\ \partial_1\ }C_0$$
称为**链复形**，如果 $$\partial_1\circ\partial_2=0$$（"边界的边界为零"）。此时 $$\operatorname{im}\partial_2\subseteq\ker\partial_1$$，可以定义
$$H_1=\ker\partial_1\ /\ \operatorname{im}\partial_2$$
（"闭链"除以"边界"，量出"没被填满的洞"）。

**例 3.2（同一组顶点、边，两种同调）** 取 $$C_1=\mathbb Z\langle e_1,e_2,e_3\rangle$$、$$C_0=\mathbb Z\langle v_1,v_2,v_3\rangle$$、$$\partial_1$$ 如上。

**(i) 有面（$$C_2=\mathbb Z\langle\sigma\rangle$$，填实的三角形）。** 先求 $$\ker\partial_1$$：设 $$ae_1+be_2+ce_3\in\ker\partial_1$$，代入
$$\partial_1(ae_1+be_2+ce_3)=a(v_2-v_1)+b(v_3-v_2)+c(v_3-v_1)=(-a-c)v_1+(a-b)v_2+(b+c)v_3=0,$$
由 $$v_1,v_2,v_3$$ 线性无关得三条方程 $$a+c=0$$、$$a=b$$、$$b+c=0$$；解得 $$a=b=-c$$，即 $$\ker\partial_1=\mathbb Z\cdot(e_1+e_2-e_3)$$。而 $$\operatorname{im}\partial_2=\mathbb Z\cdot\partial_2\sigma=\mathbb Z\cdot(e_1+e_2-e_3)$$——两者**相等**，故 $$H_1=0$$：填实的三角形没有洞。

**(ii) 无面（$$C_2=0$$，只有三条边围成的空心三角形）。** 此时 $$\operatorname{im}\partial_2=0$$（没有 $$\sigma$$ 可用），而 $$\ker\partial_1$$ 仍是上面算出的 $$\mathbb Z\cdot(e_1+e_2-e_3)$$，所以
$$H_1=\ker\partial_1/0\cong\mathbb Z.$$
空心三角形有一个洞——$$H_1\cong\mathbb Z$$ 精确地量出了它。

**这一步预告了第 80 章的哪些内容。** (i)(ii) 的差别只在"$$C_2$$ 是什么"，$$\partial_1,\partial_2$$ 的具体公式完全没变：这正是第 80 章注 3.2 说的"$$D$$ 换了身份，构造逐字相同"的最小版本。而"良定义"（同调不依赖代表元的选取）在这个具体例子里是自动的——$$\ker\partial_1$$、$$\operatorname{im}\partial_2$$ 都是显式算出来的子群，不需要另外验证；第 80 章定理 3.2 的"良定义"证明，做的正是把这一步在一般环、一般链映射下重新核实一遍。

### 3.3 谱：不可逆的点

先把入口题 (c) 算完整。$$T=\begin{pmatrix}2&1\\0&3\end{pmatrix}$$ 是上三角矩阵，特征值就是对角元 $$2,3$$（因为 $$\det(\lambda I-T)=(\lambda-2)(\lambda-3)$$，上三角行列式是对角元之积）。取 $$\lambda=5$$：
$$5I-T=\begin{pmatrix}3&-1\\0&2\end{pmatrix},\qquad \det(5I-T)=3\cdot2-(-1)\cdot0=6\ne0,$$
用 $$2\times2$$ 矩阵求逆公式 $$\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$$：
$$(5I-T)^{-1}=\frac16\begin{pmatrix}2&1\\0&3\end{pmatrix}=\begin{pmatrix}1/3&1/6\\0&1/2\end{pmatrix}.$$

**命题 3.3（有限维预解恒等式，具体版）** 设 $$T$$ 是 $$n\times n$$ 矩阵，$$\lambda,\mu$$ 都不是 $$T$$ 的特征值（记 $$R(\lambda)=(\lambda I-T)^{-1}$$）。则
$$R(\lambda)-R(\mu)=(\mu-\lambda)R(\lambda)R(\mu).$$

**证明**：在恒等式 $$X^{-1}-Y^{-1}=X^{-1}(Y-X)Y^{-1}$$（两边左乘 $$X$$、右乘 $$Y$$ 即验证：$$X\big(X^{-1}(Y-X)Y^{-1}\big)Y=(Y-X)$$，而 $$X(X^{-1}-Y^{-1})Y=Y-X$$，两边相等）中取 $$X=\lambda I-T$$、$$Y=\mu I-T$$，则 $$Y-X=(\mu-\lambda)I$$，代入得 $$R(\lambda)-R(\mu)=(\mu-\lambda)R(\lambda)R(\mu)$$。$$\blacksquare$$

**例 3.3（数字验证）** 取 $$\lambda=5$$、$$\mu=6$$。先算 $$R(6)$$：$$6I-T=\begin{pmatrix}4&-1\\0&3\end{pmatrix}$$，$$\det=12$$，故 $$R(6)=\frac1{12}\begin{pmatrix}3&1\\0&4\end{pmatrix}=\begin{pmatrix}1/4&1/12\\0&1/3\end{pmatrix}$$。左边：
$$R(5)-R(6)=\begin{pmatrix}1/3-1/4&1/6-1/12\\0&1/2-1/3\end{pmatrix}=\begin{pmatrix}1/12&1/12\\0&1/6\end{pmatrix}.$$
右边（$$\mu-\lambda=1$$，故只需算 $$R(5)R(6)$$）：
$$R(5)R(6)=\begin{pmatrix}1/3&1/6\\0&1/2\end{pmatrix}\begin{pmatrix}1/4&1/12\\0&1/3\end{pmatrix}=\begin{pmatrix}1/12&\ 1/36+1/18\\0&1/6\end{pmatrix}=\begin{pmatrix}1/12&1/12\\0&1/6\end{pmatrix}.$$
两边逐项相等，命题 3.3 验证通过。

**这为什么是第 80 章定理 3.3 的雏形。** 有限维时"谱非空"是显然的（特征多项式是复系数多项式，代数基本定理保证有根，谱就是特征值集合）；但无穷维的 Hilbert/Banach 空间上没有"行列式"，"特征多项式"这句话根本无意义。第 80 章要做的，是完全绕开行列式，只用预解恒等式（就是命题 3.3，只是换成算子而不是矩阵）证出"预解式在谱外解析"，再用 Liouville 定理反证谱非空。你在这里手算过一遍的等式，到那里会原样出现，只是矩阵换成有界算子。

### 3.4 域越大，群越小：一个最小的 Galois 对应

先把入口题 (d) 算完整。$$K=\mathbb Q(\sqrt2)$$，$$\mathbb Q$$-自同构只能把 $$\sqrt2$$ 送到 $$x^2-2=0$$ 的根，即 $$\pm\sqrt2$$，所以
$$\operatorname{Gal}(K/\mathbb Q)=\{\mathrm{id},\sigma\},\qquad \sigma(a+b\sqrt2)=a-b\sqrt2\ (a,b\in\mathbb Q).$$
子群只有两个：$$\{\mathrm{id}\}$$ 与 $$G=\{\mathrm{id},\sigma\}$$。固定域：$$K^{\{\mathrm{id}\}}=K$$（恒等映射固定一切）；$$K^G$$ 要求 $$\sigma(a+b\sqrt2)=a+b\sqrt2$$，即 $$a-b\sqrt2=a+b\sqrt2$$，即 $$2b\sqrt2=0$$，即 $$b=0$$，故 $$K^G=\mathbb Q$$。

**定义 3.4（Galois 连接，两元素最小版）** 设 $$P=\{\mathbb Q,K\}$$ 按包含序（$$\mathbb Q\subseteq K$$），$$Q=\{\{\mathrm{id}\},G\}$$ 也按包含序（$$\{\mathrm{id}\}\subseteq G$$）。取
$$F:P\to Q,\quad F(E)=\operatorname{Gal}(K/E);\qquad G_{\mathrm{fix}}:Q\to P,\quad G_{\mathrm{fix}}(H)=K^H.$$
称 $$(F,G_{\mathrm{fix}})$$ 满足**"越大越小"**，如果 $$E\subseteq E'$$ 时 $$F(E)\supseteq F(E')$$（$$P$$ 里变大，$$Q$$ 里变小）。

**例 3.4（逐条验证）** 表列全部数据：

| $$E\in P$$ | $$F(E)=\operatorname{Gal}(K/E)$$ | $$H\in Q$$ | $$G_{\mathrm{fix}}(H)=K^H$$ |
|---|---|---|---|
| $$\mathbb Q$$ | $$G$$ | $$\{\mathrm{id}\}$$ | $$K$$ |
| $$K$$ | $$\{\mathrm{id}\}$$ | $$G$$ | $$\mathbb Q$$ |

"越大越小"在这里只有一组非平凡的包含要检验：$$\mathbb Q\subseteq K$$，对应 $$F(\mathbb Q)=G\supseteq\{\mathrm{id}\}=F(K)$$——的确"域变大，群变小"。

再验证第 80 章定义 3.4 要求的等价式 $$H\subseteq F(E)\iff E\subseteq G_{\mathrm{fix}}(H)$$，四种组合逐一核对：

- $$E=\mathbb Q,H=\{\mathrm{id}\}$$：$$\{\mathrm{id}\}\subseteq G$$ 真；$$\mathbb Q\subseteq K$$ 真——两边都真。
- $$E=\mathbb Q,H=G$$：$$G\subseteq G$$ 真；$$\mathbb Q\subseteq\mathbb Q$$ 真——两边都真。
- $$E=K,H=\{\mathrm{id}\}$$：$$\{\mathrm{id}\}\subseteq\{\mathrm{id}\}$$ 真；$$K\subseteq K$$ 真——两边都真。
- $$E=K,H=G$$：$$G\subseteq\{\mathrm{id}\}$$ **假**（$$G$$ 有两个元素）；$$K\subseteq\mathbb Q$$ **假**（$$K\ne\mathbb Q$$）——两边都假。

四种组合里"真假"逐一对齐，等价式在这个最小例子上成立。

**这为什么是第 80 章定理 3.4 的雏形。** $$\mathbb Q(\sqrt2)$$ 只有两个中间域、两个子群，等价式的四种组合可以逐一穷举验证；第 80 章要做的，是把"逐一穷举"换成对**任意**偏序集、**任意**满足这个等价式的一对反序映射都成立的一般证明（定理 3.4），再套回 $$\mathbb Q(\sqrt2,\sqrt3)$$ 这种子群、中间域各有好几个、不能再穷举的例子。**这里必须提醒一句**：$$Q$$（子群那一边）用的是**标准**包含序，不是反过来的序——"域越大、群越小"这句话说的是 $$F$$ 这个**映射**本身是反序的，不是说要把 $$Q$$ 这个集合的序颠倒过来定义；把两件事混起来是最容易踩的坑。

## 四、几何与物理直觉 (Intuition)

**对偶：从"问答"认识一个东西。** 你没法直接把一个人"倒出来"给别人看，但如果你知道他对**每一个**可能的问题会怎么回答，你其实已经完全掌握了他。数学里"$$V^*$$"就是这种"问答集合"：$$V$$ 里的向量不能直接比较，但每个线性泛函 $$\varphi\in V^*$$ 都是对 $$V$$ 提的一个"问题"（"这个向量在某方向上的分量是多少"），知道向量对**所有**问题的答案，就知道了这个向量本身。而"箭头倒过来"正是因为问答关系天生是倒过来的：你不能"把问题作用在人身上"，只能"让人去回答问题"——箭头的方向从"对象"指向"问题集合"。

**$$D^2=0$$：边界没有边界。** 一个国家的国境线是一条闭合曲线——它本身没有"端点"，因为它首尾相接。这就是"边界的边界为零"最直白的版本：3.2 节里三角形的三条边首尾相接绕一圈，走一圈回到起点，位移之和必然是零。物理上同一件事换个说法就是"没有磁单极子"（$$\operatorname{div}\mathbf B=0$$，第 80 章命题 3.5 会算出来）：磁力线闭合成圈，没有"起点"或"终点"，正因为磁场是某个势的"旋度"，而"旋度的散度恒为零"就是 $$D^2=0$$ 的一个物理化身。

**谱：共振频率。** 推一个秋千，只有在特定频率下推才会让振幅越推越大——这个频率就是系统的"共振点"。数学上，"$$\lambda I-T$$ 不可逆"说的正是"以频率 $$\lambda$$ 驱动系统 $$T$$ 会共振、解会爆掉"；谱 $$\sigma(T)$$ 就是全部共振频率的集合，而"谱非空"翻译成物理直觉就是**任何有界的物理系统都至少有一个共振频率**——3.3 节里 $$\lambda=2,3$$ 让 $$\lambda I-T$$ 不可逆，正是两个"共振点"。

**Galois 连接：要求越多，选择越少。** 一份合同要经过的审批人越多（子群越大），能同时满足所有人要求、保持不变的条款就越少（固定域越小）——这与"域越大、Galois 群越小"是同一个单调关系换了个场景：约束（群）与自由度（域）互相牵制，一边变大，另一边必然变小。第 80 章注 3.4 会指出，这个"审批人数 ↔ 剩余条款数"的关系，换成"覆盖空间的叶数 ↔ 基本群的子群"后是**逐字相同**的定理——这不是类比，是同一条证明。

## 五、经典问题精讲 (Classical Problems)

### 题 1：三个矩阵的转置

**题目**：设 $$A=\begin{pmatrix}1&0\\2&1\end{pmatrix}$$、$$B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$、$$C=\begin{pmatrix}1&1\\0&1\end{pmatrix}$$。分别算出 $$(ABC)^T$$ 与 $$C^TB^TA^T$$，验证相等。

**解**：先算 $$AB=\begin{pmatrix}1&0\\2&1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&1\\1&2\end{pmatrix}$$，再算 $$ABC=\begin{pmatrix}0&1\\1&2\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}=\begin{pmatrix}0&1\\1&3\end{pmatrix}$$。故 $$(ABC)^T=\begin{pmatrix}0&1\\1&3\end{pmatrix}$$（这个矩阵恰好对称，转置后不变）。

另一边：$$C^T=\begin{pmatrix}1&0\\1&1\end{pmatrix}$$、$$B^T=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$、$$A^T=\begin{pmatrix}1&2\\0&1\end{pmatrix}$$。先算 $$C^TB^T=\begin{pmatrix}1&0\\1&1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&1\\1&1\end{pmatrix}$$，再算 $$(C^TB^T)A^T=\begin{pmatrix}0&1\\1&1\end{pmatrix}\begin{pmatrix}1&2\\0&1\end{pmatrix}=\begin{pmatrix}0&1\\1&3\end{pmatrix}$$。

两边相等。$$\blacksquare$$ 这是命题 3.1 用了两次（先把 $$BC$$ 那一对转置、再把 $$A$$ 那一对转置）；练习研1 会把它推广成**任意多个**矩阵的一般命题。

### 题 2：填一个三角形还是两个——同一副骨架，两种洞

**题目**：正方形四个顶点 $$v_1,v_2,v_3,v_4$$，四条边 $$e_1=v_1v_2,e_2=v_2v_3,e_3=v_3v_4,e_4=v_1v_4$$（注意 $$e_4$$ 的方向是 $$v_1\to v_4$$），对角线 $$e_5=v_1v_3$$。**(i)** 若不填任何面（$$C_2=0$$），算出 $$H_1$$。**(ii)** 若用对角线把正方形切成两个三角形 $$\sigma_1=v_1v_2v_3$$、$$\sigma_2=v_1v_3v_4$$ 都填实，算出 $$H_1$$。

**解**：$$\partial_1$$ 的定义是"终点减起点"：$$\partial_1e_1=v_2-v_1,\ \partial_1e_2=v_3-v_2,\ \partial_1e_3=v_4-v_3,\ \partial_1e_4=v_4-v_1,\ \partial_1e_5=v_3-v_1$$。

**(i)** 设 $$x=ae_1+be_2+ce_3+de_4+fe_5\in\ker\partial_1$$（$$C_2=0$$，所以 $$e_5$$ 也在 $$C_1$$ 里，只是本小题里 $$f$$ 允许非零——但下面会看到 $$(i)$$ 的答案不涉及 $$e_5$$，先按只有 $$e_1$$–$$e_4$$ 四条边的正方形骨架算，即令 $$f=0$$ 的子情形）。代入 $$v_1,v_2,v_3,v_4$$ 的系数：
$$\partial_1x=(-a-d)v_1+(a-b)v_2+(b-c)v_3+(c+d)v_4=0.$$
四条方程：$$a+d=0,\ a=b,\ b=c,\ c+d=0$$（第四条与第一条等价）。解得 $$a=b=c=-d$$，一维解空间：$$\ker\partial_1=\mathbb Z\cdot(e_1+e_2+e3-e_4)$$（把 $$a=1$$ 代入）。因为 $$C_2=0$$，$$\operatorname{im}\partial_2=0$$，故
$$H_1=\ker\partial_1\cong\mathbb Z.$$
空心正方形有一个洞，$$e_1+e_2+e_3-e_4$$ 正是绕这个洞一圈的路径。

**(ii)** 现在 $$C_1=\mathbb Z\langle e_1,\dots,e_5\rangle$$（五条边，含对角线），$$C_2=\mathbb Z\langle\sigma_1,\sigma_2\rangle$$。按 3.2 节的规则（绕一圈相加、"回去"那条边取负号）：
$$\partial_2\sigma_1=e_1+e_2-e_5\quad(v_1\to v_2\to v_3\to v_1),\qquad \partial_2\sigma_2=e_5+e_3-e_4\quad(v_1\to v_3\to v_4\to v_1).$$
**先求 $$\ker\partial_1$$（现在允许 $$e_5$$ 出现）。** 设 $$x=ae_1+be_2+ce_3+de_4+fe_5$$，
$$\partial_1x=(-a-d-f)v_1+(a-b)v_2+(b-c+f)v_3+(c+d)v_4=0.$$
四条方程给出 $$b=a,\ d=-c,\ f=c-a$$（第一条方程 $$a+d+f=0$$ 代入 $$d=-c$$ 得 $$f=c-a$$，与第三条方程 $$b-c+f=0$$ 即 $$a-c+f=0$$ 给出的 $$f=c-a$$ 一致，不是独立条件）。故 $$\ker\partial_1$$ 是**二维**的，由 $$a,c$$ 自由取值张成：取 $$(a,c)=(1,0)$$ 得 $$e_1+e_2-e_5$$（正是 $$\partial_2\sigma_1$$！）；取 $$(a,c)=(0,1)$$ 得 $$e_3-e_4+e_5$$（正是 $$\partial_2\sigma_2$$！）。于是
$$\ker\partial_1=\mathbb Z\langle\partial_2\sigma_1,\partial_2\sigma_2\rangle=\operatorname{im}\partial_2,$$
两者**恰好相等**，故
$$H_1=\ker\partial_1/\operatorname{im}\partial_2=0.$$
填实的正方形没有洞。$$\blacksquare$$ **对比**：(i)(ii) 用的是同一套 $$\partial_1$$ 公式，唯一的区别是"有没有 $$C_2$$ 来把 $$\ker\partial_1$$ 商掉"——这正是本章 3.2 节注记里"同一骨架、两种同调"的进阶版：这里甚至能**亲眼看到**两个三角形的边界公式里，对角线 $$e_5$$ 前后符号相反、相加时自动抵消（$$-e_5+e_5=0$$），这就是"填两个三角形"与"填一个正方形"给出同一个边界的代数原因。

### 题 3：一个"缺一个特征向量"的矩阵，谱依然是一个点

**题目**：设 $$T=\begin{pmatrix}2&1\\0&2\end{pmatrix}$$（Jordan 块）。求 $$T$$ 的特征值；分别算出 $$\lambda=5$$ 与 $$\lambda=2$$ 时 $$\lambda I-T$$ 是否可逆。

**解**：$$T$$ 是上三角矩阵，特征值是对角元，即 $$\lambda=2$$（重数 $$2$$，即 $$\det(\lambda I-T)=(\lambda-2)^2$$）。

$$\lambda=5$$：$$5I-T=\begin{pmatrix}3&-1\\0&3\end{pmatrix}$$，$$\det=9\ne0$$，可逆，$$(5I-T)^{-1}=\dfrac19\begin{pmatrix}3&1\\0&3\end{pmatrix}=\begin{pmatrix}1/3&1/9\\0&1/3\end{pmatrix}$$。

$$\lambda=2$$：$$2I-T=\begin{pmatrix}0&-1\\0&0\end{pmatrix}$$，$$\det=0$$，**不可逆**。$$\blacksquare$$

**这道题提醒了一件事，第 80 章会正面处理。** $$T$$ 不是数量矩阵（$$T\ne2I$$），只有一个（不是两个）线性无关的特征向量（$$(1,0)^T$$），但它的谱依然只有一个点 $$\{2\}$$——"谱只有一个点"不等于"矩阵是数量矩阵"，这个区别在有限维靠"特征值的重数"就能说清楚，但第 80 章要问的是**算子**（可能作用在无穷维空间上）什么时候谱退化成一个点、这时候算子长什么样，那里"重数"这个词甚至不一定还有意义。

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 设 $$A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$$、$$B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$。验证 $$(AB)^T=B^TA^T$$。

**基2.** 三角形顶点 $$p,q,r$$，边 $$f_1=pq,\ f_2=qr,\ f_3=pr$$，面 $$\tau=pqr$$，边界规则与正文相同：$$\partial_2\tau=f_1+f_2-f_3$$，$$\partial_1f_i=$$终点$$-$$起点。算出 $$\partial_1(\partial_2\tau)$$。

**基3.** 设 $$T=\begin{pmatrix}1&0\\0&4\end{pmatrix}$$。求特征值，并算出 $$(2I-T)^{-1}$$。

**基4.** 设 $$K=\mathbb Q(\sqrt5)$$。写出 $$\operatorname{Gal}(K/\mathbb Q)$$ 的全部元素、全部子群与每个子群的固定域。

### 竞赛（本课目标难度）

**竞1.** 设 $$T=\begin{pmatrix}1&2\\0&3\end{pmatrix}$$。取 $$\lambda=4,\mu=5$$（都不是特征值），分别算出 $$R(4),R(5)$$，并验证命题 3.3 的预解恒等式 $$R(4)-R(5)=(5-4)R(4)R(5)$$。

**竞2.** 沿用题 2 的正方形骨架，但这次**只填一个三角形** $$\sigma_1=v_1v_2v_3$$（$$C_2=\mathbb Z\langle\sigma_1\rangle$$，不填 $$\sigma_2$$）。算出 $$H_1$$，并用 Euler 示性数 $$\chi=V-E+F$$ 核对你的答案（提示：连通复形有 $$\operatorname{rank}H_0=1$$，若 $$H_2=0$$ 则 $$\chi=\operatorname{rank}H_0-\operatorname{rank}H_1$$）。

**竞3.** 设 $$K=\mathbb Q(i,\sqrt2)$$（$$\mathbb Q$$ 上次数为 $$4$$）。写出 $$\operatorname{Gal}(K/\mathbb Q)$$ 的全部 $$4$$ 个元素，找出全部 $$3$$ 个非平凡真子群，并对每个子群求出固定域（提示：其中一个固定域是 $$\mathbb Q(\sqrt{-2})=\mathbb Q(i\sqrt2)$$）。

### 研究（通向下一章）

**研1.** 把题 1 推广到任意多个矩阵：证明对任意 $$k\ge2$$ 个形状匹配的矩阵 $$A_1,\dots,A_k$$，$$(A_1A_2\cdots A_k)^T=A_k^T\cdots A_2^TA_1^T$$。

**研2.** 四面体（$$3$$-单形）有顶点 $$v_0,v_1,v_2,v_3$$，$$4$$ 个面（$$2$$-单形，去掉一个顶点）、$$6$$ 条边、$$1$$ 个体（$$3$$-单形本身）。标准边界公式是"轮流去掉一个顶点、符号交替"：
$$\partial_3[v_0v_1v_2v_3]=[v_1v_2v_3]-[v_0v_2v_3]+[v_0v_1v_3]-[v_0v_1v_2],$$
$$\partial_2[v_iv_jv_k]=[v_jv_k]-[v_iv_k]+[v_iv_j]\quad(i<j<k).$$
算出 $$\partial_2(\partial_3[v_0v_1v_2v_3])$$，验证它等于零。

### 解答 (Solutions)

**解 基1.** $$AB=\begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}2&1\\4&3\end{pmatrix}$$，故 $$(AB)^T=\begin{pmatrix}2&4\\1&3\end{pmatrix}$$。$$A^T=\begin{pmatrix}1&3\\2&4\end{pmatrix}$$，$$B^T=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$，$$B^TA^T=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&3\\2&4\end{pmatrix}=\begin{pmatrix}2&4\\1&3\end{pmatrix}$$。两边相等。$$\blacksquare$$

**解 基2.** $$\partial_1(\partial_2\tau)=\partial_1(f_1+f_2-f_3)=(q-p)+(r-q)-(r-p)=q-p+r-q-r+p=0$$（逐项相消：$$q$$ 出现 $$+1-1=0$$ 次，$$p$$ 出现 $$-1+1=0$$ 次，$$r$$ 出现 $$+1-1=0$$ 次）。$$\blacksquare$$

**解 基3.** $$T$$ 对角，特征值 $$1,4$$。$$2I-T=\begin{pmatrix}1&0\\0&-2\end{pmatrix}$$，$$\det=-2\ne0$$，$$(2I-T)^{-1}=\begin{pmatrix}1&0\\0&-1/2\end{pmatrix}$$。

**解 基4.** $$\mathbb Q$$-自同构只能把 $$\sqrt5$$ 送到 $$x^2-5=0$$ 的另一根 $$\pm\sqrt5$$，故 $$\operatorname{Gal}(K/\mathbb Q)=\{\mathrm{id},\sigma\}$$（$$\sigma(a+b\sqrt5)=a-b\sqrt5$$）。子群只有 $$\{\mathrm{id}\}$$ 与整个群 $$G$$。$$K^{\{\mathrm{id}\}}=K$$；$$K^G$$ 要求 $$a-b\sqrt5=a+b\sqrt5$$，即 $$b=0$$，故 $$K^G=\mathbb Q$$。$$\blacksquare$$（与入口题 (d) 逐字同构，只是把 $$2$$ 换成了 $$5$$。）

**解 竞1.** $$4I-T=\begin{pmatrix}3&-2\\0&1\end{pmatrix}$$，$$\det=3$$，$$R(4)=\dfrac13\begin{pmatrix}1&2\\0&3\end{pmatrix}=\begin{pmatrix}1/3&2/3\\0&1\end{pmatrix}$$。$$5I-T=\begin{pmatrix}4&-2\\0&2\end{pmatrix}$$，$$\det=8$$，$$R(5)=\dfrac18\begin{pmatrix}2&2\\0&4\end{pmatrix}=\begin{pmatrix}1/4&1/4\\0&1/2\end{pmatrix}$$。

左边：$$R(4)-R(5)=\begin{pmatrix}1/3-1/4&2/3-1/4\\0&1-1/2\end{pmatrix}=\begin{pmatrix}1/12&5/12\\0&1/2\end{pmatrix}$$。

右边：$$R(4)R(5)=\begin{pmatrix}1/3&2/3\\0&1\end{pmatrix}\begin{pmatrix}1/4&1/4\\0&1/2\end{pmatrix}=\begin{pmatrix}1/12&1/12+1/3\\0&1/2\end{pmatrix}=\begin{pmatrix}1/12&5/12\\0&1/2\end{pmatrix}$$（$$1/12+1/3=1/12+4/12=5/12$$）。$$\mu-\lambda=1$$，故右边就是 $$R(4)R(5)$$ 本身。两边相等。$$\blacksquare$$

**解 竞2.** 沿用题 2 (ii) 的 $$\ker\partial_1$$（五条边，二维：$$\ker\partial_1=\mathbb Z\langle e_1+e_2-e_5,\ e_3-e_4+e_5\rangle$$）。现在 $$\operatorname{im}\partial_2=\mathbb Z\cdot\partial_2\sigma_1=\mathbb Z\cdot(e_1+e_2-e_5)$$，是 $$\ker\partial_1$$ 里的一个**一维**子群（$$\ker\partial_1$$ 本身二维）。商群
$$H_1=\ker\partial_1/\operatorname{im}\partial_2\cong\mathbb Z$$
（二维格去掉一维子格，商仍是秩为 $$1$$ 的自由群——用 $$e_3-e_4+e_5$$ 的像作为生成元）。

**Euler 示性数核对**：$$V=4,\ E=5,\ F=1$$（只有 $$\sigma_1$$），$$\chi=4-5+1=0$$。连通复形 $$\operatorname{rank}H_0=1$$；若 $$H_2=0$$（这里显然成立，$$C_3=0$$），则 $$\chi=\operatorname{rank}H_0-\operatorname{rank}H_1+\operatorname{rank}H_2=1-\operatorname{rank}H_1$$，即 $$\operatorname{rank}H_1=1-\chi=1-0=1$$，与 $$H_1\cong\mathbb Z$$（秩 $$1$$）吻合。$$\blacksquare$$ 几何上：$$\sigma_2$$ 那半个正方形没填，剩下的洞就是它。

**解 竞3.** $$K=\mathbb Q(i,\sqrt2)$$，$$[K:\mathbb Q]=4$$（$$\sqrt2\notin\mathbb Q(i)$$，因为 $$\mathbb Q(i)$$ 里的元素平方后虚部为零当且仅当原数是实数或纯虚数，$$\sqrt2$$ 不满足 $$x^2=2$$ 在 $$\mathbb Q(i)$$ 内有解——可用范数论证：若 $$a+bi\in\mathbb Q(i)$$ 满足 $$(a+bi)^2=2$$，则 $$a^2-b^2=2,2ab=0$$，$$b=0$$ 时 $$a^2=2$$ 无有理解，$$a=0$$ 时 $$-b^2=2$$ 无解）。

$$\mathbb Q$$-自同构由 $$i\mapsto\pm i$$、$$\sqrt2\mapsto\pm\sqrt2$$ 两个独立选择确定，共 $$4$$ 个：
$$\mathrm{id},\quad \sigma:(i,\sqrt2)\mapsto(-i,\sqrt2),\quad \tau:(i,\sqrt2)\mapsto(i,-\sqrt2),\quad \sigma\tau:(i,\sqrt2)\mapsto(-i,-\sqrt2).$$
（$$\sigma^2=\tau^2=\mathrm{id}$$，$$\sigma\tau=\tau\sigma$$，故 $$\operatorname{Gal}(K/\mathbb Q)\cong\mathbb Z/2\times\mathbb Z/2$$，**不是**循环群——这与入口题 (d)、基4 的循环情形不同，是本题特意选的地方。）

三个非平凡真子群都是二阶的：$$\langle\sigma\rangle=\{\mathrm{id},\sigma\}$$、$$\langle\tau\rangle=\{\mathrm{id},\tau\}$$、$$\langle\sigma\tau\rangle=\{\mathrm{id},\sigma\tau\}$$。

固定域：$$K^{\langle\sigma\rangle}$$——$$\sigma$$ 固定 $$\sqrt2$$、翻转 $$i$$，故固定 $$a+b\sqrt2$$（$$a,b\in\mathbb Q$$）这类元素，即 $$K^{\langle\sigma\rangle}=\mathbb Q(\sqrt2)$$。$$K^{\langle\tau\rangle}$$——$$\tau$$ 固定 $$i$$、翻转 $$\sqrt2$$，故 $$K^{\langle\tau\rangle}=\mathbb Q(i)$$。$$K^{\langle\sigma\tau\rangle}$$——$$\sigma\tau$$ 同时翻转 $$i$$ 与 $$\sqrt2$$，乘积 $$i\sqrt2$$ 两个负号抵消，$$\sigma\tau(i\sqrt2)=(-i)(-\sqrt2)=i\sqrt2$$ 不变，故 $$K^{\langle\sigma\tau\rangle}=\mathbb Q(i\sqrt2)=\mathbb Q(\sqrt{-2})$$。$$\blacksquare$$

三个二阶子群对应三个二次中间域 $$\mathbb Q(\sqrt2),\mathbb Q(i),\mathbb Q(\sqrt{-2})$$——这正是第 80 章要处理的"子群不止一条链"的最小样本：入口题 (d) 的 $$\mathbb Q(\sqrt2)/\mathbb Q$$ 只有一条平凡的包含链，这里第一次看到"树状"的子群格。

**解 研1.** 对 $$k$$ 用数学归纳法。**基础情形** $$k=2$$ 就是命题 3.1。**归纳步骤**：设结论对 $$k-1$$ 个矩阵成立，即 $$(A_1\cdots A_{k-1})^T=A_{k-1}^T\cdots A_1^T$$。把 $$A_1\cdots A_k$$ 看成两块相乘：$$(A_1\cdots A_{k-1})\cdot A_k$$，对这两块用命题 3.1（$$k=2$$ 的情形）：
$$(A_1\cdots A_k)^T=\big((A_1\cdots A_{k-1})A_k\big)^T=A_k^T\,(A_1\cdots A_{k-1})^T=A_k^T\,(A_{k-1}^T\cdots A_1^T)=A_k^T A_{k-1}^T\cdots A_1^T$$
（第二步用命题 3.1，第三步用归纳假设）。$$\blacksquare$$ 第 80 章会把这个归纳法原样搬到"任意范畴里 $$k$$ 个箭头的复合"上，命题 3.1 对应的正是那里定理 3.1 的 $$k=2$$ 情形。

**解 研2.** 按公式逐项展开（$$3.2$$ 节三角形算过 $$n=2$$ 情形，这里是 $$n=3$$）：
$$\partial_2(\partial_3[v_0v_1v_2v_3])=\partial_2[v_1v_2v_3]-\partial_2[v_0v_2v_3]+\partial_2[v_0v_1v_3]-\partial_2[v_0v_1v_2]$$
$$=([v_2v_3]-[v_1v_3]+[v_1v_2])-([v_2v_3]-[v_0v_3]+[v_0v_2])+([v_1v_3]-[v_0v_3]+[v_0v_1])-([v_1v_2]-[v_0v_2]+[v_0v_1]).$$
按边分类合并系数：
- $$[v_2v_3]$$：第 1 项 $$+1$$、第 2 项 $$-1$$，合计 $$0$$；
- $$[v_1v_3]$$：第 1 项 $$-1$$、第 3 项 $$+1$$，合计 $$0$$；
- $$[v_1v_2]$$：第 1 项 $$+1$$、第 4 项 $$-1$$，合计 $$0$$；
- $$[v_0v_3]$$：第 2 项 $$+1$$（$$-(-[v_0v_3])$$）、第 3 项 $$-1$$，合计 $$0$$；
- $$[v_0v_2]$$：第 2 项 $$-1$$、第 4 项 $$+1$$，合计 $$0$$；
- $$[v_0v_1]$$：第 3 项 $$+1$$、第 4 项 $$-1$$，合计 $$0$$。

六条边的系数全部为零，故 $$\partial_2(\partial_3[v_0v_1v_2v_3])=0$$。$$\blacksquare$$ 与 3.2 节三角形的情形对比：$$n=2$$ 时三条边两两相消，$$n=3$$ 时六条边两两相消——**每去掉两个顶点，恰好有两种去法（先去大的再去小的、先去小的再去大的），两条路径符号相反**，这正是第 80 章定理 3.2 对**一般** $$n$$ 证明 $$\partial_{n-1}\circ\partial_n=0$$ 时"符号交替求和"这套记号真正要处理的组合机制——这里的六项两两抵消，是那个一般证明里 $$\binom{n+1}{2}$$ 对抵消项的一个具体、可以逐项数出来的实例。

## 七、Takeaway 与延伸 (Takeaways)

1. **"转置反转合成顺序"不是线性代数的孤立技巧，是"反变"这个概念的胚胎。** 题 1、研 1 把它从两个矩阵推广到任意多个——第 80 章要做的最后一步，只是把"矩阵乘法"换成"任意范畴里的箭头复合"，命题就长成了"反变函子/对偶范畴"的定义本身。

2. **同一套边界公式 $$\partial_k$$，填不填某一层"面"，直接决定同调群是零还是非零。** 题 2、竞 2 用同一个正方形骨架，只改变"填几个三角形"，就让 $$H_1$$ 在 $$\mathbb Z$$、$$0$$ 之间跳来跳去——这正是"洞"这个几何直觉被同调群精确量化的样子；研 2 验证了同一个"边界的边界为零"的机制，从三角形（$$2$$ 条边抵消 $$3$$ 组）升到四面体（$$6$$ 条边抵消 $$4$$ 组）时**符号交替**这件事本身没有变。

3. **谱是"不可逆的点"，不是"特征值"的同义词——题 3 是这句话第一次露出破绽的地方。** $$T=\begin{pmatrix}2&1\\0&2\end{pmatrix}$$ 只有一个特征方向，谱却依然规规矩矩地只有一个点：说明"谱"这个概念从一开始就该用"$$\lambda I-T$$ 不可逆"来定义，而不是"特征方程的根"——后者在无穷维根本没有意义，前者才是能推广的定义。

4. **子群格从"一条链"变成"一棵树"，Galois 对应也依然逐条成立。** 竞 3 的 $$\mathbb Q(i,\sqrt2)/\mathbb Q$$ 第一次给出三个平级的中间域——这是第 80 章要处理的真正困难：入口题 (d) 那种"只有一条链"的情形，反序对应是显然的；子群格变复杂之后，"越大越小"这条单调关系还成立吗？（答案是成立，但需要真正的证明，不能再靠穷举。）

5. **四道题背后是同一件事：把"具体算一遍、发现规律"升级成"对一般情形证明规律"。** 这正是全书从第 01 章到这里反复使用的方法——第 80 章不会引入新的方法论，只会把这套方法论用在"对偶范畴""任意环上的链复形""Banach 空间上的算子""任意偏序集"这四个更大的舞台上。

**下一章的悬念。** 本章的每一个"证明"都靠的是**穷举**或**直接展开**——矩阵是具体的、三角形/正方形是具体的、$$T$$ 是 $$2\times2$$ 的、$$\mathbb Q(\sqrt2)$$ 只有两个子群。第 80 章要问：去掉"具体"两个字，这四条陈述还成立吗？对**任意**范畴、**任意**环上的模、**任意**（可能无穷维、没有"行列式"这种工具的）Banach 空间、**任意**偏序集，同样的结论要怎么证？读完第 80 章，你会看到：本章手算的每一步，都能在更大的舞台上找到逐字对应的一步——这正是全书想让你亲眼看到的事：现代数学从来不是凭空发明新方法，而是把同一批"具体算过的招数"，用得越来越远。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch78_Galois群与Galois对应_下.md">← 第78章 Galois 群与 Galois 对应·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch80_尾声_从Galois到现代数学_下.md">第80章 尾声：从 Galois 到现代数学·下 →</a></div>
</div>
