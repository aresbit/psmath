# 加性组合 (Additive Combinatorics)

> 整理自：Roth (1953)、Szemerédi (1975)、Croot–Lev–Pach、Ellenberg–Gijswijt、Freiman、Plünnecke–Ruzsa、Bogolyubov、Balog–Szemerédi–Gowers、Erdős–Szemerédi、Szemerédi–Trotter、Elekes、Solymosi 原始结果；教材框架取自 Yufei Zhao《Graph Theory and Additive Combinatorics》(MIT 18.217) 的 Roth 定理、集合加法的结构、和积问题三章（Lecture 18–26）。

## 1. Roth 定理：正密度集必有 3-AP

记 $$r_3([N])$$ 为 $$[N]$$ 中 3-AP-free 子集的最大大小。**Roth 定理**即 $$r_3([N])=o(N)$$。正则引理证明给约 $$N/\log^*N$$，Fourier 证明给 $$N/\log\log N$$。当前最好上界 $$r_3([N])\le N/(\log N)^{1-o(1)}$$（Sanders/Bloom），下界 $$r_3(N)\ge Ne^{-O(\sqrt{\log N})}$$（Behrend）。

### 1.1 有限域模型：密度增量三步

有限域是测试方法的"沙盒"。在 $$\mathbb F_3^n$$ 中 $$x,y,z$$ 成 3-AP ⟺ $$x+y+z=0$$ ⟺ 成直线。**Meshulam**：$$r_3(\mathbb F_3^n)=O(3^n/n)$$。

Fourier 记号：字符 $$\gamma_r(x)=\omega^{r\cdot x}$$（$$\omega=e^{2\pi i/3}$$），$$\hat f(r)=\mathbb E_x f(x)\omega^{-r\cdot x}$$。核心性质：$$\hat f(0)=\mathbb E f$$；Parseval $$\mathbb E_x f\bar g=\sum_r\hat f\bar{\hat g}$$；反演与卷积定理 $$(\widehat{f*g})=\hat f\hat g$$。**3-AP 恒等式**：

$$\mathbb E_{x,y}f(x)g(x+y)h(x+2y)=\sum_r\hat f(r)\hat g(-2r)\hat h(r).$$

**计数引理**：$$\lvert A\rvert=\alpha3^n$$ 时 $$\lvert\Lambda_3(A)-\alpha^3\rvert\le\alpha\max_{r\ne0}\lvert\hat 1_A(r)\rvert$$，其中 $$\Lambda_3(A)$$ 是 3-AP 密度。**三步密度增量**：
1. **无 3-AP ⇒ 有大 Fourier 系数**：若 $$A$$ 无 3-AP 且 $$N\ge2\alpha^{-2}$$，则存在 $$r\ne0$$ 使 $$\lvert\hat 1_A(r)\rvert\ge\alpha^2/2$$。
2. **大 Fourier 系数 ⇒ 超平面密度增量**：若 $$\lvert\hat 1_A(r)\rvert\ge\delta$$，则 $$A$$ 在某超平面（$$r^\perp$$ 的陪集）上密度至少 $$\alpha+\delta/2$$（关键恒等式 $$\hat 1_A(r)=\frac13(\alpha_0+\alpha_1\omega+\alpha_2\omega^2)$$）。
3. **迭代**：密度 $$\alpha_i\ge\alpha_{i-1}+\alpha_{i-1}^2/4$$，加倍 $$\alpha$$ 至多 $$O(1/\alpha)$$ 步，最终 $$\alpha=O(1/n)$$。

**Fourier 系数小只控制 3-AP，不控制 4-AP**：$$A=\{x\in\mathbb F_5^n:x\cdot x=0\}$$ 非零 Fourier 系数都小却有无正确的 4-AP 数——**高阶（二次）Fourier 分析**是 Gowers 为把 Roth 推广到 Szemerédi 定理而发展的。

### 1.2 整数上的 Roth 定理（原证）

