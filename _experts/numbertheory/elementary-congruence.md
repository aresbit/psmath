# 初等数论与同余：整除、Bézout、CRT、单位群

> 整理自 Victor Shoup, *A Computational Introduction to Number Theory and Algebra* (v2, Cambridge University Press, 2008)，第 1 章（整数的基本性质）、第 2 章（同余）。

## 1. 整除、素数、理想

对整数 $a, b$，若存在整数 $c$ 使 $b = ac$，称 $a$ 整除 $b$，记 $a \mid b$。整数 $p > 1$ 称为**素数**，若其正因子只有 $1$ 与 $p$ 自身；否则（$>1$ 且非素）称为**合数**（前几个素数是 $2, 3, 5, 7, 11, 13, \dots$）。

整除是自反、传递关系，但**不是**反对称的：$a\mid b$ 且 $b\mid a$ 只推出 $a = \pm b$。这一"相差一个单位"的差别，正是后面用理想取代元素来研究整除的根本原因。

$\mathbb{Z}$ 的**理想**是满足下两条的非空子集 $I\subseteq\mathbb{Z}$：加法封闭（$a,b\in I\Rightarrow a+b\in I$），吸收律（$a\in I,\ z\in\mathbb{Z}\Rightarrow az\in I$）。

**定理（$\mathbb{Z}$ 是主理想整环，PID）**：$\mathbb{Z}$ 的每个理想 $I$ 都形如 $d\mathbb{Z}=\{dz: z\in\mathbb{Z}\}$。当 $I\neq\{0\}$ 时 $d$ 是 $I$ 中最小正元素。

给定 $a,b$，理想 $a\mathbb{Z}+b\mathbb{Z}$ 必等于某个 $d\mathbb{Z}$，这个 $d$ 就是 $\gcd(a,b)$。由此立刻得到 gcd 的**线性组合性质**（Bézout 恒等式的存在性）：存在整数 $s,t$ 使

$$as + bt = \gcd(a,b).$$

这是全书最通用的一个事实——它是扩展 Euclid 算法、模逆元计算、以及 RSA 解密正确性证明的共同来源。

## 2. 算术基本定理与三个推论

**Euclid 引理**：若素数 $p\mid ab$，则 $p\mid a$ 或 $p\mid b$。证明归结为：若 $p\mid ab$ 且 $p\nmid a$，则 $\gcd(p,a)=1$，由 Bézout 恒等式 $sp+ta=1$ 两边乘 $b$ 得 $p\mid b$。

**定理（算术基本定理，唯一分解）**：每个非零整数 $n$ 可唯一写成

$$n = \pm\prod_{i=1}^{r} p_i^{e_i}, \qquad p_1<p_2<\cdots<p_r\ \text{为素数},\ e_i\ge 1.$$

**推论 1（gcd/lcm 的素数幂表示）**：设 $a=\prod p_i^{e_i},\ b=\prod p_i^{f_i}$（允许指数为 0），则

$$\gcd(a,b) = \prod_i p_i^{\min(e_i,f_i)}, \qquad \mathrm{lcm}(a,b) = \prod_i p_i^{\max(e_i,f_i)}.$$

**推论 2（乘积公式）**：$\gcd(a,b)\cdot\mathrm{lcm}(a,b) = \lvert ab\rvert$。

**推论 3（欧拉函数公式）**：欧拉函数 $\varphi(n)$ 是小于 $n$ 且与 $n$ 互素的正整数个数。若 $n=\prod p_i^{e_i}$，则

$$\varphi(n) = \prod_i p_i^{e_i-1}(p_i-1) = n\prod_{p\mid n}\left(1-\frac{1}{p}\right).$$

$\varphi$ 是**可乘函数**：$\gcd(a,b)=1$ 时 $\varphi(ab)=\varphi(a)\varphi(b)$。这一性质与 $\mathbb{Z}_n^{\ast}$ 的群结构、RSA 的安全性分析直接相关。

## 3. 同余与剩余类

给定正整数 $n$，称 $a$ 与 $b$ **模 $n$ 同余**，记 $a\equiv b\pmod n$，当且仅当 $n\mid(a-b)$。同余是等价关系，且与加、乘相容：$a\equiv a'$ 且 $b\equiv b'$ $\Rightarrow$ $a+b\equiv a'+b'$、$ab\equiv a'b'$。

$a$ 所在的等价类记 $[a]_n$，称为模 $n$ 的**剩余类**。全体剩余类构成环 $\mathbb{Z}_n$，其运算由代表元诱导——良定义性正来自上述相容性。

## 4. 线性同余

**定理（线性同余的可解性）**：方程 $ax\equiv b\pmod n$ 有解当且仅当 $d=\gcd(a,n)\mid b$。此时恰有 $d$ 个模 $n$ 互不同余的解；若 $x_0$ 是一特解，全体解为

