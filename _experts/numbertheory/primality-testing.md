# 素性检验：试除法、Miller–Rabin 与 AKS

> 整理自 Victor Shoup, *A Computational Introduction to Number Theory and Algebra* (v2, Cambridge University Press, 2008)，第 5 章（素数的分布）、第 10 章（概率素性检验）、第 21 章（确定性素性检验）。

## 1. 试除法与素性检验/分解的不对称

试除法用 $\le\sqrt n$ 的所有素数逐个试除 $n$。由算术基本定理，$n$ 若为合数必有因子 $\le\sqrt n$，故试除法**确定性地**判素。但复杂度为 $O(\sqrt n)$ 次除法，即关于比特长度 $k=\mathrm{len}(n)$ 是**指数级** $O(2^{k/2})$。它只适用于小整数或"验到某上界"的部分分解。

这揭示了素性检验与整数分解的**不对称性**：判素（Miller–Rabin、AKS）是多项式时间，而分解（index calculus）是亚指数时间。二者难度悬殊，正是 RSA 安全性的基础。

## 2. 素数的分布（初等估计）

**素数计数函数**：

$$\pi(x) := \lvert\{p\le x: p\ \text{是素数}\}\rvert.$$

**定理（Chebyshev）**：存在正常数 $c_1<c_2$，使对所有足够大的 $x$，

$$c_1\frac{x}{\ln x} \le \pi(x) \le c_2\frac{x}{\ln x}.$$

**证明思路**：核心工具是中心二项式系数 $\binom{2n}{n}$。其素数分解中每个素数 $p$ 的指数由 Legendre 公式给出 $\sum_{k\ge 1}\lfloor 2n/p^k\rfloor - 2\lfloor n/p^k\rfloor$；另一方面 $\binom{2n}{n}<4^n$。比较两侧对数，即得 $\pi(x)$ 的上下界。Chebyshev 完全初等地夹住了主项 $x/\ln x$，只差常数因子。

**定理（Bertrand 公设）**：对每个整数 $n>1$，存在素数 $p$ 满足 $n<p<2n$。等价地区间 $(n,2n]$ 内至少有一个素数，可由 Chebyshev 定理推出。

**算法意义**：随机生成素数时，可在 $[2^k,2^{k+1})$ 内随机取数、逐个试除，期望只需检查 $O(k)$ 个数就遇到一个素数——因为密度下界是 $1/\ln(2^{k+1})=\Theta(1/k)$。这使随机素数生成可行。

**定理（Mertens）**：存在常数 $B_1$ 使

$$\sum_{p\le x}\frac{1}{p} = \ln\ln x + B_1 + o(1); \qquad \sum_{p\le x}\frac{\ln p}{p} = \ln x + O(1).$$

素数倒数和的发散（$\ln\ln x$）说明素数"足够密"；后一式是 index calculus 中 **smooth 数密度**分析的核心。

**Eratosthenes 筛**：枚举 $\le n$ 的全部素数，复杂度 $O(n\log\log n)$（由 Mertens 定理 $\sum_{p\le\sqrt n}n/p = n\log\log n$），空间 $O(n)$。

```python
def sieve(n: int):
    """Eratosthenes 筛：返回 [2, n] 内所有素数。"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1
    return [i for i in range(2, n + 1) if is_prime[i]]
```

**素数定理（PNT）**：$\pi(x)\sim x/\ln x$。经典证明需解析工具（$\zeta(s)$ 在 $\operatorname{Re}s=1$ 无零点），超出初等范围；而 Chebyshev 定理、Bertrand 公设、Mertens 定理都可用完全初等方法证明。对算法分析而言，Chebyshev 的常数界往往已足够——**算法只关心"多项式上界"，不关心渐近常数**。

## 3. Miller–Rabin 检验

设 $n$ 为待测奇数（$n>1$），$\mathbb{Z}_n^{+}$ 为 $\mathbb{Z}_n$ 的非零元素集合（$\lvert\mathbb{Z}_n^{+}\rvert=n-1$）。

**一般框架**：定义集合 $L_n\subseteq\mathbb{Z}_n^{+}$，满足：

1. 存在高效算法判定 $\alpha\in L_n$；
2. 若 $n$ 素数，则 $L_n=\mathbb{Z}_n^{\ast}$；
3. 若 $n$ 合数，则 $\lvert L_n\rvert\le c(n-1)$，$c<1$ 为常数。

随机取 $k$ 个 $\alpha_1,\dots,\alpha_k\in\mathbb{Z}_n^{+}$，若全在 $L_n$ 中则输出"素数"，否则"合数"。素数必输出正确；合数误判为素数的概率 $\le c^k$。

**第一次尝试（Fermat 检验）**：取 $L_n:=\{\alpha\in\mathbb{Z}_n^{+}:\alpha^{n-1}=1\}$。由 Lagrange 定理，素数时 $L_n=\mathbb{Z}_n^{\ast}$。但存在 **Carmichael 数**——满足 $L_n=\mathbb{Z}_n^{\ast}$ 的合数，最小者 $561=3\cdot 11\cdot 17$。故第一次尝试失败。

