# 最优传输 (Optimal Transport, OT)

> 整理自 Gabriel Peyré & Marco Cuturi《Computational Optimal Transport》(arXiv:1803.00567)；Cédric Villani《Optimal Transport: Old and New》(2009) 与《Topics in Optimal Transportation》(2003)；Filippo Santambrogio《Optimal Transport for Applied Mathematicians》(Birkhäuser, 2015)。

## 0. 一句话定位

最优传输研究**"以最小代价把一份质量分布搬成另一份"的数学**。给定源分布 $\mu$、目标分布 $\nu$ 与搬一单位质量从 $x$ 到 $y$ 的代价 $c(x,y)$，OT 问：什么样的搬运方案使总代价最小？这个最小值本身诱导出分布空间上的一个**距离**——Wasserstein 距离 $W_p$，它度量"把 $\mu$ 变成 $\nu$ 需要搬多远"，比 KL/TV 更贴合几何直觉。

**核心心智模型**：

- **push-forward** $T_\sharp\mu$ = "按映射搬运质量"；
- **Monge 问题** = "一针一货、不许分拆"（刚性、可能无解）；
- **Kantorovich 松弛** = "允许分拆的耦合"，是**线性规划**（有对偶、有强对偶）；
- **Wasserstein 距离** = "OT 最小值当度量"，度量弱收敛；
- **对偶** = "用价格而不是方案算最小值"；
- **Brenier 定理** = "最优映射是凸函数的梯度"；
- **熵正则 OT** = "OT 加可微、可并行求解的软化项"（Sinkhorn）。

---

## 1. 测度、push-forward 与耦合

**测度作为质量分布**：Radon 测度 $\mu$ 给每个可测集分配质量；概率测度 $\mu(X)=1$。密度由 **Radon–Nikodym 定理**连接：$\mu(A)=\int_A\rho\,dx$。**离散测度** $\alpha=\sum_ia_i\delta_{x_i}$。离散与连续测度用**同一套框架**。

**push-forward（前推）**：对可测 $T:X\to Y$，$(T_\sharp\mu)(B)=\mu(T^{-1}(B))$。直觉：目标区域 $B$ 收到的质量 = 源里"会被搬进 $B$"的那些 $x$ 的总质量——**质量守恒的换元公式**。实用形式（期望换元）：

$$\int_Yh(y)\,d(T_\sharp\mu)(y)=\int_Xh(T(x))\,d\mu(x).$$

密度版换元（$T$ 可逆光滑）：$\rho_T(y)=\rho(T^{-1}(y))\lvert\det\nabla T^{-1}(y)\rvert$（$\lvert\det\nabla T\rvert$ = 体积被拉伸的倍数）。

**耦合 (coupling)**：$\mu\in\mathcal{P}(X)$、$\nu\in\mathcal{P}(Y)$ 的耦合是 $X\times Y$ 上概率测度 $\pi$，边缘分别为 $\mu,\nu$：

$$\pi(A\times Y)=\mu(A),\qquad\pi(X\times B)=\nu(B).$$

记全体为 $\Pi(\mu,\nu)$。边缘 = 投影映射的 push-forward。**两个极端耦合**：独立耦合 $\mu\otimes\nu$（零相关）；确定耦合 $\pi=(\mathrm{Id},T)_\sharp\mu$（质量压在函数图像上——Monge 方案的几何意义）。

**离散版**：$\mu=\sum_ia_i\delta_{x_i}$、$\nu=\sum_jb_j\delta_{y_j}$ 时，耦合是非负矩阵 $P$ 满足 $P\mathbf 1=a$、$P^\top\mathbf 1=b$；全体记 $\mathbf U(a,b)$，是**运输多面体 (transport polytope)**。

**相对熵**：$\mathrm{KL}(\pi\mid\xi)=\int\log\frac{d\pi}{d\xi}d\pi+\int(d\xi-d\pi)$，在熵正则 OT 与 Schrödinger 桥中作正则项。

---

## 2. Monge 问题与 Kantorovich 松弛

**Monge 问题（1781）**：找单一映射 $T:X\to Y$ 满足 $T_\sharp\mu=\nu$，最小化

$$\min_T\int_Xc(x,T(x))\,d\mu(x)\quad\text{s.t.}\quad T_\sharp\mu=\nu.$$

**Monge 的三大毛病**：(1) 可能无解（$\mu=\delta_{x_0}$、$\nu=\frac12\delta_{y_1}+\frac12\delta_{y_2}$，整份质量凑不出两个半份）；(2) 约束 $T_\sharp\mu=\nu$ 关于 $T$ 非线性（含 $\det\nabla T$），可行集非凸；(3) 最优映射未必存在（只在"几乎处处"意义达到）。

