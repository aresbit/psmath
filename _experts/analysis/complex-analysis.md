# 复分析 (Complex Analysis)

> 整理自 Lars V. Ahlfors《Complex Analysis》；Elias M. Stein & Rami Shakarchi《Complex Analysis》；MIT OCW 18.112（Functions of a Complex Variable）；NTNU TMA4175 讲义。

## 0. 一句话心智模型

复分析不是"两个实变量函数的微积分"。它的全部威力来自一个惊人的事实：

> **可导（全纯）远比实可导强。** 只要 $f$ 在开集上复可导（**全纯, holomorphic**），它就自动**无限次可导**、自动**展开成幂级数**、自动满足**柯西积分公式**（区域内任意一点的值由边界值完全决定）。这一串"自动"是实分析里想都不敢想的**刚性 (rigidity)**。

主线由四个互相等价的刻画串起：

$$\text{全纯} \iff \text{满足 Cauchy–Riemann 方程} \iff \text{柯西积分公式成立} \iff \text{局部可展成幂级数（解析）}$$

一旦满足其一，就满足全部，于是：零点孤立（除非恒为零）；有界整函数必为常数（Liouville 定理）；模在内部取不到严格极大（极大模原理）；幂级数在收敛圆盘外**必然**发散（收敛半径由最近的奇点决定）。

---

## 1. 复平面与全纯函数

**复数域** $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$，$z=x+iy$，共轭 $\bar z=x-iy$，模 $\lvert z\rvert=\sqrt{z\bar z}$。极坐标 $z=re^{i\theta}$，**Euler 公式** $e^{i\theta}=\cos\theta+i\sin\theta$，乘法 = 平面上"旋转 + 伸缩"。

**区域 (region)** = 连通开集；**单连通 (simply connected)** = 区域内任意闭曲线可连续缩成一点（没有"洞"）。单连通性在 Cauchy 定理与 Riemann 映射定理中起决定性作用。

**围道积分**定义为把 $\mathbb{C}$ 当作 $\mathbb{R}^2$ 的线积分：$\int_\gamma f(z)\,dz:=\int_a^b f(\gamma(t))\gamma'(t)\,dt$。

**ML 不等式（估计积分的基本武器）**：

$$\left\lvert\int_\gamma f(z)\,dz\right\rvert \le \left(\max_\gamma\lvert f\rvert\right)\cdot \ell(\gamma),$$

$\ell(\gamma)$ 是道路长度。几乎所有"大圆弧/小圆弧趋于零"的论证都用它。

**定义（全纯）**：若极限 $f'(z_0):=\lim_{h\to0}\frac{f(z_0+h)-f(z_0)}{h}$（$h\in\mathbb{C},\,h\ne0$）存在，称 $f$ 在 $z_0$ 复可导；开集上每点复可导则称**全纯**；在整个 $\mathbb{C}$ 上全纯的函数叫**整函数 (entire function)**。关键：$h$ 是复数，可从**任意方向**趋于 $0$——比实导数强得多。

**Cauchy–Riemann 方程**：写 $f=u+iv$，则 $f$ 复可导（在 $u,v\in C^1$ 时）$\iff$

$$u_x=v_y,\qquad u_y=-v_x,\qquad\text{且}\quad f'(z_0)=u_x+iv_x.$$

理由：实 Jacobi 矩阵要等于"复数乘法"的实形式 $\begin{pmatrix}a&-b\\b&a\end{pmatrix}$。

**两个推论**：
1. **实部虚部都是调和函数**：$u_{xx}+u_{yy}=0$，$v_{xx}+v_{yy}=0$（即 $\Delta u=0$）。这是全纯函数与 Laplace 方程的桥梁。
2. **形式导数**：$\partial_{\bar z}=\tfrac12(\partial_x+i\partial_y)$，CR 方程 $\iff \partial_{\bar z}f=0$，即"全纯 = 不依赖 $\bar z$"。

**全纯即保角**：若 $f$ 全纯且 $f'(z_0)\ne0$，则过 $z_0$ 的两条曲线夹角（大小与方向）不变——**保角 (conformal)**，且保向。反之非退化的保角保向 $C^1$ 映射必全纯。

---

## 2. 柯西积分定理与柯西积分公式

**定理（Cauchy–Goursat）**：设 $f$ 在单连通域 $D$ 上全纯，$\gamma\subset D$ 任意闭曲线，则 $\oint_\gamma f\,dz=0$。

