# 二次剩余、Legendre/Jacobi 符号与二次互反律

> 整理自 Victor Shoup, *A Computational Introduction to Number Theory and Algebra* (v2, Cambridge University Press, 2008)，第 12 章（二次互反律与模平方根）。

给定奇素数 $p$，问整数 $a$ 是不是模 $p$ 的**二次剩余**——即是否存在 $x$ 使 $x^2\equiv a\pmod p$。Legendre/Jacobi 符号给出完整判定理论，二次互反律是数论的皇冠定理，模平方根算法是 Rabin 密码系统的基础。

## 1. Legendre 符号

对奇素数 $p$ 与整数 $a$，定义

$$\left(\frac{a}{p}\right) = \begin{cases} 1, & a\ \text{是模 } p\ \text{的二次剩余且}\ p\nmid a,\\ -1, & a\ \text{不是二次剩余且}\ p\nmid a,\\ 0, & p\mid a.\end{cases}$$

**定理（基本性质）**：设 $p$ 为奇素数，$a,b\in\mathbb{Z}$：

1. **Euler 准则**：$\left(\frac{a}{p}\right)\equiv a^{(p-1)/2}\pmod p$；特别地 $\left(\frac{-1}{p}\right)=(-1)^{(p-1)/2}$；
2. **可乘性**：$\left(\frac{a}{p}\right)\left(\frac{b}{p}\right)=\left(\frac{ab}{p}\right)$；
3. **周期性**：$a\equiv b\pmod p\Rightarrow\left(\frac{a}{p}\right)=\left(\frac{b}{p}\right)$；
4. $\left(\frac{2}{p}\right)=(-1)^{(p^2-1)/8}$；
5. **二次互反律**：若 $q$ 为奇素数，则

$$\left(\frac{p}{q}\right) = (-1)^{\frac{p-1}{2}\frac{q-1}{2}}\left(\frac{q}{p}\right).$$

**推论**：$-1$ 是模 $p$ 二次剩余当且仅当 $p\equiv 1\pmod 4$；$2$ 是二次剩余当且仅当 $p\equiv\pm 1\pmod 8$。互反律说明 $\left(\frac{p}{q}\right)$ 与 $\left(\frac{q}{p}\right)$ 同号当且仅当 $p\equiv 1\pmod 4$ 或 $q\equiv 1\pmod 4$。

**应用示例**：判定 5 是否为模 $p$ 二次剩余。因 $5\equiv 1\pmod 4$，互反律给出 $\left(\frac{5}{p}\right)=\left(\frac{p}{5}\right)$，而模 5 的二次剩余是 $\pm 1$，故 5 是二次剩余当且仅当 $p\equiv\pm 1\pmod 5$。

## 2. Gauss 引理

**定理（Gauss 引理）**：设 $p$ 为奇素数，$p\nmid a$。定义 $\alpha_j := ja\bmod p$（$j=1,\dots,(p-1)/2$），令 $n$ 为满足 $\alpha_j>p/2$ 的下标个数。则

$$\left(\frac{a}{p}\right)=(-1)^n.$$

**证明思路**：设 $r_1,\dots,r_n$ 为超过 $p/2$ 的 $\alpha_j$，$s_1,\dots,s_k$ 为其余的。它们互异且非零，且序列 $s_1,\dots,s_k,p-r_1,\dots,p-r_n$ 恰好是 $1,\dots,(p-1)/2$ 的一个重排。于是

$$\left(\frac{p-1}{2}\right)! \equiv s_1\cdots s_k(-r_1)\cdots(-r_n) \equiv (-1)^n\left(\frac{p-1}{2}\right)!\,a^{(p-1)/2}\pmod p.$$

约去 $\left(\frac{p-1}{2}\right)!$ 得 $a^{(p-1)/2}\equiv(-1)^n\pmod p$，再由 Euler 准则即得结论。

**加强形式**：

$$\left(\frac{a}{p}\right)=(-1)^t, \qquad t=\sum_{j=1}^{(p-1)/2}\left\lfloor\frac{ja}{p}\right\rfloor.$$

