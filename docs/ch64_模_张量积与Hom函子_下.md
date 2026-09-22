---
layout: default
---

# 第64章: 模、张量积与 Hom 函子·下：完整推导 (Modules, Tensor Products and the Hom Functor · Part II: Full Derivation)

> 配套预备: 见 第63章 模、张量积与 Hom 函子·上（同一主题的具体铺垫，建议先读）

> 专家依据: `_experts/algebra/commutative-algebra.md`（主）+ `_experts/algebra/category-universal-properties.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

读完第 63 章的具体例子后——你已经亲手算过 $$\mathbb{Z}/2\otimes\mathbb{Z}/2$$、$$\mathbb{Z}/4\otimes\mathbb{Z}/6$$、$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/3,\mathbb{Z}/9)$$ 这些具体数值，也亲眼见过张量积与 $$\operatorname{Hom}$$ 各自"断"在哪一半——这里把同样的构造写成一般定义，并给出对任意模都成立的完整证明。

前两卷里，标量一直在**域**上：$$\mathbb{R}$$、$$\mathbb{C}$$，最不济也是第四章的 $$\mathbb{R}^n$$。第 62 章我们把「结构」抽象成范畴、把「结构之间的映射」抽象成函子，但对象本身还是老的。本章把标量从域放宽到**环**，对象就从**向量空间**变成**模 (module)**。

这一步只是把 $$\mathbb{R}$$ 换成 $$\mathbb{Z}$$，代价却很大：线性代数有两根支柱当场折断——「每个空间都有基」与「线性映射都能用矩阵写出来」。折了之后靠两样东西把理论重新撑起来：**张量积** $$-\otimes_A N$$ 与 **Hom 函子** $$\operatorname{Hom}_A(M,-)$$。它们是第 62 章「函子」的第一批有内容的例子，也是第 66 章「伴随函子」的**第一个具体配对**（本章 3.6 会把这句说清楚）。

三个衔接点：其一，第 22 章的域上张量积在这里被**升级**——万有性质原封不动，但「基与维数」那条定理死了（3.4 指出死在哪里）；其二，第 06 章的「对偶 = 反变」会以 $$\operatorname{Hom}_A(-,W)$$ 的身份重新出现，成为「反变函子」的原型；其三，本章两个函子一左一右地各保住正合性的一半，这个现象正是第 66 章「左伴随保余极限、右伴随保极限」的最小样本。

## 二、入口：一道具体的问题 (Entry Problem)

**先做题，不给定义。** 下面四个都是可以在纸张上算完的具体问题（(a)(b)(d) 依相关风格自编，(c) 取自交换代数标准习题）。第 3 节之前你不需要任何新名词，第 5 节我们会把这四个全部回收。

**(a)** 计算 $$\mathbb{Z}/2\mathbb{Z}\ \otimes_{\mathbb{Z}}\ \mathbb{Z}/2\mathbb{Z}$$。你的第一反应大概是二者之一：「两个 2 阶的东西相乘，得 $$\mathbb{Z}/4$$」，或者「乘完只剩 0」。到底是哪一个？为什么？

**(b)** 设 $$n\ge2$$。计算 $$\mathbb{Q}\ \otimes_{\mathbb{Z}}\ \mathbb{Z}/n\mathbb{Z}$$。两个都非零，答案却是 0。一个「什么都没剩下」的结果，是从哪条规则里挤出来的？

**(c)** 「$$\mathbb{Z}/2$$ 只有两个元素，当然可以拿来当 $$\mathbb{Z}$$-模用。」这句话对。那么：它能不能当 $$\mathbb{R}$$-向量空间用？把这两个问题的差别说清楚——差的到底是哪一条公理？

**(d)** 设 $$V,W$$ 是有限维实向量空间。下面的两个数恒相等：

$$\dim(V\otimes_{\mathbb{R}}W)=\dim V\cdot\dim W,\qquad \dim\operatorname{Hom}_{\mathbb{R}}(V,W)=\dim V\cdot\dim W.$$

但它们**不是**同一回事：把满射 $$g:W\to W''$$ 接进第二个变量，$$V\otimes g$$ 仍是满射，而 $$\operatorname{Hom}(V,g)$$ 不再保证满；把单射 $$f:V'\to V$$ 接进第一个变量，$$\operatorname{Hom}(f,W)$$ 仍是单射，而 $$f\otimes W$$ 不再保证单。**同一个数，相反的性**——这是本章的骨架。

> **问题 1、问题 3** 把 (a) 算干净；**问题 3、问题 2** 给出 (b) 的两个算法；**问题 2** 同时回答 (c)，并说明 (b) 与 (c) 是同一件事的两面；**(d)** 的完整答案要等到 3.5、3.6 两节（定理 3.20 与注 3.21）。3.3 里「模不一定有基」这句话，也只有在把 $$\mathbb{Z}/2$$ 拿在手里之后才有分量。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 模：把标量从域放宽到环

**定义 3.1（左模、右模, left/right module）** 设 $$A$$ 是含单位元 $$1$$ 的环。一个 **$$A$$-左模 (left $$A$$-module)** 是三元组 $$(M,+,\cdot)$$，其中 $$(M,+)$$ 是 **Abel 群**，$$\cdot:A\times M\to M$$ 是标量乘法，满足对一切 $$a,b\in A$$、$$m,n\in M$$：

$$a\cdot(m+n)=a\cdot m+a\cdot n,\qquad (a+b)\cdot m=a\cdot m+b\cdot m,$$
$$(ab)\cdot m=a\cdot(b\cdot m),\qquad 1\cdot m=m.$$

**$$A$$-右模 (right $$A$$-module)** 把第三条换成 $$m\cdot(ab)=(m\cdot a)\cdot b$$。若 $$A$$ 交换，任何左模通过 $$m\cdot a:=a\cdot m$$ 成为右模，两者不再区分，统称 **$$A$$-模 (module)**，其元素叫**向量 (vector)**，$$A$$ 的元素叫**标量 (scalar)**。全体 $$A$$-模与模同态（见定义 3.3）构成范畴 $$A\text{-}\mathbf{Mod}$$。

**为什么第一条要求 $$M$$ 交换。** 把标量乘法重新打包成 $$\rho:A\to\operatorname{End}(M)$$，$$\rho(a)(m)=a\cdot m$$。分配律 $$(a+b)\cdot m=a\cdot m+b\cdot m$$ 说的是 $$\rho(a+b)=\rho(a)+\rho(b)$$——**右端的加号是逐点相加**。「逐点和的自同态仍是自同态」只在 $$M$$ 交换时成立：$$M$$ 不交换时 $$\varphi+\psi$$ 一般不保持加法，$$\operatorname{End}(M)$$ 便不是环。**所以「Abel 群」不是约定的简化，而是让「$$A\to\operatorname{End}(M)$$ 是环同态」这句话有意义唯一可能的形式。**

**例 3.1（四个必须记住的例子）**

**(i) $$A=\mathbb{Z}$$：$$\mathbb{Z}$$-模与 Abel 群是同一个东西。** 设 $$M$$ 是 Abel 群。任何 $$\mathbb{Z}$$-模结构都被 $$1$$ 的作用钉死：由 $$1\cdot m=m$$ 与结合律得

$$n\cdot m=\underbrace{m+\cdots+m}_{n\ \text{项}}\quad(n>0),\qquad 0\cdot m=0,\qquad (-n)\cdot m=-(n\cdot m).$$

于是 $$M$$ 上的 $$\mathbb{Z}$$-模结构**至多有一种**；反过来按上式定义 $$n\cdot m$$，分配律与结合律都成立（整数乘法自身的分配律被继承下来），故**恰好有一种**。所以

$${\mathbb{Z}}\text{-}\mathbf{Mod}=\mathbf{Ab}\qquad(\text{作为范畴}).$$

这条恒等式是本章所有反例的源头：**$$\mathbb{Z}$$-模理论里的每个怪现象，都是 Abel 群理论里的一个事实。**

入口题 (c) 也由它回答。$$\mathbb{Z}/2$$ 是 Abel 群，所以它自动是 $$\mathbb{Z}$$-模；它不能是 $$\mathbb{R}$$-向量空间，理由如下。设它已是 $$\mathbb{R}$$-向量空间，取 $$m=\bar1$$。公理 $$(ab)\cdot m=a\cdot(b\cdot m)$$（取 $$a=2$$、$$b=\frac12$$）给

$$2\cdot\Big(\frac{1}{2}\cdot m\Big)=\Big(2\cdot\frac{1}{2}\Big)\cdot m=1\cdot m=m=\bar 1 .$$

另一方向，公理 $$(a+b)\cdot m=a\cdot m+b\cdot m$$（取 $$a=b=1$$）给 $$2\cdot x=(1+1)\cdot x=1\cdot x+1\cdot x=x+x$$，故左端 $$=m+m=\bar1+\bar1=\bar0$$。于是 $$\bar1=\bar0$$，矛盾。**它折在「标量环的每个非零元可逆」这一条上，而不是折在「有没有基」上**——凡是能当 $$\mathbb{Z}$$-模的东西，都自动是某种「带加法」的结构；$$\mathbb{R}$$-向量空间多要的那一条，是除法。

**(ii) $$A=k[x]$$：$$k[x]$$-模就是「一个 $$k$$-向量空间配一个线性算子」。** 设 $$V$$ 是 $$k$$-向量空间，$$T:V\to V$$ 是线性算子。对 $$p(x)=\sum_ic_ix^i$$ 规定 $$p(x)\cdot v:=\sum_i c_i\,T^i v$$ 并线性延拓。结合律成立因为 $$T^iT^j=T^{i+j}$$，单位律因为 $$T^0=\mathrm{id}$$，两条分配律分别来自 $$T^i$$ 的线性与求和的分配。反过来，若 $$V$$ 是 $$k[x]$$-模，则 $$v\mapsto x\cdot v$$ 是 $$k$$-线性的（标量乘法对第二变元线性），记作 $$T$$；再由结合律，$$p(x)\cdot v=p(T)v$$ 被 $$T$$ 完全确定。两个方向互为逆，故

$$\{\text{有限维 }k[x]\text{-模的结构}\}\ \longleftrightarrow\ \{\text{有限维 }k\text{-向量空间}\}+\{\text{一个线性算子}\}.$$

**这个例子是本章通向其余各卷的桥**：第 16–19 章讲的「可观测量与本征态」「算子的谱」「谱定理」，本质上都是 $$k[x]$$-模（或 $$\mathbb{C}[x]$$-模）的结构定理。第 32 章写下的**预解式**

$$(\lambda I-A)\psi=0$$

在模语言里读作：$$\psi$$ 是 $$\mathbb{C}[x]$$-模 $$\mathcal{H}$$ 中被 $$(x-\lambda)$$ 零化的元素。**$$\lambda I-A$$ 不可逆，等价于 $$\lambda$$ 是 $$A$$ 的特征值，等价于 $$x-\lambda$$ 在 $$k[x]$$ 中的那个元素「杀掉了」某个非零 $$\psi$$。** 三种说法的互译，就是第 32 章与本章之间的接口。

**(iii) $$A$$ 自身。** 左乘 $$(a,m)\mapsto am$$ 使 $$A$$ 成为 $$A$$-左模。它的**子模恰好是 $$A$$ 的左理想**，它到自身的**模同态恰好是右乘**（$$\varphi(m)=mc$$ 对某个固定 $$c$$）。这两句话是「理想 = 模」「理想论 = 模论的特例」的精确形式，也是交换代数把理想问题翻译成模问题的入口。

**(iv) 商环 $$A/\mathfrak{a}$$。** 若 $$\mathfrak{a}$$ 是理想，则 $$a\cdot(m+\mathfrak{a}):=am+\mathfrak{a}$$ 良定义（$$m-m'\in\mathfrak{a}$$ 时 $$a(m-m')\in\mathfrak{a}$$），它使 $$A/\mathfrak{a}$$ 成为 $$A$$-模。

**注 3.1（模与向量空间的分水岭）** 域 $$k$$ 上的模就叫 $$k$$-向量空间，所以模论**涵盖**了线性代数。差别只有一处：$$A$$ 中非零元不一定可逆。线性代数证明里凡是「两边同时除以 $$a$$」的地方，到模上都要重审。本章逐条检查两个受影响的结论：3.3 检查「每个模都有基」，3.4 检查「张量积保单射」。**答案都是「不」——而正是这两声「不」，造出了同调代数。**

### 3.2 子模、商模与正合序列

线性代数里"子空间"这个概念要搬到模上，需要先确认它值得搬：子空间之所以有用，是因为核与像都是子空间，而核与像正是判断一个线性映射"好不好"的第一手信息。模同态的核与像同样值得研究，这就是为什么第一件事是把"子空间"翻译成"子模"。

**定义 3.2（子模, submodule）** $$A$$-模 $$M$$ 的子集 $$N$$ 称为**子模**，若它对加法封闭（是子群）且对 $$A$$ 的标量乘法封闭。

模的**核 (kernel)** $$\ker f=\{m\in M:f(m)=0\}$$ 与**像 (image)** $$\operatorname{im}f=\{f(m)\}$$ 都是子模——**前者的证明要用到 $$f$$ 线性**：$$f(am+bn)=af(m)+bf(n)=0$$。

**例 3.2** 四个子模的翻译：
(i) $$\mathbb{Z}$$-模的子模 = Abel 群的子群；
(ii) $$A$$ 作为自身的子模 = $$A$$ 的左理想；
(iii) $$k[x]$$-模的子模 = $$T$$-**不变子空间 (invariant subspace)**。因为 $$N$$ 对 $$\mathbb{Z}$$ 的标量作用封闭就是加群封闭，对 $$x$$ 的作用封闭就是 $$T(N)\subseteq N$$，其余多项式由 $$T$$ 生成。**「不变子空间」这个线性代数名词，在模语言里就是「子模」；这两个词从此可以互换。**
(iv) $$\mathbb{Q}$$ 作为 $$\mathbb{Z}$$-模的子模 = $$\mathbb{Q}$$ 的加法子群。

**定义 3.3（模同态与商模, module homomorphism / quotient module）** 映射 $$f:M\to N$$ 是 **$$A$$-模同态**，若

$$f(m_1+m_2)=f(m_1)+f(m_2),\qquad f(am)=a\,f(m)$$

对一切 $$m_1,m_2,m\in M$$、$$a\in A$$。若 $$N\subseteq M$$ 是子模，商群 $$M/N$$ 上规定

$$a\cdot(m+N):=am+N.$$

**这是一条需要验证的定义**：取另一个代表元 $$m'=m+n$$（$$n\in N$$），则 $$am'=am+an$$，而 $$an\in N$$（子模对标量封闭），故 $$am'+N=am+N$$，运算符良定义。四条公理逐条从 $$M$$ 继承（加法与标量的运算都只是把 $$M$$ 中的等式搬到陪集上）。商映射 $$\pi:M\to M/N$$，$$\pi(m)=m+N$$，是满同态，且 $$\ker\pi=N$$。

**定理 3.4（第一同构定理）** 设 $$f:M\to N$$ 是模同态，则 $$\bar f:M/\ker f\to\operatorname{im}f$$，$$\bar f(m+\ker f)=f(m)$$，是良定义的模同构。

*证明思路*：分四步——良定义、加法与标量、单、满。
*证明*。**良定义**：设 $$m-m'\in\ker f$$，即 $$f(m-m')=0$$；由 $$f$$ 线性 $$f(m)=f(m')$$，故 $$\bar f(m+\ker f)$$ 不依赖代表元。**同态**：$$\bar f\big((m_1+\ker f)+(m_2+\ker f)\big)=\bar f\big((m_1+m_2)+\ker f\big)=f(m_1+m_2)=f(m_1)+f(m_2)$$；标量同理。**单**：若 $$\bar f(m+\ker f)=0$$，则 $$f(m)=0$$，即 $$m\in\ker f$$，故 $$m+\ker f=\ker f$$ 是零元。**满**：$$\operatorname{im}\bar f=\operatorname{im}f$$ 按定义。$$\blacksquare$$

第一同构定理把"核"与"像"焊在了一起：$$M/\ker f\cong\operatorname{im}f$$。如果把一整条同态链首尾相接地摆出来，"上一步的像恰好是下一步的核"这句话就能反复用在链上的每一处——这既是把多个同构定理压成一句话的写法，也是本章接下来判断"张量积/$$\operatorname{Hom}$$ 到底还剩多少正合性"的公共语言，所以要先把它正式定义出来。

**定义 3.5（正合序列, exact sequence）** 模同态序列

$$\cdots\to M_{i-1}\xrightarrow{f_i}M_i\xrightarrow{f_{i+1}}M_{i+1}\to\cdots$$

称为**正合 (exact)**，若在每一处 $$\operatorname{im}f_i=\ker f_{i+1}$$。形如

$$0\to M'\xrightarrow{u}M\xrightarrow{v}M''\to 0$$

的正合序列叫**短正合序列 (short exact sequence)**。

**命题 3.5（短正合列的三种读法）** 记号同上，则：(1) 在 $$M'$$ 处正合（$$0\to M'\xrightarrow{u}M$$ 正合）$$\iff$$ $$u$$ 单射；(2) 在 $$M''$$ 处正合（$$M\xrightarrow{v}M''\to0$$ 正合）$$\iff$$ $$v$$ 满射；(3) 整个序列正合 $$\iff$$ $$u$$ 单、$$v$$ 满、且 $$M''\cong M/u(M')$$。

*证明*。(1) 左边正合的意思是 $$\operatorname{im}(0\to M')=\{0\}=\ker u$$（零映射的像是 $$\{0\}$$），即 $$\ker u=0$$，这正是单射的定义。(2) 右边正合的意思是 $$\operatorname{im}v=\ker(M''\to0)=\ker 0=M''$$，这正是满射的定义。(3) 由 (1)(2) 只剩中间一条 $$\operatorname{im}u=\ker v$$；此时 $$v$$ 诱导同构 $$\bar v:M/\ker v\to\operatorname{im}v=M''$$（定理 3.4），把 $$\ker v=\operatorname{im}u=u(M')$$ 代入即得。$$\blacksquare$$

**例 3.5（本章会用到的两个短正合列）**

**(i) 理想版**：$$0\to\mathfrak{a}\to A\to A/\mathfrak{a}\to0$$（包含映射、商映射）。

**(ii) 整数版（本章的主角）**：对 $$n\ge1$$，

$$0\to\mathbb{Z}\xrightarrow{\ \times n\ }\mathbb{Z}\xrightarrow{\ \pi\ }\mathbb{Z}/n\mathbb{Z}\to 0 ,$$

其中 $$\times n$$ 是乘以 $$n$$、$$\pi$$ 是商映射。正合性：$$\times n$$ 单（$$n\ne0$$ 时 $$nm=0\Rightarrow m=0$$）；$$\pi$$ 满；$$\operatorname{im}(\times n)=n\mathbb{Z}=\ker\pi$$。**这个序列将同时给出张量积不左正合的反例（3.4）与 Hom 不右正合的反例（3.5）——同一个三项序列，两个相反方向的失败。**

### 3.3 直和、自由模，与「基」的失效

下一步要造一个模，能把一族模"并排摆放"，又不至于因为指标集无限而让加法失去意义——这就是为什么要求"只有有限多个分量非零"：这样任意有限多项的加法在每个分量上都只是有限和，运算始终有意义。

**定义 3.6（直和, direct sum）** 设 $$\{M_i\}_{i\in I}$$ 是一族 $$A$$-模。它们的**直和** $$\bigoplus_{i\in I}M_i$$ 是全体**有限支撑**的族 $$(m_i)_{i\in I}$$（即只有有限多个 $$i$$ 使 $$m_i\ne0$$），加法与标量乘法按分量进行。第 $$i$$ 个**嵌入 (embedding)** $$\iota_i:M_i\to\bigoplus_jM_j$$ 把 $$m$$ 送到第 $$i$$ 坐标为 $$m$$、其余为 $$0$$ 的族。指标集有限时，直和与**直积 (direct product)** $$\prod_iM_i$$（取消有限支撑要求）作为模相同。

**命题 3.6（直和的万有性质）** 设 $$N$$ 是 $$A$$-模，$$\{f_i:M_i\to N\}_{i\in I}$$ 是一族同态。则存在**唯一**的同态 $$f:\bigoplus_iM_i\to N$$ 使 $$f\circ\iota_i=f_i$$ 对一切 $$i$$ 成立。

*证明*。**存在性**：规定 $$f\big((m_i)_i\big):=\sum_if_i(m_i)$$。这个和是有限和（因为族有限支撑），故有意义；加法与标量逐分量验证，$$f$$ 是 $$A$$-线性的（用了每个 $$f_i$$ 线性）。在 $$\iota_i(m)$$（第 $$i$$ 坐标 $$m$$、其余 $$0$$）上求值，和里只剩一项，得 $$f_i(m)$$。**唯一性**：任何满足条件的 $$g$$ 在所有 $$\iota_i(m_i)$$ 上与 $$f$$ 一致，而每个族 $$(m_i)$$ 都是有限和 $$\sum_i\iota_i(m_i)$$，故 $$g$$ 由 $$g\circ\iota_i$$ 决定。$$\blacksquare$$

**例 3.6** $$\mathbb{Z}^n=\bigoplus_{i=1}^n\mathbb{Z}$$；有限生成 Abel 群的结构定理说的就是「$$\cong$$ 自由部分 $$\oplus$$ 若干循环群」。若用 $$A=k[x]$$，不变子空间是各 $$M_i$$ 的不变子空间的直和——**第 38 章把 Hilbert 空间分解成一维不变子空间的直和，用模语言写就是：把 $$\mathbb{C}[x]$$-模写成最简子模的直和。** 在范畴论的语言里（第 62 章的主题），直和是**余积**；命题 3.6 就是它的万有性质在 $$A\text{-}\mathbf{Mod}$$ 里的样子。

**定义 3.7（自由模, free module）** 称 $$A$$-模 $$F$$ 是**自由的**，若存在一组元素 $$\{e_i\}_{i\in I}\subseteq F$$ 使每个元素 $$m\in F$$ 都能**唯一**地写成有限线性组合

$$m=\sum_{i\in I}a_ie_i\qquad(a_i\in A,\ \text{只有有限多个非零}).$$

这组 $$\{e_i\}$$ 叫 $$F$$ 的一组**基 (basis)**。等价地说，$$F\cong\bigoplus_{i\in I}A$$（第 $$i$$ 个分量是 $$A e_i$$）。

**定理 3.8（自由模的万有性质）** 设 $$F$$ 是以 $$\{e_i\}_{i\in I}$$ 为基的自由 $$A$$-模，$$N$$ 是任意 $$A$$-模，$$\{n_i\}_{i\in I}\subseteq N$$ 是任意一族元素。则存在**唯一**的同态 $$f:F\to N$$ 使 $$f(e_i)=n_i$$ 对一切 $$i$$。

*证明*。**唯一性**：$$F$$ 中每个元素是 $$\sum_ia_ie_i$$，$$f$$ 线性迫使 $$f\big(\sum_ia_ie_i\big)=\sum_ia_in_i$$，故 $$f$$ 被它在基上的取值决定。**存在性**：直接按上式定义 $$f$$。需要验证两件事。其一，**良定义**：若 $$\sum_ia_ie_i=\sum_ib_ie_i$$，由基的表示唯一性 $$a_i=b_i$$ 对一切 $$i$$，故两个表达式给出同一个值。其二，**线性**：$$\sum_i(a_i+a_i')e_i$$ 的像是 $$\sum_i(a_i+a_i')n_i=\sum_ia_in_i+\sum_ia_i'n_i$$（有限和的重新组合），标量同理。$$\blacksquare$$

**例 3.8** $$A^n=\bigoplus_{i=1}^nA$$ 自由，基是标准基。$$A=k[x]$$ 作为 $$k[x]$$-模自由（基 $$\{1\}$$），作为 $$k$$-模也自由（基 $$\{1,x,x^2,\dots\}$$，**无限**基，所以「自由模不必有限生成」）。定理 3.8 就是线性代数里「线性映射由基上取值唯一决定」这条事实在环上的逐字推广，它同时说明自由模「最省」：**造从 $$F$$ 出发的同态，只要在基上随便指哪里，就有唯一的同态接上。** 第 66 章会把它重述为「自由函子是遗忘函子的左伴随」。

**定理 3.9（自由模的秩良定义）** 设 $$A$$ 是非零交换环，$$A^{\oplus I}\cong A^{\oplus J}$$ 作为 $$A$$-模，则 $$\lvert I\rvert=\lvert J\rvert$$。这个公共的基数称为自由模的**秩 (rank)**。

*证明*。先注意：**每个非零交换环都有极大理想**。证：$$A$$ 的真理想按包含构成偏序集，它非空（$$(0)$$ 是真理想，因为 $$A\ne0$$）。链 $$\mathfrak{a}_\lambda$$ 的并 $$\mathfrak{a}=\bigcup_\lambda\mathfrak{a}_\lambda$$ 仍是理想（两个元素落在链的某一段里）且 $$1\notin\mathfrak{a}$$，故是真理想、是这条链的上界。由 Zorn 引理得极大元 $$\mathfrak{m}$$。于是 $$k:=A/\mathfrak{m}$$ 是**域**（$$\mathfrak{m}$$ 极大 $$\iff$$ $$A/\mathfrak{m}$$ 无非平凡理想 $$\iff$$ 每个非零元可逆）。

取 $$\mathfrak{m}F\subseteq F$$ 为由所有 $$\mathfrak{m}$$ 中元素乘 $$F$$ 中元素生成的子模。商 $$F/\mathfrak{m}F$$ 被 $$k$$ 作用：$$(a+\mathfrak{m})\cdot(m+\mathfrak{m}F):=am+\mathfrak{m}F$$ 良定义（换代表元相差的都落在 $$\mathfrak{m}F$$ 里），且使 $$F/\mathfrak{m}F$$ 成为 **$$k$$-向量空间**。

现在取 $$F=A^{\oplus I}$$，基为 $$\{e_i\}$$。商映射 $$\pi:F\to F/\mathfrak{m}F$$ 满。**$$\{\pi(e_i)\}$$ 是 $$F/\mathfrak{m}F$$ 的基**：生成性来自 $$\pi$$ 满与每个元素是基的线性组合；**线性无关性**——若 $$\sum_i(a_i+\mathfrak{m})\,\pi(e_i)=0$$，即 $$\sum_ia_ie_i\in\mathfrak{m}F$$，则存在 $$m_j\in\mathfrak{m}$$ 使 $$\sum_ia_ie_i=\sum_jm_je_j$$。由 $$\{e_i\}$$ 是基、表示唯一，两边 $$e_i$$ 的系数相等，得 $$a_i\in\mathfrak{m}$$ 对一切 $$i$$，即每个标量 $$\overline{a_i}=0$$。所以

$$\dim_k\big(F/\mathfrak{m}F\big)=\lvert I\rvert .$$

若 $$A^{\oplus I}\cong A^{\oplus J}$$，这个同构把 $$\mathfrak{m}F_I$$ 映到 $$\mathfrak{m}F_J$$（因为 $$\mathfrak{m}$$ 的标量作用与同态交换），诱导 $$k$$-向量空间的同构 $$F_I/\mathfrak{m}F_I\cong F_J/\mathfrak{m}F_J$$，故 $$\lvert I\rvert=\lvert J\rvert$$（向量空间的维数良定义，见第 06 章定理 3.4）。$$\blacksquare$$

**例 3.9（模不一定有基——三档例子）**

**(a) $$\mathbb{Z}/n\mathbb{Z}$$，$$n\ge2$$。** 它有限（$$n$$ 个元素）。若它自由，则它是某个 $$\mathbb{Z}^{\oplus I}$$：$$I\neq\varnothing$$ 时这有可数无穷多个元素，$$I=\varnothing$$ 时是 $$\{0\}$$。两种都不是 $$\mathbb{Z}/n$$。**故它无基。** 注意这里拦路的是「有限」：$$\mathbb{Z}$$-模若要非零且自由，就必须无限。**这是它与向量空间最刺眼的区别——域上只要是有限维就有基，环上有限的东西可能根本没有基。**

**(b) $$\mathbb{Q}$$ 作为 $$\mathbb{Z}$$-模。** 先证 $$\mathbb{Q}$$ 中任何两个元素都 $$\mathbb{Z}$$-线性相关：对 $$q_1=\frac ab$$、$$q_2=\frac cd$$（$$b,d\ne0$$）取 $$u=bc$$、$$v=-ad$$，则

$$u\cdot\frac ab+v\cdot\frac cd=\frac{bca}{b}-\frac{adc}{d}=ac-ac=0,$$

而 $$(u,v)=(bc,-ad)$$ 不全为零（$$a,c$$ 至少一个非零时；若两者都为 $$0$$ 那本来就相关）。若 $$\mathbb{Q}$$ 有基，则任何两组基元素都相关，故 $$\lvert B\rvert\le1$$。$$B=\varnothing$$ 给 $$\mathbb{Q}=0$$，错。$$B=\{q\}$$ 给 $$\mathbb{Q}=\mathbb{Z}q$$，即 $$\mathbb{Q}$$ 是**循环群**；但取 $$q=\frac ab$$，元素 $$\frac{1}{2b}$$ 要求整数 $$k$$ 使 $$\frac{ka}{b}=\frac{1}{2b}$$，即 $$2ka=1$$，无解。**故 $$\mathbb{Q}$$ 无基。** 而它的「秩感」还在：任何两个元素相关、任何单个非零元素都够撑满它——**这种「有维数、没有基」的现象只有在环上才可能发生**，它是第 70 章「平坦、内射、投射」这些概念出场的直接原因。

**(c) $$k[x]/(x^2)$$ 作为 $$k[x]$$-模。** 它是 $$2$$ 维 $$k$$-向量空间，被元素 $$\bar1$$ 单独生成。若它自由，则由生成元个数为 $$1$$，它只能是秩 $$1$$ 的自由模 $$k[x]$$；但 $$k[x]$$ 是无限维 $$k$$-向量空间，与 $$2$$ 维的 $$k[x]/(x^2)$$ 不同构。**故无基。** 即使模由单个元素生成、即使在 $$k$$ 上有限维，它也可以不自由：$$x\cdot\bar1=\bar x\ne0$$ 而 $$x^2\cdot\bar1=0$$——**生成元被一个非零标量杀掉了，这就是不自由的精确原因。**

**注 3.9（交换性不是装饰）** 定理 3.9 的证明里，「极大理想」与「$$A/\mathfrak{m}$$ 是域」两处都用了交换性。去掉它，$$\lvert I\rvert$$ 不再是自由模的不变量：存在非交换环 $$R$$ 与 $$n\ne m$$ 使 $$R^n\cong R^m$$（非交换环论的经典事实，构造超出本章）。**这正是「行列式」「秩」默认交换的原因。**

### 3.4 张量积：万有性质活着，基与维数死了

**定义 3.10（$$A$$-双线性映射, $$A$$-bilinear map）** 设 $$M,N,P$$ 是 $$A$$-模。映射 $$h:M\times N\to P$$ 称为 **$$A$$-双线性**，若对每个固定的第二变元它是 $$A$$-线性的、对每个固定的第一变元它也是 $$A$$-线性的，即

$$h(m+m',n)=h(m,n)+h(m',n),\qquad h(am,n)=a\,h(m,n),$$
$$h(m,n+n')=h(m,n)+h(m,n'),\qquad h(m,an)=a\,h(m,n)$$

对一切 $$m,m'\in M$$、$$n,n'\in N$$、$$a\in A$$ 成立。$$\mathbb{Z}$$-双线性就是「对两个变元分别可加」——因为 $$\mathbb{Z}$$-模的标量作用由加法生成（例 3.1(i)）。

**与第 22 章同一处陷阱**：把 $$M\times N$$ 看作直积模（定义 3.6），则一个同态 $$h:M\times N\to P$$ 必形如 $$h(m,n)=f(m)+g(n)$$（$$f,g$$ 为同态），它永远「不加混合项」；而一般的双线性映射不是这个样子（例如 $$A=\mathbb{Z}$$、$$h(m,n)=mn$$）。**所以 $$M\times N$$ 不是承载双线性映射的正确空间，必须另造一个。** 这与第 22 章命题 3.2 是同一件事。

**定义 3.11（张量积的万有性质, universal property of the tensor product）** 设 $$M,N$$ 是 $$A$$-模。一对 $$(T,\otimes)$$，其中 $$T$$ 是 $$A$$-模、$$\otimes:M\times N\to T$$ 是 $$A$$-双线性映射，称为 $$M$$ 与 $$N$$ 的**张量积 (tensor product)**，若：对任何 $$A$$-模 $$P$$ 与任何 $$A$$-双线性映射 $$h:M\times N\to P$$，存在**唯一**的 $$A$$-模同态 $$\bar h:T\to P$$ 使

$$\bar h\circ\otimes=h .$$

**把这个定义与第 22 章定义 3.4 并排读**：那里写「实线性空间 / 线性映射」，这里写「$$A$$-模 / $$A$$-线性同态」。**除这两个词以外，一字未改。** 本章的「升级」在定义层面上是零成本的——成本全部会在下面两条注里冒出来。

**定理 3.12（存在性）** 对任意 $$A$$-模 $$M,N$$，满足定义 3.11 的 $$(T,\otimes)$$ 存在。

*证明思路*：先造一个「太自由」的模 $$F$$（以 $$M\times N$$ 为基），再把「双线性」的四条要求作为关系一次性商掉，最后用 $$F$$ 的万有性质验证剩下的都自动成立。

*证明*。取 $$F$$ 为以集合 $$M\times N$$ 为基的自由 $$A$$-模（定义 3.7，$$I=M\times N$$），基元素记作 $$e_{(m,n)}$$。取 $$K\subseteq F$$ 为由下列四类元素生成的子模（对一切 $$m,m'\in M$$、$$n,n'\in N$$、$$a\in A$$）：

$$e_{(m+m',n)}-e_{(m,n)}-e_{(m',n)},\qquad e_{(am,n)}-a\,e_{(m,n)},$$
$$e_{(m,n+n')}-e_{(m,n)}-e_{(m,n')},\qquad e_{(m,an)}-a\,e_{(m,n)} .$$

令 $$T:=F/K$$，并令 $$\otimes(m,n):=e_{(m,n)}+K\in T$$。

**第一步：$$\otimes$$ 是 $$A$$-双线性的。** 上述四类元素正是双线性四条等式搬进 $$F$$ 后的样子；它们在 $$K$$ 中被杀掉，搬回 $$T$$ 就是等式。例如

$$\otimes(m+m',n)-\otimes(m,n)-\otimes(m',n)=\big(e_{(m+m',n)}-e_{(m,n)}-e_{(m',n)}\big)+K=0 ,$$

即 $$\otimes(m+m',n)=\otimes(m,n)+\otimes(m',n)$$。另外三条同法（第二条给 $$\otimes(am,n)=a\otimes(m,n)$$，第三条给第二变元的可加性，第四条给 $$\otimes(m,an)=a\otimes(m,n)$$）。

**第二步：万有性质。** 给定 $$A$$-双线性 $$h:M\times N\to P$$。因为 $$F$$ 以所有 $$e_{(m,n)}$$ 为基，定理 3.8 给出**唯一**同态 $$\varphi:F\to P$$ 使 $$\varphi(e_{(m,n)})=h(m,n)$$。$$h$$ 的双线性说明 $$\varphi$$ 在每一类生成元上取 $$0$$，例如

$$\varphi\big(e_{(am,n)}-a\,e_{(m,n)}\big)=h(am,n)-a\,h(m,n)=0 .$$

故 $$K\subseteq\ker\varphi$$。于是 $$\varphi$$ 在 $$F/K=T$$ 上分解（这正是定理 3.4 的用法：$$\bar\varphi(t+K):=\varphi(t)$$，良定义因为 $$K\subseteq\ker\varphi$$）：得同态 $$\bar h:T\to P$$，且

$$\bar h\big(\otimes(m,n)\big)=\bar h\big(e_{(m,n)}+K\big)=\varphi(e_{(m,n)})=h(m,n),$$

即 $$\bar h\circ\otimes=h$$。**第三步：唯一性。** $$T$$ 由诸 $$\otimes(m,n)$$ 生成（因为 $$T$$ 由诸 $$e_{(m,n)}+K$$ 生成，而后者就是 $$\otimes(m,n)$$），任何两个使 $$\bar h\circ\otimes=h$$ 成立的同态在所有生成元上一致，故相等。$$\blacksquare$$

**定理 3.13（唯一性）** 若 $$(T,\otimes)$$ 与 $$(T',\otimes')$$ 都满足定义 3.11（同一对 $$M,N$$），则存在**唯一**同构 $$\alpha:T\to T'$$ 使 $$\alpha\circ\otimes=\otimes'$$。

*证明*。把 $$\otimes':M\times N\to T'$$ 看成双线性映射，对 $$(T,\otimes)$$ 用万有性质，得唯一同态 $$\alpha:T\to T'$$ 使 $$\alpha\circ\otimes=\otimes'$$。对称地，把 $$\otimes$$ 看成双线性映射，对 $$(T',\otimes')$$ 用万有性质，得唯一同态 $$\beta:T'\to T$$ 使 $$\beta\circ\otimes'=\otimes$$。于是

$$\beta\alpha\circ\otimes=\beta\circ(\alpha\circ\otimes)=\beta\circ\otimes'=\otimes=\mathrm{id}_T\circ\otimes .$$

两边都是「使 $$\gamma\circ\otimes=\otimes$$ 成立、由 $$T$$ 的万有性质给出的那个同态」，故由唯一性 $$\beta\alpha=\mathrm{id}_T$$；同理 $$\alpha\beta=\mathrm{id}_{T'}$$。所以 $$\alpha$$ 是所要求的同构，唯一性由万有性质的唯一性直接给出。$$\blacksquare$$

因此记号 $$M\otimes_AN$$ 与 $$m\otimes n$$ 都无歧义（唯一到典范同构），本章从此放心使用。

**命题 3.14（基本运算律）** 下列同构都是**典范的**（不需要任何选择）。设 $$M,N,P$$ 是 $$A$$-模：

$$A\otimes_AM\cong M,\qquad M\otimes_AN\cong N\otimes_AM,\qquad (M\otimes_AN)\otimes_AP\cong M\otimes_A(N\otimes_AP),$$

$$M\otimes_A\Big(\bigoplus_{i\in I}N_i\Big)\cong\bigoplus_{i\in I}\big(M\otimes_AN_i\big).$$

*证明*。(1) 映射 $$h:A\times M\to M$$，$$h(a,m)=am$$，是双线性的——这正是定义 3.1 的四条公理（前两条给第二变元线性，第三、四条给第一变元的可加性与 $$(ab)m=a(bm)$$）。由万有性质得同态 $$\bar h:A\otimes M\to M$$，$$\bar h(a\otimes m)=am$$。另定义 $$\sigma:M\to A\otimes M$$，$$\sigma(m):=1\otimes m$$。$$\sigma$$ 是 $$A$$-线性的：由张量积的关系（定理 3.12 证明中第二类生成元，取 $$a=1$$ 方向的等价形式）$$a_0\otimes m=1\otimes(a_0m)$$，故

$$\sigma(a_0m)=1\otimes(a_0m)=a_0\otimes m=a_0(1\otimes m)=a_0\,\sigma(m).$$

于是 $$\bar h\sigma=\mathrm{id}_M$$（$$\bar h(\sigma(m))=\bar h(1\otimes m)=1\cdot m=m$$）；而 $$\sigma\bar h=\mathrm{id}_{A\otimes M}$$，因为两者在每个生成元 $$a\otimes m$$ 上一致：$$\sigma(\bar h(a\otimes m))=\sigma(am)=1\otimes am=a\otimes m$$。(2) $$(m,n)\mapsto n\otimes m$$ 双线性（双线性的定义只关心「对哪个变元线性」，交换两个变元仍然是双线性），由万有性质得 $$\alpha:M\otimes N\to N\otimes M$$；对称地得 $$\beta$$；在生成元上验证 $$\beta\alpha(m\otimes n)=m\otimes n$$ 与 $$\alpha\beta(n\otimes m)=n\otimes m$$。(3) 三次万有性质：$$(m,n,p)\mapsto m\otimes(n\otimes p)$$ 对三个变元分别线性，先得双线性映射 $$(M\otimes N)\times P\to M\otimes(N\otimes P)$$，其诱导同态即所求；反过来同样构造，在生成元上互逆。(4) 由命题 3.6，双线性映射 $$M\times\bigoplus_iN_i\to\bigoplus_i(M\otimes N_i)$$、$$(m,(n_i))\mapsto(m\otimes n_i)_i$$（有限支撑保证右端仍有限支撑）诱导出所求同态；反向同法，两者在生成元上互逆。$$\blacksquare$$

**注 3.14（第 22 章的哪条定理在这里死了）** 第 22 章定理 3.7 断言 $$\dim(V\otimes W)=\dim V\cdot\dim W$$，其证明是「展开 $$v=\sum_ia_ie_i$$、$$w=\sum_jb_jf_j$$，再比较系数」。到模上它**两处都坏**：

其一，**基可能不存在**（例 3.9 的 $$\mathbb{Z}/n$$、$$\mathbb{Q}$$），「展开」无从下笔；
其二，即使两边都有基，结论也不成立，因为张量积**可以把两个非零元打成零**：$$m\otimes n=0$$ 而 $$m,n\ne0$$。第五节的问题 1 会算出 $$\mathbb{Z}/m\otimes_{\mathbb{Z}}\mathbb{Z}/n\cong\mathbb{Z}/\gcd(m,n)$$，取 $$\gcd(m,n)=1$$ 就是 0；入口题 (b) 的 $$\mathbb{Q}\otimes\mathbb{Z}/n=0$$ 是同一现象的极端情形。

一句话记账：**定义层面的万有性质（定义 3.11）与第 22 章逐字相同，完好无损；死掉的是计算层面的「用基与维数算张量积」。** 替代品是正合性（定理 3.15）与万有性质的直接运用（问题 1、问题 3）。**这一节是本章与第 22 章的正式接口。**

**定理 3.15（张量积右正合）** 若 $$M'\xrightarrow{f}M\xrightarrow{g}M''\to0$$ 正合，则对任何 $$A$$-模 $$N$$，序列

$$M'\otimes_AN\xrightarrow{\ f\otimes1\ }M\otimes_AN\xrightarrow{\ g\otimes1\ }M''\otimes_AN\to0$$

正合。

*证明思路*：先造出两个映射；「满」与「复合为零」是生成元上的直接计算；**实质的一步是中间的正合性**，它等价于一个同构 $$\operatorname{coker}(f\otimes1)\cong M''\otimes N$$，我们把这个同构证成。

*证明*。映射 $$f\otimes1$$ 来自双线性映射 $$(m',n)\mapsto f(m')\otimes n$$（由定义 3.11 得同态），$$g\otimes1$$ 同理。

**(a) $$g\otimes1$$ 满。** $$\otimes$$ 的像是 $$M\otimes N$$ 的生成元集，而任一生成元 $$m''\otimes n$$ 由 $$g$$ 满可写成 $$g(m)\otimes n=(g\otimes1)(m\otimes n)$$。

**(b) $$(g\otimes1)\circ(f\otimes1)=0$$。** 在生成元上 $$(g\otimes1)((f\otimes1)(m'\otimes n))=g(f(m'))\otimes n=0$$，因为 $$\operatorname{im}f=\ker g$$。（生成元上的零映射是零同态。）

**(c) 中间的正合性。** 记 $$\operatorname{coker}(f\otimes1):=(M\otimes N)/\operatorname{im}(f\otimes1)$$。我们要证 $$\operatorname{coker}(f\otimes1)\cong M''\otimes N$$：由于 $$g\otimes1$$ 满且复合为零，它唯一的分解就是所需同构，只需验证 $$M''\otimes N$$ 确实具有这个余核性质，即：同态 $$\varphi:M\otimes N\to P$$ 满足 $$\varphi\circ(f\otimes1)=0$$ 当且仅当 $$\varphi=\bar\varphi\circ(g\otimes1)$$ 对某个（由满性唯一）$$\bar\varphi$$ 成立。

「$$\Longleftarrow$$」由 (b)。「$$\Longrightarrow$$」：设 $$\varphi\circ(f\otimes1)=0$$。定义 $$M''\times N\to P$$ 上的 $$(m'',n)\mapsto\varphi(\tilde m\otimes n)$$，其中 $$\tilde m$$ 是 $$m''$$ 在 $$g$$ 下的任一原像。**良定义**：若 $$g(\tilde m)=g(\tilde m')$$，则 $$\tilde m-\tilde m'=f(m')$$ 对某个 $$m'$$（因为 $$\ker g=\operatorname{im}f$$），于是

$$\varphi(\tilde m\otimes n)-\varphi(\tilde m'\otimes n)=\varphi\big((f\otimes1)(m'\otimes n)\big)=0 .$$

**双线性**：对 $$m''_1,m''_2$$ 各取原像 $$\tilde m_1,\tilde m_2$$，则 $$\tilde m_1+\tilde m_2$$ 是 $$m''_1+m''_2$$ 的原像，故 $$(m''_1+m''_2,n)$$ 处的值等于两处之和；标量同理（取 $$\widetilde{a_0m''}=a_0\tilde m$$），第二变元就是 $$\varphi(\tilde m\otimes-)$$ 的线性。由定义 3.11 得同态 $$\bar\varphi:M''\otimes N\to P$$，且 $$\bar\varphi(g(m)\otimes n)=\varphi(m\otimes n)$$，即 $$\bar\varphi\circ(g\otimes1)=\varphi$$。

所以 $$\operatorname{coker}(f\otimes1)$$ 与 $$M''\otimes N$$ 被同一组万有性质刻画，由余核的唯一性它们典范同构，这正是「$$\operatorname{im}(f\otimes1)=\ker(g\otimes1)$$」。$$\blacksquare$$

**例 3.15（张量积不左正合：完整的反例）** 取例 3.5(ii) 的短正合列 $$0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\xrightarrow{\pi}\mathbb{Z}/2\to0$$，张量上 $$\mathbb{Z}/2$$（写 $$\bar1$$ 表示 $$\mathbb{Z}/2$$ 中的生成元）：

$$\mathbb{Z}\otimes\mathbb{Z}/2\xrightarrow{\ (\times2)\otimes1\ }\mathbb{Z}\otimes\mathbb{Z}/2\xrightarrow{\ \pi\otimes1\ }\mathbb{Z}/2\otimes\mathbb{Z}/2\to0 .$$

由命题 3.14(1)，$$\mathbb{Z}\otimes\mathbb{Z}/2\cong\mathbb{Z}/2$$。而

$$(\times2)\otimes1\ (1\otimes\bar1)=2\otimes\bar1=1\otimes(2\cdot\bar1)=1\otimes\bar0=0$$

（中间一步是把标量从左边搬到右边，这是 $$K$$ 里的第三、四类关系）。所以 $$(\times2)\otimes1$$ 是**零映射**，特别地不单。**左正合性在此丧失**：$$\ker\big((\times2)\otimes1\big)=\mathbb{Z}/2\supsetneq0=\operatorname{im}(\text{零映射})$$。

再用定理 3.15 在**同一张纸上**算掉入口题 (a)：

$$\mathbb{Z}/2\otimes_{\mathbb{Z}}\mathbb{Z}/2\cong(\mathbb{Z}\otimes\mathbb{Z}/2)\big/\operatorname{im}\big((\times2)\otimes1\big)\cong(\mathbb{Z}/2)/0\cong\mathbb{Z}/2 .$$

**入口题 (a) 的答案：$$\mathbb{Z}/2\otimes_{\mathbb{Z}}\mathbb{Z}/2\cong\mathbb{Z}/2$$。** 正确的图像是：$$\mathbb{Z}$$ 里那个「乘以 2」**单**，是因为整数没有 2-扭；换成 $$\mathbb{Z}/2$$ 后 2-扭出现，$$\times2$$ 变成零映射，于是张量积把两个「2」全部塌掉，只剩一个 $$\mathbb{Z}/2$$。

**定义 3.16（平坦模, flat module）** $$A$$-模 $$N$$ 称为**平坦的**，若函子 $$-\otimes_AN$$ 保持单射：$$f$$ 单则 $$f\otimes1$$ 单。由定理 3.15，这等价于 $$-\otimes_AN$$ 保持一切短正合列。

**命题 3.16（平坦性的三个判断）** (1) $$A$$ 平坦，于是任何自由模平坦；(2) $$\mathbb{Z}/n$$（$$n\ge2$$）不平坦；(3) 一族模的直和 $$\bigoplus_iN_i$$ 平坦 $$\iff$$ 每个 $$N_i$$ 平坦。

*证明*。(1) 由命题 3.14(1)，$$-\otimes_AA$$ 与恒等函子自然同构（这些同构对 $$M$$ 一致地给出），恒等函子保一切单射，故 $$A$$ 平坦。对 $$F=A^{\oplus I}$$：由命题 3.14(4)，$$M\otimes F\cong\bigoplus_I(M\otimes A)\cong\bigoplus_IM$$；在这个同构下一个同态 $$f:M\to M'$$ 对应的映射就是 $$\bigoplus_I f$$（在 $$\bigoplus_I(M\otimes A)$$ 的每个分量上都是 $$f$$ 与 $$\mathrm{id}_A$$ 的复合），而分量逐项单则直和整体单（一个元素 $$(x_i)_i$$ 被 $$\bigoplus_If$$ 送到 $$0$$，当且仅当每个分量 $$f(x_i)=0$$，当且仅当每个 $$x_i=0$$）。这正是自由模平坦的完整论证。

**(3) 的正向证明要点相同，只是把 $$A$$ 换成任意平坦的 $$N_i$$。** 设每个 $$N_i$$ 平坦，$$f:M\to M'$$ 单。由命题 3.14(4)（对一般的 $$N_i$$，不限于 $$N_i=A$$），$$M\otimes\big(\bigoplus_iN_i\big)\cong\bigoplus_i(M\otimes N_i)$$，且这个同构把 $$f\otimes1_{\bigoplus N_i}$$ 对应到 $$\bigoplus_i(f\otimes1_{N_i})$$（逐分量地看，两边在生成元 $$m\otimes(n_i)_i$$ 上给出同一族元素）。因为每个 $$N_i$$ 平坦，每个分量映射 $$f\otimes1_{N_i}$$ 都单；再用上一段同样的"逐分量为零 $$\iff$$ 每个分量为零"的论证，$$\bigoplus_i(f\otimes1_{N_i})$$ 整体单。**反向**：若 $$\bigoplus_iN_i$$ 平坦，取定一个下标 $$i_0$$，任何单射 $$f:M\to M'$$ 沿同一个同构对应到 $$\bigoplus_i(f\otimes1_{N_i})$$ 单，特别地把它限制在第 $$i_0$$ 个分量上（其余分量取零）就得到 $$f\otimes1_{N_{i_0}}$$ 单——这就是「取一个分量即得」的具体含义。(2) 见例 3.15：映射 $$(\times n)\otimes1:\mathbb{Z}\otimes\mathbb{Z}/n\to\mathbb{Z}\otimes\mathbb{Z}/n$$ 把 $$1\otimes\bar1$$ 送到 $$n\otimes\bar1=1\otimes(n\bar1)=0$$，故是零映射；而 $$\mathbb{Z}\otimes\mathbb{Z}/n\cong\mathbb{Z}/n\ne0$$（命题 3.14(1)），所以它不单。$$\blacksquare$$

**注 3.16（$$\mathbb{Q}$$ 为什么平坦）** $$\mathbb{Z}\xrightarrow{\times n}\mathbb{Z}$$ 单；张量上 $$\mathbb{Q}$$ 后变成 $$\times n:\mathbb{Q}\to\mathbb{Q}$$，它**仍然单**，因为 $$\mathbb{Q}$$ 里的元素可以被 $$n$$ 整除。$$\mathbb{Z}/n$$ 的失败恰恰在于它**不能除以 $$n$$**（$$\bar1$$ 没有 $$n$$ 分之一，例 3.1(i) 已经算过这件事）。**「能除」与「不能除」的对立就是平坦与不平坦的对立**，它是第 70 章「局部化是平坦的」这条定理的雏形；本章只把它作为对照组记下。

### 3.5 Hom 函子：反变性与第 06 章的对偶

3.4 节把"两个模拼成一个模"的操作（张量积）研究透了；反过来，"两个模之间全体同态本身能不能也组织成一个模"，是同一个问题的另一半，也是本节要展开的对象——它将同时给出第 06 章"对偶空间"的推广（3.5 节末尾）与"投射模"的判据（3.7 节）。

**定义 3.17（Hom 集, Hom-set）** 设 $$M,N$$ 是 $$A$$-模。记

$$\operatorname{Hom}_A(M,N):=\{\varphi:M\to N\ :\ \varphi\ \text{是}\ A\text{-模同态}\},$$

并在其上规定**逐点**加法与标量乘法：

$$(\varphi+\psi)(m):=\varphi(m)+\psi(m),\qquad (a\varphi)(m):=a\,\varphi(m).$$

**命题 3.17** $$\operatorname{Hom}_A(M,N)$$ 在逐点加法下是 Abel 群；若 $$A$$ 交换，它在逐点标量乘法下是 $$A$$-模。

*证明*。零元是零映射，负元是 $$(-\varphi)(m):=-\varphi(m)$$。首先要验证 $$\varphi+\psi$$ 与 $$a\varphi$$ **仍是模同态**：

$$(\varphi+\psi)(m+m')=\varphi(m+m')+\psi(m+m')=\varphi(m)+\varphi(m')+\psi(m)+\psi(m')=(\varphi+\psi)(m)+(\varphi+\psi)(m'),$$

$$(\varphi+\psi)(a_0m)=\varphi(a_0m)+\psi(a_0m)=a_0\varphi(m)+a_0\psi(m)=a_0(\varphi+\psi)(m).$$

交换性来自 $$N$$ 是 Abel 群：$$(\varphi+\psi)(m)=\varphi(m)+\psi(m)=\psi(m)+\varphi(m)=(\psi+\varphi)(m)$$——**这一步用到的正是 3.1 里要求 $$M$$ 交换的同一条理由**。再看 $$a\varphi$$：$$(a\varphi)(a_0m)=a\,a_0\,\varphi(m)$$，而 $$a_0(a\varphi)(m)=a_0\,a\,\varphi(m)$$；两者相等要求 $$aa_0=a_0a$$——**$$A$$ 交换的假设在这里第一次真正上场**。其余公理（结合、单位、分配）逐点继承自 $$N$$。$$\blacksquare$$

**定义 3.18（协变 Hom 函子与反变 Hom 函子, covariant / contravariant Hom functor）**

**(1) 协变：** 固定 $$M$$，$$\operatorname{Hom}_A(M,-)$$ 是函子 $$A\text{-}\mathbf{Mod}\to\mathbf{Ab}$$：对象 $$N\mapsto\operatorname{Hom}_A(M,N)$$；同态 $$g:N\to P$$ 映为

$$\operatorname{Hom}_A(M,g):\operatorname{Hom}_A(M,N)\to\operatorname{Hom}_A(M,P),\qquad \varphi\mapsto g\circ\varphi$$

（**后复合**, postcomposition，箭头方向顺着 $$g$$ 走）。

**(2) 反变：** 固定 $$N$$，$$\operatorname{Hom}_A(-,N)$$ 是函子 $$(A\text{-}\mathbf{Mod})^{\mathrm{op}}\to\mathbf{Ab}$$：对象 $$M\mapsto\operatorname{Hom}_A(M,N)$$；同态 $$f:M'\to M$$ 映为

$$\operatorname{Hom}_A(f,N):\operatorname{Hom}_A(M,N)\to\operatorname{Hom}_A(M',N),\qquad \psi\mapsto\psi\circ f$$

（**前复合**, precomposition）。注意箭头被翻转：$$f:M'\to M$$ 给出的却是 $$\operatorname{Hom}(M,N)\to\operatorname{Hom}(M',N)$$——从 $$M$$ 那一头**倒着**走。

*验证反变那一支确是函子*：恒等——$$\operatorname{Hom}(\mathrm{id}_M,N)(\psi)=\psi\circ\mathrm{id}_M=\psi$$。复合——设 $$f:M'\to M$$、$$f':M''\to M'$$，则对任意 $$\psi\in\operatorname{Hom}(M,N)$$，

$$\operatorname{Hom}(f\circ f',N)(\psi)=\psi\circ(f\circ f')=(\psi\circ f)\circ f'=\operatorname{Hom}(f',N)\big(\operatorname{Hom}(f,N)(\psi)\big),$$

即 $$\operatorname{Hom}(f\circ f',N)=\operatorname{Hom}(f',N)\circ\operatorname{Hom}(f,N)$$。**右端两个函子的次序被翻了过来**——这就是「反变」的准确含义：它把复合的原序颠倒。协变那一支则是 $$\operatorname{Hom}(M,g\circ g')=\operatorname{Hom}(M,g)\circ\operatorname{Hom}(M,g')$$，次序不翻。

**注 3.18（第 06 章的对偶在这里回来）** 取 $$A=k$$ 是域、$$N=k$$。则反变函子 $$\operatorname{Hom}_k(-,k)$$ 把 $$V$$ 送到**对偶空间** $$V^*$$（第 06 章定义 3.2），把 $$T:V\to W$$ 送到**转置映射** $$T^{\mathsf T}:W^*\to V^*$$（第 06 章定义 3.13）。第 06 章定理 3.14 说的「转置线性、且反序复合」，与上面那一行 $$\operatorname{Hom}(f\circ f',N)=\operatorname{Hom}(f',N)\circ\operatorname{Hom}(f,N)$$ 是同一句话；第 06 章定理 3.17 及其后的「$$V^{**}$$ 与 $$V$$ 自然同构」则是对偶函子**用两次**、箭头转回协变的结果。**所以第 06 章的「对偶 = 反变」不是孤立现象，它是 $$\operatorname{Hom}_A(-,N)$$ 固定第二变元后的一个特例。**

**定理 3.19（Hom 左正合）** 设 $$M'\xrightarrow{f}M\xrightarrow{g}M''\to0$$ 正合，则对任何 $$N$$，

$$0\to\operatorname{Hom}_A(M'',N)\xrightarrow{\ \operatorname{Hom}(g,N)\ }\operatorname{Hom}_A(M,N)\xrightarrow{\ \operatorname{Hom}(f,N)\ }\operatorname{Hom}_A(M',N)$$

正合。

*证明*。(i) **$$\operatorname{Hom}(g,N)$$ 单**：设 $$\varphi\in\operatorname{Hom}(M'',N)$$ 使 $$\varphi\circ g=0$$。任取 $$m''=g(m)$$（$$g$$ 满），则 $$\varphi(m'')=\varphi(g(m))=0$$，故 $$\varphi=0$$。(ii) **复合为零**：$$\operatorname{Hom}(f,N)\big(\operatorname{Hom}(g,N)(\varphi)\big)=\varphi\circ g\circ f=0$$，因为 $$g\circ f=0$$（$$\operatorname{im}f=\ker g$$）。(iii) **$$\ker\operatorname{Hom}(f,N)\subseteq\operatorname{im}\operatorname{Hom}(g,N)$$**：设 $$\psi\in\operatorname{Hom}(M,N)$$ 满足 $$\psi\circ f=0$$，即 $$\psi$$ 在 $$\operatorname{im}f=\ker g$$ 上取 0。定义 $$\bar\psi:M''\to N$$，$$\bar\psi(m''):=\psi(\tilde m)$$（$$\tilde m$$ 是 $$m''$$ 的任一原像）。**良定义**：两个原像之差属于 $$\ker g=\operatorname{im}f$$，$$\psi$$ 在该差上取 0。**线性**：取原像 $$\tilde m_1+\tilde m_2$$ 与 $$a_0\tilde m$$ 可见。于是 $$\operatorname{Hom}(g,N)(\bar\psi)=\bar\psi\circ g=\psi$$。$$\blacksquare$$

**定理 3.20（Hom 不右正合：完整的反例）** 仍用 $$0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\xrightarrow{\pi}\mathbb{Z}/2\to0$$，接上反变函子 $$\operatorname{Hom}_{\mathbb{Z}}(-,\mathbb{Z})$$：

$$\operatorname{Hom}(\mathbb{Z}/2,\mathbb{Z})\xrightarrow{\ \operatorname{Hom}(\pi,\mathbb{Z})\ }\operatorname{Hom}(\mathbb{Z},\mathbb{Z})\xrightarrow{\ \operatorname{Hom}(\times2,\mathbb{Z})\ }\operatorname{Hom}(\mathbb{Z},\mathbb{Z})\to0\ ?$$

逐项算。$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z},\mathbb{Z})\cong\mathbb{Z}$$：同态由 $$1$$ 的像唯一决定（定理 3.8），$$1$$ 可送到任意整数。最后那个映射是**前复合** $$\psi\mapsto\psi\circ(\times2)$$；在 $$\mathbb{Z}\cong\operatorname{Hom}(\mathbb{Z},\mathbb{Z})$$ 这个同构下它就是「乘以 2」，像为 $$2\mathbb{Z}\subsetneq\mathbb{Z}$$，**不满**。**这就是右正合性的失败。**

顺带算掉左端那一项：$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z})=0$$。因为对任何 $$\varphi$$，由 $$2\cdot\bar1=\bar0$$ 得

$$2\,\varphi(\bar1)=\varphi(2\cdot\bar1)=\varphi(\bar0)=0 ,$$

而 $$\mathbb{Z}$$ 中若 $$\varphi(\bar1)\ne0$$ 则 $$2\varphi(\bar1)\ne0$$，故只能 $$\varphi(\bar1)=0$$，从而 $$\varphi=0$$。**把 $$\mathbb{Z}$$ 换成 $$\mathbb{Q}$$，这条序列就补齐成短正合列了**：$$\operatorname{Hom}(\times2,\mathbb{Q})$$ 是 $$\mathbb{Q}$$ 上的乘以 2，它**满**。$$\mathbb{Q}$$ 具备的这种性质叫**内射性 (injectivity)**，正是平坦性的对偶，第 70 章会正式引入。**于是入口题 (d) 的两半各就各位**：$$-\otimes N$$ 只保右正合，$$\operatorname{Hom}(M,-)$$ 只保左正合。

### 3.6 张量–Hom 伴随：第 66 章的起点

**定理 3.21（张量–Hom 伴随, tensor–Hom adjunction）** 设 $$A$$ 交换，$$M,N,P$$ 是 $$A$$-模。存在同构

$$\operatorname{Hom}_A(M\otimes_AN,\ P)\ \cong\ \operatorname{Hom}_A\big(N,\ \operatorname{Hom}_A(M,P)\big),$$

它对 $$M,N,P$$ 都是**自然的**。

*证明思路*：同构由「把二元函数的第二个变量固定、得到一族一元函数」给出。左边把 $$m\otimes n$$ 一起读，右边先读 $$n$$、再读 $$m$$。

*证明*。**构造 $$\Phi$$。** 给定 $$\varphi\in\operatorname{Hom}_A(M\otimes_AN,P)$$，规定

$$\Phi(\varphi):N\to\operatorname{Hom}_A(M,P),\qquad \Phi(\varphi)(n):=\big(m\mapsto\varphi(m\otimes n)\big).$$

(1) $$\Phi(\varphi)(n)$$ 确实落在 $$\operatorname{Hom}_A(M,P)$$ 里：$$m\mapsto\varphi(m\otimes n)$$ 是线性映射与「$$m\mapsto m\otimes n$$」（对第一变元线性）的复合。(2) $$\Phi(\varphi)$$ 是 $$A$$-线性的：对 $$n+n'$$ 用 $$\varphi$$ 在第一变元的线性，对 $$a_0n$$ 用 $$\varphi(m\otimes a_0n)=\varphi(a_0(m\otimes n))=a_0\varphi(m\otimes n)$$，后者正是 $$\operatorname{Hom}_A(M,P)$$ 的逐点标量乘法。(3) $$\Phi$$ 是 $$A$$-线性的（对 $$\varphi+\varphi'$$ 与 $$a_0\varphi$$ 逐点验证）。

**构造 $$\Psi$$。** 给定 $$\psi\in\operatorname{Hom}_A\big(N,\operatorname{Hom}_A(M,P)\big)$$。定义 $$h:M\times N\to P$$，$$h(m,n):=\psi(n)(m)$$。**$$h$$ 双线性**：对第一变元，每个 $$\psi(n)$$ 是线性的；对第二变元，$$n\mapsto\psi(n)$$ 线性、再逐点求值。由定义 3.11，$$h$$ 唯一诱导 $$\Psi(\psi)\in\operatorname{Hom}_A(M\otimes_AN,P)$$，满足

$$\Psi(\psi)(m\otimes n)=h(m,n)=\psi(n)(m).$$

**互逆。** 只需在生成元上验证（$$\{m\otimes n\}$$ 生成 $$M\otimes_AN$$）：

$$\Psi\big(\Phi(\varphi)\big)(m\otimes n)=\Phi(\varphi)(n)(m)=\varphi(m\otimes n)\ \Longrightarrow\ \Psi\Phi=\mathrm{id};$$

$$\Phi\big(\Psi(\psi)\big)(n)(m)=\Psi(\psi)(m\otimes n)=\psi(n)(m)\quad\text{对一切 }m,n\ \Longrightarrow\ \Phi\Psi=\mathrm{id}.$$

**自然性（先看 $$P$$ 这个变元）。** 设 $$\rho:P\to P'$$。两个函子 $$P\mapsto\operatorname{Hom}(M\otimes N,P)$$ 与 $$P\mapsto\operatorname{Hom}(N,\operatorname{Hom}(M,P))$$ 上的自然变换都取「与 $$\rho$$ 后复合」。追踪一个 $$\varphi$$：

$$\Phi(\rho\circ\varphi)(n)(m)=(\rho\circ\varphi)(m\otimes n)=\rho\big(\varphi(m\otimes n)\big),$$

而右端恰是 $$\big(\operatorname{Hom}(M,\rho)\circ\Phi(\varphi)\big)(n)(m)$$。故 $$\Phi(\rho\circ\varphi)=\operatorname{Hom}(M,\rho)\circ\Phi(\varphi)$$，即自然性方块交换。对 $$M$$ 与 $$N$$ 的变元同法：把 $$\varphi$$ 沿 $$M$$ 或 $$N$$ 做前复合后再追踪生成元，可见 $$\Phi$$ 与之交换。$$\blacksquare$$

**注 3.21（这里就是第 66 章的入口）** 定理 3.21 写成函子语言就是

$$-\otimes_AM\ \dashv\ \operatorname{Hom}_A(M,-)\quad:\quad \operatorname{Hom}_A(N\otimes_AM,P)\cong\operatorname{Hom}_A\big(N,\operatorname{Hom}_A(M,P)\big),$$

这正是**伴随函子 (adjoint functor)** 的定义式：左伴随是张量积，右伴随是 Hom。在经典伴随对清单（自由–遗忘、张量–Hom、诱导–限制）中，「张量积 $$-\otimes_AM$$ / Hom $$\operatorname{Hom}_A(M,-)$$」这一行就是本章这一节。**第 66 章「伴随函子与 Yoneda 引理」的第一个具体例子，正是这条同构**；第 66 章会证明「左伴随保余极限、右伴随保极限」，届时**定理 3.15（张量右正合）与定理 3.19（Hom 左正合）立刻变成同一条定理的两个特例**——余核是余极限，核是极限。

这也是入口题 (d) 的最终答案。两个数

$$\dim(V\otimes_{\mathbb{R}}W)=\dim V\cdot\dim W,\qquad \dim\operatorname{Hom}_{\mathbb{R}}(V,W)=\dim V\cdot\dim W$$

相等纯属**有限维**这一特殊情形下的巧合；它们的**性**之所以相反，是因为它们分别站在伴随的两侧：$$-\otimes M$$ 保余极限（满射、直和、余核），$$\operatorname{Hom}(M,-)$$ 保极限（单射、直积、核）。**一侧保「合起来」，另一侧保「拆开来」——这就是全部原因。**

**一条更朴素的读法。** 在集合范畴里，二元函数的第二种读法是「固定一个变量」：$$\{f:M\times N\to P\}\ \longleftrightarrow\ \{n\mapsto(m\mapsto f(m,n))\}$$。定理 3.21 就是这条指数律在模上的化身：张量积扮演「把两个变元打包成变量数为 1 的定义域」，Hom 扮演「把函数本身装成一个空间」。

### 3.7 自由模与投射模的雏形

3.3 节已经看到自由模是"最省"的模——从它出发的同态可以随意指定基上的取值。但自由模太少（例 3.9 三档反例都不自由），于是要问：**哪些模虽然不自由，却仍然继承了自由模那条最有用的性质——从它出发的同态能沿任何满射"抬"上去？** 这个性质本身，就足以撑起下面整节。

**定义 3.22（投射模, projective module）** $$A$$-模 $$P$$ 称为**投射的**，若对任何满同态 $$g:M\twoheadrightarrow M''$$ 与任何同态 $$h:P\to M''$$，存在同态 $$\tilde h:P\to M$$ 使

$$g\circ\tilde h=h .$$

$$\tilde h$$ 称为 $$h$$ 沿 $$g$$ 的**提升 (lift)**。直观：**从 $$P$$ 出发的同态总能沿满射抬一层。**

**定理 3.23（投射的三个等价刻画）** 对 $$A$$-模 $$P$$，下列三条等价：

(1) $$P$$ 投射；(2) 存在 $$A$$-模 $$Q$$ 使 $$P\oplus Q$$ 是自由模（即 $$P$$ 是自由模的**直和项 (direct summand)**）；(3) 函子 $$\operatorname{Hom}_A(P,-)$$ 保持满射。

*证明*。**(1)$$\iff$$(3)**：设 $$g:M\twoheadrightarrow M''$$。「$$\operatorname{Hom}(P,g)$$ 满」的意思是：任意 $$h\in\operatorname{Hom}(P,M'')$$ 都等于 $$g\circ\tilde h$$ 对某个 $$\tilde h$$。这正是 (1) 的定义，故 (3) 与 (1) 是同一句话的两种写法。

**(2)$$\Rightarrow$$(1)**：设 $$P\oplus Q=F$$ 自由，记 $$\pi_P:F\to P$$ 为投影、$$\iota_P:P\to F$$ 为嵌入（$$\pi_P\circ\iota_P=\mathrm{id}_P$$）。给定 $$g:M\twoheadrightarrow M''$$ 与 $$h:P\to M''$$，考虑 $$h\circ\pi_P:F\to M''$$。因 $$F$$ 自由（定理 3.8），同态由基上取值唯一决定；对每个基元 $$e_i$$，因 $$g$$ 满，可选 $$m_i\in M$$ 使 $$g(m_i)=(h\circ\pi_P)(e_i)$$。设 $$\tilde k:F\to M$$ 是「$$\tilde k(e_i)=m_i$$」给出的同态，则 $$g\circ\tilde k$$ 与 $$h\circ\pi_P$$ 在所有 $$e_i$$ 上一致，故相等。令 $$\tilde h:=\tilde k\circ\iota_P$$，则

$$g\circ\tilde h=g\circ\tilde k\circ\iota_P=h\circ\pi_P\circ\iota_P=h .$$

**(1)$$\Rightarrow$$(2)**：先取一组生成元。令 $$I:=P$$（取所有元素为指标），$$F:=A^{\oplus I}$$，其基为 $$\{e_p\}_{p\in P}$$。由定理 3.8 得同态

$$\pi:F\to P,\qquad \pi(e_p)=p .$$

$$\pi$$ 满：任意 $$p\in P$$ 是「一个基元的系数为 1、其余为 0」的组合。对满射 $$\pi$$ 与 $$h=\mathrm{id}_P$$ 用提升性质，得 $$s:P\to F$$ 使 $$\pi\circ s=\mathrm{id}_P$$。断言

$$F=s(P)\oplus\ker\pi .$$

**和是直和**：若 $$y\in s(P)\cap\ker\pi$$，则 $$y=s(p)$$ 且 $$0=\pi(y)=\pi(s(p))=p$$，故 $$y=s(0)=0$$。**和是整个 $$F$$**：对任意 $$x\in F$$ 写

$$x=s\big(\pi(x)\big)+\big(x-s(\pi(x))\big),$$

第一项在 $$s(P)$$ 中，第二项在 $$\ker\pi$$ 中（因为 $$\pi(x)-\pi(s(\pi(x)))=\pi(x)-\pi(x)=0$$）。于是 $$s(P)\cong P$$（$$s$$ 与 $$\pi\vert_{s(P)}$$ 互逆），$$P$$ 是自由模 $$F$$ 的直和项，取 $$Q:=\ker\pi$$ 即得。$$\blacksquare$$

**例 3.23（投射但不自由：最小的例子）** 取 $$A=\mathbb{Z}/6$$、$$P=\mathbb{Z}/2$$，$$P$$ 上的 $$A$$-作用为 $$(a+6\mathbb{Z})\cdot(m+2\mathbb{Z}):=am+2\mathbb{Z}$$（良定义：$$6\mathbb{Z}\cdot m\subseteq2\mathbb{Z}$$）。由中国剩余定理，

$$\mathbb{Z}/6\to\mathbb{Z}/2\times\mathbb{Z}/3,\qquad k\mapsto(k\bmod2,\ k\bmod3)$$

是**环**同构，因而也是 $$\mathbb{Z}/6$$-模同构；而 $$\mathbb{Z}/6$$ 是秩 1 的自由 $$A$$-模。所以 $$P=\mathbb{Z}/2$$ 是自由模的直和项，由定理 3.23(2)$$\Rightarrow$$(1)，**它是投射的**。

它**不自由**：秩为 $$r$$ 的自由 $$A$$-模有 $$6^r$$ 个元素（$$r=0$$ 时 1 个，$$r\ge1$$ 时 $$6^r\ge6$$），而 $$P$$ 只有 2 个元素。两者对不上，故不自由。

**这个例子还说明投射性依赖基环。** 同一个 Abel 群 $$\mathbb{Z}/2$$ 作为 $$\mathbb{Z}$$-模**不**投射：若投射，由定理 3.23(3)，$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/2,-)$$ 保满射；但把它作用在满射 $$\mathbb{Z}\twoheadrightarrow\mathbb{Z}/2$$ 上得到 $$\operatorname{Hom}(\mathbb{Z}/2,\mathbb{Z})\to\operatorname{Hom}(\mathbb{Z}/2,\mathbb{Z}/2)$$，左端是 0（定理 3.20 算过），右端 $$\cong\mathbb{Z}/2\ne0$$，不满，矛盾。**所以「投射」不是群自身的性质，而是「群加上它的基环」的性质。**

**注 3.23（为什么这件事重要）** 「投射但不自由」不是病态，而是**常态**。几何上（Serre–Swan 对应），$$A$$ 上的有限生成投射模对应 $$A$$ 上的有限秩**向量丛**——自由模对应**平凡丛**，而 $$\mathbb{Z}/6$$ 与 $$\mathbb{Z}/2$$ 这一对就是「某个环上存在一条非平凡线丛」的最小代数模型。这条对应通向第 36、37 章。第 70 章会把「投射 / 内射 / 导出函子」整套机器装好，那时 $$\mathbb{Z}/2$$（作为 $$\mathbb{Z}$$-模）**不**投射这件事会被改写成 $$\operatorname{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z})\cong\mathbb{Z}/2$$——正是这个非零的上同调不变量挡住了提升。

## 四、几何与物理直觉 (Intuition)

**（一）模是「空间上的东西」，不是「空间」。** 域上向量空间可以当「空间」看：有基、有维数、有坐标。而模，按例 3.1(i)，$$\mathbb{Z}$$-模就是 Abel 群——Abel 群当然也有「秩」和「挠」，但它没有坐标。正确的图像来自代数几何：设 $$A=k[x_1,\dots,x_n]$$ 是 $$\mathbb{A}^n$$ 的坐标环，则

$$\{\text{有限生成 }A\text{-模}\}\ \longleftrightarrow\ \{\mathbb{A}^n\text{ 上的（拟）凝聚层}\}.$$

在这个对应下：**自由模** = 平凡向量丛，**有限生成投射模** = 一般的向量丛（Serre–Swan，注 3.23），**子模** = 子层，**张量积** = 层的张量积，**$$\operatorname{Hom}$$** = 内部 hom 层。**「模不一定有基」在几何上根本不是病态——它对应「向量丛不一定是平凡的」。**

**（二）张量积 = 基变换。** 设环同态 $$A\to B$$（例如 $$\mathbb{Z}\to\mathbb{Q}$$）。把 $$A$$-模 $$M$$ 送到 $$B\otimes_AM$$ 叫作**标量扩张 (extension of scalars)**——「$$M$$ 的元素允许被 $$B$$ 中的元素重新缩放」。入口题 (b) 就是它的极端情形：**把 $$\mathbb{Z}/n$$ 搬到 $$\mathbb{Q}$$ 上，那个「不能被 $$n$$ 除」的扭元素被除掉了，整块塌成 0。** 反之 $$\mathbb{Z}\to\mathbb{Z}/n$$ 是「搬到模掉 $$n$$ 的世界」（见问题 3）。

**（三）物理：态空间上有两个环在作用。** 这是原专栏的原始动机，值得完整写出来。设 $$\mathcal{H}$$ 是量子力学的态空间（第 30 章）。它上面有两个结构同时存在：

- $$\mathcal{H}$$ 是 $$\mathbb{C}$$-**模**（就是复向量空间），标量 $$\lambda$$ 的作用是 $$\psi\mapsto\lambda\psi$$；
- $$\mathcal{H}$$ 又是**算子环** $$\Lambda$$（自伴、正规、有界……这些算子构成的环）上的模，$$A\in\Lambda$$ 的作用是 $$\psi\mapsto A\psi$$。

预解式方程

$$(\lambda I-A)\psi=0$$

的两边各站着一个环：左端 $$\lambda\psi$$ 是 **$$\mathbb{C}$$-模作用**，右端 $$A\psi$$ 是 **$$\Lambda$$-模作用**。**「求解特征值问题」在模语言里就是「让两个不同的模作用对上」**：找到 $$\lambda$$，使 $$\lambda I-A\in\Lambda$$ 有非零核。而 $$\Lambda$$ 一般**不交换**（量子力学的全部内容就是这个不交换性：$$[x,p]=i\hbar$$，见第 44 章），所以范畴论语言在这里不是装饰——**非交换环上的模范畴，是量子力学天然的居住地**。

**（四）同一件事的四种语言。**

| 域上线性代数（第 22 章） | 环上模论（本章） | 几何（第 36–37 章） | 物理（第 15–19 章） |
|---|---|---|---|
| 向量空间 | $$A$$-模 | 拟凝聚层 | 态空间 $$\mathcal{H}$$ |
| 基 / 维数 | 自由模 / 秩（**可能不存在**） | 平凡丛 | 一组本征态 |
| $$V\otimes W$$ | $$M\otimes_AN$$ | 基变换（拉回） | 复合系统的状态 |
| 对偶 $$V^*$$ | $$\operatorname{Hom}_A(M,A)$$ | 对偶层 | 对偶空间（Dirac 左矢） |
| $$\operatorname{Hom}(V,W)$$ | $$\operatorname{Hom}_A(M,N)$$ | 内部 hom | 算子空间 |
| 线性算子 | 模同态 | 层映射 | 可观测量 |

**（五）伴随的几何读法。** 张量–Hom 伴随（定理 3.21）的几何版本是：**「从拉回的丛到目标丛的映射」与「从原丛到内部 hom 丛的映射」一一对应**。它成立只因「双线性」允许你把一个变量先扣下来、再处理另一个——**几何上这叫「先把纤维方向定下来」，代数上叫「currying」。** 第 66 章会把它抽象成「伴随」并给出统一判据。

## 五、经典问题精讲 (Classical Problems)

### 问题 1：$$\mathbb{Z}/m\otimes_{\mathbb{Z}}\mathbb{Z}/n$$ 的值

**考点**：张量积的万有性质（定义 3.11）与右正合性（定理 3.15）。**在结构里的位置**：回收入口题 (a)，并把它推广到全部 $$\gcd$$ 情形。

**解。** 记 $$d=\gcd(m,n)$$。两种算法给出同一答案。

**算法一（右正合）。** 用例 3.5(ii) 的短正合列（取 $$m$$）：

$$0\to\mathbb{Z}\xrightarrow{\ \times m\ }\mathbb{Z}\xrightarrow{\ \pi\ }\mathbb{Z}/m\to0 .$$

由定理 3.15，张量上 $$\mathbb{Z}/n$$ 后得正合列（并用命题 3.14(1) 把 $$\mathbb{Z}\otimes\mathbb{Z}/n$$ 换成 $$\mathbb{Z}/n$$）：

$$\mathbb{Z}/n\xrightarrow{\ (\times m)\otimes1\ }\mathbb{Z}/n\to\mathbb{Z}/m\otimes_{\mathbb{Z}}\mathbb{Z}/n\to0 .$$

于是 $$\mathbb{Z}/m\otimes\mathbb{Z}/n\cong(\mathbb{Z}/n)\big/\operatorname{im}\big((\times m)\otimes1\big)$$。而 $$(\times m)\otimes1$$ 就是 $$\mathbb{Z}/n$$ 上的「乘以 $$m$$」，其像是由 $$\bar m$$ 生成的循环子群，阶为 $$n/d$$（循环群中元素 $$\bar m$$ 的阶是 $$n/\gcd(m,n)$$，这里 $$\gcd(m,n)=d$$）。商群是循环群的商，仍循环，阶为

$$n\big/(n/d)=d=\gcd(m,n),$$

故 $$\mathbb{Z}/m\otimes_{\mathbb{Z}}\mathbb{Z}/n\cong\mathbb{Z}/d=\mathbb{Z}/\gcd(m,n)$$。

**算法二（直接由生成元与关系）。** 由定义 3.11，$$\mathbb{Z}/m\otimes\mathbb{Z}/n$$ 由元素 $$1\otimes1$$ 生成（因为 $$a\otimes b=ab(1\otimes1)$$：把两个标量先后搬到同一侧）。记 $$u=1\otimes1$$。关系

$$m\,u=(m\cdot1)\otimes1=0\otimes1=0,\qquad n\,u=1\otimes(n\cdot1)=1\otimes0=0$$

（$$m\cdot1=0$$ 在 $$\mathbb{Z}/m$$ 中，$$n\cdot1=0$$ 在 $$\mathbb{Z}/n$$ 中）。于是 $$u$$ 被 $$m$$ 与 $$n$$ 双双零化，等价于被 $$d=\gcd(m,n)$$ 零化：**由 Bézout**，$$d=am+bn$$，故 $$d\,u=a(mu)+b(nu)=0$$；反之若 $$k\,u=0$$ 则 $$\gcd(m,n)\mid k$$（因为 $$ku=0$$ 意味着 $$k$$ 在 $$\mathbb{Z}/m$$ 中是 $$0$$ 且在 $$\mathbb{Z}/n$$ 中是 $$0$$，即 $$m\mid k$$ 且 $$n\mid k$$）。所以 $$\mathbb{Z}/m\otimes\mathbb{Z}/n$$ 是由 $$u$$ 生成、被 $$d$$ 零化而不被任何更小的正整数零化的循环群，即 $$\mathbb{Z}/d$$。$$\blacksquare$$

**回收**：取 $$m=n=2$$，得 $$\mathbb{Z}/2\otimes\mathbb{Z}/2\cong\mathbb{Z}/\gcd(2,2)=\mathbb{Z}/2$$——入口题 (a) 的答案。取 $$\gcd(m,n)=1$$，得 0。

### 问题 2：$$\mathbb{Q}\otimes_{\mathbb{Z}}\mathbb{Z}/n=0$$，而 $$\mathbb{Q}$$ 不自由

**考点**：右正合性 + 「模可以没有基」（例 3.9(b)）。**位置**：回收入口题 (b) 与 (c)，并展示「秩 1」与「自由」是两个概念。

**解。** **第一步：** 用 $$0\to\mathbb{Z}\xrightarrow{\times n}\mathbb{Z}\to\mathbb{Z}/n\to0$$ 张量 $$\mathbb{Q}$$，定理 3.15 给

$$\mathbb{Q}\xrightarrow{\ \times n\ }\mathbb{Q}\to\mathbb{Q}\otimes_{\mathbb{Z}}\mathbb{Z}/n\to0 .$$

$$\mathbb{Q}$$ 上的「乘以 $$n$$」是**满**的：任何 $$q\in\mathbb{Q}$$ 都有 $$q=n\cdot(q/n)$$。故像几乎是整个 $$\mathbb{Q}$$，商为 0：

$$\mathbb{Q}\otimes_{\mathbb{Z}}\mathbb{Z}/n=0 .$$

**这就解释了入口题 (b)**：$$\mathbb{Z}/n$$ 是非零模，$$\mathbb{Q}$$ 也是非零模，但张量积把 $$n$$-扭整体除掉，结果是零。

**第二步：$$\mathbb{Q}$$ 的秩是 1。** 对整环 $$A$$ 与 $$A$$-模 $$M$$，定义

$$\operatorname{rank}M:=\dim_{\operatorname{Frac}(A)}\big(M\otimes_A\operatorname{Frac}(A)\big).$$

对 $$A=\mathbb{Z}$$、$$M=\mathbb{Q}$$，先证 $$\mathbb{Q}\otimes_{\mathbb{Z}}\mathbb{Q}\cong\mathbb{Q}$$：映射 $$\alpha:\mathbb{Q}\otimes\mathbb{Q}\to\mathbb{Q}$$，$$\alpha(a\otimes b)=ab$$，**满**（$$\alpha(a\otimes1)=a$$）；**单**——取公分母 $$d$$，把任意 $$\sum_ia_i\otimes b_i$$ 写成

$$\sum_i\frac{c_i}{d}\otimes b_i=\sum_i\frac{1}{d}\otimes c_ib_i=\frac{1}{d}\otimes\Big(\sum_ic_ib_i\Big),$$

（用了张量积的关系把标量 $$\frac{c_i}{d}$$ 从左边搬到右边）；若 $$\alpha\Big(\frac1d\otimes\sum_ic_ib_i\Big)=\frac1d\cdot\sum_ic_ib_i=0$$，则 $$\sum_ic_ib_i=0$$，从而 $$\frac1d\otimes0=0$$。故 $$\alpha$$ 是同构，$$\operatorname{rank}\mathbb{Q}=\dim_{\mathbb{Q}}\mathbb{Q}=1$$。

**第三步：$$\mathbb{Q}$$ 不自由。** 由例 3.9(b)：$$\mathbb{Q}$$ 中任何两个元素都 $$\mathbb{Z}$$-线性相关，故基至多 1 个元素；而 $$\mathbb{Q}$$ 不是循环群，故无基。**于是 $$\mathbb{Q}$$ 有秩 1、却不是 $$\mathbb{Z}$$**——「秩」（一个数）与「自由」（一个结构性质）第一次分家。这与入口题 (c) 是同一件事的两面：$$\mathbb{Z}$$-模住在 Abel 群的范畴里，「维数」只剩下它的影子「秩」。$$\blacksquare$$

### 问题 3：把 $$\mathbb{Z}/n\otimes_{\mathbb{Z}}M$$ 算干净

**考点**：定理 3.15 的直接应用。**位置**：一个把所有扭现象一网打尽的公式，入口题 (a)(b) 都是它的特例。

**解。** 命题：对任何 $$\mathbb{Z}$$-模 $$M$$ 与 $$n\ge1$$，

$$\mathbb{Z}/n\mathbb{Z}\otimes_{\mathbb{Z}}M\cong M/nM .$$

证明：取 $$0\to\mathbb{Z}\xrightarrow{\times n}\mathbb{Z}\to\mathbb{Z}/n\to0$$ 张量 $$M$$，定理 3.15 给正合列

$$M\xrightarrow{\ \times n\ }M\to\mathbb{Z}/n\otimes_{\mathbb{Z}}M\to0 ,$$

故 $$\mathbb{Z}/n\otimes_{\mathbb{Z}}M\cong M\big/nM$$。检验两个特例：$$M=\mathbb{Z}/2$$、$$n=2$$ 给 $$(\mathbb{Z}/2)/0\cong\mathbb{Z}/2$$（入口题 (a)）；$$M=\mathbb{Z}/3$$、$$n=2$$ 给 $$0$$（因为 $$2$$ 在模 3 下可逆，与问题 1 的 $$\gcd$$ 公式一致）；$$M=\mathbb{Q}$$ 给 $$\mathbb{Q}/n\mathbb{Q}=0$$（入口题 (b)）。

**这个公式是 $$\mathbb{Z}$$-模里「扭」的全部算术**：张量上 $$\mathbb{Z}/n$$ 就是「模掉 $$n$$ 倍」。$$\blacksquare$$

### 问题 4：$$k[x]$$-模、特征值与预解式

**考点**：例 3.1(ii)（$$k[x]$$-模 = 带算子的空间）与例 3.2(iii)（子模 = 不变子空间）。**位置**：本章与第 15–19 章的接口。

**解。** 设 $$k$$ 是域，$$V$$ 是有限维 $$k$$-向量空间，$$T:V\to V$$ 是线性算子，按例 3.1(ii) 把 $$V$$ 看成 $$k[x]$$-模（$$x\cdot v:=Tv$$）。命题：对 $$\lambda\in k$$，

$$\lambda\ \text{是}\ T\ \text{的特征值}\iff x-\lambda\ \text{零化某个非零}\ v\in V .$$

**证明**。由模结构，多项式 $$p(x)=\sum_ic_ix^i$$ 的作用是 $$p(T)=\sum_ic_iT^i$$；特别地常数多项式 $$\lambda$$ 的作用是 $$\lambda v$$，于是

$$(x-\lambda)\cdot v=Tv-\lambda v .$$

于是

$$\ker(x-\lambda)=\{v: Tv=\lambda v\}=\{\lambda\text{-特征向量}\}\cup\{0\},$$

这正是 $$T$$ 的 $$\lambda$$-**特征空间 (eigenspace)**。所以「$$\lambda$$ 是特征值」$$\iff$$ $$\ker(x-\lambda)\ne0$$ $$\iff$$ $$x-\lambda$$ 零化某个非零向量。

**与预解式的联系**：有限维时 $$\lambda I-T$$ 不可逆 $$\iff$$ $$\ker(\lambda I-T)\ne0$$（秩-零化度定理）；而 $$\ker(\lambda I-T)=\ker(x-\lambda)$$，两者是同一个子模。所以

$$\det(\lambda I-T)=0\iff\lambda I-T\ \text{不可逆}\iff(x-\lambda)\ \text{有非零核}\iff V\ \text{有非零的}\ (x-\lambda)\text{-扭子模}.$$

**这就是预解式 $$(\lambda I-A)\psi=0$$ 的模论读法**：左端的 $$\lambda\psi$$ 来自 $$\mathbb{C}$$-模作用，右端的 $$A\psi$$ 来自算子环 $$\Lambda$$-模作用。有限维时这件事由行列式收尾（第 36 章的谱）；无穷维时 $$\lambda I-T$$ 可以既不单、又不满、却有非零核——那时「谱」必须从「特征值集合」升级成「使 $$\lambda I-T$$ 不可逆的 $$\lambda$$ 的集合」（第 18、19 章），而模语言一步都不用改。$$\blacksquare$$

### 问题 5：$$\mathbb{Z}/n$$ 什么时候是投射 $$\mathbb{Z}$$-模？

**考点**：定理 3.23（投射的三个等价刻画）与「自由模无挠」。**位置**：3.7 的直接练习。

**解。** 命题：$$\mathbb{Z}/n$$ 是投射 $$\mathbb{Z}$$-模 $$\iff$$ $$n=1$$。

**证明**。**$$n=1$$ 方向**：$$\mathbb{Z}/1=0$$，零模是自由 $$\mathbb{Z}$$-模（以空集为基），自由则投射。**$$n\ge2$$ 方向**：设 $$\mathbb{Z}/n$$ 投射。由定理 3.23(2)，存在 $$\mathbb{Z}$$-模 $$Q$$ 使 $$F:=\mathbb{Z}/n\oplus Q$$ 自由。自由 $$\mathbb{Z}$$-模**无挠**：$$F\cong\mathbb{Z}^{\oplus I}$$，若 $$a x=0$$ 而 $$a\ne0$$，把 $$x$$ 写成有限线性组合 $$\sum_ik_ie_i$$，则每个 $$ak_i=0$$，故每个 $$k_i=0$$，$$x=0$$。而**子模继承无挠**：子模的元素仍是 $$F$$ 的元素，若它在子模中被 $$a$$ 零化，它在 $$F$$ 中也被 $$a$$ 零化，故只能是 0。现在 $$\mathbb{Z}/n$$ 是 $$F$$ 的直和项，因而（通过嵌入 $$\iota$$）是 $$F$$ 的子模；但 $$\mathbb{Z}/n$$ 有挠：$$n\cdot\bar1=\bar0$$ 而 $$\bar1\ne0$$（$$n\ge2$$）。这与无挠矛盾。故 $$n\ge2$$ 时不投射。$$\blacksquare$$

**若把基环换成 $$\mathbb{Z}/6$$，同一个例子的答案是「$$\mathbb{Z}/2$$ 投射」**（例 3.23）——所以本题的答案必须连同基环一起说，这是 3.7 要给读者的最后一条提醒。$$\blacksquare$$

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 写出 $$\mathbb{Z}/12\mathbb{Z}$$ 作为 $$\mathbb{Z}$$-模的全部子模，并指出其中哪些是直和项；最后指出分解 $$\mathbb{Z}/12\cong\mathbb{Z}/4\oplus\mathbb{Z}/3$$ 对应的是哪两个子模。

**基2.** 计算 $$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/m\mathbb{Z},\mathbb{Z}/n\mathbb{Z})$$。

**基3.** 计算 $$\mathbb{Z}/2\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/4\mathbb{Z}$$ 与 $$\mathbb{Z}/2\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Q}$$。

**基4.** 判断下列映射哪些是 $$\mathbb{Z}$$-模同态，并说明理由：
(a) $$\mathbb{Z}/6\mathbb{Z}\to\mathbb{Z}/6\mathbb{Z}$$，$$x\mapsto 3x$$；
(b) $$\mathbb{Z}\to\mathbb{Z}$$，$$n\mapsto n^2$$；
(c) $$\mathbb{Q}\to\mathbb{Q}$$，$$q\mapsto 2q$$；
(d) $$\mathbb{R}\to\mathbb{R}$$，$$x\mapsto x+1$$。

### 竞赛（本课目标难度）

**竞1.** 证明 $$\mathbb{Q}\otimes_{\mathbb{Z}}\mathbb{Q}/\mathbb{Z}=0$$ 与 $$\mathbb{Q}/\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Q}/\mathbb{Z}=0$$。

**竞2.** 设 $$P$$ 是投射 $$A$$-模。证明函子 $$\operatorname{Hom}_A(P,-)$$ 既保单射又保满射（即它是**正合函子**）。

**竞3.** 设 $$0\to M'\xrightarrow{f}M\xrightarrow{g}M''\to0$$ 是短正合列。说明为什么序列
$$0\to\operatorname{Hom}(M'',N)\to\operatorname{Hom}(M,N)\to\operatorname{Hom}(M',N)$$
一般**不能**在末尾补 $$\to0$$；再证明：若 $$M''$$ 投射，则可以补 $$\to0$$。

**竞4.** 设 $$P=P_1\oplus P_2$$ 是投射 $$A$$-模。证明 $$P_1$$ 与 $$P_2$$ 都投射。

**竞5.** 证明 $$\mathbb{Z}^n$$ 的每个子模都是自由 $$\mathbb{Z}$$-模；并由此证明：有限生成投射 $$\mathbb{Z}$$-模都是自由 $$\mathbb{Z}$$-模。

### 研究（通向下一章）

**研1.** 对伴随对 $$-\otimes_AN\dashv\operatorname{Hom}_A(N,-)$$，显式写出**单位**与**余单位**，并验证两条**三角恒等式**。说明这两条恒等式如何给出第 66 章「伴随函子」定义的另一半。

**研2.** 证明 $$\operatorname{Hom}_A(A,-)\cong\mathrm{id}_{A\text{-}\mathbf{Mod}}$$ 是自然同构；再证明：若两个函子 $$\operatorname{Hom}_A(P,-)$$ 与 $$\operatorname{Hom}_A(Q,-)$$ 自然同构，则 $$P\cong Q$$。说明这个命题与「$$P$$ 投射」这一性质的关系。

### 解答 (Solutions)

**解 基1.** $$\mathbb{Z}/12$$ 是循环群，循环群的子群与 $$12$$ 的正因子一一对应：阶为 $$d$$ 的子群是 $$\langle\overline{12/d}\rangle$$（唯一）。故子模共 6 个：

$$\{0\}\ (\text{阶}1),\quad \langle\bar6\rangle=\{0,6\}\cong\mathbb{Z}/2\ (\text{阶}2),\quad \langle\bar4\rangle\cong\mathbb{Z}/3\ (\text{阶}3),$$
$$\langle\bar3\rangle\cong\mathbb{Z}/4\ (\text{阶}4),\quad \langle\bar2\rangle\cong\mathbb{Z}/6\ (\text{阶}6),\quad \mathbb{Z}/12\ (\text{阶}12).$$

**直和项**：$$H$$ 是直和项，当且仅当存在 $$K$$ 使 $$H\cap K=\{0\}$$ 且 $$H+K=\mathbb{Z}/12$$。用中国剩余定理这个视角最清楚：

$$\mathbb{Z}/12\cong\mathbb{Z}/4\oplus\mathbb{Z}/3,\qquad \bar1\mapsto(\bar1,\bar1).$$

在这个分解下 $$\bar4\mapsto(0,1)$$，故 $$\langle\bar4\rangle$$ 是 $$\mathbb{Z}/3$$ 那个分量的全体，**是**直和项；$$\bar3\mapsto(3,0)$$，故 $$\langle\bar3\rangle\cong\mathbb{Z}/4$$ 是 $$\mathbb{Z}/4$$ 那个分量的全体，也**是**直和项。而 $$\bar6\mapsto(2,0)$$，$$\langle\bar6\rangle\cong\{0,2\}\times\{0\}\cong\mathbb{Z}/2$$ **不是** $$\mathbb{Z}/4$$ 的直和项：$$\mathbb{Z}/4$$ 不可分解（$$4$$ 是素数幂），它唯一的非零真子群 $$\langle2\rangle$$ 与任何非零子群都相交非零，故找不到补。最后 $$\bar2\mapsto(2,2)$$，$$\langle\bar2\rangle$$ 的阶为 6，它的任何补子群 $$K$$ 需阶 2，而 $$\mathbb{Z}/4\oplus\mathbb{Z}/3$$ 中唯一的阶 2 子群是 $$\{0,2\}\times\{0\}$$，其元素 $$(2,0)=3\cdot(2,2)\in\langle\bar2\rangle$$，交非零，故**不是**直和项。

**所以直和项恰好四个**：$$\{0\}$$、$$\mathbb{Z}/12$$、$$\langle\bar4\rangle\cong\mathbb{Z}/3$$、$$\langle\bar3\rangle\cong\mathbb{Z}/4$$。题末要求的分解正是 $$\mathbb{Z}/12\cong\langle\bar3\rangle\oplus\langle\bar4\rangle$$。

**解 基2.** 设 $$\varphi:\mathbb{Z}/m\to\mathbb{Z}/n$$ 是 $$\mathbb{Z}$$-模同态（$$=$$ Abel 群同态）。因为 $$\bar1$$ 生成 $$\mathbb{Z}/m$$，$$\varphi$$ 由 $$t:=\varphi(\bar1)\in\mathbb{Z}/n$$ 完全决定：$$\varphi(\bar k)=kt$$。约束条件来自 $$\bar0=m\cdot\bar1$$：

$$0=\varphi(\bar0)=\varphi(m\cdot\bar1)=m\,t .$$

反之，任何满足 $$mt=0$$ 的 $$t$$ 都给出一个同态 $$\varphi(\bar k):=kt$$，良定义是因为 $$k$$ 换成 $$k+m$$ 时 $$(k+m)t=kt+mt=kt$$。所以

$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/m,\mathbb{Z}/n)\cong\{t\in\mathbb{Z}/n:\ mt=0\}=\ker\big(\times m\ \text{on}\ \mathbb{Z}/n\big).$$

这个核在循环群 $$\mathbb{Z}/n$$ 中由 $$\gcd(m,n)$$ 的像生成：$$mt=0\iff n\mid mt\iff\frac{n}{\gcd(m,n)}\mid t$$。于是核 $$=\big\langle\overline{\gcd(m,n)}\big\rangle$$，其阶为 $$\gcd(m,n)$$，故

$$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/m,\mathbb{Z}/n)\cong\mathbb{Z}/\gcd(m,n) .$$

**解 基3.** 两个都用「$$\mathbb{Z}/n\otimes M\cong M/nM$$」（第五节问题 3）。

$$\mathbb{Z}/2\otimes\mathbb{Z}/4\cong(\mathbb{Z}/4)\big/2(\mathbb{Z}/4)=(\mathbb{Z}/4)/\{0,2\}\cong\mathbb{Z}/2 .$$

$$\mathbb{Z}/2\otimes\mathbb{Q}\cong\mathbb{Q}/2\mathbb{Q}=\mathbb{Q}/\mathbb{Q}=0 ,$$

末一步因为 $$2\mathbb{Q}=\mathbb{Q}$$（任何 $$q\in\mathbb{Q}$$ 都是 $$2\cdot(q/2)$$）。**这两题正好展示同一个公式的两种结局：一个「有扭」的模把扭留下来，一个「可除」的模把整个东西吃掉。**

**解 基4.** (a) **是**。$$x\mapsto3x$$ 保持加法（$$3(x+y)=3x+3y$$）与 $$\mathbb{Z}$$-标量（$$\mathbb{Z}$$-模同态就是加群同态，标量条件自动满足）。
(b) **不是**。加法不保持：$$(1+1)^2=4$$，而 $$1^2+1^2=2$$，$$4\ne2$$。
(c) **是**。乘以 2 保持加法与整数标量；事实上它还是 $$\mathbb{Q}$$-线性的，因为 $$2(\lambda q)=\lambda(2q)$$。
(d) **不是**。加法不保持：取 $$x=y=0$$，左端 $$(0+0)+1=1$$，右端 $$(0+1)+(0+1)=2$$，$$1\ne2$$。

**解 竞1.** **(i)** $$\mathbb{Q}\otimes_{\mathbb{Z}}\mathbb{Q}/\mathbb{Z}=0$$。张量积由生成元 $$q\otimes\bar b$$ 线性张成，故只要证每个生成元为 0。任取 $$\bar b\in\mathbb{Q}/\mathbb{Z}$$：它是**挠元**，即存在 $$n\ge1$$ 使 $$n\bar b=0$$。**理由**：$$\bar b=\overline{a/n}$$（$$\mathbb{Q}$$ 中每个元素有分数表示，模掉 $$\mathbb{Z}$$ 后仍可取公分母 $$n$$），故 $$n\bar b=\overline{a}=0$$。于是

$$q\otimes\bar b=\Big(n\cdot\frac qn\Big)\otimes\bar b=\frac qn\otimes(n\bar b)=\frac qn\otimes0=0 .$$

**(ii)** $$\mathbb{Q}/\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Q}/\mathbb{Z}=0$$。任取生成元 $$\bar a\otimes\bar b$$；设 $$\bar a$$ 的阶为 $$n$$（同上，$$\mathbb{Q}/\mathbb{Z}$$ 的元素都有有限阶）。**关键 leap 在于用 $$n\bar c=\bar a$$ 的「除以 $$n$$」把 $$\bar a$$ 改写**。这样的 $$\bar c$$ 存在，因为 $$\mathbb{Q}/\mathbb{Z}$$ 是**可除群 (divisible group)**：对 $$\bar a=\overline{a/n}$$ 取 $$\bar c:=\overline{a/n^2}$$，则 $$n\bar c=\overline{a/n}=\bar a$$。于是

$$\bar a\otimes\bar b=(n\bar c)\otimes\bar b=\bar c\otimes(n\bar b)=\bar c\otimes0=0 .$$

**这题的 key leap**：把「元素能被 $$n$$ 除」翻译成 $$a=nc$$，再用张量积的关系把标量 $$n$$ 从左边搬到右边——右端那个 $$n\bar b=0$$ 是现成的，于是整项塌成 0。同一个手法在第五节问题 2（$$\mathbb{Q}\otimes\mathbb{Z}/n=0$$）里已经用过一次：**「可除」是 $$-\otimes$$ 的杀手**。$$\blacksquare$$

**解 竞2.** 函子 $$\operatorname{Hom}_A(P,-)$$ 作用在 $$f:M'\to M$$ 上给出

$$\operatorname{Hom}(P,f):\operatorname{Hom}(P,M')\to\operatorname{Hom}(P,M),\qquad \psi\mapsto f\circ\psi .$$

**保单射**：设 $$f$$ 单。若 $$f\circ\psi=0$$，则对每个 $$p\in P$$，$$f(\psi(p))=0$$，由 $$f$$ 单得 $$\psi(p)=0$$；$$p$$ 任意故 $$\psi=0$$。所以 $$\operatorname{Hom}(P,f)$$ 单。**注意这里没有用到 $$P$$ 的任何性质**——Hom 函子永远保单，这正是定理 3.19 的内容。**保满射**：设 $$g:M\twoheadrightarrow M''$$。要证 $$\operatorname{Hom}(P,g)$$ 满，即任意 $$h:P\to M''$$ 都形如 $$g\circ\tilde h$$；**这正是 $$P$$ 投射的定义（定义 3.22），也等价于定理 3.23(3)**。

两条合起来：$$P$$ 投射时，$$\operatorname{Hom}_A(P,-)$$ 把一切短正合列 $$0\to M'\to M\to M''\to0$$ 映成短正合列 $$0\to\operatorname{Hom}(P,M')\to\operatorname{Hom}(P,M)\to\operatorname{Hom}(P,M'')\to0$$，这就是**正合函子**。$$\blacksquare$$

**解 竞3.** 由定理 3.19，那一列在三个位置都正合。补 $$\to0$$ 意味着要求 $$\operatorname{Hom}(f,N)$$ **满**，即每个 $$\psi:M'\to N$$ 都能沿 $$f$$ 延拓为 $$M\to N$$。**一般不行**：取第五节定理 3.20 的反例，$$M'=\mathbb{Z}\xrightarrow{\times2}M=\mathbb{Z}$$、$$M''=\mathbb{Z}/2$$、$$N=\mathbb{Z}$$，$$\psi=\mathrm{id}_{\mathbb{Z}}$$。若它延拓为 $$\tilde\psi$$，则 $$\tilde\psi(2)=\tilde\psi(2\cdot1)=2\tilde\psi(1)$$，而这必须等于 $$\psi(1)=1$$——即 $$2$$ 整除 $$1$$，矛盾。

**若 $$M''$$ 投射**（$$N$$ 任意）：对满射 $$g:M\twoheadrightarrow M''$$ 与 $$h:=\mathrm{id}_{M''}\in\operatorname{Hom}(M'',M'')$$ 用提升性质（定义 3.22），得 $$s:M''\to M$$ 使 $$g\circ s=\mathrm{id}_{M''}$$。断言

$$M=f(M')\oplus s(M'').$$

**和是直和**：若 $$y=f(m')=s(m'')$$，则 $$m''=g(s(m''))=g(f(m'))=0$$（因为 $$g\circ f=0$$），故 $$y=s(0)=0$$。**和是整个 $$M$$**：对 $$m\in M$$，$$\pi(m):=m-s(g(m))$$ 满足 $$g(\pi(m))=g(m)-g(s(g(m)))=g(m)-g(m)=0$$，故 $$\pi(m)\in\ker g=\operatorname{im}f$$，于是 $$m=f(m')+s(g(m))$$ 对某个 $$m'$$。现在定义

$$\tilde\psi\big(f(m')+s(m'')\big):=\psi(m') .$$

由直和性，$$M$$ 中每个元素**唯一**地写成 $$f(m')+s(m'')$$，故 $$\tilde\psi$$ 良定义；它是线性的（两个分量各自线性）；且 $$\tilde\psi\circ f=\psi$$。所以 $$\operatorname{Hom}(f,N)$$ 满，末尾可以补 $$\to0$$。$$\blacksquare$$

**（顺带看清结构）** 上面的论证说明 $$M\cong M'\oplus M''$$，即短正合列**分裂 (split)**。「$$M''$$ 投射 $$\iff$$ 任何以 $$M''$$ 为商的短正合列都分裂」，这是定理 3.23(2) 中「直和项」那种说法的等价形式。

**解 竞4.** 设 $$P$$ 投射、$$P=P_1\oplus P_2$$。由定理 3.23(2)，存在 $$Q$$ 使 $$P\oplus Q$$ 自由。则

$$P_1\oplus(P_2\oplus Q)=(P_1\oplus P_2)\oplus Q=P\oplus Q=\text{自由模}$$

（第一步是直和的结合律，见定义 3.6）。所以 $$P_1$$ 是自由模的直和项，由定理 3.23(2)$$\Rightarrow$$(1)，$$P_1$$ 投射；对 $$P_2$$ 同理（交换求和次序即可）。$$\blacksquare$$

**解 竞5.** **第一步：$$\mathbb{Z}$$ 的每个子模都同构于 $$\mathbb{Z}$$ 或 $$0$$。** 设 $$G\le\mathbb{Z}$$、$$G\ne\{0\}$$。取

$$d:=\min\{g\in G:\ g>0\},$$

它存在：$$G$$ 中有正元素（对 $$g\ne0$$ 取 $$\pm g$$ 中正的那个），正整数集由良序原理有最小元。对任意 $$g\in G$$ 做带余除法 $$g=qd+r$$、$$0\le r<d$$。则 $$r=g-qd\in G$$；若 $$r>0$$ 就与 $$d$$ 的最小性矛盾，故 $$r=0$$，即 $$g\in d\mathbb{Z}$$。于是 $$G\subseteq d\mathbb{Z}$$；反向由 $$d\in G$$ 得 $$d\mathbb{Z}\subseteq G$$。故 $$G=d\mathbb{Z}\cong\mathbb{Z}$$。

**第二步：$$\mathbb{Z}^n$$ 的每个子模都自由。** 对 $$n$$ 归纳。$$n=0$$ 时只有 $$\{0\}$$，以空集为基，自由。设结论对 $$n-1$$ 成立，$$G\le\mathbb{Z}^n$$。取「最后一个坐标」投影 $$\pi:\mathbb{Z}^n\to\mathbb{Z}$$。则 $$\pi(G)\le\mathbb{Z}$$ 是子模，由第一步 $$\pi(G)=d\mathbb{Z}$$（$$d\ge0$$）。
若 $$d=0$$：则 $$G\subseteq\mathbb{Z}^{n-1}\times\{0\}\cong\mathbb{Z}^{n-1}$$，由归纳假设自由。
若 $$d>0$$：取 $$g_0\in G$$ 使 $$\pi(g_0)=d$$。断言

$$G=\big(G\cap(\mathbb{Z}^{n-1}\times\{0\})\big)\oplus\mathbb{Z}g_0 .$$

**直**：若 $$mg_0$$ 的末坐标为 0，则 $$md=0$$，故 $$m=0$$。**和是整个 $$G$$**：对 $$g\in G$$，$$\pi(g)=kd$$，故 $$\pi(g-kg_0)=0$$，即 $$g-kg_0\in G\cap(\mathbb{Z}^{n-1}\times\{0\})$$。右端第一个和项是 $$\mathbb{Z}^{n-1}$$ 的子模，由归纳假设自由；故 $$G$$ 是自由模与 $$\mathbb{Z}$$ 的直和，自由。

**第三步：有限生成投射 $$\mathbb{Z}$$-模自由。** 设 $$P$$ 有限生成，取生成元 $$p_1,\dots,p_n$$，由定理 3.8 得满同态 $$\pi:\mathbb{Z}^n\to P$$、$$\pi(e_i)=p_i$$。对满射 $$\pi$$ 与 $$h=\mathrm{id}_P$$ 用提升性质（$$P$$ 投射），得 $$s:P\to\mathbb{Z}^n$$ 使 $$\pi\circ s=\mathrm{id}_P$$。于是 $$s$$ 是单射，$$P\cong s(P)\le\mathbb{Z}^n$$。由第二步，$$s(P)$$ 自由，故 $$P$$ 自由。$$\blacksquare$$

**（这道题的意义）** 定理 3.23 把「投射」与「自由」分开，本题却说明**在 $$\mathbb{Z}$$ 上它们分不开**（有限生成时）——例 3.23 那对反例必须换到 $$\mathbb{Z}/6$$ 上才出现。这与注 3.23 的向量丛图像一致：$$\mathbb{Z}$$ 上的线丛都平凡，非平凡线丛需要更复杂的基环。$$\blacksquare$$

**解 研1.** 固定 $$N$$，记 $$F=-\otimes_AN$$、$$G=\operatorname{Hom}_A(N,-)$$。

**单位**：对每个 $$M$$，定义

$$\eta_M:M\to \operatorname{Hom}_A(N,\ M\otimes_AN),\qquad \eta_M(m):=\big(n\mapsto m\otimes n\big).$$

$$\eta_M(m)$$ 落在 $$\operatorname{Hom}_A(N,M\otimes_AN)$$ 里：$$n\mapsto m\otimes n$$ 是 $$N\to M\otimes_AN$$ 的线性映射（张量积对第二变元线性）。$$\eta_M$$ 本身线性：$$(m+m')\otimes n=m\otimes n+m'\otimes n$$。

**余单位**：对每个 $$P$$，定义

$$\varepsilon_P:N\otimes_A\operatorname{Hom}_A(N,P)\to P,\qquad \varepsilon_P\big(n\otimes\varphi\big):=\varphi(n).$$

良定义：映射 $$(n,\varphi)\mapsto\varphi(n)$$ 是双线性的——对 $$n$$ 线性因为每个 $$\varphi$$ 线性，对 $$\varphi$$ 线性因为 $$\operatorname{Hom}$$ 上的加法与标量是逐点定义的（命题 3.17）；由定义 3.11 它唯一诱导出 $$\varepsilon_P$$。

**记号上的一点提醒**：这里把 $$\varepsilon_P$$ 的定义域写成 $$N\otimes_A\operatorname{Hom}_A(N,P)$$（$$N$$ 在左），而 $$F=-\otimes_AN$$ 按定义会把 $$N$$ 放在右边；两者只差命题 3.14(2) 那条交换同构 $$M\otimes N\cong N\otimes M$$，下面凡是把 $$m\otimes n$$ 与 $$n\otimes m$$ 互换书写的地方，都是在隐式使用这条交换同构，不再逐次注明。

**三角恒等式 (i)**：$$\varepsilon_{FM}\circ F\eta_M=\mathrm{id}_{FM}$$，其中 $$FM=M\otimes_AN$$。计算：$$F\eta_M=\mathrm{id}\otimes\eta_M$$ 把 $$m\otimes n$$ 送到 $$n\otimes\eta_M(m)$$；再作用 $$\varepsilon_{FM}$$：

$$n\otimes\eta_M(m)\ \longmapsto\ \eta_M(m)(n)=m\otimes n .$$

故复合是恒等。

**三角恒等式 (ii)**：$$G\varepsilon_P\circ\eta_{GP}=\mathrm{id}_{GP}$$，其中 $$GP=\operatorname{Hom}_A(N,P)$$。对 $$\varphi\in GP$$：$$\eta_{GP}(\varphi)\in\operatorname{Hom}_A(N,\ N\otimes\operatorname{Hom}(N,P))$$，$$\eta_{GP}(\varphi)(n)=n\otimes\varphi$$；再作用 $$G\varepsilon_P$$（即后复合 $$\varepsilon_P$$）：

$$\big(G\varepsilon_P(\eta_{GP}(\varphi))\big)(n)=\varepsilon_P(n\otimes\varphi)=\varphi(n)\qquad\text{对一切 }n .$$

故复合是恒等。

**与第 66 章的关系**：伴随函子有两种等价定义——**Hom 集判据**（定理 3.21：自然同构 $$\operatorname{Hom}(FM,P)\cong\operatorname{Hom}(M,GP)$$）与**单位–余单位判据**（存在 $$\eta,\varepsilon$$ 满足上述两条三角恒等式）。本章给出了前者的完整验证，而本题给出后者的完整验证：**同一个伴随的两副面孔**。第 66 章会把这两副面孔的等价性作为定理证出来，并用它推出「左伴随保余极限、右伴随保极限」。**这就是第 66 章的起点。**$$\blacksquare$$

**解 研2.** **命题 A**：$$\operatorname{Hom}_A(A,-)\cong\mathrm{id}_{A\text{-}\mathbf{Mod}}$$，自然同构。构造

$$\theta_M:\operatorname{Hom}_A(A,M)\to M,\qquad \theta_M(\varphi):=\varphi(1).$$

**逆**：$$\theta_M^{-1}(m):=\big(a\mapsto am\big)$$。**互逆**：$$\theta_M^{-1}(\theta_M(\varphi))$$ 是映射 $$a\mapsto a\,\varphi(1)=\varphi(a)$$（用了 $$\varphi$$ 的 $$A$$-线性），即 $$\varphi$$ 本身；$$\theta_M(\theta_M^{-1}(m))=1\cdot m=m$$。**自然性**：对 $$g:M\to P$$，$$\theta_P\big(\operatorname{Hom}(A,g)(\varphi)\big)=\theta_P(g\circ\varphi)=g(\varphi(1))=g\big(\theta_M(\varphi)\big)$$。故 $$\theta$$ 是自然同构。

**命题 B**：若 $$\alpha:\operatorname{Hom}_A(P,-)\Rightarrow\operatorname{Hom}_A(Q,-)$$ 是自然同构，则 $$P\cong Q$$。记 $$\beta:=\alpha^{-1}$$，并定义

$$f:=\alpha_P(\mathrm{id}_P)\in\operatorname{Hom}_A(Q,P),\qquad g:=\beta_Q(\mathrm{id}_Q)\in\operatorname{Hom}_A(P,Q).$$

**断言 $$g\circ f=\mathrm{id}_Q$$。** 在映射 $$g:P\to Q$$ 处写下 $$\alpha$$ 的自然性方块。$$\operatorname{Hom}(P,-)$$ 在 $$g$$ 上取「后复合 $$g$$」，$$\operatorname{Hom}(Q,-)$$ 同理，方块为

$$\alpha_Q\circ\operatorname{Hom}(P,g)=\operatorname{Hom}(Q,g)\circ\alpha_P .$$

代入 $$u=\mathrm{id}_P\in\operatorname{Hom}(P,P)$$：左端是 $$\alpha_Q\big(g\circ\mathrm{id}_P\big)=\alpha_Q(g)$$；右端是 $$g\circ\alpha_P(\mathrm{id}_P)=g\circ f$$。故

$$\alpha_Q(g)=g\circ f .$$

但 $$g=\beta_Q(\mathrm{id}_Q)$$，而 $$\alpha_Q\circ\beta_Q=\mathrm{id}$$，故 $$\alpha_Q(g)=\mathrm{id}_Q$$。于是 $$g\circ f=\mathrm{id}_Q$$。
**对称地**（交换 $$P,Q$$ 与 $$\alpha,\beta$$ 的角色，结论与推导逐字对应）得 $$f\circ g=\mathrm{id}_P$$。故 $$P\cong Q$$。（反向蕴含是平凡的：同构 $$\phi:P\to Q$$ 给出自然同构 $$\operatorname{Hom}(Q,-)\Rightarrow\operatorname{Hom}(P,-)$$，取逆即可。）

**与投射性的关系**：由定理 3.23(3)，$$P$$ 投射 $$\iff$$ 函子 $$\operatorname{Hom}_A(P,-)$$ 保满射。所以「投射性」是**函子的属性**，而命题 B 又说明这个函子反过来**完全决定了 $$P$$**。两件事合起来就是那句话：**一个对象完全由它与所有其它对象的态射决定**——它在这里第一次变成可计算的命题。第 66 章会把它升级成 **Yoneda 引理** $$\operatorname{Nat}\big(\operatorname{Hom}_A(C,-),F\big)\cong F(C)$$，并由此得到 Yoneda 嵌入与可表函子理论。**这正是第 66 章「伴随函子与 Yoneda 引理」的起点。**$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**（一）模是环上的向量空间，但「除以标量」这条腿断了。** 记住三个等式：$${\mathbb{Z}}\text{-}\mathbf{Mod}=\mathbf{Ab}$$（例 3.1(i)）、$$k[x]$$-模 = 「$$k$$-向量空间 + 一个线性算子」（例 3.1(ii)）、$$A$$-模的子模 = $$k[x]$$ 情形下的「不变子空间」。凡是线性代数证明里出现「解出 $$m=\frac ba$$」的地方，到模上都要重审。**第 16–19 章的谱理论，就是 $$k[x]$$-模结构定理的物理版本**（问题 4）。

**（二）张量积的定义原封不动，计算方式全部作废。** 定义 3.11 与第 22 章定义 3.4 逐字相同——万有性质是「升级」中唯一活下来的东西。而死掉的是第 22 章定理 3.7：模可能没有基，且 $$m\otimes n$$ 可以是 0（$$m,n\ne0$$）。它的替代品是**正合性**（定理 3.15）与万有性质的直接运用（第五节问题 1、3）。**这条从「有基」到「有正合列」的转移，是整个同调代数的动机。**

**（三）$$\operatorname{Hom}$$ 的两种变性是同一件事的两面。** $$\operatorname{Hom}_A(M,-)$$ 协变（后复合），$$\operatorname{Hom}_A(-,N)$$ 反变（前复合，且把复合的原序颠倒）。第 06 章的「对偶 = 反变」就是反变那一支取 $$N=k$$ 的情形，转置映射 $$T^{\mathsf T}$$ 就是它在态射上的作用（注 3.18）。**「反变」不是记号问题，它是「箭头掉头」这件事本身。**

**（四）张量–Hom 伴随把两个「半截定理」缝成一条。** $$-\otimes_AM\dashv\operatorname{Hom}_A(M,-)$$（定理 3.21）。张量只保右正合、Hom 只保左正合，看起来是两个孤立的技术事实；到第 66 章它们会合并成一条定理：**左伴随保余极限、右伴随保极限。** 入口题 (d) 的「对称的数、不对称的性」由此彻底解答（注 3.21）。

**（五）自由与投射只在基环足够复杂时才分开。** 在 $$\mathbb{Z}$$ 上，有限生成投射模就是自由模（竞赛 5）；分开它们的最小例子是 $$\mathbb{Z}/6$$ 上的 $$\mathbb{Z}/2$$（例 3.23）。几何上这正是「向量丛是否平凡」——**Serre–Swan 对应是本章通往代数几何的正门**（注 3.23）。

**下一章的悬念。** 本章给出了一个伴随对的完整验证（定理 3.21），但每次都要「构造 $$\Phi$$、构造 $$\Psi$$、验证互逆、验证自然性」四步。三个问题悬在那里：**伴随对为什么总是成对出现？「左伴随保余极限」为什么必然成立？「一个对象被它的 Hom 函子决定」（研究 2）能推到多一般？** 第 66 章用两条工具一并回答：**单位–余单位判据与 Yoneda 引理**。本章的每一条同构，都会在那一章获得统一的名字。

**延伸阅读。**
- Atiyah–MacDonald《Introduction to Commutative Algebra》第 2 章（模、张量积、正合序列）——本章的 $$\mathbb{Z}$$-模例子全部取自这一章的标准习题。
- Emily Riehl《Category Theory in Context》第 1–2 章（函子与自然变换、伴随）——第 66 章会用到的语言。
- Saunders Mac Lane《Categories for the Working Mathematician》第 IV 章（伴随）——三角恒等式的标准出处。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch63_模_张量积与Hom函子_上.md">← 第63章 模、张量积与 Hom 函子·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch65_伴随函子与Yoneda引理_上.md">第65章 伴随函子与Yoneda 引理·上 →</a></div>
</div>
