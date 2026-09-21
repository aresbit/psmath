---
layout: default
---

# 第55章: 复半单 Lie 代数与根系·上：预备与直觉 (Complex Semisimple Lie Algebras and Root Systems · Part I: Warm-up and Intuition)

> 配套深化: 见 第56章 复半单 Lie 代数与根系·下（完整推导），本章是它的具体铺垫，建议先读本章
> 对应原专栏: MP73
> 专家依据: `_experts/algebra/lie-algebra-root-systems.md`（主，主场）+ `_experts/algebra/_SKILL.md`
> 知识库依据: `opc2/knowledge/math/李代数/`（15 篇）
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

本章要为第56章里四个"跳步"最凶的地方做准备。第一处：$$\mathfrak{sl}(2,\mathbb C)$$ 有限维不可约表示由一个非负整数决定这件事，第56章只用几行抽象记号 $$v_k=F^kv$$ 完成，本章先在一个具体的三维表示里把每一步拆开手算。第二处：Killing 型 $$\kappa(x,y)=\operatorname{tr}(\operatorname{ad}x\operatorname{ad}y)$$ 与 Cartan 判据看起来像凭空冒出的定义，本章先在两个最小的例子（$$\mathfrak{sl}(2,\mathbb C)$$ 与一个二维可解代数）里把 $$2\times2$$ 的 $$\operatorname{ad}$$ 矩阵乘出来、算出行列式，让读者亲眼看到"半单 $$\iff\kappa$$ 非退化"这句话背后是什么。第三处：根空间分解 $$L=H\oplus\bigoplus_\alpha L_\alpha$$ 第一次出现时是一句抽象陈述，本章直接在 $$\mathfrak{sl}(3,\mathbb C)$$ 里对角化两个具体的 $$\operatorname{ad}h$$，把"根"从符号变成一对具体数字。第四处：第56章 定理 3.29 里"夹角只有七种"用到一对 Cartan 整数 $$\langle\beta,\alpha\rangle,\langle\alpha,\beta\rangle$$，长根短根到底谁配到哪个数值，是全书最容易记反符号的地方之一，本章用一对不等长的平面向量把公式代入算一遍，把这件事钉死。

读完本章，你应该已经能：徒手算出 $$\mathfrak{sl}(2,\mathbb C)$$ 小维数表示的权链、徒手判定一个小代数是否半单、徒手写出 $$\mathfrak{sl}(3,\mathbb C)$$ 的全部根、徒手算对一对不等长根的 Cartan 整数。第56章要做的，只是把这四件事从"算过的例子"升级为"对任意半单 Lie 代数、任意维数都成立"的一般定理。

## 二、入口：一道具体的问题 (Entry Problem)

**(i) 热身：把 $$2\times2$$ 矩阵的换位子算一遍。** 取

$$E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad F=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad H=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

直接算 $$[H,E]$$、$$[H,F]$$、$$[E,F]$$（三次 $$2\times2$$ 矩阵乘法即可，不需要任何理论）。

**(ii) 猜规律：一个三维的例子。** 假设有另一组作用在三维空间 $$V=\operatorname{span}\{v_0,v_1,v_2\}$$ 上的算子 $$E,F,H$$（同一套记号，不同的表示），满足

$$Hv_0=2v_0,\quad Fv_0=v_1,\quad Fv_1=v_2,\quad Fv_2=0,\quad Ev_0=0 .$$

只用 $$[H,F]=-2F$$（(i) 里已经算出）与上面五条关系，能不能不做任何一般证明，就**算出** $$Hv_1,\ Hv_2,\ Ev_1,\ Ev_2$$ 具体是多少？（提示：$$H(Fv_0)=(HF)v_0=(FH-2F)v_0$$。）先猜出数字，答案与验证在 三.1 节给出。

**(iii) 猜形状：$$\mathfrak{sl}(3,\mathbb C)$$ 里的六个数。** 取 $$3\times3$$ 迹零矩阵构成的空间 $$L=\mathfrak{sl}(3,\mathbb C)$$，取对角矩阵 $$h_1=\operatorname{diag}(1,0,-1)$$，取矩阵单位 $$E_{12},E_{13},E_{23},E_{21},E_{31},E_{32}$$（即第 $$i$$ 行第 $$j$$ 列为 $$1$$、其余为 $$0$$ 的矩阵）。直接算 $$[h_1,E_{ij}]$$（$$6$$ 次矩阵乘法），把结果写成 $$[h_1,E_{ij}]=c_{ij}E_{ij}$$ 的形式，列出六个数 $$c_{ij}$$。你会发现有些 $$c_{ij}$$ 重复——这说明只用一个 $$h_1$$ 分不清六个方向。三.3 节会加入第二个对角矩阵 $$h_2$$，把六个方向**完全**分开。

**本题的地位**：(i) 是全部计算的起点；(ii) 预演第56章 入口题(iii) 的权链公式；(iii) 预演第56章 定理 3.22 的根空间分解——本章结束时你会亲手算出这两件事的答案，第56章只是把"算过的例子"写成对任意维数都成立的定理。

## 三、结构：定义与完整推导 (Structure & Proof)

本节挑出第56章里四个最容易"跳步"的地方，逐一先手算、再抽象：3.1 权链，3.2 Killing 型，3.3 根空间分解，3.4 Cartan 整数。

