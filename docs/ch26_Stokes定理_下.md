---
layout: default
---

# 第26章: Stokes 定理·下：完整推导 (Stokes' Theorem · Part II: Full Derivation)

> 配套预备: 见 第25章 Stokes 定理·上（同一主题的具体铺垫，建议先读）

> 对应原专栏: MP27–MP28
> 专家依据: `_experts/algebra/homological-algebra.md`（主）+ `_experts/algebra/_SKILL.md`
> 知识库依据: `opc2/knowledge/math/微分几何/differential-geometry/`（ch08 定向积分与 Stokes 定理）
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

读完第 25 章的具体例子后——正方形上的 Green 公式、立方体上的散度定理、三角形边界的符号、一次具体的拉回——这里把同一批构造写成一般定义，并给出完整证明。

本章要解决的核心问题只有一个：**把微积分里那几条彼此孤立的积分公式，认成同一条定理。**

平面上的 Green 公式、空间中的 Gauss 散度定理、沿曲面的 Kelvin–Stokes 公式，再加上一维的 Newton–Leibniz 公式，在通常的课本里分散在三四个学期、用三四套记号、各自证明一遍。本章要说明：它们全是

$$\int_{\partial M}\omega=\int_M d\omega$$

在不同维数、不同舞台上的同一句话。

**从哪来**：第 14 章造出了外微分 $$d$$ 并证明了 $$d^2=0$$；第 17–20 章造出了链群、边界算子 $$\partial$$ 与同调群，并证明了 $$\partial^2=0$$（第 18 章）；第 24 章把 $$d$$ 落到了 Maxwell 方程组上。本章把这两条线接起来——拓扑那一侧的 $$\partial$$ 与分析这一侧的 $$d$$，在这里第一次被写在同一个等式的两边。

**到哪去**：第 28 章会指出，这条等式不只是在说"两个算子配了对"。它把 $$M$$ 上的微分形式与 $$M$$ 的同调**配对成一个双线性型**，而这个配对是非退化的——那就是 de Rham 定理。

## 二、入口：一道具体的问题 (Entry Problem)

本节先给题，不给定义。下面三问都不会在本节解答，它们是全章的引子：读完第三节你会知道 (a)(b) 的答案，读完第五节你会算出 (c)。

**入口题（自编；风格取自教材经典例题与 Квант 口径，(c) 取自 Paulin 讲义第六章习题）。**

**(a) 一条定理，三个公式。** 不查任何积分表，只用一条定理同时证明下面三条。

- （平面 Green 公式）设 $$D\subset\mathbb{R}^2$$ 是以简单闭曲线 $$\partial D$$ 为边界的区域，$$P,Q$$ 在 $$D$$ 附近光滑，则

$$\oint_{\partial D}P\,dx+Q\,dy=\iint_D\Bigl(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Bigr)\,dx\,dy;$$

- （空间 Gauss 散度定理）设 $$\Omega\subset\mathbb{R}^3$$ 是闭区域，$$\vec F=(F^x,F^y,F^z)$$ 在 $$\Omega$$ 附近光滑，则

$$\iint_{\partial\Omega}\bigl(F^x\,dy\,dz+F^y\,dz\,dx+F^z\,dx\,dy\bigr)=\iiint_\Omega\Bigl(\frac{\partial F^x}{\partial x}+\frac{\partial F^y}{\partial y}+\frac{\partial F^z}{\partial z}\Bigr)\,dx\,dy\,dz;$$

- （Kelvin–Stokes 公式）设 $$S\subset\mathbb{R}^3$$ 是带边的定向曲面，则

$$\oint_{\partial S}\vec F\cdot d\vec r=\iint_S(\nabla\times\vec F)\cdot d\vec S.$$

**问题**：这三条为什么是"同一条"？它们公共的那个形式长什么样？

**(b) 三处"差一"是被同一样东西咬住的吗？** 公共形式 $$\int_{\partial M}\omega=\int_M d\omega$$ 里，左边被积的是 $$k$$-形式，右边是 $$(k+1)$$-形式，而 $$\partial M$$ 又比 $$M$$ 恰好低一维。三个"一"分别来自哪里——是三件互相无关的事，还是同一件事的三个投影？

**(c) 具体算一个。** 设 $$S^2$$ 是 $$\mathbb{R}^3$$ 中的单位球面，定向取外法向，求

$$\int_{S^2}\omega,\qquad \omega=x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy.$$

（提示：把 $$\omega$$ 限制到 $$S^2$$ 上算，会得到一个你熟悉的数；但本章的工具能让你不算这个限制积分就得到答案。）


## 三、结构：定义与完整推导 (Structure & Proof)

本章的推导按原专栏的路线走两站：先在最规整的舞台上把定理证出来（标准单形，MP27），再把舞台换成任意流形（奇异链，MP28）。两站之间需要一台搬运机器——拉回。

### 3.1 定向与诱导定向 (Orientation and induced orientation)

积分号要能定义，前提是"正方向"这个词有意义。先把这件事说清楚。

**定义 3.1（定向 / orientation）**。设 $$M$$ 是 $$n$$ 维微分流形。$$M$$ 的一个**定向**是一族坐标卡 $$\{(U_\alpha,\varphi_\alpha)\}$$ 覆盖 $$M$$，使得任意两张卡重叠处的转移映射 $$\tau_{\alpha\beta}=\varphi_\beta\circ\varphi_\alpha^{-1}$$ 满足

$$\det\bigl(d\tau_{\alpha\beta}\bigr)>0$$

（处处成立）。带定向的 $$M$$ 称为**定向流形 (oriented manifold)**。

**为什么是这个条件**。在一点 $$p$$ 处，切空间 $$T_pM$$ 的一组基 $$(v_1,\dots,v_n)$$ 被坐标卡 $$\varphi_\alpha$$ 读成 $$\mathbb{R}^n$$ 中的一组向量；两张大卡读出的是同一组向量被一个线性映射（Jacobi 矩阵）搬运的结果。若雅可比行列式为正，则"这组基是正的"这个判断在两张大卡下一致——于是"正基"变成一个**全局**概念。若行列式为负，判断相反，就没有全局的"正"可言。所以定向不是额外数据，它是"能让'正'这个词在 $$\det>0$$ 的图上不变"这件事本身。

**为什么需要这一条定义**。主定理最终要写成 $$\int_{\partial D}\omega=\int_Dd\omega$$，左边这个积分号要有意义，$$\partial D$$ 就必须先有自己的定向——而这个定向不能凭空另定，它必须由 $$D$$ 自己的定向唯一确定，否则等式两边的符号会各算各的、对不上号。第25章 3.1 节已经用矩形边界手算过一次"外法向排第一"的规则；下面把同一条规则写成任意维数的一般定义。

**定义 3.2（诱导定向 / induced orientation）**。设 $$M$$ 是带边的定向 $$n$$ 维流形。在边界点 $$p\in\partial M$$ 处，取 $$T_pM$$ 的**外法向 (outward normal)** $$N_p$$（指向 $$M$$ 外部、且与 $$p$$ 处的边界相截的那个方向）。约定 $$\partial M$$ 的**诱导定向**为：$$\partial M$$ 在 $$p$$ 处的一组基 $$(u_1,\dots,u_{n-1})$$ 是正的，当且仅当

$$(N_p,u_1,\dots,u_{n-1})$$

是 $$T_pM$$ 的正基（即"外法向排在第一位"）。

**注 3.3（约定必须和符号一起定）**。若把 3.2 改成"内法向在前"，则本章主定理的右端要整体多一个负号。这不是可以随手改的记号，因为它必须和第 18 章已经用过的边界公式 $$\partial=\sum_i(-1)^i f_i$$ 相容——3.2 正是被那个公式逼出来的约定，下面 定理 3.8 会当场验证。

**例 3.4（两个低维核对）**。

- $$n=1$$：$$M=[a,b]\subset\mathbb{R}$$，定向取 $$x$$ 轴正方向。$$\partial M=\{a,b\}$$ 是 0 维流形，其定向就是给每个点一个 $$\pm1$$。在 $$b$$ 处外法向是 $$+e_1$$，它本身是 $$\mathbb{R}^1$$ 的正基，故 $$b$$ 取 $$+1$$；在 $$a$$ 处外法向是 $$-e_1$$，是 $$\mathbb{R}^1$$ 的负基，故 $$a$$ 取 $$-1$$。于是 $$\partial[a,b]=[b]-[a]$$。
- $$n=2$$：$$M$$ 是平面区域，定向取标准定向（$$x$$ 轴在前、$$y$$ 轴在后）。沿边界逆时针行走时外法向指向行进方向的右手边——于是 3.2 给出的正是逆时针定向。

这两个例子的结论，恰好就是第 18 章里 $$\partial$$ 的那个 $$\sum_i(-1)^i$$ 的符号来源。这不是巧合，定理 3.8 会把它算实。

### 3.2 标准单形、面映射与边界 (Standard simplex, face maps, boundary)

要证的定理最终要在任意形状的流形上成立，但流形形状各异、坐标各异，没法直接下手算。标准做法是先选一个"最干净"的模型——顶点、边、面都用固定坐标写死，算起来是纯粹的多元微积分——把定理在这个模型上证完，再用一台搬运机器（3.4 节的拉回）把结论原样搬到任意流形上。标准单形就是这个模型；下面的面映射、边界，都是为了在这个模型上把"边界"这个几何操作写成可以计算的代数式。第25章 3.5 节已经在 $$n=2$$ 的情形手算过一次面映射与边界的符号，这里把它写成任意维数的一般定义。

**定义 3.5（标准单形 / standard simplex）**。$$\mathbb{R}^n$$ 中的 **$$n$$-标准单形** $$\sigma_n$$ 是

$$\sigma_n=\Bigl\{x\in\mathbb{R}^n:\ x_1\ge0,\ \dots,\ x_n\ge0,\ \sum_{i=1}^n x_i\le1\Bigr\}.$$

它的 $$n+1$$ 个顶点是 $$p_0=(0,\dots,0)$$ 与 $$p_i=e_i$$（第 $$i$$ 个坐标是 $$1$$、其余是 $$0$$），其中 $$i=1,\dots,n$$。约定 $$\sigma_n$$ 的定向由 $$\mathbb{R}^n$$ 的标准定向继承，即

$$dx^1\wedge\cdots\wedge dx^n$$

为正体积形式（于是第 14 章意义下的积分 $$\int_{\sigma_n}dx^1\wedge\cdots\wedge dx^n$$ 就是 $$\sigma_n$$ 的通常体积 $$1/n!$$）。

**定义 3.6（面映射 / face map）**。对 $$i=0,1,\dots,n$$，第 $$i$$ 个**面映射** $$f_i:\sigma_{n-1}\to\sigma_n$$ 把 $$\sigma_{n-1}$$ 的顶点按顺序映到 $$\sigma_n$$ 去掉 $$p_i$$ 后剩下的 $$n$$ 个顶点上。写成坐标（$$u=(u_1,\dots,u_{n-1})$$ 是 $$\sigma_{n-1}$$ 的坐标）：

$$f_0(u)=\Bigl(1-\sum_{l=1}^{n-1}u_l,\ u_1,\ u_2,\ \dots,\ u_{n-1}\Bigr),\qquad
f_i(u)=\bigl(u_1,\dots,u_{i-1},\ 0,\ u_i,\dots,u_{n-1}\bigr)\quad(i\ge1).$$

$$f_0$$ 的像落在"斜面" $$x_1+\cdots+x_n=1$$ 上（它去掉的是 $$p_0$$）；$$f_i\ (i\ge1)$$ 的像落在坐标超平面 $$x_i=0$$ 上（它去掉的是 $$p_i$$）。

**定义 3.7（单形的边界）**。定义

$$\partial\sigma_n=\sum_{i=0}^{n}(-1)^i\,f_i .$$

这是第 18 章的 $$\partial$$ 在单个单形上的写法，它的意义要到 3.5 才完整（那时我们看到它是一个"降一维的链"）。第 18 章已经证明过 $$\partial^2=0$$，即 $$\partial(\partial\sigma_n)=0$$；这个代数事实正是 $$f_i$$ 前那些 $$\pm1$$ 被设计出来的原因。

**定理 3.8（$$\partial$$ 的符号 = 诱导定向）**。定义 3.7 里的 $$\partial\sigma_n=\sum_i(-1)^if_i$$ 与 定义 3.2 的"外法向在前"诱导定向完全相容：按 $$\sum_i(-1)^if_i$$ 读出的边界定向，正是外法向在前的定向。

**证明**。只需在两个低维情形逐字核对，一般 $$n$$ 由归纳与 3.2 的局部性给出。

