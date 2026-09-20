# 解析数论：zeta 函数、L 函数、素数定理与黎曼假设

> 整理自 J. R. Quine, *Lectures on Analytic Number Theory*，以 Donald J. Newman, *Analytic Number Theory* (GTM 177, Springer, 1998)、D. Zagier, *Newman's short proof of the prime number theorem* (Amer. Math. Monthly 104, 1997)、Elias M. Stein & Rami Shakarchi, *Fourier Analysis: An Introduction* 为参照。

解析数论用**分析学与复变函数论**研究**整数中最离散的对象——素数**。它把关于素数的算术信息编码成一个解析对象（Dirichlet 级数，尤其黎曼 zeta 函数与 Dirichlet L 函数），再通过研究这些函数的**极点、零点、解析延拓**反推出素数的分布规律。

## 1. 生成函数：把数列编码成解析函数

核心思想：把关心的数论序列 $\{a_n\}_{n\ge 1}$ 编码成一个解析函数（幂级数或 Dirichlet 级数），使数列的运算（加法、卷积、求逆）对应函数的运算，然后用微积分与复分析研究这个函数，最后把信息"读回"数列。两类最基本的生成函数：

- **幂级数**：$\sum_{k\ge 0}a_k z^k$，用于"加法型"组合结构（整数分拆、幂和）；
- **Dirichlet 级数**：$\sum_{n\ge 1}a_n n^{-s}$，用于"乘法型"算术结构（素数、整除关系）。

解析数论主要使用 Dirichlet 级数，因为素数与整数的乘法结构天然匹配 Dirichlet 级数的乘法卷积。

**一个微积分与数论交汇的例子**：由 $\sum_{k=1}^{n}k z^{k-1}=\frac{d}{dz}\frac{z^{n+1}-1}{z-1}=\frac{n z^{n+1}-(n+1)z^n+1}{(z-1)^2}$，令 $z\to 1$ 用洛必达法则得 $\sum_{k=1}^{n}k=\frac{n(n+1)}{2}$——用微积分导出了一个纯数论公式。

### Dirichlet 级数的形式运算

**加法**：逐项相加。**乘法（Dirichlet 卷积）**：

$$\left(\sum_{m\ge 1}a_m m^{-s}\right)\left(\sum_{n\ge 1}b_n n^{-s}\right)=\sum_{k\ge 1}c_k k^{-s}, \qquad c_k=\sum_{mn=k}a_m b_n.$$

系数 $c_k$ 是"沿双曲线 $mn=k$"的求和——这正是乘法结构的表现（幂级数乘法沿直线 $m+n=k$，Dirichlet 级数乘法沿双曲线 $mn=k$）。

**求逆**：若级数写成 $1+h(s)$，$h(s)=\sum_{n\ge 2}a_n n^{-s}$，则由几何级数 $\frac{1}{1+h(s)}=\sum_{k\ge 0}(-1)^k h(s)^k$ 形式求出逆。

**例 $1/\zeta(s)$ 与 Möbius 函数**：取 $h(s)=\sum_{n\ge 2}n^{-s}$，得

$$\frac{1}{\zeta(s)} = 1 - 2^{-s} - 3^{-s} - 5^{-s} + 6^{-s} + \cdots = \sum_{n\ge 1}\mu(n)n^{-s}, \qquad \mu(n)\in\{-1,0,1\}.$$

**例 Bernoulli 数**：对 $\frac{e^z-1}{z}=1+\frac{z}{2}+\frac{z^2}{6}+\cdots$ 求逆，记 $\frac{z}{e^z-1}=\sum_{k\ge 0}\frac{B_k}{k!}z^k$，得

$$B_0=1,\quad B_1=-\frac{1}{2},\quad B_2=\frac{1}{6},\quad B_4=-\frac{1}{30},\quad B_6=\frac{1}{42},$$

且奇数 $k\ge 3$ 时 $B_k=0$。Bernoulli 数是 Euler–Maclaurin 求和与 zeta 函数方程的核心。

## 2. 黎曼 zeta 函数与 Euler 乘积

对实数 $s>1$，**黎曼 zeta 函数**定义为 $\zeta(s)=\sum_{n=1}^{\infty}n^{-s}$。

**定理（Euler 乘积）**：对每个 $s>1$，

$$\zeta(s)=\prod_{p}(1-p^{-s})^{-1},$$

