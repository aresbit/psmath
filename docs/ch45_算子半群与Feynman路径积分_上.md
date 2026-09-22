---
layout: default
---

# 第45章: 算子半群与 Feynman 路径积分·上：预备与直觉 (Operator Semigroups and Feynman Path Integrals · Part I: Warm-up and Intuition)

> 配套深化: 见 第46章 算子半群与 Feynman 路径积分·下（完整推导），本章是它的具体铺垫，建议先读本章
> 专家依据: `_experts/analysis/functional-analysis.md`(主) + `_experts/analysis/measure-integration.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

读第46章第三节，你会在很短的篇幅里连续遇到几个"一步压好几步"的地方：三条半群公理 (S1)(S2)(S3) 紧接着就被用来定义**生成元**——一个用范数意义下的极限定义、定义域可能只是真稠密子空间的无界算子；紧接着又冒出**预解式**——半群的一个积分变换；然后 Hille–Yosida 定理把"哪些算子能生成半群"归结成预解式上的一条不等式，五步构造一气呵成；最后一节把 Trotter 乘积公式和 Feynman 路径积分接在一起，读者要同时盯住"矩阵指数不能直接相加"和"无穷维空间上没有测度"两件事。

本章要做的，是把这几步拆开、先用小尺寸的例子手算一遍：标量衰减方程给出半群最简单的原型；把标量换成对角矩阵，让"生成元 = 求导"变得可以逐分量验证；把矩阵换成一个具体的高斯核，让第46章直接引用的"生成元是 $$-d^2/dx^2$$"这句话，至少在形式层面被算出来一次；最后回到第46章入口题 (c)(d) 用过的那两个 $$2\times2$$ 矩阵，亲手验证 $$e^{A}e^{B}\ne e^{A+B}$$，数出差是什么、随参数怎么变小。做完这些，读第46章时，"由半群的强连续性""由预解恒等式""取强极限"这些短语，你会知道它们在具体地算什么。

## 二、入口：一道具体的问题 (Entry Problem)

本节给四问，数字比第46章的入口题小，只要求算出答案或验证一个等式，不要求给出一般证明。

**(a) 同一个矩阵，只算一步。** 取

$$A=\begin{pmatrix}0&1\\0&0\end{pmatrix}.$$

算出 $$A^2$$，写出 $$e^{tA}=I+tA+\dfrac{t^2A^2}{2}+\cdots$$ 的封闭形式。取 $$s=1,t=2$$，直接算出 $$e^{sA}$$、$$e^{tA}$$、$$e^{sA}e^{tA}$$ 与 $$e^{(s+t)A}$$ 这四个矩阵的具体数值，验证 $$e^{sA}e^{tA}=e^{(s+t)A}$$ 是否成立。

**(b) 标量的情形。** 取常微分方程 $$x'(t)=-3x(t)$$，解是 $$x(t)=e^{-3t}x(0)$$。取 $$s=1,t=2$$，算出 $$e^{-3\cdot1}\cdot e^{-3\cdot2}$$ 与 $$e^{-3\cdot3}$$，它们相等吗？再问：$$t\to-\infty$$ 时 $$e^{-3t}$$ 怎么样？这告诉你"倒着解"这个方程会遇到什么问题。

**(c) 两个矩阵，乘积对不对。** 取

$$A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$$

（与 (a) 同一个 $$A$$）。分别算出 $$e^{A}=I+A$$、$$e^{B}=I+B$$、$$e^{A}e^{B}$$ 这三个矩阵的具体数值；再算出 $$A+B$$，注意到 $$(A+B)^2=I$$，用这条关系把 $$e^{A+B}$$ 的级数求和成封闭形式，算出具体数值。比较 $$e^{A}e^{B}$$ 与 $$e^{A+B}$$：相等吗？差是什么？

**(d) 高斯核卷起来。** 取 $$G_t(x)=\dfrac{1}{\sqrt{4\pi t}}e^{-x^2/4t}$$。取 $$s=t=1$$，算出

$$(G_1*G_1)(x)=\int_{\mathbb R}G_1(x-y)G_1(y)\,dy,$$

并验证它等于 $$G_2(x)$$。（提示：两个方差为 $$2$$ 的正态分布之和，方差是 $$4$$，对应 $$G_2$$ 里 $$4\pi\cdot2=8\pi$$ 的归一化——先把两个高斯的指数部分配方，凑出一个新的高斯乘一个与 $$y$$ 无关的常数，再对 $$y$$ 积分。）

本章会让你在算完这四问之后，直接拿到第46章开头就要用的三个事实：**半群律不是凭空规定，它就是"解在时间上可以先走一段再走一段"这件事的代数写法；两个不对易的矩阵，乘积和"和的指数"是两回事，差恰好由对易子决定；高斯核的卷积律，就是"热半群"这个名字的来源。**

## 三、结构：定义与完整推导 (Structure & Proof)

本节分四段，依次对应第46章 3.1 节（半群公理）、3.2 节（生成元）、3.3 节（预解式）、3.6 节（Trotter 乘积公式）这几处压缩最狠的地方：每段先用入口题里出现过的具体对象手算，再抽象成一般定义或命题。

### 3.1 半群：从"先走一段再走一段"到公理

入口题 (b) 里，方程 $$x'(t)=-3x(t)$$ 的解是 $$x(t)=e^{-3t}x(0)$$。把它写成算子的样子：令 $$T(t)x_0=e^{-3t}x_0$$，这是（一维空间 $$\mathbb R$$ 上）一族映射，下标 $$t\ge0$$。三件事直接算：

$$T(0)x_0=e^{0}x_0=x_0,$$

即 $$T(0)=\mathrm{id}$$；再算

$$T(s)\bigl(T(t)x_0\bigr)=e^{-3s}\bigl(e^{-3t}x_0\bigr)=e^{-3(s+t)}x_0=T(s+t)x_0,$$

这就是指数律 $$e^{a}e^{b}=e^{a+b}$$——**半群律不是新东西，它就是这条指数律换了个写法**；连续性是初等函数 $$t\mapsto e^{-3t}x_0$$ 的连续性，显然成立。

入口题 (a) 的矩阵给出一个真正"算子"的例子。因为 $$A^2=0$$，级数在第二项截断：$$e^{tA}=I+tA$$。取 $$s=1,t=2$$：

$$e^{sA}=I+A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
e^{tA}=I+2A=\begin{pmatrix}1&2\\0&1\end{pmatrix},$$

$$e^{sA}e^{tA}=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&2\\0&1\end{pmatrix}=\begin{pmatrix}1&3\\0&1\end{pmatrix},
\qquad e^{(s+t)A}=I+3A=\begin{pmatrix}1&3\\0&1\end{pmatrix}.$$

两边相等。一般地，对任意 $$s,t$$，

$$(I+sA)(I+tA)=I+(s+t)A+stA^2=I+(s+t)A$$

（最后一步用了 $$A^2=0$$）——**半群律在这里就是"把矩阵乘出来、用 $$A^2=0$$ 消掉多余项"这件具体的代数运算**。

这两个例子里，$$\lVert T(t)\rVert$$ 的行为不一样：标量例子里 $$\lvert T(t)\rvert=e^{-3t}\to0$$，矩阵例子里 $$\lVert e^{tA}\rVert\to\infty$$——取单位向量 $$x=(0,1)^{\mathsf T}$$，$$e^{tA}x=(t,1)^{\mathsf T}$$，故 $$\lVert e^{tA}\rVert\ge\lVert e^{tA}x\rVert=\sqrt{1+t^2}\to\infty$$（这只是一个下界，不是等号；一般的增长上界见第46章 定理 3.1）。这提示我们：半群不必是压缩的，但范数增长必须有个上界——不能突然炸到无穷。

把这两个例子共有的三条性质抽出来：

**定义 3.1（强连续半群, strongly continuous semigroup）**。设 $$X$$ 是 Banach 空间，$$\{T(t)\}_{t\ge0}\subset\mathcal B(X)$$ 是一族有界线性算子，满足

- **(S1)** $$T(0)=I$$；
- **(S2)** $$T(s+t)=T(s)T(t)$$（$$s,t\ge0$$）；
- **(S3)** 对每个 $$x\in X$$，$$t\mapsto T(t)x$$ 连续。

则称它为**强连续半群**。第46章 定义 3.1 一字不差地写着同一件事——它只是把上面两个具体例子里"代入数字验证"的部分，换成了对任意 Banach 空间成立的公理。

**例 3.1**。入口题 (b) 验证的是 $$X=\mathbb R$$、$$T(t)=e^{-3t}$$ 的情形；入口题 (a) 验证的是 $$X=\mathbb R^2$$、$$T(t)=I+tA$$ 的情形。两个例子里 (S1)(S2) 都是初等代数，(S3) 都是初等函数的连续性——第46章处理热半群、酉群这些无穷维例子时，(S3) 才真正成为需要专门论证的一条（第46章 命题 3.1 给出了一条简化验证的办法：只需在 $$t=0$$ 处验证）。

### 3.2 生成元：从差商到定义域

半群描述"演化"；要驱动这个演化的是哪个算子？办法是对 $$t$$ 求导，在 $$t=0$$ 处看差商。

入口题 (b) 的标量例子：

$$\frac{T(t)x_0-x_0}{t}=\frac{e^{-3t}-1}{t}x_0 .$$

用 $$e^{-3t}=1-3t+O(t^2)$$（Taylor 展开）代入，$$\dfrac{e^{-3t}-1}{t}=-3+O(t)\to-3$$（$$t\to0$$）。差商的极限是 $$-3$$——**正是原方程 $$x'=-3x$$ 里的那个系数**：半群"记得"驱动它的方程，生成元就是把这件事反过来读出来。

矩阵例子更干脆：$$T(t)=I+tA$$ 对每个 $$t\ne0$$ 都精确给出

$$\frac{T(t)x-x}{t}=\frac{(I+tA)x-x}{t}=Ax ,$$

不需要取极限就已经是 $$Ax$$（因为 $$A^2=0$$ 截断了级数）。这个例子特别干净地说明：**生成元不是某种神秘的新对象，它就是半群在 $$t=0$$ 处的"瞬时变化率"**，只不过一般情形要取真正的极限，且极限未必对每个 $$x$$ 都存在。

**定义 3.2（无穷小生成元, infinitesimal generator）**。设 $$\{T(t)\}_{t\ge0}$$ 是强连续半群。令

$$D(A)=\Bigl\{x\in X:\ \lim_{t\to0^{+}}\frac{T(t)x-x}{t}\ \text{在}\ X\ \text{中存在}\Bigr\},\qquad
Ax=\lim_{t\to0^{+}}\frac{T(t)x-x}{t}\ \ (x\in D(A)).$$

**例 3.2**。上面两个例子里 $$D(A)=X$$（全空间）——因为 $$A$$ 有界。这不是一般情形：第46章的热半群例子里，生成元的定义域是 $$H^2(\mathbb R)$$，是 $$L^2(\mathbb R)$$ 的真稠密子空间，"无界"正是从这里冒出来的。下面用一个形式计算，先在具体函数上把这件事算出来。

**例 3.3（热核的生成元：形式计算）**。设 $$f$$ 光滑、紧支集，$$T(t)f(x)=\displaystyle\int_{\mathbb R}G_t(x-y)f(y)\,dy$$，$$G_t(z)=\dfrac{1}{\sqrt{4\pi t}}e^{-z^2/4t}$$（入口题 (d) 的核）。换元 $$z=x-y$$：

$$T(t)f(x)=\int_{\mathbb R}G_t(z)f(x-z)\,dz .$$

把 $$f(x-z)$$ 在 $$z=0$$ 处 Taylor 展开：$$f(x-z)=f(x)-zf'(x)+\dfrac{z^2}{2}f''(x)+O(z^3)$$。$$G_t$$ 是均值 $$0$$、方差 $$2t$$ 的正态密度（把 $$G_t$$ 写成 $$N(0,2t)$$ 的标准形式 $$\frac{1}{\sqrt{2\pi\cdot2t}}e^{-z^2/(2\cdot2t)}$$ 即可核对 $$4t=2\cdot2t$$），故

$$\int_{\mathbb R}G_t(z)\,dz=1,\qquad \int_{\mathbb R}zG_t(z)\,dz=0,\qquad \int_{\mathbb R}z^2G_t(z)\,dz=2t$$

（第一条是归一化；第二条由被积函数是奇函数；第三条是正态分布方差的定义）。逐项积分（$$O(z^3)$$ 项因为对称性贡献为 $$0$$，$$O(z^4)$$ 项的矩是 $$O(t^2)$$，比留下的项高阶）：

$$T(t)f(x)=f(x)\cdot1-f'(x)\cdot0+\frac{f''(x)}{2}\cdot2t+O(t^2)=f(x)+t\,f''(x)+O(t^2).$$

于是

$$\frac{T(t)f(x)-f(x)}{t}=f''(x)+O(t)\ \xrightarrow[t\to0^{+}]{}\ f''(x).$$

这就（形式地）算出了热半群 $$T(t)=e^{-tH_0}$$（$$H_0=-d^2/dx^2$$）的生成元是 $$\Delta=d^2/dx^2=-H_0$$——负号翻过来是因为半群里带着 $$e^{-tH_0}$$ 的负号。第46章把这个形式计算严格化：定义域从"光滑紧支集函数"换成 $$H^2(\mathbb R)$$，"Taylor 展开＋逐项积分"换成范数意义下的极限（第46章 定理 3.2 给出一般理论）。

### 3.3 预解式：从一个具体的拉普拉斯变换开始

如果把差商的极限 $$Ax=\lim(T(t)x-x)/t$$ 想成 "$$T(t)=e^{tA}$$"，那反过来，对 $$e^{tA}$$ 做拉普拉斯变换应该能读出 $$A$$ 的信息。先在标量例子上算一次。

入口题 (b) 的标量半群 $$T(t)=e^{-3t}$$，生成元 $$A=-3$$。取 $$\lambda=2$$，算

$$\int_0^{\infty}e^{-\lambda t}T(t)\,dt=\int_0^{\infty}e^{-2t}e^{-3t}\,dt=\int_0^{\infty}e^{-5t}\,dt=\frac15 .$$

另一方面，$$(\lambda-A)^{-1}=(2-(-3))^{-1}=\dfrac15$$——两个数完全相同。这不是巧合：$$\displaystyle\int_0^\infty e^{-\lambda t}e^{-at}\,dt=\dfrac{1}{\lambda+a}$$ 对 $$\lambda>-a$$ 恒成立，而 $$\lambda+a=\lambda-A$$（$$A=-a$$）正是 $$(\lambda-A)$$。

**定义 3.3（预解集与预解式, resolvent set and resolvent）**。设 $$A$$ 是闭稠定线性算子，$$\rho(A)=\{\lambda\in\mathbb C:\lambda I-A\text{ 是双射}\}$$ 为**预解集**，$$R(\lambda,A)=(\lambda I-A)^{-1}$$ 为 $$A$$ 在 $$\lambda$$ 处的**预解式**。

**例 3.4**。取 $$2\times2$$ 对角矩阵 $$A=\operatorname{diag}(-2,-3)$$（描述两个互不干扰的标量衰减方程），$$T(t)=e^{tA}=\operatorname{diag}(e^{-2t},e^{-3t})$$。逐分量重复上面的计算：

$$R(\lambda,A)=\int_0^\infty e^{-\lambda t}T(t)\,dt=\operatorname{diag}\Bigl(\frac1{\lambda+2},\,\frac1{\lambda+3}\Bigr),\qquad\lambda>-2 .$$

这与直接求逆 $$(\lambda I-A)^{-1}=\operatorname{diag}\bigl((\lambda+2)^{-1},(\lambda+3)^{-1}\bigr)$$ 逐分量吻合。**预解式是半群的"频域像"**：第46章 定理 3.3 把这条逐分量成立的等式，一般化到任意 Banach 空间上的强连续半群，证明的骨架和这里的计算完全一样——只是把标量积分换成 Bochner 积分，把"逐分量"换成"对每个 $$x\in X$$"。

### 3.4 Trotter 乘积公式：亲手算一次对易子

回到入口题 (c)：$$A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$$、$$B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$$，已经算出

$$e^{A}e^{B}=(I+A)(I+B)=I+A+B+AB=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
e^{A+B}=\begin{pmatrix}\cosh1&\sinh1\\ \sinh1&\cosh1\end{pmatrix}\approx\begin{pmatrix}1.543&1.175\\1.175&1.543\end{pmatrix}$$

（$$AB=\begin{pmatrix}1&0\\0&0\end{pmatrix}$$ 直接乘出来；$$e^{A+B}$$ 用 $$(A+B)^2=I$$ 把级数求和成 $$\cosh(1)I+\sinh(1)(A+B)$$，见入口题 (c) 的提示）。两者不相等，差是

$$e^{A}e^{B}-e^{A+B}=\begin{pmatrix}2-1.543&1-1.175\\1-1.175&1-1.543\end{pmatrix}\approx\begin{pmatrix}0.457&-0.175\\-0.175&-0.457\end{pmatrix}\ne0.$$

问题是：这个差能不能通过"先除以 $$m$$ 再取 $$m$$ 次方"变小？取 $$m=2$$：因为 $$(A/2)^2=(B/2)^2=0$$，$$e^{A/2}=I+A/2$$、$$e^{B/2}=I+B/2$$ 仍然精确，

$$X_2:=e^{A/2}e^{B/2}=I+\frac{A+B}{2}+\frac{AB}{4}=\begin{pmatrix}1.25&0.5\\0.5&1\end{pmatrix},$$

$$X_2^2=\begin{pmatrix}1.25&0.5\\0.5&1\end{pmatrix}\begin{pmatrix}1.25&0.5\\0.5&1\end{pmatrix}=\begin{pmatrix}1.8125&1.125\\1.125&1.25\end{pmatrix}.$$

与 $$e^{A+B}\approx\begin{pmatrix}1.543&1.175\\1.175&1.543\end{pmatrix}$$ 比较，差的最大分量从 $$m=1$$ 时的约 $$0.46$$ 缩小到 $$m=2$$ 时的约 $$0.29$$——变小了，量级上与"误差按 $$1/m$$ 衰减"的猜测不矛盾（$$m=1\to2$$ 时还带着不小的高阶项，看不出精确的减半；第46章 定理 3.7 给出严格的误差界 $$O(1/m)$$ 并证明极限确实是 $$e^{A+B}$$，第46章 经典问题 5.3 用 $$m=100$$ 做了更精细的数值核对，误差已经很接近 $$O(1/m)$$ 的理论值）。

这两次计算里，$$e^{\varepsilon A}e^{\varepsilon B}$$ 与 $$e^{\varepsilon(A+B)}$$ 的差从哪里来？取一般的 $$\varepsilon$$（上面 $$m=1$$ 用了 $$\varepsilon=1$$，$$m=2$$ 用了 $$\varepsilon=\frac12$$）。因为 $$A^2=B^2=0$$，$$e^{\varepsilon A}=I+\varepsilon A$$、$$e^{\varepsilon B}=I+\varepsilon B$$ 对任意 $$\varepsilon$$ 都精确成立（不是近似），故

$$e^{\varepsilon A}e^{\varepsilon B}=I+\varepsilon(A+B)+\varepsilon^2AB .$$

另一边，因为 $$(A+B)^2=I$$，$$e^{\varepsilon(A+B)}$$ 的级数可以精确求和成 $$\cosh(\varepsilon)I+\sinh(\varepsilon)(A+B)$$（与入口题 (c) 处理 $$e^{A+B}$$ 是同一个技巧）。用 $$\cosh\varepsilon=1+\dfrac{\varepsilon^2}2+O(\varepsilon^4)$$、$$\sinh\varepsilon=\varepsilon+O(\varepsilon^3)$$，两式相减：

$$e^{\varepsilon A}e^{\varepsilon B}-e^{\varepsilon(A+B)}=\Bigl(1-\cosh\varepsilon\Bigr)I+\bigl(\varepsilon-\sinh\varepsilon\bigr)(A+B)+\varepsilon^2AB
=\varepsilon^2\Bigl(AB-\frac{I}{2}\Bigr)+O(\varepsilon^3)$$

（$$1-\cosh\varepsilon=-\varepsilon^2/2+O(\varepsilon^4)$$ 给出 $$-\varepsilon^2I/2$$；$$\varepsilon-\sinh\varepsilon=O(\varepsilon^3)$$ 吸收进余项）。代入 $$AB=\begin{pmatrix}1&0\\0&0\end{pmatrix}$$ 与 $$[A,B]=AB-BA=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$$（$$BA$$ 直接乘出来是 $$\begin{pmatrix}0&0\\0&1\end{pmatrix}$$），

$$AB-\frac{I}{2}=\begin{pmatrix}\frac12&0\\0&-\frac12\end{pmatrix}=\frac{[A,B]}{2},$$

即

$$e^{\varepsilon A}e^{\varepsilon B}-e^{\varepsilon(A+B)}=\frac{\varepsilon^2}{2}[A,B]+O(\varepsilon^3).$$

**对易子 $$[A,B]=AB-BA$$ 第一次在这里现身：它精确地度量"先做 $$A$$ 再做 $$B$$"和"$$A,B$$ 同时做"这两件事的二阶差别。** 取 $$\varepsilon=\frac1m$$ 代入上式，正是第46章 (3.5) 式；上面 $$m=1,2$$ 的数值计算是这条一般公式在 $$\varepsilon=1,\frac12$$ 处的具体取值，第46章 定理 3.7 的证明就是把这里的代数搬到一般的（不假设 $$A^2=B^2=0$$ 的）矩阵上，再加上 $$m$$ 次幂的误差累积估计。

**命题 3.4（Trotter 公式的具体版本）**。对上面的 $$A,B$$，数值计算显示 $$\bigl(e^{A/m}e^{B/m}\bigr)^m$$ 随 $$m$$ 增大而逼近 $$e^{A+B}$$，误差量级是 $$1/m$$。一般地，对任意方阵 $$A,B$$（不必可换），都有

$$\lim_{m\to\infty}\Bigl(e^{A/m}e^{B/m}\Bigr)^{m}=e^{A+B},$$

误差的主项由 $$[A,B]$$ 控制。这是第46章 定理 3.7（Lie 乘积公式）的内容，那里给出完整证明；本节只做了两次具体的数值验证——它已经足够让你猜出结论、也足够让你在读证明时知道每一步"展开到二阶、相减、取 $$m$$ 次幂"在具体地算什么。

## 四、几何与物理直觉 (Intuition)

**一、半群是"只能顺着看的录像"。** 一滴墨水滴进水里，过程只能正着放：录像倒放会看到墨水自己聚成一滴，这在现实里不会发生。热半群 $$e^{-tH_0}$$ 正是这样——它把"扩散"这件不可逆的事翻译成了算子，$$t<0$$ 没有意义。相反，平移酉群 $$f(x)\mapsto f(x+t)$$ 像放一段没有信息丢失的动画：正放、倒放都合理，$$t$$ 可正可负。半群与群的区别，就是"墨水扩散"与"传送带平移"的区别。

**二、生成元是出发时刻的瞬时速度。** 一辆车在时刻 $$t$$ 的位置是 $$T(t)x_0$$；生成元 $$A$$ 就是 $$t=0$$ 那一刻的速度表读数 $$Ax_0=\lim_{t\to0^+}(T(t)x_0-x_0)/t$$。如果规则不随时间变化（这正是半群律 $$T(s+t)=T(s)T(t)$$ 的含义——"从任意时刻出发，接下来怎么走只取决于当前位置，不取决于已经走了多久"），那么知道出发时刻的速度表读数，原则上就该能重建整条轨迹——这正是"指数映射" $$A\mapsto e^{tA}$$ 要做的事。

**三、预解式是"未来收益的现值"。** 把 $$T(t)x$$ 想成第 $$t$$ 年能拿到的一笔钱，$$\lambda$$ 是贴现率。$$R(\lambda,A)x=\int_0^\infty e^{-\lambda t}T(t)x\,dt$$ 就是这整条未来收益流按 $$\lambda$$ 贴现后的现值——它把"每一年拿多少"这条完整的时间序列，压缩成了一个只依赖 $$\lambda$$ 的数（或向量）。第三节入口题的标量算例 $$1/(\lambda+3)$$，就是"每年衰减到 $$e^{-3t}$$ 倍的一笔钱，用贴现率 $$2$$ 算出来的现值"。

**四、不对易就是"先转弯还是先前进"。** 机器人先向右转 $$90°$$ 再往前走一步，和先往前走一步再向右转 $$90°$$，落地的位置不一样——这就是"操作顺序影响结果"最直观的样子。$$e^{A}e^{B}\ne e^{A+B}$$ 讲的是同一件事：先做 $$A$$ 再做 $$B$$，和把 $$A,B$$"同时做"，是两种不同的操作，差多少由对易子 $$[A,B]$$ 定出。第五节的路径积分正是把"许多次微小的转弯与前进交替"连成一条折线——折线足够密时，先后顺序的差别趋于零，折线本身趋于一条光滑的路径，这就是第46章 Trotter 公式与路径积分的几何雏形。

## 五、经典问题精讲 (Classical Problems)

### 经典问题 5.1（对角矩阵：半群、生成元、预解式一次算全）

设 $$A=\operatorname{diag}(-2,-3)$$、$$T(t)=e^{tA}$$。**(a)** 直接验证 $$T(1)T(1)=T(2)$$。**(b)** 用差商算出生成元就是 $$A$$ 本身。**(c)** 验证 $$(\lambda I-A)R(\lambda,A)=I$$（$$\lambda>-2$$）。

**解**：**(a)** $$T(t)=\operatorname{diag}(e^{-2t},e^{-3t})$$，故 $$T(1)=\operatorname{diag}(e^{-2},e^{-3})$$，

$$T(1)T(1)=\operatorname{diag}(e^{-2}\cdot e^{-2},\,e^{-3}\cdot e^{-3})=\operatorname{diag}(e^{-4},e^{-6})=T(2).$$

**(b)** 逐分量算差商：

$$\frac{T(t)x-x}{t}=\Bigl(\frac{e^{-2t}-1}{t}x_1,\ \frac{e^{-3t}-1}{t}x_2\Bigr)\ \xrightarrow[t\to0^{+}]{}\ (-2x_1,-3x_2)=Ax$$

（每个分量都是标量指数函数在 $$0$$ 处的导数，即例 3.2 的计算逐分量重复一次）。

**(c)** 由例 3.4，$$R(\lambda,A)=\operatorname{diag}\bigl((\lambda+2)^{-1},(\lambda+3)^{-1}\bigr)$$，故

$$(\lambda I-A)R(\lambda,A)=\operatorname{diag}\bigl((\lambda+2)(\lambda+2)^{-1},\,(\lambda+3)(\lambda+3)^{-1}\bigr)=\operatorname{diag}(1,1)=I. \qquad\blacksquare$$

### 经典问题 5.2（入口题 (d) 的完整解答：高斯核卷积）

证明 $$G_1*G_1=G_2$$，其中 $$G_t(x)=\dfrac{1}{\sqrt{4\pi t}}e^{-x^2/4t}$$。

**解**：按定义，

$$(G_1*G_1)(x)=\int_{\mathbb R}G_1(x-y)G_1(y)\,dy=\frac1{4\pi}\int_{\mathbb R}\exp\Bigl(-\frac{(x-y)^2}{4}-\frac{y^2}{4}\Bigr)dy .$$

先把指数上的 $$y$$ 二次式配方。展开 $$(x-y)^2+y^2=x^2-2xy+2y^2$$，故指数是 $$-\dfrac{1}{4}(2y^2-2xy+x^2)=-\dfrac12\bigl(y^2-xy\bigr)-\dfrac{x^2}4$$。对 $$y^2-xy$$ 配方：$$y^2-xy=\bigl(y-\frac x2\bigr)^2-\dfrac{x^2}4$$。代回：

$$-\frac12\Bigl[\bigl(y-\tfrac x2\bigr)^2-\frac{x^2}4\Bigr]-\frac{x^2}4=-\frac12\bigl(y-\tfrac x2\bigr)^2+\frac{x^2}8-\frac{x^2}4=-\frac12\bigl(y-\tfrac x2\bigr)^2-\frac{x^2}8 .$$

于是

$$(G_1*G_1)(x)=\frac1{4\pi}e^{-x^2/8}\int_{\mathbb R}e^{-\frac12(y-x/2)^2}\,dy=\frac1{4\pi}e^{-x^2/8}\sqrt{2\pi}$$

（换元 $$u=y-x/2$$ 后是标准高斯积分 $$\int e^{-u^2/2}du=\sqrt{2\pi}$$）。系数化简：$$\dfrac{\sqrt{2\pi}}{4\pi}$$，平方后是 $$\dfrac{2\pi}{16\pi^2}=\dfrac1{8\pi}$$，故 $$\dfrac{\sqrt{2\pi}}{4\pi}=\dfrac1{\sqrt{8\pi}}$$。所以

$$(G_1*G_1)(x)=\frac{1}{\sqrt{8\pi}}e^{-x^2/8}=\frac1{\sqrt{4\pi\cdot2}}e^{-x^2/(4\cdot2)}=G_2(x). \qquad\blacksquare$$

这正是热半群律 $$T(1)T(1)=T(2)$$ 在卷积算子上的具体样子——与经典问题 5.1(a) 是同一件事的两个版本，一个逐分量乘，一个逐点卷积。

### 经典问题 5.3（离散"作用量"与经典路径）

一个自由粒子（$$m=1$$），从 $$x_0=0$$ 出发，$$t=2$$ 时到达 $$x_2=2$$，中途只留一个可调节点 $$x_1$$（对应 $$N=2$$，步长 $$\varepsilon=1$$）。第46章 (3.8) 式定义的离散作用量在无势能（$$V=0$$）、$$N=2$$ 时是

$$S_2(x_1)=\varepsilon\cdot\frac{(x_1-x_0)^2}{2\varepsilon^2}+\varepsilon\cdot\frac{(x_2-x_1)^2}{2\varepsilon^2}=\frac{x_1^2+(2-x_1)^2}{2}$$

（代入 $$\varepsilon=1,x_0=0,x_2=2$$）。**(a)** 求使 $$S_2(x_1)$$ 最小的 $$x_1$$，并算出最小值。**(b)** 把这个最小值与连续情形的作用量 $$S=\int_0^2\frac12\dot x(s)^2\,ds$$（对匀速直线运动 $$x(s)=s$$）比较。

**解**：**(a)** $$S_2(x_1)=\dfrac{x_1^2+(2-x_1)^2}2$$ 是 $$x_1$$ 的二次函数，求导：

$$\frac{d}{dx_1}S_2(x_1)=\frac{2x_1-2(2-x_1)}2=2x_1-2 .$$

令其为零：$$x_1=1$$。代回：$$S_2(1)=\dfrac{1^2+1^2}2=1$$。

**(b)** 使 $$S_2$$ 最小的折线是 $$0\to1\to2$$，也就是匀速直线运动 $$x(s)=s$$（$$s\in[0,2]$$，速度恒为 $$1$$）。连续情形的作用量：

$$S=\int_0^2\frac12\cdot1^2\,ds=\frac12\cdot2=1,$$

与 (a) 算出的离散最小值恰好相等。**这不是巧合**：离散作用量 $$S_N$$ 是沿折线速度平方的黎曼和（第三节结构里已经说明），折线是直线时每一段速度都相同，黎曼和退化成"速度平方乘以总时长的一半"，与连续积分完全重合；折线不是直线时，$$S_2(x_1)>S_2(1)=1$$（因为二次函数在顶点外严格更大），对应的物理图像是"偏离匀速直线运动要多耗费作用量"。第46章 3.7 节会说明：量子力学的相位是 $$e^{iS/\hbar}$$，$$\hbar\to0$$ 时偏离最小作用量路径的相位振荡得极快、彼此抵消，只有让 $$S$$ 取极值的路径（这里就是这条直线）贡献才不被抵消——这就是"经典轨道是量子路径积分的驻定相位点"这句话背后最基础的算例。

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 设 $$T(t)=e^{-5t}$$（$$\mathbb R$$ 上的标量半群）。验证 $$T(2)T(3)=T(5)$$，并求它的生成元。

**基2.** 设 $$A=\operatorname{diag}(1,-1)$$，$$T(t)=e^{tA}=\operatorname{diag}(e^{t},e^{-t})$$。求 $$\lVert T(t)\rVert$$（提示：算子范数是各分量绝对值的最大者），并说明为什么这不是压缩半群。

**基3.** 设 $$A=-4$$（标量）。用定义直接算出 $$R(\lambda,A)=\displaystyle\int_0^\infty e^{-\lambda t}e^{-4t}\,dt$$（$$\lambda>-4$$），并验证 $$(\lambda-A)R(\lambda,A)=1$$。

### 竞赛（本课目标难度）

**竞1.** 用 3.4 节推出的精确公式 $$e^{\varepsilon A}e^{\varepsilon B}-e^{\varepsilon(A+B)}=(1-\cosh\varepsilon)I+(\varepsilon-\sinh\varepsilon)(A+B)+\varepsilon^2AB$$（$$A,B$$ 是入口题 (c) 的矩阵），取 $$\varepsilon=\dfrac13$$，算出左边的精确值，并与近似值 $$\dfrac{\varepsilon^2}2[A,B]$$ 比较，求两者之差的最大分量。

**竞2.** 设 $$A=\operatorname{diag}(-1,2)$$。写出 $$T(t)=e^{tA}$$ 的显式表达式，算出 $$\lVert T(t)\rVert$$ 关于 $$t\ge0$$ 的表达式，并求出使 $$\lVert T(t)\rVert\le e^{\omega t}$$ 对一切 $$t\ge0$$ 成立的最小 $$\omega$$。

**竞3.** 设 $$T_1(t)=e^{-2t}$$、$$T_2(t)=e^{-5t}$$ 是 $$\mathbb R$$ 上两个标量半群，$$T(t):=T_1(t)T_2(t)$$（逐点乘积）。验证 $$\{T(t)\}$$ 也是强连续半群，求它的生成元，并验证这个生成元恰好等于 $$T_1,T_2$$ 两个生成元之和。

### 研究（通向下一章）

**研1.**（Yosida 逼近的最简版本）设 $$A=\operatorname{diag}(-2,-3)$$。对 $$\lambda>0$$ 算出 $$\lambda R(\lambda,A)$$ 的显式表达式，验证 $$\lVert\lambda R(\lambda,A)\rVert\le1$$，并说明当 $$\lambda\to\infty$$ 时 $$\lambda R(\lambda,A)\to I$$（逐分量收敛）。这个 $$\lambda R(\lambda,A)$$ 正是下一章 Hille–Yosida 定理证明里 $$A_\lambda=\lambda AR(\lambda,A)$$ 的"表亲"。

**研2.**（三段折线的驻定路径）把经典问题 5.3 的设置换成 $$N=3$$：自由粒子从 $$x_0=0$$ 出发，$$t=3$$ 时到达 $$x_3=3$$，步长 $$\varepsilon=1$$，中间两个可调节点是 $$x_1,x_2$$。离散作用量是

$$S_3(x_1,x_2)=\frac{(x_1-x_0)^2}{2}+\frac{(x_2-x_1)^2}{2}+\frac{(x_3-x_2)^2}{2}.$$

求使 $$S_3$$ 最小的 $$(x_1,x_2)$$，算出最小值，并与连续情形的作用量比较。

### 解答 (Solutions)

**解 基1.** $$T(2)T(3)=e^{-10}\cdot e^{-15}=e^{-25}=e^{-5\cdot5}=T(5)$$，半群律成立。生成元：$$\dfrac{T(t)-1}{t}=\dfrac{e^{-5t}-1}{t}\to-5$$（$$t\to0^{+}$$，同例 3.2 的算法），故生成元是 $$-5$$。

**解 基2.** $$T(t)=\operatorname{diag}(e^t,e^{-t})$$ 作用在 $$x=(x_1,x_2)$$ 上给出 $$(e^tx_1,e^{-t}x_2)$$，算子范数是使 $$\lVert T(t)x\rVert\le c\lVert x\rVert$$ 成立的最小 $$c$$，对角算子的这个 $$c$$ 就是对角元绝对值的最大者：

$$\lVert T(t)\rVert=\max(e^t,e^{-t})=e^t\qquad(t\ge0).$$

因为 $$e^t>1$$（$$t>0$$ 时），$$\lVert T(t)\rVert>1$$，不满足压缩半群 $$\lVert T(t)\rVert\le1$$ 的要求——**沿第一个分量的方向，$$T(t)$$ 把向量拉长而不是缩短**，这正是 $$A$$ 在这个方向上的对角元 $$+1>0$$（而不是 $$\le0$$）的直接后果。$$\blacksquare$$

**解 基3.** $$\displaystyle\int_0^\infty e^{-\lambda t}e^{-4t}dt=\int_0^\infty e^{-(\lambda+4)t}dt=\dfrac1{\lambda+4}$$（$$\lambda+4>0$$ 时收敛，即 $$\lambda>-4$$）。验证：$$(\lambda-A)R(\lambda,A)=(\lambda+4)\cdot\dfrac1{\lambda+4}=1$$。$$\blacksquare$$

**解 竞1.** 先算精确值。用 $$\cosh x=\dfrac{e^x+e^{-x}}2$$、$$\sinh x=\dfrac{e^x-e^{-x}}2$$ 与 $$e^{1/3}\approx1.395612$$（即 $$e$$ 的立方根）算出

$$\cosh\tfrac13\approx1.056072,\qquad\sinh\tfrac13\approx0.339541 .$$

$$(A+B)=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$，$$AB=\begin{pmatrix}1&0\\0&0\end{pmatrix}$$，$$\varepsilon=\frac13$$。逐项代入 $$(1-\cosh\varepsilon)I+(\varepsilon-\sinh\varepsilon)(A+B)+\varepsilon^2AB$$：

$$1-\cosh\tfrac13\approx-0.056072,\qquad \tfrac13-\sinh\tfrac13\approx-0.006208,\qquad \varepsilon^2=\tfrac19\approx0.111111 .$$

代入矩阵形式：

$$\text{精确差}\approx\begin{pmatrix}-0.056072+0.111111&-0.006208\\-0.006208&-0.056072\end{pmatrix}=\begin{pmatrix}0.055039&-0.006208\\-0.006208&-0.056072\end{pmatrix}.$$

近似值 $$\dfrac{\varepsilon^2}2[A,B]=\dfrac{1}{18}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\approx\begin{pmatrix}0.055556&0\\0&-0.055556\end{pmatrix}$$。两者之差（精确减近似）：

$$\begin{pmatrix}0.055039-0.055556&-0.006208-0\\-0.006208-0&-0.056072+0.055556\end{pmatrix}\approx\begin{pmatrix}-0.000517&-0.006208\\-0.006208&-0.000516\end{pmatrix},$$

最大分量约 $$0.0062$$，量级是 $$\varepsilon^3=\frac1{27}\approx0.037$$ 的几分之一——与"余项是 $$O(\varepsilon^3)$$"吻合。$$\blacksquare$$

**解 竞2.** $$T(t)=\operatorname{diag}(e^{-t},e^{2t})$$，故 $$\lVert T(t)\rVert=\max(e^{-t},e^{2t})=e^{2t}$$（$$t\ge0$$ 时 $$2t\ge-t$$）。要 $$e^{2t}\le e^{\omega t}$$ 对一切 $$t\ge0$$ 成立，需要 $$2\le\omega$$，取等号即最小的 $$\omega=2$$——**恰好是 $$A$$ 里较大的那个对角元**：一般地，对角矩阵生成元的最优增长指数 $$\omega$$ 就是对角元的最大值（这是第46章 定理 3.1 的界 $$\lVert T(t)\rVert\le Me^{\omega t}$$ 在对角情形取到等号的例子，$$M=1$$）。$$\blacksquare$$

**解 竞3.** $$T(t)=e^{-2t}e^{-5t}=e^{-7t}$$，这仍是标量指数半群（半群律、连续性同 基1 的验证），生成元是 $$-7$$（同例 3.2 的算法：$$(e^{-7t}-1)/t\to-7$$）。而 $$T_1,T_2$$ 的生成元分别是 $$-2,-5$$，和恰好是 $$-2+(-5)=-7$$。**这在标量（可交换）情形里成立，是因为标量乘法可交换**：$$e^{-2t}e^{-5t}=e^{-(2+5)t}$$ 这条指数律本身就不需要 Trotter 公式。第46章要处理的 $$H_0,V$$ 是不可交换的算子，$$e^{-tH_0}e^{-tV}\ne e^{-t(H_0+V)}$$，"生成元相加"这件事只能通过 $$m\to\infty$$ 的极限（Trotter 公式）间接成立——**这正是本章 3.4 节要为下一章做的铺垫：可交换时"加法即乘积"是免费的，不可交换时要花一个极限去换。**$$\blacksquare$$

**解 研1.** $$R(\lambda,A)=\operatorname{diag}\bigl((\lambda+2)^{-1},(\lambda+3)^{-1}\bigr)$$（同例 3.4），故

$$\lambda R(\lambda,A)=\operatorname{diag}\Bigl(\frac{\lambda}{\lambda+2},\frac{\lambda}{\lambda+3}\Bigr).$$

每个分量都 $$<1$$（$$\lambda>0$$ 时分子小于分母），故 $$\lVert\lambda R(\lambda,A)\rVert=\max\bigl(\frac{\lambda}{\lambda+2},\frac{\lambda}{\lambda+3}\bigr)=\frac{\lambda}{\lambda+2}<1$$。当 $$\lambda\to\infty$$ 时，$$\frac{\lambda}{\lambda+2}\to1$$、$$\frac{\lambda}{\lambda+3}\to1$$，逐分量趋于 $$1$$，即 $$\lambda R(\lambda,A)\to\operatorname{diag}(1,1)=I$$。**这就是"用预解式在无穷远处逼近恒等算子"这件事在对角情形最直白的样子**——下一章 Hille–Yosida 定理的证明里，$$A_\lambda=\lambda^2R(\lambda,A)-\lambda I$$ 这个"Yosida 逼近"，就是把 $$A$$（这里是 $$\operatorname{diag}(-2,-3)$$ 本身）用 $$\lambda R(\lambda,A)A$$（一个有界算子）去逼近；在对角情形可以直接算出 $$\lambda R(\lambda,A)A=\operatorname{diag}\bigl(\frac{-2\lambda}{\lambda+2},\frac{-3\lambda}{\lambda+3}\bigr)\to\operatorname{diag}(-2,-3)=A$$，与定理里"$$A_\lambda\to A$$"的结论逐分量吻合。$$\blacksquare$$

**解 研2.** $$S_3(x_1,x_2)=\dfrac{x_1^2+(x_2-x_1)^2+(3-x_2)^2}2$$ 对 $$x_1,x_2$$ 分别求偏导并令为零：

$$\frac{\partial S_3}{\partial x_1}=\frac{2x_1-2(x_2-x_1)}2=2x_1-x_2=0,\qquad
\frac{\partial S_3}{\partial x_2}=\frac{2(x_2-x_1)-2(3-x_2)}2=2x_2-x_1-3=0 .$$

由第一式 $$x_2=2x_1$$，代入第二式：$$2(2x_1)-x_1-3=0\Rightarrow3x_1=3\Rightarrow x_1=1$$，故 $$x_2=2$$。这正是把 $$[0,3]$$ 三等分的匀速直线路径 $$0\to1\to2\to3$$。代回：

$$S_3(1,2)=\frac{1^2+1^2+1^2}2=\frac32 .$$

连续情形（速度恒为 $$1$$，时长 $$3$$）的作用量是 $$S=\int_0^3\frac12\cdot1^2\,ds=\frac32$$，与离散最小值精确相等——**折线段数从 $$N=2$$ 变成 $$N=3$$，只要终点条件对应同一条匀速直线，最小作用量按比例增长（这里从 $$1$$ 变成 $$\frac32$$，正是总时长从 $$2$$ 变成 $$3$$ 的比例），驻定路径始终是那条直线**。这就是经典问题 5.3 的模式可以直接推广到任意 $$N$$ 的证据：第46章不会重复这个论证，但它是"$$\hbar\to0$$ 时相位在经典路径处驻定"这句直觉背后，唯一需要动笔验证的具体计算。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**1. 半群律就是"先走一段再走一段"。** $$T(s+t)=T(s)T(t)$$ 不是凭空的公理，标量情形里它就是指数律 $$e^ae^b=e^{a+b}$$；矩阵情形里它是"把矩阵乘出来、用具体的代数关系（如 $$A^2=0$$）化简"。第46章的三条公理，只是把这件具体的事写成对任意 Banach 空间都成立的语言。

**2. 生成元是出发点的瞬时变化率，未必处处存在。** 标量、矩阵例子里生成元就是求导、逐分量求导；换成热核，生成元的计算需要 Taylor 展开＋逐项积分，且只对"足够光滑"的函数成立——这正是第46章里"定义域 $$D(A)$$ 是真稠密子空间"这件事第一次露出苗头的地方。

**3. 预解式是半群的"现值"。** $$R(\lambda,A)=\int_0^\infty e^{-\lambda t}T(t)\,dt$$ 把一整条时间演化压缩成一个只依赖 $$\lambda$$ 的量；标量、对角情形里这就是初等的收敛积分 $$1/(\lambda+a)$$，第46章的定理 3.3 把它搬到一般算子上，证明的每一步在本章都已经在具体数字上算过一遍。

**4. 对易子是"顺序差"的精确度量，且只在 $$\varepsilon^2$$ 阶现身。** $$e^{\varepsilon A}e^{\varepsilon B}-e^{\varepsilon(A+B)}=\dfrac{\varepsilon^2}2[A,B]+O(\varepsilon^3)$$——这条式子在本章的具体矩阵上是可以逐项验证的等式，不是抽象论断；第46章 Trotter 公式的全部技术内容，就是把它从"某个具体的 $$2\times2$$ 例子"搬到"任意（不必可换的）算子"上，并且把 $$\varepsilon=1/m$$ 的 $$m$$ 次幂误差控制住。

**5. "驻定路径"不是新概念，是一个二次函数求极值。** 离散作用量 $$S_N(x_1,\dots,x_{N-1})$$ 在自由粒子的情形下就是若干项 $$(x_k-x_{k-1})^2$$ 的和，求极值给出的正是匀速直线运动——第46章路径积分里"$$\hbar\to0$$ 时相位在经典路径处驻定"这句话，背后唯一的具体计算就是本章经典问题 5.3、研究 2 已经做过的求偏导数、解线性方程组。

**现在你已经能手算出：半群律为什么成立、生成元怎么从差商里读出来、预解式是什么、两个不可交换的算子指数乘积差多少、离散折线的"作用量"怎么在自由粒子情形下取到最小值。** 下一章会把这些具体计算，一步步变成对任意 Banach 空间、任意无界自伴算子都成立的严格陈述与完整证明——从强连续半群的公理出发，用 Hille–Yosida 定理回答"哪些算子能生成半群"，用 Stone 定理把量子力学的时间演化接进来，最后用 Trotter 乘积公式证明 Feynman 路径积分只是一个良定义的算子极限，而不是一个"对所有路径积分"的新测度。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch44_正则对易关系与Stone_vonNeumann_下.md">← 第44章 正则对易关系与 Stone–von Neumann·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch46_算子半群与Feynman路径积分_下.md">第46章 算子半群与 Feynman 路径积分·下 →</a></div>
</div>