### 3.1 sl(2,C) 的权链：从三维例子看到一般公式

**定义 3.1（权，weight）**。设 $$V$$ 是某个表示（$$E,F,H$$ 三个线性算子满足与入口题 (i) 相同的换位子关系 $$[H,E]=2E,[H,F]=-2F,[E,F]=H$$），若 $$Hv=\lambda v$$（$$v\neq0$$），就说 $$v$$ 的**权** (weight) 是 $$\lambda$$。之所以要单独起名字：因为 $$H$$ 的作用在合适基下是"对角"的，把它的本征值单独记下来，比每次都写"$$H$$ 作用后的系数"更省事——这是全书第一次用到"权"这个词，后面反复出现。

**回答入口题 (ii)：把三维表示完整算出来。** 延续入口题 (ii) 的假设，用 $$[H,F]=-2F$$：

$$Hv_1 = H(Fv_0) = (HF)v_0 = (FH-2F)v_0 = F(Hv_0)-2Fv_0 = F(2v_0)-2v_1 = 2v_1-2v_1=0 .$$

$$Hv_2 = H(Fv_1) = (FH-2F)v_1 = F(Hv_1)-2Fv_1 = F(0)-2v_2 = -2v_2 .$$

三个权是 $$2,0,-2$$——公差为 $$-2$$ 的等差数列。再用 $$[E,F]=H$$（即 $$EF=FE+H$$）：

$$Ev_1 = E(Fv_0) = (FE+H)v_0 = F(Ev_0)+Hv_0 = F(0)+2v_0 = 2v_0 .$$

$$Ev_2 = E(Fv_1) = (FE+H)v_1 = F(Ev_1)+Hv_1 = F(2v_0)+0 = 2v_1 .$$

**把六条关系整理成矩阵。** 取 $$V$$ 的基 $$(v_0,v_1,v_2)$$，上面算出的六条关系（$$Hv_0=2v_0,Hv_1=0,Hv_2=-2v_2$$；$$Ev_0=0,Ev_1=2v_0,Ev_2=2v_1$$；$$Fv_0=v_1,Fv_1=v_2,Fv_2=0$$）恰好给出

$$H=\begin{pmatrix}2&0&0\\0&0&0\\0&0&-2\end{pmatrix},\qquad E=\begin{pmatrix}0&2&0\\0&0&2\\0&0&0\end{pmatrix},\qquad F=\begin{pmatrix}0&0&0\\1&0&0\\0&1&0\end{pmatrix}.$$

**自检**：直接乘矩阵验证 $$[E,F]=H$$。$$EF$$ 的 $$(1,1)$$ 元是 $$E$$ 的第一行 $$(0,2,0)$$ 点乘 $$F$$ 的第一列 $$(0,1,0)^t$$，等于 $$2$$；逐项算出 $$EF=\operatorname{diag}(2,2,0)$$，$$FE=\operatorname{diag}(0,2,2)$$，两者相减得 $$\operatorname{diag}(2,0,-2)=H$$ ✓，与入口题 (i) 里的关系式完全一致，只是维数从 $$2$$ 变成了 $$3$$。

**命题 3.2（权链的规律：从 $$m=2$$ 看一般情形）**。上面算出的权是 $$2,0,-2$$（从最高权 $$m=2$$ 起、公差 $$-2$$），而

$$Ev_1 = 2v_0 = 1\cdot(2-1+1)\,v_0,\qquad Ev_2=2v_1=2\cdot(2-2+1)\,v_1 .$$

猜想：若最高权是 $$m$$（这里 $$m=2$$），则一般地 $$Hv_k=(m-2k)v_k$$、$$Ev_k=k(m-k+1)v_{k-1}$$，且权链在 $$k=m$$ 处终止（$$v_{m+1}=0$$），维数 $$=m+1$$。**这正是第56章 入口题 (iii) 要证明的公式；本节只是对 $$m=2$$ 亲手验证了一遍，把符号 $$k(\lambda-k+1)$$ 换成了两个具体数字 $$1\times2$$ 与 $$2\times1$$。** 五节 题一 会再用这组矩阵验证 Casimir 算子，六节 竞3 会用 $$m=1$$ 再核对一遍。

### 3.2 Killing 型：为什么会想到定义它，以及一个退化的对照例子

**为什么要定义 $$\kappa(x,y)=\operatorname{tr}(\operatorname{ad}x\operatorname{ad}y)$$？** $$\operatorname{ad}x$$ 是 $$L\to L$$ 的线性变换，两个线性变换的复合 $$\operatorname{ad}x\circ\operatorname{ad}y$$ 还是线性变换，而"线性变换的迹"是从线性变换榨出一个数字最朴素的办法——比行列式线性、比特征值好算。$$\kappa$$ 就是把这个想法系统化：对每一对 $$x,y$$ 都做一次"复合再取迹"。它是否非退化，直接反映 $$\operatorname{ad}$$ 这族变换"够不够扩散到全空间"。

**定义 3.3（Killing 型，具体版）**。$$\kappa(x,y):=\operatorname{tr}(\operatorname{ad}x\circ\operatorname{ad}y)$$。