Cauchy 最初假设 $f'$ 连续，Goursat 去掉了这一假设，只假设 $f$ 全纯。**含义**：一旦复可导，积分自动为零，不需任何关于导数连续的信息。等价的表述：$f\,dz$ 是闭微分，故积分只依赖道路的同伦类；单连通域上积分与路径无关。

**原函数**：单连通域上每个全纯函数都有全纯原函数 $F(z)=\int_{z_0}^z f\,d\zeta$，$F'=f$。多连通域上未必——典型反例 $\oint_{\lvert z\rvert=1}\frac{dz}{z}=2\pi i\ne0$，这个"$2\pi i$"精确记录了"$1/z$ 在原点有奇点"，是整个留数理论的种子。

**定理（Cauchy 积分公式）**：若 $f$ 在含闭曲线 $\gamma$ 内部全纯，$z$ 在 $\gamma$ 内，则

$$f(z)=\frac{1}{2\pi i}\oint_\gamma \frac{f(\zeta)}{\zeta-z}\,d\zeta.$$

**为什么是"奇迹"**：区域内**任意一点**的值由**边界**上的值唯一决定。全纯函数是刚性的——不能在内部随意改动而不破坏全纯性。

**导数公式**：对 $z$ 逐次求导（可交换积分与求导），$f^{(n)}(z)=\frac{n!}{2\pi i}\oint_\gamma\frac{f(\zeta)}{(\zeta-z)^{n+1}}d\zeta$。**这是复分析最大的"免费午餐"**：全纯 $\Rightarrow$ 任意阶导数存在（实分析里 $C^1$ 推不出 $C^2$）。

**Cauchy 估计与 Liouville**：若 $\lvert f\rvert\le M$ 在 $\lvert\zeta-z_0\rvert=R$ 上，则 $\lvert f^{(n)}(z_0)\rvert\le\frac{n!M}{R^n}$。取 $n=1$ 令 $R\to\infty$ 得 **Liouville 定理**：有界整函数必为常数。

**Morera 定理**（Cauchy 定理的逆）：若 $f$ 连续且沿任意闭曲线积分为零，则 $f$ 全纯。由此立刻推出：全纯函数的紧一致收敛极限仍全纯。

**代数基本定理**：反设 $P$ 无根，则 $1/P$ 是有界整函数，由 Liouville 为常数，矛盾。

**刚性推论**：极大模原理（非常数全纯函数在区域内取不到严格模极大）；零点孤立；恒等定理。

---

## 3. 幂级数与解析函数

**核心定理（全纯 = 解析）**：$f$ 全纯 $\iff$ 局部可展成幂级数，且展开是唯一的 Taylor 级数

$$f(z)=\sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!}(z-z_0)^n.$$

证明要点：把 Cauchy 公式核 $\frac{1}{\zeta-z}=\frac{1}{\zeta-z_0}\sum_{n\ge0}\left(\frac{z-z_0}{\zeta-z_0}\right)^n$ 展成几何级数再逐项积分。

**收敛半径与奇点**：$R$ 由 Hadamard 公式 $\frac1R=\limsup_n\lvert a_n\rvert^{1/n}$ 给出；在圆盘内绝对收敛、圆外发散，且收敛圆周上**必至少有一个奇点**——幂级数总被最近奇点挡住。例：$\frac{1}{1-z}=\sum z^n$ 的 $R=1$，奇点 $z=1$ 恰在圆周上。这也解释了实数 $f(x)=\frac1{1+x^2}$ 的 Taylor 级数为何 $R=1$——复平面上的奇点 $\pm i$ 在作祟。

**恒等定理**：若 $f,g$ 在连通域 $D$ 全纯，且在"有聚点的集合"上相等，则 $f\equiv g$。等价：非常数全纯函数零点无聚点。威力：全纯函数被任意一小段弧（哪怕只是有聚点的点列）完全钉死——这是解析延拓唯一性的理论基础。而实分析里 $e^{-1/x^2}$ 与零函数 Taylor 系数全同却不相等。

**基本整函数**：$e^z=\sum z^n/n!$，$\sin z=\frac{e^{iz}-e^{-iz}}{2i}$，$\cos z=\frac{e^{iz}+e^{-iz}}{2}$。注意 $\sin z,\cos z$ 在复平面**无界**（如 $\sin(it)=i\sinh t$），$\lvert e^z\rvert=e^{\operatorname{Re}z}$ 故 $e^z$ 无零点。