**Kantorovich 松弛（1942）**：不要求单一映射，只要求耦合 $\pi\in\Pi(\mu,\nu)$：

$$L_c(\mu,\nu)=\min_{\pi\in\Pi(\mu,\nu)}\int_{X\times Y}c(x,y)\,d\pi(x,y).$$

**为什么是"松弛"**：每个 Monge 映射对应完全相关耦合 $(\mathrm{Id},T)_\sharp\mu$，故 (K) 可行域 $\supset$ (M) 可行域。而 (K) 是**线性规划**（目标对 $\pi$ 线性、约束线性），自动继承 LP 的**强对偶**与**顶点结构**。

**离散版**：$L_C(a,b)=\min_{P\ge0}\langle C,P\rangle$ s.t. $P\mathbf 1=a,\ P^\top\mathbf 1=b$。可行集 $\mathbf U(a,b)$ 有 $n+m-1$ 个独立等式约束；其**顶点**是"支撑成树"的矩阵。当 $a=b=\mathbf 1/n$ 时顶点是**置换矩阵**——最优解即经典**指派问题 (assignment problem)**。

**Monge = Kantorovich 何时成立**：一维凸代价（最优映射单调非减）；高维二次代价 + $\mu$ 有密度（最优映射 $=\nabla\varphi$）；但**离散测度**时 (M) 无解而 (K) 有解，松弛是**严格**的。

---

## 3. Wasserstein 距离

**定义**：$c(x,y)=d(x,y)^p$（$p\ge1$），

$$W_p(\mu,\nu)=\left(\inf_{\pi\in\Pi(\mu,\nu)}\int_{\Omega\times\Omega}d(x,y)^p\,d\pi(x,y)\right)^{1/p}.$$

即 $W_p^p$ = 代价 $d^p$ 的 Kantorovich 最小值。"把 $\mu$ 搬成 $\nu$ 需要搬多远"的最优代价。最常见 $W_1$（平均搬运距离）与 $W_2$（均方搬运距离，有黎曼结构）。

**三条度量公理**：正定性（$W_p=0\iff\mu=\nu$，因 $\pi$ 支撑在对角线上）；对称性；**三角不等式**（证明靠**胶合引理**：把 $\mu$–$\rho$ 与 $\rho$–$\nu$ 的最优耦合沿 $\rho$ 粘起来，再用 Minkowski）。

**$W_p$ 度量弱收敛（招牌性质）**：

$$\mu_k\xrightarrow{\text{weak}}\mu\iff W_p(\mu_k,\mu)\to0$$

（紧空间或矩一致收敛下）。**为什么了不起**：KL/TV 不具备——两个 Dirac 质量 $\delta_{x_k}$、$\delta_x$ 只要 $x_k\ne x$，KL/TV 都是 $+\infty$，但 $W_p(\delta_{x_k},\delta_x)=d(x_k,x)\to0$。**$W_p$ 能"看见"空间位置**。$W_p(\delta_x,\delta_y)=d(x,y)$，故 $x\mapsto\delta_x$ 是**等距嵌入**。

**$W_1$ 的 Kantorovich–Rubinstein 对偶**：

$$W_1(\mu,\nu)=\sup_{\lVert f\rVert_{\mathrm{Lip}}\le1}\left(\int f\,d\mu-\int f\,d\nu\right),$$

上确界取遍 1-Lipschitz 函数。直觉：用最陡不过 1 的测试函数去区分 $\mu,\nu$ 的最大区分度（**积分概率度量 IPM** 的实例；WGAN 判别器目标的数学来源）。

**高斯情形的 $W_2$ 闭式解**（Gelbrich 1990）：$\mu=\mathcal N(m_0,\Sigma_0)$、$\nu=\mathcal N(m_1,\Sigma_1)$ 时

$$W_2^2(\mu,\nu)=\lVert m_0-m_1\rVert^2+\operatorname{tr}\left(\Sigma_0+\Sigma_1-2(\Sigma_0^{1/2}\Sigma_1\Sigma_0^{1/2})^{1/2}\right).$$

一维退化为 $W_2^2=(\Delta m)^2+(\Delta\sigma)^2$。这是生成模型评估指标 **FID (Fréchet Inception Distance)** 的数学源头。

