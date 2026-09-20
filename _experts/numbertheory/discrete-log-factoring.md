# 离散对数与整数分解：本原根、baby-step giant-step、index calculus

> 整理自 Victor Shoup, *A Computational Introduction to Number Theory and Algebra* (v2, Cambridge University Press, 2008)，第 11 章（生成元与离散对数）、第 15 章（亚指数时间离散对数与整数分解）。

## 1. 寻找生成元

$\mathbb{Z}_p^{\ast}$（$p$ 素数）是循环群，其生成元即**本原根**。

**判定准则**：$g\in\mathbb{Z}_p^{\ast}$ 是生成元当且仅当对 $p-1$ 的每个素因子 $q$，都有

$$g^{(p-1)/q}\not\equiv 1 \pmod p.$$

**理由**：$g$ 的阶整除 $p-1$（Lagrange 定理）。$g$ 的阶严格小于 $p-1$ 当且仅当存在素因子 $q\mid(p-1)$ 使 $g$ 的阶整除 $(p-1)/q$，即 $g^{(p-1)/q}=1$。逐条排除即确认阶为 $p-1$。

```python
def is_generator(g: int, p: int, prime_factors: list[int]) -> bool:
    """判断 g 是否为 Z_p^* 的生成元，需给定 p-1 的素因子分解。"""
    for q in prime_factors:
        if pow(g, (p - 1) // q, p) == 1:
            return False
    return True


def find_generator(p: int, prime_factors: list[int]) -> int:
    while True:
        g = random.randrange(2, p)
        if is_generator(g, p, prime_factors):
            return g
```

**期望成本**：$\mathbb{Z}_p^{\ast}$ 中生成元共有 $\varphi(p-1)$ 个，密度为 $\varphi(p-1)/(p-1)$。虽无常数下界，但实践中密度足够大，随机采样很快命中。代价是**必须先分解 $p-1$**——这本身一般困难，因此实用中常选"安全素数" $p=2q+1$（$q$ 也素），此时 $p-1=2q$ 分解平凡，生成元极易判定。

## 2. 离散对数问题与 baby-step giant-step

**离散对数问题（DLP）**：给定素数 $p$、生成元 $g$ 与 $y\in\mathbb{Z}_p^{\ast}$，求 $x\in[0,p-1)$ 使 $g^x\equiv y\pmod p$。

**蛮力**：逐一尝试 $x=0,1,\dots$，复杂度 $O(p)$，指数级。

**Baby-step Giant-step（Shanks 算法）**：设 $m=\lceil\sqrt{p-1}\rceil$，写 $x=im+j$（$0\le i,j<m$）。由 $g^{im+j}=y$ 得

$$g^j = y\cdot(g^{-m})^i.$$

1. 预计算 "baby steps"：哈希表存 $\{g^j: j=0,\dots,m-1\}$；
2. 计算 "giant steps"：令 $c=g^{-m}$，$z=y$，对 $i=0,1,\dots$ 查 $z$ 是否在表中；命中则 $x=im+j$。

时间与空间均为 $O(\sqrt{p-1})$，即关于 $k=\mathrm{len}(p)$ 是 $O(2^{k/2})$。它把"枚举所有 $x$"改进为"折半时间换空间"，是生日悖论思想的直接应用。

```python
def baby_step_giant_step(g: int, y: int, p: int) -> int:
    """在 Z_p^* 中解 g^x = y (mod p)，返回 x。"""
    import math
    m = math.isqrt(p - 1) + 1
    table = {}                            # g^j -> j
    cur = 1
    for j in range(m):
        if cur not in table:
            table[cur] = j
        cur = cur * g % p
    gm = pow(g, m, p)
    ginv_m = pow(gm, p - 2, p)            # (g^m)^{-1}
    z = y
    for i in range(m):
        if z in table:
            return i * m + table[z]
        z = z * ginv_m % p
    raise ValueError("no discrete logarithm found")
```

更快的算法：Pohlig–Hellman 利用 $p-1$ 光滑性；index calculus 达亚指数。

## 3. Diffie–Hellman 密钥协商

**协议**：公开参数为素数 $p$ 与生成元 $g$。

1. Alice 选秘密 $a$，发送 $A=g^a\bmod p$；
2. Bob 选秘密 $b$，发送 $B=g^b\bmod p$；
3. 双方各自计算共享密钥 $K=B^a\equiv A^b\equiv g^{ab}\pmod p$。

**安全性**：窃听者只能看到 $p,g,A,B$，恢复 $K$ 需从 $A$ 算出 $a$（或从 $B$ 算 $b$），即求解**离散对数**；更精确地说，依赖于**计算性 Diffie–Hellman（CDH）**假设（给定 $g^a,g^b$ 求 $g^{ab}$ 困难）与更强的**判定性 Diffie–Hellman（DDH）**假设（$g^{ab}$ 与随机群元素不可区分）。

```python
def diffie_hellman(p: int, g: int, a_priv: int, b_priv: int):
    A = pow(g, a_priv, p)
    B = pow(g, b_priv, p)
    K_alice = pow(B, a_priv, p)
    K_bob = pow(A, b_priv, p)
    assert K_alice == K_bob
    return K_alice
```

朴素 Diffie–Hellman 不提供身份认证，易受**中间人攻击**，实际系统需叠加数字签名或证书。

## 4. 光滑数

整数 $n$ 称为 **$y$-光滑**，若 $n$ 的所有素因子都 $\le y$。光滑数的密度决定 index calculus 的效率。

**密度估计（Canfield–Erdős–Pomerance）**：设 $\psi(x,y)$ 为 $\le x$ 且 $y$-光滑的整数个数。当 $u=\ln x/\ln y$ 适中时，

