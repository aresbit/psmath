# 谱理论：算子谱理论 (Spectral Theory of Operators)

> 整理自 William Arveson《A Short Course on Spectral Theory》(GTM 209)；Ronald G. Douglas《Banach Algebra Techniques in Operator Theory》(GTM 179)；Gerald Teschl《Mathematical Methods in Quantum Mechanics》(GSM 157)；Emmanuel Kowalski《Spectral Theory in Hilbert Spaces》(ETH)；Roman Vershynin《Lectures in Functional Analysis》Ch.5；Joel Feinstein《Introduction to Fredholm Operators》；MIT OCW 18.102（Dirichlet 问题应用）。

## 0. 一句话定位

谱理论回答一个贯穿数学与物理的问题：**给定希尔伯特空间上的（自伴/正规）算子 $T$，如何把它"对角化"？** 有限维答案是特征值分解；无限维里谱不再只由离散特征值构成，而要用**谱测度 (spectral measure)** 这把"投影值测度"的尺子把算子写成对谱的积分 $T=\int\lambda\,dE(\lambda)$。

**核心心智模型**：

- **自伴算子 = 量子力学"可观测量"**：$T=T^*$ 的谱在实轴，$\lVert T\rVert=\sup_{\lVert x\rVert=1}\lvert\langle Tx,x\rangle\rvert$。
- **谱 = 广义特征值，谱测度 = 连续谱下的特征投影**：$\lambda\notin\sigma(T)\iff\lambda I-T$ 可逆。
- **谱定理 = 无限维对角化**：有限维 → 紧正规（求和）→ 一般正规（积分）。
- **紧算子 = "几乎有限维"**：谱除 0 外都是孤立有限重特征值。
- **Fredholm 算子 = 模掉紧算子可逆**：Atkinson 定理；指标 $\operatorname{ind}T=\dim\ker T-\dim\ker T^*$ 是拓扑不变量。
- **本质谱 = 模掉紧扰动后剩下的谱**：紧扰动只动离散谱，本质谱刚性不变。

---

## 1. 谱与预解集

**定义**：$T\in B(X)$（$X$ Banach），$\lambda$ 属**预解集** $\rho(T)$ 若 $\lambda I-T$ 可逆（有界逆）；否则属**谱** $\sigma(T)$。$R_\lambda(T)=(\lambda I-T)^{-1}$ 称**预解式**。

**基本性质**：$\sigma(T)$ 是 $\mathbb{C}$ 的**非空紧子集**，包含在 $\{\lvert z\rvert\le\lVert T\rVert\}$ 中；预解式在 $\rho(T)$ 上解析，满足**预解恒等式** $R_\lambda-R_\mu=(\mu-\lambda)R_\lambda R_\mu$；谱非空来自 Liouville 定理的反证（若谱空，$R_\lambda$ 是整函数且在无穷远趋于 0，故恒为 0）。

**无限维的微妙**：谱 $\ne$ 特征值集合。

- $T:\ell^2\to\ell^2$，$a\mapsto(a_1/1,a_2/2,\dots)$：$0\in\sigma(T)$ 但 0 **不是**特征值（$T$ 单射却不满射，逆无界）；
- 乘法算子 $Tf(x)=xf(x)$ 在 $L^2([0,1])$：**无特征值**，但 $\sigma(T)=[0,1]$；
- 单侧移位 $S$：$\sigma(S)=\overline{\mathbb D}$（闭单位圆盘），$\sigma_p(S)=\varnothing$。

---

## 2. 谱半径公式

**定义**：$r(T)=\sup_{\lambda\in\sigma(T)}\lvert\lambda\rvert$。

**定理（Gelfand 谱半径公式）**：

$$r(T)=\lim_{n\to\infty}\lVert T^n\rVert^{1/n}=\inf_{n\ge1}\lVert T^n\rVert^{1/n}.$$

极限存在（次可乘性保证）。对任何巴拿赫代数元素成立。

**推论（正规算子）**：$T$ 正规 $\Rightarrow r(T)=\lVert T\rVert$（证明用 C\* 恒等式 $\lVert T^{2^n}\rVert=\lVert T\rVert^{2^n}$）。这把"谱有多大"与"算子幂的范数增长"精确挂钩。

---

## 3. 谱的细分

按"$\lambda I-T$ 不可逆的具体原因"分解：

