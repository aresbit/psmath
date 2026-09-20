# 表示论：有限群与紧李群 (Representation Theory)

> **整理自**：Fulton–Harris《Representation Theory: A First Course》(GTM 129)、Serre《Linear Representations of Finite Groups》、Anupam Singh《Representation Theory of Finite Groups》(arXiv:1004.1287)、Brian Hall《Lie Groups, Lie Algebras, and Representations》、Peter Woit 讲义（Columbia）、Sepanski《Compact Lie Groups》
> **适用触发词**：表示、G-模、群代数、不可约、完全可约、Maschke、Schur 引理、特征标、类函数、正交关系、特征标表、多重度、诱导表示、限制、Frobenius 互反、Mackey、Artin-Wedderburn、Young 图、Specht 模、钩长公式、Schur 函数、紧李群、Haar 测度、Peter-Weyl、表示环、最高权、Weyl 积分、Weyl 特征标公式、SU(2)、SU(3)

## 0. 一句话定位

表示论让群作用在线性空间上，把抽象群翻译成矩阵语言。一条主线贯穿：**把群变成矩阵 → 用迹（特征标）提取不变量 → 用正交关系把表示空间对角化**。三个递进问题：有限群表示能否完全拆解（Maschke + 特征标正交）、如何从子群"造"出表示的诱导、紧李群由最高权分类。

## 1. 表示、$$G$$-模与 Schur 引理（ch01）

- **表示** = 群同态 $$\rho:G\to\operatorname{GL}(V)$$ = 群作用在向量空间上 = $$\mathbb{C}[G]$$-模（四者等价）。群代数 $$\mathbb{C}[G]$$ 把群论化归为环上模论。
- **子表示**（$$G$$-不变子空间）、**不可约表示**（原子）、**完全可约**（可拆成不可约直和）。
- **等变映射**：$$\phi\circ\rho(g)=\sigma(g)\circ\phi$$；全体记 $$\operatorname{Hom}_G(V,W)$$。
- **Schur 引理**：
  1. 不可约表示间的等变映射非 0 即同构；
  2. 不可约表示的自同态是标量倍（依赖代数闭域，用特征值 + 核非零论证）。
  - Schur 引理是特征标正交性的代数根基。
- **Maschke 定理**：有限群复表示完全可约。核心技巧是**平均**：$$\pi_0(v)=\dfrac{1}{|G|}\sum_g\rho(g)\pi\rho(g^{-1})v$$ 是等变投影。
  - 需要 $$\operatorname{char}\mathbb{C}\nmid|G|$$；特征整除 $$|G|$$ 时失效（模表示论复杂的根源）。

## 2. 特征标理论（ch02）

- **特征标** $$\chi_\rho(g)=\operatorname{tr}\rho(g)$$：$$\chi(e)=\dim V$$，$$\chi(ghg^{-1})=\chi(h)$$（类函数），$$\chi_{V\oplus W}=\chi_V+\chi_W$$，$$\chi_{V\otimes W}=\chi_V\cdot\chi_W$$，$$\chi_{V^*}=\overline{\chi_V}$$。
- **类函数空间** $$\mathcal{C}(G)$$（维数 = 共轭类个数），内积 $$\langle f_1,f_2\rangle=\dfrac{1}{|G|}\sum_g f_1(g)\overline{f_2(g)}$$。
- **第一正交性**：不可约特征标正交单位 $$\langle\chi,\psi\rangle=\delta_{\chi\psi}$$（把 Schur 引理翻译成迹的运算）。
- **结构定理**：不可约表示个数 = 共轭类个数。**第二正交性**（列加权正交）：$$\sum_i\chi_i(\mathcal{C}_1)\overline{\chi_i(\mathcal{C}_2)}=\dfrac{|G|}{|\mathcal{C}_1|}\delta_{\mathcal{C}_1,\mathcal{C}_2}$$。
- **特征标表**：行 = 不可约表示，列 = 共轭类。例 $$S_3$$（3 个共轭类）：平凡 $$(1,1,1)$$、符号 $$(1,-1,1)$$、标准 $$(2,0,-1)$$。
- **多重度公式**：$$V\cong\bigoplus_i V_i^{\oplus m_i}$$，$$m_i=\langle\chi_V,\chi_i\rangle$$。判据：$$V$$ 不可约 $$\iff\langle\chi_V,\chi_V\rangle=1$$。
- **正则表示**：$$\chi_{\text{reg}}(g)=|G|$$（$$g=e$$）或 0——由此得**维数平方和** $$\sum_i(\dim V_i)^2=|G|$$，且每个 $$V_i$$ 在正则表示中出现 $$\dim V_i$$ 次。

## 3. 诱导表示（ch03）

