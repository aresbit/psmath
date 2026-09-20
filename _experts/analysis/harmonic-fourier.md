# 调和分析与 Fourier 分析 (Harmonic Analysis)

> 整理自 Elias M. Stein & Rami Shakarchi《Fourier Analysis: An Introduction》(Princeton Lectures in Analysis, Vol. 1)；Chengchun Hao《Introduction to Harmonic Analysis》(AMSS, 2016)；Elias M. Stein《Singular Integrals and Differentiability Properties of Functions》；Elias M. Stein & Guido Weiss《Introduction to Fourier Analysis on Euclidean Spaces》；Loukas Grafakos《Classical/Modern Fourier Analysis》(GTM 249/250)。

## 0. 一句话心智模型

调和分析研究**如何用简单"波"（正弦波、复指数、Gauss 核）分解与重构一般函数，并研究那些与频带相关的算子**。它的"硬件"是**卷积与逼近恒等**，"软件"是**插值定理与奇异积分算子**。

- **Fourier 级数** = 函数在"频率字典"$\{e^{inx}\}$ 上的展开，$\hat f(n)$ 度量频率 $n$ 处的含量；Parseval 说"能量 = 各频率能量之和"。
- **好核 = 逼近恒等**：Fejér（Cesàro 平均）、Poisson（Abel 平均）是好核，故逐点收敛；Dirichlet 核不是（$\lVert D_N\rVert_{L^1}\sim\log N$）。
- **Fourier 变换 = 对偶性**：把平移不变算子对角化——卷积变乘积，微分变乘法 $(2\pi i\xi)^\alpha$。
- **缓增分布** = 连续线性泛函，统一 $\delta$、$\operatorname{p.v.}1/x$ 与常函数。
- **插值** = 用两端推中间（Riesz–Thorin 复插值、Marcinkiewicz 弱型实插值）。
- **奇异积分** = 靠奇对称消去的主值，在 $L^p\,(1<p<\infty)$ 上有界。

**归一化约定**：$\hat f(\xi)=\int f(x)e^{-2\pi ix\xi}dx$，故 $\widehat{e^{-\pi x^2}}=e^{-\pi\xi^2}$、Parseval/Plancherel 无常数。

---

## 1. Fourier 级数的起源与好核

**动机**：振动弦方程 $\partial_t^2u=\partial_x^2u$ 与热方程 $\partial_tu=\partial_x^2u$ 用分离变量都引出"把函数展成三角函数之和"。热方程解 $u=\sum\hat f(n)e^{inx}e^{-n^2t}$（**热核** $H_t=\sum e^{-n^2t}e^{inx}$）：**热流逐频率指数衰减，高频先消失**——"频率滤波"思想的最早体现。

**Fourier 系数与卷积**（$2\pi$ 周期 $f$）：

$$\hat f(n)=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(\theta)e^{-in\theta}d\theta,\qquad (f*g)(x)=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(y)g(x-y)dy.$$

**核心字典**：$\widehat{f*g}(n)=\hat f(n)\hat g(n)$——**卷积在频域变乘法**。

**定义（好核）**：$\{K_n\}$ 且 (1) $\frac{1}{2\pi}\int K_n=1$；(2) $\lVert K_n\rVert_{L^1}\le M$ 一致有界；(3) 对每个 $\delta>0$，$\int_{\delta\le\lvert x\rvert\le\pi}\lvert K_n\rvert\to0$。

**定理（好核逼近）**：$K_n$ 好核、$f$ 在 $x$ 连续 $\Rightarrow$ $(f*K_n)(x)\to f(x)$；$f$ 处处连续则一致收敛。

- **Fejér 核**（Dirichlet 核的算术平均）$F_N(x)=\frac{1}{N+1}\frac{\sin^2((N+1)x/2)}{\sin^2(x/2)}$ 是好核（Cesàro 求和），给出 **Weierstrass 逼近定理**；
- **Poisson 核** $P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}$（$r\to1^-$）是好核（Abel 求和），同时是圆盘 Dirichlet 问题的解核。

---

## 2. Fourier 级数的收敛