**Laurent 级数**：对圆环域 $r<\lvert z-z_0\rvert<R$，有双边展开 $f(z)=\sum_{n=-\infty}^{\infty}a_n(z-z_0)^n$，$a_n=\frac{1}{2\pi i}\oint\frac{f(\zeta)}{(\zeta-z_0)^{n+1}}d\zeta$。主部（负幂项）分类孤立奇点：

- **可去奇点**：主部为零（如 $\frac{\sin z}{z}$ 在 $0$）；
- **极点**：主部有限多项；$a_{-m}\ne0$ 而 $a_n=0\,(n<-m)$ 称 $m$ 阶极点；
- **本性奇点**：主部无穷多项（如 $e^{1/z}$ 在 $0$）。

**Casorati–Weierstrass 定理**：在本性奇点任意小的邻域内，函数值在 $\mathbb{C}$ 中稠密。（Picard 大定理更强：至多一个值取不到。）

---

## 4. 留数理论

**定义**：$f$ 在孤立奇点 $z_0$ 的 Laurent 系数 $a_{-1}$ 称为**留数** $\operatorname{Res}(f,z_0)$。因为 $\oint_{\lvert z-z_0\rvert=\varepsilon}f\,dz=2\pi i\,a_{-1}$（其余项积分为零）。**留数 = 积分的原子**。

**定理（留数定理）**：$f$ 在 $D$ 内除有限个孤立奇点 $a_1,\dots,a_k$ 外全纯，$\gamma$ 包围它们，则

$$\oint_\gamma f(z)\,dz=2\pi i\sum_{j=1}^k\operatorname{Res}(f,a_j).$$

**留数计算**：
- 一阶极点 $f=g/h$（$g(z_0)\ne0$，$h(z_0)=0$，$h'(z_0)\ne0$）：$\operatorname{Res}=\frac{g(z_0)}{h'(z_0)}$；
- $m$ 阶极点：$\operatorname{Res}(f,z_0)=\frac{1}{(m-1)!}\lim_{z\to z_0}\frac{d^{m-1}}{dz^{m-1}}[(z-z_0)^m f(z)]$；
- 本性奇点：读 Laurent 级数取 $a_{-1}$。

**用留数算实积分（三类套路）**：

1. $\int_0^{2\pi}R(\cos\theta,\sin\theta)\,d\theta$：令 $z=e^{i\theta}$，$d\theta=dz/(iz)$，$\cos\theta=\frac{z+z^{-1}}{2}$，$\sin\theta=\frac{z-z^{-1}}{2i}$，化为单位圆周围道积分；
2. $\int_{-\infty}^\infty\frac{P(x)}{Q(x)}dx$（$\deg Q\ge\deg P+2$）：沿"实轴 + 上半平面大半圆"围道，半圆由 ML 不等式趋于零，取上半平面极点留数 $\times2\pi i$；
3. Fourier 型 $\int_{-\infty}^\infty f(x)e^{iax}dx$：用 **Jordan 引理**控制 $\lvert e^{iaz}\rvert$；对 $a>0$ 取上半平面留数。

**多值函数绕割线**：处理 $\int_0^\infty x^{\alpha-1}f(x)\,dx$ 用"钥匙孔围道"，典型结论 $\int_0^\infty\frac{x^{\alpha-1}}{1+x}dx=\frac{\pi}{\sin(\pi\alpha)}$（$0<\alpha<1$）。

**级数求和**：$\pi\cot(\pi z)$ 在 $z=n$ 的留数为 $1/\pi$，用 $\pi\cot(\pi z)f(z)$ 绕大矩形，令矩形趋于无穷，得 $\sum_n f(n)=-\sum\text{留数}$。经典例子（Euler 解 Basel 问题）：取 $f=1/z^2$ 得

$$\sum_{n=1}^\infty\frac{1}{n^2}=\frac{\pi^2}{6}.$$