- **限制** $$\operatorname{Res}_H^G V$$（往下走）与**诱导** $$\operatorname{Ind}_H^G W$$（往上走），是一对伴随。
- **构造**：$$\operatorname{Ind}_H^G W=\{f:G\to W:f(gh)=\sigma(h^{-1})f(g)\}$$，$$G$$ 左平移，维数 $$[G:H]\dim W$$；纤维版：复制 $$[G:H]$$ 份 $$W$$ 并用群作用编织。
- **Frobenius 互反律**：$$\langle\operatorname{Ind}_H^G W,V\rangle_G=\langle W,\operatorname{Res}_H^G V\rangle_H$$。
- **诱导特征标**：$$\chi_{\operatorname{Ind}_H^G W}(g)=\sum_{i:g_i^{-1}gg_i\in H}\chi_W(g_i^{-1}gg_i)$$（$$g_i$$ 跑遍陪集代表元）——由"$$g$$ 的共轭落回 $$H$$"的项加权。
- **例子**：正则 = $$\operatorname{Ind}_{\{e\}}^G\mathbb{C}$$；传递置换表示 = 平凡表示的诱导；$$S_3$$ 二维标准表示 = 从 $$\langle(12)\rangle$$ 的符号表示诱导。
- **传递性** $$\operatorname{Ind}_H^G\circ\operatorname{Ind}_K^H\cong\operatorname{Ind}_K^G$$；**Mackey 公式**：$$\operatorname{Res}_K^G\operatorname{Ind}_H^G W\cong\bigoplus_{g\in K\backslash G/H}\operatorname{Ind}_{K\cap gHg^{-1}}^K({}^gW)$$，是判诱导不可约的核心工具。

## 4. 群代数与对称群（ch04）

- **Artin–Wedderburn**：$$\mathbb{C}[G]\cong\bigoplus_i\operatorname{End}(V_i)\cong\bigoplus_i M_{d_i}(\mathbb{C})$$，两边维数相等给出 $$\sum d_i^2=|G|$$。正则表示是"总仓库"，每个 $$V_i$$ 以多重度 $$d_i$$ 藏在其中。
- **中心** $$Z(\mathbb{C}[G])$$ 由**类求和** $$C_{\mathcal{K}}=\sum_{g\in\mathcal{K}}g$$ 张成，$$\dim Z=r$$（共轭类个数）——双重视角印证"不可约表示个数 = 共轭类个数"。
- **对称群** $$S_n$$：共轭类由**循环型（划分）** 分类，故不可约表示个数 = $$n$$ 的划分数 $$p(n)$$。
- **Young 图与 Specht 模** $$S^\lambda$$：划分 $$\lambda$$ 参数化不可约表示，维数由**钩长公式**给出
  $$\dim S^\lambda=\dfrac{n!}{\prod_{\square\in\lambda}h(\square)},$$
  $$h(\square)$$ = 该格右侧 + 下方 + 自身的格子数。$$\lambda=(n)$$ 平凡，$$(1,\dots,1)$$ 符号，$$(n-1,1)$$ 标准表示（维数 $$n-1$$）。
- **Frobenius 特征标公式**：$$\chi_{S^\lambda}(\mu)=[x_1^{l_1}\cdots x_m^{l_m}]\ \Delta(x)\prod_j p_{\mu_j}(x)$$（$$l_i=\lambda_i+m-i$$，$$\Delta$$ 为 Vandermonde，$$p_k$$ 为幂和）——把 $$S_n$$ 特征标化为对称函数系数，接通用 **Schur 函数** $$s_\lambda$$。

## 5. 紧李群与 Peter–Weyl（ch05）

- **Haar 测度**：紧群上唯一的双不变归一化 Borel 测度（$$\mu(G)=1$$），是有限群计数测度的连续类比。
- **紧群表示完全可约**：用 Haar 测度平均构造 $$G$$-不变内积 $$\langle v,w\rangle=\int_G(\rho(g)v,\rho(g)w)\,dg$$，再取正交补。不可约表示有限维，满足 Schur 引理。
- **Peter–Weyl 定理**：矩阵系数在 $$L^2(G)$$ 中稠密；正则表示分解为
  $$L^2(G)\cong\widehat{\bigoplus}_{\rho\in\widehat{G}}(V_\rho\otimes V_\rho^*),$$
  每个不可约表示以多重度 $$\dim V_\rho$$ 出现——有限群 Artin–Wedderburn 的无穷维连续版本。
- **特征标正交性**：$$\int_G\chi_\rho(g)\overline{\chi_\sigma(g)}\,dg=\delta_{\rho\sigma}$$。
- **表示环** $$R(G)$$：直和 ⊕ 与张量积 ⊗ 下的 Grothendieck 群，特征标给出单射 $$R(G)\hookrightarrow\mathcal{C}(G)$$。**Clebsch–Gordan 系数**：$$V_\lambda\otimes V_\mu\cong\bigoplus_\nu c_{\lambda\mu}^\nu V_\nu$$。例：$$R(\operatorname{SU}(2))\cong\mathbb{Z}[t]$$。

## 6. 最高权理论（ch06）

