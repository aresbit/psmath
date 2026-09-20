# 代数数论：数域、整数环、戴德金环、理想类群与单位定理

> 整理自 Daniel A. Marcus, *Number Fields* (Universitext, Springer)，配合 J. S. Milne, *Algebraic Number Theory* (v3.08) 与 Robert B. Ash, *A Course in Algebraic Number Theory*。

从 $\mathbb{Q}$ 的算术（唯一分解、整数、单位）推广到一般数域 $K$，核心对象是整数环 $\mathcal{O}_K$ 上的理想算术。

## 一句话心智模型

$\mathbb{Z}$ 里唯一分解会失效（例如 $\mathbb{Z}[\sqrt{-5}]$ 中 $6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})$），但**理想**总是唯一分解成**素理想**。于是把"数"替换成"理想"：类数度量理想分解与主理想分解的差距，单位群刻画"乘法可逆元"的结构。

## 1. 数域、代数整数与整数环

**代数数**：复数 $\alpha$ 是某个非零有理系数多项式的根。**代数数域**：$\mathbb{Q}$ 的有限次扩张 $K$，$[K:\mathbb{Q}]=n$。由本原元定理，$K=\mathbb{Q}(\alpha)$，其中 $\alpha$ 是某个 $n$ 次不可约多项式 $f\in\mathbb{Q}[X]$ 的根。

**代数整数**：$\alpha$ 是某个**首一**整数系数多项式的根，即存在

$$X^m + a_{m-1}X^{m-1}+\cdots+a_0\in\mathbb{Z}[X],\qquad a_i\in\mathbb{Z}$$

使 $f(\alpha)=0$。

**整数环** $\mathcal{O}_K$：$K$ 中全体代数整数构成的集合。它是一个环，且是 $\mathbb{Z}$ 在 $K$ 中的**整闭包**。

**关键判别**：$\alpha\in K$ 是代数整数 $\iff$ 其极小多项式系数都在 $\mathbb{Z}$。$\mathcal{O}_K\cap\mathbb{Q}=\mathbb{Z}$。

### 范数与迹

设 $K/\mathbb{Q}$ 有 $n$ 个嵌入 $\sigma_1,\dots,\sigma_n:K\hookrightarrow\mathbb{C}$（$r_1$ 个实嵌入，$2r_2$ 个复嵌入，$n=r_1+2r_2$）。对 $\alpha\in K$，

$$\mathrm{Nm}_{K/\mathbb{Q}}(\alpha)=\prod_{i=1}^{n}\sigma_i(\alpha), \qquad \mathrm{Tr}_{K/\mathbb{Q}}(\alpha)=\sum_{i=1}^{n}\sigma_i(\alpha).$$

核心性质：

- $\alpha\in\mathcal{O}_K\Rightarrow\mathrm{Nm}(\alpha),\mathrm{Tr}(\alpha)\in\mathbb{Z}$。
- $\alpha\in\mathcal{O}_K$ 是**单位** $\iff\mathrm{Nm}(\alpha)=\pm 1$。
- 若 $f=X^n+c_{n-1}X^{n-1}+\cdots+c_0$ 是 $\alpha$ 的极小多项式，则 $\mathrm{Tr}(\alpha)=-\frac{n}{m}c_{m-1}$、$\mathrm{Nm}(\alpha)=(-1)^n c_0^{n/m}$，$m=[\mathbb{Q}(\alpha):\mathbb{Q}]$。

### 判别式

对 $n$ 个元素 $\alpha_1,\dots,\alpha_n\in K$，

$$\mathrm{disc}(\alpha_1,\dots,\alpha_n)=\det\left(\mathrm{Tr}(\alpha_i\alpha_j)\right)_{1\le i,j\le n}=\det\left(\sigma_i(\alpha_j)\right)^2.$$

- 判别式 $\ne 0\iff\{\alpha_1,\dots,\alpha_n\}$ 是 $K$ 的 $\mathbb{Q}$-基。
- 若 $\{\alpha_1,\dots,\alpha_n\}$ 是 $\mathcal{O}_K$ 的 $\mathbb{Z}$-**整基**，则判别式是与基选取无关的整数，记 $\Delta_K=\mathrm{disc}(\mathcal{O}_K/\mathbb{Z})$，称为**域的判别式**。

对多项式 $f=\prod_{i=1}^n(X-\alpha_i)$，$\mathrm{disc}(f)=\prod_{i<j}(\alpha_i-\alpha_j)^2=(-1)^{n(n-1)/2}\prod_{i=1}^n f'(\alpha_i)$。