**$$n=1$$**：$$\sigma_1=[0,1]$$，$$p_0=0$$，$$p_1=1$$。$$f_0:\sigma_0=\{0\}\to\{0\}$$（去掉 $$p_0$$，剩下 $$p_1=1$$，故 $$f_0(0)=1$$）；$$f_1:\sigma_0\to\{0\}$$（去掉 $$p_1$$，剩下 $$p_0=0$$）。于是

$$\partial\sigma_1=f_0-f_1=[1]-[0].$$

与 例 3.4 中由外法向算出的 $$\partial[a,b]=[b]-[a]$$ 逐项相同。

**$$n=2$$**：$$\sigma_2$$ 的顶点是 $$p_0=(0,0)$$、$$p_1=(1,0)$$、$$p_2=(0,1)$$。由定义 3.6：

$$f_0(u)=(1-u_1,u_1),\qquad f_1(u)=(0,u_1),\qquad f_2(u)=(u_1,0).$$

把它们看成三条**有向线段**：

- $$f_0$$：$$u_1=0\mapsto(1,0)=p_1$$，$$u_1=1\mapsto(0,1)=p_2$$，即 $$p_1\to p_2$$；
- $$f_1$$：$$0\mapsto(0,0)=p_0$$，$$1\mapsto(0,1)=p_2$$，即 $$p_0\to p_2$$；
- $$f_2$$：$$0\mapsto(0,0)$$，$$1\mapsto(1,0)$$，即 $$p_0\to p_1$$。

于是

$$\partial\sigma_2=f_0-f_1+f_2=(p_1\to p_2)-(p_0\to p_2)+(p_0\to p_1)=(p_0\to p_1)+(p_1\to p_2)+(p_2\to p_0),$$

后一步用了 $$-(p_0\to p_2)=(p_2\to p_0)$$。这条链首尾相接、绕行方向是**逆时针**（$$p_0\to p_1\to p_2\to p_0$$），正是 例 3.4 里由外法向在前给出的定向。$$\square$$

**注 3.9**。$$\partial^2\sigma_2=0$$ 现在有了一个看得见的翻译：三条边首尾相接的链在取一次边界后全部抵消——"边界的边界是空"就是"闭曲线没有端点"。

### 3.3 标准单形上的积分与 Stokes 定理（MP27，完整证明）

先把 $$\mathbb{R}^n$$ 上的积分搬进单形。

**定义 3.10（形式在标准单形上的积分）**。设 $$\omega=W(x)\,dx^1\wedge\cdots\wedge dx^n$$ 是定义在 $$\sigma_n$$ 的一个邻域上的 $$n$$-形式（系数 $$W$$ 连续），定义

$$\int_{\sigma_n}\omega=\int_{\sigma_n}W(x)\,dx_1\cdots dx_n,$$

右端是 $$\sigma_n$$ 上的通常（$$n$$ 重）积分。这是全书第一次真刀真枪地定义"形式的积分"：一个 $$n$$-形式配上一个 $$n$$ 维的区域，用第 14 章的楔积语言说，就是把 $$n$$ 个 $$dx$$ 全用掉。

**一个准备**。设 $$\psi$$ 是 $$\sigma_n$$ 邻域上的 $$(n-1)$$-形式。用第 14 章 3.17 的基把它写开：

$$\psi=\sum_{j=1}^{n}\Psi_j(x)\,dx^1\wedge\cdots\wedge\widehat{dx^j}\wedge\cdots\wedge dx^n,$$

其中 $$\widehat{dx^j}$$ 表示"删去这一项"（即第 $$j$$ 个基 1-形式不出现）。由第 14 章定理 3.17 的公式 $$(\ast)$$，直接算外微分：

$$d\psi=\sum_{j=1}^{n}(-1)^{\,j-1}\,\frac{\partial \Psi_j}{\partial x^j}\,dx^1\wedge\cdots\wedge dx^n .$$

（这里的 $$(-1)^{j-1}$$ 来源要说清楚，不能跳过：把 $$d\Psi_j$$ 楔到 $$dx^1\wedge\cdots\widehat{dx^j}\cdots\wedge dx^n$$ 时，$$d\Psi_j=\sum_k\partial_k\Psi_j\,dx^k$$ 中的 $$dx^k$$ 要穿过前面 $$j-1$$ 个因子抵达它"原来属于的第 $$j$$ 位"，于是出一个 $$(-1)^{j-1}$$；而求和只留下 $$k=j$$ 的项，因为其它 $$k$$ 会让同一个 $$dx^k$$ 出现两次。**这里用了 $$d(dx^i)=0$$，即第 14 章的 $$d^2=0$$。**）

**代一个具体的 $$n$$ 核对一下**。取 $$n=3,\ j=2$$：这一项是 $$\Psi_2\,dx^1\wedge dx^3$$（删去 $$dx^2$$）。它对 $$d\psi$$ 的贡献是 $$d\Psi_2\wedge dx^1\wedge dx^3$$，其中 $$d\Psi_2=\partial_1\Psi_2\,dx^1+\partial_2\Psi_2\,dx^2+\partial_3\Psi_2\,dx^3$$。楔上 $$dx^1\wedge dx^3$$ 后，含 $$dx^1$$ 或 $$dx^3$$ 的两项都因重复因子而为零，只剩

$$\partial_2\Psi_2\,dx^2\wedge dx^1\wedge dx^3 .$$

要把它整理成标准顺序 $$dx^1\wedge dx^2\wedge dx^3$$，只需把 $$dx^2$$ 和 $$dx^1$$ 对调一次（跨过 $$1$$ 个因子），出一个负号：$$dx^2\wedge dx^1\wedge dx^3=-dx^1\wedge dx^2\wedge dx^3$$，符号恰是 $$(-1)^1=(-1)^{j-1}$$（$$j=2$$）。这与第25章 3.2 节里"$$dy\wedge dx=-dx\wedge dy$$"是同一种反交换换算；一般的 $$j$$ 只是要跨过的因子从 $$1$$ 个变成 $$j-1$$ 个，符号相应地累积成 $$(-1)^{j-1}$$。

**定理 3.11（标准单形上的 Stokes 定理 / Stokes on the standard simplex）**。对 $$\sigma_n$$ 邻域上任意光滑的 $$(n-1)$$-形式 $$\psi$$，

$$\int_{\partial\sigma_n}\psi=\int_{\sigma_n}d\psi .$$

**证明思路**。把两边都化成 $$\sigma_{n-1}$$ 上的 $$(n-1)$$ 重积分，逐项对号。右端是 $$n$$ 重积分，对第 $$j$$ 个变量用一次 **Newton–Leibniz 公式**（富比尼定理 + 微积分基本定理）就会吐出一个"上下限之差"；左端是边界积分，按 $$\partial\sigma_n=\sum_i(-1)^if_i$$ 展开成 $$n+1$$ 个面积分。关键是一一对上：坐标面 $$x_j=0$$ 对应右端的**下限**项，斜面 $$f_0$$ 对应右端的**上限**项。不上算不算的——下面逐项做。

**证明**。

**第一步：右端化成 $$n+1$$ 个积分。** 由定义 3.10 与上面的准备，

$$\int_{\sigma_n}d\psi=\sum_{j=1}^{n}(-1)^{j-1}\int_{\sigma_n}\frac{\partial \Psi_j}{\partial x^j}\,dV,\qquad dV=dx_1\cdots dx_n .$$

**第二步：对每个 $$j$$ 用富比尼 + N–L。** 固定 $$j$$，把 $$\sigma_n$$ 看成沿 $$x_j$$ 方向的一摞纤维：其余变量记作 $$x_{\hat j}=(x_1,\dots,\widehat{x_j},\dots,x_n)$$，它们跑遍

$$P_j=\Bigl\{x_{\hat j}:\ x_k\ge0\ (k\ne j),\ \sum_{k\ne j}x_k\le1\Bigr\},$$

而对固定的 $$x_{\hat j}$$，$$x_j$$ 恰跑遍区间 $$\bigl[0,\ 1-\sum_{k\ne j}x_k\bigr]$$。于是

$$\int_{\sigma_n}\frac{\partial \Psi_j}{\partial x^j}\,dV
=\int_{P_j}\Bigl[\Psi_j\Big\vert_{x_j=1-\sum_{k\ne j}x_k}-\Psi_j\Big\vert_{x_j=0}\Bigr]\,dx_{\hat j},$$

这里 $$dx_{\hat j}$$ 指 $$\prod_{k\ne j}dx_k$$（顺序按 $$x_1,\dots,\widehat{x_j},\dots,x_n$$）。记这两个积分为

$$A_j:=\int_{P_j}\Psi_j\Big\vert_{x_j=1-\sum_{k\ne j}x_k}dx_{\hat j},\qquad
B_j:=\int_{P_j}\Psi_j\Big\vert_{x_j=0}\,dx_{\hat j}.$$

代入第一步：

$$\int_{\sigma_n}d\psi=\sum_{j=1}^{n}(-1)^{j-1}\bigl(A_j-B_j\bigr).\qquad(\star)$$

**第三步：左端化成面积分。** 由 $$\partial\sigma_n=\sum_i(-1)^if_i$$，左端是

$$\int_{\partial\sigma_n}\psi=\sum_{i=0}^{n}(-1)^i\int_{\sigma_{n-1}}f_i^{*}\psi .$$

逐面算 $$f_i^{*}\psi$$。

**坐标面 $$i\ge1$$**：$$f_i$$ 把 $$x_i$$ 固定成 $$0$$，把其余坐标按 $$u$$ 的顺序排好。$$\psi$$ 的 $$j$$-项里含因子 $$dx^i$$（当 $$j\ne i$$）或含"被删项 $$dx^i$$"（当 $$j=i$$）。当 $$j\ne i$$ 时该项含 $$dx^i$$，而 $$f_i^{*}(dx^i)=0$$，贡献为零；只有 $$j=i$$ 项活下来。又 $$f_i$$ 把 $$dx^1\wedge\cdots\widehat{dx^i}\cdots\wedge dx^n$$ 拉回成 $$du^1\wedge\cdots\wedge du^{n-1}$$（每个 $$dx$$ 与对应的 $$du$$ 一一对上，符号为正）。所以

$$\int_{\sigma_{n-1}}f_i^{*}\psi=B_i\qquad(i\ge1).$$

**斜面 $$i=0$$**：由 $$f_0(u)=\bigl(1-\sum_l u_l,u_1,\dots,u_{n-1}\bigr)$$ 得 $$dx^1=-\sum_l du^l$$、$$dx^{k}=du^{k-1}\ (k\ge2)$$。逐项拉回：

- $$j=1$$ 项（删去 $$dx^1$$，含 $$dx^2,\dots,dx^n$$）拉回成 $$\Psi_1\,du^1\wedge\cdots\wedge du^{n-1}$$。
- $$j\ge2$$ 项（含 $$dx^1$$，删去 $$dx^j$$）拉回成 $$\Psi_j\cdot\bigl(-\sum_l du^l\bigr)\wedge du^1\wedge\cdots\widehat{du^{j-1}}\cdots\wedge du^{n-1}$$。求和中只有 $$l=j-1$$（那个被删掉的脚标）能活下来，而把 $$du^{j-1}$$ 搬回它该在的第 $$j-1$$ 位要出 $$(-1)^{j-2}$$，两次符号相乘得 $$(-1)^{j-1}$$。所以这一项拉回成 $$(-1)^{j-1}\Psi_j\,du^1\wedge\cdots\wedge du^{n-1}$$。

合起来（斜面用 $$P_1$$ 作参数域，$$u$$ 就是 $$x_2,\dots,x_n$$）：

$$\int_{\sigma_{n-1}}f_0^{*}\psi=\int_{P_1}\Bigl[\Psi_1+\sum_{j=2}^{n}(-1)^{j-1}\Psi_j\Bigr]_{\text{斜面上}}dx_{\hat 1},\qquad dx_{\hat1}=dx_2\cdots dx_n .$$

**第四步：对号。** 把 $$(\star)$$ 的 $$B$$ 部分先对上：由第三步，$$\sum_{j=1}^n(-1)^{j-1}B_j=\sum_{i\ge1}(-1)^{i-1}B_i=-\sum_{i\ge1}(-1)^iB_i$$，即

$$-\sum_{j=1}^{n}(-1)^{j-1}B_j=\sum_{i\ge1}(-1)^i\int_{\sigma_{n-1}}f_i^{*}\psi .$$

**剩下要证**

$$\sum_{j=1}^{n}(-1)^{j-1}A_j=\int_{\sigma_{n-1}}f_0^{*}\psi .\qquad(\star\star)$$

这一步是全部符号的所在地，用换元来做。斜面在坐标系统 $$(x_2,\dots,x_n)$$（就是 $$P_1$$）与 $$(x_1,\dots,\widehat{x_j},\dots,x_n)$$（就是 $$P_j$$）下各有坐标。把 $$A_j$$ 的积分域从 $$P_j$$ 换到 $$P_1$$：

