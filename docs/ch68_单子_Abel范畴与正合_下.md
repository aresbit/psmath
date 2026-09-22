---
layout: default
---

# 第68章: 单子、Abel 范畴与正合·下：完整推导 (Monads, Abelian Categories and Exactness · Part II: Full Derivation)

> 专家依据: `_experts/algebra/category-universal-properties.md` + `_experts/algebra/homological-algebra.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）
> 配套预备: 见 第67章 单子、Abel 范畴与正合·上（同一主题的具体铺垫，建议先读）

## 一、本章概要 (Overview)

读完第67章的具体例子后——你已经在 $$\mathbb R^2$$、$$\mathbb R^3$$ 上手算过核、双积、像与余像、连接同态与单子的单位/结合律——这里把同样的构造写成一般定义，并给出完整证明。

第 09、10、14 章一直在做同一件事：取一个映射的核，再取前一个映射的像，然后把像塞进核里做商。第 18 章算出 $$\partial^2=0$$，于是 $$\operatorname{im}\partial_{k+1}$$ 落在 $$\ker\partial_k$$ 里，商才有意义；第 20 章把它命名为同调群 $$H_k=\ker\partial_k/\operatorname{im}\partial_{k+1}$$；第 28 章换成分形式，得到 $$H^k_{dR}=\ker d_k/\operatorname{im}d_{k-1}$$。当时每一步都靠"分母确实是分子的子对象"这一句具体验证撑着。**本章要问的是：这些验证里，哪一部分是结构上必然的、哪一部分才是真正携带信息的量；把"必然的那一部分"抽出来当成公理，会得到什么。**

这条路从第 31–33 章来：那里我们备齐了范畴、函子、自然变换、极限与余极限、伴随与 Yoneda，但它们到此为止还只是语言。本章是这些语言第一次**真的开始算东西**——算出来的第一个对象叫**正合 (exact)**。三条主线：正合序列、**阿贝尔范畴 (abelian category)**（让核、像、商都自动有意义的公理系统）、**单子 (monad)**（伴随的"影子"，把自由构造与约束折叠分开）。

到哪去：第 70 章讲导出函子，它会给"同调为什么必然存在"一个统一的答案；本章是那一步的全部预备。

## 二、入口：一道具体的问题 (Entry Problem)

> 题源：自编，取材 MP120（原专栏正是用两个正交投影算子引出"二次复合为零"）。

设 $$\mathcal H$$ 是 $$n$$ 维 $$\mathbb{C}$$-向量空间，$$P_1,P_2\in\operatorname{End}(\mathcal H)$$ 是两个**正交投影算子 (orthogonal projection)**：$$P_i^2=P_i$$ 且 $$P_i^\ast=P_i$$；又设二者**正交**，即 $$\operatorname{im}P_1\perp\operatorname{im}P_2$$。考虑态射序列

$$\mathcal H\xrightarrow{\ P_1\ }\mathcal H\xrightarrow{\ P_2\ }\mathcal H .$$

**(1)** 证明 $$P_2\circ P_1=0$$。这一步只用"投影"与"正交"四个字。

**(2)** 现在**只假设** $$P_2\circ P_1=0$$。定义

$$H:=\ker P_2\big/\operatorname{im}P_1 .$$

证明这个商确实有意义（分母是分子的子空间），并把 $$\dim H$$ 用 $$P_1,P_2$$ 的数据写出来。

**(3)** 问：几何上什么条件保证 $$H=0$$？把 (2) 的结果翻译成一句关于 $$P_1,P_2$$ 的话。然后回答：**这句话为什么值得单独起一个名字？**（先别急着叫它"正合"；试着说清，"命名"在这里究竟标记了什么。）

**(4)** 把 (2) 里的商 $$H$$ 与第 20 章的 $$H_k=\ker\partial_k/\operatorname{im}\partial_{k+1}$$ 摆在一起看：它们是同一种构造吗？如果是，为什么第 20 章要花力气去验证 $$\operatorname{im}\partial_{k+1}\subseteq\ker\partial_k$$，而这里 $$H$$ 的存在却是"自动的"？

这道题是整章的引子：**(1) 是"复形"、(2) 是"同调"、(3) 是"正合"、(4) 是"阿贝尔范畴"**——本章的四个主角。现在只给题，不给定义；(3) 的"命名"问题与 (4) 的"自动性"问题，到 3.3、3.4 节才会被正面回答。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 零对象、零态射与核

入口题 (1)(2) 用到的"$$P_2\circ P_1=0$$"与"$$\ker P_2$$"，在 $$\mathbf{Ab}$$、$$\mathbf{Vect}$$ 之类具体范畴里唾手可得：零同态、子空间都摸得到元素。要在**没有元素**的一般范畴里说同样的话，第一步必须先把"零"这个对象本身、以及"两个态射复合为零"这句话，用万有性质重新说一遍——否则"$$f\circ k=0$$"根本无从谈起。

**定义 3.1（零对象与零态射, zero object and zero morphism）** 范畴 $$\mathcal C$$ 中的对象 $$0$$ 称为**零对象**，若它同时是**始对象**（对每个 $$X$$ 恰有一个态射 $$0\to X$$）与**终对象**（对每个 $$X$$ 恰有一个态射 $$X\to 0$$）。此时对任意 $$A,B$$，把复合
$$A\to 0\to B$$
记作 $$0_{A,B}$$，称**零态射 (zero morphism)**。

**注 3.1（零态射不依赖任何选择）** 因为 $$A\to 0$$ 与 $$0\to B$$ 各自唯一，$$0_{A,B}$$ 是**唯一确定**的态射，而不是"某一个"态射。并且对任意 $$f:A'\to A$$、$$g:B\to B'$$，
$$g\circ 0_{A,B}=0_{A,B'}=0_{A,B}\circ f ,$$
左边等号是因为 $$A'\to 0$$ 唯一（两个复合都是 $$A'\to 0\to B'$$），右边同理。这条小性质在后面反复用：**零态射吸收一切复合**。

**定义 3.2（核与余核, kernel and cokernel）** 设 $$f:A\to B$$。$$f$$ 的**核 (kernel)** 是等化子 $$\ker f:=\operatorname{eq}(f,\,0_{A,B})$$：一个对象 $$K$$ 连同态射 $$k:K\to A$$，满足 $$f\circ k=0$$，且**万有**——对任何满足 $$f\circ u=0$$ 的态射 $$u:X\to A$$，存在**唯一** $$\bar u:X\to K$$ 使 $$k\circ\bar u=u$$。对偶地，$$f$$ 的**余核 (cokernel)** 是余等化子 $$\operatorname{coker}f:=\operatorname{coeq}(f,\,0_{A,B})$$：对象 $$C$$ 连同态射 $$\pi:B\to C$$，满足 $$\pi\circ f=0$$ 且万有——任何满足 $$v\circ f=0$$ 的 $$v:B\to Y$$ 唯一地穿过 $$\pi$$。

**定理 3.3（核是单态射，余核是满态射）** 若 $$k=\ker f$$，则 $$k$$ 是单态射；若 $$\pi=\operatorname{coker}f$$，则 $$\pi$$ 是满态射。

*证明思路*：单态射的定义是"左可消"。核只有一条万有性质，而这条性质里带着"存在**唯一**"四个字——**唯一性恰好是用来消灭两个候选的**。所以把两个候选塞进同一条万有性质，让唯一性收尾。这是范畴论里最常用的证明模式。

*证明*：设 $$u,v:X\to K$$ 满足 $$k\circ u=k\circ v$$。记 $$h:=k\circ u$$。则
$$f\circ h=f\circ k\circ u=0\circ u=0,$$
即 $$h$$ 是满足"与 $$f$$ 复合为零"的态射 $$X\to A$$。由核的万有性质，存在**唯一**的 $$\bar h:X\to K$$ 使 $$k\circ\bar h=h$$。现在 $$u$$ 与 $$v$$ 都满足 $$k\circ u=k\circ v=h$$，故二者都是合法的 $$\bar h$$；由唯一性 $$u=v$$。于是 $$k$$ 左可消，是单态射。余核的情形把一切箭头反向（满态射即右可消），逐字对偶。$$\blacksquare$$

**例 3.3（$$\mathbf{Ab}$$ 与 $$R\text{-}\mathbf{Mod}$$ 中的核与余核）** 取 $$\mathcal C=\mathbf{Ab}$$ 或 $$R\text{-}\mathbf{Mod}$$。
- 零对象是平凡群 $$0=\{0\}$$（在 $$\mathbf{Ab}$$ 中同构意义下只有一个），零态射就是零同态。
- $$\ker f=\{a\in A:f(a)=0\}$$，配以含入 $$k:\ker f\hookrightarrow A$$。验证万有性质：若 $$f\circ u=0$$，则 $$u$$ 的像整体落在 $$\ker f$$ 内，故 $$u$$ 唯一地穿过含入——所谓"唯一"，就是每个元素必须映到它自己。
- $$\operatorname{coker}f=B/\operatorname{im}f$$，配以商映射 $$\pi:B\to B/\operatorname{im}f$$。验证：若 $$v\circ f=0$$，则 $$\operatorname{im}f\subseteq\ker v$$，而 $$\ker v$$ 是 $$B$$ 的子群，故 $$v$$ 在 $$\operatorname{im}f$$ 上取零、可以下降到商上，且下降后的同态唯一。

**注 3.3（「$$\ker$$ 的像 = 核」为什么值得起个名字）** 现在回答入口题 (3)。在 $$\mathbf{Ab}$$ 中，对 $$A\xrightarrow{f}B\xrightarrow{g}C$$，若 $$g\circ f=0$$，则
$$\operatorname{im}f\subseteq\ker g$$
是**自动的**：$$f$$ 值域里的每个元素都被 $$g$$ 杀掉，这是 $$g\circ f=0$$ 的逐字翻译。而
$$\operatorname{im}f=\ker g$$
不是自动的——它是一个**条件**。两者的差别在于：包含式说"$$g$$ 至少杀掉了 $$f$$ 造出的全部东西"，等号说"$$g$$ 没有多杀任何东西"。多杀掉的那部分，正好就是商 $$\ker g/\operatorname{im}f$$。

命名的逻辑是这样的：一个条件如果**永远成立**，不值得命名；如果它**几乎总不成立、但成立时整个结构就退化**，那它值得命名。正合属于后者——它成立时商为零、复形同调为零、序列"不携带信息"。于是这个名字真正的用途在它的**反面**：一旦你会说"这里不正合"，你就必须有一个量来度量"差多少"，那个量就是同调。**"正合"这个词是为"不正合"准备的。** 这句话在 3.5 节被精确兑现（定理 3.14：正合 $$\iff$$ 同调全为零）。

### 3.2 加性范畴与双积

定理 3.6 的证明要用到"两个态射相加"（$$i_Ap_A+i_Bp_B$$）——这在 $$\mathbf{Set}$$ 之类范畴里毫无意义（两个函数不能相加）。要让"直和的积角色与余积角色重合"这句话（第67章定理 3.4 在具体空间里验证过）在一般范畴里成立，必须先补上"态射能相加"这条结构，这就是加性范畴的由来。

**定义 3.4（预加性范畴, preadditive category）** 范畴 $$\mathcal C$$ 称**预加性**，若每个态射集 $$\operatorname{Hom}(A,B)$$ 上给定一个 Abel 群结构，且复合对两个变量都 $$\mathbb{Z}$$-双线性：
$$(g_1+g_2)\circ f=g_1\circ f+g_2\circ f,\qquad g\circ(f_1+f_2)=g\circ f_1+g\circ f_2 .$$
两项都要：复合是每个变量各自的函子，只对一边线性是不够的。

**定义 3.5（加性范畴与加性函子, additive category and additive functor）** 预加性范畴 $$\mathcal C$$ 若还满足 (i) 有零对象；(ii) 任意两个对象既有积又有余积，则称**加性范畴 (additive category)**。加性范畴之间的函子 $$F:\mathcal C\to\mathcal D$$ 若在每个 Hom 集上诱导群同态（等价地：保持零态射、保持加法），称**加性函子 (additive functor)**。

**定理 3.6（加性范畴中有限积 = 有限余积）** 在加性范畴中，对任意 $$A,B$$，积 $$A\times B$$ 与余积 $$A\sqcup B$$ 存在且**典范同构**；这个共同的对象记作 $$A\oplus B$$，称**双积 (biproduct)**。

*证明思路*：在同一对对象上，"积"与"余积"各由一条万有性质刻画。加性结构的用处是：从 $$A\times B$$ 到 $$A\sqcup B$$ 这种"混合方向"的映射，可以用加法和复合拼出来（$$i_A\circ p_A+i_B\circ p_B$$）。把态射按 $$2\times2$$ 表格排开，两条万有性质就变成矩阵运算。

*证明*：设 $$(A\times B,\,p_A,p_B)$$ 是积，$$(A\sqcup B,\,i_A,i_B)$$ 是余积。
① 造 $$\varphi:A\sqcup B\to A\times B$$：由积的万有性质，给出到 $$A\times B$$ 的态射等价于给出一对到 $$A$$、到 $$B$$ 的态射。这两个态射由余积的万有性质指定：
$$p_A\circ\varphi\circ i_A=1_A,\quad p_A\circ\varphi\circ i_B=0,\qquad p_B\circ\varphi\circ i_A=0,\quad p_B\circ\varphi\circ i_B=1_B .$$
用矩阵写法即 $$\varphi$$ 对应 $$\begin{pmatrix}1_A&0\\0&1_B\end{pmatrix}$$。
② 造 $$\psi:A\times B\to A\sqcup B$$：用加性结构令 $$\psi:=i_A\circ p_A+i_B\circ p_B$$。
③ 算 $$\psi\circ\varphi$$：余积的万有性质说，态射 $$A\sqcup B\to A\sqcup B$$ 由它作用在两个含入上的像唯一决定。于是
$$(\psi\circ\varphi)\circ i_A=\psi\circ(\varphi\circ i_A)=(i_A p_A+i_B p_B)\circ(1_A,0)=i_A\circ 1_A+i_B\circ 0=i_A ,$$
同法 $$(\psi\circ\varphi)\circ i_B=i_B$$。故 $$\psi\circ\varphi=1_{A\sqcup B}$$。（这里用了双线性把和拆开，以及注 3.1 的零态射吸收性。）
④ 算 $$\varphi\circ\psi$$：积的万有性质说，态射 $$A\times B\to A\times B$$ 由两个投影的复合唯一决定。于是
$$p_A\circ(\varphi\circ\psi)=(p_A\circ\varphi)\circ\psi=(p_A\circ\varphi)\circ(i_A p_A+i_B p_B)=1_A\circ p_A+0=p_A ,$$
同法 $$p_B\circ\varphi\circ\psi=p_B$$。故 $$\varphi\circ\psi=1_{A\times B}$$。
由 ③④，$$\varphi$$ 是同构。$$\blacksquare$$

**注 3.6** 定理 3.6 是"加性"一词的全部内容：它保证有限积与有限余积不再分家，统一直和 $$\oplus$$。在 $$\mathbf{Ab}$$、$$R\text{-}\mathbf{Mod}$$、$$\mathbf{Vect}_k$$ 中，这个 $$\oplus$$ 就是熟悉的对象层面的直和；而在一般范畴（如 $$\mathbf{Set}$$）里，积（笛卡尔积）与余积（不相交并）是完全不同的东西——这正是 $$\mathbf{Set}$$ 不是加性范畴的原因。

### 3.3 阿贝尔范畴：像与余像

第67章定理 3.6 在 $$\operatorname{coim}u\cong\operatorname{im}u$$ 这件事上用的是"能摸到元素"这个作弊手段。要在一般范畴里说清"子空间的核描述"与"商空间的余核描述"给出同一个对象，需要恰好三条公理：一条保证核、余核总存在（否则连"像""余像"都写不出来），另外两条保证"单态射自己就是像""满态射自己就是余像"——这两条不是随便加的，它们正是让下面的定理 3.9 成立所需要的**最少**假设。

**定义 3.7（阿贝尔范畴, abelian category）** 加性范畴 $$\mathcal A$$ 称**阿贝尔范畴**，若
(A1) 每个态射都有核与余核；
(A2) 每个单态射 $$m:M\to A$$ 都是它自己的余核的核，即 $$m\cong\ker(\operatorname{coker}m)$$；
(A3) 每个满态射 $$e:A\to E$$ 都是它自己的核的余核，即 $$e\cong\operatorname{coker}(\ker e)$$。

**定义 3.8（像与余像, image and coimage）** 对态射 $$u:A\to B$$，定义
$$\operatorname{Im}u:=\ker\bigl(\operatorname{coker}u\bigr),\qquad \operatorname{Coim}u:=\operatorname{coker}\bigl(\ker u\bigr).$$
具体地：若 $$c:B\to\operatorname{Coker}u$$ 是余核，则 $$\operatorname{Im}u=\ker c$$ 配含入 $$m:\operatorname{Im}u\to B$$；若 $$k:\ker u\to A$$ 是核，则 $$\operatorname{Coim}u=\operatorname{coker}k$$ 配满态射 $$q:A\to\operatorname{Coim}u$$。注意 (A2)(A3) 说：**单态射就是它自己的像，满态射就是它自己的余像。**

**定理 3.9（满-单分解与 $$\operatorname{Coim}\cong\operatorname{Im}$$）** 在阿贝尔范畴中，每个态射 $$u:A\to B$$ 都有分解
$$u=m\circ\bar u\circ q,\qquad A\xrightarrow{\ q\ }\operatorname{Coim}u\xrightarrow{\ \bar u\ }\operatorname{Im}u\xrightarrow{\ m\ }B ,$$
其中 $$q$$ 满、$$m$$ 单，且**典范态射 $$\bar u$$ 是同构**。于是"像"与"余像"在阿贝尔范畴里是同一个对象。

*证明思路*：先用"$$u$$ 杀掉 $$\ker u$$"穿过余核造出 $$\bar u$$；再说明 $$\bar u$$ 满、单。下面在 $$R\text{-}\mathbf{Mod}$$ 中把元素写出来——这正是本章实际要用的情形；一般阿贝尔范畴里 (A2)(A3) 保证同样的论证在"广义元素"（即态射 $$X\to\cdot$$）层面逐句成立。

*证明（$$R\text{-}\mathbf{Mod}$$ 情形）*：记 $$k=\ker u$$（含入），$$q=\operatorname{coker}k$$（商映射 $$A\to A/k(A)$$），$$c=\operatorname{coker}u$$（商映射 $$B\to B/u(A)$$），$$m=\ker c$$（含入 $$\operatorname{Im}u=u(A)\hookrightarrow B$$，因为 $$c$$ 的核恰是 $$u(A)$$）。
① 造 $$\bar u$$：由 $$u\circ k=0$$，同态 $$u$$ 在 $$k(A)$$ 上取零，故唯一地下降为 $$\tilde u:A/k(A)\to B$$，满足 $$\tilde u\circ q=u$$。
② 降入像：$$c\circ\tilde u\circ q=c\circ u=0$$，而 $$q$$ 是满同态，故 $$c\circ\tilde u=0$$。于是 $$\tilde u$$ 的像落在 $$\ker c=u(A)$$ 内，给出唯一的 $$\bar u:A/k(A)\to u(A)$$ 使 $$m\circ\bar u=\tilde u$$。合起来 $$m\circ\bar u\circ q=\tilde u\circ q=u$$。
③ $$\bar u$$ 满：任取 $$y\in\operatorname{Im}u=u(A)$$，则 $$y=u(a)=\tilde u(q(a))$$ 对某个 $$a$$，故 $$y=\bar u(q(a))$$。
④ $$\bar u$$ 单：设 $$\bar u(x)=0$$，写 $$x=q(a)$$。则 $$u(a)=m\bar uq(a)=m(0)=0$$，即 $$a\in k(A)$$，于是 $$x=q(a)=0$$。
由 ③④，$$\bar u$$ 是同构。$$\blacksquare$$

**例 3.9（阿贝尔范畴与非阿贝尔范畴）** 阿贝尔范畴：$$\mathbf{Ab}$$（即 $$\mathbb{Z}\text{-}\mathbf{Mod}$$）、$$R\text{-}\mathbf{Mod}$$、$$\mathbf{Vect}_k$$、有限生成 $$R$$-模范畴（$$R$$ Noether 时）、以及第 72 章要用的层范畴 $$\mathbf{Sh}(X;\mathbf{Ab})$$（核逐点取，余核取预层余核后再层化，公理逐条成立）。
**不是**阿贝尔范畴的：$$\mathbf{Set}$$、$$\mathbf{Top}$$（态射集上没有群结构，连加性都不满足）；$$\mathbf{Ring}$$（环同态不能相减，Hom 集不是 Abel 群）；$$\mathbf{Grp}$$（Hom 集上没有群结构，且 (A2) 失效——竞 4 给出一个单态射不是核的具体例子）。

**注 3.9（公理 (A2)(A3) 在干什么，以及入口题 (4) 的答案）** 定理 3.9 的证明用到 (A2)(A3) 才把 $$\operatorname{Coim}u$$ 与 $$\operatorname{Im}u$$ 认成同一个东西。这件事的意义是：**"像"与"核"来自两个不同的构造（一个用余核造、一个本身是核），要让"$$\operatorname{im}f=\ker g$$"这句话里的等号有意义，必须先有定理 3.9 把它们放进同一个世界里。** 没有 (A2)(A3)，这句话左右两边甚至不在同一层。

回到入口题 (4)。第 20 章必须验证 $$\operatorname{im}\partial_{k+1}\subseteq\ker\partial_k$$，是因为在那里"商"是在群论里手工作的，分母必须是子群。而在阿贝尔范畴里，$$H_n$$ 被**定义**为余核
$$H_n=\operatorname{Coker}\bigl(\operatorname{Im}d_{n+1}\hookrightarrow\operatorname{Ker}d_n\bigr),$$
公理 (A1) 保证这个余核**总是存在**。至于那个含入态射从何而来：它存在**当且仅当** $$\operatorname{Im}d_{n+1}\subseteq\operatorname{Ker}d_n$$，而这条件正是复形的定义 $$d^2=0$$（定义 3.12）。所以两件事是同一件事的两种说法：**第 20 章花力气验证的包含式，在这里被吸收进了"复形"这个定义本身**；从此以后写 $$H_n$$ 不必再验任何东西。

### 3.4 正合序列

**定义 3.10（正合列、短正合列, exact sequence, short exact sequence）** 阿贝尔范畴中的序列
$$A\xrightarrow{\ f\ }B\xrightarrow{\ g\ }C$$
称在 $$B$$ 处**正合 (exact)**，若 $$\operatorname{Im}f=\operatorname{Ker}g$$（等号在 $$\operatorname{Im}f$$ 与 $$\operatorname{Ker}g$$ 都被认成 $$B$$ 的子对象的意义下取，合法性来自定理 3.9）。处处正合的序列称**正合序列**。形如
$$0\to A\xrightarrow{\ f\ }B\xrightarrow{\ g\ }C\to 0$$
的正合序列称**短正合列 (short exact sequence)**。

**定理 3.11（正合性的三个基本刻画）** 在阿贝尔范畴中：
(i) $$0\to A\xrightarrow{f}B$$ 正合 $$\iff$$ $$f$$ 是单态射；
(ii) $$B\xrightarrow{g}C\to 0$$ 正合 $$\iff$$ $$g$$ 是满态射；
(iii) $$0\to A\xrightarrow{f}B\xrightarrow{g}C\to 0$$ 正合 $$\iff$$ $$f$$ 单、$$g$$ 满、$$\operatorname{Im}f=\operatorname{Ker}g$$；此时
$$\operatorname{Ker}g\cong A,\qquad \operatorname{Coker}f\cong C .$$

*证明*：(i) 在 $$A$$ 处正合意味着 $$\operatorname{Im}(0\to A)=\operatorname{Ker}f$$。而 $$0\to A$$ 的余核是 $$A$$ 本身（$$\operatorname{id}_A$$ 满足万有性质），故 $$\operatorname{Im}(0\to A)=\operatorname{Ker}(\operatorname{id}_A)=0$$。于是正合 $$\iff$$ $$\operatorname{Ker}f=0$$ $$\iff$$ $$f$$ 单态射（核为零当且仅当左可消：若 $$f\circ s=f\circ t$$ 则 $$f\circ(s-t)=0$$，$$s-t$$ 穿过 $$0$$ 故 $$s=t$$；反之若 $$f$$ 单，任何穿过 $$\ker f$$ 的态射复合 $$f$$ 为零、又单，故它为零）。
(ii) 把 (i) 的一切箭头反向，得到 $$\operatorname{Coker}(C\to 0)$$ 的讨论，结论是 $$g$$ 满态射。
(iii) 设正合。则 $$f$$ 单、$$g$$ 满分别由 (i)(ii)；而 $$\operatorname{Im}f=\operatorname{Ker}g$$ 就是在 $$B$$ 处正合。又由 (A3)（$$g$$ 满）与 (A2)，$$g=\operatorname{coker}(\ker g)=\operatorname{coker}(\operatorname{Im}f)=\operatorname{coker}f$$，最后一步用了"$$f$$ 与它的像含入只差一个满态射，故余核相同"（$$f=q'\circ\text{(像含入)}$$，其中 $$q'$$ 是 $$A\to A/\ker f$$，为满态射）。于是 $$\operatorname{Coker}f\cong C$$。$$\operatorname{Ker}g\cong A$$ 对偶。反向：$$\operatorname{Im}f=\operatorname{Ker}g$$ 是定义，其余两项由 (i)(ii)。$$\blacksquare$$

**例 3.11** 取 $$\mathcal A=\mathbf{Ab}$$，$$m\ge1$$：
$$0\to\mathbb{Z}\xrightarrow{\ \times m\ }\mathbb{Z}\xrightarrow{\ \bmod m\ }\mathbb{Z}/m\to 0$$
是短正合列：$$\times m$$ 单、$$\bmod m$$ 满、$$\operatorname{Im}(\times m)=m\mathbb{Z}=\operatorname{Ker}(\bmod m)$$。且 $$\mathbb{Z}/m=\operatorname{coker}(\times m)$$，正是定理 3.11(iii)。这个例子在 5.5 与练习里会被反复用作"最容易手算的正合列"。

### 3.5 复形、同调与蛇引理

第67章例 3.4 手算过"$$\operatorname{im}f\subseteq\ker g$$"成立与不成立两种情形——成立时商 $$\ker g/\operatorname{im}f$$ 才有意义。把这件事从"一步"推广到"一串"映射，就是复形：每一步的像都落进下一步的核，这样才能在每个位置都合法地取商。$$d^2=0$$ 这条条件不是随便写的，它恰好就是"处处都能取商"这件事的最省记号。

**定义 3.12（复形与链映射, complex and chain map）** 阿贝尔范畴 $$\mathcal A$$ 中的**（链）复形 (chain complex)** $$C_\bullet$$ 是一族对象 $$C_n$$（$$n\in\mathbb Z$$）连同**微分 (differential)** $$d_n:C_n\to C_{n-1}$$，满足
$$d_{n-1}\circ d_n=0\qquad\bigl(\text{等价地}\ \operatorname{Im}d_{n+1}\subseteq\operatorname{Ker}d_n\bigr).$$
（等价性：$$d_{n-1}d_n=0$$ 当且仅当 $$d_n$$ 穿过 $$\ker d_{n-1}$$ 分解，即 $$\operatorname{Im}d_n\subseteq\operatorname{Ker}d_{n-1}$$。）复形之间的**链映射 (chain map)** $$f:C_\bullet\to D_\bullet$$ 是一族 $$f_n:C_n\to D_n$$ 满足 $$f_{n-1}\circ d^C_n=d^D_n\circ f_n$$。复形与链映射构成范畴 $$\mathbf{Ch}(\mathcal A)$$，它本身是阿贝尔范畴（核、余核逐分量取）。

**定义 3.13（同调, homology）**
$$H_n(C_\bullet):=\operatorname{Ker}d_n\big/\operatorname{Im}d_{n+1}=\operatorname{Coker}\!\bigl(\operatorname{Im}d_{n+1}\hookrightarrow\operatorname{Ker}d_n\bigr).$$
这里那个含入态射存在，正是因为 $$d^2=0$$（定义 3.12）；而 $$\mathcal A$$ 是阿贝尔范畴，故余核总是有定义的（注 3.9）。

**定理 3.14（正合 $$\iff$$ 同调为零；同调是函子）** 
(i) 复形 $$C_\bullet$$ 在 $$n$$ 处正合 $$\iff$$ $$H_n(C_\bullet)=0$$；
(ii) 链映射 $$f:C_\bullet\to D_\bullet$$ 诱导态射 $$H_n(f):H_n(C)\to H_n(D)$$，使 $$H_n:\mathbf{Ch}(\mathcal A)\to\mathcal A$$ 成为加性函子。

*证明*：(i) 记 $$\iota:\operatorname{Im}d_{n+1}\hookrightarrow\operatorname{Ker}d_n$$。由定理 3.11(ii)，$$H_n=\operatorname{Coker}\iota=0$$ $$\iff$$ $$\iota$$ 是满态射；又 $$\iota$$ 本身是单态射（定理 3.3），故满 $$\iff$$ 同构 $$\iff$$ $$\operatorname{Im}d_{n+1}=\operatorname{Ker}d_n$$，即"在 $$n$$ 处正合"。
(ii) 先看 $$f$$ 把该映的东西映到位：若 $$z\in\operatorname{Ker}d^C_n$$，则 $$d^D_n(f_n z)=f_{n-1}(d^C_n z)=0$$，故 $$f_n z\in\operatorname{Ker}d^D_n$$；若 $$y=d^C_{n+1}x$$，则 $$f_n y=d^D_{n+1}(f_{n+1}x)\in\operatorname{Im}d^D_{n+1}$$。于是 $$f_n$$ 分别限制为 $$\operatorname{Ker}d^C_n\to\operatorname{Ker}d^D_n$$ 与 $$\operatorname{Im}d^C_{n+1}\to\operatorname{Im}d^D_{n+1}$$，且这两个限制与含入态射交换，故由余核的万有性质诱导出 $$H_n(f)$$。恒同与复合逐分量成立，加性由 $$f_n$$ 的加性给出。$$\blacksquare$$

**例 3.14（第 09、10、14 章都是本章的特例）** 
- **第 18 章**：单纯复形 $$K$$ 的链群 $$C_q(K)$$（自由 Abel 群）连同边界算子 $$\partial_q$$。定理"$$\partial^2=0$$"就是定义 3.12 的 $$d^2=0$$；取 $$\mathcal A=\mathbf{Ab}$$，则 $$C_\bullet(K)$$ 是一个复形。那一章结尾强调"$$\partial^2=0$$ 是让 $$\ker\partial/\operatorname{im}\partial$$ 有定义的唯一理由"，正是定义 3.13 与注 3.9 的直觉版。
- **第 20 章**：$$H_k=\ker\partial_k/\operatorname{im}\partial_{k+1}$$ 就是定义 3.13。同调类是商里的元素，$$\partial^2=0$$ 则保证了余核有意义。
- **第 28 章**：de Rham 复形 $$(\Omega^\bullet(M),d)$$ 是 $$\mathcal A=\mathbf{Vect}_{\mathbb R}$$（或 $$\mathbf{Vect}_{\mathbb C}$$）里的**上链复形 (cochain complex)**——指标上升（$$d_k:\Omega^k\to\Omega^{k+1}$$）；把 $$k$$ 换成 $$-k$$ 就回到链复形的形状。$$H^k_{dR}=\ker d_k/\operatorname{im}d_{k-1}$$ 就是上同调。
- 于是"第 14 章的 $$d^2=0$$、第 18 章的 $$\partial^2=0$$、第 28 章的上同调"在同一句话里统一：**它们全都是阿贝尔范畴里的复形**；差别只在 $$\mathcal A$$ 取 $$\mathbf{Ab}$$ 还是 $$\mathbf{Vect}_{\mathbb R}$$，以及指标是升还是降。当年在单个群、单个向量空间上逐条验证的东西（像落在核里、商有意义、链映射诱导映射），现在由三条公理一次性包办。

**定理 3.15（蛇引理, snake lemma）** 设 $$\mathcal A$$ 阿贝尔，下图行正合且每个方块交换：
$$\begin{array}{ccccccc}
A & \xrightarrow{\ f\ } & B & \xrightarrow{\ g\ } & C & \xrightarrow{\ \ }\ & 0\\[4pt]
{\scriptstyle a}\big\downarrow & & {\scriptstyle b}\big\downarrow & & {\scriptstyle c}\big\downarrow & & \\[4pt]
0 & \xrightarrow{\ \ }\ & A' & \xrightarrow{\ f'\ } & B' & \xrightarrow{\ g'\ } & C'
\end{array}$$
则存在正合序列
$$\operatorname{Ker}a\xrightarrow{\ \bar f\ }\operatorname{Ker}b\xrightarrow{\ \bar g\ }\operatorname{Ker}c\xrightarrow{\ \delta\ }\operatorname{Coker}a\xrightarrow{\ \bar f'\ }\operatorname{Coker}b\xrightarrow{\ \bar g'\ }\operatorname{Coker}c ,$$
其中 $$\bar f,\bar g,\bar f',\bar g'$$ 是 $$f,g,f',g'$$ 限制/下降而来的态射，$$\delta$$ 称**连接同态 (connecting homomorphism)**。

*$$\delta$$ 的构造（追图）*：设 $$x\in\operatorname{Ker}c\subseteq C$$。
① **取原像**：由 $$g$$ 满（行正合 + 定理 3.11(ii)），选 $$y\in B$$ 使 $$g(y)=x$$；
② **推下去**：$$g'(b(y))=c(g(y))=c(x)=0$$，故 $$b(y)\in\operatorname{Ker}g'=\operatorname{Im}f'$$（行正合），选 $$z\in A'$$ 使 $$f'(z)=b(y)$$；
③ **落进余核**：令 $$\delta(x):=z+\operatorname{Im}a\ \in\ \operatorname{Coker}a=A'/\operatorname{Im}a$$。

*良定义性*：设换了另一组选择 $$y',z'$$。由 $$g(y-y')=0$$ 得 $$y-y'\in\operatorname{Ker}g=\operatorname{Im}f$$，即 $$y-y'=f(w)$$ 对某个 $$w\in A$$；于是
$$f'(z-z')=b(y-y')=b(f(w))=f'(a(w)),$$
而 $$f'$$ 单（行正合 + 定理 3.11(i)），故 $$z-z'=a(w)\in\operatorname{Im}a$$，即 $$z,z'$$ 在 $$\operatorname{Coker}a$$ 里是同一个类。若只换 $$z$$ 不换 $$y$$，则 $$f'(z-z')=0$$ 直接给出 $$z=z'$$。故 $$\delta$$ 与选择无关。正合性的完整验证放在 5.1。

**定理 3.16（长正合列, long exact sequence）** 设 $$0\to A_\bullet\xrightarrow{f}B_\bullet\xrightarrow{g}C_\bullet\to 0$$ 是 $$\mathbf{Ch}(\mathcal A)$$ 中的短正合列（即每个 $$n$$ 上 $$0\to A_n\to B_n\to C_n\to 0$$ 短正合，且三个映射是链映射）。则存在**长正合列**
$$\cdots\to H_{n+1}(C)\xrightarrow{\ \partial\ }H_n(A)\xrightarrow{H_n(f)}H_n(B)\xrightarrow{H_n(g)}H_n(C)\xrightarrow{\ \partial\ }H_{n-1}(A)\to\cdots$$

*证明*（$$R\text{-}\mathbf{Mod}$$ 情形，一般阿贝尔范畴逐句在"广义元素"层面成立）。先说明一个容易踩的坑，再给出正确构造：把定理 3.15 直接应用于
$$\begin{array}{c}
0\to A_n\to B_n\to C_n\to 0\\[3pt]
{\scriptstyle d^A_n}\big\downarrow\quad\ {\scriptstyle d^B_n}\big\downarrow\quad\ {\scriptstyle d^C_n}\big\downarrow\\[3pt]
0\to A_{n-1}\to B_{n-1}\to C_{n-1}\to 0
\end{array}$$
（两行正合、方块交换，因为 $$f,g$$ 是链映射）确实给出六项正合列
$$\operatorname{Ker}d^A_n\to\operatorname{Ker}d^B_n\to\operatorname{Ker}d^C_n\xrightarrow{\ \delta\ }\operatorname{Coker}d^A_n\to\operatorname{Coker}d^B_n\to\operatorname{Coker}d^C_n ,\tag{$$\ast$$}$$
但这**不是**定理要的序列：$$\operatorname{Ker}d^A_n$$ 只是 $$n$$ 层闭链 $$Z_n(A)$$，还没模掉边缘；$$\operatorname{Coker}d^A_n=A_{n-1}/\operatorname{Im}d^A_n$$ 是 $$A_{n-1}$$ 模掉边缘后的**全体**，比 $$H_{n-1}(A)=\operatorname{Ker}d^A_{n-1}/\operatorname{Im}d^A_n$$ 大得多——后者还要求元素落在 $$\operatorname{Ker}d^A_{n-1}$$ 里。例如取 $$A_2=\mathbb Z\xrightarrow{\times2}A_1=\mathbb Z\xrightarrow{\bmod2}A_0=\mathbb Z/2$$，则 $$\operatorname{Coker}(d_2^A)=\mathbb Z/2\mathbb Z\ne0=H_1(A)$$（$$H_1(A)=\operatorname{Ker}(\bmod2)/\operatorname{Im}(\times2)=2\mathbb Z/2\mathbb Z=0$$）：$$(\ast)$$ 里的 $$\operatorname{Coker}d_n^A$$ 与 $$H_{n-1}(A)$$ 是两个不同的对象，不能直接"抹掉一层"就互相等同。正确的构造要把"取核""取商"这两步**同时**做，具体如下。

设 $$[z]\in H_n(C)$$，代表元 $$z\in C_n$$ 满足 $$d_n^Cz=0$$。构造 $$\partial[z]\in H_{n-1}(A)$$，手法与定理 3.15 的 ①②③ 相同，只是这次从**闭链**出发，且要多验一步"象仍是闭链"：
① 由 $$g_n$$ 满，取 $$y\in B_n$$ 使 $$g_n(y)=z$$；
② $$g_{n-1}(d_n^By)=d_n^C(g_ny)=d_n^Cz=0$$（链映射交换性，加上 $$z$$ 是闭链），故 $$d_n^By\in\operatorname{Ker}g_{n-1}=\operatorname{Im}f_{n-1}$$（第 $$n-1$$ 层正合），取 $$w\in A_{n-1}$$ 使 $$f_{n-1}(w)=d_n^By$$；
③ **（这一步是 $$(\ast)$$ 的六项序列里没有、却是本定理成立的关键）** 验证 $$w$$ 本身是闭链：
$$f_{n-2}\bigl(d_{n-1}^Aw\bigr)=d_{n-1}^B\bigl(f_{n-1}w\bigr)=d_{n-1}^B\bigl(d_n^By\bigr)=\bigl(d_{n-1}^Bd_n^B\bigr)(y)=0,$$
第一步用左方块交换性 $$f_{n-2}d_{n-1}^A=d_{n-1}^Bf_{n-1}$$，第二步代入 $$w$$ 的定义，第三步用 $$B_\bullet$$ 是复形（$$d^2=0$$）。而 $$f_{n-2}$$ 单（第 $$n-2$$ 层正合），故 $$d_{n-1}^Aw=0$$，即 $$w\in\operatorname{Ker}d_{n-1}^A$$：这正是 $$(\ast)$$ 里被漏掉的限制，$$w$$ 不只是 $$A_{n-1}$$ 的任意元素，而确实落在闭链里，$$[w]\in H_{n-1}(A)$$ 才有意义。定义 $$\partial[z]:=[w]$$。

*良定义性*：与 ①② 中 $$y,w$$ 的选择无关，逐字同定理 3.15。再验证换一个闭链代表元 $$z'=z+d_{n+1}^Cc$$（$$c\in C_{n+1}$$）不改变结果：由 $$g_{n+1}$$ 满取 $$b\in B_{n+1}$$ 使 $$g_{n+1}b=c$$，则 $$y':=y+d_{n+1}^Bb$$ 满足 $$g_n(y')=g_n(y)+d_{n+1}^C(g_{n+1}b)=z+d_{n+1}^Cc=z'$$，是 $$z'$$ 的合法原像；而
$$d_n^By'=d_n^By+d_n^Bd_{n+1}^Bb=d_n^By+0=d_n^By$$
（用了 $$B_\bullet$$ 的复形条件），故按 ② 得到的 $$w'$$ 满足 $$f_{n-1}(w')=d_n^By'=d_n^By=f_{n-1}(w)$$，而 $$f_{n-1}$$ 单，故 $$w'=w$$ 逐字相等，$$[w']=[w]$$。于是 $$\partial:H_n(C)\to H_{n-1}(A)$$ 良定义。

*正合性*：在 $$H_n(A),H_n(B),H_n(C),H_{n-1}(A)$$ 四处的正合性，把问题 5.1 对 $$\delta$$ 的两段追图逐字重做一遍——把其中的元素换成同调类、把"$$=0$$"换成"是边缘"即可，此处不重复；每个 $$n$$ 上得到的六项 $$H_{n+1}(C)\to H_n(A)\to H_n(B)\to H_n(C)\xrightarrow{\partial}H_{n-1}(A)\to\cdots$$ 首尾相接，拼成定理中的无穷长正合列。$$\blacksquare$$

**注 3.16（$$(\ast)$$ 错在哪、为什么这处修正是必需的）** $$(\ast)$$ 本身作为一条正合列是**对**的——它只是回答了错误的问题。它比较的是"$$d_n$$ 的核"与"$$d_n$$ 的余核"，而同调比较的是"$$d_n$$ 的核"与"$$d_{n-1}$$ 的核模掉 $$d_n$$ 的像"，后者比前者多一层限制（$$w$$ 必须是闭链）。这层限制不是自动满足的：一般的 $$w\in A_{n-1}$$（满足 $$f_{n-1}(w)=d_n^By$$）未必有 $$d_{n-1}^Aw=0$$，③ 的验证恰恰是**用了 $$B_\bullet$$ 的复形条件 $$d^2=0$$** 才把它保证下来。跳过这一步、直接把 $$\operatorname{Coker}d_n^A$$ 说成 $$H_{n-1}(A)$$，正是"一个等式看似显然、实则悄悄用掉一条没写出来的前提"的典型例子——这也是第67章反复强调"先手算、再抽象"的原因：具体例子（如上面 $$\times2,\bmod2$$ 的例子）能立刻把这种大小不一致的错误暴露出来。

### 3.6 单子

**定义 3.17（自函子范畴）** 记 $$\mathbf{End}_{\mathcal C}:=[\mathcal C,\mathcal C]$$：对象是自函子 $$T:\mathcal C\to\mathcal C$$，态射是自然变换 $$\alpha:T\Rightarrow T'$$；复合是自然变换的复合，恒同是 $$1_{\mathcal C}$$。函子复合 $$\circ$$（严格结合）给 $$\mathbf{End}_{\mathcal C}$$ 一个**严格幺半范畴 (strict monoidal category)** 结构，单位对象为 $$1_{\mathcal C}$$。

第67章例 3.5 在三元素集合上手算过"打包"（$$\eta$$）与"摊平"（$$\mu$$）两个操作，也验证过"打包再摊平等于什么都没做"以及"两种顺序摊平结果相同"。单子的定义要做的事，就是把这两个具体操作与它们满足的两条具体等式，翻译成对任意范畴、任意自函子都成立的一般语言：$$\eta$$ 与 $$\mu$$ 变成自然变换，两条等式变成下面的结合律与单位律。

**定义 3.18（单子, monad）** $$\mathcal C$$ 上的**单子**是一个三元组 $$(T,\eta,\mu)$$：自函子 $$T:\mathcal C\to\mathcal C$$、自然变换 $$\eta:1_{\mathcal C}\Rightarrow T$$（**单位, unit**）与 $$\mu:T^2=T\circ T\Rightarrow T$$（**乘法, multiplication**），满足两条**一致性条件 (coherence conditions)**：
$$\text{结合律：}\quad \mu\circ(T\mu)=\mu\circ(\mu T)\qquad(\text{两边都是 }T^3\Rightarrow T);$$
$$\text{单位律：}\quad \mu\circ(T\eta)=1_T=\mu\circ(\eta T)\qquad(\text{两边都是 }T\Rightarrow T).$$
记号约定：$$T\mu$$ 指 $$\mu$$ 与 $$1_T$$ 的水平复合 $$T\circ T^2\Rightarrow T\circ T$$；$$\mu T$$ 指 $$1_T\circ\mu:T^2\circ T\Rightarrow T\circ T$$。两者都定义在 $$T^3$$ 上。

**定理 3.19（伴随产生单子）** 设 $$F:\mathcal C\to\mathcal D$$、$$G:\mathcal D\to\mathcal C$$ 满足 $$F\dashv G$$，单位 $$\eta:1_{\mathcal C}\Rightarrow GF$$，余单位 $$\varepsilon:FG\Rightarrow1_{\mathcal D}$$。令
$$T:=GF,\qquad \mu:=G\varepsilon F\ \ (\varepsilon \text{ 沿 } F \text{ 的 whiskering 再施 } G),$$
则 $$(T,\eta,\mu)$$ 是 $$\mathcal C$$ 上的单子。

*证明思路*：两条单位律**恰好就是三角恒等式**——这不是巧合，三角恒等式的原始作用就是保证"单位与余单位互相抵消"，而单子的单位律要求的正是"$$\eta$$ 被 $$\mu$$ 吸收回恒同"。结合律则纯粹是 $$\varepsilon$$ 的自然性。

*证明*：
① $$\mu$$ 与 $$\eta$$ 都是自然变换：$$\varepsilon$$ 的 whiskering $$\varepsilon F:FGF\Rightarrow F$$ 自然，函子 $$G$$ 保持自然性，故 $$\mu=G(\varepsilon F)$$ 自然。
② 单位律右式：在对象 $$c$$ 上，$$(T\eta)_c=T(\eta_c)=GF(\eta_c)$$，故
$$(\mu\circ T\eta)_c=G(\varepsilon_{Fc})\circ GF(\eta_c)=G\bigl(\varepsilon_{Fc}\circ F(\eta_c)\bigr)=G\bigl(1_{Fc}\bigr)=1_{GFc},$$
中间用三角恒等式 $$(\varepsilon F)\circ(F\eta)=1_F$$。
③ 单位律左式：$$(\eta T)_c=\eta_{GFc}$$，故
$$(\mu\circ\eta T)_c=G(\varepsilon_{Fc})\circ\eta_{GFc}=1_{GFc},$$
用三角恒等式 $$(G\varepsilon)\circ(\eta G)=1_G$$ 在对象 $$Fc$$ 处的取值。
④ 结合律：在 $$c$$ 处，
$$(\mu\circ T\mu)_c=G(\varepsilon_{Fc})\circ GFG(\varepsilon_{Fc})=G\bigl(\varepsilon_{Fc}\circ FG(\varepsilon_{Fc})\bigr),$$
$$(\mu\circ\mu T)_c=G(\varepsilon_{Fc})\circ G(\varepsilon_{FGFc})=G\bigl(\varepsilon_{Fc}\circ\varepsilon_{FGFc}\bigr).$$
两式相等，因为 $$\varepsilon:FG\Rightarrow1$$ 的自然性方块对态射 $$h=\varepsilon_{Fc}:FGFc\to Fc$$ 给出
$$\varepsilon_{Fc}\circ FG(\varepsilon_{Fc})=\varepsilon_{Fc}\circ\varepsilon_{FGFc}.$$
（自然性说的是：对任意 $$h:X\to Y$$ 有 $$\varepsilon_Y\circ FG(h)=h\circ\varepsilon_X$$；取 $$X=FGFc$$、$$Y=Fc$$、$$h=\varepsilon_{Fc}$$ 即得。）$$\blacksquare$$

**例 3.19（三个单子）** 
(a) **幂集单子**（$$\mathcal C=\mathbf{Set}$$）：$$T=\mathcal P$$ 是幂集函子，$$\eta_S:S\to\mathcal P(S)$$ 送 $$s\mapsto\{s\}$$，$$\mu_S:\mathcal P(\mathcal P(S))\to\mathcal P(S)$$ 取**并**。三条公理分别就是"并的结合律"与"并的幺元律"，逐元素验算即得：$$\mu$$ 把"一族集合的族"摊平成一个集合。它的 Eilenberg–Moore 代数恰是**完备格 (complete lattice)**（$$a=\sup$$）。
(b) **自由 Abel 群单子**（$$\mathbf{Set}\xrightarrow{\ \mathbb Z[-]\ }\mathbf{Ab}\xrightarrow{\ U\ }\mathbf{Set}$$，$$T=U\circ\mathbb Z[-]$$）：$$\eta_S$$ 送 $$s$$ 到生成元 $$e_s$$；$$\mu_S$$ 把"形式整数线性组合的形式整数线性组合"按分配律展开收拢。这是定理 3.19 的最标准例子（自由 $$\dashv$$ 遗忘）。
(c) **张量代数单子**（$$\mathcal C=\mathbf{Vect}_k$$）：$$T(V)=\bigoplus_{n\ge0}V^{\otimes n}$$，$$\eta_V$$ 是 $$V=V^{\otimes1}$$ 的含入，$$\mu_V$$ 把两个张量词"拼接"（第 12 章的 $$V^{\otimes m}\otimes V^{\otimes n}\cong V^{\otimes(m+n)}$$ 正是这件事的算术）。张量代数常被记作 $$TV$$——这个记号本身就来自单子 $$T$$。

定理 3.19 说伴随能"折叠"成单子；反过来，给定一个单子，能不能"拆回"一个伴随？答案不唯一——下面两种拆法是两个极端：一种只记住"打包"操作本身怎么复合（Kleisli），另一种把"折叠"$$a:TA\to A$$ 直接当成对象的一部分随身携带（Eilenberg–Moore）。

**定义 3.20（Kleisli 范畴与 Eilenberg–Moore 代数）** 设 $$(T,\eta,\mu)$$ 是 $$\mathcal C$$ 上的单子。
- **Kleisli 范畴** $$\mathcal C_T$$：对象与 $$\mathcal C$$ 相同；态射 $$A\to B$$ 定义为 $$\mathcal C$$ 中的态射 $$A\to TB$$；恒同是 $$\eta_A:A\to TA$$；复合为
$$g\circ_T f:=\mu_C\circ Tg\circ f,\qquad A\xrightarrow{\ f\ }TB\xrightarrow{\ Tg\ }T^2C\xrightarrow{\ \mu_C\ }TC .$$
- **Eilenberg–Moore 代数（$$T$$-代数）**：一对 $$(A,a)$$，其中 $$a:TA\to A$$ 满足 $$a\circ\eta_A=1_A$$ 与 $$a\circ Ta=a\circ\mu_A$$；两个 $$T$$-代数间的态射 $$(A,a)\to(B,b)$$ 是 $$\mathcal C$$ 中态射 $$h:A\to B$$ 使 $$h\circ a=b\circ Th$$。

**注 3.20** Kleisli 与 EM 是把同一个单子"拆回成伴随"的两种极端方式：Kleisli 范畴保留最少的结构（只记住 $$\eta,\mu$$ 的复合规则），EM 范畴保留最多（把 $$a:TA\to A$$ 这种"折叠"本身当作对象的一部分）。定理 3.22 说明它们的普遍性地位。

**定理 3.21（单子 = 自函子范畴里的幺半群）** 在定义 3.17 的幺半范畴结构下，$$\mathbf{End}_{\mathcal C}$$ 的一个**幺半对象 (monoid object)** 恰好就是一个单子。于是 Mac Lane 的名言"$$\mathcal C$$ 中的单子不过是 $$\mathcal C$$ 的自函子范畴上的一个幺半群"是一句**逐字为真**的断言，不是修辞。

*证明*：幺半对象是三元组 $$(T,\ m:I\to T,\ \nu:T\otimes T\to T)$$，这里 $$I=1_{\mathcal C}$$、$$\otimes=\circ$$，满足
$$\nu\circ(\nu\otimes1)=\nu\circ(1\otimes\nu),\qquad \nu\circ(m\otimes1)=1_T=\nu\circ(1\otimes m).$$
逐字翻译：$$\nu=\mu:T^2\Rightarrow T$$；$$m=\eta:1_{\mathcal C}\Rightarrow T$$；$$\nu\otimes1=\mu T$$（在左边粘一层 $$T$$）；$$1\otimes\nu=T\mu$$；$$m\otimes1=\eta T$$；$$1\otimes m=T\eta$$。于是两条公理就是定义 3.18 的两条。$$\blacksquare$$

**定理 3.22（Kleisli 与 EM 各给出一个分解）** 记号同定义 3.20。
(i) 令 $$F_T:\mathcal C\to\mathcal C_T$$ 在对象上为恒同（$$A\mapsto A$$）、在态射上 $$f\mapsto\eta_B\circ f$$（$$A\to TB$$）；令 $$U_T:\mathcal C_T\to\mathcal C$$ 在对象上 $$A\mapsto TA$$、在态射上把 $$g:A\to TB$$ 送到 $$\mu_B\circ Tg:TA\to TB$$。则 $$F_T\dashv U_T$$，且 $$U_TF_T=T$$（这个伴随产生的单子正是 $$T$$）；
(ii) 同样，$$\mathcal C\xrightarrow{F^T}\mathcal C^T\xrightarrow{U^T}\mathcal C$$ 也构成伴随且给出同一个 $$T$$；
(iii) 在所有满足"伴随产生的单子等于 $$T$$"的伴随对中，Kleisli 分解是**最初的**、EM 分解是**最后的**。

*证明思路*：(i) 的关键是观察：按定义 3.20，$$\mathcal C_T$$ 中态射 $$A\to B$$ **就是** $$\mathcal C$$ 中态射 $$A\to TB$$，于是伴随要求的 Hom 同构退化为恒等：
$$\mathcal C_T(F_TA,B)=\mathcal C(A,TB)=\mathcal C(A,U_TB).$$
余单位在 $$B$$ 处是 $$\mu_B:T(TB)\to TB$$。用 $$\eta,\mu$$ 的一致性条件（定义 3.18）验证单位律与三角恒等式；再算 $$U_TF_T$$ 在态射 $$f:A\to B$$ 上的作用：
$$U_T\bigl(F_T(f)\bigr)=\mu_B\circ T(\eta_B\circ f)=\mu_B\circ T\eta_B\circ Tf=Tf,$$
用了 $$\mu\circ T\eta=1_T$$，故 $$U_TF_T=T$$，且这个伴随按定理 3.19 给出的 $$\mu$$ 恰是 $$U_T\varepsilon F_T$$。(ii) 同法，EM 范畴的余单位在 $$(B,b)$$ 处是 $$b:TB\to B$$。(iii) 是 (i)(ii) 的普遍性表述，此处只用它的存在性。$$\blacksquare$$

## 四、几何与物理直觉 (Intuition)

**正合 = "没有信息被多杀"。** 注 3.3 已经点破：$$\operatorname{im}f\subseteq\ker g$$ 说的是"$$g$$ 至少杀掉了 $$f$$ 造的东西"，等号说的是"$$g$$ 没有多杀"。几何上，把 $$f:A\to B$$ 想成把 $$A$$ 贴进 $$B$$，$$\ker g$$ 是"被 $$g$$ 压平的那一片"。正合的意思是好：$$B$$ 里"压平"的那一片，恰好就是 $$A$$ 贴进来的那片——中间没有多出来的部分。非正合时，多出来的那片 $$\ker g/\operatorname{im}f$$ 是**障碍**：它测出"$$A$$ 没能解释 $$B$$ 的死核"。

**极限与余极限的几何，正合是它们的特例。** 第 66 章把拉回与推出讲成纤维积与粘合。本节的核与余核就是那两类构造的最简特例：$$\ker f$$ 是 $$\operatorname{eq}(f,0)$$（一个极限），$$\operatorname{coker}f$$ 是 $$\operatorname{coeq}(f,0)$$（一个余极限）。所以阿贝尔范畴是"极限与余极限都够用、而且能互相比较（定理 3.6、定理 3.9）"的范畴。**蛇引理的几何读法**：$$\delta$$ 把 $$C$$ 一侧的障碍搬到 $$A$$ 一侧的障碍——它不是新东西，是同一个障碍换了立足点。这就是连接同态 (connecting homomorphism) 这个名字的来由：它在序列的两端之间拉了一根线。

**短正合列 = 正交分解。** 入口题里 $$H=0$$ 的条件是 $$\operatorname{im}P_1\oplus\operatorname{im}P_2=\mathcal H$$，也就是 $$P_1+P_2=1$$。这正是"$$\mathcal H$$ 被两个正交投影分解为两个直和项"，用序列写就是
$$0\to\operatorname{im}P_1\hookrightarrow\mathcal H\xrightarrow{\ P_2\ }\operatorname{im}P_2\to 0 .$$
MP120 用这个例子引出同调，形式上是把"二次复合为零"当成起点；本章则说清了为什么这个起点是对的：**$$P_2P_1=0$$ 让 $$(1)$$ 成为复形，"$$H=0$$"就是它正合，而 $$H\ne0$$ 时 $$H$$ 的维数就是两个投影"没把 $$\mathcal H$$ 铺满"的缺口。**

**物理里的复形：Maxwell 与规范自由度。** 第 24 章的 $$d^2=0$$ 与第 28 章的 $$H^k_{dR}$$ 是本章最重的物理落点。在 $$\mathbb R^3$$ 上，de Rham 复形的一部分是
$$\text{数量函数}\xrightarrow{\ \operatorname{grad}\ }\text{向量场}\xrightarrow{\ \operatorname{curl}\ }\text{向量场}\xrightarrow{\ \operatorname{div}\ }\text{数量函数},$$
"$$d^2=0$$"就是 $$\operatorname{curl}\circ\operatorname{grad}=0$$ 与 $$\operatorname{div}\circ\operatorname{curl}=0$$。**恰当 = 规范**（如 $$\mathbf B=\operatorname{curl}\mathbf A$$ 里的矢势 $$\mathbf A$$）、**闭 = 满足方程**（如 $$\operatorname{div}\mathbf B=0$$，无磁单极子）。$$H^2_{dR}\ne0$$ 意味着"存在满足 $$\operatorname{div}\mathbf B=0$$ 却写不成 $$\operatorname{curl}\mathbf A$$ 的场"——物理上这正对应"场携带了无法用势解释的拓扑信息"。规范自由度（$$\mathbf A\mapsto\mathbf A+\operatorname{grad}\chi$$）本身就是一个恰当形式，所以**可观测量必须对规范不变，等价地说，它只依赖上同调类**。

**单子的物理读法。** 单子把"自由生成"（$$T$$）与"折叠"（$$\mu$$）分开：幂集单子的 $$\mu$$ 是取并，自由 Abel 群单子的 $$\mu$$ 是展开线性组合，张量代数单子的 $$\mu$$ 是拼接张量词。物理里凡"先生成尽可能自由的量、再用约束折叠回去"的构造都在这个模式内（自由场、自由代数、约束系统）。特别地，定理 3.19 说：**只要你在物理里看到一个伴随（自由-遗忘、张量-Hom、诱导-限制），你就自动得到一个单子**——单子不是额外结构，是伴随的影子。

## 五、经典问题精讲 (Classical Problems)

**问题 5.1（蛇引理：连接同态与两处正合）**
**考点**：追图 (diagram chase)——同调代数唯一的手上功夫。**位置**：定理 3.15 的补全。
记号承定理 3.15，$$\delta$$ 的构造见该定理的 ①②③。证明 (i) 在 $$\ker c$$ 处正合：$$\operatorname{im}\bar g=\ker\delta$$；(ii) 在 $$\operatorname{coker}a$$ 处正合：$$\operatorname{im}\delta=\ker\bar f'$$。

**解**：(i) $$\operatorname{im}\bar g\subseteq\ker\delta$$：设 $$x=\bar g(\beta)$$，$$\beta\in\operatorname{Ker}b\subseteq B$$。取原像 $$y:=\beta$$，则 $$g(y)=x$$（合法）；又 $$b(y)=b(\beta)=0$$，故在 ② 中可取 $$z$$ 满足 $$f'(z)=0$$，由 $$f'$$ 单（行正合）得 $$z=0$$，即 $$\delta(x)=0$$。
$$\ker\delta\subseteq\operatorname{im}\bar g$$：设 $$x\in\operatorname{Ker}c$$ 且 $$\delta(x)=0$$。按构造取 $$y\in B$$（$$g(y)=x$$）与 $$z\in A'$$（$$f'(z)=b(y)$$）。$$\delta(x)=0$$ 即 $$z\in\operatorname{Im}a$$，写 $$z=a(w)$$，$$w\in A$$。则
$$b(y)=f'(z)=f'(a(w))=b(f(w)),$$
中间一步是左方块的交换性 $$f'\circ a=b\circ f$$。故 $$\beta:=y-f(w)\in\operatorname{Ker}b$$，而
$$\bar g(\beta)=g(y)-g(f(w))=x-0=x,$$
用了 $$\operatorname{Im}f=\operatorname{Ker}g$$（$$g\circ f=0$$）。于是 $$x\in\operatorname{im}\bar g$$。
(ii) $$\operatorname{im}\delta\subseteq\ker\bar f'$$：$$\bar f'$$ 是由 $$f'$$ 下降得到的 $$\operatorname{coker}a\to\operatorname{coker}b$$，故
$$\bar f'\bigl(\delta(x)\bigr)=\bar f'\bigl(z+\operatorname{Im}a\bigr)=f'(z)+\operatorname{Im}b=b(y)+\operatorname{Im}b=0 .$$
$$\ker\bar f'\subseteq\operatorname{im}\delta$$：设 $$z+\operatorname{Im}a\in\ker\bar f'$$，即 $$f'(z)\in\operatorname{Im}b$$，写 $$f'(z)=b(y)$$，$$y\in B$$。则
$$c\bigl(g(y)\bigr)=g'\bigl(b(y)\bigr)=g'\bigl(f'(z)\bigr)=0,$$
中间一步是右方块的交换性，最后一步用了 $$\operatorname{Im}f'=\operatorname{Ker}g'$$。故 $$x:=g(y)\in\operatorname{Ker}c$$；而构造 $$\delta(x)$$ 时用的正是这组 $$(y,z)$$，所以 $$\delta(x)=z+\operatorname{Im}a$$。$$\blacksquare$$

**问题 5.2（五项引理, five lemma）**
**考点**：单/满在追图里互相借用；**位置**：3.4 节——它是"正合性可以被同构搬运"的精确化。
设行正合的交换图
$$\begin{array}{ccccccccc}
A & \xrightarrow{f} & B & \xrightarrow{g} & C & \xrightarrow{h} & D & \xrightarrow{i} & E\\[4pt]
{\scriptstyle a}\big\downarrow & & {\scriptstyle b}\big\downarrow & & {\scriptstyle c}\big\downarrow & & {\scriptstyle d}\big\downarrow & & {\scriptstyle e}\big\downarrow\\[4pt]
A' & \xrightarrow{f'} & B' & \xrightarrow{g'} & C' & \xrightarrow{h'} & D' & \xrightarrow{i'} & E'
\end{array}$$
若 $$a,b,d,e$$ 都是同构，则 $$c$$ 也是同构。

**解**：分两步。
**① $$c$$ 单**：设 $$x\in\operatorname{Ker}c\subseteq C$$。则 $$d(h(x))=h'(c(x))=0$$，而 $$d$$ 单，故 $$h(x)=0$$，即 $$x\in\operatorname{Ker}h=\operatorname{Im}g$$，写 $$x=g(y)$$。于是 $$g'(b(y))=c(g(y))=c(x)=0$$，故 $$b(y)\in\operatorname{Ker}g'=\operatorname{Im}f'$$，写 $$b(y)=f'(a')$$，$$a'\in A'$$。由 $$a$$ 满，$$a'=a(a)$$ 对某 $$a\in A$$。左方块交换给出 $$f'(a(a))=b(f(a))$$，而 $$f'$$ 单（行正合），故 $$b(y)=b(f(a))$$，即 $$y-f(a)\in\operatorname{Ker}b=0$$（$$b$$ 单），得 $$y=f(a)$$。于是 $$x=g(y)=g(f(a))=0$$（$$\operatorname{Im}f=\operatorname{Ker}g$$）。
**② $$c$$ 满**：任取 $$x'\in C'$$。用右方块的交换性 $$e\circ i=i'\circ d$$ 与行正合给出的 $$i'\circ h'=0$$。先取 $$x_0\in D$$ 使 $$d(x_0)=h'(x')$$（$$d$$ 是同构，故满）。则
$$e\bigl(i(x_0)\bigr)=i'\bigl(d(x_0)\bigr)=i'\bigl(h'(x')\bigr)=0,$$
由 $$e$$ 单得 $$i(x_0)=0$$，即 $$x_0\in\operatorname{Ker}i=\operatorname{Im}h$$，写 $$x_0=h(y)$$，$$y\in B$$。于是
$$h'(x')=d(x_0)=d\bigl(h(y)\bigr)=h'\bigl(c(y)\bigr),$$
最后一步用右方块交换性 $$h'\circ c=d\circ h$$。故 $$x'-c(y)\in\operatorname{Ker}h'=\operatorname{Im}g'$$，写 $$x'-c(y)=g'(b')$$，$$b'\in B'$$。由 $$b$$ 满，$$b'=b(y_2)$$，$$y_2\in B$$。于是
$$x'=c(y)+g'\bigl(b(y_2)\bigr)=c(y)+c\bigl(g(y_2)\bigr)=c\bigl(y+g(y_2)\bigr),$$
最后一步再用右方块交换性 $$c\circ g=g'\circ b$$ 以及 $$c$$ 的加性。故 $$x'\in\operatorname{Im}c$$。结合 ①②，$$c$$ 是同构。$$\blacksquare$$

**问题 5.3（分裂引理, splitting lemma）**
**考点**：短正合列与直和的关系；**位置**：定理 3.11 与定理 3.6。在 $$R\text{-}\mathbf{Mod}$$ 中，设
$$0\to A\xrightarrow{\ f\ }B\xrightarrow{\ g\ }C\to 0$$
正合。则以下三条等价：(i) 存在 $$s:C\to B$$ 使 $$g\circ s=1_C$$（$$s$$ 称**截面, section**）；(ii) 存在 $$r:B\to A$$ 使 $$r\circ f=1_A$$（$$r$$ 称**收缩, retraction**）；(iii) 存在同构 $$\varphi:A\oplus C\to B$$ 使 $$\varphi\circ i_A=f$$、$$g\circ\varphi=p_C$$（$$i_A$$ 是含入、$$p_C$$ 是投影）。

**解**：(i)$$\Rightarrow$$(iii)：用加性结构定义 $$\varphi:A\oplus C\to B$$，$$\varphi(a,c):=f(a)+s(c)$$。则
$$g\bigl(\varphi(a,c)\bigr)=g f(a)+g s(c)=0+c=c,$$
故 $$g\circ\varphi=p_C$$；又 $$\varphi(a,0)=f(a)$$，即 $$\varphi\circ i_A=f$$。造逆：对 $$b\in B$$，注意 $$g\bigl(b-s(g(b))\bigr)=g(b)-g(b)=0$$，故 $$b-s(g(b))\in\operatorname{Ker}g=\operatorname{Im}f$$，且由 $$f$$ 单，存在**唯一** $$a\in A$$ 使 $$f(a)=b-s(g(b))$$。令
$$\psi(b):=\bigl(a,\ g(b)\bigr).$$
则 $$\psi\circ\varphi(a,c)$$：$$\varphi(a,c)=f(a)+s(c)$$，其 $$C$$ 分量为 $$g(f(a)+s(c))=c$$；其 $$A$$ 分量由 $$f(a')=f(a)+s(c)-s(g(f(a)+s(c)))=f(a)+s(c)-s(c)=f(a)$$ 给出 $$a'=a$$。故 $$\psi\varphi=1_{A\oplus C}$$。反向 $$\varphi\psi(b)=f(a)+s(g(b))=\bigl(b-s(g(b))\bigr)+s(g(b))=b$$。故 $$\varphi$$ 是同构。
(ii)$$\Rightarrow$$(iii)：令 $$\psi:B\to A\oplus C$$，$$\psi(b):=\bigl(r(b),\ g(b)\bigr)$$。则 $$\psi\circ f(a)=\bigl(rf(a),\,gf(a)\bigr)=(a,0)$$，即 $$\psi\circ f=i_A$$，于是 $$\varphi:=\psi^{-1}$$ 满足 $$\varphi\circ i_A=f$$；又 $$p_C\circ\psi=g$$，故 $$g\circ\varphi=p_C$$。只需证 $$\psi$$ 是同构。**单**：若 $$\psi(b)=0$$，则 $$r(b)=0$$ 且 $$g(b)=0$$；后者给出 $$b=f(a)$$（$$\operatorname{Ker}g=\operatorname{Im}f$$），代入前者得 $$a=rf(a)=r(b)=0$$，故 $$b=0$$。**满**：给定 $$(a,c)\in A\oplus C$$，由 $$g$$ 满取 $$b_0\in B$$ 使 $$g(b_0)=c$$，令
$$b:=f(a)+\bigl(b_0-f(r(b_0))\bigr).$$
则
$$g(b)=gf(a)+g(b_0)-g\bigl(f(r(b_0))\bigr)=0+c-0=c,\qquad r(b)=rf(a)+r(b_0)-rf\bigl(r(b_0)\bigr)=a+r(b_0)-r(b_0)=a ,$$
（用了 $$g\circ f=0$$、$$gf(r(b_0))=(gf)(r(b_0))=0$$ 与 $$r\circ f=1_A$$），故 $$\psi(b)=(a,c)$$。于是 $$\psi$$ 是同构。$$\blacksquare$$
(iii)$$\Rightarrow$$(i)(ii)：$$s:=\varphi\circ i_C$$ 与 $$r:=p_A\circ\varphi^{-1}$$ 满足要求。
(iii) 的形式说明：**短正合列分裂 $$\iff$$ 中间对象是两端直和**。$$\blacksquare$$

**问题 5.4（伴随产生的单子，以及它的 EM 代数）**
**考点**：一致性条件来自三角恒等式；**位置**：定理 3.19、定义 3.20。设 $$\mathcal C=\mathbf{Set}$$，$$T=\mathcal P$$ 为幂集单子（例 3.19(a)）。证明 $$T$$ 的 Eilenberg–Moore 代数恰是**完备格 (complete lattice)**。

**解**：$$T$$-代数是 $$(S,a)$$，$$a:\mathcal P(S)\to S$$，满足
$$\text{(甲)}\ a(\{s\})=s,\qquad \text{(乙)}\ a\Bigl(\bigcup_{i}U_i\Bigr)=a\bigl(\{a(U_i)\}_i\bigr)\ \text{对任意一族 } U_i\subseteq S .$$
在 $$S$$ 上定义 $$s\le t:\iff a(\{s,t\})=t$$。
**① $$\le$$ 是偏序**：自反即 (甲)：$$a(\{s,s\})=a(\{s\})=s$$。反对称：$$s\le t$$ 与 $$t\le s$$ 给出 $$a(\{s,t\})=t$$ 与 $$=s$$，故 $$s=t$$。
**② $$a(X)$$ 是 $$X$$ 的上界**：对 $$x\in X$$，由 (乙) 取族 $$\{\{x\},X\}$$，
$$a(X)=a\bigl(\{x\}\cup X\bigr)=a\bigl(\{a(\{x\}),a(X)\}\bigr)=a\bigl(\{x,a(X)\}\bigr),$$
最后一个等号用了 (甲)；比较首尾即 $$a(\{x,a(X)\})=a(X)$$，也就是 $$x\le a(X)$$。
**③ 传递性**：设 $$s\le t$$、$$t\le u$$，即 $$a(\{s,t\})=t$$、$$a(\{t,u\})=u$$。由 (乙) 取族 $$\{\{s,t\},\{t,u\}\}$$，
$$a(\{s,t,u\})=a\bigl(\{a(\{s,t\}),a(\{t,u\})\}\bigr)=a(\{t,u\})=u .$$
由 ②，$$s\le a(\{s,t,u\})=u$$，即 $$s\le u$$。
**④ $$a(X)=\sup X$$**：上界性已由 ② 给出。最小性：设 $$y$$ 是 $$X$$ 的上界，即对一切 $$x\in X$$ 有 $$a(\{x,y\})=y$$。由 (乙) 取族 $$\bigl\{\{x,y\}\bigr\}_{x\in X}$$，
$$a\bigl(X\cup\{y\}\bigr)=a\Bigl(\bigcup_{x\in X}\{x,y\}\Bigr)=a\bigl(\{a(\{x,y\})\}_{x\in X}\bigr)=a\bigl(\{y\}\bigr)=y ,$$
又由 (乙) 取族 $$\{X,\{y\}\}$$，$$a(X\cup\{y\})=a(\{a(X),y\})$$。两式比较得 $$a(\{a(X),y\})=y$$，即 $$a(X)\le y$$。故 $$a(X)$$ 是 $$X$$ 的最小上界。
于是 $$a(X)=\sup X$$ 对任何 $$X\subseteq S$$ 成立：**代数结构就是"任意子集都有上确界"**，即完备格。反之给定完备格，令 $$a(X):=\sup X$$，则 (甲) 是 $$\sup\{s\}=s$$，(乙) 是"上确界的迭代等于并的上确界"。$$\blacksquare$$

**问题 5.5（收口：第 09、10、14 章都是这里的一个例子）**
**考点**：把旧计算认成新结构——这是本章存在的理由。**位置**：例 3.14、定义 3.12、定义 3.13。
**(1)** 取 $$\mathcal A=\mathbf{Vect}_k$$，对象 $$C_1=k^2$$、$$C_0=k$$，微分 $$\partial_1(x,y):=x-y$$。定义
$$\partial_2:k\to k^2,\qquad \partial_2(z):=(z,z).$$
证明 $$C_\bullet:\ 0\to k\xrightarrow{\partial_2}k^2\xrightarrow{\partial_1}k\to 0$$ 是复形，并计算 $$H_1$$；再把 $$\partial_2$$ 换成零映射，重新算 $$H_1$$。
**(2)** 用一句话说清：第 18 章的链群与 $$\partial^2=0$$、第 20 章的 $$H_k$$、第 28 章的 $$H^k_{dR}$$ 分别是本章哪个定义的实例。

**解**：**(1)** 复形条件：$$\partial_1\partial_2(z)=\partial_1(z,z)=z-z=0$$ ✓。于是 $$\operatorname{Im}\partial_2\subseteq\operatorname{Ker}\partial_1$$，
$$\operatorname{Ker}\partial_1=\{(x,y):x=y\}=\{(z,z)\}=\operatorname{Im}\partial_2,\qquad H_1=\operatorname{Ker}\partial_1/\operatorname{Im}\partial_2=0 .$$
按定理 3.14(i)，该复形在位置 1 正合。若 $$\partial_2=0$$，则复形条件仍成立（$$\partial_1\circ 0=0$$），但
$$H_1=\operatorname{Ker}\partial_1/\operatorname{Im}0=\operatorname{Ker}\partial_1\cong k\ne0,$$
复形在位置 1 **不**正合：$$\partial_1$$ 杀掉了一整条对角线 $$\{x=y\}$$，而上一层一个元素都没产生，多杀的部分就是这 $$1$$ 维的 $$H_1$$。这正是注 3.3 的"正合是为不正合准备的"：同一个复形形状，$$H_1$$ 从 $$0$$ 变成 $$k$$，信息就出现在那里。
**(2)** 第 18 章的链群 $$C_q(K)$$ 连同 $$\partial^2=0$$ 就是**定义 3.12 中取 $$\mathcal A=\mathbf{Ab}$$ 的复形**；第 20 章的 $$H_k=\ker\partial_k/\operatorname{im}\partial_{k+1}$$ 就是**定义 3.13**；第 28 章的 $$(\Omega^\bullet(M),d)$$ 是同一构造在 $$\mathcal A=\mathbf{Vect}_{\mathbb R}$$ 中的**上链**版本，$$H^k_{dR}$$ 是其上同调。三者当年各自要验的"像落在核里""商有意义""链映射诱导映射"，现在全部由阿贝尔范畴的三条公理（定义 3.7）与定理 3.14 一次性提供。$$\blacksquare$$

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 设 $$n\ge1$$，在 $$\mathbf{Ab}$$ 中取 $$f=\times n:\mathbb{Z}\to\mathbb{Z}$$。求出 $$\ker f$$ 与 $$\operatorname{coker}f$$（连同它们的万有性质），并写出 $$\mathbf{Ab}$$ 的零对象与零态射 $$0_{\mathbb{Z},\mathbb{Z}}$$。

**基2.** 在任意范畴中证明：若 $$k=\ker f$$，则 $$k$$ 是单态射；若 $$\pi=\operatorname{coker}f$$，则 $$\pi$$ 是满态射。明确写出万有性质中"唯一"二字在证明的哪一步起了作用。

**基3.** 对下列三个序列，判断 (a) 它是否是复形；(b) 若是复形，它在中间那个对象处是否正合（不是复形的说明理由）。是复形的求出它的同调 $$H$$。
$$\text{(a)}\ 0\to\mathbb{Z}\xrightarrow{\ \times2\ }\mathbb{Z}\xrightarrow{\ \bmod 2\ }\mathbb{Z}/2\to 0;\qquad
\text{(b)}\ \mathbb{Z}/2\xrightarrow{\ 0\ }\mathbb{Z}/4\xrightarrow{\ \times2\ }\mathbb{Z}/4;\qquad
\text{(c)}\ \mathbb{Z}\xrightarrow{\ \times2\ }\mathbb{Z}\xrightarrow{\ \times3\ }\mathbb{Z}.$$

**基4.** 证明定理 3.14(i)：复形 $$C_\bullet$$ 在位置 $$n$$ 处正合当且仅当 $$H_n(C_\bullet)=0$$。并把第 20 章的 $$H_k=\ker\partial_k/\operatorname{im}\partial_{k+1}$$ 改写成定义 3.13 所用的余核形式。

### 竞赛（本课目标难度）

**竞1.** 在 $$\mathbf{Vect}_k$$ 中把定理 3.6 的 $$\varphi$$ 与 $$\psi$$ 写成矩阵，验证 $$\psi\varphi=1_{A\sqcup B}$$ 与 $$\varphi\psi=1_{A\times B}$$。再说明为什么同一条陈述在 $$\mathbf{Set}$$ 中失效，并指出 $$\mathbf{Set}$$ 缺少定义 3.4、定义 3.5 中的哪一条。

**竞2.** 证明定理 3.11(iii) 的细节：在 $$0\to A\xrightarrow{f}B\xrightarrow{g}C\to 0$$ 中 $$A\cong\operatorname{Ker}g$$、$$C\cong\operatorname{Coker}f$$。再用它说明 $$\mathbf{Grp}$$ 不是阿贝尔范畴：给出一个单态射，它不是任何态射的核。

**竞3.** 在 $$\mathbf{Ab}$$ 中取行正合的交换图
$$\begin{array}{ccccccc}
\mathbb{Z} & \xrightarrow{\ \times2\ } & \mathbb{Z} & \xrightarrow{\ \bmod 2\ } & \mathbb{Z}/2 & \xrightarrow{\ \ }\ & 0\\[4pt]
{\scriptstyle \times2}\big\downarrow & & {\scriptstyle \times2}\big\downarrow & & {\scriptstyle 0}\big\downarrow & & \\[4pt]
0 & \xrightarrow{\ \ }\ & \mathbb{Z} & \xrightarrow{\ \times2\ } & \mathbb{Z} & \xrightarrow{\ \bmod 2\ } & \mathbb{Z}/2
\end{array}$$
写出蛇引理给出的六项正合列，逐个算出六个对象，并显式计算连接同态 $$\delta$$ 在生成元上的取值，判断它是否同构。

**竞4.** 逐条验证幂集单子 $$(\mathcal P,\eta,\mu)$$ 的三条一致性条件；并证明它的 Kleisli 范畴 $$\mathbf{Set}_{\mathcal P}$$ 恰是**关系范畴** $$\mathbf{Rel}$$（对象为集合，态射为二元关系）。

### 研究（通向下一章）

**研1.** 设 $$\mathcal A$$ 是阿贝尔范畴，$$u:A\to B$$ 有两个满-单分解 $$u=m\circ e=m'\circ e'$$（$$e,e'$$ 满，$$m,m'$$ 单）。证明：存在**唯一**同构 $$\theta$$ 使 $$m=m'\circ\theta$$、$$e'=\theta\circ e$$；并由此证明任何满-单分解的中间对象同时同构于 $$\operatorname{Coim}u$$ 与 $$\operatorname{Im}u$$。

**研2.** 取 $$\mathbf{Ab}$$ 中的短正合列 $$0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\xrightarrow{\bmod 2}\mathbb{Z}/2\to 0$$。分别用三个函子作用于它：(i) $$\operatorname{Hom}(-,\mathbb{Z}/2)$$；(ii) $$-\otimes_{\mathbb Z}\mathbb{Z}/2$$；(iii) $$\operatorname{Hom}(\mathbb{Z},-)$$。对每一个，说明正合性还在不在，并把丢失的那一段显式算出来。

### 解答 (Solutions)

**解 基1.** $$\ker(\times n)=\{z\in\mathbb{Z}:nz=0\}=\{0\}$$（$$n\ge1$$），配以含入 $$k:0\hookrightarrow\mathbb{Z}$$；万有性质说的是：任何 $$u:X\to\mathbb{Z}$$ 满足 $$(\times n)\circ u=0$$ 都唯一地穿过 $$0$$——因为 $$n\ne0$$ 时这样的 $$u$$ 只能是零同态，而零同态恰穿过 $$0$$。于是 $$\ker(\times n)=0$$。
$$\operatorname{coker}(\times n)=\mathbb{Z}/n\mathbb{Z}$$，配以商映射 $$\pi:\mathbb{Z}\to\mathbb{Z}/n\mathbb{Z}$$；万有性质：若 $$v:\mathbb{Z}\to Y$$ 满足 $$v\circ(\times n)=0$$，则 $$v$$ 在 $$n\mathbb{Z}$$ 上取零，故可下降到 $$\mathbb{Z}/n\mathbb{Z}$$ 上，且下降后的同态唯一。
零对象是平凡群 $$\mathbf 0=\{0\}$$；$$0_{\mathbb{Z},\mathbb{Z}}$$ 是零同态 $$z\mapsto0$$（即 $$\mathbb{Z}\to\mathbf 0\to\mathbb{Z}$$ 的复合）。

**解 基2.** **核的情形**：设 $$u,v:X\to K$$ 满足 $$k\circ u=k\circ v$$。记 $$h:=k\circ u$$，则 $$f\circ h=f\circ k\circ u=0\circ u=0$$，即 $$h$$ 是"与 $$f$$ 复合为零"的态射 $$X\to A$$。由核的万有性质，存在**唯一** $$\bar h:X\to K$$ 使 $$k\circ\bar h=h$$。于是 $$u$$ 与 $$v$$ 都满足 $$k\circ u=k\circ v=h$$，**二者都是这条性质允许的同一个 $$\bar h$$**；由唯一性 $$u=v$$。这里"唯一"的作用是：万有性质本身只保证"存在一个 $$\bar h$$"，是唯一性把 $$u,v$$ 这两个候选合并成一个。故 $$k$$ 左可消，是单态射。
**余核的情形**：设 $$u,v:C\to X$$ 满足 $$u\circ\pi=v\circ\pi$$。记 $$h:=u\circ\pi$$，则 $$h\circ f=u\circ\pi\circ f=0$$，由余核的万有性质存在**唯一** $$\bar h:C\to X$$ 使 $$\bar h\circ\pi=h$$；$$u,v$$ 都是这个 $$\bar h$$，故 $$u=v$$。于是 $$\pi$$ 右可消，是满态射。$$\blacksquare$$

**解 基3.** **(a)** 复形：$$(\bmod 2)\circ(\times2)(z)=2z\bmod2=0$$ ✓。正合：$$\operatorname{Ker}(\bmod2)=2\mathbb{Z}=\operatorname{Im}(\times2)$$，故在 $$\mathbb{Z}$$ 处正合；由定理 3.14(i)，$$H=0$$。
**(b)** 复形：$$(\times2)\circ 0=0$$ ✓。但 $$\operatorname{Ker}(\times2:\mathbb{Z}/4\to\mathbb{Z}/4)=\{0,2\}\cong\mathbb{Z}/2$$，而 $$\operatorname{Im}0=0$$，故
$$H=\operatorname{Ker}(\times2)/\operatorname{Im}0\cong\mathbb{Z}/2\ne0,$$
在中间处**不**正合。$$H\cong\mathbb{Z}/2$$ 就是"$$\times2$$ 多杀掉的"那部分。
**(c)** 不是复形：$$(\times3)\circ(\times2)=\times6\ne0$$；等价地 $$\operatorname{Im}(\times2)=2\mathbb{Z}\not\subseteq\operatorname{Ker}(\times3)=\{0\}$$。故 $$d^2\ne0$$，商 $$\operatorname{Ker}/\operatorname{Im}$$ 根本没定义。$$\blacksquare$$

**解 基4.** 记 $$\iota:\operatorname{Im}d_{n+1}\hookrightarrow\operatorname{Ker}d_n$$（定义 3.13 中的含入）。由定理 3.11(ii)，$$H_n=\operatorname{Coker}\iota=0$$ $$\iff$$ $$\iota$$ 是满态射；又 $$\iota$$ 本身是核的含入，是单态射（定理 3.3），故 $$\iota$$ 满 $$\iff$$ $$\iota$$ 是同构 $$\iff$$ $$\operatorname{Im}d_{n+1}=\operatorname{Ker}d_n$$，而最后一句就是"在 $$n$$ 处正合"（定义 3.10）。
第 20 章的写法：在 $$\mathbf{Ab}$$ 中，$$\iota$$ 就是子群含入 $$\operatorname{im}\partial_{k+1}\hookrightarrow\ker\partial_k$$，其余核是商群
$$H_k=\operatorname{Coker}\iota=\ker\partial_k\big/\operatorname{im}\partial_{k+1},$$
与定义 3.13 逐字一致。$$\blacksquare$$

**解 竞1.** 在 $$\mathbf{Vect}_k$$（乃至任何 $$R\text{-}\mathbf{Mod}$$）中，$$A$$ 与 $$B$$ 的积与余积都是直和 $$A\oplus B$$（分量逐项相加、分量投影/含入）。按定理 3.6 的构造：
$$\varphi:A\oplus B\to A\oplus B,\qquad \varphi=\begin{pmatrix}1_A&0\\0&1_B\end{pmatrix}=I;\qquad
\psi:A\oplus B\to A\oplus B,\qquad \psi=i_A\circ p_A+i_B\circ p_B=\begin{pmatrix}1_A&0\\0&1_B\end{pmatrix}=I .$$
故 $$\psi\varphi=\varphi\psi=I$$，$$\varphi$$ 是同构。
**关键 leap**：这里两个构造给出的**是同一个东西**，因为"积"与"余积"在 $$\mathbf{Vect}_k$$ 中恰好重合；定理 3.6 的内容正是说这个重合不是巧合，而是"Hom 集是 Abel 群 + 复合双线性"逼出来的。
**$$\mathbf{Set}$$ 中失效**：取 $$A=B=\{\ast\}$$，则 $$A\times B$$ 只有一个元素，而 $$A\sqcup B$$ 有两个元素，故二者不同构。原因逐条对应：$$\mathbf{Set}$$ 的 Hom 集上没有 Abel 群结构（定义 3.4 不成立，$$\psi=i_Ap_A+i_Bp_B$$ 这个"和"根本写不出来），所以它连预加性范畴都不是，更谈不上加性（定义 3.5）。$$\blacksquare$$

**解 竞2.** **$$A\cong\operatorname{Ker}g$$**：$$g$$ 满（(ii)），且 $$\operatorname{Im}f=\operatorname{Ker}g$$，故把 $$f$$ 看成 $$A\to\operatorname{Ker}g$$ 的态射（核心是 $$f$$）是满态射；又 $$f$$ 本身是单态射，故它是同构 $$A\xrightarrow{\ \sim\ }\operatorname{Ker}g$$。
**$$C\cong\operatorname{Coker}f$$**：由 (A3)（$$\operatorname{Im}f=\operatorname{Ker}g$$ 且 $$g$$ 满）
$$g=\operatorname{coker}(\ker g)=\operatorname{coker}(\operatorname{Im}f).$$
而 $$f$$ 与它的像含入只差一个满态射（$$f=\text{含入}\circ q$$，$$q:A\to A/\ker f$$ 满），余核因此在两者上相同，即 $$\operatorname{coker}(\operatorname{Im}f)=\operatorname{coker}f$$。故 $$C\cong\operatorname{Coker}f$$。
**$$\mathbf{Grp}$$ 的反例**：取 $$\mathbb{Z}/2=\langle(12)\rangle\hookrightarrow S_3$$ 的含入 $$\iota$$，它是单态射。在 $$\mathbf{Grp}$$ 中，态射 $$f:G\to H$$ 的余核是 $$H\to H/N$$，其中 $$N$$ 是 $$f(G)$$ 的**正规闭包**。这里 $$\iota$$ 的像 $$\langle(12)\rangle$$ 的正规闭包：任何包含一个对换的正规子群包含它的全部共轭（所有对换），而对换生成整个 $$S_3$$，故正规闭包是 $$S_3$$ 本身。于是 $$\operatorname{coker}\iota$$ 是 $$S_3\to S_3/S_3=\mathbf 1$$，其核为整个 $$S_3\ne\operatorname{Im}\iota$$。这既说明 $$\iota\ne\ker(\operatorname{coker}\iota)$$，即 (A2) 失效，也说明 $$\iota$$ 不是任何群同态的核：$$\operatorname{Ker}$$ 只能是包含 $$\iota$$ 的像的**正规**子群在某个商下的原像，而唯一这样的正规子群是 $$S_3$$ 自己，它给出的核是 $$S_3$$。故 $$\mathbf{Grp}$$ 不满足 (A2)，不是阿贝尔范畴。$$\blacksquare$$

**解 竞3.** 先验交换性：右方块 $$0\circ(\bmod2)=(\bmod2)\circ(\times2)$$（两边都是零映射）；左方块 $$(\times2)\circ(\times2)=(\times2)\circ(\times2)$$ ✓。两行正合（就是基3(a) 的序列）。
六个对象：$$\operatorname{Ker}(\times2)=0$$；$$\operatorname{Ker}(\times2)=0$$；$$\operatorname{Ker}0=\mathbb{Z}/2$$；$$\operatorname{Coker}(\times2)=\mathbb{Z}/2$$；$$\operatorname{Coker}(\times2)=\mathbb{Z}/2$$；$$\operatorname{Coker}0=\mathbb{Z}/2$$。
蛇引理给出的六项正合列是
$$0\xrightarrow{\ \ }\ 0\xrightarrow{\ \ }\ \mathbb{Z}/2\xrightarrow{\ \delta\ }\mathbb{Z}/2\xrightarrow{\ \bar f'\ }\mathbb{Z}/2\xrightarrow{\ \bar g'\ }\mathbb{Z}/2 .$$
其中 $$\bar f'$$ 由 $$\times2:\mathbb{Z}\to\mathbb{Z}$$ 诱导到商上，即 $$\mathbb{Z}/2\xrightarrow{\ \times2\ }\mathbb{Z}/2$$ 是零映射。
**计算 $$\delta$$**：取生成元 $$x=1\in\mathbb{Z}/2=\operatorname{Ker}c$$。① 取原像 $$y=1\in\mathbb{Z}$$（$$y\bmod2=1$$）。② $$b(y)=2\in\mathbb{Z}$$；由 $$f'=\times2$$ 取 $$z=1$$（$$2\cdot1=2$$）。③ $$\delta(1)=1+\operatorname{Im}(\times2)=1+2\mathbb{Z}\in\mathbb{Z}/2=\operatorname{Coker}a$$。故 $$\delta(1)=1$$，即 $$\delta$$ 把生成元送到生成元，是**同构**。
**正合性核对**：在 $$\operatorname{Ker}c$$ 处，$$\operatorname{im}(0\to\mathbb{Z}/2)=0=\ker\delta$$（$$\delta$$ 单）；在 $$\operatorname{Coker}a$$ 处，$$\operatorname{im}\delta=\mathbb{Z}/2=\ker(\bar f')$$，因为 $$\bar f'$$ 由 $$f'=\times2:\mathbb{Z}\to\mathbb{Z}$$ 诱导，在 $$\mathbb{Z}/2$$ 上是零映射；在 $$\operatorname{Coker}b$$ 处，$$\operatorname{im}\bar f'=0=\ker\bar g'$$，因为 $$\bar g'$$ 由 $$g'=\bmod 2$$ 诱导，是 $$\mathbb{Z}/2\to\mathbb{Z}/2$$ 的同构。三处都是零对零，正合。$$\blacksquare$$

**解 竞4.** 记 $$\mathcal P^n(S)$$ 为 $$S$$ 的 $$n$$ 重幂集。
**① 结合律 $$\mu\circ\mathcal P\mu=\mu\circ\mu\mathcal P$$**：取 $$\mathcal U\in\mathcal P^3(S)$$，即 $$\mathcal U$$ 是一族 $$\mathcal P^2(S)$$ 的元素。
$$\mathcal P\mu(\mathcal U)=\{\mu(U):U\in\mathcal U\}=\Bigl\{\bigcup U:U\in\mathcal U\Bigr\},\qquad
\mu\bigl(\mathcal P\mu(\mathcal U)\bigr)=\bigcup_{U\in\mathcal U}\bigcup U .$$
$$\mu\mathcal P(\mathcal U)=\mu_{\mathcal P(S)}(\mathcal U)=\bigcup\mathcal U\subseteq\mathcal P(S),\qquad
\mu\bigl(\mu\mathcal P(\mathcal U)\bigr)=\bigcup\Bigl(\bigcup\mathcal U\Bigr)=\bigcup_{U\in\mathcal U}\bigcup U .$$
两式相等（"并的并"与"按两层摊平"是同一件事）。
**② $$\mu\circ\mathcal P\eta=1_{\mathcal P}$$**：$$\mathcal P\eta_S(A)=\{\eta_S(a):a\in A\}=\{A\}$$，故 $$\mu_S(\{A\})=\bigcup\{A\}=A$$ ✓。
**③ $$\mu\circ\eta\mathcal P=1_{\mathcal P}$$**：$$\eta\mathcal P_S=\eta_{\mathcal P(S)}$$，同样有 $$\eta_{\mathcal P(S)}(A)=\{A\}$$，故 $$\mu_S(\{A\})=A$$ ✓。
**Kleisli 范畴**：对象是集合；$$\mathbf{Set}_{\mathcal P}$$ 中态射 $$S\to T$$ 按定义 3.20 是函数 $$S\to\mathcal P(T)$$，即 $$S$$ 与 $$T$$ 之间的一个二元关系（$$s\sim t\iff t\in f(s)$$）。恒同是 $$\eta_S:s\mapsto\{s\}$$，即对角关系。复合
$$(g\circ_T f)(s)=\mu_U\bigl(\mathcal Pg(f(s))\bigr)=\bigcup_{t\in f(s)}g(t),$$
恰是关系的复合 $$s\sim_U u\iff\exists t\,(s\sim_T t\ \text{且}\ t\sim_U u)$$。结合律与单位律由单子公理保证（这也说明 $$\mathbf{Set}_{\mathcal P}$$ 确实是范畴）。$$\blacksquare$$

**解 研1.** **① 造 $$\theta$$**：由 $$m'e'=me$$，
$$\operatorname{coker}(m')\circ m\circ e=\operatorname{coker}(m')\circ m'\circ e'=0 .$$
$$e$$ 是满态射，故可右消去得 $$\operatorname{coker}(m')\circ m=0$$。由 (A2)，$$m'=\ker(\operatorname{coker}m')$$，于是 $$m$$ 唯一地穿过 $$m'$$：存在**唯一** $$\theta:I\to I'$$ 使 $$m=m'\circ\theta$$（$$I,I'$$ 是两个分解的中间对象）。
**② 对称地**存在唯一 $$\theta':I'\to I$$ 使 $$m'=m\circ\theta'$$。
**③ $$\theta$$ 是同构**：$$m=m'\theta=(m\theta')\theta=m(\theta'\theta)$$，而 $$m$$ 单，故 $$\theta'\theta=1_I$$；对称地 $$\theta\theta'=1_{I'}$$。
**④ 唯一性**：若 $$m=m'\theta_1=m'\theta_2$$，则 $$m'$$ 单给出 $$\theta_1=\theta_2$$。又由 $$m'e'=me=m'\theta e$$ 与 $$m'$$ 单得 $$e'=\theta\circ e$$。分解在同构意义下唯一。
**⑤ 中间对象是 $$\operatorname{Coim}u$$ 与 $$\operatorname{Im}u$$**：对任意满-单分解 $$u=m'e'$$，
· 由 $$m'$$ 单，$$m'e's=0\iff e's=0$$，故 $$\ker e'=\ker u$$。由 (A3)（$$e'$$ 满）
$$e'=\operatorname{coker}(\ker e')=\operatorname{coker}(\ker u)=\operatorname{Coim}u .$$
· 由 $$e'$$ 满，$$t\circ m'=0\iff t\circ m'e'=0\iff t\circ u=0$$，故 $$\operatorname{coker}m'=\operatorname{coker}u$$。由 (A2)
$$m'=\ker(\operatorname{coker}m')=\ker(\operatorname{coker}u)=\operatorname{Im}u .$$
于是 $$I'$$ 同时同构于 $$\operatorname{Coim}u$$ 与 $$\operatorname{Im}u$$——这正是定理 3.9 说的事，而且是**免费**得到的：一旦知道分解存在，(A2)(A3) 就唯一地确定了它的两端。
注意这条"分解存在且同构意义下唯一"正是第 70 章的枢纽：**投射消解在同构意义下唯一的比较引理**用的就是同一套论证（把"单"换成"链映射是单射"，把"满"换成"链映射在每层是满射"），而导出函子之所以良定义，全靠这类唯一性。那正是下一章的起点。$$\blacksquare$$

**解 研2.** **(i) $$\operatorname{Hom}(-,\mathbb{Z}/2)$$（反变）**：把函子作用在 $$0\to\mathbb{Z}\xrightarrow{\times2}\mathbb{Z}\xrightarrow{\bmod2}\mathbb{Z}/2\to0$$ 上（反变函子把箭头全反向）得
$$0\to\operatorname{Hom}(\mathbb{Z}/2,\mathbb{Z}/2)\xrightarrow{\ \sim\ }\operatorname{Hom}(\mathbb{Z},\mathbb{Z}/2)\xrightarrow{\ \times2\ }\operatorname{Hom}(\mathbb{Z},\mathbb{Z}/2)\to0,$$
即 $$0\to\mathbb{Z}/2\xrightarrow{\ 1\ }\mathbb{Z}/2\xrightarrow{\ 0\ }\mathbb{Z}/2\to0$$。第一段正合（第一个映射是同构），但**右端不正合**：最后一个映射是零映射而不是满射，$$\operatorname{Coker}=\mathbb{Z}/2\ne0$$。
**(ii) $$-\otimes_{\mathbb Z}\mathbb{Z}/2$$（右正合）**：得到
$$\mathbb{Z}/2\xrightarrow{\ 0\ }\mathbb{Z}/2\xrightarrow{\ 1\ }\mathbb{Z}/2\to0$$
（$$\times2\otimes1$$ 在 $$\mathbb{Z}\otimes\mathbb{Z}/2=\mathbb{Z}/2$$ 上是乘以 $$2$$，即零映射）。**左端不正合**：$$\operatorname{Ker}=\mathbb{Z}/2\ne0$$。
**(iii) $$\operatorname{Hom}(\mathbb{Z},-)$$（协变）**：自然同构 $$\operatorname{Hom}(\mathbb{Z},A)\cong A$$，故作用后逐字得到原序列，仍然正合。
**结论与衔接**：正合性会被函子破坏。(ii) 破坏的是左端、(i) 破坏的是右端，而丢失的量分别是
$$\operatorname{Tor}_1^{\mathbb Z}(\mathbb{Z}/2,\mathbb{Z}/2)=\ker= \mathbb{Z}/2,\qquad \operatorname{Ext}^1_{\mathbb Z}(\mathbb{Z}/2,\mathbb{Z}/2)=\operatorname{coker}=\mathbb{Z}/2 .$$
第 70 章要做的事情正是把这个观察制度化：**给定函子，用消解把"丢掉的段"逐个逐层算出来，得到的函子族就是导出函子**——这就是"同调为什么必然存在"的统一答案。那正是下一章的起点。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**1. 正合是人给"退化"起的名字，它真正的生产力在反面。** $$\operatorname{im}f=\ker g$$ 成立时序列不携带信息；不成立时，商 $$\ker g/\operatorname{im}f$$ 本身就是信息。所以"正合"的用途不是描述好情况，而是让你能说清"哪里坏、坏了多少"——坏掉多少就是同调（定理 3.14）。这也是入口题 (3) 的答案。

**2. 阿贝尔范畴是"让核、像、商自动有意义"的最小公理系统。** 五条公理分工明确：加性保证 Hom 集是 Abel 群、有限积与有限余积合一（定理 3.6）；(A1) 保证核与余核总有定义，于是写商时不必再验分母；(A2)(A3) 保证像与余像重合（定理 3.9），于是"$$\operatorname{im}=\ker$$"这个等号两边才有共同的世界。第 09、10、14 章里那些"先验证包含式再作商"的手续，从此被"复形"的定义本身吸收（注 3.9）。

**3. 单子不是新怪物，它就是伴随的影子。** 任何伴随 $$F\dashv G$$ 都给出单子 $$(GF,\ \eta,\ G\varepsilon F)$$（定理 3.19），而它的两条一致性条件恰是一对三角恒等式；反过来，每个单子都能通过 Kleisli 范畴或 Eilenberg–Moore 范畴分解回一个伴随（定理 3.22）。Mac Lane 那句"单子不过是自函子范畴里的一个幺半群"是逐字为真的陈述（定理 3.21）。

**4. 旧账在这里一次结清。** 第 14 章的 $$d^2=0$$、第 18 章的 $$\partial^2=0$$、第 20 章的 $$H_k$$、第 28 章的 $$H^k_{dR}$$，全都是同一个构造取不同 $$\mathcal A$$、不同指标方向的实例（例 3.14、问题 5.5）。当年在 $$\mathbb{Z}$$-模与 $$\mathbb{R}$$-向量空间上逐条验算的东西（像落在核里、商有意义、链映射诱导映射），现在由三条公理与定理 3.14 一次性提供。

**5. 下一章的悬念。** 本章讲清了正合，却也暴露出一个刺眼的事实：正合性**会被函子破坏**。练习研2 已经算出，$$\operatorname{Hom}(-,\mathbb{Z}/2)$$ 丢掉满射端、$$-\otimes\mathbb{Z}/2$$ 丢掉单射端，而丢掉的量都等于 $$\mathbb{Z}/2$$。这些量不是意外：它们有名字、有函子性、还能逐层往上算。第 70 章讲**导出函子 (derived functor)**——用消解把函子"离正合有多远"逐层量化，得到 $$\operatorname{Tor}$$ 与 $$\operatorname{Ext}$$，并给"同调为什么必然存在"一个统一的答案。

**延伸阅读**：Weibel《An Introduction to Homological Algebra》第 1 章（$$\mathbf{Ch}(\mathcal A)$$ 与长正合列的标准处理，本章据此整理）；Mac Lane《Categories for the Working Mathematician》第 VI 章（单子与代数的原始叙述）；Kashiwara–Schapira《Categories and Sheaves》第 8 章（定义 3.7 所依据的公理化版本）；Riehl《Category Theory in Context》第 5 章（单子与伴随分解）；第 72 章将把本章的 $$\mathbf{Sh}(X;\mathbf{Ab})$$ 用作层论的基本舞台。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch67_单子_Abel范畴与正合_上.md">← 第67章 单子、Abel 范畴与正合·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch69_同调代数_直和_投射_内射模_导出函子_上.md">第69章 同调代数：直和、投射/内射模、导出函子·上 →</a></div>
</div>