$$\psi(x,y) \approx x\cdot u^{-u}.$$

直观地，若取 $y$ 使 $\ln y\approx\sqrt{\ln x\,\ln\ln x}$（即 $u\approx\sqrt{\ln x/\ln\ln x}$），则光滑数占比约 $u^{-u}=L_x[1/2,-1/2]$——恰好匹配亚指数复杂度。严格化依赖 Mertens 定理。

## 5. 离散对数的 index calculus

**目标**：在 $\mathbb{Z}_p^{\ast}$ 中解 $g^x=y$。

**预计算**：

1. 选**因子基** $B=\{q_1,\dots,q_k\}$（小素数集合）；
2. 随机取 $r$，尝试分解 $g^r\bmod p$；若其所有素因子都在 $B$ 中（即 $g^r$ 是 $B$-光滑），得一条**关系**：

$$g^r \equiv \prod_{i=1}^{k} q_i^{e_i}\pmod p \quad\Rightarrow\quad r\equiv\sum_{i=1}^{k} e_i\log_g q_i \pmod{p-1};$$

3. 收集 $\ge k$ 条线性无关的关系，得到关于未知量 $\log_g q_i$ 的线性方程组（模 $p-1$）；
4. 用高斯消元解出所有 $\log_g q_i$。

**求目标对数**：随机取 $r$ 使 $y\cdot g^r$ 是 $B$-光滑，得

$$\log_g y + r \equiv \sum_{i} e_i\log_g q_i \pmod{p-1},$$

从而解出 $\log_g y$。

**复杂度**：取 $\lvert B\rvert\approx L_p[1/2,1/2]$，总时间约 $L_p[1/2,c]$，远快于 $O(\sqrt p)$。这是对 $\mathbb{Z}_p^{\ast}$ 离散对数最强的通用攻击，也是 Diffie–Hellman 必须用 2048 位素数、或改用椭圆曲线的原因。

## 6. 整数的 index calculus（Dixon 分解）

同一框架可分解 $n$：

1. 选因子基 $B$；
2. 随机取 $r$，计算 $r^2\bmod n$，若 $B$-光滑则记 $r^2\equiv\prod q_i^{e_i}\pmod n$；
3. 收集关系，在 $\mathbb{F}_2$ 上解线性方程组，找若干关系使指数向量之和为偶，得**同余平方** $x^2\equiv y^2\pmod n$；
4. 若 $x\ne\pm y\pmod n$，则 $\gcd(x-y,n)$ 是 $n$ 的非平凡因子。

核心思想：由 $x^2\equiv y^2\pmod n$ 得 $(x-y)(x+y)\equiv 0\pmod n$，故 $x-y$ 与 $n$ 有非平凡公因子（除非 $x\equiv\pm y$）。"碰运气"概率 $\ge 1/2$。

```python
def dixon_factor(n: int, B: list[int]):
    """Dixon 随机平方分解（示意，省略线性代数细节）。"""
    relations = []                       # 每条: (r, 指数向量 mod 2)
    while len(relations) < len(B) + 1:
        r = random.randrange(2, n)
        z = (r * r) % n
        vec = []
        for q in B:
            e = 0
            while z % q == 0:
                z //= q
                e += 1
            vec.append(e % 2)
        if z == 1:                       # r^2 是 B-光滑
            relations.append((r, vec))
    # 在 F_2 上找指数向量之和为零的子集，得 x^2 ≡ y^2 (mod n)
    # ...（线性代数）...
    # return gcd(x - y, n)
```

**复杂度**：Dixon 约 $L_n[1/2,c]$。后续的**二次筛法**与**数域筛法（NFS）**把 $\alpha$ 进一步降至 $1/2$（常数更优）乃至 $1/3$（NFS，$L_n[1/3,c]$）。NFS 是当前分解 RSA 模数的最强算法。

## 7. 亚指数复杂度记号

**定义**：对 $\alpha\in[0,1]$ 与常数 $c$，

$$L_n[\alpha,c] := \exp\left(c(\ln n)^{\alpha}(\ln\ln n)^{1-\alpha}\right).$$

- $\alpha=0$：多项式时间 $L_n[0,c]=(\ln n)^c$；
- $\alpha=1$：指数时间 $L_n[1,c]=n^c$；
- $\alpha=1/2$：介于两者之间的**亚指数**时间。

index calculus 类算法落在 $\alpha=1/2$，NFS 落在 $\alpha=1/3$。这一记号是理解"为什么 RSA-2048 安全而 RSA-512 已被分解"的标准语言。

## 8. 心智模型

1. **生成元判定只需 $p-1$ 的素因子**：逐个检查 $g^{(p-1)/q}\ne 1$；求生成元依赖分解 $p-1$，这解释了"安全素数" $p=2q+1$ 的实用动机。
2. **Baby-step giant-step 是生日悖论的应用**：$O(\sqrt p)$ 时间空间，比蛮力 $O(p)$ 好但仍指数级。
3. **Diffie–Hellman 的安全性归约到 DLP/CDH/DDH**，是公钥密码学的经典困难假设链；朴素版无认证，需防中间人。
4. **光滑数是 index calculus 的燃料**，其密度由 CEP 给出 $u^{-u}$ 形式。
5. **离散对数与分解共享同一框架**：收集光滑关系 → 解线性方程组 → 提取答案。
6. **NFS 是当前最强**（$L_n[1/3]$）；**椭圆曲线群免疫 index calculus**，故密钥更短（这是我的知识源只在"替代群"意义上触及椭圆曲线的边界处）。