- **点谱** $\sigma_p(T)$：$\lambda I-T$ 非单射（即 $\lambda$ 是特征值）；
- **近似点谱** $\sigma_{ap}(T)$：存在 $\lVert x_n\rVert=1$ 使 $(\lambda I-T)x_n\to0$（$\lambda I-T$ 非下有界）；
- **连续谱** $\sigma_c(T)$：$\lambda I-T$ 单射、值域稠密但不满；
- **剩余谱** $\sigma_r(T)$：单射但值域不稠密。

关系：$\sigma=\sigma_p\cup\sigma_c\cup\sigma_r$；$\partial\sigma\subset\sigma_{ap}\subset\sigma$。

**正规算子谱分类**：自伴 $\sigma\subset\mathbb{R}$（$[m,M]$，$m=\inf\langle Tx,x\rangle$、$M=\sup\langle Tx,x\rangle$）；正 $\sigma\subset[0,\infty)$；酉 $\sigma\subset\{\lvert z\rvert=1\}$；投影 $\sigma\subset\{0,1\}$；正规算子剩余谱为空。

**乘法算子是"谱 = 取值集合"的典范**：$(M_\varphi f)(t)=\varphi(t)f(t)$，$\sigma(M_\varphi)=\varphi([0,1])$（值域），无特征值（除非 $\varphi$ 在正测度集上取常值），谱全连续。

---

## 4. 谱测度与函数演算

**连续函数演算**：$T$ 正规 $\Rightarrow$ 存在唯一等距 \*-同态 $\Phi:C(\sigma(T))\to B(H)$，$f\mapsto f(T)$，$\Phi(1)=I$、$\Phi(\mathrm{id})=T$。满足 $\lVert f(T)\rVert=\lVert f\rVert_\infty=\sup_{\lambda\in\sigma(T)}\lvert f(\lambda)\rvert$；**谱映射定理** $\sigma(f(T))=f(\sigma(T))$；$f\ge0\Rightarrow f(T)\ge0$。

**谱测度（投影值测度, PVM）**：$E:\mathcal B\to B(H)$，$E(\Delta)$ 为投影，满足

1. $E(\varnothing)=0$，$E(\mathbb{C})=I$；
2. 两两不交 $\Delta_n$ 满足 $E(\bigcup_n\Delta_n)=\sum_n E(\Delta_n)$（弱算子拓扑）；
3. $E(\Delta_1\cap\Delta_2)=E(\Delta_1)E(\Delta_2)$。

对每个 $x\in H$，$\mu_x(\Delta)=\langle E(\Delta)x,x\rangle$ 是普通 Borel 测度。

**定理（Borel 函数演算 / 自伴谱定理）**：$T$ 自伴 $\Rightarrow$ 唯一谱测度 $E$（支撑在 $\sigma(T)\subset\mathbb{R}$）使

$$T=\int_{\sigma(T)}\lambda\,dE(\lambda),\qquad f(T)=\int f(\lambda)\,dE(\lambda)$$

（$f$ 有界 Borel），且 $\lVert f(T)\rVert\le\lVert f\rVert_\infty$、$(fg)(T)=f(T)g(T)$、$\bar f(T)=f(T)^*$。

**定理（正规算子谱定理，终结形态）**：$T$ 正规 $\Rightarrow$ 唯一谱测度 $E$（支撑在 $\sigma(T)\subset\mathbb{C}$）使 $T=\int_{\sigma(T)}z\,dE(z)$，且 $f(T)=\int f(z)\,dE(z)$ 是 Borel 函数演算（\*-同态）。特别地 $T^*=\int\bar z\,dE(z)$，特征函数 $\chi_\Delta(T)=E(\Delta)$ 是谱投影，$\langle f(T)x,y\rangle=\int f\,d\mu_{x,y}$（$\mu_{x,y}(\Delta)=\langle E(\Delta)x,y\rangle$）。

**阶梯的统一**：紧正规频谱集中在可数集 $\{\lambda_n\}$ 上，积分退化为求和 $T=\sum_n\lambda_n P_n$；一般正规谱可连续，故用积分。

**双交换子定理**：由正规 $T$ 生成的 von Neumann 代数等于双交换子 $\{T,T^*\}''$，等于所有谱投影 $E(\Delta)$ 生成的代数——von Neumann 代数的入口。

---

## 5. 紧算子谱

**定理（紧算子谱，Riesz–Schauder）**：$T\in\mathcal K(H)$：