**Miller–Rabin 的修正**：写 $n-1=t\cdot 2^h$，$t$ 为奇数（$h\ge 1$）。定义

$$L'_n := \left\{\alpha\in\mathbb{Z}_n^{+}: \alpha^{t\cdot 2^h}=1\ \text{且}\ \alpha^{t\cdot 2^{j+1}}=1\Rightarrow\alpha^{t\cdot 2^j}=\pm 1,\ j=0,\dots,h-1\right\}.$$

即：从 $\alpha^t$ 起反复平方到 $\alpha^{n-1}$，若中途出现 $1$，则其前一步必须是 $\pm 1$。这一条件恰好捕捉"$\mathbb{Z}_n^{\ast}$ 中平方根只有 $\pm 1$"这一素数特有性质。

```python
def in_L_prime(alpha: int, n: int, t: int, h: int) -> bool:
    """判断 alpha 是否属于 Miller–Rabin 集合 L'_n，其中 n-1 = t * 2^h。"""
    beta = pow(alpha, t, n)          # beta = alpha^t
    if beta == 1:
        return True
    for _ in range(h):
        if beta == n - 1:            # beta == -1 (mod n)
            return True
        if beta == 1:                # 提前出现 1 但前一步不是 ±1
            return False
        beta = beta * beta % n
    return False
```

该过程用平方-乘算法在 $O(\mathrm{len}(n)^3)$ 时间内完成。

### 正确性与错误概率

**定理（Miller–Rabin 的核心）**：若 $n$ 素数，则 $L'_n=\mathbb{Z}_n^{\ast}$；若 $n$ 合数，则

$$\lvert L'_n\rvert \le \frac{n-1}{4}.$$

**证明要点**：

- **素数情形**：$\mathbb{Z}_n^{\ast}$ 是 $n-1$ 阶循环群，每个 $\alpha$ 满足 $\alpha^{n-1}=\alpha^{t\cdot 2^h}=1$。对满足 $\alpha^{t\cdot 2^{j+1}}=1$ 的 $j$，令 $\beta=\alpha^{t\cdot 2^j}$，则 $\beta^2=1$；循环群中阶整除 2 的元素恰为 $\pm 1$。
- **合数情形**（$n=p^e$ 素幂，$e>1$）：$L'_n$ 含于"$n-1$ 次幂映射"的核 $K$，$\lvert K\rvert=\gcd(\varphi(n),n-1)$。由 $\varphi(n)=p^{e-1}(p-1)$ 可算出 $\lvert L'_n\rvert\le\lvert K\rvert=p-1\le(n-1)/4$。
- **一般合数**：用 CRT 把 $\mathbb{Z}_n^{\ast}$ 分量到各素数幂分量，综合各界。

**推论**：重复 $k$ 次独立 Miller–Rabin 检验，合数误判为素数的概率 $\le(1/4)^k$。取 $k=64$，错误概率 $\le 2^{-128}$。

```python
def miller_rabin(n: int, rounds: int = 64) -> bool:
    """Miller–Rabin 素性检验（Monte Carlo）。"""
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n % p == 0:
            return n == p
    t, h = n - 1, 0
    while t % 2 == 0:
        t //= 2
        h += 1
    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        if not in_L_prime(a, n, t, h):
            return False      # 确定是合数
    return True               # 大概率是素数
```

**运行时间**：$O(k\cdot\mathrm{len}(n)^3)$。生成一个 $k$ 位素数，结合密度下界，总期望 $O(k^4)$。

### 分解与欧拉函数的等价

**计算 $\varphi(n)$ 与分解 $n$ 是多项式等价的**。一方面分解 $n$ 后 $\varphi(n)$ 可直接由乘积公式算出；另一方面若已知 $\varphi(n)$，则 $p,q$ 可由二次方程

$$X^2 - (n-\varphi(n)+1)X + n = 0$$

的根恢复（当 $n=pq$）。因此任何能高效求 $\varphi$ 的算法都能高效分解 $n$——这解释了为何 RSA 中 $\varphi(n)$ 必须保密。

### 一个副产品

若 $\alpha^{t\cdot 2^{j+1}}=1$ 但 $\alpha^{t\cdot 2^j}\ne\pm 1$，则 $\gcd(\alpha^{t\cdot 2^j}-1, n)$ 是 $n$ 的非平凡因子（这正是 Dixon 分解的思路之一）。

## 4. AKS：PRIMES ∈ P

Miller–Rabin 是概率算法。**AKS 算法**（Agrawal–Kayal–Saxena, 2002）**确定性**地、在多项式时间内判定素数，证明素性检验 $\in\mathrm{P}$。

### 基本恒等式

**定理（素性的代数刻画）**：设 $n>1$。若 $n$ 素数，则对所有 $a\in\mathbb{Z}_n$，在环 $\mathbb{Z}_n[X]$ 中有

$$(X+a)^n = X^n + a. \tag{1}$$

反之，若 $n$ 合数，则对所有 $a\in\mathbb{Z}_n^{\ast}$，(1) 不成立。