整数群 $$\mathbb Z$$ 的对偶是 $$\mathbb R/\mathbb Z$$，Fourier 级数 $$\hat f(\theta)=\sum_x f(x)e(-x\theta)$$。三步同样，但第 2 步不同——$$[N]$$ 没有超平面，需把字符 $$x\mapsto e(x\theta)$$ "近似常数"地分块，工具是 **Dirichlet 逼近**（鸽巢）：对 $$\theta$$ 与 $$0<\delta<1$$ 存在 $$d\le1/\delta$$ 使 $$\lVert d\theta\rVert_{\mathbb R/\mathbb Z}\le\delta$$。由此得**密度增量**：无 3-AP 的 $$A\subseteq[N]$$ 存在子 AP $$P$$，$$\lvert P\rvert\ge N^{1/3}$$，$$\lvert A\cap P\rvert\ge(\alpha+\alpha^2/40)\lvert P\rvert$$。迭代后密度加倍，但每步大小缩到立方根，得 $$\alpha=O(1/\log\log N)$$。改进方向是用 **Bohr 集** $$Bohr(S,\varepsilon)=\{x:\lVert sx/N\rVert\le\varepsilon\ \forall s\in S\}$$ 代替子 AP 作"子空间"类比（Bourgain）。

### 1.3 多项式方法（Croot–Lev–Pach / Ellenberg–Gijswijt）

$$r_3(\mathbb F_3^n)=O(2.76^n)$$。对 **cap set**（3-AP-free 集）$$A$$ 有恒等式 $$\delta_0(x+y+z)=\sum_{a\in A}\delta_a(x)\delta_a(y)\delta_a(z)$$（$$x,y,z\in A$$），左边"低 slice-rank"、右边"高 slice-rank"。**slice-rank** = 形如 $$f(x_i)g(\text{其余})$$ 的函数线性组合的最小项数。对角函数 slice-rank 恰为 $$\lvert A\rvert$$；而 $$\delta_0(x+y+z)=\prod_i(1-(x_i+y_i+z_i)^2)$$ 每单项式三坐标次数和 $$\le2n/3$$，slice-rank $$\le3M$$（$$M=\sum_{a+b+c=n,b+2c\le2n/3}\frac{n!}{a!b!c!}$$）。用生成函数估 $$M\le\inf_{0<x<1}\frac{(1+x+x^2)^n}{x^{2n/3}}\le2.76^n$$，故 $$\lvert A\rvert\le3M=O(2.76^n)$$。代数方法威力大但"脆弱"——能否推广到 4-AP 或整数仍开放。

### 1.4 热门公差

**定理（Green）**：$$\lvert A\rvert=\alpha3^n$$ 时存在 $$y\ne0$$ 使 $$\lvert\{x:x,x+y,x+2y\in A\}\rvert\ge(\alpha^3-\varepsilon)3^n$$——存在"热门公差"使 3-AP 数接近随机期望。整数上同样成立；但 **5-AP 的对应命题是假的**（Bergelson–Host–Kra）。

## 2. Freiman 定理：小加倍集合必有加法结构

**和集** $$A+B=\{a+b\}$$、$$kA=A+\cdots+A$$、伸缩 $$k\cdot A=\{ka\}$$。**命题**：$$2\lvert A\rvert-1\le\lvert A+A\rvert\le\binom{\lvert A\rvert+1}2$$（下界在等差数列，上界在几何级数）。**加倍常数** $$=\lvert A+A\rvert/\lvert A\rvert$$。

**定义（广义等差数列 GAP）**：$$\{x_0+\ell_1x_1+\cdots+\ell_dx_d:0\le\ell_i<L_i\}$$；真 GAP（无非平凡重合）加倍常数至多 $$2^d$$。

**Freiman 定理**：$$A\subseteq\mathbb Z$$ 有限且 $$\lvert A+A\rvert\le K\lvert A\rvert$$ ⟹ $$A$$ 含于维数 $$\le d(K)$$、大小 $$\le f(K)\lvert A\rvert$$ 的 GAP。最优界猜想 $$d(K)=O(K),f(K)=2^{O(K)}$$；目前最好（Sanders）$$d(K)=K(\log K)^{O(1)}$$。

