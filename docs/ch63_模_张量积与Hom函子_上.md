---
layout: default
---

# 第63章: 模、张量积与 Hom 函子·上：预备与直觉 (Modules, Tensor Products and the Hom Functor · Part I: Warm-up and Intuition)

> 配套深化: 见 第64章 模、张量积与 Hom 函子·下（完整推导），本章是它的具体铺垫，建议先读本章
> 对应原专栏: MP114–MP117、Hom函子
> 专家依据: `_experts/algebra/commutative-algebra.md`（主）+ `_experts/algebra/category-universal-properties.md`
> 知识库依据: `opc2/knowledge/math/交换代数/`（8 篇）、`opc2/knowledge/math/代数几何/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

第64章里，模的公理只是把"域"换成"环"这一个词，可紧跟着冒出来的几件事，每一件都在一行内压缩了好几步具体运算："张量积用一个几乎无穷大的自由模造出来、又一口气商掉四类关系"；"正合列像变戏法一样，张量积只保右边、$$\operatorname{Hom}$$ 只保左边"；"模可能压根没有基"。这些结论都对，但推导速度对一个刚学会"环可以不是域"的读者来说太快。

本章不引入任何第64章之外的新数学，只把这几步拆开：先在几个手指头数得过来的具体例子（$$\mathbb{Z}/4$$、$$\mathbb{Z}/2$$、$$\mathbb{Z}/3$$、$$\mathbb{Z}/6$$、$$\mathbb{Q}$$）上把这些运算真正算一遍，让第64章的严格陈述出现时，你已经知道"为什么会这样、为什么必须这样定义"。读完本章，你应该能不看书直接算出 $$\mathbb{Z}/4\otimes_{\mathbb{Z}}\mathbb{Z}/6$$、$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/3,\mathbb{Z}/9)$$ 这类数值，并能说清楚"模为什么可能没有基"背后卡住的到底是哪一条公理。

## 二、入口：一道具体的问题 (Entry Problem)

**先做题，不给定义。** 下面四问都能在纸上直接算出来，用到的规则只有一条：标量乘法与加法的日常算术（第 3 节才会把这条规则正式写成公理）。

**(a)** 数一数 $$\mathbb{Z}/2\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/2\mathbb{Z}$$ 里有几个元素——只要求算出"个数"，不要求给出严格证明。

**(b)** 再数一数 $$\mathbb{Z}/2\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/3\mathbb{Z}$$（这次两个数互素）。先猜一猜答案会不会跟 (a) 不一样，再想办法验证你的猜测。

**(c)** $$\mathbb{Z}/4\mathbb{Z}$$ 能不能当 $$\mathbb{R}$$-向量空间用？试着解方程 $$2x=\bar1$$（$$x\in\mathbb{Z}/4\mathbb{Z}$$，把 $$\bar1,\bar2,\bar3,\bar0$$ 都代进去试），看看到底卡在哪一步、卡住的是"加法"还是"乘法"。

**(d)** 一个个数：$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/4\mathbb{Z},\mathbb{Z}/6\mathbb{Z})$$ 里到底有几个模同态？提示：一个同态完全由 $$\bar1$$ 的像决定，把 $$\bar1$$ 可能的像（$$\mathbb{Z}/6\mathbb{Z}$$ 的六个元素）逐个代进去检验哪些能用。

> 第 3 节会把 (a)(b) 用两种手算方法重新做一遍并给出严格论证；(c) 会告诉你卡住的公理是哪一条；(d) 的枚举法会在第 5 节被同一个方法用到 $$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/3,\mathbb{Z}/9)$$ 上再练一次。这四问对应的是第64章入口题 (a)(b)(c)(d) 的预热版——数字更小，只要求算，不要求一般证明。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 模：先撞一下"除法"这条腿

**具体验证，从加法算起。** 取 $$\mathbb{Z}/4\mathbb{Z}=\{\bar0,\bar1,\bar2,\bar3\}$$，标量取普通整数。先验证两条你在线性代数里天天用、却从没写下来验证过的规则，代进真数字：

$$(2+3)\cdot\bar1\ \overset{?}{=}\ 2\cdot\bar1+3\cdot\bar1 .$$

左边：$$2+3=5$$，$$5\cdot\bar1=\bar5=\bar1$$（$$5$$ 除以 $$4$$ 余 $$1$$）。右边：$$2\cdot\bar1=\bar2$$，$$3\cdot\bar1=\bar3$$，$$\bar2+\bar3=\bar5=\bar1$$。两边都是 $$\bar1$$，等式成立。再验证另一条：

$$(2\cdot3)\cdot\bar1\ \overset{?}{=}\ 2\cdot(3\cdot\bar1) .$$

左边：$$2\cdot3=6$$，$$6\cdot\bar1=\bar6=\bar2$$。右边：$$3\cdot\bar1=\bar3$$，$$2\cdot\bar3=\bar6=\bar2$$。两边都是 $$\bar2$$，也成立。这两条算下来没有用到任何"除法"——只用了整数的加法与乘法分配律，一步没跳。

**具体验证，除法这条腿断在哪。** 现在试着把 $$\mathbb{Z}/4\mathbb{Z}$$ 当 $$\mathbb{R}$$-向量空间用，也就是允许标量取 $$\frac12$$。逐个代入 $$x=\bar0,\bar1,\bar2,\bar3$$ 解方程 $$2x=\bar1$$：

$$2\cdot\bar0=\bar0,\quad 2\cdot\bar1=\bar2,\quad 2\cdot\bar2=\bar0,\quad 2\cdot\bar3=\bar2 .$$

四个结果只有 $$\bar0,\bar2$$ 两种，$$\bar1$$ 根本不在"翻倍"能到达的范围里——**翻倍这个操作在 $$\mathbb{Z}/4\mathbb{Z}$$ 里永远落在偶数下标上，奇数下标出不来。** 于是 $$\frac12\cdot\bar1$$ 没有任何候选值能让 $$2\cdot\big(\frac12\cdot\bar1\big)=\bar1$$ 成立——这正是入口题 (c) 卡住的地方：**不是加法坏了（加法四条公理照样成立），是"$$2$$ 在 $$\mathbb{Z}/4\mathbb{Z}$$ 里没有逆"这件事，把"除以 $$2$$"堵死了。**

**从具体到一般。** 上面两段分别验证了"加法与乘法如何交织"（第一段，永远成立）与"标量能不能被除"（第二段，只在标量环是域时成立）。这正是模论要抓住的分界线，现在把它写成定义。

**定义 3.1（$$A$$-模）** 设 $$A$$ 是含单位元 $$1$$ 的环。一个 **$$A$$-模** 是三元组 $$(M,+,\cdot)$$，其中 $$(M,+)$$ 是 Abel 群，$$\cdot:A\times M\to M$$ 满足：对一切 $$a,b\in A$$、$$m,n\in M$$，

$$a\cdot(m+n)=a\cdot m+a\cdot n,\qquad (a+b)\cdot m=a\cdot m+b\cdot m,$$
$$(ab)\cdot m=a\cdot(b\cdot m),\qquad 1\cdot m=m .$$

（若 $$A$$ 是域，这就是向量空间的公理——一字不改。第64章定义 3.1 给出更完整的左模/右模两个版本，本章只取交换环的情形，因为下面所有具体例子的标量环都交换。）

**例 3.1（$$\mathbb{Z}/n\mathbb{Z}$$ 是 $$\mathbb{Z}$$-模）** 任何 Abel 群 $$M$$ 自动是 $$\mathbb{Z}$$-模，标量乘法由 $$1\cdot m=m$$ 与加法反复相加唯一给出：$$n\cdot m=m+\cdots+m$$（$$n$$ 项）。上面对 $$\mathbb{Z}/4\mathbb{Z}$$ 的两条验证，正是这条一般事实的一个具体实例——不用重新验证公理，因为它们自动继承自"整数加法自身的分配律与结合律"。

**命题 3.2（$$\mathbb{Z}/4\mathbb{Z}$$ 不是 $$\mathbb{R}$$-向量空间）** 不存在使 $$\mathbb{Z}/4\mathbb{Z}$$ 成为 $$\mathbb{R}$$-向量空间的标量乘法（且与已有的整数标量乘法相容）。

*证明*。若存在，取 $$m=\bar1$$，由公理 $$(ab)\cdot m=a\cdot(b\cdot m)$$（$$a=2,b=\frac12$$）得 $$2\cdot\big(\frac12\cdot m\big)=1\cdot m=\bar1$$。但上面已经逐一验证：$$2$$ 乘 $$\mathbb{Z}/4\mathbb{Z}$$ 的任何元素只能落在 $$\{\bar0,\bar2\}$$，不可能等于 $$\bar1$$。矛盾。$$\blacksquare$$

**这就是第64章例 3.1(i) 与注 3.1 要讲的分水岭的具体版本：卡住向量空间理论下放到环上的，从来不是加法，而是"标量环里的非零元不一定可逆"。**

### 3.2 张量积热身：用手把生成元-关系走一遍

**目标记号。** 我们想给一对元素 $$m\in M,\ n\in N$$ 配一个符号 $$m\otimes n$$，使它满足两条搬运规则（先承认规则，不问出处，第64章定义 3.11 会给出它们从何而来）：

$$(am)\otimes n=a(m\otimes n)=m\otimes(an)\qquad(a\in\mathbb{Z})，$$

以及对每个变元各自可加。**光有记号还不够**，我们需要知道 $$m\otimes n$$ 到底是不是 $$0$$——这正是入口题 (a)(b) 要算的东西，下面用手把它做出来。

**计算 (a)：$$\mathbb{Z}/2\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/2\mathbb{Z}$$。** 两个因子都由 $$\bar1$$ 生成，所以整个张量积由 $$u:=\bar1\otimes\bar1$$ 生成（任何 $$a\bar1\otimes b\bar1$$ 都等于 $$ab\cdot u$$，把标量一路搬到同一边）。先看 $$u$$ 被什么零化：

$$2u=(2\cdot\bar1)\otimes\bar1=\bar0\otimes\bar1=0$$

（用了 $$2\cdot\bar1=\bar0$$ 在 $$\mathbb{Z}/2\mathbb{Z}$$ 中成立，再把这个 $$\bar0$$ 搬回符号里）。所以 $$u$$ 的阶整除 $$2$$，张量积至多有 $$2$$ 个元素——但**这还没排除 $$u=0$$（张量积整个塌成一个元素）的可能性**，需要另一步才能确认 $$u\ne0$$。

**见证映射，第64章反复用的技巧。** 造一个具体的双线性映射 $$h:\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}\to\mathbb{Z}/2\mathbb{Z}$$，$$h(a,b):=ab$$（就用 $$\mathbb{Z}/2\mathbb{Z}$$ 自己的乘法）。这是 $$\mathbb{Z}$$-双线性的：对每个变元分别可加（乘法对加法的分配律），且与整数标量搬运相容。按照 $$m\otimes n$$ 该满足的搬运规则，$$h$$ 必须能"读出" $$u$$ 的取值：把 $$u=\bar1\otimes\bar1$$ 喂给 $$h$$ 对应的求值，得到 $$h(\bar1,\bar1)=\bar1\cdot\bar1=\bar1\ne0$$。**如果 $$u$$ 真是 $$0$$，任何双线性映射读出来的值都该是 $$0$$（$$0$$ 元素喂给线性的东西只能出 $$0$$）——但 $$h$$ 读出了 $$\bar1\ne0$$，所以 $$u\ne0$$。** 于是 $$u$$ 的阶恰好是 $$2$$，

$$\mathbb{Z}/2\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/2\mathbb{Z}\ \cong\ \mathbb{Z}/2\mathbb{Z}\qquad(\text{恰好 2 个元素：}0,u)。$$

**这回答了入口题 (a)。**

**计算 (b)：$$\mathbb{Z}/2\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/3\mathbb{Z}$$。** 同样由 $$u:=\bar1\otimes\bar1$$ 生成。这次 $$u$$ 同时被两个数零化：

$$2u=(2\cdot\bar1)\otimes\bar1=\bar0\otimes\bar1=0\qquad(\text{在 }\mathbb{Z}/2\mathbb{Z}\text{ 里 }2\cdot\bar1=\bar0)，$$
$$3u=\bar1\otimes(3\cdot\bar1)=\bar1\otimes\bar0=0\qquad(\text{在 }\mathbb{Z}/3\mathbb{Z}\text{ 里 }3\cdot\bar1=\bar0)。$$

$$2$$ 与 $$3$$ 互素，Bézout 等式 $$1=3\cdot1+2\cdot(-1)$$（验证：$$3-2=1$$）给出

$$u=1\cdot u=(3\cdot1+2\cdot(-1))\cdot u=1\cdot(3u)+(-1)\cdot(2u)=1\cdot0+(-1)\cdot0=0 .$$

**这一次 $$u$$ 本身就被逼成 $$0$$**，而张量积又是由 $$u$$ 生成的，所以整个张量积只剩零元素：

$$\mathbb{Z}/2\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/3\mathbb{Z}=0 .$$

**这回答了入口题 (b)：你的猜测应该是"不一样"——(a) 是 $$2$$ 个元素，(b) 塌成 $$1$$ 个（零模）。差别就在于 $$2,2$$ 不互素而 $$2,3$$ 互素。** 对照着看：(a) 那一步没法用 Bézout 把 $$u$$ 消成 $$0$$（$$2,2$$ 的最大公因子是 $$2$$，不是 $$1$$），所以留下了残余；(b) 里 $$2,3$$ 互素，Bézout 把残余一次性搬空。

**从具体到一般。** 上面两次计算用到的"搬运规则"与"见证映射排除塌陷"，正是张量积一般理论的全部技术内核。现在写下一般定义。

**定义 3.3（$$A$$-双线性映射）** 设 $$M,N,P$$ 是 $$A$$-模。$$h:M\times N\to P$$ 称为 **$$A$$-双线性**，若固定一个变元时对另一个变元 $$A$$-线性。（这正是 3.2 里 $$h(a,b)=ab$$ 满足的条件，也是 $$\otimes$$ 本身该满足的条件。）

**定义 3.4（张量积的泛性质）** 一对 $$(T,\otimes)$$（$$T$$ 是 $$A$$-模，$$\otimes:M\times N\to T$$ 双线性）称为 $$M,N$$ 的**张量积**，若对任何双线性 $$h:M\times N\to P$$，存在唯一同态 $$\bar h:T\to P$$ 使 $$\bar h\circ\otimes=h$$。**它的存在性与唯一性、以及为什么必须造一个"自由模模掉关系"才能得到 $$T$$——这些完整证明留给第64章定理 3.12、3.13；本章只负责让你先亲手算出几个具体的 $$T$$。**

**这条定义解释了"见证映射"技巧为什么管用**：泛性质说任何双线性 $$h$$ 都能唯一分解成 $$\bar h\circ\otimes$$，所以 $$\bar h(m\otimes n)=h(m,n)$$——**如果 $$h(m,n)\ne0$$，$$m\otimes n$$ 就不可能是 $$0$$（否则 $$\bar h$$ 作为同态会把 $$0$$ 送到 $$0$$）。** 这正是上面两次计算里"造一个具体 $$h$$ 来验证 $$u\ne0$$"的理论依据。

### 3.3 模不一定有基：先在有限集合里数一遍

**$$\mathbb{Z}/4\mathbb{Z}$$ 没有基（完整论证，不是猜测）。** 若 $$\mathbb{Z}/4\mathbb{Z}$$ 是自由 $$\mathbb{Z}$$-模，它就同构于某个 $$\mathbb{Z}^{\oplus I}$$。$$I=\varnothing$$ 给出零模，$$1$$ 个元素，跟 $$\mathbb{Z}/4\mathbb{Z}$$ 的 $$4$$ 个元素对不上；$$I\ne\varnothing$$ 时 $$\mathbb{Z}^{\oplus I}$$ 至少含一整份 $$\mathbb{Z}$$，是无限集合，同样对不上。**两种可能都被"数元素个数"这一件事直接排除**——这是第64章例 3.9(a) 的论证方式，这里先用一个具体的小数字走一遍。

**命题 3.5（$$\mathbb{Q}$$ 没有基：具体见证）** 取 $$\mathbb{Q}$$ 里三个具体的数 $$\frac12,\frac13,\frac15$$。它们两两 $$\mathbb{Z}$$-线性相关：

$$2\cdot\frac12+(-3)\cdot\frac13=1-1=0,\qquad 2\cdot\frac12+(-5)\cdot\frac15=1-1=0,\qquad 3\cdot\frac13+(-5)\cdot\frac15=1-1=0 .$$

（每组系数都不全为零。）**这提示——第64章例 3.9(b) 会把它证成一般结论——$$\mathbb{Q}$$ 中任何两个元素都是这样相关的，所以基至多有 $$1$$ 个元素。** 但单个元素也不够：假设基是 $$\big\{\frac16\big\}$$，问元素 $$\frac{1}{12}$$ 能不能写成 $$k\cdot\frac16$$（$$k\in\mathbb{Z}$$）——解出 $$k=\frac12$$，不是整数，所以 $$\frac{1}{12}$$ 逃出了 $$\big\{\frac16\big\}$$ 能生成的范围。**同样的失败对任何单个候选基元素都会发生（取该元素的一半作为逃逸点），所以 $$\mathbb{Q}$$ 没有基。**

**这正是入口题背后的现象在预告：$$\mathbb{Z}/4\mathbb{Z}$$ 因为"太小"（有限）而没有基，$$\mathbb{Q}$$ 因为"太能除"（处处可除）而没有基——两种相反的病因，同一个后果。第64章例 3.9 会把这两种病因外加第三种（$$k[x]/(x^2)$$，被一个非零标量杀掉的生成元）配齐成完整的三档反例。**

### 3.4 正合列热身：亲手看一次两头各断一边

**具体的短正合列。** 取

$$0\to\mathbb{Z}\xrightarrow{\ \times3\ }\mathbb{Z}\xrightarrow{\ \pi\ }\mathbb{Z}/3\mathbb{Z}\to0 .$$

逐项验证正合：$$\times3$$ 单射（$$3m=0\Rightarrow m=0$$，整数无零因子）；$$\pi$$ 满射（商映射本身）；$$\operatorname{im}(\times3)=3\mathbb{Z}=\ker\pi$$（$$\pi(m)=0\iff m\equiv0\pmod3\iff m\in3\mathbb{Z}$$）。三处都对上，序列正合。

**张量上 $$\mathbb{Z}/3\mathbb{Z}$$，看右边还在不在。** 把上面序列接上 $$-\otimes_{\mathbb{Z}}\mathbb{Z}/3\mathbb{Z}$$（用 $$\mathbb{Z}\otimes M\cong M$$ 把左边两项换成 $$\mathbb{Z}/3\mathbb{Z}$$ 自己）：

$$\mathbb{Z}/3\mathbb{Z}\xrightarrow{\ (\times3)\otimes1\ }\mathbb{Z}/3\mathbb{Z}\to\mathbb{Z}/3\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/3\mathbb{Z}\to0 .$$

$$(\times3)\otimes1$$ 把 $$1\otimes\bar1$$（对应 $$\mathbb{Z}/3\mathbb{Z}$$ 里的 $$\bar1$$）送到 $$3\otimes\bar1=1\otimes(3\bar1)=1\otimes\bar0=0$$——**原本在 $$\mathbb{Z}$$ 上单的 $$\times3$$，张量完变成了零映射，不再单。左边的正合性直接被撕掉了一半。** 剩下的右边依旧正合（这是右正合性，第64章定理 3.15 会证明它对任何模都成立，不只是这个例子）：像是零映射的像 $$\{0\}$$，商群就是整个 $$\mathbb{Z}/3\mathbb{Z}$$ 自己，所以

$$\mathbb{Z}/3\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/3\mathbb{Z}\cong\mathbb{Z}/3\mathbb{Z}\big/\{0\}\cong\mathbb{Z}/3\mathbb{Z} .$$

**接上 $$\operatorname{Hom}_{\mathbb{Z}}(-,\mathbb{Z})$$，看左边还在不在。** 同一条短正合列，这次接反变函子：

$$\operatorname{Hom}(\mathbb{Z}/3\mathbb{Z},\mathbb{Z})\to\operatorname{Hom}(\mathbb{Z},\mathbb{Z})\xrightarrow{\ \operatorname{Hom}(\times3,\mathbb{Z})\ }\operatorname{Hom}(\mathbb{Z},\mathbb{Z})\to0\ ?$$

用 $$\operatorname{Hom}(\mathbb{Z},\mathbb{Z})\cong\mathbb{Z}$$（同态由 $$1$$ 的像决定），最后一个映射 $$\psi\mapsto\psi\circ(\times3)$$ 在这个同构下就是"乘以 $$3$$"：$$\psi(3)=3\psi(1)$$。它的像是 $$3\mathbb{Z}\subsetneq\mathbb{Z}$$，**不满**——右边的正合性在这里断了。顺带算左端：若 $$\varphi\in\operatorname{Hom}(\mathbb{Z}/3\mathbb{Z},\mathbb{Z})$$，由 $$3\bar1=\bar0$$ 得 $$3\varphi(\bar1)=\varphi(\bar0)=0$$；$$\mathbb{Z}$$ 里没有非零元乘 $$3$$ 等于 $$0$$，故 $$\varphi(\bar1)=0$$，即 $$\operatorname{Hom}(\mathbb{Z}/3\mathbb{Z},\mathbb{Z})=0$$。

**命题 3.6（一次看两头）** 对上述短正合列：$$-\otimes_{\mathbb{Z}}\mathbb{Z}/3\mathbb{Z}$$ 保住了右边的正合性、却把左边的单射压成了零映射；$$\operatorname{Hom}_{\mathbb{Z}}(-,\mathbb{Z})$$ 保住了左边的正合性、却把右边的满射压成了不满的乘 $$3$$ 映射。**两个函子各断一半，且断的是相反的两半——这正是第64章定理 3.15、定理 3.19、定理 3.20 要证的一般事实，本章先让你在一个具体例子里把两种"断法"都亲眼看一遍。**

## 四、几何与物理直觉 (Intuition)

**（一）向量空间像"连续可调"的旋钮，模像"只能整格拨动"的棘轮。** $$\mathbb{R}$$-向量空间里任何非零标量都能"反着用"（乘 $$\frac12$$ 等于退回一半）；$$\mathbb{Z}$$-模只能整数倍地加、整数倍地减——3.1 里 $$2x=\bar1$$ 无解，就是"棘轮拨不出半格"的代数写法。

**（二）张量积像拼合两种不兼容的度量单位。** 把"以 $$2$$ 为单位的尺子"（$$\mathbb{Z}/2\mathbb{Z}$$）与"以 $$2$$ 为单位的另一把尺子"拼在一起，会留下一份"$$2$$ 单位"的读数（3.2 的 (a)：$$\mathbb{Z}/2\otimes\mathbb{Z}/2\cong\mathbb{Z}/2$$，不是想象中的 $$4$$）；但把"以 $$2$$ 为单位"和"以 $$3$$ 为单位"的尺子拼在一起，两种刻度互相"套不上"，读数直接归零（(b)：$$\mathbb{Z}/2\otimes\mathbb{Z}/3=0$$）。**张量积不是"相乘"，是"合并两套刻度系统后，只留下两边都认可的那部分信息"。**

**（三）正合列像一条验货流水线。** 每一站的"合格品"（像）必须恰好等于下一站的"允许进货清单"（核）。3.4 里把 $$\times3$$ 张量上 $$\mathbb{Z}/3\mathbb{Z}$$ 后，第一站的"合格品检测器"（单射性）直接失灵——货物在还没到下一站之前就已经被判定成"跟没进货一样"（零映射）；这就是"张量积会制造出本不该有的坍缩"的直观图像。而 $$\operatorname{Hom}(-,\mathbb{Z})$$ 那边，流水线在最后一站"卡住"（不满）——不是坍缩，是"总有些订单永远交不出货"。

**（四）为什么模论要专门造两个函子来分别救这两条腿。** 一个函子救不了两条腿，这不是巧合而是结构性的——它正是第64章定理 3.21"张量–Hom 伴随"要正式讲的现象：两个函子站在同一枚硬币的两面，各自只保得住半条命，合在一起才是完整的信息。本章的具体计算，就是那枚硬币的两面第一次被你摸到。

## 五、经典问题精讲 (Classical Problems)

### 问题 1：$$\mathbb{Z}/4\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/6\mathbb{Z}$$

**考点**：3.2 的生成元-关系手算法，加上"见证映射"排除塌陷。

**解。** 张量积由 $$u:=\bar1\otimes\bar1$$ 生成。$$u$$ 被 $$4$$ 与 $$6$$ 同时零化：$$4u=(4\bar1)\otimes\bar1=\bar0\otimes\bar1=0$$（$$\mathbb{Z}/4\mathbb{Z}$$ 里 $$4\bar1=\bar0$$），$$6u=\bar1\otimes(6\bar1)=\bar1\otimes\bar0=0$$（$$\mathbb{Z}/6\mathbb{Z}$$ 里 $$6\bar1=\bar0$$）。$$\gcd(4,6)=2$$，Bézout 等式 $$2=6\cdot1+4\cdot(-1)$$（验证：$$6-4=2$$）给出

$$2u=1\cdot(6u)+(-1)\cdot(4u)=0 .$$

所以 $$u$$ 的阶整除 $$2$$。**排除 $$u=0$$**：取双线性映射 $$h:\mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/6\mathbb{Z}\to\mathbb{Z}/2\mathbb{Z}$$，$$h(a,b):=\rho_1(a)\rho_2(b)$$，其中 $$\rho_1:\mathbb{Z}/4\mathbb{Z}\to\mathbb{Z}/2\mathbb{Z}$$、$$\rho_2:\mathbb{Z}/6\mathbb{Z}\to\mathbb{Z}/2\mathbb{Z}$$ 是模 $$2$$ 约化（都是良定义的群同态，因为 $$2\mid4$$、$$2\mid6$$）。$$h$$ 双线性是因为 $$\rho_1,\rho_2$$ 都是加法同态。$$h(\bar1,\bar1)=\rho_1(\bar1)\rho_2(\bar1)=1\cdot1=1\ne0$$。故 $$u\ne0$$，阶恰为 $$2$$：

$$\mathbb{Z}/4\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/6\mathbb{Z}\ \cong\ \mathbb{Z}/2\mathbb{Z} .$$

$$\blacksquare$$

### 问题 2：$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/3\mathbb{Z},\mathbb{Z}/9\mathbb{Z})$$（回收入口题 (d) 的方法）

**考点**：枚举法——同态由 $$\bar1$$ 的像唯一决定。

**解。** 设 $$\varphi:\mathbb{Z}/3\mathbb{Z}\to\mathbb{Z}/9\mathbb{Z}$$ 是模同态，$$t:=\varphi(\bar1)\in\mathbb{Z}/9\mathbb{Z}$$。约束来自 $$3\cdot\bar1=\bar0$$：必须 $$3t=\bar0$$（在 $$\mathbb{Z}/9\mathbb{Z}$$ 里）。逐个代入 $$t=0,1,\dots,8$$ 算 $$3t\bmod9$$：

$$0,\ 3,\ 6,\ 0,\ 3,\ 6,\ 0,\ 3,\ 6 .$$

只有 $$t\in\{0,3,6\}$$ 满足 $$3t\equiv0\pmod9$$，共 **3 个**合法的 $$t$$，每个都给出唯一的同态（反过来验证：$$\varphi(\bar k):=kt$$ 对这三个 $$t$$ 都良定义，因为 $$k$$ 换成 $$k+3$$ 时 $$(k+3)t=kt+3t=kt$$）。所以

$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/3\mathbb{Z},\mathbb{Z}/9\mathbb{Z})\ \cong\ \mathbb{Z}/3\mathbb{Z}\qquad(\text{3 个元素，}\gcd(3,9)=3)。$$

$$\blacksquare$$

**这道题与问题 1 合起来说明同一件事的两面**：张量积把"公共的可整除部分"（$$\gcd$$）留下来当结果，$$\operatorname{Hom}$$ 把"公共可整除部分"数出来当元素个数——两条路都通向同一个数 $$\gcd(m,n)$$，第64章基础练习 2 会把这条公式一般地证出来。

### 问题 3：特征值热身——$$2\times2$$ 矩阵上的具体计算

**考点**：为第64章例 3.1(ii)、问题 4 的"$$k[x]$$-模 = 向量空间配一个线性算子"做铺垫；这里不涉及模语言，只把要用到的具体代数先算一遍。

**解。** 取 $$T=\begin{pmatrix}2&0\\0&5\end{pmatrix}$$，作用在 $$V=\mathbb{R}^2$$ 上。对标量 $$\lambda$$，考察 $$(\lambda I-T)v=0$$ 何时有非零解：

$$\lambda I-T=\begin{pmatrix}\lambda-2&0\\0&\lambda-5\end{pmatrix} .$$

这是对角矩阵，有非零核当且仅当至少一个对角元为 $$0$$，即 $$\lambda=2$$ 或 $$\lambda=5$$。**代入 $$\lambda=2$$ 具体验证**：矩阵变成 $$\begin{pmatrix}0&0\\0&-3\end{pmatrix}$$，方程组是 $$0\cdot x=0$$、$$-3y=0$$，解集 $$\{(x,0):x\in\mathbb{R}\}$$ 非零。**代入 $$\lambda=3$$ 作对照**（$$3$$ 不是特征值）：矩阵变成 $$\begin{pmatrix}1&0\\0&-2\end{pmatrix}$$，方程组只有 $$x=0,y=0$$ 一个解。所以 $$T$$ 的特征值恰是 $$\{2,5\}$$，与直接读对角元一致。

**记一下这个具体计算里出现的模式**：$$(\lambda I-T)v=0$$ 有非零解，等价于"用多项式 $$x-\lambda$$ 作用在 $$v$$ 上能得到 $$0$$"——如果把"$$x$$ 作用在 $$v$$ 上"理解成 $$Tv$$（第64章例 3.1(ii) 会把这个理解正式定义成 $$k[x]$$-模结构），"求特征值"这件事就变成了"找一个形如 $$x-\lambda$$ 的多项式，能把某个非零向量杀死"。**这句话现在只是一个观察，第64章问题 4 会把它写成严格的模论命题并证明。**

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 仿照 3.1 的做法，取 $$\mathbb{Z}/8\mathbb{Z}$$，验证 $$(2+5)\cdot\bar1=2\cdot\bar1+5\cdot\bar1$$ 与 $$(2\cdot5)\cdot\bar1=2\cdot(5\cdot\bar1)$$ 两条模公理，把两边都算成具体的 $$\bar k$$。

**基2.** 计算 $$\mathbb{Z}/3\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/5\mathbb{Z}$$（提示：$$\gcd(3,5)=1$$，模仿 3.2 (b) 的 Bézout 手法）。

**基3.** 用枚举法计算 $$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/4\mathbb{Z},\mathbb{Z}/4\mathbb{Z})$$（把 $$t=0,1,2,3$$ 逐个代入约束 $$4t\equiv0\pmod4$$）。

**基4.** 判断 $$0\to\mathbb{Z}\xrightarrow{\times5}\mathbb{Z}\xrightarrow{\pi}\mathbb{Z}/5\mathbb{Z}\to0$$ 是否正合，逐处（单射、满射、像=核）验证。

### 竞赛（本课目标难度）

**竞1.** 证明 $$\frac12,\frac13,\frac15$$ 两两 $$\mathbb{Z}$$-线性相关（给出每一对的具体整数见证，仿 3.3），再取具体候选基 $$\big\{\frac{1}{10}\big\}$$，说明为什么它生成不了 $$\frac{1}{20}$$，从而说明单元素基也不行。

**竞2.** 用 3.2 的生成元-关系手法（不用套公式）计算 $$\mathbb{Z}/4\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/6\mathbb{Z}$$——先找 $$\gcd$$ 与 Bézout 系数，再造一个见证双线性映射排除塌陷。

**竞3.** 把 $$0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\xrightarrow{\pi}\mathbb{Z}/2\mathbb{Z}\to0$$ 接上 $$\operatorname{Hom}_{\mathbb{Z}}(-,\mathbb{Z}/4\mathbb{Z})$$，逐项算出三个 $$\operatorname{Hom}$$ 群（用枚举法），并指出序列在哪一处失去了正合性。

### 研究（通向下一章）

**研1.** 计算 $$\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/6\mathbb{Z}$$：证明它由 $$v:=1\otimes\bar1$$ 生成，$$6v=0$$；再用见证映射（提示：用模 $$\mathbb{Z}/6\mathbb{Z}$$ 自身的标量作用当 $$h$$）证明 $$v$$ 的阶恰好是 $$6$$，从而 $$\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/6\mathbb{Z}\cong\mathbb{Z}/6\mathbb{Z}$$。

**研2.** 设 $$P:=\mathbb{Z}/2\mathbb{Z}\oplus\mathbb{Z}/3\mathbb{Z}$$（看成 $$\mathbb{Z}$$-模）。(a) 证明 $$P$$ 不是自由 $$\mathbb{Z}$$-模（提示：数元素个数，仿 3.3）。(b) 利用 $$\mathbb{Z}/6\mathbb{Z}\cong\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$$（中国剩余定理）给 $$P$$ 配一个 $$\mathbb{Z}/6\mathbb{Z}$$-模结构，证明这样看时 $$P\cong\mathbb{Z}/6\mathbb{Z}$$ 自由（基为单个元素）。

### 解答 (Solutions)

**解 基1.** 左边：$$2+5=7$$，$$7\cdot\bar1=\bar7$$（$$7<8$$，无需再约）。右边：$$2\cdot\bar1=\bar2$$，$$5\cdot\bar1=\bar5$$，$$\bar2+\bar5=\bar7$$。两边都是 $$\bar7$$，相等。第二条：左边 $$2\cdot5=10$$，$$10\cdot\bar1=\overline{10}=\bar2$$（$$10-8=2$$）。右边：$$5\cdot\bar1=\bar5$$，$$2\cdot\bar5=\overline{10}=\bar2$$。两边都是 $$\bar2$$，相等。$$\blacksquare$$

**解 基2.** 记 $$u:=\bar1\otimes\bar1$$。$$3u=(3\bar1)\otimes\bar1=\bar0\otimes\bar1=0$$（$$\mathbb{Z}/3\mathbb{Z}$$ 里 $$3\bar1=\bar0$$），$$5u=\bar1\otimes(5\bar1)=\bar1\otimes\bar0=0$$（$$\mathbb{Z}/5\mathbb{Z}$$ 里 $$5\bar1=\bar0$$）。$$\gcd(3,5)=1$$，Bézout：$$1=3\cdot2+5\cdot(-1)$$（验证 $$6-5=1$$）。故

$$u=2\cdot(3u)+(-1)\cdot(5u)=2\cdot0+(-1)\cdot0=0 .$$

$$u$$ 生成整个张量积，$$u=0$$ 故 $$\mathbb{Z}/3\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/5\mathbb{Z}=0$$。$$\blacksquare$$

**解 基3.** 设 $$t=\varphi(\bar1)\in\mathbb{Z}/4\mathbb{Z}$$，约束 $$4t\equiv0\pmod4$$。逐个代入 $$t=0,1,2,3$$：$$4\cdot0=0,\ 4\cdot1=4\equiv0,\ 4\cdot2=8\equiv0,\ 4\cdot3=12\equiv0$$——**全部满足**（因为 $$4t$$ 恒被 $$4$$ 整除）。所以 $$4$$ 个 $$t$$ 全部合法，$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/4\mathbb{Z},\mathbb{Z}/4\mathbb{Z})\cong\mathbb{Z}/4\mathbb{Z}$$（4 个元素）。$$\blacksquare$$

**解 基4.** **单射**：$$5m=0$$ 在 $$\mathbb{Z}$$ 中只有 $$m=0$$（整数无零因子），故 $$\times5$$ 单。**满射**：$$\pi$$ 是商映射，按定义满。**像 = 核**：$$\operatorname{im}(\times5)=5\mathbb{Z}$$；$$\ker\pi=\{m:\pi(m)=0\}=\{m:5\mid m\}=5\mathbb{Z}$$。三处吻合，序列正合。$$\blacksquare$$

**解 竞1.** 见证：$$2\cdot\frac12+(-3)\cdot\frac13=1-1=0$$；$$2\cdot\frac12+(-5)\cdot\frac15=1-1=0$$；$$3\cdot\frac13+(-5)\cdot\frac15=1-1=0$$。三组系数均不全为零，故三对两两相关。再看候选基 $$\big\{\frac{1}{10}\big\}$$：若 $$\frac{1}{20}=k\cdot\frac{1}{10}$$（$$k\in\mathbb{Z}$$），解得 $$k=\frac12$$，不是整数，故 $$\frac{1}{20}$$ 无法由 $$\frac{1}{10}$$ 的整数倍表出，单元素基失败。**（第64章例 3.9(b) 会把"任何两个元素相关"与"没有单元素基"两句话对任意分母一般地证出来，这里只是用具体分母走了一遍。）** $$\blacksquare$$

**解 竞2.** 记 $$u:=\bar1\otimes\bar1$$。$$4u=0$$（$$4\bar1=\bar0$$ 在 $$\mathbb{Z}/4\mathbb{Z}$$），$$6u=0$$（$$6\bar1=\bar0$$ 在 $$\mathbb{Z}/6\mathbb{Z}$$）。$$\gcd(4,6)=2$$，Bézout：$$2=6-4$$，故 $$2u=6u-4u=0$$，$$u$$ 的阶整除 $$2$$。见证映射：$$h(a,b):=\rho_1(a)\rho_2(b)$$（模 $$2$$ 约化后相乘），$$h(\bar1,\bar1)=1\ne0$$，故 $$u\ne0$$，阶恰为 $$2$$。

$$\mathbb{Z}/4\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/6\mathbb{Z}\cong\mathbb{Z}/2\mathbb{Z} .$$

（与第五节问题 1 完全一致——同一个数用同一套方法再算一遍。）$$\blacksquare$$

**解 竞3.** $$\operatorname{Hom}(\mathbb{Z},\mathbb{Z}/4\mathbb{Z})\cong\mathbb{Z}/4\mathbb{Z}$$（同态由 $$\varphi(1)$$ 自由决定，$$\mathbb{Z}$$ 无约束）。$$\operatorname{Hom}(\mathbb{Z}/2\mathbb{Z},\mathbb{Z}/4\mathbb{Z})$$：设 $$t=\varphi(\bar1)$$，约束 $$2t\equiv0\pmod4$$，逐个代入 $$t=0,1,2,3$$：$$0,2,0,2$$——合法的是 $$t\in\{0,2\}$$，共 2 个，故 $$\cong\mathbb{Z}/2\mathbb{Z}$$。

末端映射 $$\operatorname{Hom}(\times2,\mathbb{Z}/4\mathbb{Z}):\operatorname{Hom}(\mathbb{Z},\mathbb{Z}/4\mathbb{Z})\to\operatorname{Hom}(\mathbb{Z},\mathbb{Z}/4\mathbb{Z})$$ 是 $$\psi\mapsto\psi\circ(\times2)$$，在 $$\operatorname{Hom}(\mathbb{Z},\mathbb{Z}/4\mathbb{Z})\cong\mathbb{Z}/4\mathbb{Z}$$（$$\psi\leftrightarrow\psi(1)$$）下对应 $$t\mapsto2t\bmod4$$：$$0\mapsto0,1\mapsto2,2\mapsto0,3\mapsto2$$，像为 $$\{0,2\}$$，**不满**（漏掉 $$1,3$$）。

**结论**：序列在前两处正合（第64章定理 3.19 保证的一般事实），但末尾断在"满"这一步——与 3.4 里的 $$\mathbb{Z}$$ 例子是同一种断法，只是把 $$N$$ 从 $$\mathbb{Z}$$ 换成了 $$\mathbb{Z}/4\mathbb{Z}$$。$$\blacksquare$$

**解 研1.** $$\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/6\mathbb{Z}$$ 由 $$v:=1\otimes\bar1$$ 生成（任何 $$a\otimes\bar k=ak\cdot v$$）。$$6v=1\otimes(6\bar1)=1\otimes\bar0=0$$，故 $$v$$ 的阶整除 $$6$$。取见证映射 $$h:\mathbb{Z}\times\mathbb{Z}/6\mathbb{Z}\to\mathbb{Z}/6\mathbb{Z}$$，$$h(a,m):=am$$（就是模的标量作用本身，显然双线性）。$$h(1,\bar1)=\bar1$$，而 $$\bar1$$ 在 $$\mathbb{Z}/6\mathbb{Z}$$ 里的阶恰好是 $$6$$。同态把元素的阶只能变小（阶整除原阶），所以由 $$\bar h(v)=h(1,\bar1)=\bar1$$ 阶为 $$6$$，可推出 $$v$$ 的阶是 $$6$$ 的倍数；配合"阶整除 $$6$$"，$$v$$ 的阶恰好是 $$6$$。故

$$\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/6\mathbb{Z}\ \cong\ \mathbb{Z}/6\mathbb{Z}\qquad(v\leftrightarrow\bar1)。$$

$$\blacksquare$$

**解 研2.** (a) $$P=\mathbb{Z}/2\mathbb{Z}\oplus\mathbb{Z}/3\mathbb{Z}$$ 有 $$2\times3=6$$ 个元素，非零且有限。若它作为 $$\mathbb{Z}$$-模自由，就该同构于某个 $$\mathbb{Z}^{\oplus I}$$：$$I=\varnothing$$ 给零模（$$1$$ 个元素），$$I\ne\varnothing$$ 给无限集合——都对不上 $$6$$ 个元素，矛盾。故 $$P$$ 不是自由 $$\mathbb{Z}$$-模。

(b) 中国剩余定理给出环同构 $$\mathbb{Z}/6\mathbb{Z}\xrightarrow{\ \sim\ }\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/3\mathbb{Z}$$，$$k\bmod6\mapsto(k\bmod2,\ k\bmod3)$$。用它把 $$P$$ 的每个元素 $$(a,b)$$ 对应到唯一的 $$k\in\mathbb{Z}/6\mathbb{Z}$$，并用这个对应把 $$\mathbb{Z}/6\mathbb{Z}$$ 的标量乘法搬到 $$P$$ 上，得到 $$P\cong\mathbb{Z}/6\mathbb{Z}$$（作为 $$\mathbb{Z}/6\mathbb{Z}$$-模）。$$\mathbb{Z}/6\mathbb{Z}$$ 作为自身的模显然自由，基为单个元素 $$\{1\}$$（任何元素 $$k$$ 唯一写成 $$k\cdot1$$）。**所以同一个 Abel 群 $$P$$，当 $$\mathbb{Z}$$-模看不自由，换个基环 $$\mathbb{Z}/6\mathbb{Z}$$ 看却自由——这正是第64章例 3.23"投射未必自由"那组反例的原型，第64章会在这个现象上再往前走一步。** $$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**（一）模只是把标量环从域换成环，能不能"除以标量"决定了一大堆结论是否还成立。** 你已经在 $$\mathbb{Z}/4\mathbb{Z}$$ 里亲手撞见过这堵墙：$$2x=\bar1$$ 无解，不是加法坏了，是 $$2$$ 在 $$\mathbb{Z}/4\mathbb{Z}$$ 里没有逆。

**（二）记号 $$m\otimes n$$ 背后是"自由模模掉双线性关系"，你已经用手把它跑通了三次。** $$\mathbb{Z}/2\otimes\mathbb{Z}/2\cong\mathbb{Z}/2$$、$$\mathbb{Z}/2\otimes\mathbb{Z}/3=0$$、$$\mathbb{Z}/4\otimes\mathbb{Z}/6\cong\mathbb{Z}/2$$——每一次都靠"Bézout 消元 + 见证双线性映射排除塌陷"这两步棋，而这两步棋正是第64章定理 3.12、3.15 证明里真正在做的事。

**（三）模不一定有基，你已经见过两种相反的病因。** $$\mathbb{Z}/4\mathbb{Z}$$ 因为"太小"（有限而非零）没有基；$$\mathbb{Q}$$ 因为"太能除"（处处可除）没有基。第64章例 3.9 会补上第三种病因（生成元被标量杀死），把三档反例配齐。

**（四）正合列只在中间"传递"，两端要单独看，且两个函子各断一半、断的是相反的两半。** 你已经具体验证过 $$(\times3)\otimes1$$ 塌成零映射（张量积不左正合）、$$\operatorname{Hom}(\times3,-)$$ 缺满（Hom 不右正合）——这正是第64章定理 3.15、3.19、3.20 要证的一般事实的具体样本。

**交棒。** 现在你已经能手算 $$\mathbb{Z}/m\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/n\mathbb{Z}$$、$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/m\mathbb{Z},\mathbb{Z}/n\mathbb{Z})$$ 这类具体数值，也亲眼见过左右正合性各自的破口，还提前摸到了"投射不等于自由"的最小样本（研2）。**下一章会把这些具体计算一次性收进张量积与 $$\operatorname{Hom}$$ 的泛性质、两条正合性定理的严格证明里，并进一步引出张量–Hom 伴随与投射模的完整理论——你手算过的每一个数字，都会在那里重新出现，只是这次配上了对任意模都成立的证明。**

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch62_范畴与函子_下.md">← 第62章 范畴与函子·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch64_模_张量积与Hom函子_下.md">第64章 模、张量积与 Hom 函子·下 →</a></div>
</div>