乘积取遍所有素数。**证明思想**：由算术基本定理每个 $n$ 唯一写成 $n=\prod_p p^{\alpha_p}$，故 $\prod_{p\le N}(1-p^{-s})^{-1}$ 展开后恰含所有"仅由 $\le N$ 的素数构成"的整数 $n^{-s}$，令 $N\to\infty$ 即可。

**素数无限性的解析证明**：取对数 $\log\zeta(s)=-\sum_p\log(1-p^{-s})=\sum_p p^{-s}+O(1)$（误差项由 $\sum_{n\ge 2}n^{-2}<\infty$ 控制）。令 $s\to 1^{+}$，因 $\zeta(s)\to\infty$，得

$$\sum_{p}\frac{1}{p}=\infty,$$

即素数的倒数和发散——由此素数无限。**这条证明虽不是最简单，但能推广到任意算术级数。**

**无穷多个 $4k+1$ 型素数**：定义模 4 的 Dirichlet 特征 $\chi(n)$（$n$ 偶取 0，$n\equiv 1\pmod 4$ 取 1，$n\equiv 3\pmod 4$ 取 $-1$），$L(s,\chi)=1-\frac{1}{3^s}+\frac{1}{5^s}-\frac{1}{7^s}+\cdots$。因交错，$L(1,\chi)$ 有限（事实上 $=\pi/4$）；由 Euler 乘积取对数得 $\log L(s,\chi)=\sum_p\chi(p)p^{-s}+O(1)$，$s\to 1^{+}$ 时有界。结合 $\sum_p p^{-s}=2^{-s}+2\sum_{p\equiv 1}p^{-s}+O(1)$ 得 $\sum_{p\equiv 1}1/p=\infty$。这完整展示了 Dirichlet 定理的套路：L 函数在 $s=1$ 处有限且非零，加特征正交性，就能分离出每个剩余类。

## 3. Dirichlet 特征与 L 函数

**Dirichlet 定理**：若 $q,\ell$ 互素，则存在无穷多个形如 $\ell+kq$ 的素数。

**定义（Dirichlet 特征）**：模 $q$ 的特征是映射 $\chi:\mathbb{Z}(q)^{\ast}\to S^1\subset\mathbb{C}$，满足 $\chi(mn)=\chi(m)\chi(n)$——单位群到单位圆周的群同态。延拓：与 $q$ 互素的 $n$ 用其剩余类定义，$\gcd(n,q)>1$ 时约定 $\chi(n)=0$。**平凡特征** $\chi_0$ 对所有与 $q$ 互素的 $n$ 取 1。

**构造例（$q=5$）**：$\mathbb{Z}(5)^{\ast}=\{1,2,3,4\}\cong\mathbb{Z}(4)$（由 2 生成）。取四次单位根 $z\in\{1,i,-1,-i\}$，定义 $\chi(2^j)=z^j$，得 4 个特征，其矩阵 $A$ 满足 $\frac{1}{2}A$ 酉。

**构造例（$q=8$）**：$\mathbb{Z}(8)^{\ast}=\{1,3,5,7\}$ 非循环（$\cong\mathbb{Z}(2)\oplus\mathbb{Z}(2)$），$7=3\cdot 5$。取 $z_1,z_2\in\{\pm 1\}$，$\chi(3^j5^k)=z_1^jz_2^k$，得 4 个特征。

**一般构造**依赖有限交换群分解为循环群直积：存在 $a_1,\dots,a_k$（阶 $N_1,\dots,N_k$，$N_1\cdots N_k=\phi(q)$）使每个单位唯一写成 $a_1^{j_1}\cdots a_k^{j_k}$。令 $\omega_l=e^{2\pi i/N_l}$，则 $\chi(a_1^{j_1}\cdots a_k^{j_k})=\omega_1^{n_1j_1}\cdots\omega_k^{n_kj_k}$，共得 $\phi(q)$ 个特征。

**定理（存在性与正交性）**：$\mathbb{Z}(q)^{\ast}$ 恰有 $\phi(q)$ 个特征，特征集在乘法下成群且与 $\mathbb{Z}(q)^{\ast}$ 同构；写成矩阵 $A$ 时 $AA^{\ast}=\phi(q)I$。**行正交**：$\sum_{n\in\mathbb{Z}(q)^{\ast}}\chi_1(n)\overline{\chi_2(n)}=\phi(q)\delta_{\chi_1,\chi_2}$；**列正交**：$\sum_{\chi}\chi(\ell)\overline{\chi(n)}=\phi(q)\delta_{\ell,n}$。