### $\mathcal{O}_K$ 是秩 $n$ 的自由 $\mathbb{Z}$-模

**定理**：$\mathcal{O}_K$ 是秩 $n$ 的自由阿贝尔群，即存在整基 $\{\alpha_1,\dots,\alpha_n\}$ 使

$$\mathcal{O}_K=\mathbb{Z}\alpha_1\oplus\cdots\oplus\mathbb{Z}\alpha_n.$$

**证明要点**：先证 $\mathcal{O}_K$ 含在某自由模中（取 $\mathbb{Q}$-基 $\beta_i\in\mathcal{O}_K$，乘公共分母），再证其为秩 $\le n$ 的有限生成 $\mathbb{Z}$-模，最后用判别式非退化证秩恰为 $n$。核心工具是迹形式 $(\alpha,\beta)\mapsto\mathrm{Tr}(\alpha\beta)$ 的非退化性。

### 例子

**二次域 $\mathbb{Q}(\sqrt m)$**（$m$ 无平方因子）：

$$\mathcal{O}_K = \begin{cases} \mathbb{Z}[\sqrt m] = \mathbb{Z}+\mathbb{Z}\sqrt m, & m\equiv 2,3\pmod 4,\\ \mathbb{Z}\left[\dfrac{1+\sqrt m}{2}\right], & m\equiv 1\pmod 4;\end{cases} \qquad \Delta_K = \begin{cases}4m, & m\equiv 2,3\pmod 4,\\ m, & m\equiv 1\pmod 4.\end{cases}$$

**分圆域 $\mathbb{Q}(\zeta_p)$**（$\zeta_p$ 为 $p$ 次本原单位根）：$\mathcal{O}_K=\mathbb{Z}[\zeta_p]$，$[K:\mathbb{Q}]=p-1$，$\Delta_K=\pm p^{\,p-2}$。

## 2. 戴德金环与理想唯一分解

### 动机

在 $\mathbb{Z}[\sqrt{-5}]$ 中 $6=2\cdot 3=(1+\sqrt{-5})(1-\sqrt{-5})$，$2,3,1\pm\sqrt{-5}$ 都是不可约元但彼此不结合，故 $6$ 有两种本质不同的分解，$\mathbb{Z}[\sqrt{-5}]$ 不是 UFD。

**Dedekind 的洞见**（受 Kummer 的"理想数"启发）：换成**理想**后唯一分解恢复：

$$(2)=(2,1+\sqrt{-5})^2,\qquad (3)=(3,1+\sqrt{-5})(3,1-\sqrt{-5}),$$

$$(1+\sqrt{-5})=(2,1+\sqrt{-5})(3,1+\sqrt{-5}),\qquad (1-\sqrt{-5})=(2,1+\sqrt{-5})(3,1-\sqrt{-5}),$$

两边合起来恰好得 $(6)=(2,1+\sqrt{-5})^2(3,1+\sqrt{-5})(3,1-\sqrt{-5})$，唯一。

### 定义与核心定理

**定义**：整环 $A$ 是**戴德金环**，若满足：

1. 诺特（理想升链条件）；
2. 整闭（$A$ 是其分式域中的整闭包）；
3. 每个非零素理想都极大（$\dim A\le 1$）。

**定理**：数域 $K$ 的整数环 $\mathcal{O}_K$ 是戴德金环。

证明要点：$\mathcal{O}_K$ 是秩 $n$ 自由 $\mathbb{Z}$-模故诺特；整闭来自整闭包定义；"非零素理想极大"由 $\mathfrak{p}\cap\mathbb{Z}=(p)$ 及 $\mathcal{O}_K/\mathfrak{p}$ 是有限整环（因而是域）证明。

**定理（理想唯一分解）**：在戴德金环 $A$ 中，每个非零真理想 $\mathfrak{a}$ 唯一写成

$$\mathfrak{a}=\mathfrak{p}_1^{e_1}\mathfrak{p}_2^{e_2}\cdots\mathfrak{p}_r^{e_r},$$

$\mathfrak{p}_i$ 互不相同的非零素理想。分解在次序与素理想集合上唯一。

**微观机制**：局部化 $A_{\mathfrak{p}}$ 是 DVR，DVR 中理想唯一分解为 $\mathfrak{m}^n$；由"非零素理想极大"知含 $\mathfrak{a}$ 的极大理想必是素因子；存在性靠局部化后除 $\mathfrak{p}$ 的幂归纳下降，唯一性靠局部化到每个素理想处比对指数。