**完整证明链**：
- **Plünnecke–Ruzsa**：$$\lvert A+A\rvert\le K\lvert A\rvert\Rightarrow\lvert mA-nA\rvert\le K^{m+n}\lvert A\rvert$$（小加倍 ⇒ 任意迭代和差集也小）。基石是 **Ruzsa 三角不等式** $$\lvert A\rvert\lvert B-C\rvert\le\lvert A-B\rvert\lvert A-C\rvert$$（构造单射 $$(a,d)\mapsto(a-b(d),a-c(d))$$）。
- **Ruzsa 覆盖引理**：$$\lvert X+B\rvert\le K\lvert B\rvert\Rightarrow X\subset T+B-B$$（$$\lvert T\rvert\le K$$，用极大不相交球填充）。
- **建模引理**：存在 $$A'\subset A$$（$$\lvert A'\rvert\ge\lvert A\rvert/s$$）使 $$A'$$ Freiman $$s$$-同构于 $$\mathbb Z/N\mathbb Z$$ 的子集；推论给 $$N\le2K^{16}\lvert A\rvert$$、$$\lvert A'\rvert\ge\lvert A\rvert/8$$。
- **Bogolyubov 引理**：$$\lvert A\rvert=\alpha N$$ 则 $$2A-2A$$ 含 Bohr 集 $$Bohr(R,1/4)$$（$$\lvert R\rvert<1/\alpha^2$$）——Bohr 集是循环群里的"子空间"。
- **数的几何**：**Minkowski 第二定理** $$\lambda_1\cdots\lambda_d\operatorname{vol}(K)\le2^d\det(\Lambda)$$；用格证明 Bohr 集含大 GAP。
- 串起来：小加倍 $$A$$ →（建模）$$\mathbb Z/N\mathbb Z$$ 的 $$B$$ →（Bogolyubov）$$2B-2B$$ 含 Bohr 集 →（数的几何）含真 GAP →（Freiman 同构）映回 $$2A'-2A'$$ →（覆盖引理）平移覆盖整个 $$A$$。

**一般 Abel 群（Green–Ruzsa）**：$$\lvert A+A\rvert\le K\lvert A\rvert$$ ⟹ $$A$$ 含于维数 $$d(K)$$、大小 $$f(K)\lvert A\rvert$$ 的**陪集级数** $$P+H$$ 中。非 Abel 群的对应结果用超滤子（Hrushovski；Breuillard–Green–Tao），不给显式界；**Gromov 定理**：有限生成群多项式增长 ⟺ 几乎幂零。

**PFR 猜想（$$\mathbb F_2^n$$）**：$$\lvert A+A\rvert\le K\lvert A\rvert$$ ⟹ 存在仿射子空间 $$V$$（$$\lvert V\rvert\le\lvert A\rvert$$）使 $$\lvert V\cap A\rvert\ge K^{-O(1)}\lvert A\rvert$$。当前最好界是 Sanders 的拟多项式 $$e^{(\log K)^{O(1)}}$$。

**加法能量**：$$E(A,B)=\lvert\{(a_1,a_2,b_1,b_2):a_1+a_2=b_1+b_2\}\rvert=\sum_x r_{A,B}(x)^2$$（计数 Cayley 图中的 4-环）。$$\lvert A\rvert^2\le E(A)\le\lvert A\rvert^3$$。**Balog–Szemerédi–Gowers 定理**：若 $$E(A)\ge\lvert A\rvert^3/K$$，则存在 $$A'\subset A$$（$$\lvert A'\rvert\ge K^{-O(1)}\lvert A\rvert$$）有 $$\lvert A'+A'\rvert\le K^{O(1)}\lvert A'\rvert$$——大加法能量必有高结构化的小加倍子集（证明归约到图论：受限和集 + 长 3 路径引理）。

## 3. 和积问题：加法与乘法的张力

**猜想（Erdős–Szemerédi）**：对有限集 $$A\subset\mathbb R$$，

$$\max\{\lvert A+A\rvert,\lvert A\cdot A\rvert\}\ge\lvert A\rvert^{2-o(1)}.$$

取 $$A=[N]$$：$$\lvert A+A\rvert=2N-1$$ 小，但 $$\lvert A\cdot A\rvert=N^{2-o(1)}$$ 大（Erdős 乘法表问题）；取几何级数则相反。核心猜想是二者至少一个接近最大。

**交叉数不等式**：若 $$\lvert E\rvert\ge4\lvert V\rvert$$，则 $$cr(G)\ge c\lvert E\rvert^3/\lvert V\rvert^2$$。证明：平面图 Euler 给 $$cr(G)\ge\lvert E\rvert-3\lvert V\rvert$$，随机保留顶点（概率 $$p$$）取期望，$$p^4cr(G)\ge p^2\lvert E\rvert-3p\lvert V\rvert$$，取 $$p=4\lvert V\rvert/\lvert E\rvert$$。

