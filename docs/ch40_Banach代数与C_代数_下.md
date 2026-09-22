---
layout: default
---

# 第40章: Banach 代数与 C\* 代数·下：完整推导 (Banach Algebras and C\*-Algebras · Part II: Full Derivation)

> 配套预备: 见 第39章 Banach 代数与 C\* 代数·上（同一主题的具体铺垫，建议先读）

> 专家依据: `_experts/analysis/functional-analysis.md`（主）+ `_experts/analysis/spectral-theory.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

读完第 39 章的具体例子后——你已经在 $$\mathbb C^3$$、$$M_2(\mathbb C)$$ 这类有限维对象上手算过可逆性、谱、特征与自伴矩阵的实特征值——这里把同样的构造写成一般的 Banach 代数、C\* 代数定义，并给出完整证明。

第 36 章把「谱」定义成算子 $$\lambda I - T$$ 不可逆的标量集合，第 38 章用投影算子值测度把正规算子写成 $$T = \int z \, dE(z)$$。这两章里，「算子」始终是主角。但第 36 章留下了一个从未被回答的问题：**为什么自伴算子的谱一定落在实轴上？** 谱定理本身答不了它——谱定理是「给定自伴 $$T$$，构造 $$E$$」，它预设了 $$T$$ 自伴，却没有解释这条件如何逼出实数谱。

本章把镜头从「一个算子」退到「这个算子所在的代数」。一旦不盯着具体的 $$T$$、而是研究 $$T$$ 所在的代数 $$\mathcal A$$ 本身，谱就脱去了算子外衣，成为一个纯代数概念：$$\sigma(a) = \lbrace \lambda : \lambda e - a \text{ 不可逆} \rbrace$$。在这个高度上，**Gelfand 表示定理**说：任何含单位的交换 Banach 代数都同构于某个紧 Hausdorff 空间上的连续函数代数的子代数，于是

$$\sigma(a) = \Gamma(a)(\Delta(\mathcal A)) \qquad \text{「元素的谱」} = \text{「函数的值域」}.$$

再补上「对合」与 **C\* 恒等式** $$\lVert a^* a \rVert = \lVert a \rVert^2$$，**Arens 引理** 便一句话判定了自伴元的 Gelfand 表示是实值函数——第 36 章的悬念就此了结，量子力学「可观测量必须是实数」的公理有了数学根据。

从全书看，这是「对偶」这个动作第三次出现：第 06 章对偶的是向量空间，第 30 章（Riesz 表示）对偶的是 Hilbert 空间，本章对偶的是**代数本身**。前两次的对偶对象是「有线性结构的集合」，这次的对象还背着乘法——这预示着对偶不再只是空间与空间的配对，而会升级成范畴与范畴的等价（第 62 章）。

## 二、入口：一道具体的问题 (Entry Problem)

先摆两个代数。它们一个来自拓扑，一个来自算子论，表面上毫无关系。

**代数甲.** 设 $$X$$ 是紧 Hausdorff 空间，$$\mathcal A = C(X)$$ 是 $$X$$ 上的一切复值连续函数，装备逐点加法、逐点乘法，以及上确界范数
$$\lVert f \rVert_{C(X)} = \sup_{x \in X} \lvert f(x) \rvert .$$
乘法交换，单位元是常函数 $$\mathbf 1$$（恒取 1 的那个函数）。

**代数乙.** 设 $$H$$ 是复 Hilbert 空间，$$\mathcal B = \mathcal B(H)$$ 是 $$H$$ 上一切有界线性算子，装备加法、乘法（算子的复合）与算子范数 $$\lVert T \rVert = \sup_{\lVert x \rVert \le 1} \lVert Tx \rVert$$。单位元是恒同算子 $$I$$。当 $$\dim H \ge 2$$ 时乘法**不交换**。

**入口题（自编；骨架取自 Rudin《Functional Analysis》第 10 章习题，与 Kowalski《Spectral Theory in Hilbert Spaces》第 4 章）**

**(a)【函数的谱】** 在 $$\mathcal A = C(X)$$ 中称 $$f$$ **可逆**，若存在 $$g \in C(X)$$ 使 $$fg = \mathbf 1$$（即 $$f(x)g(x) = 1$$ 对每个 $$x$$ 成立）。证明：

$$f \text{ 不可逆} \iff \text{存在 } x \in X \text{ 使 } f(x) = 0 .$$

左边的「不可逆」是纯代数的（只用到乘法与单位元），右边的「取零」是纯几何的（只用到 $$X$$ 的点和函数值）。请体会这个等价的分量：**代数性质被翻译成了逐点性质**。

**(b)【算子的谱】** 取 $$H = L^2[0,1]$$，定义乘法算子
$$(M f)(x) = x f(x) \qquad (f \in L^2[0,1]) .$$
证明 $$M$$ 有界，并直接算出 $$\sigma(M) = [0,1]$$。

**(c)【统一的形状】** 把 (a)(b) 的答案并排写：

$$\sigma(f) = f(X) = \lbrace f(x) : x \in X \rbrace, \qquad \sigma(M) = [0,1] = \lbrace x : x \in [0,1] \rbrace .$$

右端都是「某个东西的**取值集合**」。于是请**猜**一个把两件事合并成同一条定理的陈述：应当存在一个紧空间 $$K$$、一个映射 $$\Gamma : \mathcal A \to C(K)$$（$$\mathcal A$$ 是交换的），使得 $$\Gamma$$ 保乘法、保单位、$$\lVert \Gamma(a) \rVert_\infty \le \lVert a \rVert$$，并且

$$\sigma(a) = \Gamma(a)(K) \qquad \text{对一切 } a \in \mathcal A .$$

请说明：$$K$$ 应该是什么？$$\Gamma$$ 应该往哪里送？

**(d)【非交换的边界】** $$L^2[0,1]$$ 上所有乘法算子 $$M_\varphi$$（$$\varphi \in L^\infty[0,1]$$）放在一起构成的代数 $$\mathcal M$$ 是**交换**的，(c) 对它有意义。但 $$\mathcal B(H)$$ 不交换：当 $$\dim H \ge 2$$ 时，只有 $$\lambda I$$ 形式的算子与所有算子交换。请解释：(c) 的陈述里「交换」这个前提**为什么不能去掉**（换句话说，$$\Delta$$ 这个「点集」在非交换时怎么会消失）；并给出一个**仍然有意义**的替代品——提示：固定单个算子 $$T$$，考虑由 $$T$$ 与 $$I$$ 生成的**交换**闭子代数。

一道题把这一章的全部骨架逼出来了：代数的谱（a）、算子谱是它的特例（b）、把两者统一起来的那张网（c）、以及这张网的适用边界（d）。下面开始造这张网。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 从线性空间到代数

第 02 章说过：复平面 $$\mathbb{C}$$ 相对于实平面 $$\mathbb{R}^2$$，多出来的东西就是那个二元乘法。把这句话抽象出来，就是本节的主角。

**定义 3.1（赋范代数与 Banach 代数, normed algebra / Banach algebra）** 设 $$\mathcal A$$ 是复线性空间，其上另给一个二元运算 $$\mathcal A \times \mathcal A \to \mathcal A$$，$$(a,b) \mapsto ab$$，称为**乘法 (multiplication)**。若乘法满足

- **结合律**：$$(ab)c = a(bc)$$；
- **双线性**：$$a(b+c) = ab + ac$$、$$(a+b)c = ac + bc$$、$$\lambda(ab) = (\lambda a)b = a(\lambda b)$$ 对一切 $$\lambda \in \mathbb{C}$$；

则称 $$\mathcal A$$ 是一个**代数 (algebra)**。若存在 $$e \in \mathcal A$$、$$e \ne 0$$，使 $$ea = ae = a$$ 对一切 $$a$$ 成立，则称 $$\mathcal A$$ 是**含单位的 (unital)**，$$e$$ 称为**单位元 (identity)**。若乘法还满足 $$ab = ba$$，则称 $$\mathcal A$$ **交换 (commutative)**。若每个非零元都可逆（即存在 $$b$$ 使 $$ab = ba = e$$），则称 $$\mathcal A$$ 为**可除代数 (division algebra)**。

若 $$\mathcal A$$ 上还给了一个范数 $$\lVert \cdot \rVert$$，使 $$\mathcal A$$ 在此范数下完备（每个柯西列收敛），并且满足**次乘性 (submultiplicativity)**

$$\lVert ab \rVert \le \lVert a \rVert \, \lVert b \rVert \qquad \text{对一切 } a, b \in \mathcal A,$$

则称 $$\mathcal A$$ 为**赋范代数 (normed algebra)**；若再完备，称它为 **Banach 代数 (Banach algebra)**。我们本章总是假设 Banach 代数含单位元，并**约定** $$\lVert e \rVert = 1$$。

**例（本章反复使用的三个 Banach 代数）**

1. $$C(X)$$：$$X$$ 紧 Hausdorff，逐点乘法，上确界范数。交换、含单位。
2. $$\mathcal B(H)$$：$$H$$ 复 Hilbert 空间，算子复合，算子范数。含单位 $$I$$；当 $$\dim H \ge 2$$ 时不交换。
3. $$\ell^1(\mathbb{Z})$$：绝对可和的双向数列 $$a = (a_n)_{n \in \mathbb{Z}}$$，$$\lVert a \rVert_1 = \sum_n \lvert a_n \rvert$$，乘法取**卷积**
$$(a * b)_n = \sum_{k \in \mathbb{Z}} a_k \, b_{n-k} .$$
单位元是 $$\delta_0 = (\dots,0,1,0,\dots)$$（仅在 $$n = 0$$ 处取 1）。交换、含单位。$$\ell^1(\mathbb{Z})$$ 与圆周 $$\mathbb{T}$$ 上的「绝对收敛 Fourier 级数代数」是同一件事：把 $$a$$ 送成形式级数 $$\sum_n a_n z^n$$，卷积就变成级数的乘法。

约定 $$\lVert e \rVert = 1$$ 是必要的一个技术选择。它自动成立的情形：$$C(X)$$ 中的 $$\mathbf 1$$、$$\mathcal B(H)$$ 中的 $$I$$、$$\ell^1$$ 中的 $$\delta_0$$ 都满足。若原始范数不满足，可以用等价的范数替换（见练习 基1 之后的注）。

### 3.2 代数的谱

第 36 章的谱定义里出现了 $$T$$、$$I$$ 与「$$H$$ 上的可逆」，处处依赖 Hilbert 空间。下面的定义把它剥到只剩代数运算。

**定义 3.2（可逆群与谱, group of invertibles / spectrum）** 设 $$\mathcal A$$ 是含单位的 Banach 代数。记
$$G(\mathcal A) = \lbrace a \in \mathcal A : a \text{ 在 } \mathcal A \text{ 中可逆} \rbrace$$
称为 $$\mathcal A$$ 的**可逆元群**。对 $$a \in \mathcal A$$，定义 $$a$$ 的**谱 (spectrum)** 与**预解集 (resolvent set)** 为

$$\sigma_{\mathcal A}(a) = \lbrace \lambda \in \mathbb{C} : \lambda e - a \notin G(\mathcal A) \rbrace, \qquad \rho_{\mathcal A}(a) = \mathbb{C} \setminus \sigma_{\mathcal A}(a) .$$

$$\sigma_{\mathcal A}(a)$$ 中的元素称为 $$a$$ 的**谱点**。当 $$\mathcal A = \mathcal B(H)$$ 时，这就是第 36 章已经用过的 $$\sigma(T)$$，所以我们不再区分记号，一律写 $$\sigma(a)$$。

要研究 $$\sigma(a)$$，第一件要弄清楚的事是「可逆」这个条件有多容易满足——如果可逆元多到充满一个开集，$$\sigma(a)$$ 才可能是良态的集合（闭集、甚至紧集）。第 39 章已经在 $$2\times2$$ 矩阵上手算过：只要 $$a$$ 「足够小」，$$e-a$$ 就能用幂级数直接写出逆。下面把这件事一般化到任意 Banach 代数。

**命题 3.3（Neumann 级数；可逆群是开集）** 设 $$\mathcal A$$ 含单位、$$\lVert e \rVert = 1$$。

(i) 若 $$\lVert a \rVert < 1$$，则 $$e - a \in G(\mathcal A)$$，并且
$$(e - a)^{-1} = \sum_{n=0}^{\infty} a^n, \qquad \lVert (e-a)^{-1} \rVert \le \frac{1}{1 - \lVert a \rVert} .$$

(ii) $$G(\mathcal A)$$ 是 $$\mathcal A$$ 的开集，且 $$a \mapsto a^{-1}$$ 在 $$G(\mathcal A)$$ 上连续。

**证明思路.** (i) 把截断和 $$s_N = e + a + \dots + a^{N-1}$$ 与 $$(e-a)$$ 相乘，中间的项全部相消，得到 $$(e-a)s_N = e - a^N$$。只要证明 $$a^N \to 0$$、$$s_N$$ 收敛，就让 $$N \to \infty$$。(ii) 在 (i) 的基础上，把可逆元 $$a$$ 附近的小扰动写成 $$a + h = a\,(e + a^{-1}h)$$。

**证明.** (i) 由次乘性归纳可得 $$\lVert a^n \rVert \le \lVert a \rVert^n$$，故 $$\sum_{n \ge 0} \lVert a^n \rVert \le \sum_{n\ge0}\lVert a \rVert^n = (1-\lVert a \rVert)^{-1} < \infty$$。由 $$\mathcal A$$ 完备与「绝对可和蕴含收敛」（见第 36 章的完备性判据），级数 $$s = \sum_{n\ge0} a^n$$ 在 $$\mathcal A$$ 中收敛。又

$$(e - a)s_N = s_N - a s_N = (e + a + \dots + a^{N-1}) - (a + a^2 + \dots + a^{N}) = e - a^N .$$

令 $$N \to \infty$$：左端 $$(e-a)s_N \to (e-a)s$$（乘法连续，因为 $$\lVert (e-a)(s - s_N) \rVert \le \lVert e - a \rVert \lVert s - s_N \rVert$$），右端 $$e - a^N \to e$$（因为 $$\lVert a^N \rVert \le \lVert a \rVert^N \to 0$$）。故 $$(e-a)s = e$$。同理把 $$s_N(e-a)$$ 展开得 $$s(e-a) = e$$。于是 $$(e-a)^{-1} = s$$。范数估计：$$\lVert s \rVert \le \sum_{n\ge0}\lVert a \rVert^n = (1-\lVert a\rVert)^{-1}$$。

(ii) 设 $$a \in G(\mathcal A)$$，取 $$h \in \mathcal A$$ 满足 $$\lVert h \rVert < \lVert a^{-1} \rVert^{-1}$$（若 $$a^{-1} = 0$$ 不可能，因为 $$a^{-1}$$ 可逆）。则 $$\lVert a^{-1}h \rVert \le \lVert a^{-1}\rVert \lVert h\rVert < 1$$，由 (i) $$e + a^{-1}h$$ 可逆，从而

$$a + h = a\,(e + a^{-1}h) \in G(\mathcal A),$$

即 $$a$$ 的一个邻域整体落在 $$G(\mathcal A)$$ 里，故 $$G(\mathcal A)$$ 开。再由 (i) 的级数，

$$(a+h)^{-1} = (e + a^{-1}h)^{-1} a^{-1} = \Big( \sum_{n\ge0} (-a^{-1}h)^n \Big) a^{-1},$$

于是 $$\lVert (a+h)^{-1} - a^{-1} \rVert = \lVert \big(\sum_{n\ge1}(-a^{-1}h)^n\big)a^{-1}\rVert \le \frac{\lVert a^{-1}h \rVert}{1 - \lVert a^{-1}h\rVert}\,\lVert a^{-1}\rVert \to 0$$（当 $$h \to 0$$）。逆映射连续。$$\blacksquare$$

命题 3.3 说明可逆元群是开集；下面把它翻译成谱的语言——「不可逆」是「可逆」的补集，补一个开集是闭集，于是 $$\sigma(a)$$ 自动是闭集，再加上一条容易的估计就能说它是紧集；「非空」则需要更硬的一条分析工具（Liouville 定理）。

**命题 3.4（谱是紧集且非空）** 设 $$\mathcal A$$ 含单位。对任意 $$a \in \mathcal A$$：

(i) $$\sigma(a)$$ 是 $$\mathbb{C}$$ 中的闭集，且 $$\sigma(a) \subset \lbrace \lambda : \lvert \lambda \rvert \le \lVert a \rVert \rbrace$$；于是一致有 $$\lVert \lambda e - a \rVert \ge \lvert \lambda \rvert - \lVert a \rVert$$。特别地，$$\sigma(a)$$ 是有界闭集，即**紧集**。

(ii) $$\sigma(a) \ne \varnothing$$。

**证明思路.** (i) 是命题 3.3 (ii) 的改写：补集 $$\rho(a)$$ 是 $$G(\mathcal A)$$ 在连续映射 $$\lambda \mapsto \lambda e - a$$ 下的原像，故开。(ii) 是 Liouville 定理的反证：若谱空，则预解式 $$R(\lambda) = (\lambda e - a)^{-1}$$ 是整函数，且在无穷远处趋于 $$0$$；用连续线性泛函把它压成纯量整函数，就得到矛盾。

**证明.** (i) 映射 $$\lambda \mapsto \lambda e - a$$ 从 $$\mathbb{C}$$ 到 $$\mathcal A$$ 连续（$$\lVert (\lambda e - a) - (\mu e - a)\rVert = \lvert \lambda - \mu \rvert \lVert e \rVert = \lvert \lambda-\mu \rvert$$）。由命题 3.3 (ii)，$$G(\mathcal A)$$ 开，故 $$\rho(a)$$ 是开集的原像，开；$$\sigma(a)$$ 闭。若 $$\lvert \lambda \rvert > \lVert a \rVert$$，则 $$\lVert a/\lambda \rVert = \lVert a \rVert/\lvert \lambda \rvert < 1$$，由命题 3.3 (i)

$$\lambda e - a = \lambda\,(e - a/\lambda) \text{ 可逆}, \qquad (\lambda e - a)^{-1} = \lambda^{-1}\sum_{n\ge0} (a/\lambda)^n,$$

且 $$\lVert (\lambda e - a)^{-1} \rVert \le \lvert\lambda\rvert^{-1}\,(1 - \lVert a \rVert/\lvert\lambda\rvert)^{-1} = \frac{1}{\lvert \lambda \rvert - \lVert a \rVert}$$。故 $$\lambda \notin \sigma(a)$$，即 $$\sigma(a)$$ 含于半径 $$\lVert a \rVert$$ 的闭圆盘内。

(ii) 记 $$R(\lambda) = (\lambda e - a)^{-1}$$（$$\lambda \in \rho(a)$$），称**预解式 (resolvent)**。先算**预解恒等式 (resolvent identity)**：对 $$\lambda, \mu \in \rho(a)$$，

$$R(\lambda) - R(\mu) = R(\lambda)\big[(\mu e - a) - (\lambda e - a)\big]R(\mu) = (\mu - \lambda)\, R(\lambda)R(\mu),\tag{3.1}$$

第一个等号是因为 $$R(\lambda)^{-1} = \lambda e - a = (\lambda e - a)$$，故 $$R(\lambda) = R(\lambda)(\mu e - a)R(\mu)$$、$$R(\mu) = R(\lambda)(\lambda e - a)R(\mu)$$，相减即得。

现在假设 $$\sigma(a) = \varnothing$$，即 $$R(\lambda)$$ 对一切 $$\lambda \in \mathbb{C}$$ 有定义。对任意连续线性泛函 $$f \in \mathcal A^*$$，令 $$u(\lambda) = f(R(\lambda))$$。由 (3.1)，

$$\frac{u(\lambda) - u(\mu)}{\lambda - \mu} = -\,f\big(R(\lambda)R(\mu)\big) \xrightarrow{\ \lambda \to \mu\ } -f\big(R(\mu)^2\big),$$

最后一步用了 $$R$$ 的连续性（命题 3.3 (ii)：$$R(\lambda) \to R(\mu)$$，乘法连续）。故 $$u$$ 在每点可导，是**整函数**。又当 $$\lvert \lambda \rvert > \lVert a \rVert$$ 时由 (i) 的估计 $$\lvert u(\lambda) \rvert \le \lVert f \rVert \, (\lvert \lambda \rvert - \lVert a \rVert)^{-1} \to 0$$，所以 $$u$$ 在整个 $$\mathbb{C}$$ 上有界。由 Liouville 定理（第 02 章），$$u$$ 是常函数；又 $$\lvert \lambda \rvert \to \infty$$ 时 $$u(\lambda) \to 0$$，故 $$u \equiv 0$$。

于是 $$f(R(\lambda)) = 0$$ 对一切 $$f \in \mathcal A^*$$、一切 $$\lambda$$ 成立。由 Hahn–Banach 的分离点推论（第 30 章的 Riesz 一节；若 $$R(\lambda) \ne 0$$，存在 $$f \in \mathcal A^*$$ 使 $$f(R(\lambda)) \ne 0$$），必须 $$R(\lambda) = 0$$ 对一切 $$\lambda$$。但 $$R(\lambda)$$ 是可逆元（它有逆 $$\lambda e - a$$），而 $$0$$ 不可逆（不存在 $$b$$ 使 $$0 \cdot b = e \ne 0$$）。矛盾。故 $$\sigma(a) \ne \varnothing$$。$$\blacksquare$$

### 3.3 谱半径公式

命题 3.4 只给出 $$\sigma(a) \subset \{\lvert\lambda\rvert \le \lVert a\rVert\}$$ 这样一个粗糙的包围圈，谱半径 $$r(a)$$ 究竟等于多少，$$\lVert a\rVert$$ 本身答不出来——第 39 章的例子已经提示了：一个幂零矩阵可以范数不小、谱半径却是零。下面这条公式给出 $$r(a)$$ 的精确值,而且只用到 $$a$$ 的幂的范数增长率。

**定理 3.5（谱半径公式, spectral radius formula）** 设 $$\mathcal A$$ 含单位，$$a \in \mathcal A$$，记 **谱半径 (spectral radius)**
$$r(a) = \sup_{\lambda \in \sigma(a)} \lvert \lambda \rvert .$$
（由命题 3.4，这是紧集上的上确界，有限且被取到。）则数列 $$\lVert a^n \rVert^{1/n}$$ 收敛，且

$$r(a) = \lim_{n \to \infty} \lVert a^n \rVert^{1/n} = \inf_{n \ge 1} \lVert a^n \rVert^{1/n} .$$

**证明思路.** 两个方向。**上界**：若 $$\lambda \in \sigma(a)$$ 则 $$\lambda^n \in \sigma(a^n)$$，于是 $$\lvert \lambda \rvert^n \le \lVert a^n \rVert$$，取 $$n$$ 次根再对 $$\lambda$$ 取上确界，得 $$r(a) \le \inf_n \lVert a^n\rVert^{1/n}$$。**下界 / 收敛性**：考察 $$(e - \lambda a)^{-1}$$ 的幂级数展开，它在 $$0$$ 附近的收敛半径由 Cauchy–Hadamard 公式给出，而这个函数的解析区域又受 $$\sigma(a)$$ 限制，两者夹逼即得。

**证明.** 第一步，先证次乘性给出的一个预备事实：数列 $$c_n = \lVert a^n \rVert$$ 满足 $$c_{m+n} \le c_m c_n$$（因为 $$a^{m+n} = a^m a^n$$）。由 **Fekete 引理**（见下），$$c_n^{1/n}$$ 收敛且极限等于 $$\inf_n c_n^{1/n}$$。所以极限与下确界的存在性已经有了，剩下的只是把它算成 $$r(a)$$。

（Fekete 引理的证明，一并给出，因为后面要用：固定 $$m$$，把 $$n$$ 写成 $$n = qm + s$$，$$0 \le s < m$$。则 $$c_n = c_{qm+s} \le c_m^{q} c_s$$，于是
$$c_n^{1/n} \le c_m^{q/n} \, c_s^{1/n}, \qquad \frac{q}{n} \to \frac1m .$$
$$c_s$$ 只取有限个值（$$s < m$$），故 $$c_s^{1/n} \to 1$$；令 $$n \to \infty$$ 得 $$\limsup_n c_n^{1/n} \le c_m^{1/m}$$。再对 $$m$$ 取下确界：$$\limsup_n c_n^{1/n} \le \inf_m c_m^{1/m} \le \liminf_n c_n^{1/n}$$。三者相等，极限存在且等于下确界。)

第二步，**上界** $$r(a) \le \inf_n \lVert a^n \rVert^{1/n}$$。设 $$\lambda \in \sigma(a)$$。注意恒等式

$$(\lambda e - a)\,(\lambda^{n-1}e + \lambda^{n-2}a + \dots + \lambda a^{n-2} + a^{n-1}) = \lambda^n e - a^n .$$

若 $$\lambda^n e - a^n$$ 可逆，则由 $$(\lambda e - a) \cdot [\text{中间和}] \cdot (\lambda^n e - a^n)^{-1} = e$$ 与 $$(\lambda^n e-a^n)^{-1} \cdot [\text{中间和}] \cdot (\lambda e - a) = e$$，得 $$\lambda e - a$$ 可逆，与 $$\lambda \in \sigma(a)$$ 矛盾。故 $$\lambda^n \in \sigma(a^n)$$，从而 $$\lvert \lambda \rvert^n \le r(a^n) \le \lVert a^n \rVert$$（末一步用命题 3.4 (i)）。开 $$n$$ 次方：$$\lvert \lambda \rvert \le \lVert a^n \rVert^{1/n}$$ 对一切 $$n$$ 成立。对 $$\lambda \in \sigma(a)$$ 取上确界、再对 $$n$$ 取下确界：

$$r(a) \le \inf_{n \ge 1} \lVert a^n \rVert^{1/n} .$$

第三步，**反向不等式** $$\limsup_n \lVert a^n \rVert^{1/n} \le r(a)$$。令
$$f(\lambda) = (e - \lambda a)^{-1} .$$
由命题 3.3 (i)，$$f$$ 在 $$\lvert \lambda \rvert < 1/\lVert a \rVert$$ 上由幂级数给出：
$$f(\lambda) = \sum_{n \ge 0} \lambda^n a^n ,$$
其收敛半径 $$R$$ 满足 $$1/R = \limsup_n \lVert a^n \rVert^{1/n}$$（向量值幂级数的 Cauchy–Hadamard，与纯量情形同样由 $$\lVert \lambda^n a^n\rVert \le \lvert \lambda\rvert^n \lVert a^n\rVert$$ 与「绝对可和蕴含收敛」得到）。

另一方面，只要 $$e - \lambda a$$ 可逆，$$f(\lambda)$$ 就有定义；而 $$e - \lambda a = -\lambda(\lambda^{-1} e - a)$$，当 $$\lambda \ne 0$$ 时它可逆等价于 $$\lambda^{-1} \notin \sigma(a)$$，即 $$\lvert \lambda^{-1} \rvert > r(a)$$，亦即 $$\lvert \lambda \rvert < 1/r(a)$$。所以 $$f$$ 在圆盘 $$\lvert \lambda \rvert < 1/r(a)$$ 上处处有定义；并且由 (3.1) 同样的推理，$$f$$ 在这个圆盘上解析（复可微，逐点用命题 3.3 (ii) 的连续性）。幂级数在解析区域内不会遇到奇点，故收敛半径 $$R \ge 1/r(a)$$，即

$$\limsup_n \lVert a^n \rVert^{1/n} = 1/R \le r(a) .$$

（当 $$r(a) = 0$$ 时把 $$\lvert \lambda \rvert < 1/r(a)$$ 读作「一切 $$\lambda \in \mathbb{C}$$」，$$f$$ 是整函数，故 $$R = \infty$$，不等式同样成立。）

第三步与第二步合用：$$r(a) \le \inf_n \lVert a^n\rVert^{1/n} \le \liminf_n \lVert a^n \rVert^{1/n} \le \limsup_n \lVert a^n \rVert^{1/n} \le r(a)$$。两头相夹，所有不等号都是等号，极限存在且等于下确界与 $$r(a)$$。$$\blacksquare$$

**注** 谱半径公式的要点是：**谱的大小由幂的范数增长率决定，而不是由 $$a$$ 本身的范数决定**。$$\lVert a \rVert$$ 可以远大于 $$r(a)$$：见经典问题 1 的 Volterra 算子，$$\lVert V \rVert > 0$$ 而 $$r(V) = 0$$。

### 3.4 极大理想与 Gelfand–Mazur 定理

要把「交换 Banach 代数」同构到「函数代数」，必须先找到「点」。在函数代数里点是「代数的极大理想」，而这个想法来自代数几何：多项式环 $$\mathbb{C}[z]$$ 的极大理想就是 $$\lbrace f : f(x_0) = 0 \rbrace$$，正好对应复平面上的点 $$x_0$$。

**定义 3.6（理想、极大理想、商代数, ideal / maximal ideal / quotient algebra）** 设 $$\mathcal A$$ 是代数。子空间 $$\mathfrak I \subset \mathcal A$$ 称为**理想 (ideal)**，若 $$a \in \mathfrak I$$、$$b \in \mathcal A$$ 蕴含 $$ab \in \mathfrak I$$ 且 $$ba \in \mathfrak I$$（**双侧理想**）。若 $$\mathfrak I \ne \mathcal A$$，称 $$\mathfrak I$$ **真 (proper)**。若 $$\mathfrak I$$ 真，且不存在真理想 $$\mathfrak J$$ 使 $$\mathfrak I \subsetneq \mathfrak J \subsetneq \mathcal A$$，则称 $$\mathfrak I$$ 为**极大理想 (maximal ideal)**。商线性空间 $$\mathcal A/\mathfrak I$$ 继承乘法 $$(a + \mathfrak I)(b + \mathfrak I) = ab + \mathfrak I$$（定义与代表元选取无关，因为 $$\mathfrak I$$ 是理想），构成商代数。

**命题 3.7（极大理想的性质）** 设 $$\mathcal A$$ 是含单位的**交换** Banach 代数。

(i) 真理想不含可逆元；等价地，若 $$a \in \mathfrak I$$ 可逆则 $$\mathfrak I = \mathcal A$$。

(ii) 每个真理想 $$\mathfrak I$$ 的闭包 $$\overline{\mathfrak I}$$ 仍是真理想。特别地，**极大理想必闭**。

(iii) $$\mathfrak I$$ 是极大理想 $$\iff$$ $$\mathcal A/\mathfrak I$$ 是可除代数（即域）。

**证明.** (i) 若 $$a \in \mathfrak I$$ 可逆，则 $$e = a^{-1}a \in \mathfrak I$$（理想吸收乘法），于是任意 $$b = be \in \mathfrak I$$，故 $$\mathfrak I = \mathcal A$$。反过来，若 $$e \in \mathfrak I$$ 则 $$\mathfrak I = \mathcal A$$，所以真理想不含 $$e$$。

(ii) 先看 $$\overline{\mathfrak I}$$ 是理想：若 $$x_n \to x$$、$$x_n \in \mathfrak I$$、$$b \in \mathcal A$$，则 $$bx_n \to bx$$ 且 $$bx_n \in \mathfrak I$$，故 $$bx \in \overline{\mathfrak I}$$；同理 $$xb \in \overline{\mathfrak I}$$。次证 $$\overline{\mathfrak I}$$ 真：若 $$e \in \overline{\mathfrak I}$$，则存在 $$y \in \mathfrak I$$ 使 $$\lVert e - y \rVert < 1$$。由命题 3.3 (i)，$$y = e - (e - y)$$ 可逆，与 (i) 及 $$\mathfrak I$$ 真矛盾。故 $$e \notin \overline{\mathfrak I}$$，$$\overline{\mathfrak I}$$ 真。

(iii) 设 $$\mathfrak I$$ 极大。在 $$\mathcal A/\mathfrak I$$ 中取非零元 $$a + \mathfrak I$$。令 $$\mathfrak J = \lbrace ac + i : c \in \mathcal A,\ i \in \mathfrak I \rbrace$$（即由 $$a$$ 与 $$\mathfrak I$$ 生成的理想）。因 $$a \notin \mathfrak I$$，$$\mathfrak I \subsetneq \mathfrak J$$；由极大性 $$\mathfrak J = \mathcal A$$，故 $$e = ac + i$$ 对某 $$c \in \mathcal A$$、$$i \in \mathfrak I$$，即 $$(a + \mathfrak I)(c + \mathfrak I) = e + \mathfrak I$$。交换性使左乘右乘一致，故 $$a + \mathfrak I$$ 可逆。即 $$\mathcal A/\mathfrak I$$ 的每个非零元可逆。

反过来，设 $$\mathcal A/\mathfrak I$$ 可除，$$\mathfrak J \supsetneq \mathfrak I$$，取 $$a \in \mathfrak J \setminus \mathfrak I$$。在 $$\mathcal A/\mathfrak I$$ 中 $$a + \mathfrak I \ne 0$$，故有逆 $$c + \mathfrak I$$，即 $$ac - e \in \mathfrak I \subset \mathfrak J$$。又 $$a \in \mathfrak J$$ 给出 $$ac \in \mathfrak J$$，两式相减得 $$e \in \mathfrak J$$，故 $$\mathfrak J = \mathcal A$$。所以 $$\mathfrak I$$ 极大。$$\blacksquare$$

命题 3.7 已经把「极大理想」与「可除代数」挂上了钩；要让这条挂钩真正给出「点」，还差最后一环：可除的 Banach 代数到底长什么样？下面这条定理说，答案出奇地简单——只有 $$\mathbb C$$ 自己。

**定理 3.8（Gelfand–Mazur）** 设 $$\mathcal A$$ 是**可除的** Banach 代数（含单位、$$\lVert e \rVert = 1$$）。则 $$\mathcal A$$ 等距同构于 $$\mathbb{C}$$：具体地，$$\mathcal A = \mathbb{C} e$$，且映射 $$\lambda \mapsto \lambda e$$ 是等距同构。

**证明思路.** 任取 $$a \in \mathcal A$$。谱非空（命题 3.4 (ii)）给出某个 $$\lambda$$ 使 $$\lambda e - a$$ 不可逆；可除性把「不可逆」升级为「等于零」，于是 $$a$$ 必须是 $$e$$ 的数量倍。

**证明.** 设 $$a \in \mathcal A$$。由命题 3.4 (ii)，$$\sigma(a) \ne \varnothing$$，取 $$\lambda \in \sigma(a)$$。按定义 $$\lambda e - a \notin G(\mathcal A)$$，即 $$\lambda e - a$$ 不可逆。若 $$\lambda e - a \ne 0$$，则由可除性它是可逆的，矛盾。故 $$\lambda e - a = 0$$，即 $$a = \lambda e$$。

于是每个 $$a$$ 都是 $$e$$ 的数量倍，$$\mathcal A = \mathbb{C}e$$。映射 $$\lambda \mapsto \lambda e$$ 显然是代数同构；它保范，因为 $$\lVert \lambda e \rVert = \lvert \lambda \rvert \lVert e \rVert = \lvert \lambda \rvert$$（用了 $$\lVert e \rVert = 1$$）。故是等距同构。$$\blacksquare$$

Gelfand–Mazur 的分量在于：它说**除了 $$\mathbb{C}$$ 之外没有别的 Banach 除环**。把命题 3.7 (iii) 与它拼起来，就得到：交换 Banach 代数的极大理想 $$\mathfrak I$$ 使 $$\mathcal A/\mathfrak I$$ 既可除又完备，故 $$\mathcal A/\mathfrak I \cong \mathbb{C}$$。每一个极大理想因此给出一个到 $$\mathbb{C}$$ 的投影——那就是我们要找的「点」。

### 3.5 特征与极大理想空间

**定义 3.9（特征与极大理想空间, character / maximal ideal space）** 设 $$\mathcal A$$ 是含单位的交换 Banach 代数。称非零线性泛函 $$\varphi : \mathcal A \to \mathbb{C}$$ 为 $$\mathcal A$$ 的**特征 (character)**，若
$$\varphi(ab) = \varphi(a)\varphi(b) \quad \text{对一切 } a, b \in \mathcal A .$$
全体特征记为 $$\Delta(\mathcal A)$$，称为 $$\mathcal A$$ 的**极大理想空间 (maximal ideal space)**。（由 $$\varphi \ne 0$$ 与 $$\varphi(e) = \varphi(e)^2$$ 可推出 $$\varphi(e) = 1$$：若 $$\varphi(e)=0$$ 则 $$\varphi(a) = \varphi(ae) = \varphi(a)\varphi(e) = 0$$ 对一切 $$a$$，与 $$\varphi \ne 0$$ 矛盾。）

**定理 3.10（特征 ↔ 极大理想）** 设 $$\mathcal A$$ 是含单位的交换 Banach 代数。

(i) 映射 $$\varphi \mapsto \ker \varphi$$ 是 $$\Delta(\mathcal A)$$ 到 $$\mathcal A$$ 的极大理想全体之间的一一对应，其逆为 $$\mathfrak I \mapsto (\mathcal A \twoheadrightarrow \mathcal A/\mathfrak I \xrightarrow{\ \cong\ } \mathbb{C})$$。

(ii) 每个 $$\varphi \in \Delta(\mathcal A)$$ 是连续线性泛函，且 $$\lVert \varphi \rVert = 1$$。

(iii) 对每个 $$a \in \mathcal A$$ 与每个 $$\varphi \in \Delta(\mathcal A)$$，$$\varphi(a) \in \sigma(a)$$。特别地 $$\lvert \varphi(a) \rvert \le r(a) \le \lVert a \rVert$$。

**证明.** (i) 设 $$\varphi \in \Delta(\mathcal A)$$。$$\ker\varphi$$ 是理想（若 $$\varphi(a)=0$$，则 $$\varphi(ab) = \varphi(a)\varphi(b) = 0$$）。它真：否则 $$\varphi \equiv 0$$。商映射给出代数同构 $$\mathcal A/\ker\varphi \cong \varphi(\mathcal A)$$；$$\varphi(\mathcal A)$$ 是 $$\mathbb{C}$$ 的非零子空间（含 $$\varphi(e)=1$$），故就是 $$\mathbb{C}$$，于是 $$\mathcal A/\ker\varphi \cong \mathbb{C}$$ 是可除代数，由命题 3.7 (iii) $$\ker\varphi$$ 极大。这证明 $$\varphi \mapsto \ker\varphi$$ **单射**（因为 $$\ker\varphi$$ 极大，且 $$\mathcal A/\ker\varphi \cong \mathbb{C}$$ 中的同构唯一，反推 $$\varphi$$ 由核决定：$$\varphi(a)$$ 就是 $$a + \ker\varphi$$ 在 $$\mathbb{C}$$ 中的像）。

**满射**：设 $$\mathfrak I$$ 极大。由命题 3.7 (ii) $$\mathfrak I$$ 闭，故商空间 $$\mathcal A/\mathfrak I$$ 以商范数 $$\lVert a + \mathfrak I \rVert = \inf\lbrace \lVert a - i\rVert : i \in \mathfrak I\rbrace$$ 成为 Banach 空间（完备性是「商掉闭子空间仍完备」，见第 36 章）。乘积不等式对商范数同样成立，所以 $$\mathcal A/\mathfrak I$$ 是 Banach 代数；由命题 3.7 (iii) 它可除；由定理 3.8 存在等距同构 $$\psi : \mathcal A/\mathfrak I \to \mathbb{C}$$；令 $$\varphi = \psi \circ \pi$$（$$\pi$$ 是商映射），则 $$\varphi$$ 是非零乘法线性泛函且 $$\ker\varphi = \mathfrak I$$。故 $$\mathfrak I$$ 来自某个特征。

(ii) 由 (iii)（下面即将证明）与 $$\varphi(e)=1$$：$$1 = \lvert \varphi(e) \rvert \le \lVert e \rVert = 1$$ 给出 $$\lVert \varphi \rVert \ge 1$$；而 $$\lvert \varphi(a) \rvert \le r(a) \le \lVert a \rVert$$ 给出 $$\lVert \varphi \rVert \le 1$$。故 $$\lVert \varphi \rVert = 1$$。

(iii) 设 $$a \in \mathcal A$$，$$\varphi \in \Delta(\mathcal A)$$。$$b = \varphi(a)e - a \in \ker\varphi$$，而 $$\ker\varphi$$ 是**真**理想（$$\varphi(e) = 1 \ne 0$$），由命题 3.7 (i) 它不含可逆元，故 $$b$$ 不可逆，即 $$\varphi(a) \in \sigma(a)$$。$$\blacksquare$$

### 3.6 Gelfand 拓扑与 Gelfand 表示定理

有了「点」的位置：$$\Delta(\mathcal A)$$ 由定理 3.10 (ii) 含于 $$\mathcal A^*$$ 的闭单位球面。把它装上从 $$\mathcal A^*$$ 继承的弱\*拓扑，它就成了紧空间——这正是第 30 章「弱\*拓扑下单位球紧」（Banach–Alaoglu）的又一次应用。

**定义 3.11（Gelfand 拓扑与 Gelfand 表示, Gelfand topology / Gelfand transform）** 在 $$\Delta(\mathcal A) \subset \mathcal A^*$$ 上取**弱\*拓扑**（使一切赋值 $$\varphi \mapsto \varphi(a)$$（$$a \in \mathcal A$$）连续的最粗拓扑，见第 30 章的弱拓扑一节）作为子空间拓扑，称 **Gelfand 拓扑 (Gelfand topology)**。对 $$a \in \mathcal A$$，定义
$$\hat a : \Delta(\mathcal A) \to \mathbb{C}, \qquad \hat a(\varphi) = \varphi(a),$$
称为 $$a$$ 的 **Gelfand 表示 (Gelfand transform)**；$$a \mapsto \hat a$$ 记为 $$\Gamma = \Gamma_{\mathcal A}$$。$$\hat a$$ 的**根 (radical)** 是 $$\mathrm{rad}(\mathcal A) = \bigcap_{\varphi \in \Delta}\ker\varphi$$。

**定理 3.12（Gelfand 表示定理, Gelfand representation theorem）** 设 $$\mathcal A$$ 是含单位的交换 Banach 代数。

(i) $$\Delta(\mathcal A)$$ 在 Gelfand 拓扑下是**紧 Hausdorff 空间**。

(ii) 对每个 $$a \in \mathcal A$$，$$\hat a \in C(\Delta(\mathcal A))$$，且 $$\lVert \hat a \rVert_\infty \le \lVert a \rVert$$。

(iii) $$\Gamma : \mathcal A \to C(\Delta(\mathcal A))$$ 是含单位的代数同态的收缩（$$\hat e = \mathbf 1$$，$$\widehat{ab} = \hat a \hat b$$，$$\lVert\Gamma\rVert \le 1$$）。

(iv) **（谱 = 值域）** 对每个 $$a \in \mathcal A$$，
$$\sigma(a) = \lbrace \hat a(\varphi) : \varphi \in \Delta(\mathcal A) \rbrace = \Gamma(a)(\Delta(\mathcal A)) ,$$
并且 $$r(a) = \lVert \hat a \rVert_\infty$$。特别地 $$\Gamma$$ 的核正是根：$$\Gamma(a) = 0 \iff \hat a \equiv 0 \iff r(a) = 0$$。

**证明.** (i) 由定理 3.10 (ii)，$$\Delta(\mathcal A) \subset B$$，$$B = \lbrace \varphi \in \mathcal A^* : \lVert \varphi \rVert \le 1\rbrace$$。由 Banach–Alaoglu（见第 30 章的弱拓扑一节），$$B$$ 在弱\*拓扑下紧；Hausdorff 空间的子空间 Hausdorff。故只需证 $$\Delta(\mathcal A)$$ 在 $$B$$ 中弱\*闭。

把它写成弱\*闭集的交。弱\*拓扑下，「$$\varphi \mapsto \varphi(a)$$」连续，故对固定的 $$a, b \in \mathcal A$$，
$$F_{a,b} = \lbrace \varphi \in B : \varphi(ab) - \varphi(a)\varphi(b) = 0\rbrace$$
是闭集：因为乘法在 $$\mathbb{C}$$ 中连续，$$(\varphi(a), \varphi(b)) \mapsto \varphi(a)\varphi(b)$$ 连续，$$\varphi \mapsto \varphi(ab) - \varphi(a)\varphi(b)$$ 连续，取零点集。同理 $$F_e = \lbrace \varphi \in B : \varphi(e) = 1\rbrace$$ 闭。于是
$$\Delta(\mathcal A) = \Big( \bigcap_{a,b \in \mathcal A} F_{a,b} \Big) \cap F_e$$
是闭集（$$\varphi \ne 0$$ 由 $$\varphi(e)=1$$ 自动成立）。紧空间的闭子集紧。

(ii) $$\hat a = \varphi \mapsto \varphi(a)$$ 连续，因为弱\*拓扑的定义就是让这些映射连续。$$\lvert \hat a(\varphi) \rvert = \lvert \varphi(a) \rvert \le \lVert \varphi \rVert \lVert a \rVert = \lVert a \rVert$$（定理 3.10 (ii)），故 $$\lVert \hat a \rVert_\infty \le \lVert a \rVert$$。

(iii) $$\hat e(\varphi) = \varphi(e) = 1$$，故 $$\hat e = \mathbf 1$$。$$\widehat{ab}(\varphi) = \varphi(ab) = \varphi(a)\varphi(b) = \hat a(\varphi)\hat b(\varphi)$$，故 $$\widehat{ab} = \hat a\hat b$$。加上线性性（$$\varphi$$ 是线性的），$$\Gamma$$ 是含单位同态；收缩性即 (ii)。

(iv) 先证 $$\supseteq$$：定理 3.10 (iii) 说 $$\varphi(a) = \hat a(\varphi) \in \sigma(a)$$。

再证 $$\subseteq$$：设 $$\lambda \in \sigma(a)$$，即 $$\lambda e - a$$ 不可逆。由命题 3.7 (i)，由 $$\lambda e - a$$ 生成的理想
$$\mathfrak J = \lbrace (\lambda e - a)c : c \in \mathcal A \rbrace$$
是真理想（它不含 $$e$$：否则 $$\lambda e - a$$ 可逆）。用 Zorn 引理（见 3.13 的注）把 $$\mathfrak J$$ 扩成极大理想 $$\mathfrak I \supset \mathfrak J$$。由定理 3.10 (i)，$$\mathfrak I = \ker\varphi$$ 对某 $$\varphi \in \Delta(\mathcal A)$$。于是 $$\lambda e - a \in \ker\varphi$$，即 $$\lambda - \varphi(a) = 0$$，故 $$\lambda = \hat a(\varphi) \in \Gamma(a)(\Delta)$$。

最后，$$r(a) = \sup_{\lambda \in \sigma(a)}\lvert\lambda\rvert = \sup_{\varphi}\lvert \hat a(\varphi)\rvert = \lVert \hat a\rVert_\infty$$（用命题 3.4 (i) 保证上确界被取到，因为 $$\Delta$$ 紧、$$\hat a$$ 连续）。$$\Gamma(a) = 0 \iff \varphi(a) = 0 \ \forall \varphi \iff \sigma(a) = \lbrace 0\rbrace \iff r(a) = 0$$，这也正是 $$\bigcap_\varphi \ker\varphi$$。$$\blacksquare$$

**注 3.13（Zorn 引理的使用）** 上面「把真理想扩成极大理想」用了 Zorn 引理：设 $$\mathcal F$$ 是所有包含 $$\mathfrak J$$ 的真理想，按包含关系成偏序集。任一链 $$\lbrace \mathfrak I_\alpha\rbrace$$ 的并 $$\bigcup_\alpha \mathfrak I_\alpha$$ 仍是理想（理想是子空间，链的并仍是子空间；吸收性逐元素验证），且仍真（若 $$e$$ 在其中某个 $$\mathfrak I_\alpha$$，那个 $$\mathfrak I_\alpha$$ 就不真）。故每个链有上界，Zorn 给出极大元，正是包含 $$\mathfrak J$$ 的极大理想。$$\Delta(\mathcal A)$$ 不空也就此有了保证。

**定理 3.12 的「形状」正是入口题 (c) 的答案**：$$K = \Delta(\mathcal A)$$，$$\Gamma$$ 就是 Gelfand 表示，$$\sigma(a) = \Gamma(a)(K)$$。请读者回头核对入口题 (a)：在 $$C(X)$$ 中，$$\Gamma$$ 恰好把 $$f$$ 送回 $$f$$ 自己（经典问题 3 会证这件事），于是 $$\sigma(f) = f(X)$$ 就是入口题 (a) 的结论。

### 3.7 对合与 C\* 代数

到目前为止我们只用了代数运算与范数。要处理「实值」与「共轭」，必须把复共轭这个操作也抽象进去——这就是**对合**。它让 Banach 代数理论终于能回答第 36 章的那个问题。

**定义 3.14（对合代数, involutive algebra）** 设 $$\mathcal A$$ 是复代数。映射 $$* : \mathcal A \to \mathcal A$$，$$a \mapsto a^*$$ 称为**对合 (involution)**，若对一切 $$a, b \in \mathcal A$$、$$\lambda \in \mathbb{C}$$：

$$(a+b)^* = a^* + b^*, \quad (\lambda a)^* = \bar\lambda\, a^*, \quad (ab)^* = b^* a^*, \quad (a^*)^* = a .$$

也就是说 $$*$$ 是周期 2 的**共轭线性反自同构 (conjugate-linear anti-automorphism)**（反字指 $$(ab)^* = b^*a^*$$ 中次序颠倒）。带对合的代数记为 $$\mathcal A(*)$$。满足 $$a^* = a$$ 的元素称**自伴元 (self-adjoint)** 或 **Hermite 元 (Hermitian)**。

三个例子：$$C(X)$$ 上取 $$f^* = \bar f$$（复共轭）；$$\mathcal B(H)$$ 上取伴随算子 $$T^*$$（第 32 章定义的伴随）；$$\ell^1(\mathbb{Z})$$ 上取 $$(a^*)_n = \overline{a_{-n}}$$。三者都使「自伴」这个抽象定义落回具体的「实值函数」「自伴算子」「实系数序列」。

普通复数总能唯一分成实部加 $$i$$ 乘虚部；对合就是为了让「实部/虚部」这套语言在任意代数里都能重讲一遍——「自伴元」扮演「实数」的角色。下面先确认这件事真的总能做到、而且分法唯一，后面 Arens 引理才有立足点。

**命题 3.15（唯一的自伴分解）** 设 $$\mathcal A(*)$$ 是对合代数。每个 $$a \in \mathcal A$$ 有**唯一**的分解

$$a = u + iv, \qquad u^* = u, \quad v^* = v, \qquad u = \frac{a + a^*}{2}, \quad v = \frac{a - a^*}{2i} .$$

**证明.** 先验证 $$u, v$$ 自伴：
$$u^* = \Big(\frac{a+a^*}{2}\Big)^* = \frac{a^* + a^{**}}{2} = \frac{a^*+a}{2} = u, \qquad v^* = \Big(\frac{a-a^*}{2i}\Big)^* = \frac{a^* - a}{\overline{2i}} = \frac{a^*-a}{-2i} = \frac{a-a^*}{2i} = v .$$
再验证和：$$u + iv = \frac{a+a^*}{2} + i\,\frac{a-a^*}{2i} = \frac{a+a^*}{2} + \frac{a-a^*}{2} = a$$。

**唯一性**：设 $$a = u + iv = u' + iv'$$，其中 $$u,v,u',v'$$ 都自伴。则 $$w = u - u' = i(v' - v)$$。左端 $$w^* = u - u' = w$$（自伴）；右端 $$w^* = \overline{i}\,(v' - v)^* = -i(v'-v) = -(i(v'-v)) = -w$$。故 $$w = -w$$，即 $$2w = 0$$，$$w = 0$$；于是 $$u = u'$$，同理 $$v = v'$$。$$\blacksquare$$

**定义 3.16（C\* 代数与 C\* 恒等式, C\*-algebra / C\*-identity）** 设 $$\mathcal A$$ 是带对合的 Banach 代数。若对一切 $$a \in \mathcal A$$ 满足 **C\* 恒等式**
$$\lVert a^* a \rVert = \lVert a \rVert^2,$$
则称 $$\mathcal A$$ 为 **C\* 代数 (C\*-algebra)**。（称为 C\* 是因为历史上写成 $$C^*$$，「\*」代表对合。）

C\* 恒等式是本理论的核心公理：它把**范数**（分析数据）与**对合**（代数数据）焊在一起，一头拴住谱，一头拴住大小。

**命题 3.17（C\* 恒等式的直接推论）** 设 $$\mathcal A$$ 是 C\* 代数。

(i) $$\lVert a^* \rVert = \lVert a \rVert$$（对合保范）。

(ii) 若 $$a$$ 自伴，则 $$\lVert a^2 \rVert = \lVert a \rVert^2$$。

(iii) 若 $$a$$ 正规（$$a^*a = aa^*$$），则 $$r(a) = \lVert a \rVert$$。

**证明.** (i) $$\lVert a \rVert^2 = \lVert a^*a \rVert \le \lVert a^* \rVert \lVert a \rVert$$（次乘性）。若 $$\lVert a \rVert \ne 0$$，两边除以 $$\lVert a \rVert$$ 得 $$\lVert a \rVert \le \lVert a^* \rVert$$；若 $$\lVert a \rVert = 0$$ 则 $$a = 0$$，结论也成立。把此不等式用于 $$a^*$$（注意 $$a^{**} = a$$）：$$\lVert a^* \rVert \le \lVert a^{**} \rVert = \lVert a \rVert$$。两向合并即得。

(ii) $$a = a^*$$ 时 $$a^*a = a^2$$，C\* 恒等式直接给出 $$\lVert a^2 \rVert = \lVert a \rVert^2$$。

(iii) 先证一条比 (ii) 更一般的引理：**若 $$b$$ 正规（不必自伴），则 $$\lVert b^2 \rVert = \lVert b \rVert^2$$。**（这一步不能直接套用 (ii)：(ii) 的前提是 $$b$$ 自伴，而正规只保证 $$b^*b = bb^*$$，两者并不是同一件事——比如把 $$a$$ 取成一个「旋转 + 伸缩」型的正规矩阵，$$a^* \ne a$$ 但 $$a^*a = aa^*$$，此时 (ii) 根本不能直接引用。正确的路线是绕道走 $$b^*b$$，因为 $$b^*b$$ **总是自伴的**（$$(b^*b)^* = b^*b^{**} = b^*b$$），不管 $$b$$ 是否自伴。）由 C\* 恒等式与正规性，
$$\lVert b^2 \rVert^2 = \lVert (b^2)^*b^2 \rVert = \lVert (b^*)^2b^2 \rVert = \lVert b^*(b^*b)b \rVert = \lVert b^*(bb^*)b \rVert = \lVert (b^*b)(b^*b) \rVert = \lVert (b^*b)^2 \rVert ,$$
中间把 $$b^*b$$ 换成 $$bb^*$$ 用的正是正规性 $$b^*b = bb^*$$，换过之后四个因子 $$b^*, b, b^*, b$$ 重新配对成 $$(b^*b)(b^*b)$$。现在 $$b^*b$$ 自伴，可以合法引用 (ii)：$$\lVert (b^*b)^2 \rVert \overset{\text{(ii)}}{=} \lVert b^*b \rVert^2$$；再由 C\* 恒等式 $$\lVert b^*b \rVert = \lVert b \rVert^2$$（这一步对任意 $$b$$ 成立，不需要正规性），得
$$\lVert b^2 \rVert^2 = \lVert b^*b \rVert^2 = \big(\lVert b \rVert^2\big)^2 = \lVert b \rVert^4 ,$$
开平方即 $$\lVert b^2 \rVert = \lVert b \rVert^2$$，引理得证。

现在用这条引理对 $$n$$ 归纳证明 $$\lVert a^{2^n} \rVert = \lVert a \rVert^{2^n}$$。$$n=0$$ 平凡。设对 $$n$$ 成立。需要 $$a^{2^n}$$ 正规：由 $$\lVert \cdot \rVert$$ 与对合相容，可验证 $$(a^{2^n})^* a^{2^n} = (a^* a)^{2^n} = a^{2^n}(a^{2^n})^*$$（把 $$a^*a = aa^*$$ 反复用于把 $$*$$ 移过去；等式两端展开后是同一串因子在交换律 $$a^*a = aa^*$$ 下的重排）。于是 $$a^{2^n}$$ 正规（但一般不自伴），把上面的引理用在 $$b = a^{2^n}$$ 上（**不是**直接用 (ii)，因为 $$a^{2^n}$$ 只保证正规），得
$$\lVert a^{2^{n+1}} \rVert = \lVert (a^{2^n})^2 \rVert \overset{\text{引理}}{=} \lVert a^{2^n} \rVert^2 = \lVert a \rVert^{2^n \cdot 2} .$$
由谱半径公式（定理 3.5）取子列 $$n = 2^k$$：
$$r(a) = \lim_{k\to\infty} \lVert a^{2^k} \rVert^{1/2^k} = \lim_{k\to\infty} \lVert a \rVert^{2^k/2^k} = \lVert a \rVert . \qquad\blacksquare$$

### 3.8 Arens 引理：自伴元谱为实

现在正式补上第 36 章留下的洞。

**定理 3.18（Arens 引理, Arens' lemma）** 设 $$\mathcal A$$ 是含单位的交换 **C\* 代数**，$$a \in \mathcal A$$ 自伴（$$a^* = a$$）。则 $$\hat a : \Delta(\mathcal A) \to \mathbb{C}$$ 是**实值函数**；等价地，$$\varphi(a) \in \mathbb{R}$$ 对一切 $$\varphi \in \Delta(\mathcal A)$$。

**证明思路.** 对每个固定特征 $$\varphi$$，把 $$\varphi(a)$$ 写成 $$\alpha + i\beta$$（$$\alpha, \beta \in \mathbb{R}$$），并拿 $$b = a + ite$$（$$t \in \mathbb{R}$$）做实验。$$\lvert \varphi(b) \rvert = \lvert \alpha + i(\beta + t)\rvert$$ 可以被 $$\lVert b \rVert$$ 压住（$$\varphi$$ 是范数为 $$1$$ 的连续线性泛函），再由 **C\* 恒等式** $$\lVert b \rVert^2 = \lVert b^*b \rVert$$ 把 $$\lVert b \rVert$$ 换成可以直接计算的 $$\lVert b^*b \rVert$$，而 $$b^*b = a^2 + t^2e$$ 的范数被 $$\lVert a\rVert^2 + t^2$$ 控制。两边都出现 $$t^2$$，相消后剩下一个对一切 $$t$$ 恒成立的**一次**不等式——一次函数有上界只能斜率为零。

（这里有一个**顺序问题**必须点明：证明中**不能**去算 $$\varphi(b^*b) = \lvert \varphi(b) \rvert^2$$。那个等式等价于 $$\varphi(b^*) = \overline{\varphi(b)}$$，而后者正是本定理要证的结论——把它当初始条件用就是循环论证，对一般 Banach \*-代数并不成立，见下面的注 3.18。正确的路线是「先 $$\lvert \varphi(\cdot) \rvert \le \lVert \cdot \rVert$$，再用 C\* 恒等式换范数」。）

**证明.** 固定 $$\varphi \in \Delta(\mathcal A)$$，记 $$\varphi(a) = \alpha + i\beta$$，$$\alpha, \beta \in \mathbb{R}$$。对 $$t \in \mathbb{R}$$ 令 $$b = a + ite$$。因为 $$a^* = a$$、$$e^* = e$$、$$\bar{it} = -it$$：

$$b^* = a^* + \overline{it}\,e = a - it e, \qquad b^*b = (a - ite)(a + ite) = a^2 + ita - ita + t^2 e = a^2 + t^2 e .$$

于是

$$\lVert b^*b \rVert = \lVert a^2 + t^2 e \rVert \le \lVert a^2 \rVert + \lVert t^2 e \rVert = \lVert a \rVert^2 + t^2 , \tag{3.2}$$

末一步用了 $$a$$ 自伴时的 $$\lVert a^2 \rVert = \lVert a \rVert^2$$（命题 3.17 (ii)）与 $$\lVert e \rVert = 1$$。

另一方面，$$\varphi(b) = \varphi(a) + it\varphi(e) = \alpha + i(\beta + t)$$，故

$$\lvert \varphi(b) \rvert^2 = \alpha^2 + (\beta + t)^2 . \tag{3.3}$$

由定理 3.10 (ii)，$$\lVert \varphi \rVert = 1$$，故 $$\lvert \varphi(c) \rvert \le \lVert c \rVert$$ 对一切 $$c \in \mathcal A$$。取 $$c = b$$，再用 **C\* 恒等式** $$\lVert b \rVert^2 = \lVert b^*b \rVert$$（注意 $$b^*b$$ 自动自伴）把 $$\lVert b \rVert$$ 换成 (3.2) 控制得住的量：

$$\alpha^2 + (\beta + t)^2 = \lvert \varphi(b) \rvert^2 \le \lVert b \rVert^2 = \lVert b^*b \rVert \le \lVert a \rVert^2 + t^2 .$$

展开 $$(\beta+t)^2 = \beta^2 + 2\beta t + t^2$$，两边的 $$t^2$$ 相消：

$$\alpha^2 + \beta^2 + 2\beta t \le \lVert a \rVert^2 \qquad \text{对一切 } t \in \mathbb{R} .$$

若 $$\beta \ne 0$$，让 $$t \to +\infty$$（当 $$\beta>0$$）或 $$t \to -\infty$$（当 $$\beta<0$$）可使左端任意大，与右端是常数矛盾。故 $$\beta = 0$$，即 $$\varphi(a) = \alpha \in \mathbb{R}$$。对一切 $$\varphi$$ 成立，故 $$\hat a$$ 实值。$$\blacksquare$$

**注 3.18（为什么假设不能减弱：Banach \*-代数上 Arens 引理不成立）** 定理 3.18 的假设「C\* 代数」**不能**放宽成「带对合的交换 Banach 代数」，哪怕对合还是保范的。反例只需要两个点。

取 $$\mathcal A_0 = \mathbb{C}^2$$，加法与乘法逐分量（$$(z_1,w_1)(z_2,w_2) = (z_1z_2,\ w_1w_2)$$），范数取上确界范数
$$\lVert (z,w) \rVert = \max(\lvert z \rvert,\ \lvert w \rvert),$$
对合取
$$(z,w)^* = (\bar w,\ \bar z) .$$
逐条验证它满足**除 C\* 恒等式之外**的全部要求：

1. **含单位的交换 Banach 代数**：$$e = (1,1)$$，$$\lVert e \rVert = 1$$；次乘性 $$\lVert xy \rVert = \max(\lvert z_1z_2 \rvert, \lvert w_1w_2 \rvert) \le \lVert x \rVert \lVert y \rVert$$；$$\mathbb{C}^2$$ 在 $$\max$$ 范数下完备。
2. **对合合法**：$$*$$ 共轭线性（$$\overline{\lambda z} = \bar\lambda \bar z$$ 逐分量成立）、$$(x^*)^* = x$$，且次序确实颠倒：
$$(xy)^* = (\overline{w_1w_2},\ \overline{z_1z_2}) = (\bar w_2,\bar z_2)(\bar w_1,\bar z_1) = y^*x^*,$$
与定义 3.14 相符。
3. **对合保范**：$$\lVert x^* \rVert = \max(\lvert \bar w \rvert, \lvert \bar z \rvert) = \lVert x \rVert$$。
4. **不是 C\* 代数**：取 $$x = (1,0)$$，则 $$x^* = (0,1)$$，逐分量相乘得 $$x^*x = (0,0)$$，于是
$$\lVert x^*x \rVert = 0 \ne 1 = \lVert x \rVert^2 .$$

在这个 $$\mathcal A_0$$ 上，定理 3.18 的结论**不成立**。取
$$a = (1+i,\ 1-i), \qquad a^* = (\overline{1-i},\ \overline{1+i}) = (1+i,\ 1-i) = a,$$
即 $$a$$ 自伴。特征 $$\varphi_1(z,w) = z$$（乘法性显然，$$\varphi_1(e) = 1 \ne 0$$）给出
$$\varphi_1(a) = 1 + i \notin \mathbb{R},$$
于是 $$\hat a$$ 不是实值函数。由定理 3.12 (iv)（它只用到交换性，在这里仍然适用）这等价地说
$$\sigma_{\mathcal A_0}(a) = \lbrace \varphi_1(a),\ \varphi_2(a) \rbrace = \lbrace 1+i,\ 1-i \rbrace \not\subset \mathbb{R},$$
其中 $$\varphi_2(z,w) = w$$ 是另一个特征，$$\Delta(\mathcal A_0) = \lbrace \varphi_1, \varphi_2 \rbrace$$。自伴元的谱不落在实轴上。

证明究竟卡在哪一步？回到那个 $$\varphi(b^*) = \overline{\varphi(b)}$$。在 $$\mathcal A_0$$ 里取 $$\varphi = \varphi_1$$、$$b = a + ite = (1+i+it,\ 1-i+it)$$，则 $$b^* = (1+i-it,\ 1-i-it)$$，于是
$$\varphi_1(b^*) = 1 + i - it \ne 1 - i - it = \overline{\varphi_1(b)} ,$$
而
$$\lvert \varphi_1(b) \rvert^2 = \lvert 1+i+it \rvert^2 = (1+t)^2 + 1, \qquad \lvert \varphi_1(b^*b) \rvert = \lvert \varphi_1(b^*)\varphi_1(b) \rvert = \lvert (1+i)^2 + t^2 \rvert = \sqrt{t^4 + 4} .$$
两者只在 $$t = 0$$ 时相等，所以恒等式 $$\lvert \varphi(b) \rvert^2 = \varphi(b^*b)$$ 在 $$\mathcal A_0$$ 上失效——原证明把它当成初始条件，这一步正是循环论证。

修正后的证明只多用了一处：$$\lVert b \rVert^2 = \lVert b^*b \rVert$$，即「对合与范数相配」中 C\* 代数独有的那一半。在 $$\mathcal A_0$$ 里这一条失效（$$t = 1$$ 时 $$\lVert b \rVert^2 = 5$$ 而 $$\lVert b^*b \rVert = \sqrt5$$），于是 $$\lVert b \rVert^2 \le \lVert a \rVert^2 + t^2$$ 不再成立，整个估计崩塌。**这条注的意义不小于定理本身**：读者天然会以为「只要有对合就够」，而 $$\mathcal A_0$$ 除 C\* 恒等式外样样满足。

Arens 引理只说了自伴元的 Gelfand 表示是实值函数；下面把它升级成「对合本身翻译成复共轭」，再进一步把 §3.6 的收缩 $$\Gamma$$ 升级成不折不扣的等距同构——这才是「$$\mathcal A$$ 与 $$C(\Delta(\mathcal A))$$ 是同一个东西」的完整版本。

**定理 3.19（交换 C\* 代数的 Gelfand–Naimark）** 设 $$\mathcal A$$ 是交换 C\* 代数。

(i) 对一切 $$a \in \mathcal A$$，$$\widehat{a^*} = \overline{\hat a}$$（逐点复共轭），即 $$\varphi(a^*) = \overline{\varphi(a)}$$。

(ii) $$\Gamma : \mathcal A \to C(\Delta(\mathcal A))$$ 是**等距 \*-同构**（等距、保乘法、保单位、保对合）；若 $$\mathcal A$$ 含单位，$$\Gamma$$ 满射，于是 $$\mathcal A$$ 与某个紧 Hausdorff 空间上的连续函数代数**完全一样**（作为 C\* 代数）。

**证明思路.** (i) 由命题 3.15 把 $$a$$ 拆成 $$u + iv$$，$$u, v$$ 自伴；对 $$u, v$$ 用 Arens 引理。（这正是 Arens 引理「解释对合」的地方。）(ii) 等距性来自 C\* 恒等式与谱半径公式：$$\lVert a \rVert^2 = \lVert a^*a \rVert = r(a^*a) = \lVert \widehat{a^*a}\rVert_\infty = \lVert \lvert \hat a\rvert^2 \rVert_\infty = \lVert \hat a \rVert_\infty^2$$。满射性用 Stone–Weierstrass：像是分离点、处处非零的闭 \*-子代数。

**证明.** (i) 由命题 3.15，$$a = u + iv$$，$$u^* = u$$、$$v^* = v$$，故 $$a^* = u - iv$$。由 Arens 引理（定理 3.18），$$\hat u, \hat v$$ 实值。于是对每个 $$\varphi$$，
$$\varphi(a^*) = \varphi(u - iv) = \hat u(\varphi) - i\hat v(\varphi) = \overline{\hat u(\varphi) + i\hat v(\varphi)} = \overline{\varphi(u+iv)} = \overline{\varphi(a)} ,$$
因为实数的共轭是自身。

(ii) 先算等距性。$$\lVert a \rVert^2 = \lVert a^*a \rVert$$（C\* 恒等式）$$= r(a^*a)$$（命题 3.17 (iii)：$$a^*a$$ 自伴因而正规）$$= \lVert \widehat{a^*a} \rVert_\infty$$（定理 3.12 (iv)）。由 (i)，$$\widehat{a^*a} = \widehat{a^*}\,\hat a = \overline{\hat a}\,\hat a = \lvert \hat a \rvert^2$$，故 $$\lVert \widehat{a^*a}\rVert_\infty = \lVert \lvert \hat a \rvert^2\rVert_\infty = \lVert \hat a\rVert_\infty^2$$。合并得 $$\lVert a \rVert^2 = \lVert \hat a \rVert_\infty^2$$，开方即 $$\lVert \Gamma(a)\rVert_\infty = \lVert a\rVert$$。

满射性：令 $$\mathcal B = \Gamma(\mathcal A) \subset C(\Delta(\mathcal A))$$。由定理 3.12 (iii) 与 (i)，$$\mathcal B$$ 是含 $$\mathbf 1$$ 的闭 \*-子代数（$$\Gamma$$ 等距，像完备故闭）。它**分离点**：若 $$\varphi \ne \psi$$ 是 $$\Delta$$ 中两点，由定理 3.10 (i) 它们的核不同，故存在 $$a$$ 使 $$\varphi(a) \ne \psi(a)$$，即 $$\hat a(\varphi) \ne \hat a(\psi)$$。它**处处不为零**：$$\hat e = \mathbf 1$$ 在每点取值 1，故对任意 $$\varphi$$ 有 $$\hat e(\varphi) = 1 \ne 0$$。由 **Stone–Weierstrass 定理**（分离点、处处非零的含单位闭 \*-子代数在 $$C(\Delta)$$ 中稠密，而 $$\mathcal B$$ 闭），$$\mathcal B = C(\Delta(\mathcal A))$$。故 $$\Gamma$$ 满射，作为一个等距 \*-同构把 $$\mathcal A$$ 与 $$C(\Delta(\mathcal A))$$ 等同。$$\blacksquare$$

**注** 定理 3.19 常写成 **Gelfand–Naimark 定理**；无单位时结论变成 $$\mathcal A \cong C_0(X)$$（$$X$$ 局部紧、$$\mathcal A$$ 无单位的情形在练习里出现）。

### 3.9 正常算子与第 36 章悬念的收束

**定义 3.20（正常算子, normal operator）** 设 $$H$$ 是复 Hilbert 空间，$$T \in \mathcal B(H)$$。若
$$T^*T = TT^*,$$
则称 $$T$$ 为**正常算子 (normal operator)**。自伴算子（$$T^*=T$$）与酉算子（$$U^*U = UU^* = I$$）都是正常算子。

**定理 3.21（自伴算子的谱是实的；第 36 章 3.7 的答案）** 设 $$T \in \mathcal B(H)$$ 自伴。则 $$\sigma(T) \subset \mathbb{R}$$。更一般地，若 $$T$$ 正规，则 $$\sigma(T) = \lbrace \hat T(\varphi) : \varphi \in \Delta(\mathcal A)\rbrace$$，其中 $$\mathcal A$$ 是 $$T$$ 与 $$I$$ 生成的闭 \*-子代数；特别地 $$r(T) = \lVert T \rVert$$，且 $$T$$ 酉时 $$\sigma(T) \subset \mathbb{T} = \lbrace z : \lvert z \rvert = 1\rbrace$$。

**证明.** 令 $$\mathcal A$$ 为 $$B(H)$$ 中由 $$T$$ 与 $$I$$ 生成的闭 \*-子代数（即 $$\lbrace p(T,T^*) : p \text{ 是二元多项式}\rbrace$$ 的闭包）。因为 $$T$$ 正规，$$\mathcal A$$ **交换**：生成元 $$T, T^*, I$$ 两两交换（$$TT^* = T^*T$$ 与 $$I$$ 交换是定义），而交换元的多项式仍是交换的，取闭包保持交换。$$\mathcal A$$ 含单位 $$I$$，且是闭 \*-子代数，故以 $$T$$ 上的算子范数与伴随为对合，$$\mathcal A$$ 是含单位的**交换 C\* 代数**。

把 $$\mathcal A$$ 看成自己的 Banach 代数。由定理 3.12 (iv)，$$\sigma_{\mathcal A}(T) = \lbrace \hat T(\varphi) : \varphi \in \Delta(\mathcal A)\rbrace$$。由 Arens 引理（定理 3.18，用于交换 Banach 代数 $$\mathcal A$$ 及其自伴元 $$T$$），$$\hat T$$ 实值，故 $$\sigma_{\mathcal A}(T) \subset \mathbb{R}$$。

最后一步是把 $$\sigma_{\mathcal A}(T)$$ 与 $$\sigma_{\mathcal B(H)}(T)$$ 挂钩。若 $$\lambda \in \mathbb{C}$$ 使 $$\lambda I - T$$ 在 $$\mathcal A$$ 中可逆，其逆 $$\in \mathcal A \subset \mathcal B(H)$$，故 $$\lambda I - T$$ 在 $$\mathcal B(H)$$ 中也可逆。取逆否：

$$\sigma_{\mathcal B(H)}(T) \subseteq \sigma_{\mathcal A}(T) \subset \mathbb{R} .$$

（若 $$\lambda I - T$$ 在 $$\mathcal B(H)$$ 中不可逆，它在更小的 $$\mathcal A$$ 中当然也不可逆——这就是包含关系的内容。）

酉情形：若 $$U^*U = UU^* = I$$，则 $$U^*U = I = \hat e$$，于是 $$\lvert \hat U \rvert^2 = \widehat{U^*U} = \widehat{U^*}\hat U = \mathbf 1$$（用定理 3.19 (i)），故 $$\lvert \hat U \rvert \equiv 1$$，即 $$\sigma_{\mathcal A}(U) \subset \mathbb{T}$$；再用同一个包含关系。正常情形下的 $$r(T) = \lVert T\rVert$$ 由命题 3.17 (iii) 与定理 3.12 (iv) 合并。$$\blacksquare$$

**这段证明值得单独记住**：Arens 引理说「自伴 $$\Rightarrow$$ Gelfand 表示实值」，定理 3.12 说「谱 = 表示的值域」，两者一拼就是「自伴 $$\Rightarrow$$ 谱实」。第 36 章里，这件事曾被当作 $$\sigma(T) \subset \mathbb{R}$$ 的一个孤立事实（用谱定理或二次型符号直接得到）；现在它有了一个**结构性**的解释：$$\sigma(T)$$ 是 $$\hat T$$ 这个实值函数在紧空间 $$\Delta(\mathcal A)$$ 上的像。

**注 3.22（用「包含」而不用「相等」）** 上面的证明只用了 $$\sigma_{\mathcal B(H)}(T) \subseteq \sigma_{\mathcal A}(T)$$，方向是「越小的地方越难可逆」。对 C\* 代数，这个包含实际上是**等式**（自伴/正规的情形）——理由是 $$\lVert T\rVert = r_{\mathcal A}(T) = r_{\mathcal B(H)}(T)$$ 且谱是紧集，加上一个标准的连通性论证。我们不需要这个等式，故不展开；但请记住这个小技巧：**换到子代数上算谱，只会把谱放大，不会缩小**。

## 四、几何与物理直觉 (Intuition)

### 4.1 元素就是函数：三条视角的合流

本章唯一的动作，是把下面三句话叠成同一句。

**拓扑视角.** 在 $$C(X)$$ 里，$$f$$ 本来就是函数。它的「取值」$$f(x)$$ 是几何对象。

**算子视角.** 在 $$\mathcal B(H)$$ 里，$$T$$ 是算子，不是函数。但它的谱 $$\sigma(T)$$ 是「使 $$\lambda I - T$$ 不可逆的 $$\lambda$$」——这是**代数**对象，而且第 36 章已经证明它是 $$\mathbb{C}$$ 的非空紧子集。

**代数视角.** 在任意交换 Banach 代数 $$\mathcal A$$ 里，$$\sigma(a)$$ 是「使 $$\lambda e - a$$ 不可逆的 $$\lambda$$」——与算子情形是同一个定义，只是把 $$I$$ 换成 $$e$$、把 $$\mathcal B(H)$$ 换成 $$\mathcal A$$。

Gelfand 表示定理（定理 3.12 (iv)）把三者焊到一起：

$$\boxed{\ \sigma(a) = \lbrace \varphi(a) : \varphi \in \Delta(\mathcal A) \rbrace = \hat a(\Delta(\mathcal A))\ }$$

**元素的谱 = 它的 Gelfand 表示的值域。** 于是：谱点 $$\lambda$$ 就是「$$\hat a$$ 在某个点 $$\varphi$$ 上的取值」；「$$\lambda e - a$$ 不可逆」这句话，被翻译成了「存在一个点 $$\varphi$$ 使 $$\hat a(\varphi) = \lambda$$」。加一句概括：**$$\Delta(\mathcal A)$$ 是空间，$$\varphi$$ 是点，$$a$$ 是函数，$$\hat a(\varphi)$$ 是函数在点上的值。** 这就是本章的标题句「元素就是函数」。

点从哪来？从极大理想来。定理 3.10 说 $$\varphi \leftrightarrow \ker\varphi$$ 是一一对应，而 $$\ker\varphi = \lbrace a : \hat a(\varphi) = 0\rbrace$$——正是「在点 $$\varphi$$ 处取零的函数全体」。这与代数几何完全平行：多项式环 $$\mathbb{C}[z]$$ 的极大理想 $$\lbrace f : f(x_0) = 0\rbrace$$ 对应复平面上的点 $$x_0$$（这就是 **Hilbert 零点定理** 的雏形）。Gelfand 做的事是：把「用理想定义点」这个代数几何的操作，从多项式环搬到 Banach 代数上。上面对 $$\Delta(\mathcal A)$$ 装的那个弱\*拓扑（Gelfand 拓扑）恰好就是「逐点收敛」——它让代数结构自动生成了几何。

### 4.2 对偶的第三次出场

这是本章必须标出的一条主线。回顾全书：

| | 章 | 对偶的对象 | 内容 |
|---|---|---|---|
| 第一次 | 第 06 章 | **向量空间** | $$V \mapsto V^* = \mathcal B(V, \mathbb{C})$$，对偶空间、逆变与协变 |
| 第二次 | 第 30 章 | **Hilbert 空间** | Riesz 表示：$$H \cong H^*$$，「取内积」就是「取泛函」 |
| 第三次 | 本章 | **代数** | Gelfand：交换 Banach 代数 $$\mathcal A \mapsto C(\Delta(\mathcal A))$$，「元素」就是「函数」 |

三次的结构其实完全一样：**造一个「在对象上取值的探针」的集合，用探针的参数化这个对象。** 第 06 章的探针是线性泛函，第 30 章的探针是「与某个向量取内积」，本章的探针是特征 $$\varphi$$。

但第三次有一次**质变**。前两次对偶的出发点是「线性空间」，得到的对偶对象也是线性空间——对偶一次，结构变得一模一样，只是反过来。这一次出发点是**代数**，得到的却是**函数代数**：$$\mathcal A$$ 上只有抽象的乘法，而 $$C(\Delta(\mathcal A))$$ 上的乘法是**逐点相乘**。乘法被「解压」成了几何操作。这意味着对偶不再只是「空间 ↦ 空间」，而是「**一类结构与另一类结构之间的对应**」——这就是范畴对偶 (categorical duality) 的雏形。第 62 章会把这种「一类结构 ≅ 另一类结构」的对应正式定义成一个范畴等价（函子、自然变换）。本章是这条路的入口。

$$\textbf{记忆锚：}\quad \text{ch03：向量} \to \text{泛函} \;\Longrightarrow\; \text{ch15：向量} \to \text{内积} \;\Longrightarrow\; \text{ch20：元素} \to \text{函数} .$$

### 4.3 物理直觉：为什么可观测量必须取实数

量子力学第一公理说：**可观测量的测量结果必须是实数**。数学上，可观测量是自伴算子 $$T = T^*$$，测量结果的可能性集合是它的谱 $$\sigma(T)$$。所以物理公理等价于数学命题「$$\sigma(T) \subset \mathbb{R}$$」——这正是定理 3.21 的内容。

定理 3.21 的证明链条把物理相容性的来源说清楚了：

$$\underbrace{T = T^*}_{\text{物理：可观测量}} \Rightarrow \underbrace{\hat T \text{ 实值}}_{\text{代数：Arens 引理}} \Rightarrow \underbrace{\sigma(T) \subset \mathbb{R}}_{\text{物理：测量值是实数}} .$$

中间那步是纯代数的：它只用到「$$\varphi(a^*) = \overline{\varphi(a)}$$」与「$$\lvert\varphi(c)\rvert \le \lVert c\rVert$$」。换句话说，**测量值是实数这件事，不是量子力学的特设假设，而是 C\* 代数公理（对合 + 范数）的必然推论**。这就是为什么 C\* 代数被当作量子力学的标准数学语言。

顺着这条路再往前走一步，物理图景会更完整：

- **可观测量**（自伴元）对应 $$C(\Delta)$$ 中的实值函数；
- **谱** $$\sigma(T)$$ 是 $$\hat T$$ 的值域，也就是「这个物理量可能取到的一切数值」；
- **量子态**对应 C\* 代数的**态 (state)**——满足 $$\varphi(e) = 1$$ 与 $$\varphi(a^*a) \ge 0$$ 的线性泛函，物理意义是「期望值」；
- **$$\Delta(\mathcal A)$$ 上的点** $$\varphi$$ 是交换情形下的「态」——即「取值探针」，物理上就是**纯态**。

第 32 章讲可观测量与本征态时，我们只有「算子 + 谱测度」这一套语言；现在多了「代数 + 态」这套语言。两者是同一件事的两个坐标：谱测度描述「测量结果的分布」（几何/测度侧），态描述「系统的准备方式」（代数侧）。第 44 章（正则对易关系与 Stone–von Neumann）会看到，正是「态」与「表示」的关系，决定了量子力学的 Hilbert 空间表示在什么意义下是唯一的。

### 4.4 Gelfand 拓扑的几何含义

$$\Delta(\mathcal A)$$ 上的 Gelfand 拓扑是弱\*拓扑。用第 30 章的语言：$$\varphi_n \to \varphi$$ 当且仅当 $$\varphi_n(a) \to \varphi(a)$$ 对**每个** $$a \in \mathcal A$$。翻译成函数语言，就是

$$\hat a(\varphi_n) \to \hat a(\varphi) \ \ \forall a \in \mathcal A \qquad \Longleftrightarrow \qquad \text{「函数序列在每点上收敛」} .$$

于是「$$\Delta(\mathcal A)$$ 紧」这句抽象的话，有一个非常具体的含义：**它保证了连续函数代数中有足够多的点来实现最大值**——$$\lVert \hat a\rVert_\infty = \sup_\varphi \lvert \hat a(\varphi)\rvert$$ 里的上确界一定被取到（真的达到，不是逼近）。这就是谱半径公式里 $$\sup$$ 能写成 $$\max$$、命题 3.4 (i) 能断言 $$\sigma(a)$$ 是**紧**集的深层原因。

同时，迹 (iv) 还给出了一个自动的「Stone–Weierstrass 型」结论：$$\Gamma(\mathcal A)$$ 在 $$C(\Delta(\mathcal A))$$ 中分离点、处处非零，于是稠密；C\* 情形下因等距而更进一层，直接**充满**。

### 4.5 交换的边界：非交换几何的入口

入口题 (d) 问的是：交换条件去掉会怎样？

答案很干脆。特征的定义里用了 $$\varphi(ab) = \varphi(a)\varphi(b)$$，而如果 $$\mathcal A$$ 非交换，两个**不可交换**的元 $$a, b$$ 会撞车：由 $$\varphi(ab) = \varphi(a)\varphi(b)$$ 与 $$\varphi(ba) = \varphi(b)\varphi(a)$$（$$\mathbb{C}$$ 交换）加上 $$\varphi(ab) = \varphi(ba)$$（同一个特征在同一点取值），立刻推出 $$\varphi([a,b]) = 0$$ 对一切交换子成立——即每个特征都零化整个交换子理想。当 $$\mathcal A = \mathcal B(H)$$（$$\dim H \ge 2$$）时，$$\mathcal B(H)$$ 的交换子理想是整个 $$\mathcal B(H)$$，于是不存在非零特征：$$\Delta(\mathcal B(H)) = \varnothing$$。**空间消失了。**

这正是「非交换几何 (non-commutative geometry)」要处理的情形：没有点，那就**不要点**。把「空间」直接定义成代数，把「几何操作」都翻译成代数操作（测度 = 正线性泛函、向量丛 = 投影模、微分 = 交换子、积分 = 迹）。Gelfand–Naimark 一般情形（无单位时 $$\mathcal A \cong C_0(X)$$、一般情形 $$\mathcal A$$ 是某个 $$\mathcal B(H)$$ 的闭 \*-子代数）说明：**抽象的 C\* 代数一定是具体算子代数**，所以代数本身就够当「空间」用。

回到入口题 (d) 的提示：对非交换的 $$\mathcal B(H)$$，仍然有意义的替代品是**取单个正规算子 $$T$$，退到它生成的交换子代数** $$\mathcal A = \overline{\lbrace p(T, T^*) \rbrace}$$。这就是定理 3.21 的做法，也是第 38 章谱定理的代数化版本：非交换世界里，我们只能一个一个算子地「局部交换化」，$$\Delta(\mathcal A)$$ 就是 $$\sigma(T)$$。这也解释了一个第 38 章留下的现象——**为什么自伴算子的谱测度能唯一存在**：因为生成的代数是交换 C\* 代数，Gelfand 表示在它上面是等距 \*-同构，于是「连续函数演算」$$f(T) = \Gamma^{-1}(f)$$ 是唯一确定的。第 38 章用谱测度构造 $$f(T)$$；本章从 C\* 代数的公理重新导出一遍，两条路殊途同归。

## 五、经典问题精讲 (Classical Problems)

下面五题各对应正文里的一台机器，逐题给完整解，且与第六节的练习不重复。每题先标 **【考点】**（用到哪条定理）与 **【位置】**（它在 §3 的结构里的坐标）。

### 经典问题 1（拟幂零但不为零：Volterra 积分算子）

**【考点】** 谱半径公式（定理 3.5）与「谱非空」（命题 3.4 (ii)）。
**【位置】** §3.3——定理 3.5 之后那条注点名的正是这个例子。

取 $$H = L^2[0,1]$$，定义 **Volterra 积分算子**
$$(Vf)(x) = \int_0^x f(t)\,dt \qquad (f \in L^2[0,1]) .$$

(i) 证明 $$V \in \mathcal B(H)$$ 且 $$\lVert V \rVert \le 1$$；(ii) 证明 $$\lVert V \rVert \ge 1/\sqrt3$$；(iii) 求出 $$V^n$$ 并证明 $$r(V) = 0$$；(iv) 算出 $$\sigma(V)$$，并解释为什么这与命题 3.17 (iii) 不冲突。

**解.**

(i) 对 $$f \in L^2[0,1]$$ 与 $$x \in [0,1]$$，
$$\lvert (Vf)(x) \rvert = \Big\lvert \int_0^x f(t)\,dt \Big\rvert \le \int_0^1 \lvert f(t) \rvert\,dt = \lVert f \rVert_1 \le \lVert f \rVert_2 ,$$
末一步是 Cauchy–Schwarz（$$[0,1]$$ 的总测度为 $$1$$）。故 $$Vf$$ 有界且 $$\lVert Vf \rVert_\infty \le \lVert f \rVert_2$$，于是 $$\lVert Vf \rVert_2 \le \lVert Vf \rVert_\infty \le \lVert f\rVert_2$$。所以 $$V$$ 有界、$$\lVert V \rVert \le 1$$。线性性来自积分的线性性。$$\blacksquare$$

(ii) 取 $$f_0 = \mathbf 1$$。则 $$(Vf_0)(x) = x$$，故
$$\lVert V \rVert \ge \frac{\lVert V f_0 \rVert_2}{\lVert f_0 \rVert_2} = \Big(\int_0^1 x^2\,dx\Big)^{1/2} = \frac{1}{\sqrt3} > 0 .$$
（事实上 $$\lVert V \rVert = 2/\pi$$，这是经典的变分计算结果；本题只需要一个正的常数，故不展开。）$$\blacksquare$$

(iii) 先用归纳证明
$$(V^n f)(x) = \frac{1}{(n-1)!}\int_0^x (x-t)^{n-1} f(t)\,dt \qquad (n \ge 1) .$$
$$n=1$$ 时右端是 $$\int_0^x f(t)\,dt = (Vf)(x)$$。设对 $$n$$ 成立，则
$$(V^{n+1}f)(x) = \int_0^x (V^n f)(u)\,du = \frac{1}{(n-1)!}\int_0^x\!\!\int_0^u (u-t)^{n-1}f(t)\,dt\,du .$$
交换积分次序（被积函数在三角形 $$\lbrace 0 \le t \le u \le x\rbrace$$ 上连续，Fubini 适用）：
$$\frac{1}{(n-1)!}\int_0^x f(t)\Big(\int_t^x (u-t)^{n-1}\,du\Big)dt = \frac{1}{(n-1)!}\int_0^x f(t)\,\frac{(x-t)^{n}}{n}\,dt = \frac{1}{n!}\int_0^x (x-t)^n f(t)\,dt .$$

于是对 $$x \in [0,1]$$，
$$\lvert (V^n f)(x) \rvert \le \frac{1}{(n-1)!}\int_0^x (x-t)^{n-1}\lvert f(t)\rvert\,dt \le \frac{\lVert f \rVert_1}{(n-1)!} \le \frac{\lVert f \rVert_2}{(n-1)!} ,$$
故 $$\lVert V^n \rVert \le 1/(n-1)!$$。开 $$n$$ 次方，并用 $$(n-1)! \ge ((n-1)/e)^{n-1}$$：
$$\lVert V^n \rVert^{1/n} \le \big((n-1)!\big)^{-1/n} \le \Big(\frac{e}{n-1}\Big)^{(n-1)/n} \xrightarrow{\ n \to \infty\ } 0 .$$
由谱半径公式（定理 3.5），$$r(V) = \lim_{n\to\infty}\lVert V^n \rVert^{1/n} = 0$$。$$\blacksquare$$

(iv) 命题 3.4 (ii) 给出 $$\sigma(V) \ne \varnothing$$，而 $$r(V) = \sup_{\lambda \in \sigma(V)}\lvert \lambda\rvert = 0$$ 逼出
$$\sigma(V) = \lbrace 0 \rbrace .$$

这与命题 3.17 (iii) 不冲突，因为 $$V$$ **不正规**：命题 3.17 (iii) 的前提是 $$a^*a = aa^*$$。$$V$$ 的伴随是 $$(V^*g)(x) = \int_x^1 g(t)\,dt$$，于是对 $$g = \mathbf 1$$，
$$(VV^*\mathbf 1)(x) = \int_0^x (1-t)\,dt = x - \frac{x^2}{2}, \qquad (V^*V\mathbf 1)(x) = \int_x^1 t\,dt = \frac{1-x^2}{2},$$
两者在 $$x = 0$$ 处取值分别为 $$0$$ 与 $$1/2$$，不等，故 $$VV^* \ne V^*V$$。于是 $$r(V) = 0 < 1/\sqrt3 \le \lVert V \rVert$$ 完全在预料之中。$$\blacksquare$$

**读法.** $$\lVert V \rVert > 0 = r(V)$$ 是本章第一处「$$a$$ 本身的范数决定不了谱」的硬证据。谱半径公式的正确读法是：**谱的大小由幂 $$\lVert a^n \rVert$$ 的增长速率决定**；$$V^n$$ 按 $$1/n!$$ 衰减，这才是 $$r(V) = 0$$ 的来源。

### 经典问题 2（非交换的边界：$$M_n(\mathbb{C})$$ 一个特征都没有）

**【考点】** 极大理想与特征（定义 3.6、定义 3.9、命题 3.7 (iii)），以及「交换」这一前提的作用。
**【位置】** §3.4–3.5；它把入口题 (d) 从「不可交换的元会撞车」补成一个完备的证明。

设 $$n \ge 2$$，$$\mathcal A = M_n(\mathbb{C})$$ 为复 $$n \times n$$ 矩阵代数（范数取 $$\mathbb{C}^n$$ 上的算子范数，乘法为矩阵乘法，对合取共轭转置）。

(i) 说明 $$\mathcal A$$ 是含单位的 Banach 代数，但 $$n \ge 2$$ 时不交换；(ii) 证明 $$\mathcal A$$ **单**：仅有的双侧理想是 $$\lbrace 0\rbrace$$ 与 $$\mathcal A$$；(iii) 由此证明 $$\Delta(\mathcal A) = \varnothing$$；(iv) 指出命题 3.7 (iii) 的哪一步用了交换性，并说明「仍然有意义」的替代品。

**解.**

(i) $$\mathbb{C}^n$$ 有限维，故 $$\mathcal A$$ 在算子范数下完备；$$\lVert AB \rVert \le \lVert A \rVert \lVert B \rVert$$ 是算子范数的标准性质；$$\lVert I \rVert = 1$$。非交换：用矩阵单位 $$E_{ij}$$（第 $$i$$ 行第 $$j$$ 列为 $$1$$、其余为 $$0$$），
$$E_{12}E_{21} = E_{11} \ne E_{22} = E_{21}E_{12} . \qquad \blacksquare$$

(ii) 设 $$\mathfrak I$$ 是双侧理想，$$\mathfrak I \ne \lbrace 0\rbrace$$。取 $$0 \ne X \in \mathfrak I$$，则存在下标 $$i, j$$ 使 $$X_{ij} \ne 0$$（否则 $$X = 0$$）。由 $$E_{ab}E_{cd} = \delta_{bc}E_{ad}$$，
$$E_{ii}\,X\,E_{jj} = X_{ij}E_{ij} \in \mathfrak I \quad\Longrightarrow\quad E_{ij} = X_{ij}^{-1}\big(E_{ii}XE_{jj}\big) \in \mathfrak I ,$$
这里第二个式子用了 $$\mathfrak I$$ 是子空间。再对任意 $$k$$，
$$E_{kk} = E_{ki}E_{ij}E_{jk} \in \mathfrak I .$$
于是 $$I = \sum_{k=1}^{n} E_{kk} \in \mathfrak I$$，从而任意 $$Y = YI \in \mathfrak I$$，即 $$\mathfrak I = \mathcal A$$。故 $$\mathcal A$$ 单。$$\blacksquare$$

(iii) 设 $$\varphi \in \Delta(\mathcal A)$$。$$\ker\varphi$$ 是双侧理想（若 $$\varphi(X)=0$$，则 $$\varphi(XY) = \varphi(X)\varphi(Y) = 0$$，同理 $$\varphi(YX)=0$$），且真（$$\varphi \ne 0$$）。由 (ii)，$$\ker\varphi = \lbrace 0\rbrace$$，即 $$\varphi$$ 是单射。但 $$\varphi : M_n(\mathbb{C}) \to \mathbb{C}$$ 是线性映射，若单则 $$\dim M_n(\mathbb{C}) = n^2 \le \dim\mathbb{C} = 1$$，与 $$n \ge 2$$ 矛盾。故
$$\Delta(\mathcal A) = \varnothing .$$
**Gelfand 空间是空集**：没有点，几何彻底消失。$$\blacksquare$$

(iv) 命题 3.7 (iii) 的证明在「$$\mathfrak J = \mathcal A$$，故 $$e = ac + i$$」之后写了「交换性使左乘右乘一致」——**这一步就是交换性的全部用途**。去掉它，从 $$e = ac + i$$ 只能读出「$$a + \mathfrak I$$ 有右逆」，得不出可逆。

结论本身在非交换时也假：由 (ii)，$$\lbrace 0\rbrace$$ 是 $$\mathcal A$$ 的极大理想（它真，且没有真理想严格包含它），但商代数
$$\mathcal A/\lbrace 0\rbrace = M_n(\mathbb{C})$$
不是可除代数。所以非交换时「极大理想 ↔ 特征」这条一一对应整体失效：每个特征仍给出极大理想 $$\ker\varphi$$，反过来不成立，而且可能一个特征都没有（就是本题）。

**替代品**（见 §4.5 与定理 3.21）：不再问整个 $$\mathcal B(H)$$ 的特征，而是固定一个**正规算子** $$T$$，退到由 $$T$$ 与 $$I$$ 生成的**交换**闭 \*-子代数 $$\mathcal A_T$$。那里 $$\Delta(\mathcal A_T)$$ 不但非空，而且 $$\sigma(T) = \Gamma(T)(\Delta(\mathcal A_T))$$——「点」在单个算子的局部世界里重新出现了。$$\blacksquare$$

### 经典问题 3（$$C(X)$$ 的 Gelfand 表示就是恒等：入口题 (a)(c) 的结算）

**【考点】** 定理 3.10 (i)、定理 3.12 (ii)(iii)(iv)。
**【位置】** §3.5–3.6。正文在定理 3.12 之后点名此题；入口题 (a) 与 (c) 的正式解答就在这里。

设 $$X$$ 是紧 Hausdorff 空间，$$\mathcal A = C(X)$$（上确界范数、逐点乘法），对 $$x \in X$$ 定义 $$A_x(f) = f(x)$$。

(i) 证明 $$A_x \in \Delta(\mathcal A)$$ 且 $$\Gamma(f)(A_x) = f(x)$$；
(ii) 证明 $$\Delta(\mathcal A) = \lbrace A_x : x \in X\rbrace$$；
(iii) 综合说明：在等同 $$X \cong \Delta(\mathcal A)$$ 下，$$\Gamma$$ 就是 $$C(X) \to C(\Delta(\mathcal A))$$ 的**恒等映射**，于是 $$\sigma(f) = f(X)$$。

**解.**

(i) $$A_x$$ 线性、非零（$$A_x(\mathbf 1) = 1$$），且 $$A_x(fg) = (fg)(x) = f(x)g(x) = A_x(f)A_x(g)$$，故 $$A_x \in \Delta(\mathcal A)$$。再由 Gelfand 表示的定义（定义 3.11），$$\Gamma(f)(A_x) = A_x(f) = f(x)$$。$$\blacksquare$$

(ii) 关键是先证一条**公共零点引理**：若 $$\mathfrak I \subsetneq \mathcal A$$ 是真理想，则存在 $$x_0 \in X$$ 使 $$f(x_0) = 0$$ 对一切 $$f \in \mathfrak I$$。

*引理的证明.* 反设每个 $$x$$ 都有某个 $$f \in \mathfrak I$$ 使 $$f(x) \ne 0$$。由 $$f$$ 连续，存在 $$x$$ 的开邻域 $$U_x$$ 使 $$f \ne 0$$ 于 $$U_x$$ 上。$$\lbrace U_x\rbrace_{x \in X}$$ 是紧空间 $$X$$ 的开覆盖，取出有限子覆盖 $$U_{x_1},\dots,U_{x_k}$$，对应 $$f_1,\dots,f_k \in \mathfrak I$$，使得：**每个** $$y \in X$$ 至少落在一个 $$U_{x_i}$$ 里，故至少有一个 $$f_i(y) \ne 0$$。令
$$g = \lvert f_1 \rvert^2 + \dots + \lvert f_k \rvert^2 = f_1 \bar f_1 + \dots + f_k \bar f_k \in \mathfrak I$$
（每项 $$f_i\bar f_i$$ 落在 $$\mathfrak I$$ 里，因为 $$\bar f_i \in \mathcal A$$ 而 $$\mathfrak I$$ 吸收乘法）。在每个 $$y$$，右端是若干非负实数之和且至少一项为正，故 $$g(y) > 0$$。紧空间上连续正函数有正下界，故 $$1/g \in C(X)$$，于是
$$\mathbf 1 = g \cdot \frac{1}{g} \in \mathfrak I ,$$
与 $$\mathfrak I$$ 真矛盾（由命题 3.7 (i)，真理想不含可逆元，而 $$\mathbf 1$$ 可逆）。引理得证。

现在取任意 $$\varphi \in \Delta(\mathcal A)$$。由定理 3.10 (i)，$$\ker\varphi$$ 是极大理想，当然真，故引理给出 $$x_0$$ 使 $$f(x_0) = 0$$ 对一切 $$f \in \ker\varphi$$。于是线性泛函
$$\psi = \varphi - A_{x_0}$$
在 $$\ker\varphi$$ 上恒为零。由定理 3.10 (i) 又有 $$\mathcal A/\ker\varphi \cong \mathbb{C}$$，即 $$\ker\varphi$$ 的余维为 $$1$$；而在余维 $$1$$ 的子空间上为零的两个线性泛函必成比例，故 $$\psi = c\varphi$$ 对某个 $$c \in \mathbb{C}$$。在单位元 $$\mathbf 1$$ 处取值定出 $$c$$：
$$c = c\,\varphi(\mathbf 1) = \psi(\mathbf 1) = \varphi(\mathbf 1) - A_{x_0}(\mathbf 1) = 1 - 1 = 0 .$$
故 $$\psi = 0$$，即 $$\varphi = A_{x_0}$$。连同 (i) 得到 $$\Delta(\mathcal A) = \lbrace A_x : x \in X\rbrace$$。$$\blacksquare$$

(iii) 由 (ii)，$$x \mapsto A_x$$ 是满射；它是**单射**：若 $$A_x = A_y$$ 则 $$f(x) = f(y)$$ 对一切 $$f \in C(X)$$，由 $$X$$ Hausdorff 与 Urysohn 引理（连续函数分离点）得 $$x = y$$。它还是**连续**的：若网 $$x_\alpha \to x$$，则对每个 $$f \in C(X)$$ 有 $$f(x_\alpha) \to f(x)$$（$$f$$ 连续），即 $$A_{x_\alpha}(f) \to A_x(f)$$，这正是 $$\Delta$$ 上弱\*拓扑（Gelfand 拓扑）的收敛。于是连续双射从紧空间 $$X$$ 到 Hausdorff 空间 $$\Delta(\mathcal A)$$，故是同胚：
$$X \cong \Delta(\mathcal A) .$$

在这个等同下，(i) 说 $$\Gamma(f)$$ 在点 $$x$$ 处的值就是 $$f(x)$$，即
$$\Gamma(f) = f \qquad \text{（把 } \Delta(\mathcal A) \text{ 与 } X \text{ 等同起来看）}.$$
所以 **$$\Gamma$$ 是恒等映射**。再由定理 3.12 (iv)，
$$\sigma(f) = \Gamma(f)\big(\Delta(\mathcal A)\big) = f(X) ,$$
这就是入口题 (a) 的结论；而 $$K = \Delta(\mathcal A) \cong X$$、$$\Gamma = \mathrm{id}$$ 正是入口题 (c) 要猜的那对 $$(K, \Gamma)$$。

顺带一句：$$C(X)$$ 本身是交换 C\* 代数（对合取 $$f^* = \bar f$$，则 $$\lVert f^*f \rVert_\infty = \lVert \lvert f \rvert^2 \rVert_\infty = \lVert f \rVert_\infty^2$$），故定理 3.19 在此给出更强的结论：$$\Gamma$$ 是等距 \*-同构。**$$C(X)$$ 是 Gelfand 理论里「一切都不退化」的极端情形。**$$\blacksquare$$

### 经典问题 4（乘法算子的谱：自伴性怎么读，Arens 引理又用在哪）

**【考点】** 定理 3.21（自伴/正规 $$\Rightarrow$$ 实谱）与定理 3.18（Arens 引理）；对合在算子上的具体含义。
**【位置】** §3.7–3.8；它把入口题 (b) 与「对合抽象了复共轭」这件事收在一起。

取 $$H = L^2[0,1]$$，设 $$\varphi \in C[0,1]$$ 复值连续，定义**乘法算子**
$$(M_\varphi f)(x) = \varphi(x) f(x) .$$
(i) 证明 $$M_\varphi \in \mathcal B(H)$$ 且 $$\lVert M_\varphi \rVert = \lVert \varphi \rVert_\infty$$；(ii) 证明 $$M_\varphi^* = M_{\bar\varphi}$$，特别地 $$M_\varphi$$ 自伴 $$\iff$$ $$\varphi$$ 实值；(iii) 证明 $$\sigma(M_\varphi) = \varphi([0,1])$$；(iv) 说明 (iii) 与 Arens 引理各自证明了「自伴 $$\Rightarrow$$ 实谱」的哪一半，并指出哪一步真正需要 C\* 恒等式。

**解.**

(i) $$\lVert M_\varphi f \rVert_2^2 = \int_0^1 \lvert \varphi \rvert^2\lvert f\rvert^2 \le \lVert \varphi \rVert_\infty^2 \lVert f \rVert_2^2$$，故 $$\lVert M_\varphi \rVert \le \lVert \varphi \rVert_\infty$$。反向：取 $$x_0$$ 使 $$\lvert \varphi(x_0)\rvert = \lVert \varphi \rVert_\infty$$。若 $$\lVert \varphi \rVert_\infty = 0$$ 则 $$\varphi \equiv 0$$，结论平凡；否则对 $$\varepsilon \in (0, \lVert\varphi\rVert_\infty)$$，由连续性存在 $$x_0$$ 的邻域 $$U$$ 使 $$\lvert \varphi \rvert > \lVert \varphi \rVert_\infty - \varepsilon$$ 于 $$U$$ 上。取 $$f_\varepsilon$$ 为 $$U$$ 上、$$\lVert f_\varepsilon \rVert_2 = 1$$ 的任意 $$L^2$$ 函数（例如 $$U$$ 上归一化的指示函数）。则
$$\lVert M_\varphi f_\varepsilon \rVert_2 \ge \big(\lVert \varphi \rVert_\infty - \varepsilon\big)\lVert f_\varepsilon \rVert_2 = \lVert \varphi \rVert_\infty - \varepsilon .$$
令 $$\varepsilon \to 0$$ 得 $$\lVert M_\varphi \rVert \ge \lVert \varphi\rVert_\infty$$。两向合并取等。$$\blacksquare$$

(ii) 对 $$f, g \in L^2[0,1]$$，
$$\langle M_\varphi f, g\rangle = \int_0^1 \varphi f \bar g = \int_0^1 f\,\overline{\bar\varphi g} = \langle f, M_{\bar\varphi}\, g\rangle ,$$
故由伴随的唯一性 $$M_\varphi^* = M_{\bar\varphi}$$。于是 $$M_\varphi$$ 自伴 $$\iff$$ $$M_\varphi = M_{\bar\varphi}$$ $$\iff$$ $$\varphi = \bar\varphi$$ 处处（连续函数相等只需在每点成立）$$\iff$$ $$\varphi$$ 实值。$$\blacksquare$$

(iii) **含于**：设 $$\lambda \notin \varphi([0,1])$$。$$\varphi([0,1])$$ 紧，故 $$\lambda$$ 到它的距离 $$d > 0$$。于是 $$\psi = 1/(\varphi - \lambda)$$ 连续、$$\lVert \psi \rVert_\infty \le 1/d$$，且逐点有 $$\psi(\varphi - \lambda) = 1$$。按乘法算子的定义，这读出
$$M_\psi\,(\lambda I - M_\varphi) = (\lambda I - M_\varphi)\,M_\psi = I ,$$
故 $$\lambda \notin \sigma(M_\varphi)$$。

**包含**：设 $$\lambda = \varphi(x_0)$$，$$\varepsilon > 0$$。取 $$g_\varepsilon \in L^2$$ 为单位向量，支集含于邻域 $$U_\varepsilon = \lbrace x : \lvert \varphi(x) - \lambda \rvert < \varepsilon\rbrace$$（$$x_0 \in U_\varepsilon$$，故非空）。则
$$\lVert (\lambda I - M_\varphi)g_\varepsilon \rVert_2^2 = \int_0^1 \lvert \lambda - \varphi(x)\rvert^2\lvert g_\varepsilon(x)\rvert^2\,dx \le \varepsilon^2 .$$
若 $$\lambda \notin \sigma(M_\varphi)$$，设 $$R = (\lambda I - M_\varphi)^{-1} \in \mathcal B(H)$$，则
$$1 = \lVert g_\varepsilon \rVert_2 = \lVert R(\lambda I - M_\varphi)g_\varepsilon \rVert_2 \le \lVert R \rVert \cdot \varepsilon .$$
令 $$\varepsilon \to 0$$ 得 $$1 \le 0$$，矛盾。故 $$\lambda \in \sigma(M_\varphi)$$。两边合并：$$\sigma(M_\varphi) = \varphi([0,1])$$。$$\blacksquare$$

(iv) 设 $$\varphi$$ 实值。两条路都能得到实谱，但它们证明的东西不同：

- (iii) 是**逐点计算**：$$\sigma(M_\varphi) = \varphi([0,1]) \subset \mathbb{R}$$，只用到 $$\varphi$$ 的具体表达式。
- 定理 3.21 是**结构性的**：$$M_\varphi$$ 自伴，故在由 $$M_\varphi$$ 与 $$I$$ 生成的交换 C\* 代数上用 Arens 引理，得 $$\hat M_\varphi$$ 实值，再由定理 3.12 (iv) 得实谱。它**完全不需要知道 $$\varphi$$ 与 $$x$$ 长什么样**——任何 Hilbert 空间上的自伴算子都适用。这正是 §4.3 那条链
$$T = T^* \Rightarrow \hat T \ \text{实值} \Rightarrow \sigma(T) \subset \mathbb{R}$$
中中间一步的价值。

需要 C\* 恒等式的**只有中间那一步**，即 Arens 引理（定理 3.18）：它把 $$\lvert \varphi(b) \rvert^2$$ 一路压到不超过 $$\lVert a \rVert^2 + t^2$$，其中换范数的那一次 $$\lVert b \rVert^2 = \lVert b^*b \rVert$$ 正是 C\* 恒等式。没有这一条（例如注 3.18 的 $$\mathcal A_0$$），自伴元的谱可以跑出实轴。$$\blacksquare$$

### 经典问题 5（「元素就是函数」最简的一次落地：两个点的 C\* 代数）

**【考点】** 定理 3.12 (iv) 与定理 3.18；§4.1 那张「谱 = 值域」的图。
**【位置】** §3.9 的收束。它与注 3.18 的反例共用**同一个底空间 $$\mathbb{C}^2$$、同一个范数**，差别只在**对合**——这正好把 C\* 恒等式的作用照出来。

取 $$T = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \in M_2(\mathbb{C})$$，令 $$\mathcal A_T$$ 为由 $$T$$ 与 $$I$$ 生成的闭 \*-子代数（算子范数、对合取共轭转置）。

(i) 证明 $$T$$ 自伴、$$T^2 = I$$，且 $$\mathcal A_T = \lbrace \alpha I + \beta T : \alpha,\beta \in \mathbb{C}\rbrace$$；
(ii) 算出 $$\Delta(\mathcal A_T)$$（恰两个点）与 $$\Gamma$$ 的显式形状；
(iii) 算出 $$\sigma(T)$$，并核对 $$\sigma(T) = \Gamma(T)(\Delta(\mathcal A_T))$$；
(iv) 把 $$\mathcal A_T$$ 与注 3.18 的 $$\mathcal A_0$$ 并排，指出是**哪个元素**让 $$\mathcal A_0$$ 的 C\* 恒等式失效，并解释为什么 $$\mathcal A_T$$ 这边不出问题。

**解.**

(i) $$T$$ 是实对称矩阵，故 $$T^* = T$$；直接计算 $$T^2 = I$$。于是 $$V = \mathrm{span}\lbrace I, T\rbrace$$ 对乘法封闭（$$(\alpha I + \beta T)(\gamma I + \delta T) = (\alpha\gamma + \beta\delta)I + (\alpha\delta + \beta\gamma)T$$，用了 $$T^2 = I$$），对伴随也封闭（$$(\alpha I + \beta T)^* = \bar\alpha I + \bar\beta T$$）。有限维空间里的子空间自动闭，故 $$\mathcal A_T$$ 就是这个二维 \*-子代数。$$\blacksquare$$

(ii) 设 $$\varphi \in \Delta(\mathcal A_T)$$。$$\varphi(I) = 1$$（定义 3.9），$$\varphi$$ 由 $$\mu := \varphi(T)$$ 唯一决定。乘性要求
$$\mu^2 = \varphi(T)^2 = \varphi(T^2) = \varphi(I) = 1 ,$$
故 $$\mu \in \lbrace 1, -1\rbrace$$。反之，对 $$\mu = \pm 1$$，
$$\varphi_\mu(\alpha I + \beta T) = \alpha + \beta\mu$$
确实是良定义的特征：$$\lbrace I, T\rbrace$$ 线性无关保证良定义，$$\mu^2 = 1$$ 与 (i) 的乘法公式保证乘性，$$\varphi_\mu(I) = 1 \ne 0$$。于是
$$\Delta(\mathcal A_T) = \lbrace \varphi_+,\ \varphi_- \rbrace, \qquad \Gamma(\alpha I + \beta T)\big(\varphi_\pm\big) = \alpha \pm \beta .$$
用 $$\mathbb{C}^2$$ 的坐标写（把 $$(\alpha + \beta,\ \alpha - \beta)$$ 记成 $$(z, w)$$），$$\Gamma$$ 就是「把 $$(\alpha,\beta)$$ 送成两点上的函数」这一步，且
$$\lVert \alpha I + \beta T \rVert = \max(\lvert \alpha + \beta \rvert,\ \lvert \alpha - \beta \rvert) = \lVert \Gamma(\alpha I + \beta T) \rVert_\infty ,$$
因为 $$T$$ 正规（对称）、特征值为 $$\pm 1$$，算子范数等于谱半径（命题 3.17 (iii)）。这就是「元素 = 函数」的最简实现：**$$\mathcal A_T$$ 与 $$C(\Delta(\mathcal A_T))$$ 都是 $$\mathbb{C}^2$$，$$\Gamma$$ 在两者之间是恒等。**$$\blacksquare$$

(iii) 由 $$T^2 = I$$：若 $$Tv = \lambda v$$，$$v \ne 0$$，则 $$\lambda^2 v = v$$，故 $$\lambda = \pm 1$$。两个值都取到：$$T\binom{1}{1} = \binom{1}{1}$$，$$T\binom{1}{-1} = -\binom{1}{-1}$$。故
$$\sigma(T) = \lbrace 1,\ -1\rbrace .$$
核对定理 3.12 (iv)：$$\Gamma(T)(\Delta(\mathcal A_T)) = \lbrace \varphi_+(T),\ \varphi_-(T)\rbrace = \lbrace 1,\ -1\rbrace = \sigma(T)$$。也与定理 3.18 相符：$$T$$ 自伴，而 $$\Gamma(T)$$ 在两个点上的取值 $$1$$ 与 $$-1$$ 都是实数；$$\sigma(T) \subset \mathbb{R}$$。此外 $$r(T) = 1 = \lVert T \rVert$$，与命题 3.17 (iii) 一致。$$\blacksquare$$

(iv) 先把两者放在同一个坐标系里。$$\mathcal A_T$$ 的 $$\alpha I + \beta T$$ 在 $$\Delta$$ 上对应 $$(z,w) = (\alpha+\beta, \alpha-\beta)$$，在相反方向 $$\alpha = (z+w)/2$$、$$\beta = (z-w)/2$$。在这组坐标下：
- $$\mathcal A_T$$ 的范数是 $$\max(\lvert z\rvert, \lvert w \rvert)$$（(ii) 已算），与 $$\mathcal A_0$$ 的上确界范数**完全一样**；
- $$\mathcal A_T$$ 的对合是伴随 $$(\alpha I + \beta T)^* = \bar\alpha I + \bar\beta T$$，对应到 $$(z,w)$$ 就是
$$(z,\ w) \mapsto (\bar z,\ \bar w) \qquad \text{（逐分量共轭）},$$
而 $$\mathcal A_0$$ 用的是**交换再共轭** $$(z,w)^* = (\bar w, \bar z)$$。

差别仅在这一点。失效的元素就是 (iv) 要的那个：取 $$x = (1,0)$$（即 $$\alpha = \beta = 1/2$$，$$x = \frac12 I + \frac12 T$$）。逐分量共轭下 $$x^* = (1,0) = x$$，$$x^*x = (1,0)$$，$$\lVert x^*x \rVert = 1 = \lVert x \rVert^2$$，C\* 恒等式成立；交换共轭下 $$x^* = (0,1)$$，$$x^*x = (0,0)$$，$$\lVert x^*x \rVert = 0 \ne 1$$，恒等式崩掉。

为什么 $$\mathcal A_T$$ 这边自动不出问题？因为 $$\mathcal A_T$$ 是 $$\mathcal B(\mathbb{C}^2)$$ 的 \*-子代数，范数是**算子范数**，而算子满足
$$\lVert A \rVert^2 = \sup_{\lVert u \rVert \le 1}\langle Au, Au\rangle = \sup_{\lVert u\rVert\le1}\langle A^*Au, u\rangle \le \lVert A^*A \rVert \le \lVert A^* \rVert\lVert A \rVert = \lVert A \rVert^2 ,$$
两头相夹即 $$\lVert A^*A\rVert = \lVert A \rVert^2$$。**所以「具体算子代数」天然是 C\* 代数，C\* 恒等式不是外加的技术条件，而是「这个抽象代数确实来自算子」的判据**——这正是 Gelfand–Naimark 一般形式的内容（§4.5）。$$\blacksquare$$

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.**（含单位 Banach 代数总可以不妨设 $$\lVert e \rVert = 1$$）设 $$(\mathcal A, \lVert \cdot \rVert)$$ 是含单位元 $$e \ne 0$$ 的 Banach 代数。定义
$$\lVert a \rVert' = \sup \lbrace \lVert ab \rVert : b \in \mathcal A,\ \lVert b \rVert \le 1 \rbrace .$$
证明：

(i) $$\lVert \cdot \rVert'$$ 是 $$\mathcal A$$ 上的范数，且 $$\lVert e \rVert' = 1$$；

(ii) $$\lVert \cdot \rVert'$$ 满足次乘性 $$\lVert ab \rVert' \le \lVert a \rVert' \, \lVert b \rVert'$$；

(iii) $$\lVert \cdot \rVert'$$ 与 $$\lVert \cdot \rVert$$ 等价，具体地
$$\frac{\lVert a \rVert}{\lVert e \rVert} \le \lVert a \rVert' \le \lVert a \rVert \qquad \text{对一切 } a \in \mathcal A ;$$

(iv) $$(\mathcal A, \lVert \cdot \rVert')$$ 仍是 Banach 代数。

**基2.**（$$C(X)$$：Gelfand 表示退回为「取函数值」）设 $$X$$ 是紧 Hausdorff 空间，$$\mathcal A = C(X)$$ 装备上确界范数与逐点乘法，单位元是常函数 $$\mathbf 1$$。对 $$x \in X$$ 定义 $$\delta_x(f) = f(x)$$。

(i) 证明 $$\delta_x \in \Delta(\mathcal A)$$，且 $$\Gamma(f)(\delta_x) = f(x)$$；

(ii) 不引用 Gelfand 表示定理，直接证明：$$f$$ 在 $$\mathcal A$$ 中可逆 $$\iff$$ $$f(x) \ne 0$$ 对一切 $$x \in X$$；并由此算出 $$\sigma(f) = f(X)$$；

(iii) 用定理 3.12 (iv) 再算一遍 $$\sigma(f)$$，并核对两种算法给出同一个集合。

**基3.**（谱半径可以远小于范数）取 $$\mathcal A = \mathcal B(\mathbb{C}^2)$$，即 $$2 \times 2$$ 复矩阵代数，装备算子范数；取
$$a = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} .$$
(i) 证明 $$a^2 = 0$$，并直接算出 $$\sigma(a) = \lbrace 0 \rbrace$$、$$r(a) = 0$$；

(ii) 证明 $$\lVert a \rVert = 1$$，从而 $$r(a) < \lVert a \rVert$$；

(iii) 用谱半径公式（定理 3.5）验证 $$r(a) = \lim_{n \to \infty} \lVert a^n \rVert^{1/n} = 0$$；

(iv) 验证 C\* 恒等式在本例成立：$$\lVert a^* a \rVert = \lVert a \rVert^2$$。

**基4.**（$$\lVert a^*a \rVert = \lVert a \rVert^2$$ 的直接后果）设 $$\mathcal A$$ 是含单位的 C\* 代数。

(i) 证明对合保范：$$\lVert a^* \rVert = \lVert a \rVert$$；

(ii) 证明：若 $$a$$ 正规，则 $$\lVert a \rVert = r(a)$$；

(iii) 解释 基3 中的 $$a$$ 为什么绕开了 (ii)：验证 $$a^* a \ne a a^*$$。

### 竞赛（本课目标难度）

**竞1.**（$$\ell^1(\mathbb{Z})$$ 的 Gelfand 空间与 Wiener 引理）设 $$\mathcal A = \ell^1(\mathbb{Z})$$，乘法为卷积 $$(a * b)_n = \sum_{k \in \mathbb{Z}} a_k b_{n-k}$$，范数 $$\lVert a \rVert_1 = \sum_n \lvert a_n \rvert$$，单位元 $$\delta_0$$。对 $$z \in \mathbb{T} = \lbrace z \in \mathbb{C} : \lvert z \rvert = 1 \rbrace$$ 定义
$$\varphi_z(a) = \sum_{n \in \mathbb{Z}} a_n z^n .$$
(i) 证明 $$\varphi_z \in \Delta(\mathcal A)$$ 且 $$\lVert \varphi_z \rVert = 1$$；

(ii) 证明 $$\lVert \hat a \rVert_\infty \le \lVert a \rVert_1$$，并取 $$a = \delta_0 + \delta_1 - \delta_2$$ 算出两端，说明等号可以严格不成立；

(iii) 证明 $$\Delta(\mathcal A) = \lbrace \varphi_z : z \in \mathbb{T} \rbrace$$，并算出 $$\sigma(\delta_1) = \mathbb{T}$$、$$r(\delta_1) = \lVert \delta_1 \rVert_1 = 1$$；

(iv)（Wiener 引理）设 $$a \in \ell^1(\mathbb{Z})$$ 满足 $$\hat a(z) = \sum_n a_n z^n \ne 0$$ 对一切 $$z \in \mathbb{T}$$。证明 $$a$$ 在 $$\ell^1(\mathbb{Z})$$ 中可逆，即存在 $$b \in \ell^1(\mathbb{Z})$$ 使 $$a * b = \delta_0$$——等价地说，$$1/\hat a$$ 有绝对收敛的 Fourier 级数。

**竞2.**（谱映射定理）设 $$\mathcal A$$ 是含单位的交换 Banach 代数，$$a \in \mathcal A$$，$$p(z) = c_0 + c_1 z + \dots + c_m z^m$$ 是复系数多项式，$$p(a) = c_0 e + c_1 a + \dots + c_m a^m$$。

(i) 证明 $$\sigma(p(a)) = p(\sigma(a)) = \lbrace p(\lambda) : \lambda \in \sigma(a) \rbrace$$；

(ii) 由此证明 $$r(p(a)) = \max_{\lambda \in \sigma(a)} \lvert p(\lambda) \rvert$$；

(iii) 取 $$\mathcal A = C(X)$$、$$f \in C(X)$$，写出 (i) 在这时的具体形状。

**竞3.**（$$\Delta(C(X))$$ 与 $$X$$ 同胚）设 $$X$$ 是紧 Hausdorff 空间，$$\mathcal A = C(X)$$。

(i) 设 $$\mathfrak I \subsetneq \mathcal A$$ 是真理想。证明存在 $$x \in X$$ 使 $$f(x) = 0$$ 对一切 $$f \in \mathfrak I$$。（提示：若每个 $$x$$ 都有某个 $$f \in \mathfrak I$$ 在其上不为零，用紧性取出有限个 $$f_1, \dots, f_k \in \mathfrak I$$ 无公共零点，再考察 $$g = f_1\overline{f_1} + \dots + f_k\overline{f_k}$$。）

(ii) 证明 $$\Delta(\mathcal A) = \lbrace \delta_x : x \in X \rbrace$$，且 $$x \mapsto \delta_x$$ 是 $$X \to \Delta(\mathcal A)$$ 的同胚（$$\Delta$$ 上取 Gelfand 拓扑）；

(iii) 证明在这个对应下 $$\Gamma(f)(\delta_x) = f(x)$$，于是 $$\lVert \Gamma(f) \rVert_\infty = \lVert f \rVert_\infty$$。

**竞4.**（根、表示的单射性、以及 C\* 恒等式不可省）设 $$\mathcal A$$ 是含单位的交换 Banach 代数，$$\mathrm{rad}(\mathcal A) = \bigcap_{\varphi \in \Delta(\mathcal A)} \ker \varphi$$。

(i) 证明 $$\mathrm{rad}(\mathcal A) = \lbrace a : r(a) = 0 \rbrace = \lbrace a : \sigma(a) = \lbrace 0 \rbrace \rbrace$$；

(ii) 证明 $$\Gamma$$ 单射 $$\iff$$ $$\mathrm{rad}(\mathcal A) = \lbrace 0 \rbrace$$；

(iii) 取 $$\mathcal A = \mathbb{C}[\varepsilon]/(\varepsilon^2) = \lbrace u + v\varepsilon : u, v \in \mathbb{C} \rbrace$$，乘法由 $$\varepsilon^2 = 0$$ 决定，范数 $$\lVert u + v\varepsilon \rVert = \lvert u \rvert + \lvert v \rvert$$。证明 $$\mathcal A$$ 是含单位的交换 Banach 代数，算出 $$\Delta(\mathcal A)$$ 恰含一点、$$\mathrm{rad}(\mathcal A) = \mathbb{C}\varepsilon$$，于是 $$\Gamma$$ 既不是单射也不是等距。

**竞5.**（Arens 引理：那一步到底用了什么）设 $$\mathcal A$$ 是含单位的交换 C\* 代数，$$\varphi \in \Delta(\mathcal A)$$。

(i) 设 $$a = a^*$$。**不借助命题 3.15 的自伴分解**，证明 $$\varphi(a) \in \mathbb{R}$$，从而 $$\sigma(a) \subset \mathbb{R}$$。（提示：对 $$t \in \mathbb{R}$$ 考察 $$b = a + ite$$，把 $$\lvert \varphi(b) \rvert$$ 与 $$\lVert b \rVert$$ 比较，而不是与 $$\lVert b^*b \rVert$$ 比较。）

(ii) 指出 (i) 中哪一步用掉了 C\* 恒等式，并说明它不能被「带对合、且对合保范」替代。取 $$\mathcal A_0 = \mathbb{C}^2$$（逐分量乘法、上确界范数）与对合 $$(z,w)^* = (\bar w, \bar z)$$，验证：

(a) $$\mathcal A_0$$ 是含单位的交换 Banach 代数，且 $$\lVert x^* \rVert = \lVert x \rVert$$ 对一切 $$x$$；(b) $$a = (1+i, 1-i)$$ 满足 $$a^* = a$$；(c) 特征 $$\varphi_1(z,w) = z$$ 给出 $$\varphi_1(a) = 1 + i \notin \mathbb{R}$$，于是这个自伴元的谱不落在实轴上；(d) C\* 恒等式在 $$\mathcal A_0$$ 上失效：取 $$x = (1,2)$$，算出 $$\lVert x^*x \rVert$$ 与 $$\lVert x \rVert^2$$ 并比较。

### 研究（通向下一章）

**研1.**（无单位：局部紧空间与 $$C_0(X)$$）设 $$\mathcal A$$ 是不含单位的交换 Banach 代数。作**单位化 (unitalization)** $$\mathcal A_1 = \mathcal A \oplus \mathbb{C}$$，元素写成 $$a + \lambda \mathbf 1$$，乘法为
$$(a + \lambda \mathbf 1)(b + \mu \mathbf 1) = (ab + \lambda b + \mu a) + \lambda\mu \mathbf 1,$$
范数取 $$\lVert a + \lambda \mathbf 1 \rVert_1 = \lVert a \rVert + \lvert \lambda \rvert$$。

(i) 证明 $$\mathcal A_1$$ 是含单位的交换 Banach 代数，$$e_1 = \mathbf 1$$ 是其单位元，而 $$\mathcal A$$ 是 $$\mathcal A_1$$ 的闭理想；

(ii) 证明 $$\varphi_\infty(a + \lambda \mathbf 1) = \lambda$$ 是 $$\mathcal A_1$$ 的特征，且限制映射 $$\varphi \mapsto \varphi\vert_{\mathcal A}$$ 是 $$\Delta(\mathcal A_1) \setminus \lbrace \varphi_\infty \rbrace$$ 到 $$\Delta(\mathcal A)$$ 的同胚；

(iii) 由此证明 $$\Delta(\mathcal A)$$ 局部紧 Hausdorff，且对每个 $$a \in \mathcal A$$，$$\hat a$$ 在无穷远处趋于零，即 $$\Gamma(\mathcal A) \subset C_0(\Delta(\mathcal A))$$；

(iv) 说明「代数缺一个单位元」与「无界算子的定义域不是全空间」是同一类现象的两个面相。

**研2.**（Cayley 变换：把自伴算子换成酉算子）设 $$H$$ 是复 Hilbert 空间，$$T \in \mathcal B(H)$$ 自伴。

(i) 证明 $$T + iI$$ 可逆（提示：定理 3.21 给出 $$\sigma(T) \subset \mathbb{R}$$，故 $$-i \notin \sigma(T)$$）；

(ii) 令 $$U = (T - iI)(T + iI)^{-1}$$。证明 $$U$$ 是酉算子，并算出 $$I - U = 2i(T + iI)^{-1}$$，从而 $$I - U$$ 可逆；

(iii) 证明 $$T = i(I + U)(I - U)^{-1}$$；

(iv) 证明 $$\sigma(T) = \lbrace i\,\frac{1 + \zeta}{1 - \zeta} : \zeta \in \sigma(U) \rbrace$$。

### 解答 (Solutions)

**解 基1.** 这个 $$\lVert \cdot \rVert'$$ 就是把「算子范数」搬到抽象代数上的写法：在 $$\mathcal B(H)$$ 里它恰好就是原来的范数。先确认它有限。

(i) **有限性**：对 $$\lVert b \rVert \le 1$$，由次乘性 $$\lVert ab \rVert \le \lVert a \rVert \lVert b \rVert \le \lVert a \rVert$$，故右端集合有上界，$$\lVert a \rVert'$$ 是有限实数。

**齐次性**：$$\lVert \lambda a \rVert' = \sup_{\lVert b \rVert \le 1} \lVert \lambda ab \rVert = \lvert \lambda \rvert \sup_{\lVert b \rVert \le 1} \lVert ab \rVert = \lvert \lambda \rvert \lVert a \rVert'$$。

**三角不等式**：对 $$\lVert b \rVert \le 1$$，$$\lVert (a + a')b \rVert = \lVert ab + a'b \rVert \le \lVert ab \rVert + \lVert a'b \rVert$$；对 $$b$$ 取上确界得 $$\lVert a + a' \rVert' \le \lVert a \rVert' + \lVert a' \rVert'$$。

**非退化**：若 $$\lVert a \rVert' = 0$$，则 $$\lVert ab \rVert = 0$$ 对一切 $$\lVert b \rVert \le 1$$，故 $$ab = 0$$。取 $$b_0 = e/\lVert e \rVert$$（$$\lVert b_0 \rVert = 1$$，因 $$e \ne 0$$），得 $$a = ab_0 = 0$$。

最后 $$\lVert e \rVert' = \sup_{\lVert b \rVert \le 1} \lVert eb \rVert = \sup_{\lVert b \rVert \le 1} \lVert b \rVert = 1$$。

(ii) 记 $$M = \lVert b \rVert' = \sup_{\lVert c \rVert \le 1} \lVert bc \rVert$$。若 $$M = 0$$，由 (i) 的非退化论证（用于 $$b$$）得 $$b = 0$$，此时待证不等式是 $$0 \le \lVert a \rVert' \lVert b \rVert'$$，成立。以下设 $$M > 0$$。

任取 $$\lVert c \rVert \le 1$$。若 $$bc = 0$$，则 $$\lVert a(bc) \rVert = 0 \le M \lVert a \rVert'$$。若 $$bc \ne 0$$，令 $$d = bc/\lVert bc \rVert$$，则 $$\lVert d \rVert = 1$$，于是
$$\lVert a(bc) \rVert = \lVert bc \rVert \, \lVert ad \rVert \le M \cdot \lVert a \rVert' ,$$
其中用了 $$\lVert bc \rVert \le M$$ 与 $$\lVert ad \rVert \le \lVert a \rVert'$$（后者由 $$\lVert d \rVert = 1$$）。对 $$\lVert c \rVert \le 1$$ 取上确界：
$$\lVert ab \rVert' = \sup_{\lVert c \rVert \le 1} \lVert (ab)c \rVert = \sup_{\lVert c \rVert \le 1} \lVert a(bc) \rVert \le M \lVert a \rVert' = \lVert b \rVert' \lVert a \rVert' .$$

**要点**：归一化必须用 $$M = \lVert b \rVert'$$，不能用原始范数 $$\lVert b \rVert$$；两者只差一个常数因子，用错了方向就得不到次乘性。这正是「$$\lVert \cdot \rVert'$$ 与自己的乘积运算相容」的实质。

(iii) 上界已由 (i) 的第一段给出：$$\lVert a \rVert' \le \lVert a \rVert$$。下界：$$b_0 = e/\lVert e \rVert$$ 满足 $$\lVert b_0 \rVert = 1$$，故
$$\lVert a \rVert' \ge \lVert ab_0 \rVert = \frac{\lVert ae \rVert}{\lVert e \rVert} = \frac{\lVert a \rVert}{\lVert e \rVert} .$$
两式合并即得所述夹逼。$$\lVert e \rVert > 0$$ 是常数，故两范数互相控制，诱导同样的拓扑（及同样的收敛序列）。

(iv) 两范数等价，因此 $$(a_n)$$ 在 $$\lVert \cdot \rVert'$$ 下是 Cauchy 列 $$\iff$$ 在 $$\lVert \cdot \rVert$$ 下是 Cauchy 列。后者按 $$\mathcal A$$ 的完备性收敛于某 $$a \in \mathcal A$$；由等价性，$$\lVert a_n - a \rVert' \to 0 \iff \lVert a_n - a \rVert \to 0$$，故该列在 $$\lVert \cdot \rVert'$$ 下也收敛于 $$a$$。乘法连续性由次乘性与范数等价性给出，次乘性已在 (ii) 验证。于是 $$(\mathcal A, \lVert \cdot \rVert')$$ 是 Banach 代数，且 $$\lVert e \rVert' = 1$$。$$\blacksquare$$

**注（基1 说明了什么）** 本章开头约定「总是假设 Banach 代数含单位，且 $$\lVert e \rVert = 1$$」，基1 表明这个约定**不失一般性**：任何含单位的 Banach 代数都能改造成 $$\lVert e \rVert = 1$$，而乘法、可逆性、谱、$$\Delta(\mathcal A)$$ 全部是拓扑不变的对象，在等价范数下原样保留。特别地，$$\mathcal B(H)$$ 的算子范数本身就是对自己的 $$\lVert \cdot \rVert'$$：$$\lVert T \rVert = \sup \lbrace \lVert Tb \rVert : \lVert b \rVert \le 1 \rbrace$$，这就解释了为什么它有 $$\lVert I \rVert = 1$$。

**解 基2.**

(i) $$\delta_x$$ 线性（逐点加法与数乘）、保乘法（逐点乘法）、且 $$\delta_x(\mathbf 1) = 1 \ne 0$$，故按定义 3.9，$$\delta_x \in \Delta(\mathcal A)$$。由定义 3.11，$$\Gamma(f)(\delta_x) = \delta_x(f) = f(x)$$。

(ii) **（$$\Rightarrow$$）** 设 $$f$$ 可逆，即有 $$g \in C(X)$$ 使 $$fg = \mathbf 1$$。逐点取值：$$f(x)g(x) = 1$$ 对一切 $$x$$，故 $$f(x) \ne 0$$ 处处。

**（$$\Leftarrow$$）** 设 $$f(x) \ne 0$$ 对一切 $$x \in X$$。因 $$X$$ 紧、$$\lvert f \rvert$$ 连续，命题「连续实值函数在紧集上达到最小值」给出
$$m = \min_{x \in X} \lvert f(x) \rvert > 0 .$$
令 $$g(x) = 1/f(x)$$。$$g$$ 连续：可写成 $$g = \overline{f}/\lvert f \rvert^2$$，分母 $$\lvert f \rvert^2 \ge m^2 > 0$$ 是连续函数且处处不为零，商的连续性可用。又 $$f(x)g(x) = 1$$ 对一切 $$x$$，即 $$fg = \mathbf 1$$，故 $$f$$ 可逆。

于是
$$\sigma(f) = \lbrace \lambda : \lambda\mathbf 1 - f \notin G(\mathcal A) \rbrace = \lbrace \lambda : \lambda - f(x) = 0 \text{ 对某个 } x \in X \rbrace = \lbrace f(x) : x \in X \rbrace = f(X) ,$$
其中第二个等号把 (ii) 的结论用在函数 $$\lambda\mathbf 1 - f$$（其取值是 $$\lambda - f(x)$$）上。

(iii) 由定理 3.12 (iv)，
$$\sigma(f) = \Gamma(f)(\Delta(\mathcal A)) = \lbrace \Gamma(f)(\varphi) : \varphi \in \Delta(\mathcal A) \rbrace .$$
由 (i)，取 $$\varphi = \delta_x$$ 得到的值正是 $$f(x)$$，所以 $$\lbrace \Gamma(f)(\delta_x) : x \in X \rbrace = f(X) \subseteq \sigma(f)$$——这一步已经把 $$\supseteq$$ 做出来了。要得到等号，还需要知道 $$\Delta(C(X))$$ 里没有别的点，即 $$\Delta(C(X)) = \lbrace \delta_x : x \in X \rbrace$$：这正是 竞3 (ii)。代入便得
$$\sigma(f) = \Gamma(f)(\lbrace \delta_x : x \in X \rbrace) = \lbrace f(x) : x \in X \rbrace = f(X) ,$$
与 (ii) 的直接计算一致。两处都用到「$$X$$ 紧」：一处保证 $$\min \lvert f \rvert$$ 被取到，一处（竞3 (i)）保证理想能收缩到一个点。

**解 基3.**

(i) 直接相乘：
$$a^2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = 0 .$$

于是对 $$\lambda \ne 0$$，直接验证
$$(\lambda I - a) \cdot \lambda^{-1}\Big(I + \frac{a}{\lambda}\Big) = \lambda^{-1}(\lambda I - a)\Big(I + \frac{a}{\lambda}\Big) = \lambda^{-1}\Big(\lambda I + a - a - \frac{a^2}{\lambda}\Big) = I ,$$
同样地 $$\lambda^{-1}(I + a/\lambda)(\lambda I - a) = I$$，故 $$\lambda I - a$$ 可逆，$$\lambda \notin \sigma(a)$$。

而 $$0 \in \sigma(a)$$：$$-a \ne 0$$ 是幂零元，若存在 $$c$$ 使 $$ac = I$$，则 $$a^2c = a$$，左端为 $$0$$、右端为 $$a \ne 0$$，矛盾。故 $$a$$ 不可逆。于是 $$\sigma(a) = \lbrace 0 \rbrace$$，$$r(a) = \sup_{\lambda \in \sigma(a)} \lvert \lambda \rvert = 0$$。

(ii) 记 $$\lVert \cdot \rVert$$ 为 $$\mathbb{C}^2$$ 的 Euclid 范数对应的算子范数，$$e_1 = (1,0)$$、$$e_2 = (0,1)$$ 是标准正交基。$$ae_2 = e_1$$，故
$$\lVert a \rVert = \sup_{\lVert x \rVert \le 1} \lVert ax \rVert \ge \lVert ae_2 \rVert = \lVert e_1 \rVert = 1 .$$
另一方面对 $$x = x_1e_1 + x_2e_2$$ 有 $$ax = x_2e_1$$，$$\lVert ax \rVert = \lvert x_2 \rvert \le \lVert x \rVert$$，故 $$\lVert a \rVert \le 1$$。合并得 $$\lVert a \rVert = 1$$，于是 $$r(a) = 0 < 1 = \lVert a \rVert$$。

(iii) $$a^2 = 0$$ 给出 $$a^n = 0$$ 对一切 $$n \ge 2$$，故 $$\lVert a^n \rVert^{1/n} = 0$$ 对一切 $$n \ge 2$$，从而
$$\lim_{n \to \infty} \lVert a^n \rVert^{1/n} = 0 = r(a) .$$
定理 3.5 在这里的读法是：谱半径由**幂的增长速率**决定，而不是由 $$a$$ 本身的大小决定。$$a$$ 的范数是 $$1$$（甚至在每个单位向量上「满值」），但幂立刻死掉，谱半径因此塌成 $$0$$。这与 $$r(a) \le \lVert a \rVert$$（命题 3.4 (i)）相容——那里本来就只有不等号。

(iv) $$a^* = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$$，故
$$a^*a = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}, \qquad aa^* = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} .$$
两者都是正交投影，算子范数都是 $$1$$。于是 $$\lVert a^*a \rVert = 1 = \lVert a \rVert^2$$，C\* 恒等式成立。

**解 基4.** 思路：整个 (ii) 的发动机是一串**精确**的等式 $$\lVert a^{2^n} \rVert = \lVert a \rVert^{2^n}$$，它是用 (i) 的自伴情形一步步乘方得来的；再把这个子列喂给谱半径公式，$$2$$ 次根的齐次性恰好把指数消平。

(i) 由 C\* 恒等式与次乘性，
$$\lVert a \rVert^2 = \lVert a^*a \rVert \le \lVert a^* \rVert \lVert a \rVert .$$
若 $$\lVert a \rVert \ne 0$$，两边除以 $$\lVert a \rVert$$ 得 $$\lVert a \rVert \le \lVert a^* \rVert$$。把这条不等式用在 $$a^*$$ 上，注意 $$(a^*)^* = a$$，得 $$\lVert a^* \rVert \le \lVert a \rVert$$。两向合并即得 $$\lVert a^* \rVert = \lVert a \rVert$$。若 $$\lVert a \rVert = 0$$，则 $$a = 0$$、$$a^* = 0$$，等号同样成立。

(ii) **第一步：自伴元的情形。** 设 $$s^* = s$$。则 $$s^*s = s^2$$，C\* 恒等式给出 $$\lVert s^2 \rVert = \lVert s \rVert^2$$。对它归纳：$$s^{2^n}$$ 仍是自伴元（$$(s^{2^n})^* = (s^*)^{2^n} = s^{2^n}$$），故
$$\lVert s^{2^{n+1}} \rVert = \lVert (s^{2^n})^2 \rVert = \lVert s^{2^n} \rVert^2 ,$$
于是 $$\lVert s^{2^n} \rVert = \lVert s \rVert^{2^n}$$ 对一切 $$n \ge 0$$ 成立。

**第二步：正规元的情形。** 设 $$a^*a = aa^*$$。先算 $$n = 1$$ 这一步。注意 $$a^*a$$ 自伴，且
$$(a^2)^*(a^2) = (a^*)^2a^2 = a^*(a^*a)a = a^*(aa^*)a = (a^*a)(a^*a) = (a^*a)^2 ,$$
中间两次把 $$a^*a$$ 与 $$aa^*$$ 互换（正规性），使因子可以重排成同一串。于是由第一步（用于自伴元 $$s = a^*a$$）
$$\lVert a^2 \rVert^2 = \lVert (a^2)^*a^2 \rVert = \lVert (a^*a)^2 \rVert = \lVert a^*a \rVert^2 = \lVert a \rVert^4 ,$$
故 $$\lVert a^2 \rVert = \lVert a \rVert^2$$。又正规元的幂仍正规，于是对每个 $$n$$ 有
$$\lVert a^{2^{n+1}} \rVert = \lVert (a^{2^n})^2 \rVert = \lVert a^{2^n} \rVert^2 ,$$
归纳得 $$\lVert a^{2^n} \rVert = \lVert a \rVert^{2^n}$$ 对一切 $$n \ge 0$$。

**第三步：喂给谱半径公式。** 定理 3.5 说 $$\lVert a^m \rVert^{1/m}$$ 的极限存在。取子列 $$m = 2^n$$：极限与子列极限相同，故
$$r(a) = \lim_{m \to \infty} \lVert a^m \rVert^{1/m} = \lim_{n \to \infty} \lVert a^{2^n} \rVert^{1/2^n} = \lim_{n \to \infty} \big(\lVert a \rVert^{2^n}\big)^{1/2^n} = \lVert a \rVert . \qquad \blacksquare$$

(iii) 由 基3 (iv) 已算出
$$a^*a = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \ne \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = aa^* ,$$
所以 $$a$$ 不正规，(ii) 的假设不成立，结论自然不必成立——而它确实不成立：$$\lVert a \rVert = 1$$ 而 $$r(a) = 0$$。这说明 (ii) 中「正规」这一条不能换成更弱的条件，也说明 $$\lVert a \rVert = r(a)$$ 不是范数的普遍性质，是 C\* 恒等式加交换性（或正规性）挣来的。

**解 竞1.** 关键 leap 在 (iii)：$$\ell^1(\mathbb{Z})$$ 的对偶是 $$\ell^\infty(\mathbb{Z})$$，于是每个特征都对应一个**有界数列** $$c = (c_n)$$，乘性条件 $$\varphi(a*b) = \varphi(a)\varphi(b)$$ 翻译成数列方程 $$c_{m+n} = c_m c_n$$；这是 $$\mathbb{Z}$$ 上的乘法函数方程，解只有 $$c_n = z^n$$，而有界性把 $$z$$ 钉在圆周上。认出 $$\Delta(\mathcal A) = \mathbb{T}$$ 之后，(iv) 就只是定理 3.12 (iv) 的一句话推论。

(i) **有定义与线性**：$$\sum_n \lvert a_n z^n \rvert = \sum_n \lvert a_n \rvert = \lVert a \rVert_1 < \infty$$，故级数绝对收敛，$$\varphi_z$$ 线性。

**乘性**：把 $$n = k + j$$ 代入并按 $$k$$ 重排，
$$\varphi_z(a * b) = \sum_{n} \Big(\sum_{k} a_k b_{n-k}\Big) z^n = \sum_{k} a_k z^k \sum_{j} b_j z^{j} = \varphi_z(a)\varphi_z(b) ,$$
重排合法是因为重级数绝对收敛（$$\sum_{k,j}\lvert a_k\rvert \lvert b_j \rvert = \lVert a \rVert_1 \lVert b \rVert_1 < \infty$$）。

**非零**：$$\varphi_z(\delta_0) = z^0 = 1$$。故 $$\varphi_z \in \Delta(\mathcal A)$$。

**范数**：由 $$\lvert \varphi_z(a) \rvert \le \sum_n \lvert a_n \rvert = \lVert a \rVert_1$$ 得 $$\lVert \varphi_z \rVert \le 1$$；又 $$\lVert \delta_0 \rVert_1 = 1$$ 且 $$\varphi_z(\delta_0) = 1$$ 得 $$\lVert \varphi_z \rVert \ge 1$$。故 $$\lVert \varphi_z \rVert = 1$$，与定理 3.10 (ii) 一致。

(ii) 上界 $$\lVert \hat a \rVert_\infty = \sup_z \lvert \varphi_z(a) \rvert \le \lVert a \rVert_1$$ 就是 (i) 的估计。

取 $$a = \delta_0 + \delta_1 - \delta_2$$（即 $$a_0 = 1$$、$$a_1 = 1$$、$$a_2 = -1$$，其余为 $$0$$）：$$\lVert a \rVert_1 = 1 + 1 + 1 = 3$$。而
$$\hat a(z) = 1 + z - z^2 .$$
把 $$\lvert \hat a(z) \rvert^2$$ 展开（$$\lvert z \rvert = 1$$，故 $$\bar z = z^{-1}$$）：
$$\lvert \hat a(z) \rvert^2 = (1 + z - z^2)(1 + z^{-1} - z^{-2}) = 3 - z^2 - z^{-2} = 3 - 2\cos 2\theta , \qquad z = e^{i\theta} .$$
（$$z$$ 与 $$z^{-1}$$ 的一次交叉项各有两个，成对相消；常数项有三个，各给 $$1$$。）右端在 $$\cos 2\theta = -1$$ 时取最大值 $$5$$，故 $$\lVert \hat a \rVert_\infty = \sqrt 5$$。于是
$$\lVert \hat a \rVert_\infty = \sqrt 5 < 3 = \lVert a \rVert_1 ,$$
等号确实可以严格不成立。顺带指出：$$\ell^1(\mathbb{Z})$$ 上的这个对合**不**满足 C\* 恒等式，所以它与 $$C(X)$$、$$\mathcal B(H)$$ 是不同的物种。取 $$a = \delta_0 + i\delta_1 + \delta_2$$，则 $$a^* = \delta_0 - i\delta_{-1} + \delta_{-2}$$，逐项相乘得
$$a^*a = \delta_{-2} + 3\delta_0 + \delta_2 , \qquad \lVert a^*a \rVert_1 = 1 + 3 + 1 = 5 \ne 9 = \lVert a \rVert_1^2 .$$
本小题只用到上面那个数值比较；「$$\ell^1(\mathbb{Z})$$ 不是 C\* 代数」这一点在 (iv) 与 竞4 里会有回响。

(iii) 设 $$\varphi \in \Delta(\mathcal A)$$。由定理 3.10 (ii)，$$\varphi$$ 是范数 $$1$$ 的有界线性泛函。$$\ell^1(\mathbb{Z})$$ 的对偶是 $$\ell^\infty(\mathbb{Z})$$（等距同构：每个有界线性泛函都形如 $$\psi_c(a) = \sum_n a_n c_n$$，$$c \in \ell^\infty(\mathbb{Z})$$，且 $$\lVert \psi_c \rVert = \lVert c \rVert_\infty$$），故存在 $$c \in \ell^\infty(\mathbb{Z})$$ 使
$$\varphi(a) = \sum_{n} a_n c_n \quad \text{对一切 } a \in \ell^1(\mathbb{Z}), \qquad \lVert c \rVert_\infty = \lVert \varphi \rVert = 1 .$$
把 $$a = \delta_m$$ 代入得 $$\varphi(\delta_m) = c_m$$。由 $$\delta_m * \delta_n = \delta_{m+n}$$ 与 $$\varphi$$ 的乘性，
$$c_{m+n} = \varphi(\delta_{m+n}) = \varphi(\delta_m * \delta_n) = \varphi(\delta_m)\varphi(\delta_n) = c_mc_n \qquad \text{对一切 } m, n \in \mathbb{Z} .$$
取 $$m = n = 0$$：$$c_0 = c_0^2$$；又 $$\varphi(\delta_0) = \varphi(e) = 1$$（定义 3.9 之后的说明），故 $$c_0 = 1$$。取 $$m = 1, n = -1$$：$$c_1c_{-1} = 1$$。而 $$\lvert c_n \rvert \le \lVert c \rVert_\infty = 1$$ 对一切 $$n$$，两个模 $$\le 1$$ 的复数之积为 $$1$$，只能 $$\lvert c_1 \rvert = \lvert c_{-1} \rvert = 1$$。记 $$z = c_1 \in \mathbb{T}$$，则 $$c_{-1} = z^{-1}$$，并由乘法方程归纳得
$$c_n = z^n \quad (n \ge 0), \qquad c_{-n} = (z^{-1})^{n} = z^{-n} \quad (n \ge 0),$$
即 $$c_n = z^n$$ 对一切 $$n \in \mathbb{Z}$$。于是
$$\varphi(a) = \sum_n a_n z^n = \varphi_z(a) ,$$
即 $$\varphi = \varphi_z$$。反之由 (i) 每个 $$\varphi_z$$ 都是特征，故
$$\Delta(\mathcal A) = \lbrace \varphi_z : z \in \mathbb{T} \rbrace .$$
参数还是一一对应的：$$z = \varphi(\delta_1)$$ 能从 $$\varphi$$ 反解回来。并且 $$z \mapsto \varphi_z$$ 连续（弱\*拓扑下 $$\varphi_z(a) = \sum_n a_n z^n$$ 关于 $$z$$ 连续），$$\mathbb{T}$$ 紧、$$\Delta(\mathcal A)$$ Hausdorff，连续双射即同胚。

由 $$\hat{\delta_1}(\varphi_z) = \varphi_z(\delta_1) = z$$ 与定理 3.12 (iv)，
$$\sigma(\delta_1) = \lbrace \hat{\delta_1}(\varphi) : \varphi \in \Delta(\mathcal A) \rbrace = \lbrace z : z \in \mathbb{T} \rbrace = \mathbb{T}, \qquad r(\delta_1) = \lVert \hat{\delta_1} \rVert_\infty = 1 = \lVert \delta_1 \rVert_1 .$$
（$$r(\delta_1) = \lVert \delta_1 \rVert_1$$ 是巧合：一般地由 (ii) 只知 $$r(a) \le \lVert a \rVert_1$$。）

(iv) 先立一条引理，它在任何含单位的交换 Banach 代数里都成立：

**（可逆性判据）** $$a \in G(\mathcal A) \iff \varphi(a) \ne 0$$ 对一切 $$\varphi \in \Delta(\mathcal A)$$。

**证明**：若 $$a$$ 可逆则 $$\varphi(a)\varphi(a^{-1}) = \varphi(e) = 1$$，故 $$\varphi(a) \ne 0$$。反之设 $$a$$ 不可逆。则由 $$a$$ 生成的理想 $$a\mathcal A = \lbrace ac : c \in \mathcal A \rbrace$$ 是真理想：它是子空间、被 $$\mathcal A$$ 吸收（交换性保证左吸收与右吸收一致），且不含 $$e$$（否则 $$ac = e$$，$$a$$ 可逆）。由 Zorn 引理（注 3.13）把 $$a\mathcal A$$ 扩成极大理想 $$\mathfrak I$$；由定理 3.10 (i)，$$\mathfrak I = \ker\varphi$$ 对某 $$\varphi \in \Delta(\mathcal A)$$。而 $$a = ae \in a\mathcal A \subseteq \mathfrak I$$，故 $$\varphi(a) = 0$$。取逆否即得。$$\blacksquare$$

现在设 $$\hat a(z) \ne 0$$ 对一切 $$z \in \mathbb{T}$$。由 (iii) 的 $$\Delta(\mathcal A) = \lbrace \varphi_z\rbrace$$，这句话就是说 $$\varphi(a) \ne 0$$ 对一切 $$\varphi \in \Delta(\mathcal A)$$。由上一条引理，$$a \in G(\mathcal A)$$，即存在 $$b \in \ell^1(\mathbb{Z})$$ 使
$$a * b = b * a = \delta_0 .$$
逐项写出 $$a * b = \delta_0$$ 就是 $$\sum_k a_k b_{n-k} = \delta_0(n)$$ 对一切 $$n$$，也就是说 $$1/\hat a$$ 的 Fourier 级数（系数为 $$b$$）绝对可和，且它就是 $$b$$ 的 Gelfand 表示。这正是 Wiener 引理：$$\mathbb{T}$$ 上处处不为零的绝对收敛 Fourier 级数，其倒数仍是绝对收敛的 Fourier 级数。$$\blacksquare$$

**解 竞2.** 关键 leap：不要直接对 $$p(a)$$ 求逆，而是**把问题搬到函数层面**——定理 3.12 (iii) 说 $$\Gamma$$ 保乘法，于是「对 $$a$$ 取多项式」这件事在 Gelfand 表示下变成「对函数 $$\hat a$$ 逐点取同一个多项式」。

(i) 由定理 3.12 (iii)，$$\hat e = \mathbf 1$$、$$\widehat{ab} = \hat a\hat b$$，归纳得 $$\widehat{a^m} = (\hat a)^m$$（$$m \ge 0$$）。再由 $$\Gamma$$ 的线性，
$$\widehat{p(a)}(\varphi) = c_0 + c_1\hat a(\varphi) + \dots + c_m\hat a(\varphi)^m = p(\hat a(\varphi)) \qquad (\varphi \in \Delta(\mathcal A)),$$
即 $$\widehat{p(a)} = p \circ \hat a$$。

把定理 3.12 (iv) 用于元素 $$p(a)$$，再用刚算出的表示：
$$\sigma(p(a)) = \widehat{p(a)}(\Delta(\mathcal A)) = (p \circ \hat a)(\Delta(\mathcal A)) = p\big(\hat a(\Delta(\mathcal A))\big) = p(\sigma(a)) ,$$
最后一个等号是定理 3.12 (iv) 用于 $$a$$。

(ii) 由 $$r(b) = \lVert \hat b \rVert_\infty$$（定理 3.12 (iv)）与 (i)，
$$r(p(a)) = \lVert \widehat{p(a)} \rVert_\infty = \lVert p \circ \hat a \rVert_\infty = \sup_{\varphi \in \Delta(\mathcal A)} \lvert p(\hat a(\varphi)) \rvert = \sup_{\lambda \in \sigma(a)} \lvert p(\lambda) \rvert = \max_{\lambda \in \sigma(a)} \lvert p(\lambda) \rvert ,$$
末一步把上确界写成最大值：$$\sigma(a)$$ 是紧集（命题 3.4 (i)），$$\lvert p \rvert$$ 连续，故上确界在 $$\sigma(a)$$ 的某点被取到。（同样地，$$\Delta(\mathcal A)$$ 紧、$$p \circ \hat a$$ 连续。）

(iii) 取 $$\mathcal A = C(X)$$。由 竞3 (ii)，$$\Delta(C(X)) = \lbrace \delta_x : x \in X \rbrace$$，且 $$\hat f(\delta_x) = f(x)$$，于是 (i) 变成
$$\sigma(p \circ f) = \lbrace p(f(x)) : x \in X \rbrace = (p \circ f)(X) .$$
最简情形 $$X = [0,1]$$、$$f(x) = x$$ 给出 $$\sigma(p) = p([0,1])$$：多项式的谱就是它在 $$[0,1]$$ 上的值域，与 基2 (ii) 一致。

**解 竞3.** 关键 leap 在 (i)：把「理想是真理想」这个**全局代数条件**翻译成「有公共零点」这个**逐点几何结论**。桥是紧性加一个免费的正元素：在 $$C(X)$$ 里 $$\overline{f}$$ 总是合法的，因此 $$f\overline{f} = \lvert f \rvert^2$$ 随手可得——在抽象 C\* 代数里这一步要靠 C\* 恒等式供给（见 竞5），这里则是现成的。

(i) 反设：每个 $$x \in X$$ 都有某个 $$f \in \mathfrak I$$ 使 $$f(x) \ne 0$$。对每个 $$x$$ 挑定一个这样的 $$f_x \in \mathfrak I$$。集合 $$\lbrace \lvert f_x \rvert > 0 \rbrace$$ 是 $$x$$ 的开邻域，全体构成 $$X$$ 的开覆盖。由 $$X$$ 紧，取有限子覆盖，即存在 $$x_1, \dots, x_k \in X$$ 使
$$\lbrace \lvert f_{x_1} \rvert > 0 \rbrace \cup \dots \cup \lbrace \lvert f_{x_k} \rvert > 0 \rbrace = X .$$
记 $$f_i = f_{x_i} \in \mathfrak I$$，令
$$g = f_1\overline{f_1} + \dots + f_k\overline{f_k} = \lvert f_1 \rvert^2 + \dots + \lvert f_k \rvert^2 .$$
$$g$$ 连续、处处 $$\ge 0$$；由覆盖关系，每个 $$x$$ 至少落在一个 $$\lbrace \lvert f_i \rvert > 0\rbrace$$ 里，故 $$g(x) > 0$$ 对一切 $$x$$。又每一项 $$f_i\overline{f_i}$$ 形如（$$\mathfrak I$$ 中元素）乘以（$$\mathcal A$$ 中元素）——因为 $$\overline{f_i} \in C(X) = \mathcal A$$——被理想吸收，故 $$g \in \mathfrak I$$。由 基2 (ii)，处处不为零的 $$g$$ 在 $$\mathcal A$$ 中可逆。于是 $$\mathfrak I$$ 含可逆元，由命题 3.7 (i) 得 $$\mathfrak I = \mathcal A$$，与 $$\mathfrak I$$ 真矛盾。故存在 $$x \in X$$ 使 $$f(x) = 0$$ 对一切 $$f \in \mathfrak I$$。

(ii) **（$$\supseteq$$）** 由 基2 (i)，每个 $$\delta_x$$ 都是特征，故 $$\lbrace \delta_x : x \in X\rbrace \subseteq \Delta(\mathcal A)$$。

**（$$\subseteq$$）** 设 $$\varphi \in \Delta(\mathcal A)$$，$$\mathfrak I = \ker\varphi$$。因 $$\varphi(\mathbf 1) = 1 \ne 0$$，$$\mathfrak I$$ 是真理想；由 (i) 存在 $$x \in X$$ 使 $$f(x) = 0$$ 对一切 $$f \in \mathfrak I$$，即 $$\mathfrak I \subseteq \ker\delta_x$$。而 $$\ker\delta_x$$ 也是真理想，故由 $$\mathfrak I$$ 的极大性（定理 3.10 (i)）得 $$\mathfrak I = \ker\delta_x$$；再由定理 3.10 (i) 中「$$\varphi \mapsto \ker\varphi$$ 是单射」得 $$\varphi = \delta_x$$。

于是 $$\Delta(\mathcal A) = \lbrace \delta_x : x \in X\rbrace$$。

**一一性**：若 $$\delta_x = \delta_y$$，则 $$f(x) = f(y)$$ 对一切 $$f \in C(X)$$。$$X$$ 紧 Hausdorff，故正规，Urysohn 引理给出：若 $$x \ne y$$，存在 $$f \in C(X)$$ 使 $$f(x) = 1$$、$$f(y) = 0$$；这与 $$f(x) = f(y)$$ 矛盾。故 $$\delta_x = \delta_y \Rightarrow x = y$$，映射 $$x \mapsto \delta_x$$ 单射。

**连续性**：设 $$x_\alpha \to x$$（网或序列）。对每个 $$f \in C(X)$$，$$f$$ 连续给出 $$f(x_\alpha) \to f(x)$$，即 $$\delta_{x_\alpha}(f) \to \delta_x(f)$$ 对一切 $$f$$。按定义 3.11 的 Gelfand 拓扑（即弱\*拓扑），这正是 $$\delta_{x_\alpha} \to \delta_x$$。故 $$x \mapsto \delta_x$$ 连续。

连续双射从紧空间到 Hausdorff 空间必是同胚（紧集的连续像紧，从而是闭集；双射加闭映射即同胚），故 $$X \cong \lbrace \delta_x : x \in X\rbrace = \Delta(C(X))$$。

(iii) 由定义 3.11，$$\Gamma(f)(\varphi) = \varphi(f)$$，故 $$\Gamma(f)(\delta_x) = \delta_x(f) = f(x)$$。结合 (ii)，
$$\lVert \Gamma(f) \rVert_\infty = \sup_{\delta_x \in \Delta(C(X))} \lvert \Gamma(f)(\delta_x) \rvert = \sup_{x \in X} \lvert f(x) \rvert = \lVert f \rVert_\infty .$$
这说明 $$\Gamma$$ 在这个例子里是等距，把定理 3.12 (ii) 的收缩估计升级成了等式（$$C(X)$$ 是 C\* 代数，这也与定理 3.19 (ii) 一致）。机制一目了然：$$\Delta(C(X))$$ 就是 $$X$$，「在 $$\delta_x$$ 处取值」就是「在 $$x$$ 处取值」。

**解 竞4.**

(i) 由定理 3.12 (iv)，$$\hat a \equiv 0 \iff r(a) = 0$$，且 $$\sigma(a) = \hat a(\Delta(\mathcal A))$$，故
$$\sigma(a) = \lbrace 0 \rbrace \iff \hat a \equiv 0 .$$
（$$\sigma(a)$$ 非空（命题 3.4 (ii)），而 $$r(a) = \sup_{\lambda \in \sigma(a)} \lvert \lambda \rvert$$，故 $$r(a) = 0 \iff \sigma(a) = \lbrace 0\rbrace$$。）另一方面
$$\hat a \equiv 0 \iff \varphi(a) = 0 \ \forall \varphi \in \Delta(\mathcal A) \iff a \in \bigcap_{\varphi} \ker\varphi = \mathrm{rad}(\mathcal A) .$$
三句串起来即得
$$\mathrm{rad}(\mathcal A) = \lbrace a : \hat a \equiv 0 \rbrace = \lbrace a : r(a) = 0 \rbrace = \lbrace a : \sigma(a) = \lbrace 0 \rbrace \rbrace .$$

(ii) $$\Gamma$$ 单射 $$\iff$$ （$$\Gamma(a) = 0 \Rightarrow a = 0$$）$$\iff$$ （$$a \in \mathrm{rad}(\mathcal A) \Rightarrow a = 0$$）$$\iff$$ $$\mathrm{rad}(\mathcal A) = \lbrace 0\rbrace$$，中间用 (i) 把「$$\Gamma(a) = 0$$」等同于「$$a \in \mathrm{rad}(\mathcal A)$$」。

(iii) 先核对 $$\mathcal A = \mathbb{C}[\varepsilon]/(\varepsilon^2)$$ 是含单位的交换 Banach 代数。

**代数**：以 $$\lbrace 1, \varepsilon \rbrace$$ 为基，$$\varepsilon^2 = 0$$，乘法 $$(u + v\varepsilon)(u' + v'\varepsilon) = uu' + (uv' + vu')\varepsilon$$ 结合、交换、双线性，单位元是 $$1$$。

**范数**：$$\lVert u + v\varepsilon \rVert = \lvert u \rvert + \lvert v \rvert$$ 是范数（非退化、齐次、三角不等式三项逐条核对即得）；次乘性：
$$\lVert (u + v\varepsilon)(u' + v'\varepsilon) \rVert = \lvert uu' \rvert + \lvert uv' + vu' \rvert \le \lvert u \rvert\lvert u' \rvert + \lvert u \rvert\lvert v' \rvert + \lvert v \rvert\lvert u' \rvert \le (\lvert u \rvert + \lvert v \rvert)(\lvert u' \rvert + \lvert v' \rvert) .$$

**完备**：复二维线性空间上的范数，有限维必完备。又 $$\lVert 1 \rVert = 1$$。

**特征**：设 $$\varphi \in \Delta(\mathcal A)$$。由 $$\varepsilon^2 = 0$$ 得 $$\varphi(\varepsilon)^2 = \varphi(\varepsilon^2) = 0$$，故 $$\varphi(\varepsilon) = 0$$；又 $$\varphi(1) = 1$$，于是
$$\varphi(u + v\varepsilon) = u \qquad \text{对一切 } u, v \in \mathbb{C} .$$
反过来，这个泛函 $$\varphi_0(u + v\varepsilon) = u$$ 线性、保乘法（$$\varphi_0\big((u + v\varepsilon)(u' + v'\varepsilon)\big) = uu' = \varphi_0(u + v\varepsilon)\,\varphi_0(u' + v'\varepsilon)$$）、且 $$\varphi_0(1) = 1 \ne 0$$，故是特征。所以 $$\Delta(\mathcal A) = \lbrace \varphi_0\rbrace$$ 恰含一个点。

**根**：$$\mathrm{rad}(\mathcal A) = \ker\varphi_0 = \lbrace v\varepsilon : v \in \mathbb{C}\rbrace = \mathbb{C}\varepsilon \ne \lbrace 0 \rbrace$$。

于是由 (ii)，$$\Gamma$$ 不是单射：对 $$v \ne 0$$，$$\Gamma(v\varepsilon)$$ 在唯一的点 $$\varphi_0$$ 上取值 $$\varphi_0(v\varepsilon) = 0$$，即 $$\Gamma(v\varepsilon) \equiv 0$$，而 $$v\varepsilon \ne 0$$。它也不是等距：$$\lVert v\varepsilon \rVert = \lvert v \rvert$$ 而 $$\lVert \Gamma(v\varepsilon) \rVert_\infty = 0$$。

对照定理 3.19 (ii)：那里 $$\Gamma$$ 是等距 \*-同构，靠的正是 C\* 恒等式。在本例上给对合 $$\varepsilon^* = \varepsilon$$（于是 $$(u + v\varepsilon)^* = \bar u + \bar v\varepsilon$$），则
$$\lVert \varepsilon^*\varepsilon \rVert = \lVert \varepsilon^2 \rVert = \lVert 0 \rVert = 0 \ne 1 = \lVert \varepsilon \rVert^2 ,$$
C\* 恒等式失效。**这就是 C\* 恒等式不可省的地方**：它把范数与对合焊在一起，才能保证 $$\Gamma$$ 既不丢信息又不缩尺度；只靠「有乘法、有范数、有对合」，Gelfand 表示可能缩成一个点上的零函数。

**解 竞5.** 关键 leap：(i) 用 $$t$$ 造一个单参数族 $$b = a + ite$$，把 $$\lvert \varphi(b) \rvert$$ 用 $$\lVert b \rVert$$ 压住；因为 $$\lVert b \rVert^2 = \lVert b^*b \rVert \le \lVert a \rVert^2 + t^2$$，两边都出现 $$t^2$$，相消之后就只剩一条关于 $$t$$ 的**一次**不等式——一次函数在 $$\mathbb{R}$$ 上有上界，斜率只能为零。这与正文 定理 3.18 的算术一样，区别只在**用 $$\lVert b \rVert$$ 而不是 $$\lVert b^*b \rVert$$ 去压 $$\lvert \varphi(b) \rvert$$**，而这一步才是真正需要 C\* 恒等式的地方（见 (ii)）。

(i) 固定 $$\varphi \in \Delta(\mathcal A)$$。由定理 3.10 (ii)，$$\lVert \varphi \rVert = 1$$，故
$$\lvert \varphi(c) \rvert \le \lVert c \rVert \qquad \text{对一切 } c \in \mathcal A .$$

记 $$\varphi(a) = \alpha + i\beta$$，$$\alpha, \beta \in \mathbb{R}$$。对 $$t \in \mathbb{R}$$ 令 $$b = a + ite$$。由 $$a^* = a$$、$$e^* = e$$、$$\overline{it} = -it$$，
$$b^* = a^* + \overline{it}\,e^* = a - ite .$$
先算 $$\lVert b \rVert^2$$。$$\mathcal A$$ 交换，故可以直接展开：
$$b^*b = (a - ite)(a + ite) = a^2 + itae - itea + (it)^2e^2 = a^2 + t^2e ,$$
中间两个交叉项相消（$$ae = ea = a$$），末项 $$(-it)(it)e^2 = -i^2t^2e = t^2e$$。于是
$$\lVert b^*b \rVert \le \lVert a^2 \rVert + t^2 \le \lVert a \rVert^2 + t^2 .$$
**这里用 C\* 恒等式**：$$\lVert b \rVert^2 = \lVert b^*b \rVert$$，故
$$\lVert b \rVert^2 \le \lVert a \rVert^2 + t^2 .$$

另一方面 $$\varphi(b) = \varphi(a) + it\varphi(e) = \alpha + i(\beta + t)$$，故 $$\lvert \varphi(b) \rvert^2 = \alpha^2 + (\beta + t)^2$$。由 $$\lvert \varphi(b) \rvert \le \lVert b \rVert$$，
$$\alpha^2 + (\beta + t)^2 \le \lVert a \rVert^2 + t^2 \qquad \text{对一切 } t \in \mathbb{R} .$$
展开 $$(\beta + t)^2 = \beta^2 + 2\beta t + t^2$$，两端消去 $$t^2$$：
$$\alpha^2 + \beta^2 + 2\beta t \le \lVert a \rVert^2 \qquad \text{对一切 } t \in \mathbb{R} .$$
右端与 $$t$$ 无关。若 $$\beta > 0$$，令 $$t \to +\infty$$ 使左端趋于 $$+\infty$$，矛盾；若 $$\beta < 0$$，令 $$t \to -\infty$$ 同样矛盾。故 $$\beta = 0$$，即 $$\varphi(a) = \alpha \in \mathbb{R}$$。

最后由定理 3.12 (iv)，$$\sigma(a) = \lbrace \varphi(a) : \varphi \in \Delta(\mathcal A)\rbrace \subseteq \mathbb{R}$$。$$\blacksquare$$

（把这条用于 $$\mathcal B(H)$$ 中自伴的 $$T$$ 与它生成的交换 C\* 代数，就得到 定理 3.21 的 $$\sigma(T) \subset \mathbb{R}$$，且全程不经过命题 3.15 的自伴分解。）

(ii) (i) 中用 C\* 恒等式的地方只有一处，就是把 $$\lVert b^*b \rVert \le \lVert a \rVert^2 + t^2$$ 升级为 $$\lVert b \rVert^2 \le \lVert a \rVert^2 + t^2$$。若只有「带对合、对合保范」，$$\lVert b \rVert^2$$ 与 $$\lVert b^*b \rVert$$ 之间没有这样的关系，整条论证断路。下面给出一个反例。

取 $$\mathcal A_0 = \mathbb{C}^2 = \lbrace (z,w) : z, w \in \mathbb{C} \rbrace$$，乘法逐分量，范数 $$\lVert (z,w) \rVert = \max(\lvert z \rvert, \lvert w \rvert)$$，对合 $$(z,w)^* = (\bar w, \bar z)$$。

**(a)** 逐分量乘法使 $$\mathcal A_0$$ 成为交换代数，单位元 $$(1,1)$$ 满足 $$\lVert (1,1) \rVert = 1$$；次乘性：$$\lVert (z,w)(z',w') \rVert = \max(\lvert zz' \rvert, \lvert ww' \rvert) \le \max(\lvert z \rvert,\lvert w \rvert)\max(\lvert z' \rvert, \lvert w' \rvert)$$。有限维故完备。对合保范：$$\lVert (z,w)^* \rVert = \max(\lvert \bar w \rvert, \lvert \bar z \rvert) = \max(\lvert z \rvert, \lvert w \rvert)$$。还要核对对合公理：$$(ab)^* = b^*a^*$$ 在这里成立，因为 $$\mathbb{C}$$ 交换，逐分量写出即得；共轭线性与 $$(x^*)^* = x$$ 也逐项核对。

**(b)** $$a = (1+i, 1-i)$$：$$a^* = (\overline{1-i}, \overline{1+i}) = (1+i, 1-i) = a$$。

**(c)** $$\varphi_1(z,w) = z$$ 是乘法线性泛函（$$\varphi_1((z,w)(z',w')) = zz' = \varphi_1(z,w)\varphi_1(z',w')$$）且 $$\varphi_1(1,1) = 1 \ne 0$$，故 $$\varphi_1 \in \Delta(\mathcal A_0)$$。于是 $$\varphi_1(a) = 1 + i \ne \overline{1+i}$$：

$$\varphi_1(a) = 1 + i \notin \mathbb{R} , \qquad \text{而 } a^* = a .$$

由定理 3.12 (iv)（它对任何含单位的交换 Banach 代数都成立，不需要对合），$$\sigma(a) = \lbrace \varphi(a) : \varphi \in \Delta(\mathcal A_0)\rbrace$$（这里 $$\Delta(\mathcal A_0)$$ 含 $$\varphi_1, \varphi_2$$，其中 $$\varphi_2(z,w) = w$$），故 $$1+i \in \sigma(a)$$，$$\sigma(a) \not\subseteq \mathbb{R}$$。可见「$$\lVert x^* \rVert = \lVert x \rVert$$ 且 $$x^* = x$$」**不蕴含**谱落在实轴上。

**(d)** 取 $$x = (1,2)$$。$$x^* = (2,1)$$，故
$$x^*x = (2,1)(1,2) = (2, 2), \qquad \lVert x^*x \rVert = 2 .$$
而 $$\lVert x \rVert^2 = \max(1,2)^2 = 4$$。两者不等，C\* 恒等式失效。

**这个例子说明的三件事**：第一，Arens 引理的正确假设是 $$\lVert b \rVert^2 = \lVert b^*b \rVert$$（C\* 恒等式），一个交换 **C\* 代数**足够了；本章后续的定理 3.19 (i)、定理 3.21 都只在 C\* 代数的情形调用 Arens 引理，因此不受影响。第二，「$$\lVert a^* \rVert = \lVert a \rVert$$」远比 C\* 恒等式弱：前者只说对合是等距，后者才把范数的**大小**（$$\lVert b \rVert$$）与**代数平方**（$$b^*b$$）绑在一起。第三，$$\mathcal A_0$$ 的对合还有一个特点：$$(1,0)^* = (0,1)$$，它把两个「坐标方向」互换，这正是它躲开 C\* 恒等式的方式。

**解 研1.** 思路：$$\mathcal A$$ 缺的就是「$$e$$」这把尺子，而谱、$$\Delta(\mathcal A)$$、$$\Gamma$$ 都要用 $$e$$ 来写。最省事的修法是把 $$e$$ 人工添进去：$$\mathcal A_1 = \mathcal A \oplus \mathbb{C}$$，把 $$\mathcal A$$ 看成余维 $$1$$ 的闭理想，原来的 $$\mathcal A$$ 就是「$$e$$ 恰好落在这个理想里」的退化情形。

(i) **代数**：乘法按题目给出，结合律与交换性逐项核对（$$\mathcal A$$ 结合、交换）。单位元 $$e_1 = \mathbf 1$$：$$(a + \lambda\mathbf 1)\mathbf 1 = a + \lambda\mathbf 1$$。

**范数**：$$\lVert a + \lambda \mathbf 1 \rVert_1 = \lVert a \rVert + \lvert \lambda \rvert$$ 是 $$\mathcal A \oplus \mathbb{C}$$ 上的 $$\ell^1$$ 型范数，非退化（$$\lVert a \rVert + \lvert \lambda \rvert = 0 \Rightarrow a = 0, \lambda = 0$$）、齐次、满足三角不等式。次乘性：
$$\lVert (a + \lambda \mathbf 1)(b + \mu \mathbf 1) \rVert_1 = \lVert ab + \lambda b + \mu a \rVert + \lvert \lambda \mu \rvert \le \lVert a \rVert\lVert b \rVert + \lvert \lambda \rvert\lVert b \rVert + \lvert \mu \rvert\lVert a \rVert + \lvert \lambda \rvert\lvert \mu \rvert = (\lVert a \rVert + \lvert \lambda \rvert)(\lVert b \rVert + \lvert \mu \rvert) .$$

**完备**：$$\mathcal A_1 = \mathcal A \oplus \mathbb{C}$$ 是完备空间的直和（$$\ell^1$$ 范数下 Cauchy 列的两个分量分别 Cauchy）。又 $$\lVert e_1 \rVert_1 = \lVert 0 \rVert + \lvert 1 \rvert = 1$$。

**$$\mathcal A$$ 是闭理想**：$$\mathcal A = \lbrace a + 0 \cdot \mathbf 1\rbrace$$ 是范数 $$\lVert a \rVert_1 = \lVert a \rVert$$ 下的子空间，故闭（$$\mathcal A$$ 完备）。理想性：$$(a + \lambda\mathbf 1)(b + 0\cdot\mathbf 1) = (ab + \lambda b) + 0\cdot \mathbf 1 \in \mathcal A$$，且由交换性左右吸收一致。$$\blacksquare$$

(ii) **$$\varphi_\infty$$ 是特征**：
$$\varphi_\infty\big((a + \lambda\mathbf 1)(b + \mu\mathbf 1)\big) = \varphi_\infty\big((ab + \lambda b + \mu a) + \lambda\mu\mathbf 1\big) = \lambda\mu = \varphi_\infty(a + \lambda\mathbf 1)\varphi_\infty(b + \mu\mathbf 1) ,$$
且线性、$$\varphi_\infty(\mathbf 1) = 1 \ne 0$$。

**限制映射单射**：设 $$\varphi \in \Delta(\mathcal A_1)$$、$$\varphi \ne \varphi_\infty$$。则 $$\varphi\vert_{\mathcal A} \ne 0$$（若 $$\varphi\vert_{\mathcal A} = 0$$，则 $$\varphi(a + \lambda\mathbf 1) = \lambda\varphi(\mathbf 1) = \lambda = \varphi_\infty(a + \lambda\mathbf 1)$$，矛盾）。$$\varphi\vert_{\mathcal A}$$ 按定义是 $$\mathcal A$$ 上的乘法线性泛函，故 $$\varphi\vert_{\mathcal A} \in \Delta(\mathcal A)$$；又 $$\varphi$$ 由它在 $$\mathcal A$$ 上与在 $$\mathbf 1$$ 上的值唯一决定。

**满射**：设 $$\psi \in \Delta(\mathcal A)$$。在 $$\mathcal A_1$$ 上定义 $$\varphi(a + \lambda\mathbf 1) = \psi(a) + \lambda$$。它是线性的、乘法保持的（与 (i) 中的展开逐项核对，交叉项分别由 $$\psi(b)$$、$$\psi(a)$$ 承担），且 $$\varphi\vert_{\mathcal A} = \psi$$。故限制映射是 $$\Delta(\mathcal A_1) \setminus \lbrace \varphi_\infty\rbrace$$ 到 $$\Delta(\mathcal A)$$ 的双射。

**拓扑**：$$\mathcal A_1$$ 含单位，故由定理 3.12 (i)，$$\Delta(\mathcal A_1)$$ 是紧 Hausdorff 空间。限制映射 $$\varphi \mapsto \varphi\vert_{\mathcal A}$$ 在弱\*拓扑下连续（$$\psi \mapsto \psi(a)$$ 是弱\*拓扑的基本连续函数）；它的逆 $$\psi \mapsto \varphi$$ 也连续（$$\varphi(a + \lambda\mathbf 1) = \psi(a) + \lambda$$ 关于 $$\psi$$ 连续，因为右端是弱\*连续函数的和）。连续双射把紧空间送到 Hausdorff 空间，故是同胚。$$\blacksquare$$

(iii) 由 (ii)，$$\Delta(\mathcal A) \cong \Delta(\mathcal A_1) \setminus \lbrace \varphi_\infty\rbrace$$；右端是紧空间挖去一点，故局部紧 Hausdorff。

顺带说明「$$\Delta(\mathcal A)$$ 只局部紧、不紧」的来源：若 $$\mathcal A$$ 本含单位 $$e$$，则 $$\varphi_\infty(e) = 0$$ 与 $$e \ne \mathbf 1$$ 冲突，限制映射不再是双射——$$\mathcal A_1$$ 里多出的那个点，正是「单位元缺失」的记号。

最后看 $$\hat a$$ 的衰减。把 $$a \in \mathcal A$$ 看成 $$\mathcal A_1$$ 的元素，其 Gelfand 表示 $$\hat a$$ 在 $$\Delta(\mathcal A_1)$$ 上连续，且在 $$\varphi_\infty$$ 处取值
$$\hat a(\varphi_\infty) = \varphi_\infty(a + 0 \cdot \mathbf 1) = 0 .$$
$$\Delta(\mathcal A)$$ 就是 $$\Delta(\mathcal A_1)$$ 挖掉 $$\varphi_\infty$$ 之后的开子集，故「在这个开集的补上（即 $$\varphi_\infty$$ 处）取值为零」正是 $$C_0(\Delta(\mathcal A))$$ 的定义：$$\Gamma(\mathcal A) \subset C_0(\Delta(\mathcal A))$$。特别地，$$\mathbf 1$$ 属于 $$\mathcal A_1$$ 而不属于 $$\mathcal A$$，所以 $$\Gamma(\mathcal A)$$ 里没有常函数。

(iv) 把两件事并排看：

| | 代数侧 | 算子侧 |
|---|---|---|
| 缺什么 | 单位元 $$e$$ | 定义域 $$D(T) = H$$ |
| 后果 | $$\lambda e - a$$ 写不出来，谱无从定义 | $$T \notin \mathcal B(H)$$，$$T + \lambda I$$ 只在 $$D(T)$$ 上有意义 |
| 补救 | 添 $$e$$ 得 $$\mathcal A_1$$，$$e_1$$ 记号化「缺失」 | 取有界可逆的 $$(T + iI)^{-1}$$，或按图范数把 $$T$$ 当闭算子 |

两者的结构一致：对象本身少了一块，标准机器（谱、Gelfand 表示、算子范数）开不动，于是先做安全封装，让机器在封装后的对象上跑，再读回来。对代数，封装是 $$\mathcal A_1$$；对无界算子，封装就是 **Cayley 变换**（研2）——把无界的东西换成有界酉算子。这正是第 42 章的开场。

**解 研2.** 思路：自伴性把 $$\sigma(T)$$ 逼进实轴（定理 3.21），实轴上的点 $$\lambda$$ 经 Möbius 变换 $$\zeta = (\lambda - i)/(\lambda + i)$$ 落到圆周上——于是「实轴 + 无穷远」被整条搬到「圆周」，无界的 $$\lambda$$ 变成有界的 $$\zeta$$。Cayley 变换就是这次搬运在算子层面的实现。

(i) 由定理 3.21，$$\sigma(T) \subset \mathbb{R}$$。注意 $$T + iI = (-i)I - T$$，故 $$\mu = -i$$ 时 $$\mu I - T = T + iI$$。既然 $$-i \notin \sigma(T) \subset \mathbb{R}$$，按定义 $$T + iI = (-i)I - T$$ 可逆。$$\blacksquare$$

(ii) **先算 $$U$$ 的伴随**。用两条标准事实：$$(AB)^* = B^*A^*$$，以及 $$S$$ 可逆时 $$(S^{-1})^* = (S^*)^{-1}$$；又 $$T$$ 自伴给出 $$(T \pm iI)^* = T \mp iI$$。于是
$$U^* = \big((T - iI)(T + iI)^{-1}\big)^* = \big((T + iI)^{-1}\big)^*(T - iI)^* = \big((T + iI)^*\big)^{-1}(T - iI) = (T - iI)^{-1}(T + iI) .$$

**酉性**：因为 $$T$$ 自伴，$$T + iI$$ 与 $$T - iI$$ 都是 $$T$$ 的多项式，两者相乘可交换。于是
$$U^*U = (T - iI)^{-1}(T + iI)(T - iI)(T + iI)^{-1} = (T - iI)^{-1}(T - iI)(T + iI)(T + iI)^{-1} = I ,$$
同理 $$UU^* = I$$。故 $$U$$ 是酉算子。

**算 $$I - U$$**：把 $$I$$ 写成 $$(T + iI)(T + iI)^{-1}$$，
$$I - U = (T + iI)(T + iI)^{-1} - (T - iI)(T + iI)^{-1} = \big[(T + iI) - (T - iI)\big](T + iI)^{-1} = 2iI \cdot (T + iI)^{-1} = 2i(T + iI)^{-1} .$$
由 (i)，$$(T + iI)^{-1} \in \mathcal B(H)$$ 可逆，故 $$I - U$$ 可逆，且
$$(I - U)^{-1} = \frac{1}{2i}(T + iI) = -\frac{i}{2}(T + iI) . \qquad \blacksquare$$

(iii) 同样把 $$I + U$$ 通分：
$$I + U = (T + iI)(T + iI)^{-1} + (T - iI)(T + iI)^{-1} = \big[(T + iI) + (T - iI)\big](T + iI)^{-1} = 2T(T + iI)^{-1} .$$
两边用 (ii) 的 $$(I - U)^{-1} = -\frac{i}{2}(T + iI)$$：
$$(I + U)(I - U)^{-1} = 2T(T + iI)^{-1} \cdot \Big(-\frac{i}{2}\Big)(T + iI) = -iT .$$
两边乘 $$i$$：$$i(I + U)(I - U)^{-1} = -i^2T = T$$。$$\blacksquare$$

(iv) 记 $$\mu \in \mathbb{C}$$。我们要刻画「$$\mu \in \sigma(T)$$」。由 (iii) 把 $$T$$ 用 $$U$$ 表出：
$$\mu I - T = \mu I - i(I + U)(I - U)^{-1} = \Big[\mu(I - U) - i(I + U)\Big](I - U)^{-1} = \Big[(\mu - i)I - (\mu + i)U\Big](I - U)^{-1} ,$$
其中把 $$\mu I$$ 写成 $$\mu(I - U)(I - U)^{-1}$$ 后与前一项合并。因 $$(I - U)^{-1}$$ 可逆，$$\mu I - T$$ 可逆当且仅当 $$(\mu - i)I - (\mu + i)U$$ 可逆。

设 $$\mu \ne -i$$（由 $$\sigma(T) \subset \mathbb{R}$$，$$\sigma(T)$$ 中的 $$\mu$$ 当然 $$\ne -i$$）。则 $$(\mu + i) \ne 0$$，可以提出因子：
$$(\mu - i)I - (\mu + i)U = -(\mu + i)\Big[U - \frac{\mu - i}{\mu + i}I\Big] ,$$
故它可逆当且仅当 $$\zeta := \dfrac{\mu - i}{\mu + i} \notin \sigma(U)$$。把这句话取逆否（$$\mu I - T$$ 与 $$(\mu - i)I - (\mu + i)U$$ 可逆性一致），即得
$$\mu \in \sigma(T) \iff \zeta(\mu) = \frac{\mu - i}{\mu + i} \in \sigma(U) .$$

再解出 $$\mu$$：由 $$\zeta(\mu + i) = \mu - i$$，即 $$\zeta\mu + i\zeta = \mu - i$$，故 $$\mu(\zeta - 1) = -i(\zeta + 1)$$，即
$$\mu = i\,\frac{1 + \zeta}{1 - \zeta} .$$
分母在 $$\zeta = 1$$ 处为零；由 (ii)，$$I - U = 2i(T + iI)^{-1}$$ 可逆，故 $$1 \notin \sigma(U)$$（$$I - U$$ 可逆当且仅当 $$1 \notin \sigma(U)$$），分母不会为零。于是
$$\sigma(T) = \lbrace \mu : \zeta(\mu) \in \sigma(U) \rbrace = \left\lbrace i\,\frac{1 + \zeta}{1 - \zeta} : \zeta \in \sigma(U) \right\rbrace .$$
这与 $$\sigma(U) \subset \mathbb{T}$$（定理 3.21 的酉情形：$$\lvert \hat U \rvert \equiv 1$$）相容：$$\zeta \in \mathbb{T}$$ 时右端落在实轴上，因为它是 Möbius 变换把圆周映回实轴。$$\blacksquare$$

（检验一个例子：取 $$H = \mathbb{C}$$、$$T = \lambda_0 \in \mathbb{R}$$。则 $$\zeta = (\lambda_0 - i)/(\lambda_0 + i)$$，而 $$i(1+\zeta)/(1-\zeta) = \lambda_0$$，故 $$\sigma(T) = \lbrace \lambda_0\rbrace$$ 与右端一致。）

**这一段正是第 42 章的起点。** $$\zeta = (\mu - i)/(\mu + i)$$ 把实轴连同无穷远点双射到单位圆周（$$\mu \to \infty$$ 对应 $$\zeta \to 1$$）。对**有界**自伴 $$T$$，$$\infty$$ 不在谱里，一切顺当；对**无界**自伴算子，$$\sigma(T)$$ 是 $$\mathbb{R}$$ 中的无界闭集，$$\infty$$ 是它的极限点，$$T$$ 不再是 $$\mathcal B(H)$$ 的元素，本章为有界算子建的理论直接失效。第 42 章把方向反过来用：不追 $$T$$，只追 $$U = (T - iI)(T + iI)^{-1}$$。自伴性保证 $$(T + iI)^{-1}$$ 仍有界（$$\lVert (T + iI)^{-1} \rVert \le 1$$），于是 $$U$$ 是**有界酉算子**，$$T$$ 的全部信息（谱、谱测度、函数演算）都编码在 $$U$$ 与那个「缺失的点」$$\zeta = 1$$ 上。无界问题就此归约成有界问题——本章的 C\* 代数机器得以接管第 42 章。

## 七、Takeaway 与延伸 (Takeaways)

### 7.1 五条核心洞察 (Takeaways)

**T1. 谱是纯代数的对象，不是算子的附属品。** 定义 3.2 里只有乘法与单位元：$$\sigma(a) = \lbrace \lambda : \lambda e - a \notin G(\mathcal A)\rbrace$$。把它写成这样之后，第 36 章「$$\lambda I - T$$ 不可逆」立刻变成特例，而第 36 章留下的问题（自伴为何给出实谱）也才有了结构性的回答；只盯住算子本身，问题就永远停在「个别算子的个别性质」这一层。

**T2. 元素就是函数。** 本章唯一的动作是把这句话叠成：
$$\sigma(a) = \lbrace \varphi(a) : \varphi \in \Delta(\mathcal A)\rbrace = \hat a\big(\Delta(\mathcal A)\big).$$
$$\Delta(\mathcal A)$$ 是空间，$$\varphi$$ 是点，$$a$$ 是函数，$$\hat a(\varphi)$$ 是函数在点上的值。点是**极大理想**（$$\ker\varphi$$ 就是「在该点取零的函数全体」），这跟代数几何用理想定义点是同一个动作，只是把 $$\mathbb{C}[z]$$ 换成了 Banach 代数。这是全书的**第三次对偶**（ch03 向量空间、ch15 Hilbert 空间、本章代数），而且是一次质变：前两次对偶出来还是线性空间，这一次出来的是**函数代数**——乘法被「解压」成逐点相乘，对偶升级成「一类结构 ↔ 另一类结构」（第 62 章的范畴等价）。

**T3. 谱半径公式：谱的大小由幂的增长速率决定，而不是由元素本身的范数决定。** $$r(a) = \lim_n \lVert a^n \rVert^{1/n}$$。经典问题 1 的 Volterra 算子是极端证据：$$\lVert V \rVert \ge 1/\sqrt3 > 0 = r(V)$$、$$\sigma(V) = \lbrace 0\rbrace$$。推论是 $$r(a) \le \lVert a \rVert$$ 且等号只在「$$a$$ 正规」这类特殊情形（命题 3.17 (iii)）成立；**把 $$r(a)$$ 误当成 $$\lVert a \rVert$$ 是初学本章最常见的错误**。

**T4. C\* 恒等式是唯一的焊点，而且这个假设不能减弱。** 恒等式 $$\lVert a^*a \rVert = \lVert a \rVert^2$$ 一头拴住对合（代数数据）、一头拴住范数（分析数据）。它换来 Arens 引理（定理 3.18）：**自伴元的 Gelfand 表示是实值函数**，于是 $$\sigma(T) \subset \mathbb{R}$$，于是量子力学「可观测量取实数」不是特设公理而是公理的推论（§4.3）。而注 3.18 的 $$\mathbb{C}^2$$ 反例说明：把假设放宽成「带保范对合的交换 Banach 代数」，结论立刻假——那个代数里 $$a = (1+i, 1-i)$$ 自伴，谱却是 $$\lbrace 1+i, 1-i\rbrace$$。**「只要有对合就够」是本章最容易产生的错觉。**

**T5. 交换性是 Gelfand 理论的生死线。** 非交换时 $$\Delta$$ 会整个消失（经典问题 2：$$\Delta(M_n(\mathbb{C})) = \varnothing$$，因为 $$M_n(\mathbb{C})$$ 单而 $$\dim > 1$$）。出路不是放弃几何，而是**局部交换化**：固定一个正规算子 $$T$$，退到它生成的交换闭 \*-子代数，那里 $$\Delta(\mathcal A_T)$$ 照常是「点集」，且与 $$\sigma(T)$$ 一一对应（定理 3.21、经典问题 5）。第 38 章谱定理的代数版本、以及「非交换几何」把代数本身当空间用的做法，都从这里出发（§4.5）。

### 7.2 下一章：从有界走到无界（第 42 章 无界算子与 Cayley 变换）

本章的全部结论都压在两块「有限性」上：

- **元素是有界的**（$$a$$ 属于一个 Banach 代数，$$\lVert a \rVert < \infty$$）：命题 3.3 的 Neumann 级数、定理 3.5 的谱半径公式、定理 3.12 的 Gelfand 表示，都以这一条为前提；
- **$$\sigma(a)$$ 是 $$\mathbb{C}$$ 中的紧集**（命题 3.4 (i)）：于是上确界被取到、$$r(a) < \infty$$、Liouville 论证走得通。

量子力学的动量 $$P = -i\,d/dx$$ 与位置 $$Q$$ 都是**无界**自伴算子：$$P \notin \mathcal B(H)$$，$$\sigma(P) = \mathbb{R}$$ 是无界闭集，$$\infty$$ 成了谱的极限点。本章的机器在这里一步也开不动——没有算子范数，$$\Delta$$ 无从谈起。

救命的工具在练习 研2 里已经算完：**Cayley 变换**
$$U = (T - iI)(T + iI)^{-1},$$
它把无界自伴 $$T$$ 换成一个**有界酉算子** $$U$$（有界情形下我们证明了 $$U^*U = UU^* = I$$、$$I - U$$ 可逆、$$T = i(I+U)(I-U)^{-1}$$）。背后的几何是 Möbius 变换
$$\zeta = \frac{\mu - i}{\mu + i},$$
它把实轴连同无穷远点双射到单位圆周；$$\mu \to \infty$$ 对应 $$\zeta \to 1$$，所以 $$\sigma(T) \subset \mathbb{R}$$ 与 $$\sigma(U) \subset \mathbb{T}$$ 是同一件事的两种写法，而 $$\zeta = 1$$ 这个「缺失的点」正是 $$T$$ 无界的记号。

第 42 章反过来用这条等式：**不追 $$T$$，只追 $$U$$**。$$U$$ 有界，所以本章的 C\* 代数机器（Gelfand 表示、谱半径公式、函数演算）全部接管；$$T$$ 的谱、谱测度、函数演算都编码在 $$U$$ 加上那个缺失的点里。再往前一格是第 44 章：正则对易关系与 Stone–von Neumann——那里的主角 $$P, Q$$ 也是无界算子，而 $$[P, Q] = -iI$$ 这条关系本身就是「二者不可能同时有界」的代数表达。

一句话把本章与下一章接起来：**本章把有界自伴算子的谱搬到实轴上（定理 3.21），下一章把无界的搬到圆周上（Cayley 变换），而这两次搬运用的是同一台机器。**

### 7.3 延伸阅读 (Further reading)

- W. Rudin, *Functional Analysis*, 2nd ed., Ch. 10–11——本章 §3.3–3.6 的骨架，也是入口题 (a)(b) 的出处。
- J. B. Conway, *A Course in Functional Analysis*, 2nd ed., Ch. VII——Gelfand 理论讲得最细的一本入门。
- G. J. Murphy, *C\*-Algebras and Operator Theory*, Ch. 1–2——从 Banach 代数走到 C\* 代数，含 Gelfand–Naimark 一般形式。
- R. V. Kadison & J. R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I, Ch. 4——C\* 代数的标准参考，态与 GNS 构造。
- W. Arveson, *An Invitation to C\*-Algebras*, Ch. 1——篇幅小，观点高，适合读完本章后当「第二遍」。
- 历史注记：R. Arens, *On a theorem of Gelfand and Neumark*, Proc. Nat. Acad. Sci. U.S.A. **32** (1946), 237–239——注 3.18 讨论的「自伴性条件到底需要多强」，正是这篇文章的议题。
- A. Connes, *Noncommutative Geometry*, Ch. 1——§4.5 提到的「没有点也要定义几何」的正式版本。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch39_Banach代数与C_代数_上.md">← 第39章 Banach 代数与 C\* 代数·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch41_无界算子与Cayley变换_上.md">第41章 无界算子与 Cayley 变换·上 →</a></div>
</div>