**(a) 形式的拉回。** 参数化 $$x_1=1-\sum_{k\ge2}x_k$$，$$x_k=x_k\ (k\ge2)$$。与第三步同样的算法给出

$$dx^1\wedge\cdots\widehat{dx^j}\cdots\wedge dx^n=(-1)^{\,j-1}\,dx^2\wedge\cdots\wedge dx^n\qquad(j\ge2).$$

**(b) 定向的翻转。** $$P_1\to P_j$$ 这个坐标变换（把 $$x_j$$ 挤出去、把 $$x_1$$ 表成 $$x_2,\dots,x_n$$ 的组合）的 Jacobi 行列式是 $$(-1)^{\,j+1}$$：只有 $$x_1$$ 那一行是 $$\partial x_1/\partial x_k=-1$$，其余各行是标准基向量，而 $$x_j$$ 那一行被"跳过"，展开时出一个 $$(-1)^{j-1}$$，与第一行的 $$-1$$ 相乘得 $$(-1)^{\,j+1}$$。域 $$P_j$$ 的定向是它自己的标准定向，不是 $$P_1$$ 的推前——两者相差这个符号的倒数，即再乘 $$(-1)^{\,j+1}$$。

**代 $$n=3,j=2$$ 核对**（这与第25章 3.1 节算过的极坐标 Jacobi 行列式是同一类计算，只是这里换元更绕）：坐标变换是 $$(x_2,x_3)\mapsto(x_1,x_3)=(1-x_2-x_3,\,x_3)$$。Jacobi 矩阵是 $$\begin{pmatrix}\partial x_1/\partial x_2&\partial x_1/\partial x_3\\ \partial x_3/\partial x_2&\partial x_3/\partial x_3\end{pmatrix}=\begin{pmatrix}-1&-1\\0&1\end{pmatrix}$$，行列式 $$=-1\cdot1-(-1)\cdot0=-1$$，恰是 $$(-1)^{j+1}=(-1)^3=-1$$（$$j=2$$）。

**(c) 两次符号相乘。** $$(-1)^{\,j-1}\cdot(-1)^{\,j+1}=(-1)^{\,2j}=+1$$。所以

$$A_j=\int_{P_1}\Psi_j\Big\vert_{\text{斜面上}}dx_{\hat1}\qquad(j\ge2),$$

**不带任何符号**；而 $$j=1$$ 时按定义 $$A_1$$ 就是这个积分。代回 $$(\star\star)$$ 左边，逐项与第三步算出的 $$f_0^{*}\psi$$ 对号，两项完全一致。$$(\star\star)$$ 得证。

**第五步：合并。** 把 $$(\star)$$、第四步的两半合起来：

$$\int_{\sigma_n}d\psi=\sum_{j}(-1)^{j-1}A_j-\sum_{j}(-1)^{j-1}B_j
=\int_{\sigma_{n-1}}f_0^{*}\psi+\sum_{i\ge1}(-1)^i\int_{\sigma_{n-1}}f_i^{*}\psi
=\sum_{i=0}^{n}(-1)^i\int_{\sigma_{n-1}}f_i^{*}\psi=\int_{\partial\sigma_n}\psi .\ \square$$

**注 3.12（两组符号各司其职）**。证明里出现过两类符号来源，弄清它们各自的活儿是有价值的：

| 符号来源 | 出现在 | 它的数学身份 |
|---|---|---|
| $$(-1)^{j-1}$$（第 14 章 $$d$$ 的公式里） | 右端 $$d\psi$$ 的系数 | 把 $$d\Psi_j$$ 楔回第 $$j$$ 位时的**反对称** |
| $$(-1)^{j+1}$$（换元的 Jacobi） | 第四步 | 斜面两组坐标之间的**定向翻转** |

在第四步 (c) 里，这两者相乘为 $$+1$$——**这是"边界的定向约定"与"$$d$$ 的符号约定"精确对齐的唯一方式**。如果 3.2 里把诱导定向换成内法向在前，这个 $$+1$$ 就会变成 $$-1$$，于是定理右端整体多一个负号。这就是注 3.3 说的"约定必须和符号一起定"。

**注 3.13（$$n=2$$ 的手算核对）**。取 $$n=2$$，$$\sigma_2$$ 是顶点 $$(0,0),(1,0),(0,1)$$ 的三角形，$$\psi=\Psi_1\,dx^2+\Psi_2\,dx^1$$。取 $$\Psi_1=x_1,\Psi_2=0$$：则 $$d\psi=\partial_1\Psi_1\,dx^1\wedge dx^2=dx^1\wedge dx^2$$，右端 $$=\int_{\sigma_2}dx_1dx_2=\tfrac12$$（三角形面积）。左端：$$f_0^{*}\psi=(1-u_1)du_1$$ 给出 $$\int_0^1(1-u_1)du_1=\tfrac12$$；$$f_1^{*}\psi=0$$（$$x_1\equiv0$$）；$$f_2^{*}\psi=u_1\cdot d(0)=0$$。于是左端 $$=\tfrac12-0+0=\tfrac12$$，两边相等。再取 $$\Psi_1=0,\Psi_2=x_1$$：$$d\psi=0$$，右端 $$=0$$；左端 $$f_0^{*}(x_1dx^1)=-\tfrac12$$、$$f_1^{*}\psi=0$$、$$f_2^{*}(x_1dx^1)=\tfrac12$$，合计 $$-\tfrac12+0+\tfrac12=0$$。两边仍相等。

### 3.4 拉回：把形式搬着走 (Pullback)

要把定理从 $$\sigma_n$$ 搬到任意流形，需要一台把"形式"往反方向搬运的机器。

**定义 3.14（拉回 / pullback）**。设 $$F:M\to N$$ 是光滑映射，$$p\in M$$。切映射 $$F_{*}:T_pM\to T_{F(p)}N$$ 把切向量往前推；它的对偶（第 04、06 章的"转置"）反向而行：

$$F^{*}:T^{*}_{F(p)}N\longrightarrow T^{*}_{p}M,$$

称为**拉回**。它的定义由配对唯一确定：对一切 $$v\in T_pM$$、$$\omega\in T^{*}_{F(p)}N$$，

$$\langle F^{*}\omega,\ v\rangle_M=\langle \omega,\ F_{*}v\rangle_N .$$

对 $$k$$-形式逐点拉回并保持外积，得到 $$F^{*}:\Omega^{k}(N)\to\Omega^{k}(M)$$。**注意方向是反的**：$$F$$ 把点送出去，$$F^{*}$$ 把形式拉回来——这就是它名字的全部含义。

**展开成坐标里能算的样子**。上面的定义是抽象配对，真要算的时候只需要两条规则：$$F^{*}(fg)=(F^{*}f)(F^{*}g)$$（对函数直接复合，$$F^{*}f=f\circ F$$）、$$F^{*}(df)=d(F^{*}f)$$（这正是下面 定理3.15 要证的特殊情形，$$k=0$$）。于是若 $$N$$ 上取坐标 $$y^1,\dots,y^n$$，$$F$$ 写成 $$y^i=F^i(x)$$，则 $$F^{*}(dy^i)=dF^i=\sum_j\frac{\partial F^i}{\partial x^j}dx^j$$，把 $$\omega=\sum W_I\,dy^{i_1}\wedge\cdots\wedge dy^{i_k}$$ 里的每个 $$y^i$$ 换成 $$F^i(x)$$、每个 $$dy^i$$ 换成 $$dF^i$$，再展开楔积，就是 $$F^{*}\omega$$。第25章 3.4 节已经手算过一次：$$F(t)=(\cos t,\sin t)$$，$$\omega=x\,dy-y\,dx$$，逐项代入 $$x=\cos t,\ dy=d(\sin t)=\cos t\,dt$$ 等，算出 $$F^{*}\omega=dt$$——这就是下面的抽象定义在具体坐标里的样子，本节只是把这套"代入再展开"的算法写成一般规则。

**定理 3.15（拉回与外微分交换）**。对光滑 $$F:M\to N$$ 与 $$\omega\in\Omega^{k}(N)$$，

$$F^{*}(d\omega)=d(F^{*}\omega).$$

**证明**。这是第 14 章定理 3.19，那里已用链式法则证过：只需对函数 $$\omega=f$$ 验证（因为 $$d$$ 被第 14 章的 3.17 逼死，而 $$F^{*}$$ 与楔积交换），而 $$F^{*}(df)$$ 与 $$d(F^{*}f)$$ 都等于"$$f\circ F$$ 的方向导数"这同一个东西。$$\square$$

**为什么这条是搬家的关键**。它说的是：**$$F^{*}$$ 把 $$d$$ 整个抬过来，一步不多一步不少**。于是"先在 $$M$$ 上取 $$d$$，再拉回"与"先拉回，再在 $$\sigma_n$$ 上取 $$d$$"是同一件事——这正是下面把定理 3.11 搬到流形上时唯一需要的性质。

### 3.5 奇异单形、奇异链与其上的积分（MP28）

定理 3.11 只在标准单形 $$\sigma_n$$ 上证过；但要处理的区域，比如球面、环面上的一块曲面，形状各不相同，没有哪一个能直接就是某个 $$\sigma_n$$。解决办法不是把每种形状单独证一遍，而是承认它们都可以"捏"出来——用一个光滑映射把规整的 $$\sigma_r$$ 映到流形上一块任意形状的区域。这样一来，流形上任意一块区域上的积分，就都能通过这个映射，换算成 $$\sigma_r$$ 上已经会算的积分（定义 3.10）。这就是引入奇异单形的理由。

**定义 3.16（奇异单形 / singular simplex）**。设 $$M$$ 是 $$n$$ 维（或更高维）微分流形。$$M$$ 的一个 **$$r$$-奇异单形**是一个光滑映射

$$s:\sigma_r\longrightarrow M .$$

（原专栏加强了光滑同胚的条件以保证拓扑性质完全保留；对本章的积分推导，光滑已够。）与 $$\sigma_r$$ 对照，$$s$$ 是把"标准积木"捏成 $$M$$ 里一块任意形状的单形；单纯同调中"必须三角剖分"的限制，到这里被 $$s$$ 的灵活性彻底松开。

**定义 3.17（奇异单形上的积分）**。设 $$\omega\in\Omega^{r}(M)$$，定义

$$\int_{s}\omega:=\int_{\sigma_r}s^{*}\omega .$$

**为什么必须用拉回，而不能直接写 $$\int_s\omega=\int_\sigma\omega$$**。因为 $$s$$ 捏过之后的单形上，被积的东西已经变了：$$\sigma_r$$ 上有一个现成的坐标 $$u$$，$$s(\sigma_r)$$ 上没有。$$s^{*}\omega$$ 做的正是"把 $$M$$ 上的 $$\omega$$ 用参数 $$u$$ 重新表达"——它把 $$s$$ 的作用记在了形式里，而积分只在规则的 $$\sigma_r$$ 上做。若省掉 $$s^{*}$$，等式两边就是两个不同单形上的两个不同积分，绝不相等。

**定义 3.18（奇异链 / singular chain）**。$$M$$ 的 $$r$$-奇异链是有限形式和

$$c=\sum_k z_k\,s_k,\qquad z_k\in\mathbb{Z}\ \text{或}\ \mathbb{R},\quad s_k\ \text{是}\ r\text{-奇异单形},$$

即 $$\sigma_r$$ 生成的自由模中的元素。所有 $$r$$-奇异链组成**奇异链群** $$C_r(M)$$。

**定义 3.19（奇异链上的积分与边界）**。线性地定义

$$\int_{c}\omega:=\sum_k z_k\int_{s_k}\omega,\qquad
\partial s:=\sum_{i=0}^{r}(-1)^{\,i}\,(s\circ f_i),\qquad
\partial c:=\sum_k z_k\,\partial s_k .$$

$$\partial(c)$$ 是 $$(r-1)$$-奇异链。第 18 章证明过 $$\partial^2=0$$；本定义把同一个 $$\partial$$ 逐字搬到了光滑映射的单形上，因而 $$\partial^2c=0$$ 依旧成立。

### 3.6 奇异链上的 Stokes 定理 (Stokes on singular chains)

现在把 定理 3.11 搬上流形。搬运只需要一件事：定理 3.15。

**定理 3.20（奇异链上的 Stokes 定理）**。对 $$\omega\in\Omega^{r-1}(M)$$ 与 $$r$$-奇异链 $$c\in C_r(M)$$，

$$\int_{\partial c}\omega=\int_{c}d\omega .$$

**证明**。两边都对 $$c$$ 线性，故只需对单个 $$r$$-奇异单形 $$s$$ 证明。

**右端**：由定义 3.17、定理 3.15 与定理 3.11，

$$\int_{s}d\omega=\int_{\sigma_r}s^{*}(d\omega)=\int_{\sigma_r}d\bigl(s^{*}\omega\bigr)=\int_{\partial\sigma_r}s^{*}\omega .$$