**测地线（McCann 插值）**：若 $T$ 是最优映射（Brenier 意义），$\mu_t=((1-t)\mathrm{Id}+tT)_\sharp\mu$，$t\in[0,1]$。每个质量点沿"当前位置到目标位置的直线"匀速移动——$W_2$ 空间的"直线"，Wasserstein 梯度流的几何基础。

---

## 4. Kantorovich 对偶与 $c$-变换

(K) 是 LP，配一个对偶（强对偶成立）。**带约束的对偶（位势形式）**：

$$L_c(\mu,\nu)=\sup_{(f,g)\in\mathcal{R}(c)}\int f\,d\mu+\int g\,d\nu,\qquad\mathcal R(c)=\{f(x)+g(y)\le c(x,y)\}.$$

$f,g$ 称 **Kantorovich 位势**。**无约束形式**：$L_c=\sup_{f,g}\int f\,d\mu+\int g\,d\nu+\min_{x,y}(c-f-g)$。离散版 $L_C(a,b)=\max_{f_i+g_j\le C_{ij}}\langle f,a\rangle+\langle g,b\rangle$。

**经济直觉（物流外包定价）**：货主可把运输外包给物流商，物流商报价 = 收货价 $f_i$ + 送货价 $g_j$；货主接受当且仅当报价不高于自运成本 $f_i+g_j\le C_{ij}$。物流商在约束下最大化报价。**强对偶**：物流商能榨出的最高报价 = 货主自运的最优成本。

**$c$-变换**：给定 $f$，$g$ 的最大允许值是确定的：

$$f^c(y)=\inf_{x\in X}(c(x,y)-f(x)).$$

于是对偶可压成一个函数 $L_c(\mu,\nu)=\sup_f\int f\,d\mu+\int f^c\,d\nu$。$f=f^{c\bar c}$ 的 $f$ 称 **$c$-凹**；$f^{cc}$ 是 $f$ 的 $c$-凸包络。当 $c(x,y)=\lVert x-y\rVert^2$ 时，$c$-变换退化为 **Legendre–Fenchel 共轭** $f^*(y)=\sup_x(\langle x,y\rangle-f(x))$。

**互补松弛**：最优 $\pi^\star$ 与最优位势满足

$$\operatorname{supp}(\pi^\star)\subset\{(x,y):f^\star(x)+g^\star(y)=c(x,y)\}.$$

最优方案只把质量搬到"报价恰好等于成本"的路线（$f+g=c$）上。

**$W_1$ 的 KR 对偶**是 $c=d$ 的特例：约束 $f(x)+g(y)\le d(x,y)$ 等价于"$f=-g$ 且 $f$ 是 1-Lipschitz"。

---

## 5. Brenier 定理与 Monge–Ampère 方程

**定理（Brenier）**：$X=Y=\mathbb{R}^d$，$c(x,y)=\lVert x-y\rVert^2$，$\mu$ 关于 Lebesgue 测度**有密度**。则 (K) 的最优 $\pi$ **唯一**，且支撑在某个 **Monge 映射** $T$ 的图像上：

$$\pi=(\mathrm{Id},T)_\sharp\mu,\qquad T=\nabla\varphi,$$

其中 $\varphi$ 是**凸函数**（唯一，相差加性常数），满足 $(\nabla\varphi)_\sharp\mu=\nu$；且 $\varphi(x)=\frac{\lVert x\rVert^2}{2}-f(x)$。**一句话**：二次代价下，最优搬运是"凸函数的梯度"。

**证明骨架（拆平方 + 凸对偶 + 互补松弛）**：

1. **拆平方** $\lVert x-y\rVert^2=\lVert x\rVert^2+\lVert y\rVert^2-2\langle x,y\rangle$，最小化 $\int\lVert x-y\rVert^2d\pi$ 等价于最大化 $\int\langle x,y\rangle d\pi$；
2. 写对偶 $\min_{\varphi,\psi:\varphi(x)+\psi(y)\ge\langle x,y\rangle}\int\varphi d\mu+\int\psi d\nu$；
3. 用共轭消掉 $\psi$（取 $\psi=\varphi^*$，Legendre–Fenchel 共轭）得 $\min_\varphi\int\varphi d\mu+\int\varphi^*d\nu$；
4. 两次共轭 $\varphi^{**}$ 是凸的且目标值不增，故可设 $\varphi$ 凸；
5. 读梯度：互补松弛说最优 $\pi$ 支撑在 $\varphi(x)+\varphi^*(y)=\langle x,y\rangle$ 处，凸函数下 $y\in\partial\varphi(x)$（次梯度），因 $\varphi$ 几乎处处可微、$\mu$ 有密度，得 $y=\nabla\varphi(x)$（a.e.）。