**L 函数的 Euler 乘积**：对模 $q$ 的每个特征，$L(s,\chi)=\sum_{n\ge 1}\chi(n)n^{-s}$（$s>1$），且有

$$L(s,\chi)=\prod_{p}(1-\chi(p)p^{-s})^{-1}, \qquad \log L(s,\chi)=\sum_p\chi(p)p^{-s}+O(1).$$

### Dirichlet 定理的证明纲领

用特征正交性"筛选"出 $p\equiv\ell\pmod q$ 的素数。由列正交，$\phi(q)\delta_\ell(m)=\sum_\chi\chi(\ell)\overline{\chi(m)}$。拆出 $\chi_0$，两边乘 $m^{-s}$ 并对素数 $m=p$ 求和：

$$\phi(q)\sum_{p\equiv\ell}p^{-s}=\sum_{p\nmid q}p^{-s}+\sum_{\chi\ne\chi_0}\chi(\ell)\sum_p\overline{\chi(p)}p^{-s}.$$

因 $\sum_{p\nmid q}p^{-s}\to\infty$，只要对每个非平凡特征证明 $\sum_p\chi(p)p^{-s}$ 在 $s\to 1^{+}$ 有界，就得到 $\sum_{p\equiv\ell}1/p=\infty$。由 $\sum_p\chi(p)p^{-s}=\log L(s,\chi)+O(1)$，关键归结为：

$$L(1,\chi)\ \text{有限且非零，对每个非平凡特征}\ \chi.$$

故完整链条是：**特征正交性 + $L(1,\chi)\ne 0$ $\Longrightarrow$ Dirichlet 定理。**

## 4. L 函数的解析性质与 $L(1,\chi)\ne 0$

**定理**：非平凡特征的 $L(s,\chi)$ 在 $\operatorname{Re}s>0$ 全纯。证明用分部求和：记 $A(x)=\sum_{1\le k\le x}\chi(k)$，非平凡特征与平凡特征正交给出 $\sum_{n<k\le n+q}\chi(k)=0$，故 $A$ 周期 $q$ 且有界 $\lvert A(x)\rvert\le q$。分部求和 $\sum_{n=1}^{N}\chi(n)n^{-s}=A(N)N^{-s}+s\int_1^N x^{-s-1}A(x)\,dx$ 一致收敛，得 $L(s,\chi)=s\int_1^\infty x^{-s-1}A(x)\,dx$。

**平凡特征**：$L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s})^{-1}$，故其极点性质完全由 $\zeta$ 决定。**$\zeta$ 的延拓**：分部求和得

$$\zeta(s)=\frac{1}{s-1}+1+s\int_1^\infty x^{-s-1}([x]-x)\,dx,$$

右端在 $\operatorname{Re}s>0$ 亚纯，仅有 $s=1$ 的简单极点（留数 1）。故 $L(s,\chi_0)$ 在 $s=1$ 有简单极点。

**复特征**：构造 $\mathcal{L}(s)=\prod_\chi L(s,\chi)$。由正交性 $\sum_\chi\chi(p^k)=\phi(q)$ 当 $p^k\equiv 1\pmod q$，否则 0，故对实 $s$ 有 $\log\mathcal{L}(s)\ge 0$，即 $\mathcal{L}(s)\ge 1$。若复特征 $\chi$ 有 $L(1,\chi)=0$，则其共轭 $\overline\chi$ 也是复特征且 $L(1,\overline\chi)=0$，乘积中一个因子有极点、两个因子有零点，故 $\mathcal{L}(1)=0$，与 $\mathcal{L}(s)\ge 1$ 矛盾。**故复特征 $L(1,\chi)\ne 0$。**

**实特征**：构造双曲和 $S_N=\sum_{k\le N}\sum_{mn=k}\frac{\chi(n)}{(nm)^{1/2}}$。下界 $S_N\ge c\log N$（因 $\sum_{n\mid k}\chi(n)$ 在 $k$ 非平方时 $\ge 0$ 且对平方数 $\ge 1$），渐近 $S_N=2N^{1/2}L(1,\chi)+O(1)$。若 $L(1,\chi)=0$ 则 $S_N$ 有界，矛盾。**故实特征也有 $L(1,\chi)\ne 0$。**

综合：对每个非平凡特征 $L(1,\chi)\ne 0$ 且有限，Dirichlet 定理得证。

