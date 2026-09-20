# 几何分析 (Geometric Analysis)：调和函数、比较几何与曲率流

> 整理自 Peter Li《Geometric Analysis》(Cambridge Studies in Advanced Mathematics 134)；Richard Schoen & Shing-Tung Yau《Lectures on Differential Geometry》；Peter Topping《Lectures on the Ricci Flow》(LMS Lecture Note Series 325)；John M. Lee & Thomas H. Parker《The Yamabe Problem》(Bull. AMS 17, 1987)；Otis Chodosh《The Bernstein Problem》讲义；R. Hamilton, J. Differential Geom. 17 (1982)；G. Perelman, arXiv:math/0211159, math/0303109。

## 0. 一句话定位

几何分析研究**曲率如何约束流形上的分析量（调和函数、热核、体积、谱），以及如何用 PDE 的演化去改造度量（Ricci 流、Yamabe 问题、极小曲面）**。灵魂是**"比较"**：把未知流形上的量与常曲率模型空间（$\mathbb{R}^n,\mathbb{S}^n,\mathbb{H}^n$）上的对应量做比较，把几何条件（如 $\operatorname{Ric}\ge0$）翻译成分析结论（体积增长、Harnack 常数、特征值下界）。

**核心心智模型**：

1. **曲率 ⇒ 分析**：$\operatorname{Ric}\ge0$ 是几乎所有正结论的充分条件，经 **Bochner 公式**进入调和函数/热核估计，经 **Bishop–Gromov** 进入体积与测地球，经 Laplacian 比较进入距离函数。
2. **比较几何**：与模型空间做 Jacobi 场比较，得体积、Laplacian、特征值的单调性与上下界。
3. **演化 / 变分**：Ricci 流 $\partial_tg=-2\operatorname{Ric}$、Yamabe 问题（标量曲率共形规范化）、极小曲面（面积泛函临界点）共享"用椭圆/抛物 PDE 驱动几何"的范式。
4. **临界性与尺度不变性**：Yamabe 的临界 Sobolev 指数 $\frac{n+2}{n-2}$、Ricci 流的熵，都是尺度不变的临界现象——困难（集中紧性、气泡）的根源。
5. **梯度估计 / 最大值原理**：Yau 梯度估计、Li–Yau 抛物 Harnack、Hamilton 张量最大值原理。

---

## 1. 调和函数

**Laplace–Beltrami 算子**：$\Delta f=\operatorname{div}(\nabla f)=g^{ij}\nabla_i\nabla_j f$，自伴负定：$\int_M f\Delta h=-\int_M\langle\nabla f,\nabla h\rangle$。约定 $\Delta f\le0$ 次调和、$\Delta f\ge0$ 超调和。

**定义（调和函数）**：$\Delta f=0$。它是 Dirichlet 能量泛函 $E(f)=\int_M\lvert\nabla f\rvert^2d\mu$ 的临界点。

**均值性质**：$u$ 在测地球 $B(p,r)$ 调和 $\Rightarrow$ $u(p)=\frac{1}{\operatorname{vol}(\partial B(p,r))}\int_{\partial B}u\,d\sigma=\frac{1}{\operatorname{vol}(B)}\int_Bu\,d\mu$（一般流形上只有渐近形式；无穷小版本 $\Delta u(p)=0$ 恰是球面积分二阶展开为零）。

**强极大值原理**：连通开集上调和函数在内点取到极大/极小则必为常数。**Hopf 边界引理**：边界严格极大处外法向导数严格为正。

**Liouville 定理（$\mathbb{R}^n$）**：有界调和函数必为常数（由 Harnack 或均值性质推出）。

**Yau 梯度估计（1975）**：$M$ 完备、$\operatorname{Ric}\ge0$、$u$ 正调和，则 $\lvert\nabla\log u\rvert\le\sqrt{\frac{2(n-1)}{r}}$ 在 $B(p,r)$ 内。令 $r\to\infty$ 得 $\lvert\nabla\log u\rvert\le0$，即 **Yau 定理**：$\operatorname{Ric}\ge0$ 的完备流形上**正调和函数必为常数**（Liouville 性质成立）。证明核心是 Bochner 公式 + 截断函数梯度估计。

**多项式增长调和函数有限维**（Cheng–Yau, Li–Tam）：$\operatorname{Ric}\ge0$ 时，$\mathcal H_d(M)=\{u\text{ 调和}:\lvert u(x)\rvert\le C(1+d(p,x))^d\}$ 满足 $\dim\mathcal H_d(M)\le C_n d^{n-1}<\infty$。**线性增长调和函数**对应流的**末端 (ends)** 个数。