**左端**：由定义 3.19，$$\partial s=\sum_i(-1)^i(s\circ f_i)$$，于是

$$\int_{\partial s}\omega=\sum_{i=0}^{r}(-1)^i\int_{s\circ f_i}\omega
=\sum_{i=0}^{r}(-1)^i\int_{\sigma_{r-1}}(s\circ f_i)^{*}\omega
=\sum_{i=0}^{r}(-1)^i\int_{\sigma_{r-1}}f_i^{*}\bigl(s^{*}\omega\bigr)
=\int_{\partial\sigma_r}s^{*}\omega,$$

第三步用了 $$(s\circ f_i)^{*}=f_i^{*}\circ s^{*}$$（拉回是反变的函子），第四步回到定义 3.7 与 3.10 的写法。两端都是 $$\int_{\partial\sigma_r}s^{*}\omega$$，故相等。$$\square$$

**这条证明值得停下来看一眼**。它把第 18 章的 $$\partial$$ 与第 14 章的 $$d$$ 各自的作用照原样"抬"到了流形上，中间没有任何新的几何输入——只用了定理 3.15 一条。原专栏的整个 MP28 就在做这一件事。

### 3.7 带边流形上的 Stokes 定理 (Stokes on manifolds with boundary)

奇异链版本已经足够一般，但要把定理写成 $$\int_{\partial M}$$ 的形式，还需要说明"链的边界"就是"流形的边界"。这一步在单纯/奇异同调里是标准的（第 17–20 章的构造保证：一个定向紧流形可以被它的奇异链以保定向的方式三角剖分，且三角剖分的边界链就是 $$\partial M$$ 的链），我们直接引用。

**定理 3.21（带边流形上的 Stokes 定理 / Stokes' theorem）**。设 $$D$$ 是定向 $$n$$ 维带边流形 $$M$$ 的开子流形，$$M$$ 的定向诱导出 $$D$$ 与 $$\partial D$$ 的定向（3.2）。对 $$\omega\in\Omega^{n-1}(M)$$ 紧支（或 $$D$$ 紧），

$$\int_{D}d\omega=\int_{\partial D}\omega .$$

**证明（化归到半空间）**。这是标准路线，也是原专栏提到的"Nakahara 的证明思想"的原型；把它写全，因为它是定理 3.11 之后唯一还需要补的一块。

**第一步：半空间情形。** 记 $$H^n=\{x\in\mathbb{R}^n:x_n\le0\}$$，$$\partial H^n=\{x_n=0\}$$，都取标准定向，$$\partial H^n$$ 取 3.2 的诱导定向。设 $$\omega=\sum_{i=1}^{n}f_i\,dx^1\wedge\cdots\widehat{dx^i}\cdots\wedge dx^n$$ 紧支。则

$$d\omega=\sum_{i=1}^{n}(-1)^{\,i-1}\frac{\partial f_i}{\partial x^i}\,dx^1\wedge\cdots\wedge dx^n,$$

于是

$$\int_{H^n}d\omega=\sum_{i=1}^{n}(-1)^{\,i-1}\int_{H^n}\frac{\partial f_i}{\partial x^i}\,dV .$$

- 当 $$i\le n-1$$：对 $$x_i$$ 用 N–L，$$x_i$$ 从 $$-\infty$$ 跑到 $$+\infty$$（$$\omega$$ 紧支，两端 $$f_i=0$$），积分为 $$0$$。
- 当 $$i=n$$：对 $$x_n$$ 用 N–L，$$x_n$$ 从 $$-\infty$$ 跑到 $$0$$，得 $$\int_{-\infty}^{0}\partial_nf_n\,dx_n=f_n(x_n=0)-0$$。于是

$$\int_{H^n}d\omega=(-1)^{\,n-1}\int_{x_n=0}f_n\,dx_1\cdots dx_{n-1}.$$

**边界侧**：$$\partial H^n=\{x_n=0\}$$ 的外法向是 $$+e_n$$。$$\omega$$ 的各项中，$$i\le n-1$$ 项含因子 $$dx^n$$，而 $$x_n=0$$ 上 $$dx^n$$ 拉回为 $$0$$，故都不贡献；只有 $$i=n$$ 项活下来，拉回为 $$f_n\,dx_1\wedge\cdots\wedge dx_{n-1}$$。至于符号：3.2 的"外法向在前"要求 $$(u_1,\dots,u_{n-1})$$ 是 $$\partial H^n$$ 的正基当且仅当 $$(e_n,u_1,\dots,u_{n-1})$$ 是 $$\mathbb{R}^n$$ 的正基。取 $$u_k=e_k$$，则

$$\det(e_n,e_1,\dots,e_{n-1})=(-1)^{\,n-1},$$

即按坐标顺序 $$(x_1,\dots,x_{n-1})$$ 读出的定向相对 $$\partial H^n$$ 的诱导定向差一个 $$(-1)^{n-1}$$。所以

$$\int_{\partial H^n}\omega=(-1)^{\,n-1}\int_{x_n=0}f_n\,dx_1\cdots dx_{n-1}.$$

两端都是 $$(-1)^{n-1}\int_{x_n=0}f_n$$，相等。**注意这个 $$(-1)^{n-1}$$ 在两端同时出现**——它不是误差，而是 3.2 那个约定留下的印记；这也再次说明约定与符号是一体的。

**第二步：一般流形。** 取从属于 $$D$$ 的定向图册的单位分解 $$\{\rho_\alpha\}$$（$$\sum_\alpha\rho_\alpha\equiv1$$ 于 $$\mathrm{supp}\,\omega$$ 附近）。每个 $$\rho_\alpha\omega$$ 支在单张定向坐标卡内，坐标卡把这小块映到 $$\mathbb{R}^n$$ 中的区域，边界部分落在某个坐标超平面上——局部上就是第一步的半空间情形。由第一步，$$\int_D d(\rho_\alpha\omega)=\int_{\partial D}\rho_\alpha\omega$$。又由 Leibniz 律，$$d(\rho_\alpha\omega)=d\rho_\alpha\wedge\omega+\rho_\alpha\,d\omega$$。

**展开"求和时抵消"这一句**：对 $$\alpha$$ 求和，

$$\sum_\alpha d(\rho_\alpha\omega)=\sum_\alpha d\rho_\alpha\wedge\omega+\Bigl(\sum_\alpha\rho_\alpha\Bigr)d\omega .$$

单位分解要求 $$\sum_\alpha\rho_\alpha\equiv1$$ 在 $$\mathrm{supp}\,\omega$$ 附近恒成立，两边取 $$d$$ 得 $$\sum_\alpha d\rho_\alpha\equiv0$$（常数 $$1$$ 的外微分是 $$0$$）。代入上式，右边第一项整体为零，只剩 $$1\cdot d\omega=d\omega$$，即

$$\sum_\alpha d(\rho_\alpha\omega)=d\omega .$$

两边对 $$D$$ 积分，再逐项代入第一步的结果：

$$\int_D d\omega=\sum_\alpha\int_D d(\rho_\alpha\omega)=\sum_\alpha\int_{\partial D}\rho_\alpha\omega=\int_{\partial D}\Bigl(\sum_\alpha\rho_\alpha\Bigr)\omega=\int_{\partial D}\omega .\ \square$$

**推论 3.22（四个经典公式，同一句话）**。在定理 3.21 中更换 $$n$$ 与 $$\omega$$，就得到入口题 (a) 的三条以及 N–L 本身。翻译细节留给第五节经典题 1、3、4——那里有 $$d$$ 与 $$\nabla$$ 的逐项对照。

### 3.8 暗线闭合：$$\partial$$ 与 $$d$$ 互为伴随 (The duality)

现在回来回答入口题 (b)。

**定理 3.23（$$\partial$$ 与 $$d$$ 对偶）**。把"$$r$$-链 $$c$$ 与 $$(r-1)$$-形式 $$\omega$$ 的配对"记作

$$\langle \partial c,\omega\rangle=\int_{\partial c}\omega,\qquad
\langle c,d\omega\rangle=\int_{c}d\omega .$$

则定理 3.20 说的恰好是

$$\bigl\langle \partial c,\ \omega\bigr\rangle=\bigl\langle c,\ d\omega\bigr\rangle .$$

用算子的语言：$$d$$ 与 $$\partial$$ 互为**伴随 (adjoint)**（差一个"次数平移"）。

**这就是入口题 (b) 的答案**：三处"差一"是**同一件事**的三个投影。

- 右边是 $$(k+1)$$-形式，因为 $$d:\Omega^{k}\to\Omega^{k+1}$$ **升**一格（第 14 章）；
- 左边是 $$k$$-形式，因为 $$\partial$$ 把 $$k$$ 维的积分域**降**一格（第 18 章）；
- 两边能对上，正是因为升与降在配对里彼此抵消——$$\langle\partial c,\omega\rangle$$ 与 $$\langle c,d\omega\rangle$$ 里出现的都是"一个 $$k$$-形式配一个 $$k$$ 维的域"。

而这条陪伴关系还有一处呼应，必须点明：

**暗线的闭合**。

| 章 | 式子 | 它说的是 |
|---|---|---|
| 第 14 章 | $$d^2=d\circ d=0$$ | 分析侧：连续取两次"无穷小边界"归零 |
| 第 18 章 | $$\partial^2=\partial\circ\partial=0$$ | 拓扑侧：连续取两次"宏观边界"归零 |
| **本章** | $$\displaystyle\int_{\partial}\omega=\int d\omega$$ | **两侧互为伴随——$$d$$ 是 $$\partial$$ 的转置** |

第 14 章末尾那句"$$\operatorname{curl}\circ\operatorname{grad}=0$$ 与 $$\operatorname{div}\circ\operatorname{curl}=0$$ 和 $$\partial^2=0$$ 是同一句话、只是分别写在形式世界和链世界"，到这一章才真正兑现：把它们焊在一起的，就是 定理 3.23 这一个等式。而且对偶一旦成立，$$d^2=0$$ 与 $$\partial^2=0$$ 也立刻成为彼此的转置——同一个零，两副面孔。

**向前一步**。定理 3.21 只用了 $$M$$ 的定向与 $$\omega$$ 的紧支性，完全没有用到度量的概念：积分、$$d$$、$$\partial$$ 都是"不需要尺子"的算子。于是定理 3.23 会自动给出一个纯代数的推论（第五节经典题 5 会证明它）：**闭形式在闭流形上的积分只依赖它的"上同调类"**。把这个配对往深处推一层——证明它非退化、并把 $$\Omega^{\bullet}$$ 的同调算出来——就是第 28 章的 de Rham 定理。


## 四、几何与物理直觉 (Intuition)

**一句话的图像**：$$\int_{D}d\omega=\int_{\partial D}\omega$$ 说的是——

> **内部的全部变化，等于边界上的净流出。**

这句话有两个方向可读，两个方向都有物理在背后站着。

**方向一：从左往右读（"局部累加 = 全局差值"）。** 这就是 Newton–Leibniz 定理的那根水管（原专栏 MP27 的图景）：一根位置坐标为 $$x\in[x_1,x_2]$$ 的水管，处处漏水、流速稳定，漏水的速度是 $$f(x)$$。问这段管子总共漏了多少水，有两种测法：

- **局部测法**：在每一个位置 $$x$$ 测"流速的变化率" $$f'(x)$$，再加起来，得 $$\int_{x_1}^{x_2}f'(x)\,dx$$。这是逐点操作，需要知道管内每一点。
- **全局测法**：只在两个端点各测一次流速，做差 $$f(x_2)-f(x_1)$$。这是边界操作，完全不需要知道管内发生了什么。

N–L 定理断言两者相等。把它当作 Stokes 定理的 $$n=1$$ 特例，定理的内容就一句话：**逐点累加内部的"变化率"，等于只读边界一次**。这也解释了定理为什么"省事"——它把"对整个区域的逐点积分"换成了"只沿边界的一次积分"，工作量从 $$n$$ 维降到 $$n-1$$ 维。

**方向二：从右往左读（"通量只认边界"）。** 这是 Gauss 的图景（MP27）：$$\Omega$$ 里有一个点电荷，它的电场向四面八方发散，发散的程度就是散度 $$\nabla\cdot\vec F$$。把散度在整个 $$\Omega$$ 上积分，得到的是区域内部的总源；而穿过边界 $$\partial\Omega$$ 的电场通量，与之精确相等。

关键在于**通量对曲面形状不敏感**：只要闭曲面把点电荷包围起来，无论它同胚于球面还是被揉成别的闭曲面，电通量都相同。**这是一个拓扑性质**——它只依赖"曲面把源围住了"这件事，不依赖曲面的具体几何。原专栏在讲 Stokes 之前花了四讲（MP19–MP22）堆拓扑，理由就在这里：**Stokes 定理的右端是几何量，左端的可变形性却是拓扑的**。同一个通量，对应的是一整族同调的曲面；这正是下一节经典题 4 要算的东西。