**先算一个会退化的例子，看看"退化"长什么样。** 取二维代数 $$L=\operatorname{span}\{x,y\}$$，唯一非零括号 $$[x,y]=x$$（这与第56章 反例 3.4 是同一个代数——那里用它演示"可解但不幂零"，这里换个角度，看它的 Killing 型）。

$$\operatorname{ad}x(x)=[x,x]=0,\qquad \operatorname{ad}x(y)=[x,y]=x\quad\Longrightarrow\quad \operatorname{ad}x=\begin{pmatrix}0&1\\0&0\end{pmatrix}\ (\text{基 }(x,y)).$$

$$\operatorname{ad}y(x)=[y,x]=-x,\qquad \operatorname{ad}y(y)=[y,y]=0\quad\Longrightarrow\quad \operatorname{ad}y=\begin{pmatrix}-1&0\\0&0\end{pmatrix}.$$

逐个算：

$$(\operatorname{ad}x)^2=\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix}=\begin{pmatrix}0&0\\0&0\end{pmatrix}\ \Longrightarrow\ \kappa(x,x)=0 .$$

$$\operatorname{ad}x\operatorname{ad}y=\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}-1&0\\0&0\end{pmatrix}=\begin{pmatrix}0&0\\0&0\end{pmatrix}\ \Longrightarrow\ \kappa(x,y)=0 .$$

$$(\operatorname{ad}y)^2=\begin{pmatrix}-1&0\\0&0\end{pmatrix}\begin{pmatrix}-1&0\\0&0\end{pmatrix}=\begin{pmatrix}1&0\\0&0\end{pmatrix}\ \Longrightarrow\ \kappa(y,y)=1 .$$

**命题 3.4（这个例子的 Killing 型退化）**。在基 $$(x,y)$$ 下，

$$\kappa=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad \det\kappa=0 .$$

$$\kappa$$ **退化**：$$x$$ 与全空间的 $$\kappa$$-配对恒为零（$$\kappa(x,x)=\kappa(x,y)=0$$），但 $$x\neq0$$。

**这与半单性的关系（先看现象，第56章 定理 3.16 给出一般证明）**：这个代数可解（第56章 反例 3.4 已验证 $$L^{(2)}=0$$），不是半单的；而它的 $$\kappa$$ 恰好退化。反过来，第56章 题1(1) 会算出 $$\mathfrak{sl}(2,\mathbb C)$$（三维、单）的 Killing 型矩阵是 $$\begin{pmatrix}0&0&2\\0&8&0\\2&0&0\end{pmatrix}$$，行列式 $$-32\neq0$$，非退化。**"退化 vs 非退化"这个对照，就是 Cartan 第二判据（半单 $$\iff\kappa$$ 非退化）要讲的整件事——本节只是先把两个最小的例子摆在一起，让读者在看到一般证明之前先亲眼确认它确实成立。**

### 3.3 sl(3,C) 的根：从一个 $$h$$ 不够，到两个 $$h$$ 够

**回答入口题 (iii)。** 取 $$h_1=\operatorname{diag}(1,0,-1)$$。用 $$[\operatorname{diag}(a_1,a_2,a_3),E_{ij}]=(a_i-a_j)E_{ij}$$（直接展开矩阵乘法可验证：$$h_1E_{ij}$$ 只放大 $$E_{ij}$$ 所在的第 $$i$$ 行、乘上 $$a_i$$；$$E_{ij}h_1$$ 只放大第 $$j$$ 列、乘上 $$a_j$$；相减得 $$(a_i-a_j)E_{ij}$$）：

$$[h_1,E_{12}]=1\cdot E_{12},\quad [h_1,E_{13}]=2\cdot E_{13},\quad [h_1,E_{23}]=1\cdot E_{23},$$
$$[h_1,E_{21}]=-1\cdot E_{21},\quad [h_1,E_{31}]=-2\cdot E_{31},\quad [h_1,E_{32}]=-1\cdot E_{32}.$$

六个数是 $$1,2,1,-1,-2,-1$$——**$$E_{12}$$ 与 $$E_{23}$$ 给出同一个数 $$1$$**，单靠 $$h_1$$ 分不清它们。这不是巧合：$$\mathfrak{sl}(3)$$ 的 Cartan 子代数是二维的（迹零对角矩阵有两个自由参数），只用一个 $$h_1$$ 相当于只测量了根这个二维对象的一个坐标。

**加入第二个方向。** 取 $$h_2=\operatorname{diag}(0,1,-1)$$，同样算：

$$[h_2,E_{12}]=-1\cdot E_{12},\quad [h_2,E_{13}]=1\cdot E_{13},\quad [h_2,E_{23}]=2\cdot E_{23},$$
$$[h_2,E_{21}]=1\cdot E_{21},\quad [h_2,E_{31}]=-1\cdot E_{31},\quad [h_2,E_{32}]=-2\cdot E_{32}.$$

**命题 3.5（六个根，写成坐标对）**。把每个 $$E_{ij}$$ 对应的一对数 $$(c_1,c_2):=\bigl([h_1,E_{ij}]\text{ 的系数},\ [h_2,E_{ij}]\text{ 的系数}\bigr)$$ 列出：

$$E_{12}:(1,-1),\quad E_{13}:(2,1),\quad E_{23}:(1,2),\quad E_{21}:(-1,1),\quad E_{31}:(-2,-1),\quad E_{32}:(-1,-2).$$

