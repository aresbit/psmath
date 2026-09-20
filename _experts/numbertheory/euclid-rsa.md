# Euclid 算法、模逆元、有理数重构与 RSA

> 整理自 Victor Shoup, *A Computational Introduction to Number Theory and Algebra* (v2, Cambridge University Press, 2008)，第 4 章（Euclid 算法）。

Euclid 算法是计算数论的核心引擎：它高效求 gcd、模逆元、做中国剩余重构，并直接支撑 RSA。

## 1. 基本 Euclid 算法

对输入 $a\ge b>0$，反复做带余除法：

$$a = bq + r, \qquad 0\le r < b.$$

由 Euclid 引理 $\gcd(a,b)=\gcd(b,r)$。不断替换 $(a,b)\leftarrow(b,r)$ 直到 $r=0$，此时 $\gcd(a,b)=b$。

```python
def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
```

### 运行时间分析

**定理**：Euclid 算法对 $a\ge b>0$ 的运行时间是 $O(\mathrm{len}(a)\mathrm{len}(b))$ 次比特操作，$\mathrm{len}(x)$ 表示 $x$ 的比特长度。

**Lamé 定理**：辗转相除的步数不超过 $5$ 倍于 $b$ 的十进制位数。更精确地，若 $b$ 的比特长度为 $k$，步数至多为 Fibonacci 数的某个下标量级；相邻 Fibonacci 数之比趋于黄金比 $\varphi=(1+\sqrt5)/2$，每步余数至少按常数比例缩小，故总步数 $O(\mathrm{len}(b))$。

**最坏情况**恰是**连续 Fibonacci 数**：对 $F_{k+1},F_k$，每步余数依次为 $F_{k-1},F_{k-2},\dots$，需约 $k$ 步。故 $F_{n+2},F_{n+1}$ 恰好需要 $n$ 步。

## 2. 扩展 Euclid 算法

扩展版本在计算 gcd 的同时维护两个不变量，最终输出 Bézout 系数 $s,t$ 与 $d=\gcd(a,b)$，满足

$$as + bt = d.$$

```python
def extended_gcd(a: int, b: int):
    """返回 (g, s, t) 使 g = gcd(a,b) = a*s + b*t。"""
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t
```

**不变量**：每一步都保持 $a\cdot s + b\cdot t = r$。结束时 $r=0$，前一行的 $old_r=\gcd(a,b)$，$old_s,old_t$ 即 Bézout 系数。运行时间与基本算法同阶 $O(\mathrm{len}(a)\mathrm{len}(b))$。

## 3. 模逆元与 CRT 重构

### 3.1 模逆元

求 $a$ 模 $n$ 的逆元（$\gcd(a,n)=1$）：调用 `extended_gcd(a, n)` 得 $s$ 使 $as+nt=1$，则 $a^{-1}\equiv s\pmod n$。

### 3.2 快速 CRT 重构

Gauss 算法需 $k$ 次求逆。实际中常用**增量式 CRT**（逐对合并）：维护当前解 $x\pmod N$，与下一组 $a\pmod n$ 合并时只需求 $N$ 模 $n$ 的一次逆元：

$$x' = x + N\cdot t, \qquad t\equiv (a-x)N^{-1}\pmod n.$$

总成本 $O(k\cdot\mathrm{len}(n)^2)$ 量级。

### 3.3 模运算加速

一个大整数运算可"并行化"到模运算：若需精确计算大乘积/大行列式，先在多个互素的模数下分别计算，再用 CRT 合并出真值——只要模数乘积超过结果的上界。这在多项式与线性代数中被系统使用。

## 4. 有理数重构

**问题**：已知模 $n$ 的余数 $\bar a$ 与上界 $B$，恢复有理数 $a=x/y$，其中 $0\le x<B$、$0<y<B$、$\gcd(x,y)=1$、$\gcd(y,n)=1$，使 $\bar a\equiv xy^{-1}\pmod n$。

**定理（重构条件）**：当 $n>2B^2$ 时，若解存在则唯一。算法就是对输入 $n,\bar a$ 运行扩展 Euclid，在某一步余数首次降到 $B$ 以下时读出 $(x,y)$。

有理数重构是**纠错码**（BCH/Reed–Solomon 解码）与 **Padé 逼近**的算术内核。

## 5. RSA 密码系统

RSA 串联了前述所有工具。

**密钥生成**：选大素数 $p,q$，令 $n=pq$，$\varphi(n)=(p-1)(q-1)$；选 $e$ 使 $\gcd(e,\varphi(n))=1$，用扩展 Euclid 求 $d\equiv e^{-1}\pmod{\varphi(n)}$。公钥 $(n,e)$，私钥 $d$。

**加密**：$c\equiv m^e\pmod n$；**解密**：$m\equiv c^d\pmod n$。

**正确性**：$ed\equiv 1\pmod{\varphi(n)}$，故 $ed=1+k\varphi(n)$。由 Euler 定理 $m^{\varphi(n)}\equiv 1\pmod n$（对 $\gcd(m,n)=1$），得

$$c^d \equiv m^{ed} \equiv m^{1+k\varphi(n)} \equiv m \pmod n.$$

**安全性**：分解 $n$ 与求 $\varphi(n)$ 等价，也与求 $d$ 等价。因此 RSA 的安全性建立在大整数分解困难之上（攻击算法见 reference `discrete-log-factoring`）。

```python
def rsa_decrypt(c: int, d: int, n: int) -> int:
    """模幂：平方-乘算法，O(len(n)^3)。"""
    result = 1
    base = c % n
    while d > 0:
        if d & 1:
            result = result * base % n
        base = base * base % n
        d >>= 1
    return result
```

## 6. 心智模型

1. **扩展 Euclid 是一台三用的机器**：求 gcd、求 Bézout 系数、求模逆元，一次 `extended_gcd` 全部得到。
2. **Fibonacci 数是最坏情况的标尺**，$O(\mathrm{len}(a)\mathrm{len}(b))$ 是 gcd 的严格上界，也是全书几乎所有数论算法的基准复杂度。
3. **有理数重构把"模意义下的解"翻译回"有理数"**，是纠错码与符号计算共享的桥梁；唯一定性要求 $n>2B^2$。
4. **RSA 是理论链条的终点**：唯一分解 $\to$ Euler 定理 $\to$ 模逆元 $\to$ RSA。理解 RSA 的正确性等于掌握前两章的全部内容。