- $\sigma(T)$ 至多可数，除 $0$ 外无聚点（$0$ 是唯一可能的聚点）；
- 每个非零 $\lambda\in\sigma(T)$ 是**特征值**，特征空间 $\ker(\lambda I-T)$ 有限维；
- 若 $\lambda\ne0$，则 $\lambda I-T$ 是 Fredholm 算子且指标为 0。

**定理（紧正规算子谱定理）**：$T\in\mathcal K(H)$ 正规 $\Rightarrow$ 存在正交规范基 $\{e_n\}$ 与 $\lambda_n\to0$ 使

$$T=\sum_n\lambda_n P_n,\qquad Tx=\sum_n\lambda_n\langle x,e_n\rangle e_n.$$

**这是真正的对角化**（无限维对角矩阵）。

**推论（紧自伴，极大极小原理）**：$\lambda_n\in\mathbb{R}$，$\lvert\lambda_1\rvert\ge\lvert\lambda_2\rvert\ge\cdots\to0$，

$$\lambda_n=\max_{\dim E=n}\min_{0\ne x\in E}\frac{\langle Tx,x\rangle}{\langle x,x\rangle}.$$

Rayleigh 商变分刻画——有限元法、特征值数值方法的理论基础。

**Fredholm 择一**（紧算子版）：$T$ 紧、$\lambda\ne0$，$(\lambda I-T)x=y$ 要么对每个 $y$ 有唯一解，要么齐次方程有非平凡解。精确地：可解当且仅当 $y\perp\ker(\bar\lambda I-T^*)$，此时 $\operatorname{ran}(\lambda I-T)=\ker(\bar\lambda I-T^*)^\perp$。

**关系链**：迹类 $\subset$ Hilbert–Schmidt $\subset$ 紧 $\subset$ 有界（$\lVert T\rVert\le\lVert T\rVert_{HS}\le\lVert T\rVert_1$）。

---

## 6. Fredholm 算子与指标

**定义（Fredholm 算子）**：$\operatorname{ran}T$ 闭；$\dim\ker T<\infty$；$\dim\ker T^*<\infty$。**指标**

$$\operatorname{ind}T=\dim\ker T-\dim\ker T^*.$$

**Calkin 代数**：$\mathcal K(H)$ 是 $B(H)$ 的闭双侧理想，商代数 $\mathcal Q(H)=B(H)/\mathcal K(H)$ 是 C\* 代数。**本质范数** $\lVert\pi(T)\rVert=\inf_{K\in\mathcal K}\lVert T-K\rVert$。

**定理（Atkinson）**：$T$ **Fredholm** $\iff$ $\pi(T)$ 在 Calkin 代数中**可逆**。

**指标的基本性质**：Fredholm 集是开集、指标在其上**局部常**（小扰动不变）；**紧扰动不变** $\operatorname{ind}(T+K)=\operatorname{ind}T$；$\operatorname{ind}T^*=-\operatorname{ind}T$；$\operatorname{ind}(ST)=\operatorname{ind}S+\operatorname{ind}T$；可逆 + 紧 $\Rightarrow$ 指标 0；指标是**同伦不变量**。

**Toeplitz 算子（指标 = 拓扑量的范例）**：Hardy 空间 $H^2$ = $L^2(\mathbb{T})$ 中负 Fourier 系数为零的闭子空间，$P_+$ 为 Szegő 投影。对 $f\in C(\mathbb{T})$，$T_fg=P_+(fg)$。则

$$T_f\text{ Fredholm}\iff 0\notin f(\mathbb{T}),\qquad \operatorname{ind}T_f=-\operatorname{wind}(f)\ (\text{绕数}).$$

**指标是拓扑量**——由 $f$ 的绕数（同伦不变量）给出，连续变形不经过 0 时指标不变。这是 Atiyah–Singer 指标定理的最简范本。特例：右移 $S=T_z$ 满足 $\operatorname{ind}S=-1$。

---

## 7. 本质谱

**定义**：$\sigma_{\mathrm{ess}}(T)=\sigma_{\mathcal Q(H)}(\pi(T))=\{\lambda:\lambda I-T\text{ 非 Fredholm}\}$。

**基本性质**：$\sigma_{\mathrm{ess}}\subset\sigma$；非空紧集；**紧扰动不变** $\sigma_{\mathrm{ess}}(T+K)=\sigma_{\mathrm{ess}}(T)$；$\lambda\notin\sigma_{\mathrm{ess}}\iff\lambda I-T$ Fredholm。