六个坐标对**两两不同**——两个方向 $$h_1,h_2$$ 足够把六个根完全分开。**这就是第56章 定义 3.21 的根空间 $$L_\alpha=\{x:[h,x]=\alpha(h)x\ \forall h\in H\}$$ 在具体坐标下的样子**：每个根 $$\alpha$$ 不是一个数，而是一条"给定任何 $$h\in H$$ 都能求值"的规则（线性泛函）。例如 $$E_{13}$$ 对应的根 $$\alpha$$ 满足 $$\alpha(h_1)=2,\ \alpha(h_2)=1$$，这与第56章 例 3.25 里 $$\varepsilon_1-\varepsilon_3$$（在对角矩阵 $$\operatorname{diag}(a_1,a_2,a_3)$$ 上取值 $$a_1-a_3$$）完全一致：代入 $$h_1$$ 得 $$1-(-1)=2$$ ✓，代入 $$h_2$$ 得 $$0-(-1)=1$$ ✓。

**观察对称性**：$$E_{21}$$ 的坐标 $$(-1,1)$$ 恰是 $$E_{12}$$ 的坐标 $$(1,-1)$$ 的相反数；同理 $$E_{31}$$ 与 $$E_{13}$$、$$E_{32}$$ 与 $$E_{23}$$ 互为相反数。六个点两两配对成三对相反向量——这预告第56章 定理 3.23(iii)（$$\alpha\in\Phi\Rightarrow-\alpha\in\Phi$$）。

### 3.4 Cartan 整数：一对不等长向量，算清楚谁配谁

**动机**：第56章 定理 3.29 要证明"两根夹角只能是七个值之一"，核心工具是一对整数 $$\langle\beta,\alpha\rangle,\langle\alpha,\beta\rangle$$；这对整数谁在前、长根短根各配到哪个数，是最容易搞混的地方。本节先在纯几何（不涉及任何 Lie 代数）里，把公式代入两个具体的、不等长的平面向量，把这件事算实。

**定义 3.6（Cartan 整数与反射，具体版）**。给定欧氏空间中两个向量 $$\alpha,\beta$$（$$\alpha\neq0$$），定义

$$\langle\beta,\alpha\rangle:=\frac{2(\beta,\alpha)}{(\alpha,\alpha)},\qquad \sigma_\alpha(\beta):=\beta-\langle\beta,\alpha\rangle\,\alpha .$$

注意分母永远是**后一个**下标 $$\alpha$$ 的长度平方——这个"分母跟着第二个下标走"的约定，正是本节要练熟的地方。

**代入具体数字。** 取短向量 $$\alpha=(0,1)$$（$$(\alpha,\alpha)=1$$）、长向量 $$\beta=(-1,-1)$$（$$(\beta,\beta)=2$$）。先算夹角：

$$(\alpha,\beta)=(0)(-1)+(1)(-1)=-1,\qquad \cos\theta=\frac{-1}{\sqrt1\cdot\sqrt2}=-\frac{1}{\sqrt2}\ \Longrightarrow\ \theta=135^\circ .$$

再代入定义：

$$\langle\beta,\alpha\rangle=\frac{2(-1)}{1}=-2\qquad(\text{用短向量 }\alpha\text{ 做分母，数值大}),$$

$$\langle\alpha,\beta\rangle=\frac{2(-1)}{2}=-1\qquad(\text{用长向量 }\beta\text{ 做分母，数值小}).$$

**命题 3.7（谁配谁：长度比与 Cartan 整数的大小成反比）**。一般地，若 $$\lvert\alpha\rvert\le\lvert\beta\rvert$$，则 $$\langle\beta,\alpha\rangle$$（分母是短的 $$\alpha$$）的绝对值**不小于** $$\langle\alpha,\beta\rangle$$（分母是长的 $$\beta$$）的绝对值——上面的例子里 $$\lvert{-2}\rvert\ge\lvert{-1}\rvert$$ 正是如此。原因很直接：两式分子相同（都是 $$2(\alpha,\beta)$$），分母不同，除以小分母得到大结果。**记住这一条，第56章 定理 3.29 的角度—整数对照表就不会把长短根的整数配反。**

**验证反射确实封闭（根系公理 (R3) 的具体版）**。算 $$\sigma_\alpha(\beta)$$ 与 $$\sigma_\beta(\alpha)$$：

$$\sigma_\alpha(\beta)=\beta-\langle\beta,\alpha\rangle\alpha=(-1,-1)-(-2)(0,1)=(-1,-1)+(0,2)=(-1,1).$$

$$\sigma_\beta(\alpha)=\alpha-\langle\alpha,\beta\rangle\beta=(0,1)-(-1)(-1,-1)=(0,1)-(1,1)=(-1,0).$$

把 $$\alpha,\beta,\sigma_\alpha(\beta),\sigma_\beta(\alpha)$$ 连同它们的相反向量收集起来：

$$\{(0,\pm1),\ (\pm1,0),\ (\pm1,\pm1)\}\qquad(\text{共 }2+2+4=8\text{ 个}).$$

这八个向量在"互相反射"下封闭（可以逐对验证，比如 $$\sigma_{(0,1)}((1,0))=(1,0)-0\cdot(0,1)=(1,0)$$ 不变，$$\sigma_{(0,1)}((1,1))=(1,1)-2(0,1)=(1,-1)$$ 仍在集合里）——这正是第56章 竞3 会重新认领的 $$B_2$$ 根系（换一套坐标、对应 $$\mathfrak{so}(5,\mathbb C)$$）。本节的计算就是那道题背后真正在算的东西。