## 5. 素数计数函数与 Möbius/von Mangoldt

$$\pi(x)=\#\{p\le x\}, \qquad \vartheta(x)=\sum_{p\le x}\log p, \qquad \psi(x)=\sum_{n\le x}\Lambda(n),$$

其中 **von Mangoldt 函数** $\Lambda(n)=\log p$ 若 $n=p^k$，否则 0，由 $-{\zeta'}/{\zeta}=\sum_n\Lambda(n)n^{-s}$ 引入。**Möbius 函数** $\mu(n)$：$\mu(1)=1$，$n=p_1\cdots p_k$（$k$ 个不同素数之积）时 $\mu(n)=(-1)^k$，含平方因子时为 0；$1/\zeta(s)=\sum_n\mu(n)n^{-s}$。**Mertens 函数** $M(x)=\sum_{n\le x}\mu(n)$。

**命题**：$\pi(x)\sim\frac{x}{\log x}\iff\vartheta(x)\sim x\iff\psi(x)\sim x$。证明：对 $\varepsilon>0$ 有 $(1-\varepsilon)\pi(x)\log x+O(x^{1-\varepsilon})\log x\le\vartheta(x)\le\pi(x)\log x$；且 $\psi(x)-\vartheta(x)=\sum_{p^k\le x,k\ge 2}\log p\le\sqrt x\log x=o(x)$。故 PNT 可简化为证 $\psi(x)\sim x$ 或 $\vartheta(x)\sim x$。

**关键恒等式**：由 $-\zeta'=\zeta\cdot(-\zeta'/\zeta)$ 比较系数得 $\log n=\sum_{d\mid n}\Lambda(d)$；由 $-{\zeta'}/{\zeta}=\zeta^{-1}\cdot(-\zeta')$ 得 $\Lambda(k)=\sum_{mn=k}\mu(m)\log n$。这是 **Möbius 反演**的原型。