**定向：为什么积分号前面必须有"正方向"。** 积分 $$\int_{D}\omega$$ 是对"无穷小体积元"的带符号累加。要谈符号，"哪些方向算正"必须先定下来。定向就是这件事：在每一点连续地选一个"正基"。于是：

- $$\mathbb{R}^n$$、$$S^n$$、环面都可定向（有右手定则）；
- **Möbius 带**不可定向——它是"扭了一次"的带子，你在上面走一圈回来，右手定则变成了左手定则。不可定向的流形上**不存在处处非零的体积形式**，于是"带符号的体积元"无从定义，$$\int_M\omega$$ 这个词本身失去意义。这就是定向不是繁文缛节的理由：**没有定向，就没有积分**。

**边界定向：为什么要求"外法向排第一位"。** $$\partial D$$ 的定向不是凭空规定的，它由 $$D$$ 的定向诱导。约定的内容是：边界点处的一组基是正的，当且仅当把它和外法向拼起来后是 $$D$$ 的正基。它的物理含义是"从内部指向外部的方向优先"——这样约定出来的边界方向，恰好是"净流出"为正的方向。把约定改成内法向在前，定理右端会整体反号（注 3.3、注 3.12），可见约定和符号是一体的。

**几何 ↔ 物理 ↔ 代数的三线表。** 本章的主线是这三者对齐：

| 层面 | 对象 | 算子 | 关系 |
|---|---|---|---|
| 几何 | 区域 $$D$$ / 边界 $$\partial D$$ | $$\partial$$（取边界） | $$\partial^2=0$$（边界的边界是空） |
| 分析 | 形式 $$\omega$$ / $$d\omega$$ | $$d$$（外微分） | $$d^2=0$$（第 14 章） |
| 物理 | 通量 / 环量 / 源 / 旋 | $$\nabla\cdot,\ \nabla\times$$ | $$\int_{\partial D}\omega=\int_D d\omega$$ 统一全部积分定理 |

第三条正是本章把前两条焊在一起的地方：**$$\partial$$ 是宏观的边界算子，$$d$$ 是无穷小的边界算子，Stokes 定理说它们是同一个算子在两个尺度上的样子，互为转置**。

**一个反直觉但重要的点**。定理 3.21 的证明从头到尾没有用过长度、角度、内积。$$d$$ 不需要尺子（第 14 章的公理只有线性和 Leibniz），$$\partial$$ 更不需要（第 18 章只数顶点）。所以 Stokes 定理是一条**纯拓扑 + 纯代数**的定理，它不讲"曲面有多大"，只讲"区域里发生了什么、边界上流出了多少"。也正因为它不依赖度量，才能作 de Rham 定理的基石——第 28 章会把这个配对抬成一个关于同调群与上同调群的非退化双线性型。

## 五、经典问题精讲 (Classical Problems)

下面五题把第三节的机器逐一落到入口题 (a)(b)(c) 与它的后续上。每题标注考点与它在本章结构里的位置。

### 经典题 1：Green 公式的翻译（考点：$$d$$ 在 $$\mathbb{R}^2$$ 上的作用；位置：定理 3.11 的 $$n=2$$ 情形）

**题**。用定理 3.21 导出平面 Green 公式

$$\oint_{\partial D}P\,dx+Q\,dy=\iint_D\Bigl(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Bigr)dx\,dy,$$

其中 $$D\subset\mathbb{R}^2$$ 取标准定向，$$\partial D$$ 取逆时针定向。

**解**。取 1-形式

$$\omega=P\,dx+Q\,dy .$$

**第一步算 $$d\omega$$。** 由第 14 章 3.17 的公理 1 与 3：

$$d\omega=dP\wedge dx+dQ\wedge dy .$$

而 $$dP=\frac{\partial P}{\partial x}dx+\frac{\partial P}{\partial y}dy$$，$$dQ=\frac{\partial Q}{\partial x}dx+\frac{\partial Q}{\partial y}dy$$。代入，并用楔积的反交换 $$dy\wedge dx=-dx\wedge dy$$ 与 $$dx\wedge dx=dy\wedge dy=0$$：

$$dP\wedge dx=\Bigl(\frac{\partial P}{\partial x}dx+\frac{\partial P}{\partial y}dy\Bigr)\wedge dx=\frac{\partial P}{\partial y}\,dy\wedge dx=-\frac{\partial P}{\partial y}\,dx\wedge dy,$$

$$dQ\wedge dy=\Bigl(\frac{\partial Q}{\partial x}dx+\frac{\partial Q}{\partial y}dy\Bigr)\wedge dy=\frac{\partial Q}{\partial x}\,dx\wedge dy .$$

相加得

$$d\omega=\Bigl(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Bigr)dx\wedge dy .$$

**第二步把两边写成通常积分。** 由定义 3.10 与 定理 3.21：

$$\int_{\partial D}\omega=\oint_{\partial D}(P\,dx+Q\,dy),\qquad
\int_{D}d\omega=\iint_D\Bigl(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Bigr)dx\,dy,$$

后者是把 2-形式的积分读成二重积分（$$dx\wedge dy$$ 对应 $$dx\,dy$$，正号——因为 $$D$$ 的定向就是标准定向）。

**第三步核对定向。** 定理 3.21 要求 $$\partial D$$ 取诱导定向；由例 3.4，标准定向的平面区域诱导出的正是逆时针方向。题设的"逆时针"与之吻合，故无需补符号。

由定理 3.21 两端相等，Green 公式得证。$$\square$$

**关键 leap**：$$d(P\,dx+Q\,dy)$$ 的两个交叉项，一个出 $$+$$、一个出 $$-$$，差别全部来自楔积的反交换 $$dy\wedge dx=-dx\wedge dy$$。Green 公式里那个"$$\partial Q/\partial x-\partial P/\partial y$$"的减号，不是人为约定，而是**外积的反对称性**。这与第 14 章 $$d^2=0$$ 的证明里"一正一负相乘为零"是同一台机器。

### 经典题 2：入口题 (c) —— 球面上的积分（考点：用 Stokes 换掉积分域；位置：定理 3.21 + 定理 3.23 对偶）

**题**。设 $$\omega=x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy$$，$$S^2$$ 是单位球面取外法向定向，求 $$\int_{S^2}\omega$$。

**解**。

**第一步，算 $$d\omega$$。** 逐项用公理 1、3（$$d$$ 是反导子）：

$$d\bigl(x\,dy\wedge dz\bigr)=dx\wedge dy\wedge dz+x\,d(dy)\wedge dz+x\,dy\wedge d(dz)=dx\wedge dy\wedge dz,$$

因为 $$d(dy)=d^2y=0$$、$$d(dz)=d^2z=0$$（这里再次用到 $$d^2=0$$）。同理 $$d(y\,dz\wedge dx)=dy\wedge dz\wedge dx$$、$$d(z\,dx\wedge dy)=dz\wedge dx\wedge dy$$。而

$$dy\wedge dz\wedge dx=(-1)^{2}dx\wedge dy\wedge dz=dx\wedge dy\wedge dz,\qquad dz\wedge dx\wedge dy=dx\wedge dy\wedge dz$$

（对 $$(dx,dy,dz)$$ 做偶置换）。所以

$$d\omega=3\,dx\wedge dy\wedge dz .$$

**第二步，把 $$S^2$$ 换成 $$B^3$$。** 令 $$B^3=\{x^2+y^2+z^2\le1\}$$ 取标准定向。$$S^2=\partial B^3$$，且由 3.2 的"外法向在前"约定，$$\partial B^3$$ 的诱导定向正是外法向朝外的定向——与题设吻合。由定理 3.21：

$$\int_{S^2}\omega=\int_{\partial B^3}\omega=\int_{B^3}d\omega=3\int_{B^3}dx\wedge dy\wedge dz .$$

**第三步，读成通常体积分。** 由定义 3.10，$$\int_{B^3}dx\wedge dy\wedge dz=\operatorname{vol}(B^3)=\frac{4\pi}{3}$$。故

$$\int_{S^2}\omega=3\cdot\frac{4\pi}{3}=4\pi .$$

**第四步（核对，不进主证明）。** 直接限制到 $$S^2$$ 上：在 $$x^2+y^2+z^2=1$$ 上，$$x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy$$ 拉回成球面的面积形式，故积分就是单位球面面积 $$4\pi$$。与第一步一致。$$\square$$

**关键 leap**：注意到 $$\omega$$ 不是闭形式（$$d\omega=3\,dV\ne0$$），因此**不能**直接说"$$\omega$$ 限制到 $$S^2$$ 上后随便换一个同调曲面"。巧处在于把 $$S^2$$ **往下填成 $$B^3$$**，让 $$d\omega$$ 出场，于是积分变成算球的体积——一个初等积分。这也说明入口题 (c) 的提示里"不算限制积分"是可行的：定理 3.21 让你避开它。

### 经典题 3：Kelvin–Stokes 与环量（考点：$$d$$ 与旋度的词典；位置：定理 3.11 的 $$n=3$$、$$\omega\in\Omega^{1}$$）

**题**。(i) 用定理 3.21 导出 Kelvin–Stokes 公式 $$\oint_{\partial S}\vec F\cdot d\vec r=\iint_S(\nabla\times\vec F)\cdot d\vec S$$。(ii) 用它算 $$\oint_{C}(x\,dy-y\,dx)$$，$$C$$ 是逆时针单位圆。

**解 (i)**。把向量场 $$\vec F=(F^x,F^y,F^z)$$ 翻译成 1-形式

$$\omega_{\vec F}=F^x\,dx+F^y\,dy+F^z\,dz .$$

**算 $$d\omega_{\vec F}$$。** 与经典题 1 同样的算法，只是多一个变量。逐项：

$$dF^x\wedge dx=\frac{\partial F^x}{\partial y}dy\wedge dx+\frac{\partial F^x}{\partial z}dz\wedge dx
=-\frac{\partial F^x}{\partial y}dx\wedge dy-\frac{\partial F^x}{\partial z}dz\wedge dx,$$

$$dF^y\wedge dy=\frac{\partial F^y}{\partial z}dz\wedge dy+\frac{\partial F^y}{\partial x}dx\wedge dy
=-\frac{\partial F^y}{\partial z}dy\wedge dz+\frac{\partial F^y}{\partial x}dx\wedge dy,$$

$$dF^z\wedge dz=\frac{\partial F^z}{\partial x}dx\wedge dz+\frac{\partial F^z}{\partial y}dy\wedge dz
=-\frac{\partial F^z}{\partial x}dz\wedge dx+\frac{\partial F^z}{\partial y}dy\wedge dz .$$

按基 $$dy\wedge dz,\ dz\wedge dx,\ dx\wedge dy$$ 归并：

$$d\omega_{\vec F}=\Bigl(\frac{\partial F^z}{\partial y}-\frac{\partial F^y}{\partial z}\Bigr)dy\wedge dz
+\Bigl(\frac{\partial F^x}{\partial z}-\frac{\partial F^z}{\partial x}\Bigr)dz\wedge dx
+\Bigl(\frac{\partial F^y}{\partial x}-\frac{\partial F^x}{\partial y}\Bigr)dx\wedge dy .$$

三个系数恰好是 $$\nabla\times\vec F$$ 的三个分量：第一分量 $$\partial_yF^z-\partial_zF^y$$、第二分量 $$\partial_zF^x-\partial_xF^z$$、第三分量 $$\partial_xF^y-\partial_yF^x$$。而 $$dy\wedge dz,\ dz\wedge dx,\ dx\wedge dy$$ 正是"面积元向量"的三个分量（第 24 章 Hodge 星算子的对应）。于是 $$d\omega_{\vec F}$$ 就是 $$(\nabla\times\vec F)\cdot d\vec S$$。代入定理 3.21：

$$\oint_{\partial S}\vec F\cdot d\vec r=\int_{\partial S}\omega_{\vec F}=\int_S d\omega_{\vec F}=\iint_S(\nabla\times\vec F)\cdot d\vec S .\ \square$$

**解 (ii)**。取 $$\vec F$$ 使 $$\omega_{\vec F}=x\,dy-y\,dx$$，即 $$F^x=-y,\ F^y=x,\ F^z=0$$。由 (i)：

$$d\omega_{\vec F}=\Bigl(\frac{\partial x}{\partial x}-\frac{\partial(-y)}{\partial y}\Bigr)dx\wedge dy=(1-(-1))\,dx\wedge dy=2\,dx\wedge dy .$$

（也可直接算：$$d(x\,dy-y\,dx)=dx\wedge dy-dy\wedge dx=2\,dx\wedge dy$$。）设 $$D$$ 是单位圆盘取标准定向，$$C=\partial D$$ 取逆时针。由定理 3.21：

