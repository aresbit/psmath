# 有限域与有限域算法：存在唯一性、Frobenius、Cantor–Zassenhaus、Berlekamp

> 整理自 Victor Shoup, *A Computational Introduction to Number Theory and Algebra* (v2, Cambridge University Press, 2008)，第 19 章（有限域）、第 20 章（有限域算法）；应用部分整理自 Madhu Sudan, *Essential Coding Theory* (Harvard CS 229r)。

有限域是密码学、编码论与算法设计的基本对象。它是 $\mathbb{Z}_p$（$p$ 素数）的自然推广，也是椭圆曲线密码、AES、Reed–Solomon 码的公共基础。

## 1. 存在性与构造

**定理**：有限域的阶必为素数幂 $p^d$；反之，对任意素数 $p$ 与 $d\ge 1$，存在 $p^d$ 元有限域，记作 $\mathbb{F}_{p^d}$。

**构造方法**：取素数域 $\mathbb{F}_p=\mathbb{Z}_p$ 上的 $d$ 次**不可约多项式** $f(X)\in\mathbb{F}_p[X]$，则商环 $\mathbb{F}_p[X]/(f)$ 是域，且

$$\lvert\mathbb{F}_p[X]/(f)\rvert = p^d.$$

**为何是域**：$\mathbb{F}_p[X]$ 是主理想整环，$f$ 不可约等价于 $(f)$ 是**极大理想**，故商环是域。元素表示：每个剩余类可唯一写成次数 $<d$ 的多项式，即 $d$ 个 $\mathbb{F}_p$ 系数的向量。

**不可约多项式的存在性**：用**计数**证明。$X^{p^d}-X$ 的全部根恰是 $\mathbb{F}_{p^d}$ 的元素，而不可约多项式按次数分拆 $X^{p^d}-X$ 的因子，比较次数得不可约多项式个数的递推式

$$I_p(d) = \frac{1}{d}\left(p^d - \sum_{e\mid d,\ e<d} e\,I_p(e)\right),$$

从而 $I_p(d)>0$。

## 2. 唯一性与子域结构

**唯一性定理**：任意两个 $p^d$ 元有限域同构。因此"$\mathbb{F}_{p^d}$"在同构意义下良定义。

**分裂域观点**：$\mathbb{F}_{p^d}$ 是多项式 $X^{p^d}-X$ 在 $\mathbb{F}_p$ 上的分裂域；唯一性来自"分裂域在同构意义下唯一"。

**子域结构**：$\mathbb{F}_{p^d}$ 包含子域 $\mathbb{F}_{p^e}$ 当且仅当 $e\mid d$。当 $e\mid d$ 时，$\mathbb{F}_{p^e}$ 恰好由满足 $x^{p^e}=x$ 的元素构成。

**乘法群结构**：$\mathbb{F}_{p^d}^{\ast}$ 是 $p^d-1$ 阶**循环群**，其生成元称为**本原元素**。这是有限域上离散对数的基础。

## 3. Frobenius 自同构、共轭、范数与迹

**Frobenius 自同构**：映射

$$\sigma: \mathbb{F}_{p^d}\to\mathbb{F}_{p^d}, \qquad \sigma(x)=x^p$$

是 $\mathbb{F}_{p^d}$ 的自同构，且固定 $\mathbb{F}_p$（由 Fermat 小定理）。$\sigma$ 的阶恰为 $d$，且 $d$ 个自同构 $x,x^p,x^{p^2},\dots,x^{p^{d-1}}$ 构成 $\mathbb{F}_{p^d}$ 的全部自同构（$\operatorname{Gal}(\mathbb{F}_{p^d}/\mathbb{F}_p)$ 是 $d$ 阶循环群）。

**共轭**：元素 $x$ 的共轭为 $x,x^p,x^{p^2},\dots,x^{p^{d-1}}$（Frobenius 作用下的轨道）。

**范数与迹**：

$$N(x) = x\cdot x^p\cdots x^{p^{d-1}} = x^{(p^d-1)/(p-1)},$$

$$\operatorname{Tr}(x) = x + x^p + \cdots + x^{p^{d-1}}.$$

