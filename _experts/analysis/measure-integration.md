# 测度论与 Lebesgue 积分 (Measure Theory and Lebesgue Integration)

> 整理自 MIT OCW 18.102《Introduction to Functional Analysis》(Spring 2021, Casey Rodriguez；Melrose 讲义)；V. I. Bogachev《Measure Theory》。push-forward/耦合部分整理自 Peyré & Cuturi《Computational Optimal Transport》§2.1。

## 0. 为什么需要 Lebesgue 积分

目标：造一种比 Riemann 积分更一般的积分，使**可积函数构成 Banach 空间**。Riemann 可积函数空间 $L^1_R([0,1])$ 赋 $\lVert f\rVert_1=\int_0^1\lvert f\rvert dx$ **不完备**（构造出的柯西列极限可能不可 Riemann 积），这正是 Lebesgue 积分取代 Riemann 的根源——如同 $\mathbb{Q}$ 不完备而需 $\mathbb{R}$。

**对测度 $m$ 的四个期望**：能测 $\mathbb{R}$ 的一切子集；区间测度 = 长度；**可数可加性**；**平移不变性**。**Vitali 构造**说明这四条对 $\mathcal{P}(\mathbb{R})$ 上一切集合无法同时满足，故采取 Carathéodory 策略：放弃第一条，只测"表现良好"的子集。

---

## 1. 外测度与可测集

**定义（外测度）**：对 $A\subset\mathbb{R}$，

$$m^*(A)=\inf\left\{\sum_n\ell(I_n):\{I_n\}\text{ 可数个开区间},\ A\subset\bigcup_n I_n\right\}.$$

性质：单调性；**可数集零测度**（$m^*(\mathbb{Q})=0$）；**可数次可加性** $m^*(\bigcup_n A_n)\le\sum_n m^*(A_n)$；平移不变；区间测度正确 $m^*(I)=\ell(I)$。缺的正是**可数可加性**。

**定义（可测集，Carathéodory 条件）**：$E$ 可测，若对一切 $A\subset\mathbb{R}$，

$$m^*(A)=m^*(A\cap E)+m^*(A\cap E^c).$$

（反向不等式由次可加性恒成立；直观：$E$ 把任意 $A$"切得干净"。）**可数可加性只有在可测集上才成立**——把外测度限制到可测集上就"修复"了这条性质。

**σ-代数**：对补集与**可数并**封闭的集族（由 De Morgan 也对可数交封闭，必含 $\varnothing,\mathbb{R}$）。**Borel σ-代数** $\mathcal B$ = 含一切开集的最小 σ-代数。可测集全体 $\mathcal M$ 是 σ-代数，且 $\mathcal B\subset\mathcal M$。**Lebesgue 测度** $m(E)=m^*(E)$（$E$ 可测）。

**定理（可数可加性与连续性）**：两两不交可测集列满足 $m(\bigcup_n E_n)=\sum_n m(E_n)$；递增可测集列 $E_n\nearrow$ 满足 $m(\bigcup_k E_k)=\lim_n m(E_n)$。

---

## 2. 可测函数与简单函数

**可测函数**（四等价定义）：$f^{-1}((a,\infty))$ 可测对一切 $a$；或对开集/可测集的原像可测。**几乎处处 (a.e.)**：除一个零测集外成立。

**简单函数**：$\varphi=\sum_{j=1}^n a_j\chi_{A_j}$（$A_j$ 两两不交、并为 $E$）。**逐点递增逼近定理**：非负可测函数 $f$ 是某个递增简单函数列的逐点极限——这是 Lebesgue 积分从简单函数出发的定义基础。

---

## 3. Lebesgue 积分与三大收敛定理

**简单函数积分**：$\int_E\varphi=\sum_j a_j m(A_j)$。

**非负函数积分**：$\int_E f=\sup\{\int_E\varphi:\varphi\text{ 简单},\ 0\le\varphi\le f\}$（用上确界定义，避免"逼近序列的极限是否依赖序列"）。

**定理（单调收敛定理, MCT）**：$\{f_n\}\subset L^+(E)$ 满足 $0\le f_1\le f_2\le\cdots$ 且 $f_n\to f$ 逐点，则

$$\lim_{n\to\infty}\int_E f_n=\int_E f.$$

只需逐点收敛，远弱于 Riemann 所需的一致收敛。推论：$\int\sum_n f_n=\sum_n\int_E f_n$（对部分和用 MCT）。

**定理（Fatou 引理）**：非负可测函数列满足

$$\int_E\liminf_{n\to\infty}f_n\le\liminf_{n\to\infty}\int_E f_n.$$

**定理（积分零 $\iff$ 零 a.e.）**：$\int_E f=0\iff f=0$ a.e.。

**Lebesgue 可积**：可测 $f$ 可积若 $\int_E\lvert f\rvert<\infty$；此时 $\int_E f=\int_E f^+-\int_E f^-$（两项都有限，绝不出现 $\infty-\infty$）。

**定理（控制收敛定理, DCT）**：$g\ge0$ 可积，$\lvert f_n\rvert\le g$ a.e.，$f_n\to f$ a.e.，则

$$\lim_{n\to\infty}\int_E f_n=\int_E f.$$