$$\oint_C(x\,dy-y\,dx)=\int_D 2\,dx\wedge dy=2\iint_D dx\,dy=2\pi .$$

**核对**：令 $$x=\cos t,\ y=\sin t$$，$$t:0\to2\pi$$，则 $$x\,dy-y\,dx=\cos^2t\,dt+\sin^2t\,dt=dt$$，积分 $$\int_0^{2\pi}dt=2\pi$$，一致。$$\square$$

**关键 leap**：把 $$\vec F\cdot d\vec r$$ 认成 $$\omega_{\vec F}$$ 的积分，于是 $$\nabla\times$$ 不再是"行列式记法"，而是 $$d$$ 在 1-形式上的作用。**Kelvin–Stokes 公式里的旋度，就是外微分**——这是第 24 章"$$d$$ 与 $$\nabla$$ 对齐"的直接兑现。

### 经典题 4：Gauss 散度定理与"通量只认边界"（考点：$$d$$ 与散度的词典、拓扑不变量；位置：定理 3.11 的 $$n=3$$、$$\omega\in\Omega^{2}$$）

**题**。(i) 用定理 3.21 导出 Gauss 散度定理。(ii) 设 $$\Omega\subset\mathbb{R}^3$$ 中 $$\nabla\cdot\vec F=0$$，$$S_1,S_2\subset\Omega$$ 是两张同调（即 $$S_1-S_2$$ 是 $$\Omega$$ 内某区域的全部边界）的闭曲面，证明通过两者的通量相等。

**解 (i)**。把向量场翻译成 2-形式

$$\omega=F^x\,dy\wedge dz+F^y\,dz\wedge dx+F^z\,dx\wedge dy .$$

**算 $$d\omega$$。** 逐项：

$$d\bigl(F^x\,dy\wedge dz\bigr)=\frac{\partial F^x}{\partial x}dx\wedge dy\wedge dz,$$

因为另外两项含 $$d(dy)$$ 或 $$d(dz)$$，由 $$d^2=0$$ 归零。同理

$$d\bigl(F^y\,dz\wedge dx\bigr)=\frac{\partial F^y}{\partial y}dy\wedge dz\wedge dx=\frac{\partial F^y}{\partial y}dx\wedge dy\wedge dz,$$

$$d\bigl(F^z\,dx\wedge dy\bigr)=\frac{\partial F^z}{\partial z}dz\wedge dx\wedge dy=\frac{\partial F^z}{\partial z}dx\wedge dy\wedge dz .$$

（后两行用偶置换把基整理成 $$dx\wedge dy\wedge dz$$。）相加：

$$d\omega=\Bigl(\frac{\partial F^x}{\partial x}+\frac{\partial F^y}{\partial y}+\frac{\partial F^z}{\partial z}\Bigr)dx\wedge dy\wedge dz=(\nabla\cdot\vec F)\,dV .$$

而 $$\int_{\partial\Omega}\omega$$ 的展开式正是 $$\iint_{\partial\Omega}(F^x\,dy\,dz+F^y\,dz\,dx+F^z\,dx\,dy)$$——这就是"通量"。由定理 3.21：

$$\iint_{\partial\Omega}(F^x\,dy\,dz+F^y\,dz\,dx+F^z\,dx\,dy)=\iiint_\Omega(\nabla\cdot\vec F)\,dx\,dy\,dz .\ \square$$

**解 (ii)**。设 $$R\subset\Omega$$ 是使 $$\partial R=S_1-S_2$$ 的区域（两者定向都取外法向；若 $$S_1$$ 在外则 $$S_1-S_2=\partial R$$）。通量记作

$$\Phi(S)=\iint_S(F^x\,dy\,dz+F^y\,dz\,dx+F^z\,dx\,dy)=\int_S\omega .$$

由定理 3.21 与 (i)：

$$\Phi(S_1)-\Phi(S_2)=\int_{S_1-S_2}\omega=\int_{\partial R}\omega=\int_R d\omega=\int_R(\nabla\cdot\vec F)\,dV=0,$$

因为 $$\nabla\cdot\vec F\equiv0$$。故 $$\Phi(S_1)=\Phi(S_2)$$。$$\square$$

**关键 leap**：这一问是本章"拓扑"味道最重的地方。通量相等**没有用到 $$\Omega$$ 的任何度量信息**，只用到了 $$S_1-S_2$$ 是某个区域的边界（同调）与 $$d\omega=0$$。把 $$S_2$$ 形变到 $$S_1$$ 的整个过程中，通量不变——**通量是定义在同调类上的量**。这正是原专栏 MP19–MP22 那四讲拓扑的兑现点。

### 经典题 5：闭形式的积分只依赖上同调类（考点：配对降落到同调/上同调上；位置：定理 3.23 的推论，通向第 28 章）

**题**。设 $$M$$ 是定向 $$n$$ 维流形（可带边），$$\omega\in\Omega^{k}(M)$$，$$c\in C_k(M)$$。(i) 若 $$\omega=d\eta$$ 且 $$\partial c=0$$，证明 $$\int_c\omega=0$$。(ii) 若 $$d\omega=0$$ 且 $$c-c'=\partial b$$，证明 $$\int_c\omega=\int_{c'}\omega$$。(iii) 解释这两个结论为什么说明"配对 $$\langle c,\omega\rangle\mapsto\int_c\omega$$ 只依赖 $$[c]\in H_k$$ 与 $$[\omega]\in H^{k}$$"。

**解 (i)**。由定理 3.20：

$$\int_c\omega=\int_c d\eta=\int_{\partial c}\eta=0,$$

因为 $$\partial c=0$$。$$\square$$

**解 (ii)**。由定理 3.20：