范数是乘法同态 $N(xy)=N(x)N(y)$，迹是加法同态 $\operatorname{Tr}(x+y)=\operatorname{Tr}(x)+\operatorname{Tr}(y)$，且 $\operatorname{Tr}$ 是 $\mathbb{F}_p$-线性的。范数与迹在有限域编码理论（如迹表示）与代数数论中反复出现。

**极小多项式**：对 $\alpha\in\mathbb{F}_{p^d}$，其极小多项式是使 $f(\alpha)=0$ 的次数最低首一多项式 $f\in\mathbb{F}_p[X]$。次数等于 $\alpha$ 的共轭个数，且

$$f(X) = \prod_{i=0}^{e-1}(X-\alpha^{p^i}),$$

其中 $e\mid d$ 是使 $\alpha^{p^e}=\alpha$ 的最小正整数。

## 4. 不可约性检验

**关键恒等式**：在 $\mathbb{F}_p[X]$ 中，

$$X^{p^d} - X = \prod_{\substack{f\ \text{首一不可约}\\ \deg(f)\mid d}} f(X),$$

即 $X^{p^d}-X$ 恰是所有次数整除 $d$ 的首一不可约多项式之积。因此 $f$（$d$ 次）不可约当且仅当：

1. $f\mid X^{p^d}-X$（即 $\gcd(f,X^{p^d}-X)=f$）；
2. 对 $f$ 的每个真因子 $e$（$e\mid d,\ e<d$），$\gcd(f,X^{p^e}-X)=1$。

**检验算法**：对 $f$ 的所有真因子 $e$ 检查 $\gcd(f,X^{p^e}-X)=1$。若 $d$ 有 $k$ 个真因子，需 $k$ 次模幂与 gcd，总复杂度 $O(k\cdot\mathrm{len}(p)\cdot d^2)$ 量级，多项式时间。

```python
def is_irreducible(f, p: int) -> bool:
    """检验 F_p[X] 上多项式 f（d 次）是否不可约。"""
    d = len(f) - 1
    for e in range(1, d):
        if d % e == 0:                       # 真因子 e
            g = pow_poly_mod([0, 1], p ** e, f, p)   # X^{p^e} mod f
            g = poly_sub(g, [0, 1], p)               # X^{p^e} - X
            if poly_gcd(f, g, p) != [1]:
                return False
    return True
```

## 5. 平方自由分解

**目标**：把 $f$ 写成 $f=\prod_i g_i^i$，其中 $g_i$ 无重因子。核心工具是**形式导数** $f'$。

**关键事实**：若 $f$ 有重因子，则 $\gcd(f,f')\ne 1$。更精确地，在特征 $p$ 下：

- 若 $f'\ne 0$，则 $f/\gcd(f,f')$ 是 $f$ 的所有一次因子之积（剥离了重数）；
- 若 $f'=0$（即 $f=h(X^p)$），则 $f=\tilde h(X)^p$，可利用 Frobenius 的线性性把 $p$ 次根"提出"，递归处理。

平方自由分解是 Cantor–Zassenhaus 与 Berlekamp 的预处理。

## 6. Cantor–Zassenhaus 算法

**目标**：分解一个无重因子、且所有不可约因子同次的多项式。

**第一步（不同次数分解，确定性）**：对 $e=1,2,\dots$ 计算 $\gcd(f,X^{p^e}-X)$，它恰是所有次数 $\mid e$ 的不可约因子之积。据此把 $f$ 按因子次数分组，得若干"同次分量"。

**第二步（同次数分解，随机化）**：设 $f$ 是 $k$ 个 $d$ 次不可约多项式之积（无重因子）。

- 若 $p$ 为奇素数：随机取 $h\in\mathbb{F}_p[X]$（$\deg h<\deg f$），计算

$$\gcd\left(f,\ h^{(p^d-1)/2}-1\right).$$

由于各不可约分量 $\mathbb{F}_p[X]/(f_i)\cong\mathbb{F}_{p^d}$ 中，$h^{(p^d-1)/2}$ 随机地落在 $\pm 1$（各半概率），故该 gcd 以约 $1/2$ 概率给出一个非平凡因子。

- 若 $p=2$：改用迹映射 $\operatorname{Tr}(h)=h+h^2+h^4+\cdots+h^{2^{d-1}}$，计算 $\gcd(f,\operatorname{Tr}(h))$，同样以约 $1/2$ 概率拆分。