**整除 = 包含**：$\mathfrak{a}\mid\mathfrak{b}\iff\mathfrak{a}\supseteq\mathfrak{b}$。这是理想算术与元素算术最关键的区别——"整除"翻译成了反包含。

### 分式理想成群

**分式理想**：$K$ 中满足"存在 $d\in A,d\ne 0$ 使 $d\,\mathfrak{a}\subseteq A$"的 $A$-子模 $\mathfrak{a}$。

**定理**：戴德金环 $A$ 的非零分式理想在乘法下构成**群** $\mathrm{Id}(A)$，其中 $\mathfrak{a}^{-1}=\{x\in K: x\,\mathfrak{a}\subseteq A\}$。

**等价刻画**（择要）：$A$ 诺特、整闭、$\dim\le 1$ $\iff$ 每个非零理想唯一分解为素理想 $\iff$ 非零分式理想成群 $\iff$ 每个非零素理想可逆 $\iff$ 每个 $A_{\mathfrak{p}}$ 是 DVR。

**与 UFD/PID 的关系**：$\text{PID}\Rightarrow\text{UFD}\Rightarrow\text{整闭}$，且 $\text{戴德金}+\text{UFD}=\text{PID}$。对 $\mathcal{O}_K$：$\mathcal{O}_K$ 是 UFD $\iff$ 是 PID $\iff$ 类数 $h_K=1$。

## 3. 素理想分解

设 $p$ 为素数，$p\mathcal{O}_K$ 在 $\mathcal{O}_K$ 中分解为

$$p\mathcal{O}_K=\mathfrak{P}_1^{e_1}\mathfrak{P}_2^{e_2}\cdots\mathfrak{P}_g^{e_g}.$$

定义三个量：

- **分歧指数** $e_i=e(\mathfrak{P}_i/p)$：$\mathfrak{P}_i^{e_i}\mid p\mathcal{O}_K$ 但 $\mathfrak{P}_i^{e_i+1}\nmid p\mathcal{O}_K$；
- **惯性次数/剩余次数** $f_i=f(\mathfrak{P}_i/p)=[\mathcal{O}_K/\mathfrak{P}_i:\mathbb{Z}/p\mathbb{Z}]$；
- $g$：$p$ 上方的素理想个数。

**基本恒等式**：

$$\sum_{i=1}^{g} e_i f_i = [K:\mathbb{Q}] = n.$$

**三种形态**：

- **分歧**：某个 $e_i>1$；
- **分裂**（完全分裂）：$e_i=f_i=1$ 对所有 $i$，即 $g=n$；
- **惯性**：$e=1,\ f=n,\ g=1$，即 $p\mathcal{O}_K$ 仍是素理想。

**理想范数**：$N(\mathfrak{a})=\lvert\mathcal{O}_K/\mathfrak{a}\rvert$。性质：$N(\mathfrak{ab})=N(\mathfrak{a})N(\mathfrak{b})$；$N((\alpha))=\lvert\mathrm{Nm}_{K/\mathbb{Q}}(\alpha)\rvert$；$N(\mathfrak{P})=p^{f}$。于是基本恒等式等价于 $N(p\mathcal{O}_K)=p^n$。

### Kummer 分解定理

**定理**：设 $\mathcal{O}_K=\mathbb{Z}[\alpha]$，$\alpha$ 的极小多项式为 $f\in\mathbb{Z}[X]$。若素数 $p\nmid[\mathcal{O}_K:\mathbb{Z}[\alpha]]$（当 $\{1,\alpha,\dots,\alpha^{n-1}\}$ 是整基时恒成立），设

$$\bar f(X)=\bar g_1(X)^{e_1}\cdots\bar g_r(X)^{e_r}\pmod p,$$

$\bar g_i\in\mathbb{F}_p[X]$ 互异首一不可约，$g_i\in\mathbb{Z}[X]$ 为任意提升。则

$$p\mathcal{O}_K=\mathfrak{P}_1^{e_1}\cdots\mathfrak{P}_r^{e_r}, \qquad \mathfrak{P}_i=(p,g_i(\alpha)),$$

且 $f(\mathfrak{P}_i/p)=\deg g_i$。

**一句话**：模 $p$ 多项式分解 $\bar f=\prod\bar g_i^{e_i}$ 直接给出理想分解 $p=\prod\mathfrak{P}_i^{e_i}$，指数对应，剩余次数对应度数。

