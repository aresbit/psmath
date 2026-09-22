---
layout: default
---

# 第72章: 层、Zariski 拓扑、概形、Hilbert 零点定理·下：完整推导 (Sheaves, Zariski Topology, Schemes, Hilbert's Nullstellensatz · Part II: Full Derivation)

> 配套预备: 见 第71章 层、Zariski 拓扑、概形、Hilbert 零点定理·上（同一主题的具体铺垫，建议先读）

> 对应原专栏: MP129、MP133、MP138–MP140、MP145
> 专家依据: `_experts/algebra/algebraic-geometry-topology-k.md`（主）+ `_experts/algebra/commutative-algebra.md`
> 知识库依据: `opc2/knowledge/math/代数几何/`、`opc2/knowledge/math/交换代数/`、`opc2/knowledge/math/复几何/ens-lyon-riemann/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

读完第 71 章的具体例子（手算过粘合失败、Zariski 开集必相交、一个根理想、一次 Noether 正规化的代换、一个对偶数环）之后，这里把同样的构造写成一般定义并给出完整证明——第 71 章里"先算后信"的每一步，本章都会回过头来证明"为什么对任意情形都成立"。

本章要完成一件事：把「几何对象」这个词的含义整个换掉。前面三十五章里，几何对象一直是**点的集合**再加结构——流形是点的集合加图册，纤维丛是点的集合加局部平凡化。本章把顺序倒过来：**先给一个环，再从环里长出空间**。几何对象不再首先是「一些点」，而首先是「一些函数」。

核心问题有两个，它们是一枚硬币的两面：

1. 一个多项式方程组 $$f_1=\cdots=f_m=0$$ 什么时候有解？为什么这个问题可以不靠「解方程」来回答，而只靠检查理想 $$(f_1,\dots,f_m)$$ 是否等于整个环？
2. 反过来，如果只拿到「函数环」，能不能还原出空间？（Hilbert 零点定理说：能，但还原出来的东西比原来大——它比原来多了幂零元。）

**从哪来。** 第 31–35 章给了范畴、函子、模与导出函子。这些抽象到本章才第一次拿到几何的解释——**层就是「开集范畴上的反变函子」**，这句话正是第 62 章「函子」概念的本行。
**到哪去。** 第 74 章用本章的层语言重写向量丛，并把上同调定义为「整体截面函子」的导出函子：第 70 章的 $$\operatorname{Ext}$$ 与 $$\operatorname{Tor}$$ 在那里变形为 $$H^i(X,\mathcal{F})$$。

三个显式接口：

- 第 12 章的**纤维丛**在本章被代数化。丛要求「局部同构于 $$U\times F$$」，层只要求「局部数据能粘合」，后者更宽。局部自由层与向量丛是同一件事的两个名字（定义 3.10 指明对应，第 74 章展开）。
- 第 28 章的 **de Rham 上同调**是层上同调的特例：取常数层 $$\underline{\mathbb{R}}$$，它在光滑流形上的层上同调同构于 de Rham 上同调。本章只点明接口，同构留给第 74 章。
- 第 62 章的 **Yoneda 引理**在本章以「$$\operatorname{Spec}$$ 是反变函子」的形式出现；更强的一条是 $$\operatorname{Spec}$$ 与整体截面 $$\Gamma$$ 互为伴随，给出「环论与几何等价」的一句精确陈述（定理 3.13）。

## 二、入口：一道具体的问题 (Entry Problem)

**先做题，不给定义。** 下面四个问题都能在纸上算完，而且第 3 节之前你不需要任何新名词。第 5 节会把这四个全部回收。

**(a) 方程组有解吗？** 考虑实数域上的方程组

$$x^2+y^2=0 .$$

在 $$\mathbb{R}$$ 中它的解集只有一个点 $$(0,0)$$；换到 $$\mathbb{C}$$ 中，解集是一条「曲线」，它可以写成 $$x+iy=0$$ 或 $$x-iy=0$$，也就是两条复直线之并。同一个方程组，解集的「大小」随基域变化——这件事本身不奇怪。奇怪的是下面这句：

> 判断方程组有没有解，不需要解它，只需要看 $$(x^2+y^2)$$ 这个理想**是不是整个多项式环**。

若 $$x^2+y^2$$ 的零点集非空，则 $$1$$ 不可能落在由 $$x^2+y^2$$ 生成的理想里（因为 $$1$$ 在任何点取值都是 $$1\ne0$$，不能是零点的公共方程）。反过来，如果解集是空的，能不能推出 $$1$$ 落在理想里？**这一步就是本章的主角**——它不是解方程，而是把一个几何问题（有没有点）翻译成一个环论问题（理想是否等于整个环）。第 3.3 节的零点定理就是这句话的精确形式。

**(b) 「函数环」这个词暗示了什么？** 设 $$X$$ 是一个点。它上面的函数环是 $$\mathbb{R}$$（每个函数由它在那一点的取值唯一决定）；反过来拿到 $$\mathbb{R}$$，也能还原出「一个点」。

现在把问题弄脏一点。考虑

$$A=\mathbb{R}[\varepsilon]/(\varepsilon^2),\qquad \varepsilon\ne0,\ \varepsilon^2=0 .$$

它是两个实数的「一阶展开」$$a+b\varepsilon$$，加法逐项，乘法用 $$\varepsilon^{2}=0$$。这个环仍只有一个极大理想 $$(\varepsilon)$$，在古典意义下「对应一个点」。可它比 $$\mathbb{R}$$ 大：多了一整个方向的额外信息。**同一个点，两个不同的函数环——那么「空间」到底该配哪个环？** 这个问题的答案（该配 $$A$$）就是 3.4 节「概形」的入口。

**(c) 为什么 Zariski 拓扑这么粗？** 在 $$\mathbb{R}$$ 上取 $$f(x)=x(x-1)(x-2)$$，它的零点集是三个点。在把「多项式的零点集」取作闭集所得的拓扑里：开集长什么样？某开集上恒为零的多项式一定是零多项式吗？任意两个非空开集是否一定相交？

直觉上开集应该很细（像通常的 $$\mathbb{R}$$ 拓扑那样有大量小区间）。3.2 节会给答案，而答案会解释为什么代数几何不能用「开集上的局部结构」而必须用「层」——在这么粗的拓扑里**开集太少、太大**，光有开集区分不出局部。

**(d) 理想什么时候可以放大？** 在 $$\mathbb{C}[x,y]$$ 中取

$$I=(x^2,\ xy).$$

它的零点集是 $$Z(I)=\{(0,y)\}$$，即 $$y$$ 轴。$$x^{2}$$、$$xy$$、$$x$$ 都在 $$y$$ 轴上恒为零（$$y$$ 轴上 $$x=0$$，故它们也都取零）；但 $$x$$ **不在** $$I$$ 里（$$I$$ 中每个元素都没有一次项）。于是

$$I\subsetneq I(Z(I)),\qquad I(Z(I))=(x)=\sqrt I .$$

**理想被放大了，而且放大到它的根**。放大到什么程度才停？这是 Hilbert 零点定理的答案。注意 $$\sqrt I=(x)$$ 是素理想：$$y$$ 轴不可约。如果零点集由两段拼成，会怎样？

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 预层与层：把「局部」写成函子

本章要换掉「几何对象」的定义，第一步必须先把「局部数据」这件事说清楚。

给定拓扑空间 $$X$$，取它的全体开集为对象，把包含关系 $$V\subseteq U$$ 取作从 $$V$$ 到 $$U$$ 的态射（每个包含关系恰给一个态射），不含关系的开集对之间没有态射。这样得到一个范畴，记作 $$\mathfrak{Top}(X)$$，称为 $$X$$ 的**开集范畴 (category of open sets)**。（第 62 章说过：只要对象与态射定清楚了，一个范畴就定清楚了；这里没有任何额外结构。）

**定义 3.1（预层, presheaf）** 设 $$\mathcal{C}$$ 是含零对象的范畴（本章只用到交换环与 Abel 群两种情形）。$$X$$ 上的一个 **$$\mathcal{C}$$-值预层**是一个反变函子

$$\mathcal{F}:\mathfrak{Top}(X)^{\mathrm{op}}\longrightarrow\mathcal{C}.$$

具体写出：对每个开集 $$U$$ 给一个对象 $$\mathcal{F}(U)\in\mathcal{C}$$，对每个包含关系 $$V\subseteq U$$ 给一个态射 $$\rho^{U}_{V}:\mathcal{F}(U)\to\mathcal{F}(V)$$，称为**限制映射 (restriction map)**，满足两条：

1. $$\rho^{U}_{U}=\operatorname{id}_{\mathcal{F}(U)}$$；
2. 若 $$W\subseteq V\subseteq U$$，则 $$\rho^{V}_{W}\circ\rho^{U}_{V}=\rho^{U}_{W}$$（函子保复合）。

$$\mathcal{F}(U)$$ 中的元素称为 $$U$$ 上的**截面 (section)**，记 $$s\vert_{V}:=\rho^{U}_{V}(s)$$。

**为什么是反变函子。** 函子的方向常被记混，这里没有选择余地：包含关系 $$V\subseteq U$$ 说的是「$$V$$ 比 $$U$$ 小」，而函数从大集合限制到小集合，方向是 $$\mathcal{F}(U)\to\mathcal{F}(V)$$——**集合的箭头反了，函数的箭头才是正着的**。反变正是「局部化」这件事的范畴语义：越往下（越小）走，信息越多（限制是丢掉一部分信息）。

**为什么预层不够用。** 预层只规定了"限制"，没有规定"拼合"：给一堆局部数据（比如每个小开集上各一个函数），预层不保证这堆数据能拼成一个整体对象，也不保证拼法唯一。而"局部数据决定整体对象"正是几何里最基本的直觉（连续函数、光滑函数、正则函数都满足这一点）。层就是把这条直觉写成公理。

**定义 3.2（层, sheaf）** 预层 $$\mathcal{F}$$ 称为**层**，若对每个开集 $$U$$ 与它的每个开覆盖 $$U=\bigcup_{i\in I}U_i$$，下面这条序列正合：

$$0\longrightarrow\mathcal{F}(U)\xrightarrow{\ \rho\ }\prod_{i\in I}\mathcal{F}(U_i)\mathrel{\overset{\alpha}{\underset{\beta}{\rightrightarrows}}}\prod_{i,j\in I}\mathcal{F}(U_i\cap U_j)$$

其中 $$\rho(s)=(s\vert_{U_i})_i$$，$$\alpha\big((s_i)_i\big)=\big(s_i\vert_{U_i\cap U_j}\big)_{i,j}$$，$$\beta\big((s_i)_i\big)=\big(s_j\vert_{U_i\cap U_j}\big)_{i,j}$$，正合指的是 $$\alpha$$ 与 $$\beta$$ 的**均衡子 (equalizer)** 恰是 $$\mathcal{F}(U)$$ 的像：即「$$\alpha(x)=\beta(x)$$ 的解集」恰为 $$\mathcal{F}(U)$$ 在 $$\rho$$ 下的像。把这句话拆成不含范畴语言的版本，就是两条公理：

- **粘合 (gluing)**：若一族截面 $$s_i\in\mathcal{F}(U_i)$$ 在每一处交上一致，即 $$s_i\vert_{U_i\cap U_j}=s_j\vert_{U_i\cap U_j}$$ 对一切 $$i,j$$ 成立，则存在 $$s\in\mathcal{F}(U)$$ 使 $$s\vert_{U_i}=s_i$$ 对一切 $$i$$；
- **唯一性 (uniqueness)**：这样的 $$s$$ 只有一个。

**注 3.2（在集合上粘合是白给的，在结构上不是）。** 若 $$\mathcal{F}(U)$$ 只是一堆集合，「粘合」就只是取并集。层的分量在于：$$\mathcal{F}(U)$$ 上带着代数结构（环、模），而粘合必须**对这个结构是封闭的**——粘出来的 $$s$$ 要落在 $$\mathcal{F}(U)$$ 里，即它得自带同一个环结构。下面例 3.2 的常数预层就是在这一点上翻的车。

**例 3.2（三个必记的例子）**

**(i) 连续函数层与光滑函数层。** $$X$$ 上取 $$\mathcal{O}_{X}(U)=\{f:U\to\mathbb{R}\ \text{连续}\}$$、限制映射为函数限制，得到层：连续函数在交上一致就能拼成一个整体连续函数，且拼法唯一（「连续」「可微」「全纯」都是局部性质，逐点定义后逐点验证即可）。把 $$\mathbb{R}$$ 换成 $$\mathbb{C}$$ 或任意拓扑环同样成立。$$X$$ 是光滑流形时的 $$C^{\infty}$$ 层、$$X$$ 是复流形时的全纯函数层都是这一族例子，它们是第 12 章「流形上的局部结构」的精确重述。

**(ii) 常数预层不是层。** 取 $$X=\{p,q\}$$（离散拓扑），令 $$\mathcal{F}(U)=\mathbb{Z}$$ 对一切开集 $$U$$，限制映射一律取恒等。取覆盖 $$X=\{p\}\cup\{q\}$$。因为 $$\{p\}\cap\{q\}=\varnothing$$，空交「无需检验」（空指标集的积是单点集），所以任意一对截面 $$s_p$$、$$s_q$$ 都满足一致条件。可限制映射是恒等，被粘出的 $$s\in\mathcal{F}(X)=\mathbb{Z}$$ 必须同时等于 $$s_p$$ 与 $$s_q$$——当 $$s_p\ne s_q$$ 时不存在这样的 $$s$$。**粘合失败。**

常数预层的**层化**是「局部常值函数层」：$$\underline{\mathbb{Z}}(U)=\{U\ \text{上的局部常值整值函数}\}$$，此时 $$\underline{\mathbb{Z}}(X)=\mathbb{Z}\times\mathbb{Z}$$，正好放下了 $$(s_p,s_q)=(1,2)$$。这个例子说明：**层化不是装饰，它把「预层丢掉的粘合信息」补回来**。

**(iii) 正则函数层 $$\mathcal{O}_X$$。** 这是本章真正的主角，它的定义要到 3.4 节才给。现在只需记住一句话：仿射簇上的正则函数层，是把 (i) 里的「连续」「光滑」换成「是多项式函数」得到的。

**定理 3.3（层化与茎, sheafification / stalk）** 设 $$\mathcal{F}$$ 是 $$\mathcal{C}$$-值预层。则存在层 $$\mathcal{F}^{\#}$$ 与预层态射 $$\theta:\mathcal{F}\to\mathcal{F}^{\#}$$，使得对任意层 $$\mathcal{G}$$，拉回

$$\theta^{*}:\operatorname{Hom}(\mathcal{F}^{\#},\mathcal{G})\longrightarrow\operatorname{Hom}(\mathcal{F},\mathcal{G})$$

是双射。即：$$\mathcal{F}\mapsto\mathcal{F}^{\#}$$ 是嵌入函子 $$\operatorname{Sh}(X)\hookrightarrow\operatorname{PreSh}(X)$$ 的**左伴随**（第 66 章的伴随语言在这里第一次出现在几何里）。且层化不改变「逐点的局部信息」：$$\mathcal{F}^{\#}_{x}\cong\mathcal{F}_{x}$$ 对一切 $$x\in X$$。

*证明思路*：直接把 $$\mathcal{F}^{\#}$$ 造出来。第一步造**茎**（定义 3.4），它是「预层在一点处的极限」；第二步令 $$\mathcal{F}^{\#}(U)$$ 为 $$U$$ 上「取值于茎、且局部来自 $$\mathcal{F}$$ 的截面」全体。可以验出这样得到的是层，并且它是满足伴随性质的最小者。$$\blacksquare$$

**定义 3.4（茎, stalk）** 预定 $$x\in X$$。$$\mathcal{F}$$ 在 $$x$$ 处的**茎**是正向极限

$$\mathcal{F}_{x}=\varinjlim_{U\ni x}\mathcal{F}(U),$$

即「$$x$$ 的所有开邻域上的截面」按「在更小的邻域上相等」作等价关系后的商。$$\mathcal{F}_{x}$$ 的元素称为**函数芽 (germ)**。

**为什么要研究茎。** 定理 3.4（下面）之前先说一句：验证两个层的态射序列是否正合，直接在每个开集 $$U$$ 上验证要照顾所有的 $$U$$，非常繁琐；而茎只在"一点附近"看问题，是层里最小、最容易验证的局部单位。下面这条定理说：对层而言，**逐点验证就够了**——这把"整体命题"化归成了"逐点的代数命题"，是层论里被用得最多的一条判定法则。

**定理 3.4（茎上的正合性判定）** 层的态射序列

$$0\to\mathcal{F}\to\mathcal{F}'\to\mathcal{F}''\to 0$$

正合，当且仅当对一切 $$x\in X$$，茎上的序列

$$0\to\mathcal{F}_{x}\to\mathcal{F}'_{x}\to\mathcal{F}''_{x}\to 0$$

正合。

*证明思路*：这是「层是局部定义的」这句话的定量形式。核与像都是层（对层来说 $$\ker$$ 与 $$\operatorname{im}$$ 自动满足粘合公理），而两个层相等当且仅当它们在每个茎上相等（层化不改变茎，见定理 3.3；一次截面若在每个点附近都同于另一截面，便在每个点的一个邻域上相等，这些邻域覆盖 $$X$$，由唯一性公理即得整体相等）。$$\blacksquare$$

**注 3.4（与第 12 章纤维丛的对照）。** 纤维丛的局部数据是「$$U_\alpha\times F\to U_\alpha$$」加一族转移函数 $$g_{\alpha\beta}$$，粘合条件写成 $$g_{\alpha\alpha}=1$$、$$g_{\alpha\beta}g_{\beta\gamma}g_{\gamma\alpha}=1$$——**一群显式写出的相容性方程**。层论把这件事抽象掉：不再要求「局部同构于某个标准模型」，只要求「局部截面能粘合」。因此层是比丛更宽的框架；反过来，当一个层**恰好**局部自由（定义 3.10）时，它才退化回丛。第 74 章会把这一方向补全。

### 3.2 Zariski 拓扑与素谱

**定义 3.5（Zariski 闭集, Zariski closed set）** 设 $$k$$ 是域。对多项式集合 $$S\subseteq k[x_1,\dots,x_n]$$，定义它的**零点集**

$$Z(S)=\{a=(a_1,\dots,a_n)\in k^{n}\ \mid\ f(a)=0\ \ \text{对一切}\ f\in S\}.$$

$$k^{n}$$ 中能写成某个 $$Z(S)$$ 的子集称为 **Zariski 闭集**，其补集称为 **Zariski 开集**。全体 Zariski 闭集构成的集族记作 $$\overline{\mathfrak{Top}}(k^{n})$$。

**定理 3.5（ $$\overline{\mathfrak{Top}}(k^{n})$$ 确实是拓扑的闭集族）** 上面的定义给出 $$k^{n}$$ 上的一个拓扑（称为 **Zariski拓扑 (Zariski topology)**）。

*证明*：要验证三条。

1. **空集与全集是闭集。** $$Z(\varnothing)=k^{n}$$（没有方程要满足），$$Z(\{1\})=\varnothing$$（常数 $$1$$ 处处不为零）。
2. **任意交是闭集。** 对任意一族 $$\{S_\alpha\}$$ 有 $$Z\big(\bigcup_\alpha S_\alpha\big)=\bigcap_\alpha Z(S_\alpha)$$：$$a$$ 落在左端等价于「一切 $$\alpha$$、一切 $$f\in S_\alpha$$ 有 $$f(a)=0$$」，等价于「一切 $$\alpha$$ 有 $$a\in Z(S_\alpha)$$」。**这一步只用到全称量词可以交换次序**，与被验证的数学内容无关。
3. **有限并是闭集。** 先证理想版本：$$Z(\mathfrak{a}\mathfrak{b})=Z(\mathfrak{a})\cup Z(\mathfrak{b})$$。「$$\subseteq$$」：设 $$a\notin Z(\mathfrak{a})\cup Z(\mathfrak{b})$$，则存在 $$f\in\mathfrak{a}$$、$$g\in\mathfrak{b}$$ 使 $$f(a)\ne0$$、$$g(a)\ne0$$，于是 $$(fg)(a)=f(a)g(a)\ne0$$（**这里用了 $$k$$ 是域，无零因子**），故 $$a\notin Z(\mathfrak{a}\mathfrak{b})$$。「$$\supseteq$$」：$$a\in Z(\mathfrak{a})$$ 时 $$\mathfrak{a}$$ 中每个 $$f$$ 满足 $$f(a)=0$$，而 $$\mathfrak{a}\mathfrak{b}$$ 由乘积 $$fg$$ 生成，$$(fg)(a)=f(a)g(a)=0$$，故 $$a\in Z(\mathfrak{a}\mathfrak{b})$$。由两个的并逐步归结到有限并。

还差一步：定义里允许 $$S$$ 是任意多项式集合，而上面写的是理想。补上 $$Z(S)=Z((S))$$：「$$\supseteq$$」由 $$S\subseteq(S)$$ 得；「$$\subseteq$$」由 $$a\in Z(S)$$ 时 $$\mathfrak{a}$$ 中元素 $$\sum g_if_i$$ 在 $$a$$ 取值为 $$\sum g_i(a)\cdot0=0$$ 得。$$\blacksquare$$

**例 3.5** 在 $$\mathbb{A}^1_{\mathbb{R}}=\mathbb{R}$$ 上，Zariski 闭集恰是 $$\varnothing$$、$$\mathbb{R}$$ 与**有限点集**——因为非零多项式只有有限个根。所以非空开集都是「去掉有限个点」的集合。**入口题 (c) 的第一问在此回答：任意两个非空开集一定相交**——若要 $$\mathbb{R}\setminus F_1$$ 与 $$\mathbb{R}\setminus F_2$$ 不交，就要求 $$F_1\cup F_2=\mathbb{R}$$，而有限集不能等于 $$\mathbb{R}$$。

**推论 3.5** 由这一结构立得两件事，它们解释入口题 (c) 的第二问：**（一）**Zariski 拓扑不是 Hausdorff 的（任意两个非空开集都相交，谈不上用不交邻域分离两点）。**（二）**「在开集上恒为零」是很强的条件：若非零多项式 $$f$$ 在某个非空 Zariski 开集上恒为零，则它有无穷多个根，矛盾。

**这是代数几何不能用「开集上的函数论」而必须用层的原因**：Zariski 开集太少、太大，几乎「一样大」，无法区分局部。局部信息必须由**茎**（定义 3.4）承载。

**从 $$k^n$$ 到任意环。** 上面的 $$Z(S)$$ 只对"域上的多项式环"有意义，因为要在 $$k^n$$ 里代入求值。但入口题 (b)、(d) 已经说明，我们真正关心的对象是**环本身**（$$\mathbb{R}$$、$$\mathbb{R}[\varepsilon]/(\varepsilon^2)$$……），而不只是它的点集。要让"零点集"这套语言对任意交换环 $$A$$ 都讲得通，就不能再用"代入求值"（一般的环元素没有"取值"这回事），只能换成纯代数的条件：$$f$$ 在"点" $$\mathfrak{p}$$ 处为零，就定义为 $$f\in\mathfrak{p}$$。这正是下面素谱的定义。

**定义 3.6（素谱, prime spectrum）** 设 $$A$$ 是交换环。它的**素谱**是素理想全体

$$\operatorname{Spec}A=\{\mathfrak{p}\subseteq A\ \mid\ \mathfrak{p}\ \text{是素理想}\}.$$

对任意子集 $$S\subseteq A$$ 定义

$$V(S)=\{\mathfrak{p}\in\operatorname{Spec}A\ \mid\ S\subseteq\mathfrak{p}\},$$

并称 $$\operatorname{Spec}A\setminus V(S)$$ 为 Zariski 开集。对单个元素 $$f\in A$$ 记

$$D(f)=\{\mathfrak{p}\in\operatorname{Spec}A\ \mid\ f\notin\mathfrak{p}\}=\operatorname{Spec}A\setminus V(\{f\}).$$

**定理 3.6（素谱的拓扑性质）** 上述集合族使 $$\operatorname{Spec}A$$ 成为拓扑空间，且：

1. $$V(S)=V((S))$$，其中 $$(S)$$ 是 $$S$$ 生成的理想；
2. 有限并来自理想积：$$V(\mathfrak{a}\mathfrak{b})=V(\mathfrak{a})\cup V(\mathfrak{b})$$；
3. $$\{D(f)\}_{f\in A}$$ 构成拓扑的**基**，即每个开集是若干 $$D(f)$$ 之并；
4. $$\operatorname{Spec}A$$ 是**拟紧的 (quasi-compact)**：每个开覆盖有有限子覆盖。

*证明*：

1 与 2 与定理 3.5 的证明逐字平行，只需把「$$f(a)=0$$」换成「$$f\in\mathfrak{p}$$」，并把「$$k$$ 无零因子」换成「$$\mathfrak{p}$$ 是素理想」。

3：任取开集 $$\operatorname{Spec}A\setminus V(S)$$。只要证明它等于 $$\bigcup_{f\in S}D(f)$$：一个素理想 $$\mathfrak{p}$$ 不在 $$V(S)$$ 中，等价于「存在 $$f\in S$$ 使 $$f\notin\mathfrak{p}$$」，等价于「存在 $$f\in S$$ 使 $$\mathfrak{p}\in D(f)$$」。

4：设 $$\operatorname{Spec}A=\bigcup_{i\in I}D(f_i)$$。取补集得 $$\bigcap_i V(\{f_i\})=\varnothing$$，即没有素理想包含全体 $$f_i$$。于是由 $$\{f_i\}$$ 生成的理想 $$J=(f_i)_{i\in I}$$ 不落在任何素理想里。若 $$J\ne A$$，由 Zorn 引理（每个真理想含于某个极大理想，而极大理想必是素理想）$$J$$ 会含于某个极大理想，矛盾。故 $$J=A$$，即 $$1\in J$$。按定义，$$1$$ 是有限个 $$f_i$$ 的组合：存在有限子集 $$\{f_{i_1},\dots,f_{i_k}\}$$ 与 $$a_1,\dots,a_k\in A$$ 使 $$a_1f_{i_1}+\cdots+a_kf_{i_k}=1$$。这说明 $$(f_{i_1},\dots,f_{i_k})=A$$，故 $$\bigcap_{j}V(\{f_{i_j}\})=\varnothing$$，即 $$\bigcup_j D(f_{i_j})=\operatorname{Spec}A$$。**有限子覆盖存在**。$$\blacksquare$$

**例 3.6（三个必须画出来的素谱）**

**(i) $$\operatorname{Spec}k$$（$$k$$ 是域）。** 唯一的理想是 $$(0)$$，它是素理想。所以 $$\operatorname{Spec}k$$ 是单点空间。

**(ii) $$\operatorname{Spec}\mathbb{Z}$$。** 素理想是 $$(0)$$ 与各素数 $$(p)$$。于是这个空间的点就是「全体素数加上一个额外的点 $$\eta=(0)$$」。闭集是 $$V\big((n)\big)=\{(p)\ \mid\ p\ \text{整除}\ n\}$$——**有限个点**（$$n$$ 的素因子有限），加上 $$V\big((0)\big)=\operatorname{Spec}\mathbb{Z}$$ 全体。所以开集同样都是「去掉有限个点」。点 $$\eta$$ 有个奇怪的属性：它的闭包 $$\overline{\{\eta\}}=V\big((0)\big)$$ 是整个空间。这样的点称为**一般点 (generic point)**：它「稠密地」躺在空间里，任何非空开集都含它（因为开集是去掉有限个闭点）。

**(iii) $$\operatorname{Spec}k[x]$$（$$k=\overline{k}$$）。** 素理想是 $$(0)$$ 与 $$(x-a)$$（$$a\in k$$）：$$k[x]$$ 是主理想整环，非零素理想由不可约多项式生成，而 $$k$$ 代数闭时不可约多项式都是一次的。所以空间是「$$k$$ 的每个点各对应一个闭点，再加一个一般点 $$\eta=(0)$$」，拓扑同 (ii)。**这里出现了古典簇理论里看不见的一般点**：它使得「多项式在 $$\eta$$ 处取值」这件事有意义，是「把多项式看成空间上的函数」所需要的额外的点。

**点不够用了。** 例 3.6(ii)(iii) 已经看到：$$\operatorname{Spec}A$$ 里除了"古典的点"（极大理想），还有像一般点 $$\eta$$ 这样的怪点，它的闭包是整个空间。要把这类点系统地归类，需要先说清楚"一整块不能再分解的闭集"是什么——这就是下面的不可约性，它是"点"这个概念在拓扑里的推广。

**定义 3.7（不可约空间, irreducible space）** 拓扑空间 $$X$$ 称为**不可约的**，若它不能写成两个非空闭真子集之并。

**定理 3.7（素理想与不可约闭集的一一对应）** 对交换环 $$A$$：

1. $$\operatorname{Spec}A$$ 不可约，当且仅当 $$A$$ 的幂零根 $$\mathfrak{N}(A)$$ 是素理想（特别地，$$A$$ 是整环时 $$\operatorname{Spec}A$$ 不可约）；
2. 更一般地，$$\operatorname{Spec}A$$ 的不可约闭子集与 $$A$$ 的素理想一一对应，对应由 $$\mathfrak{p}\mapsto V(\mathfrak{p})$$ 给出，其逆为 $$Y\mapsto I(Y)=\{f\in A\ \mid\ Y\subseteq V(\{f\})\}$$。

*证明*：

先做一个子步骤。设 $$\mathfrak{p}$$ 是素理想，则 $$V(\mathfrak{p})$$ 不可约。设 $$V(\mathfrak{p})=V(\mathfrak{a})\cup V(\mathfrak{b})$$。若 $$V(\mathfrak{p})\ne V(\mathfrak{a})$$，取 $$f\in\mathfrak{a}\setminus\mathfrak{p}$$（存在，否则 $$\mathfrak{a}\subseteq\mathfrak{p}$$ 给出反包含）；同理取 $$g\in\mathfrak{b}\setminus\mathfrak{p}$$。由 $$\mathfrak{p}$$ 素，$$fg\notin\mathfrak{p}$$，即 $$\mathfrak{p}\notin V(\mathfrak{a}\mathfrak{b})=V(\mathfrak{a})\cup V(\mathfrak{b})$$，与分解矛盾。故 $$V(\mathfrak{p})$$ 不可约。

(1)：若 $$\mathfrak{N}(A)$$ 是素理想，则 $$V(\mathfrak{N}(A))=\operatorname{Spec}A$$（每个素理想都含 $$\mathfrak{N}(A)$$，这是幂零根的定义性刻画），由上一段它不可约。反之，$$\operatorname{Spec}A=V((0))$$ 不可约迫使 $$\sqrt{(0)}=\mathfrak{N}(A)$$ 为素理想：若 $$\mathfrak{a}\mathfrak{b}\subseteq\mathfrak{N}(A)$$，则 $$V(\mathfrak{a})\cup V(\mathfrak{b})=\operatorname{Spec}A$$，故其中之一是整个空间、设为 $$V(\mathfrak{a})$$，则 $$\mathfrak{a}\subseteq\mathfrak{N}(A)$$。

(2)：对闭子集 $$Y=V(\mathfrak{a})$$，令 $$\mathfrak{p}=\sqrt{\mathfrak{a}}$$，则 $$Y=V(\mathfrak{p})$$：$$\mathfrak{a}\subseteq\mathfrak{p}$$ 给出 $$V(\mathfrak{p})\subseteq Y$$；反向，$$\mathfrak{p}$$ 中元素 $$r$$ 满足 $$r^n\in\mathfrak{a}$$，故 $$r(a)^n=0$$，由取值落在域里得 $$r(a)=0$$。再说明 $$\sqrt{\mathfrak{a}}$$ 由 $$Y$$ 唯一决定：任何使 $$Y=V(\mathfrak{q})$$ 的**根**理想 $$\mathfrak{q}$$ 满足 $$\mathfrak{q}=\bigcap_{\mathfrak{q}\subseteq\mathfrak{r}}\mathfrak{r}$$，而 $$\{\mathfrak{r}\supseteq\mathfrak{q}\}$$ 恰是 $$Y$$ 中的点，故这个交由 $$Y$$ 决定。于是「根理想 ↔ 闭子集」是双射；在这个双射下，「素理想 ↔ 不可约闭子集」由不可约性的定义与「$$V(\mathfrak{p})$$ 不可约」合起来得到。$$\blacksquare$$

**注 3.7** 定理 3.7(2) 是入口题 (b) 的第一个线索：**空间里的点不再只有「极大理想」一种**。$$V(\mathfrak{p})$$ 这个不可约闭集整体，也被一个「点」$$\mathfrak{p}$$ 代表了；而 $$V(\mathfrak{p})$$ 里其余的点对应 $$\mathfrak{p}$$ 以下的素理想。所以「一个点携带一整块子空间的信息」——这是 $$A=\mathbb{R}[\varepsilon]/(\varepsilon^2)$$ 那句话的几何翻译。

### 3.3 Hilbert 零点定理

设 $$k$$ 代数闭。本节证明：$$\mathbb{A}^{n}$$ 中的闭集与 $$k[x_1,\dots,x_n]$$ 中的根理想一一对应。这是把「几何」翻译成「环论」的那部字典的核心条目。

**定理 3.8（弱零点定理, weak Nullstellensatz）** 设 $$k$$ 是代数闭域，$$\mathfrak{a}\subsetneq k[x_1,\dots,x_n]$$ 是真理想，则 $$Z(\mathfrak{a})\ne\varnothing$$。

要证它，需要一个纯代数的引理。

**引理 3.8（Zariski 引理 / Noether 正规化）** 若域 $$K$$ 是 $$k$$-代数且有限生成，则 $$K$$ 是 $$k$$ 的有限代数扩张。

*证明*：分三步。

**第一步（Noether 正规化）**。设 $$K=k[t_1,\dots,t_n]$$。我们证明：存在代数无关的 $$y_1,\dots,y_d\in K$$ 使 $$K$$ 在 $$B=k[y_1,\dots,y_d]$$ 上**整**。

对 $$n$$ 归纳。若 $$t_1,\dots,t_n$$ 代数无关，取 $$y_i=t_i$$，$$d=n$$，结论成立。否则存在非零多项式 $$f\in k[T_1,\dots,T_n]$$ 使 $$f(t_1,\dots,t_n)=0$$。设 $$f=\sum_{\alpha}c_{\alpha}T^{\alpha}$$，取整数 $$N$$ 大于所有 $$\lvert\alpha\rvert$$。作代换

$$T_i\ \longmapsto\ Y_i+T_n^{\,N^{i}}\quad(1\le i\le n-1),\qquad T_n\longmapsto T_n .$$

单项式 $$T^{\alpha}$$ 随之变成 $$(Y_1+T_n^{N})^{\alpha_{1}}\cdots(Y_{n-1}+T_n^{N^{n-1}})^{\alpha_{n-1}}T_n^{\alpha_{n}}$$。把每个因子 $$(Y_i+T_n^{N^i})^{\alpha_i}$$ 按二项式展开，$$T_n$$ 的幂次可以是 $$N^ij$$（$$0\le j\le\alpha_i$$），对应系数带 $$Y_i^{\alpha_i-j}$$；只有取满 $$j=\alpha_i$$（即每个因子都选 $$T_n^{N^i}$$ 那一项，系数 $$\binom{\alpha_i}{\alpha_i}=1$$）才能让这个因子对 $$T_n$$-次数的贡献达到最大值 $$N^i\alpha_i$$，而这个选法恰好不带任何 $$Y_i$$。于是 $$T^{\alpha}$$ 的像作为 $$T_n$$ 的多项式，**最高次项次数**是

$$e(\alpha)=\alpha_1N+\alpha_2N^{2}+\cdots+\alpha_{n-1}N^{n-1}+\alpha_n,$$

**且这一项不含 $$Y$$**——系数就是原来的 $$c_{\alpha}$$ 本身：因为要达到次数 $$e(\alpha)$$，$$n-1$$ 个因子必须同时取到各自的最大贡献 $$N^i\alpha_i$$，这就把每个因子里的 $$Y_i$$ 都排除了。由于 $$N$$ 大于一切 $$\lvert\alpha\rvert$$，映射 $$\alpha\mapsto e(\alpha)$$ 是单射：按 $$N$$ 进制看，$$\alpha_1,\dots,\alpha_{n-1}$$ 是各位数字、$$\alpha_n$$ 是个位，而 $$\lvert\alpha_i\rvert<N$$ 保证位数不溢出。这同时说明：任何 $$\alpha\ne\alpha^*$$ 对 $$T_n^{e(\alpha^*)}$$ 这一项**没有贡献**——$$\alpha$$ 自身能达到的最高次数已经是 $$e(\alpha)<e(\alpha^*)$$，它展开出的其余（非最高次）各项次数只会更低。

于是在 $$f$$ 的代换结果里，使 $$e(\alpha)$$ 最大的 $$\alpha^{*}$$ **唯一**，它给出 $$T_n$$ 的最高次项，其系数就是 $$c_{\alpha^{*}}$$ 本身——一个 $$k$$ 中的**非零常数**（不是 $$c_{\alpha^*}Y^{\alpha^*}$$：$$Y$$ 的幂次只出现在次数低于 $$e(\alpha^*)$$ 的那些项里）。$$c_{\alpha^*}\in k$$ 非零，故在域 $$k$$ 中可逆，从而也是 $$k[Y_1,\dots,Y_{n-1}]$$ 中的可逆元。于是 $$T_n$$ 满足一个以 $$k[Y_1,\dots,Y_{n-1}]$$ 中元素为系数、首项系数为 $$k$$ 中非零常数的多项式方程；两边除以这个常数（除以域中非零元恒可行，不会跑出 $$k[Y_1,\dots,Y_{n-1}]$$ 这个系数环）即得首一多项式方程，故 $$T_n$$ 在 $$k[Y_1,\dots,Y_{n-1}]$$ 上整。而 $$T_i=Y_i+T_n^{N^{i}}$$ 也在其上整（$$Y_i$$ 是基环元素、$$T_n^{N^i}$$ 是整元的多项式，而整元之和与积仍整）。因此 $$K=k[Y_1,\dots,Y_{n-1}][T_n]$$ 在 $$k[Y_1,\dots,Y_{n-1}]$$ 上整。后者仍是有限生成 $$k$$-代数且是整环（多项式环的子环），对它用归纳假设得代数无关的 $$y_1,\dots,y_d$$ 使它在 $$k[y_1,\dots,y_d]$$ 上整；整性传递，故 $$K$$ 在 $$k[y_1,\dots,y_d]$$ 上整。

**第二步（整 + 域蕴含基环是域）**。设 $$B$$ 是整环，$$K\supseteq B$$ 是域且在 $$B$$ 上整。取 $$0\ne b\in B$$。则 $$b^{-1}\in K$$（$$K$$ 是域）在 $$B$$ 上整，故存在 $$m\ge1$$ 与 $$c_0,\dots,c_{m-1}\in B$$ 使

$$(b^{-1})^{m}+c_{m-1}(b^{-1})^{m-1}+\cdots+c_0=0 .$$

两边乘 $$b^{m-1}$$，得

$$b^{-1}=-(c_{m-1}+c_{m-2}b+\cdots+c_0b^{m-1})\in B .$$

于是 $$B$$ 中每个非零元在 $$B$$ 中可逆，$$B$$ 是域。

**第三步（收官）**。由第一步，$$K$$ 在 $$B=k[y_1,\dots,y_d]$$ 上整。由第二步，$$B$$ 是域。但 $$d\ge1$$ 时 $$B=k[y_1,\dots,y_d]$$ 不是域：$$y_1$$ 不可逆——若 $$y_1q=1$$，把 $$q$$ 按 $$y_1$$ 的幂次写成 $$\sum_{i\ge0}q_i y_1^{i}$$（$$q_i\in k[y_2,\dots,y_d]$$），则左端的 $$y_1$$-次数至少为 $$1$$，而右端为 $$0$$，矛盾。故 $$d=0$$，即 $$B=k$$，于是 $$K$$ 在 $$k$$ 上整，也就是 $$k$$ 上的有限代数扩张。$$\blacksquare$$

*证定理 3.8*。取 $$L=k[x_1,\dots,x_n]/\mathfrak{m}$$，其中 $$\mathfrak{m}\supseteq\mathfrak{a}$$ 是任一包含 $$\mathfrak{a}$$ 的极大理想（$$\mathfrak{a}\ne A$$ 时由 Zorn 引理存在）。$$L$$ 是域，且是有限生成的 $$k$$-代数，由引理 3.8 它在 $$k$$ 上有限且代数。$$k$$ 代数闭蕴含 $$L=k$$。设 $$a_i$$ 是 $$x_i$$ 在 $$L=k$$ 中的像，则环同态 $$\varphi:k[x_1,\dots,x_n]\to k$$、$$\varphi(x_i)=a_i$$ 的核是 $$\mathfrak{m}$$：一方面 $$\mathfrak{m}\subseteq\ker\varphi$$（$$\mathfrak{m}$$ 中元素都被映零），另一方面 $$\ker\varphi$$ 是真理想且 $$\mathfrak{m}$$ 极大，故等号。于是 $$\mathfrak{a}\subseteq\mathfrak{m}=(x_1-a_1,\dots,x_n-a_n)$$，即 $$a=(a_1,\dots,a_n)\in Z(\mathfrak{a})$$。**非空**。$$\blacksquare$$

**从"有没有解"到"差多少"。** 定理 3.8 只回答了"方程组有没有解"这个是/否问题。入口题 (d) 问的是更精细的问题：一个理想与它对应的零点集所能反推出的理想（$$I(Z(\mathfrak{a}))$$）之间究竟差多少。下面的定理给出精确答案：差的部分恰好被"取根"补齐，一步都不多、一步都不少。

**定理 3.9（Hilbert 零点定理, Hilbert's Nullstellensatz）** 设 $$k$$ 代数闭，$$\mathfrak{a}\subseteq k[x_1,\dots,x_n]$$ 是理想，则

$$\sqrt{\mathfrak{a}}=I\big(Z(\mathfrak{a})\big),\qquad\text{其中}\quad \sqrt{\mathfrak{a}}=\{f\ \mid\ f^{m}\in\mathfrak{a}\ \text{对某个}\ m\ge1\},\qquad I(Y)=\{f\ \mid\ f\ \text{在}\ Y\ \text{上恒为零}\}.$$

*证明*：关键是下面这个 **Rabinowitsch 技巧**——把一个「根式」问题换成一个「真理想」问题，代价是添一个变量。

「$$\subseteq$$」：设 $$f^{m}\in\mathfrak{a}$$。则对每个 $$a\in Z(\mathfrak{a})$$ 有 $$f(a)^{m}=0$$，取值落在域 $$k$$ 里，故 $$f(a)=0$$。于是 $$f\in I(Z(\mathfrak{a}))$$。

「$$\supseteq$$」：设 $$f\in I(Z(\mathfrak{a}))$$。$$f=0$$ 时结论成立。否则在 $$k[x_1,\dots,x_{n+1}]$$ 中取

$$J=\mathfrak{a}\cdot k[x_1,\dots,x_{n+1}]+(1-x_{n+1}f).$$

断言 $$Z(J)=\varnothing$$。事实上，若 $$(a_1,\dots,a_{n+1})\in Z(J)$$，则由 $$J$$ 含 $$\mathfrak{a}$$ 得 $$(a_1,\dots,a_n)\in Z(\mathfrak{a})$$，故 $$f(a_1,\dots,a_n)=0$$；再由 $$J$$ 含 $$1-x_{n+1}f$$ 得

$$0=1-a_{n+1}\cdot 0=1,$$

矛盾（这里用了 $$k$$ 中 $$1\ne0$$）。

由 $$Z(J)=\varnothing$$ 与定理 3.8 的逆否命题，$$J=k[x_1,\dots,x_{n+1}]$$，即 $$1\in J$$。于是存在 $$a^{(1)},\dots,a^{(r)}\in\mathfrak{a}\cdot k[x_{n+1}]$$ 与 $$g\in k[x_{n+1}]$$ 使

$$1=a^{(1)}+\cdots+a^{(r)}+g\cdot(1-x_{n+1}f). \tag{72.1}$$

设 $$N$$ 大于 $$a^{(1)},\dots,a^{(r)},g$$ 中 $$x_{n+1}$$ 的次数的最大值。在 (72.1) 中把 $$x_{n+1}$$ 用 $$\frac{1}{f}$$ 形式地代入并两边乘 $$f^{N}$$：右端第二项中括号里的 $$f$$ 与分母相约，变成

$$f^{N}\cdot g\Big(x,\tfrac{1}{f}\Big)\cdot\Big(1-\tfrac{1}{f}\cdot f\Big)=f^{N}\cdot g\Big(x,\tfrac{1}{f}\Big)\cdot 0=0,$$

而每个 $$f^{N}\cdot a^{(i)}(x,1/f)$$ 中的 $$x_{n+1}$$ 负次幂被 $$f^{N}$$ 消去（$$N$$ 足够大），得到 $$k[x_1,\dots,x_n]$$ 中一个属于 $$\mathfrak{a}$$ 的元素。于是

$$f^{N}\in\mathfrak{a},$$

即 $$f\in\sqrt{\mathfrak{a}}$$。$$\blacksquare$$

**推论 3.9（几何—代数字典）** 设 $$k$$ 代数闭。映射 $$Z$$ 与 $$I$$ 给出互逆的一一对应

$$\{\mathfrak{a}\subseteq k[x_1,\dots,x_n]\ \mid\ \mathfrak{a}=\sqrt{\mathfrak{a}}\}\ \longleftrightarrow\ \{Y\subseteq\mathbb{A}^{n}_k\ \mid\ Y\ \text{是 Zariski 闭集}\},\qquad \mathfrak{a}\mapsto Z(\mathfrak{a}),\quad Y\mapsto I(Y),$$

并且这个对应把包含关系反转，把「和」送到「交」，把「素理想」送到「不可约闭集」，把「极大理想」送到「单点」（$$k$$ 代数闭时极大理想恰为 $$(x_1-a_1,\dots,x_n-a_n)$$，见定理 3.8 的证明）。

**例 3.9（入口题 (d) 的完整回收）** 取 $$\mathfrak{a}=(x^2,xy)\subseteq\mathbb{C}[x,y]$$。由定理 3.9，$$I(Z(\mathfrak{a}))=\sqrt{\mathfrak{a}}$$。算 $$\sqrt{\mathfrak{a}}$$：$$x^2\in\mathfrak{a}$$ 给 $$x\in\sqrt{\mathfrak{a}}$$；又 $$\mathfrak{a}\subseteq(x)$$ 且 $$(x)$$ 是素理想（进而根理想），而「取根」保持包含关系，故 $$\sqrt{\mathfrak{a}}\subseteq\sqrt{(x)}=(x)$$。于是 $$\sqrt{\mathfrak{a}}=(x)$$。与直接算 $$Z(\mathfrak{a})=\{(0,y)\}$$、$$I(Z(\mathfrak{a}))=(x)$$ 一致。**理想被放大到它的根，多出来的正是那些「在零点集上为零、但按幂次不落在原理想里」的多项式（这里是 $$x$$）。**

**注 3.9（零点定理不能去掉代数闭性）** 定理 3.9 中「$$k$$ 代数闭」是必需的。取 $$k=\mathbb{R}$$、$$n=1$$、$$\mathfrak{a}=(x^2+1)$$。则 $$Z(\mathfrak{a})=\varnothing$$，于是 $$I(Z(\mathfrak{a}))=\mathbb{R}[x]$$，而 $$\sqrt{\mathfrak{a}}=(x^2+1)$$，等号破裂。原因在定理 3.8 的证明里看得很清楚：$$L=\mathbb{R}[x]/(x^2+1)\cong\mathbb{C}$$ 是 $$\mathbb{R}$$ 的有限代数扩张，但**不是** $$\mathbb{R}$$ 自身，于是核 $$\mathfrak{m}$$ 中读不出 $$\mathbb{R}$$ 上的那个「点」——那个点不在 $$\mathbb{R}$$ 上，而在 $$\mathbb{C}$$ 上。**这正是概形相对簇的第一个优势**：在 $$\operatorname{Spec}\mathbb{R}[x]$$ 里，$$\mathfrak{m}=(x^2+1)$$ 是一个货真价实的点，代表一对复共轭点。

### 3.4 结构层与概形

**只有拓扑空间还不够。** $$\operatorname{Spec}A$$ 目前只是一个拓扑空间——一堆点加一族开集，还没有"函数"这个概念。可入口题 (b) 已经说明，光看点集（甚至光看拓扑）区分不出 $$\mathbb{R}$$ 与 $$\mathbb{R}[\varepsilon]/(\varepsilon^2)$$：两者对应同一个单点空间。要把这份"多出来的信息"找回来，必须在拓扑空间上**再挂一层函数的数据**——这就是结构层的作用，而"拓扑空间 + 一个环层"这一整套装置就是下面的环化空间。

**定义 3.10（环化空间, ringed space）** **环化空间**是一对 $$(X,\mathcal{O}_X)$$，其中 $$X$$ 是拓扑空间，$$\mathcal{O}_X$$ 是 $$X$$ 上的交换环层，称为**结构层 (structure sheaf)**。若每个茎 $$\mathcal{O}_{X,x}$$ 都是局部环，则称 $$(X,\mathcal{O}_X)$$ 为**局部环化空间 (locally ringed space)**。$$\mathcal{O}_X$$-**模层 (module sheaf)** 是层 $$\mathcal{F}$$，使每个 $$\mathcal{F}(U)$$ 是 $$\mathcal{O}_X(U)$$-模、且限制映射与模作用相容。

$$\mathcal{O}_X$$-模层 $$\mathcal{F}$$ 称为**局部自由的 (locally free)**、秩 $$n$$，若存在开覆盖 $$X=\bigcup_iU_i$$ 与同构 $$\mathcal{F}\vert_{U_i}\cong(\mathcal{O}_X\vert_{U_i})^{\oplus n}$$。秩 $$1$$ 的局部自由层称为**可逆层 (invertible sheaf)**。

**注 3.10（与第 12 章的对照）** 定义 3.10 与第 12 章纤维丛的定义逐条对齐：环化空间之于流形，就是基空间之于底空间；模层之于纤维，就是截面的芽之于纤维上的向量空间。**唯一的实质差别**：纤维丛要求纤维是固定模型 $$F$$（通常是 $$\mathbb{R}^n$$）且局部同构于 $$U\times F$$；局部自由层只要求「局部同构于 $$\mathcal{O}_X^{\oplus n}$$」，而 $$\mathcal{O}_X$$ 自身可以是任意的环层（例如在 $$\operatorname{Spec}\mathbb{Z}$$ 上取 $$\mathcal{O}=\mathbb{Z}$$）。所以层是比丛更宽的框架；可逆层就是第 74 章「线丛」的代数版本。

**定理 3.11（结构层, structure sheaf）** 设 $$A$$ 是交换环，$$X=\operatorname{Spec}A$$。则 $$X$$ 上存在唯一的环层 $$\mathcal{O}_X$$ 满足

$$\mathcal{O}_X(D(f))=A_f=A[f^{-1}]\quad\text{对一切}\ f\in A,$$

且它在点 $$\mathfrak{p}$$ 处的茎是局部化

$$\mathcal{O}_{X,\mathfrak{p}}=A_{\mathfrak{p}}=(A\setminus\mathfrak{p})^{-1}A .$$

特别地，每个茎是局部环（唯一极大理想是 $$\mathfrak{p}A_{\mathfrak{p}}$$），故 $$\operatorname{Spec}A$$ 是**局部环化空间**。

*证明*：分「造」、「验层」、「算截面」、「取茎」四步。

**造法**。定义一个预层 $$\mathcal{F}$$：对开集 $$U\subseteq X$$，令

$$\mathcal{F}(U)=\Big\{(s_{\mathfrak{p}})_{\mathfrak{p}\in U}\in\prod_{\mathfrak{p}\in U}A_{\mathfrak{p}}\ \Big\vert\ \forall\mathfrak{p}\in U,\ \exists f\notin\mathfrak{p}\ \text{与}\ a\in A:\ \mathfrak{q}\in D(f)\subseteq U\ \Rightarrow\ s_{\mathfrak{q}}=\frac{a}{f}\ \text{在}\ A_{\mathfrak{q}}\ \text{中}\Big\}.$$

意思是：$$U$$ 上的一个截面是一族芽，**局部地都是同一个分式 $$a/f$$**。限制映射取「把族限制到子集」，预层两条公理逐条直接验证。

**验证是层**。设 $$U=\bigcup_iU_i$$，截面族 $$(s_i)$$ 在交上一致。

*唯一性*：若 $$s,s'$$ 限制到每个 $$U_i$$ 都相等，则对 $$\mathfrak{p}\in U_i$$ 有 $$s_{\mathfrak{p}}=(s\vert_{U_i})_{\mathfrak{p}}=(s'\vert_{U_i})_{\mathfrak{p}}=s'_{\mathfrak{p}}$$，逐点相等故 $$s=s'$$。

*粘合*：给定 $$(s_i)$$，对 $$\mathfrak{p}\in U$$ 取 $$i$$ 使 $$\mathfrak{p}\in U_i$$ 并令 $$s_{\mathfrak{p}}:=(s_i)_{\mathfrak{p}}$$。**不依赖 $$i$$**：若 $$\mathfrak{p}\in U_i\cap U_j$$，一致性给出 $$(s_i)_{\mathfrak{p}}=(s_j)_{\mathfrak{p}}$$。再取 $$s_i$$ 的局部表示 $$D(f)\subseteq U_i$$、$$a/f$$，同一表示对 $$s$$ 在 $$D(f)$$ 上成立（因为 $$D(f)\subseteq U_i$$，而两者在 $$U_i$$ 上一致），故 $$s$$ 满足局部条件。

**计算 $$D(f)$$ 上的截面**，证明 $$\mathcal{F}(D(f))\cong A_f$$。定义 $$\varphi:A_f\to\mathcal{F}(D(f))$$，把 $$a/f^{m}$$ 送到族 $$\mathfrak{q}\mapsto a/f^{m}\in A_{\mathfrak{q}}$$（良定义：$$f\notin\mathfrak{q}$$ 时 $$f$$ 在 $$A_{\mathfrak{q}}$$ 中可逆）。

*单性*：设 $$a/f^m=0\in A_{\mathfrak{q}}$$ 对一切 $$\mathfrak{q}\in D(f)$$。由局部化中「$$a=0$$」的判据，对每个这样的 $$\mathfrak{q}$$ 存在 $$h\notin\mathfrak{q}$$ 使 $$ha=0$$。于是 $$\operatorname{Ann}(a)=\{b\ \mid\ ba=0\}$$ 不落在任何 $$\mathfrak{q}\in D(f)$$ 里，即 $$V(\operatorname{Ann}(a))\subseteq V(f)$$，故 $$f\in\sqrt{\operatorname{Ann}(a)}$$，即有 $$N$$ 使 $$f^{N}a=0$$，于是 $$a/f^{m}=0\in A_f$$。

*满性*：任取截面 $$s$$，它在 $$D(f)$$ 的每点附近是某个 $$a_{\mathfrak{q}}/f_{\mathfrak{q}}$$。由 $$D(f)$$ 拟紧（定理 3.6(4)）取有限个 $$D(f_1),\dots,D(f_k)$$ 覆盖 $$D(f)$$，在每片 $$D(f_i)$$ 上 $$s$$ 由 $$a_i/f_i$$ 表示。把每个表示改写成 $$\tilde a_i/f^{M}$$ 的形状（$$M$$ 取各 $$f_i$$ 的公共幂），诸表示的一致性给出各 $$\tilde a_i$$ 在 $$A_f$$ 中定义同一个元素 $$a/f^{M}$$，它映到 $$s$$。故 $$\varphi$$ 满。综上 $$\mathcal{F}(D(f))\cong A_f$$。

**取茎**。$$\mathcal{O}_{X,\mathfrak{p}}=\varinjlim_{\mathfrak{p}\in D(f)}\mathcal{F}(D(f))=\varinjlim_{f\notin\mathfrak{p}}A_f=A_{\mathfrak{p}}$$（末一式是局部化的正向极限）。$$A_{\mathfrak{p}}$$ 是局部环、唯一极大理想 $$\mathfrak{p}A_{\mathfrak{p}}$$，故 $$(X,\mathcal{O}_X)$$ 局部环化。

**唯一性**。$$\{D(f)\}$$ 是拓扑的基，而层由它在基上的取值决定：任意开集 $$U$$ 上的截面由它在每个 $$D(f)\subseteq U$$ 上的限制决定，再由粘合公理唯一给出。$$\blacksquare$$

**定义 3.12（仿射概形与概形, affine scheme / scheme）** 环化空间 $$(\operatorname{Spec}A,\mathcal{O}_{\operatorname{Spec}A})$$ 称为**仿射概形 (affine scheme)**。一个**概形 (scheme)** 是局部环化空间 $$(X,\mathcal{O}_X)$$，使存在开覆盖 $$X=\bigcup_iU_i$$，在每片上有环化空间的同构 $$(U_i,\mathcal{O}_X\vert_{U_i})\cong(\operatorname{Spec}A_i,\mathcal{O}_{\operatorname{Spec}A_i})$$，其中各 $$A_i$$ 是交换环。

**从概形到环，来回走一遍。** 定义 3.12 说了"怎么从环造出概形"（$$A\mapsto\operatorname{Spec}A$$）；反过来，任何概形 $$X$$ 也自带一个环，就是它的整体截面 $$\Gamma(X,\mathcal{O}_X)$$。这两个方向是不是互逆？下面的定理给出精确到"态射集合"层面的答案，而不只是"对象层面"的答案——这正是第 62 章 Yoneda 引理式的问题。

**定理 3.13（ $$\operatorname{Spec}$$ 与整体截面互为伴随）** 设 $$X$$ 是概形，$$A$$ 是交换环。整体截面函子 $$\Gamma(X,-)=\mathcal{O}_X(X)$$ 与 $$\operatorname{Spec}$$ 之间有一一对应

$$\operatorname{Hom}_{\text{Sch}}\big(X,\operatorname{Spec}A\big)\ \cong\ \operatorname{Hom}_{\text{Ring}}\big(A,\ \Gamma(X,\mathcal{O}_X)\big).$$

*证明思路*：两个方向都写得出来。给定概形态射 $$(f,f^{\#}):X\to\operatorname{Spec}A$$，在全局截面上取 $$f^{\#}$$ 就得到环同态 $$A=\Gamma(\operatorname{Spec}A,\mathcal{O})\to\Gamma(X,\mathcal{O}_X)$$（末一个等号是定理 3.11 的截面计算在 $$U=X=D(1)$$ 上的情形）。反过来，给定环同态 $$\varphi:A\to\Gamma(X,\mathcal{O}_X)$$，先对仿射开集 $$U=\operatorname{Spec}B\subseteq X$$ 构造 $$U\to\operatorname{Spec}A$$——它对应环同态 $$A\to B$$，由 $$\varphi$$ 限制到 $$U$$ 得到——再用「概形态射是局部构造、相容时能粘合」把各片粘起来。两个方向互逆由粘合的唯一性保证。$$\blacksquare$$

**推论 3.13（Yoneda 的面孔；第 62 章的接口）** 取 $$X=\operatorname{Spec}B$$，并将定理 3.13 两边取全局截面（注意 $$\Gamma(\operatorname{Spec}B,\mathcal{O})=B$$），得到

$$\operatorname{Hom}_{\text{Sch}}(\operatorname{Spec}B,\operatorname{Spec}A)\ \cong\ \operatorname{Hom}_{\text{Ring}}(A,B).$$

也就是说：**$$\operatorname{Spec}$$ 是反变函子**

$$\operatorname{Spec}:\{\text{交换环}\}^{\mathrm{op}}\longrightarrow\{\text{概形}\},\qquad A\mapsto\operatorname{Spec}A,\quad (\varphi:A\to B)\mapsto(\operatorname{Spec}B\to\operatorname{Spec}A),$$

而且它是**全忠实的 (fully faithful)**：上面那个映射在每对同态集之间是双射。全忠实意味着环 $$A$$ 被概形 $$\operatorname{Spec}A$$ **完全**决定（决定到同构）。**这就是第 62 章 Yoneda 引理在几何里的面貌**：一个空间由「从一切空间到它的映射」完全决定；而在环这一侧，这些映射的可表对象恰是环的态射集，于是「几何研究空间」与「代数研究环」在范畴层面完全等价。第 66 章讲的伴随——$$\Gamma$$ 是左伴随、$$\operatorname{Spec}$$ 是右伴随——在这里第一次以几何的面貌出现。

**例 3.13（对偶数：入口题 (b) 的回收）** 取 $$k$$ 是域，$$A=k[\varepsilon]/(\varepsilon^{2})$$。则 $$\operatorname{Spec}A$$ 是单点空间（唯一素理想 $$(\varepsilon)$$），但它的结构层是 $$A$$，比 $$k$$ 大。由定理 3.13，

$$\operatorname{Hom}_{\text{Sch}}\big(\operatorname{Spec}A,\ X\big)\cong\operatorname{Hom}_{\text{Ring}}\big(\Gamma(X,\mathcal{O}_X),\ k[\varepsilon]/(\varepsilon^{2})\big).$$

对 $$X=\operatorname{Spec}k[x_1,\dots,x_n]$$，右端是同态 $$k[x_1,\dots,x_n]\to k[\varepsilon]/(\varepsilon^{2})$$，它们恰由 $$x_i\mapsto a_i+c_i\varepsilon$$ 给出（$$a_i,c_i\in k$$，因为要保持 $$k$$ 上的结构）。于是 $$\operatorname{Hom}(\operatorname{Spec}A,X)$$ 的元素就是「$$X$$ 的一个点 $$a$$ 加上一个切方向 $$c$$」——**这正是 $$a$$ 处的切向量**：

$$T_{a}X\cong\operatorname{Hom}_{\text{Sch}}\big(\operatorname{Spec}k[\varepsilon]/(\varepsilon^{2}),\ X\big)_{a},$$

右下标的 $$a$$ 表示落在 $$a$$ 处的那些态射。**空间本身还原不出 $$A$$，但「所有映射到 $$X$$ 的 $$\operatorname{Spec}A$$」还原得出来。** 这就是入口题 (b) 的精确答案：概形必须携带结构层，因为幂零元在拓扑上不可见，只能通过态射被看见。

### 3.5 有理函数域

**每个点的"取值范围"可以不一样。** 例 3.13 已经露出苗头：$$\operatorname{Spec}k[\varepsilon]/(\varepsilon^2)$$ 这个空间的"点"附带的函数环比 $$k$$ 大。要系统地讲清楚"函数在一点处取的值到底住在哪个域里"，需要先定义每一点自己的"取值域"——这就是剩余域。

**定义 3.14（概形的局部环与剩余域）** 设 $$(X,\mathcal{O}_X)$$ 是局部环化空间，$$x\in X$$。茎 $$\mathcal{O}_{X,x}$$ 的唯一极大理想记 $$\mathfrak{m}_x$$，商域

$$k(x)=\mathcal{O}_{X,x}/\mathfrak{m}_x$$

称为 $$x$$ 处的**剩余域 (residue field)**。对 $$\operatorname{Spec}A$$ 中的点 $$\mathfrak{p}$$，$$k(\mathfrak{p})=A_{\mathfrak{p}}/\mathfrak{p}A_{\mathfrak{p}}\cong\operatorname{Frac}(A/\mathfrak{p})$$。

**注 3.14（这是概形与簇的根本差别）** 在古典簇理论里，整个空间只有**一个**基域 $$k$$，函数在每一点取值于同一个 $$k$$。在概形里，**每个点有自己的剩余域**，取值域随点而变。在 $$\operatorname{Spec}\mathbb{Z}$$ 上，闭点 $$(p)$$ 的剩余域是 $$\mathbb{F}_{p}$$，而一般点 $$\eta=(0)$$ 的剩余域是 $$\mathbb{Q}$$。**同一条几何对象上同时住着有限域和有理数域**——这正是概形能统一几何与数论的原因。

**定义 3.15（有理函数域, field of rational functions）** 设 $$X$$ 是不可约概形（由定理 3.7，这等价于它的结构环无零因子），$$\eta$$ 是它的一般点。$$\eta$$ 处的茎 $$\mathcal{O}_{X,\eta}$$ 是一个域：它是素理想 $$(0)$$ 处的局部化——把一切非零元变可逆（幂零元随之被消去），剩下的正是分式域。它称为 $$X$$ 的**有理函数域**，记

$$k(X)=\mathcal{O}_{X,\eta}=\operatorname{Frac}\big(\mathcal{O}_X(U)\big)\quad(\text{任意非空仿射开集}\ U).$$

对仿射簇 $$X=Z(\mathfrak{p})$$（$$\mathfrak{p}$$ 素理想），它的**坐标环 (coordinate ring)** 是 $$k[X]=k[x_1,\dots,x_n]/\mathfrak{p}$$，而 $$k(X)=\operatorname{Frac}\big(k[X]\big)$$。

**为什么要问"不变量"。** 同构是簇之间最强的等价，但太苛刻——很多几何上"本质相同"的簇（相差一些低维的奇异点或可去的差异）并不同构。双有理等价放松了要求，只看"绝大部分"点上的对应；下面的定理说，这个更松的等价恰好由一个纯代数的量——有理函数域——完全捕捉。

**定理 3.15（有理函数域是双有理不变量）** 两个不可约仿射簇之间的**双有理等价 (birational equivalence)**——即存在互为逆的有理映射——恰是「它们的有理函数域同构」。因此有理函数域是簇的双有理分类的不变量。

*证明要点*：给定支配有理映射 $$\varphi:X\dashrightarrow Y$$（即限制在某个非空开集上是态射、且像稠密），它在函数域上诱导出 $$k$$-代数同态 $$\varphi^{*}:k(Y)\to k(X)$$（把 $$Y$$ 上的有理函数拉成 $$X$$ 上的有理函数：先在 $$\varphi$$ 有定义的开集上拉回，再作为有理函数唯一延拓）。若 $$\varphi$$ 有有理逆 $$\psi$$，则 $$\psi^{*}\circ\varphi^{*}=\operatorname{id}$$ 与 $$\varphi^{*}\circ\psi^{*}=\operatorname{id}$$ 成立，故 $$\varphi^{*}$$ 是同构。反之若 $$\varphi^{*}$$ 是同构：把 $$k(Y)$$ 的生成元（即 $$Y$$ 的坐标函数）的像写成 $$k(X)$$ 中的分式，得到 $$\varphi$$ 的显式公式；同理构造 $$\psi$$；两个复合在各自的稠密开集上恒等，故互为逆。$$\blacksquare$$

**例 3.15（算两个有理函数域）**

**(i) 直线与抛物线。** $$X=\mathbb{A}^{1}$$（坐标环 $$k[t]$$）与 $$Y=Z(y-x^{2})\subseteq\mathbb{A}^{2}$$（坐标环 $$k[x,y]/(y-x^{2})\cong k[x]$$）。两者坐标环同构，故 $$k(X)\cong k(Y)\cong k(t)$$——它们是双有理等价的（事实上同构）。

**(ii) 带结点的三次曲线。** $$C=Z(y^{2}-x^{2}-x^{3})\subseteq\mathbb{A}^{2}$$。坐标环 $$k[C]=k[x,y]/(y^{2}-x^{2}-x^{3})$$ 是整环（生成元不可约），故 $$C$$ 不可约，且

$$k(C)=\operatorname{Frac}\big(k[x,y]/(y^{2}-x^{2}-x^{3})\big).$$

$$C$$ 在原点处有一个结点，所以 $$C$$ 与 $$\mathbb{A}^{1}$$ **不同构**；但参数化

$$x=t^{2}-1,\qquad y=t(t^{2}-1)$$

给出双有理等价：代进方程得 $$t^{2}(t^{2}-1)^{2}-(t^{2}-1)^{2}-(t^{2}-1)^{3}=(t^{2}-1)^{2}\big(t^{2}-1-(t^{2}-1)\big)=0$$，而逆有理映射是 $$t=y/x$$。于是 $$k(C)\cong k(t)$$，却 $$k[C]\not\cong k[t]$$。**这正是「有理函数域丢掉了什么」：它看不见结点。** 第 74 章的上同调会把丢掉的信息捡回来。

## 四、几何与物理直觉 (Intuition)

### 4.1 把「点」换成「函数」，几何会更丰富

经典几何（欧氏几何、微分几何、第 05–07 章的流形）都建立在同一个假设上：**先有空间，再谈空间上的函数**。代数几何把顺序颠倒，而颠倒之后理论反而更有力，因为「函数环」比「点集」多装了东西：$$\mathbb{R}$$ 与 $$\mathbb{R}[\varepsilon]/(\varepsilon^{2})$$ 对应同一个拓扑点，但后者多装了一个切方向；$$\mathbb{C}$$ 与 $$\mathbb{R}[x]/(x^{2}+1)$$ 的关系也是这样——后者把 $$\mathbb{R}$$ 上不可见的复共轭点显式摆了出来。而第 62 章的 Yoneda 引理（在本章兑现为定理 3.13）说明：一个空间能提供的全部信息就是「它上面的函数」。

所以「从微分几何到代数几何」这个标题的准确含义是：**几何对象从「点集加结构」换成了「函数环」，而拓扑、函数、局部性这些概念都从环的运算里重新长出来**。层是这一转换的技术载体，Zariski 拓扑是它的分类基准，概形是它的成品。

### 4.2 Zariski 拓扑为什么必须这么粗

初看 Zariski 拓扑荒谬：开集少得可怜，任何两个非空开集都相交，连分离两点都做不到（推论 3.5）。为什么不给 $$\mathbb{C}^{n}$$ 用通常的欧氏拓扑？

答案在「我们要研究什么」上。微分几何研究**光滑的**对象，光滑性在欧氏拓扑下有极好的局部结构，所以开集越细越好。代数几何研究**多项式的零点**，而多项式的刚性极强：一个非零多项式只有有限个零点，取值被极少的信息确定。改用欧氏拓扑会出两个问题：

- 若取欧氏拓扑，多项式函数层的茎是「某点附近的解析函数芽」，其中绝大多数**不是多项式**——层里塞进了太多不属于代数范畴的东西，几何对象就失去了代数性。
- 「多项式零点集」本身生成的拓扑恰好是 Zariski 拓扑（因为 Zariski 闭集正是全体多项式族的零点集）。这个拓扑是让「环 → 拓扑」的对应成为**代数运算的精确反映**的最小者。

粗一点没关系，因为**局部信息由茎承载，而茎是纯代数的**（$$\mathcal{O}_{X,\mathfrak{p}}=A_{\mathfrak{p}}$$，定理 3.11）。一句话：**Zariski 拓扑的功用在「分类点」，不在「分离点」**。

### 4.3 与物理的接口

层与上同调在物理里出现的地方远比代数几何的入门教科书写得多。三个例子：

- **规范场论。** 第 12 章的纤维丛讲的就是规范场（主丛加联络），场强是曲率 $$F=\mathrm{d}A+A\wedge A$$。层论把描述推广到「不是局部平凡」的情形：丛只是局部自由的层，而物理上真正需要的是**系数层**（例如旋量场），它未必有丛结构；瞬子数、磁单极荷这类拓扑荷都是层上同调类。
- **「局部—整体」的落差。** 局部能写出的东西（局部势、局部相、局部坐标卡）未必能整体写出，这个落差由 $$H^{1}$$ 度量。电磁势 $$A$$ 在 $$\mathbb{R}^{2}\setminus\{0\}$$ 上不一定能整体写出，这个「不一定」就是 $$H^{1}\ne0$$。
- **格点模型。** 统计力学里格点模型的可观测量本质上就是「在每个格点附近定义、在交上一致」的截面，而整体可定义性的障碍正是第一个上同调群。

当然，把第 12 章的纤维丛代数化之后，上面这些都还要经过「局部自由」这一条件，本章只负责把接口打开。

## 五、经典问题精讲 (Classical Problems)

**问题 1（Zariski 拓扑下开集必相交）** 设 $$k$$ 是无限域，$$n\ge1$$。证明 $$\mathbb{A}^{n}_{k}$$ 不可约，并由此证明任意两个非空 Zariski 开集相交。

**考点**：定理 3.5、定理 3.7(1)、例 3.5 的加强。
**位置**：入口题 (c) 的严格回答，也是「为什么局部信息不靠开集靠茎」的理由。

**解**。设

$$\mathbb{A}^{n}_{k}=Z(\mathfrak{a})\cup Z(\mathfrak{b}).$$

要证其中之一等于 $$\mathbb{A}^{n}_{k}$$。第一步把这句话翻译成理想语言。由定理 3.5 证明中建立的关系 $$Z(\mathfrak{a})\cup Z(\mathfrak{b})=Z(\mathfrak{a}\mathfrak{b})$$，以及 $$Z(S)=Z((S))$$，等式等价于 $$Z(\mathfrak{a}\mathfrak{b})=\mathbb{A}^{n}_{k}$$，再等价于

$$I\big(Z(\mathfrak{a}\mathfrak{b})\big)=I(\mathbb{A}^{n}_{k})=(0),$$

最后一步用了「任何多项式在 $$\mathbb{A}^{n}$$ 上处处为零则它是零多项式」（定理 3.5 的推论，对 $$n\ge1$$ 与无限域 $$k$$ 都成立：一个非零多项式不能有无限多个零点）。

第二步：取 $$f\in\mathfrak{a}$$、$$g\in\mathfrak{b}$$。则 $$fg\in\mathfrak{a}\mathfrak{b}$$，而由上一段 $$\mathfrak{a}\mathfrak{b}$$ 中每个元素都是零多项式（因为 $$I(Z(\mathfrak{a}\mathfrak{b}))=(0)$$ 而 $$\mathfrak{a}\mathfrak{b}\subseteq I(Z(\mathfrak{a}\mathfrak{b}))$$——这一包含来自「元素在零点集上为零」）。于是 $$fg=0$$。由于 $$k[x_1,\dots,x_n]$$ 是整环（$$k$$ 是域），对**每一对** $$(f,g)\in\mathfrak{a}\times\mathfrak{b}$$ 都有「$$f=0$$ 或 $$g=0$$」。

第三步：分情形。若 $$\mathfrak{a}=(0)$$，则 $$Z(\mathfrak{a})=\mathbb{A}^{n}_{k}$$，结论成立。若 $$\mathfrak{a}\ne(0)$$，取 $$0\ne f\in\mathfrak{a}$$；由第二步，对一切 $$g\in\mathfrak{b}$$ 有 $$fg=0$$，整环给出 $$g=0$$。于是 $$\mathfrak{b}=(0)$$，从而 $$Z(\mathfrak{b})=\mathbb{A}^{n}_{k}$$。两种情形都得到结论。所以 $$\mathbb{A}^{n}_{k}$$ 不可约。

由不可约性推「开集必相交」：设 $$U,V$$ 是**不交**的两个非空开集，令 $$Z_{U}=\mathbb{A}^{n}\setminus U$$、$$Z_{V}=\mathbb{A}^{n}\setminus V$$，它们是闭真子集且 $$Z_{U}\cup Z_{V}=\mathbb{A}^{n}\setminus(U\cap V)=\mathbb{A}^{n}$$。这与不可约性矛盾。于是在 Zariski 拓扑下，**任意两个非空开集相交**。（这个论证对任何不可约空间都成立，与是否有 Zariski 无关。）

**关键 leap**：把「两个闭集覆盖全空间」翻译成「两个理想之积的零点集是全空间 ⟹ 乘积中的每个元素都是零多项式 ⟹ 每对因子中有一个为零 ⟹ 有一个理想是零理想」。**第二步（整环）是全部内容**：一旦多项式环有零因子，$$\mathbb{A}^{n}$$ 就可能被两个真闭集覆盖，不可约性崩塌。

---

**问题 2（包含关系反转，定量版）** 设 $$k$$ 代数闭，$$I,J\subseteq k[x_1,\dots,x_n]$$ 是理想。证明

$$Z(I)\subseteq Z(J)\iff \sqrt{J}\subseteq\sqrt{I}.$$

**考点**：定理 3.9 与推论 3.9。
**位置**：把「零点集包含」这件事翻译成「根理想包含」，这是几何—代数字典的使用说明书。

**解**。

**（$$\Leftarrow$$）** 设 $$\sqrt{J}\subseteq\sqrt{I}$$。若 $$a\in Z(I)$$，则 $$I$$ 中每个 $$f$$ 满足 $$f(a)=0$$；任取 $$g\in\sqrt{J}\subseteq\sqrt{I}$$，有 $$g(a)=0$$。于是 $$\sqrt{J}$$ 中一切元素在 $$a$$ 处为零，从而 $$J\subseteq\sqrt{J}$$ 中的元素也在 $$a$$ 处为零，即 $$a\in Z(J)$$。故 $$Z(I)\subseteq Z(J)$$。

**（$$\Rightarrow$$）** 设 $$Z(I)\subseteq Z(J)$$。由定理 3.9，$$\sqrt{I}=I(Z(I))$$、$$\sqrt{J}=I(Z(J))$$。设 $$g\in\sqrt{J}=I(Z(J))$$，即 $$g$$ 在 $$Z(J)$$ 上恒为零。因为 $$Z(I)\subseteq Z(J)$$，$$g$$ 也在 $$Z(I)$$ 上恒为零，即 $$g\in I(Z(I))=\sqrt{I}$$。故 $$\sqrt{J}\subseteq\sqrt{I}$$。$$\blacksquare$$

**注（这一条为什么值钱）** 它把「几何包含」与「代数包含」用**反转的箭头**精确对齐：几何上的「小」对应代数上的「大」，而对应本身是**取根之后再对应**，不是原理想直接对应。若误把 $$\sqrt{}$$ 丢掉，命题立刻假：取 $$I=(x)$$、$$J=(x^{2})$$，两者零点集都是 $$y$$ 轴，几何包含是双向的，而 $$(x^{2})\subsetneq(x)$$ 只是单向。

---

**问题 3（茎与剩余域的具体计算）** 取 $$A=\mathbb{Z}$$，$$\mathfrak{p}=(p)$$（$$p$$ 是素数），$$X=\operatorname{Spec}A$$。计算 $$\mathcal{O}_{X,\mathfrak{p}}$$、$$\mathfrak{m}_{\mathfrak{p}}$$、$$k(\mathfrak{p})$$；再对一般点 $$\eta=(0)$$ 做同样的计算。

**考点**：定义 3.14、定理 3.11。
**位置**：把「每个点有自己的剩余域」这口号变成两个能写出来的域，它是注 3.14 的实例化。

**解**。

**闭点 $$\mathfrak{p}=(p)$$。** 由定理 3.11，
$$\mathcal{O}_{X,\mathfrak{p}}=A_{\mathfrak{p}}=\Big\{\frac{a}{b}\ \Big\vert\ a,b\in\mathbb{Z},\ p\nmid b\Big\}\subseteq\mathbb{Q}.$$
这是一个局部环，唯一极大理想是
$$\mathfrak{m}_{\mathfrak{p}}=\mathfrak{p}A_{\mathfrak{p}}=\Big\{\frac{a}{b}\ \Big\vert\ p\mid a,\ p\nmid b\Big\}.$$
它确实是极大理想：商环
$$k(\mathfrak{p})=A_{\mathfrak{p}}/\mathfrak{p}A_{\mathfrak{p}}\cong\mathbb{Z}/(p)=\mathbb{F}_{p}.$$
验证这个同构：映射 $$\mathbb{Z}_{(p)}\to\mathbb{F}_{p}$$，$$a/b\mapsto(a\bmod p)(b\bmod p)^{-1}$$，分母在 $$\mathbb{F}_{p}$$ 中可逆、且映到零的恰是分子被 $$p$$ 整除的元素，即 $$\mathfrak{p}\mathbb{Z}_{(p)}$$。**剩余域是 $$\mathbb{F}_{p}$$。**

**一般点 $$\eta=(0)$$。** 由定理 3.11，$$\mathcal{O}_{X,\eta}=A_{(0)}=\mathbb{Z}_{(0)}$$。这里允许的分母是全体非零整数，故
$$\mathbb{Z}_{(0)}=\Big\{\frac{a}{b}\ \Big\vert\ a,b\in\mathbb{Z},\ b\ne0\Big\}=\mathbb{Q}.$$
它是一个域，所以唯一极大理想是 $$\mathfrak{m}_{\eta}=(0)$$，剩余域
$$k(\eta)=\mathbb{Q}/(0)=\mathbb{Q}.$$

**读数**：$$\operatorname{Spec}\mathbb{Z}$$ 这个空间上，闭点处的「函数值」住在 $$\mathbb{F}_{p}$$ 里，一般点处的「函数值」住在 $$\mathbb{Q}$$ 里。这就是注 3.14 说的「每个点有自己的剩余域」——**一条几何对象上同时住着无穷多个互不相同（且特征不同）的域**。这也是「概形统一几何与数论」的具体口径：在 $$\operatorname{Spec}\mathbb{Z}$$ 上做几何，等于同时做所有素数处的算术。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 取 $$X=\{p,q\}$$ 与离散拓扑，令 $$\mathcal{F}$$ 为常数预层 $$\mathcal{F}(U)=\mathbb{Z}$$、限制映射全取恒等。(i) 逐条验证预层公理；(ii) 找出层公理失败的那一对截面；(iii) 写出 $$\mathcal{F}$$ 的层化 $$\mathcal{F}^{\#}$$ 并算出 $$\mathcal{F}^{\#}(X)$$。

**基2.** 在 $$\mathbb{A}^{2}_{\mathbb{C}}$$ 中判断下列子集是否为 Zariski 闭集，是则写出定义理想：

$$C_{1}=\{(t,t^{2})\ \mid\ t\in\mathbb{C}\},\quad C_{2}=\{(t^{2},t^{3})\ \mid\ t\in\mathbb{C}\},\quad S=\{(x,y)\ \mid\ xy=0\},\quad T=\{(x,e^{x})\ \mid\ x\in\mathbb{C}\}.$$

**基3.** 算出 $$\operatorname{Spec}\mathbb{C}[x]/(x^{2}-1)$$、$$\operatorname{Spec}\mathbb{C}[x]/(x^{2})$$、$$\operatorname{Spec}\mathbb{R}[x]/(x^{2}+1)$$ 的点集与结构环，并解释「点数」与「环的大小」之间的落差。

**基4.** 在 $$k[x,y]$$（$$k$$ 是域）中计算 $$\sqrt{(x^{2}y,\ xy^{2})}$$ 与 $$\sqrt{(x^{2}-y^{2})}$$，并说明为什么第二个根理想等于原理想本身。

### 竞赛（本课目标难度）

**竞1.** 不引用定理 3.6(4)，独立证明 $$\operatorname{Spec}A$$ 是拟紧的。再举一例说明仿射概形一般不是 Hausdorff 空间。

**竞2.** 设 $$A$$ 是诺特环。证明 $$\operatorname{Spec}A$$ 是**诺特拓扑空间**（闭集降链终止）。

**竞3.** 设 $$I=(x^{2}+y^{2}-1,\ x-1)\subseteq\mathbb{C}[x,y]$$。算出 $$Z(I)$$ 与 $$\sqrt{I}$$，并验证 $$I(Z(I))=\sqrt{I}$$。

**竞4.** 证明根理想的素理想刻画

$$\sqrt{\mathfrak{a}}=\bigcap_{\mathfrak{p}\supseteq\mathfrak{a}}\mathfrak{p},$$

并用它加上 Hilbert 零点定理，补全推论 3.9 中「根理想与 Zariski 闭集一一对应」的证明。

### 研究（通向下一章）

**研1.** 设 $$A,B$$ 是交换环。证明

$$\operatorname{Hom}_{\text{Sch}}(\operatorname{Spec}B,\operatorname{Spec}A)\ \cong\ \operatorname{Hom}_{\text{Ring}}(A,B),$$

即 $$\operatorname{Spec}$$ 是全忠实反变函子；并指出这一步与第 62 章 Yoneda 引理的关系。

**研2.** 把圆周 $$S^{1}$$ 用两个可缩开集 $$U,V$$ 覆盖（$$U=S^{1}$$ 去掉一点，$$V=S^{1}$$ 去掉另一点）。对常数层 $$\underline{\mathbb{Z}}$$ 算 Čech 复形

$$0\to\underline{\mathbb{Z}}(U)\oplus\underline{\mathbb{Z}}(V)\xrightarrow{\ \delta\ }\underline{\mathbb{Z}}(U\cap V)\to0,$$

求 $$H^{0}$$ 与 $$H^{1}$$，并解释 $$H^{1}\ne0$$ 与「整体截面函子不正合」之间的关系。

### 解答 (Solutions)

**解 基1.** (i) 预层公理是 $$\rho^{U}_{U}=\operatorname{id}$$ 与 $$W\subseteq V\subseteq U$$ 时 $$\rho^{V}_{W}\circ\rho^{U}_{V}=\rho^{U}_{W}$$。本例中 $$\rho$$ 一律取恒等映射，两条都化成「恒等复合恒等仍是恒等」，成立。所以 $$\mathcal{F}$$ 是预层。

(ii) 取覆盖 $$X=\{p\}\cup\{q\}$$（$$X$$ 是离散拓扑）。取 $$s_p=1$$、$$s_q=2$$。因为 $$\{p\}\cap\{q\}=\varnothing$$，而空指标集的积是单点集（自动一致），这族截面满足**粘合公理的一致性条件**。但若存在 $$s\in\mathcal{F}(X)=\mathbb{Z}$$ 同时满足 $$s\vert_{\{p\}}=1$$ 与 $$s\vert_{\{q\}}=2$$，由限制映射是恒等必须有 $$s=1$$ 且 $$s=2$$，矛盾。**粘合失败，$$\mathcal{F}$$ 不是层。**（唯一性公理在这里不会失败：两条公理中先坏的是粘合。）

(iii) 层化由「局部常值整值函数」给出：$$\mathcal{F}^{\#}(U)=\{f:U\to\mathbb{Z}\ \mid\ f\ \text{在每个连通分支上为常值}\}$$。验证是层：逐点定义 $$f(x)=f_i(x)$$（$$x\in U_i$$）与 $$i$$ 的选取无关（一致性），且在每片 $$U_i$$ 上局部常值。算 $$\mathcal{F}^{\#}(X)$$：$$X$$ 有两个连通分支，故 $$\mathcal{F}^{\#}(X)=\mathbb{Z}^{2}$$。前面那对 $$(1,2)$$ 现在有归宿了。

**解 基2.** 四个都逐条算。

$$C_{1}=\{(t,t^{2})\}$$：这是抛物线，$$C_{1}=Z(y-x^{2})$$（一方面 $$y-x^{2}$$ 在每点取值 $$t^{2}-t^{2}=0$$；另一方面若 $$y=x^{2}$$ 则取 $$t=x$$ 即落在 $$C_{1}$$ 中）。**是闭集**，定义理想 $$(y-x^{2})$$。

$$C_{2}=\{(t^{2},t^{3})\}$$：这是尖点三次曲线，$$C_{2}=Z(y^{2}-x^{3})$$。验证：$$(t^{2})^{3}=t^{6}=(t^{3})^{2}$$，故 $$C_{2}\subseteq Z(y^{2}-x^{3})$$。反向：设 $$y^{2}=x^{3}$$。若 $$x=0$$，代入得 $$y^2=0$$ 即 $$y=0$$，取 $$t=0$$ 即落在 $$C_2$$ 中；若 $$x\ne0$$，令 $$t=y/x$$（这时 $$y\ne0$$，否则 $$x^3=0$$ 与 $$x\ne0$$ 矛盾），直接算：$$y^{2}=x^{3}$$ 两边除以 $$x^{2}$$ 得 $$t^2=(y/x)^{2}=y^{2}/x^{2}=x^{3}/x^{2}=x$$，即 $$x=t^{2}$$；再由 $$y=tx$$ 得 $$y=t\cdot t^{2}=t^{3}$$。两种情形都落在 $$C_2$$ 中。所以 $$C_{2}=Z(y^{2}-x^{3})$$。**是闭集**，定义理想 $$(y^{2}-x^{3})$$。

$$S=\{(x,y)\ \mid\ xy=0\}$$：$$S=Z(xy)$$。**是闭集**，定义理想 $$(xy)$$。（注意它不是不可约的：它是两条坐标轴之并，$$S=Z(x)\cup Z(y)$$。）

$$T=\{(x,e^{x})\}$$：**不是 Zariski 闭集**。用反证法。设 $$T=Z(\mathfrak{a})$$。每个 $$f\in\mathfrak{a}$$ 满足 $$f(x,e^{x})=0$$ 对一切 $$x\in\mathbb{C}$$。若 $$f\ne0$$，把它按 $$y$$ 的幂写成 $$f=\sum_{k=0}^{d}c_{k}(x)y^{k}$$，则 $$\sum_{k}c_{k}(x)e^{kx}\equiv0$$。当 $$x\to+\infty$$ 时最高次项 $$c_{d}(x)e^{dx}$$ 支配其余各项（每两个相邻指数项之比是 $$e^{-x}\to0$$，而多项式因子只有多项式增长），故恒等式不可能成立，矛盾。于是 $$\mathfrak{a}=(0)$$，从而 $$Z(\mathfrak{a})=\mathbb{A}^{2}\ne T$$。**不是闭集。**

**解 基3.** 逐个算。

$$\operatorname{Spec}\mathbb{C}[x]/(x^{2}-1)$$：$$x^{2}-1=(x-1)(x+1)$$，两因子互素，由中国剩余定理 $$\mathbb{C}[x]/(x^{2}-1)\cong\mathbb{C}\times\mathbb{C}$$。素理想是 $$\mathbb{C}\times(0)$$ 与 $$(0)\times\mathbb{C}$$，对应 $$(x-1)$$ 与 $$(x+1)$$。**两个点**。

$$\operatorname{Spec}\mathbb{C}[x]/(x^{2})$$：唯一素理想是 $$(x)$$（零维局部环只有一个素理想）。**一个点**，坐标环含非零幂零元 $$x$$。

$$\operatorname{Spec}\mathbb{R}[x]/(x^{2}+1)$$：环 $$\cong\mathbb{C}$$ 是域，唯一素理想是 $$(0)$$。**一个点**，坐标环是 $$\mathbb{C}$$。

**落差**：前两个环的点数是 $$2$$ 与 $$1$$，第三个是 $$1$$ 但剩余域是 $$\mathbb{C}$$ 而非 $$\mathbb{R}$$。**点数只看出「有多少个极大理想」，看不出环的「厚度」（幂零元）与「剩余域的扩张」。** $$\mathbb{C}[x]/(x^{2})$$ 与 $$\mathbb{C}$$ 对应同一个点，但前者结构层含 $$\varepsilon$$，后者不含——概形靠结构层区分它们（例 3.13）。

**解 基4.** 先算 $$\sqrt{\mathfrak{a}}$$，其中 $$\mathfrak{a}=(x^{2}y,\ xy^{2})$$。注意 $$\mathfrak{a}=xy\cdot(x,y)$$。一方面 $$(xy)^{2}=x^{2}y^{2}\in\mathfrak{a}$$，故 $$xy\in\sqrt{\mathfrak{a}}$$，即 $$(xy)\subseteq\sqrt{\mathfrak{a}}$$。反之设 $$f^{m}\in\mathfrak{a}$$：$$\mathfrak{a}$$ 中每个非零元素都被 $$xy$$ 整除（它由 $$x^{2}y$$ 与 $$xy^{2}$$ 生成），故 $$f^{m}\in(xy)$$。在 UFD 中 $$xy$$ 的不可约因子是 $$x$$ 与 $$y$$；由 $$x$$ 是素元、从 $$x\mid f^{m}$$ 得 $$x\mid f$$，同理 $$y\mid f$$，故 $$xy\mid f$$，即 $$f\in(xy)$$。于是

$$\sqrt{(x^{2}y,\ xy^{2})}=(xy).$$

再算 $$\sqrt{(x^{2}-y^{2})}$$。因式分解 $$x^{2}-y^{2}=(x-y)(x+y)$$，两个因子互素（它们的组合 $$(x+y)-(x-y)=2y$$ 与 $$x-y$$ 的公因子是常数）且都不可约。设 $$f^{m}\in(x^{2}-y^{2})$$，则两因子各整除 $$f^{m}$$，进而在 UFD 中各整除 $$f$$，故其积整除 $$f$$。所以

$$\sqrt{(x^{2}-y^{2})}=(x^{2}-y^{2}).$$

**为什么第二个等于自身**：$$x^{2}-y^{2}$$ **无平方因子**（两个不同不可约元之积），而 UFD 中一个理想等于它的根当且仅当生成元无平方因子。反面对照第一问：$$x^{2}y$$ 有平方因子 $$x$$，所以根理想更大。

**解 竞1.** 

**拟紧性。** 设 $$\operatorname{Spec}A=\bigcup_{i\in I}O_i$$ 是任意开覆盖。

第一步：化归到 $$D(f)$$ 形状的覆盖。对每点 $$\mathfrak{p}$$，取 $$i(\mathfrak{p})$$ 使 $$\mathfrak{p}\in O_{i(\mathfrak{p})}$$。则 $$\mathfrak{p}\notin V(\mathfrak{a})$$（其中 $$V(\mathfrak{a})=\operatorname{Spec}A\setminus O_{i(\mathfrak{p})}$$），即存在 $$f_{\mathfrak{p}}\in\mathfrak{a}$$ 使 $$f_{\mathfrak{p}}\notin\mathfrak{p}$$，于是

$$\operatorname{Spec}A=\bigcup_{\mathfrak{p}}D(f_{\mathfrak{p}}),\qquad D(f_{\mathfrak{p}})\subseteq O_{i(\mathfrak{p})}.$$

第二步：有限化。令 $$J=(f_{\mathfrak{p}})_{\mathfrak{p}}$$。若 $$J\ne A$$，由 Zorn 引理 $$J$$ 含于极大理想 $$\mathfrak{m}$$；但 $$\mathfrak{m}$$ 落在某个 $$D(f_{\mathfrak{p}})$$ 里，即 $$f_{\mathfrak{p}}\notin\mathfrak{m}$$，与 $$f_{\mathfrak{p}}\in J\subseteq\mathfrak{m}$$ 矛盾。故 $$J=A$$，即 $$1=\sum_{j=1}^{k}a_jf_{\mathfrak{p}_j}$$ 对有限个指标成立。

第三步：收尾。由 $$1\in(f_{\mathfrak{p}_1},\dots,f_{\mathfrak{p}_k})$$ 得 $$\bigcap_jV(f_{\mathfrak{p}_j})=\varnothing$$，即 $$\operatorname{Spec}A=\bigcup_{j}D(f_{\mathfrak{p}_j})$$；而各 $$D(f_{\mathfrak{p}_j})\subseteq O_{i(\mathfrak{p}_j)}$$，故这 $$k$$ 个 $$O$$ 已是有限子覆盖。**拟紧。**

**不 Hausdorff 的例子。** 取 $$A=\mathbb{Z}$$、点 $$(2)$$ 与 $$(3)$$。若含 $$(2)$$ 的开集与含 $$(3)$$ 的开集不交，则存在 $$f\notin(2)$$、$$g\notin(3)$$ 使 $$D(f)\cap D(g)=D(fg)=\varnothing$$，即 $$fg$$ 落在一切素理想里，故 $$fg$$ 幂零；而 $$\mathbb{Z}$$ 无幂零元，故 $$fg=0$$，即 $$f=0$$ 或 $$g=0$$，与 $$f\notin(2)$$ 矛盾。**它们无法分离。**

**解 竞2.** 设

$$V(\mathfrak{a}_1)\supseteq V(\mathfrak{a}_2)\supseteq V(\mathfrak{a}_3)\supseteq\cdots$$

是闭集的降链（不妨设各 $$\mathfrak{a}_i$$ 是根理想，因为 $$V(\mathfrak{a})=V(\sqrt{\mathfrak{a}})$$）。对每项取 $$I$$：

$$I\big(V(\mathfrak{a}_1)\big)\subseteq I\big(V(\mathfrak{a}_2)\big)\subseteq I\big(V(\mathfrak{a}_3)\big)\subseteq\cdots$$

这是 $$A$$ 中理想的升链（由 $$V(\mathfrak{a})\subseteq V(\mathfrak{b})\Rightarrow \mathfrak{b}\subseteq\mathfrak{a}$$ 得方向：闭集越小，割掉它的多项式越多）。$$A$$ 诺特，故升链在某个 $$N$$ 处稳定：

$$I\big(V(\mathfrak{a}_N)\big)=I\big(V(\mathfrak{a}_{N+1})\big)=\cdots$$

对根理想 $$\mathfrak{a}$$ 有恒等式（竞4 将证）

$$\mathfrak{a}=I\big(V(\mathfrak{a})\big),$$

于是 $$\mathfrak{a}_N=\mathfrak{a}_{N+1}=\cdots$$，从而 $$V(\mathfrak{a}_N)=V(\mathfrak{a}_{N+1})=\cdots$$。**降链终止，$$\operatorname{Spec}A$$ 是诺特拓扑空间。**（这里只用到 $$A$$ 诺特，即理想升链终止；不需要 $$A$$ 是有限生成 $$k$$-代数。）

**解 竞3.** 先算 $$Z(I)$$。$$Z(I)=Z(x^{2}+y^{2}-1)\cap Z(x-1)$$。在 $$Z(x-1)$$ 上 $$x=1$$，代进第一个方程得 $$1+y^{2}-1=y^{2}=0$$，即 $$y=0$$。所以

$$Z(I)=\{(1,0)\}.$$

再算 $$\sqrt{I}$$。作商 $$k[x,y]\to\mathbb{C}[y]$$，$$x\mapsto1$$，$$y\mapsto y$$。它的核是 $$(x-1)$$，而 $$I$$ 在其中的像是

$$(1^{2}+y^{2}-1,\ 0)=(y^{2}).$$

于是 $$\mathbb{C}[x,y]/I$$ 的「根」问题可以搬到 $$\mathbb{C}[y]/(y^{2})$$ 上：$$f\in\sqrt{I}$$ 当且仅当 $$f$$ 在 $$\mathbb{C}[y]$$ 中的像落在 $$\sqrt{(y^{2})}=(y)$$。往回翻译，$$\sqrt{I}$$ 恰是 $$(\bar y)$$ 的原像，即

$$\sqrt{I}=(x-1,\ y).$$

验证 $$I(Z(I))=(x-1,y)$$：在点 $$(1,0)$$ 处为零的多项式恰是以 $$(1,0)$$ 为根的那些，而所有这些多项式构成的理想是极大理想 $$(x-1,y)$$（这是 $$k$$ 代数闭时极大理想的标准形状，由定理 3.8 的证明给出）。于是

$$I(Z(I))=(x-1,y)=\sqrt{I},$$

与定理 3.9 一致。

**解 竞4.** 

**根理想的刻画。** 证明 $$\sqrt{\mathfrak{a}}=\bigcap_{\mathfrak{p}\supseteq\mathfrak{a}}\mathfrak{p}$$。

「$$\subseteq$$」：设 $$f\in\sqrt{\mathfrak{a}}$$，即 $$f^{m}\in\mathfrak{a}$$ 对某个 $$m\ge1$$。任取素理想 $$\mathfrak{p}\supseteq\mathfrak{a}$$，则 $$f^{m}\in\mathfrak{p}$$；由 $$\mathfrak{p}$$ 素与归纳得 $$f\in\mathfrak{p}$$。故 $$f$$ 落在右边。

「$$\supseteq$$」：设 $$f\notin\sqrt{\mathfrak{a}}$$，即 $$f^{m}\notin\mathfrak{a}$$ 对一切 $$m\ge1$$。考虑乘法封闭集 $$S=\{1,f,f^{2},\dots\}$$ 与局部化 $$A_f=S^{-1}A$$。我们先用反证说明 $$\mathfrak{a}A_f\ne A_f$$：若 $$\mathfrak{a}A_f=A_f$$，则 $$1/1\in\mathfrak{a}A_f$$，即 $$1/1=\sum_j(a_j/1)\cdot(b_j/f^{k})$$ 对某几个 $$a_j\in\mathfrak{a}$$；两边乘 $$f^{K}$$（$$K$$ 取各 $$k$$ 的最大值）得 $$f^{K}=\sum_j a_jb_jf^{K-k}\in\mathfrak{a}$$，与假设矛盾。于是 $$\mathfrak{a}A_f$$ 是 $$A_f$$ 的真理想，含于某个极大理想 $$\mathfrak{n}$$。取原像 $$\mathfrak{p}=\{a\in A\ \mid\ a/1\in\mathfrak{n}\}$$。按局部化与素理想的对应，$$\mathfrak{p}$$ 是素理想且 $$\mathfrak{a}\subseteq\mathfrak{p}$$。又 $$f/1$$ 在 $$A_f$$ 中可逆，故 $$f/1\notin\mathfrak{n}$$（单位不落在任何真理想中），于是 $$f\notin\mathfrak{p}$$。这个 $$\mathfrak{p}$$ 满足 $$\mathfrak{p}\supseteq\mathfrak{a}$$ 而 $$f\notin\mathfrak{p}$$，故 $$f$$ 不在右边的交里。

综上两边相等。$$\blacksquare$$

**补全推论 3.9 的证明。** 设 $$k$$ 代数闭，定义两个映射

$$\Phi:\{\mathfrak{a}=\sqrt{\mathfrak{a}}\}\to\{Y\ \text{闭}\},\quad \mathfrak{a}\mapsto Z(\mathfrak{a});\qquad \Psi:\{Y\ \text{闭}\}\to\{\mathfrak{a}=\sqrt{\mathfrak{a}}\},\quad Y\mapsto I(Y).$$

要证 $$\Psi\Phi=\operatorname{id}$$ 与 $$\Phi\Psi=\operatorname{id}$$。

**$$\Psi\Phi=\operatorname{id}$$**：对根理想 $$\mathfrak{a}$$，$$I(Z(\mathfrak{a}))=\sqrt{\mathfrak{a}}=\mathfrak{a}$$，这正是定理 3.9。

**$$\Phi\Psi=\operatorname{id}$$**：对闭集 $$Y=Z(\mathfrak{b})$$。「$$Y\subseteq Z(I(Y))$$」来自定义。反向：设 $$\mathfrak{q}\notin Y$$，则存在 $$g\in\mathfrak{b}$$ 使 $$g\notin\mathfrak{q}$$；而 $$g\in\mathfrak{b}\subseteq I(Z(\mathfrak{b}))=I(Y)$$（用了 $$I$$ 的单调性与「$$\mathfrak{b}$$ 中元素在 $$Y$$ 上为零」）。取 $$f=g$$ 即得 $$\mathfrak{q}\notin Z(I(Y))$$。

两个映射互逆，故都是双射。**这就是推论 3.9。** $$\blacksquare$$

**解 研1.** 分三步：造两个方向的映射，再证互逆。

**方向一**。设 $$\varphi:A\to B$$ 是环同态，定义 $$f:\operatorname{Spec}B\to\operatorname{Spec}A$$，$$f(\mathfrak{q})=\varphi^{-1}(\mathfrak{q})$$。

*良定义*：若 $$xy\in\varphi^{-1}(\mathfrak{q})$$，则 $$\varphi(x)\varphi(y)\in\mathfrak{q}$$，由 $$\mathfrak{q}$$ 素得 $$x$$ 或 $$y$$ 落在其中；又 $$1\notin\varphi^{-1}(\mathfrak{q})$$（否则 $$1=\varphi(1)\in\mathfrak{q}$$）。

*连续*：$$f^{-1}\big(D(a)\big)=D(\varphi(a))$$——$$\varphi^{-1}(\mathfrak{q})\in D(a)$$ 等价于 $$\varphi(a)\notin\mathfrak{q}$$，等价于 $$\mathfrak{q}\in D(\varphi(a))$$。

*层映射*：对 $$a\in A$$ 定义 $$A_a\to B_{\varphi(a)}$$，$$u/a^{m}\mapsto\varphi(u)/\varphi(a)^{m}$$；它与局部化相容、在交上相容，故粘成 $$f^{\#}:\mathcal{O}_{\operatorname{Spec}A}\to f_{*}\mathcal{O}_{\operatorname{Spec}B}$$。茎上它把 $$A_{\mathfrak{p}}$$（$$\mathfrak{p}=\varphi^{-1}(\mathfrak{q})$$）送到 $$B_{\mathfrak{q}}$$，且 $$\varphi(\mathfrak{p})\subseteq\mathfrak{q}$$ 使 $$\mathfrak{p}A_{\mathfrak{p}}$$ 落到 $$\mathfrak{q}B_{\mathfrak{q}}$$，故是**局部同态**。记为 $$\operatorname{Spec}\varphi$$。

**方向二**。设 $$(f,f^{\#}):\operatorname{Spec}B\to\operatorname{Spec}A$$。取整体截面得环同态

$$A=\Gamma(\operatorname{Spec}A,\mathcal{O})\xrightarrow{\ f^{\#}\ }\Gamma\big(\operatorname{Spec}B,\ f_{*}\mathcal{O}\big)=\Gamma(\operatorname{Spec}B,\mathcal{O})=B,$$

两个等号来自定理 3.11 在 $$U=D(1)$$ 上的情形。

**互逆**。从 $$\varphi$$ 造出的 $$\operatorname{Spec}\varphi$$ 再取整体截面，得到 $$\varphi$$ 本身（$$D(1)=\operatorname{Spec}A$$ 时的层映射就是 $$\varphi$$）。反之，若取出的全局同态是 $$\varphi$$，则 $$f^{\#}$$ 在每个 $$D(a)$$ 上的分量由它在整空间上的分量限制而来（层的相容性），故 $$f^{\#}$$ 被 $$\varphi$$ 完全决定。于是两个方向互逆，得到双射。

**与 Yoneda 的关系。** 第 62 章的 Yoneda 引理给出 $$\operatorname{Nat}\big(\operatorname{Hom}_{\mathcal{C}}(c,-),F\big)\cong F(c)$$；特别地，嵌入 $$c\mapsto\operatorname{Hom}_{\mathcal{C}}(-,c)$$ 全忠实。这里的 $$\operatorname{Spec}$$ 是同一件事在**反变**一侧的形态：把环 $$A$$ 送到 $$\operatorname{Hom}_{\text{Ring}}(A,-)$$，再几何化为 $$\operatorname{Spec}A$$；上面的双射正是「概形之间的映射被它的可表函子完全决定」。**全忠实性保证 $$\operatorname{Spec}A$$ 唯一决定 $$A$$**，这就是「几何可以替代代数」的精确断言。

**接到下一章**：第 74 章把向量丛做成局部自由层，而层与层之间的态射正是靠「先局部、再按相容性粘合」定义与验证的。**本章刚证的这个双射，就是下一章「向量丛的态射 = $$\mathcal{O}_X$$-模层同态」这条定理的模型。**

**解 研2.** 把 $$S^{1}$$ 看成 $$\mathbb{R}/\mathbb{Z}$$，取 $$U=S^{1}\setminus\{0\}$$、$$V=S^{1}\setminus\{\tfrac12\}$$。两者都同胚于开区间，可缩；$$U\cap V$$ 是两条开区间之并，两个分支都可缩但不连通。

**截面。** 对局部常值整值函数层：$$\underline{\mathbb{Z}}(U)=\mathbb{Z}$$、$$\underline{\mathbb{Z}}(V)=\mathbb{Z}$$、$$\underline{\mathbb{Z}}(U\cap V)=\mathbb{Z}\oplus\mathbb{Z}$$（因为 $$U\cap V$$ 有两个连通分支，函数在每个分支上各取一个常值，两个值独立）。

**Čech 复形。** 覆盖只有两片，复形退化为

$$0\to\underline{\mathbb{Z}}(U)\oplus\underline{\mathbb{Z}}(V)\xrightarrow{\ \delta\ }\underline{\mathbb{Z}}(U\cap V)\to0,\qquad\delta(a,b)=(b-a,\ b-a),$$

后一个写法是因为 $$U$$、$$V$$ 上都是常值 $$a$$、$$b$$，限制到每个分支仍是 $$a$$、$$b$$。

**算。** $$H^{0}=\ker\delta=\{(a,b)\ \mid\ b=a\}=\{(a,a)\}\cong\mathbb{Z}$$，这就是整体截面 $$\Gamma(S^{1},\underline{\mathbb{Z}})=\mathbb{Z}$$，与「$$S^{1}$$ 连通」一致。又 $$\delta$$ 的像是对角线子群 $$\{(c,c)\}$$，故

$$H^{1}=\operatorname{coker}\delta=(\mathbb{Z}\oplus\mathbb{Z})/\{(c,c)\}\cong\mathbb{Z},$$

同构可由 $$(m,n)\mapsto m-n$$ 显式给出。

**解释 $$H^{1}\ne0$$。** 在 $$U$$、$$V$$ 上各给一个常值截面是**局部数据**；当两份数据在交上「差一个整数」$$m-n$$ 时，它不来自任何整体截面，而 $$m-n$$ 正是**绕圆周的圈数**——与第 16 章的 $$\pi_{1}(S^{1})\cong\mathbb{Z}$$ 是同一个 $$\mathbb{Z}$$。更一般地：整体截面函子 $$\Gamma(S^{1},-)$$ 若正合，则把层正合列作用后 $$H^{1}$$ 会恒为零；而这里 $$H^{1}=\mathbb{Z}\ne0$$，**「局部截面能拼成整体截面」这件事在同调上有障碍，障碍的大小就是 $$\mathbb{Z}$$**。第 70 章的导出函子到这里第一次露出几何的一面：$$H^{i}$$ 就是 $$\Gamma$$ 的第 $$i$$ 个右导出函子。

**接到下一章**：第 74 章把 $$\underline{\mathbb{Z}}$$ 换成向量丛的截面层（局部自由层），把 $$H^{1}$$ 解释成「向量丛的扭结」（Picard 群、第一 Chern 类）的载体，并把 de Rham 上同调与层上同调正式等同。**$$S^{1}$$ 上的这个 $$\mathbb{Z}$$ 就是那一章所有计算的最小样本。**

## 七、Takeaway 与延伸 (Takeaways)

**1. 几何的对象可以换，换法是把「点」看成「函数环的极大理想」。** 这一步的真正内容在定理 3.13：$$\operatorname{Spec}$$ 与整体截面 $$\Gamma$$ 互为伴随，且 $$\operatorname{Spec}$$ 全忠实。于是「几何研究空间」与「代数研究环」不是类比，而是**同一个范畴的两种写法**——第 62 章的 Yoneda 引理在这里第一次兑现成几何定理。

**2. Zariski 拓扑的职责是「分类点」，不是「分离点」。** 它粗得出格：任意两个非空开集相交、连两点都难分离（推论 3.5、练习竞1）。这种粗不是缺陷，而是为了让闭集族恰好等于「多项式公共零点集族」，从而拓扑完全由环的代数运算决定。局部信息因此不能靠开集，只能靠**茎**——而茎是纯代数的（$$\mathcal{O}_{X,\mathfrak{p}}=A_{\mathfrak{p}}$$）。

**3. 层是比纤维丛更宽的框架，两者的分界是「局部自由」。** 第 12 章的丛要求局部同构于 $$U\times F$$；层只要求局部截面能粘合（定义 3.10）。因此「丛 ⟹ 层」单向通行，「层 ⟹ 丛」只在局部自由时成立。这个不对称是第 74 章的起点。

**4. Hilbert 零点定理是那部字典的核心条目，也是「为什么要概形」的答案。** $$\sqrt{\mathfrak{a}}=I(Z(\mathfrak{a}))$$ 精确说出了「理想与它定义的几何对象差多少」：差的正是不在理想里、但在零点集上为零的那些元素。它一旦失效（注 3.9：$$\mathbb{R}$$ 上的 $$x^{2}+1$$），就正好是概形出场的地方——$$\operatorname{Spec}$$ 中多出一个古典簇理论看不见的点。

**5. 有理函数域看不见结点，而上同调把它们捡回来。** 例 3.15 说明：双有理等价（$$k(C)\cong k(t)$$）抹掉了结点，坐标环（$$k[C]\not\cong k[t]$$）却记得。**几何学家需要一种既能记住「差多少」、又能算出来的不变量**——那就是上同调。

---

### 下一章的悬念

第 74 章「从向量丛到上同调」要做三件事：

1. 把向量丛改写成**局部自由层与可逆层**，直接对准第 12 章与例 3.13 的几何直觉；
2. 定义**层上同调** $$H^{i}(X,\mathcal{F})=R^{i}\Gamma(X,\mathcal{F})$$，即第 70 章「导出函子」在整体截面函子上的应用，并证明它等于 Čech 上同调（练习研2 是这条路线的第一个样本）；
3. 把 de Rham 上同调（第 28 章）解释成常数层 $$\underline{\mathbb{R}}$$ 的层上同调，把「分析式上同调」与「代数式上同调」合流。

一句话：**本章搭好舞台（层、拓扑、概形），第 74 章才开始演出（上同调的计算）。**

### 延伸阅读

- Robin Hartshorne, *Algebraic Geometry*, GTM 52. 第 II 章是概形与层的标准参考，第 III 章是层上同调。
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*. 现代范畴化写法，把本章每个构造都写成函子与万有性质。
- Igor Shafarevich, *Basic Algebraic Geometry 1*. 对「有理函数域与双有理分类」的讲述比 Hartshorne 初等。
- Atiyah–MacDonald, *Introduction to Commutative Algebra*. 本章用到的素理想、局部化、Zorn 引理、诺特性都在第 1、3 章。
- 原专栏 MP129、MP133、MP138–MP140、MP145。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch71_层_Zariski拓扑_概形_Hilbert零点定理_上.md">← 第71章 层、Zariski 拓扑、概形、Hilbert 零点定理·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch73_从向量丛到上同调_上.md">第73章 从向量丛到上同调·上 →</a></div>
</div>