**Green 函数**：$\Delta_yG(x,y)=-\delta_x(y)$，Laplace 算子基本解。正 Green 函数存在等价于流形**非抛物**；抛物性 $\iff$ 布朗运动递归。$\operatorname{Ric}\ge0$ 时，体积增长 $\le Cr^2$ 则抛物、$\ge cr^{2+\epsilon}$ 则非抛物（Varopoulos）。

---

## 2. Harnack 不等式

**经典 Harnack 不等式**：$u\ge0$ 在 $B(p,R)$ 调和，则对 $0<r<R$ 存在 $C(n,r,R)$ 使 $\sup_{B(p,r)}u\le C\inf_{B(p,r)}u$。含义：非负调和函数在连通区域内部不能剧烈变化。它是 Liouville 定理的直接来源（令区域无限增大，上下确界比趋于 1）。

**从梯度估计到 Harnack**：$\operatorname{Ric}\ge0$ 时 $\lvert\nabla\log u\rvert\le C/r$，沿测地线积分得 $u(x_2)/u(x_1)\le e^{Cd(x_1,x_2)/r}$。**Cheng–Yau 梯度估计**允许 $\operatorname{Ric}\ge-(n-1)K$（$K\ge0$）：$\lvert\nabla\log u\rvert\le C(1/r+\sqrt K)$。**Harnack 常数与曲率等价**（Li–Wang）：常数增长达到欧氏最优增长率 $\Rightarrow$ $\operatorname{Ric}\ge0$（"分析量 ⇔ 几何量"的双向对应）。

**Moser 迭代（De Giorgi–Nash–Moser）**：纯 PDE 方法建立正次调和的均方估计 $\sup_{B_{r/2}}u\le C(\frac{1}{\operatorname{vol}B_r}\int_{B_r}u^p)^{1/p}$。**解的 Hölder 连续性、Harnack 不等式只依赖方程椭圆性，与系数光滑性解耦**。

**Li–Yau 抛物 Harnack（1986）**：$M$ 完备、$\operatorname{Ric}\ge0$、$u$ 正热方程解，则对 $\alpha>1$，$\frac{\lvert\nabla u\rvert^2}{u^2}-\alpha\frac{u_t}{u}\le\frac{n\alpha^2}{2t}$。取 $\alpha=\frac32$ 沿时空测地线积分得抛物 Harnack：$u(x_1,t_1)\le u(x_2,t_2)(t_2/t_1)^{n/2}\exp\frac{d^2}{4(t_2-t_1)}$。

**推论（Gaussian 热核上下界）**：$\operatorname{Ric}\ge0$ 时 $\frac{c_1}{\operatorname{vol}B(x,\sqrt t)}e^{-C_1d^2/t}\le H(x,y,t)\le\frac{C_2}{\operatorname{vol}B(x,\sqrt t)}e^{-C_2d^2/t}$。

**Grigor'yan–Saloff-Coste**：热核 Gaussian 上下界、抛物 Harnack、体积倍增 + Poincaré 不等式，三者等价。这使 Harnack 成为**度量测度空间**（不必光滑）上"曲率非负"的替代定义（RCD 理论的入口）。

---

## 3. Ricci 曲率与比较定理

**Ricci 曲率**：黎曼曲率张量缩并 $\operatorname{Ric}(X,Y)=\sum_i\langle R(X,e_i)e_i,Y\rangle$（曲率的"迹"，即包含 $v$ 的所有二维平面截面曲率之和）。几何含义：$\operatorname{Ric}$ 控制沿测地线的**体积元畸变**——$\operatorname{Ric}\ge0$ 意味体积元沿测地线不增。