**$L^2$（均方）收敛**：$S_N(f)$ 是所有 $\le N$ 次三角多项式中 $L^2$ 距离最小者（正交投影）。**Bessel** $\sum\lvert\hat f(n)\rvert^2\le\lVert f\rVert_{L^2}^2$；**Parseval** $\lVert f\rVert_{L^2}^2=\sum\lvert\hat f(n)\rvert^2$，且 $S_N(f)\to f$ 在 $L^2$ 收敛。故 $\{e^{inx}\}$ 是 $L^2$ 的完备正交基。

**Dirichlet 核与逐点收敛**：$D_N(x)=\frac{\sin((N+\frac12)x)}{\sin(x/2)}$，$S_N(f)=f*D_N$。**为何不是好核**：$\lVert D_N\rVert_{L^1}\sim\frac{4}{\pi^2}\log N\to\infty$，条件 (2) 被破坏——这正是 Fourier 级数对连续函数也可能在某点发散（du Bois-Reymond 反例）的原因。

**定理（Dirichlet 逐点收敛）**：$f$ 分段光滑 $\Rightarrow$ $S_N(f)(x)\to\frac{f(x^+)+f(x^-)}{2}$（连续点收敛到 $f(x)$）。证明用 **Riemann–Lebesgue 引理**：$f\in L^1\Rightarrow\hat f(n)\to0$（高频振荡积分相消）。

**Gibbs 现象**：跳跃间断点附近过冲不随 $N\to\infty$ 消失，稳定在约 $9\%$（精确 $0.0895$）的跃度。机理：$D_N$ 的振荡主峰与函数卷积产生不消失的过冲——"Dirichlet 核不是好核"在逐点层面的后果（好核 Fejér 不会有 Gibbs）。

---

## 3. Fourier 级数的应用

**等周不等式**：$\mathcal A\le\ell^2/4\pi$，等号当且仅当圆。Fourier 证法：用弧长参数化 + Green 面积公式 + Parseval，把面积/弧长都用频率系数表出，得"高频分量浪费周长却不增加面积"。

**Weyl 等分布**：$\{\xi_n\}$ 等分布（每个区间 $[a,b)$ 的频率趋于 $b-a$）$\iff$ 对每个非零整数 $k$，$\frac1N\sum_{n=1}^N e^{2\pi ik\xi_n}\to0$（**Weyl 判据**）。**Kronecker–Weyl**：$\alpha$ 无理 $\Rightarrow$ $\{n\alpha\}$ 等分布（几何级数 + 判据）。这是"相消 → 均匀"的桥梁。

**热方程**：$u=(f*H_t)$，$H_t$ 是好核；对任意 $t>0$ 解是 $C^\infty$（**抛物正则性**）；$t\to\infty$ 时趋于平均值 $\hat f(0)$。

**Wirtinger 不等式**：$f$ 零平均 $\Rightarrow$ $\int\lvert f\rvert^2\le\int\lvert f'\rvert^2$，由 Parseval 与 $\widehat{f'}(n)=in\hat f(n)$、$\lvert n\rvert\ge1$ 立即得到——一维 Poincaré 不等式的原型。

---

## 4. 直线上的 Fourier 变换

**Schwartz 空间** $\mathcal S(\mathbb{R})$：$C^\infty$ 且 $\sup_x\lvert x^\alpha f^{(\beta)}(x)\rvert<\infty$（速降）。它是 Fourier 变换的"不动点"。定义 $\hat f(\xi)=\int f(x)e^{-2\pi ix\xi}dx$。

**对偶字典**：