$$\int_{c-c'}\omega=\int_{\partial b}\omega=\int_b d\omega=\int_b 0=0,$$

因为 $$d\omega=0$$。故 $$\int_c\omega-\int_{c'}\omega=0$$。$$\square$$

**解 (iii)**。(i) 说明：把 $$\omega$$ 换成同一条上同调类里的另一个代表（即差一个恰当形式 $$d\eta$$），且 $$c$$ 是循环（$$\partial c=0$$）时，积分不变。故 $$\int_c\omega$$ 只依赖 $$[\omega]\in H^{k}_{dR}(M)=\ker d/\operatorname{im}d$$。(ii) 说明：把 $$c$$ 换成同一条同调类里的另一个代表时积分不变。故 $$\int_c\omega$$ 只依赖 $$[c]\in H_k(M)=\ker\partial/\operatorname{im}\partial$$。合起来，$$\int$$ 诱导出一个良定义的双线性映射

$$\langle\,\cdot\,,\,\cdot\,\rangle:\ H^{k}_{dR}(M)\times H_k(M)\longrightarrow\mathbb{R},\qquad
\bigl([\omega],[c]\bigr)\longmapsto\int_c\omega .$$

**注意这里出现的两个商**：$$\ker d/\operatorname{im}d$$（第 14 章的 $$d$$）与 $$\ker\partial/\operatorname{im}\partial$$（第 18 章的 $$\partial$$）。它们是本章 定理 3.23 那个伴随关系在对偶空间上留下的痕迹——**$$d$$ 与 $$\partial$$ 互为转置，于是它们的核与像也互为转置**。

**接到下一章**。(iii) 证明了这个配对良定义，但一个字也没说它**非退化**。事实是：当 $$M$$ 是光滑紧流形时，这个配对非退化，对应地有 $$H^{k}_{dR}(M)\cong H^k(M;\mathbb{R})$$——**微分形式的同调与拓扑的同调算了同一件事**。这就是 de Rham 定理，也正是第 28 章的标题。本章到此为止地把 $$\partial$$ 与 $$d$$ 配成对；第 28 章会把这对配对做成一个同构。


## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 把定理 3.21 取成 $$n=1$$、$$\omega=f$$（$$0$$-形式，即函数）：写出 $$\partial[a,b]$$ 按定义 3.2 的定向，并验证两端相等。这一条就是 Newton–Leibniz 公式。

**基2.** 取 $$\sigma_3\subset\mathbb{R}^3$$（顶点 $$0,e_1,e_2,e_3$$），$$\psi=x\,dy\wedge dz$$。直接算出 $$\int_{\partial\sigma_3}\psi$$ 与 $$\int_{\sigma_3}d\psi$$，验证定理 3.11。

**基3.** 对正方形 $$[0,1]^2$$，按 3.2 的"外法向在前"约定逐条边确定方向，写出它的定向边界链，并判断这个链是顺时针还是逆时针。

**基4.** 判断下列 $$\mathbb{R}^2$$ 上的 1-形式哪些是闭的、哪些是恰当的；并算出每一个沿逆时针单位圆的积分：$$\alpha=x\,dy-y\,dx$$；$$\beta=\dfrac{x\,dy-y\,dx}{x^2+y^2}$$；$$\gamma=e^{x}\cos y\,dx-e^{x}\sin y\,dy$$。

### 竞赛（本课目标难度）

**竞1.** 设 $$C$$ 是逆时针简单闭曲线。用定理 3.21 计算 $$\displaystyle\oint_{C}\frac{x\,dy-y\,dx}{x^2+y^2}$$，分两种情形：$$C$$ 不包围原点；$$C$$ 包围原点。

**竞2.** 设 $$\Omega\subset\mathbb{R}^3$$ 单连通，$$\vec F$$ 光滑且 $$\nabla\times\vec F=\vec 0$$。用定理 3.21 证明曲线积分 $$\int_A^B\vec F\cdot d\vec r$$ 只依赖端点，从而 $$\vec F$$ 是某个函数的梯度。

**竞3.** 用定理 3.21 计算 $$\displaystyle\int_{S^2}x\,dy\wedge dz$$，再用对称性写出 $$\displaystyle\int_{S^2}\bigl(x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy\bigr)$$。

**竞4.** 设 $$D\subset\mathbb{R}^n$$ 是紧区域，证明

$$\int_{\partial D}\sum_{i=1}^{n}(-1)^{\,i-1}x_i\,dx^1\wedge\cdots\widehat{dx^i}\cdots\wedge dx^n=n\cdot\operatorname{vol}(D).$$

**竞5.** 证明不存在光滑映射 $$f:B^3\to S^2$$ 使得 $$f$$ 在 $$\partial B^3=S^2$$ 上是恒等映射。（提示：取 $$S^2$$ 的面积形式 $$\omega$$，注意它是 $$S^2$$ 上的 2-形式，故 $$d\omega=0$$。）

### 研究（通向下一章）

**研1.** 定义配对 $$\langle c,\omega\rangle=\int_c\omega$$（$$c\in C_k(M)$$，$$\omega\in\Omega^{k}(M)$$）。(a) 证明它双线性；(b) 证明 $$d\omega=0$$ 时 $$\langle\partial c,\omega\rangle=0$$，$$\partial c=0$$ 时 $$\langle c,d\eta\rangle=0$$；(c) 解释为什么 $$\int_{S^1}d\theta=2\pi$$（$$\theta$$ 是极角）说明 $$d\theta$$ 在 $$\mathbb{R}^2\setminus\{0\}$$ 上闭但不恰当，并说明它与 $$\mathbb{R}^2\setminus\{0\}$$ 不单连通的关系。

**研2.** (a) 证明 $$H^{0}_{dR}(M)=\{f\in C^{\infty}(M):df=0\}$$ 同构于 $$\mathbb{R}^{m}$$，其中 $$m$$ 是 $$M$$ 的连通分支数；(b) 比较它与 $$H_0(M)$$；(c) 用一句话说明为什么这是一次"微分形式算出了拓扑"。

### 解答 (Solutions)

**解 基1.** $$\omega=f$$ 是 0-形式。$$M=[a,b]$$ 取 $$x$$ 轴正向，例 3.4 已经算过 $$\partial[a,b]=[b]-[a]$$（$$b$$ 取 $$+1$$、$$a$$ 取 $$-1$$）。0-形式在 0-链上的积分就是求值：$$\int_{[b]}[f]=f(b),\ \int_{[a]}f=f(a)$$，故

$$\int_{\partial[a,b]}f=f(b)-f(a).$$

另一侧：$$df=f'(x)dx$$ 是 1-形式，由定义 3.10，$$\int_{[a,b]}df=\int_a^bf'(x)\,dx$$。定理 3.21 断言两者相等，即

$$\int_a^bf'(x)\,dx=f(b)-f(a),$$

正是 Newton–Leibniz 公式。$$\square$$

**解 基2.** 先算右端。$$d\psi=dx\wedge dy\wedge dz$$，故

$$\int_{\sigma_3}d\psi=\int_{\sigma_3}dx_1dx_2dx_3=\operatorname{vol}(\sigma_3)=\frac{1}{3!}=\frac16 .$$

再算左端。由定义 3.7，$$\partial\sigma_3=f_0-f_1+f_2-f_3$$，其中（由定义 3.6）

$$f_0(u)=(1-u_1-u_2,\ u_1,\ u_2),\quad f_1(u)=(0,u_1,u_2),\quad f_2(u)=(u_1,0,u_2),\quad f_3(u)=(u_1,u_2,0).$$

逐面拉回 $$\psi=x\,dy\wedge dz$$：

- $$f_0$$：$$x=1-u_1-u_2$$，$$dy=du_1$$，$$dz=du_2$$，故 $$f_0^{*}\psi=(1-u_1-u_2)\,du_1\wedge du_2$$，
$$\int_{\sigma_2}f_0^{*}\psi=\int_0^1\!\!\int_0^{1-u_2}(1-u_1-u_2)\,du_1du_2=\int_0^1\frac{(1-u_2)^2}{2}du_2=\frac16 .$$
（内层积分：$$\int_0^{1-u_2}(1-u_1-u_2)du_1=(1-u_2)^2-\frac{(1-u_2)^2}{2}=\frac{(1-u_2)^2}{2}$$。）
- $$f_1$$：$$x\equiv0$$，故 $$f_1^{*}\psi=0$$，积分为 $$0$$。
- $$f_2$$：$$dy=d(0)=0$$，故 $$f_2^{*}\psi=0$$。
- $$f_3$$：$$dz=d(0)=0$$，故 $$f_3^{*}\psi=0$$。

于是

$$\int_{\partial\sigma_3}\psi=\frac16-0+0-0=\frac16=\int_{\sigma_3}d\psi .$$

两端相等，定理 3.11 在这个例子上成立。$$\square$$

**解 基3.** 记 $$N$$ 为外法向，$$u$$ 为沿边的方向向量。由 3.2，$$u$$ 是边的正方向当且仅当 $$(N,u)$$ 是 $$\mathbb{R}^2$$ 的正基，即 $$\det(N,u)>0$$。

- 底边 $$y=0$$：$$N=-e_2$$。$$\det(-e_2,u)=-\det(e_2,u)=-(-u_1)=u_1$$，故要求 $$u_1>0$$：从 $$(0,0)$$ 到 $$(1,0)$$。
- 右边 $$x=1$$：$$N=+e_1$$。$$\det(e_1,u)=u_2>0$$：从 $$(1,0)$$ 到 $$(1,1)$$。
- 顶边 $$y=1$$：$$N=+e_2$$。$$\det(e_2,u)=-u_1>0$$，即 $$u_1<0$$：从 $$(1,1)$$ 到 $$(0,1)$$。
- 左边 $$x=0$$：$$N=-e_1$$。$$\det(-e_1,u)=-u_2>0$$，即 $$u_2<0$$：从 $$(0,1)$$ 到 $$(0,0)$$。

四条边首尾相接成

$$\partial[0,1]^2=(0,0)\to(1,0)\to(1,1)\to(0,1)\to(0,0),$$

即**逆时针**。这与例 3.4 在 $$\sigma_2$$ 上得到的方向一致，也与 $$\partial^2[0,1]^2=0$$（四个顶点两两抵消）一致。$$\square$$

**解 基4.**

**$$\alpha=x\,dy-y\,dx$$**：$$d\alpha=dx\wedge dy-dy\wedge dx=2\,dx\wedge dy\ne0$$，故 $$\alpha$$ **不闭**，因此也**不恰当**（恰当必闭，见第 14 章）。沿单位圆的积分即经典题 3 的 (ii)：$$\oint\alpha=2\pi$$。

**$$\beta=\dfrac{x\,dy-y\,dx}{x^2+y^2}$$**：记 $$r^2=x^2+y^2$$。直接用第 14 章的商法则（对函数 $$\frac1{r^2}$$ 与形式 $$\alpha$$ 用 Leibniz）。计算

$$d\Bigl(\frac1{r^2}\Bigr)=-\frac{2x\,dx+2y\,dy}{r^4},\qquad
d\beta=d\Bigl(\frac1{r^2}\Bigr)\wedge\alpha+\frac1{r^2}d\alpha .$$

第一项：$$-\frac{2(x\,dx+y\,dy)}{r^4}\wedge(x\,dy-y\,dx)=-\frac{2}{r^4}\bigl(x^2dx\wedge dy-xy\,dx\wedge dx+xy\,dy\wedge dy-y^2dy\wedge dx\bigr)$$。其中 $$dx\wedge dx=dy\wedge dy=0$$、$$dy\wedge dx=-dx\wedge dy$$，故第一项 $$=-\frac{2(x^2+y^2)}{r^4}dx\wedge dy=-\frac{2}{r^2}dx\wedge dy$$。第二项：$$\frac1{r^2}\cdot 2dx\wedge dy=\frac{2}{r^2}dx\wedge dy$$。相加为零：在 $$\mathbb{R}^2\setminus\{0\}$$ 上 $$d\beta=0$$，**闭**。沿单位圆 $$r^2=1$$，$$\beta$$ 就是 $$\alpha$$，故 $$\oint\beta=2\pi$$；由经典题 5(i)，积分非零说明 $$\beta$$ **不恰当**（它不是任何函数的微分）。

**$$\gamma=e^{x}\cos y\,dx-e^{x}\sin y\,dy$$**：逐项算

$$d\bigl(e^x\cos y\,dx\bigr)=\frac{\partial(e^x\cos y)}{\partial y}dy\wedge dx=-e^x\sin y\,dy\wedge dx=e^{x}\sin y\,dx\wedge dy,$$

$$d\bigl(-e^{x}\sin y\,dy\bigr)=-\frac{\partial(e^{x}\sin y)}{\partial x}dx\wedge dy=-e^{x}\sin y\,dx\wedge dy .$$

相加为零，**闭**。又直接验证

$$d\bigl(e^{x}\cos y\bigr)=e^{x}\cos y\,dx-e^{x}\sin y\,dy=\gamma,$$

故 $$\gamma$$ **恰当**，沿任何闭曲线积分为零：$$\oint\gamma=0$$（也可直接由经典题 5(i)：恰当形式配循环得零）。$$\square$$

**解 竞1.** 记 $$\beta=\dfrac{x\,dy-y\,dx}{x^2+y^2}$$，基4 已算得它在 $$\mathbb{R}^2\setminus\{0\}$$ 上闭。

**情形一：$$C$$ 不包围原点。** 设 $$R$$ 是 $$C$$ 围成的区域。因 $$C$$ 不包围原点，$$0\notin R$$，$$\beta$$ 在 $$R$$ 的闭包附近处处有定义且 $$d\beta=0$$。由定理 3.21（取 $$D=R$$，$$\omega=\beta$$，这里 $$\partial R=C$$ 且定向吻合）：

$$\oint_C\beta=\int_R d\beta=0 .$$

**情形二：$$C$$ 包围原点。** 取充分小的 $$\varepsilon>0$$，使半径 $$\varepsilon$$ 的圆 $$C_\varepsilon$$ 完全落在 $$C$$ 内部。设 $$R$$ 是 $$C$$ 与 $$C_\varepsilon$$ 之间的环形区域，则 $$R$$ 是带边流形，且按"外法向在前"

$$\partial R=C-C_\varepsilon$$

（$$C$$ 取逆时针、$$C_\varepsilon$$ 取逆时针；因为 $$C_\varepsilon$$ 的外法向相对 $$R$$ 是指向圆心的，故 $$C_\varepsilon$$ 在 $$\partial R$$ 里带负号）。$$\beta$$ 在 $$R$$ 上处处有定义且 $$d\beta=0$$，由定理 3.21：

$$0=\int_R d\beta=\int_{\partial R}\beta=\oint_C\beta-\oint_{C_\varepsilon}\beta .$$

于是 $$\oint_C\beta=\oint_{C_\varepsilon}\beta$$。在 $$C_\varepsilon$$ 上 $$x^2+y^2=\varepsilon^2$$，故 $$\beta=\frac1{\varepsilon^2}(x\,dy-y\,dx)$$，由经典题 3(ii)（把半径换成 $$\varepsilon$$：$$\oint_{C_\varepsilon}(x\,dy-y\,dx)=2\pi\varepsilon^2$$）：

$$\oint_C\beta=\frac{1}{\varepsilon^2}\cdot2\pi\varepsilon^2=2\pi .\ \square$$

**关键 leap**：$$\beta$$ 在原点没有定义，所以不能直接对 $$C$$ 围成的整块区域用定理 3.21。办法是**在原点处挖一个小洞**，把"有洞的区域"变成带边流形 $$R$$；于是 $$C$$ 与 $$C_\varepsilon$$ 成为同一条边界链的两半，积分随之相等。这就是"用 Stokes 处理奇点"的标准手法，$$C_\varepsilon$$ 起的作用是让定理可用的"探针"。

**解 竞2.** "只依赖端点"等价于"任何闭曲线上的积分为零"：若对每条闭曲线 $$\oint=0$$，则对任意两条从 $$A$$ 到 $$B$$ 的曲线 $$\Gamma_1,\Gamma_2$$，$$\Gamma_1-\Gamma_2$$ 是闭曲线，故 $$\int_{\Gamma_1}=\int_{\Gamma_2}$$。

先证闭曲线上的积分为零。设 $$\Gamma$$ 是 $$\Omega$$ 内闭曲线。把 $$\vec F$$ 翻成 1-形式 $$\omega_{\vec F}$$，由经典题 3(i)，$$d\omega_{\vec F}$$ 的三个系数正是 $$\nabla\times\vec F$$ 的三个分量，故 $$\nabla\times\vec F=0$$ 等价于 $$d\omega_{\vec F}=0$$。

$$\Omega$$ **单连通**意味着 $$\Gamma$$ 是 $$\Omega$$ 内某张曲面 $$S$$ 的边界（可以把 $$\Gamma$$ 连续收缩成一点，收缩过程扫出的曲面就是 $$S$$；这一步是单连通的定义的直接推论）。于是由定理 3.21：

$$\oint_{\Gamma}\omega_{\vec F}=\int_{\partial S}\omega_{\vec F}=\int_S d\omega_{\vec F}=\int_S 0=0 .$$

于是积分与路径无关。固定 $$x_0\in\Omega$$，定义 $$\varphi(x)=\int_{x_0}^{x}\omega_{\vec F}$$（沿任一道路，良定义已证）。取 $$x$$ 沿 $$e_1$$ 方向的小位移 $$t$$，则 $$\varphi(x+te_1)-\varphi(x)=\int_0^tF^x(x+se_1)\,ds$$，两边对 $$t$$ 求导得 $$\partial_1\varphi=F^x$$；同理 $$\partial_2\varphi=F^y$$、$$\partial_3\varphi=F^z$$。故 $$\vec F=\nabla\varphi$$。$$\square$$

**关键 leap**：单连通性不是用来"让定理 3.21 成立"的（定理 3.21 对任何曲面都成立），而是用来保证**每一条闭曲线都能被一张曲面填满**。有了这一步，"$$\nabla\times\vec F=0$$"（局部信息）才能升级成"$$\vec F=\nabla\varphi$$"（全局信息）。

**解 竞3.** 令 $$\omega=x\,dy\wedge dz$$，则 $$d\omega=dx\wedge dy\wedge dz$$（其它两项含 $$d(dy)$$ 或 $$d(dz)$$，由 $$d^2=0$$ 归零）。由定理 3.21，$$S^2=\partial B^3$$（外法向定向吻合）：

$$\int_{S^2}x\,dy\wedge dz=\int_{\partial B^3}\omega=\int_{B^3}d\omega=\int_{B^3}dx\wedge dy\wedge dz=\operatorname{vol}(B^3)=\frac{4\pi}{3}.$$

对另外两项，做变量轮换 $$x\to y\to z\to x$$：球体与球面在两个轮换下都保持不变（都是偶置换），于是三项的积分相等，各为 $$\frac{4\pi}{3}$$，合计

$$\int_{S^2}\bigl(x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy\bigr)=3\cdot\frac{4\pi}{3}=4\pi .\ \square$$

**关键 leap**：单看三项之和 $$\omega$$ 时，可以直接用 $$d\omega=3\,dV$$ 一步到位（经典题 2）；但若只给一项，就要注意 $$\omega_1=x\,dy\wedge dz$$ 的 $$d\omega_1=dx\wedge dy\wedge dz$$ 也恰好是体积形式，所以单项与三项之和只差一个系数 $$3$$。用对称性把三项拆开算，是处理"带对称的积分"的标准技巧。

**解 竞4.** 记

$$\omega=\sum_{i=1}^{n}(-1)^{\,i-1}x_i\,dx^1\wedge\cdots\widehat{dx^i}\cdots\wedge dx^n=\sum_{i=1}^{n}(-1)^{\,i-1}x_i\,W_i,\qquad W_i=dx^1\wedge\cdots\widehat{dx^i}\cdots\wedge dx^n .$$

逐项算 $$d\bigl((-1)^{i-1}x_iW_i\bigr)=(-1)^{i-1}dx_i\wedge W_i$$（因为 $$dW_i$$ 是 $$(n-1+1)=n$$ 形式的微分、落在 $$\Omega^{n+1}=0$$ 里，故此项为零——它含 $$d(dx^k)$$；具体地说 $$dW_i$$ 的每一项都含某个 $$d^2x^k=0$$）。而

$$dx_i\wedge W_i=(-1)^{\,i-1}dx^1\wedge\cdots\wedge dx^n,$$

理由：把 $$dx_i$$ 从最前面移到第 $$i$$ 位，要穿过 $$W_i$$ 中位于它左边的 $$i-1$$ 个因子，出 $$(-1)^{i-1}$$。两次 $$(-1)^{i-1}$$ 相乘得 $$+1$$，故

$$d\bigl((-1)^{i-1}x_iW_i\bigr)=dx^1\wedge\cdots\wedge dx^n .$$

对 $$i=1,\dots,n$$ 求和：

$$d\omega=n\,dx^1\wedge\cdots\wedge dx^n .$$

由定理 3.21 与定义 3.10：

$$\int_{\partial D}\omega=\int_D d\omega=n\int_D dx_1\cdots dx_n=n\cdot\operatorname{vol}(D).\ \square$$

（$$n=3$$ 时 $$\omega=x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy$$，结论 $$\int_{\partial D}\omega=3\operatorname{vol}(D)$$ 就是经典题 2 的第四步与竞3。）

**解 竞5.** 设这样的 $$f$$ 存在。取

$$\omega=x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy,$$

把它看成 $$S^2$$ 上的 2-形式（即把 $$\mathbb{R}^3$$ 上的 $$\omega$$ 限制到 $$S^2$$；由基4 的算法，$$S^2$$ 上 $$\omega$$ 处处非零，它就是面积形式）。$$S^2$$ 是 2 维的，其上不存在非零的 3-形式，故 $$d\omega=0$$（作为 $$S^2$$ 上的形式）。

考虑 2-形式 $$f^{*}\omega$$，它是 $$B^3$$ 上的 2-形式。由定理 3.15（拉回与 $$d$$ 交换）：

$$d\bigl(f^{*}\omega\bigr)=f^{*}(d\omega)=f^{*}0=0 .$$

$$B^3$$ 的边界是 $$S^2$$，取外法向定向。由定理 3.21：

$$\int_{S^2}f^{*}\omega=\int_{\partial B^3}f^{*}\omega=\int_{B^3}d\bigl(f^{*}\omega\bigr)=\int_{B^3}0=0 .$$

另一方面，$$f$$ 在 $$\partial B^3=S^2$$ 上是恒等映射，故 $$f^{*}\omega$$ 限制到 $$S^2$$ 上就是 $$\omega$$ 本身，于是

$$\int_{S^2}f^{*}\omega=\int_{S^2}\omega=4\pi,$$

最后一步用了经典题 2。得到 $$4\pi=0$$，矛盾。故这样的 $$f$$ 不存在。$$\square$$

**关键 leap**：要点是**把 $$\omega$$ 看成 $$S^2$$ 上的形式而不是 $$\mathbb{R}^3$$ 上的形式**。作为 $$\mathbb{R}^3$$ 上的 2-形式，$$d\omega=3\,dV\ne0$$，整条论证会立刻失效；一旦限制到 2 维的 $$S^2$$ 上，"最高次形式自动闭"就让 $$d\omega=0$$ 无偿成立。这个技巧叫"用上同调类的非平凡性证不可能性"，是代数拓扑的基本武器之一。

**解 研1.**

**(a) 双线性。** $$c\mapsto\int_c\omega$$ 关于 $$c$$ 线性，因为定义 3.19 就是按系数线性地定义的；$$\omega\mapsto\int_c\omega$$ 关于 $$\omega$$ 线性，因为拉回 $$s^{*}$$ 与外积、求和都线性（定义 3.14），且积分线性（定义 3.10）。

**(b)** 由定理 3.20（$$\partial$$ 与 $$d$$ 的伴随关系）：

$$\langle\partial c,\omega\rangle=\int_{\partial c}\omega=\int_c d\omega=0\qquad(d\omega=0),$$

$$\langle c,d\eta\rangle=\int_c d\eta=\int_{\partial c}\eta=0\qquad(\partial c=0).$$

**(c)** 在 $$\mathbb{R}^2\setminus\{0\}$$ 上，极角 $$\theta$$ 是局部定义的，$$d\theta=\dfrac{-y\,dx+x\,dy}{x^2+y^2}$$ 是全局定义的 1-形式。由基4 的计算（$$\beta$$ 与之仅差符号），$$d(d\theta)=0$$ 在整个 $$\mathbb{R}^2\setminus\{0\}$$ 上成立，故 $$d\theta$$ 闭。若它恰当，即 $$d\theta=d\eta$$，则由经典题 5(i)（$$\partial S^1=0$$）应有 $$\int_{S^1}d\theta=0$$。但直接计算：沿单位圆 $$x=\cos t,\ y=\sin t$$，

$$\int_{S^1}d\theta=\int_0^{2\pi}dt=2\pi\ne0 .$$

所以 $$d\theta$$ **闭但不恰当**。这与 $$\mathbb{R}^2\setminus\{0\}$$ **不单连通**是一回事：Poincaré 引理说"在可缩（特别地，单连通的开星形）区域上，闭 1-形式必恰当"；$$\mathbb{R}^2\setminus\{0\}$$ 中间有个洞，围绕洞的闭曲线 $$S^1$$ 不是任何二维区域的边界，上面的论证就无从启动。**这个洞就是 $$H_1(\mathbb{R}^2\setminus\{0\})\cong\mathbb{Z}$$ 的生成元。**

**接下一章**：(b)(c) 合起来说明，$$\int$$ 这个配对在 $$\ker d$$ 与 $$\ker\partial$$ 上只读出"商掉像之后"的信息——它定义在 $$H^{k}_{dR}\times H_k$$ 上。第 28 章要证的 de Rham 定理说：这个配对非退化，故 $$H^{k}_{dR}(M)\cong H^{k}(M;\mathbb{R})$$。

**解 研2.**

**(a)** 0-形式就是函数。$$df=0$$ 意味着沿着 $$M$$ 上任意道路 $$f$$ 的取值不变（因为沿道路 $$\gamma$$，$$\frac{d}{dt}f(\gamma(t))=df(\gamma'(t))=0$$）；反之 $$f$$ 在每条道路上都不变则 $$df=0$$。于是"$$df=0$$"等价于"$$f$$ 在 $$M$$ 的每个连通分支上是常数"。若 $$M$$ 有 $$m$$ 个连通分支，则这样的函数由 $$m$$ 个实常数决定，即

$$\{f:df=0\}\cong\mathbb{R}^{m}.$$

而 0-形式的恰当形式只有零（因为 $$\operatorname{im}d$$ 在 $$\Omega^{0}$$ 里只能来自 $$\Omega^{-1}=\{0\}$$ 的 $$d$$）。故

$$H^{0}_{dR}(M)=\ker(d:\Omega^0\to\Omega^1)\big/\operatorname{im}(d:\Omega^{-1}\to\Omega^0)=\{f:df=0\}/\{0\}\cong\mathbb{R}^{m}.$$

**(b)** $$H_0(M)$$ 是 0 维同调群，其循环空间是所有 0-链（$$M$$ 中的有限点集），边缘是那些"成对出现、系数相消"的点；商掉后，每个连通分支贡献一个自由生成元（同一分支内任意两点之差是某条 1-单形边界的边缘）。故

$$H_0(M)\cong\mathbb{Z}^{m}.$$

两者同秩 $$m$$，且是**对偶**的：$$H^{0}_{dR}(M)\cong\mathbb{R}^{m}\cong\operatorname{Hom}_{\mathbb{Z}}(H_0(M),\mathbb{R})$$，配对正是 $$\langle[f],[p]\rangle=f(p)$$。

**(c)** 由 (a)(b)：右侧 $$H_0(M)$$ 是纯拓扑的量（只数"$$M$$ 分成几块"），左侧 $$H^{0}_{dR}(M)$$ 是用微分方程 $$df=0$$ 解出来的量，两者同构。这说明**微分形式解出的方程，算出了流形的拓扑**——这是本课第一次看到"分析算拓扑"。

**接下一章**：(a) 用的是 $$df=0$$ 这个具体方程，只算出了第 0 层。把同一套 $$H^{k}_{dR}=\ker d/\operatorname{im}d$$ 对每个 $$k$$ 都算一遍，再证明它与奇异同调 $$H_k$$ 配对非退化——这就是 de Rham 定理，也是第 28 章的起点。

## 七、Takeaway 与延伸 (Takeaways)

1. **一条定理，四个公式。** $$\int_{\partial M}\omega=\int_M d\omega$$ 在 $$n=1$$ 是 Newton–Leibniz，$$n=2$$ 平面是 Green，$$n=3$$ 把 $$\omega$$ 取 1-形式得 Kelvin–Stokes、取 2-形式得 Gauss。它们不是"四条相似的定理"，而是同一条定理在四个维数上的投影。判断依据不在公式长相，而在**$$\omega$$ 的次数**与**区域维数**是否配套。

2. **$$\partial$$ 与 $$d$$ 互为伴随。** 定理 3.23：$$\langle\partial c,\omega\rangle=\langle c,d\omega\rangle$$。第 14 章的 $$d^2=0$$（分析侧）与第 18 章的 $$\partial^2=0$$（拓扑侧）在这里被焊在一起——它们是同一台算子的两个尺度，互为转置。**这是全书暗线的正式闭合点。**

3. **三处"差一"是同一件事。** $$d$$ 升一格、$$\partial$$ 降一格、$$\partial M$$ 比 $$M$$ 低一维——这不是三个巧合。它说的正是"升与降在配对里抵消"，从而积分只能定义在"$$k$$-形式配 $$k$$ 维域"上。

4. **证明的骨架是 FTC + 拉回 + 符号对齐。** 定理 3.11 的证明只做了一件事：右端用 Newton–Leibniz 吐出 $$n+1$$ 个"上下限之差"，左端按 $$\partial=\sum(-1)^if_i$$ 展开成 $$n+1$$ 个面积分，然后逐项对上。其中坐标面对应下限、斜面对应上限，而两组符号（$$d$$ 的 $$(-1)^{j-1}$$ 与换元的 $$(-1)^{j+1}$$）相乘为 $$+1$$——**这个 $$+1$$ 就是"边界定向约定"必须与"$$d$$ 的符号约定"配套的全部理由**（注 3.12）。

5. **定理不需要度量。** 定理 3.21 的证明没有用到长度、角度、内积。所以 Stokes 定理是纯拓扑 + 纯代数的：它只讲"区域里发生了什么、边界上流出了多少"。正因如此，它才能作 de Rham 定理的基石。

**下一章的悬念。** 经典题 5 与研1 证明了一个"降落到商空间"的配对：$$\int$$ 只依赖 $$[c]\in H_k$$ 与 $$[\omega]\in H^{k}_{dR}$$。可我们**只证明了它良定义**，一个字也没说它非退化——即：会不会有一整类非零的 $$[\omega]$$ 对所有 $$[c]$$ 都给出零？答案是"不会"（当 $$M$$ 是紧光滑流形时），而这需要一整章的机器去证：Poincaré 引理、Mayer–Vietoris 序列、de Rham 复形的同伦不变性。**第 28 章 de Rham 上同调**会把本章的这条配对做成一个同构

$$H^{k}_{dR}(M)\cong H^{k}(M;\mathbb{R}),$$

从而回答一个听起来不可思议的问题：**为什么解微分方程能算出洞的个数。**

**延伸阅读。**

- 原专栏：MP27（标准单形上的 Stokes 定理）、MP28（奇异同调及微分形式在其上的积分）——本章第三节两站的直接来源。
- 教材：M. Spivak《Calculus on Manifolds》，第四章（半空间证明）；M. Nakahara《Geometry, Topology and Physics》，第 5–6 章（原专栏提到的"详细证明"出处）；R. Bott & L. Tu《Differential Forms in Algebraic Topology》，第 1 章（奇异链版本，与本章 3.6 同一路线）。
- 向量分析的经典对照：任何一本《高等数学》下册的 Gauss / Stokes / Green 三节，可以拿来逐条对照第五节经典题 1、3、4 的翻译表。
- 后续：第 28 章 de Rham 上同调（本章配对的非退化性）；第 24 章 Hodge 星算子（$$d$$ 与 $$\nabla\cdot,\nabla\times$$ 的词典）。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch25_Stokes定理_上.md">← 第25章 Stokes 定理·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch27_de_Rham上同调_上.md">第27章 de Rham 上同调·上 →</a></div>
</div>
