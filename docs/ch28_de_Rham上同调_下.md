---
layout: default
---

# 第28章: de Rham 上同调·下：完整推导 (de Rham Cohomology · Part II: Full Derivation)

> 配套预备: 见 第27章 de Rham 上同调·上（同一主题的具体铺垫，建议先读）

> 对应原专栏: MP29
> 专家依据: `_experts/algebra/homological-algebra.md`（主）+ `_experts/algebra/algebraic-geometry-topology-k.md`
> 知识库依据: `opc2/knowledge/math/微分几何/differential-geometry/`（ch07 de Rham 上同调、ch09 紧支上同调与 Poincaré 对偶）、`opc2/knowledge/math/代数拓扑/paulin-topology/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

读完第 27 章的具体例子后（那一章已经带你手算过闭、恰当、局部常值函数计数，以及"绕原点积分给出一个数"这三件事），这里把同样的构造写成一般定义，并给出完整证明。本章只回答一个问题：**一个闭形式，什么时候恰好是某个形式的微分？**

**从哪来。** 卷二走到这里，已经铺了三条平行的线，它们在这一章第一次拧成一根绳：

- 第 09–10 章：链群 $$C_k$$ 上的边界算子 $$\partial$$ 满足 $$\partial^2=0$$，"闭链除以边界"给出同调群 $$H_k=Z_k/B_k$$，它数的是流形上的洞；
- 第 14 章：微分形式上的外微分 $$d$$ 满足 $$d^2=0$$（定理 3.18），"闭形式除以恰当形式"给出一个形状完全相同的商——只是箭头方向相反：$$\partial$$ 降维，$$d$$ 升维；
- 第 26 章：Stokes 定理 $$\int_D d\omega=\int_{\partial D}\omega$$ 把这两台机器**配对**起来。

**到哪去。** 本章定义 $$H^k_{dR}(M)=\ker d_k/\operatorname{im} d_{k-1}$$，证明它只依赖流形的拓扑（同伦不变性），证明它是**反变**函子，陈述 de Rham 定理 $$H^k_{dR}\cong H^k_{\text{sing}}$$ 的对偶形式，并用它把"洞的个数"从一个积分里读出来。卷二在此收官。第 30 章起，我们换一副眼镜——不再用**配对**看这些空间，而用**内积**，于是进入卷三（泛函分析）。

## 二、入口：一道具体的问题 (Entry Problem)

**题目**（来源：教材经典例题，Stokes 定理与上同调的标准入门题；下面三问为自编）。

在 $$M=\mathbb{R}^2\setminus\{0\}$$（挖掉原点的平面）上定义 1-形式

$$\omega=\frac{-y\,dx+x\,dy}{x^2+y^2}.$$

**(a)** 直接计算：$$d\omega$$ 等于多少？
**(b)** 是否存在光滑函数 $$f:M\to\mathbb{R}$$，使得 $$\omega=df$$？
**(c)** 把单位圆周 $$\gamma(t)=(\cos t,\sin t)$$，$$t\in[0,2\pi]$$ 代入，算出 $$\int_\gamma\omega$$ 的值。这个值与 (b) 的答案有什么关系？

**为什么先问这三问。** 这三问的顺序是刻意排的：

- (a) 是纯粹的局部计算，一个下午就能算完，但它**只**告诉你"闭不闭"；
- (b) 是真正的全局问题。请注意它**不能**靠"我算了半天没凑出 $$f$$"来回答——算不出来不等于不存在。这是本题的第一个陷阱：局部的证据不足以判定全局的存在性；
- (c) 神在它能给 (b) 一个判决。它给出一个"局部看不见、只有绕一圈才出现"的数。第 26 章的 Stokes 定理会说明，这个数一旦非零，$$f$$ 就绝无可能存在。

先把 (a)(b)(c) 都当成三分钟的练习题做掉，再往下读。本章全部的定义，都是从这三问的答案里长出来的。
## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 复形：把 $$d^2=0$$ 装进一台机器

回顾第 14 章定理 3.18：对任意光滑流形 $$M$$ 与每个 $$k$$，外微分

$$d_k:\Omega^k(M)\longrightarrow\Omega^{k+1}(M)$$

满足 $$d_{k+1}\circ d_k=0$$。写成一行就是

$$\Omega^0(M)\xrightarrow{\ d_0\ }\Omega^1(M)\xrightarrow{\ d_1\ }\Omega^2(M)\xrightarrow{\ d_2\ }\cdots\xrightarrow{\ d_{n-1}\ }\Omega^n(M)\xrightarrow{\ d_n\ }0,$$

且相邻两个复合为零。具有这种形状的数据（一串向量空间配上一串线性映射，复合为零）叫**上链复形 (cochain complex)**。上标记次数，下标只是给这个映射起个名字。

这里值得停下来看一件事：$$\partial^2=0$$（第 18 章）与 $$d^2=0$$ 是**两个不同对象上的同一条法则**。一个降维，一个升维，别的没有区别。而第 09–10 章已经演示过：只要手上有一串"复合为零"的映射，就能造出一台商机器 $$H=Z/B$$。所以本章要做的第一件事，就是把那台机器原封不动地搬到上链复形上。

### 3.2 闭形式与恰当形式

**为什么先定义这两个词。** 3.1 节把"复合为零"这条法则搬了过来，但还没有名字给复形里的元素分类。入口题已经把两类对象摆在了眼前：$$d\omega=0$$ 这一条件（(a) 算出来的那种"平"）值得起一个名字；"$$\omega$$ 是不是某个函数的微分"（(b) 问的那件事）也值得起一个名字。下面这两个定义就是把入口题里已经用过的两句话，正式钉成术语。

**定义 3.1（闭形式 / closed form）**。$$\omega\in\Omega^k(M)$$ 称为**闭的 (closed)**，若 $$d_k\omega=0$$。全体闭 $$k$$-形式记

$$Z^k(M)=\ker d_k,$$

称为 **$$k$$-上闭链群 (cocycle group)**。

**定义 3.2（恰当形式 / exact form）**。$$\omega\in\Omega^k(M)$$ 称为**恰当的 (exact)**，若存在 $$\eta\in\Omega^{k-1}(M)$$ 使 $$\omega=d_{k-1}\eta$$。全体恰当 $$k$$-形式记

$$B^k(M)=\operatorname{im} d_{k-1},$$

称为 **$$k$$-上边缘群 (coboundary group)**。

**记号说明。** 第 20 章的边界/闭链用的是**下标** $$B_k,Z_k$$，因为那里数的是"链"；本章用**上标**，因为数的是"上链"（形式）。$$Z$$ 来自 cycle（闭链、闭合的东西），$$B$$ 来自 boundary（边界、从别处流过来的东西）。叫 "coboundary" 只是说它在"上链"这一侧，含义完全平行。

**命题 3.3（恰当必闭）**。$$B^k(M)\subseteq Z^k(M)$$。

**证明。** 设 $$\omega\in B^k$$，即 $$\omega=d\eta$$，$$\eta\in\Omega^{k-1}(M)$$。则依第 14 章定理 3.18，

$$d_k\omega=d_k(d_{k-1}\eta)=(d_{k+1}\circ d_k)(\eta)\big\vert_{k\mapsto k-1}=(d_k\circ d_{k-1})\eta=0,$$

故 $$\omega\in Z^k$$。$$\blacksquare$$

这个包含式就是全章的动机。$$B^k\subseteq Z^k$$ 意味着"闭"是一个比"恰当"更弱的条件。如果两者相等，下面的商就是零；**两者差多少，才是信息**。

### 3.3 de Rham 上同调群

**定义 3.4（de Rham 上同调群 / de Rham cohomology group；也译"德拉姆上同调"）**。

$$H^k_{dR}(M)=\frac{Z^k(M)}{B^k(M)}=\frac{\ker\big(d_k:\Omega^k\to\Omega^{k+1}\big)}{\operatorname{im}\big(d_{k-1}:\Omega^{k-1}\to\Omega^k\big)}.$$

**良定义性。** 由命题 3.3，$$B^k$$ 是 $$Z^k$$ 的子向量空间。加法群关于任意子群都是正规的，所以商群有意义；由于这里的一切都是 $$\mathbb{R}$$-向量空间，商还是 $$\mathbb{R}$$-向量空间，维数

$$\dim H^k_{dR}(M)=\dim Z^k-\dim B^k$$

（在有限的情形下计算用）。商里的元素记 $$[\omega]=\omega+B^k$$，称**上同调类 (cohomology class)**。由商的定义立刻得到三条：

1. $$[\omega]=[\omega']$$ 当且仅当 $$\omega-\omega'=d\eta$$ 对某个 $$\eta\in\Omega^{k-1}$$ 成立；
2. $$[\omega]=0$$ 当且仅当 $$\omega$$ 恰当；
3. $$H^k_{dR}(M)=0$$ 当且仅当 $$M$$ 上每个闭 $$k$$-形式都恰当。

用第 20 章的话说：$$Z^k$$ 是我们关心的量（闭形式），$$B^k$$ 是我们认定平凡的量（恰当形式，它们"来自上一层的微分"），商掉 $$B^k$$，剩下的就是"闭但不恰当"的净信息。**上同调就是"闭模恰当"。**

### 3.4 第一个计算：$$H^0$$ 数连通分支

**命题 3.5**。$$Z^0(M)=\{f\in C^\infty(M):df=0\}$$ 恰为 $$M$$ 上的**局部常值函数 (locally constant function)**，且

$$H^0_{dR}(M)=Z^0(M)\cong\mathbb{R}^{c(M)},$$

其中 $$c(M)$$ 是 $$M$$ 的连通分支个数。

**证明。** 分两步。

*第一步：$$df=0$$ 等价于 $$f$$ 局部常值。* 在任一坐标卡 $$(U,\varphi)$$ 内，$$df=\sum_{i}\partial_i f\,dx^i$$，而 $$\lbrace dx^i\rbrace$$ 逐点线性无关（第 12 章：$$\lbrace dx^i\rbrace$$ 是余切空间的一组基），故 $$df=0$$ 当且仅当所有 $$\partial_i f=0$$。在一条线段上偏导数恒为零的光滑函数必为常数：对任意两点，沿连接它们的直线段用链式法则与微积分基本定理，$$f(b)-f(a)=\int_0^1\frac{d}{dt}f(a+t(b-a))\,dt=0$$。把 $$U$$ 中任意两点用有限条这样的线段（一张卡内）连起来，就得到 $$f$$ 在 $$U$$ 上是常数。因此 $$df=0$$ 的函数在每张卡上取常值，即局部常值。反之，局部常值函数显然有 $$df=0$$。

*第二步：连通流形上的局部常值函数是常数。* 设 $$M$$ 连通、$$f$$ 局部常值。取 $$a\in M$$，令

$$A=\lbrace x\in M:f(x)=f(a)\rbrace.$$

$$A\ne\varnothing$$。$$A$$ 是开集：对每个 $$x\in A$$，因 $$f$$ 局部常值，存在 $$x$$ 的邻域在 $$f$$ 下取常值，而该常值必为 $$f(x)=f(a)$$，故整个邻域落在 $$A$$ 内。补集 $$M\setminus A=f^{-1}\big(\mathbb{R}\setminus\lbrace f(a)\rbrace\big)$$ 同理是开集：对每个 $$y\notin A$$，取 $$y$$ 的邻域在其上 $$f$$ 取常值 $$f(y)\ne f(a)$$，该邻域整个落在 $$A$$ 之外。于是 $$A$$ 既开又闭、非空；而连通空间没有非平凡的开闭子集，故 $$A=M$$，即 $$f$$ 恒等于 $$f(a)$$。

*第三步：数维数。* 由第二步，$$\ker d_0$$ 由"在每个连通分支上取常数"的函数组成，其维数等于连通分支个数。又 $$B^0=\operatorname{im}d_{-1}=0$$（不存在 $$-1$$ 次形式，$$d_{-1}$$ 是零映射），故

$$H^0_{dR}(M)=\ker d_0/\lbrace 0\rbrace=\ker d_0\cong\mathbb{R}^{c(M)}. \qquad\blacksquare$$

**推论 3.6**。$$H^0_{dR}(M)\cong\mathbb{R}$$ 当且仅当 $$M$$ 连通。

这是"上同调读出拓扑"的第一个例子：一个纯分析条件（$$df=0$$）的解空间的维数，数出了连通分支的个数。

### 3.5 Poincaré 引理：以及它在哪里失效

**定理 3.7（Poincaré 引理 / Poincaré lemma）**。设 $$U\subseteq\mathbb{R}^n$$ 是关于原点的**星形区域 (star-shaped domain)**：对每个 $$x\in U$$ 与每个 $$t\in[0,1]$$，都有 $$tx\in U$$。则

$$H^0_{dR}(U)\cong\mathbb{R},\qquad H^k_{dR}(U)=0\ \ (k\ge1).$$

换句话说：星形区域上的闭形式全都恰当。

**证明思路。** 要说明 $$\omega$$ 恰当，就得**把 $$\eta$$ 造出来**。$$\eta$$ 没法凭空猜，但有一个自然的来源：把 $$M$$ 沿径向收缩到原点，$$t\mapsto tx$$，把 $$\omega$$ 一路拉回。这个过程的"速度"就是一个算子，它的积分给出 $$\eta$$。整个证明只有两件事：先算清沿径向流的莱布尼茨型恒等式（引理 3.8），再把恒等式沿时间积分（定理 3.9）。

记 $$\phi_t(x)=tx$$ 为径向收缩（$$\phi_0$$ 把整个 $$U$$ 压到原点，$$\phi_1=\mathrm{id}$$），其速度场（第 10 章：流与 Lie 导数）是**径向场**

$$X=\sum_{i=1}^{n}x^i\partial_i.$$

**引理 3.8（Cartan 公式，径向场情形）**。记 $$\iota_X:\Omega^k\to\Omega^{k-1}$$ 为向量场 $$X$$ 的**缩并 (interior product)**，即对 $$\omega=\sum_I f_I\,dx^{i_1}\wedge\cdots\wedge dx^{i_k}$$，

$$\iota_X\omega=\sum_I\sum_{j=1}^{k}(-1)^{j-1}f_I\,x^{i_j}\,dx^{i_1}\wedge\cdots\widehat{dx^{i_j}}\cdots\wedge dx^{i_k}$$

（帽子表示删去该项）。记 $$L_X$$ 为沿 $$X$$ 的 Lie 导数（一般定义见第 24 章），它由 $$X$$ **真正的流**生成：径向场 $$X=\sum_ix^i\partial_i$$ 的流不是 $$\phi_t$$，而是指数流

$$\psi_s(x)=e^sx,\qquad s\in\mathbb{R},\qquad \psi_0=\mathrm{id},\qquad \frac{d}{ds}\psi_s(x)=e^sx=\psi_s(x)=X\big(\psi_s(x)\big).$$

**提醒（本节最容易混的一处记号）。** $$\psi_s$$ 与本节稍后要用的径向收缩 $$\phi_t(x)=tx$$（$$t\in[0,1]$$）是两个不同的族：$$\phi_t$$ 只在 $$t\in[0,1]$$ 上有定义，$$\phi_0$$ 把整个 $$U$$ 压成原点这一件事，恰恰是任何向量场的流都做不到的（流在 $$\mathrm{id}$$ 附近，不可能把开集压成一点）——所以 $$\phi_t$$ 本身**不是** $$X$$ 的流，只是恰好在 $$t>0$$ 时与流有 $$\phi_t=\psi_{\ln t}$$ 这层换参数的关系。这层关系在定理 3.9 的证明里要用到，届时会看到混淆两者会漏掉一个因子。此处我们只需 $$L_X$$ 的两条性质：其一，$$\displaystyle L_X\omega=\frac{d}{ds}\Big(\psi_s^*\omega\Big)\Big\vert_{s=0}$$；其二，$$L_X$$ 是 $$\Omega^\bullet(U)$$ 上的**偶（零次）分次导子**，即满足

$$L_X(\alpha\wedge\beta)=L_X\alpha\wedge\beta+\alpha\wedge L_X\beta,$$

并且作用在函数上就是沿 $$X$$ 的方向导数：$$L_Xf=Xf$$。则对一切 $$\omega\in\Omega^\bullet(U)$$，

$$L_X\omega=d(\iota_X\omega)+\iota_X(d\omega).$$

**证明。** 两个观察。

*(i) 两边都是偶导子。* 右边：$$d$$ 与 $$\iota_X$$ 分别是 $$+1$$ 次与 $$-1$$ 次的**奇导子**，即满足分次莱布尼茨规则

$$d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^{p}\alpha\wedge d\beta,\qquad
\iota_X(\alpha\wedge\beta)=\iota_X\alpha\wedge\beta+(-1)^{p}\alpha\wedge\iota_X\beta,$$

其中 $$p=\deg\alpha$$（第 14 章定理 3.17 与缩并的定义）。设 $$D=d\iota_X+\iota_X d$$。把两条规则各用一次并代入，展开后两次出现的交叉项是 $$(-1)^{p+1}\iota_X\alpha\wedge d\beta$$ 与 $$(-1)^{p}\iota_X\alpha\wedge d\beta$$，符号相反、互相抵消；剩下

$$D(\alpha\wedge\beta)=(D\alpha)\wedge\beta+\alpha\wedge(D\beta).$$

这就是"偶导子"的含义：没有符号。左边：由 $$\phi_t^*(\alpha\wedge\beta)=\phi_t^*\alpha\wedge\phi_t^*\beta$$（第 14 章定理 3.15），两边对 $$t$$ 求导（$$t=0$$）即得 $$L_X(\alpha\wedge\beta)=L_X\alpha\wedge\beta+\alpha\wedge L_X\beta$$，也是偶导子。

*(ii) 偶导子由它在生成元上的值决定。* 任一形式在局部可写成 $$\sum_I f_I\,dx^I$$。偶导子 $$D$$ 作用其上时由莱布尼茨规则展开：

$$D\Big(\sum_I f_I\,dx^{i_1}\wedge\cdots\wedge dx^{i_k}\Big)=\sum_I\Big[(Df_I)\,dx^I+f_I\sum_{j=1}^{k}dx^{i_1}\wedge\cdots\wedge D(dx^{i_j})\wedge\cdots\wedge dx^{i_k}\Big].$$

所以只要知道 $$D$$ 在所有**函数**上、以及在 $$dx^1,\dots,dx^n$$ 上的值，$$D$$ 就完全确定。

于是在生成元上核对两边：

- **函数 $$f$$**：$$L_Xf=Xf=\sum_i x^i\partial_i f$$；而 $$d(\iota_Xf)+\iota_X(df)=0+df(X)=Xf$$，因为 $$0$$-形式的缩并恒为零，而 $$df(X)$$ 就是 $$Xf$$。相符。
- **$$dx^i$$**：一方面 $$L_X(dx^i)=d(L_Xx^i)=d(x^i)=dx^i$$（第一步用 $$L_X$$ 与 $$d$$ 交换：由 $$\psi_s^*d=d\psi_s^*$$——$$\psi_s$$ 是光滑映射，第 14 章定理 3.16 对任意光滑映射都成立——两边对 $$s$$ 求导即得 $$L_Xd=dL_X$$）；另一方面 $$d\big(\iota_X(dx^i)\big)+\iota_X\big(d(dx^i)\big)=d(x^i)+0=dx^i$$。相符。

由 (i)(ii)，两个偶导子处处相等。$$\blacksquare$$

**为什么会想到造这样一个算子。** 引理 3.8 把 $$d\omega$$ 和 $$L_X\omega$$ 用 $$\iota_X$$ 连在了一起；而 $$L_X\omega$$ 又是"沿 $$X$$ 的流把 $$\omega$$ 推一点点"的变化率。如果能把这个"推一点点"从 $$t=0$$ 一路积分到 $$t=1$$（也就是把 $$U$$ 从"一个点"渐变到"恒等"走一遍），左右两边累积下来，应该正好把 $$\omega$$ 和 $$\phi_0^*\omega=0$$ 的差配平——而配平所用的那个原函数，就是要找的 $$K\omega$$。下面把这个想法做实。

**定理 3.9（同伦公式 / homotopy formula）**。在星形区域 $$U$$ 上定义线性算子 $$K:\Omega^k(U)\to\Omega^{k-1}(U)$$（$$k\ge1$$）为

$$K\omega=\int_0^1\frac1t\,\phi_t^*\big(\iota_X\omega\big)\,dt,$$

并对 $$\Omega^0(U)$$ 约定 $$Kf=0$$。**这个 $$1/t$$ 不是笔误。** 下面的证明会看到：$$\phi_t^*(\iota_X\omega)$$ 本身总带一个多余的因子 $$t$$（$$\iota_X$$ 把坐标 $$x^i$$ 代进去，拉回又把 $$x^i$$ 换成 $$tx^i$$，多出一个 $$t$$），这里的 $$1/t$$ 恰好把它消掉；消掉之后，被积对象对每个固定的 $$x$$ 是 $$t$$ 的光滑函数，在 $$t=0$$ 处也没有真正的奇点，可以逐点积分。则对一切 $$\omega\in\Omega^k(U)$$，

$$d\big(K\omega\big)+K\big(d\omega\big)=\omega-\phi_0^*\omega.$$

特别地，当 $$k\ge1$$ 时 $$\phi_0^*\omega=0$$（$$\phi_0$$ 是常值映射，微分恒为零，它的拉回把一切正次形式杀成零，见第 14 章定理 3.15），于是

$$d\big(K\omega\big)+K\big(d\omega\big)=\omega\qquad(k\ge1).$$

**证明。** 固定 $$x\in U$$，写 $$\omega=\sum_If_I\,dx^I$$（$$\lvert I\rvert=k$$）。

*第一步：直接算 $$\dfrac{d}{dt}\big(\phi_t^*\omega\big)$$，不经过"$$\phi_t$$ 是流"这条近路。* 由 $$\phi_t^*(dx^i)=d(tx^i)=t\,dx^i$$ 得 $$\phi_t^*(dx^I)=t^k\,dx^I$$，故

$$\phi_t^*\omega=t^k\sum_If_I(tx)\,dx^I .$$

对 $$t$$ 求导，乘积法则给出两项：

$$\frac{d}{dt}\big(\phi_t^*\omega\big)=\sum_I\Big[k\,t^{k-1}f_I(tx)+t^k\,\frac{d}{dt}f_I(tx)\Big]dx^I ,$$

再用链式法则 $$\dfrac{d}{dt}f_I(tx)=\displaystyle\sum_jx^j(\partial_jf_I)(tx)$$（对 $$t$$ 求导时，$$x$$ 是常数，变化的是 $$tx$$ 这个自变量）代入，并把公共因子 $$t^{k-1}$$ 提出：

$$\frac{d}{dt}\big(\phi_t^*\omega\big)=t^{k-1}\sum_I\Big[k\,f_I(tx)+\sum_jx^j(\partial_jf_I)(tx)\Big]dx^I . \qquad(\star)$$

*第二步：认出 $$(\star)$$ 括号里的量就是 $$L_X\omega$$（在点 $$tx$$ 取值）。* 径向场满足 $$Xx^i=x^i$$（直接代入 $$X=\sum_jx^j\partial_j$$ 即得），故对任意 $$f$$，$$Xf=\sum_jx^j\partial_jf$$——这正是 $$(\star)$$ 括号里第二项的定义。又由引理 3.8 已验证的 $$L_X(dx^i)=dx^i$$ 及 $$L_X$$ 是导子，

$$L_X(dx^I)=\sum_{s=1}^kdx^{i_1}\wedge\cdots\wedge L_X(dx^{i_s})\wedge\cdots\wedge dx^{i_k}=\sum_{s=1}^kdx^I=k\,dx^I$$

（$$k$$ 个因子各自贡献一次 $$dx^I$$，没有变化，加起来是 $$k$$ 倍）。于是

$$L_X\omega=\sum_I(Xf_I)\,dx^I+\sum_If_I\,L_X(dx^I)=\sum_I\big[Xf_I+k\,f_I\big]dx^I,$$

其系数恰是 $$(\star)$$ 方括号里的表达式（只是自变量还没代入 $$tx$$）。把 $$L_X\omega$$ 在点 $$tx$$ 取值，再乘 $$t^k$$（同第一步的换算规则），就是 $$\phi_t^*(L_X\omega)$$；对照 $$(\star)$$：

$$\frac{d}{dt}\big(\phi_t^*\omega\big)=t^{k-1}\big(L_X\omega\big)(tx)=\frac1t\cdot t^k(L_X\omega)(tx)=\frac1t\,\phi_t^*(L_X\omega). \qquad(\ast)$$

**为什么不能直接写 $$\frac{d}{dt}\phi_t^*\omega=\phi_t^*(L_X\omega)$$（少了 $$1/t$$）。** 引理 3.8 那条注已经提醒过：$$X$$ 真正的流是指数流 $$\psi_s(x)=e^sx$$，而 $$\phi_t(x)=tx=\psi_{\ln t}(x)$$ 只是把流的参数从 $$s$$ 换成了 $$t=e^s$$——这是一次**不等速**的换钟，$$\dfrac{ds}{dt}=\dfrac1t$$。链式法则算变化率时，会自动把这个换钟因子 $$\dfrac1t$$ 乘进来；$$(\star)$$ 的直接坐标计算等于把这件事如实做了一遍，$$(\ast)$$ 里的 $$1/t$$ 正是这个来源，不能省略。

*第三步：代入 Cartan 公式（引理 3.8），再对 $$t$$ 积分。* 由 $$(\ast)$$ 与引理 3.8，

$$\frac{d}{dt}\phi_t^*\omega=\frac1t\phi_t^*\big(d\iota_X\omega+\iota_Xd\omega\big)
=\frac1t\Big[d\big(\phi_t^*\iota_X\omega\big)+\phi_t^*\iota_X(d\omega)\Big],$$

第二步用了 $$\phi_t^*$$ 与 $$d$$ 交换（第 14 章定理 3.16）以及与 $$\iota_X$$ 交换（拉回与缩并都是逐点代数运算）。由 $$(\star)$$ 可见 $$\frac1t\phi_t^*(\iota_X\omega)$$（它正是 $$K\omega$$ 被积表达式的来源）本质上是 $$t^{k-1}$$ 乘一个在 $$t=0$$ 处取有限值的多项式型表达式，当 $$k\ge1$$ 时对 $$t\in[0,1]$$ 连续、光滑，$$t=0$$ 处没有真正的奇点——这就兑现了定理陈述里"$$1/t$$ 不会在 $$t=0$$ 出问题"的说法。函数 $$t\mapsto\phi_t^*\omega$$（在点 $$x$$ 取值）光滑，由微积分基本定理

$$\omega(x)-\phi_0^*\omega(x)=\int_0^1\frac{d}{dt}\Big(\phi_t^*\omega\Big)\,dt
=\int_0^1\frac1t\Big[d\big(\phi_t^*\iota_X\omega\big)+\phi_t^*\iota_X(d\omega)\Big]dt.$$

被积对象对 $$(t,x)$$ 光滑、积分区域紧，故积分与 $$d$$ 交换：

$$\omega-\phi_0^*\omega=d\Big(\int_0^1\frac1t\phi_t^*\iota_X\omega\,dt\Big)+\int_0^1\frac1t\phi_t^*\iota_X(d\omega)\,dt=d(K\omega)+K(d\omega). \qquad\blacksquare$$

**验个小例子，确认这个 $$1/t$$ 确实必要。** 取 $$U=\mathbb{R}^2$$、$$\omega=x\,dx$$（$$k=1$$，$$f_I(x,y)=x$$）。按 $$L_X\omega=\sum[Xf_I+kf_I]dx^I$$ 算，$$Xf_I=X(x)=x$$，故 $$L_X\omega=(x+x)dx=2x\,dx$$；这与直接用导子法则 $$L_X(x\,dx)=(Xx)dx+x\,L_X(dx)=x\,dx+x\,dx=2x\,dx$$ 相符。若漏掉 $$1/t$$、直接用 $$\widetilde K\omega=\int_0^1\phi_t^*(\iota_X\omega)\,dt$$，由 $$\iota_X(x\,dx)=x\cdot x=x^2$$（$$\iota_X$$ 把 $$dx$$ 换成 $$X$$ 的 $$x$$-分量，即 $$x$$，再乘系数 $$x$$），$$\phi_t^*(x^2)=(tx)^2=t^2x^2$$，得 $$\widetilde K\omega=\int_0^1t^2x^2\,dt=\frac13x^2$$，于是 $$d(\widetilde K\omega)=\frac23x\,dx\ne\omega$$——同伦公式在 $$\widetilde K$$ 下不成立，说明漏掉 $$1/t$$ 确实是错的。换成本定理的 $$K$$：$$\dfrac1t\phi_t^*(\iota_X\omega)=\dfrac1t\cdot t^2x^2=tx^2$$，$$K\omega=\int_0^1tx^2\,dt=\dfrac12x^2$$，$$d(K\omega)=x\,dx=\omega$$（$$d\omega=0$$ 已知，故 $$K(d\omega)=0$$），同伦公式成立。

**定理 3.7 的证明。** 设 $$\omega\in\Omega^k(U)$$（$$k\ge1$$）闭，即 $$d\omega=0$$。由定理 3.9，

$$\omega=d(K\omega)+K(0)=d(K\omega),$$

即 $$\omega$$ 恰当（取 $$\eta=K\omega\in\Omega^{k-1}$$）。这证明了 $$Z^k\subseteq B^k$$，与命题 3.3 合起来得 $$Z^k=B^k$$，于是

$$H^k_{dR}(U)=Z^k/B^k=0\qquad(k\ge1).$$

对 $$k=0$$：同伦公式给 $$f-\phi_0^*f=d(Kf)+K(df)$$，其中 $$Kf=0$$，$$\phi_0^*f=f(0)$$ 是常数，即

$$f(x)-f(0)=K(df)(x).$$

若 $$df=0$$，则 $$K(df)=0$$，故 $$f(x)=f(0)$$ 恒成立。于是 $$Z^0$$ 恰由常值函数组成，$$H^0_{dR}(U)=\mathbb{R}$$（与命题 3.5 一致，因为星形区域是道路连通、因而是连通的）。$$\blacksquare$$

**Poincaré 引理的失效点在哪里？** 请看证明里唯一用到星形的地方：$$\phi_t(x)=tx$$ 必须**落在 $$U$$ 内**。也就是说，"把整个区域收缩成一个点"这条路径不能跑出流形。对 $$\mathbb{R}^2\setminus\{0\}$$ 做不到——收缩到原点的路上必须穿过原点，而原点被挖掉了。于是 $$\phi_0$$ 不存在，同伦公式右边那一项 $$\phi_0^*\omega$$ 无法消掉，$$K(d\omega)$$ 也帮不上忙。第 3.7 节会看到，这个"缩不过去"的事实有可测量的后果：$$H^1_{dR}\big(\mathbb{R}^2\setminus\{0\}\big)\ne0$$，而且它的维数恰好是 1。

**注（可缩 vs 星形）**。定理 3.9 的条件其实比"星形"更宽：只要存在一个同伦把 $$M$$ "缩成一点"，同样的公式（把 $$\phi_t$$ 换成那个同伦）就能用。3.8 节给出这个推广（同伦不变性），并说明它为什么不依赖坐标。

### 3.6 回到入口题：一个闭而不恰当的形式

现在把第二节的三问一次做完。记 $$r^2=x^2+y^2$$，$$\omega=\dfrac{-y}{r^2}dx+\dfrac{x}{r^2}dy$$，即 $$\omega=P\,dx+Q\,dy$$，其中

$$P=-\frac{y}{x^2+y^2},\qquad Q=\frac{x}{x^2+y^2}.$$

**(a) 计算 $$d\omega$$。** 在平面区域上 $$d(P\,dx+Q\,dy)=(\partial_xQ-\partial_yP)\,dx\wedge dy$$。逐项求导（用商的求导法则）：

$$\partial_xQ=\frac{1\cdot (x^2+y^2)-x\cdot 2x}{(x^2+y^2)^2}=\frac{y^2-x^2}{(x^2+y^2)^2},$$

$$\partial_yP=\frac{-1\cdot(x^2+y^2)+y\cdot 2y}{(x^2+y^2)^2}=\frac{y^2-x^2}{(x^2+y^2)^2}.$$

两者相等，故

$$d\omega=0.$$

$$\omega$$ **是闭形式**。

**(c) 先做 (c)，因为它反过来决定 (b)。** 沿 $$\gamma(t)=(\cos t,\sin t)$$，$$t\in[0,2\pi]$$，有 $$dx=-\sin t\,dt$$、$$dy=\cos t\,dt$$、$$x^2+y^2=1$$。于是

$$\omega(\gamma'(t))=\frac{-y\cdot(-\sin t)+x\cdot\cos t}{1}=\sin^2t+\cos^2t=1,$$

故

$$\int_\gamma\omega=\int_0^{2\pi}1\,dt=2\pi.$$

**(b) 不存在这样的 $$f$$。** 反设 $$\omega=df$$。第 26 章（微积分基本定理，Stokes 定理的 0 维特例）给出：对任意分段光滑曲线 $$\gamma:[0,1]\to M$$，

$$\int_\gamma df=f\big(\gamma(1)\big)-f\big(\gamma(0)\big).$$

我们的 $$\gamma$$ 是**闭**曲线（$$\gamma(0)=\gamma(2\pi)=(1,0)$$），于是 $$\int_\gamma df=f(1,0)-f(1,0)=0$$。但 (c) 算出 $$\int_\gamma\omega=2\pi\ne0$$，矛盾。所以不存在这样的 $$f$$：

$$\omega\text{ 闭，但 }\omega\text{ 不恰当},\qquad [\omega]\ne0\in H^1_{dR}\big(\mathbb{R}^2\setminus\{0\}\big).$$

**为什么 (c) 能判决 (b)。** 要害只有一句：$$\gamma$$ 是闭曲线。$$\omega$$ 闭的形式（$$d\omega=0$$）在**局部**总能积分成势：在挖去一条射线的区域上，极角 $$\theta$$ 是单值的，直接算得

$$d\theta=\frac{-y\,dx+x\,dy}{x^2+y^2}=\omega.$$

但 $$\theta$$ 不能成为整个 $$M$$ 上的函数：绕原点一周，$$\theta$$ 增加 $$2\pi$$，它是个**多值函数**。而 (c) 里那个数 $$2\pi$$ 正是这个多值性的量化——绕一周，势回不来。所以 $$\omega$$ 非恰当的障碍不是任何局部解析性质（$$\omega$$ 在每一点都光滑、都局部恰当），纯粹是**全局的单值性**，而单值性由"挖掉的那个点"决定。这就是"有洞"的精确含义。

### 3.7 反变性：为什么进来的是上同调

到目前为止，"闭模恰当"还只是 $$M$$ 上的一套形式运算。要让它是**拓扑不变量**，第一步得让它对映射有反应。而对映射的反应方式，第 14 章已经替我们定好了：形式只能拉回，不能推前。

**定理 3.10（函子性 / functoriality）**。设 $$F:M\to N$$ 光滑。则拉回 $$F^*:\Omega^k(N)\to\Omega^k(M)$$ 下降为上同调之间的线性映射

$$F^*:H^k_{dR}(N)\longrightarrow H^k_{dR}(M),\qquad F^*[\omega]:=[F^*\omega].$$

**证明。** 要验两件事。

*(1) $$F^*$$ 保闭、保恰当。* 若 $$d\omega=0$$，则依第 14 章定理 3.16（$$F^*d=dF^*$$），

$$d(F^*\omega)=F^*(d\omega)=F^*0=0;$$

若 $$\omega=d\eta$$，则 $$F^*\omega=F^*(d\eta)=d(F^*\eta)$$，恰当。

*(2) 因此商映射良定义。* 由 (1)，$$F^*$$ 把 $$Z^k(N)$$ 映入 $$Z^k(M)$$、把 $$B^k(N)$$ 映入 $$B^k(M)$$，于是它诱导商空间之间的线性映射 $$Z^k(N)/B^k(N)\to Z^k(M)/B^k(M)$$。具体地，若 $$[\omega]=[\omega']$$，即 $$\omega-\omega'=d\eta$$，则

$$F^*\omega-F^*\omega'=F^*(d\eta)=d(F^*\eta)\in B^k(M),$$

故 $$[F^*\omega]=[F^*\omega']$$。代表元的选取不影响结果，映射良定义。$$\blacksquare$$

**推论 3.11**。$$H^k_{dR}$$ 是一个**反变函子 (contravariant functor)**：

$$(\mathrm{id}_M)^*=\mathrm{id},\qquad (G\circ F)^*=F^*\circ G^*,$$

（两条都由第 14 章定理 3.15 与定义直接得到）。也就是说，箭头 $$F:M\to N$$ 被送到反方向的箭头 $$F^*:H^k_{dR}(N)\to H^k_{dR}(M)$$。

**这就是第 14 章"只拉不推"的全局后果。** 第 14 章 3.5 节说明了：一般光滑映射 $$F$$ 会丢信息（$$dF_p$$ 可能不可逆），$$M$$ 上的形式没有唯一的方式推到 $$N$$ 上去，而拉回永远可行、永远自然（$$N$$ 上的楔积与 $$d$$ 都被无条件搬运到 $$M$$）。这个局部的不对称，到了上同调层面就成了一条铁律。对比一下另一侧：链上的**推前 (pushforward)** $$F_\#:C_k(M)\to C_k(N)$$ 总是可行的（把单形复合上 $$F$$），所以第 20 章的同调是**协变**的。

于是同一对流形之间的映射，在下同调上同向走，在上同调上反向走。第 06 章讲对偶空间时那句"指标的上下与箭头的方向是一回事"，到这里第一次成为整章的结构：$$\partial$$ 协变配下标，$$d$$ 反变配上标。**这不是记号约定，是数学事实。**

### 3.8 同伦不变性

反变性（3.7）只说明 $$H^k$$ 对映射有反应，还没说明它是拓扑不变量——因为不同的 $$F$$ 可能给出不同的 $$F^*$$。下面这条定理把它压住了。

**定理 3.12（同伦不变性 / homotopy invariance）**。若 $$F_0,F_1:M\to N$$ 光滑同伦，则

$$F_0^*=F_1^*:H^k_{dR}(N)\longrightarrow H^k_{dR}(M).$$

**证明思路。** 要证两个映射在上同调上相等，只需证明它们的差是"某个恰当形式"，即找到线性映射 $$h:\Omega^k(N)\to\Omega^{k-1}(M)$$ 使

$$F_1^*\omega-F_0^*\omega=d(h\omega)+h(d\omega)\qquad\text{对一切 }\omega. \qquad(\ast)$$

这样的 $$h$$ 叫 $$F_0^*,F_1^*$$ 的**链同伦 (chain homotopy)**。一旦 $$(\ast)$$ 成立、且 $$\omega$$ 闭，右边就只剩 $$d(h\omega)$$，即差恰当，故上同调类相同。

**构造与验证。** 设 $$H:M\times[0,1]\to N$$ 是 $$F_0$$ 到 $$F_1$$ 的光滑同伦（$$H(x,s)=F_s(x)$$）。记 $$\partial_t$$ 为 $$M\times[0,1]$$ 上沿 $$t$$ 方向的坐标向量场，$$j_s:M\to M\times[0,1]$$，$$j_s(x)=(x,s)$$。定义

$$h\omega=\int_0^1 j_s^*\Big(\iota_{\partial_t}\big(H^*\omega\big)\Big)\,ds .$$

验证与 3.5 节定理 3.9 的推导逐字相同——把那里的径向场 $$X$$ 换成 $$\partial_t$$、把径向流 $$\phi_t(x)=tx$$ 换成平移流 $$(x,s)\mapsto(x,s+t)$$ 即可（引理 3.8 的证明只用到"$$X$$ 有流"与"两边是偶导子"，对 $$\partial_t$$ 逐字重写）。于是同伦公式给出

$$j_1^*(H^*\omega)-j_0^*(H^*\omega)=d(h\omega)+h(d\omega),$$

而 $$j_s^*(H^*\omega)=(H\circ j_s)^*\omega=F_s^*\omega$$，这正是 $$(\ast)$$。$$\blacksquare$$

**推论 3.13**。若 $$F:M\to N$$ 是同伦等价，则 $$F^*:H^k_{dR}(N)\to H^k_{dR}(M)$$ 是同构。特别地，**可缩流形**（同伦等价于一个点）满足

$$H^0_{dR}\cong\mathbb{R},\qquad H^k_{dR}=0\ (k\ge1).$$

这是定理 3.7 的范畴版本。注意它的条件比 Poincaré 引理宽：不要求星形、不要求嵌在 $$\mathbb{R}^n$$ 里，只要求能缩成一点。（$$\mathbb{R}^n$$ 本身、凸开集、上半平面都可缩；$$S^n$$ 不可缩，因为它有 $$H^n\ne0$$。）

### 3.9 Stokes 把两个复形配对起来

现在把第 09–10 章的链拉进来。设 $$\sigma:\Delta_k\to M$$ 是奇异 $$k$$-单形（第 18 章），$$\omega\in\Omega^k(M)$$，定义

$$\langle\sigma,\omega\rangle:=\int_\sigma\omega:=\int_{\Delta_k}\sigma^*\omega .$$

按第 18 章的写法，奇异链是单形的整系数形式和 $$c=\sum a_i\sigma_i$$，把配对线性延拓：

$$\Big\langle\sum_ia_i\sigma_i,\ \omega\Big\rangle=\sum_i a_i\int_{\sigma_i}\omega .$$

于是得到一个双线性映射 $$C_k(M)\times\Omega^k(M)\to\mathbb{R}$$。第 26 章的 Stokes 定理在这个记号下写成一行极简的形式：

$$\langle c,d\omega\rangle=\langle\partial c,\omega\rangle .$$

左边是 $$d$$ 升维、右边是 $$\partial$$ 降维，两个算子在积分配对下互为**伴随 (adjoint)**。

**命题 3.15（配对下降到 (上)同调）**。若 $$c\in C_k(M)$$ 是闭链（$$\partial c=0$$）、$$\omega\in\Omega^k(M)$$ 是闭形式（$$d\omega=0$$），则数 $$\langle c,\omega\rangle$$ 只依赖 $$[c]\in H_k(M;\mathbb{R})$$ 与 $$[\omega]\in H^k_{dR}(M)$$。因此有良定义的配对

$$H_k(M;\mathbb{R})\times H^k_{dR}(M)\longrightarrow\mathbb{R},\qquad\big([c],[\omega]\big)\longmapsto\langle c,\omega\rangle,$$

称为 **Kronecker 配对 (Kronecker pairing)**。

**证明。** 两类"换代表元"都要验，而两处用的正是 Stokes 定理的两个朝向。

*(1) 换链：* 设 $$c'=c+\partial b$$。则

$$\langle c',\omega\rangle=\langle c,\omega\rangle+\langle\partial b,\omega\rangle=\langle c,\omega\rangle+\langle b,d\omega\rangle=\langle c,\omega\rangle+\langle b,0\rangle=\langle c,\omega\rangle,$$

第三步用 Stokes，第四步用 $$d\omega=0$$。

*(2) 换形式：* 设 $$\omega'=\omega+d\eta$$。则

$$\langle c,\omega'\rangle=\langle c,\omega\rangle+\langle c,d\eta\rangle=\langle c,\omega\rangle+\langle\partial c,\eta\rangle=\langle c,\omega\rangle+\langle 0,\eta\rangle=\langle c,\omega\rangle,$$

第三步用 Stokes，第四步用 $$\partial c=0$$。$$\blacksquare$$

**这是本章全部机制的汇合点，值得把话说透。** $$\partial^2=0$$ 让"闭链"成为一个有意义的集合，$$d^2=0$$ 让"闭形式"成为一个有意义的集合；而 Stokes 定理**恰好**使得"模掉边界 / 模掉恰当形式"这个操作与积分相容。三者缺一，命题 3.15 就不成立：若 $$d^2\ne0$$，则 $$B^k$$ 里会有不闭的元素，商 $$Z^k/B^k$$ 根本无从谈起；若 $$\partial^2\ne0$$，则 $$\partial b$$ 不是闭链，"换一个闭链代表元"这件事也没有意义。**这条配对是全书第二条大暗线的落点：第 18 章的 $$\partial^2=0$$ 与第 14 章的 $$d^2=0$$，在这里被同一个商结构统一。**

### 3.10 de Rham 定理

命题 3.15 给出了一个配对。de Rham 定理说：把系数取成实数时，这个配对其实是**完美配对**，两边的信息一一对应。

**定理 3.16（de Rham）**。设 $$M$$ 是光滑流形。对每个 $$k$$ 有线性映射

$$\Phi:H^k_{dR}(M)\longrightarrow\big(H_k(M;\mathbb{R})\big)^*=\operatorname{Hom}\big(H_k(M;\mathbb{R}),\mathbb{R}\big),\qquad
[\omega]\longmapsto\Big([c]\mapsto\langle c,\omega\rangle\Big),$$

它是同构：

$$H^k_{dR}(M)\cong\big(H_k(M;\mathbb{R})\big)^*\cong H^k_{\text{sing}}(M;\mathbb{R}).$$

当 $$M$$ 是紧流形时，$$H_k(M;\mathbb{R})$$ 与 $$H^k_{dR}(M)$$ 都有限维，这个配对双线性非退化。

**关于证明的实话。** 这个定理的两半用的是完全不同、而且都非常深的技术：左端完全用微分形式（本章的全部工具），右端用奇异链与它的同调（第 09–10 章），而"两端相等"是分析（形式）与拓扑（链）之间一座非平凡的桥，其完整证明超出本课范围（见延伸阅读）。**本课只使用它的推论**，而且对 $$S^n$$、$$T^n$$、$$\mathbb{R}^n\setminus\{0\}$$ 这类常见空间，两边可以分别算出结果来互相验证（见第五节与练习）。

**注（它为什么顺带解释了反变性）**。既然 $$H^k_{dR}\cong\operatorname{Hom}(H_k,\mathbb{R})$$，而 Hom 函子**反转箭头**（第 20 章：$$f\mapsto f\circ\varphi$$ 把 $$H_k(M)\to H_k(N)$$ 变成 $$\operatorname{Hom}(H_k(N),\mathbb{R})\to\operatorname{Hom}(H_k(M),\mathbb{R})$$），那么"同调协变、上同调反变"就不是两条独立的经验规律，而是同一条对偶的两个侧面。3.7 节从形式这边看到的 $$F^*$$，与这一节从链这边看到的 Hom，是同一个东西。

### 3.11 两个复形，一台机器

现在把暗线显式闭合。把正文里出现过的两个定义并排写在下面：

$$H_k(M)=\frac{\ker\big(\partial_k:C_k\to C_{k-1}\big)}{\operatorname{im}\big(\partial_{k+1}:C_{k+1}\to C_k\big)},
\qquad
H^k_{dR}(M)=\frac{\ker\big(d_k:\Omega^k\to\Omega^{k+1}\big)}{\operatorname{im}\big(d_{k-1}:\Omega^{k-1}\to\Omega^k\big)} .$$

两式的**形状一字不差**：

- 分子都是"复合为零"的那一半（闭链 / 闭形式）；
- 分母都是"来自上一层"的那一半（边界 / 恰当形式）；
- 商的含义都是同一句：**保留闭的，扣掉平凡的**。

差别只有两处，而且都是"刻度盘反着转"：

| | 同调（第 09–10 章） | 上同调（本章） |
|---|---|---|
| 算子 | $$\partial$$，**降**维 | $$d$$，**升**维 |
| 指标 | 下标 $$H_k$$ | 上标 $$H^k$$ |
| 函子 | 协变（推前 $$F_\#$$） | 反变（拉回 $$F^*$$） |
| 生成本质 | $$\partial^2=0$$ | $$d^2=0$$ |

所以本章最重要的一句话是：**同调数洞，上同调还是用同一台机器数同一批洞，只是刻度盘反着转。** "数洞"在这里有精确含义——$$H^k_{dR}$$ 的非零元素是"闭但不恰当"的形式，它们是"局部能积分、全局积不出来"的障碍；这种障碍的个数（维数）就是通常说的 Betti 数。

**预告第 70 章。** 上面这个商结构其实完全是**形式**的：并没有用到 $$\partial$$ 与 $$d$$ 的任何几何含义，只用到了一串线性映射满足复合为零。第 70 章（同调代数：导出函子）会把这件事推到一般形式：

- 任意函子都谈不上"正合"（保持短正合列），它的**正合性缺陷**可以用同调群的形状逐层量化；
- $$\ker/\operatorname{im}$$ 正是"离正合有多远"的度量：复形正合当且仅当 $$H=0$$；
- 第 09–10 章的 $$\partial$$ 与第 07–14 章的 $$d$$，都只是那条一般理论的两个特例；第 70 章还会把"链同伦"（3.8 节那个 $$h$$）一般化，用它证明消解的链同伦等价唯一，从而让**导出函子**（$$\operatorname{Ext}$$、$$\operatorname{Tor}$$）良定义化。

**这条线在本书里第二次抬头，就是那里。**

## 四、几何与物理直觉 (Intuition)

**1. 闭 = 无旋，恰当 = 有势，上同调 = 数"无旋无势"的场有多少。**

在 $$\mathbb{R}^3$$ 的向量分析语言里（第 14 章 3.9 节的对齐表）：1-形式闭 $$\iff$$ 对应的向量场旋度为零；1-形式恰当 $$\iff$$ 场是某个标量势的梯度。于是 $$H^1_{dR}=0$$ 就是那句熟悉的"无旋场必有势"（Poincaré 引理在 $$\mathbb{R}^3$$ 上的特例）；而 $$H^1_{dR}\ne0$$ 意味着**存在无旋但无势的场**——这样的场只在有洞的区域内出现。入口题里的 $$\omega$$ 正是最经典的例子：$$\mathbb{R}^2\setminus\{0\}$$ 上那个"绕原点打转"的涡旋场。

**2. $$\int_\gamma$$ 是一个"探测器"。**

上同调类是非零的，这件事如何被看见？用积分。$$[\omega]\in H^1_{dR}(M)$$ 与一个闭曲线 $$\gamma$$ 配成 $$\int_\gamma\omega$$：这是"洞"与"绕洞的回路"之间的读数。绕数一非零，类就非零。这个思想在物理里的三次登场值得记住：

- **电磁势与 Dirac 磁单极**。Maxwell 方程组的一半写成 $$dF=0$$（第 24 章）：场强张量 $$F$$ 总是闭的。$$F$$ 是否**全局**等于某个势 $$A$$ 的微分（$$F=dA$$），是上同调问题。在 $$\mathbb{R}^3\setminus\{\text{一条轴}\}$$ 上取一条磁单极线，$$S^2$$ 的 $$H^2_{dR}=\mathbb{R}\ne0$$，于是 $$A$$ 无法全局存在（Dirac 弦）——这直接给出磁荷的量子化条件：积分必须取分立值，否则量子力学的相位不单值。
- **Aharonov–Bohm 效应**。电子在螺线管外走一圈，那里 $$B=dA=0$$（场强为零），但 $$\oint A\ne0$$。干涉条纹的移动正是这个积分；它就是"$$A$$ 闭但不恰当"的物理读数。
- **Berry 相（绝热相位）**。参数空间上，量子态沿闭合路径演化一圈回来的相位，同样是一个"闭但不恰当"的积分，取值由参数空间的洞（简并点）决定。

这三个例子是现代物理中"几何相位"这个词的全部含义：**上同调把"局部可解"与"全局可解"的差距变成线性代数。**

**3. 为什么"反变"是几何的，而不是记号的。**

设想 $$F:M\to N$$ 是两个空间之间的映射。$$N$$ 上的洞，在 $$M$$ 上通过 $$F$$ 被"拉"回来。若 $$F$$ 是一个同伦等价（比如把 $$\mathbb{R}^3\setminus\{0\}$$ 沿径向压到 $$S^2$$），洞与洞就一一对应；若 $$F$$ 把整个 $$M$$ 压成一个点，则所有正的洞都消失（$$F^*=0$$）——因为 $$F$$ 的像里容不下洞。这是最直观的"反变"：**信息只能从大的空间流向小的空间，而且方向与映射相反。**

**4. 欧拉示性数是两条线的交汇点。**

第 09–10 章从胞腔数出发定义 $$\chi=\sum_k(-1)^k(\text{$$k$$-胞腔数})$$，本章给出另一条路

$$\chi(M)=\sum_{k=0}^{n}(-1)^k\dim H^k_{dR}(M)=\sum_{k=0}^n(-1)^kb_k,$$

其中 $$b_k$$ 是 Betti 数。第 26 章的 Gauss–Bonnet 定理说 $$\int_M K\,dA=2\pi\chi(M)$$：曲率的积分等于它。四章的内容在同一个数上汇合，这不是巧合——第五节经典题 4 会给出"两条路给出同一个数"的纯代数证明。

## 五、经典问题精讲 (Classical Problems)

### 经典题 1：$$H^0$$ 与连通分支

**题。** 计算 $$\mathbb{R}\setminus\{0,1\}$$ 的 de Rham 上同调群，并说明为什么这里的答案是纯拓扑的。

**考点与位置。** 直接检验定义 3.4 与命题 3.5；它也是"上同调是拓扑不变量"的最简例子。

**解。** 记 $$M=\mathbb{R}\setminus\{0,1\}$$，它是三个开区间 $$(-\infty,0)$$、$$(0,1)$$、$$(1,+\infty)$$ 的不交并，故 $$c(M)=3$$。由命题 3.5，

$$H^0_{dR}(M)\cong\mathbb{R}^3 .$$

对正次上同调：$$M$$ 的每个连通分支（开区间）都同构于 $$\mathbb{R}$$，因而可缩。把 $$M$$ 沿每个分支收缩到该分支内取定的一个点，得到三个点构成的离散空间 $$P=\lbrace p_1,p_2,p_3\rbrace$$，这是同伦等价。由推论 3.13（同伦不变性），

$$H^k_{dR}(M)\cong H^k_{dR}(P)\qquad(k\ge0).$$

离散空间的 $$k$$-形式（$$k\ge1$$）恒为零，故 $$H^k_{dR}(P)=0$$（$$k\ge1$$）；$$H^0_{dR}(P)=\mathbb{R}^3$$ 与上面一致。于是

$$H^0_{dR}(M)=\mathbb{R}^3,\qquad H^k_{dR}(M)=0\ \ (k\ge1),\qquad \chi(M)=3 .$$

**为什么"纯拓扑"。** $$\mathbb{R}\setminus\{0,1\}$$ 与 $$\mathbb{R}$$（挖掉 $$n$$ 个点则与 $$n+1$$ 个点同伦等价）的上同调只依赖"挖掉了几个点"，与用什么具体形状挖、用什么坐标描述无关。这就是同伦不变性的内容。

### 经典题 2：$$\mathbb{R}^3\setminus\{0\}$$（以及一般的 $$\mathbb{R}^n\setminus\{0\}$$）

**题。** 完整计算 $$H^k_{dR}\big(\mathbb{R}^3\setminus\{0\}\big)$$，并把结论与 $$H^k_{dR}(\mathbb{R}^3)$$、$$H^k_{dR}(S^2)$$ 对照。

**考点与位置。** 同伦不变性（推论 3.13）+ 一个显式的"闭而不恰当"形式（入口题的高维版本）+ 拼接引理。这是本章的"标准范本"：它演示了当 Poincaré 引理失效时，如何用两件工具把结果算干净。

**解。**

**第一步：先算出"不该是什么"。** $$\mathbb{R}^3$$ 可缩，由推论 3.13 得 $$H^0_{dR}(\mathbb{R}^3)=\mathbb{R}$$、$$H^{k}_{dR}(\mathbb{R}^3)=0\ (k\ge1)$$。而挖掉原点以后结果会变——下面看到 $$H^2$$ 会非零。**所以"挖掉一个点"确实是一处真实的拓扑改变，Poincaré 引理正是在这里失效的。**

**第二步：把 $$\mathbb{R}^3\setminus\{0\}$$ 同伦压到球面。** 令 $$\rho(x)=x/\lvert x\rvert$$，$$i:S^2\hookrightarrow\mathbb{R}^3\setminus\{0\}$$ 为包含。则 $$\rho\circ i=\mathrm{id}_{S^2}$$；而 $$H_t(x)=(1-t)x+t\,x/\lvert x\rvert$$，$$t\in[0,1]$$，满足

$$H_t(x)=\Big((1-t)+\frac{t}{\lvert x\rvert}\Big)x,\qquad (1-t)+\frac{t}{\lvert x\rvert}>0\ \ (t<1),$$

故 $$H_t(x)\ne0$$，且 $$H_0=\mathrm{id}$$、$$H_1=i\circ\rho$$。所以 $$H_t$$ 是从恒等到 $$i\circ\rho$$ 的同伦，$$i$$ 与 $$\rho$$ 互为同伦逆。由推论 3.13，

$$H^k_{dR}\big(\mathbb{R}^3\setminus\{0\}\big)\cong H^k_{dR}(S^2)\qquad(k\ge0).$$

**第三步：算 $$H^\bullet(S^2)$$（先给一个引理）。**

**拼接引理 (patching lemma)。** 设 $$M=U\cup V$$，$$U,V$$ 是开集，$$U\cap V$$ **连通**，且 $$H^1_{dR}(U)=H^1_{dR}(V)=0$$。则 $$H^1_{dR}(M)=0$$。

*证明。* 设 $$\alpha\in\Omega^1(M)$$ 闭。因为 $$H^1(U)=H^1(V)=0$$，存在 $$f_U\in C^\infty(U)$$、$$f_V\in C^\infty(V)$$ 使 $$\alpha\vert_U=df_U$$、$$\alpha\vert_V=df_V$$。在 $$U\cap V$$ 上 $$d(f_U-f_V)=\alpha-\alpha=0$$，而 $$U\cap V$$ 连通，由命题 3.5（第一步）$$f_U-f_V$$ 在 $$U\cap V$$ 上是常数 $$c$$。定义 $$f:M\to\mathbb{R}$$：在 $$U$$ 上取 $$f_U$$，在 $$V$$ 上取 $$f_V+c$$。在 $$U\cap V$$ 上这两个定义相符（$$f_V+c$$ 与 $$f_U$$ 相等），故 $$f$$ 是整体光滑函数；且 $$df=\alpha$$（在 $$U$$ 上 $$df_U=\alpha$$，在 $$V$$ 上 $$d(f_V+c)=df_V=\alpha$$）。于是每个闭 1-形式都恰当。$$\blacksquare$$

*算 $$H^0(S^2)$$：* $$S^2$$ 连通，由推论 3.6，$$H^0_{dR}(S^2)=\mathbb{R}$$。

*算 $$H^1(S^2)=0$$：* 取 $$U=S^2\setminus\{N\}$$（挖去北极）、$$V=S^2\setminus\{S\}$$（挖去南极）。由球极投影，$$U\cong V\cong\mathbb{R}^2$$ 可缩，故 $$H^1(U)=H^1(V)=0$$；而 $$U\cap V=S^2\setminus\{N,S\}$$ 是球面上两条纬线之间的环带，径向缩到赤道给出它到 $$S^1$$ 的同伦等价，特别地**连通**。由拼接引理，$$H^1_{dR}(S^2)=0$$。

*算 $$H^2(S^2)\ne0$$：* 记 $$\mathrm{vol}=dx\wedge dy\wedge dz$$，径向场 $$X=x\partial_x+y\partial_y+z\partial_z$$，定义

$$\omega_2=\frac{1}{r^3}\,\iota_X(\mathrm{vol}),\qquad r=\sqrt{x^2+y^2+z^2},$$

即在坐标下 $$\omega_2=\dfrac{x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy}{(x^2+y^2+z^2)^{3/2}}$$（与 $$\iota_X(\mathrm{vol})$$ 对照即知，符号与标准定义一致）。

*$$\omega_2$$ 是闭的。* 由引理 3.8（Cartan 公式，它是在任何开集上成立的局部恒等式），

$$d\big(\iota_X(\mathrm{vol})\big)=L_X(\mathrm{vol})-\iota_X(d\,\mathrm{vol})=L_X(\mathrm{vol}).$$

而 $$L_X(\mathrm{vol})=(\operatorname{div}X)\,\mathrm{vol}=3\,\mathrm{vol}$$（$$L_X$$ 与 $$d$$ 交换、$$L_Xdx^i=d(x^i)=dx^i$$，故 $$L_X$$ 把每个 $$dx^i$$ 变成自己，三重楔积多出因子 3）。于是

$$d\omega_2=d\big(r^{-3}\big)\wedge\iota_X(\mathrm{vol})+r^{-3}d\big(\iota_X(\mathrm{vol})\big)
=\Big(-\frac{3}{r^{5}}\sum_i x^i dx^i\Big)\wedge\iota_X(\mathrm{vol})+\frac{3}{r^{3}}\mathrm{vol}.$$

再用一次 $$\iota_X$$ 的定义：$$\sum_i x^idx^i\wedge\iota_X(\mathrm{vol})=\sum_i (x^i)^2\,\mathrm{vol}=r^2\mathrm{vol}$$（展开 $$\iota_X\mathrm{vol}=\sum_i(-1)^{i-1}x^idx^1\wedge\cdots\widehat{dx^i}\cdots\wedge dx^3$$，只有 $$j=i$$ 的项留下 $$dx^i\wedge dx^{I\setminus i}=\mathrm{vol}$$，且两次符号相乘得 $$+1$$）。代入得

$$d\omega_2=-\frac{3}{r^{3}}\mathrm{vol}+\frac{3}{r^{3}}\mathrm{vol}=0 .$$

*$$\omega_2$$ 不恰当。* 在单位球面 $$S^2$$ 上 $$r=1$$、$$X$$ 就是外法向单位向量场，此时 $$\iota_X(\mathrm{vol})$$ 正是 $$S^2$$ 的体积形式，故

$$\int_{S^2}\omega_2=\operatorname{area}(S^2)=4\pi\ne0 .$$

反设 $$\omega_2=d\eta$$，则用 Stokes（$$\partial S^2=\varnothing$$，$$S^2$$ 是闭曲面）

$$\int_{S^2}\omega_2=\int_{S^2}d\eta=\int_{\partial S^2}\eta=0,$$

与 $$4\pi\ne0$$ 矛盾。所以 $$[\omega_2]\ne0\in H^2_{dR}(S^2)$$。而 3 维流形上不存在 3-形式以上的非零形式，$$H^k(S^2)=0\ (k\ge3)$$；且 $$H^2$$ 是 1 维的（由 de Rham 定理 3.16 与第 20 章 $$\dim H_2(S^2)=1$$；第五节经典题 4 会给出一个不依赖它的独立论证）。

**结论：**

$$H^k_{dR}(S^2):\quad H^0=\mathbb{R},\ H^1=0,\ H^2=\mathbb{R};\qquad
H^k_{dR}\big(\mathbb{R}^3\setminus\{0\}\big):\ \text{同 }S^2.$$

**第四步：一般 $$n$$。** 把 $$\rho$$、$$H_t$$ 逐字换成 $$\mathbb{R}^n$$ 的版本，得 $$\mathbb{R}^n\setminus\{0\}\simeq S^{n-1}$$；再令

$$\omega_{n-1}=\frac{1}{r^{n}}\,\iota_X(\mathrm{vol}_n),\qquad \mathrm{vol}_n=dx^1\wedge\cdots\wedge dx^n,$$

同样的三步计算给出 $$d\omega_{n-1}=0$$（把上面出现的 3 换作 $$n$$），而 $$\int_{S^{n-1}}\omega_{n-1}=\operatorname{vol}(S^{n-1})\ne0$$，故 $$[\omega_{n-1}]\ne0$$，即

$$H^{n-1}_{dR}\big(\mathbb{R}^n\setminus\{0\}\big)\ne0 .$$

$$n=2$$ 时这就是入口题的 $$\omega$$（差一个符号约定：$$\iota_X(dx\wedge dy)=x\,dy-y\,dx$$，而 $$\int_{S^1}\frac{x\,dy-y\,dx}{x^2+y^2}=2\pi$$，与 3.6 节算得的 $$2\pi$$ 相符）。

### 经典题 3：闭 $$\wedge$$ 闭、恰当 $$\wedge$$ 闭

**题。** 设 $$\alpha\in\Omega^p(M)$$、$$\beta\in\Omega^q(M)$$ 都闭。

(i) 证明 $$\alpha\wedge\beta$$ 闭。
(ii) 若 $$\alpha$$ 恰当、$$\beta$$ 闭，证明 $$\alpha\wedge\beta$$ 恰当。
(iii) 举例说明：两个闭形式的楔积**不一定**恰当。

**考点与位置。** 检验定义与分次莱布尼茨规则（第 14 章定理 3.17）；(iii) 是"$$H^*$$ 上有乘法"这一事实的第一个读数（第 70 章会把它讲成 cup 积）。

**解。**

**(i)** 由分次莱布尼茨规则（第 14 章定理 3.17 第 3 条）

$$d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^{p}\alpha\wedge d\beta=0\wedge\beta+(-1)^{p}\alpha\wedge0=0 .$$

**(ii)** 设 $$\alpha=d\gamma$$，$$\gamma\in\Omega^{p-1}(M)$$。则

$$d(\gamma\wedge\beta)=d\gamma\wedge\beta+(-1)^{p-1}\gamma\wedge d\beta=\alpha\wedge\beta+0=\alpha\wedge\beta,$$

最后一步用了 $$\beta$$ 闭。故 $$\alpha\wedge\beta=d(\gamma\wedge\beta)$$ 恰当。（这个计算顺便说明：恰当 $$\wedge$$ 恰当也恰当；而"闭 $$\wedge$$ 恰当"也恰当。）

**(iii)** 取 $$M=T^2=\mathbb{R}^2/\mathbb{Z}^2$$（环面），$$\alpha=d\theta_1$$、$$\beta=d\theta_2$$，其中 $$\theta_1,\theta_2$$ 是两个角坐标（局部定义，$$\alpha,\beta$$ 整体良定义）。两者都闭（$$d^2=0$$）。而

$$\int_{T^2}\alpha\wedge\beta=\int_0^1\!\!\int_0^1 d\theta_1\wedge d\theta_2=1\ne0 .$$

若 $$\alpha\wedge\beta$$ 恰当，即 $$\alpha\wedge\beta=d\eta$$（$$\eta\in\Omega^1(T^2)$$），则用 Stokes 与 $$\partial T^2=\varnothing$$

$$\int_{T^2}\alpha\wedge\beta=\int_{T^2}d\eta=\int_{\partial T^2}\eta=0,$$

矛盾。所以 $$\alpha\wedge\beta$$ 闭而不恰当，$$[\alpha\wedge\beta]\ne0\in H^2_{dR}(T^2)$$。

**附注**：这两条合起来正是 $$H^\bullet_{dR}(M)=\bigoplus_kH^k_{dR}(M)$$ 成为分次代数的原因：楔积在商的层面仍良定义（(i)(ii) 保证换代表元不改变结果），于是上同调不只携带"洞的个数"，还携带"洞之间如何相乘"。这是上同调比同调更强的地方（第 20 章）。

### 经典题 4：用上同调证明 Brouwer 不动点定理（$$D^2$$ 版）

**题。** 用 de Rham 上同调证明：每个连续映射 $$f:D^2\to D^2$$（$$D^2=\lbrace x\in\mathbb{R}^2:\lvert x\rvert\le1\rbrace$$）都有不动点。

**考点与位置。** 这是反变性（3.7 节）的最经典应用：整个证明只有一行线性代数，但那一行起作用的前提是"上同调反变"。它也是第 16 章"用代数不变量否定几何存在性"这一纲领的又一次实践。

**证明。** 分三步。

**第一步（反设并造出收缩）。** 反设 $$f$$ 无不动点，即对一切 $$x\in D^2$$ 有 $$f(x)\ne x$$。定义 $$r(x)$$ 为：从 $$f(x)$$ 出发经过 $$x$$ 的射线与圆周 $$S^1=\partial D^2$$ 的交点。写成参数式：$$r(x)=f(x)+t(x)\big(x-f(x)\big)$$，其中 $$t(x)\ge0$$ 取为使 $$\lvert r(x)\rvert=1$$ 的那个解。

先看 $$t(x)$$ 存在且 $$t(x)\ge0$$：条件 $$\lvert f(x)+t(x-f(x))\rvert^2=1$$ 是 $$t$$ 的二次方程

$$\lvert x-f(x)\rvert^2t^2+2\langle f(x),x-f(x)\rangle t+\lvert f(x)\rvert^2-1=0 .$$

（$$x\ne f(x)$$，故二次项系数非零。）在 $$t=0$$ 处左边 $$=\lvert f(x)\rvert^2-1\le0$$，而 $$t\to+\infty$$ 时左边 $$\to+\infty$$，故该二次方程必有一个 $$\ge0$$ 的实根；取 $$t(x)$$ 为"连续变化的那个非负根"（根可由求根公式连续写出，且在判别式为零处两个根重合，不产生跳跃）。于是 $$r:D^2\to S^1$$ 连续。

再看关键性质：若 $$x\in S^1$$，则 $$\lvert x\rvert=1$$，取 $$t(x)=0$$ 即满足方程，故

$$r(x)=f(x)+0\cdot\big(x-f(x)\big)=x,\qquad\text{即 }r\circ i=\mathrm{id}_{S^1},$$

其中 $$i:S^1\hookrightarrow D^2$$ 是包含映射。也就是说：$$f$$ 若没有不动点，就能造出一个从圆盘到圆周的**收缩 (retraction)** $$r$$。

**第二步（上同调上的推论）。** 由推论 3.11（反变性），$$r\circ i=\mathrm{id}_{S^1}$$ 给出

$$i^*\circ r^*=(\mathrm{id}_{S^1})^*=\mathrm{id}_{H^1(S^1)} .$$

**第三步（矛盾）。** 取入口题里的 $$\omega=\frac{-y\,dx+x\,dy}{x^2+y^2}$$ 于 $$S^1$$ 上（它是 $$S^1$$ 上的光滑 1-形式）。$$D^2$$ 可缩，由推论 3.13 得 $$H^1_{dR}(D^2)=0$$，故对一切 $$\eta\in H^1_{dR}(S^1)$$ 有 $$r^*\eta=0$$（因为 $$r^*$$ 的余定义域是 $$H^1_{dR}(D^2)=0$$），特别地

$$i^*\big(r^*[\omega]\big)=i^*(0)=0 .$$

但另一方面，由第二步

$$i^*\big(r^*[\omega]\big)=\mathrm{id}\big([\omega]\big)=[\omega] .$$

而 3.6 节已算出 $$\int_{S^1}\omega=2\pi\ne0$$，若 $$\omega$$ 恰当则积分必为 0（Stokes），故 $$[\omega]\ne0$$。矛盾。

所以反设不成立，$$f$$ 必有不动点。$$\blacksquare$$

**这个证明的"一行"在哪里。** 全部内容就是 $$i^*\circ r^*=\mathrm{id}$$ 与 $$r^*=0$$ 不能同时成立。它之所以成立，是因为 $$H^1$$ **反变**：$$i:S^1\to D^2$$ 把 $$H^1$$ 从 $$D^2$$ 拉回 $$S^1$$，而 $$D^2$$ 的 $$H^1$$ 是零，拉回来的自然也是零。**如果上同调像同调那样协变，"拉回"就无从谈起，整个论证无法启动。**

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 判定下列形式是闭？恰当？（要给出理由或反例）

(i) $$\mathbb{R}^2$$ 上：$$\omega=(2xy+y^3)\,dx+(x^2+3xy^2)\,dy$$；
(ii) $$\mathbb{R}^2$$ 上：$$\omega=y\,dx-x\,dy$$；
(iii) $$\mathbb{R}^3$$ 上：$$\omega=x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy$$。

**基2.** 计算 $$H^0_{dR}(S^1)$$ 与 $$H^1_{dR}(S^1)$$ 的维数，并各给出一个非零元素的代表形式。（提示：上界用"积分为零即有原函数"。）

**基3.** 设 $$U\subseteq\mathbb{R}^n$$ 开，$$\omega=\sum_{i=1}^nf_i\,dx^i$$。证明：$$\omega$$ 闭 $$\iff$$ $$\partial_if_j=\partial_jf_i$$ 对一切 $$i,j$$ 成立。并说明当 $$n=3$$ 时这恰好是"向量场的旋度为零"。

**基4.** 设 $$\gamma_0,\gamma_1:[0,1]\to M$$ 是两条端点相同的光滑道路，且存在固定端点的光滑同伦 $$H:[0,1]^2\to M$$（$$H(s,0)=\gamma_0(s)$$，$$H(s,1)=\gamma_1(s)$$，$$H(0,t)=H(1,t)=x_0$$ 为常数）。证明：对任意闭 1-形式 $$\omega$$，

$$\int_{\gamma_0}\omega=\int_{\gamma_1}\omega .$$

### 竞赛（本课目标难度）

**竞1.** 证明 $$H^1_{dR}\big(\mathbb{R}^2\setminus\{0\}\big)\cong\mathbb{R}$$，且它由入口题的 $$\omega$$ 生成。

**竞2.** 证明 $$H^1_{dR}\big(\mathbb{R}^2\setminus\{0,1\}\big)\cong\mathbb{R}^2$$：构造两个闭 1-形式，证明它们线性无关，并给出维数不超过 2 的论证。

**竞3.** 计算环面 $$T^2=\mathbb{R}^2/\mathbb{Z}^2$$ 的 $$H^1_{dR}$$ 与 $$H^2_{dR}$$，并算出 $$\chi(T^2)$$。

**竞4.** 设 $$F:S^1\to S^1$$ 光滑，$$\omega=\dfrac{-y\,dx+x\,dy}{x^2+y^2}$$，定义 $$F$$ 的**度数 (degree)** 为 $$\deg(F)=\dfrac{1}{2\pi}\displaystyle\int_{S^1}F^*\omega$$。证明

$$F^*[\omega]=\deg(F)\cdot[\omega]\qquad\text{于 }H^1_{dR}(S^1).$$

### 研究（通向下一章）

**研1.** 设 $$M$$ 是紧致、定向、连通的 $$n$$ 维光滑流形。

(i) 证明 $$\displaystyle\int_M:\Omega^n(M)\to\mathbb{R}$$ 在恰当形式上取零，因而下降为线性泛函 $$\displaystyle\int_M:H^n_{dR}(M)\to\mathbb{R}$$。
(ii) 用单位分解构造一个 $$\theta\in\Omega^n(M)$$ 使 $$\displaystyle\int_M\theta=1$$。
(iii) 由此说明 $$H^n_{dR}(M)\ne0$$，并解释为什么"$$H^n_{dR}(M)\cong\mathbb{R}$$"这句话正是 de Rham 定理的一个特例。

**研2.** 设 $$(C^\bullet,\delta)$$ 是域 $$\mathbb{R}$$ 上的**上链复形**：$$C^k$$ 是 $$\mathbb{R}$$-向量空间，$$\delta_k:C^k\to C^{k+1}$$ 线性且 $$\delta_{k+1}\delta_k=0$$。定义 $$H^k(C)=\ker\delta_k/\operatorname{im}\delta_{k-1}$$。

(i) 设 $$\varphi:C^\bullet\to D^\bullet$$ 是**上链映射**（$$\delta^D\varphi=\varphi\delta^C$$）。证明它诱导线性映射 $$H^k(\varphi):H^k(C)\to H^k(D)$$，且 $$H^k(\mathrm{id})=\mathrm{id}$$、$$H^k(\psi\varphi)=H^k(\psi)H^k(\varphi)$$。
(ii) 设 $$\varphi,\psi:C^\bullet\to D^\bullet$$ 是上链映射，且存在线性映射 $$h^k:C^k\to D^{k-1}$$ 使
$$\varphi-\psi=\delta^D h+h\,\delta^C .$$
证明 $$H^k(\varphi)=H^k(\psi)$$。
(iii) 说明本章定理 3.12 只是 (ii) 的一个特例，并指出 (ii) 在后续哪一章会以更一般的面貌回来。

### 解答 (Solutions)

**解 基1.**

**(i)** 记 $$\omega=P\,dx+Q\,dy$$，$$P=2xy+y^3$$，$$Q=x^2+3xy^2$$。在平面上 $$d\omega=(\partial_xQ-\partial_yP)\,dx\wedge dy$$，而

$$\partial_xQ=2x+3y^2,\qquad \partial_yP=2x+3y^2 ,$$

两者相等，故 $$d\omega=0$$，$$\omega$$ 闭。又 $$\mathbb{R}^2$$ 可缩，由推论 3.13 得 $$H^1_{dR}(\mathbb{R}^2)=0$$，故 $$\omega$$ 恰当。把原函数直接写出来作验证：

$$f(x,y)=x^2y+xy^3+C,\qquad \partial_xf=2xy+y^3=P,\quad \partial_yf=x^2+3xy^2=Q .$$

$$\omega=df$$。

**(ii)** $$P=y$$，$$Q=-x$$。$$\partial_xQ=-1$$，$$\partial_yP=1$$，二者不等，故 $$d\omega=-2\,dx\wedge dy\ne0$$，$$\omega$$ **不闭**，从而（由命题 3.3 的逆否）**不恰当**。

*这道小题是一个陷阱*：$$y\,dx-x\,dy$$ 与入口题的分子只差一个符号与分母，但少了分母 $$x^2+y^2$$ 之后它就不再闭了。可见"闭"是一个会碎的性质，入口题的 $$\omega$$ 闭是靠分母精确配平出来的。

**(iii)** 对 $$\omega=P\,dy\wedge dz+Q\,dz\wedge dx+R\,dx\wedge dy$$（$$P=x$$，$$Q=y$$，$$R=z$$），

$$d\omega=(\partial_xP+\partial_yQ+\partial_zR)\,dx\wedge dy\wedge dz=(1+1+1)\,dx\wedge dy\wedge dz=3\,dx\wedge dy\wedge dz\ne0 .$$

故 $$\omega$$ **不闭**，也不恰当。与经典题 2 的 $$\omega_2$$ 对照：那里把同一个形式除以 $$r^3$$，三项的贡献恰好抵消，闭性成立。**"乘以一个径向函数"能否修好闭性，是一个精确的计算，不是"看起来差不多"。**

**解 基2.**

**$$H^0$$：** $$S^1$$ 连通，由推论 3.6，$$H^0_{dR}(S^1)=\mathbb{R}$$，非零元素是常值函数（如 $$f\equiv1$$）所在的上同调类。

**$$H^1$$：** 取局部角坐标 $$\theta$$，则 $$\omega=d\theta$$ 在每张坐标卡上成立（入口题已算），故整体上 $$\omega$$ 是 $$S^1$$ 上的光滑 1-形式且 $$d\omega=d(d\theta)=0$$，即 $$\omega$$ 闭。而 3.6 节算出 $$\int_{S^1}\omega=2\pi\ne0$$；若 $$\omega$$ 恰当（$$\omega=df$$），则由 Stokes（$$\partial S^1=\varnothing$$）$$\int_{S^1}\omega=\int_{S^1}df=\int_{\partial S^1}f=0$$，矛盾。故

$$[\omega]\ne0,\qquad \dim H^1_{dR}(S^1)\ge1 .$$

**上界：** 设 $$\alpha\in\Omega^1(S^1)$$ 闭。令

$$\lambda=\frac{1}{2\pi}\int_{S^1}\alpha,\qquad \beta=\alpha-\lambda\omega .$$

则 $$\int_{S^1}\beta=\int_{S^1}\alpha-\lambda\int_{S^1}\omega=0$$。断言：**$$\int_{S^1}$$ 上积分为零的闭 1-形式必恰当。** 证明如下。

固定基点 $$x_0=(1,0)$$。对每个 $$x\in S^1$$，任取一条从 $$x_0$$ 到 $$x$$ 的分段光滑道路 $$\gamma_x$$，定义

$$f(x)=\int_{\gamma_x}\beta .$$

需要说明它与道路选取无关。取两条这样的道路 $$\gamma,\gamma'$$，拼成闭路 $$c=\gamma'*\bar\gamma$$（$$\bar\gamma$$ 为 $$\gamma$$ 反向）。把 $$c$$ 的绕数记为 $$n\in\mathbb{Z}$$：由第 16 章（$$\pi_1(S^1)\cong\mathbb{Z}$$，基本群由绕数给出）与第 20 章（Hurewicz 定理，$$H_1(S^1;\mathbb{Z})\cong\mathbb{Z}$$），$$[c]=n[\gamma_{S^1}]$$，其中 $$\gamma_{S^1}$$ 是绕行一周的闭路。由命题 3.15（配对只依赖同调类）

$$\int_c\beta=n\int_{S^1}\beta=0 .$$

所以 $$\int_\gamma\beta=\int_{\gamma'}\beta$$，$$f$$ 良定义且光滑（局部地 $$f$$ 就是 $$\beta$$ 沿坐标积分，$$\partial_\theta f=\beta_\theta$$），于是 $$df=\beta$$，$$\beta$$ 恰当。

从而 $$\alpha=df+\lambda\omega$$，即 $$[\alpha]=\lambda[\omega]$$。**每一个上同调类都是 $$[\omega]$$ 的倍数**，故 $$\dim H^1_{dR}(S^1)\le1$$。结合下界：

$$H^0_{dR}(S^1)\cong\mathbb{R},\qquad H^1_{dR}(S^1)\cong\mathbb{R},\qquad \chi(S^1)=1-1=0 .$$

**解 基3.**

设 $$\omega=\sum_if_i\,dx^i$$。由 $$d$$ 在 $$\Omega^0$$ 上的定义与分次莱布尼茨规则（第 14 章 3.17），

$$d\omega=\sum_i df_i\wedge dx^i=\sum_{i,j}\partial_jf_i\,dx^j\wedge dx^i .$$

把求和按无序对 $$i<j$$ 归并。对固定的一对 $$i<j$$，来自 $$(j,i)$$ 与 $$(i,j)$$ 的两项是

$$\partial_jf_i\,dx^j\wedge dx^i+\partial_if_j\,dx^i\wedge dx^j=\big(\partial_if_j-\partial_jf_i\big)\,dx^i\wedge dx^j,$$

（等式用了 $$dx^j\wedge dx^i=-dx^i\wedge dx^j$$）。$$i=j$$ 的项含 $$dx^i\wedge dx^i=0$$（第 14 章引理 3.5）。而 $$\lbrace dx^i\wedge dx^j\rbrace_{i<j}$$ 在每点线性无关（第 14 章 3.3 节的维数讨论），故

$$d\omega=0\iff \partial_if_j-\partial_jf_i=0\ \text{对一切 }i<j\iff \partial_if_j=\partial_jf_i\ \text{对一切 }i,j .$$

**与旋度的关系：** $$n=3$$ 时，把 $$\omega$$ 对应到向量场 $$\vec F=(f_1,f_2,f_3)$$。由第 14 章 3.9 节的对齐表，$$d\omega$$ 是 2-形式

$$d\omega=(\partial_2f_3-\partial_3f_2)\,dx^2\wedge dx^3+(\partial_3f_1-\partial_1f_3)\,dx^3\wedge dx^1+(\partial_1f_2-\partial_2f_1)\,dx^1\wedge dx^2,$$

其三个系数正是 $$\operatorname{curl}\vec F$$ 的三个分量。于是上面的判据读作：$$\omega$$ 闭 $$\iff\operatorname{curl}\vec F=\vec0$$——"无旋"。

**解 基4.**

把 $$\gamma_0,\gamma_1$$ 看成 1-链，把 $$H$$ 在链层面推前，得 2-链 $$c=H_\#\big([0,1]^2\big)$$（第 18 章：推前把单形复合上映射）。由第 18 章的边界公式，正方形 $$[0,1]^2$$ 的边界是四条边按定向相加；两条竖直边定向相反而相消，两条水平边分别映到 $$\gamma_0$$、$$\gamma_1$$，而剩余两条边（$$s=0$$ 与 $$s=1$$）映到常值道路 $$x_0$$。常值道路的切向量恒为零，故 $$H^*\omega$$ 在它们上面为零，积分为零。于是作为 1-链

$$\partial c=\gamma_1-\gamma_0 .$$

对 $$c$$ 用 Stokes 定理（第 26 章），再用 $$d\omega=0$$：

$$\int_{\gamma_1}\omega-\int_{\gamma_0}\omega=\int_{\partial c}\omega=\int_c d\omega=\int_c0=0 .$$

即 $$\int_{\gamma_0}\omega=\int_{\gamma_1}\omega$$。$$\blacksquare$$

**这条引理的用处：** 它说明"闭形式沿道路的积分只依赖道路的同伦类"。入口题的论证是它的一个极简特例：取 $$\gamma_1=\gamma$$（绕原点一周）与 $$\gamma_0=\text{常值道路}$$（同伦于 $$\gamma$$ 的对手不存在，故矛盾只来自 $$\int_\gamma\omega\ne0$$ 本身）；而 $$H^1_{dR}(M)=0$$ 的几何含义正是"任何两条同端点的道路都能互相变形"，于是一切闭 1-形式都有原函数。

**解 竞1.**

**下界（$$[\omega]\ne0$$）：** 已在 3.6 节完整给出：$$d\omega=0$$，且 $$\int_{S^1}\omega=2\pi\ne0$$，若 $$\omega=df$$ 则沿闭曲线积分必为零，矛盾。

**上界（每个闭 1-形式都是 $$\lambda\omega+df$$）：** 设 $$\alpha\in\Omega^1\big(\mathbb{R}^2\setminus\{0\}\big)$$ 闭。令 $$\lambda=\frac{1}{2\pi}\int_{S^1}\alpha$$，$$\beta=\alpha-\lambda\omega$$，则 $$\int_{S^1}\beta=0$$。

固定基点 $$x_0=(1,0)$$，对 $$x\in M$$ 取道路 $$\gamma_x$$ 并定义

$$f(x)=\int_{\gamma_x}\beta .$$

**与道路选取无关：** 取两条道路拼成闭路 $$c$$。由第 16 章，$$\pi_1\big(\mathbb{R}^2\setminus\{0\}\big)\cong\mathbb{Z}$$（挖掉一个点的平面与 $$S^1$$ 同伦等价，基本群由绕数给出：绕原点 $$n$$ 周的道路代表 $$n$$）；由第 20 章 Hurewicz，$$H_1\big(M;\mathbb{Z}\big)\cong\mathbb{Z}$$，且 $$[c]=n[S^1]$$。于是由命题 3.15

$$\int_c\beta=n\int_{S^1}\beta=0 .$$

**$$f$$ 光滑且 $$df=\beta$$：** 在任一不绕原点的开集上，$$\beta$$ 有原函数，$$f$$ 与之相差常数（由上面的一致性），故光滑；局部取坐标算偏导，$$\partial_if=\beta_i$$，即 $$df=\beta$$。

于是 $$\alpha=df+\lambda\omega$$，$$[\alpha]=\lambda[\omega]$$，$$\dim H^1_{dR}(M)\le1$$。结合下界，

$$H^1_{dR}\big(\mathbb{R}^2\setminus\{0\}\big)\cong\mathbb{R},\qquad\text{生成元 }[\omega].$$

**关键 leap：** 全部难点在一处——把"沿闭路积分为零"升级为"有原函数"。这一步的桥是 **$$\int$$ 只依赖同调类（命题 3.15）**，从而"绕数为 $$n$$ 的闭路"这个几何事实被翻译成了"积分为 $$n$$ 倍"。缺了命题 3.15，就只剩下一堆看起来对、但没法拼起来的局部原函数。

**解 竞2.**

**构造两个闭形式。** 分别以 $$0$$ 与 $$1$$ 为"洞"，把入口题的 $$\omega$$ 平移过去：

$$\omega_0=\frac{-y\,dx+x\,dy}{x^2+y^2},\qquad
\omega_1=\frac{-y\,d(x-1)+(x-1)\,dy}{(x-1)^2+y^2}=\frac{-y\,dx+(x-1)\,dy}{(x-1)^2+y^2}.$$

两者都在 $$M=\mathbb{R}^2\setminus\{0,1\}$$ 上有定义且光滑。$$\omega_1$$ 是 $$\omega_0$$ 沿平移 $$(x,y)\mapsto(x-1,y)$$ 的拉回，而拉回与 $$d$$ 交换（第 14 章定理 3.16），故 $$d\omega_1=0$$；$$d\omega_0=0$$ 已在 3.6 节算出。两者都闭。

**线性无关。** 取两条闭路：$$\gamma_0$$ 为绕 $$0$$ 的单位圆（例如圆心在 $$0$$、半径为 $$1/2$$），$$\gamma_1$$ 为绕 $$1$$ 的单位圆（圆心在 $$1$$、半径 $$1/2$$）。它们分别避开另一个洞，且

$$\int_{\gamma_0}\omega_0=2\pi,\qquad\int_{\gamma_0}\omega_1=0,\qquad
\int_{\gamma_1}\omega_0=0,\qquad\int_{\gamma_1}\omega_1=2\pi .$$

（$$\omega_1$$ 沿 $$\gamma_0$$ 的积分：$$\gamma_0$$ 的像不包含 $$1$$，而 $$\omega_1$$ 在该圆盘状区域上有单值原函数（极角 $$\theta_1$$ 在那里单值），故积分为零；对称地得另一条。）设 $$\lambda_0\omega_0+\lambda_1\omega_1=df$$（即上同调类为零），则由命题 3.15 得 $$2\pi\lambda_0=0$$、$$2\pi\lambda_1=0$$，故 $$\lambda_0=\lambda_1=0$$。于是

$$\dim H^1_{dR}(M)\ge2 .$$

**上界。** 设 $$\alpha$$ 闭，令 $$\lambda_i=\frac{1}{2\pi}\int_{\gamma_i}\alpha$$，$$\beta=\alpha-\lambda_0\omega_0-\lambda_1\omega_1$$，则 $$\beta$$ 沿两条生成闭路的积分为零。由第 16 章 van Kampen 定理，$$\pi_1\big(\mathbb{R}^2\setminus\{0,1\}\big)$$ 是自由群 $$\mathbb{F}_2$$（两个生成元分别绕两个洞，$$\mathbb{R}^2\setminus\{0,1\}$$ 同伦等价于两个圆的楔和）；由第 20 章 Hurewicz，$$H_1(M;\mathbb{Z})\cong\mathbb{Z}^2$$，由 $$[\gamma_0],[\gamma_1]$$ 生成。于是任一闭路 $$c$$ 满足 $$[c]=m[\gamma_0]+n[\gamma_1]$$，由命题 3.15

$$\int_c\beta=m\cdot0+n\cdot0=0 .$$

与竞1 中完全相同的论证：沿道路积分 $$\int_{\gamma_x}\beta$$ 与道路选取无关，给出光滑 $$f$$ 使 $$df=\beta$$。故 $$[\alpha]=\lambda_0[\omega_0]+\lambda_1[\omega_1]$$，$$\dim H^1_{dR}(M)\le2$$。结合下界：

$$H^1_{dR}\big(\mathbb{R}^2\setminus\{0,1\}\big)\cong\mathbb{R}^2,\qquad
H^0_{dR}\cong\mathbb{R}\ (\text{连通}),\qquad H^k_{dR}=0\ (k\ge2).$$

**关键 leap：** 找到一个"上界论证"，把无限的 $$\Omega^1$$ 压到有限维。这个论证的形状是通用的：**只要能说清 $$H_1$$ 由哪几条闭路生成，"配零周期"就能把每个闭形式化成生成元的线性组合加一个恰当形式。** 换句话说，同调负责"上界"，形式负责"下界"，而命题 3.15 是两者之间的换算率。

**解 竞3.**

记 $$\theta_1,\theta_2$$ 为 $$T^2$$ 上的两个角坐标（各自局部单值），$$\alpha_i=d\theta_i$$（整体良定义、闭），$$\mu=d\theta_1\wedge d\theta_2$$。

**$$H^1(T^2)\cong\mathbb{R}^2$$。** 取 $$\gamma_i$$ 为沿第 $$i$$ 个因子绕行一周的闭路，则

$$\int_{\gamma_1}\alpha_1=\int_{\gamma_2}\alpha_2=1,\qquad \int_{\gamma_1}\alpha_2=\int_{\gamma_2}\alpha_1=0 .$$

故 $$[\alpha_1],[\alpha_2]$$ 线性无关（同上）：$$\dim H^1\ge2$$。上界：由第 16 章 van Kampen，$$\pi_1(T^2)\cong\mathbb{Z}^2=\langle\gamma_1,\gamma_2\rangle$$，Hurewicz 给 $$H_1(T^2;\mathbb{Z})\cong\mathbb{Z}^2$$，再重复"配零周期 ⟹ 有原函数"的论证（同竞1、竞2），得 $$\dim H^1\le2$$。于是

$$H^1_{dR}(T^2)\cong\mathbb{R}^2,\qquad\text{生成元 }[d\theta_1],[d\theta_2].$$

**$$H^2(T^2)\cong\mathbb{R}$$。** *下界：* $$\mu$$ 是 2-形式，自动闭（$$T^2$$ 上没有 3-形式，$$d\mu=0$$ 平凡成立）。而

$$\int_{T^2}\mu=\int_0^1\!\!\int_0^1d\theta_1\wedge d\theta_2=1\ne0,$$

若 $$\mu=d\eta$$ 则由 Stokes 与 $$\partial T^2=\varnothing$$ 得积分为 0，矛盾。故 $$[\mu]\ne0$$。

*上界：* $$T^2$$ 上的任意 2-形式都可写成 $$\beta=f\,d\theta_1\wedge d\theta_2$$，$$f$$ 是双周期光滑函数。设 $$\int_{T^2}\beta=0$$，下面把 $$\beta$$ 写成恰当形式。

把 $$f$$ 分解为"对 $$\theta_1$$ 均值为零的部分"加"只依赖 $$\theta_2$$ 的部分"：

$$f(\theta_1,\theta_2)=\underbrace{f(\theta_1,\theta_2)-\int_0^1f(s,\theta_2)\,ds}_{\displaystyle g(\theta_1,\theta_2)}+\underbrace{\int_0^1f(s,\theta_2)\,ds}_{\displaystyle \varphi(\theta_2)} .$$

对每个固定 $$\theta_2$$，$$g(\cdot,\theta_2)$$ 的均值为零，于是

$$h(\theta_1,\theta_2)=\int_0^{\theta_1}g(s,\theta_2)\,ds$$

是双周期光滑函数（对 $$\theta_1$$ 的周期性由均值为零保证，对 $$\theta_2$$ 的周期性由 $$g$$ 的周期性保证），且 $$\partial_{\theta_1}h=g$$，故 $$g\,d\theta_1\wedge d\theta_2=d\big(h\,d\theta_2\big)$$。又

$$\int_{T^2}\beta=\int_0^1\!\!\int_0^1f\,d\theta_1d\theta_2=\int_0^1\varphi(\theta_2)\,d\theta_2=0,$$

（第二步用了 $$\int g\,d\theta_1=0$$），故 $$\varphi$$ 的均值为零，$$F(\theta_2)=\int_0^{\theta_2}\varphi(s)\,ds$$ 是周期函数，且 $$-F'=\varphi$$ 给出

$$\varphi(\theta_2)\,d\theta_1\wedge d\theta_2=d\big(-F\,d\theta_1\big)$$

（验证：$$d(-F\,d\theta_1)=-F'd\theta_2\wedge d\theta_1=F'd\theta_1\wedge d\theta_2$$）。于是 $$\beta=d\big(h\,d\theta_2-F\,d\theta_1\big)$$ 恰当。所以 $$[\beta]\mapsto\int_{T^2}\beta$$ 是单射；又它是满射（$$[\mu]\mapsto1$$），故

$$H^2_{dR}(T^2)\cong\mathbb{R},\qquad\text{由 }[d\theta_1\wedge d\theta_2]\text{ 生成}.$$

**Betti 数与欧拉示性数：** $$b_0=1,b_1=2,b_2=1$$，

$$\chi(T^2)=1-2+1=0 .$$

这与第 18 章的胞腔计数一致（一个 0-胞腔、两个 1-胞腔、一个 2-胞腔：$$1-2+1=0$$），也与经典题 3(iii) 的结论 $$[\alpha\wedge\beta]\ne0$$ 一致。

**解 竞4.**

**思路：** $$H^1_{dR}(S^1)$$ 是一维的（基2），所以 $$F^*$$ 这个线性映射必然是"乘一个数"。把那个数算出来，它只能是 $$\deg(F)$$；算法就是"配上 $$[S^1]$$ 取积分"。

**证明。** 由基2，$$\dim H^1_{dR}(S^1)=1$$ 且 $$[\omega]$$ 是基，故存在 $$c\in\mathbb{R}$$ 使

$$F^*[\omega]=c\,[\omega] .$$

用命题 3.15 的配对（取 $$[S^1]\in H_1(S^1;\mathbb{R})$$ 为绕行一周的闭链）作用两边：

$$\big\langle[S^1],F^*[\omega]\big\rangle=c\,\big\langle[S^1],[\omega]\big\rangle .$$

右边是 $$c\int_{S^1}\omega=2\pi c$$。左边按定义是 $$\int_{S^1}F^*\omega=2\pi\deg(F)$$。于是 $$c=\deg(F)$$，即

$$F^*[\omega]=\deg(F)\,[\omega] . \qquad\blacksquare$$

**附注（$$\deg(F)$$ 必为整数）。** 由第 16 章与第 20 章，$$F$$ 诱导 $$H_1(S^1;\mathbb{Z})\to H_1(S^1;\mathbb{Z})$$ 是乘以某个整数 $$d$$（因为 $$H_1(S^1;\mathbb{Z})\cong\mathbb{Z}$$，自同态都是 $$\times d$$）；而配对与推前相容（$$\langle F_\#[c],\omega\rangle=\langle c,F^*\omega\rangle$$，这是拉回定义与积分换元的直接推论），故 $$\deg(F)=d\in\mathbb{Z}$$。**这个整数就是"$$F$$ 把圆绕了几圈"**——上同调与基本群在这里给出同一个答案。

**解 研1.**

**(i)** 设 $$\omega=d\eta$$，$$\eta\in\Omega^{n-1}(M)$$。$$M$$ 是紧流形，$$\partial M=\varnothing$$；由 Stokes 定理（第 26 章）

$$\int_M\omega=\int_Md\eta=\int_{\partial M}\eta=0 .$$

故 $$\int_M$$ 在 $$B^n(M)$$ 上取零。又 $$\int_M$$ 线性，若 $$\omega'=\omega+d\eta$$ 则 $$\int_M\omega'=\int_M\omega$$，即 $$\int_M$$ 只依赖 $$[\omega]$$，下降为线性泛函

$$\int_M:H^n_{dR}(M)\longrightarrow\mathbb{R},\qquad[\omega]\longmapsto\int_M\omega .$$

**(ii)** 取一个有限的"定向坐标卡"覆盖：因 $$M$$ 紧，存在有限个坐标卡 $$(U_1,\varphi_1),\dots,(U_N,\varphi_N)$$，每个 $$U_i$$ 落在某个保持定向的坐标卡内。取从属于该覆盖的光滑单位分解 $$\lbrace\rho_i\rbrace$$（$$\rho_i\ge0$$，$$\operatorname{supp}\rho_i\subseteq U_i$$，$$\sum_i\rho_i\equiv1$$）。

在每个 $$U_i$$ 上取 $$\eta_i=\rho_i\,dx^1\wedge\cdots\wedge dx^n$$（$$x^j$$ 为该卡的坐标，按 $$\varphi_i$$ 拉回到 $$M$$ 上；因 $$\varphi_i$$ 保定向，$$\int_{U_i}\eta_i=\int\rho_i\,dx>0$$，其中第二个积分是 $$\mathbb{R}^n$$ 中紧支集上的通常积分）。令

$$\theta=\frac{\sum_{i=1}^N\eta_i}{\sum_{i=1}^N\int_M\eta_i}.$$

分母是有限个正数之和，严格为正。由 $$\int_M$$ 的线性，

$$\int_M\theta=\frac{\sum_i\int_M\eta_i}{\sum_i\int_M\eta_i}=1 .$$

于是 $$\theta\in\Omega^n(M)$$、$$\int_M\theta=1$$，故 $$\int_M:H^n_{dR}(M)\to\mathbb{R}$$ 是满射。

**(iii)** 由 (i)(ii)，$$\int_M$$ 是满射；而 de Rham 定理（定理 3.16）说明

$$H^n_{dR}(M)\cong\big(H_n(M;\mathbb{R})\big)^* ,$$

且对紧致定向连通 $$n$$ 维流形，$$H_n(M;\mathbb{R})\cong\mathbb{R}$$（由第 20 章的基本类 $$[M]$$ 生成），故右端是 $$\mathbb{R}$$。于是 $$[\theta]$$ 非零，$$H^n_{dR}(M)\cong\mathbb{R}$$，且这个同构正是"积分"给出的那一个。把 $$\theta$$ 沿 $$M$$ 摊开看，它没有零点意义上的"洞"可钻，却依然给出非零的上同调类——**最高次上同调不是靠"绕洞"被探测到的，而是靠"整块体积"**。

**接到下一章。** (i) 里那个"$$\int_M$$ 只看上同调类"的现象，说到底是"$$\omega$$ 与 $$[\omega]$$ 之间隔着 $$B^n$$，而 $$\int_M$$ 恰好在 $$B^n$$ 上消失"。这套话说完之后，我们会自然想问：如果不是"$$\int$$ 在某个子空间上消失"，而是"两个空间之间有一个配上就非退化的规则"，会发生什么？第 30 章开始研究 **Hilbert 空间与内积结构**：那里把本课一直在使用的**配对**升级成**内积**，于是 $$H_k$$ 与 $$H^k$$ 的关系变成 Riesz 表示定理下的一枚硬币两面，而"正交分解"这类操作也才有意义（后续 Hodge 理论里，每个上同调类会有一个唯一的"调和"代表形式）。

**解 研2.**

**(i)** 设 $$\varphi:C^\bullet\to D^\bullet$$ 满足 $$\delta^D\varphi=\varphi\delta^C$$。若 $$z\in C^k$$ 且 $$\delta^Cz=0$$，则 $$\delta^D(\varphi z)=\varphi(\delta^Cz)=0$$，故 $$\varphi z\in\ker\delta^D_k$$。若又有 $$z'=z+\delta^Cw$$（$$w\in C^{k-1}$$），则

$$\varphi z'-\varphi z=\varphi\delta^Cw=\delta^D(\varphi w)\in\operatorname{im}\delta^D_{k-1},$$

故 $$\varphi z'$$ 与 $$\varphi z$$ 在 $$H^k(D)$$ 中同类。于是 $$H^k(\varphi):[z]\mapsto[\varphi z]$$ 良定义且线性。

函子性：$$H^k(\mathrm{id})[z]=[\mathrm{id}\,z]=[z]$$；$$H^k(\psi\varphi)[z]=[(\psi\varphi)z]=[\psi(\varphi z)]=H^k(\psi)\big([\varphi z]\big)=H^k(\psi)H^k(\varphi)[z]$$。

**(ii)** 设 $$\varphi-\psi=\delta^D h+h\delta^C$$，其中 $$h^k:C^k\to D^{k-1}$$。取 $$z\in C^k$$ 且 $$\delta^Cz=0$$。则

$$\varphi z-\psi z=\delta^D\big(h^kz\big)+h^{k+1}\big(\delta^Cz\big)=\delta^D\big(h^kz\big)\in\operatorname{im}\delta^D_{k-1},$$

故 $$[\varphi z]=[\psi z]$$，即 $$H^k(\varphi)=H^k(\psi)$$。$$\blacksquare$$

**(iii)** 本章定理 3.12 就是 (ii) 的实例：取

- $$C^\bullet=\Omega^\bullet(N)$$，$$\delta^C=d$$；$$D^\bullet=\Omega^\bullet(M)$$，$$\delta^D=d$$；
- $$\varphi=F_1^*$$，$$\psi=F_0^*$$；
- $$h\omega=\displaystyle\int_0^1j_s^*\big(\iota_{\partial_t}(H^*\omega)\big)\,ds$$（定理 3.12 的证明里构造的那个算子）。

于是 (ii) 立刻给出 $$F_1^*=F_0^*$$ 于上同调上——定理 3.12 的全部内容是纯代数的，几何只用来**造出**那个 $$h$$。

**这条线索的去向：** 第 70 章（同调代数：导出函子）会把"上链复形 + 上链映射 + 链同伦"这套语言推到一般形式。届时我们会看到：在同一链同伦类里的映射在导出函子上给出同一个结果，这正是消解的**链同伦等价唯一**，也是 $$\operatorname{Ext}$$ 与 $$\operatorname{Tor}$$ 良定义的根基。

**接到下一章。** (ii) 的证明只有一行，但它揭示了一件事：**两个空间（或两个复形）之间的"相等"，常常可以放宽成"相差一个恰当的东西"**；而一旦允许这种放宽，就需要一套配套的几何语言来度量"差距有多大、在哪些方向上为零"。本课的下一步不是继续放宽，而是反过来**加装结构**：第 30 章给这些空间装上**内积**，于是"差距"可以用长度与夹角来度量，"正交"可以定义，$$\ker$$ 与 $$\operatorname{im}$$ 之间会出现一个漂亮的补空间——这正是 Hodge 理论（每个上同调类有唯一调和代表元）的起点，也是卷三泛函分析的第一块砖。

## 七、Takeaway 与延伸 (Takeaways)

**1. 一句话定义，三句话解释。** $$H^k_{dR}(M)=\ker d_k/\operatorname{im}d_{k-1}$$：分子是闭形式，分母是恰当形式，商就是"闭而不恰当"的净信息。$$H^k_{dR}=0$$ 意味着该维数上没有洞；$$H^k_{dR}\ne0$$ 意味着存在局部能积分、全局积不出来的形式。**度量洞的多少，是把无限的函数空间压成有限维线性代数的过程。**

**2. Poincaré 引理的失效点是可以精确定位的。** 证明里唯一的关键是"区域能缩成一点"，所以失效点就是"缩不过去"：$$\mathbb{R}^2\setminus\{0\}$$ 缩不进原点。这不是模糊的"有洞所以不行"，而是一个可验证的机制——$$\phi_0$$ 不存在，同伦公式右边那一项就消不掉。记住这句话：**上同调为零是"可缩"的代数影子。**

**3. 反变性不是约定，是同调代数的事实。** 形式只能拉回（第 14 章"只拉不推"），所以 $$H^k$$ 反变；链能推前，所以 $$H_k$$ 协变；而 de Rham 定理说 $$H^k_{dR}\cong\operatorname{Hom}(H_k,\mathbb{R})$$，把这两件事锁在一起。经典题 4（Brouwer 不动点）是这条事实最干净的应用：整个证明就是 $$i^*\circ r^*=\mathrm{id}$$ 与 $$r^*=0$$ 的冲突。

**4. 第二条大暗线在本章闭合。** 第 18 章的 $$\partial^2=0$$ 与第 14 章的 $$d^2=0$$ 是同一台引擎的两个朝向；第 09–10 章的 $$H_k$$ 与本章的 $$H^k$$ 是同一台商机器的两个刻度方向；Stokes 定理（第 26 章）是两者之间的换算律（命题 3.15）。**同调数洞，上同调也用同一台机器数同一批洞，只是刻度盘反着转。** 这条线在第 70 章（同调代数：导出函子）会以完全一般的形式回来：任意函子的正合性缺陷都可以被同调群量化，而 $$\ker/\operatorname{im}$$ 就是"离正合有多远"的度量。

**5. 数字会合流。** $$\chi(M)=\sum_k(-1)^kb_k$$ 与第 18 章的胞腔计数一致；第 26 章的 Gauss–Bonnet 定理把它写成曲率的积分。上同调、胞腔、曲率、向量场零点，四条路通向同一个数。

**下一章的悬念（第 30 章：Hilbert 空间与内积结构）。** 本章用**配对** $$\langle c,\omega\rangle$$ 把同调与上同调绑在一起；配对是"双线性"的，但一个配对并不告诉你"两个向量有多接近"。卷三换一副眼镜：给向量空间装上**内积**，于是有长度、有正交、有正交投影。到那时，$$\ker d$$ 与 $$\operatorname{im}$$ 的差距将不再只是一个商空间，而是一个可以正交分解的几何结构——这是 Hodge 理论的入口，也是量子力学里"态与可观测量"这套语言的起点。**卷二到此结束；从下一章起，我们进入泛函分析。**

**延伸阅读。**

- R. Bott, L. Tu, *Differential Forms in Algebraic Topology*（GTM 82）：de Rham 定理与 Mayer–Vietoris、谱序列的正典参考。
- A. Hatcher, *Algebraic Topology*：奇异同调与上同调（第 20 章那条线的完整展开）、de Rham 定理的证明。
- M. Spivak, *Calculus on Manifolds*：形式与 Stokes 定理的最短入门，入口题同名形式的出处。
- C. Weibel, *An Introduction to Homological Algebra*：第 70 章的预备（链复形、链同伦、导出函子）。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch27_de_Rham上同调_上.md">← 第27章 de Rham 上同调·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch29_Hilbert空间与内积结构_上.md">第29章 Hilbert 空间与内积结构·上 →</a></div>
</div>