**证明要点**：由二项式定理

$$(X+a)^n = X^n + a^n + \sum_{i=1}^{n-1}\binom{n}{i}a^i X^{n-i}.$$

- **素数情形**：Fermat 小定理给出 $a^n=a$；且 $\binom{n}{i}$ 对 $i=1,\dots,n-1$ 都被 $n$ 整除，故中间项消失。
- **合数情形**：取 $n$ 的素因子 $p$，写 $n=p^k m$（$p\nmid m$），可证 $p^k\nmid\binom{n}{p}$，于是 $a\in\mathbb{Z}_n^{\ast}$ 时 $X^{n-p}$ 的系数非零。

**问题**：直接展开 (1) 需 $O(n)$ 项，指数级。AKS 的关键洞察：若 (1) 在**模 $X^r-1$** 下对"足够多"的 $a$ 成立，则 $n$ 必为素数；而合适的 $r$ 与 $a$ 的个数都可用 $\mathrm{len}(n)$ 的多项式界住。

### 算法

```
AKS(n), 输入 n > 1:
1. 若 n 形如 a^b（a > 1, b > 1），返回 false
2. 找最小的整数 r > 1 使：
     要么 gcd(n, r) > 1
     要么 gcd(n, r) = 1 且 [n]_r 在 Z_r^* 中的乘法阶 > 4·len(n)^2
3. 若 r = n，返回 true
4. 若 gcd(n, r) > 1，返回 false
5. 对 j = 1 到 2·len(n)·⌊r^{1/2}⌋ + 1：
      若 (X + j)^n ≠ X^n + j (mod X^r - 1) 于环 Z_n[X]，返回 false
6. 返回 true
```

**运行时间定理**：存在满足第 2 步条件的 $r$，且 $r=O(\mathrm{len}(n)^5)$。证明用"坏素数"的计数：若 $r$ 不满足条件，则 $r\mid n$ 或 $r\mid(n^d-1)$（某 $d\le 4\mathrm{len}(n)^2$），故所有坏素数的乘积整除 $n\prod_{d=1}^{m}(n^d-1)$。取对数并利用素数分布界 $\sum_{r\le x}\log r\ge cx$，得 $r$ 的多项式上界。

**推论（总复杂度）**：AKS 可实现为 $O(\mathrm{len}(n)^{16.5})$ 时间。主导开销在第 5 步：需 $O(r^{1/2}\mathrm{len}(n))$ 次"模 $X^r-1$、指数为 $n$"的幂运算，每次 $O(\mathrm{len}(n))$ 次 $\mathbb{Z}_n[X]/(X^r-1)$ 运算，每次 $O(r^2)$ 次 $\mathbb{Z}_n$ 运算，每次 $O(\mathrm{len}(n)^2)$。

**正确性**：

- **素数输入必输出 true**：第 1 步（完美幂检验）失败，第 2 步的 $r$ 满足条件，第 5 步由定理 (1) 全部通过。
- **合数输入必输出 false**：需用"模 $X^r-1$ 的恒等式对足够多 $a$ 成立则 $n$ 是素数幂"这一反方向结论（依赖 $r$ 的选择与 $n$ 在 $\mathbb{Z}_r^{\ast}$ 中的阶）。

### 实现要点

- **第 1 步完美幂检验**：对 $b=2,\dots,\lfloor\log_2 n\rfloor$ 二分求 $n$ 的 $b$ 次根是否为整数，多项式时间。
- **第 2 步**：对 $r$ 暴力搜索；验证 $[n]_r$ 在 $\mathbb{Z}_r^{\ast}$ 中的阶，只需在 $\gcd(n,r)=1$ 后反复计算 $n$ 的幂模 $r$ 直到回到 1。
- **第 5 步**：在 $\mathbb{Z}_n[X]/(X^r-1)$ 中做模幂，是标准的多项式幂运算。

### 历史意义

AKS 的意义不在工程效率（$O(\mathrm{len}(n)^{16.5})$ 远慢于 Miller–Rabin 或 ECPP），而在于**证明了 PRIMES $\in$ P**，终结了一个自 1970 年代悬而未决的复杂度问题。此后 Lenstra–Pomerance、Bernstein 等把常数大幅改进（理论上接近 $O(\mathrm{len}(n)^6)$），但实践中 Miller–Rabin 仍是首选，AKS 更多用于理论确定性与教学。

## 5. 心智模型

1. **Miller–Rabin 用"平方根只有 $\pm 1$"这一素数特征**设计检验集 $L'_n$，把错误概率压到 $1/4$，可重复任意降低。
2. **Carmichael 数是 Fermat 检验的盲区**，Miller–Rabin 通过检查"中途平方"绕开它们。
3. **素性检验与分解的复杂度鸿沟**：判素多项式时间，分解亚指数时间，这是现代密码学的基石。
4. **$\varphi(n)$ 与分解 $n$ 等价**，故 RSA 的私钥必须严格保密。
5. **$(X+a)^n\equiv X^n+a$ 是素性的完整代数刻画**，"模 $X^r-1$"是 AKS 的核心创新。