取 $a=2$ 即得 $\left(\frac{2}{p}\right)=(-1)^{(p^2-1)/8}$；对一般奇素数 $q$ 做细致计数即得二次互反律。整个证明完全初等，仅用带余除法与奇偶计数。

## 3. Jacobi 符号

**定义**：对奇数 $n=\prod p_i^{e_i}$，定义

$$\left(\frac{a}{n}\right) := \prod_{i}\left(\frac{a}{p_i}\right)^{e_i}.$$

**关键性质**：Jacobi 符号满足与 Legendre 符号相同的运算律——可乘性、周期性、以及**广义二次互反律**（对任意奇数 $m,n$）。更重要的是，它可以在**不分解 $n$** 的前提下用 Euclid 算法的高效变体（反复应用互反律与"除以 2"规则）在 $O(\mathrm{len}(n)^2)$ 时间内算出。

**重要区别**：$\left(\frac{a}{n}\right)=1$ **不**意味着 $a$ 是模 $n$ 的二次剩余（$n$ 合数时）；它只是各分量乘积为 1。这正是**二次剩余假设（QR assumption）**的微妙之处。

```python
def jacobi(a: int, n: int) -> int:
    """计算 Jacobi 符号 (a/n)，n 为正奇数。"""
    assert n > 0 and n % 2 == 1
    a %= n
    result = 1
    while a != 0:
        while a % 2 == 0:                    # 处理因子 2
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a                          # 应用互反律
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0
```

## 4. 计算模平方根

**问题**：给定奇素数 $p$ 与二次剩余 $a$，求 $x$ 使 $x^2\equiv a\pmod p$。

**$p\equiv 3\pmod 4$ 的情形（简单）**：$x=a^{(p+1)/4}$ 即为一个根。因为

$$\left(a^{(p+1)/4}\right)^2 \equiv a^{(p+1)/2} \equiv a\cdot a^{(p-1)/2} \equiv a\cdot 1 \equiv a \pmod p.$$

**$p\equiv 1\pmod 4$ 的情形（Tonelli–Shanks 算法）**：写 $p-1=2^s\cdot q$（$q$ 奇数），$s\ge 2$。找一个非二次剩余 $z$，令 $M=s$，$c=z^q$，$t=a^q$，$R=a^{(q+1)/2}$。迭代调整 $R,t,M$，使不变量 $t^{2^{M-1}}=1$ 与 $R^2\equiv at$ 保持，最终得到根。复杂度 $O(\mathrm{len}(p)^3)$ 量级。

模平方根算法的密码学应用是 **Rabin 加密**：$c=m^2\bmod n$（$n=pq$），解密需求 $c$ 模 $p$ 与模 $q$ 的平方根，再用 CRT 合并——这需要知道 $p,q$，与分解 $n$ 等价。

## 5. 二次剩余假设（QR 假设）

**QR 假设**：给定 $n=pq$ 与一个满足 $\left(\frac{a}{n}\right)=1$ 的 $a$，**无法**在多项式时间内判定 $a$ 是否是模 $n$ 的二次剩余（即 $a$ 是否同时是模 $p$、模 $q$ 的二次剩余），除非能分解 $n$。

这一假设是 Goldwasser–Micali 语义安全加密、以及许多零知识证明系统的安全基石。它精确刻画了"Jacobi 符号可算、但二次剩余性不可判"这一不对称性。

## 6. 心智模型

1. **Euler 准则把二次剩余判定化为一次模幂**：$\left(\frac{a}{p}\right)\equiv a^{(p-1)/2}$。
2. **二次互反律让 Legendre 符号的计算互相归约**，配合"除 2"规则，Jacobi 符号可在 $O(\mathrm{len}(n)^2)$ 内计算而无需分解 $n$。
3. **Gauss 引理是互反律的初等证明核心**，只用带余除法与奇偶计数。
4. **$\left(\frac{a}{n}\right)=1$ 不等于 $a$ 是模 $n$ 二次剩余**（$n$ 合数时）——这是 QR 假设成立的全部微妙之处。
5. **QR 假设揭示"可算符号"与"可判剩余性"之间的鸿沟**，是公钥密码安全性的又一支柱。