**递归**：对每个非平凡因子递归应用，直到所有因子不可约。整体期望多项式时间。

```python
def cantor_zassenhaus_split(f, d, p):
    """拆分无重因子、同 d 次的 f 为一个不可约因子 + 余下部分。"""
    while True:
        h = random_poly(len(f) - 1, p)
        if p == 2:
            tr = h
            cur = h
            for _ in range(1, d):
                cur = poly_mul(cur, cur, p)      # cur = h^{2^i}
                cur = poly_mod(cur, f, p)
                tr = poly_add(tr, cur, p)
            g = poly_gcd(f, tr, p)
        else:
            g = poly_gcd(f, poly_sub(pow_poly_mod(h, (p**d - 1)//2, f, p), [1], p), p)
        if g != [1] and g != f:
            return g
```

## 7. Berlekamp 算法

Berlekamp 算法用**线性代数**统一处理同次数分解。核心是构造 **Berlekamp 矩阵**：对 $i=0,\dots,d-1$ 计算 $X^{ip}\bmod f$，其系数排成矩阵 $Q$。则多项式 $g$ 满足 $g^p\equiv g\pmod f$ 当且仅当 $g$ 的系数向量在 $Q-I$ 的**核**中。

对核空间中每个非平凡向量 $g$，计算 $\gcd(f,g)$ 即可得非平凡因子（由 $g^p=g$，$f$ 的每个不可约因子必整除某个 $g-c$，$c\in\mathbb{F}_p$）。

**步骤**：

1. 计算 Berlekamp 矩阵 $Q$，求 $Q-I$ 的核空间基（高斯消元）；
2. 对核空间基向量 $g$，尝试 $\gcd(f,g-c)$ 对 $c=0,\dots,p-1$，收集非平凡因子；
3. 递归分解。

**复杂度**：核空间求基是 $O(d^3)$ 次 $\mathbb{F}_p$ 运算，比 Cantor–Zassenhaus 的随机化更确定，但矩阵运算是主导开销。

## 8. 编码论应用：Reed–Solomon 与 MDS

（整理自 Madhu Sudan, *Essential Coding Theory*, Harvard CS 229r。）

**代数构造把解码翻译成多项式代数**：Reed–Solomon 码是有限域上的多项式求值——取 $\mathbb{F}_q$ 的一个求值点集，码字为次数 $<k$ 的多项式的取值向量。其距离源于一条纯代数事实：**次数 $d$ 的多项式至多 $d$ 个根**，故两个不同码字至多重合 $k-1$ 个位置，相对距离 $\delta = 1-(k-1)/n$。

**Singleton 界与 MDS 码**：任何码满足 $d\le n-k+1$（$k$ 为维数）；Reed–Solomon 码恰好取等号，故称 **MDS（Maximum Distance Separable）码**。这是"速率-距离权衡"在代数构造下的最优实现。

**唯一解码**：靠 Peterson 伴随式与 Welch–Berlekamp 插值求解，可纠错半径 $(d-1)/2$；列表解码（Guruswami–Sudan、折叠 RS）把半径推到容量 $\rho\approx 1-R$。

**为什么归入数论工具**：这些构造与解码器的可实现性，本质依赖有限域上的多项式算术——不可约性检验、多项式 gcd、模幂与平方自由分解，正是本节第 4–7 节的算法。

## 9. 心智模型

1. **有限域 $=\mathbb{F}_p[X]/(f)$**，$f$ 不可约；这是把有限域做成可计算对象的标准手法。
2. **阶必为 $p^d$，且同构唯一**；子域满足 $e\mid d$ 的整除链。
3. **Frobenius 自同构生成全部自同构**，范数与迹是从扩域"压回"基域的两个基本工具。
4. **不可约性检验 = 检查 $\gcd(f,X^{p^e}-X)$**；分解分两步：先按次数分组（确定性），再同次拆分（CZ 随机化 / Berlekamp 线性代数）。
5. **乘法群是循环群**，故有限域上的离散对数可被 index calculus 攻击，也可被更短的椭圆曲线群替代（后者免疫 index calculus）。