**Weyl 判据**：$T=T^*$ 自伴，则 $\lambda\in\sigma_{\mathrm{ess}}(T)$ $\iff$ 存在 **Weyl 序列**（正交规范 $\{x_n\}$，$x_n\rightharpoonup0$）使 $(T-\lambda I)x_n\to0$。

**离散谱与本质谱分解**（自伴）：$\sigma(T)=\sigma_{\mathrm{disc}}(T)\sqcup\sigma_{\mathrm{ess}}(T)$，$\sigma_{\mathrm{disc}}$ = 孤立有限重特征值。

**Weyl 定理**：$T$ 自伴、$K$ 紧自伴 $\Rightarrow$ $\sigma_{\mathrm{ess}}(T+K)=\sigma_{\mathrm{ess}}(T)$。即**本质谱对紧（自伴）扰动完全不变**，紧扰动只能移动离散特征值。

**物理对应**：Schrödinger 算子 $H=-\Delta+V$ 加局部紧势不改变本质谱 $[0,\infty)$（连续谱），只引入/移动束缚态（负特征值，离散谱）——"微扰不改变连续谱"的数学证明。

**等价刻画**（自伴）：Fredholm 刻画；Weyl 序列刻画；$\sigma_{\mathrm{ess}}=\sigma\setminus\sigma_{\mathrm{disc}}$；$\sigma_{\mathrm{ess}}=\bigcap_{K\in\mathcal K}\sigma(T+K)$。

**指标与本质谱**：$\mathbb{C}\setminus\sigma_{\mathrm{ess}}(T)$ 的每个连通分支上 $\operatorname{ind}(\lambda I-T)$ 为常数——本质谱的补集正是"指标有定义且局部常"的区域（BDF 理论与 Atiyah–Singer 的起点）。

---

## 8. 应用：紧自伴算子与 Dirichlet 问题

**定理（紧自伴算子谱定理）**：$A=A^*$ 紧，非零特征值 $\lvert\lambda_1\rvert\ge\lvert\lambda_2\rvert\ge\cdots$（计重数），对应标准正交特征向量 $\{u_k\}$，则 $\{u_k\}$ 张成 $\overline{\operatorname{ran}(A)}$，可补上 $\ker(A)$ 的正交基成为 $H$ 的正交基，且

$$Au=\sum_k\lambda_k\langle u,u_k\rangle u_k.$$

**应用（Dirichlet 问题）**：求 $-u''(x)+V(x)u=f(x)$，$u(0)=u(1)=0$。取连续核 $K(x,y)$（$0\le y\le x\le1$ 时 $(x-1)y$，否则 $x(y-1)$），积分算子 $Af(x)=\int_0^1K(x,y)f(y)dy$ 是 $L^2([0,1])$ 上的**紧自伴**算子（Arzelà–Ascoli 给紧，对称性给自伴），$u=Af$ 是 $-u''=f$ 的唯一解。

$A$ 的特征函数 $u_k(x)=\sqrt2\sin(k\pi x)$、特征值 $\lambda_k=\frac{1}{k^2\pi^2}$。由谱定理 $\{\sqrt2\sin(k\pi x)\}_{k\ge1}$ 是 $L^2([0,1])$ 的正交基（振动弦的本征模，也是 Fourier 级数变体）。$V\ge0$ 时用 Fredholm 择一 + 平方根算子 $A^{1/2}$ 证解存在唯一。

---

## 关键结论速查

- **谱 = 广义特征值集合**：无限维里可连续（乘法算子）、可以是圆盘（移位），但总非空、总紧、总在范数圆盘内。
- **谱半径公式** $r(T)=\lim\lVert T^n\rVert^{1/n}$；正规算子 $r(T)=\lVert T\rVert$。
- **谱定理阶梯**：对角化 → 紧正规 $\sum\lambda_n P_n$ → 一般正规 $\int z\,dE(z)$。
- **Fredholm = Calkin 代数可逆元**（Atkinson）；指标 Hermitian 是拓扑不变量，紧扰动不变。
- **Toeplitz 指标** $\operatorname{ind}T_f=-\operatorname{wind}(f)$：分析量 = 拓扑量。
- **本质谱** = 模掉紧扰动的谱；Weyl 定理：紧扰动只动离散谱。