$$x = x_0 + \frac{n}{d}\cdot m, \qquad m = 0,1,\dots,d-1.$$

**求特解**：由 Bézout 恒等式存在 $s,t$ 使 $as+nt=d$；当 $b=d\cdot b'$ 时特解 $x_0 = s\cdot b'$。本质是求模逆元。

特别地，当 $\gcd(a,n)=1$ 时 $ax\equiv 1\pmod n$ 有唯一解 $x\equiv a^{-1}\pmod n$，称为 $a$ 的**模 $n$ 逆元**。

## 5. 中国剩余定理（CRT）

**定理（中国剩余定理）**：设 $n_1,\dots,n_k$ 两两互素，$n=\prod n_i$。则映射

$$\theta: \mathbb{Z}_n \to \mathbb{Z}_{n_1}\times\cdots\times\mathbb{Z}_{n_k}, \qquad [a]_n \mapsto \left([a]_{n_1},\dots,[a]_{n_k}\right)$$

是**环同构**。等价地，同余方程组

$$x\equiv a_i \pmod{n_i}, \qquad i=1,\dots,k$$

对任意右端 $a_1,\dots,a_k$ 有唯一解模 $n$。

**构造性证明（Gauss 算法）**：令 $n_i^{\ast}=n/n_i$。因 $\gcd(n_i,n_i^{\ast})=1$，取 $t_i$ 使 $t_i n_i^{\ast}\equiv 1\pmod{n_i}$，则

$$x = \sum_{i=1}^{k} a_i\, n_i^{\ast}\, t_i \pmod n$$

是方程组的解。这一"合并"过程在快速 CRT 重构与多方密钥协商中反复出现。

**增量式 CRT 合并**（逐对合并，只需一次求逆）：

$$x' = x + N\cdot t, \qquad t \equiv (a - x)N^{-1} \pmod n,$$

其中当前解为 $x \pmod N$，要与 $a\pmod n$ 合并。

## 6. 单位群与指数运算

### 6.1 单位群

$[a]_n\in\mathbb{Z}_n$ 可逆当且仅当 $\gcd(a,n)=1$。全体可逆元构成**单位群** $\mathbb{Z}_n^{\ast}$，其阶为

$$\lvert\mathbb{Z}_n^{\ast}\rvert = \varphi(n).$$

### 6.2 Euler 定理与 Fermat 小定理

**定理（Euler 定理）**：对任意 $\gcd(a,n)=1$ 的 $a$，有

$$a^{\varphi(n)} \equiv 1 \pmod n.$$

**定理（Fermat 小定理）**：当 $p$ 为素数且 $p\nmid a$ 时，

$$a^{p-1}\equiv 1 \pmod p.$$

Euler 定理是 Lagrange 定理（有限群的子群阶整除群阶）在 $\mathbb{Z}_n^{\ast}$ 上的直接推论，它给出"模 $n$ 指数化简"的通用规则：指数可以约去 $\varphi(n)$ 的倍数。

**推论（Euler 准则的雏形）**：对奇素数 $p$ 与 $p\nmid a$，二次剩余性由 $a^{(p-1)/2}\equiv\pm 1\pmod p$ 判定（详见 reference `quadratic-residues`）。

## 7. 参考代码

```python
def gcd(a: int, b: int) -> int:
    """辗转相除法（详见 reference euclid-rsa）。"""
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def crt_solve(pairs, modinv):
    """pairs: [(a1, n1), (a2, n2), ...] 两两互素。
    返回 (x, N) 满足 x ≡ ai (mod ni)，N = prod(ni)。"""
    x, N = 0, 1
    for a, n in pairs:
        m = N % n
        inv_m = modinv(m, n)             # 扩展 Euclid 求 m 模 n 的逆元
        t = ((a - x) % n) * inv_m % n
        x = x + N * t
        N = N * n
        x %= N
    return x, N
```

## 8. 心智模型

1. **理想是"正确"的整除语言**：$a\mathbb{Z}+b\mathbb{Z}=d\mathbb{Z}$ 既避开"相差单位"的歧义，又自然给出 Bézout 恒等式。
2. **Bézout 恒等式是全章最值钱的等式**：模逆元、CRT、RSA 解密全部归结为"存在 $s,t$ 使 $as+bt=1$"。
3. **唯一分解不是免费的**：它需要 Euclid 引理，而 Euclid 引理需要 gcd 的线性组合表示。
4. **CRT 是分而治之**：环同构 $\mathbb{Z}_n\cong\prod\mathbb{Z}_{n_i}$ 意味着模 $n$ 的运算可拆到互素因子上做，再合并回来。
5. **解线性同余 = 求模逆元 = 扩展 Euclid**，三者是同一件事的三个名字。