- **极大环面** $$T$$：每个元素共轭于 $$T$$ 中元素（$$G=\bigcup_x xTx^{-1}$$），故类函数由其在 $$T$$ 上的值决定；表示限制到 $$T$$ 可同时对角化。
- **权格** $$X^*(T)=\operatorname{Hom}(T,S^1)\cong\mathbb{Z}^m$$；**权空间** $$V_\mu=\{v:\rho(t)v=\mu(t)v\}$$，$$V=\bigoplus_\mu V_\mu$$；特征标 = 权的带重数和 $$\chi_V(t)=\sum_\mu\dim V_\mu\,e^\mu(t)$$。
- **根**：伴随表示 $$\operatorname{Ad}:G\to\operatorname{GL}(\mathfrak{g})$$ 的非零权；$$\mathfrak{g}_{\mathbb{C}}=\mathfrak{t}_{\mathbb{C}}\oplus\bigoplus_{\alpha\in\Phi}\mathfrak{g}_\alpha$$（每个根空间一维）。选正根 $$\Phi^+$$、单根 $$\Delta$$。
- **Weyl 群** $$W=N_G(T)/T$$，由反射 $$s_\alpha(\mu)=\mu-\langle\mu,\alpha^\vee\rangle\alpha$$ 生成（$$\operatorname{SU}(n)$$ 时即 $$S_n$$）。
- **支配权**：$$\langle\lambda,\alpha^\vee\rangle\ge0$$ 对一切正根；**最高权**：偏序 $$\mu\le\lambda\iff\lambda-\mu\in\mathbb{Z}_{\ge0}\Phi^+$$ 下最大。
- **最高权定理**：连通紧李群的不可约表示与支配权一一对应；权集被 Weyl 群不变，且 $$\mu\le\lambda$$。
- **$$\operatorname{SU}(2)$$**：支配权 = 非负整数 $$\lambda$$，$$V_\lambda=\operatorname{Sym}^\lambda\mathbb{C}^2$$，维数 $$\lambda+1$$，权集 $$\{\lambda,\lambda-2,\dots,-\lambda\}$$，特征标 $$\chi_\lambda(t)=\dfrac{\sin((\lambda+1)\theta)}{\sin\theta}$$（自旋 $$j=\lambda/2$$ 表示）。

## 7. Weyl 特征标公式（ch07）

- **Weyl 积分公式**：$$\int_G f(g)\,dg=\dfrac{1}{|W|}\int_T|\Delta(t)|^2\Big(\int_{G/T}f(xtx^{-1})\,d(xT)\Big)dt$$，$$\Delta(t)=\prod_{\alpha\in\Phi^+}(e^{\alpha/2}-e^{-\alpha/2})$$ 是 **Weyl 分母**。类函数时内层积分与 $$x$$ 无关。
- **交错和** $$A(\mu)=\sum_{w\in W}\varepsilon(w)e^{w\mu}$$（$$\varepsilon(w)=\det w=(-1)^{\ell(w)}$$）。
- **Weyl 特征标公式**：$$\chi_\lambda=\dfrac{A(\lambda+\rho)}{A(\rho)}=\dfrac{\sum_w\varepsilon(w)e^{w(\lambda+\rho)}}{\sum_w\varepsilon(w)e^{w\rho}}$$，$$\rho=\frac{1}{2}\sum_{\alpha>0}\alpha$$。
- **分母公式**：$$A(\rho)=\prod_{\alpha>0}(e^{\alpha/2}-e^{-\alpha/2})=\Delta(t)$$。
- **Weyl 维数公式**：$$\dim V_\lambda=\prod_{\alpha>0}\dfrac{\langle\lambda+\rho,\alpha\rangle}{\langle\rho,\alpha\rangle}$$。
  - $$\operatorname{SU}(2)$$：$$\dim V_\lambda=\lambda+1$$，特征标回到 $$\sin((\lambda+1)\theta)/\sin\theta$$。
  - $$\operatorname{SU}(3)$$：$$\dim V_{(m,n)}=\dfrac{(m+1)(n+1)(m+n+2)}{2}$$（八重法：夸克 3 维、八重态 8 维）。
- **延伸**：Borel–Weil 定理（$$V_\lambda$$ 实现为旗流形 $$G/T$$ 上的全纯线丛截面）、Kac–Weyl 公式（仿射李代数）、Harish-Chandra 特征标公式（非紧约化群）。

## 8. 代数大师的解题清单（表示论侧）

1. **先判完全可约**：有限群用 Maschke（特征 0 自动），紧群用 Haar 平均——然后聚焦不可约表示的分类。
2. **不可约表示用特征标记账**：个数 = 共轭类数，维数平方和 = $$|G|$$，正交关系是可计算的核心。
3. **要"造"表示就诱导**：从子群表示诱导，用 Frobenius 互反 + Mackey 判定不可约。
4. **对称群用组合**：划分 ↔ Young 图 ↔ Specht 模 ↔ Schur 函数，维数用钩长公式。
5. **李群用最高权**：不可约表示 ↔ 支配权；维数用 Weyl 维数公式，特征标用 Weyl 特征标公式，张量积分解用表示环 + Clebsch–Gordan。