**幅角原理与 Rouché 定理**：若 $f$ 在 $\gamma$ 内亚纯，则 $\frac{1}{2\pi i}\oint_\gamma\frac{f'}{f}dz=N-P$（$N$ 零点数、$P$ 极点数，计重数）。**Rouché 定理**：若 $\lvert f\rvert>\lvert g\rvert$ 在 $\gamma$ 上，则 $f$ 与 $f+g$ 在 $\gamma$ 内有相同零点数——"小扰动不改变零点个数"，也是代数基本定理的又一证法。

---

## 5. 共形映射

**全纯 = 局部保角**；**共形映射**通常指**单射**（单叶, univalent）全纯映射，因为单射才能谈区域间的"一一保角对应"。

**Möbius 变换（分式线性变换）**：$f(z)=\frac{az+b}{cz+d}$，$ad-bc\ne0$。它把 Riemann 球 $\hat{\mathbb{C}}=\mathbb{C}\cup\{\infty\}$ 映到自身，是 $\hat{\mathbb{C}}$ 上唯一的双全纯自同构群 $\operatorname{Aut}(\hat{\mathbb{C}})$。性质：

1. **保圆**（圆与直线互映，直线视作过 $\infty$ 的圆）；
2. **保交比** $\frac{(z_1-z_3)(z_2-z_4)}{(z_1-z_4)(z_2-z_3)}$；
3. **三自由度**：给定三对点存在唯一 Möbius 变换；
4. **可分解**为平移、旋转、伸缩、反演 $z\mapsto1/z$ 的复合。

**标准例子**：**Cayley 变换** $z\mapsto\frac{z-i}{z+i}$ 把上半平面 $\mathbb{H}$ 映到单位圆盘 $\mathbb{D}$；圆盘自同构群 $\operatorname{Aut}(\mathbb{D})=\left\{e^{i\theta}\frac{z-a}{1-\bar a z}:\lvert a\rvert<1\right\}$。

**Schwarz 引理**：设 $f:\mathbb{D}\to\mathbb{D}$ 全纯且 $f(0)=0$，则 $\lvert f(z)\rvert\le\lvert z\rvert$、$\lvert f'(0)\rvert\le1$；若某点等号成立则 $f(z)=e^{i\theta}z$（纯旋转）。证明思路：$g=f/z$ 全纯，由极大模原理 $\lvert g\rvert\le1$。这是**最根本的"全纯刚性"工具**。

**初等共形映射字典**：

| 源区域 | 目标区域 | 映射 |
|--------|----------|------|
| 上半平面 $\mathbb{H}$ | 单位圆盘 $\mathbb{D}$ | $w=\frac{z-i}{z+i}$（Cayley） |
| 角域 $\{0<\arg z<\alpha\}$ | 上半平面 | $w=z^{\pi/\alpha}$ |
| 带形 $\{0<\operatorname{Im}z<\pi\}$ | 上半平面 | $w=e^z$ |
| 单位圆盘 | 自身 | $w=e^{i\theta}\frac{z-a}{1-\bar az}$ |

幂映射 $z^\alpha$ 展平角域，指数映射 $e^z$ 展开带形。

---

## 6. 黎曼映射定理

**定理（Riemann 映射定理）**：设 $D\subsetneq\mathbb{C}$ 单连通且 $D\ne\mathbb{C}$，则存在双全纯（共形）映射 $f:D\to\mathbb{D}$。

**一句话**：任何"非整个平面的单连通区域"都与单位圆盘共形等价——**拓扑性质完全决定共形类**。条件不可去：圆环 $r<\lvert z\rvert<R$（非单连通）不能共形映到圆盘；$\mathbb{C}$ 到 $\mathbb{D}$ 不存在（否则有界整函数必常数）。

**规范化后唯一**：对 $z_0\in D$、$\alpha\in\mathbb{R}$，存在唯一共形 $f:D\to\mathbb{D}$ 使 $f(z_0)=0,\ f'(z_0)>0$。唯一性用 Schwarz 引理。

**存在性证明思路（正规族法，非构造性）**：考虑所有映入圆盘的单射全纯 $f$（$f(z_0)=0$，$f'(z_0)>0$），取 $M=\sup f'(z_0)$，取极值列；由 **Montel 定理**（局部一致有界 $\Rightarrow$ 存在局部一致收敛子列）得极限 $f$；由 **Hurwitz 定理**（单射的极限单射或常数）$f$ 单射；再证满射（否则用 Schwarz 引理 + 平方根扩张构造更大导数的 $g$，矛盾）。

**Carathéodory 定理（边界行为）**：若 $\partial D$ 是 Jordan 曲线，则 Riemann 映射可连续延拓到边界，诱导边界同胚 $\partial D\to\partial\mathbb{D}$。

**应用：解 Dirichlet 问题**。把 $D$ 共形映到 $\mathbb{D}$，在圆盘上解 Dirichlet 问题（有显式 **Poisson 积分公式**），再拉回。圆盘上的解：

$$u(re^{i\theta})=\frac{1}{2\pi}\int_0^{2\pi}\frac{1-r^2}{1-2r\cos(\theta-t)+r^2}u(e^{it})\,dt,$$

核 $P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}$ 称 **Poisson 核**。Riemann 映射定理把"任意单连通域上的调和边值问题"都归约为圆盘 Poisson 积分。