## 四、几何与物理直觉 (Intuition)

**权像温度计上的刻度。** $$H$$ 的作用只做一件事：给每个基向量贴一个数字（权），$$E$$ 把这个数字调高 $$2$$、$$F$$ 调低 $$2$$——像温度计上等间距的刻度，$$E,F$$ 是"往上挪一格""往下挪一格"的按钮。3.1 节里 $$2,0,-2$$ 三个刻度就是最小的非平凡例子。

**Killing 型像"转动的强度计"。** $$\operatorname{ad}x$$ 把整个空间搅动一遍，$$\kappa(x,x)=\operatorname{tr}(\operatorname{ad}x)^2$$ 大致在问"$$x$$ 把空间搅动得有多剧烈"。3.2 节的退化例子里，$$x$$ 方向的搅动"往复抵消"（$$(\operatorname{ad}x)^2=0$$），量出来的强度就是零；这类"搅了但量不出强度"的方向，正是可解、不半单代数的病灶所在。

**根空间分解像把光分解成不同颜色的光谱。** 一支白光穿过棱镜，被分解成一条条不同频率的窄带；$$\operatorname{ad}h$$（$$h\in H$$）就是那个"棱镜"，把 $$L$$ 分解成一条条本征子空间 $$L_\alpha$$，每个 $$\alpha$$ 是一种"频率"。3.3 节里两个 $$h_1,h_2$$ 相当于从两个不同角度重新测量同一束光，把原来分不清的两条谱线（$$E_{12}$$ 与 $$E_{23}$$ 在 $$h_1$$ 下都是 $$1$$）区分开来。

**Cartan 整数像一把只能读整数刻度的尺子。** 反射 $$\sigma_\alpha$$ 把 $$\beta$$ 变到 $$\beta-\langle\beta,\alpha\rangle\alpha$$，如果 $$\langle\beta,\alpha\rangle$$ 不是整数，反射后的点就会落在"根的集合"之外——这是一种**离散性**的来源：不是所有几何都被允许，只有能整齐嵌进整数格点的几何才行。3.4 节的八点集合就是这种离散性的一个具体样本：它不能被任意拉伸变形，八个点的相对位置被整数关系死死钉住。

**下一章的镜子。** 3.4 节反射生成的那群变换（Weyl 群）就像走廊两端装满镜子：光线在镜子间反复弹射，最终只能落在有限个方向上。第56章会证明这件事对任意半单 Lie 代数都成立，而且"镜子的个数"最终决定了一整张分类表。

**一个更贴身的类比：陀螺仪与角动量。** 如果你转过一个陀螺，会发现它的转轴只能对着有限几个"自然方向"稳定下来，而不是随便哪个方向都行——这与角动量在量子力学里只能取分立值（$$m,m-2,\dots,-m$$）是同一类现象：连续对称性（转动）遇上"必须回到自身"的约束（这里是有限维、整数权），结果被迫离散化。3.1 节权链两端各差 $$2$$、总长 $$m+1$$，就是这个"离散化"最简单的样本；物理上它对应自旋为 $$m/2$$ 的粒子有 $$m+1$$ 个可能的自旋态。第56章 4.3 节会把这条类比精确化到谐振子与 $$SU(3)$$ 色荷，但那里第一件事就是拆穿一个几乎人人都会犯的误认——本章不剧透，留给第56章入口题 (iv)–(vi) 揭晓。

## 五、经典问题精讲 (Classical Problems)

### 题一：用 3.1 节的 $$3\times3$$ 矩阵验证 Casimir 算子

**题面**：对 3.1 节构造的三维表示（$$E,F,H$$ 是 $$3\times3$$ 矩阵），直接计算 $$c=EF+FE+\tfrac12H^2$$，验证它是数量矩阵，并核对数值与公式 $$\tfrac12m(m+2)$$（$$m=2$$）一致。

**解**：3.1 节已算出 $$EF=\operatorname{diag}(2,2,0)$$、$$FE=\operatorname{diag}(0,2,2)$$，故

$$EF+FE=\operatorname{diag}(2,4,2).$$

又 $$H=\operatorname{diag}(2,0,-2)$$，故 $$H^2=\operatorname{diag}(4,0,4)$$，$$\tfrac12H^2=\operatorname{diag}(2,0,2)$$。两者相加：

$$c=\operatorname{diag}(2,4,2)+\operatorname{diag}(2,0,2)=\operatorname{diag}(4,4,4)=4I .$$

$$c$$ 确实是数量矩阵（三个对角元相等），数值为 $$4$$。核对公式：$$\tfrac12m(m+2)=\tfrac12\cdot2\cdot4=4$$ ✓。**第56章 题1(3) 会对一般的 $$m$$ 重做这个计算（用抽象的 $$v_0,\dots,v_m$$），这里先看到 $$m=2$$ 时数字确实吻合。**$$\blacksquare$$

### 题二：sl(3,C) 里验证 $$[E_{12},E_{23}]=E_{13}$$，看结构常数怎么"加根"

