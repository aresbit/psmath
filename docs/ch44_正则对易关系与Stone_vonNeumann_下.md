---
layout: default
---

# 第44章: 正则对易关系与 Stone–von Neumann·下：完整推导 (Canonical Commutation Relations and Stone–von Neumann · Part II: Full Derivation)

> 对应原专栏: MP57–MP58
> 专家依据: `_experts/analysis/spectral-theory.md`（主）+ `_experts/analysis/functional-analysis.md`（主）；`_experts/algebra/lie-algebra-root-systems.md`（对易子的代数侧）
> 知识库依据: `opc2/knowledge/math/泛函分析/`、`opc2/knowledge/math/李代数/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）
> 配套预备: 见 第43章 正则对易关系与 Stone–von Neumann·上（同一主题的具体铺垫，建议先读）

## 一、本章概要 (Overview)

本章只做一件事：把 $$[X,P]=i\hbar$$ 这一条关系**当成全部**，追问它究竟决定了什么。三个结论依次出现：这个关系不可能被一对有界算子承载（第 42 章的无界世界是它的天然居所）；指数化之后它只涉及酉算子，成为 Weyl 关系，而 Weyl 关系正是Heisenberg群——一个 Lie 群——的群律；满足 Weyl 关系的不可约实现，在酉等价意义下只有一种，就是 $$L^2(\mathbb R)$$ 上"乘以 $$x$$"与"$$-i\hbar$$ 求导"这一对，这就是 Stone–von Neumann 定理。

逻辑上本章是卷三的收官：第 32 章的对易子、第 34 章的谐振子升降算子、第 42 章的 Stone 定理，在这里合流成一句话——**对易关系是一个 Lie 代数，指数化后是它的 Lie 群，而唯一性是表示论的第一条定理**。这条线在卷四会以完全一般的 Lie 群表示论（第 54 章）与射影表示（第 60 章）形式回来。

## 二、入口：一道具体的问题 (Entry Problem)

**入口题（自编，取材于 Wielandt–Wintner 定理与 Hall《Quantum Theory for Mathematicians》(GTM 267) 第 14 章的引例）**

设 $$\mathcal H$$ 是复Hilbert 空间，$$A,B$$ 是 $$\mathcal H$$ 上两个**有界**线性算子。

**(1)** 若 $$\mathcal H$$ 有限维，证明 $$AB-BA=I$$ 不可能成立。

**(2)** 若 $$\mathcal H$$ 无限维，证明上面的结论**仍然**成立：$$AB-BA=I$$ 在有界算子的范围内无解。于是"位置"与"动量"这样一对算子根本不可能同时有界——它们必然是**无界**的。

**(3)** 现在转到 $$L^2(\mathbb R)$$，具体写出这样一对无界算子，然后回答本章真正的问题：

> 设 $$\mathcal H$$ 上有一对自伴算子 $$X,P$$ 满足 $$[X,P]=i\hbar$$。只凭这一条关系，你能确定 $$X,P$$ **长什么样**吗？所有满足它的实现，是不是都只是同一个东西在"换视角"（酉变换）之后的样子？还是说，存在彼此**不酉等价**的多种实现？

第 (1)(2) 问是经典结论，第 (3) 问是 Stone–von Neumann 定理的问题化表述——它是本章的主线，答案在第三节的定理 3.11。请注意这道题的提问方式：**不给定义、不给背景，只给一个关系式，问它能推出多少**。这正是俄罗斯数学圈的入口风格，也是本章唯一的动机来源。

## 三、结构：定义与完整推导 (Structure & Proof)

**定义 3.1（对易子, commutator）** 设 $$A,B$$ 是Hilbert 空间 $$\mathcal H$$ 上的两个线性算子（可以无界）。在公共定义域上定义
$$[A,B]:=AB-BA .$$
它度量"两个算子复合的顺序之差"。对易子满足三条恒等式：

**(i) 双线性** $$[\alpha A+\beta B,C]=\alpha[A,C]+\beta[B,C]$$，对第二变元同理；

**(ii) 反交换** $$[A,B]=-[B,A]$$，特别地 $$[A,A]=0$$；

**(iii) Jacobi 恒等式** $$[A,[B,C]]+[B,[C,A]]+[C,[A,B]]=0$$。

(i)(ii)(iii) 恰好就是第 54 章将要定义的 **Lie 代数 (Lie algebra)** 的三条公理：对易子就是算子代数上的 Lie 括号。这是本章把"对易关系"抽象成"Lie 代数"的全部理由。

三条的验证都是直接展开。以 (iii) 为例：把六个乘积项 $$ABC-ACB-BCA+CBA+CAB-CBA-\cdots$$ 完全展开，每一个形如 $$AXY$$ 的项都在 $$[A,[B,C]]$$ 与 $$[B,[C,A]]$$ 里各出现一次而符号相反，故总和为零。∎

**定义 3.2（正则对易关系, canonical commutation relation, CCR）** 设 $$X,P$$ 是 $$\mathcal H$$ 上的自伴算子。若存在一个稠密线性子空间 $$D\subseteq\operatorname{Dom}(XP)\cap\operatorname{Dom}(PX)$$，它在 $$X$$ 与 $$P$$ 下不变（即 $$X D\subseteq D$$、$$P D\subseteq D$$），且
$$[X,P]\psi=XP\psi-PX\psi=i\hbar\,\psi\qquad(\psi\in D),$$
即 $$[X,P]=i\hbar I$$ 在 $$D$$ 上成立，则称 $$X$$ 为**位置算子 (position operator)**、$$P$$ 为**动量算子 (momentum operator)**，称 $$D$$ 为关系的一个**定义域 (domain)**，上式称为**正则对易关系**。

这里必须交代定义域：由引理 3.4 知 $$X,P$$ 不可能同时有界，而两个无界算子的复合 $$XP$$ 只在 $$\operatorname{Dom}(XP)$$ 上有意义，所以"$$[X,P]=i\hbar$$"这句话只有在指定了公共不变定义域 $$D$$ 之后才是一个数学命题。第 42 章的无界算子语言在这里第一次被真正用上。

**定义 3.3（Heisenberg代数, Heisenberg algebra）** 设 $$\mathfrak h$$ 是复向量空间，以 $$X,P,Z$$ 为基，其上括号由
$$[X,P]=Z,\qquad [X,Z]=0,\qquad [P,Z]=0$$
双线性延拓给出。称 $$\mathfrak h$$ 为三维**Heisenberg代数**。在正则对易关系的一个实现中，取 $$\mathfrak h=\operatorname{span}\{X,\,P,\,i\hbar I\}$$，此时中心元 $$Z$$ 被送到标量 $$i\hbar I$$。

Heisenberg代数是本章的"代数骨架"：**把具体的算子忘掉，只留下对易关系，得到的就是它**。关系式 $$[X,P]=i\hbar I$$ 的全部内容，等价于说"$$(\mathfrak h,[\cdot,\cdot])$$ 的一个表示把中心元 $$Z$$ 送到 $$i\hbar I$$"。后面的 Stone–von Neumann 定理，说的就是这个表示的**唯一性**。

**命题 3.3（Heisenberg代数是幂零的）** $$\mathfrak h$$ 满足 $$[\mathfrak h,\mathfrak h]=\mathbb C Z$$ 且 $$[\mathfrak h,[\mathfrak h,\mathfrak h]]=0$$。因此它是幂零但非交换的，并且是维数最小的非交换幂零 Lie 代数；它的导出代数严格小于自身，所以它**不可能是半单的**。

**证明** $$\mathfrak h$$ 的基中两两括号里，只有 $$[X,P]=Z$$ 非零，故 $$[\mathfrak h,\mathfrak h]=\mathbb C Z$$。于是
$$\mathfrak h^1:=\mathfrak h,\qquad \mathfrak h^2:=[\mathfrak h,\mathfrak h]=\mathbb C Z,\qquad \mathfrak h^3:=[\mathfrak h,\mathfrak h^2]=[\mathfrak h,\mathbb C Z]=0,$$
下中心列归零，故幂零。又 $$[\mathfrak h,\mathfrak h]=\mathbb C Z\neq\mathfrak h$$；而第 56 章将证明半单李代数必须满足 $$[L,L]=L$$，所以 $$\mathfrak h$$ 不半单。维数最小的非交换 Lie 代数是二维的 $$[x,y]=x$$（它可解而非幂零），故非交换幂零的最小维数是 $$3$$。∎

**引理 3.4（有界情形的不可能性, Wielandt–Wintner）** 设 $$\mathcal A$$ 是含单位元的巴拿赫代数。则不存在 $$A,B\in\mathcal A$$ 满足 $$AB-BA=I$$。

**证明思路**：先把恒等式不断与 $$A$$ 取括号，得到的算子含 $$n!$$ 因子；再用预解式把它写成 $$\lambda I-B$$ 的幂，与范数估计比较，令 $$n\to\infty$$ 由阶乘快于指数增长导出矛盾。

**证明** 先建立一个恒等式。由 $$[A,B]=I$$，对一切 $$n\ge1$$ 有
$$[A,B^n]=nB^{n-1}.$$
（对 $$n$$ 归纳：$$[A,B^{n+1}]=[A,B^n]B+B^n[A,B]=nB^{n-1}B+B^n\cdot I=(n+1)B^n$$。这里用了 Leibniz 法则 $$[A,BC]=[A,B]C+B[A,C]$$。）

取 $$\lambda\in\mathbb C$$ 满足 $$\lvert\lambda\rvert>\lVert B\rVert$$，则 $$R:=(\lambda I-B)^{-1}$$ 存在，且 $$\lVert R\rVert\le(\lvert\lambda\rvert-\lVert B\rVert)^{-1}$$。注意 $$\lambda I-B=R^{-1}$$，故 $$\lVert R^{-1}\rVert\le\lvert\lambda\rvert+\lVert B\rVert$$。对恒等式 $$I=(\lambda I-B)R$$ 与 $$A$$ 取括号：
$$0=[A,I]=[A,\lambda I-B]R+(\lambda I-B)[A,R]=-R+(\lambda I-B)[A,R],$$
其中用了 $$[A,\lambda I-B]=-[A,B]=-I$$。于是
$$[A,R]=(\lambda I-B)^{-1}R=R^{2}.$$
对 $$k$$ 归纳得 $$[A,R^{k}]=kR^{k+1}$$；再对 $$n$$ 归纳得
$$\operatorname{ad}_A^{\,n}(R)=n!\,R^{\,n+1},\qquad \operatorname{ad}_A T:=[A,T].$$
（$$\operatorname{ad}_A^{n}(R)=[A,n!R^{n+1}]=n!\,[A,R^{n+1}]=n!(n+1)R^{n+2}=(n+1)!R^{n+2}$$。）

另一方面，$$\lVert\operatorname{ad}_A T\rVert\le2\lVert A\rVert\lVert T\rVert$$，迭代得 $$\lVert\operatorname{ad}_A^{\,n}(R)\rVert\le(2\lVert A\rVert)^n\lVert R\rVert$$。又 $$R^{n+1}$$ 可逆且 $$(R^{n+1})^{-1}=(\lambda I-B)^{n+1}$$，故
$$1=\lVert R^{n+1}(\lambda I-B)^{n+1}\rVert\le\lVert R^{n+1}\rVert\,\lVert\lambda I-B\rVert^{n+1},$$
即 $$\lVert R^{n+1}\rVert\ge\lVert\lambda I-B\rVert^{-(n+1)}$$。两边的下界与上界合并：
$$n!\le(2\lVert A\rVert)^{n}\,\lVert R\rVert\,\lVert\lambda I-B\rVert^{\,n+1}\qquad(n=1,2,3,\dots).$$
右端关于 $$n$$ 是等比增长（公比 $$2\lVert A\rVert\lVert\lambda I-B\rVert$$ 与 $$n$$ 无关），左端是阶乘增长。取 $$n$$ 充分大即得矛盾。∎

**推论** 正则对易关系 $$[X,P]=i\hbar$$ 的两个自伴算子 $$X,P$$ 不可能同时有界。

**证明** 若有界，则 $$A=X$$、$$B=P/(i\hbar)$$ 是巴拿赫代数 $$B(\mathcal H)$$ 中两个元，且
$$AB-BA=\tfrac1{i\hbar}(XP-PX)=\tfrac1{i\hbar}\cdot i\hbar I=I,$$
与引理 3.4 矛盾。∎

这条推论解释了入口题第 (2) 问，也解释了为什么"位置算子"必须定义在 $$\operatorname{Dom}\mathsf X=\{\psi:\int x^2\lvert\psi\rvert^2<\infty\}$$ 这样的真子空间上。

**定义 3.5（Weyl 关系, Weyl relations）** 设 $$\mathcal H$$ 是Hilbert 空间，$$s,t\in\mathbb R$$。一族酉算子 $$\{U(s)\}_{s\in\mathbb R}$$ 与 $$\{V(t)\}_{t\in\mathbb R}$$ 若满足
$$U(s)U(s')=U(s+s'),\qquad U(0)=I,$$
$$V(t)V(t')=V(t+t'),\qquad V(0)=I,$$
$$U(s)V(t)=e^{-i\hbar st}\,V(t)U(s),$$
并且对每个 $$\xi\in\mathcal H$$，映射 $$s\mapsto U(s)\xi$$、$$t\mapsto V(t)\xi$$ 都连续（**强连续 (strongly continuous)**），则称 $$(U,V)$$ 是正则对易关系的一个 **Weyl 形式 (Weyl form)**，或称 $$(U,V)$$ 是一个 **Weyl 系统 (Weyl system)**。

Weyl 形式里出现的全是**有界算子**（酉算子），没有定义域的负担。代价是：无穷小的关系 $$[X,P]=i\hbar$$ 被换成了有限的群律。记
$$W(s,t):=e^{i\hbar st/2}\,U(s)V(t),$$
由定义逐项计算（把 $$V(t)U(s')=e^{i\hbar s't}U(s')V(t)$$ 代入）得
$$W(s,t)W(s',t')=e^{\frac{i\hbar}{2}(s't-st')}\,W(s+s',t+t'),\qquad W(s,t)^{*}=W(-s,-t).$$
这正是**Heisenberg群** $$H_3(\mathbb R)$$ 的群律的表示论影子（见第四节）。

**命题 3.6（对易关系蕴含 Weyl 关系）** 设 $$X,P$$ 自伴，$$[X,P]=i\hbar$$ 在公共不变定义域 $$D$$ 上成立，且 $$D$$ 是 $$X$$ 与 $$P$$ 的公共解析向量空间（例如 $$L^2(\mathbb R)$$ 中的 Schwartz 空间 $$\mathcal S(\mathbb R)$$）。则 $$U(s):=e^{isX}$$、$$V(t):=e^{itP}$$ 是酉算子，且满足 Weyl 关系。

**证明** $$X,P$$ 自伴，故 $$e^{isX},e^{itP}$$ 是酉算子（$$\left(e^{isX}\right)^{*}=e^{-isX}=\left(e^{isX}\right)^{-1}$$）。用 Baker–Campbell–Hausdorff 公式：当 $$[A,B]$$ 与 $$A,B$$ 都交换时，级数在 $$[A,B]$$ 处截断，
$$e^{A}e^{B}=\exp\!\left(A+B+\tfrac12[A,B]\right).$$
取 $$A=isX$$、$$B=itP$$。由于 $$[X,P]=i\hbar I$$ 是标量，它与 $$X,P$$ 交换，故截断成立：
$$[A,B]=[isX,itP]=-st\,[X,P]=-i\hbar st\,I,$$
$$e^{A}e^{B}=\exp\!\left(isX+itP-\tfrac{i}{2}\hbar st\right).$$
同理 $$e^{B}e^{A}=\exp(isX+itP+\tfrac{i}{2}\hbar st)$$。两式相除（指数上的标量相加即算子相乘）得
$$e^{isX}e^{itP}=e^{-i\hbar st}\,e^{itP}e^{isX}.$$
$$U(s)U(s')=e^{isX}e^{is'X}=e^{i(s+s')X}=U(s+s')$$ 等三条同理。∎

**定理 3.7（Stone 定理）** 设 $$t\mapsto U(t)$$ 是 $$\mathcal H$$ 上强连续的单参数酉群（$$U(t+s)=U(t)U(s)$$、$$U(0)=I$$、$$t\mapsto U(t)\xi$$ 连续）。则存在**唯一**的自伴算子 $$X$$ 使 $$U(t)=e^{itX}$$。

**证明思路**：在"可微向量"集合 $$\mathcal D=\{ \xi: \lim_{t\to0}\frac{U(t)\xi-\xi}{t}\ \text{存在}\}$$ 上定义 $$iX\xi=\lim_{t\to0}\frac{U(t)\xi-\xi}{t}$$；用 $$U(t)$$ 的酉性与群律证明 $$\mathcal D$$ 稠密、$$X$$ 对称；再用 $$(X\pm i)$$ 值域封闭（这是把 $$e^{\pm i t X}$$ 与谱定理接上的关键一步）得到 $$X$$ 自伴；唯一性来自生成元的定义本身。

**这是第 42 章的核心结论，此处引用而不重证**（完整证明见第 42 章）。它在这里的作用是把通道打通成双向：命题 3.6 从自伴算子造出单参数酉群，Stone 定理反过来从单参数酉群找回唯一的自伴算子。于是"Weyl 系统"与"一对自伴算子 $$X,P$$"是同一件事的两种说法，可以自由往返。

**定义 3.8（Schrödinger 表示, Schrödinger representation）** 取 $$\mathcal H=L^2(\mathbb R)$$，定义
$$(\mathsf X\psi)(x)=x\,\psi(x),\qquad \operatorname{Dom}\mathsf X=\Bigl\{\psi\in L^2:\int_{\mathbb R}x^{2}\lvert\psi(x)\rvert^{2}\,dx<\infty\Bigr\},$$
$$(\mathsf P\psi)(x)=-i\hbar\,\psi'(x),\qquad \operatorname{Dom}\mathsf P=H^{1}(\mathbb R)=\{\psi\in L^2:\psi'\in L^2\}.$$
称 $$(\mathsf X,\mathsf P)$$ 为 $$L^2(\mathbb R)$$ 上的 **Schrödinger 表示**（位置与动量的标准实现）。对应的单参数酉群是
$$\bigl(e^{is\mathsf X}\psi\bigr)(x)=e^{isx}\psi(x),\qquad \bigl(e^{it\mathsf P}\psi\bigr)(x)=\psi(x+\hbar t).$$

这里 $$\mathsf X$$ 是乘法算子、$$\mathsf P$$ 是求导算子；两者都是无界自伴算子（$$\mathsf X$$ 的谱是整个实轴，$$\mathsf P$$ 由 Fourier 变换化归为 $$\mathsf X$$，见第六节竞 1）。

**引理 3.9（Schrödinger 表示满足 Weyl 关系）** 上例中的 $$U(s)=e^{is\mathsf X}$$、$$V(t)=e^{it\mathsf P}$$ 构成 Weyl 系统。

**证明** 在稠密的 Schwartz 空间 $$\mathcal S(\mathbb R)\subset L^2$$ 上计算（$$\mathcal S(\mathbb R)$$ 在 $$\mathsf X,\mathsf P$$ 下不变）。对 $$\psi\in\mathcal S(\mathbb R)$$：
$$\bigl(U(s)V(t)\psi\bigr)(x)=e^{isx}\bigl(V(t)\psi\bigr)(x)=e^{isx}\,\psi(x+\hbar t),$$
$$\bigl(V(t)U(s)\psi\bigr)(x)=\bigl(U(s)\psi\bigr)(x+\hbar t)=e^{is(x+\hbar t)}\,\psi(x+\hbar t)=e^{i\hbar st}\,e^{isx}\,\psi(x+\hbar t).$$
两次结果相差因子 $$e^{-i\hbar st}$$，故在 $$\mathcal S(\mathbb R)$$ 上成立；两边是有界算子，$$\mathcal S(\mathbb R)$$ 稠密，故在全 $$L^2$$ 上成立。单参数群性 $$U(s)U(s')=U(s+s')$$ 由指数律直接得到，强连续性由 $$\lVert U(s)\psi-\psi\rVert\to0\ (s\to0)$$（有界收敛 + $$\mathcal S$$ 上稠密）得到。∎

**定理 3.10（Schrödinger 表示的不可约性）** $$L^2(\mathbb R)$$ 上不存在非平凡的闭子空间同时被所有 $$U(s),V(t)$$ 保持；等价地，与所有 $$U(s),V(t)$$ 交换的有界算子只有标量 $$cI$$。

**证明思路**：先证"与所有 $$U(s)$$ 交换 $$\Rightarrow$$ 是乘法算子"，再用"与所有平移 $$V(t)$$ 交换 $$\Rightarrow$$ 该乘法函数是常数"。

**证明** 设 $$T\in B(L^2)$$ 与一切 $$U(s)$$ 交换。记 $$e_s(x)=e^{isx}$$，则 $$U(s)=M_{e_s}$$（乘 $$e_s$$）。函数族 $$\{e_s\}_{s\in\mathbb R}$$ 分离 $$\mathbb R$$ 上的点、含常函数 $$e_0=1$$、对乘法与共轭封闭（$$e_se_{s'}=e_{s+s'}$$，$$\overline{e_s}=e_{-s}$$）。由 Stone–Weierstrass 定理，它在任意紧区间上的连续函数代数中稠密；因此 $$\{e_s\}$$ 生成的 $$\sigma$$-代数是 Borel $$\sigma$$-代数，从而由 $$\{U(s)\}$$ 生成的 von Neumann 代数正是乘法算子代数 $$\{M_f:f\in L^\infty(\mathbb R)\}$$。于是 $$T=M_g$$ 对某个 $$g\in L^\infty$$。

（这一步是乘法代数作为**极大交换 von Neumann 代数**的标准性质：乘法代数 $$\{M_f\}$$ 包含全部谱投影 $$M_{\chi_E}$$（$$E$$ 取遍 Borel 集），故它的交换子就是它自身；于是与全体 $$M_f$$ 交换的 $$T$$ 必是某个 $$M_g$$。）

再要求 $$T$$ 与一切 $$V(t)$$ 交换。记平移 $$(\tau_a\varphi)(x)=\varphi(x+a)$$，则 $$V(t)=\tau_{\hbar t}$$。由 $$M_g\tau_{\hbar t}=\tau_{\hbar t}M_g$$ 得
$$g(x+\hbar t)\,\varphi(x+\hbar t)=g(x)\,\varphi(x+\hbar t)\quad\text{对一切}\ \varphi\in L^2,$$
取 $$\varphi$$ 在 $$x$$ 的邻域内为正即得 $$g(x+\hbar t)=g(x)$$ 几乎处处，对一切 $$t\in\mathbb R$$。因 $$\hbar\neq0$$，$$g$$ 在整个 $$\mathbb R$$ 上几乎处处等于常数 $$c$$，即 $$T=cI$$。

最后把不可约性接上：算子族 $$\{U(s),V(t)\}$$ 对伴随封闭（$$U(s)^{*}=U(-s)$$，$$V(t)^{*}=V(-t)$$）。若有非平凡闭不变子空间 $$M$$，则因 $$U,V$$ 是酉算子，$$M^{\perp}$$ 也不变，故正交投影 $$P_M$$ 与全体 $$U,V$$ 交换且 $$P_M\neq0,I$$，与"交换子只有标量"矛盾。∎

**引理 3.11（von Neumann 投影）** 定义
$$P_0=\frac{1}{2\pi}\iint_{\mathbb R^{2}}e^{-(s^{2}+t^{2})/4}\,e^{-i(s\mathsf X+t\mathsf P)}\,ds\,dt .$$
则 $$P_0$$ 是 $$L^2(\mathbb R)$$ 上到一维子空间 $$\mathbb C\Omega$$ 的正交投影，其中 $$\Omega(x)=\pi^{-1/4}e^{-x^{2}/2}$$ 是归一化高斯（谐振子基态）。特别地 $$P_0\neq0$$、$$P_0^{2}=P_0=P_0^{*}$$。

**证明** 第五节经典问题精讲题 4 给出逐项计算：把 $$\bigl(e^{-i(s\mathsf X+t\mathsf P)}\psi\bigr)(x)=e^{ist/2}e^{-isx}\psi(x-t)$$ 代入，先对 $$s$$ 积分（高斯积分 $$\int e^{-s^{2}/4}e^{-is(x-t/2)}ds=2\sqrt\pi\,e^{-(x-t/2)^{2}}$$），再对 $$t$$ 配方，指数合并为 $$-(x^{2}+y^{2})/2$$（$$y=x-t$$），最终化为
$$P_0\psi=\Bigl(\frac1{\sqrt\pi}\int_{\mathbb R}e^{-y^{2}/2}\psi(y)\,dy\Bigr)e^{-x^{2}/2}=\langle\Omega,\psi\rangle\,\Omega .$$
故 $$P_0=\lvert\Omega\rangle\langle\Omega\rvert$$ 是秩一正交投影。这里的逐项指数配方与积分都是显式的，没有引理之外的假设。∎

**定理 3.11（Stone–von Neumann）** 设 $$(U,V)$$ 是可分Hilbert 空间 $$\mathcal H$$ 上的 Weyl 系统（定义 3.5）。则存在一族（有限或可数）正交闭子空间 $$\mathcal H_j$$ 与酉算子
$$W_j:\mathcal H_j\longrightarrow L^{2}(\mathbb R),$$
使得 $$\mathcal H=\bigoplus_j\mathcal H_j$$，每个 $$\mathcal H_j$$ 在全体 $$U(s),V(t)$$ 下不变，且
$$W_jU(s)W_j^{-1}=e^{is\mathsf X},\qquad W_jV(t)W_j^{-1}=e^{it\mathsf P}\qquad\text{（对一切 }s,t\text{）}.$$
特别地，**若 $$(U,V)$$ 不可约，则直和只有一个分量**：任何不可约 Weyl 系统都酉等价于 Schrödinger 表示。换言之，在不可约情形，$$L^2(\mathbb R)$$ 上那一对 $$(\mathsf X,\mathsf P)$$ 是满足正则对易关系的**唯一**实现（差一个酉变换）。

**证明思路（三步）**

**第一步（从不可约性降下唯一性）**：设 $$(U,V)$$ 与 $$(U',V')$$ 是两个不可约 Weyl 系统。定义它们在直和上的"对角"系统 $$\widetilde U=U\oplus U'$$、$$\widetilde V=V\oplus V'$$，它一般可约。用下面的第二步构造出的投影把直和拆开，再用 Schur 型论证（交换子只有标量 $$\Rightarrow$$ 两个不可约分量之间的缠绕算子唯一，见定理 3.10 的手法）得到唯一的酉等价。

**第二步（von Neumann 投影，全部困难所在）**：在一般 Weyl 系统中把引理 3.11 的积分替换为
$$P_0=\frac{1}{2\pi}\iint_{\mathbb R^{2}}e^{-(s^{2}+t^{2})/4}\,e^{i\hbar st/2}\,U(-s)V(-t)\,ds\,dt .$$
被积算子全是酉算子（范数 $$1$$），高斯权 $$\iint e^{-(s^{2}+t^{2})/4}ds\,dt=4\pi<\infty$$ 可积，故积分按算子范数收敛，$$P_0$$ 是有界算子（$$\lVert P_0\rVert\le2$$）。由 Weyl 关系与高斯卷积恒等式可以证明 $$P_0\neq0$$ 且 $$P_0^{2}=P_0=P_0^{*}$$——也就是说，**任何** Weyl 系统都自动含有一个"真空方向"。引理 3.11 是这一步在 Schrödinger 表示中的显式验证。

**第三步（直和分解）**：取 $$P_0$$ 的值域中的一个单位向量 $$\Omega_0$$，令 $$\mathcal H_j$$ 为 $$\Omega_0$$ 在全体 $$W(s,t)$$ 下的闭轨道张成。由第二步的构造，$$\mathcal H_j$$ 不可约；再把 $$\mathcal H_j^{\perp}$$ 上的限制重复第二步，得可数正交分解。

我们完整证明了第一、二步在 Schrödinger 表示中的可实现性（引理 3.11）、不可约性的判据（定理 3.10）与逆命题（引理 3.9）；第二步在一般 Weyl 系统中的"$$P_0$$ 是非零投影"以及第三步的完备性需要测度论式的积分论证，其标准叙述见 Hall《Quantum Theory for Mathematicians》(GTM 267) 第 14 章。∎

**推论 3.12（测不准原理）** 设 $$X,P$$ 自伴，$$[X,P]=i\hbar$$ 在公共不变定义域 $$D$$ 上成立，$$\psi\in D$$ 且 $$\lVert\psi\rVert=1$$。记 $$\Delta X=\lVert(X-\langle X\rangle I)\psi\rVert$$、$$\Delta P=\lVert(P-\langle P\rangle I)\psi\rVert$$（$$\langle X\rangle=\langle\psi,X\psi\rangle$$），则
$$\Delta X\cdot\Delta P\ge\frac{\hbar}{2}.$$

**证明** 记 $$A_0=X-\langle X\rangle I$$、$$B_0=P-\langle P\rangle I$$。由自伴性，$$\Delta X=\lVert A_0\psi\rVert$$、$$\Delta P=\lVert B_0\psi\rVert$$。用 Cauchy–Schwarz 与虚部估计：
$$\lVert A_0\psi\rVert\,\lVert B_0\psi\rVert\ge\lvert\langle A_0\psi,B_0\psi\rangle\rvert\ge\bigl\lvert\operatorname{Im}\langle A_0\psi,B_0\psi\rangle\bigr\rvert .$$
而 $$\langle A_0\psi,B_0\psi\rangle=\langle B_0A_0\psi,\psi\rangle$$（用 $$B_0$$ 自伴），故其共轭为 $$\langle A_0B_0\psi,\psi\rangle$$，于是虚部可以整体估掉：
$$\operatorname{Im}\langle A_0\psi,B_0\psi\rangle=\frac{1}{2i}\bigl(\langle B_0A_0\psi,\psi\rangle-\langle A_0B_0\psi,\psi\rangle\bigr)=\frac{1}{2i}\bigl(-\langle[A_0,B_0]\psi,\psi\rangle\bigr)=-\frac{\hbar}{2}.$$
下标平移不改变对易子，即 $$[A_0,B_0]=[X,P]=i\hbar I$$，所以 $$\bigl\lvert\operatorname{Im}\langle A_0\psi,B_0\psi\rangle\bigr\rvert=\hbar/2$$。代入上面的不等式即得
$$\Delta X\,\Delta P\ge\frac{\hbar}{2}. \quad\blacksquare$$

**推论 3.13（图景的酉等价，MP57）** 设 $$H$$ 是自伴 Hamilton 算子。时间演化算子 $$U(t)=e^{-iHt/\hbar}$$ 是强连续单参数酉群（定理 3.7 的生成元为 $$-H/\hbar$$），且 $$\psi(t)=U(t)\psi(0)$$ 就是 Schrödinger 方程 $$i\hbar\partial_t\psi=H\psi$$ 的解。取任意酉算子 $$\mathcal U$$ 作变换
$$\mathsf X'=\mathcal U\mathsf X\mathcal U^{-1},\qquad \mathsf P'=\mathcal U\mathsf P\mathcal U^{-1},$$
则 $$(\mathsf X',\mathsf P')$$ 仍满足正则对易关系；由定理 3.11，$$\mathsf X',\mathsf P'$$ 在不可约情形必酉等价于 $$(\mathsf X,\mathsf P)$$。**"换视角"不改变对易关系，"换视角"也穷尽了一切实现**——这正是 MP57 里"酉变换只是改变观察视角"的精确含义。


## 四、几何与物理直觉 (Intuition)

同一件事有三组语言：几何（相空间与辛结构）、物理（测不准与图景）、代数（Lie 代数与表示）。本节把三者摆到一起。

**一、相空间与辛结构。** 经典力学里位置与动量张成相空间 $$\mathbb R^{2}$$，其上辛形式是 $$\omega\bigl((x,p),(x',p')\bigr)=xp'-px'$$（第 08 章）。在相空间坐标下，Poisson 括号给出 $$\{x,p\}=1$$。正则对易关系就是它的量子化影子：
$$\{x,p\}=1\qquad\longmapsto\qquad [X,P]=i\hbar\,I .$$
也就是说，把 Poisson 括号换成 $$\frac1{i\hbar}[\cdot,\cdot]$$。**整个量子运动学的输入只有这一条关系**，本章剩下的全部工作都是在问：这一条能推出多少？答案分两半——推出的东西很多（Weyl 关系、测不准原理、谐振子能谱、时间演化的群结构），但**实现只有一种**（定理 3.11）。

**二、$$[X,P]$$ 的一个量子数：$$\pi/2$$ 旋转。** 把 $$[X,P]=i\hbar I$$ 作用到波函数上，它把 $$\psi$$ 整体乘以 $$i\hbar$$。在复平面上乘以 $$i$$ 是逆时针旋转 $$\pi/2$$。所以"位置与动量不对易"在几何上就是：**交换它们的顺序，等于对整个状态做一个 $$\pi/2$$ 的旋转再缩放 $$\hbar$$**。这个旋转正是辛形式 $$\omega$$ 对应的 $$90^{\circ}$$ 旋转（辛结构在相空间上的标准复结构），它把 $$x$$ 方向转到 $$p$$ 方向。物理上它对应"位置与动量是不可交换的共轭量"。

**三、Weyl 关系 = 相空间平移的射影表示。** 相空间 $$\mathbb R^{2}$$ 的平移构成交换群。物理上位置平移由 $$V(t)=e^{itP}$$ 实现、动量平移由 $$U(s)=e^{isX}$$ 实现（在 Schrödinger 表示中就是 $$\psi(x)\mapsto\psi(x+\hbar t)$$ 与 $$\psi(x)\mapsto e^{isx}\psi(x)$$）。Weyl 关系 $$U(s)V(t)=e^{-i\hbar st}V(t)U(s)$$ 说：两个平移的复合**差一个相位**。所以相空间平移群在Hilbert 空间上的作用不是普通表示，而是**射影表示 (projective representation)**，相位 $$(s,t)\mapsto e^{-i\hbar st}$$ 是 $$\mathbb R^{2}$$ 上的一个上循环 (cocycle)。

要把它变回真正的表示，就得把 $$\mathbb R^{2}$$ 扩大成**Heisenberg群** $$H_3(\mathbb R)$$：
$$(s,t,\theta)\cdot(s',t',\theta')=\Bigl(s+s',\ t+t',\ \theta+\theta'+\tfrac{\hbar}{2}(st'-s't)\Bigr).$$
这是一个中心扩张：$$1\to\mathbb R\to H_3(\mathbb R)\to\mathbb R^{2}\to1$$，中心是 $$\{(0,0,\theta)\}$$，而 $$W(s,t)=e^{i\hbar st/2}U(s)V(t)$$ 给出它的一个酉表示。于是 Stone–von Neumann 定理有了几何说法：**固定中心特征（即固定 $$\hbar$$）之后，$$H_3(\mathbb R)$$ 的不可约酉表示在等价意义下唯一。** 这是第 60 章"射影表示"的第一个、也是最著名的例子——上循环不平凡时，射影表示"提升"为中心扩张的真实表示，而提升后的不可约表示反而变唯一了。这条链（辛结构 $$\to$$ 射影表示 $$\to$$ 中心扩张 $$\to$$ 唯一性）是"几何 ↔ 物理 ↔ 代数"在本课程的又一处合流。

**四、谐振子 = 一条半有界的权链。** 第 34 章用 $$[X,P]=i\hbar$$ 造出升降算子
$$a=\sqrt{\frac{m\omega}{2\hbar}}\Bigl(X+\frac{iP}{m\omega}\Bigr),\qquad a^{\dagger}=\sqrt{\frac{m\omega}{2\hbar}}\Bigl(X-\frac{iP}{m\omega}\Bigr),$$
并且只用对易关系就得到 $$[a,a^{\dagger}]=I$$。记 $$N=a^{\dagger}a$$（粒子数算子），则
$$[N,a]=-a,\qquad [N,a^{\dagger}]=a^{\dagger}.$$
把 $$N,a,a^{\dagger},I$$ 放在一起，它们张成一个四维 Lie 代数 $$\mathfrak{osc}=\operatorname{span}\{N,a,a^{\dagger},I\}$$，其导出代数是 $$[\mathfrak{osc},\mathfrak{osc}]=\operatorname{span}\{a,a^{\dagger},I\}$$，恰是Heisenberg代数；再做一次导出得 $$[\operatorname{span}\{a,a^{\dagger},I\},\operatorname{span}\{a,a^{\dagger},I\}]=\mathbb C I$$，第二次就归零，故 $$\mathfrak{osc}$$ 可解。也就是说，**第 34 章那套升降算子的代数结构，就是"Heisenberg代数 + 一个测权算子 $$N$$"**。

$$N$$ 的本征值是 $$\mathbb N=\{0,1,2,\dots\}$$；$$a^{\dagger}$$ 升 $$1$$、$$a$$ 降 $$1$$，所以谱是等差阶梯。第 56 章会看到，$$\mathfrak{sl}(2)$$ 的不可约表示 $$V(m)$$ 也有一条这样的阶梯：$$h$$ 测权、$$x$$ 升权、$$y$$ 降权，权重是 $$m,m-2,\dots,-m$$。两处的代数机制完全一样，差别只在**阶梯的形态**：$$\mathfrak{sl}(2)$$ 的阶梯是有限的（$$m+1$$ 级），谐振子的阶梯是半有界无限的。这个差别决定了两者的表示论走向不同的结局——$$\mathfrak{sl}(2)$$ 的不可约表示由最高权 $$\mathbb N$$ 分类（第 56 章），而Heisenberg代数的不可约表示在固定 $$\hbar$$ 之后**只有一个**（定理 3.11）。

**五、物理上的三句总结。** 其一，测不准原理（推论 3.12）不是独立公理，它是对易关系的直接推论。其二，位置表象与动量表象之间的变换是 Fourier 变换（第六节竞 1），它是酉变换，所以是"换视角"而不是"换物理"。其三，Schrödinger 图景（态随时间演化、算符不动）与 Heisenberg 图景（算符演化、态不动）由 $$A_H(t)=U(t)^{-1}AU(t)$$ 联系，二者物理等价——这正是 MP57 的标题"从 Schrödinger 图景看酉变换"想说的：**图景是记账方式，不是不同的物理**。

## 五、经典问题精讲 (Classical Problems)

**题 1（验证 Schrödinger 表示）** 在 $$L^2(\mathbb R)$$ 上取 $$\mathsf X$$ 为乘 $$x$$、$$\mathsf P=-i\hbar\frac{d}{dx}$$。取 $$D=\mathcal S(\mathbb R)$$（Schwartz 空间）。
**(a)** 证明 $$[\mathsf X,\mathsf P]\psi=i\hbar\psi$$ 对一切 $$\psi\in D$$ 成立，并说明 $$\mathsf X D\subseteq D$$、$$\mathsf P D\subseteq D$$。
**(b)** 写出 $$e^{is\mathsf X}$$ 与 $$e^{it\mathsf P}$$ 的显式作用。

**考点**：定义 3.2（正则对易关系要指定定义域）与引理 3.9（Weyl 关系）。**位置**：把第三节最抽象的关系落到全书最具体的实现上，是后面一切讨论的"原型"。

**解 (a)** 对 $$\psi\in\mathcal S(\mathbb R)$$ 逐步计算：
$$(\mathsf X\mathsf P\psi)(x)=x\cdot\bigl(-i\hbar\psi'(x)\bigr)=-i\hbar x\,\psi'(x),$$
$$(\mathsf P\mathsf X\psi)(x)=-i\hbar\frac{d}{dx}\bigl[x\psi(x)\bigr]=-i\hbar\bigl(\psi(x)+x\psi'(x)\bigr)=-i\hbar\psi(x)-i\hbar x\psi'(x).$$
相减：
$$[\mathsf X,\mathsf P]\psi=\bigl(-i\hbar x\psi'\bigr)-\bigl(-i\hbar\psi-i\hbar x\psi'\bigr)=i\hbar\psi .$$
由于 $$\psi\in\mathcal S(\mathbb R)$$ 时 $$x\psi\in\mathcal S(\mathbb R)$$、$$\psi'\in\mathcal S(\mathbb R)$$，故 $$\mathsf X D\subseteq D$$、$$\mathsf P D\subseteq D$$，且 $$D$$ 在 $$L^2$$ 中稠密。三项定义域条件（稠密、不变、等式成立）全部满足，故 $$(\mathsf X,\mathsf P)$$ 满足正则对易关系。$$\blacksquare$$

**解 (b)** $$\mathsf X$$ 是乘法算子，其函数演算就是"乘以对应的函数"：$$e^{is\mathsf X}$$ 是乘 $$e^{isx}$$，即
$$\bigl(e^{is\mathsf X}\psi\bigr)(x)=e^{isx}\psi(x).$$
$$\mathsf P$$ 在 Fourier 侧的像也是乘法（见题 3），故 $$e^{it\mathsf P}$$ 是平移。也可以直接由 $$\mathsf P=-i\hbar\frac{d}{dx}$$ 与"$$e^{a\frac{d}{dx}}f(x)=f(x+a)$$"（把指数算子对 Taylor 级数逐项展开即得）看出：
$$\bigl(e^{it\mathsf P}\psi\bigr)(x)=\psi(x+\hbar t).$$
两者都是酉算子（前者是模为 $$1$$ 的函数乘法，后者是保测度的平移），且强连续。$$\blacksquare$$

**题 2（有界情形的不可能性：有限维版本）** 设 $$\mathcal H$$ 有限维，$$\dim\mathcal H=n<\infty$$。证明不存在矩阵 $$A,B$$ 使 $$AB-BA=I$$。

**考点**：引理 3.4 的"轻量版"。**位置**：它与引理 3.4 用两种完全不同的机制排除有界情形（迹 vs 预解式），对照着看能看清"迹"在这个问题里为什么失效于无限维。

**解** 用迹的循环性 $$\operatorname{tr}(AB)=\operatorname{tr}(BA)$$（因为 $$\operatorname{tr}(AB)=\sum_{i,j}A_{ij}B_{ji}=\sum_{i,j}B_{ji}A_{ij}=\operatorname{tr}(BA)$$）。于是
$$\operatorname{tr}(AB-BA)=\operatorname{tr}(AB)-\operatorname{tr}(BA)=0 .$$
但 $$\operatorname{tr}(I)=n\neq0$$（因 $$n\ge1$$）。等式 $$AB-BA=I$$ 两边取迹得 $$0=n$$，矛盾。$$\blacksquare$$

**注** 无限维时迹 $$\operatorname{tr}I=\infty$$ 失去意义，迹论证失效；引理 3.4 用预解式与阶乘增长补上了这个缺口。**同一个结论在有限维靠"维数"，在无限维靠"阶乘压过指数"。** 这也解释了为何"位置与动量"只能是无界算子——它们不是矩阵。

**题 3（谐振子代数与半有界权链）** 设 $$X,P$$ 自伴、$$[X,P]=i\hbar$$，取
$$a=\sqrt{\frac{m\omega}{2\hbar}}\Bigl(X+\frac{iP}{m\omega}\Bigr),\quad a^{\dagger}=\sqrt{\frac{m\omega}{2\hbar}}\Bigl(X-\frac{iP}{m\omega}\Bigr),\quad N=a^{\dagger}a .$$
**(a)** 证明 $$[a,a^{\dagger}]=I$$，并证明 $$\dfrac{P^{2}}{2m}+\dfrac12 m\omega^{2}X^{2}=\hbar\omega\bigl(N+\tfrac12\bigr)$$。
**(b)** 证明 $$[N,a]=-a$$、$$[N,a^{\dagger}]=a^{\dagger}$$，并由此推出 $$N$$ 的谱恰为 $$\mathbb N=\{0,1,2,\dots\}$$。

**考点**：定义 3.3（Heisenberg代数的表示）与第四节的"权链"直觉。**位置**：这是第 34 章的谐振子结果在本章代数语言下的重述——它为"对易关系决定了一个 Lie 代数的表示"提供最具体的证据，也预告第 56 章 $$\mathfrak{sl}(2)$$ 的权链。

**解 (a)** 记 $$c=\sqrt{\frac{m\omega}{2\hbar}}$$，则 $$a=c(\alpha)$$、$$a^{\dagger}=c(\beta)$$，其中 $$\alpha=X+\frac{i}{m\omega}P$$、$$\beta=X-\frac{i}{m\omega}P$$。先算 $$\alpha,\beta$$ 的对易子（用双线性与 $$[X,P]=i\hbar$$）：
$$[\alpha,\beta]=\Bigl[X+\frac{i}{m\omega}P,\ X-\frac{i}{m\omega}P\Bigr]=\Bigl[X,-\frac{i}{m\omega}P\Bigr]+\Bigl[\frac{i}{m\omega}P,X\Bigr]$$
$$=-\frac{i}{m\omega}[X,P]+\frac{i}{m\omega}[P,X]=-\frac{i}{m\omega}(i\hbar)+\frac{i}{m\omega}(-i\hbar)=\frac{\hbar}{m\omega}+\frac{\hbar}{m\omega}=\frac{2\hbar}{m\omega}.$$
故 $$[a,a^{\dagger}]=c^{2}[\alpha,\beta]=\frac{m\omega}{2\hbar}\cdot\frac{2\hbar}{m\omega}=1$$。

再算 $$N=a^{\dagger}a=c^{2}\beta\alpha=c^{2}\bigl([\beta,\alpha]+\alpha\beta\bigr)=c^{2}\Bigl(-\frac{2\hbar}{m\omega}+\alpha\beta\Bigr)$$。把 $$\alpha\beta=\bigl(X+\frac{i}{m\omega}P\bigr)\bigl(X-\frac{i}{m\omega}P\bigr)=X^{2}+\frac{1}{m^{2}\omega^{2}}P^{2}+\frac{i}{m\omega}(PX-XP)$$ 展开，其中 $$PX-XP=-[X,P]=-i\hbar$$，故
$$\alpha\beta=X^{2}+\frac{P^{2}}{m^{2}\omega^{2}}+\frac{i}{m\omega}(-i\hbar)=X^{2}+\frac{P^{2}}{m^{2}\omega^{2}}+\frac{\hbar}{m\omega}.$$
于是
$$N=\frac{m\omega}{2\hbar}\Bigl(X^{2}+\frac{P^{2}}{m^{2}\omega^{2}}+\frac{\hbar}{m\omega}-\frac{2\hbar}{m\omega}\Bigr)=\frac{m\omega}{2\hbar}X^{2}+\frac{P^{2}}{2m\hbar\omega}-\frac12 .$$
整理得 $$\hbar\omega\bigl(N+\tfrac12\bigr)=\tfrac12 m\omega^{2}X^{2}+\tfrac{P^{2}}{2m}$$。$$\blacksquare$$

**解 (b)** 用 $$[a,a^{\dagger}]=I$$ 与 Leibniz 法则：
$$[N,a]=[a^{\dagger}a,a]=a^{\dagger}[a,a]+[a^{\dagger},a]a=0+(-I)a=-a,$$
$$[N,a^{\dagger}]=[a^{\dagger}a,a^{\dagger}]=a^{\dagger}[a,a^{\dagger}]+[a^{\dagger},a^{\dagger}]a=a^{\dagger}+0=a^{\dagger}.$$

由 $$[N,a]=-a$$：若 $$N\psi=n\psi$$，则 $$N(a\psi)=aN\psi+[N,a]\psi=n(a\psi)-a\psi=(n-1)a\psi$$，即 $$a$$ 把 $$N$$ 的本征值降 $$1$$；同理 $$a^{\dagger}$$ 升 $$1$$。

先说明 $$N$$ 是正算子：对任意 $$\psi\in\operatorname{Dom}N$$，
$$\langle\psi,N\psi\rangle=\langle\psi,a^{\dagger}a\psi\rangle=\langle a\psi,a\psi\rangle=\lVert a\psi\rVert^{2}\ge0 .$$
所以 $$N$$ 的谱含于 $$[0,\infty)$$，本征值非负。又 $$N\psi=0\iff\lVert a\psi\rVert=0\iff a\psi=0$$。

**每个本征值都是自然数。** 设 $$N\psi=n\psi$$、$$\psi\neq0$$。由 $$\langle\psi,N\psi\rangle=n\lVert\psi\rVert^{2}\ge0$$ 得 $$n\ge0$$。由 $$[N,a]=-a$$，$$a^{k}\psi$$ 是 $$N$$ 的本征向量、本征值 $$n-k$$（只要它本身非零）。设 $$k_0$$ 是使 $$a^{k_0}\psi=0$$ 的最小非负整数。这样的 $$k_0$$ 必存在：若对一切 $$k$$ 都有 $$a^{k}\psi\neq0$$，则 $$n-k$$ 对一切 $$k$$ 都是非负本征值，取 $$k>n$$ 即得 $$n-k<0$$，与"本征值非负"矛盾。令 $$x=a^{k_0-1}\psi\neq0$$（$$k_0\ge1$$），则 $$ax=0$$、$$Nx=(n-k_0+1)x$$，于是
$$0=\lVert ax\rVert^{2}=\langle x,a^{\dagger}ax\rangle=\langle x,Nx\rangle=(n-k_0+1)\lVert x\rVert^{2},$$
故 $$n=k_0-1\in\mathbb N$$。**所以 $$N$$ 的每个本征值都落在 $$\mathbb N$$ 中。**

**基态存在，阶梯取遍 $$\mathbb N$$。** 在 Schrödinger 表示中（取 $$m=\omega=\hbar=1$$），方程 $$a\psi_0=0$$ 就是 $$\psi_0'=-x\psi_0$$，它有一个归一化解 $$\psi_0(x)=\pi^{-1/4}e^{-x^{2}/2}$$；故 $$0$$ 是 $$N$$ 的本征值。从 $$\psi_0$$ 出发：令 $$\psi_k=(a^{\dagger})^{k}\psi_0$$。由 $$[N,a^{\dagger}]=a^{\dagger}$$ 归纳得 $$N\psi_k=k\psi_k$$，且
$$\lVert\psi_k\rVert^{2}=\langle a^{\dagger}\psi_{k-1},a^{\dagger}\psi_{k-1}\rangle=\langle\psi_{k-1},aa^{\dagger}\psi_{k-1}\rangle=\langle\psi_{k-1},(N+I)\psi_{k-1}\rangle=k\lVert\psi_{k-1}\rVert^{2}>0,$$
（用了 $$aa^{\dagger}=a^{\dagger}a+I$$），故 $$\psi_k\neq0$$。于是每个 $$k\in\mathbb N$$ 都是本征值。结合上一段，$$N$$ 的本征值集恰为 $$\mathbb N$$（更精确地说，$$N$$ 的谱恰为 $$\mathbb N$$，每个点为单重本征值）。$$\blacksquare$$

**注（与第 56 章的接口）** 这条阶梯 $$0\to1\to2\to\cdots$$ 与 $$\mathfrak{sl}(2)$$ 的权链 $$m\to m-2\to\cdots\to-m$$ 是同一套机制（一个测权算子 + 一对升降算子），但前者半有界无限、后者有限。**正是"半有界无限"使得Heisenberg代数的不可约表示唯一（定理 3.11），而 $$\mathfrak{sl}(2)$$ 的不可约表示要由一个最高权参数来分类。** 卷四第 56 章会把这条对照讲透。

**题 4（von Neumann 投影的显式计算）** 证明第三节引理 3.11：
$$P_0=\frac{1}{2\pi}\iint_{\mathbb R^{2}}e^{-(s^{2}+t^{2})/4}\,e^{-i(s\mathsf X+t\mathsf P)}\,ds\,dt$$
是 $$L^2(\mathbb R)$$ 上到 $$\mathbb C\Omega$$ 的正交投影，$$\Omega(x)=\pi^{-1/4}e^{-x^{2}/2}$$。

**考点**：定理 3.11 证明的第二步——"任何 Weyl 系统都含一个真空方向"。**位置**：这是本章唯一一处把"唯一性证明的构造"算到底的地方；它同时是谐振子基态、Gauss 积分与 Weyl 算子三者的交汇点。

**解 第一步：把指数算子写成具体作用。** 由命题 3.6 的 Baker–Campbell–Hausdorff 计算（取 $$\hbar=1$$，最后再把 $$\hbar$$ 放回；本题只涉及归一化，$$\hbar$$ 不进结果）
$$e^{i(s\mathsf X+t\mathsf P)}=e^{ist/2}e^{is\mathsf X}e^{it\mathsf P},$$
故（把 $$s,t$$ 换成 $$-s,-t$$）
$$e^{-i(s\mathsf X+t\mathsf P)}=e^{ist/2}e^{-is\mathsf X}e^{-it\mathsf P}.$$
代入题 1(b) 的显式作用（$$\hbar=1$$）：$$e^{-is\mathsf X}$$ 是乘 $$e^{-isx}$$，$$e^{-it\mathsf P}$$ 是平移 $$\psi\mapsto\psi(\cdot-t)$$。故
$$\bigl(e^{-i(s\mathsf X+t\mathsf P)}\psi\bigr)(x)=e^{ist/2}e^{-isx}\,\psi(x-t).$$

**第二步：对 $$s$$ 积分。** 对 $$\psi\in\mathcal S(\mathbb R)$$，
$$(P_0\psi)(x)=\frac{1}{2\pi}\iint_{\mathbb R^{2}}e^{-(s^{2}+t^{2})/4}e^{ist/2}e^{-isx}\psi(x-t)\,ds\,dt .$$
先积 $$s$$。把 $$e^{ist/2}e^{-isx}=e^{-is(x-t/2)}$$，用高斯积分公式（配方直接得到）
$$\int_{\mathbb R}e^{-s^{2}/4}e^{-ibs}\,ds=\sqrt{4\pi}\,e^{-b^{2}}\qquad(b=x-\tfrac t2),$$
得
$$\int_{\mathbb R}e^{-s^{2}/4}e^{-is(x-t/2)}\,ds=2\sqrt\pi\,e^{-(x-t/2)^{2}} .$$
于是
$$(P_0\psi)(x)=\frac{2\sqrt\pi}{2\pi}\int_{\mathbb R}e^{-t^{2}/4}e^{-(x-t/2)^{2}}\psi(x-t)\,dt=\frac{1}{\sqrt\pi}\int_{\mathbb R}e^{-t^{2}/4}e^{-(x-t/2)^{2}}\psi(x-t)\,dt .$$

**第三步：换元与配方。** 令 $$y=x-t$$（$$t=x-y$$），则
$$(P_0\psi)(x)=\frac{1}{\sqrt\pi}\int_{\mathbb R}e^{-(x-y)^{2}/4}\,e^{-\bigl(x-\frac{x-y}{2}\bigr)^{2}}\psi(y)\,dy=\frac{1}{\sqrt\pi}\int_{\mathbb R}e^{-(x-y)^{2}/4}e^{-\bigl(\frac{x+y}{2}\bigr)^{2}}\psi(y)\,dy .$$
两个指数相加并配方：
$$-\frac{(x-y)^{2}}{4}-\frac{(x+y)^{2}}{4}=-\frac{(x-y)^{2}+(x+y)^{2}}{4}=-\frac{2x^{2}+2y^{2}}{4}=-\frac{x^{2}+y^{2}}{2}.$$
故被积函数对 $$x,y$$ 完全分离：
$$(P_0\psi)(x)=\frac{e^{-x^{2}/2}}{\sqrt\pi}\int_{\mathbb R}e^{-y^{2}/2}\psi(y)\,dy=e^{-x^{2}/2}\Bigl\langle \pi^{-1/4}e^{-y^{2}/2},\,\psi\Bigr\rangle .$$
即 $$P_0\psi=\langle\Omega,\psi\rangle\,\Omega$$，其中 $$\Omega(x)=\pi^{-1/4}e^{-x^{2}/2}$$，且 $$\lVert\Omega\rVert^{2}=\pi^{-1/2}\int e^{-y^{2}}dy=\pi^{-1/2}\sqrt\pi=1$$。

所以 $$P_0=\lvert\Omega\rangle\langle\Omega\rvert$$，它是到一维子空间 $$\mathbb C\Omega$$ 的正交投影，特别地 $$P_0\neq0$$、$$P_0^{2}=P_0=P_0^{*}$$。$$\blacksquare$$

**注** 这个计算揭示了构造的来历：权 $$e^{-(s^{2}+t^{2})/4}$$ 恰好匹配"真空态在 $$\mathsf X$$ 与 $$\mathsf P$$ 上各有一半方差 $$\tfrac12$$"这一事实——因为 $$e^{-(s^{2}+t^{2})/4}$$ 正是 $$\langle\Omega,e^{-i(s\mathsf X+t\mathsf P)}\Omega\rangle$$。在一般 Weyl 系统里做同样的积分，得到的 $$P_0$$ 就是"抽象真空"的投影；这正是定理 3.11 第二步的内容。


## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 证明对易子的两条 **Leibniz 法则**：$$[A,BC]=[A,B]C+B[A,C]$$ 与 $$[AB,C]=A[B,C]+[A,C]B$$（注意第二式的第二项是 $$[A,C]B$$，不是 $$[A,B]C$$）。然后用第一式证明
$$[A,B^{n}]=\sum_{k=0}^{n-1}B^{k}\,[A,B]\,B^{\,n-1-k},$$
并验证：当 $$[A,B]=I$$ 时 $$[A,B^{n}]=nB^{n-1}$$。

**基2.** 设 $$f\in C^{\infty}(\mathbb R)$$ 且各阶导数有界，$$M_f$$ 是 $$L^2(\mathbb R)$$ 上乘 $$f$$ 的有界算子，$$\mathsf P=-i\hbar\frac{d}{dx}$$。证明 $$[M_f,\mathsf P]=i\hbar\,M_{f'}$$。取 $$f(x)=x$$ 复核正则对易关系。

**基3.** 记 Weyl 算子 $$W(s,t)=e^{i\hbar st/2}U(s)V(t)$$。由定义 3.5 的 Weyl 关系证明
$$W(s,t)W(s',t')=e^{\frac{i\hbar}{2}(s't-st')}\,W(s+s',t+t'),\qquad W(s,t)^{*}=W(-s,-t),$$
并验证 $$\{W(s,t)\}$$ 的全体有限线性组合在乘法下封闭。

### 竞赛（本课目标难度）

**竞1.** 定义 Fourier 变换
$$(\mathcal F\psi)(k)=\frac{1}{\sqrt{2\pi\hbar}}\int_{\mathbb R}e^{-ikx/\hbar}\psi(x)\,dx .$$
证明 $$\mathcal F\mathsf P\mathcal F^{-1}=\mathsf X$$、$$\mathcal F\mathsf X\mathcal F^{-1}=-\mathsf P$$（右边都在动量表象中理解：$$\mathsf X$$ 是乘 $$k$$、$$\mathsf P=-i\hbar\frac{d}{dk}$$）。说明这给出了正则对易关系的一个酉等价，即"换视角"。

**竞2.** 不套用 Baker–Campbell–Hausdorff 公式，改用 **Heisenberg 运动方程** 重新推出 Weyl 关系：设 $$\psi$$ 是解析向量，令
$$F(s)=e^{-is\mathsf X}\,\mathsf P\,e^{is\mathsf X}.$$
**(a)** 证明 $$\dfrac{d}{ds}F(s)=\hbar I$$，从而 $$F(s)=\mathsf P+\hbar s\,I$$；
**(b)** 由此推出 $$e^{is\mathsf X}e^{it\mathsf P}=e^{-i\hbar st}e^{it\mathsf P}e^{is\mathsf X}$$。

**竞3.** 在 $$L^2(\mathbb R)$$ 中取高斯 $$\Omega(x)=\pi^{-1/4}e^{-x^{2}/2}$$（$$\hbar=1$$）。证明真空期望
$$\bigl\langle\Omega,\ e^{-i(s\mathsf X+t\mathsf P)}\,\Omega\bigr\rangle=e^{-(s^{2}+t^{2})/4},$$
并解释这个结果与引理 3.11 里高斯权 $$e^{-(s^{2}+t^{2})/4}$$ 的来历。

**竞4.** 证明位置算子 $$\mathsf X$$ 在 $$L^2(\mathbb R)$$ 中**没有本征向量**，且其谱 $$\sigma(\mathsf X)=\mathbb R$$ 全是连续谱；再用竞 1 的结论推出 $$\sigma(\mathsf P)=\mathbb R$$ 也全为连续谱。据此说明"位置是连续可观测量的典型"。

### 研究（通向下一章）

**研1.（不可约 Weyl 系统的唯一性）** 设 $$(U,V)$$ 与 $$(U',V')$$ 分别是Hilbert 空间 $$\mathcal H,\mathcal H'$$ 上的两个不可约 Weyl 系统，$$W,W'$$ 是对应的 Weyl 算子。
**(i)** 证明任一非零 $$\xi\in\mathcal H$$ 都是**循环向量**：$$\mathcal H=\overline{\operatorname{span}}\{W(s,t)\xi:\ s,t\in\mathbb R\}$$。
**(ii)** 设存在单位向量 $$\xi,\xi'$$ 使矩阵元恒等
$$\langle\xi,W(s,t)\xi\rangle=\langle\xi',W'(s,t)\xi'\rangle\qquad\text{对一切 }s,t,$$
证明 $$(U,V)$$ 与 $$(U',V')$$ 酉等价。
**(iii)** 结合竞 3 与引理 3.11，说明"不可约 Weyl 系统唯一"归结为"抽象真空方向的存在性"，这正是定理 3.11 第二步所构造的。

**研2.（从群到半群：时间演化的边界）** 设 $$H$$ 是 $$\mathcal H$$ 上自伴且 $$H\ge0$$ 的算子。
**(i)** 证明 $$U(t)=e^{-iHt/\hbar}$$（$$t\in\mathbb R$$）是强连续单参数**酉群**，且 $$\psi(t)=U(t)\psi(0)$$ 是 Schrödinger 方程的解。
**(ii)** 现在令 $$T(t)=e^{-tH/\hbar}$$。证明 $$T(0)=I$$、$$T(t+s)=T(t)T(s)$$（$$t,s\ge0$$）、$$\lVert T(t)\rVert\le1$$，但每个 $$T(t)$$（$$t>0$$）**不是**酉算子。指出它的生成元是什么。
**(iii)** 从 (i) 到 (ii)，"群"退化成了"半群"。说出你观察到的原因。

### 解答 (Solutions)

**解 基1.** **第一条**：直接展开
$$[A,BC]=ABC-BCA=(ABC-BAC)+(BAC-BCA)=[A,B]C+B[A,C].$$
**第二条**：同样展开
$$[AB,C]=ABC-CAB=(ABC-ACB)+(ACB-CAB)=A[B,C]+[A,C]B .$$
注意第二步合并的是 $$ACB-CAB=(AC-CA)B=[A,C]B$$，所以第二项是 $$[A,C]B$$ 而非 $$[A,B]C$$；用 $$A=B=C$$ 的矩阵试一下就会发现问题。

**求和公式**：对 $$n$$ 归纳。$$n=1$$ 时右边只有 $$k=0$$ 一项 $$[A,B]$$，成立。设对 $$n$$ 成立，则用第一条：
$$[A,B^{n+1}]=[A,B^{n}]B+B^{n}[A,B]=\Bigl(\sum_{k=0}^{n-1}B^{k}[A,B]B^{n-1-k}\Bigr)B+B^{n}[A,B]=\sum_{k=0}^{n}B^{k}[A,B]B^{n-k},$$
正是 $$n+1$$ 的形式。当 $$[A,B]=I$$ 时，$$[A,B]$$ 与任何 $$B$$ 交换，每项都化为 $$B^{n-1}$$，共 $$n$$ 项，故 $$[A,B^{n}]=nB^{n-1}$$。$$\blacksquare$$

**解 基2.** 对 $$\psi\in\mathcal S(\mathbb R)$$（再由稠密性与有界性延拓）：
$$[M_f,\mathsf P]\psi=f\cdot(-i\hbar\psi')-(-i\hbar)(f\psi)'=-i\hbar f\psi'+i\hbar(f'\psi+f\psi')=i\hbar f'\psi .$$
所以 $$[M_f,\mathsf P]=i\hbar M_{f'}$$。取 $$f(x)=x$$，则 $$f'=1$$，得 $$[\mathsf X,\mathsf P]=i\hbar I$$，与题 1 一致。$$\blacksquare$$

**解 基3.** 由 $$W(s,t)=e^{i\hbar st/2}U(s)V(t)$$：
$$W(s,t)W(s',t')=e^{\frac{i\hbar}{2}(st+s't')}\,U(s)V(t)U(s')V(t').$$
用 $$V(t)U(s')=e^{i\hbar s't}U(s')V(t)$$（把定义 3.5 的第三式改写）：
$$U(s)V(t)U(s')V(t')=e^{i\hbar s't}\,U(s+s')V(t+t').$$
故
$$W(s,t)W(s',t')=e^{\frac{i\hbar}{2}(st+s't'+2s't)}\,U(s+s')V(t+t')=e^{\frac{i\hbar}{2}(s't-st')}\,W(s+s',t+t'),$$
最后一步把指数拆成 $$\frac{i\hbar}{2}\bigl((s+s')(t+t')+(s't-st')\bigr)$$ 再对比 $$W(s+s',t+t')=e^{\frac{i\hbar}{2}(s+s')(t+t')}U(s+s')V(t+t')$$ 即可。

伴随：$$W(s,t)^{*}=e^{-i\hbar st/2}V(t)^{*}U(s)^{*}=e^{-i\hbar st/2}V(-t)U(-s)$$，再用 $$V(-t)U(-s)=e^{i\hbar st}U(-s)V(-t)$$，得
$$W(s,t)^{*}=e^{i\hbar st/2}U(-s)V(-t)=W(-s,-t).$$
乘法律表明有限线性组合的乘积仍是这样组合的线性组合（乘一个相位再平移指标），故封闭。$$\blacksquare$$

**解 竞1.** 先算动量的像。对 $$\psi\in\mathcal S(\mathbb R)$$，
$$\widehat{\mathsf P\psi}(k)=\frac{1}{\sqrt{2\pi\hbar}}\int_{\mathbb R}e^{-ikx/\hbar}\bigl(-i\hbar\psi'(x)\bigr)dx .$$
分部积分（$$u=e^{-ikx/\hbar},\ dv=-i\hbar\psi'dx$$，边界项因 $$\psi$$ 速降为零）：
$$\int_{\mathbb R}u\,dv=-\int_{\mathbb R}v\,du=-\int_{\mathbb R}(-i\hbar\psi)\Bigl(-\frac{ik}{\hbar}e^{-ikx/\hbar}\Bigr)dx=-\int_{\mathbb R}\bigl(-ke^{-ikx/\hbar}\psi\bigr)dx=k\int_{\mathbb R}e^{-ikx/\hbar}\psi\,dx .$$
故 $$\widehat{\mathsf P\psi}(k)=k\,\hat\psi(k)$$，即
$$\mathcal F\mathsf P\mathcal F^{-1}=M_k=\mathsf X .$$

再算位置的像。注意 $$\dfrac{d}{dk}e^{-ikx/\hbar}=-\dfrac{ix}{\hbar}e^{-ikx/\hbar}$$，故 $$x\,e^{-ikx/\hbar}=i\hbar\dfrac{d}{dk}e^{-ikx/\hbar}$$，可以把它提到积分号外：
$$\widehat{\mathsf X\psi}(k)=i\hbar\frac{d}{dk}\Bigl(\frac{1}{\sqrt{2\pi\hbar}}\int_{\mathbb R}e^{-ikx/\hbar}\psi(x)dx\Bigr)=i\hbar\frac{d}{dk}\hat\psi(k),$$
即 $$\mathcal F\mathsf X\mathcal F^{-1}=i\hbar\frac{d}{dk}=-\mathsf P$$（在动量表象中 $$\mathsf P=-i\hbar\frac{d}{dk}$$）。

**一致性**：在新表象下重算对易子，
$$[\mathcal F\mathsf X\mathcal F^{-1},\mathcal F\mathsf P\mathcal F^{-1}]=[-\mathsf P,\mathsf X]=-[ \mathsf P,\mathsf X]=i\hbar,$$
与原来一致。所以 Fourier 变换是一个把 $$(\mathsf X,\mathsf P)$$ 换成 $$(-\mathsf P,\mathsf X)$$ 的**酉变换**——位置画到了动量、动量画到了负位置，这正是"换视角"：物理没变，只是坐标系转了 $$90^{\circ}$$（与第四节"C 中乘 $$i$$ 是 $$\pi/2$$ 旋转"的几何图像吻合）。$$\blacksquare$$

**解 竞2.** **(a)** 由 Leibniz 法则与 $$[\mathsf P,\mathsf X]=-i\hbar I$$，
$$F'(s)=\frac{d}{ds}\bigl(e^{-is\mathsf X}\mathsf P e^{is\mathsf X}\bigr)=e^{-is\mathsf X}(-i\mathsf X\mathsf P+i\mathsf P\mathsf X)e^{is\mathsf X}=e^{-is\mathsf X}\,i[\mathsf P,\mathsf X]\,e^{is\mathsf X}=e^{-is\mathsf X}\hbar\,e^{is\mathsf X}=\hbar I .$$
（$$\mathsf X$$ 与自身当然交换，所以只有中间那一项留下。）又 $$F(0)=\mathsf P$$，对 $$s$$ 积分得
$$F(s)=\mathsf P+\hbar s\,I .$$
**(b)** 由 (a)：$$\mathsf P e^{is\mathsf X}=e^{is\mathsf X}(\mathsf P+\hbar s I)$$。对 $$n$$ 归纳得 $$\mathsf P^{n}e^{is\mathsf X}=e^{is\mathsf X}(\mathsf P+\hbar s I)^{n}$$。取指数：
$$e^{it\mathsf P}e^{is\mathsf X}=\sum_{n\ge0}\frac{(it)^{n}}{n!}\mathsf P^{n}e^{is\mathsf X}=e^{is\mathsf X}\sum_{n\ge0}\frac{(it)^{n}}{n!}(\mathsf P+\hbar s I)^{n}=e^{is\mathsf X}e^{it(\mathsf P+\hbar s I)}=e^{i\hbar st}\,e^{is\mathsf X}e^{it\mathsf P},$$
最后一步用了 $$e^{it(\mathsf P+\hbar sI)}=e^{i\hbar st}e^{it\mathsf P}$$（标量 $$\hbar sI$$ 与 $$\mathsf P$$ 交换）。两边左乘 $$e^{-is\mathsf X}$$ 右乘 $$e^{-it\mathsf P}$$ 的逆（即 $$e^{is\mathsf X}e^{it\mathsf P}=e^{-i\hbar st}e^{it\mathsf P}e^{is\mathsf X}$$）。

**关键 leap**：不去展开两个指数算子，而是**只看它们夹在中间的那个算子如何随参数流动**——$$F(s)$$ 满足一个平凡的常微分方程。这正是 Heisenberg 图景（算符随时间演化）的雏形。$$\blacksquare$$

**解 竞3.** 由题 1(b)（$$\hbar=1$$）：$$\bigl(e^{-i(s\mathsf X+t\mathsf P)}\Omega\bigr)(x)=e^{ist/2}e^{-isx}\Omega(x-t)$$。故
$$\bigl\langle\Omega,e^{-i(s\mathsf X+t\mathsf P)}\Omega\bigr\rangle=e^{ist/2}\pi^{-1/2}\int_{\mathbb R}e^{-x^{2}/2}\,e^{-isx}\,e^{-(x-t)^{2}/2}\,dx .$$
指数合并（$$\Omega$$ 的实指数部分）：
$$-\frac{x^{2}+(x-t)^{2}}{2}-isx=-x^{2}+tx-\frac{t^{2}}{2}-isx .$$
于是积分化为标准高斯 $$\int e^{-x^{2}+ax}dx=\sqrt\pi\,e^{a^{2}/4}$$，取 $$a=t-is$$：
$$\bigl\langle\Omega,e^{-i(s\mathsf X+t\mathsf P)}\Omega\bigr\rangle=e^{ist/2}\pi^{-1/2}e^{-t^{2}/2}\sqrt\pi\,e^{(t-is)^{2}/4}.$$
把 $$(t-is)^{2}=t^{2}-2ist-s^{2}$$ 代入并合并指数：
$$\frac{ist}{2}-\frac{t^{2}}{2}+\frac{t^{2}}{4}-\frac{ist}{2}-\frac{s^{2}}{4}=-\frac{t^{2}}{4}-\frac{s^{2}}{4}.$$
所以结果就是 $$e^{-(s^{2}+t^{2})/4}$$。

**解释**：这正是 $$\Omega$$ 在 $$\mathsf X$$ 与 $$\mathsf P$$ 上"各占一半方差"的体现——由测不准原理取等号知 $$\Delta\mathsf X=\Delta\mathsf P$$，而 $$\Omega$$ 恰是取等号的态（高斯），故 $$\Delta\mathsf X^{2}=\Delta\mathsf P^{2}=\frac12$$，特征函数为 $$e^{-(s^{2}\Delta\mathsf X^{2}+t^{2}\Delta\mathsf P^{2})/2}=e^{-(s^{2}+t^{2})/4}$$。引理 3.11 的积分正是这个特征函数的 Fourier 反演，所以权必须取 $$e^{-(s^{2}+t^{2})/4}$$。$$\blacksquare$$

**解 竞4.** **$$\mathsf X$$ 无本征向量**：设 $$\mathsf X\psi=x_0\psi$$，即 $$(x-x_0)\psi(x)=0$$ 几乎处处。在 $$x\neq x_0$$ 处得 $$\psi(x)=0$$；单点集的测度为零，故 $$\psi=0$$ 于 $$L^2$$。所以 $$\mathsf X$$ 没有（非零）本征向量，本征值集为空。

**谱为 $$\mathbb R$$**：对 $$\lambda\in\mathbb R$$，算子 $$\mathsf X-\lambda I$$ 是乘 $$x-\lambda$$，单射（同上）且值域稠密（所有在 $$\lambda$$ 的邻域外为零的 $$L^2$$ 函数都在值域内，它们稠密）。但它不满射：若 $$\mathsf X-\lambda I$$ 可逆，其逆应为乘 $$1/(x-\lambda)$$，而 $$1/(x-\lambda)$$ 在 $$\lambda$$ 附近无界，不是本质有界函数，故逆不是有界算子。因此 $$\lambda\in\sigma(\mathsf X)$$，且属于连续谱（单射、值域稠密、不满）。$$\lambda$$ 任意，所以 $$\sigma(\mathsf X)=\mathbb R$$ 全为连续谱。

**$$\mathsf P$$ 的情形**：由竞 1，$$\mathcal F$$ 是酉算子且 $$\mathcal F\mathsf P\mathcal F^{-1}=\mathsf X$$；谱在酉等价下不变，故 $$\sigma(\mathsf P)=\sigma(\mathsf X)=\mathbb R$$，同样全为连续谱。

**结论**：位置（以及动量）是"连续可观测量"的原型——它的谱是连续统，没有真正的本征态；物理上一个严格定域于一点的状态不是 $$L^2$$ 函数。这与测不准原理（推论 3.12）相容：$$\lvert\psi\rvert^{2}$$ 只能是一个有限的"波包"，$$\Delta\mathsf X$$ 永远为正。$$\blacksquare$$

**解 研1.** **(i)** 令 $$\mathcal K=\overline{\operatorname{span}}\{W(s,t)\xi\}$$。要证 $$\mathcal K=\mathcal H$$。因 $$(U,V)$$ 酉等价于 $$\{W\}$$ 的生成（只差相位），$$\mathcal K$$ 在全体 $$U(s),V(t)$$ 下不变（$$U(s)W(s',t')=e^{i\theta}W(s+s',t')$$ 等），故 $$\mathcal K^{\perp}$$ 也不变。若 $$\mathcal K^{\perp}\neq\{0\}$$，则正交投影 $$P_{\mathcal K^{\perp}}$$ 与全体 $$U,V$$ 交换且不是标量，与不可约性（定理 3.10 的判据）矛盾。故 $$\mathcal K=\mathcal H$$。

**(ii)** 在线性映射 $$T:\ W(s,t)\xi\mapsto W'(s,t)\xi'$$ 上验证。先看它是否**保持内积**：对任意 $$s,t,s_1,t_1$$，
$$\langle W(s,t)\xi,\,W(s_1,t_1)\xi\rangle=\langle\xi,\,W(s,t)^{*}W(s_1,t_1)\xi\rangle .$$
用解 基3 的乘法律（$$\xi'$$ 一侧同理），$$W(s,t)^{*}W(s_1,t_1)=e^{i\phi}W(s_1-s,\,t_1-t)$$ 对某个只依赖 $$s,t,s_1,t_1$$ 的相位 $$\phi$$，于是
$$\langle W(s,t)\xi,W(s_1,t_1)\xi\rangle=e^{i\phi}\langle\xi,W(s_1-s,t_1-t)\xi\rangle=e^{i\phi}\langle\xi',W'(s_1-s,t_1-t)\xi'\rangle=\langle W'(s,t)\xi',W'(s_1,t_1)\xi'\rangle,$$
上面第二个等号用了题设的矩阵元恒等。于是 $$T$$ 在稠密的张成集上保持内积；对任意有限线性组合 $$\sum c_k W(s_k,t_k)\xi$$，用极化恒等式把内积写成范数组合可知 $$T$$ 的范数保持成立，所以 $$T$$ 唯一延拓为等距算子 $$\mathcal H\to\mathcal H'$$，由 (i) 两边都是循环的，$$T$$ 的值域稠密且是等距，故 $$T$$ 是**酉**算子。最后，对 $$W(a,b)$$：
$$T\,W(a,b)\,W(s,t)\xi=T\bigl(e^{i\psi}W(a+s,b+t)\xi\bigr)=e^{i\psi}W'(a+s,b+t)\xi'=W'(a,b)W'(s,t)\xi'=W'(a,b)\,T\,W(s,t)\xi,$$
两边在稠密集上相等，故 $$T W(a,b)=W'(a,b)T$$。这就是酉缠绕，即两个 Weyl 系统酉等价。

**(iii)** 竞 3 说：Schrödinger 表示的真空 $$\Omega$$ 满足 $$\langle\Omega,W(s,t)\Omega\rangle=e^{-(s^{2}+t^{2})/4}$$。于是由 (ii)：**只要另一个不可约 Weyl 系统里也能找到一个单位向量 $$\xi'$$ 使矩阵元同为 $$e^{-(s^{2}+t^{2})/4}$$，唯一性立刻成立**。定理 3.11 第二步构造的 $$P_0$$ 正是为了在任意 Weyl 系统里造出这样一个"抽象真空"——它的存在性（$$P_0\neq0$$）是全部困难；引理 3.11 是它在 Schrödinger 表示中的显式验证。

**接下一章前的伏笔**：上面 (ii) 的论证只用到"矩阵元相同"，这对**不可约**系统足够。若系统可约，"矩阵元相同"就只是必要条件——一般的 Weyl 系统要写成不可约分量的直和，分量个数（多重数）成了唯一的等价不变量。描述这个多重数需要 **von Neumann 代数 (von Neumann algebra)** 与**因子 (factor)** 的类型理论，那是第 54 章 Lie 代数表示论与第 60 章射影表示的一般框架；届时本章的 $$H_3(\mathbb R)$$ 会成为"中心扩张的不可约表示由中心特征完全决定"这一现象的第一个范例。$$\blacksquare$$

**解 研2.** **(i)** $$H$$ 自伴，故由谱定理（第 38 章）$$f(H)=\int f(\lambda)\,dE(\lambda)$$ 对 Borel 函数 $$f$$ 有定义，且 $$\lVert f(H)\rVert\le\lVert f\rVert_{\infty}$$。取 $$f_t(\lambda)=e^{-i\lambda t/\hbar}$$，则 $$\lvert f_t\rvert\equiv1$$，故 $$U(t)=e^{-iHt/\hbar}$$ 是酉算子，且
$$U(t)U(s)=e^{-iHt/\hbar}e^{-iHs/\hbar}=e^{-iH(t+s)/\hbar}=U(t+s),\qquad U(0)=I,$$
群律成立（函数演算是 \*-同态，相乘即函数相乘）。强连续性由控制收敛定理（对 $$d\mu_\psi=\langle E(\cdot)\psi,\psi\rangle$$）给出。对 $$\psi\in\operatorname{Dom}H$$，
$$\frac{U(t)\psi-\psi}{t}=\frac{e^{-iHt/\hbar}-1}{t}\psi\ \longrightarrow\ -\frac{i}{\hbar}H\psi,$$
故 $$U$$ 的生成元是 $$-H/\hbar$$，$$\psi(t)=U(t)\psi(0)$$ 满足 $$i\hbar\partial_t\psi=H\psi$$。这与定理 3.7 完全一致：自伴算子 $$H$$ 与单参数酉群 $$U$$ 一一对应。

**(ii)** 取 $$g_t(\lambda)=e^{-\lambda t/\hbar}$$（$$t\ge0$$）。因 $$H\ge0$$，$$\lVert g_t\rVert_{\infty}=\sup_{\lambda\ge0}e^{-\lambda t/\hbar}=1$$（$$t>0$$ 时在 $$\lambda=0$$ 取到），故 $$T(t)=e^{-tH/\hbar}$$ 有界且 $$\lVert T(t)\rVert\le1$$；$$T(0)=I$$、$$T(t+s)=T(t)T(s)$$ 由函数演算得到。它不是酉算子：$$\lVert T(t)\psi\rVert<\lVert\psi\rVert$$ 当 $$\psi$$ 有正的谱分量（例如 $$H\psi>0$$），因为 $$g_t$$ 的模在 $$\lambda>0$$ 处严格小于 $$1$$。它的**生成元是 $$-H/\hbar$$**（在 $$\operatorname{Dom}H$$ 上，$$\frac{T(t)\psi-\psi}{t}\to-\frac1\hbar H\psi$$）。

**(iii)** 差别只在 $$f_t(\lambda)=e^{-i\lambda t/\hbar}$$ 与 $$g_t(\lambda)=e^{-\lambda t/\hbar}$$ 的**模**：前者的模恒为 $$1$$，所以每个 $$U(t)$$ 可逆（逆是 $$U(-t)$$），$$t$$ 可以取负值，构成群；后者在 $$\lambda>0$$ 处模小于 $$1$$，$$T(t)$$ 不可逆，于是只能在 $$t\ge0$$ 上定义，群律退化成半群律。**"群"与"半群"的界线，就是生成元的谱是否被限制在一条射线的一侧**——这里 $$H\ge0$$ 把谱压在 $$[0,\infty)$$，虚数方向的指数 $$e^{-i\lambda t}$$ 可以双向流动，实方向的指数 $$e^{-\lambda t}$$ 只能单向衰减。

**接下一章**：$$T(t)=e^{-tH/\hbar}$$ 是热传导/扩散型演化，而物理上真正需要的 $$\langle x'\rvert U(t)\lvert x\rangle$$（Schrödinger 演化的积分核）可以形式地写成对路径的积分 $$\int e^{\frac{i}{\hbar}S[\text{路径}]}\mathcal D x$$。把这条路径积分**严格化**，标准路线正是先用 Trotter 乘积公式把 $$U(t)$$ 拆成许多小步，再借算子半群的理论取极限——那正是第 46 章《算子半群与 Feynman 路径积分》的起点。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**1. 一条关系，一个 Lie 代数。** $$[X,P]=i\hbar$$ 的全部代数内容，是说"三维Heisenberg代数 $$\mathfrak h$$ 的一个表示把中心元 $$Z$$ 送到 $$i\hbar I$$"。第 32 章的"对易子"在第 54 章会被正式命名为 Lie 括号；本章提前用上了这个视角，于是"量子化"这句话有了精确含义：**把 Poisson 括号 $$\{x,p\}=1$$ 换成 $$[\cdot,\cdot]/(i\hbar)$$，就是把相空间平移群的交换 Lie 代数换成了Heisenberg代数**。

**2. 无界性是必然的，不是技术缺陷。** 引理 3.4（Wielandt–Wintner）证明含单位元的巴拿赫代数里 $$AB-BA=I$$ 无解，所以位置与动量不可能同时有界。这不是"数学家偷懒不去处理无界算子"，而是关系式本身拒绝有界实现。补救办法是**指数化**：Weyl 形式只用到酉算子，把"无穷小"的困难换成了"有限"的群律。

**3. 唯一性 = 只被一个参数（$$\hbar$$）标记。** Stone–von Neumann 定理说：不可约的 Weyl 系统在酉等价意义下只有 Schrödinger 表示一种。也就是说，$$\hbar$$ 是唯一自由参数；给定 $$\hbar$$，量子运动学被完全确定。**对比**：$$\mathfrak{sl}(2)$$ 的不可约表示由最高权分类（一个离散参数族），Heisenberg代数的不可约表示却只有一个——差别来自谐振子权链是半有界无限的（第四节、经典题 3）。这正是"Lie 代数表示论"里两种典型结局的第一次正面相遇。

**4. 几何 ↔ 物理 ↔ 代数的又一次三合一。** 同一个对象有四种面孔：相空间上的 $$90^{\circ}$$ 旋转（辛结构）、相空间平移的射影表示（上循环）、Heisenberg群的中心扩张、以及一个 Lie 代数的唯一不可约表示。第 60 章的"射影表示"会把这四句话变成一般定理。

**5. 图景是记账方式。** 推论 3.13：Schrödinger 图景与 Heisenberg 图景由酉变换 $$A_H(t)=U(t)^{-1}AU(t)$$ 联系，二者物理等价。定理 3.11 给了这句话一个更强的版本：**不只是两个图景之间，而是满足对易关系的一切实现之间，都只差一个酉变换**——"换视角"穷尽了一切可能性。

**下一章（第 46 章）的悬念。** 本章把时间演化写成 $$U(t)=e^{-iHt/\hbar}$$，一个单参数酉群；由 Stone 定理，它的生成元 $$H$$ 必须自伴。可物理上有大量重要过程**不是群**：热方程 $$\partial_t u=-Hu$$、扩散、以及 Feynman 路径积分里那种"半群取极限"的构造。把 $$e^{-iHt/\hbar}$$ 换成 $$e^{-tH/\hbar}$$ 时，酉群退化成半群（研 2 已经看到机制）；问题于是变成：**半群的生成元要满足什么条件（Hille–Yosida / Lumer–Phillips），Trotter 乘积公式如何把路径积分严格化？** 这是第 46 章《算子半群与 Feynman 路径积分》要回答的。

**再往后看（卷四）。** 本章的对易关系在卷四会以完全一般的面貌回来：第 54 章把"对易子"抽象为 Lie 代数并研究 $$\exp$$ 映射（本章的 $$e^{isX}$$ 只是它的一例），第 60 章用中心扩张与上同调处理"射影表示"，届时本章的 $$H_3(\mathbb R)$$ 会成为整个理论的原型。

**延伸阅读**（对应原专栏与参考书）：
- MP57《从 Schrödinger 图景看量子力学中的酉变换》（时间演化算子、算子指数、单参数半群）；
- MP58《正则对易关系、Stone–von Neumann 定理、后继学习的展望》（本章主线）；
- MP43（正则对易关系与 Poisson 括号的首次出现）、MP46（谐振子与升降算子）；
- Hall, *Quantum Theory for Mathematicians* (GTM 267)，第 28 章（Heisenberg 群与 Stone–von Neumann 的完整证明）；
- Reed & Simon, *Methods of Modern Mathematical Physics I*，§VIII.5（Weyl 关系与唯一性）；
- Weyl, *The Theory of Groups and Quantum Mechanics*（Weyl 形式的原始出处）。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch43_正则对易关系与Stone_vonNeumann_上.md">← 第43章 正则对易关系与 Stone–von Neumann·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch45_算子半群与Feynman路径积分_上.md">第45章 算子半群与 Feynman 路径积分·上 →</a></div>
</div>