**推论（分歧判别式判据）**：$p$ 在 $\mathcal{O}_K$ 中分歧 $\iff p\mid\Delta_K$。只有有限多个素数分歧，它们恰是 $\Delta_K$ 的素因子。

### 二次域实例

对 $K=\mathbb{Q}(\sqrt m)$（$m$ 无平方因子）：

- $p\mid\Delta_K\Rightarrow p$ 分歧：$(p)=\mathfrak{p}^2$（$e=2,f=1,g=1$）。
- $p$ 为奇素数，$p\nmid m$：由 Legendre 符号 $\left(\frac{m}{p}\right)$ 判定——
  - $\left(\frac{m}{p}\right)=1$：$p$ 分裂，$(p)=\mathfrak{p}_1\mathfrak{p}_2$（$e=1,f=1,g=2$）；
  - $\left(\frac{m}{p}\right)=-1$：$p$ 惯性，$(p)=\mathfrak{p}$（$e=1,f=2,g=1$）。
- $p=2$ 且 $m\equiv 1\pmod 4$：$m\equiv 1\pmod 8$ 时分裂，$m\equiv 5\pmod 8$ 时惯性。

**Gauss 整数例子**：$\mathbb{Z}[i]=\mathcal{O}_{\mathbb{Q}(i)}$ 是 PID。奇素数 $p$ 分裂 $\iff p\equiv 1\pmod 4\iff p=a^2+b^2$ 可表为两平方和。这是"两平方和定理"的代数数论证明。

## 4. 伽罗瓦理论与素分解

设 $L/K$ 是数域的伽罗瓦扩张，$G=\mathrm{Gal}(L/K)$，$\mathfrak{P}\mid\mathfrak{p}$。伽罗瓦情形的基本恒等式 $e f g=[L:K]$，且 $e,f,g$ 对 $\mathfrak{p}$ 上方的每个 $\mathfrak{P}$ 都相同。

**分解群**：$D_{\mathfrak{P}}=\{\sigma\in G:\sigma(\mathfrak{P})=\mathfrak{P}\}\le G$。

**惯性群**：$I_{\mathfrak{P}}=\{\sigma\in D_{\mathfrak{P}}:\sigma(x)\equiv x\pmod{\mathfrak{P}}\ \forall x\in\mathcal{O}_L\}\trianglelefteq D_{\mathfrak{P}}$。

数量关系：$\lvert D_{\mathfrak{P}}\rvert=ef$，$\lvert I_{\mathfrak{P}}\rvert=e$，$[D_{\mathfrak{P}}:I_{\mathfrak{P}}]=f$，$[G:D_{\mathfrak{P}}]=g$。

**Frobenius 元**：设 $\mathfrak{P}$ 非分歧（$I_{\mathfrak{P}}=1$），则 $D_{\mathfrak{P}}\cong\mathrm{Gal}(\kappa_{\mathfrak{P}}/\kappa_{\mathfrak{p}})$。有限域扩张有唯一 Frobenius 自同构 $x\mapsto x^q$（$q=\lvert\kappa_{\mathfrak{p}}\rvert$），其在 $D_{\mathfrak{P}}$ 中的原像记 $\mathrm{Frob}_{\mathfrak{P}}$，由 $\mathrm{Frob}_{\mathfrak{P}}(x)\equiv x^q\pmod{\mathfrak{P}}$ 唯一刻画，阶为 $f$。共轭类 $\mathrm{Frob}_{\mathfrak{p}}$ 不依赖 $\mathfrak{P}$ 的选取。

**阿贝尔情形**：$G$ 阿贝尔时 Frobenius 元良定义为 Artin 符号 $\left(\frac{L/K}{\mathfrak{p}}\right)\in G$，且 $\mathfrak{p}$ 分裂 $\iff\mathrm{Frob}_{\mathfrak{p}}=1$。$\mathbb{Q}(\sqrt m)/\mathbb{Q}$ 中 $\left(\frac{m}{p}\right)$ 正是 Frobenius 元的符号——这是互反律的原型。Chebotarev 密度定理说 Frobenius 元在 $G$ 中"均匀分布"，Dirichlet 定理是它的特例。

## 5. 格与 Minkowski 理论

**格**：$\mathbb{R}^n$ 中形如 $\Lambda=\mathbb{Z}e_1\oplus\cdots\oplus\mathbb{Z}e_n$ 的离散加法子群（$e_i$ 线性无关）。**基本域**体积 $\mathrm{covol}(\Lambda)=\lvert\det(e_1,\dots,e_n)\rvert$。