**题面**：直接用矩阵乘法验证 $$[E_{12},E_{23}]=E_{13}$$，并用 3.3 节算出的坐标对，检查 $$E_{12}$$ 与 $$E_{23}$$ 对应的根相加是否正好等于 $$E_{13}$$ 对应的根。

**解**：矩阵单位满足 $$E_{ij}E_{kl}=\delta_{jk}E_{il}$$（第 $$j$$ 列与第 $$k$$ 行"接上"才非零）。故

$$E_{12}E_{23}=E_{13}\quad(\text{因为 }j=2=k),\qquad E_{23}E_{12}=0\quad(\text{因为 }j=3\neq1=k) .$$

于是 $$[E_{12},E_{23}]=E_{12}E_{23}-E_{23}E_{12}=E_{13}-0=E_{13}$$。

再看坐标：$$E_{12}$$ 的根坐标是 $$(1,-1)$$，$$E_{23}$$ 的是 $$(1,2)$$，相加得 $$(2,1)$$——正是 $$E_{13}$$ 的坐标！**这不是巧合**：一般地 $$[L_\alpha,L_\beta]\subseteq L_{\alpha+\beta}$$（第56章 定理 3.23(i)），本题是这条一般规律在 $$\mathfrak{sl}(3)$$ 里最简单的一次现身。$$\blacksquare$$

### 题三：3.4 节的八点集合——数一数有几条"镜子线"

**题面**：3.4 节得到的八个向量 $$\{(0,\pm1),(\pm1,0),(\pm1,\pm1)\}$$，每个向量 $$\alpha$$ 都给出一条反射镜面 $$\alpha^\perp$$（过原点、垂直于 $$\alpha$$ 的直线）。这八个向量一共给出几条**不同**的镜面直线？

**解**：互为相反数的两个向量给出同一条镜面（$$\alpha^\perp=(-\alpha)^\perp$$）。把八个向量按"相反数"配对：

$$\{(0,1),(0,-1)\},\ \{(1,0),(-1,0)\},\ \{(1,1),(-1,-1)\},\ \{(1,-1),(-1,1)\}.$$

四对给出四条镜面直线：$$x=0$$（竖直）、$$y=0$$（水平）、$$y=x$$、$$y=-x$$（两条对角线）。**四条镜面把平面切成八个楔形扇区**（每两条相邻镜面夹 $$45^\circ$$）。**这预告第56章 定理 3.38 的 Weyl 群**：由反射生成的群把空间切成若干"基本房"，房的个数等于群的阶——这里四条镜面生成的反射群阶数是 $$8$$（与八个扇区一一对应），这正是第56章 例 3.39 里 $$B_2$$ 的 Weyl 群阶 $$2^2\cdot2!=8$$ 的具体样子。$$\blacksquare$$

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 取入口题 (i) 的 $$2\times2$$ 矩阵 $$E,F,H$$。只用一次矩阵乘法，验证 $$[H,E]=2E$$（不需要算 $$[H,F]$$ 或 $$[E,F]$$）。

**基2.** 对 3.1 节构造的三维表示 $$E,F,H$$（$$3\times3$$ 矩阵），直接验证 $$Fv_2=0$$（即 $$F$$ 的矩阵作用在第三个基向量上得零向量）。

**基3.** 判断二维交换代数 $$L=\operatorname{span}\{x,y\}$$（$$[x,y]=0$$）的可解性、幂零性，并说明它的 Killing 型是什么（不需要严格证明半单性，只需说明为什么这个代数不可能半单）。

### 竞赛（本课目标难度）

**竞1.** 用 3.3 节的坐标对，取根 $$\alpha:=E_{12}$$（坐标 $$(1,-1)$$）与根 $$\beta:=E_{23}$$（坐标 $$(1,2)$$），只用标准欧氏内积 $$(u_1,u_2)\cdot(v_1,v_2)=u_1v_1+u_2v_2$$ 计算 Cartan 整数 $$\langle\alpha,\beta\rangle,\langle\beta,\alpha\rangle$$ 与夹角 $$\theta$$（不需要 Killing 型的精确尺度，只是练习公式代入）。

**竞2.** 3.4 节的八个向量中取 $$\gamma=(1,1)$$、$$\delta=(1,-1)$$，计算 $$\sigma_\gamma(\delta)$$，验证结果仍落在这八个向量里。

**竞3.** 对 $$\mathfrak{sl}(2,\mathbb C)$$ 的标准表示（$$m=1$$，即入口题 (i) 里的 $$2\times2$$ 矩阵本身），直接计算 Casimir 算子 $$c=EF+FE+\tfrac12H^2$$，验证它是数量矩阵，数值应为 $$\tfrac12\cdot1\cdot3=\tfrac32$$。

### 研究（通向下一章）

**研1.** 3.3 节里 $$\mathfrak{sl}(3,\mathbb C)$$（$$3\times3$$ 矩阵）给出 $$6$$ 个根；$$\mathfrak{sl}(2,\mathbb C)$$（$$2\times2$$）只有 $$2$$ 个根。猜一个公式：$$n\times n$$ 的迹零矩阵 $$\mathfrak{sl}(n,\mathbb C)$$ 应该有多少个根？用 $$n=4$$（即 $$\mathfrak{sl}(4,\mathbb C)$$）直接数一遍矩阵单位 $$E_{ij}$$（$$i\neq j$$）的个数，验证你的猜想。

