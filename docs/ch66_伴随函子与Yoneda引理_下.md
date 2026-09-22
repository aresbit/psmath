---
layout: default
---

# 第66章: 伴随函子与Yoneda 引理·下：完整推导 (Adjoint Functors and the Yoneda Lemma · Part II: Full Derivation)

> 配套预备: 见 第65章 伴随函子与Yoneda 引理·上（同一主题的具体铺垫，建议先读）

> 对应原专栏: MP118、MP124–MP125、MP137
> 专家依据: `_experts/algebra/category-universal-properties.md`（主）+ `_experts/algebra/_SKILL.md`
> 知识库依据: `opc2/knowledge/math/范畴论/`（含 `pursuing-stacks/` 12 篇）、`opc2/knowledge/math/代数几何/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

读完第 65 章的具体例子——自由生成的字如何唯一延拓成同态、$$\mathbb{Z}/2\otimes\mathbb{Z}/2$$ 与它对应的 Hom 集怎样一一配对、方阵之间的"自然变换"怎么就是乘一个矩阵——之后，这里把同样的构造写成一般定义，并给出完整、不省步骤的证明。

第 62 章把「结构」抽象成**范畴**、把「结构之间的映射」抽象成**函子**；第 64 章把标量从域放宽到环，撞出了第一对**成对出现的函子**——张量积 $$-\otimes_A M$$ 与 Hom 函子 $$\operatorname{Hom}_A(M,-)$$，并注意到它们「一左一右、各保正合性的一半」。那个被搁置的问题就是本章要回答的：

**为什么这些构造成对出现？**

答案是一句话：成对的不是「两个长得像的函子」，而是**一对互相可逆的对应**。把「从 $$F$$ 的像出发的映射」与「射进 $$G$$ 的像的映射」写成同构

$$\mathcal{D}(Fc,d)\cong\mathcal{C}(c,Gd),$$

就得到**伴随函子 (adjoint functor)**——范畴论里比同构松、比「相似」强得多、并且**自动携带大量结构**的关系。本章的另一半是 **Yoneda 引理**：一个对象被它到所有对象的态射完全决定，于是「元素」和「自然变换」变成同一种东西。有了它，伴随的抽象定义立刻落回可计算的同构，而「张量 ⊣ Hom」「自由 ⊣ 遗忘」「$$\Sigma\dashv\Omega$$」全部被认出来是同一件事的不同化身；第 40 章的 Gelfand 对偶也会在这一章被重新认出是一对伴随（3.23）。

往后看：第 68 章把「一对伴随」进一步压成**单子**，并在 Abel 范畴里把「保正合」精确成短正合列——本章 3.21 的「左伴随保余极限」正是那条路的入口。

## 二、入口：一道具体的问题 (Entry Problem)

**先做题，不给定义。** 下面四问都能在纸上做完；前三问（(a)(b)(c)）分别取自自由群的万有性质、模的张量积、MP137 里「线性代数版的 Yoneda」。第 3 节之前不需要任何新名词，第 5 节会把它们全部回收。

**(a) 自由生成的两张面孔。** 取集合 $$S=\{s,t\}$$，自由群 $$F_S$$ 是 $$S$$ 生成的约化字构成的群（字 $$s^{\pm1}t^{\pm1}\cdots$$，乘法是拼接后约化）。现在给你任意一个群 $$G$$ 和**任意一个映射** $$f:S\to G$$——不要求 $$f$$ 保持任何东西，两个元素各自随便挑一个群元就行。

**证明**：存在唯一的群同态 $$\varphi:F_S\to G$$ 使 $$\varphi(s)=f(s)$$、$$\varphi(t)=f(t)$$。然后把这件事改写成一个等式：左边是一个「群同态集合」，右边是一个「集合映射集合」，两边一一对应。**问**：右边那个集合是**无条件**存在的，左边那个集合却必须满足乘法、单位、逆元三条公理——为什么两边能一一对应？这个「无条件 vs 有条件」的落差是被什么吃掉的？

**(b) 张量 ⊣ Hom，具体算一遍。** 不用任何新概念，把下面两个集合各算一遍：

$$\operatorname{Hom}_{\mathbb{Z}}\bigl(\mathbb{Z}/2\otimes_{\mathbb{Z}}\mathbb{Z}/2,\ \mathbb{Z}/2\bigr),\qquad \operatorname{Hom}_{\mathbb{Z}}\bigl(\mathbb{Z}/2,\ \operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2)\bigr).$$

两个都是 2 元集。找出它们之间那个**不依赖任何选择**的一一对应，并把它念出来：一个「以 $$\mathbb{Z}/2\otimes\mathbb{Z}/2$$ 为定义域的 $$\mathbb{Z}$$-线性映射」与一个「先送给 $$\mathbb{Z}/2$$、再由它送回一个映射的规则」为什么是同一件事？

**(c) 矩阵版的 Yoneda。** 记 $$\mathfrak{m}=\mathbb{K}^{m\times m}$$ 是 $$m$$ 阶方阵环（$$\mathbb{K}=\mathbb{R}$$ 或 $$\mathbb{C}$$），$$\mathfrak{m}\text{-}\mathbf{Mod}$$ 是左 $$\mathfrak{m}$$-模范畴，其中对象是各种 $$\mathbb{K}^{m\times p}$$。固定对象 $$A=\mathbb{K}^{m\times n}$$。

**验证**：对每个 $$p$$ 有同构 $$\operatorname{Hom}_{\mathfrak{m}-}(A,\ \mathbb{K}^{m\times p})\cong\mathbb{K}^{n\times p}$$，并且 $$A$$ 上的「态射 $$f$$ 诱导出的映射」就是**右乘** $$f$$。然后回答：**若两个对象 $$A,B$$ 使得 $$\operatorname{Hom}(A,X)$$ 与 $$\operatorname{Hom}(B,X)$$ 对一切 $$X$$ 都同构、而且这些同构互相相容，能不能推出 $$A\cong B$$？** 如果能，那个同构是唯一的吗？（这一问和第 (a) 问其实是同一件事。）

**(d) 元问题。** (a)(b)(c) 表面上毫无关系：一个是自由群，一个是环上的张量积，一个是矩阵。可是把它们各自画成「两个态射集之间的双射」的图，**形状一模一样**。

**问**：这个共同的形状有没有名字？为什么它值得单独立一章，而不是当作三个互不相干的技巧？（提示：一个函子在左、一个在右——而极限与余极限、核与余核、积与余积也总是成对出现。）

> 第 5 节的**问题 1、问题 2、问题 3、问题 4** 分别把 (a)(b)(c) 以及「保极限还是保余极限」算完；问题 4 会顺手解释 (d) 里的那个二选一。

## 三、结构：定义与完整推导 (Structure & Proof)

### 函子范畴与自然变换

第 62 章已经有了函子与自然变换的定义；本节把它们打包成一个新的范畴——**函子以此自身为对象**。这一步不只是形式上的收纳：Yoneda 引理说的正是这个新范畴里的态射集，所以先把舞台搭好。

**定义 3.1（自然变换, natural transformation）** 设 $$F,G:\mathcal{C}\to\mathcal{D}$$ 是函子。一个从 $$F$$ 到 $$G$$ 的**自然变换** $$\alpha:F\Rightarrow G$$，是指对每个对象 $$X\in\mathcal{C}$$ 指定一个态射

$$\alpha_X:F(X)\to G(X),$$

使得对 $$\mathcal{C}$$ 中每个态射 $$f:X\to Y$$，下面的方块**交换**：

$$G(f)\circ\alpha_X=\alpha_Y\circ F(f).$$

称 $$\alpha_X$$ 为 $$\alpha$$ 在 $$X$$ 处的**分量 (component)**。若每个 $$\alpha_X$$ 都是同构，称 $$\alpha$$ 是**自然同构 (natural isomorphism)**，记 $$\alpha:F\cong G$$。

**定义 3.2（函子范畴, functor category）** 以 $$\mathcal{C}\to\mathcal{D}$$ 的全体函子为对象，以它们之间的自然变换为态射，态射的复合取**垂直复合**

$$(\beta\circ\alpha)_X:=\beta_X\circ\alpha_X\qquad(\alpha:F\Rightarrow G,\ \beta:G\Rightarrow H),$$

恒等态射取**恒等自然变换** $$(1_F)_X:=1_{F(X)}$$，所得的范畴记作

$$[\mathcal{C},\mathcal{D}]\qquad\text{或}\qquad \mathcal{D}^{\mathcal{C}}.$$

**定理 3.3（函子范畴确实是范畴）** 定义 3.2 中的对象、态射、复合与恒等满足范畴的全部公理。

**证明** 四件事逐条验。

(i) **复合的类型正确、且仍是自然变换。** 设 $$\alpha:F\Rightarrow G$$、$$\beta:G\Rightarrow H$$。对任意 $$f:X\to Y$$，把两条路径从 $$F(X)$$ 送到 $$H(Y)$$：

$$H(f)\circ(\beta\circ\alpha)_X=H(f)\circ\beta_X\circ\alpha_X\ \overset{\beta\ \text{自然}}{=}\ \beta_Y\circ G(f)\circ\alpha_X\ \overset{\alpha\ \text{自然}}{=}\ \beta_Y\circ\alpha_Y\circ F(f)=(\beta\circ\alpha)_Y\circ F(f).$$

所以 $$\beta\circ\alpha:F\Rightarrow H$$ 满足自然性方块。

(ii) **恒等是自然变换。** 这里要验证的是 $$1_F:F\Rightarrow F$$（$$\alpha=1_F$$ 时取 $$G:=F$$）满足定义 3.1 的方块。分量是 $$(1_F)_X=1_{F(X)}$$、$$(1_F)_Y=1_{F(Y)}$$，代入方块左边：$$F(f)\circ(1_F)_X=F(f)\circ1_{F(X)}=F(f)$$；代入右边：$$(1_F)_Y\circ F(f)=1_{F(Y)}\circ F(f)=F(f)$$。两边分别化简后都等于同一个态射 $$F(f)$$，方块交换。

(iii) **单位律。** $$(\alpha\circ1_F)_X=\alpha_X\circ1_{F(X)}=\alpha_X=(1_G)_X\circ\alpha_X=(1_G\circ\alpha)_X$$ 对每个 $$X$$ 成立；自然变换由各分量决定，故 $$\alpha\circ1_F=\alpha=1_G\circ\alpha$$。

(iv) **结合律。** $$((\gamma\circ\beta)\circ\alpha)_X=(\gamma\circ\beta)_X\circ\alpha_X=\gamma_X\circ\beta_X\circ\alpha_X=\gamma_X\circ(\beta\circ\alpha)_X=(\gamma\circ(\beta\circ\alpha))_X$$，逐点归结为 $$\mathcal{D}$$ 中的结合律。

综上，$$[\mathcal{C},\mathcal{D}]$$ 是一个范畴。$$\blacksquare$$

**注 3.3（垂直复合与水平复合）** 定义 3.2 里用的复合叫**垂直复合**——它把两个**端点相同**的自然变换 $$F\Rightarrow G\Rightarrow H$$ 接起来。还有一种**水平复合**：给定 $$\alpha:F\Rightarrow G$$（$$F,G:\mathcal{C}\to\mathcal{D}$$）与 $$\beta:H\Rightarrow K$$（$$H,K:\mathcal{D}\to\mathcal{E}$$），可以造出 $$(\beta\alpha):HF\Rightarrow KG$$，其分量为

$$(\beta\alpha)_X:=\beta_{G(X)}\circ H(\alpha_X)=K(\alpha_X)\circ\beta_{F(X)}.$$

（最后两个表达式相等，正是 $$\beta$$ 在态射 $$\alpha_X:F(X)\to G(X)$$ 上的自然性。）本章只需要垂直复合；水平复合在第 68 章讨论单子与函子的合成时才会用到。

**例 3.4（预层范畴, presheaf category）** 取 $$\mathcal{D}=\mathbf{Set}$$，得到两类特别重要的函子范畴：

$$\mathbf{Set}^{\mathcal{C}}=[\mathcal{C},\mathbf{Set}],\qquad \hat{\mathcal{C}}:=[\mathcal{C}^{\mathrm{op}},\mathbf{Set}].$$

后者的对象叫 $$\mathcal{C}$$ 上的**预层 (presheaf)**。最经典的预层来自拓扑：取 $$\mathcal{O}(X)$$ 为拓扑空间的开集按包含构成的范畴（对象是开集，态射是包含 $$U\subseteq V$$），则一个预层把每个开集 $$U$$ 送成一个集合、把每个包含 $$U\subseteq V$$ 送成一个**限制映射** $$\rho_{VU}:F(V)\to F(U)$$，并要求 $$\rho_{UU}=1$$、$$\rho_{VU}\circ\rho_{WV}=\rho_{WU}$$。反变函子的两条公理与层论的这两条要求逐字相同——这正是第 72 章层论的入口。

### Hom 函子与可表函子

**定义 3.5（Hom 函子, Hom functor）** 固定范畴 $$\mathcal{C}$$ 的对象 $$A$$。由 $$A$$ 诱导出一对函子：

$$h^A=\mathcal{C}(A,-):\mathcal{C}\to\mathbf{Set},\qquad X\mapsto\mathcal{C}(A,X),\qquad (f:X\to Y)\mapsto\bigl(g\mapsto f\circ g\bigr),$$

$$h_A=\mathcal{C}(-,A):\mathcal{C}^{\mathrm{op}}\to\mathbf{Set},\qquad X\mapsto\mathcal{C}(X,A),\qquad (f:X\to Y)\mapsto\bigl(g\mapsto g\circ f\bigr).$$

$$h^A$$ 称为**共变 Hom 函子**，$$h_A$$ 称为**反变 Hom 函子**。

**注 3.5（Hom 函子确实是函子）** 保持恒等：$$h^A(1_X)(g)=1_X\circ g=g$$，故 $$h^A(1_X)=1_{\mathcal{C}(A,X)}$$。保持复合：对 $$f:X\to Y$$、$$k:Y\to Z$$ 与任意 $$g\in\mathcal{C}(A,X)$$，

$$h^A(k\circ f)(g)=(k\circ f)\circ g=k\circ(f\circ g)=\bigl(h^A(k)\circ h^A(f)\bigr)(g),$$

故 $$h^A(k\circ f)=h^A(k)\circ h^A(f)$$，复合顺序与 $$\mathcal{C}$$ 中一致。$$h_A$$ 只是把同样的构造搬到 $$\mathcal{C}^{\mathrm{op}}$$ 里做，差别仅在于复合顺序反转——「反变」二字指的就是这件事。

**定义 3.6（可表函子与表示, representable functor / representation）** 设 $$F:\mathcal{C}\to\mathbf{Set}$$ 是函子。若存在对象 $$A$$ 与自然同构

$$\eta:h^A\cong F,$$

则称 $$F$$ 是**可表函子 (representable functor)**，称 $$(A,\eta)$$ 是 $$F$$ 的一个**表示 (representation)**。对反变函子 $$F:\mathcal{C}^{\mathrm{op}}\to\mathbf{Set}$$ 同样定义，只需把 $$h^A$$ 换成 $$h_A$$。

**例 3.7（两个表示）**

(i) **遗忘函子由 $$\mathbb{Z}$$ 表示。** 取 $$U:\mathbf{Grp}\to\mathbf{Set}$$。对任意群 $$G$$，群同态 $$\mathbb{Z}\to G$$ 由 $$1\mapsto g$$ 唯一确定，而 $$g$$ 可以是 $$G$$ 中任何元素，于是 $$\mathbf{Grp}(\mathbb{Z},G)\cong U(G)$$：$$U$$ 是可表函子。而 $$\mathbb{Z}$$ 恰好是自由群 $$F_{\{1\}}$$——(a) 问的「自由在左、遗忘在右」在这里已经露出了影子（见 3.16）。

(ii) **Gelfand 谱由 $$\mathbb{C}$$ 表示。** 取含单位 \*-同态全体 $$\Delta(\mathcal A)=\operatorname{Hom}_{\mathbf{C^*Alg}_1}(\mathcal A,\mathbb{C})$$（即第 40 章的谱），则 $$\Delta=h_{\mathbb{C}}$$ 是反变 Hom 函子，由对象 $$\mathbb{C}$$ 表示。3.23 会把它升级成一对伴随。

**表示的物理读法（接着例 3.7）。** 可表函子 $$\mathcal{C}(A,-)$$ 的本体论是「用 $$A$$ 当探针去量所有对象」：$$\mathbb{Z}$$ 探测群的方式是「取一个元素」，$$\mathbb{C}$$ 探测 C\*-代数的方式是「取一个特征」。**换一个探针，就是换一套物理测量**。

### Yoneda 引理

现在到了本章的中心。Yoneda 引理说的是：**一个预层 $$F$$ 与一个可表预层 $$h_A$$ 之间的全部自然变换，已经被 $$F(A)$$ 这一个集合装下了**——具体地说，被它的一个元素 $$1_A$$ 的像装下了。

**定理 3.8（Yoneda 引理, Yoneda lemma）** 设 $$\mathcal{C}$$ 是范畴，$$A\in\mathcal{C}$$，$$F:\mathcal{C}^{\mathrm{op}}\to\mathbf{Set}$$ 是预层。则映射

$$\alpha:\operatorname{Nat}(h_A,F)\to F(A),\qquad \Phi\mapsto\Phi_A(1_A)$$

是**双射**。共变版本同样成立：对 $$\mathcal{C}$$ 上的函子 $$F$$，

$$\operatorname{Nat}(h^A,F)\cong F(A),\qquad \Phi\mapsto\Phi_A(1_A).$$

**证明思路**：已知 $$\Phi$$ 时，$$\Phi_A(1_A)$$ 当然算得出来——所以 $$\alpha$$ 是良定义的。难的是反方向：只给定一个元素 $$a\in F(A)$$，要**造出**整个自然变换 $$\Phi$$，即对每个对象 $$Y$$ 造出一个映射 $$\Phi_Y:h_A(Y)\to F(Y)$$。关键观察是 $$h_A(Y)=\mathcal{C}(Y,A)$$ 里的每个元素都是态射 $$f:Y\to A$$，而 $$f$$ 又可以由 $$1_A$$ 通过反变 Hom 函子得到：$$f=h_A(f)(1_A)$$。于是自然性方块**逼着** $$\Phi_Y$$ 只能取一个值：

$$\Phi_Y(f)=\Phi_Y\bigl(h_A(f)(1_A)\bigr)=F(f)\bigl(\Phi_A(1_A)\bigr)=F(f)(a).$$

所以定义只能是 $$\Phi_Y(f):=F(f)(a)$$。剩下要做的只是把这个定义真的验一遍。下面把反变版本写全（共变版本把每个 $$F(f)$$ 换成 $$F(f)$$ 的另一侧、把 $$h_A(f)$$ 换成 $$h^A(f)$$，逐字相同）。

**证明** 分四步。

**第一步：构造 $$\beta$$。** 定义

$$\beta:F(A)\to\operatorname{Nat}(h_A,F),\qquad a\mapsto\beta(a),$$

其中 $$\beta(a)$$ 在对象 $$Y\in\mathcal{C}$$ 上的分量是

$$\beta(a)_Y:h_A(Y)\to F(Y),\qquad \beta(a)_Y(f):=F(f)(a)\qquad\bigl(f\in h_A(Y)=\mathcal{C}(Y,A)\bigr).$$

这里的 $$F(f):F(A)\to F(Y)$$ 是反变函子 $$F$$ 在 $$f:Y\to A$$ 上的作用，所以 $$F(f)(a)\in F(Y)$$，类型正确。

**第二步：$$\beta(a)$$ 是自然变换。** 取任意 $$g:Z\to Y$$（$$\mathcal{C}$$ 中态射——注意箭头方向：因为 $$h_A$$、$$F$$ 都是反变函子，方块里从 $$h_A(Y)$$ 出发要落到 $$F(Z)$$，所以取的是"射进 $$Y$$ 的箭头"$$g:Z\to Y$$，而不是从 $$Y$$ 射出）与任意 $$k\in h_A(Y)=\mathcal{C}(Y,A)$$。要验证方块

$$F(g)\circ\beta(a)_Y=\beta(a)_Z\circ h_A(g).$$

左边作用在 $$k$$ 上：$$\beta(a)_Y(k)=F(k)(a)$$，故 $$F(g)\bigl(F(k)(a)\bigr)=F(k\circ g)(a)$$（这里是用了 $$F$$ 反变、把复合反过来：$$F(g)\circ F(k)=F(k\circ g)$$）。右边作用在 $$k$$ 上：$$h_A(g)(k)=k\circ g$$，故 $$\beta(a)_Z(k\circ g)=F(k\circ g)(a)$$。两边都是 $$F(k\circ g)(a)$$，方块交换。

**第三步：$$\alpha\circ\beta=1_{F(A)}$$。** 对任意 $$a\in F(A)$$，

$$\alpha(\beta(a))=\beta(a)_A(1_A)=F(1_A)(a)=1_{F(A)}(a)=a.$$

（第二步与第三步各用了一次反变性的对应条款：函子保恒等、以及复合反序。）

**第四步：$$\beta\circ\alpha=1_{\operatorname{Nat}(h_A,F)}$$。** 设 $$\Phi:h_A\Rightarrow F$$。对任意 $$Y$$ 与任意 $$f\in h_A(Y)$$，由 $$\beta\circ\alpha$$ 的定义

$$(\beta(\alpha(\Phi)))_Y(f)=F(f)\bigl(\Phi_A(1_A)\bigr).$$

另一方面，把 $$\Phi$$ 的自然性方块用在 $$f:Y\to A$$ 上。这个方块的两个顶点是

$$h_A(A)\ \xrightarrow{\ \Phi_A\ }\ F(A),\qquad h_A(Y)\ \xrightarrow{\ \Phi_Y\ }\ F(Y),$$

两条从 $$h_A(A)$$ 绕到 $$F(Y)$$ 的路分别是「先 $$\Phi_A$$ 再 $$F(f)$$」与「先 $$h_A(f)$$ 再 $$\Phi_Y$$」，交换性说的是 $$F(f)\circ\Phi_A=\Phi_Y\circ h_A(f)$$。把 $$1_A\in h_A(A)$$ 代进去：走第一条路得 $$F(f)(\Phi_A(1_A))$$，走第二条路得 $$\Phi_Y\bigl(h_A(f)(1_A)\bigr)=\Phi_Y(f)$$（因为 $$h_A(f)(1_A)=1_A\circ f=f$$）。两条路相等，于是 $$(\beta(\alpha(\Phi)))_Y(f)=\Phi_Y(f)$$。$$Y$$ 与 $$f$$ 任意，故 $$\beta(\alpha(\Phi))=\Phi$$。

结合第三、四步，$$\alpha$$ 与 $$\beta$$ 互为逆映射，$$\alpha$$ 是双射。$$\blacksquare$$

**注 3.8（为什么偏偏是 $$1_A$$）** 定理 3.8 的证明里有一步是全章的钥匙：$$h_A(f)(1_A)=1_A\circ f=f$$。集合 $$\mathcal{C}(A,A)$$ 里有很多元素，但只有 $$1_A$$ 具有这个性质——因为它对每一个 $$f$$ 都被 $$h_A(f)$$ **搬到 $$f$$ 本身**。换句话说，$$1_A$$ 是 $$h_A$$ 上那个「被所有 $$h_A(f)$$ 一致搬运的通用元素」。这就是为什么 $$\Phi$$ 这个自然变换整个被 $$\Phi_A(1_A)$$ 决定：其余分量全由自然性从这一个值推出来，而自然性只有一条路可走。

**例 3.8（矩阵版 Yoneda：入口题 (c) 的核心）** 取 $$\mathcal{C}=\mathfrak{m}\text{-}\mathbf{Mod}$$、$$A=\mathbb{K}^{m\times n}$$、$$B=\mathbb{K}^{m\times n'}$$。则 $$h_A$$ 把态射 $$f$$ 送到「右乘 $$f$$」，于是

$$\operatorname{Nat}(h_A,h_B)\cong h_B(A)=\operatorname{Hom}_{\mathfrak{m}-}(A,B)\cong\mathbb{K}^{n\times n'},$$

也就是说：**$$A$$ 与 $$B$$ 之间所有的自然变换，恰好由右乘一个 $$\mathbb{K}^{n\times n'}$$ 矩阵给出**，且这个矩阵唯一。这就是入口题 (c) 的答案——(c) 里「两个对象被所有 Hom 集相同地探测」对应的正是矩阵 $$\mathbb{K}^{n\times n}$$ 里的可逆元，而「探测起来一样」与「对象一样」在这里是同一句话。

### Yoneda 嵌入及其推论

**推论 3.9（Yoneda 嵌入, Yoneda embedding）** 对每个 $$A\in\mathcal{C}$$ 有 $$\mathcal{C}$$ 上的预层 $$h_A$$，并且 $$A\mapsto h_A$$ 延拓成一个**全忠实函子**

$$Y:\mathcal{C}\to\hat{\mathcal{C}}=[\mathcal{C}^{\mathrm{op}},\mathbf{Set}],\qquad A\mapsto h_A,$$

其中 $$Y$$ 在态射上的作用为

$$(f:A\to B)\ \mapsto\ \bigl(Yf\bigr):h_A\Rightarrow h_B,\qquad (Yf)_X:h_A(X)=\mathcal{C}(X,A)\to h_B(X)=\mathcal{C}(X,B),\quad g\mapsto f\circ g.$$

称 $$Y$$ 为 **Yoneda 嵌入 (Yoneda embedding)**，它是「全忠实」的，意思是：对每对 $$A,B$$，映射

$$Y_{A,B}:\mathcal{C}(A,B)\to\operatorname{Nat}(h_A,h_B),\qquad f\mapsto Yf$$

是双射。

**证明** 三件事。

(i) **$$Y$$ 是函子。** 恒等：$$(Y1_A)_X(g)=1_A\circ g=g$$，故 $$Y1_A=1_{h_A}$$。复合：对 $$h:A\to B$$、$$f:B\to C$$、$$g\in\mathcal{C}(X,A)$$，
$$(Y(f\circ h))_X(g)=(f\circ h)\circ g=f\circ(h\circ g)=(Yf)_X\bigl((Yh)_X(g)\bigr)=\bigl((Yf)\circ(Yh)\bigr)_X(g),$$
故 $$Y(f\circ h)=Yf\circ Yh$$，与 $$\mathcal{C}$$ 中复合顺序一致。

(ii) **单（faithful）。** 设 $$Yf=Yg$$（$$f,g:A\to B$$）。分别作用在 $$X=A$$ 上、再作用在 $$1_A$$：$$(Yf)_A(1_A)=f\circ1_A=f$$，$$(Yg)_A(1_A)=g$$。两者相等，故 $$f=g$$。

(iii) **满（full）。** 设 $$\Phi:h_A\Rightarrow h_B$$ 是任一自然变换。取 $$f:=\Phi_A(1_A)\in h_B(A)=\mathcal{C}(A,B)$$。由定理 3.8 的第四步，整个 $$\Phi$$ 由 $$\Phi_A(1_A)$$ 决定，而 $$\beta(\Phi_A(1_A))$$ 就是 $$\Phi$$；再注意 $$\beta(a)$$ 的定义 $$\beta(a)_X(g)=h_B(g)(a)=a\circ g$$，取 $$a=f$$ 得 $$\beta(f)_X(g)=f\circ g=(Yf)_X(g)$$，即 $$\beta(f)=Yf$$。所以 $$\Phi=Yf$$。

三件事合起来，$$Y$$ 是全忠实函子。$$\blacksquare$$

**推论 3.10（对象由可表函子决定）** 对 $$A,B\in\mathcal{C}$$，

$$A\cong B\qquad\Longleftrightarrow\qquad h_A\cong h_B.$$

特别地，$$h_A\cong h_B$$ 时，给出这个自然同构的态射 $$A\to B$$ 在同构意义下唯一。

**证明** ($$\Rightarrow$$) 若 $$f:A\to B$$ 是同构，设 $$g:B\to A$$ 是它的逆。由 $$Y$$ 是函子，$$Yf\circ Yg=Y(f\circ g)=Y1_B=1_{h_B}$$，$$Yg\circ Yf=1_{h_A}$$，故 $$Yf$$ 是同构。

($$\Leftarrow$$) 设 $$\Phi:h_A\cong h_B$$ 自然同构，逆为 $$\Psi$$。由推论 3.9(iii) 的满性，存在 $$f:A\to B$$ 与 $$g:B\to A$$ 使 $$Yf=\Phi$$、$$Yg=\Psi$$。于是

$$Y(f\circ g)=Yf\circ Yg=\Phi\circ\Psi=1_{h_B}=Y1_B,$$

由推论 3.9(ii) 的单性得 $$f\circ g=1_B$$；同理 $$g\circ f=1_A$$。故 $$f$$ 是同构，$$A\cong B$$。「唯一性」：任何给出 $$\Phi$$ 的态射必满足 $$f=\Phi_A(1_A)$$，所以它就是上面这一个。$$\blacksquare$$

**推论 3.11（表示的唯一性）** 设 $$F:\mathcal{C}^{\mathrm{op}}\to\mathbf{Set}$$ 有两个表示 $$(A,\eta)$$ 与 $$(B,\theta)$$（即 $$\eta:h_A\cong F$$，$$\theta:h_B\cong F$$）。则存在同构 $$f:A\to B$$，使 $$\eta=\theta\circ Yf$$；并且这个 $$f$$ 是唯一的。

**证明** 令 $$\Phi:=\theta^{-1}\circ\eta$$，则 $$\Phi:h_A\cong h_B$$ 是自然同构。由推论 3.10 的证明取 $$f:=\Phi_A(1_A)\in\mathcal{C}(A,B)$$，得 $$Yf=\Phi$$，于是 $$\theta\circ Yf=\theta\circ\theta^{-1}\circ\eta=\eta$$。唯一性：给出 $$\Phi$$ 的态射只能是 $$\Phi_A(1_A)$$，故 $$f$$ 唯一。$$\blacksquare$$

**推论 3.12（万有元, universal element）** 设 $$F:\mathcal{C}^{\mathrm{op}}\to\mathbf{Set}$$，$$A\in\mathcal{C}$$，并令 $$x:=\Phi_A(1_A)\in F(A)$$ 对应自然变换 $$\Phi:h_A\Rightarrow F$$（定理 3.8）。则 $$\Phi$$ 是自然同构，当且仅当 $$x$$ 满足：

**对每个 $$X\in\mathcal{C}$$ 与每个 $$y\in F(X)$$，存在唯一的态射 $$f:X\to A$$ 使 $$F(f)(x)=y$$。**

满足此条件的 $$x$$ 称为 $$\mathcal{C}$$ 中 $$F$$ 的**万有元 (universal element)**。

**证明** 对任意 $$X$$，"$$\Phi$$ 是自然同构"等价于"每个分量 $$\Phi_X:h_A(X)\to F(X)$$ 是双射"。而由定理 3.8 第四步中间的同一个计算，

$$\Phi_X(f)=F(f)(x)\qquad\text{对一切}\ f\in h_A(X)=\mathcal{C}(X,A).$$

于是 $$\Phi_X$$ 是双射，等价于：对每个 $$y\in F(X)$$，集合 $$\{f\in\mathcal{C}(X,A):F(f)(x)=y\}$$ 恰有一个元素。这正是要证的。$$\blacksquare$$

### 伴随函子：Hom 集刻画

有了 Yoneda,「同构」这件事就可以用「被所有 Hom 集探测的结果相同」来验证。伴随的定义正是这么写的。

**定义 3.13（伴随函子, adjoint functor）** 设 $$F:\mathcal{C}\to\mathcal{D}$$、$$G:\mathcal{D}\to\mathcal{C}$$ 是函子。若对每对对象 $$c\in\mathcal{C}$$、$$d\in\mathcal{D}$$ 给定一个双射

$$\varphi_{c,d}:\mathcal{D}(Fc,d)\ \xrightarrow{\ \cong\ }\ \mathcal{C}(c,Gd),$$

使得 $$\varphi_{c,d}$$ 对 $$c$$ 与 $$d$$ **都自然**（对 $$c$$ 反变、对 $$d$$ 协变，也就是下一条定理里要写出来的那两条交换律），则称 $$F$$ 是 $$G$$ 的**左伴随 (left adjoint)**，$$G$$ 是 $$F$$ 的**右伴随 (right adjoint)**，记作

$$F\dashv G.$$

定义 3.13 里的 $$\varphi_{c,d}$$ 是"对每一对 $$(c,d)$$ 各给一个双射"，用起来要不断指名 $$c,d$$，不方便。但双射一族里最特殊的一次取值，是**把 $$d$$ 取成 $$Fc$$ 自己**（这时 $$\mathcal{D}(Fc,Fc)$$ 里有一个免费的恒等态射 $$1_{Fc}$$ 可以代进去）、或**把 $$c$$ 取成 $$Gd$$ 自己**（这时 $$\mathcal{C}(Gd,Gd)$$ 里有免费的 $$1_{Gd}$$）。这两次特殊取值各给出一个自然变换，且后面会看到：只要知道这两个自然变换，就能把整族 $$\varphi_{c,d}$$ 重新算回来（定理 3.15）——于是它们才是伴随里"真正独立"的数据。

**定义 3.14（单位与余单位, unit and counit）** 在 $$F\dashv G$$ 中，把恒等态射分别放进 $$\varphi$$：

$$\eta_c:=\varphi_{c,Fc}(1_{Fc}):c\to GFc,\qquad \varepsilon_d:=\varphi_{Gd,d}^{-1}(1_{Gd}):FGd\to d.$$

$$\eta:1_{\mathcal{C}}\Rightarrow GF$$ 称为**单位 (unit)**，$$\varepsilon:FG\Rightarrow1_{\mathcal{D}}$$ 称为**余单位 (counit)**。

**定理 3.15（伴随的等价刻画与三角恒等式, triangle identities）** 设 $$F:\mathcal{C}\to\mathcal{D}$$、$$G:\mathcal{D}\to\mathcal{C}$$ 是函子，$$\eta:1_{\mathcal{C}}\Rightarrow GF$$、$$\varepsilon:FG\Rightarrow1_{\mathcal{D}}$$ 是自然变换。则下列两条等价：

(A) 存在定义 3.13 意义下的伴随 $$F\dashv G$$，且它的单位、余单位恰为 $$\eta$$、$$\varepsilon$$；

(B) $$\eta$$、$$\varepsilon$$ 满足两条**三角恒等式**

$$(\varepsilon F)\circ(F\eta)=1_F,\qquad (G\varepsilon)\circ(\eta G)=1_G.$$

所谓 $$F\eta$$，指的是水平复合：$$(F\eta)_c=F(\eta_c):Fc\to FGFc$$，而 $$(\varepsilon F)_c=\varepsilon_{Fc}:FGFc\to Fc$$；$$(\eta G)_d=\eta_{Gd}:Gd\to GFGd$$，$$(G\varepsilon)_d=G(\varepsilon_d):GFGd\to Gd$$。

**证明** (A)$$\Rightarrow$$(B)：由定义 3.14，$$\eta_c=\varphi_{c,Fc}(1_{Fc})$$、$$\varepsilon_d=\varphi_{Gd,d}^{-1}(1_{Gd})$$。把 $$\varepsilon_d=\varphi^{-1}(1_{Gd})$$ 两边作用 $$\varphi$$，得

$$\varphi_{Gd,d}(\varepsilon_d)=1_{Gd}.$$

现在算 $$\varphi_{Gd,d}(\varepsilon_d)$$ 是什么。固定 $$c=Gd$$、$$d=d$$，对第一个变量用自然性：设 $$f:F(Gd)\to d$$ 是任意态射，则 $$\varphi_{Gd,d}(f)=\varphi_{Gd,d}\bigl(f\circ 1_{FGd}\bigr)=G(f)\circ\varphi_{Gd,FGd}(1_{FGd})=G(f)\circ\eta_{Gd}$$。取 $$f=\varepsilon_d$$：

$$1_{Gd}=\varphi_{Gd,d}(\varepsilon_d)=G(\varepsilon_d)\circ\eta_{Gd}=(G\varepsilon)_d\circ(\eta G)_d=(G\varepsilon\circ\eta G)_d.$$

此式对一切 $$d$$ 成立，即 $$(G\varepsilon)\circ(\eta G)=1_G$$——这是第二条。

第一条要用到 $$\varphi^{-1}_{c,d}$$ 的一个通用公式，先把它单独推出来。取任意 $$c,d$$ 与任意 $$h:c\to Gd$$。由 $$\varphi$$ 对第一个变量的自然性（把 $$c$$ 换成 $$Gd$$、态射取 $$h:c\to Gd$$、第二个变量固定为 $$d$$，第一个分量取 $$f=\varepsilon_d:F(Gd)\to d$$）：

$$\varphi_{c,d}\bigl(\varepsilon_d\circ F(h)\bigr)=\varphi_{Gd,d}(\varepsilon_d)\circ h.$$

上一段已经算出 $$\varphi_{Gd,d}(\varepsilon_d)=1_{Gd}$$，代入右边得 $$\varphi_{c,d}\bigl(\varepsilon_d\circ F(h)\bigr)=1_{Gd}\circ h=h$$。这对一切 $$h:c\to Gd$$ 成立，即 $$\varphi_{c,d}$$ 把 $$\varepsilon_d\circ F(h)$$ 送回 $$h$$ 本身；两边取 $$\varphi_{c,d}^{-1}$$（$$\varphi_{c,d}$$ 是双射，逆映射存在）：

$$\varphi_{c,d}^{-1}(h)=\varepsilon_d\circ F(h)\qquad\text{对一切}\ c,d,h.$$

这正是下面 (B)$$\Rightarrow$$(A) 里 $$\psi_{c,d}$$ 的公式——这里独立推出，不必等到那一步。现在取 $$c=c$$、$$d=Fc$$、$$h=\eta_c$$：由 $$\eta_c=\varphi_{c,Fc}(1_{Fc})$$ 得 $$\varphi_{c,Fc}^{-1}(\eta_c)=1_{Fc}$$；另一方面由刚推出的公式 $$\varphi_{c,Fc}^{-1}(\eta_c)=\varepsilon_{Fc}\circ F(\eta_c)$$。两式的左边都是 $$\varphi_{c,Fc}^{-1}(\eta_c)$$，故右边相等，即

$$1_{Fc}=\varepsilon_{Fc}\circ F(\eta_c)=(\varepsilon F)_c\circ(F\eta)_c,$$

对一切 $$c$$ 成立，即 $$(\varepsilon F)\circ(F\eta)=1_F$$。

(B)$$\Rightarrow$$(A)：反之设 $$\eta,\varepsilon$$ 自然并满足三角恒等式。对 $$f:Fc\to d$$ 与 $$g:c\to Gd$$ 定义

$$\varphi_{c,d}(f):=G(f)\circ\eta_c,\qquad \psi_{c,d}(g):=\varepsilon_d\circ F(g).$$

**$$\varphi$$ 与 $$\psi$$ 互逆。** 对 $$f:Fc\to d$$，
$$\psi\varphi(f)=\varepsilon_d\circ F\bigl(G(f)\circ\eta_c\bigr)=\varepsilon_d\circ FG(f)\circ F(\eta_c)\ \overset{\varepsilon\ \text{自然}}{=}\ f\circ\varepsilon_{Fc}\circ F(\eta_c)=f\circ(\varepsilon F)_c\circ(F\eta)_c=f\circ1_{Fc}=f.$$
（第二步用了 $$\varepsilon$$ 在态射 $$f:Fc\to d$$ 上的自然性：$$\varepsilon_d\circ FG(f)=f\circ\varepsilon_{Fc}$$。）对 $$g:c\to Gd$$，用 $$\eta$$ 在 $$g$$ 上的自然性 $$\eta_{Gd}\circ g=GF(g)\circ\eta_c$$：
$$\varphi\psi(g)=G\bigl(\varepsilon_d\circ F(g)\bigr)\circ\eta_c=G(\varepsilon_d)\circ GF(g)\circ\eta_c=G(\varepsilon_d)\circ\eta_{Gd}\circ g=(G\varepsilon)_d\circ(\eta G)_d\circ g=1_{Gd}\circ g=g.$$

**$$\varphi$$ 对 $$d$$ 自然。** 取 $$k:d\to d'$$。要证 $$\varphi_{c,d'}(k\circ f)=\varphi_{c,d}(f)\circ Gk$$：
$$\varphi_{c,d'}(k\circ f)=G(k\circ f)\circ\eta_c=G(k)\circ G(f)\circ\eta_c=G(k)\circ\varphi_{c,d}(f).$$
右边两式相等（$$\mathcal{C}$$ 中箭头从 $$c$$ 到 $$Gd'$$）。

**$$\varphi$$ 对 $$c$$ 自然。** 取 $$h:c'\to c$$。要证 $$\varphi_{c',d}\bigl(f\circ Fh\bigr)=\varphi_{c,d}(f)\circ h$$：
$$\varphi_{c',d}(f\circ Fh)=G(f\circ Fh)\circ\eta_{c'}=G(f)\circ GF(h)\circ\eta_{c'}\ \overset{\eta\ \text{自然}}{=}\ G(f)\circ\eta_c\circ h=\varphi_{c,d}(f)\circ h.$$
（第二步用了 $$\eta$$ 在 $$h$$ 上的自然性 $$GF(h)\circ\eta_{c'}=\eta_c\circ h$$。）于是 $$\varphi$$ 对 $$c$$ 与 $$d$$ 都自然，$$F\dashv G$$ 成立。$$\blacksquare$$

**注 3.15（两个定义的分工）** Hom 集刻画便于**验证**（写出显式双射就够了），单位—余单位刻画便于**使用**（$$\eta$$、$$\varepsilon$$ 是具体的自然变换，三角恒等式是具体的等式）。本章两种都用：3.16—3.18 用前者，3.19 以后用后者。

### 三对伴随

**例 3.16（自由 ⊣ 遗忘, free ⊣ forgetful）** 这是入口题 (a) 的完整答案。

**(i) 模的情形。** 设 $$R$$ 是环，$$U:R\text{-}\mathbf{Mod}\to\mathbf{Set}$$ 是遗忘函子，$$F:\mathbf{Set}\to R\text{-}\mathbf{Mod}$$ 是自由模函子
$$F(S):=R^{(S)}=\bigoplus_{s\in S}R,$$
即「以 $$S$$ 为基」的自由 $$R$$-模（特别地 $$R^{(\varnothing)}=0$$、$$R^{(\{1\})}=R$$）。设 $$\iota:S\to U F(S)$$ 是把 $$s$$ 送到第 $$s$$ 个坐标上的基元素 $$e_s$$ 的映射。则 $$F\dashv U$$，伴随同构是

$$\varphi_{S,M}:\operatorname{Hom}_{R}\bigl(R^{(S)},M\bigr)\ \xrightarrow{\ \cong\ }\ \operatorname{Hom}_{\mathbf{Set}}\bigl(S,U(M)\bigr),\qquad f\mapsto f\circ\iota.$$

**证明** 造逆映射 $$\psi$$：给定集合映射 $$g:S\to U(M)$$，在基上令 $$\psi(g)(e_s):=g(s)$$——由于 $$R$$-线性映射由基上的值唯一决定，这句话已经完整地定义了 $$\psi(g):R^{(S)}\to M$$。则

$$\varphi(\psi(g))(s)=(\psi(g)\circ\iota)(s)=\psi(g)(e_s)=g(s),$$

故 $$\varphi\psi(g)=g$$；反过来 $$\psi(\varphi(f))$$ 与 $$f$$ 在基 $$\{e_s\}$$ 上取同一个值，由唯一性得 $$\psi(\varphi(f))=f$$。所以 $$\varphi$$ 是双射。自然性：对 $$R$$-线性 $$k:M\to M'$$，$$\varphi(k\circ f)=k\circ f\circ\iota=k\circ\varphi(f)=\operatorname{Hom}(S,Uk)\bigl(\varphi(f)\bigr)$$，对集合映射 $$g$$ 的情形同理。故 $$\varphi$$ 对 $$M$$ 与 $$S$$ 都自然，$$F\dashv U$$。$$\blacksquare$$

这里的单位是 $$\eta_S=\varphi(1_{R^{(S)}})=\iota:S\to U F(S)$$——它就是「$$S$$ 是一组基」这句话；余单位是 $$\varepsilon_M=\psi^{-1}(1_{U(M)})$$，即把 $$\bigoplus_{s\in M}R$$ 按坐标线性组合送回 $$M$$ 的求和映射。

**(ii) 群的情形（入口题 (a)）。** 设 $$F_S$$ 是 $$S$$ 上的自由群（元素是约化字，乘法是拼接后约化），$$U:\mathbf{Grp}\to\mathbf{Set}$$ 是遗忘函子，$$\iota:S\to U F_S$$ 是标准包含。则 $$F\dashv U$$，同构为

$$\varphi_{S,G}:\operatorname{Hom}_{\mathbf{Grp}}\bigl(F_S,G\bigr)\ \xrightarrow{\ \cong\ }\ \operatorname{Hom}_{\mathbf{Set}}\bigl(S,U(G)\bigr),\qquad \varphi\mapsto\varphi\circ\iota.$$

**证明** 同样造逆。给定任意映射 $$f:S\to U(G)$$，定义 $$\psi(f):F_S\to G$$ 在约化字上为

$$\psi(f)\bigl(s_1^{\epsilon_1}s_2^{\epsilon_2}\cdots s_n^{\epsilon_n}\bigr):=f(s_1)^{\epsilon_1}f(s_2)^{\epsilon_2}\cdots f(s_n)^{\epsilon_n}\qquad(\epsilon_i=\pm1,\ s_i\in S,\ s_i\ne s_{i+1}).$$

**良定义与同态性**：约定空字映到单位元。拼接两个字再约化时，被消去的每一对相邻的 $$ss^{-1}$$ 或 $$s^{-1}s$$ 在右边贡献 $$f(s)f(s)^{-1}=e$$ 或 $$f(s)^{-1}f(s)=e$$，所以整个乘积的值不变；又因为约化字的乘法是「拼接 + 反复消去」，任何两个字 $$w,w'$$ 都有 $$\psi(f)(ww')=\psi(f)(w)\psi(f)(w')$$——归约过程不改变值，而右端在拼接时正好相乘。故 $$\psi(f)$$ 是群同态。于是 $$\varphi\psi(f)=f$$（在单个元素 $$s$$ 上：$$\psi(f)(s)=f(s)$$），$$\psi\varphi(\varphi_0)=\varphi_0$$（两边在生成元 $$S$$ 上取值相同，而同态由生成元的像唯一决定——这条唯一性正是「约化字表示法」的效力）。自然性逐字同上。所以 $$F\dashv U$$。$$\blacksquare$$

**注 3.16（(a) 问里那个「落差」被什么吃掉了）** 入口题 (a) 问：右边无条件、左边要满足三条公理，为什么能一一对应？答案是**唯一性**把公理吸收了：任意映射都能**唯一地**延拓成同态，因为生成元上的值必须决定一切。用 3.15 的语言说，单位 $$\eta_S=\iota$$ 是一族**单射**，而余单位 $$\varepsilon_G$$ 把「以 $$G$$ 为生成元集合的自由群」压回 $$G$$。**「自由」与「唯一延拓」是同一件事的两种说法**——这是 (d) 问那个共同形状的第一块拼图。

**定理 3.17（张量–Hom 伴随, tensor–Hom adjunction）** 设 $$R,S$$ 是环，$$C$$ 是一个 $$(S,R)$$-双模（左 $$S$$、右 $$R$$），$$A$$ 是左 $$R$$-模，$$B$$ 是左 $$S$$-模。则映射

$$\Phi:\operatorname{Hom}_{S}\bigl(C\otimes_R A,\ B\bigr)\ \longrightarrow\ \operatorname{Hom}_{R}\Bigl(A,\ \operatorname{Hom}_{S}(C,B)\Bigr),\qquad \Phi(f)(a)(c):=f(c\otimes a)$$

是自然双射。因此

$$C\otimes_R-\ \dashv\ \operatorname{Hom}_{S}(C,-),$$

即左伴随是「取模 $$C$$ 的张量函子」，右伴随是「取模 $$C$$ 的 Hom 函子」。**这正是第 64 章末尾点明、留到本章兑现的那一对**：ch32 已经算清了这两个函子各保正合性的一半，本章给出的是「它们为什么成对」的答案。

**证明** 分四步。**(以下默认第 64 章的结论：$$C\otimes_R A$$ 由双线性映射的万有性质刻画，任一 $$R$$-平衡、双可加的映射 $$\beta:A\times C\to B$$ 都唯一过 $$A\otimes_R C$$ 或 $$C\otimes_R A$$ 分解。)**

**(i) $$\Phi$$ 良定义、类型正确。** 固定 $$f\in\operatorname{Hom}_S(C\otimes_R A,B)$$。对固定 $$a$$，映射 $$c\mapsto f(c\otimes a)$$ 是 $$S$$-线性的：$$f(sc\otimes a)=f(s\cdot(c\otimes a))=s\cdot f(c\otimes a)$$（$$C\otimes_R A$$ 上 $$S$$ 的作用是 $$s(c\otimes a):=(sc)\otimes a$$，与 $$A$$ 无关）。对固定 $$c$$，映射 $$a\mapsto f(c\otimes a)$$ 是加性的。最后验证 $$a\mapsto\Phi(f)(a)$$ 是 $$R$$-线性的：因为 $$\operatorname{Hom}_S(C,B)$$ 上的左 $$R$$-作用定义为 $$(r\psi)(c):=\psi(cr)$$，而对 $$r\in R$$，

$$\Phi(f)(ra)(c)=f(c\otimes ra)=f((cr)\otimes a)=\Phi(f)(a)(cr)=\bigl(r\cdot\Phi(f)(a)\bigr)(c),$$

故 $$\Phi(f)(ra)=r\cdot\Phi(f)(a)$$。

**(ii) 构造逆 $$\Psi$$。** 给定 $$g\in\operatorname{Hom}_R\bigl(A,\operatorname{Hom}_S(C,B)\bigr)$$，先在一对元素上定义

$$\beta:A\times C\to B,\qquad \beta(a,c):=g(a)(c).$$

$$\beta$$ 是 $$R$$-**平衡**的、且对两个变量分别可加：

$$\beta(ra,c)=g(ra)(c)=\bigl(r\cdot g(a)\bigr)(c)=g(a)(cr)=\beta(a,cr),$$

$$\beta(a+a',c)=\bigl(g(a)+g(a')\bigr)(c)=\beta(a,c)+\beta(a',c),\qquad \beta(a,c+c')=g(a)(c+c')=\beta(a,c)+\beta(a,c').$$

由张量积的万有性质，$$\beta$$ 唯一分解出一个映射 $$\Psi(g):C\otimes_R A\to B$$，满足 $$\Psi(g)(c\otimes a)=\beta(a,c)=g(a)(c)$$。它还是 $$S$$-线性的：$$\Psi(g)\bigl(s(c\otimes a)\bigr)=\Psi(g)\bigl((sc)\otimes a\bigr)=g(a)(sc)=s\cdot g(a)(c)=s\cdot\Psi(g)(c\otimes a)$$（用了 $$g(a)\in\operatorname{Hom}_S(C,B)$$）。故 $$\Psi(g)\in\operatorname{Hom}_S(C\otimes_R A,B)$$。

**(iii) $$\Phi\Psi=1$$、$$\Psi\Phi=1$$。** 在生成元上验：$$\Phi(\Psi(g))(a)(c)=\Psi(g)(c\otimes a)=g(a)(c)$$，故 $$\Phi(\Psi(g))=g$$；$$\Psi(\Phi(f))(c\otimes a)=\Phi(f)(a)(c)=f(c\otimes a)$$，由于形如 $$c\otimes a$$ 的元素张成 $$C\otimes_R A$$、且两边都是加性映射，故 $$\Psi(\Phi(f))=f$$。所以 $$\Phi$$ 是双射。

**(iv) 自然性。** 对 $$k:B\to B'$$：$$\Phi(k\circ f)(a)(c)=k\bigl(f(c\otimes a)\bigr)=\bigl(\operatorname{Hom}_S(C,k)(\Phi(f)(a))\bigr)(c)$$，故 $$\Phi(k\circ f)=\operatorname{Hom}_S(C,k)\circ\Phi(f)$$。对 $$h:A'\to A$$（记 $$1\otimes h:C\otimes_R A'\to C\otimes_R A$$）：

$$\Phi\bigl(f\circ(1\otimes h)\bigr)(a')(c)=f\bigl(c\otimes h(a')\bigr)=\Phi(f)\bigl(h(a')\bigr)(c)=\bigl(\Phi(f)\circ h\bigr)(a')(c),$$

注意 $$\operatorname{Hom}_S(C,B)$$ 上对 $$h$$ 的反变作用就是「先 $$h$$ 再取 $$\operatorname{Hom}$$」，两边一致。$$\blacksquare$$

**注 3.17（入口题 (b) 的完整答案）** 在 (b) 里取 $$R=S=\mathbb{Z}$$、$$C=\mathbb{Z}/2$$（它同时是左、右 $$\mathbb{Z}$$-模，因为交换环上的模自动是双模）、$$A=B=\mathbb{Z}/2$$。定理 3.17 给出

$$\operatorname{Hom}_{\mathbb{Z}}\bigl(\mathbb{Z}/2\otimes_{\mathbb{Z}}\mathbb{Z}/2,\ \mathbb{Z}/2\bigr)\cong\operatorname{Hom}_{\mathbb{Z}}\Bigl(\mathbb{Z}/2,\ \operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2)\Bigr).$$

两边各算：左边 $$\mathbb{Z}/2\otimes\mathbb{Z}/2\cong\mathbb{Z}/2$$，而 $$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2)=\{0,\mathrm{id}\}\cong\mathbb{Z}/2$$；右边内层同样得 $$\mathbb{Z}/2$$，再取一次 $$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2)\cong\mathbb{Z}/2$$。两个都是 2 元集，对应方式是 $$\Phi$$ 的那条公式

$$f\ \longmapsto\ \bigl(a\mapsto(c\mapsto f(c\otimes a))\bigr).$$

也就是说：**「在张量积上定义的线性映射」与「把第一个变量送成一个映射、再由它吃掉第二个变量」是同一个东西**——它就是编程里的 curry 化，在代数里叫张量–Hom 伴随。这里 $$\Phi$$ 对一切环 $$R,S$$ 与一切双模 $$C$$ 都成立，(b) 只是它在一个 2 元集上的样本。

**例 3.18（$$\Sigma\dashv\Omega$$：悬挂与环路空间）** 定理 3.17 的形状在拓扑里有逐字对应，只是把 $$\otimes$$ 换成 **smash 积** $$\wedge$$、把 Hom 换成**带基点映射空间**。

记 $$\mathbf{Top}_*$$ 为带基点拓扑空间的范畴，$$[X,Y]_*$$ 为保基点映射的同伦类集合。定义**约化悬挂 (reduced suspension)** 与**环路空间 (loop space)**

$$\Sigma X:=X\wedge S^1,\qquad \Omega Y:=\operatorname{Map}_*\bigl((S^1,1),\ (Y,y_0)\bigr),$$

则对一切 $$X,Y\in\mathbf{Top}_*$$ 有自然双射

$$[\Sigma X,\ Y]_*\cong[X,\ \Omega Y]_*,$$

即 $$\Sigma\dashv\Omega$$。这里「自然双射」取的是同伦类层面的（同伦论里同伦类才是真正的态射）。它和 3.17 的关系是：两者都是「张量 ⊣ Hom」在具体幺半范畴里的实现。（拓扑里还有一个同形状的实例：**离散拓扑**函子是遗忘函子 $$\mathbf{Top}\to\mathbf{Set}$$ 的左伴随。对照例 3.22 会看到群遗忘函子只有一半。）

### 左伴随保余极限、右伴随保极限

现在用 Yoneda 把伴随的全部力量逼出来。核心是一条关于 Hom 函子的老事实（第 62 章的**Hom 保极限**），我们把它写成交警力可用的形式。

**定理 3.19（Hom 保极限, Hom preserves limits）** 设 $$D:J\to\mathcal{C}$$ 是小图（$$J$$ 是小范畴），$$c\in\mathcal{C}$$，并设 $$\lim_j D_j$$ 存在。则

$$\mathcal{C}\Bigl(c,\ \lim_j D_j\Bigr)\cong\lim_j\mathcal{C}(c,D_j),$$

同构为**典范**同构（不依赖任何选择）。对偶地，反变 Hom 把余极限送成极限：

$$\mathcal{C}\Bigl(\operatorname{colim}_j D_j,\ c\Bigr)\cong\lim_j\mathcal{C}(D_j,c).$$

**证明** 用锥的语言。一个以 $$c$$ 为顶点的锥就是从 $$c$$ 出发的一族态射 $$u_j:c\to D_j$$，使得对 $$J$$ 中每条态射 $$\alpha:j\to j'$$ 都有 $$D(\alpha)\circ u_j=u_{j'}$$。把每个 $$j$$ 换成集合 $$\mathcal{C}(c,D_j)$$：上述条件恰好是「$$u_j\in\mathcal{C}(c,D_j)$$ 的像在把 $$\mathcal{C}(c,D_\alpha)$$ 作用后彼此相容」，也就是集合值函子 $$j\mapsto\mathcal{C}(c,D_j)$$ 的一条**极限元素**（在 $$\mathbf{Set}$$ 里，极限就是相容族全体，逐分量定义）。于是

$$\{\text{以 }c\text{ 为顶点、到 }D\text{ 的锥}\}\ =\ \lim_j\mathcal{C}(c,D_j).$$

另一方面，$$\lim D$$ 的万有性质说：以 $$c$$ 为顶点到 $$D$$ 的锥与单个态射 $$c\to\lim D$$ **一一对应**（存在且分解唯一）。两条一比，得到 $$\mathcal{C}(c,\lim D)\cong\lim_j\mathcal{C}(c,D_j)$$，且对应就是把每个锥换成它穿过极限的那条唯一态射——这是由万有性质唯一确定的对应，故是典范的。反变命题是把上面整段论证在 $$\mathcal{C}^{\mathrm{op}}$$ 里重做一遍。$$\blacksquare$$

**定理 3.20（右伴随保极限, right adjoints preserve limits）** 设 $$F\dashv G$$，$$F:\mathcal{C}\to\mathcal{D}$$、$$G:\mathcal{D}\to\mathcal{C}$$。若 $$D:J\to\mathcal{D}$$ 有极限，则 $$G\circ D$$ 有极限，且存在典范同构

$$G\Bigl(\lim_j D_j\Bigr)\cong\lim_j G(D_j).$$

**证明** 只需对每个 $$c\in\mathcal{C}$$ 算 Hom 集，再用 Yoneda 收口。链是

$$\mathcal{C}\Bigl(c,\ G\bigl(\lim_j D_j\bigr)\Bigr)\cong\mathcal{D}\Bigl(Fc,\ \lim_j D_j\Bigr)\cong\lim_j\mathcal{D}\bigl(Fc,D_j\bigr)\cong\lim_j\mathcal{C}\bigl(c,G(D_j)\bigr)\cong\mathcal{C}\Bigl(c,\ \lim_j G(D_j)\Bigr).$$

四步的依据分别是：伴随同构（定义 3.13，$$\varphi_{c,\lim D}$$）；定理 3.19（Hom 保极限，取 $$\mathcal{C}$$ 换成 $$\mathcal{D}$$、$$c$$ 换成 $$Fc$$）；对每个 $$j$$ 用一次伴随同构（相容性由 $$\varphi$$ 的自然性保证，所以整族同构可以同时取）；再用一次定理 3.19（取图 $$G\circ D$$）。每个同构都对 $$c$$ 自然，故这给出反变 Hom 函子之间的自然同构

$$h_{G(\lim D)}=\mathcal{C}\bigl(-,G(\lim D)\bigr)\cong\mathcal{C}\bigl(-,\lim G(D)\bigr)=h_{\lim G(D)}.$$

由推论 3.10（对象由可表函子决定），$$G(\lim D)\cong\lim G(D)$$。$$\blacksquare$$

**定理 3.21（左伴随保余极限, left adjoints preserve colimits）** 设 $$F\dashv G$$，$$D:J\to\mathcal{C}$$ 有余极限，则 $$F\circ D$$ 有余极限，且

$$F\Bigl(\operatorname{colim}_j D_j\Bigr)\cong\operatorname{colim}_j F(D_j).$$

**证明** 与定理 3.20 的证明对偶，但这次用反变 Hom（或等价地：把推论 3.10 换成它的反变版本）。对任意 $$d\in\mathcal{D}$$，

$$\mathcal{D}\Bigl(F\bigl(\operatorname{colim}_j D_j\bigr),\ d\Bigr)\cong\mathcal{C}\Bigl(\operatorname{colim}_j D_j,\ Gd\Bigr)\cong\lim_j\mathcal{C}\bigl(D_j,Gd\bigr)\cong\lim_j\mathcal{D}\bigl(FD_j,d\bigr)\cong\mathcal{D}\Bigl(\operatorname{colim}_j FD_j,\ d\Bigr).$$

四步的依据分别是：伴随同构；定理 3.19 的对偶条款（反变 Hom 把余极限送成极限）；再对每个 $$j$$ 用一次伴随同构（相容性同样来自 $$\varphi$$ 的自然性）；最后再用一次定理 3.19 的对偶条款。整条链对 $$d$$ 自然，于是反变 Hom 函子 $$h_{F(\operatorname{colim}D)}\cong h_{\operatorname{colim}FD}$$，由推论 3.10 的反变版本得 $$F(\operatorname{colim}D)\cong\operatorname{colim}FD$$。$$\blacksquare$$

**注 3.21（这就是 ch32 那句话的解释）** 定理 3.21 说 $$C\otimes_R-$$ 保一切余极限；定理 3.20 说 $$\operatorname{Hom}_S(C,-)$$ 保一切极限。核（kernel）是等化子、是极限；余核是余等化子、是余极限；满射由余等化子的性质刻画、单射由等化子的性质刻画。于是 ch32 里那两个「各保一半」的观察

$$V\otimes g\ \text{保满射},\qquad \operatorname{Hom}(f,W)\ \text{保单射}$$

不再是两个孤立事实，而是同一个定理的两个半边：**左伴随承诺保余极限，右伴随承诺保极限，谁都不承诺另一半**。这同时也预告了坏消息：$$-\otimes_R A$$ **不**承诺保核，$$\operatorname{Hom}_S(C,-)$$ **不**承诺保余核——这些「没被承诺的地方」正是第 34、35 章要用导出函子 $$\operatorname{Tor}$$、$$\operatorname{Ext}$$ 去度量的缺口。

**推论 3.22（非伴随的判定法）** 若函子 $$F$$ 不保余极限，则 $$F$$ 不是任何函子的左伴随；若 $$G$$ 不保极限，则 $$G$$ 不是任何函子的右伴随。

**例 3.22（遗忘函子：为什么它只当右伴随）** 遗忘函子 $$U:\mathbf{Grp}\to\mathbf{Set}$$ **保一切极限**：群范畴里的积是直积 $$G\times H$$（底层集合就是 $$U(G)\times U(H)$$），等化子在底层也逐元素计算，故 $$U$$ 保积、保等化子，从而保一切极限——这与定理 3.20 一致，因为例 3.16(ii) 已经证明 $$U$$ 是自由函子的**右**伴随。

但 $$U$$ **不保余积**：$$\mathbf{Set}$$ 中余积是不交并，$$\lvert U(\mathbb{Z}/2)\sqcup U(\mathbb{Z}/2)\rvert=4$$；而 $$\mathbf{Grp}$$ 中余积是**自由积** $$\mathbb{Z}/2*\mathbb{Z}/2$$，它包含形如 $$ababab\cdots$$ 的无限多约化字，故是一个无限群：

$$\lvert U(\mathbb{Z}/2*\mathbb{Z}/2)\rvert=\infty\ \ne\ 4.$$

由推论 3.22，$$U$$ **不是**任何函子的左伴随。这与例 3.18 里拓扑遗忘函子的情形形成对照：那里遗忘函子同时是左、右伴随，因为它两侧都保（Top 的余积是不交并、积是积拓扑，都与底层集合一致）。

### Gelfand 对偶是伴随

**定理 3.23（Gelfand 对偶是一对伴随, Gelfand duality）** 记 $$\mathbf{C^*Alg}_1$$ 为含单位的**交换** C\*-代数以保单位 \*-同态为态射的范畴，$$\mathbf{CHaus}$$ 为紧 Hausdorff 空间以连续映射为态射的范畴。定义两个函子

$$C:\mathbf{CHaus}^{\mathrm{op}}\to\mathbf{C^*Alg}_1,\qquad X\mapsto C(X,\mathbb{C}),$$

$$\Delta:\mathbf{C^*Alg}_1^{\mathrm{op}}\to\mathbf{CHaus},\qquad \mathcal A\mapsto\Delta(\mathcal A)=\bigl\{\varphi\in\operatorname{Hom}_{\mathbf{C^*Alg}_1}(\mathcal A,\mathbb{C})\bigr\},$$

其中 $$\Delta(\mathcal A)$$ 取弱\*拓扑（第 40 章的定义 3.11），即 $$\Delta=h_{\mathbb{C}}$$ 是反变 Hom 函子。则对一切 $$X\in\mathbf{CHaus}$$、$$\mathcal A\in\mathbf{C^*Alg}_1$$ 有自然双射

$$\operatorname{Hom}_{\mathbf{C^*Alg}_1}\bigl(C(X),\ \mathcal A\bigr)\ \cong\ \operatorname{Hom}_{\mathbf{CHaus}}\bigl(\Delta(\mathcal A),\ X\bigr),$$

即 $$C\dashv\Delta$$。更进一步，单位与余单位都是同构，因此这对伴随实际上是**范畴等价**

$$\mathbf{C^*Alg}_1^{\mathrm{op}}\ \simeq\ \mathbf{CHaus}.$$

**证明** (i) **双射的构造。** 取 $$\varphi\in\operatorname{Hom}_{\mathbf{C^*Alg}_1}(C(X),\mathcal A)$$。对每个 $$\psi\in\Delta(\mathcal A)$$，复合 $$\psi\circ\varphi:C(X)\to\mathbb{C}$$ 仍是 $$\mathbf{C^*Alg}_1$$ 中的态射；由第 40 章定理 3.12（Gelfand 表示定理）的表述(iv)，$$\Delta(C(X))\cong X$$——$$C(X)$$ 的每个保单位同态恰是某点的求值 $$\mathrm{ev}_x$$，且 $$x\mapsto\mathrm{ev}_x$$ 是同胚。故 $$\psi\circ\varphi=\mathrm{ev}_{\widehat\varphi(\psi)}$$ 对唯一一点 $$\widehat\varphi(\psi)\in X$$ 成立，这就定义了

$$\widehat\varphi:\Delta(\mathcal A)\to X,\qquad \psi\mapsto\widehat\varphi(\psi).$$

它连续：$$\psi\mapsto\psi(\varphi(f))$$ 按 Gelfand 拓扑的定义连续，而 $$\mathrm{ev}_x$$ 分离 $$X$$ 上的点。

(ii) **反方向。** 给定连续 $$u:\Delta(\mathcal A)\to X$$，定义 $$\widetilde u:C(X)\to\mathcal A$$ 为

$$\widetilde u(f):=\Gamma_{\mathcal A}^{-1}\bigl(f\circ u\bigr),$$

其中 $$\Gamma_{\mathcal A}:\mathcal A\to C(\Delta(\mathcal A))$$ 是 Gelfand 表示（第 40 章定义 3.11）。这里用了第 40 章定理 3.19（Gelfand–Naimark）：对含单位交换 C\*-代数，$$\Gamma_{\mathcal A}$$ 是**等距 \*-同构**，故可逆。$$\widetilde u$$ 保单位、保乘法、保 \*，故是 $$\mathbf{C^*Alg}_1$$ 中的态射。验证互逆：$$\widetilde{\widehat\varphi}$$ 与 $$\varphi$$ 在任意 $$f$$ 上给出同一个 $$a\in\mathcal A$$（两者都满足「$$\psi(a)=f(\widehat\varphi(\psi))$$ 对一切 $$\psi$$ 成立」，而这样的 $$a$$ 唯一，因为 $$\Delta(\mathcal A)$$ 上的函数分离点）；同法得 $$\widehat{\widetilde u}=u$$。两边于是互逆。

(iii) **自然性与等价。** 两个方向都由显式公式给出、没有做任何选择，自然性直接读出。单位 $$\eta_X$$ 是 $$x\mapsto\mathrm{ev}_x$$（同胚），余单位 $$\varepsilon_{\mathcal A}=\Gamma_{\mathcal A}^{-1}$$（同构，Gelfand–Naimark）。一对伴随的单位与余单位都是同构就给出范畴等价。$$\blacksquare$$

**注 3.23（这一步和第 40 章的关系，以及它为什么是 Yoneda）** 第 40 章的两条定理（Gelfand 表示定理 3.12、Gelfand–Naimark 定理 3.19）在这里被**重新认出**为一句范畴论的话：$$\Delta=h_{\mathbb{C}}$$ 是可表函子（例 3.7(ii)），$$C$$ 是它的左伴随，而「单位与余单位都是同构」正是那两条定理的合写。于是第 40 章那个含糊的直觉——**「元素就是函数、代数的极大理想就是空间的点」**——获得精确形式：

$$\text{「点」}=\text{从 }\mathcal A\text{ 出发的态射 }\varphi:\mathcal A\to\mathbb{C}\ =\ h_{\mathbb{C}}(\mathcal A),$$

「代数」「几何」两侧的翻译就是 $$C\dashv\Delta$$ 这对伴随的来回搬运。这也说明了为什么这一章配得上「核心概念」四个字：Yoneda 给出「对象由探测决定」，伴随给出「两个范畴之间的双向翻译」，而 Gelfand 对偶正是两者叠在一起时的最强情形——翻译不只是双向的，而且**没有信息损失**。

## 四、几何与物理直觉 (Intuition)

**（1）伴随是「最接近互逆」的一对。** 同构是奢侈品，伴随是日用品。$$F\dashv G$$ 的含义可以用两个自然变换说清：单位 $$\eta_c:c\to GFc$$ 是「先把 $$c$$ 送进对面的世界、再拉回来」，余单位 $$\varepsilon_d:FGd\to d$$ 是「先在对面造一个自由的东西、再压回来」。两者一般都不是同构（$$GFc$$ 通常严格大于 $$c$$），但三角恒等式保证「送出去再拉回来」与「造一个自由的再压回来」都等于恒等。

在「自由 ⊣ 遗忘」里，$$\eta_S:S\to U F_S$$ 把集合变成一组基（一个单射），$$\varepsilon_G:F_{UG}\to G$$ 把「以 $$G$$ 中元素为字母的自由群」压回 $$G$$（一个满射）。几何图像是：$$F$$ 是**展开**（只留生成元），$$G$$ 是**折叠**（只留底层集合）。展开再折叠损失信息，折叠再展开是恒等——这种方向上的不对称，正是「伴随不是同构」的全部来源。

**（2）那个「二选一」是什么。** 入口题 (d) 的答案是：这些构造成对，是因为它们**站队**。**左边这一队**是「自由的 / 最省的 / 粘合的 / 商掉的」，对应**左伴随、余极限、余积、余核、满射**；**右边这一队**是「遗忘的 / 受限的 / 取回的 / 嵌入的」，对应**右伴随、极限、积、核、单射**。定理 3.20 与 3.21 是这场结盟的数学陈述。于是 (a) 的自由群与 (b) 的张量积同队，它们各自的伙伴（遗忘函子、Hom 函子）在另一队——(b) 与 (a) 形状相同，因为它们都是一条**从一队到另一队的可逆通道**。

**（3）物理：自由构造就是二次量子化。** 给定单粒子态空间 $$V$$，自由场论的出发点是它的**自由代数**：玻色子用**对称代数** $$\operatorname{Sym}(V)=\bigoplus_{n\ge0}\operatorname{Sym}^n V$$，费米子用**外代数** $$\Lambda(V)$$。两者都是「自由 ⊣ 遗忘」的实例——从 $$V$$ 的元素自由生成一个代数，而任何候选场代数到它的映射由在 $$V$$ 上的取值唯一决定。这正是「唯一延拓」的物理翻译：**产生算符的作用被它在单粒子态上的取值完全钉死**。

**（4）$$\Sigma\dashv\Omega$$：为什么同伦群可以降一维算。** 悬置把 $$S^n$$ 变成 $$S^{n+1}$$，环路空间把维数降回去：

$$\Sigma S^n=S^{n+1},\qquad \Omega S^{n+1}\simeq S^n\ \ (\text{在}\ n\ge1\ \text{时}),$$

代入例 3.18 的伴随同构 $$[\Sigma X,Y]_*\cong[X,\Omega Y]_*$$，取 $$X=S^n$$、$$Y=S^{n+1}$$，得到

$$\pi_{n+1}(Y)=[S^{n+1},Y]_*\cong[S^n,\Omega Y]_*=\pi_n(\Omega Y).$$

「球面同伦群降一维」因此不是技巧，而是 $$\Sigma\dashv\Omega$$ 的直接后果——第 25、26 章反复用到的递归计算（把 $$\pi_k$$ 化到低维再用覆盖空间与纤维化处理）在这里找到了源头。物理上这条同构读作：**「一个圆圈上的构型」与「一个随时间演化的构型」是同一份数据**；环路空间把 $$S^1$$ 这条「时间轴」吸收进空间本身，这正是第 46 章 Feynman 路径积分里「时间 = 额外维」的几何原型。

**（5）Yoneda 的几何：对象由「被探测的结果」决定。** 推论 3.10 说 $$h_A$$ 决定了 $$A$$：要检验两个空间是否相同，就去问每一个射进它的探针。代数几何把这句话推到底——先给定**函子**（哪些探测给出哪些数据），空间只是它的表示对象；第 72 章的素谱与层就是从这条路走上来的。

**（6）Gelfand：几何与代数的对偶是伴随。** 定理 3.23 把第 40 章的两条定理（Gelfand 表示、Gelfand–Naimark）压缩成「$$C\dashv\Delta$$ 的单位与余单位都是同构」，图像是**同一份数据的两个视角**：一侧是空间 $$X$$ 与它上面的连续函数，另一侧是代数 $$\mathcal A$$ 与它的点。Stone 对偶（布尔代数 ≃ 完全不连通紧 Hausdorff 空间）是同一台机器（Yoneda + 伴随）的另一次换装。

## 五、经典问题精讲 (Classical Problems)

**问题 1（自由 ⊣ 遗忘的单位与余单位；入口题 (a) 的回收）** 设 $$S$$ 是集合，$$F_S$$ 是 $$S$$ 上的自由群，$$U:\mathbf{Grp}\to\mathbf{Set}$$ 是遗忘函子，$$F\dashv U$$ 是例 3.16(ii) 中的伴随。**求**单位 $$\eta_S:S\to U F_S$$ 与余单位 $$\varepsilon_G:F_{UG}\to G$$ 的具体形态，**证明** $$\eta_S$$ 是单射、$$\varepsilon_G$$ 是满同态，并求出 $$\ker\varepsilon_G$$。特别地，取 $$G=\mathbb{Z}/2$$：算出 $$F_{UG}$$ 是什么群、$$\varepsilon_G$$ 的核是什么。

**解** 由定义 3.14，$$\eta_S=\varphi_{S,F_S}(1_{F_S})=\iota:S\to U F_S$$，即把 $$s$$ 送到长度为 1 的字 $$s$$ 的映射。不同元素的像是不同的字，故 $$\eta_S$$ 是单射；它的像正是 $$F_S$$ 的自由生成集 $$S$$。

余单位：$$\varepsilon_G:F_{UG}\to G$$ 是 $$\varphi^{-1}(1_{UG})$$，由例 3.16(ii) 的证明，它把字 $$g_1^{\epsilon_1}\cdots g_n^{\epsilon_n}$$（$$g_i\in U G$$）送到群 $$G$$ 中的乘积 $$g_1^{\epsilon_1}\cdots g_n^{\epsilon_n}$$；等价地，它是唯一那个在生成元 $$U G$$ 上取值等于恒等映射的群同态。它是满的：$$G$$ 中每个元素 $$g$$ 都是长度 1 的字 $$g$$ 的像。它的核是

$$\ker\varepsilon_G=\bigl\langle\!\bigl\langle\ \text{一切在 }G\text{ 中等于 }e\text{ 的字}\ \bigr\rangle\!\bigr\rangle,$$

即这些字生成的**正规闭包**（核必是正规子群；反过来，任何在 $$G$$ 中为 $$e$$ 的字都必落入核，而核正由它们生成）。

取 $$G=\mathbb{Z}/2$$：$$UG=\{e,g\}$$ 是一个 2 元集合，但 $$e$$ 和 $$g$$ 是**两个不同的字母**——自由群不过问它们是什么。故 $$F_{UG}$$ 是秩 2 的自由群 $$\mathbb{Z}*\mathbb{Z}$$，而不是 $$\mathbb{Z}/2$$。$$\varepsilon:=\varepsilon_{\mathbb{Z}/2}$$ 把字母 $$e\mapsto e$$、$$g\mapsto \bar g$$（非平凡元），于是

$$\ker\varepsilon=\bigl\langle\!\bigl\langle\,e,\ g^2\,\bigr\rangle\!\bigr\rangle=\bigl\langle\!\bigl\langle\,g^2\,\bigr\rangle\!\bigr\rangle,$$

（$$e$$ 本身就在核里，作为生成元它是被多余地写出来的；正规闭包由 $$g^2$$ 生成）。**关键 leap**：「自由 ⊣ 遗忘」的余单位**一般不是单射**，偏差恰好是「把 $$UG$$ 里在 $$G$$ 中多余的元素自由化过头」的部分。第 68 章会把「$$\eta$$ 单、$$\varepsilon$$ 满」这条不对称刻成单子的两条自然变换。

**问题 2（张量 ⊣ Hom 的一次完整计算；入口题 (b) 的回收）** 设 $$n\ge1$$，$$B$$ 是 $$\mathbb{Z}$$-模。**证明**存在自然同构

$$\operatorname{Hom}_{\mathbb{Z}}\bigl(A\otimes_{\mathbb{Z}}\mathbb{Z}/n,\ B\bigr)\cong\operatorname{Hom}_{\mathbb{Z}}\bigl(A,\ B[n]\bigr),\qquad B[n]:=\bigl\{b\in B: nb=0\bigr\},$$

并**验证**：取 $$A=\mathbb{Z}/m$$ 时两边都等于 $$B[\gcd(m,n)]$$。（这里 $$\gcd$$ 提示：$$\mathbb{Z}/m\otimes_{\mathbb{Z}}\mathbb{Z}/n\cong\mathbb{Z}/\gcd(m,n)$$。）

**解** 由定理 3.17，在 $$R=S=\mathbb{Z}$$、$$C=\mathbb{Z}/n$$ 下直接得到

$$\operatorname{Hom}_{\mathbb{Z}}\bigl(\mathbb{Z}/n\otimes_{\mathbb{Z}}A,\ B\bigr)\cong\operatorname{Hom}_{\mathbb{Z}}\bigl(A,\ \operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/n,B)\bigr).$$

只需再认出 $$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/n,B)\cong B[n]$$：一个 $$f$$ 由 $$f(\bar1)$$ 决定，而 $$n\bar1=\bar0$$ 迫使 $$n\cdot f(\bar1)=0$$；反之任意 $$b\in B[n]$$ 都给出良定义的 $$f(\bar1)=b$$（$$k\bar1=\bar0$$ 时 $$kb=0$$）。两个方向互逆，且同构对 $$B$$ 自然（对 $$k:B\to B'$$，两边都只是把 $$b$$ 送成 $$k(b)$$）。代入即得要证的同构。

取 $$A=\mathbb{Z}/m$$。左边：由 ch32 的计算（$$\mathbb{Z}/m\otimes\mathbb{Z}/n\cong\mathbb{Z}/\gcd(m,n)$$）

$$\operatorname{Hom}_{\mathbb{Z}}\bigl(\mathbb{Z}/\gcd(m,n),\ B\bigr)\cong B[\gcd(m,n)],$$

最后一步用同一条 $$B[n]$$ 识别。右边：$$\operatorname{Hom}_{\mathbb{Z}}\bigl(\mathbb{Z}/m,\ B[n]\bigr)\cong\bigl(B[n]\bigr)[m]=\{b: nb=0,\ mb=0\}=B[\gcd(m,n)]$$（整数环里「同时被 $$m$$ 和 $$n$$ 零化」等价于「被 $$\gcd(m,n)$$ 零化」）。两边都等于 $$B[\gcd(m,n)]$$——**在两套算法上算同一个东西，得到同一个答案**，这正是伴随同构的用途。**关键 leap**：把 $$\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/n,B)$$ 认成**零化子** $$B[n]$$，于是「张量 ⊣ Hom」在 $$\mathbb{Z}$$ 上读作一句朴素的话——**「先把 $$A$$ 商到 $$n$$ 的部分再看能不能射进 $$B$$」与「先把 $$B$$ 里被 $$n$$ 零化的部分取出来再看 $$A$$ 能不能射进去」是同一件事**。

**问题 3（矩阵版的 Yoneda 嵌入；入口题 (c) 的回收）** 取 $$\mathfrak{m}=\mathbb{K}^{m\times m}$$，$$A=\mathbb{K}^{m\times n}$$、$$B=\mathbb{K}^{m\times n'}$$ 是左 $$\mathfrak{m}$$-模。**证明**

$$\operatorname{Hom}_{\mathfrak{m}-}\bigl(A,\ \mathbb{K}^{m\times p}\bigr)\cong\mathbb{K}^{n\times p},$$

并且态射 $$f:\mathbb{K}^{m\times p}\to\mathbb{K}^{m\times q}$$ 在 Hom 集上诱导的映射就是**右乘** $$f$$。再由此证明：若 $$A$$ 与 $$B$$ 使得 $$h_A\cong h_B$$，则 $$A\cong B$$，且给出同构的矩阵唯一。

**解** 分三步。

**(1) 右乘是左 $$\mathfrak{m}$$-线性的。** 对 $$X\in A=\mathbb{K}^{m\times n}$$ 与 $$a\in\mathbb{K}^{n\times p}$$ 定义 $$\rho_a(X):=Xa$$。则对 $$R\in\mathfrak{m}$$，$$\rho_a(RX)=(RX)a=R(Xa)=R\rho_a(X)$$，故 $$\rho_a\in\operatorname{Hom}_{\mathfrak{m}-}(A,\mathbb{K}^{m\times p})$$，并且 $$a\mapsto\rho_a$$ 显然是 $$\mathbb{K}$$-线性的（$$\rho_{a+a'}=\rho_a+\rho_{a'}$$、$$\rho_{ca}=c\rho_a$$）。

**(2) 单。** 若 $$\rho_a=0$$，取 $$X$$ 为第 $$j$$ 行全 1、其余行全 0 的矩阵（$$1\le j\le n$$），则 $$Xa$$ 的第 $$j$$ 行等于 $$a$$ 的第 $$j$$ 行，故 $$a$$ 的每一行都是零，$$a=0$$。

**(3) 维数相等，故是同构。** 先把左 $$\mathfrak{m}$$-模写成直和：$$A\cong(\mathbb{K}^m)^{\oplus n}$$（每一列是一个分量）。**Schur 型一步**：设 $$\theta:\mathbb{K}^m\to\mathbb{K}^m$$ 左 $$\mathfrak{m}$$-线性。取 $$R=E_{ii}$$ 与 $$v=e_k$$：$$i\ne k$$ 时两边给出 $$0=E_{ii}\theta(e_k)$$，即 $$\theta(e_k)$$ 的第 $$i$$ 个坐标为 0，故 $$\theta(e_k)=c_k e_k$$；再取 $$R=E_{ki}$$ 得 $$c_i e_k=E_{ki}\theta(e_i)=\theta(e_k)=c_k e_k$$，于是全部 $$c_k$$ 相等，$$\theta=c\cdot1$$。因此 $$\operatorname{Hom}_{\mathfrak{m}-}(\mathbb{K}^m,\mathbb{K}^m)=\mathbb{K}\cdot1$$，而左 $$\mathfrak{m}$$-线性映射 $$(\mathbb{K}^m)^{\oplus n}\to(\mathbb{K}^m)^{\oplus p}$$ 由「对每对源分量、目标分量各给一个数」决定：

$$\operatorname{Hom}_{\mathfrak{m}-}\bigl((\mathbb{K}^m)^{\oplus n},(\mathbb{K}^m)^{\oplus p}\bigr)\cong\mathbb{K}^{p\times n}.$$

$$\mathbb{K}^{p\times n}$$ 与右乘参数 $$\mathbb{K}^{n\times p}$$ 互为转置，维数都是 $$np$$（转置是 $$\mathbb{K}$$-线性同构）。结合 (2) 的单性，$$a\mapsto\rho_a$$ 是 $$\mathbb{K}$$ 上的同构，即 $$\operatorname{Hom}_{\mathfrak{m}-}(A,\mathbb{K}^{m\times p})\cong\mathbb{K}^{n\times p}$$。

**诱导映射是右乘。** 对 $$f:\mathbb{K}^{m\times p}\to\mathbb{K}^{m\times q}$$，$$h_A(f)$$ 定义为「先取 $$g\in\operatorname{Hom}_{\mathfrak{m}-}(A,\mathbb{K}^{m\times p})$$ 再复合 $$f$$」。在矩阵记法下，$$g=\rho_a$$（$$a\in\mathbb{K}^{n\times p}$$），而 $$(f\circ\rho_a)(X)=f(Xa)=\rho_{?}$$；由 (3) 的结论 $$f$$ 本身也是右乘某个 $$F\in\mathbb{K}^{p\times q}$$（取 $$p$$ 对应源），即 $$f(Y)=YF$$。于是

$$(h_A(f))(g)(X)=(f\circ\rho_a)(X)=f(Xa)=XaF=X(aF)=\rho_{aF}(X),$$

故 $$h_A(f)$$ 就是 $$a\mapsto aF$$，**正是右乘 $$f$$**。

**对象由可表函子决定。** 取 $$p=n'$$，则 $$h_A(\mathbb{K}^{m\times n'})=\operatorname{Hom}_{\mathfrak{m}-}(A,B)\cong\mathbb{K}^{n\times n'}$$。由推论 3.10，$$h_A\cong h_B\Rightarrow A\cong B$$；由推论 3.11，给出这个自然同构的矩阵 $$a\in\mathbb{K}^{n\times n'}$$ 唯一（它是 $$\Phi_A(1_A)$$ 的矩阵），且局部上「可逆 ⟺ $$a$$ 可逆」。**关键 leap**：矩阵这里扮演的正是「自然变换」——**自然变换这个抽象概念，在矩阵语言里就是「乘一个矩阵」**。

**问题 4（万有性质就是可表性；Yoneda 与 ch32 的交汇）** 设 $$R$$ 是环，$$C$$ 是右 $$R$$-模，$$A$$ 是左 $$R$$-模。对 $$\mathbb{Z}$$-模 $$B$$ 记 $$\operatorname{Bilin}_R(C,A;B)$$ 为一切 $$R$$-**平衡**双可加映射 $$\beta:C\times A\to B$$ 的集合（即 $$\beta(cr,a)=\beta(c,ra)$$、对每个变量分别可加）。**证明**：函子 $$B\mapsto\operatorname{Bilin}_R(C,A;B)$$（对 $$k:B\to B'$$ 的作用是 $$\beta\mapsto k\circ\beta$$）是可表的，其表示对象就是张量积 $$C\otimes_R A$$，而万有元就是 $$\otimes:C\times A\to C\otimes_R A$$。

**解** 由 ch32 的万有性质（定理 3.17 的证明里也用了它）：对任意 $$B$$，映射

$$\Theta:\operatorname{Hom}_{\mathbb{Z}}\bigl(C\otimes_R A,\ B\bigr)\to\operatorname{Bilin}_R(C,A;B),\qquad \Theta(f):=f\circ\otimes$$

是双射（逆是「把 $$\beta$$ 分解过张量积」）。这正是可表的定义：$$\operatorname{Bilin}_R(C,A;B)\cong h_{C\otimes_R A}(B)$$。万有元方面，把恒等态射放进左边得

$$\Theta(1_{C\otimes_R A})=1\circ\otimes=\otimes,$$

所以万有元就是那个**双线性映射** $$\otimes$$ 自己。用推论 3.12 的判据核对：对任意 $$B$$ 与任意 $$\beta\in\operatorname{Bilin}_R(C,A;B)$$，存在唯一的 $$f:C\otimes_R A\to B$$ 使 $$\beta=f\circ\otimes$$——这句话**逐字**是张量积的万有性质。

**关键 leap**：这一步把 ch32 里当作「公理」用掉的万有性质，重写成了「某个函子可表」这条**结构性**陈述。于是「张量积是什么」不再依赖任何具体构造，而只说：**它是双线性函子的表示对象，由 Yoneda 定理 3.8 与推论 3.10 在同构意义下唯一**。同一句话适用于自由群（例 3.16）、自由模、极限、余极限——**一切用「唯一分解」定义的构造都是可表函子**，这就是入口题 (d) 那个共同形状的最终答案。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 取 $$A=\{0,1\}$$，$$f:A\to A$$ 由 $$f(0)=1$$、$$f(1)=1$$ 给出。把共变 Hom 函子 $$h^A=\mathbf{Set}(A,-)$$ 在态射 $$f$$ 上的作用 $$h^A(f):h^A(A)\to h^A(A)$$ 逐元素算出来。再验证 $$h^A(1_A)$$ 是恒等映射。

**基2.** 在 $$\mathbf{Set}$$ 上，设 $$F=\mathrm{id}_{\mathbf{Set}}$$，$$G$$ 是把每个集合送到不动点集 $$\{*\}$$ 的常值函子（$$G(f)$$ 是 $$\{*\}$$ 上唯一的映射）。求 $$\operatorname{Nat}(F,G)$$ 与 $$\operatorname{Nat}(G,F)$$ 各有多少个元素。（提示：注意空集。）

**基3.** 下面这族映射**不是**自然变换。取 $$F=G=\mathrm{id}_{\mathbf{Set}}$$，并规定

$$\alpha_X:=1_X\ \text{当}\ X\ne\{0,1\};\qquad \alpha_{\{0,1\}}:=\text{交换}\ 0\ \text{与}\ 1.$$

找出至少两个态射 $$f$$ 使自然性方块不交换，并说明失败的原因。

**基4.** 取 $$F=h_B=\mathcal{C}(-,B)$$，写出定理 3.8 给出的双射

$$\operatorname{Nat}(h_A,h_B)\ \cong\ \mathcal{C}(A,B)$$

的显式公式，并验证两个方向互逆。

### 竞赛（本课目标难度）

**竞1.** 设 $$G$$ 是群，$$\mathbf{B}G$$ 是单对象群胚：一个对象 $$*$$，$$\operatorname{Hom}(*,*)=G$$，复合是群乘法。证明：对任意 $$G$$-集 $$X$$（即任一函子 $$F_X:\mathbf{B}G^{\mathrm{op}}\to\mathbf{Set}$$ 的像），有双射

$$\operatorname{Nat}(h_*,F_X)\cong X,\qquad \varphi\mapsto\varphi_*(e),$$

并把它念成一句关于群作用的话。再算出 $$\operatorname{Nat}(h_*,h_*)$$ 是什么。

**竞2.** 设 $$F:\mathcal{C}^{\mathrm{op}}\to\mathbf{Set}$$ 可表。证明：$$F$$ 的表示（在同构意义下）与 $$F$$ 的**万有元**一一对应；并证明若 $$(A,x)$$、$$(B,y)$$ 是两个这样的表示（$$x\in F(A)$$、$$y\in F(B)$$），则存在唯一的同构 $$f:A\to B$$，其特征由 $$F(f)(y)=x$$ 完全决定。

**竞3.** 证明群范畴 $$\mathbf{Grp}$$ 的余积是**自由积**（即：造出自由积的万有性质），并由此给出遗忘函子 $$U:\mathbf{Grp}\to\mathbf{Set}$$ 不保余积的一个具体见证：算出 $$U(\mathbb{Z}/2*\mathbb{Z}/2)$$ 是无限集，而 $$U(\mathbb{Z}/2)\sqcup U(\mathbb{Z}/2)$$ 只有 4 个元素。

**竞4.** 证明：若 $$F\dashv G$$，则 $$F$$ 把始对象送到始对象、$$G$$ 把终对象送到终对象（在它们分别存在时）。再用这条判据证明：遗忘函子 $$U:\mathbf{Field}\to\mathbf{Set}$$ **没有**左伴随。

**竞5.** 设 $$F\dashv G$$（$$\mathcal{C}\rightleftarrows\mathcal{D}$$）且 $$F'\dashv G'$$（$$\mathcal{D}\rightleftarrows\mathcal{E}$$）。证明复合也是伴随：

$$F'F\ \dashv\ GG'.$$

### 研究（通向下一章）

**研1.** 设 $$F\dashv G$$，单位 $$\eta:1_{\mathcal{C}}\Rightarrow GF$$、余单位 $$\varepsilon:FG\Rightarrow1_{\mathcal{D}}$$。令

$$T:=GF:\mathcal{C}\to\mathcal{C},\qquad \mu:=G\varepsilon F:T^2\Rightarrow T.$$

用两条三角恒等式证明 $$(T,\eta,\mu)$$ 满足三条公理：

$$\mu\circ\eta T=1_T,\qquad \mu\circ T\eta=1_T,\qquad \mu\circ\mu T=\mu\circ T\mu.$$

**研2.** 用定理 3.21 证明函子 $$-\otimes_{\mathbb{Z}}\mathbb{Z}/n$$ 保一切余极限（特别地保余核，因而保满射），并解释：既然它是左伴随，为什么它**不**保核这件事与定理 3.21 不矛盾。再给出一个具体见证：把短正合列 $$0\to\mathbb{Z}\xrightarrow{\ \cdot n\ }\mathbb{Z}\to\mathbb{Z}/n\to0$$ 与 $$\mathbb{Z}/n$$ 张量积，看核发生了什么变化。

### 解答 (Solutions)

**解 基1.** 先把两个集合写出来。$$h^A(A)=\mathbf{Set}(\{0,1\},\{0,1\})$$ 有 4 个元素：

$$g_1=\text{常值 }0,\quad g_2=1_A,\quad g_3=\text{常值 }1,\quad g_4=\text{交换}\ 0,1.$$

$$h^A(f)$$ 定义为 $$g\mapsto f\circ g$$，逐个算：

$$f\circ g_1:\ 0\mapsto f(0)=1,\ 1\mapsto f(0)=1\ \Rightarrow\ f\circ g_1=g_3;$$
$$f\circ g_2=f=g_3;\qquad f\circ g_3:\ 0\mapsto f(1)=1,\ 1\mapsto f(1)=1\ \Rightarrow\ f\circ g_3=g_3;$$
$$f\circ g_4:\ 0\mapsto f(1)=1,\ 1\mapsto f(0)=1\ \Rightarrow\ f\circ g_4=g_3.$$

所以 $$h^A(f)$$ 是把 4 个元素全部送到 $$g_3$$ 的常值映射。恒等方向：$$h^A(1_A)(g)=1_A\circ g=g$$ 对每个 $$g$$ 成立，故 $$h^A(1_A)=1_{h^A(A)}$$。顺带注意：$$f$$ 既非单射也非满射，而 $$h^A(f)$$ 是常值映射——**Hom 函子搬运的只是复合，与态射本身的单/满性无关**。

**解 基2.** 先算 $$\operatorname{Nat}(F,G)$$。自然变换 $$\alpha:F\Rightarrow G$$ 要对每个集合 $$X$$ 给出 $$\alpha_X:X\to\{*\}$$，而到单点集的映射是**唯一**的，故这族映射没有选择余地。自然性方面：对任意 $$f:X\to Y$$，方块要求 $$G(f)\circ\alpha_X=\alpha_Y\circ F(f)$$，左右两边都是 $$X\to\{*\}$$ 的唯一映射，自动成立。所以 $$\operatorname{Nat}(F,G)$$ 恰有 **1** 个元素。

再算 $$\operatorname{Nat}(G,F)=\operatorname{Nat}(G,\mathrm{id})$$。自然变换 $$\beta:G\Rightarrow F$$ 要对每个集合 $$X$$ 给出 $$\beta_X:\{*\}\to X$$，即要**对每个集合 $$X$$ 指定一个元素**。取 $$X=\varnothing$$：不存在映射 $$\{*\}\to\varnothing$$，故 $$\operatorname{Nat}(G,F)=\varnothing$$，有 **0** 个元素。

这一正一反说明了函子范畴的态射方向是有内容的：从 $$\mathrm{id}$$ 到常值函子有唯一一个自然变换（「每个集合都有元素」在单点集上不构成困难），反过来一个也没有（空集立刻杀死它）。

**解 基3.** 取 $$f:\{0,1\}\to\{0,1\}$$ 为常值映射 $$f\equiv0$$。自然性方块要求在 $$X=Y=\{0,1\}$$ 处

$$f\circ\alpha_X=\alpha_Y\circ f,\qquad\text{即}\qquad f\circ\alpha_{\{0,1\}}=\alpha_{\{0,1\}}\circ f.$$

逐元素算：左边 $$f(\alpha_{\{0,1\}}(0))=f(1)=0$$；右边 $$\alpha_{\{0,1\}}(f(0))=\alpha_{\{0,1\}}(0)=1$$。**取值为 0 与 1，不相等**，方块不交换。

再看 $$f=1_{\{0,1\}}$$ 时：两边都等于交换映射，方块交换；$$f=$$ 交换时：$$\alpha_{\{0,1\}}\circ f=f\circ\alpha_{\{0,1\}}$$（两次交换抵消），也交换。所以失败的映射是「把 $$\{0,1\}$$ 压成单点」的常值映射。

**失败的原因**是：$$\alpha$$ 在单个对象上的取值单独看都没有毛病，但自然性要求它在**一切对象上同步变化**——特别地，它必须与「把两个不同点粘成一个点」的常值映射相容。$$\alpha_{\{0,1\}}$$ 交换了两个点，而 $$\alpha_{\{1\}}$$ 无法模拟这个交换（$$\{1\}$$ 上只有一个点），方块于是塌掉。**自然性不是一堆局部条件，而是一条把全部对象串起来的链式约束**。

**解 基4.** 由定理 3.8（取 $$\mathcal{C}$$ 上的反变函子 $$F=h_B$$，注意 $$h_B$$ 是预层，即 $$\mathcal{C}^{\mathrm{op}}\to\mathbf{Set}$$），双射是

$$\alpha:\operatorname{Nat}(h_A,h_B)\to h_B(A)=\mathcal{C}(A,B),\qquad \Phi\mapsto\Phi_A(1_A).$$

反方向由定理 3.8 证明里的 $$\beta$$：给定 $$f\in\mathcal{C}(A,B)$$，定义 $$\beta(f)=\Phi^{(f)}$$，其中

$$\Phi^{(f)}_X:h_A(X)=\mathcal{C}(X,A)\to h_B(X)=\mathcal{C}(X,B),\qquad g\mapsto f\circ g.$$

即 $$\Phi^{(f)}=Yf$$（推论 3.9 的 Yoneda 嵌入在态射上的作用）。**验证互逆**：$$\alpha(\beta(f))=\Phi^{(f)}_A(1_A)=f\circ1_A=f$$；反过来对 $$\Phi\in\operatorname{Nat}(h_A,h_B)$$，任取 $$X$$ 与 $$g\in\mathcal{C}(X,A)$$，由 $$\Phi$$ 的自然性在 $$g:X\to A$$ 上得

$$\Phi_X(g)=\Phi_X\bigl(h_A(g)(1_A)\bigr)=h_B(g)\bigl(\Phi_A(1_A)\bigr)=\Phi_A(1_A)\circ g=\Phi^{(\Phi_A(1_A))}_X(g),$$

（第二步用了自然性方块 $$h_B(g)\circ\Phi_A=\Phi_X\circ h_A(g)$$，第三步用了 $$h_A(g)(1_A)=1_A\circ g=g$$，第四步用了 $$h_B(g)$$ 的定义）。故 $$\beta(\alpha(\Phi))=\Phi$$。两个方向都验证完毕，$$\operatorname{Nat}(h_A,h_B)\cong\mathcal{C}(A,B)$$。

**解 竞1.** 先把 $$\mathbf{B}G$$ 上的函子拆开。由定义，$$h_*$$ 在对象 $$\ast$$ 上取值 $$h_*(\ast)=\operatorname{Hom}(\ast,\ast)=G$$，而在 $$g\in\operatorname{Hom}(\ast,\ast)=G$$ 上的作用是

$$h_*(g):G\to G,\qquad k\mapsto k\circ g=kg,$$

即**右乘**。再看 $$F_X:\mathbf{B}G^{\mathrm{op}}\to\mathbf{Set}$$：它给出一个集合 $$X:=F_X(\ast)$$ 与对每个 $$g\in G$$ 一个映射 $$F_X(g):X\to X$$，并且（因为在 $$\mathbf{B}G^{\mathrm{op}}$$ 中复合法则反转）$$F_X(gh)=F_X(h)\circ F_X(g)$$——这正是「$$X$$ 上带有右 $$G$$-作用」的定义。于是一个自然变换 $$\varphi:h_*\Rightarrow F_X$$ 就是：一个映射 $$\varphi_\ast:G\to X$$（其余对象只有 $$\ast$$，没有别的分量），满足对一切 $$g\in G$$

$$F_X(g)\circ\varphi_\ast=\varphi_\ast\circ h_*(g).$$

**双射。** 设 $$\varphi$$ 是自然变换。把上式作用在 $$e$$ 上：左边 $$F_X(g)(\varphi_\ast(e))$$，右边 $$\varphi_\ast(h_*(g)(e))=\varphi_\ast(ge)=\varphi_\ast(g)$$。于是

$$\varphi_\ast(g)=F_X(g)\bigl(\varphi_\ast(e)\bigr)\qquad\text{对一切}\ g\in G,$$

也就是说 $$\varphi_\ast(e)\in X$$ 这个**单个元素**决定了整个 $$\varphi$$。反之，给定任意 $$x\in X$$，用上式**定义** $$\varphi_\ast(g):=F_X(g)(x)$$，就得到一个自然变换：对 $$g,k\in G$$，

$$\bigl(F_X(k)\circ\varphi_\ast\bigr)(g)=F_X(k)\bigl(F_X(g)(x)\bigr)=F_X(gk)(x)=\varphi_\ast(gk)=\bigl(\varphi_\ast\circ h_*(k)\bigr)(g),$$

方块交换。两个方向互逆，故 $$\operatorname{Nat}(h_*,F_X)\cong X$$，双射是 $$\varphi\mapsto\varphi_\ast(e)$$。

**念成一句话**：等变映射 $$\varphi$$ 由 $$\varphi_\ast(e)$$ 唯一决定，其余的值顺着作用被迫推出；反过来，任意指定 $$x\in X$$，$$\varphi(g):=x\cdot g$$ 都给出一个合法的等变映射。这就是 Yoneda 引理在群作用语言里的形态，也是推论 3.12 的万有元在 $$G$$-集上的特例。

**再算 $$\operatorname{Nat}(h_*,h_*)$$。** 取 $$X=G$$（右正则 $$G$$-集），双射给出 $$\operatorname{Nat}(h_*,h_*)\cong G$$，对应把 $$\varphi$$ 送到 $$\varphi_\ast(e)$$。直接验证这个双射还保持乘法（$$\operatorname{Nat}$$ 上是垂直复合、$$G$$ 上是群乘法），故它是**群同构**：**正则表示的自同态恰好就是 $$G$$ 本身**（Schur 引理的群胚版）。

**解 竞2.** 由定理 3.8，映射

$$\operatorname{Nat}(h_A,F)\to F(A),\qquad \eta\mapsto x_\eta:=\eta_A(1_A)$$

是双射。由推论 3.12，$$\eta$$ 是自然同构当且仅当 $$x_\eta$$ 是万有元。于是「$$F$$ 的表示」与「配对 $$(A,x)$$（$$A\in\mathcal{C}$$、$$x\in F(A)$$ 是万有元）」在「允许把 $$A$$ 换成同构对象」的意义下是同一份数据：**表示的同构类与万有元一一对应**。

现在取两个表示 $$(A,x)$$ 与 $$(B,y)$$。令 $$\eta:h_A\cong F$$、$$\theta:h_B\cong F$$ 是对应的自然同构，则

$$\Phi:=\theta^{-1}\circ\eta:h_A\to h_B$$

是自然同构。由推论 3.9(iii) 的满性，存在唯一的 $$f:A\to B$$ 使 $$Yf=\Phi$$；而见证唯一性的计算（推论 3.9 的证明）给出

$$f=\Phi_A(1_A)=\theta_A^{-1}\bigl(\eta_A(1_A)\bigr)=\theta_A^{-1}(x).$$

于是 $$f:A\to B$$ 由 $$\theta_A(f)=x$$ 唯一刻画。而我们想验证的特征是 $$F(f)(y)=x$$：把 $$\theta$$ 的自然性方块用在 $$f:A\to B$$ 上（注意 $$F$$ 与 $$h_B$$ 都反变，故方块为）

$$F(f)\circ\theta_B=\theta_A\circ h_B(f),$$

再作用在 $$1_B$$ 上：左边得 $$F(f)\bigl(\theta_B(1_B)\bigr)=F(f)(y)$$；右边得 $$\theta_A\bigl(h_B(f)(1_B)\bigr)=\theta_A(f\circ1_B)=\theta_A(f)$$。于是

$$F(f)(y)=\theta_A(f)=x,$$

其中最后一式就是 $$f=\theta_A^{-1}(x)$$ 的改写。反之，若 $$f$$ 满足 $$F(f)(y)=x$$，用同一个方块反推得 $$\theta_A(f)=x$$，故 $$f=\theta_A^{-1}(x)$$ 与上者相等。**特征唯一性成立**：集合 $$\{f:A\to B: F(f)(y)=x\}$$ 恰有一个元素，且它是同构。$$\blacksquare$$

**解 竞3.** 先造自由积。设 $$G_1,\dots,G_n$$ 是群，$$U G_i$$ 是底层集合。定义**自由积** $$G_1*\cdots*G_n$$ 的元素为「交错约化字」

$$w=g_1g_2\cdots g_m,\qquad g_j\in U G_{i_j},\ g_j\ne e_{i_j},\ i_j\ne i_{j+1},$$

再加上空字 $$e$$；乘法是拼接后反复消去相邻同群元素的乘积。同一群内的乘积已在 $$G_i$$ 里算好，消去过程不依赖顺序（与 ch31 自由群的情形逐字相同），故乘法良定义且结合，空字为单位。

**证明余积性质。** 设 $$H$$ 是任意群，$$\varphi_i:G_i\to H$$ 是一族同态。定义 $$\varphi:G_1*\cdots*G_n\to H$$ 在交错约化字上为

$$\varphi(g_1g_2\cdots g_m):=\varphi_{i_1}(g_1)\varphi_{i_2}(g_2)\cdots\varphi_{i_m}(g_m).$$

- **同态性**：拼接两个字时，若首尾属于不同群，右边直接相乘；若首尾属于同一个群 $$G_i$$，拼接后要先在 $$G_i$$ 里把两个元素乘起来（可能得 $$e_i$$，该字母随之消失）。两种情形下右边都由 $$\varphi_i$$ 的乘性给出同一个值，故 $$\varphi(ww')=\varphi(w)\varphi(w')$$。
- **唯一性**：$$\varphi$$ 在每个 $$G_i$$（作为长度 1 的字）上必须等于 $$\varphi_i$$，而这些像生成整个自由积，故 $$\varphi$$ 唯一。

于是 $$\coprod_i G_i=G_1*\cdots*G_n$$。

**不保余积的见证。** 取 $$G_1=G_2=\mathbb{Z}/2$$。集合层面 $$U(\mathbb{Z}/2)\sqcup U(\mathbb{Z}/2)$$ 有 4 个元素；群层面

$$\mathbb{Z}/2*\mathbb{Z}/2=\langle a,b\mid a^2=b^2=e\rangle=\{\,e,\ a,\ b,\ ab,\ ba,\ aba,\ bab,\ abab,\ \dots\,\}$$

含无限多交错字，故 $$U(\mathbb{Z}/2*\mathbb{Z}/2)$$ 无限。若 $$U$$ 保余积，余积的底层集合就该与两个分量底层集合的不交并一致，于是

$$\lvert U(\mathbb{Z}/2*\mathbb{Z}/2)\rvert=\infty\ \ne\ 4=\lvert U(\mathbb{Z}/2)\sqcup U(\mathbb{Z}/2)\rvert,$$

矛盾；故 $$U$$ 不保余积。由推论 3.22，$$U$$ 不是左伴随。（这与例 3.16(ii) 中 $$U$$ 是**右**伴随毫无冲突——右伴随只承诺保极限。）$$\blacksquare$$

**解 竞4.** 设 $$F\dashv G$$，$$F:\mathcal{C}\to\mathcal{D}$$。设 $$\mathcal{C}$$ 有始对象 $$\varnothing$$。要证 $$F\varnothing$$ 是 $$\mathcal{D}$$ 的始对象，即：对每个 $$d\in\mathcal{D}$$，$$\mathcal{D}(F\varnothing,d)$$ 恰有一个元素。由伴随同构及 $$\varnothing$$ 的始性质，

$$\mathcal{D}(F\varnothing,d)\cong\mathcal{C}(\varnothing,Gd)=\{\text{唯一那个态射}\},$$

故集合 $$\mathcal{D}(F\varnothing,d)$$ 恰有一个元素，$$F\varnothing$$ 是始对象。对偶地，设 $$\mathcal{D}$$ 有终对象 $$\mathbf{1}$$，则对每个 $$c\in\mathcal{C}$$，

$$\mathcal{C}(c,G\mathbf{1})\cong\mathcal{D}(Fc,\mathbf{1})=\{\text{唯一那个态射}\},$$

故 $$G\mathbf{1}$$ 是终对象。$$\blacksquare$$（这两条是定理 3.20、3.21 在「空图」上的特例。）

**判定 $$U:\mathbf{Field}\to\mathbf{Set}$$。** 反设存在左伴随 $$F\dashv U$$。空集 $$\varnothing$$ 是 $$\mathbf{Set}$$ 的始对象，由上一步，$$F\varnothing$$ 必须是 $$\mathbf{Field}$$ 的始对象。但 $$\mathbf{Field}$$ **没有始对象**：若 $$L$$ 是始对象，则对任意域 $$K$$ 恰有一个环同态 $$L\to K$$。取 $$K=\mathbb{Q}$$：环同态保 $$1$$，故 $$\operatorname{char}L=0$$；取 $$K=\mathbb{F}_p$$：同理 $$\operatorname{char}L=p$$。两者不能同时成立，矛盾。故这样的 $$L$$ 不存在，$$F$$ 不存在。所以 $$U$$ **没有左伴随**。$$\blacksquare$$

**解 竞5.** 只需对每对 $$c\in\mathcal{C}$$、$$e\in\mathcal{E}$$ 造出双射并验证自然性。用两次伴随同构复合：

$$\mathcal{E}\bigl(F'Fc,\ e\bigr)\ \xrightarrow[\ F'\dashv G'\ ]{\ \cong\ }\ \mathcal{D}\bigl(Fc,\ G'e\bigr)\ \xrightarrow[\ F\dashv G\ ]{\ \cong\ }\ \mathcal{C}\bigl(c,\ GG'e\bigr),$$

记合成为 $$\psi_{c,e}$$。**它是双射**，因为两个因子都是双射。**它自然**：对 $$e$$ 的变元，固定 $$c$$，第一个同构随 $$e$$ 自然（定义 3.13 中 $$\varphi$$ 对第二个变元的自然性）；第二个同构在 $$e$$ 上是「先由 $$G'$$ 诱导、再用 $$\varphi_{c,-}$$」，而 $$\varphi_{c,-}$$ 对第二变元自然、$$G'$$ 是函子，故合成对 $$e$$ 自然。对 $$c$$ 的变元同理，把两个同构各自对第一变元的自然性串起来即可。于是 $$F'F\dashv GG'$$。$$\blacksquare$$

顺带一个读法：复合伴随的单位在 $$c$$ 上就是 $$1_{\mathcal{C}}\xrightarrow{\ \eta\ }GF\xrightarrow{\ G\eta'F\ }GG'F'F$$，即先取 $$\eta_c$$ 再取 $$\eta'_{Fc}$$；两条三角恒等式的验证就是把内层与外层的方块分开，各用一次。

**解 研1.** 记 $$T=GF$$，$$\mu=G\varepsilon F$$，即 $$\mu_c=G(\varepsilon_{Fc}):GFGFc\to GFc$$。

**(1) 左单位。** $$(\eta T)_c=\eta_{Tc}=\eta_{GFc}:GFc\to GFGFc$$，而 $$\mu_c=G(\varepsilon_{Fc})$$。于是

$$\mu_c\circ(\eta T)_c=G(\varepsilon_{Fc})\circ\eta_{GFc}=\bigl((G\varepsilon)\circ(\eta G)\bigr)_{Fc}=(1_G)_{Fc}=1_{GFc},$$

第三步用了三角恒等式之一 $$(G\varepsilon)\circ(\eta G)=1_G$$，第四步用了函子保恒等。对一切 $$c$$ 成立，故 $$\mu\circ\eta T=1_T$$。

**(2) 右单位。** $$(T\eta)_c=G(F(\eta_c))=GF(\eta_c)$$（$$T\eta$$ 是水平复合：函子 $$T$$ 作用在 $$\eta_c:c\to GFc$$ 上给出 $$G F(\eta_c):GFc\to GFGFc$$）。于是

$$\mu_c\circ(T\eta)_c=G(\varepsilon_{Fc})\circ GF(\eta_c)=G\bigl(\varepsilon_{Fc}\circ F(\eta_c)\bigr)=G\bigl((\varepsilon F)_c\circ(F\eta)_c\bigr)=G(1_{Fc})=1_{GFc},$$

第三步用了另一条三角恒等式 $$(\varepsilon F)\circ(F\eta)=1_F$$。故 $$\mu\circ T\eta=1_T$$。

**(3) 结合律。** 先算两块：$$(\mu T)_c=\mu_{Tc}=G(\varepsilon_{FGFc})$$，$$(T\mu)_c=G(F(\mu_c))=GFG(\varepsilon_{Fc})$$。于是

$$\mu_c\circ(\mu T)_c=G(\varepsilon_{Fc})\circ G(\varepsilon_{FGFc})=G\bigl(\varepsilon_{Fc}\circ\varepsilon_{FGFc}\bigr),$$

$$\mu_c\circ(T\mu)_c=G(\varepsilon_{Fc})\circ GFG(\varepsilon_{Fc})=G\bigl(\varepsilon_{Fc}\circ FG(\varepsilon_{Fc})\bigr).$$

两式比较：只需在 $$G$$ 里面相等，即

$$\varepsilon_{Fc}\circ FG(\varepsilon_{Fc})=\varepsilon_{Fc}\circ\varepsilon_{FGFc}.$$

把 $$\varepsilon$$ 的自然性方块用在态射 $$\varepsilon_{Fc}:FGFc\to Fc$$ 上（即取 $$d=FGFc$$、$$d'=Fc$$、$$u=\varepsilon_{Fc}$$），方块说的是 $$\varepsilon_{Fc}\circ FG(\varepsilon_{Fc})=\varepsilon_{Fc}\circ\varepsilon_{FGFc}$$——正是所需。故 $$\mu\circ\mu T=\mu\circ T\mu$$。$$\blacksquare$$

三条公理合起来说：$$(T,\eta,\mu)$$ 是 $$\mathcal{C}$$ 上的一个**单子 (monad)**，且它由伴随 $$F\dashv G$$ **自动**产生。第 68 章正是从这里出发的：它反过来问「每一个单子都来自某个伴随吗」（回答是肯定的——用 Kleisli 或 Eilenberg–Moore 构造造出 $$F\dashv G$$ 使 $$T=GF$$），于是「伴随」与「单子」成为同一件事的两个信封。

**解 研2.** **保余极限。** 由定理 3.17 取 $$R=S=\mathbb{Z}$$、$$C=\mathbb{Z}/n$$（交换环 $$\mathbb{Z}$$ 上的模自动是双模），得到

$$\operatorname{Hom}_{\mathbb{Z}}\bigl(\mathbb{Z}/n\otimes_{\mathbb{Z}}A,\ B\bigr)\cong\operatorname{Hom}_{\mathbb{Z}}\bigl(A,\ \operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/n,B)\bigr),$$

即函子 $$\mathbb{Z}/n\otimes_{\mathbb{Z}}-$$ 是 $$B\mapsto\operatorname{Hom}_{\mathbb{Z}}(\mathbb{Z}/n,B)$$ 的**左伴随**。由定理 3.21，它保一切余极限，特别地保余核（余核是推出/余等化子型的余极限），从而把满射送成满射（$$g$$ 满 $$\iff$$ $$\operatorname{coker}g=0$$，而保余核把 $$0$$ 送成 $$0$$）。

**为什么不矛盾。** 定理 3.21 承诺的只有**余**极限；「保核」属于右伴随（定理 3.20），而 $$-\otimes_{\mathbb{Z}}\mathbb{Z}/n$$ 是左伴随，**没有任何定理承诺它保核**。它不保核不是反例，而正是「左伴随的承诺范围」的内容。

**具体见证。** 取短正合列

$$0\to\mathbb{Z}\xrightarrow{\ \cdot n\ }\mathbb{Z}\xrightarrow{\ \pi\ }\mathbb{Z}/n\to0,$$

与 $$\mathbb{Z}/n$$ 张量积。张量函子保满射，故 $$\pi\otimes1$$ 仍满；而左边一列变成

$$\mathbb{Z}/n\xrightarrow{\ n\cdot}\mathbb{Z}/n\xrightarrow{\ \pi\otimes1\ }0,$$

其中第一个映射是「乘以 $$n$$」，在 $$\mathbb{Z}/n$$ 上是**零映射**（因为 $$n\cdot\bar a=\overline{na}=0$$）。它的核是全部的 $$\mathbb{Z}/n$$，而不是 $$0$$：

$$\ker\bigl(n\cdot:\mathbb{Z}/n\to\mathbb{Z}/n\bigr)=\mathbb{Z}/n\ \ne\ 0.$$

所以「核 $$\to$$ 核」这一步不成立，张量函子**不左正合**。这个缺陷就是 $$\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/n,\mathbb{Z}/n)\cong\mathbb{Z}/n$$ 的来源。第 68 章把「正合」在 Abel 范畴里写成短正合列的语言、并把左手侧的不正合算成导出函子，本章 3.21 的那句「左伴随只承诺余极限」正是那条线索的起点。

## 七、Takeaway 与延伸 (Takeaways)

**1. Yoneda 引理是「对象 = 它的探测记录」的精确化。** $$\operatorname{Nat}(h_A,F)\cong F(A)$$ 的两句话是：一个自然变换被它的一个值决定（$$\Phi_A(1_A)$$），而一个元素能**长出**一个自然变换（$$\Phi_Y(f)=F(f)(x)$$）。推论 3.10–3.12 是它的三个后果——对象由可表函子决定、表示唯一、万有元是最通用的元素。本章所有「同构」的证明几乎都走了同一条路：算 Hom 集，得到自然同构，再用 Yoneda 收口（定理 3.20、3.21 就是这么证的）。

**2. 伴随是「一对可逆的对应」，不是「两个相似的函子」。** 定义 3.13 的全部内容就是双射 $$\mathcal{D}(Fc,d)\cong\mathcal{C}(c,Gd)$$ 加两条自然性。定理 3.15 给出它的等价刻画：一对自然变换 $$\eta,\varepsilon$$ 加两条三角恒等式。前者便于验证，后者便于使用；两种语言在本章都反复出现。

**3. ch32 的「各保一半」在这里被统一解释。** 第 64 章看到张量保满射、Hom 保单射却各差一半；本章 3.19–3.21 给出原因：左伴随 $$-\otimes_R A$$ 保一切**余**极限，右伴随 $$\operatorname{Hom}_S(C,-)$$ 保一切**极限**，谁都不承诺另一半。推论 3.22 把它变成判定法：**保不了（余）极限的函子不可能是左（右）伴随**（例 3.22 用它判掉了 $$U:\mathbf{Grp}\to\mathbf{Set}$$ 做左伴随的可能，竞4 用它判掉了 $$U:\mathbf{Field}\to\mathbf{Set}$$ 有左伴随的可能）。

**4. 第 40 章的 Gelfand 对偶被认出是一对伴随。** $$C\dashv\Delta$$、单位与余单位都是同构、因而是一对**范畴等价**（定理 3.23）。「元素就是函数」这句话的精确形式是 $$\Delta=h_{\mathbb{C}}$$——谱是可表函子，几何的点就是代数到 $$\mathbb{C}$$ 的态射。「几何 ↔ 物理 ↔ 代数」三条主线上最锋利的一段就在这里：**代数对象与几何空间之间的翻译可以完全没有信息损失**。

**5. 下一步：伴随留下的两个礼物。** 一是**单子**：研1 已经从任意伴随 $$F\dashv G$$ 造出了 $$(T=GF,\eta,\mu)$$ 并验证了三条公理；第 68 章会反过来证明每个单子都来自某个伴随（Kleisli / Eilenberg–Moore 构造），于是「伴随」与「单子」是同一份数据的两个信封。二是**正合**：3.21 那条「左伴随只承诺余极限」的缺口需要被度量，而度量它的语言是短正合列与导出函子——这就是第 68 章的 **Abel 范畴**与第 70 章的 $$\operatorname{Tor}$$、$$\operatorname{Ext}$$。

**下一章的悬念。** 研2 里算出的 $$\ker(n\cdot:\mathbb{Z}/n\to\mathbb{Z}/n)=\mathbb{Z}/n$$ 是一个具体的「缺口」。第 68 章会把它写成一个可加函子 $$\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/n,\mathbb{Z}/n)\cong\mathbb{Z}/n$$，并说明这正是「把不正合的量精确量出来」的第一例。问题的形状是：**左伴随保余极限、右伴随保极限，那么「没被保住的那一半」能不能也被组织成一个函子？**

**延伸阅读。** Mac Lane《Categories for the Working Mathematician》第 III 章第 2 节（Yoneda）与第 IV 章（伴随）；Riehl《Category Theory in Context》第 2、4 章；Leinster《Basic Category Theory》第 2、4 章。拓扑侧的同伦解释见 Hatcher《Algebraic Topology》第 4.3 节。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch65_伴随函子与Yoneda引理_上.md">← 第65章 伴随函子与Yoneda 引理·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch67_单子_Abel范畴与正合_上.md">第67章 单子、Abel 范畴与正合·上 →</a></div>
</div>