**关联几何 / Szemerédi–Trotter**：点集 $$P$$、直线集 $$L$$，关联数

$$I(P,L)=O(\lvert P\rvert^{2/3}\lvert L\rvert^{3/2}+\lvert P\rvert+\lvert L\rvert).$$

证明：把每条直线上的点连成边得图 $$G$$（$$\lvert E\rvert\ge I/2$$），交叉数不等式给 $$cr(G)\gtrsim I^3/\lvert P\rvert^2$$，又两直线至多一个交点故 $$cr(G)\le\lvert L\rvert^2$$，合并得出。$$n$$ 点 $$n$$ 直线的推论为 $$O(n^{4/3})$$。

**Elekes 下界**：$$\lvert A+A\rvert\lvert A\cdot A\rvert\gtrsim\lvert A\rvert^{5/2}$$。取 $$P=(A+A)\times(A\cdot A)$$，$$L=\{y=a(x-a'):a,a'\in A\}$$，每条线含 $$\lvert A\rvert$$ 个点，套 Szemerédi–Trotter 即得。推论 $$\max\{\lvert A+A\rvert,\lvert A\cdot A\rvert\}\gtrsim\lvert A\rvert^{5/4}$$。

**Solymosi（乘法能量）**：$$\lvert A\cdot A\rvert\lvert A+A\rvert^2\ge\frac{\lvert A\rvert^4}{4\lceil\log_2\lvert A\rvert\rceil}$$，推论 $$\max\ge\frac{\lvert A\rvert^{4/3}}{2\lceil\log_2\lvert A\rvert\rceil^{1/3}}$$。**乘法能量** $$E_\times(A)=\sum_x\lvert\{(a,b):ab=x\}\rvert^2\ge\frac{\lvert A\rvert^4}{\lvert A\cdot A\rvert}$$。证明用 dyadic 分解：按 $$\lvert(s\cdot A)\cap A\rvert$$ 分块取最大块 $$D$$，对每个 $$s_i\in D$$ 画直线 $$\ell_i:y=s_ix$$，不同 $$j$$ 的 $$L_j+L_{j+1}$$ 落在不相交区域（斜率递增），得 $$\lvert A+A\rvert^2\ge\sum_j\lvert L_j\rvert\lvert L_{j+1}\rvert\ge\frac{E_\times(A)}{4\lceil\log_2\lvert A\rvert\rceil}$$。

完全解决（指数 $$2-o(1)$$）仍是核心开放问题，当前最好界已推进到 $$4/3$$ 之上但仍未达 $$2-o(1)$$。

## 4. 速查表

| 结果 | 陈述 |
|---|---|
| Roth | $$r_3([N])=o(N)$$（Fourier 给 $$N/\log\log N$$） |
| CLP/Ellenberg–Gijswijt | $$r_3(\mathbb F_3^n)=O(2.76^n)$$（slice-rank + 生成函数） |
| Plünnecke–Ruzsa | $$\lvert A+A\rvert\le K\lvert A\rvert\Rightarrow\lvert mA-nA\rvert\le K^{m+n}\lvert A\rvert$$ |
| Freiman | 小加倍 ⟹ 含于低维 GAP（$$d(K)=K(\log K)^{O(1)}$$） |
| Bogolyubov | $$2A-2A$$ 含 Bohr 集（余维 $$<1/\alpha^2$$） |
| BSG | 大加法能量 ⟹ 高结构小加倍子集 |
| Erdős–Szemerédi | $$\max\{\lvert A+A\rvert,\lvert A\cdot A\rvert\}\ge\lvert A\rvert^{2-o(1)}$$（开放） |
| Szemerédi–Trotter | $$I(P,L)=O(\lvert P\rvert^{2/3}\lvert L\rvert^{3/2}+\lvert P\rvert+\lvert L\rvert)$$ |

Roth 的图论证明（三角形删除引理）与 Fourier/多项式证明的分工，见 `regularity-and-graph-limits`；下界构造与双计数工具，见 `extremal-graph-theory`。