**研2.** 3.2 节算出的两个例子（$$\mathfrak{sl}(2,\mathbb C)$$ 半单、Killing 型非退化；二维可解代数不半单、Killing 型退化）都是从"具体算出 $$\kappa$$ 的行列式"入手的。猜一猜：如果一个 Lie 代数是**幂零**的（比第56章 反例 3.4 的例子更"病态"，比如三维 Heisenberg 代数 $$[x,y]=z$$），它的 Killing 型会不会也退化？不要求证明，只要求给出你认为最有说服力的一条理由（提示：想想 $$\operatorname{ad}z$$ 长什么样）。

### 解答 (Solutions)

**解 基1.** $$HE=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix}=\begin{pmatrix}0&1\\0&0\end{pmatrix}$$，$$EH=\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}0&-1\\0&0\end{pmatrix}$$，故 $$[H,E]=HE-EH=\begin{pmatrix}0&2\\0&0\end{pmatrix}=2E$$。$$\blacksquare$$

**解 基2.** 3.1 节给出 $$F=\begin{pmatrix}0&0&0\\1&0&0\\0&1&0\end{pmatrix}$$，$$v_2$$ 对应第三个基向量 $$(0,0,1)^t$$。$$Fv_2$$ 是 $$F$$ 的第三列，即 $$(0,0,0)^t=0$$。$$\blacksquare$$

**解 基3.** *可解*：$$L^{(1)}=[L,L]=0$$（唯一括号 $$[x,y]=0$$），一步归零，可解（自动幂零：交换代数的下中心列同样一步归零）。

*Killing 型*：交换代数里每个 $$\operatorname{ad}u$$ 都是零算子（$$[u,\cdot]=0$$ 对一切元素成立），故 $$\kappa(u,v)=\operatorname{tr}(\operatorname{ad}u\operatorname{ad}v)=\operatorname{tr}(0)=0$$ 对一切 $$u,v$$——$$\kappa\equiv0$$，是最彻底的退化。

*为什么不可能半单*：半单要求 $$\operatorname{Rad}(L)=0$$，但这里整个 $$L$$ 自己就是可解理想（$$L\lhd L$$ 平凡成立），故 $$\operatorname{Rad}(L)=L\neq0$$，不半单。这与 $$\kappa\equiv0$$ 完全吻合，是 3.2 节现象的又一个例子——比二维可解代数的例子更极端：那里 $$\kappa$$ 只是行列式为零，这里 $$\kappa$$ 干脆恒为零。$$\blacksquare$$

**解 竞1.** $$\alpha=(1,-1),\beta=(1,2)$$。$$(\alpha,\alpha)=1+1=2$$，$$(\beta,\beta)=1+4=5$$，$$(\alpha,\beta)=1\cdot1+(-1)\cdot2=1-2=-1$$。

$$\langle\alpha,\beta\rangle=\frac{2(-1)}{5}=-\frac25,\qquad \langle\beta,\alpha\rangle=\frac{2(-1)}{2}=-1 .$$

注意 $$\langle\alpha,\beta\rangle=-2/5$$ **不是整数**——这符合预期：这里用的是"标准欧氏内积"，不是 Killing 型真正诱导的那个内积（两者成比例但一般不相等）；只有用 Killing 型诱导的内积，第56章 (R4) 的整性才成立。本题的目的只是练习公式代入。

夹角：$$\cos\theta=\dfrac{-1}{\sqrt2\cdot\sqrt5}=\dfrac{-1}{\sqrt{10}}\approx-0.316$$，$$\theta\approx108.4^\circ$$——**不落在第56章 定理 3.29 的七个允许角里**，这恰好印证了上一段的提醒：随手取的欧氏内积不满足整性，不是合法的根系内积。$$\blacksquare$$

**解 竞2.** $$\gamma=(1,1)$$（$$(\gamma,\gamma)=2$$），$$\delta=(1,-1)$$。$$(\gamma,\delta)=1\cdot1+1\cdot(-1)=0$$，故 $$\langle\delta,\gamma\rangle=\dfrac{2\cdot0}{2}=0$$，

$$\sigma_\gamma(\delta)=\delta-\langle\delta,\gamma\rangle\gamma=\delta-0=\delta=(1,-1) .$$

反射后不变——因为 $$\gamma\perp\delta$$（内积为零，$$90^\circ$$ 角），而与自己垂直的方向不受反射影响。结果 $$(1,-1)$$ 显然在八点集合 $$\{(0,\pm1),(\pm1,0),(\pm1,\pm1)\}$$ 里。$$\blacksquare$$

**解 竞3.** 用入口题 (i) 的矩阵：$$E=\begin{pmatrix}0&1\\0&0\end{pmatrix},F=\begin{pmatrix}0&0\\1&0\end{pmatrix},H=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$$。

$$EF=\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}0&0\\1&0\end{pmatrix}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad FE=\begin{pmatrix}0&0\\1&0\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix}=\begin{pmatrix}0&0\\0&1\end{pmatrix}.$$

$$EF+FE=\begin{pmatrix}1&0\\0&1\end{pmatrix}=I,\qquad H^2=\begin{pmatrix}1&0\\0&1\end{pmatrix}=I,\qquad \tfrac12H^2=\tfrac12I .$$