**对数导数把零点变成极点**：$-{\zeta'}/{\zeta}$ 的极点是 $\zeta$ 的零点（留数=零点阶数），这把素数分布与零点分布直接挂钩。

## 6. 素数定理的证明：$\zeta$ 无零点与 Newman 解析定理

**路线**：证 $\zeta(s)$ 在直线 $\operatorname{Re}s=1$ 上无零点 $\to$ 证 PNT 等价于该无零点事实（通过 Mellin 变换的解析延拓）$\to$ 用 Newman 解析定理把"边界解析"转回"$\vartheta(x)\sim x$"。

**命题（$\zeta$ 在 $\operatorname{Re}s=1$ 无零点）**：对正实数 $p$ 与实数 $\alpha$，$0\le(p^{i\alpha/2}+p^{-i\alpha/2})^4=p^{-2i\alpha}+4p^{-i\alpha}+6+4p^{i\alpha}+p^{2i\alpha}$。乘 $p^{-\sigma}\log p$ 并对所有素数求和，得

$$0\le\Phi(\sigma+2i\alpha)+4\Phi(\sigma+i\alpha)+6\Phi(\sigma)+4\Phi(\sigma-i\alpha)+\Phi(\sigma-2i\alpha),$$

其中 $\Phi(s)=\sum_p(\log p)p^{-s}$。反设 $\zeta$ 在 $1+i\alpha$ 有 $\mu$ 阶零点、$1+2i\alpha$ 有 $\nu$ 阶零点，乘 $(\sigma-1)$ 令 $\sigma\to 1$ 得 $0\le-2\nu-8\mu+6$，因 $\mu\ge 0$ 整数只有 $\mu=0$。故 $\zeta$ 在 $\operatorname{Re}s=1$ 无零点。核心恒等式是 $3+4\cos\theta+\cos 2\theta=2(1+\cos\theta)^2\ge 0$。

**Newman 解析定理（Tauberian 定理，形式 II）**：设 $f(x)$ 在 $[1,\infty)$ 上有界、局部可积，且 $g(s)=\int_1^\infty f(x)x^{-s}\,dx$（$\operatorname{Re}s>1$）可解析延拓到 $\operatorname{Re}s\ge 1$。则 $\int_1^\infty f(x)x^{-1}\,dx$ 存在且等于 $g(1)$。

**证明思想**：用 Cauchy 积分定理，取区域 $\{\lvert z\rvert\le R,\ \operatorname{Re}z\ge-\delta\}$ 的边界，核 $e^{zT}(1+z^2/R^2)/z$ 在右半平面按 $e^{-\operatorname{Re}z T}$ 衰减抵消尾项，在左半平面按 $e^{\operatorname{Re}z T}$ 收缩使消失。得 $\limsup_{T\to\infty}\lvert g(0)-g_T(0)\rvert\le 2B/R$，令 $R\to\infty$ 得证。

**PNT 的完成**：取 $f(x)=\vartheta(x)/x-1$，其 Mellin 变换 $=-{\zeta'}/{(s\zeta)}-\frac{1}{s-1}+h(s)$（$h$ 在 $\operatorname{Re}s>1/2$ 全纯）。因 $\zeta$ 在 $\operatorname{Re}s=1$ 无零点，右端在 $\operatorname{Re}s\ge 1$ 解析；又由 Chebyshev 估计 $\vartheta(x)=O(x)$，$f$ 有界。Newman 定理给出 $\int_1^\infty(\vartheta(x)/x-1)\frac{dx}{x}$ 收敛。最后由 $\vartheta$ 单调递增，该积分收敛蕴含 $\vartheta(x)/x\to 1$，即 **PNT 成立**。

**反例**（说明条件不可放松）：取 $f(t)=e^{i\alpha t}$（$\alpha\ne 0$），$g(z)=1/(z-i\alpha)$ 在 $0$ 解析，但 $\int_0^\infty e^{i\alpha t}\,dt$ 不收敛。故"边界上解析"（等价于无零点）是本质条件。

## 7. 算术级数中的素数分布

**算术级数 PNT**：对每个与 $q$ 互素的 $\ell$，

$$\pi_\ell(x)=\sum_{\substack{p\le x\\ p\equiv\ell}}1 \sim \frac{1}{\phi(q)}\frac{x}{\log x},$$

即素数在 $\phi(q)$ 个互素剩余类之间**均匀分布**。

**证明**：用特征正交性把 $\equiv\ell$ 的约束线性化：$\phi(q)\Phi_\ell(s)=\sum_\chi\chi(\ell)\sum_p\overline{\chi(p)}\frac{\log p}{p^s}=-{\zeta'}/{\zeta}-\sum_{\chi\ne\chi_0}\frac{L'(s,\chi)}{L(s,\chi)}+h_1(s)$，$h_1$ 在 $\operatorname{Re}s>1/2$ 全纯。因非平凡特征的 $L(s,\chi)$ 在 $s=1$ 非零，$\phi(q)\Phi_\ell(s)$ 在 $s=1$ 有简单极点、留数 1（完全来自 $\zeta$ 项）。

**定理（L 函数在 $\operatorname{Re}s=1$ 无零点）**：与 $\zeta$ 情形完全平行，用同一三角不等式 $3+4\cos\theta+\cos 2\theta\ge 0$ 排除所有特征所有 L 函数的边界零点。由此 $\int_1^\infty(\vartheta_\ell(x)/x-\frac{1}{\phi(q)})\frac{dx}{x}$ 收敛，再由 $\vartheta_\ell$ 单调得 $\pi_\ell(x)\sim\frac{1}{\phi(q)}\frac{x}{\log x}$。

## 8. 黎曼假设与误差项

**黎曼假设（RH）**：$\zeta(s)$ 在 $\operatorname{Re}s>1/2$ 上没有零点，即所有非平凡零点都落在临界线 $\operatorname{Re}s=1/2$ 上（平凡零点在负偶数 $s=-2,-4,\dots$）。RH 至今未证。

**PNT 的等价形式**：$\text{PNT}\iff M(x)/x\to 0\iff\sum_{n\ge 1}\mu(n)/n=0\iff M_1(x)/x\to 0$（$M_1$ 为 Liouville 函数 $\lambda(n)$ 的部分和，$\zeta(2s)/\zeta(s)=\sum\lambda(n)n^{-s}$）。

**RH 的等价形式**：对所有 $\varepsilon>0$，$\lvert M(x)\rvert/x^{1/2+\varepsilon}\to 0$ 当且仅当 RH（$M_1$ 亦然）。充分性易证：若该界成立，则 $\int_1^\infty M(x)x^{-s-1}dx$ 在 $\operatorname{Re}s>1/2+\varepsilon$ 绝对收敛，故 $1/\zeta(s)$ 在那里解析，$\zeta$ 无零点。反方向更难。

**RH 的"随机性"解释**：把 $\lambda(n)$ 想象成随机 $\pm 1$ 序列，长度 $N$ 的随机序列其和 $S$ 服从二项分布，方差 $N$，由中心极限定理缩放后趋于标准高斯，故 $P(\lvert S\rvert\le N^{1/2+\varepsilon})\to 1$——几乎所有随机 $\pm 1$ 序列都满足 RH 型界。这从概率直觉说明 RH "几乎必然"成立，但严格的数学证明仍缺失。

**RH 对误差项的含义**：PNT 已知 $\psi(x)=x+O(xe^{-c\sqrt{\log x}})$（误差来自零点与 $s=1$ 的距离，零自由区域）；若 RH 成立，则

$$\psi(x)=x+O(x^{1/2}\log^2 x),$$

误差降至 $O(\sqrt x)$ 量级——与"素数分布像随机模型"的预测一致。**RH 的本质：素数的"噪声"是最小的平方根噪声。**

## 9. 函数方程与解析延拓：Bernoulli 数与 Euler–Maclaurin

**Euler–Maclaurin 求和公式**（对光滑 $f$，整数 $M<N$）：

$$\sum_{n=M}^{N}f(n)-\int_M^N f(x)\,dx=\frac{1}{2}(f(M)+f(N))+\sum_{k=2}^{K}\frac{(-1)^kB_k}{k!}\left(f^{(k-1)}(N)-f^{(k-1)}(M)\right)+R_K,$$

余项 $R_K=\frac{(-1)^{K+1}}{K!}\int_M^N f^{(K)}(x)B_K(x-[x])\,dx$。其中 $B_k$ 是 Bernoulli 数（$\frac{t}{e^t-1}=\sum_{k\ge 0}\frac{B_k}{k!}t^{k-1}$，$B_0=1,B_1=-1/2,B_2=1/6,B_4=-1/30$，奇数 $k\ge 3$ 时 $B_k=0$）。

**用 Euler–Maclaurin 延拓 $\zeta$**：对 $f(x)=x^{-s}$、$M=1$，当 $\operatorname{Re}s>-K+1$ 时余项收敛，令 $N\to\infty$ 给出 $\zeta(s)$ 到整个复平面（除 $s=1$）的亚纯延拓：$\zeta$ 在 $s=1$ 有唯一简单极点（留数 1），其余全纯。

**函数方程**：引入完备 zeta 函数 $\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$，则 $\Lambda(s)=\Lambda(1-s)$。非对称形式

$$\zeta(s)=2^s\pi^{s-1}\sin\left(\frac{\pi s}{2}\right)\Gamma(1-s)\,\zeta(1-s).$$

由 $\sin(\pi s/2)$ 因子，$s=-2,-4,-6,\dots$ 时 $\zeta(s)=0$，这些是**平凡零点**；$\zeta(0)=-1/2$；由函数方程可算出 $\zeta(2)=\pi^2/6,\ \zeta(4)=\pi^4/90$。非平凡零点落在临界带 $0\le\operatorname{Re}s\le 1$ 内，RH 断言它们全在 $\operatorname{Re}s=1/2$。

## 10. 心智模型

1. **Dirichlet 级数是"乘法算术"的自然编码**：级数乘法沿双曲线 $mn=k$，对应整数的因子分解结构。
2. **Euler 乘积 = 算术基本定理的解析形式**：$\zeta(s)=\prod_p(1-p^{-s})^{-1}$ 让每个素数成为独立因子。
3. **Dirichlet 特征 = 模 $q$ 单位群的频谱**，正交关系 = 傅里叶反演，把"落在某一剩余类"的素数筛选出来。
4. **$\pi,\vartheta,\psi$ 是同一事实的多种加权**，渐近等价；选择哪个全看哪个更好处理。
5. **无零点 = 边界解析 = 可取极限**：$\zeta$ 在 $\operatorname{Re}s=1$ 无零点 $\iff$ Mellin 变换可延拓到边界 $\iff$ Newman 定理允许取极限 $\iff\vartheta(x)\sim x$。
6. **极点 = 主项来源**：$\zeta$ 在 $s=1$ 的简单极点（留数 1）给出 PNT 主项 $x$。
7. **PNT 是 RH 的零阶版本**：PNT 只需排除 $\operatorname{Re}s=1$ 上的零点，RH 要求把所有零点压到 $\operatorname{Re}s=1/2$；两者的差别就是误差项从 $O(xe^{-c\sqrt{\log x}})$ 缩到 $O(\sqrt x)$。