**Jacobi 场与 Rauch 比较**：Jacobi 场满足 $J''+R(J,\gamma')\gamma'=0$；模型空间解是 $\sin,\sinh$。**Rauch 比较定理**：截面曲率 $K\le\bar K$ 时（共轭点之前）流形上 Jacobi 场长度不小于模型空间——"曲率越大、测地线越早汇聚、体积越小"。

**Hessian / Laplacian 比较**：$\operatorname{Ric}\ge-(n-1)K$（$K\ge0$）时 $\nabla^2r\le\frac1r\coth(\sqrt Kr)(g-dr\otimes dr)$，取迹得 $\Delta r\le\frac{n-1}{r}\coth(\sqrt Kr)$（$K=0$ 时为 $\frac{n-1}{r}$）。$\operatorname{Ric}$ 下界给距离函数 Hessian/Laplacian 的**上界**。

**Bishop–Gromov 体积比较**：$M$ 完备、$\operatorname{Ric}\ge(n-1)K$，则 $r\mapsto\frac{\operatorname{vol}B(p,r)}{V_K(r)}$ 单调不增（$V_K$ 是模型空间球体积）。推论：$\operatorname{vol}B(p,r)\le V_K(r)$；$\operatorname{Ric}\ge0$ 时 $\frac{\operatorname{vol}B(p,r)}{r^n}$ 单调不增，**渐近体积比** $\nu=\lim_{r\to\infty}\frac{\operatorname{vol}B(p,r)}{\omega_nr^n}\le1$，$\nu=1$ 当且仅当 $M\cong\mathbb{R}^n$（Bishop 刚性）。Bishop–Gromov 是几何分析最常用的"积分化"工具：把点态曲率条件打包成整体单调、可直接代入 Sobolev 不等式的体积函数。

**Bochner 公式（发动机）**：

$$\frac12\Delta\lvert\nabla u\rvert^2=\lvert\nabla^2u\rvert^2+\langle\nabla u,\nabla\Delta u\rangle+\operatorname{Ric}(\nabla u,\nabla u).$$

对调和 $u$：$\frac12\Delta\lvert\nabla u\rvert^2=\lvert\nabla^2u\rvert^2+\operatorname{Ric}(\nabla u,\nabla u)$。$\operatorname{Ric}\ge0$ 时 $\lvert\nabla u\rvert^2$ 次调和——这是 Yau 梯度估计、Liouville、分裂定理的共同起点。**(Hodge Laplacian) − (粗 Laplacian) = Ricci**。

**Myers 定理**：完备、$\operatorname{Ric}\ge(n-1)K>0$ $\Rightarrow$ $M$ 紧致且 $\operatorname{diam}(M)\le\pi/\sqrt K$；故基本群有限。Cheng：最大直径达到当且仅当等距于常曲率球面。

**Cheeger–Gromoll 分裂定理**：$M$ 完备、$\operatorname{Ric}\ge0$，若含一条**直线 (line)**（处处极小测地线），则 $M\cong N\times\mathbb{R}$（等距分裂），$N$ 仍 $\operatorname{Ric}\ge0$。证明关键：Busemann 函数 $b^\pm(x)=\lim_{t\to\pm\infty}(t-d(x,\gamma(t)))$，用 Bochner + 最大值原理证其调和且 $\lvert\nabla b^\pm\rvert\equiv1$。**推论（Cheeger–Gromoll 结构）**：$\operatorname{Ric}\ge0$ 完备流形等距于 $N\times\mathbb{R}^k$。

---

## 4. Ricci 流

**方程**：$\partial_tg(t)=-2\operatorname{Ric}(g(t))$——度量的**非线性热方程**（调和坐标下 $\approx-\frac12\Delta g_{ij}$ + 低阶项），把正曲率"熨平"、负曲率"拉伸"。**规范化**：$\partial_tg=-2\operatorname{Ric}+\frac2n\bar Rg$（保体积）。**短时存在性**（Hamilton）：紧流形上光滑初值存在唯一解于 $[0,T)$（DeTurck 技巧把方程变严格抛物）。

**曲率演化**：标量曲率 $\partial_tR=\Delta R+2\lvert\operatorname{Ric}\rvert^2\ge\Delta R+\frac2nR^2$；Riemann 张量 $\partial_t\operatorname{Rm}=\Delta\operatorname{Rm}+Q(\operatorname{Rm})$。由最大值原理，$R\ge0$ 保持；**截面曲率非负性在 Ricci 流下保持**。

**Hamilton 张量最大值原理 / 针形估计**：三维 Ricci 流中负截面曲率被"捏挤"控制：$R_{1313}+\lambda^2R_{2323}+\mu^2R_{1212}\ge-\epsilon/t$。这保证三维奇点模型具**非负截面曲率**。

**Hamilton 定理（1982）**：$M^3$ 紧致、初值严格正 Ricci $\Rightarrow$ 规范化 Ricci 流对所有时间光滑存在，收敛于常正截面曲率度量（$\mathbb{S}^3/\Gamma$）。故 $M^3$ 微分同胚于球面空间形式（Poincaré 猜想在正 Ricci 情形）。三维特殊性：正 Ricci $\iff$ 正截面曲率。

**Perelman 熵**：$\mathcal F(g,f)=\int_M(R+\lvert\nabla f\rvert^2)e^{-f}d\mu$（$\int e^{-f}d\mu=1$）；$\mathcal W(g,f,\tau)=\int_M[\tau(R+\lvert\nabla f\rvert^2)+f-n](4\pi\tau)^{-n/2}e^{-f}d\mu$（$\tau=T-t$ 逆向时间）。$\mathcal W$ 沿 Ricci 流（配共轭热方程）**单调不减**、有界（$\le0$）；不变临界点是**收缩梯度孤子**。

**非坍塌定理**：存在 $\kappa=\kappa(g_0,T)>0$，使得在抛物柱上 $\lvert\operatorname{Rm}\rvert\le r^{-2}$ 时 $\operatorname{vol}B(x_0,r)\ge\kappa r^n$。非坍塌保证奇点附近取极限不退化，从而能定义**奇点模型**（古代解且 $\kappa$-非坍塌）。

**手术与几何化**：截去高曲率"颈"、粘标准帽、继续演化；手术只做有限多次。最终推出**几何化猜想**：任一紧致三维流形可切成若干带八种 Thurston 几何之一的块；特别地**单连通三维流形同胚于 $\mathbb{S}^3$（Poincaré 猜想）**。

---

## 5. Yamabe 问题

**问题**：给定紧致 $(M^n,g)$（$n\ge3$），是否存在共形度量 $\tilde g=u^{\frac{4}{n-2}}g$（$u>0$）使标量曲率为常数？

**共形变换公式**：$\tilde R=u^{-\frac{n+2}{n-2}}(Ru-4\frac{n-1}{n-2}\Delta u)$。令 $\tilde R=\text{const}$ 得 **Yamabe 方程**

$$4\frac{n-1}{n-2}\Delta u-Ru+\lambda u^{\frac{n+2}{n-2}}=0,$$

带**临界 Sobolev 指数** $\frac{n+2}{n-2}=2^*-1$ 的半线性椭圆方程——非线性幂恰是 Sobolev 嵌入 $H^1\hookrightarrow L^{2^*}$ 的临界幂，故**变分紧性失效**，这是困难的根源。

**Yamabe 泛函与不变量**：$Q(\tilde g)=\frac{\int_M\tilde Rd\tilde\mu}{(\operatorname{vol}(M,\tilde g))^{(n-2)/n}}$（共形不变）；**Yamabe 不变量** $\lambda(M)=\inf_{\tilde g\in[g]}Q(\tilde g)$。达到下确界的度量必为常标量曲率。$\lambda(M)\le Y(\mathbb{S}^n)=n(n-2)\omega_n^{2/n}$（Aubin 常数），**等号成立与否是分水岭**。

**解决三阶段**：

1. **次临界逼近（Trudinger）**：$p<\frac{n+2}{n-2}$ 时 Sobolev 嵌入紧，直接变分法得解；取极限可能"气泡化"。阈值：$\lambda(M)<Y(\mathbb{S}^n)$ 时不气泡化；
2. **Aubin (1976)**：$n\ge6$ 且非局部共形平坦时 $\lambda(M)<Y(\mathbb{S}^n)$，用泡测试函数 + Weyl 张量二阶展开；
3. **Schoen (1984)**：用**正质量定理**完成剩余情形（$n=3,4,5$ 或局部共形平坦）：构造共形正规坐标下渐近平坦流形的 ADM 质量，质量为正则 $\lambda(M)<Y(\mathbb{S}^n)$。

**正质量定理（Schoen–Yau 1979；Witten 1981）**：渐近平坦流形若 $R\ge0$，则 ADM 质量 $m\ge0$，$m=0$ 当且仅当等距于欧氏空间。

**集中紧性（P.-L. Lions）与气泡分析**：临界时 Palais–Smale 序列分解为 $u_k=u+\sum_j\delta_{x_j}^{-\frac{n-2}{2}}\psi(\frac{x-x_j}{\delta_{x_j}})+\text{余项}$，泡携带球面临界能量 $Y(\mathbb{S}^n)$；若 $\lambda(M)=Y(\mathbb{S}^n)$ 则解凝聚成泡而退化。**拓扑推论**：环面 $T^n$ 不能承载正标量曲率度量（Yamabe 不变量为 0）；$\lambda(M)>0$ 等价于存在正标量曲率度量。

---

## 6. 极小曲面

**面积泛函** $\mathcal A(\Sigma)=\int_\Sigma d\mathcal H^k$，一阶变分 $\frac{d}{dt}\big|_{t=0}\mathcal A=-\int_\Sigma\langle\vec H,X\rangle d\mathcal A$，$\vec H$ 是**平均曲率向量**。故**极小曲面 $\iff\vec H\equiv0$**。二阶变分非负则为**稳定极小曲面**。

**图情形的极小曲面方程 (MSE)**：$\Sigma=\operatorname{graph}(u)$ 时

$$\operatorname{div}\left(\frac{\nabla u}{\sqrt{1+\lvert\nabla u\rvert^2}}\right)=0\quad\Longleftrightarrow\quad(1+\lvert\nabla u\rvert^2)\Delta u-\sum_{i,j}u_iu_ju_{ij}=0,$$

典型**拟线性椭圆方程**，是 De Giorgi–Nash–Moser 正则性理论与几何变分问题的交汇。

**Plateau 问题**：给定闭曲线 $\Gamma$，求以 $\Gamma$ 为边界的最小面积曲面。Douglas 与 Radó（1930s）用变分法 + 共形参数化解决圆盘型；现代方法（Federer–Fleming、De Giorgi）用几何测度论的**整流 (integral current)** 与紧性定理。**正则性**：极小整流的奇异集余维至少 2（超曲面时余维 7）——维数 $\le7$ 超曲面极小曲面光滑，维数 8 起可能出现奇异点。

**Bernstein 定理**：$\mathbb{R}^3$ 上整体极小图（定义在整个 $\mathbb{R}^2$ 上的 MSE 解）必为平面。推广：$n\le7$ 时 $\mathbb{R}^n$ 上整体极小图必为超平面（De Giorgi $n=3$、Almgren $n=4$、Simons $n\le7$）；$n\ge8$ 时**否**（Bombieri–De Giorgi–Giusti 1969 构造非平凡整体极小图）。

**Simons 锥**：$C=\{(x,y)\in\mathbb{R}^m\times\mathbb{R}^m:\lvert x\rvert=\lvert y\rvert\}$。$m\le3$ 时 $C\setminus\{0\}$ 是**不稳定**极小曲面；$m\ge4$（即 $\mathbb{R}^8$ 及以上）时 $C$ 是**稳定**且**面积最小**的。故 $\mathbb{R}^8$ 中存在奇异极小超曲面（锥顶点奇异，奇异集余维 7）——这给出正则性结论的精确阈值。

**与几何分析的互动**：Bernstein 型问题与调和函数 Liouville 同源（低维刚性、高维反例）；**稳定极小超曲面上的 Sobolev 不等式**（Schoen–Yau, Michael–Simon）是正质量定理证明的关键工具；**Weierstrass 表示**把 $\mathbb{R}^3$ 极小曲面化约为复分析（一对共轭调和函数 / 亚纯函数 + 全纯 1-形式）。

---

## 关键结论速查

- **曲率 ⇒ 分析**：Bochner 公式 $\frac12\Delta\lvert\nabla u\rvert^2=\lvert\nabla^2u\rvert^2+\operatorname{Ric}(\nabla u,\nabla u)$ 是唯一通道。
- **三大刚性**：Yau（$\operatorname{Ric}\ge0$ + 正调和 ⇒ 常数）；Bishop（$\operatorname{Ric}\ge0$ + 欧氏体积增长 ⇒ 平坦）；分裂定理（$\operatorname{Ric}\ge0$ + 直线 ⇒ 乘积）。
- **Harnack = 非负解的刚性**；抛物 Harnack（Li–Yau）⇔ 热核 Gaussian 界 ⇔ 体积倍增 + Poincaré。
- **Ricci 流** = 度量的非线性热方程；Perelman 熵单调 ⇒ 非坍塌 ⇒ 奇点模型是孤子；手术 ⇒ Poincaré 猜想。
- **临界 Sobolev 指数** $2^*=\frac{2n}{n-2}$ 是 Yamabe 问题困难的根源（变分紧性失效、气泡化）。
- **极小曲面**：$\vec H=0$；奇异集余维 $\ge7$；Bernstein 定理的维数 7/8 分界（Simons 锥）。