$$c=I+\tfrac12I=\tfrac32I .$$

数量矩阵，数值 $$\tfrac32$$，与 $$\tfrac12m(m+2)\big\vert_{m=1}=\tfrac12\cdot1\cdot3=\tfrac32$$ 一致 ✓。$$\blacksquare$$

**解 研1.** 猜想：$$\mathfrak{sl}(n,\mathbb C)$$ 的根数等于非对角矩阵单位的个数，即 $$n(n-1)$$（$$n=2$$ 时给出 $$2\times1=2$$ ✓，$$n=3$$ 时给出 $$3\times2=6$$ ✓，与 3.3 节吻合）。$$n=4$$：矩阵单位 $$E_{ij}$$（$$i\neq j$$，$$1\le i,j\le4$$）共有 $$4\times4-4=12$$ 个（去掉对角的 $$4$$ 个），验证 $$4\times3=12$$ ✓。

（注：第56章 例 3.25 里写的公式是 $$\lvert\Phi\rvert=n(n+1)$$，那里的 $$n$$ 指的是 $$\mathfrak{sl}(n+1,\mathbb C)$$ 的下标（矩阵是 $$(n+1)\times(n+1)$$），与本题直接用矩阵大小记作 $$n$$ 不同——用矩阵大小 $$n$$ 记的话，根数是 $$n(n-1)$$；这是第56章符号里"用秩而不是矩阵大小"的一个常见易混点，读第56章时要留意这处换元。）$$\blacksquare$$

**解 研2.** 三维 Heisenberg 代数 $$[x,y]=z$$（$$z$$ 是中心元）。$$\operatorname{ad}z(x)=[z,x]=0$$，$$\operatorname{ad}z(y)=[z,y]=0$$，$$\operatorname{ad}z(z)=0$$——**$$\operatorname{ad}z$$ 是零算子**（$$z$$ 在中心里，与一切元素交换）。于是对任意 $$w$$，$$\kappa(z,w)=\operatorname{tr}(\operatorname{ad}z\operatorname{ad}w)=\operatorname{tr}(0)=0$$，即 $$z$$ 与全空间的 Killing 配对恒为零，而 $$z\neq0$$——**Killing 型退化**。

更一般的理由：幂零代数的每个 $$\operatorname{ad}x$$ 都是幂零线性变换（第56章 定理 3.6，Engel 定理的直接推论之一），而幂零变换的迹恒为零，所以 $$\kappa(x,x)=\operatorname{tr}(\operatorname{ad}x)^2=0$$ 对幂零代数的**每个**元素都成立（不只是中心元）——幂零代数的 Killing 型退化得比一般可解代数更彻底，也再次印证 Cartan 判据"半单 $$\iff\kappa$$ 非退化"的方向：幂零远离半单，Killing 型也远离非退化。$$\blacksquare$$


## 七、Takeaway 与延伸 (Takeaways)

**1. 权不是抽象符号，是一把尺子上的刻度。** $$H$$ 的本征值给每个基向量贴一个数字，$$E,F$$ 只是"刻度 $$+2$$""刻度 $$-2$$"的操作——3.1 节里三维例子的 $$2,0,-2$$ 就是这把尺子最短的样本。

**2. 半单性可以从"退化不退化"直接看出来。** 3.2 节算出了一个具体的 $$2\times2$$ Killing 型矩阵及其行列式；"非退化 $$\Rightarrow$$ 半单"不再是一句需要信任的抽象陈述，而是你亲手算出行列式非零/为零之后的直接观察。

**3. 一个根不是一个数，是一条"在每个 $$h$$ 上都能求值"的规则。** 3.3 节用两个方向 $$h_1,h_2$$ 才把六个根彻底分开，这提前给出了"Cartan 子代数的维数 = 秩 = 需要几个独立方向才能分清所有根"的直觉。

**4. Cartan 整数的大小由"谁做分母"决定，不是随手写的符号。** 3.4 节的具体计算钉死了"短根做分母给大数、长根做分母给小数"这条规则——这是第56章 定理 3.29 的角度—整数对照表里最容易被记反的地方。

**5. 反射生成的有限集合会自动"整齐"。** 3.4 节八个点在反射下封闭，且这种封闭性把点的个数、角度都锁死为固定值，不能随意变形——这就是根系公理为什么足以支撑起一整套分类定理的直觉起点。

**交棒给下一章**：现在你已经能手算出 $$\mathfrak{sl}(2,\mathbb C)$$ 小维数表示的权链、判断一个小代数是否半单、写出 $$\mathfrak{sl}(3,\mathbb C)$$ 的全部根、算对一对不等长根的 Cartan 整数——第56章会把这四件事从"验证过的例子"升级为"对任意半单 Lie 代数、任意维数都成立"的一般定理，并且补上本章特意留白的部分：**为什么** Cartan 子代数一定存在、**为什么**根空间必须一维、**为什么**恰好只有九加五种可能的 Dynkin 图。带着这四个具体例子去读第56章的 3.1–3.5 节，你会发现每一步抽象背后都能对上本章算过的数字。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch54_Lie代数与指数映射_下.md">← 第54章 Lie 代数与指数映射·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch56_复半单Lie代数与根系_下.md">第56章 复半单 Lie 代数与根系·下 →</a></div>
</div>