1. 平移 $\leftrightarrow$ 调制：$\widehat{f(x-h)}=\hat f(\xi)e^{-2\pi ih\xi}$；
2. 伸缩 $\leftrightarrow$ 反伸缩；
3. **微分 $\leftrightarrow$ 乘法**：$\widehat{f'}(\xi)=2\pi i\xi\hat f(\xi)$；
4. **卷积 $\leftrightarrow$ 乘积**：$\widehat{f*g}=\hat f\hat g$；
5. **Parseval**：$\int f\bar g=\int\hat f\overline{\hat g}$。

核心信息：**Fourier 变换把微分算子对角化**——求导变成乘 $2\pi i\xi$，常系数微分方程在频域变成代数方程。

**Gauss 核** $e^{-\pi x^2}$ 是 $\mathcal F$ 的特征函数：$\widehat{e^{-\pi x^2}}(\xi)=e^{-\pi\xi^2}$。**反演定理**：$f(x)=\int\hat f(\xi)e^{2\pi ix\xi}d\xi$，即 $\hat{\hat f}(x)=f(-x)$，$\mathcal F^4=\mathrm{id}$（周期 4）。

**定理（Plancherel）**：Fourier 变换从 $\mathcal S\cap L^2$ 保范延拓到 $L^2(\mathbb{R})$ 上的酉算子：$\lVert\hat f\rVert_{L^2}=\lVert f\rVert_{L^2}$。故频率空间与物理空间"能量守恒"。

**Poisson 求和公式**：$f\in\mathcal S\Rightarrow\sum_n f(n)=\sum_n\hat f(n)$。取 $f=e^{-\pi tx^2}$ 得 $\theta$ 函数函数方程 $\sum_n e^{-\pi n^2t}=t^{-1/2}\sum_n e^{-\pi n^2/t}$，通向解析数论。

**Heisenberg 不确定性原理**：$\lVert f\rVert_{L^2}=1$ 时 $\left(\int x^2\lvert f\rvert^2\right)\left(\int\xi^2\lvert\hat f\rvert^2\right)\ge\frac{1}{16\pi^2}$，等号当且仅当 $f$ 是 Gauss 函数。物理上 $\Delta x\cdot\Delta\xi\ge\frac{1}{4\pi}$。证明：分部积分 + Cauchy–Schwarz + Plancherel。

---

## 5. $\mathbb{R}^d$ 与有限 Fourier 分析

**多维**：对偶字典逐条成立（$\widehat{\partial^\alpha f}=(2\pi i\xi)^\alpha\hat f$、卷积 $\to$ 乘积、Plancherel）；新现象是**旋转不变 → 径向 → Bessel 函数**：$f=f_0(\lvert x\rvert)$ 时 $\hat f(\xi)=2\pi\lvert\xi\rvert^{-\frac{d-2}{2}}\int_0^\infty f_0(s)J_{\frac{d-2}{2}}(2\pi\lvert\xi\rvert s)s^{d/2}ds$（径向 Fourier 变换 = Hankel 变换）。

**波方程**：$\hat u=\hat f(\xi)\cos(2\pi\lvert\xi\rvert t)$；$d=3$ 给出 **Kirchhoff 公式**（初值沿球面传播，Huygens 原理），偶数维 $d=2$ 有"尾巴"（无强 Huygens 原理）。

**Radon 变换** $\mathcal R(f)(t,s)=\int_{x\cdot t=s}f\,d\sigma$；**投影切片定理** $\widehat{\mathcal R(f)(t,\cdot)}(s)=\hat f(st)$——CT 断层扫描的数学基础。

**Bessel 函数** $J_n(x)=\frac{1}{2\pi}\int_0^{2\pi}e^{ix\sin\theta}e^{-in\theta}d\theta$；**Jacobi–Anger** $e^{ix\sin\theta}=\sum_n J_n(x)e^{in\theta}$；大 $x$ 渐近 $J_n(x)\sim\sqrt{2/\pi x}\cos(x-n\pi/2-\pi/4)$。

**有限 Fourier 分析**：群 $\mathbb{Z}(N)$ 上 **DFT** $\hat a(k)=\sum_{n=0}^{N-1}a(n)\zeta_N^{-kn}$（$\zeta_N=e^{2\pi i/N}$）是酉变换；**FFT** 把 $N$ 点 DFT 拆成两个 $N/2$ 点 DFT 递归，复杂度 $O(N\log N)$（Cooley–Tukey）。

---

## 6. 缓增分布

**动机**：$\delta$ 函数、$\operatorname{p.v.}\frac1x$、常函数的 Fourier 变换在经典函数框架里装不下。**分布的思想**：不问"在点 $x$ 取值多少"，而问"对测试函数 $\varphi$ 作用多少"。

**缓增分布**：Schwartz 空间 $\mathcal S(\mathbb{R}^d)$ 上的连续线性泛函（全体 $\mathcal S'$），配对 $\langle u,\varphi\rangle$。$L^p$、多项式、常函数都嵌入 $\mathcal S'$。

**运算（对偶定义）**：导数 $\langle\partial^\alpha u,\varphi\rangle=(-1)^{\lvert\alpha\rvert}\langle u,\partial^\alpha\varphi\rangle$；乘法 $\langle fu,\varphi\rangle=\langle u,f\varphi\rangle$；**Fourier 变换** $\langle\hat u,\varphi\rangle=\langle u,\hat\varphi\rangle$。

**基本公式块（务必内化）**：

| 分布 | Fourier 变换 |
|------|--------------|
| Dirac $\delta$ | $\hat\delta=1$ |
| 常函数 $1$ | $\hat 1=\delta$ |
| 调制 $e^{2\pi iax}$ | $\delta_a$ |
| 主值 $\operatorname{p.v.}\frac1x$ | $-\pi i\operatorname{sgn}(\xi)$ |
| 符号函数 $\operatorname{sgn}$ | $\frac{1}{\pi i}\operatorname{p.v.}\frac1\xi$ |

**心智模型**："奇点 → 高频符号"：$\delta$（集中）$\leftrightarrow$ 常数（全频带）；$\operatorname{p.v.}1/x$（奇点）$\leftrightarrow$ $\operatorname{sgn}$（有界不连续）。这是 Hilbert 变换作为 Fourier 乘子的出发点。

---

## 7. 算子插值

**记号**：$T$ 强 $(p,q)$ 型指 $\lVert Tf\rVert_{L^q}\le A\lVert f\rVert_{L^p}$；**弱 $L^p$**（$L^{p,\infty}$）$\lVert f\rVert_{L^{p,\infty}}=\sup_{\lambda>0}\lambda\lvert\{\lvert f\rvert>\lambda\}\rvert^{1/p}$。

**定理（Riesz–Thorin 复插值）**：线性 $T$ 满足两端强型 $\lVert Tf\rVert_{L^{q_i}}\le M_i\lVert f\rVert_{L^{p_i}}$（$i=0,1$），则对 $\theta\in[0,1]$，

$$\frac1{p_\theta}=\frac{1-\theta}{p_0}+\frac{\theta}{p_1},\quad \frac1{q_\theta}=\frac{1-\theta}{q_0}+\frac{\theta}{q_1},\qquad \lVert T\rVert_{L^{p_\theta}\to L^{q_\theta}}\le M_0^{1-\theta}M_1^\theta.$$

证明核心：**Hadamard 三线定理**（带域上解析函数的边界控制内部）。**应用（Hausdorff–Young）**：由平凡端点 $(1,\infty)$ 与 Plancherel 端点 $(2,2)$，得 $\lVert\hat f\rVert_{L^q}\le\lVert f\rVert_{L^p}$（$1\le p\le2$，$1/p+1/q=1$）。

**定理（Marcinkiewicz 实插值）**：次线性算子 $T$ 在弱 $(p_0,q_0)$、弱 $(p_1,q_1)$ 型（$q_0\ne q_1$）则内部强 $(p_\theta,q_\theta)$ 型。证明：**层饼分解** $\lVert Tf\rVert_{L^q}^q=q\int_0^\infty\lambda^{q-1}\lvert\{\lvert Tf\rvert>\lambda\}\rvert\,d\lambda$ + 按高度拆 $f=f_\lambda+f^\lambda$。

**Stein 复插值**允许算子族 $\{T_z\}$ 随 $z$ 解析变化，可处理分数次积分与带权估计。

**心智模型**："两端推中间"，$L^p$ 有界性在参数平面形成凸区域，范数是 $\theta$ 的对数凸函数。复插值（解析，需强型）与实插值（层饼，需弱型）互补。

---

## 8. 奇异积分

**Hardy–Littlewood 极大函数** $Mf(x)=\sup_{Q\ni x}\frac{1}{\lvert Q\rvert}\int_Q\lvert f\rvert$：

- **弱 $(1,1)$**：$\lvert\{Mf>\lambda\}\rvert\le\frac{C_d}{\lambda}\lVert f\rVert_{L^1}$（证明用 **Vitali 覆盖引理**）；
- **强 $(p,p)$**（$1<p\le\infty$）：由弱 $(1,1)$ + 平凡 $(\infty,\infty)$ 用 Marcinkiewicz 插值。

**Hilbert 变换** $Hf(x)=\frac1\pi\operatorname{p.v.}\int\frac{f(y)}{x-y}dy$，其 **Fourier 乘子**表示 $\widehat{Hf}(\xi)=-i\operatorname{sgn}(\xi)\hat f(\xi)$（把每个频率分量乘 $-i\operatorname{sgn}$，即正/负频率分别相移 $\mp90^\circ$）。有界性：$1<p<\infty$ 时 $\lVert Hf\rVert_{L^p}\le C_p\lVert f\rVert_{L^p}$；端点 $L^1$ 只有**弱型**（非强型）、$L^\infty$ 落 **BMO**。

**Calderón–Zygmund 分解**：$f\in L^1$、$\lambda>0$ 时 $f=g+b$，$b=\sum_j b_j$，满足 $\lvert g\rvert\le c_d\lambda$ a.e.（好部分有界）；每个 $b_j$ 支撑在两两不交的二进方体 $Q_j$ 上且 $\int_{Q_j}b_j=0$（**坏部分零均值**）；$\sum_j\lvert Q_j\rvert\le\frac{C_d}{\lambda}\lVert f\rVert_{L^1}$。**零均值**使坏部分与奇异核卷积时"消去"奇点主值项。

**标准核**：$\lvert K(x)\rvert\le A\lvert x\rvert^{-d}$；$\lvert\nabla K\rvert\le A\lvert x\rvert^{-d-1}$；消去条件 $\int_{\varepsilon<\lvert x\rvert<R}K=0$。

**定理（Calderón–Zygmund）**：CZO（$Tf=\operatorname{p.v.}(f*K)$ 且 $L^2$ 有界）满足弱 $(1,1)$、强 $(p,p)$（$1<p<\infty$）、映 $L^\infty\to BMO$。证明骨架：$L^2$ 有界 + CZ 分解（好部分用 $L^2$，坏部分用零均值 + 核的导数衰减 $\lvert x\rvert^{-d-1}$）得弱 $(1,1)$，再用 Marcinkiewicz 插值。

**Riesz 变换** $\widehat{R_jf}(\xi)=-i\frac{\xi_j}{\lvert\xi\rvert}\hat f(\xi)$，满足 $\sum_{j=1}^d R_j^2=-I$（$R_j$ 是 $\partial_j(-\Delta)^{-1/2}$ 的化身），是 Sobolev 空间与位势论的核心工具。

**心智模型**："奇点靠消去"；"弱端点 + 插值"是标准流程（极大函数、Hilbert 变换、CZO 三者同套打法）；Fourier 乘子是奇异积分的"身份证"（频域的不连续 $\leftrightarrow$ 空间的奇异核）。

---

## 关键结论速查

- **好核三条件**：总质量 1、$L^1$ 一致有界、质量集中原点。Fejér/Poisson 是，Dirichlet 不是（$\lVert D_N\rVert_{L^1}\sim\log N$）。
- **对偶字典**：平移↔调制、微分↔乘 $2\pi i\xi$、卷积↔乘积、伸缩↔反伸缩。
- **Gauss 核**是 Fourier 特征函数，也是好核、热核、不确定性原理极值点。
- **分布最常用公式块**：$\hat\delta=1$、$\hat1=\delta$、$\widehat{\operatorname{p.v.}1/x}=-\pi i\operatorname{sgn}\xi$。
- **插值**：两端推中间；复插值（Riesz–Thorin）需强型，实插值（Marcinkiewicz）需弱型。
- **奇异积分三定理**：弱 $(1,1)$ + 强 $(p,p)$ + $L^\infty\to BMO$，靠 CZ 分解与零均值消去。
