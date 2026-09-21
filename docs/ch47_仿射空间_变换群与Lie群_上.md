---
layout: default
---

# 第47章: 仿射空间、变换群与 Lie 群·上：预备与直觉 (Affine Spaces, Transformation Groups and Lie Groups · Part I: Warm-up and Intuition)

> 配套深化: 见 第48章 仿射空间、变换群与 Lie 群·下（完整推导），本章是它的具体铺垫，建议先读本章
> 对应原专栏: MP30
> 专家依据: `_experts/algebra/lie-algebra-root-systems.md`（主）+ `_experts/algebra/_SKILL.md`
> 知识库依据: `opc2/knowledge/math/李群/lie-groups/`（15 篇）、`opc2/knowledge/math/几何力学/marsden-mech-sym/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

第48章用一节处理仿射空间，用一节处理"仿射变换怎么写成矩阵"，再用一节给出李群的定义，然后用两节把"求导"变成"代数"，最后一节把整个群本身看成一个丛。对认真的普通自学者来说，这条链里至少有四步压缩得太快：为什么点不能相加、却可以相减；一个仿射变换凭什么能"升一维"变成一个方阵；判断一个群是不是李群时，为什么只需要检查一个映射光滑而不是两个；以及最要命的一步——两个矩阵的换位子 $$AB-BA$$ 为什么恰好就是后面要反复用的"李括号"，而不是别的什么组合。

本章的任务只有一个：把这四步，每一步都先用两三组具体数字算一遍，让你在看到第48章的一般定义与证明之前，已经用手把它们算过。读完本章，你应该能不看书直接完成四件事：算出任意两点之差、把一个具体的"旋转加平移"写成 $$3\times3$$ 齐次矩阵、验证 $$SO(2)$$ 中两个具体角度相乘确实给出角度相加、以及算出一对具体矩阵的换位子。第48章要做的，只是把这些具体计算里"为什么总是对的"那一部分抽出来，写成一般定义和证明——读完本章再读第48章，你会发现那里的每一步都是本章手算过程的符号化重述。

## 二、入口：一道具体的问题 (Entry Problem)

以下三问分别是第48章入口题 (a)(b)(c) 的简化/预热版：数字更小、只要求算出答案或猜出规律，不要求给出一般证明。

### 问题 A：两点相加，得到的是什么

平面上取两点 $$P=(2,-1)$$、$$Q=(5,3)$$。按坐标直接相加得 $$P+Q=(7,2)$$。现在把整张图连同两点一起平移：新原点选在旧坐标 $$(10,10)$$ 处，于是新坐标下 $$P'=P-(10,10)=(-8,-11)$$、$$Q'=Q-(10,10)=(-5,-7)$$。请分别算出 $$P+Q$$（旧坐标）与 $$P'+Q'$$（新坐标），把 $$P'+Q'$$ 换算回旧坐标系（即再加上 $$(10,10)$$），与 $$P+Q$$ 比较：一样吗？再算 $$Q-P$$ 与 $$Q'-P'$$，看看这一次换原点前后是否一样。

### 问题 B：能不能只用一个矩阵

设 $$R$$ 是绕原点逆时针转 $$90^\circ$$ 的旋转（$$2\times2$$ 矩阵），$$T$$ 是把每个点搬到"自身 $$+(1,2)$$"的平移。把 $$f=T\circ R$$（先转后搬）作用在具体点 $$x_0=(3,0)$$ 上，算出 $$f(x_0)$$。再问：能不能找到一个 $$2\times2$$ 矩阵 $$M$$，使 $$f(x)=Mx$$ 对一切 $$x$$ 成立？（提示：先算 $$f(0,0)$$，一个 $$2\times2$$ 矩阵乘任何输入都会把 $$(0,0)$$ 送到哪里？）

### 问题 C：转两次，顺序重要吗

设 $$E=\begin{bmatrix}0&1\\0&0\end{bmatrix}$$、$$F=\begin{bmatrix}0&0\\1&0\end{bmatrix}$$。这两个矩阵满足 $$E^2=F^2=\mathbf{0}$$（自己核对一下），所以 $$I+tE$$ 与 $$I+sF$$（$$s,t\in\mathbb{R}$$）分别恰好等于幂级数 $$\sum_k(tE)^k/k!$$ 与 $$\sum_k(sF)^k/k!$$ 的和（后面所有更高次项都是零矩阵）。请算出 $$(I+sF)(I+tE)$$ 与 $$(I+tE)(I+sF)$$ 这两个乘积，看它们是否相等；如果不相等，两者之差是什么样子的一个矩阵（关于 $$s,t$$ 是几次的）？

问题 A 在问"点的和"有没有意义；问题 B 在问"仿射变换"能不能矩阵化；问题 C 在问"矩阵相乘的顺序"差多少、差出来的东西长什么样——这正是第48章要把"换位子"叫作"李括号"的起点。第三节的内容就是把这三问的答案，从具体数字算成一般结论。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 仿射空间：先算两点之差，再问"点的和"有没有意义

先回答问题 A。$$P+Q=(2+5,\,-1+3)=(7,2)$$。换了原点之后，$$P'+Q'=(-8+(-5),\,-11+(-7))=(-13,-18)$$，换算回旧坐标系是 $$(-13,-18)+(10,10)=(-3,-8)$$。这与 $$P+Q=(7,2)$$ **不一样**——"点加点"的结果依赖你选哪个点当原点，换一个原点答案就变了，所以它不是一个有内在意义的运算。

再看差：$$Q-P=(5-2,\,3-(-1))=(3,4)$$；换原点后 $$Q'-P'=(-5-(-8),\,-7-(-11))=(3,4)$$——**完全一样**。这不是巧合：差是两次减法，原点被减没了；和是没有减法保护的裸相加，原点的位置会直接掺进结果里。

**再用一个不同的日常例子把这件事说第二遍。** 时刻不能相加：下午 3 点整与下午 5 点整，"3 点 + 5 点"没有意义（你选正午为 0 点还是选午夜为 0 点，数值上的和会不一样）。但时长可以加到时刻上：3 点再过 2 小时是 5 点，这件事与你怎么给时钟编号无关——"3 点"加"2 小时"永远得到同一个钟点。这正是问题 A 的规律：**位置之间只能相减不能相加，位置与位移之间可以相加。**

现在把这条规律写成公理。设 $$A$$ 是位置的集合（如全体时刻、全体空间点），$$V$$ 是位移的集合（如全体时长、全体空间向量），它本身是一个 $$\mathbb{R}$$ 上的向量空间。若有映射 $$A\times V\to A$$，$$(p,v)\mapsto p+v$$（"位置加位移"），满足

(A1) 对一切 $$p\in A$$，$$p+0=p$$（不移动就是不变）；

(A2) 对一切 $$p\in A$$、$$u,v\in V$$，$$(p+u)+v=p+(u+v)$$（先挪 $$u$$ 再挪 $$v$$，等于一次性挪 $$u+v$$）；

(A3) 对任意 $$p,q\in A$$，存在唯一的 $$v\in V$$ 使 $$p+v=q$$（任意两个位置之间恰有一个位移把前者搬到后者）；

则称 $$A$$ 是**仿射空间 (affine space)**，$$V$$ 是它的**自由向量空间 (space of free vectors)**。(A3) 里那个唯一的 $$v$$ 记作 $$q-p$$——这就是"为什么需要 $$q-p$$ 这个记号"：它不是从向量空间里借来的减法，而是 (A3) 唯一性直接定义出来的一个新记号，只是恰好满足减法该有的样子。

**定义 3.1（仿射空间, affine space）**。同上：$$A$$ 非空集合，$$V$$ 是 $$\mathbb{R}$$-向量空间，映射 $$A\times V\to A$$ 满足 (A1)(A2)(A3)。

用问题 A 的数字直接核对 (A1)(A2)(A3) 在 $$A=V=\mathbb{R}^2$$（坐标加法）下都成立不难；下面证一条马上要用的性质。

**定理 3.2（差向量的加法律）**。在定义 3.1 下，对任意 $$p,q,r\in A$$，$$(q-p)+(r-q)=r-p$$。

证明。记 $$v=q-p$$、$$w=r-q$$，即 $$p+v=q$$、$$q+w=r$$（由 (A3) 的定义）。于是

$$p+(v+w)=(p+v)+w=q+w=r,$$

第一步用 (A2)，第二、三步用刚才两条等式。这说明 $$v+w$$ 就是那个把 $$p$$ 搬到 $$r$$ 的位移；由 (A3) 的**唯一性**，$$v+w$$ 必须等于 $$r-p$$（$$r-p$$ 本身就定义为"唯一把 $$p$$ 搬到 $$r$$ 的位移"）。故 $$(q-p)+(r-q)=r-p$$。$$\blacksquare$$

**例 3.2（用问题 A 的数字核对定理 3.2）**。取 $$p=P=(2,-1)$$、$$q=Q=(5,3)$$、再取 $$r=(6,6)$$。$$q-p=(3,4)$$（已算过）；$$r-q=(6-5,6-3)=(1,3)$$；两者相加 $$(3,4)+(1,3)=(4,7)$$。直接算 $$r-p=(6-2,6-(-1))=(4,7)$$——吻合。这条恒等式说的是"分两步挪与一步挪到底是一回事"，在日常语言里就是"上午 9 点到中午 12 点是 3 小时，中午 12 点到下午 2 点是 2 小时，上午 9 点到下午 2 点就是 $$3+2=5$$ 小时"。

第48章 定义 3.1、定理 3.1 是这里的一般版本（那里还多证了 $$p-p=0$$、$$(p+v)-p=v$$ 两条，都是同一套论证，留给那一章）。

### 3.2 仿射变换：先手算一个具体的"转+搬"，再问它能不能矩阵化

回到问题 B。$$R=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$$（$$90^\circ$$ 旋转），作用在 $$x_0=(3,0)$$ 上：

$$Rx_0=\begin{bmatrix}0&-1\\1&0\end{bmatrix}\begin{bmatrix}3\\0\end{bmatrix}=\begin{bmatrix}0\cdot3+(-1)\cdot0\\1\cdot3+0\cdot0\end{bmatrix}=\begin{bmatrix}0\\3\end{bmatrix}.$$

再平移 $$(1,2)$$：$$f(x_0)=(0,3)+(1,2)=(1,5)$$。

能不能找到单个 $$2\times2$$ 矩阵 $$M$$ 使 $$f(x)=Mx$$？先看 $$f(0,0)$$：$$R(0,0)=(0,0)$$，再加 $$(1,2)$$ 得 $$f(0,0)=(1,2)$$。而任何 $$2\times2$$ 矩阵 $$M$$ 都满足 $$M(0,0)=(0,0)$$（矩阵乘法是线性的，线性映射必把零送到零）。$$f(0,0)=(1,2)\neq(0,0)$$，所以**不存在**这样的 $$M$$——只要变换里带平移，它就不是线性映射，就不能用一个同维数矩阵乘出来。这就是"需要新记号"的地方：我们想要的是"比线性映射多一点点"的东西，而"多的那一点"恰好是一个向量 $$b$$。

**升一维的办法**：把平面上的点 $$(x,y)$$ 记成三元组 $$(x,y,1)$$（多加一个恒为 $$1$$ 的坐标，这就是"齐次坐标"这个记号存在的理由——那个额外的 $$1$$ 就是用来"吃住"平移项的），把 $$f$$ 对应到

$$\widehat f=\begin{bmatrix}0&-1&1\\1&0&2\\0&0&1\end{bmatrix}.$$

验证：

$$\widehat f\begin{bmatrix}3\\0\\1\end{bmatrix}=\begin{bmatrix}0\cdot3+(-1)\cdot0+1\cdot1\\1\cdot3+0\cdot0+2\cdot1\\0+0+1\end{bmatrix}=\begin{bmatrix}1\\5\\1\end{bmatrix}.$$

前两个坐标正是 $$(1,5)=f(x_0)$$——升一维之后，"转+搬"确实变成了单纯的矩阵乘法。

**再核对一次复合是否对应矩阵相乘。** 设 $$g$$ 是"再平移 $$(0,-5)$$"，即 $$g(x)=x+(0,-5)$$。先直接算复合 $$g\circ f$$（先 $$f$$ 后 $$g$$）:

$$(g\circ f)(x)=f(x)+(0,-5)=Rx+(1,2)+(0,-5)=Rx+(1,-3).$$

它的齐次矩阵应该是 $$\widehat{g\circ f}=\begin{bmatrix}0&-1&1\\1&0&-3\\0&0&1\end{bmatrix}$$（线性部分不变，平移换成 $$(1,-3)$$）。再用矩阵乘法算 $$\widehat g\,\widehat f$$（$$\widehat g=\begin{bmatrix}1&0&0\\0&1&-5\\0&0&1\end{bmatrix}$$）：

$$\widehat g\,\widehat f=\begin{bmatrix}1&0&0\\0&1&-5\\0&0&1\end{bmatrix}\begin{bmatrix}0&-1&1\\1&0&2\\0&0&1\end{bmatrix}=\begin{bmatrix}0&-1&1\\1&0&2-5\\0&0&1\end{bmatrix}=\begin{bmatrix}0&-1&1\\1&0&-3\\0&0&1\end{bmatrix}.$$

与直接算的 $$\widehat{g\circ f}$$ 完全一致——**复合仿射变换对应齐次矩阵相乘**，且顺序是"先作用的那个矩阵写在右边"。

**定义 3.3（仿射变换的齐次矩阵表示）**。对 $$\mathbb{R}^n$$ 上的仿射变换 $$f(x)=Mx+b$$（$$M\in GL(n,\mathbb{R})$$、$$b\in\mathbb{R}^n$$），定义 $$(n+1)\times(n+1)$$ 矩阵

$$\widehat f=\begin{bmatrix}M&b\\0&1\end{bmatrix}.$$

**定理 3.4（矩阵化是同态）**。$$\widehat{f\circ g}=\widehat f\,\widehat g$$（复合对应矩阵相乘），$$\widehat{\mathrm{id}}=I_{n+1}$$，且 $$f\mapsto\widehat f$$ 是单射。

证明。设 $$f(x)=Mx+b$$、$$g(x)=M'x+b'$$。直接展开分块矩阵乘法：

$$\widehat f\widehat g=\begin{bmatrix}M&b\\0&1\end{bmatrix}\begin{bmatrix}M'&b'\\0&1\end{bmatrix}=\begin{bmatrix}MM'&Mb'+b\\0&1\end{bmatrix}.$$

而 $$(f\circ g)(x)=f(M'x+b')=M(M'x+b')+b=MM'x+(Mb'+b)$$，其齐次矩阵正是 $$\begin{bmatrix}MM'&Mb'+b\\0&1\end{bmatrix}$$，与 $$\widehat f\widehat g$$ 相同（这正是上面用具体 $$f,g$$ 核对过的那步，这里只是把数字换成了字母）。$$\widehat{\mathrm{id}}$$ 对应 $$M=I,b=0$$，即 $$I_{n+1}$$。单射性：从 $$\widehat f$$ 的分块形状直接读出 $$M,b$$，不同的 $$(M,b)$$ 给出不同的矩阵。$$\blacksquare$$

第48章定理 3.7 就是这条定理的一般版本（那里还补了逆矩阵公式与"像恰好是哪些矩阵"两件事，本章不需要）。

### 3.3 判断"能不能乘得光滑"：先在 $$SO(2)$$ 里代两个具体角度

回答问题 C 之前，先处理"群乘法光不光滑"这件事——这是李群定义里最不直观的一条。取两个具体角度 $$\alpha=\pi/6$$（$$30^\circ$$）、$$\beta=\pi/3$$（$$60^\circ$$），

$$R(\alpha)=\begin{bmatrix}\frac{\sqrt3}{2}&-\frac12\\[2pt]\frac12&\frac{\sqrt3}{2}\end{bmatrix},\qquad R(\beta)=\begin{bmatrix}\frac12&-\frac{\sqrt3}{2}\\[2pt]\frac{\sqrt3}{2}&\frac12\end{bmatrix}.$$

逐项算乘积 $$R(\alpha)R(\beta)$$：

$$(1,1)\ \text{项}:\ \frac{\sqrt3}{2}\cdot\frac12+\Bigl(-\frac12\Bigr)\cdot\frac{\sqrt3}{2}=\frac{\sqrt3}{4}-\frac{\sqrt3}{4}=0,$$

$$(1,2)\ \text{项}:\ \frac{\sqrt3}{2}\cdot\Bigl(-\frac{\sqrt3}{2}\Bigr)+\Bigl(-\frac12\Bigr)\cdot\frac12=-\frac34-\frac14=-1,$$

$$(2,1)\ \text{项}:\ \frac12\cdot\frac12+\frac{\sqrt3}{2}\cdot\frac{\sqrt3}{2}=\frac14+\frac34=1,$$

$$(2,2)\ \text{项}:\ \frac12\cdot\Bigl(-\frac{\sqrt3}{2}\Bigr)+\frac{\sqrt3}{2}\cdot\frac12=-\frac{\sqrt3}{4}+\frac{\sqrt3}{4}=0.$$

于是 $$R(\alpha)R(\beta)=\begin{bmatrix}0&-1\\1&0\end{bmatrix}=R(\pi/2)$$——正是 $$\alpha+\beta=\pi/2$$ 对应的旋转。这不是巧合：把上面四个式子换成字母 $$\alpha,\beta$$ 重新写一遍，用到的其实是和角公式 $$\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$$ 和 $$\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$$；乘积矩阵的四个入口，永远等于 $$\cos(\alpha+\beta),-\sin(\alpha+\beta),\sin(\alpha+\beta),\cos(\alpha+\beta)$$，而 $$\cos,\sin$$ 都是光滑函数，所以"两个角度相乘"这件事，落到坐标里就是"把 $$\alpha,\beta$$ 喂进 $$\cos,\sin$$"——**天生光滑**，不需要额外证明。

这条观察提示我们：判断一个群是不是"能光滑地乘"，不必分别检查"乘法光滑"和"求逆光滑"两件事，检查一个映射就够了。定义

$$\sigma(x,y)=x^{-1}y.$$

在 $$SO(2)$$ 的例子里，$$\sigma(\alpha,\beta)=R(\alpha)^{-1}R(\beta)=R(-\alpha)R(\beta)=R(\beta-\alpha)$$，在坐标（角度）里就是 $$(\alpha,\beta)\mapsto\beta-\alpha$$——**是最简单的光滑函数，减法本身**。

**定义 3.5（Lie 群，简化版）**。集合 $$G$$ 若同时是群、是光滑流形，且乘法 $$\mu(x,y)=xy$$ 与求逆 $$\iota(x)=x^{-1}$$ 都是光滑映射，则称 $$G$$ 是 **Lie 群 (Lie group)**。（"光滑流形"的严格定义是第10章的内容；这里只需要知道"局部能用光滑函数写坐标"就够了——$$SO(2)$$ 用角度 $$\theta$$ 当坐标，$$\mathbb{R}^2$$ 用 $$(x,y)$$ 当坐标，都是这个意思。）

**定理 3.6（一个映射就够）**。在"$$G$$ 是群 + 光滑流形"的前提下，"$$\mu,\iota$$ 都光滑"等价于"$$\sigma(x,y)=x^{-1}y$$ 光滑"。

证明。若 $$\mu,\iota$$ 都光滑，则 $$\sigma(x,y)=\mu(\iota(x),y)$$ 是光滑映射的复合，光滑。反过来，若 $$\sigma$$ 光滑：取 $$x=e$$（单位元），$$\iota(y)=\sigma(e,y)$$，是 $$\sigma$$ 固定一个变量后的映射，光滑；又 $$xy=\sigma(\iota(x),y)$$（因为 $$\sigma(\iota(x),y)=\iota(x)^{-1}y=xy$$），由 $$\iota$$ 与 $$\sigma$$ 都光滑知 $$\mu$$ 光滑。$$\blacksquare$$

**例 3.6（回到具体数字）**。上面算的 $$\sigma(\pi/6,\pi/3)=\pi/3-\pi/6=\pi/6$$，对应 $$R(\pi/6)$$；直接核对：$$R(\pi/6)^{-1}R(\pi/3)=R(-\pi/6)R(\pi/3)$$，按和角公式应等于 $$R(\pi/3-\pi/6)=R(\pi/6)$$，与前面用矩阵乘法硬算出的 $$R(\alpha)R(\beta)=R(\pi/2)$$（注意这里 $$\alpha+\beta=\pi/2$$，不是 $$\sigma$$）是两件不同但一致的事：一个算的是"角度相加"（群乘法），一个算的是"角度相减"（$$\sigma$$，用来判断光滑性）。两者都只是加减法，天生光滑，这就是为什么 $$SO(2)$$ 是 Lie 群的核心原因——第48章定理 3.11 会把"$$SO(2)$$ 是 1 维流形"这另一半也补齐（本章只处理"乘法光滑"这一半，流形结构留给下一章的图册论证）。

### 3.4 换位子：先在两个具体矩阵上算一遍"顺序差多少"

现在回答问题 C。$$E=\begin{bmatrix}0&1\\0&0\end{bmatrix}$$、$$F=\begin{bmatrix}0&0\\1&0\end{bmatrix}$$。先核对 $$E^2=F^2=\mathbf 0$$：

$$E^2=\begin{bmatrix}0&1\\0&0\end{bmatrix}\begin{bmatrix}0&1\\0&0\end{bmatrix}=\begin{bmatrix}0&0\\0&0\end{bmatrix},\qquad F^2=\begin{bmatrix}0&0\\1&0\end{bmatrix}\begin{bmatrix}0&0\\1&0\end{bmatrix}=\begin{bmatrix}0&0\\0&0\end{bmatrix}.$$

因此幂级数 $$\sum_k(tE)^k/k!$$ 从 $$k\ge2$$ 起全是零矩阵，精确地等于 $$I+tE$$（不是近似，是恰好相等，因为高阶项本来就是零）；同理 $$\sum_k(sF)^k/k!=I+sF$$。

先算 $$EF$$：

$$EF=\begin{bmatrix}0&1\\0&0\end{bmatrix}\begin{bmatrix}0&0\\1&0\end{bmatrix}=\begin{bmatrix}1\cdot1&0\\0&0\end{bmatrix}=\begin{bmatrix}1&0\\0&0\end{bmatrix}$$

（第一行第一列：$$E$$ 的第一行 $$(0,1)$$ 点乘 $$F$$ 的第一列 $$(0,1)$$ 得 $$0\cdot0+1\cdot1=1$$；其余三项类似地都算出 $$0$$，读者可自行核对）。再算 $$FE$$：

$$FE=\begin{bmatrix}0&0\\1&0\end{bmatrix}\begin{bmatrix}0&1\\0&0\end{bmatrix}=\begin{bmatrix}0&0\\0&1\end{bmatrix}$$

（第二行第二列：$$F$$ 的第二行 $$(1,0)$$ 点乘 $$E$$ 的第二列 $$(1,0)$$ 得 $$1$$；其余三项为 $$0$$）。于是

$$EF-FE=\begin{bmatrix}1&0\\0&0\end{bmatrix}-\begin{bmatrix}0&0\\0&1\end{bmatrix}=\begin{bmatrix}1&0\\0&-1\end{bmatrix}=:H.$$

现在直接算问题 C 要求的两个乘积：

$$(I+sF)(I+tE)=I+tE+sF+st\,FE=I+tE+sF+st\begin{bmatrix}0&0\\0&1\end{bmatrix},$$

$$(I+tE)(I+sF)=I+sF+tE+st\,EF=I+tE+sF+st\begin{bmatrix}1&0\\0&0\end{bmatrix}.$$

两者的公共部分 $$I+tE+sF$$ 完全一样（这部分与"谁先谁后"无关），差别只在最后那个 $$st$$ 倍的矩阵项：

$$(I+tE)(I+sF)-(I+sF)(I+tE)=st\Bigl(\begin{bmatrix}1&0\\0&0\end{bmatrix}-\begin{bmatrix}0&0\\0&1\end{bmatrix}\Bigr)=st\begin{bmatrix}1&0\\0&-1\end{bmatrix}=st\,H=st(EF-FE).$$

**这就是问题 C 的答案**：先 $$F$$ 后 $$E$$ 与先 $$E$$ 后 $$F$$，两个乘积并不相等，差恰好是 $$st$$ 倍的 $$EF-FE$$——一个只用 $$E,F$$ 本身（不用任何幂级数近似）就能写出的矩阵。$$EF-FE$$ 精确地测量了"顺序颠倒付出的代价"，而且这个代价按 $$s,t$$ 各一次方增长（$$st$$ 项），这正是"二阶交互"这个说法的由来：$$s,t$$ 分别都是一阶小量，$$st$$ 是二阶小量，顺序差是最先在二阶冒出来的东西。

**为什么要单独给 $$AB-BA$$ 起个名字、记作 $$[A,B]$$**：因为它恰好是"顺序颠倒的代价"这个量本身，且 $$A,B$$ 交换（$$AB=BA$$）当且仅当 $$[A,B]=0$$——它是测量"不交换程度"的最简单的量。

**定义 3.7（矩阵的换位子/括号, commutator）**。对 $$n\times n$$ 矩阵 $$A,B$$，定义 $$[A,B]:=AB-BA$$。

**命题 3.8（括号的基本性质，直接验证）**。(i) $$[A,B]=-[B,A]$$（反对称，因为交换 $$A,B$$ 的名字，$$AB-BA$$ 变成 $$BA-AB$$，正好差一个负号）；(ii) 若 $$[A,B]=0$$ 则 $$A,B$$ 互相交换（定义即是）；(iii) 对上面的 $$E,F$$，$$[E,F]=H=\begin{bmatrix}1&0\\0&-1\end{bmatrix}$$（已算出）。

**例 3.8（多算一步，为下一章的括号运算预热）**。用同样的 $$E,F,H$$，算 $$[H,E]$$：

$$HE=\begin{bmatrix}1&0\\0&-1\end{bmatrix}\begin{bmatrix}0&1\\0&0\end{bmatrix}=\begin{bmatrix}0&1\\0&0\end{bmatrix},\qquad EH=\begin{bmatrix}0&1\\0&0\end{bmatrix}\begin{bmatrix}1&0\\0&-1\end{bmatrix}=\begin{bmatrix}0&-1\\0&0\end{bmatrix},$$

$$[H,E]=HE-EH=\begin{bmatrix}0&1\\0&0\end{bmatrix}-\begin{bmatrix}0&-1\\0&0\end{bmatrix}=\begin{bmatrix}0&2\\0&0\end{bmatrix}=2E.$$

同样地可以算出 $$[H,F]=-2F$$（留作练习竞2 的一部分）。$$H,E,F$$ 满足的这三条关系 $$[H,E]=2E$$、$$[H,F]=-2F$$、$$[E,F]=H$$，正是 `_experts/algebra/lie-algebra-root-systems.md` 里提到的 $$\mathfrak{sl}(2)$$ 标准基（那里叫 $$h,x,y$$）——同一组关系，本章只是把它当成"两个具体矩阵换位子"算了一遍，不涉及任何表示论。

第48章定理 3.20 会证明：对任意矩阵 Lie 群，恒等元处求导得到的"左不变向量场"之间的括号，恰好就是 $$[A,B]=AB-BA$$。那里的证明要引入一个任意的测试函数 $$f$$，对 $$f(\exp(sB)\exp(tA))$$ 做到二阶的 Taylor 展开——而本节因为 $$E,F$$ 幂零（$$E^2=F^2=0$$），$$\exp$$ 的级数直接截断，我们不需要 Taylor 展开、不需要任何"到二阶为止"的近似，就精确地看到了同一个答案 $$st(EF-FE)$$。这就是本节"先具体后抽象"的全部内容：下一章的一般证明，做的正是我们刚刚做过的这件事，只是换成了任意的（不一定幂零的）矩阵和任意的测试函数。

## 四、几何与物理直觉 (Intuition)

**位置与位移。** 用地图来想最直接：GPS 给出的是"位置"（一个点），导航说的"向东走 300 米"是"位移"（一个向量）。"向东走 300 米"这句话不依赖你用哪种坐标系描述地图，但"两个位置相加"毫无意义——你不会问"天安门加故宫等于哪里"。而"位置加位移"永远有意义："从天安门向东走 300 米"是一个确定的新位置，与坐标系选择无关。时刻与时长是同一个结构的另一份拷贝：钟点不能加钟点，但钟点可以加时长。仿射空间就是把这条日常直觉写成公理的结果。

**升一维换矩阵。** 齐次坐标那个多出来的"$$1$$"不是凭空添的：一个 $$n$$ 维线性映射永远固定原点不动，而我们想要的"转+搬"恰好不固定原点。解决办法就像给一张二维地图加一条"海拔恒为 1"的等高线，把原来在平面里做不到的平移，翻译成在这条等高线所在的三维空间里做旋转（严格说是切变）。机器人学里描述一台机械臂末端的位置和姿态，用的正是这个 $$4\times4$$ 矩阵（三维空间升到四维），道理和本章的 $$3\times3$$ 例子完全一样。

**光滑的群乘法。** "群乘法光滑"这件事，最好的直觉是方向盘：把方向盘从角度 $$\alpha$$ 转到角度 $$\beta$$，转动量是 $$\beta-\alpha$$，而这个量随 $$\alpha,\beta$$ 的变化是连续甚至光滑的——你不会因为 $$\alpha,\beta$$ 稍微变一点，转动量就发生跳变。$$SO(2)$$ 的光滑性说的正是这么朴素的一件事，只是我们要求它对任意群（不止旋转）都成立，并且要求这件事能用坐标里的公式（不是直觉）确认下来。

**换位子与"转两次顺序重要吗"。** 找一本书，先绕竖直轴转 $$90^\circ$$、再绕水平轴转 $$90^\circ$$；然后换一个顺序：先绕水平轴转 $$90^\circ$$、再绕竖直轴转 $$90^\circ$$。两次操作结束时书的朝向**不一样**——这是"矩阵乘法不交换"的实物版本。第三节里 $$E,F$$ 的换位子 $$H\neq0$$ measured 的正是这种"顺序差多少"；如果两个操作是两次平移（沿不同方向"走"），顺序就不重要，换位子恰好是 $$0$$，这与"位移构成交换的向量空间"（第 3.1 节）是同一件事的两个侧面：能交换的操作换位子为零，不能交换的操作换位子测量差多少。

## 五、经典问题精讲 (Classical Problems)

### 题 1：由两点的像定出一维仿射映射

**问**：设 $$f:\mathbb{R}\to\mathbb{R}$$ 是仿射映射（$$A=V=\mathbb{R}$$），已知 $$f(0)=3$$、$$f(2)=9$$。求 $$f$$ 的表达式。

**解**。仿射映射形如 $$f(x)=ax+b$$（线性部分 $$a$$，平移 $$b$$）。代入 $$f(0)=b=3$$。再代入 $$f(2)=2a+b=9$$，得 $$2a=9-3=6$$，$$a=3$$。故 $$f(x)=3x+3$$。核对：$$f(0)=3$$ ✓，$$f(2)=6+3=9$$ ✓。这道题的要点是：仿射映射由"一个点的像 + 线性部分"完全决定（这里线性部分是一个数 $$a$$），$$b=f(0)$$ 直接给出平移量，第二个点的像用来解出 $$a$$。

### 题 2：机械臂末端的位置——齐次矩阵的一次完整核算

**问**：某机械臂末端先绕基座转 $$45^\circ$$，再平移 $$(2,-1)$$。求它把点 $$(1,1)$$（工具在转动前相对基座的偏移）送到哪里，并写出对应的 $$3\times3$$ 齐次矩阵，核对矩阵乘法给出同样答案。

**解**。$$R(45^\circ)=\begin{bmatrix}\frac{\sqrt2}{2}&-\frac{\sqrt2}{2}\\[2pt]\frac{\sqrt2}{2}&\frac{\sqrt2}{2}\end{bmatrix}$$。先转：

$$R(45^\circ)\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}\frac{\sqrt2}{2}\cdot1-\frac{\sqrt2}{2}\cdot1\\[2pt]\frac{\sqrt2}{2}\cdot1+\frac{\sqrt2}{2}\cdot1\end{bmatrix}=\begin{bmatrix}0\\\sqrt2\end{bmatrix}.$$

再平移 $$(2,-1)$$：$$(0,\sqrt2)+(2,-1)=(2,\sqrt2-1)$$。

齐次矩阵：$$\widehat f=\begin{bmatrix}\frac{\sqrt2}{2}&-\frac{\sqrt2}{2}&2\\[2pt]\frac{\sqrt2}{2}&\frac{\sqrt2}{2}&-1\\0&0&1\end{bmatrix}$$。核对：

$$\widehat f\begin{bmatrix}1\\1\\1\end{bmatrix}=\begin{bmatrix}\frac{\sqrt2}{2}-\frac{\sqrt2}{2}+2\\[2pt]\frac{\sqrt2}{2}+\frac{\sqrt2}{2}-1\\1\end{bmatrix}=\begin{bmatrix}2\\\sqrt2-1\\1\end{bmatrix}.$$

前两个坐标 $$(2,\sqrt2-1)$$ 与直接算的一致。这正是第 3.2 节定义 3.3 的一次独立核对，只是换了一组数字与一个"机械臂"的叙事。

### 题 3：$$45^\circ$$ 自己转两次

**问**：验证 $$R(\pi/4)R(\pi/4)=R(\pi/2)$$。

**解**。$$\cos(\pi/4)=\sin(\pi/4)=\frac{\sqrt2}{2}$$，故 $$R(\pi/4)=\frac{\sqrt2}{2}\begin{bmatrix}1&-1\\1&1\end{bmatrix}$$。

$$R(\pi/4)^2=\frac12\begin{bmatrix}1&-1\\1&1\end{bmatrix}\begin{bmatrix}1&-1\\1&1\end{bmatrix}=\frac12\begin{bmatrix}1-1&-1-1\\1+1&-1+1\end{bmatrix}=\frac12\begin{bmatrix}0&-2\\2&0\end{bmatrix}=\begin{bmatrix}0&-1\\1&0\end{bmatrix}=R(\pi/2).$$

与直接代 $$\cos(\pi/2)=0,\sin(\pi/2)=1$$ 得到的 $$R(\pi/2)$$ 一致。这道题是第 3.3 节例 3.6 的姊妹版：那里是两个不同角度相乘，这里是同一个角度自乘，同样验证"乘法=角度相加"。

### 题 4：直接用幂级数算一个矩阵指数

**问**：设 $$A=\begin{bmatrix}0&-\pi/2\\\pi/2&0\end{bmatrix}$$（即 $$\theta=\pi/2$$ 的反对称矩阵）。写出 $$\exp(A)=\sum_{k\ge0}A^k/k!$$ 的前几项并核对它等于 $$R(\pi/2)$$。

**解**。记 $$J=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$$，则 $$A=\frac{\pi}{2}J$$。先算 $$J^2$$：

$$J^2=\begin{bmatrix}0&-1\\1&0\end{bmatrix}\begin{bmatrix}0&-1\\1&0\end{bmatrix}=\begin{bmatrix}-1&0\\0&-1\end{bmatrix}=-I.$$

于是 $$J$$ 的幂按 $$4$$ 为周期循环：$$J^0=I,J^1=J,J^2=-I,J^3=-J,J^4=I,\dots$$。把 $$\exp(A)=\sum_k(\pi/2)^kJ^k/k!$$ 按 $$J$$ 的奇偶次分组：

$$\exp(A)=\Bigl(1-\frac{(\pi/2)^2}{2!}+\frac{(\pi/2)^4}{4!}-\cdots\Bigr)I+\Bigl(\frac{\pi}{2}-\frac{(\pi/2)^3}{3!}+\cdots\Bigr)J.$$

括号里两个级数正是 $$\cos(\pi/2)$$ 与 $$\sin(\pi/2)$$ 的 Taylor 级数（这是微积分里 $$\cos,\sin$$ 的定义级数，本身不需要重新证明）。取前两项数值核对：$$\cos(\pi/2)\approx1-\frac{(\pi/2)^2}{2}\approx1-1.2337=-0.2337$$，加上第三项 $$\frac{(\pi/2)^4}{24}\approx0.2537$$ 之后已经很接近真值 $$\cos(\pi/2)=0$$；同理 $$\sin(\pi/2)$$ 的级数部分和也逐渐逼近 $$1$$。取无穷多项后精确得到 $$\cos(\pi/2)=0$$、$$\sin(\pi/2)=1$$，故

$$\exp(A)=0\cdot I+1\cdot J=J=\begin{bmatrix}0&-1\\1&0\end{bmatrix}=R(\pi/2).$$

这道题预告了第48章定理 3.24(v)：矩阵情形下 $$\exp$$ 就是幂级数 $$\sum A^k/k!$$，而"旋转矩阵 = 反对称矩阵的指数"这件事，下一章会作为定理（结合入口题 (c)）一般地证明；本章只是先用一个具体角度把幂级数亲手加了一遍。

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 在 $$A=V=\mathbb{R}$$ 上定义"运算" $$p\oplus v:=p+v^2$$（注意是 $$v$$ 的平方,不是 $$v$$ 本身）。判断 $$(A,\oplus)$$ 是否满足定义 3.1 的 (A1)(A2)？如果不满足，给出具体的反例数字。

**基2.** 平面上取三点 $$P=(2,-1)$$、$$Q=(5,3)$$、$$R=(0,4)$$（与正文例 3.2 相同的三点）。计算 $$P-Q$$、$$Q-R$$，并验证 $$(P-Q)+(Q-R)=P-R$$。

**基3.** 把"先按比例 $$2$$ 缩放（即线性部分为 $$2I$$），再平移 $$(-1,3)$$"的仿射变换写成 $$3\times3$$ 齐次矩阵，并求出这个矩阵的逆矩阵；说明逆矩阵对应的是什么几何变换。

### 竞赛（本课目标难度）

**竞1.** 设 $$A=\mathbb{R}$$（$$A=V=\mathbb{R}$$，标准加法）。证明 $$A$$ 上的仿射映射 $$f:A\to A$$ 全部形如 $$f(x)=ax+b$$（$$a,b\in\mathbb{R}$$），且 $$f$$ 可逆当且仅当 $$a\neq0$$；举出一个 $$a=0$$ 的具体例子，说明它为什么不满足"线性部分可逆"这条要求。

**竞2.** 设 $$A=\begin{bmatrix}1&2\\0&-1\end{bmatrix}$$、$$B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$$。计算 $$[A,B]=AB-BA$$，并直接核对 $$\operatorname{tr}[A,B]=0$$。另外，用正文例 3.8 的 $$H,E$$，补算 $$[H,F]$$（$$F=\begin{bmatrix}0&0\\1&0\end{bmatrix}$$），验证 $$[H,F]=-2F$$。

**竞3.** 对一般的（不给具体数值的）角度 $$\alpha,\beta$$，把 $$R(\alpha)R(\beta)$$ 的矩阵乘法完全展开，用和角公式说明乘积矩阵的四个入口都是 $$\cos(\alpha+\beta)$$ 或 $$\sin(\alpha+\beta)$$（正负号自己配平），从而说明 $$SO(2)$$ 的乘法坐标表达式对 $$(\alpha,\beta)$$ 是光滑函数。

### 研究（通向下一章）

**研1.** 设 $$A=\begin{bmatrix}0&-2\\2&0\end{bmatrix}$$（即 $$\theta=2$$ 的反对称矩阵）。仿照正文题 4 的方法，把 $$\exp(tA)$$ 按 $$J=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$$ 的奇偶次分组，写出 $$\cos(2t)$$、$$\sin(2t)$$ 各自 Taylor 级数的前两项（到 $$t^3$$ 那一项为止），并与 $$R(2t)=\cos(2t)I+\sin(2t)J$$ 的对应项核对是否一致。

**研2.** 设 $$R(t)=\begin{bmatrix}\cos(t^2)&-\sin(t^2)\\\sin(t^2)&\cos(t^2)\end{bmatrix}$$（角度是 $$t^2$$ 而不是 $$t$$）。计算 $$\omega(t):=R(t)^{-1}R'(t)$$，判断它是不是常矩阵。第48章的一条定理说：$$\omega(t)$$ 恒为常矩阵 $$A$$ 当且仅当 $$R(t)=\exp(tA)$$。据此说明为什么这条 $$R(t)$$（保持现在这个参数化方式）不能写成 $$\exp(tA)$$ 的形式。

### 解答 (Solutions)

**解 基1.** (A1) 要求 $$p\oplus0=p$$：按定义 $$p\oplus0=p+0^2=p$$，**成立**。(A2) 要求 $$(p\oplus u)\oplus v=p\oplus(u+v)$$。左边 $$=(p+u^2)\oplus v=p+u^2+v^2$$；右边 $$=p+(u+v)^2=p+u^2+2uv+v^2$$。取具体数字 $$u=v=1$$：左边 $$=p+1+1=p+2$$，右边 $$=p+(1+1)^2=p+4$$。$$p+2\neq p+4$$，故 (A2) **不成立**，$$(A,\oplus)$$ 不是仿射空间。（这条反例说明公理 (A2) 里的"结合律"不是自动满足的，一个看起来"差不多"的运算完全可能破坏它。）

**解 基2.** $$P-Q=(2-5,-1-3)=(-3,-4)$$。$$Q-R=(5-0,3-4)=(5,-1)$$。两者相加：$$(-3,-4)+(5,-1)=(2,-5)$$。直接算 $$P-R=(2-0,-1-4)=(2,-5)$$。两者相等，定理 3.2 核对通过。

**解 基3.** 线性部分 $$M=2I=\begin{bmatrix}2&0\\0&2\end{bmatrix}$$，平移 $$b=(-1,3)$$，齐次矩阵

$$\widehat f=\begin{bmatrix}2&0&-1\\0&2&3\\0&0&1\end{bmatrix}.$$

求逆：按定理 3.4 证明里用到的分块逆公式 $$\begin{bmatrix}M&b\\0&1\end{bmatrix}^{-1}=\begin{bmatrix}M^{-1}&-M^{-1}b\\0&1\end{bmatrix}$$（第48章定理 3.7 证明中给出，这里直接代入验证也不难：设逆为 $$\begin{bmatrix}M^{-1}&c\\0&1\end{bmatrix}$$，要求乘积为单位阵，$$M^{-1}$$ 项自动满足，$$Mc+b=0$$ 给出 $$c=-M^{-1}b$$）。这里 $$M^{-1}=\frac12I$$，$$-M^{-1}b=-\frac12(-1,3)=(\frac12,-\frac32)$$，故

$$\widehat f^{-1}=\begin{bmatrix}\frac12&0&\frac12\\0&\frac12&-\frac32\\0&0&1\end{bmatrix}.$$

核对：$$\widehat f\,\widehat f^{-1}$$ 的 $$(1,1)$$ 项 $$=2\cdot\frac12=1$$，$$(1,3)$$ 项 $$=2\cdot\frac12+(-1)\cdot1=1-1=0$$，其余项同理都给出单位阵（读者可自行补全）。这个逆矩阵对应的几何变换是"先按比例 $$\frac12$$ 缩放，再平移 $$(\frac12,-\frac32)$$"——它把 $$\widehat f$$ 做的事情原样撤销，这正符合"逆变换"的直觉。

**解 竞1.** 设 $$f$$ 是仿射映射，线性部分是某个线性映射 $$\varphi:\mathbb{R}\to\mathbb{R}$$，即 $$\varphi(v)=av$$（某个数 $$a$$，因为 $$1$$ 维线性映射都是乘一个常数）。由定义 3.1 节里"仿射映射"的定义式 $$f(p+v)=f(p)+\varphi(v)$$，取 $$p=0$$：$$f(v)=f(0)+av$$，记 $$b=f(0)$$，即 $$f(x)=ax+b$$ 对一切 $$x$$ 成立（把 $$v$$ 换名成 $$x$$）。

可逆性：若 $$a\neq0$$，$$f^{-1}(y)=(y-b)/a$$ 直接验证是逆映射（$$f(f^{-1}(y))=a\cdot\frac{y-b}{a}+b=y-b+b=y$$）。若 $$a=0$$，$$f(x)=b$$ 对一切 $$x$$ 恒等于同一个值 $$b$$，不是单射（例如 $$f(1)=f(2)=b$$），故不可逆。

具体例子：$$f(x)=0\cdot x+5=5$$（常值映射）。它把整条数轴压缩成一个点 $$5$$，线性部分是 $$\varphi(v)=0$$，这个 $$\varphi$$ 不是可逆线性映射（把非零的 $$v$$ 也送到 $$0$$），故按定义 3.1 节"可逆仿射变换要求线性部分可逆"这条要求，$$f$$ 被排除在外——这与"$$f$$ 不是单射"这件事是同一个道理的两种说法。

**解 竞2.**

$$AB=\begin{bmatrix}1&2\\0&-1\end{bmatrix}\begin{bmatrix}0&1\\1&0\end{bmatrix}=\begin{bmatrix}1\cdot0+2\cdot1&1\cdot1+2\cdot0\\0\cdot0+(-1)\cdot1&0\cdot1+(-1)\cdot0\end{bmatrix}=\begin{bmatrix}2&1\\-1&0\end{bmatrix},$$

$$BA=\begin{bmatrix}0&1\\1&0\end{bmatrix}\begin{bmatrix}1&2\\0&-1\end{bmatrix}=\begin{bmatrix}0\cdot1+1\cdot0&0\cdot2+1\cdot(-1)\\1\cdot1+0\cdot0&1\cdot2+0\cdot(-1)\end{bmatrix}=\begin{bmatrix}0&-1\\1&2\end{bmatrix}.$$

$$[A,B]=AB-BA=\begin{bmatrix}2&1\\-1&0\end{bmatrix}-\begin{bmatrix}0&-1\\1&2\end{bmatrix}=\begin{bmatrix}2&2\\-2&-2\end{bmatrix}.$$

迹：$$\operatorname{tr}[A,B]=2+(-2)=0$$，核对通过（一般地 $$\operatorname{tr}(AB)=\operatorname{tr}(BA)$$ 对任意方阵成立，故 $$\operatorname{tr}(AB-BA)=0$$ 恒成立，这里只是数值核对一次）。

再算 $$[H,F]$$，$$H=\begin{bmatrix}1&0\\0&-1\end{bmatrix}$$、$$F=\begin{bmatrix}0&0\\1&0\end{bmatrix}$$：

$$HF=\begin{bmatrix}1&0\\0&-1\end{bmatrix}\begin{bmatrix}0&0\\1&0\end{bmatrix}=\begin{bmatrix}0&0\\-1&0\end{bmatrix},\qquad FH=\begin{bmatrix}0&0\\1&0\end{bmatrix}\begin{bmatrix}1&0\\0&-1\end{bmatrix}=\begin{bmatrix}0&0\\1&0\end{bmatrix},$$

$$[H,F]=HF-FH=\begin{bmatrix}0&0\\-1&0\end{bmatrix}-\begin{bmatrix}0&0\\1&0\end{bmatrix}=\begin{bmatrix}0&0\\-2&0\end{bmatrix}=-2F.$$

核对通过。

**解 竞3.** 设 $$R(\alpha)=\begin{bmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{bmatrix}$$、$$R(\beta)=\begin{bmatrix}\cos\beta&-\sin\beta\\\sin\beta&\cos\beta\end{bmatrix}$$。逐项展开乘积：

$$(1,1)\ \text{项}:\ \cos\alpha\cos\beta-\sin\alpha\sin\beta=\cos(\alpha+\beta),$$

$$(1,2)\ \text{项}:\ -\cos\alpha\sin\beta-\sin\alpha\cos\beta=-(\sin\alpha\cos\beta+\cos\alpha\sin\beta)=-\sin(\alpha+\beta),$$

$$(2,1)\ \text{项}:\ \sin\alpha\cos\beta+\cos\alpha\sin\beta=\sin(\alpha+\beta),$$

$$(2,2)\ \text{项}:\ -\sin\alpha\sin\beta+\cos\alpha\cos\beta=\cos(\alpha+\beta),$$

（每一步都是把和角公式 $$\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$$、$$\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$$ 反过来代入）。四项合起来正是 $$R(\alpha+\beta)$$。因为 $$\cos,\sin$$ 都是 $$\mathbb{R}$$ 上的光滑函数，$$\alpha+\beta$$ 是 $$(\alpha,\beta)$$ 的光滑函数（多项式），复合仍光滑，故 $$(\alpha,\beta)\mapsto R(\alpha)R(\beta)$$ 的四个坐标入口都是 $$(\alpha,\beta)$$ 的光滑函数——这正是第 3.3 节定理 3.6 判据在 $$SO(2)$$ 上成立的完整（非数值）理由。$$\blacksquare$$

**解 研1.** $$A=2J$$。$$\exp(tA)=\exp(2tJ)$$，按 $$J$$ 的奇偶次分组（同正文题 4）：

$$\exp(2tJ)=\Bigl(1-\frac{(2t)^2}{2!}+\cdots\Bigr)I+\Bigl(2t-\frac{(2t)^3}{3!}+\cdots\Bigr)J.$$

$$I$$ 的系数前两项是 $$1-2t^2$$，正是 $$\cos(2t)=1-\frac{(2t)^2}{2}+\cdots=1-2t^2+\cdots$$ 的前两项。$$J$$ 的系数前两项是 $$2t-\frac{8t^3}{6}=2t-\frac{4t^3}{3}$$，正是 $$\sin(2t)=2t-\frac{(2t)^3}{6}+\cdots=2t-\frac{4t^3}{3}+\cdots$$ 的前两项。两组系数分别与 $$\cos(2t)$$、$$\sin(2t)$$ 的 Taylor 级数逐项一致，核对通过——这正是第48章定理 3.24(v) 矩阵情形（$$\exp(A)=\sum A^k/k!$$）在这个具体例子上的样子。

**解 研2.** 先算 $$R'(t)$$。记 $$\phi(t)=t^2$$，$$R(t)=\cos\phi(t)\,I+\sin\phi(t)\,J$$（把 $$-\sin\phi$$、$$\cos\phi$$ 两项按 $$I,J$$ 分组写法可以直接核对：$$\cos\phi\,I+\sin\phi\,J=\begin{bmatrix}\cos\phi&-\sin\phi\\\sin\phi&\cos\phi\end{bmatrix}$$，与 $$R(t)$$ 一致）。由链式法则，

$$R'(t)=-\phi'(t)\sin\phi(t)\,I+\phi'(t)\cos\phi(t)\,J=\phi'(t)\bigl(-\sin\phi(t)\,I+\cos\phi(t)\,J\bigr).$$

注意 $$R(t)J=(\cos\phi\,I+\sin\phi\,J)J=\cos\phi\,J+\sin\phi\,J^2=\cos\phi\,J-\sin\phi\,I$$（用了 $$J^2=-I$$，正文题 4 已算过），恰好等于括号里那一项。故

$$R'(t)=\phi'(t)\,R(t)J,\qquad\text{这里 }\phi'(t)=2t.$$

于是

$$\omega(t)=R(t)^{-1}R'(t)=R(t)^{-1}\bigl(2t\,R(t)J\bigr)=2t\,J$$

（用了 $$R(t)^{-1}R(t)=I$$）。$$\omega(t)=2tJ$$ **不是常矩阵**——它随 $$t$$ 线性变化。由第48章那条定理（$$\omega(t)$$ 恒为常矩阵当且仅当 $$R(t)=\exp(tA)$$），$$\omega(t)$$ 不恒定就说明**不存在**常矩阵 $$A$$ 使这条 $$R(t)$$（按现在的参数 $$t$$）等于 $$\exp(tA)$$。直觉上的理由也吻合：若 $$R(t)=\exp(tA)$$ 是单参数子群，就该满足 $$R(s+t)=R(s)R(t)$$，即角度该满足 $$(s+t)^2$$（左边角度）与 $$s^2+t^2$$（右边两角度之和对应的角度，因为 $$R(s)R(t)=R(s^2)R(t^2)=R(s^2+t^2)$$）相等，但 $$(s+t)^2=s^2+2st+t^2\neq s^2+t^2$$（除非 $$st=0$$）——角度按 $$t^2$$ 走，天生就不满足"匀速转动"要求的可加性，这与 $$\omega(t)$$ 不恒定是同一件事的两种说法。

## 七、Takeaway 与延伸 (Takeaways)

1. **"点不能加点、可以相减"是可以公理化的**：定义 3.1 的三条公理，逐字核对具体的两点坐标或具体的钟点，都能验证；差向量满足 $$(q-p)+(r-q)=r-p$$（定理 3.2），这条恒等式就是"分两步挪等于一步挪到底"。

2. **仿射变换升一维就能矩阵化**：给点加一个恒为 $$1$$ 的坐标，仿射变换 $$f(x)=Mx+b$$ 就变成单纯的矩阵乘法 $$\widehat f=\begin{bmatrix}M&b\\0&1\end{bmatrix}$$，且复合对应矩阵相乘（定理 3.4）——这不是记号游戏，是本节亲手核对过两次（问题 B、题 2）的事实。

3. **判断 Lie 群只需要查一个映射**：把 $$\mu,\iota$$ 两件事压缩成 $$\sigma(x,y)=x^{-1}y$$ 一件事（定理 3.6），在 $$SO(2)$$ 上这件事就是"角度相减"——最简单的光滑函数。

4. **换位子 $$[A,B]=AB-BA$$ 精确测量"顺序颠倒的代价"**：用幂零矩阵 $$E,F$$ 算出的 $$(I+tE)(I+sF)-(I+sF)(I+tE)=st[E,F]$$ 是**精确**等式，不是近似；这正是第48章要在一般情形下（用 Taylor 展开到二阶）重新证明的东西。

5. **矩阵指数就是把幂级数亲手加起来**：$$\exp(\theta J)$$ 按 $$J^2=-I$$ 分组后，$$I,J$$ 的系数恰好就是 $$\cos\theta,\sin\theta$$ 的 Taylor 级数——"旋转是反对称矩阵的指数"这条第48章的核心结论，在具体角度上就是这么一件事。

现在你已经能手算两点之差、一个仿射变换的齐次矩阵、$$SO(2)$$ 里任意两个角度相乘、以及一对具体矩阵的换位子了；第48章会把这些具体计算，逐一变成不依赖特定数字的一般定义和证明——仿射空间的三条公理会重新出现（定义 3.1），齐次矩阵会扩展到 $$n$$ 维并证明像恰好是哪个子群（定理 3.7），$$SO(2)$$ 会被证明是完整的 1 维 Lie 群（定理 3.11，图册也会第一次被真正写下来），而换位子会通过左不变向量场与一般测试函数的二阶 Taylor 展开，被证明就是"李括号"本身（定理 3.20）——你在本章亲手做过的每一步计算，都会在那里找到它的一般版本。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch46_算子半群与Feynman路径积分_下.md">← 第46章 算子半群与 Feynman 路径积分·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch48_仿射空间_变换群与Lie群_下.md">第48章 仿射空间、变换群与 Lie 群·下 →</a></div>
</div>