**定理（Minkowski 凸体定理）**：设 $\Lambda$ 是 $\mathbb{R}^n$ 中满秩格，$S$ 是凸、关于原点对称的可测集。若 $\mathrm{vol}(S)>2^n\mathrm{covol}(\Lambda)$，则 $S$ 含非零格点 $v\in\Lambda\setminus\{0\}$。

**标准嵌入**：$\sigma(\mathcal{O}_K)$ 是 $\mathbb{R}^{r_1}\times\mathbb{C}^{r_2}$ 中的满秩格，协体积

$$\mathrm{covol}\left(\sigma(\mathcal{O}_K)\right)=2^{-r_2}\sqrt{\lvert\Delta_K\rvert}.$$

这是判别式几何意义的最精确陈述。

**定理（Minkowski 界）**：每个理想类 $\mathfrak{c}\in\mathrm{Cl}(K)$ 含有整理想 $\mathfrak{a}$，其范数

$$N(\mathfrak{a})\le B_K:=\frac{n!}{n^n}\left(\frac{4}{\pi}\right)^{r_2}\sqrt{\lvert\Delta_K\rvert}.$$

**定理（类数有限）**：$h_K=\lvert\mathrm{Cl}(K)\rvert<\infty$。

证明：只需证范数 $\le M$ 的整理想只有有限多个——每个理想的素因子只能含 $N(\mathfrak{a})$ 的素理想，而每个素数上方素理想有限、指数被 $N(\mathfrak{a})$ 界定。结合 Minkowski 界即得。

**小判别式判定类数**：若 $B_K<2$，则每个理想类含范数 $<2$ 的整理想，即只有 $(1)$，故 $h_K=1$。例：$X^3+10X+1$ 判别式 $4027$，Minkowski 界 $\approx 4.28$，只需查范数 $2,3,4$ 的理想，得类数 $1$。

## 6. 理想类群

**定义**：$\mathrm{Cl}(K):=\mathrm{Id}(\mathcal{O}_K)/P(\mathcal{O}_K)$，其中 $P(\mathcal{O}_K)=\{(x):x\in K^\times\}$ 是主分式理想群。其阶 $h_K=\lvert\mathrm{Cl}(K)\rvert$ 称为**类数**。

**正合列**：

$$1\to\mathcal{O}_K^\times\to K^\times\xrightarrow{x\mapsto(x)}P(\mathcal{O}_K)\to 1, \qquad 1\to P(\mathcal{O}_K)\to\mathrm{Id}(\mathcal{O}_K)\to\mathrm{Cl}(K)\to 1.$$

**定理（$h_K=1$ 的刻画）**：以下等价：$h_K=1$；$\mathcal{O}_K$ 是 PID；$\mathcal{O}_K$ 是 UFD。故 $h_K$ 就是"$\mathcal{O}_K$ 偏离唯一分解"的量化。

**例**：

- $\mathbb{Q}(\sqrt{-5})$：类数 $2$，$\mathrm{Cl}(K)\cong\mathbb{Z}/2\mathbb{Z}$，生成元是 $(2,1+\sqrt{-5})$ 的类（$\mathfrak{p}^2=(2)$），对应 $6$ 的两种分解。
- **Heegner 定理**：$K=\mathbb{Q}(\sqrt{-m})$（$m$ 正无平方因子）类数 $1$ 当且仅当 $m\in\{1,2,3,7,11,19,43,67,163\}$——只有 9 个虚二次域是 PID。由 Heegner 1952 证明（后由 Baker、Stark 独立给出）。
- **分圆域 $\mathbb{Q}(\zeta_p)$**：类数为 $1$ 当且仅当 $p\le 19$。若 $p\nmid h_{\mathbb{Q}(\zeta_p)}$ 称 $p$ 为**正则素数**，此时费马大定理对指数 $p$ 成立。

**计算类群**：由 Minkowski 界 $B_K$，类群生成元来自范数 $\le B_K$ 的素理想。算法：列出所有范数 $\le B_K$ 的素理想（用 Kummer 定理分解 $p\mathcal{O}_K$）→ 求它们的乘积关系 → 用关系矩阵算有限阿贝尔群结构。实例：$\mathbb{Q}(\sqrt{-23})$ 类数 $3$，$\mathbb{Q}(\sqrt{-47})$ 类数 $5$。