**Monge–Ampère 方程**：若 $\mu,\nu$ 都有密度，则

$$\det(\nabla^2\varphi(x))\,\rho_\nu(\nabla\varphi(x))=\rho_\mu(x).$$

$\det(\nabla^2\varphi)$ 扮演"非线性退化拉普拉斯"角色（线性化后回到 $\Delta$）；凸性强制 $\det(\nabla^2\varphi)\ge0$。

**一维情形**：凸函数梯度 $\varphi'$ 单调非减，最优映射由**分位函数**显式给出 $T=F_\nu^{-1}\circ F_\mu$（CDF 的广义逆）——"按排名配对"。**凸函数梯度 = 高维的"单调增"**。

**边界（如实说明）**：正则性理论（Caffarelli 学派）、Alexandrov 弱解、多边际/非二次代价的完整对偶定理属于进阶缺口。

---

## 6. 熵正则 OT 与 Sinkhorn

在 OT 目标上加**熵正则** $-\varepsilon H(\pi)$；最优解变成 Gibbs 核的 KL 投影，可用 **Sinkhorn 算法**（矩阵缩放，交替归一化行列）以 GPU 友好方式求解。它同时是**静态 Schrödinger 问题**（OT 与 SDE 之间的桥）。$\varepsilon\to0$ 恢复原 OT，$\varepsilon\to\infty$ 趋于独立耦合。

---

## 7. Benamou–Brenier 动态公式

**从静态耦合到动态流**：搬运是随时间进行的连续过程，$\rho_t$ 是 $t$ 时刻密度、$v_t$ 是速度场，**连续性方程**（质量守恒的 PDE）：

$$\partial_t\rho_t+\nabla\cdot(\rho_tv_t)=0,\qquad\rho_0=\mu,\ \rho_1=\nu.$$

（这是 Fokker–Planck 方程去掉扩散项的确定性版本。）

**定理（Benamou–Brenier）**：

$$W_2^2(\mu,\nu)=\inf_{(\rho_t,v_t)}\int_0^1\int_{\mathbb{R}^d}\lVert v_t(x)\rVert^2\rho_t(x)\,dx\,dt\quad\text{s.t.}\quad(\text{连续性方程}).$$

**直觉**：把 $\mu$ 变成 $\nu$ 的最优方式是让每个质量点"匀速直线"运动（最小动能 ⟺ 测地直线，对应 McCann 插值）。**为什么重要**：(1) 把 $W_2$ 变成**凸优化**问题（目标对 $(\rho,v)$ 凸、约束线性），可数值求解（增广拉格朗日/ADMM/近端）；(2) 揭示 **$W_2$ 空间是黎曼流形**——右边是"切向量 $v_t$ 平方范数沿曲线的积分"，正是"两点距离 = 测地线长度"的定义。这是 **Otto 框架**（Wasserstein 梯度流）的起点。

**$W_1$ 的动态对应**：**Beckmann 问题**（最小化总通量 $\int\lVert w\rVert$，$\nabla\cdot w=\mu-\nu$）。

**三条出路**：Wasserstein 梯度流（$\partial_t\rho=\nabla\cdot(\rho\nabla F'(\rho))$）；Schrödinger 桥（确定流加扩散项）；扩散模型的 PF-ODE/直线流正是逼近 (7.2) 的最优直线流。

---

## 关键结论速查

- **Monge (M)** 刚性、非凸、可能无解；**Kantorovich (K)** 允许分拆，是 LP，凸、好优化。
- **$W_p$ 度量弱收敛**（KL/TV 不能）；$W_p(\delta_x,\delta_y)=d(x,y)$；$W_1$ 有 KR 对偶（1-Lipschitz 测试函数）。
- **对偶** = 物流外包定价；**$c$-变换**把对偶压成一个函数（$c=\lVert x-y\rVert^2$ 时退化为 Legendre 共轭）；**互补松弛**：最优方案支撑在 $f+g=c$ 处。
- **Brenier**：二次代价 + $\mu$ 有密度 ⟹ 最优映射 $T=\nabla\varphi$（凸函数梯度），$\varphi$ 满足 **Monge–Ampère** 方程；一维退化为分位函数 $F_\nu^{-1}\circ F_\mu$。
- **高斯 $W_2$ 闭式解**是 FID 的源头。
- **Benamou–Brenier**：$W_2^2$ = 最小动能，揭示 $W_2$ 的黎曼结构（Otto 框架）。