只需逐点收敛 + 一个**可积控制函数** $g$。证明骨架：对 $g\pm f_n\ge0$ 用 Fatou 双向夹逼。

**Riemann 与 Lebesgue 一致**：连续函数 $f\in C([a,b])$ 可积且两种积分相等；闭区间上 Riemann 可积函数皆 Lebesgue 可积且积分相同。Lebesgue 是 Riemann 的严格扩张，且让可积函数空间**完备**。

---

## 4. $L^p$ 空间

**$L^p$ 范数**：$\lVert f\rVert_{L^p(E)}=\left(\int_E\lvert f\rvert^p\right)^{1/p}$（$1\le p<\infty$）；**本质上确界** $\lVert f\rVert_{L^\infty}=\inf\{M:m(\{\lvert f\rvert>M\})=0\}$。

**Hölder 不等式**（$1/p+1/q=1$）：$\int_E\lvert fg\rvert\le\lVert f\rVert_p\lVert g\rVert_q$。关键引理是 **Young 不等式** $ab\le\frac{a^p}{p}+\frac{b^q}{q}$。

**Minkowski 不等式**：$\lVert f+g\rVert_p\le\lVert f\rVert_p+\lVert g\rVert_p$。

**等价类**：$f=g$ a.e. 视为**同一元素**——因为 $\int\lvert f\rvert^p=0$ 只推出 $f=0$ a.e.，$\lVert\cdot\rVert_p$ 只是半范数；模去零测集后才是范数。

**定理（Riesz–Fischer）**：对一切 $1\le p\le\infty$，$L^p(E)$ 是 Banach 空间。证明用"绝对可和级数收敛"判定：由 Minkowski 得 $\lVert\sum\lvert f_k\rvert\rVert_p\le M$，Fatou 得级数 a.e. 绝对收敛，再用 DCT 得部分和收敛。

**稠密性**：连续函数 $C([a,b])$ 在 $L^p([a,b])$（$1\le p<\infty$）中稠密；故 $L^p$ 可视作连续函数的**完备化**。由 Weierstrass 逼近，多项式也稠密，故 $L^p([a,b])$ 可分。

---

## 5. 测度即"质量分布"：push-forward 与耦合

**Radon 测度**给每个可测集分配非负质量；**概率测度** $m(X)=1$。测度与密度的关系靠 **Radon–Nikodym 定理**：若 $\mu$ 相对参考测度有密度 $\rho$，则 $\mu(A)=\int_A\rho\,dx$。**离散测度** $\alpha=\sum_i a_i\delta_{x_i}$（$\delta_x$ 是 Dirac 质量）。离散与连续测度用**同一套框架**处理。

**前推 (push-forward)**：对可测 $T:X\to Y$ 与测度 $\mu$，$(T_\sharp\mu)(B)=\mu(T^{-1}(B))$。这是**质量守恒的换元公式**。实用形式（期望换元）：

$$\int_Y h(y)\,d(T_\sharp\mu)(y)=\int_X h(T(x))\,d\mu(x).$$

密度版换元（$T$ 可逆光滑）：$\rho_T(y)=\rho(T^{-1}(y))\lvert\det\nabla T^{-1}(y)\rvert$。

**耦合 (coupling)**：$\mu\in\mathcal{P}(X)$、$\nu\in\mathcal{P}(Y)$ 的耦合是 $X\times Y$ 上的概率测度 $\pi$，边缘分别为 $\mu,\nu$：$\pi(A\times Y)=\mu(A)$，$\pi(X\times B)=\nu(B)$。记全体为 $\Pi(\mu,\nu)$。边缘 = 投影映射的 push-forward。

- **独立耦合** $\mu\otimes\nu$；
- **确定耦合** $\pi=(\mathrm{Id},T)_\sharp\mu$（质量压在图像上）。

**离散版**：$\mu=\sum_i a_i\delta_{x_i}$，$\nu=\sum_j b_j\delta_{y_j}$ 时，耦合是非负矩阵 $P$ 满足 $P\mathbf 1=a$、$P^\top\mathbf 1=b$；这样的 $P$ 全体是**运输多面体 (transport polytope)**。

**相对熵 (KL)**：$\mathrm{KL}(\pi\mid\xi)=\int\log\frac{d\pi}{d\xi}\,d\pi+\int(d\xi-d\pi)$，是"$\pi$ 相对参考测度 $\xi$ 的距离"（非对称、非度量），在熵正则最优传输与 Schrödinger 桥中作正则项。

---

## 关键结论速查

- **外测度 = 最省覆盖总长**；**可测集 = Carathéodory 切割条件**；可数可加性只在可测集上成立。
- **三大收敛定理**：MCT（单调，可换序）、Fatou（$\int\liminf\le\liminf\int$）、DCT（有可积控制函数，可换序）——把"积分与极限交换"从一致收敛放宽到逐点收敛。
- **Riesz–Fischer**：$L^p$ 完备（Banach）；$C([a,b])$ 在 $L^p$ 稠密。
- **Hölder / Minkowski** 是 $L^p$ 结构的支柱；**Young 不等式**是 Hölder 的引理。
- **push-forward** $\int_Y h\,d(T_\sharp\mu)=\int_X h\circ T\,d\mu$ 是搬运质量的原子操作；**耦合**是边缘固定的联合测度。