**结构性质**：$\mathrm{Cl}(K)$ 是有限阿贝尔群。**Claborn 定理**：任意阿贝尔群都可实现为某个戴德金环的类群。Hilbert 类域 $H_K$ 是 $K$ 的最大非分歧阿贝尔扩张，且 $\mathrm{Gal}(H_K/K)\cong\mathrm{Cl}(K)$。

## 7. 狄利克雷单位定理

**单位群**：$\mathcal{O}_K^\times=\{u\in\mathcal{O}_K:\mathrm{Nm}(u)=\pm 1\}$。

**定理（Dirichlet 单位定理）**：

$$\mathcal{O}_K^\times\cong\mu(K)\times\mathbb{Z}^{r_1+r_2-1},$$

其中 $\mu(K)$ 是 $K$ 中全体单位根构成的**有限循环群**；$r_1+r_2-1$ 是**单位秩**。

**对数嵌入**：$L:K^\times\to\mathbb{R}^{r_1+r_2}$，$\alpha\mapsto(\log\lvert\sigma_1(\alpha)\rvert,\dots,\log\lvert\sigma_{r_1}(\alpha)\rvert,2\log\lvert\sigma_{r_1+1}(\alpha)\rvert,\dots)$。若 $u$ 是单位则 $\mathrm{Nm}(u)=\pm 1$，故 $L(u)$ 落在超平面

$$H: x_1+\cdots+x_{r_1}+2x_{r_1+1}+\cdots+2x_{r_1+r_2}=0,$$

而 $\dim H=r_1+r_2-1$。

**证明结构**：核 $\ker L=\mu(K)$ 有限（所有共轭模长为 1 的代数整数是单位根）；像 $L(\mathcal{O}_K^\times)$ 是 $H$ 中的格（离散）；满秩是核心难点，用 Minkowski 定理反复构造小范数元素配成单位差，证其线性无关。

**regulator**：设 $t=r_1+r_2-1$，自由部分的基 $\{u_1,\dots,u_t\}$ 称**基本单位**，

$$R_K=\left\lvert\det\left(\log\lvert\sigma_j(u_i)\rvert\right)_{1\le i,j\le t}\right\rvert.$$

$R_K$ 是单位格的协体积，与判别式对偶：判别式度量加法格 $\mathcal{O}_K$ 的密度，regulator 度量乘法格（单位）的密度。

**例**：

- 实二次域 $\mathbb{Q}(\sqrt m)$（$m>0$）：$r_1=2,r_2=0$，单位秩 $=1$，$\mathcal{O}_K^\times=\{\pm 1\}\times\mathbb{Z}$，基本单位 $\varepsilon>1$ 即 Pell 方程 $x^2-my^2=\pm 1$ 的最小正解，如 $\mathbb{Q}(\sqrt 2)$ 的基本单位是 $1+\sqrt 2$。
- 虚二次域 $\mathbb{Q}(\sqrt m)$（$m<0$）：$r_1=0,r_2=1$，单位秩 $=0$，$\mathcal{O}_K^\times=\mu(K)$ 有限；除 $\mathbb{Q}(i)$（$\mu=\{\pm 1,\pm i\}$）与 $\mathbb{Q}(\sqrt{-3})$（6 次单位根）外恒为 $\{\pm 1\}$。
- 全实三次域（$r_1=3,r_2=0$）：单位秩 $=2$，需两个基本单位。

**解析类数公式**：

$$h_K R_K = \frac{2^{r_1}(2\pi)^{r_2}}{\lvert\mu(K)\rvert\sqrt{\lvert\Delta_K\rvert}}\lim_{s\to 1}(s-1)\zeta_K(s).$$

Dedekind $\zeta$ 函数 $\zeta_K(s)$ 在 $s=1$ 处的留数把类数、regulator、判别式、单位根个数串成一个等式。

## 8. 心智模型

1. **推广链**：$\mathbb{Z}\subset\mathbb{Q}$ 推广为 $\mathcal{O}_K\subset K$；判别式是"整数环装得有多满"的度量。
2. **戴德金环 = 理想版 UFD**：诺特保证存在性，整闭保证"不遗漏解"，一维保证非零素理想都是极大理想。
3. **分解的三个不变量 $e,f,g$ 满足守恒律 $\sum e_i f_i=n$**；Kummer 定理把"代数数论中的分解"降维成"有限域上的多项式因式分解"。
4. **判别式是分歧的总账**：$\Delta_K$ 的素因子恰是分歧素数。
5. **$\sqrt{\lvert\Delta_K\rvert}$ 度量加法格体积，$R_K$ 度量单位格体积**；两者与类数一起出现在解析类数公式中。