**与单值化定理**：Riemann 映射定理是**单值化定理**的平面特例——任何单连通黎曼面共形等价于 $\hat{\mathbb{C}}$、$\mathbb{C}$ 或 $\mathbb{D}$ 之一。

---

## 7. 解析延拓与多值函数

**解析延拓**：$f$ 在 $D_1$ 全纯，若存在更大区域 $D\supset D_1$ 与 $D$ 上全纯 $F$ 使 $F|_{D_1}=f$，称 $F$ 为解析延拓。由恒等定理，延拓若存在则**唯一**。延拓会被**奇点**挡住（奇点是解析延拓的天然边界）。

**沿路径延拓**：用有限多个圆盘覆盖道路 $\gamma$，相邻圆盘上函数在交集一致。延拓若存在则唯一，且只依赖路径的**同伦类**。

**Monodromy 定理**：设 $D$ 单连通，函数元素 $f_0$ 能沿 $D$ 内每条从该点出发的路径延拓，则这些延拓拼出一个 $D$ 上的**单值**全纯函数。多值性只能在**非单连通**区域出现——"洞"是"绕一圈回来变值"的根源。

**多值函数与割线**：$\sqrt z$、$\log z$ 在 $\mathbb{C}\setminus\{0\}$ 上不能单值全纯，因 $\arg z$ 模 $2\pi$。办法：挖去一条从奇点到 $\infty$ 的**割线**（如负实轴），在剩余单连通域上取**主值分支**，如 $\operatorname{Log}z=\ln\lvert z\rvert+i\operatorname{Arg}z$（$\operatorname{Arg}\in(-\pi,\pi]$）。跨过割线函数值发生跳跃——第 4 章钥匙孔围道正是利用这个跳跃。

**Schwarz 反射原理**：设 $D$ 关于实轴对称，$f$ 在 $D^+$ 全纯、连续到实轴且在实轴段取**实值**，则 $f$ 可延拓到整个 $D$，且 $f(\bar z)=\overline{f(z)}$。推广：把实轴换成圆（反射 $z\mapsto1/\bar z$）。

**自然边界**：如 $\sum_{n=0}^\infty z^{n!}$ 的收敛圆 $\lvert z\rvert=1$ 是自然边界（无法越过任一点延拓）。**Hadamard 空隙定理**：若 $\sum a_n z^{\lambda_n}$ 的非零项稀疏（$\lambda_{n+1}/\lambda_n\ge q>1$），则收敛圆周是自然边界。

**黎曼面**：处理多值函数的最优雅办法是让定义域本身变成多层曲面，使 $\sqrt z$、$\log z$ 在其上单值。$\sqrt z$ 的黎曼面两叶、在原点（支点）粘合；$\log z$ 的黎曼面是无穷多叶螺旋。这是复分析通向黎曼面理论与复几何的入口。

---

## 关键结论速查

- **Cauchy–Riemann**：全纯的充要条件（$C^1$ 假设下）$u_x=v_y,\ u_y=-v_x$。
- **柯西积分公式**：$f(z)=\frac{1}{2\pi i}\oint_\gamma\frac{f(\zeta)}{\zeta-z}d\zeta$——内部值由边界值决定。
- **全纯 $\Rightarrow$ 无限次可导**（导数公式 + Cauchy 估计）。
- **Liouville**：有界整函数为常数 $\Rightarrow$ 代数基本定理。
- **留数定理**：$\oint_\gamma f\,dz=2\pi i\sum\operatorname{Res}(f,a_j)$。
- **Riemann 映射定理**：非全平面单连通域 $\cong\mathbb{D}$；拓扑决定共形类。
- **Schwarz 引理**：$\lvert f(z)\rvert\le\lvert z\rvert$（$f:\mathbb{D}\to\mathbb{D}$，$f(0)=0$），取等号为旋转。
