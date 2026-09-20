---
layout: default
---

# 第23章: 算子半群与 Feynman 路径积分 (Operator Semigroups and Feynman Path Integrals)

> 对应原专栏: MP101–MP103
> 专家依据: `_experts/analysis/functional-analysis.md`(主) + `_experts/analysis/measure-integration.md`
> 知识库依据: `opc2/knowledge/math/泛函分析/`、`opc2/knowledge/physics/量子场论/tong-qft/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

本章要回答两个看起来不像同一个问题的具体问题：**$$e^{-tH}$$ 里的 $$H$$ 是无界算子，"指数"到底怎么定义？** 以及 **Feynman 路径积分像是在对"所有路径"积分——那是个什么测度？**

答案会落在同一处：那个积分不对应任何测度，它是一个**算子极限**的记号。而算子极限的定义，靠的是把 $$t\mapsto e^{-tH}$$ 看成一个**半群**。

**从哪来**：第 21 章的 Stone 定理说单参数酉群一一对应自伴算子，第 22 章的 Stone–von Neumann 定理说位置与动量的表示在酉等价下唯一。第 17 章写下了 Schrödinger 方程，但当时把 $$e^{-itH}$$ 当作形式记号。本章补上的是：这个记号什么时候真的有定义、为什么唯一、以及它如何长成路径积分。

**到哪去**：把指数映射从"时间"这条轴上解放出来——换成任意有限维结合代数的元素，就是 Lie 群的指数映射。那是第 24 章的起点，卷三到此收束。

## 二、入口：一道具体的问题 (Entry Problem)

本节先给题，不给定义。四问的答案分别在 3.1（(a)）、3.6（(c)）与 3.7（(b)(d)），其中 (d) 是枢纽。

**入口题（自编；取材于半群理论的经典算例 (a)(c) 与热核的标准计算 (b)，(d) 是路径积分的原始动机）。**

**(a) 一个生成元的算例。** 取

$$A=\begin{pmatrix}0&1\\0&0\end{pmatrix}.$$

算出 $$A^2$$，把指数级数 $$e^{tA}=\sum_{k\ge0}\dfrac{t^kA^k}{k!}$$ 求和、写成封闭形式，并验证 $$\{e^{tA}\}_{t\ge0}$$ 满足 $$T(0)=I$$、$$T(s)T(t)=T(s+t)$$。再算出算子范数 $$\lVert e^{tA}\rVert$$ 作为 $$t$$ 的函数，并回答：$$A$$ 自伴吗？若这族算子代表某系统的时间演化，$$\lVert e^{tA}\rVert>1$$ 说明什么？

**(b) 无界生成元的指数。** 在 $$L^2(\mathbb R)$$ 上取 $$H_0=-\dfrac{d^2}{dx^2}$$（取 $$\hbar=1$$、$$2m=1$$ 单位的自由 Schrödinger 算子）。对 $$f\in L^2(\mathbb R)$$，先承认下面这个公式（第五节会把它算出来）：

$$(e^{-tH_0}f)(x)=\frac{1}{\sqrt{4\pi t}}\int_{\mathbb R}e^{-\frac{(x-y)^2}{4t}}f(y)\,dy .$$

问三件事：$$t\to0^{+}$$ 时这个积分核趋向什么？对每个 $$t>0$$，$$\lVert e^{-tH_0}\rVert$$ 等于多少？能不能把 $$t$$ 取成负的——核在 $$t<0$$ 时还属于 $$L^1(\mathbb R)$$ 吗？

**(c) 两个指数能不能拆开。** 取

$$A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$$

（(a) 里的 $$A$$ 与这个是同一个）。把 $$e^{A/m}e^{B/m}$$ 与 $$e^{(A+B)/m}$$ 都按 $$m$$ 的幂展开到 $$\dfrac{1}{m^2}$$ 阶，求二者之差：它是零吗？若不是，等于什么、随 $$m\to\infty$$ 按什么幂次衰减？由此猜一猜 $$\lim_{m\to\infty}\left(e^{A/m}e^{B/m}\right)^{m}$$ 等于什么。

**(d) 那条"路径"在哪里。** (c) 的 $$m$$ 重乘积展开后是一串 $$m$$ 重求和；在 (b) 的核里出现的是 $$e^{-\frac{(x_k-x_{k-1})^2}{4t/m}}$$ 这样的因子。把 $$m$$ 个这样的因子连乘、取对数，指数上会留下

$$\sum_{k=1}^{m}\frac{(x_k-x_{k-1})^2}{t/m}.$$

把点 $$x_0,\dots,x_m$$ 连成一条 $$m$$ 段折线（每段"时间"是 $$\dfrac{t}{m}$$），这个和在 $$m$$ 很大时近似什么积分？再把势能项 $$V(x_k)\dfrac{t}{m}$$ 减进去，整个指数上的量与物理里哪个量长得一样？

本章会让你看到：**路径积分不是一条新公理，它是 Trotter 乘积公式的极限；而"对所有路径积分"这句话里，从来就没有过一个测度。**

## 三、结构：定义与完整推导 (Structure & Proof)

本节分七段：3.1–3.3 造出半群与生成元（"从半群读出算子"），3.4 的 Hille–Yosida 定理回答"哪些算子能当生成元"，3.5 把 Stone 定理装进半群语言，3.6 给出 Trotter 乘积公式，3.7 是高潮——路径积分作为它的极限。

### 3.1 半群的公理与三个例子

群的公理去掉"幺元存在"与"逆元存在"两条，剩下的结构就是半群。在算子理论里，半群天然地描述**只能向前走的时间**。

**定义 3.1（强连续半群, strongly continuous semigroup）**。设 $$X$$ 是 Banach 空间，$$\{T(t)\}_{t\ge0}\subset\mathcal B(X)$$ 是一族有界线性算子。若

- **(S1)** $$T(0)=I$$（$$I$$ 是 $$X$$ 上的恒等算子）；
- **(S2)** $$T(s+t)=T(s)T(t)$$ 对一切 $$s,t\ge0$$ 成立；
- **(S3)** 对每个 $$x\in X$$，映射 $$t\mapsto T(t)x$$ 从 $$[0,\infty)$$ 到 $$X$$ 连续，

则称它为**强连续半群**，也叫 $$C_0$$ 半群。$$X$$ 中一切这样的半群记作 $$\mathcal S(X)$$。

三条公理里 (S1)(S2) 是代数的，(S3) 是拓扑的。注意 (S2) 只对 $$t\ge0$$ 说事：半群不含逆元，这正是它比群弱的地方，也是它能描述"时间单向流逝"的原因。

**命题 3.1（强连续只需在原点验证）**。设 $$\{T(t)\}_{t\ge0}\subset\mathcal B(X)$$ 满足 (S1)(S2)。则 (S3) 成立当且仅当对每个 $$x\in X$$ 有 $$\lim_{t\to0^{+}}\lVert T(t)x-x\rVert=0$$。

*证明*：**必要性**：取 $$t=0$$，(S3) 在原点处的连续性就是这条极限，不需要另外论证。**充分性**：任取 $$t_0>0$$。由 (S2)，对 $$t=t_0+h$$（$$h>0$$）有 $$T(t)=T(t_0)T(h)$$；对 $$t=t_0-h$$（$$0<h\le t_0$$）由 $$T(t_0)=T(t_0-h)T(h)$$ 移项得 $$T(t_0-h)x-T(t_0)x=T(t_0-h)\bigl(x-T(h)x\bigr)$$。两式取范数：

$$\lVert T(t_0+h)x-T(t_0)x\rVert\le\lVert T(t_0)\rVert\cdot\lVert T(h)x-x\rVert,
\qquad
\lVert T(t_0-h)x-T(t_0)x\rVert\le\lVert T(t_0-h)\rVert\cdot\lVert x-T(h)x\rVert .$$

两式里的范数因子在 $$h\in[0,t_0]$$ 上都被下面的定理 3.1 的界控制（该定理的证明只用到原点连续性，不依赖本条），而 $$\lVert T(h)x-x\rVert\to0$$ 是假设。故左右极限都存在且等于 $$T(t_0)x$$，在 $$t_0$$ 连续。$$\blacksquare$$

强连续半群的一个重要后果是范数至多指数增长。

**定理 3.1（指数增长界）**。设 $$\{T(t)\}_{t\ge0}$$ 是 $$X$$ 上的强连续半群。则存在常数 $$M\ge1$$ 与 $$\omega\in\mathbb R$$，使得

$$\lVert T(t)\rVert\le Me^{\omega t},\qquad t\ge0 .$$

特别地，$$t\mapsto\lVert T(t)\rVert$$ 在紧区间 $$[0,t_0]$$ 上有界。

*证明*：对每个 $$x$$，$$t\mapsto\lVert T(t)x\rVert$$ 是 $$[0,1]$$ 上的连续函数，故有界：算子族 $$\{T(t):0\le t\le1\}$$ **逐点有界**。由一致有界原理（第 03 章），

$$M:=\sup_{0\le t\le1}\lVert T(t)\rVert<\infty,\qquad M\ge1\ (\text{因}\ T(0)=I).$$

对一般的 $$t$$，写 $$t=n+r$$（$$n=\lfloor t\rfloor\ge0$$、$$r\in[0,1)$$），由 (S2) 归纳得 $$T(t)=T(1)^{n}T(r)$$。取范数并用次乘性：

$$\lVert T(t)\rVert\le\lVert T(1)\rVert^{n}\lVert T(r)\rVert\le M^{n+1}.$$

$$M=1$$ 时 $$\lVert T(t)\rVert\le1$$，取 $$\omega=0$$ 即可；$$M>1$$ 时由 $$n\le t$$ 得 $$M^{n+1}\le Me^{t\ln M}$$，取 $$\omega=\ln M$$ 即得 $$\lVert T(t)\rVert\le Me^{\omega t}$$。紧区间上的有界性随之成立。$$\blacksquare$$

三个标准例子如下。

**例（有界生成元的指数半群）**。设 $$A\in\mathcal B(X)$$ 有界，令 $$T(t)=e^{tA}:=\sum_{k=0}^{\infty}\frac{t^{k}A^{k}}{k!}$$。级数绝对收敛（$$\sum_k\frac{t^{k}\lVert A\rVert^{k}}{k!}=e^{t\lVert A\rVert}<\infty$$），故 $$T(t)$$ 有定义且 $$\lVert e^{tA}\rVert\le e^{t\lVert A\rVert}$$。半群律来自绝对收敛级数的 Cauchy 乘积（按 $$j+k=n$$ 分组后逐项重排，再用二项式定理）；这一步用到 $$A$$ 与自己的幂全部可交换，正是这个例子不需要 Trotter 公式的原因。强连续来自 $$\lVert e^{tA}-I\rVert\le e^{t\lVert A\rVert}-1\to0$$。**入口题 (a) 的答**：那里 $$A$$ 幂零（$$A^{2}=0$$），级数在第 $$2$$ 项截断，$$e^{tA}=I+tA=\begin{pmatrix}1&t\\0&1\end{pmatrix}$$，半群律由 $$(I+sA)(I+tA)=I+(s+t)A$$ 直接验证；而 $$\lVert e^{tA}\rVert\ge\sqrt{1+t^{2}}>1$$（取 $$x=(0,1)$$），因为 $$A$$ 不自伴——**范数可以增长，这不是压缩半群**。

**例（热半群）**。在 $$L^2(\mathbb R)$$ 上取 $$H_0=-\dfrac{d^2}{dx^2}$$，热半群

$$(e^{-tH_0}f)(x)=\frac{1}{\sqrt{4\pi t}}\int_{\mathbb R}e^{-\frac{(x-y)^2}{4t}}f(y)\,dy$$

是入口题 (b) 的对象，其核 $$G_t(z)=\dfrac{1}{\sqrt{4\pi t}}e^{-\frac{z^2}{4t}}$$ 叫**热核 (heat kernel)**，且对一切 $$t>0$$ 有 $$\lVert e^{-tH_0}\rVert=1$$（见定理 3.4 的实例与练习基2）。三件事要记住：$$t\to0^{+}$$ 时 $$G_t$$ 趋近 Dirac 测度 $$\delta_0$$（$$\int G_t=1$$ 而质量集中在宽度 $$\sim\sqrt t$$ 内）；$$t<0$$ 时 $$e^{-\frac{z^2}{4t}}=e^{+\frac{z^2}{4\lvert t\rvert}}$$ 在无穷远指数增长、不再是 $$L^1$$ 函数，故没有"$$e^{+tH_0}$$"。半群在这里**真的只有一半**：热方程只能向前解。

**例（平移酉群，以及"半群未必可逆"的一般判断）**。在 $$X=L^2(\mathbb R)$$ 上令 $$(T(t)f)(x)=f(x+t)$$。由平移不变性 $$\lVert T(t)\rVert=1$$；强连续来自平移在 $$L^2$$ 中的连续性（连续紧支函数稠密，其上由一致连续得收敛，再用等距延拓）。这个公式其实给了一个**群**，逆元是 $$T(-t)$$，所以它由定理 3.6 的生成元 $$A=\dfrac{d}{dx}$$（定义域 $$H^{1}(\mathbb R)$$）生成，谱 $$\sigma(A)=i\mathbb R$$ 落在虚轴上。与上面的热半群形成准确对照：**生成元自伴且正 $$\Rightarrow$$ 压缩半群（一般不可逆）；生成元反自伴 $$\Rightarrow$$ 酉群（可逆）**。

（提醒一个常见误判：仅凭等距**不能**断言不是酉算子。热半群 $$e^{-tH_0}$$ 也有 $$\lVert T(t)\rVert=1$$，却确实不可逆——它是单射，值域是 $$L^2$$ 的真稠密子空间。判断可逆性看的是生成元自伴还是反自伴，不是范数。）

### 3.2 无穷小生成元

半群本身是"演化";我们想要的是驱动演化的那个算子。办法是求导。

**定义 3.2（无穷小生成元, infinitesimal generator）**。设 $$\{T(t)\}_{t\ge0}$$ 是 $$X$$ 上的强连续半群。令

$$D(A)=\left\{x\in X:\ \lim_{t\to0^{+}}\frac{T(t)x-x}{t}\ \text{在}\ X\ \text{中存在}\right\},$$

并对 $$x\in D(A)$$ 定义

$$Ax=\lim_{t\to0^{+}}\frac{T(t)x-x}{t}.$$

称 $$A$$ 为半群的**无穷小生成元**，$$D(A)$$ 是它的定义域。

定义里的极限是**范数意义**下的极限——正是这一点把形式化的求导变成了可以使用的算子。$$A$$ 一般**无界**：热半群的生成元是 $$-d^2/dx^2$$，它的定义域 $$H^2(\mathbb R)$$ 是 $$L^2$$ 的真稠密子空间。

**定理 3.2（生成元的基本性质）**。设 $$A$$ 是强连续半群 $$\{T(t)\}$$ 的生成元。则

**(i)** $$D(A)$$ 是 $$X$$ 的稠密线性子空间，$$A:D(A)\to X$$ 是线性算子；

**(ii)** $$A$$ 是**闭算子**：若 $$x_n\in D(A)$$、$$x_n\to x$$、$$Ax_n\to y$$，则 $$x\in D(A)$$ 且 $$Ax=y$$；

**(iii)** 对 $$x\in D(A)$$，有 $$T(t)x\in D(A)$$、$$AT(t)x=T(t)Ax$$，且映射 $$t\mapsto T(t)x$$ 在 $$[0,\infty)$$ 上连续可微，导数为

$$\frac{d}{dt}T(t)x=AT(t)x=T(t)Ax ;$$

**(iv)**（微积分基本定理）对 $$x\in D(A)$$ 与 $$t\ge0$$，

$$T(t)x-x=A\int_0^{t}T(s)x\,ds ,$$

其中右端的积分是取值于 $$X$$ 的 Bochner 积分，且 $$\int_0^tT(s)x\,ds\in D(A)$$。

*证明*：**(i)** 线性性直观：极限与减法的线性相容，逐项验证即可。

稠密性需要一个真论证。对 $$h>0$$、$$x\in X$$，令

$$x_h=\frac{1}{h}\int_0^{h}T(s)x\,ds$$

（Bochner 积分，被积函数连续）。由 (S1)(S3)，

$$\lVert x_h-x\rVert=\left\lVert\frac{1}{h}\int_0^{h}\bigl(T(s)x-x\bigr)ds\right\rVert\le\frac{1}{h}\int_0^{h}\lVert T(s)x-x\rVert\,ds\to0\qquad(h\to0^{+}),$$

故只要说明每个 $$x_h\in D(A)$$。算差商，用换元 $$u=t+s$$ 与区间可加性：

$$\frac{T(t)x_h-x_h}{t}=\frac{1}{th}\Bigl[\int_{t}^{t+h}T(u)x\,du-\int_{0}^{h}T(u)x\,du\Bigr]
=\frac{1}{th}\Bigl[\int_{h}^{t+h}T(u)x\,du-\int_{0}^{t}T(u)x\,du\Bigr].$$

固定 $$h$$ 令 $$t\to0^{+}$$：右端两个积分都是连续函数在长度 $$h$$、$$t$$ 上的平均，分别趋于 $$T(h)x$$ 与 $$T(0)x=x$$（连续函数的平均值趋于端点值）。故差商极限存在且等于 $$T(h)x-x$$，即 $$x_h\in D(A)$$、$$Ax_h=T(h)x-x$$。稠密性证完。

**(ii)** 先对 $$x\in D(A)$$ 证明积分恒等式

$$T(t)x-x=\int_0^{t}T(s)Ax\,ds. \qquad(\ast)$$

由 (S2)，$$\frac{T(t+s)x-T(s)x}{t}=T(s)\frac{T(t)x-x}{t}\to T(s)Ax$$（$$T(s)$$ 有界可与极限交换：$$\lVert T(s)(\text{差商}-Ax)\rVert\le\lVert T(s)\rVert\lVert\text{差商}-Ax\rVert$$，而 $$\lVert T(s)\rVert\le Me^{\omega s}$$ 在紧区间上有界）。故 $$s\mapsto T(s)x$$ 在 $$[0,t]$$ 上右导数处处存在、等于 $$T(s)Ax$$，且这个右导数连续，于是在 $$[0,t]$$ 上可导。把 $$\frac{d}{ds}T(s)x=T(s)Ax$$ 在 $$[0,t]$$ 上积分——这是取值于 Banach 空间 $$X$$ 的 $$C^1$$ 函数的牛顿-莱布尼茨公式：先用连续线性泛函把两边送回 $$\mathbb R$$，由 Hahn–Banach 的保范延拓（第 02 章）让 $$\mathbb R$$ 上的等式对一切泛函成立，从而推出向量等式——即得 $$(\ast)$$。

**(ii) 现在有了。** 设 $$x_n\to x$$、$$Ax_n\to y$$，对每个 $$n$$ 用 $$(\ast)$$：$$T(t)x_n-x_n=\int_0^{t}T(s)Ax_n\,ds$$。左端 $$\to T(t)x-x$$；右端由 $$\lVert T(s)(Ax_n-y)\rVert\le Me^{\omega s}\lVert Ax_n-y\rVert$$ 对 $$s\in[0,t]$$ 一致小，积分 $$\to\int_0^tT(s)y\,ds$$。于是

$$T(t)x-x=\int_0^{t}T(s)y\,ds .$$

两边除以 $$t$$ 并令 $$t\to0^{+}$$，右端是连续函数 $$s\mapsto T(s)y$$ 的平均，趋于 $$y$$。故差商极限存在且等于 $$y$$，即 $$x\in D(A)$$、$$Ax=y$$。$$A$$ 闭。

**(iii)** 第一段已经算出 $$T(t)x\in D(A)$$ 且 $$AT(t)x=T(t)Ax$$（差商极限那条式子）。把它与 $$(\ast)$$ 合起来，$$t\mapsto T(t)x$$ 右可导且导数连续（$$s\mapsto T(s)Ax$$ 连续），故在 $$[0,\infty)$$ 上 $$C^1$$、且

$$\frac{d}{dt}T(t)x=T(t)Ax=AT(t)x .$$

**(iv)** 就是上面的 $$(\ast)$$。$$\blacksquare$$

定理 3.2 和入口题 (a) 的对照值得点明。入口题里 $$A$$ 有界，$$T(t)=e^{tA}$$ 满足 $$\frac{d}{dt}T(t)=AT(t)$$，这在矩阵情形是逐项求导。定理 3.2 说的正是**同一条微分法则对无界生成元也成立**，代价是把定义域 $$D(A)$$ 显式搬上台面：等式只在 $$x\in D(A)$$ 上成立。生成元理论的全部技术困难，都来自"$$A$$ 无界、而 $$T(t)$$ 有界"这个不对称。

### 3.3 从半群读回生成元：Laplace 变换与预解式

如果把 $$\frac{d}{dt}T(t)=AT(t)$$ 想成"$$T(t)=e^{tA}$$"，那么把 $$e^{tA}$$ 的 Laplace 变换算出来应当得到 $$(\lambda I-A)^{-1}$$。这一节把这件事做成定理。先给预解式的定义。

**定义 3.3（预解集与预解式, resolvent set and resolvent）**。设 $$A:D(A)\subset X\to X$$ 是闭稠定线性算子。称

$$\rho(A)=\{\lambda\in\mathbb C:\ \lambda I-A:D(A)\to X\ \text{是双射}\}$$

为 $$A$$ 的**预解集**，$$\sigma(A)=\mathbb C\setminus\rho(A)$$ 为**谱**。对 $$\lambda\in\rho(A)$$，由开映射定理（第 03 章；此处 $$\lambda I-A$$ 闭且双射，逆算子自动有界）定义

$$R(\lambda,A)=(\lambda I-A)^{-1}\in\mathcal B(X),$$

称为 $$A$$ 在 $$\lambda$$ 处的**预解式**。

**定理 3.3（半群的 Laplace 变换即预解式）**。设 $$\{T(t)\}_{t\ge0}$$ 是强连续半群，$$\lVert T(t)\rVert\le Me^{\omega t}$$，$$A$$ 是它的生成元。则对一切实部 $$\operatorname{Re}\lambda>\omega$$，$$\lambda\in\rho(A)$$，且对每个 $$x\in X$$

$$R(\lambda,A)x=\int_{0}^{\infty}e^{-\lambda t}T(t)x\,dt,$$

其中积分是 Bochner 积分。

*证明*：**第一步，积分收敛。** 被积函数范数满足

$$\lVert e^{-\lambda t}T(t)x\rVert\le e^{-\operatorname{Re}(\lambda)t}Me^{\omega t}\lVert x\rVert=Me^{(\omega-\operatorname{Re}\lambda)t}\lVert x\rVert .$$

当 $$\operatorname{Re}\lambda>\omega$$ 时右端在 $$[0,\infty)$$ 上可积，故 Bochner 积分绝对收敛，定义了一个线性算子

$$L(\lambda)x=\int_0^{\infty}e^{-\lambda t}T(t)x\,dt,\qquad \lVert L(\lambda)\rVert\le\frac{M}{\operatorname{Re}\lambda-\omega}.$$

**第二步，$$L(\lambda)$$ 与 $$\lambda I-A$$ 互逆。** 对 $$h>0$$ 算 $$\bigl(T(h)-I\bigr)L(\lambda)$$。由 $$T(h)$$ 有界可与积分交换，再作平移换元 $$u=t+h$$：

$$T(h)L(\lambda)x=\int_0^\infty e^{-\lambda t}T(t+h)x\,dt=\int_h^\infty e^{-\lambda(u-h)}T(u)x\,du=e^{\lambda h}\int_h^{\infty}e^{-\lambda u}T(u)x\,du,$$

相减即得

$$\bigl(T(h)-I\bigr)L(\lambda)x=\bigl(e^{\lambda h}-1\bigr)L(\lambda)x-e^{\lambda h}\int_0^{h}e^{-\lambda u}T(u)x\,du .$$

两边除以 $$h$$ 并令 $$h\to0^{+}$$。右端第一项趋于 $$\lambda L(\lambda)x$$；第二项中 $$e^{\lambda h}\to1$$，而 $$\frac1h\int_0^he^{-\lambda u}T(u)x\,du$$ 是连续函数 $$u\mapsto e^{-\lambda u}T(u)x$$ 的平均，趋于它在 $$u=0$$ 处的值 $$x$$，故第二项趋于 $$x$$。于是左端极限存在（这同时把 $$L(\lambda)x\in D(A)$$ 一并证出，因为极限值就是 $$AL(\lambda)x$$），且

$$AL(\lambda)x=\lambda L(\lambda)x-x,\qquad\text{即}\qquad(\lambda I-A)L(\lambda)=I_X .$$

反方向。对 $$x\in D(A)$$，把恒等式 $$\frac{d}{dt}\bigl(e^{-\lambda t}T(t)x\bigr)=e^{-\lambda t}T(t)(A-\lambda I)x$$ 在 $$[0,\infty)$$ 上积分——这是取值于 $$X$$ 的 $$C^1$$ 函数，牛顿-莱布尼茨成立，$$t\to\infty$$ 处由指数衰减为 $$0$$：

$$-x=\int_0^{\infty}e^{-\lambda t}T(t)(A-\lambda I)x\,dt=L(\lambda)(A-\lambda I)x .$$

即 $$L(\lambda)(\lambda I-A)x=x$$ 对 $$x\in D(A)$$ 成立。两侧合起来，$$L(\lambda)$$ 是 $$\lambda I-A$$ 的双边逆，故 $$\lambda\in\rho(A)$$ 且 $$R(\lambda,A)=L(\lambda)$$。$$\blacksquare$$

定理 3.3 是本章的枢纽之一：它把"半群"这个时间对象**逐点**翻译成"预解式"这个复分析对象——只在 $$\operatorname{Re}\lambda>\omega$$ 的半平面上，但 $$A$$ 的谱信息已被这半平面上的 $$R(\lambda,A)$$ 决定。下一段反过来用这个翻译：以预解式上的估计判定一个算子能否生成半群。

### 3.4 反问题：压缩半群与 Hille–Yosida 定理

定理 3.3 只从半群读出了生成元的一部分信息。要反过来说"给定算子 $$A$$，它是不是某个半群的生成元"，需要一个充分必要条件。这就是本节。先看定义域上的界最干净的一类半群。

**定义 3.4（压缩半群, contraction semigroup）**。若强连续半群 $$\{T(t)\}_{t\ge0}$$ 满足 $$\lVert T(t)\rVert\le1$$ 对一切 $$t\ge0$$ 成立，称它为**压缩半群**。

压缩性给了预解式一个漂亮的界。

**定理 3.4（压缩半群生成元的预解式界）**。设 $$A$$ 生成压缩半群，则

$$\{\lambda\in\mathbb C:\operatorname{Re}\lambda>0\}\subset\rho(A),\qquad
\lVert R(\lambda,A)\rVert\le\frac{1}{\operatorname{Re}\lambda}\quad(\operatorname{Re}\lambda>0).$$

此外，实正 $$\lambda$$ 上有 $$\lVert\lambda R(\lambda,A)\rVert\le1$$，且对每个 $$x\in X$$

$$\lambda R(\lambda,A)x\xrightarrow[\lambda\to\infty]{}x$$

（这个极限是强收敛，不是范数收敛）。

*证明*：第一句是定理 3.3 的直接推论：压缩性给出 $$M=1$$、$$\omega=0$$，于是 $$\operatorname{Re}\lambda>0$$ 时 $$\lambda\in\rho(A)$$，且由那里对 $$L(\lambda)$$ 的范数估计

$$\lVert R(\lambda,A)\rVert\le\frac{1}{\operatorname{Re}\lambda-0}=\frac{1}{\operatorname{Re}\lambda}.$$

取 $$\lambda>0$$ 实数，被积范数 $$\le e^{-\lambda t}\lVert T(t)\rVert\lVert x\rVert\le e^{-\lambda t}\lVert x\rVert$$，故

$$\lVert R(\lambda,A)x\rVert\le\lVert x\rVert\int_0^\infty\lambda e^{-\lambda t}dt=\frac{\lVert x\rVert}{\lambda},
\qquad\text{即}\qquad\lVert\lambda R(\lambda,A)\rVert\le1 .$$

这就同时给了第三句的范数估计。还剩 $$\lambda R(\lambda,A)x\to x$$。用 $$\int_0^\infty\lambda e^{-\lambda t}dt=1$$ 把 $$x$$ 也写成同样的积分：

$$\lambda R(\lambda,A)x-x=\lambda\int_0^\infty e^{-\lambda t}\bigl(T(t)x-x\bigr)dt .$$

（被积函数的逐项相减，可积性由上面的估计保证。）取范数。对给定的 $$\varepsilon>0$$，由原点强连续取 $$\eta>0$$ 使 $$t\le\eta$$ 时 $$\lVert T(t)x-x\rVert\le\varepsilon$$。把积分拆成 $$[0,\eta]$$ 与 $$[\eta,\infty)$$。第一段：

$$\lambda\int_0^{\eta}e^{-\lambda t}\lVert T(t)x-x\rVert\,dt\le\varepsilon\lambda\int_0^{\eta}e^{-\lambda t}dt\le\varepsilon.$$

第二段用定理 3.1 的界 $$\lVert T(t)x\rVert\le Me^{\omega t}\lVert x\rVert$$，故 $$\lVert T(t)x-x\rVert\le(Me^{\omega t}+1)\lVert x\rVert$$，于是

$$\lambda\int_{\eta}^{\infty}e^{-\lambda t}\lVert T(t)x-x\rVert\,dt
\le\lVert x\rVert\Bigl(\frac{M\lambda}{\lambda-\omega}e^{-(\lambda-\omega)\eta}+e^{-\lambda\eta}\Bigr)
\qquad(\lambda>2\omega\ \text{时}),$$

这是把两项分别作显式积分 $$\int_\eta^\infty\lambda e^{-ct}dt=\lambda e^{-c\eta}/c$$ 得到的。$$\lambda\to\infty$$ 时右端指数衰减到 $$0$$。于是 $$\lambda$$ 足够大时左端 $$\le2\varepsilon$$。$$\varepsilon$$ 任意即得结论。$$\blacksquare$$

现在给充分必要条件。方向上分成两半："只有若"（生成元必满足预解式条件）已由定理 3.4 给出；"若"（预解式条件够生成一个压缩半群）是本定理的实质内容，用一个显式逼近构造来证明。

**定理 3.5（Hille–Yosida 定理, Hille–Yosida theorem）**。设 $$A:D(A)\subset X\to X$$ 是稠定闭线性算子。则 $$A$$ 生成一个压缩半群，当且仅当

$$\mathbb R_{>0}\subset\rho(A)\qquad\text{且}\qquad \lVert R(\lambda,A)\rVert\le\frac1\lambda\quad\text{对一切}\ \lambda>0\ \text{成立}. \tag{*}$$

*证明*。**必要性**即定理 3.4 在实正 $$\lambda$$ 上的那一行，不再重复。

**充分性。** 假设 $$(*)$$。整个构造分四步。

**第一步：Yosida 逼近是预解式的显式函数，因而彼此可交换。** 对 $$\lambda>0$$ 定义

$$A_\lambda=\lambda A R(\lambda,A)=\lambda^{2}R(\lambda,A)-\lambda I .$$

中间那个等式是这样来的：由 $$(\lambda I-A)R(\lambda,A)=I$$ 解出 $$AR(\lambda,A)=\lambda R(\lambda,A)-I$$，两边乘 $$\lambda$$。右端是**有界算子**的组合，于是 $$A_\lambda\in\mathcal B(X)$$ 且

$$\lVert A_\lambda\rVert\le\lambda^{2}\lVert R(\lambda,A)\rVert+\lambda\le\lambda^{2}\cdot\frac1\lambda+\lambda=2\lambda .$$

同时，$$A_\lambda$$ 是 $$R(\lambda,A)$$ 的多项式，而预解式之间可以交换。这来自**预解恒等式**

$$R(\lambda,A)-R(\mu,A)=(\mu-\lambda)R(\lambda,A)R(\mu,A), \tag{3.1}$$

其验证是纯代数的：在恒等式 $$(\mu I-A)-(\lambda I-A)=(\mu-\lambda)I$$ 的两边左乘 $$R(\lambda,A)$$、右乘 $$R(\mu,A)$$ 即得（每个乘积都是有界算子）。再交换 $$\lambda,\mu$$ 得另一式，两式相加即得

$$R(\lambda,A)R(\mu,A)=R(\mu,A)R(\lambda,A),\qquad\text{从而}\qquad
A_\lambda A_\mu=A_\mu A_\lambda\quad(\lambda,\mu>0) \tag{3.2}$$

（$$A_\lambda$$ 是 $$R(\lambda,A)$$ 的多项式）。

**第二步：$$A_\lambda$$ 在 $$D(A)$$ 上逼近 $$A$$。** 对 $$x\in D(A)$$，由第一步的恒等式 $$A_\lambda x=\lambda R(\lambda,A)Ax$$（$$R(\lambda,A)$$ 的值域落在 $$D(A)$$，而在 $$D(A)$$ 上 $$A$$ 与 $$R(\lambda,A)$$ 交换：两边都算得 $$\lambda R(\lambda,A)x-x$$）。由定理 3.4，$$\lambda R(\lambda,A)Ax\to Ax$$，故

$$A_\lambda x\xrightarrow[\lambda\to\infty]{}Ax,\qquad
\lVert A_\lambda x-Ax\rVert=\lVert R(\lambda,A)Ax\rVert\le\frac{\lVert Ax\rVert}{\lambda}\le\lVert Ax\rVert. \tag{3.3}$$

第二式是把 $$\lambda R(\lambda,A)Ax-Ax=-R(\lambda,A)Ax$$ 代进去、再用 $$\lVert R(\lambda,A)\rVert\le1/\lambda$$。

**第三步：$$e^{tA_\lambda}$$ 是强收敛的 Cauchy 族。** $$A_\lambda$$ 有界，故 $$e^{tA_\lambda}$$ 由 3.1 段的例子定义良好；要紧的是它一致压缩。$$A_\lambda$$ 也满足 $$(*)$$：由预解恒等式，

$$R(\mu,A_\lambda)=\bigl((\mu+\lambda)I-\lambda^{2}R(\lambda,A)\bigr)^{-1}
=\frac1{\mu+\lambda}\sum_{k\ge0}\Bigl(\frac{\lambda^{2}}{\mu+\lambda}R(\lambda,A)\Bigr)^{k},$$

右端是 Neumann 级数，因为 $$\bigl\lVert\frac{\lambda^{2}}{\mu+\lambda}R(\lambda,A)\bigr\rVert\le\frac{\lambda}{\mu+\lambda}<1$$，绝对收敛；求和得 $$\lVert R(\mu,A_\lambda)\rVert\le\frac1{\mu+\lambda}\cdot\frac{\mu+\lambda}{\mu}=\frac1\mu$$。既然有界算子 $$A_\lambda$$ 满足 $$(*)$$，定理 3.4 的证明（只用到 $$\lVert R(\mu,A_\lambda)\rVert\le1/\mu$$）给出

$$\lVert e^{tA_\lambda}\rVert\le1 . \tag{3.4}$$

现在对 $$x\in D(A)$$ 用**两个交换的有界算子之差的积分表示**：

$$e^{tA_\lambda}-e^{tA_\mu}=\int_0^{t}\frac{d}{ds}\Bigl[e^{sA_\lambda}e^{(t-s)A_\mu}\Bigr]ds
=\int_0^{t}e^{sA_\lambda}\bigl(A_\lambda-A_\mu\bigr)e^{(t-s)A_\mu}\,ds,$$

用了链式法则与 (3.2)（两个可交换的有界算子，其指数也可交换）。取范数并用 (3.4)：

$$\bigl\lVert\bigl(e^{tA_\lambda}-e^{tA_\mu}\bigr)x\bigr\rVert\le\int_0^{t}\lVert A_\lambda x-A_\mu x\rVert\,ds=t\lVert A_\lambda x-A_\mu x\rVert .$$

由 (3.3)，右端 $$\le t\bigl(\lVert A_\lambda x-Ax\rVert+\lVert A_\mu x-Ax\rVert\bigr)\to0$$（$$\lambda,\mu\to\infty$$），且这个收敛对 $$t$$ 在任意紧区间上**一致**（界中除因子 $$t$$ 外不含 $$t$$）。于是对每个 $$x\in D(A)$$，$$e^{tA_\lambda}x$$ 关于 $$\lambda$$ 是 Cauchy 族，极限存在，记作

$$T(t)x=\lim_{\lambda\to\infty}e^{tA_\lambda}x .$$

对一般 $$x\in X$$：因 $$A$$ 稠定，取 $$x_n\in D(A)$$、$$x_n\to x$$，由 (3.4) 有 $$\lVert T(t)x_n-T(t)x_m\rVert\le\lVert x_n-x_m\rVert$$（极限保范数），故 $$\{T(t)x_n\}$$ 是 Cauchy 列；定义 $$T(t)x=\lim_nT(t)x_n$$。这是标准的"稠密子空间上取极限 + 一致有界延拓"，与 $$\lambda$$ 的极限不冲突。

**第四步：$$T(t)$$ 是压缩半群，其生成元恰是 $$A$$。** 压缩性：由 (3.4) 与极限保范数，$$\lVert T(t)x\rVert\le\lVert x\rVert$$。半群律：由 $$e^{(s+t)A_\lambda}=e^{sA_\lambda}e^{tA_\lambda}$$ 与两个因子的强收敛取极限得到（乘积的强极限：$$\lVert e^{sA_\lambda}(e^{tA_\lambda}-T(t))x\rVert\le\lVert(e^{tA_\lambda}-T(t))x\rVert$$）。强连续性：对 $$x_0\in D(A)$$，

$$\lVert T(t)x_0-x_0\rVert=\lim_\lambda\Bigl\lVert\int_0^{t}e^{sA_\lambda}A_\lambda x_0\,ds\Bigr\rVert\le t\sup_\lambda\lVert A_\lambda x_0\rVert\le 2t\lVert Ax_0\rVert,$$

（第一个等号用了 $$e^{tA_\lambda}x_0-x_0=\int_0^te^{sA_\lambda}A_\lambda x_0ds$$，这是有界算子版的定理 3.2(iv)；最后一步用 (3.3) 型估计 $$\lVert A_\lambda x_0\rVert\le\lVert Ax_0\rVert+\lVert Ax_0\rVert$$。）故 $$t\to0^{+}$$ 时它趋于 $$0$$；一般 $$x$$ 由稠密性与压缩性夹逼（$$\lVert T(t)x-x\rVert\le2\lVert x-x_0\rVert+\lVert T(t)x_0-x_0\rVert$$）。于是 $$\{T(t)\}$$ 是压缩半群。

设 $$B$$ 是 $$\{T(t)\}$$ 的生成元。对 $$x_0\in D(A)$$，把上文那条积分表示拆开：

$$T(t)x_0-x_0=\lim_\lambda\int_0^{t}e^{sA_\lambda}A_\lambda x_0\,ds=\int_0^{t}T(s)Ax_0\,ds .$$

中间的换极限合法：被积函数差 $$\lVert e^{sA_\lambda}A_\lambda x_0-T(s)Ax_0\rVert\le\lVert A_\lambda x_0-Ax_0\rVert+\lVert(e^{sA_\lambda}-T(s))Ax_0\rVert$$，两项都在 $$s\in[0,t]$$ 上一致趋于 $$0$$。两边除以 $$t$$ 并令 $$t\to0^{+}$$，右端是连续函数 $$s\mapsto T(s)Ax_0$$ 的平均，趋于 $$Ax_0$$。故 $$x_0\in D(B)$$ 且 $$Bx_0=Ax_0$$，即

$$A\subset B .$$

最后说明这个包含号其实是等号。由必要性（定理 3.4 应用于 $$B$$），$$\lambda I-B:D(B)\to X$$ 对 $$\lambda>0$$ 是双射；由假设 $$(*)$$，$$\lambda I-A:D(A)\to X$$ 也是双射。而 $$A\subset B$$ 意味着 $$\lambda I-B$$ 是 $$\lambda I-A$$ 的延拓，两个算子都把各自的定义域双射到同一个 $$X$$ 上，于是定义域必须相同：

$$D(B)=(\lambda I-B)^{-1}(X)=(\lambda I-A)^{-1}(X)=D(A),$$

故 $$B=A$$。$$\blacksquare$$

Hille–Yosida 定理回答了本章开头的问题：**"$$e^{tA}$$"什么时候有定义**——当 $$A$$ 稠定闭、正实轴落在预解集中并有 $$1/\lambda$$ 的界时。入口题 (b) 是它的实例：$$H_0=-d^2/dx^2$$ 的预解式在 $$\lambda>0$$ 上是乘子 $$1/(\lambda+k^2)$$，关于 $$k$$ 的上确界恰是 $$1/\lambda$$，条件 $$(*)$$ 以等式成立，对应的半群范数处处等于 $$1$$。

对非压缩的半群（例如入口题 (a) 里范数会增长的 $$e^{tA}$$），同一套论证给出 **Hille–Yosida–Phillips** 形式：若存在 $$\omega\in\mathbb R$$ 与 $$M\ge1$$ 使 $$(\omega,\infty)\subset\rho(A)$$ 且

$$\bigl\lVert(\lambda I-A)^{-k}\bigr\rVert\le\frac{M}{(\lambda-\omega)^{k}}\qquad(k\in\mathbb N,\ \lambda>\omega),$$

则 $$A$$ 生成满足 $$\lVert T(t)\rVert\le Me^{\omega t}$$ 的强连续半群。每个幂次 $$k$$ 都要验，正是为了让第三步里的指数范数被控住——这就是该条件比 $$(*)$$ 多出一个 $$k$$ 的原因。

### 3.5 Stone 定理：半群语言的单参数酉群

第 21 章的 Stone 定理说"单参数强连续酉群一一对应自伴算子"。用本节的生成元语言，它可以重新表述为一条关于半群的命题。

**定理 3.6（Stone 定理, 半群表述）**。设 $$\{U(t)\}_{t\in\mathbb R}\subset\mathcal B(H)$$ 是 Hilbert 空间 $$H$$ 上的强连续单参数酉群（即 $$U(s+t)=U(s)U(t)$$ 对一切 $$s,t\in\mathbb R$$ 成立、$$U(t)^{*}U(t)=I$$、$$t\mapsto U(t)\psi$$ 连续）。则存在唯一自伴算子 $$A:D(A)\subset H\to H$$ 使

$$U(t)=e^{-itA},\qquad t\in\mathbb R .$$

反之，每个自伴算子 $$A$$ 通过这个公式生成强连续单参数酉群。

*证明*：定理本身在第 21 章已证，这里只做与本章语言的接驳。

**从群到半群。** 把 $$\{U(t)\}$$ 限制到 $$t\ge0$$，得到强连续半群 $$\{U(t)\}_{t\ge0}$$（(S1)(S2)(S3) 逐条继承）。由定理 3.2 它有生成元 $$B$$，且对 $$\psi\in D(B)$$ 有 $$\frac{d}{dt}U(t)\psi=BU(t)\psi$$。$$B$$ 的形状被酉性锁死：对 $$\psi\in D(B)$$，

$$\langle B\psi,\psi\rangle=\lim_{t\to0^{+}}\Bigl\langle\frac{U(t)\psi-\psi}{t},\psi\Bigr\rangle .$$

由 $$U(t)^{*}U(t)=I$$ 在 $$t=0$$ 处求导得 $$B^{*}+B=0$$（$$B$$ 稠定闭时 $$B^{*}$$ 存在且 $$\frac{d}{dt}\bigl[U(t)^*U(t)\bigr]\bigr\rvert_{t=0}=B^*+B$$，由上式极限与伴随的定义逐项对上），故

$$B^{*}=-B,$$

即 $$B$$ 是**反自伴**算子。令 $$A=iB$$，则 $$A$$ 自伴（$$A^{*}=(iB)^{*}=-iB^{*}=-i(-B)=iB=A$$），且对 $$\psi\in D(A)=D(B)$$

$$\frac{d}{dt}U(t)\psi=-iA\,U(t)\psi .$$

这正是 Schrödinger 方程 $$\frac{d}{dt}\psi=-iA\psi$$ 的算子形式。解的**唯一性**：若 $$u,v$$ 是同一初值问题的两个 $$C^1$$ 解，则 $$w=u-v$$ 满足 $$\frac{d}{dt}w=-iAw$$、$$w(0)=0$$，于是

$$\frac{d}{dt}\lVert w(t)\rVert^{2}=2\operatorname{Re}\langle w(t),\tfrac{d}{dt}w(t)\rangle=2\operatorname{Re}\bigl\langle w(t),-iAw(t)\bigr\rangle
=2\operatorname{Re}\bigl(i\langle Aw(t),w(t)\rangle\bigr)=0,$$

最后一步用了 $$\langle Aw,w\rangle\in\mathbb R$$（$$A$$ 自伴）。故 $$\lVert w(t)\rVert=\lVert w(0)\rVert=0$$。而 $$e^{-itA}\psi$$ 是同一初值问题的解（由定理 3.5 应用于 $$-iA$$：$$\lVert e^{-itA}\rVert=1$$ 与 $$\lVert R(\lambda,-iA)\rVert\le1/\lambda$$ 互为条件），故 $$U(t)\psi=e^{-itA}\psi$$。$$\blacksquare$$

这段接驳里有两点要单独记住。其一，**半群是群的"半边"**：$$U(t)$$ 只在 $$t\ge0$$ 上使用便得到反自伴生成元 $$B=iA$$；反过来，给定自伴 $$A$$，$$e^{-tA}$$（压缩半群）与 $$e^{-itA}$$（酉群）是**同一个 $$A$$ 的两副面孔**，由 $$t\mapsto it$$ 的解析延拓相连——物理上这就是 Minkowski 与欧氏时空之间的 Wick 转动。其二，**解析延拓不动谱**：从 $$e^{-tk^{2}}$$（实衰减，热方程）换成 $$e^{-itk^{2}}$$（纯振荡，Schrödinger 方程），乘子改的只是相位的写法，$$\sigma(A)$$ 一点没动；这就是"用虚时间解实时间的问题"在数学上不投机取巧的原因——两侧的预解式是同一个。

### 3.6 Trotter 乘积公式

定理 3.5 说清了 $$e^{tA}$$ 何时有定义，定理 3.6 说清了量子演化的生成元是谁。但物理里的 $$H=H_0+V$$ 是**和**：定理 3.5 的预解式条件要把 $$R(\lambda,H_0+V)$$ 整体算出才好验，而 $$e^{-tH_0}$$ 与 $$e^{-tV}$$ 分别可以显式写出。于是问题变成：**能不能用它们拼出 $$e^{-t(H_0+V)}$$？** 入口题 (c) 已预告障碍——两个算子不对易。先看有限维情形。

**定理 3.7（Lie 乘积公式, Lie product formula）**。对任意 $$A,B\in\mathbb C^{n\times n}$$（不必可换），

$$e^{A+B}=\lim_{m\to\infty}\Bigl(e^{A/m}e^{B/m}\Bigr)^{m},
\qquad
\Bigl\lVert\Bigl(e^{A/m}e^{B/m}\Bigr)^{m}-e^{A+B}\Bigr\rVert\le\frac{C}{m},$$

其中 $$C=\dfrac{\lVert[A,B]\rVert}2e^{\lVert A\rVert+\lVert B\rVert}$$。

*证明*：记 $$\varepsilon=\dfrac1m$$，$$S=e^{\varepsilon(A+B)}$$、$$T=e^{\varepsilon A}e^{\varepsilon B}$$。

**第一步，算出 $$S$$ 与 $$T$$ 的二阶差。** 把 $$T$$ 中的每个因子按余项展开：

$$T=\Bigl(I+\varepsilon A+\frac{\varepsilon^{2}A^{2}}2+\rho_A\Bigr)\Bigl(I+\varepsilon B+\frac{\varepsilon^{2}B^{2}}2+\rho_B\Bigr),$$

其中 $$\lVert\rho_A\rVert\le\varepsilon^{3}e^{\lVert A\rVert}$$（级数从 $$k=3$$ 起求和、提出 $$\varepsilon^{3}$$ 后被 $$e^{\lVert A\rVert}$$ 控制），$$\rho_B$$ 同理。丢弃 $$\varepsilon^{3}$$ 及以上项：

$$T=I+\varepsilon(A+B)+\varepsilon^{2}\Bigl(\frac{A^{2}}2+AB+\frac{B^{2}}2\Bigr)+O(\varepsilon^{3}).$$

同样，从 $$S=e^{\varepsilon(A+B)}$$ 得

$$S=I+\varepsilon(A+B)+\frac{\varepsilon^{2}(A+B)^{2}}2+O(\varepsilon^{3})
=I+\varepsilon(A+B)+\varepsilon^{2}\Bigl(\frac{A^{2}}2+\frac{AB+BA}2+\frac{B^{2}}2\Bigr)+O(\varepsilon^{3}).$$

相减。$$\varepsilon$$ 项抵消，$$\varepsilon^{2}$$ 的"对称部分"（$$\frac{A^2}2$$、$$\frac{AB+BA}2$$、$$\frac{B^2}2$$）也逐项抵消，只剩反对称的那一半：

$$T-S=\varepsilon^{2}\Bigl(AB-\frac{AB+BA}2\Bigr)+O(\varepsilon^{3})
=\frac{\varepsilon^{2}}2(AB-BA)+O(\varepsilon^{3})
=\frac{\varepsilon^{2}}2[A,B]+O(\varepsilon^{3}). \tag{3.5}$$

这就是入口题 (c) 的答案：**差不为零，差恰是对易子**，而且带着 $$\varepsilon^{2}=1/m^{2}$$ 而不是 $$1/m$$——所以取 $$m$$ 次幂会把它压下去。

**第二步，把二阶差放大成 $$m$$ 次幂的差。** 由 $$T^{m}-S^{m}=\sum_{k=0}^{m-1}T^{k}(T-S)S^{m-1-k}$$（等比级数求和的算子版本：把 $$T^{m}-S^{m}$$ 逐项配对即得），取范数：

$$\lVert T^{m}-S^{m}\rVert\le\sum_{k=0}^{m-1}\lVert T\rVert^{k}\lVert T-S\rVert\lVert S\rVert^{m-1-k}
\le m\max(\lVert T\rVert,\lVert S\rVert)^{m-1}\lVert T-S\rVert .$$

再用一阶界 $$\lVert T\rVert\le(1+\varepsilon\lVert A\rVert)(1+\varepsilon\lVert B\rVert)\le e^{\varepsilon(\lVert A\rVert+\lVert B\rVert)}$$（$$\lVert S\rVert\le e^{\varepsilon(\lVert A\rVert+\lVert B\rVert)}$$ 同理；其实 $$S=e^{\varepsilon(A+B)}$$），故

$$\max(\lVert T\rVert,\lVert S\rVert)^{m-1}\le e^{(m-1)\varepsilon(\lVert A\rVert+\lVert B\rVert)}\le e^{\lVert A\rVert+\lVert B\rVert}.$$

代入：$$m\cdot e^{\lVert A\rVert+\lVert B\rVert}\cdot\frac{\varepsilon^{2}}2\lVert[A,B]\rVert
=\frac{\lVert[A,B]\rVert}{2m}e^{\lVert A\rVert+\lVert B\rVert}$$（用了 $$m\varepsilon^{2}=1/m$$）。于是

$$\Bigl\lVert\Bigl(e^{A/m}e^{B/m}\Bigr)^{m}-e^{A+B}\Bigr\rVert
=\lVert T^{m}-S^{m}\rVert\le\frac{C}{m},\qquad C=\frac{\lVert[A,B]\rVert}2e^{\lVert A\rVert+\lVert B\rVert},$$

最后一步用了 $$S^{m}=\bigl(e^{\varepsilon(A+B)}\bigr)^{m}=e^{A+B}$$。$$\blacksquare$$

（(3.5) 的 $$O(\varepsilon^{3})$$ 余项被吸收进常数 $$C$$，不影响 $$1/m$$ 的量级；经典问题 5.3 用数值验证了这个量级。）

现在把 $$m$$ 从整数幂换成实数参数、把矩阵换成 Hilbert 空间上的自伴算子。无界情形不能照搬上面的展开——$$A^{2}$$ 对无界 $$A$$ 没有意义——但结论仍然成立。

**定理 3.8（Trotter 乘积公式, Trotter product formula）**。设 $$H$$ 是 Hilbert 空间，$$A,B$$ 自伴，且定义在 $$D(A)\cap D(B)$$ 上的 $$A+B$$ 是**本质自伴**的（它的闭包 $$\overline{A+B}$$ 自伴；由下述 Kato–Rellich 判据，当 $$B$$ 相对 $$A$$-有界且界 $$<1$$ 时成立）。则对一切 $$\psi\in H$$ 与 $$t\in\mathbb R$$

$$\Bigl(e^{-itA/m}e^{-itB/m}\Bigr)^{m}\psi\ \xrightarrow[m\to\infty]{}\ e^{-it\overline{A+B}}\,\psi .$$

作虚时间替换 $$t\to it$$（$$A,B$$ 换成生成压缩半群的自伴算子，例如 $$A=H_0$$、$$B=V\ge0$$ 有界），同一个结论对 $$t\ge0$$ 成立：

$$\Bigl(e^{-tH_0/m}e^{-tV/m}\Bigr)^{m}\psi\ \xrightarrow[m\to\infty]{}\ e^{-t\,\overline{H_0+V}}\,\psi .$$

*证明思路与已证部分的接驳*。**有界情形**由定理 3.7 直接给出：矩阵的证明逐字适用于 Banach 空间上的有界算子，因为全程只用了范数次乘性与指数级数的收敛。

**无界情形**的困难是 $$e^{\varepsilon A}$$ 的展开里 $$\varepsilon^{2}A^{2}$$ 无意义，所以 (3.5) 写不出来。办法是改用**预解式**验证收敛：由定理 3.5，$$e^{-tA}$$ 的生成元完全由 $$R(\lambda,A)$$ 决定，而 $$R(\lambda,A)R(\lambda,B)$$ 是两个**有界**算子，于是定理 3.7 的代数计算可以逐项搬到预解式上，得到 $$\bigl(I+\frac tm A\bigr)^{-1}\bigl(I+\frac tm B\bigr)^{-1}$$ 收敛到 $$e^{-t\overline{A+B}}$$ 的预解式。这一步的完整证明是 Kato 的收敛定理（定理 3.9），本书引用而不复证。

**定理 3.9（Trotter–Kato 收敛定理；作为已知结论引用）**。设 $$\{S_n(t)\}_{t\ge0}$$ 是 Banach 空间 $$X$$ 上一族压缩半群，生成元为 $$C_n$$（不要求有界）。若存在 $$\lambda_0>0$$ 使 $$R(\lambda_0,C_n)\to R(\lambda_0,C)$$ 强收敛（$$C$$ 闭稠定），则 $$C$$ 生成压缩半群，且 $$S_n(t)x\to e^{tC}x$$ 对一切 $$x\in X$$、$$t$$ 在紧区间上一致。证明见 Kato《Perturbation Theory for Linear Operators》第 IX 章；本课程用它把"有限维 Lie 乘积公式"提升为"无界算子 Trotter 公式"，两个定理的**代数核心是同一个对易子估计**。

**Kato–Rellich 判据（回顾）**。若 $$A$$ 自伴、$$B$$ 对称且存在 $$a<\tfrac12$$、$$b\ge0$$ 使 $$\lVert B\psi\rVert\le a\lVert A\psi\rVert+b\lVert\psi\rVert$$（$$\psi\in D(A)$$），则 $$A+B$$（定义域取 $$D(A)$$）自伴。这是定理 3.8 中"$$A+B$$ 本质自伴"的前提，例如 $$V\in L^2(\mathbb R^n)+L^\infty(\mathbb R^n)$$ 且无穷远处趋于零时成立，于是 $$H$$ 自伴、Trotter 公式可用。第 22 章的 Stone–von Neumann 定理在这里的作用是保证"$$H_0+V$$"这个写法没有隐藏的表示自由度。

### 3.7 高潮：Feynman 路径积分是 Trotter 公式的极限

准备工作做完，现在把定理 3.8 的右边一项一项算出来。设 $$\mathbb R^n$$ 中质量为 $$m$$ 的自由粒子服从

$$i\hbar\frac{\partial}{\partial t}\psi=H\psi,\qquad H=H_0+V,\qquad H_0=-\frac{\hbar^{2}}{2m}\Delta,$$

即动量算子 $$P=-i\hbar\nabla$$、动能 $$H_0=\dfrac{P^{2}}{2m}$$（第 22 章的正则对易关系 $$[Q_j,P_k]=i\hbar\delta_{jk}$$ 正是把 $$P$$ 取成 $$-i\hbar\nabla$$ 的那条约束）。$$H$$ 在 $$D(H_0)\cap D(V)$$ 上本质自伴（Kato–Rellich），故解算子 $$e^{-itH/\hbar}$$ 由定理 3.6 存在。

**定理 3.10（自由传播子的核）**。对 $$f\in L^2(\mathbb R^n)$$ 与 $$t\ne0$$，

$$\bigl(e^{-itH_0/\hbar}f\bigr)(x)=\Bigl(\frac{m}{2\pi i\hbar t}\Bigr)^{n/2}\int_{\mathbb R^n}e^{\frac{im\lvert x-y\rvert^{2}}{2\hbar t}}f(y)\,dy . \tag{3.6}$$

*证明*：取归一化 $$\hat f(k)=(2\pi)^{-n/2}\int_{\mathbb R^n}f(y)e^{-ik\cdot y}dy$$、$$f(x)=(2\pi)^{-n/2}\int_{\mathbb R^n}\hat f(k)e^{ik\cdot x}dk$$。在谱表示下 $$H_0$$ 是乘子 $$\dfrac{\hbar^{2}\lvert k\rvert^{2}}{2m}$$（第 19 章的谱定理：$$H_0=\int\frac{\hbar^2\lvert k\rvert^2}{2m}dE(k)$$，因为 $$P=-i\hbar\nabla$$ 在 Fourier 侧乘 $$\hbar k$$），故 $$e^{-itH_0/\hbar}$$ 是乘 $$e^{-\frac{i\hbar t\lvert k\rvert^{2}}{2m}}$$：

$$\bigl(e^{-itH_0/\hbar}f\bigr)(x)=(2\pi)^{-n/2}\int_{\mathbb R^n}e^{ik\cdot x}e^{-\frac{i\hbar t\lvert k\rvert^{2}}{2m}}\hat f(k)\,dk .$$

代入 $$\hat f$$ 的定义并交换积分顺序（绝对收敛：$$\hat f\in L^2$$、高斯因子有界），得到 $$(3.6)$$ 的核

$$G_t(z)=(2\pi)^{-n}\int_{\mathbb R^n}e^{ik\cdot z}e^{-\frac{i\hbar t\lvert k\rvert^{2}}{2m}}dk,\qquad z=x-y .$$

这是 $$n$$ 个一维 Gaussian 积分的乘积。记 $$a=\dfrac{i\hbar t}{2m}$$，用标准积分 $$\int_{\mathbb R}e^{ikz}e^{-ak^{2}}dk=\sqrt{\pi/a}\,e^{-z^{2}/4a}$$（$$\operatorname{Re}a>0$$ 时成立；纯虚的 $$a$$ 由两侧解析延拓到边界得到，$$\sqrt a$$ 取使 $$\operatorname{Re}\sqrt a>0$$ 的那支）：

$$\frac1{2\pi}\int_{\mathbb R}e^{ikz}e^{-ak^{2}}dk=\frac{1}{2\sqrt{\pi a}}e^{-\frac{z^{2}}{4a}}
\ \overset{a=\frac{i\hbar t}{2m}}{=}\ \sqrt{\frac{m}{2\pi i\hbar t}}\,e^{\frac{imz^{2}}{2\hbar t}},$$

与 $$(3.6)$$ 中 $$n=1$$ 的核一致；$$n$$ 维即把一维核连乘 $$n$$ 次。$$\blacksquare$$

（把 $$t$$ 换成 $$-it$$（$$t>0$$），$$(3.6)$$ 的核变成 $$(m/2\pi\hbar t)^{n/2}e^{-m\lvert z\rvert^{2}/2\hbar t}$$——$$2\pi i\hbar t$$ 翻成实因子，指数上的 $$1/t$$ 翻成 $$-1/t$$。这正是入口题 (b) 的热核（取 $$\hbar=1$$、$$2m=1$$ 得 $$\sqrt{4\pi t}$$ 的归一化）：$$t\to0^{+}$$ 时趋近 $$\delta_0$$，$$t<0$$ 时指数在无穷远发散、不再是 $$L^1$$ 函数——这就是 3.5 节说的"两副面孔"。）

第二项 $$e^{-itV/\hbar}$$ 很简单：$$V$$ 是**乘法算子**（乘实函数 $$V(x)$$），于是它的指数也是乘法算子

$$e^{-itV/\hbar}=\text{乘}\ e^{-\frac{i}{\hbar}tV(x)} .$$

（对无界 $$V$$ 由函数演算定义，见第 19 章。）

**定理 3.11（Feynman 路径积分 = Trotter 极限）**。设 $$V$$ 有界且实值。则对 $$f\in L^2(\mathbb R^n)$$ 与 $$t>0$$，

$$\bigl(e^{-itH/\hbar}f\bigr)(x_0)=\lim_{N\to\infty}
\Bigl(\frac{mN}{2\pi i\hbar t}\Bigr)^{\frac{nN}{2}}
\int_{(\mathbb R^n)^{N}}\exp\Bigl\{\frac{i}{\hbar}S_N(x_0,x_1,\dots,x_N)\Bigr\}f(x_N)\,dx_1\cdots dx_N, \tag{3.7}$$

其中

$$S_N(x_0,\dots,x_N)=\sum_{k=1}^{N}\frac{t}{N}\left(\frac{m}{2}\Bigl\lvert\frac{x_k-x_{k-1}}{t/N}\Bigr\rvert^{2}-V(x_{k-1})\right) \tag{3.8}$$

是沿折线 $$x_0\to x_1\to\cdots\to x_N$$ 的**离散作用量**。右端的极限是强极限（对每个 $$f$$ 成立），不是逐点极限。

*证明*：由定理 3.8（有界 $$V$$ 情形由 Kato–Rellich 直接给出本质自伴），

$$e^{-itH/\hbar}f=\lim_{N\to\infty}\Bigl(e^{-\frac{itH_0}{\hbar N}}e^{-\frac{itV}{\hbar N}}\Bigr)^{N}f
\qquad(\text{强极限}).$$

只要把左边每一个因子作用一次的显式积分写出来。记 $$\varepsilon=t/N$$。作用一次：先乘势能相位，再做自由传播，

$$\Bigl(e^{-\frac{itH_0}{\hbar N}}e^{-\frac{itV}{\hbar N}}g\Bigr)(x)
=\Bigl(\frac{m}{2\pi i\hbar\varepsilon}\Bigr)^{n/2}\int_{\mathbb R^n}e^{\frac{im\lvert x-y\rvert^{2}}{2\hbar\varepsilon}}e^{-\frac{i}{\hbar}\varepsilon V(y)}g(y)\,dy$$

（势能因子先作用：$$e^{-i\varepsilon V/\hbar}g$$ 在点 $$y$$ 取 $$e^{-\frac{i}{\hbar}\varepsilon V(y)}g(y)$$；再用定理 3.10，其间换名 $$z=x-y$$）。

现在施加 $$N$$ 次。第一次自变量是 $$f$$，最后一次的结果在 $$x_0$$ 取值。每次作用引进一个积分变量，共 $$N$$ 个，依次记 $$x_1,\dots,x_N$$（第 $$k$$ 次作用的积分变量是 $$x_k$$，先前一次的输出在 $$x_{k-1}$$ 处取值）：

$$\Bigl(\Bigl(e^{-\frac{itH_0}{\hbar N}}e^{-\frac{itV}{\hbar N}}\Bigr)^{N}f\Bigr)(x_0)
=\Bigl(\frac{m}{2\pi i\hbar\varepsilon}\Bigr)^{\frac{nN}{2}}
\int_{(\mathbb R^n)^{N}}\exp\Bigl\{\frac{i}{\hbar}\sum_{k=1}^{N}\Bigl(\frac{m\lvert x_k-x_{k-1}\rvert^{2}}{2\varepsilon}-\varepsilon V(x_{k-1})\Bigr)\Bigr\}f(x_N)\prod_{k=1}^{N}dx_k .$$

把 $$\varepsilon=t/N$$ 代入：系数 $$\frac{m}{2\pi i\hbar\varepsilon}=\frac{mN}{2\pi i\hbar t}$$，给出 $$(3.7)$$ 的前因子；指数上的每一项是

$$\frac{m\lvert x_k-x_{k-1}\rvert^{2}}{2\varepsilon}-\varepsilon V(x_{k-1})
=\frac{t}{N}\left(\frac{m}{2}\Bigl\lvert\frac{x_k-x_{k-1}}{t/N}\Bigr\rvert^{2}-V(x_{k-1})\right),$$

因为 $$\frac{\lvert x_k-x_{k-1}\rvert^{2}}{2\varepsilon}=\frac{1}{2\varepsilon}\lvert x_k-x_{k-1}\rvert^{2}=\frac{\varepsilon}{2}\Bigl\lvert\frac{x_k-x_{k-1}}{\varepsilon}\Bigr\rvert^{2}=\frac{t}{2N}\Bigl\lvert\frac{x_k-x_{k-1}}{t/N}\Bigr\rvert^{2}$$。求和即得 $$(3.8)$$。再对 $$N\to\infty$$ 取强极限即得 $$(3.7)$$。$$\blacksquare$$

**这个极限等于什么？** 先把 $$(3.8)$$ 认出来。把点 $$x_0,\dots,x_N$$ 连成一条折线 $$x(\cdot):[0,t]\to\mathbb R^n$$，在第 $$k$$ 段（时间从 $$\frac{(k-1)t}{N}$$ 到 $$\frac{kt}{N}$$）上速度为 $$\frac{x_k-x_{k-1}}{t/N}$$。于是

$$\frac{m}{2}\Bigl\lvert\frac{x_k-x_{k-1}}{t/N}\Bigr\rvert^{2}$$

是这一段的动能，$$V(x_{k-1})$$ 是这一段的势能，$$\frac{t}{N}$$ 是这一段的时长。所以 $$(3.8)$$ 是

$$L(x,\dot x)=\frac{m}{2}\lvert\dot x\rvert^{2}-V(x) \tag{3.9}$$

沿折线的 **Riemann 和**；$$L$$ 就是 Lagrange 量。当 $$N\to\infty$$ 且折线在合理意义下收敛到一条曲线 $$x(\cdot)$$ 时，

$$S_N\to S[x(\cdot)]=\int_0^{t}\Bigl(\frac{m}{2}\lvert\dot x(s)\rvert^{2}-V(x(s))\Bigr)ds, \tag{3.10}$$

即经典**作用量**。这就是入口题 (d) 的答案。把 $$(3.7)$$ 形式地写成

$$\bigl(e^{-itH/\hbar}f\bigr)(x_0)
\ \text{"="}\ C\int_{\mathcal P}e^{\frac{i}{\hbar}S[x(\cdot)]}f(x(t))\,\mathcal D x(\cdot),
\qquad
\mathcal P=\{x(\cdot):[0,t]\to\mathbb R^n,\ x(0)=x_0\}, \tag{3.11}$$

就是 Feynman 路径积分。

**必须把这句话里的引号讲清楚。** 记号 $$\int_{\mathcal P}\cdots\mathcal D x(\cdot)$$ 里**从来没有过一个测度**，理由三条：其一，$$(3.7)$$ 的右端对每个 $$N$$ 都是老实的 $$nN$$ 维 Lebesgue 积分，而 $$\mathcal P$$ 是无穷维的、其上不存在平移不变的 $$\sigma$$-有限测度；其二，Cameron（1960）证明了即使放弃正性与平移不变性，只要求 $$\sigma$$-可加且使 $$e^{\frac{i}{\hbar}S}$$ 可积，$$(3.11)$$ 也无法实现（那个"测度"会有无穷总变差）；其三，那个看似"归一化常数"、实则依赖 $$N$$ 且趋于无穷的前因子正是"没有测度"的症状（若真有 $$\mathcal D x$$，它就该是常数）。所以 $$(3.11)$$ 的正确读法是：**它是一个算子极限的记号**，而 $$(3.7)$$ 是这个极限的良定义版本。

**虚时间的一侧：那时测度真的存在。** 把 $$t\to-it$$（$$t>0$$）代入 $$(3.11)$$，左端变成压缩半群 $$e^{-tH/\hbar}$$ 的核。逐项验证：热核 $$\bigl(\frac{m}{2\pi\hbar t}\bigr)^{n/2}e^{-\frac{m\lvert x-y\rvert^{2}}{2\hbar t}}$$ 是非负、积分为 $$1$$ 的概率测度，势能因子 $$e^{-\frac{t}{N}V}$$ 在 $$V\ge0$$ 时落在 $$(0,1]$$ 内。于是 $$(3.7)$$ 成为**非负函数的积分**，前因子恰好是 $$N$$ 个概率归一化因子之积，$$N\to\infty$$ 时它们与路径测度合并成一件真东西：Wiener 测度。

**定理 3.12（Feynman–Kac 公式, Feynman–Kac formula）**。设 $$V\ge0$$ 有界。以 $$\{b(s)\}_{s\ge0}$$ 记从 $$b(0)=x$$ 出发的 $$n$$ 维标准布朗运动，其分布是路径空间上的 Wiener 测度 $$\mu_x$$（由 Kolmogorov 延拓定理保证存在），$$\mathbb E_x$$ 为对应的期望。则对 $$f\in L^2(\mathbb R^n)$$ 与 $$t>0$$

$$\bigl(e^{-tH/\hbar}f\bigr)(x)=\mathbb E_x\Bigl[e^{-\frac{1}{\hbar}\int_0^{t}V(b(s))\,ds}f(b(t))\Bigr]. \tag{3.12}$$

*证明*：与定理 3.11 同一条路，只是每一层都换成概率语言的读法。

**有限 $$N$$ 步。** 把 $$[0,t]$$ 等分成 $$N$$ 段（每段 $$\tau=t/N$$），令 $$b$$ 在每段上匀速直线运动，则各段增量 **独立**、服从 $$N\bigl(0,\frac{\hbar\tau}{m}I_n\bigr)$$——因为在 $$(3.7)$$ 的虚时间版本里，密度 $$(m/(2\pi\hbar\tau))^{n/2}e^{-\frac{m\lvert x_k-x_{k-1}\rvert^{2}}{2\hbar\tau}}$$ 给出的正是这个方差（它对应 $$\partial_\tau u=\frac{\hbar}{2m}\Delta u$$，扩散系数 $$\hbar/2m$$）。于是 $$(3.7)$$ 的虚时间版本逐字读成"对分段线性路径取期望"：

$$\bigl(e^{-\frac{tH}{\hbar}}f\bigr)(x)=\lim_{N\to\infty}\mathbb E_x\Bigl[e^{-\frac{1}{\hbar}\sum_{k=1}^{N}\frac{t}{N}V\bigl(b(\tfrac{(k-1)t}{N})\bigr)}f\bigl(b(t)\bigr)\Bigr], \tag{3.13}$$

其中期望对那 $$N$$ 个独立 Gaussian 增量的联合分布取。这一步只是把有限维 Lebesgue 积分改写成概率记号：前因子与 Gaussian 指数合并成密度，积分为 $$1$$。

**取 $$N\to\infty$$。** 按 Kolmogorov 延拓定理在路径空间上构造布朗运动的分布 $$\mu_x$$（有限维分布族相容：增量独立平稳 Gaussian；测度的可数可加性来自延拓定理）。在 $$\mu_x$$ 下几乎所有轨道连续，故

$$\sum_{k=1}^{N}\frac{t}{N}V\bigl(b(\tfrac{(k-1)t}{N})\bigr)\longrightarrow\int_0^{t}V(b(s))ds$$

沿 $$\mu_x$$-几乎所有轨道成立（$$V$$ 有界连续时用 Riemann 和沿连续轨道的收敛）。$$f(b(t))$$ 可积。由控制收敛定理（$$V\ge0$$ 使指数因子被常数 $$1$$ 控制——这正是要 $$V\ge0$$ 的原因），期望收敛到 $$\mathbb E_x\bigl[e^{-\frac1\hbar\int_0^tV(b(s))ds}f(b(t))\bigr]$$。左端是强极限 $$\bigl(e^{-tH/\hbar}f\bigr)(x)$$。合并即得 $$(3.12)$$。$$\blacksquare$$

> **路径积分在实时间下是极限的记号（Trotter 公式），在虚时间下是 Wiener 测度上的积分（Feynman–Kac 公式）；两者由 $$t\mapsto-it$$ 相连。**

**三条线的合流。** 至此可以把这一章与前两章接上。第 21 章的 Stone 定理说：时间演化 $$t\mapsto U(t)$$ 与它的一阶导数（生成元）一一对应，而 $$U(t)$$ 酉、生成元为 $$-iH/\hbar$$、$$H$$ 自伴；本章把这条对应扩成"半群 ↔ 生成元"，覆盖了 Stone 定理（酉群是两侧都有定义的半群，见定理 3.6）。第 22 章的 Stone–von Neumann 定理说：位置与动量的表示在酉等价下唯一。它在这里承担两件事——$$H_0=\frac{P^{2}}{2m}$$ 里 $$P=-i\hbar\nabla$$ 的形状被正则对易关系锁死，于是 $$(3.6)$$ 的核不是"某一种 Fourier 反变换"而是唯一的一种；$$H=H_0+V$$ 的表示没有隐藏自由度，于是路径积分讨论的始终是同一个 $$H$$。本章的 Trotter 公式则说：$$H_0$$ 与 $$V$$ 分别能写成核，而它们乘积的极限恢复 $$e^{-itH/\hbar}$$。

三句话合起来给出路径积分的**严格身份**：它是**自伴算子 $$H$$（由 Stone 定理）生成的时间演化，用 Trotter 公式把 $$H_0$$ 与 $$V$$ 拆成两步、取强极限**得到的对象。它不含新的公理，也不含新的测度；只是"无界算子的指数"在位置表示下的展开。

## 四、几何与物理直觉 (Intuition)

**一、时间的方向画在谱上。** 半群与群的区别是**可逆性**，而在算子侧，可逆性被翻译成生成元的谱落在哪里：生成元**反自伴**（$$\sigma(B)\subset i\mathbb R$$）$$\Rightarrow$$ $$e^{tB}$$ 是酉群，两侧有定义、信息不丢，这描述**波**；生成元**自伴半正定**（$$\sigma(A)\subset[0,\infty)$$）$$\Rightarrow$$ $$e^{-tA}$$ 是压缩半群，$$t<0$$ 一侧不存在，这描述**扩散**。几何图景：热核是宽度 $$\sim\sqrt t$$ 的一团，$$t\to0^{+}$$ 缩成一点、$$t\to\infty$$ 摊平，而摊平不可逆——倒放要求把无穷远的信息精确收回。判据不在核的公式里，在生成元的自伴性里。

**二、生成元是单位元处的切向量。** 把 $$t\mapsto T(t)$$ 看成过 $$I$$ 的曲线，$$A=\lim_{t\to0^{+}}\frac{T(t)-I}{t}$$ 是它在 $$I$$ 处的**切向量**；于是 $$A\mapsto e^{tA}$$ 是"切向量 → 曲线"的**指数映射**，(S2) 是曲线的群律，定理 3.2(iii) 说"曲线每一点的切向量都是 $$A$$ 的搬运"。这套语言不必限于算子：换成有限维结合代数就是矩阵 Lie 群的指数映射，换成流形上的向量场就是流。第 24 章把它展开成一般的 Lie 群与 Lie 代数，本章已搭好半步——**生成元集合在对易子下封闭**（定理 3.7 里的 $$[A,B]$$ 就是"两个生成元的乘积之差"），这正是 Lie 代数那条公理的来源。

**三、路径空间上为什么没有测度。** $$(3.11)$$ 的 $$\mathcal P$$ 是无穷维的，而**无穷维空间上不存在平移不变的 $$\sigma$$-有限测度**：若 $$\mu$$ 平移不变并把某个球测成有限正数，就能塞进无穷多个两两不交的等大球（并的测度是 $$\infty$$），而整个空间又能被有限多个这样的球盖住，矛盾。替代品有二：**有限维截断**（$$(3.7)$$ 的右端对每个 $$N$$ 都是老实的 $$nN$$ 维 Lebesgue 积分，"路径积分"是这样一串积分的强极限）与 **Wiener 测度**（时间转到虚轴，增量变成独立高斯，Kolmogorov 延拓给出真正的路径测度，代价是 $$e^{iS/\hbar}$$ 变成 $$e^{-S_E/\hbar}$$）。

**四、三线对应。**

| 数学对象 | 物理名称 | 出现处 |
|---|---|---|
| 压缩半群 $$e^{-tH}$$ | 虚时间（欧氏）演化 | 热方程、Feynman–Kac |
| 酉群 $$e^{-itH/\hbar}$$ | 实时间（Minkowski）演化 | Schrödinger 方程 |
| $$t\mapsto-it$$ | Wick 转动 | 欧氏 ↔ Minkowski |
| $$e^{-itH_0/\hbar}$$ 的核 | 自由传播子 | 定理 3.10 |
| 定理 3.8 的极限 | 路径积分的严格内容 | QFT 的出发点 |
| $$S[x(\cdot)]$$ | 作用量 | 经典极限 $$\hbar\to0$$ 时相位驻定 |

几何侧是路径空间与无穷维测度的缺席，物理侧是时间演化与传播子，代数侧是生成元与对易子。三条线在 Trotter 公式里合流：$$e^{-itH/\hbar}$$ 由几何对象（路径与作用量）的极限逼近，误差由代数量（对易子）控制。**量子力学的公理层面在前面三章已说完，路径积分只是同一些内容在另一组坐标下的写法。**

## 五、经典问题精讲 (Classical Problems)

本节三题，按"从显式计算到概念对照"排序。每题给出完整解答，并标注它在第三节结构里的位置。

### 经典问题 5.1（热核的卷积与自由路径积分）

**考点**：定理 3.10、定理 3.11 在 $$V=0$$ 的退化情形。
**位置**：$$(3.7)$$ 的最简检验——$$V=0$$ 时它必须退化成 $$(3.6)$$。

设 $$G_t(x)=\bigl(\frac{\lambda}{\pi t}\bigr)^{n/2}e^{-\lambda\lvert x\rvert^{2}/t}$$（$$\lambda>0$$ 是参数）。**(a)** 证明 $$G_s*G_t=G_{s+t}$$。**(b)** 取 $$\lambda=\frac{m}{2\hbar}$$，说明 $$G_t$$ 与 $$(3.6)$$ 的虚时间版本一致，并说明 $$(3.7)$$ 在 $$V=0$$ 时右端的 $$N$$ 重积分恰好给出 $$e^{-itH_0/\hbar}f$$。

**解** **(a)** 记 $$\hat f(k)=(2\pi)^{-n/2}\int f(x)e^{-ik\cdot x}dx$$。把 $$n$$ 维积分按坐标分解为 $$n$$ 个一维积分，用标准高斯积分 $$\int_{\mathbb R}e^{-ax^{2}}e^{-ikx}dx=\sqrt{\pi/a}\,e^{-k^{2}/4a}$$（$$\operatorname{Re}a>0$$，此处 $$a=\lambda/t>0$$）得

$$\widehat{G_t}(k)=\Bigl(\frac{\lambda}{\pi t}\Bigr)^{n/2}\int_{\mathbb R^n}e^{-\frac{\lambda\lvert x\rvert^{2}}{t}}e^{-ik\cdot x}dx=e^{-\frac{t\lvert k\rvert^{2}}{4\lambda}} .$$

卷积在 Fourier 侧逐点相乘（Fubini 定理：$$G_s,G_t\in L^1$$，两重积分绝对收敛），故

$$\widehat{G_s*G_t}(k)=e^{-\frac{s\lvert k\rvert^{2}}{4\lambda}}e^{-\frac{t\lvert k\rvert^{2}}{4\lambda}}=e^{-\frac{(s+t)\lvert k\rvert^{2}}{4\lambda}}=\widehat{G_{s+t}}(k),$$

再由 Fourier 变换在 $$L^2$$ 上的单射性（Plancherel）与两侧的连续性，得 $$G_s*G_t=G_{s+t}$$ 处处。

这同时说明 $$\{G_t\}$$ 在卷积下是半群，且它就是热半群：对 $$\lambda=\frac{m}{2\hbar}$$，

$$G_t(x)=\Bigl(\frac{m}{2\pi\hbar t}\Bigr)^{n/2}e^{-\frac{m\lvert x\rvert^{2}}{2\hbar t}},$$

与定理 3.10 之后那条虚时间替换给出的核逐字相同。

**(b)** 对 $$V=0$$，$$(3.7)$$ 的右端是

$$\Bigl(\frac{mN}{2\pi i\hbar t}\Bigr)^{\frac{nN}{2}}\int_{(\mathbb R^n)^{N}}\exp\Bigl\{\frac{imN}{2\hbar t}\sum_{k=1}^{N}\lvert x_k-x_{k-1}\rvert^{2}\Bigr\}f(x_N)\prod_{k=1}^{N}dx_k$$

（用了 $$\frac{t}{N}\cdot\frac{m}{2(t/N)^{2}}=\frac{mN}{2t}$$）。逐个做掉这 $$N$$ 次积分，每次都是一次 $$n$$ 维高斯卷积，其核为 $$\bigl(\frac{mN}{2\pi i\hbar t}\bigr)^{n/2}e^{\frac{imN\lvert z\rvert^{2}}{2\hbar t}}$$——这正是 $$(3.6)$$ 的核把 $$t$$ 换成 $$t/N$$ 的结果，即 $$e^{-\frac{i(t/N)H_0}{\hbar}}$$ 的核。由 (a) 的半群律（虚时间版本逐字适用：乘子 $$e^{-\frac{i\hbar(t/N)\lvert k\rvert^{2}}{2m}}$$ 的 $$N$$ 次乘积给出 $$e^{-\frac{i\hbar t\lvert k\rvert^{2}}{2m}}$$），结果是 $$e^{-\frac{itH_0}{\hbar}}$$ 的核 $$\bigl(\frac{m}{2\pi i\hbar t}\bigr)^{n/2}e^{\frac{im\lvert z\rvert^{2}}{2\hbar t}}$$。故左端恰等于 $$e^{-itH_0/\hbar}f$$，与 $$(3.7)$$（代入 $$H=H_0$$）一致。**这是 $$V=0$$ 时 $$(3.7)$$ 的独立验证。**

### 经典问题 5.2（平移酉群的生成元）

**考点**：定义 3.2、定理 3.6 与"实轴 / 虚轴"判别法。
**位置**：3.1 节的第三个例子，也是"生成元无界闭"的最干净实例。

在 $$X=L^2(\mathbb R)$$ 上取 $$(T(t)f)(x)=f(x+t)$$，$$t\in\mathbb R$$。**(a)** 证明 $$T(t)$$ 是酉算子、$$\{T(t)\}_{t\in\mathbb R}$$ 是单参数酉群。**(b)** 证明它的生成元是 $$A=\frac{d}{dx}$$，定义域 $$H^{1}(\mathbb R)$$。**(c)** 由 $$A$$ 的谱说明 $$T(t)$$ 为什么是酉群而不是压缩半群。

**解** **(a)** 保范由 Lebesgue 测度的平移不变性给出：

$$\lVert T(t)f\rVert_2^{2}=\int_{\mathbb R}\lvert f(x+t)\rvert^{2}dx=\int_{\mathbb R}\lvert f(y)\rvert^{2}dy=\lVert f\rVert_2^{2}.$$

满射：给定 $$g\in L^2$$，取 $$f(x)=g(x-t)\in L^2$$，则 $$T(t)f=g$$。故 $$T(t)$$ 是等距满射，是酉算子，逆为 $$T(-t)$$。群律 $$T(s)T(t)=T(s+t)$$ 由复合直接验证，$$T(0)=I$$。强连续性：对连续紧支的 $$f$$，由一致连续，

$$\lVert T(t)f-f\rVert_2^{2}=\int_{\mathbb R}\lvert f(x+t)-f(x)\rvert^{2}dx\to0\qquad(t\to0),$$

（把积分限制在 $$f$$ 与平移后 $$f$$ 的支集的并的紧包里，对小的 $$\lvert t\rvert$$ 一致控住被积函数）。再用连续紧支函数在 $$L^2$$ 中的稠密性与 $$\lVert T(t)\rVert=1$$ 做 $$3\varepsilon$$ 论证，得到对一切 $$f\in L^2$$ 成立。

**(b)** 对 $$f\in H^1(\mathbb R)$$（即 $$f'\in L^2$$），在 Fourier 侧算差商。记 $$\hat f(k)=(2\pi)^{-1/2}\int f(x)e^{-ikx}dx$$，则

$$\widehat{T(t)f}(k)=(2\pi)^{-1/2}\int f(x+t)e^{-ikx}dx=(2\pi)^{-1/2}\int f(y)e^{-ik(y-t)}dy=e^{ikt}\hat f(k),$$

于是

$$\widehat{\frac{T(t)f-f}{t}}(k)=\frac{e^{ikt}-1}{t}\hat f(k).$$

对每个固定的 $$k$$，$$\frac{e^{ikt}-1}{t}\to ik$$（$$t\to0$$），且

$$\Bigl\lvert\frac{e^{ikt}-1}{t}\Bigr\rvert=\Bigl\lvert\frac{1}{t}\int_0^{t}ik\,e^{iks}ds\Bigr\rvert\le\lvert k\rvert .$$

由 $$ik\hat f(k)=\widehat{f'}(k)\in L^2$$（这就是 $$f\in H^1$$ 的含义），用控制收敛定理：逐点收敛已得，被控函数 $$\lvert k\rvert\lvert\hat f(k)\rvert$$ 的平方可积，故

$$\Bigl\lVert\frac{T(t)f-f}{t}-\widehat{f'}\Bigr\rVert_{L^2}^{2}
=\int_{\mathbb R}\Bigl\lvert\frac{e^{ikt}-1}{t}-ik\Bigr\rvert^{2}\lvert\hat f(k)\rvert^{2}dk\to0,$$

在积分号下取极限的合法性由被控函数 $$(2\lvert k\rvert)^{2}\lvert\hat f(k)\rvert^{2}=4\lvert k\rvert^{2}\lvert\hat f(k)\rvert^{2}\in L^1$$ 给出。换算回位置空间：$$\frac{T(t)f-f}{t}\to f'$$ 于 $$L^2$$。故 $$f\in D(A)$$、$$Af=f'$$。

反之，若差商在 $$L^2$$ 中收敛到某 $$g$$，取 $$\varphi\in C_c^\infty(\mathbb R)$$，把 $$\int_{\mathbb R}\frac{f(x+t)-f(x)}{t}\varphi(x)dx$$ 换元 $$y=x+t$$ 化为 $$\int_{\mathbb R}f(y)\frac{\varphi(y-t)-\varphi(y)}{t}dy$$。当 $$t\to0$$ 时 $$\frac{\varphi(y-t)-\varphi(y)}{t}\to-\varphi'(y)$$ 在紧支集上一致，故该积分趋于 $$-\int f\varphi'=\int f'\varphi$$（分布意义），于是 $$g=f'$$（分布意义）且 $$g\in L^2$$，即 $$f\in H^1$$。故 $$D(A)=H^1(\mathbb R)$$、$$A=\frac{d}{dx}$$。

**(c)** 由 (b)，在 Fourier 侧 $$A$$ 是乘子 $$ik$$：$$\widehat{Af}(k)=ik\hat f(k)$$，故

$$\sigma(A)=\overline{\{ik\}}=\,i\mathbb R .$$

$$A$$ 的谱整个落在虚轴上，即 $$A^{*}=-A$$（Fourier 侧 $$ik$$ 纯虚，共轭后变号）。由定理 3.6 的接驳，反自伴生成元的指数必是酉群：$$e^{-itA}$$ 每层模为 $$1$$ 故保范，而满射性由乘子 $$e^{ikt}$$ 的模处处为 $$1$$（可逐点相除）保证。反过来，不可逆的压缩半群（如热半群）其生成元谱必须落在 $$\operatorname{Re}\lambda\le0$$ 的闭半平面里：$$H_0\ge0$$ 时 $$\sigma(-H_0)\subset(-\infty,0]$$ 是负实轴。**实轴对应扩散、虚轴对应波，判据就是生成元的自伴性。**

### 经典问题 5.3（Lie 乘积公式的数值验证）

**考点**：定理 3.7 的误差项 (3.5)。
**位置**：入口题 (c) 的完整算账，兼验定理 3.7 的常数估计。

取 $$A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$$、$$B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$$。**(a)** 算出 $$[A,B]$$ 与 $$AB$$。**(b)** 直接写出 $$I+M:=e^{A/m}e^{B/m}$$，说明 $$M=\frac{A+B}{m}+\frac{AB}{m^{2}}$$ 恰好精确（没有更高阶项）。**(c)** 用特征值算出 $$\lim_{m\to\infty}(I+M)^{m}$$，与 $$e^{A+B}$$ 对照。

**解** **(a)** $$AB=\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}0&0\\1&0\end{pmatrix}=\begin{pmatrix}1&0\\0&0\end{pmatrix}$$，$$BA=\begin{pmatrix}0&0\\1&0\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix}=\begin{pmatrix}0&0\\0&1\end{pmatrix}$$，故

$$[A,B]=AB-BA=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad A^{2}=B^{2}=0 .$$

**(b)** 因为 $$A^{2}=B^{2}=0$$，指数级数在第 $$2$$ 项截断：$$e^{A/m}=I+\frac{A}{m}$$、$$e^{B/m}=I+\frac{B}{m}$$。相乘：

$$e^{A/m}e^{B/m}=I+\frac{A+B}{m}+\frac{AB}{m^{2}} .$$

这一步**精确**，没有 $$m^{-3}$$ 项，因为 $$A^{2}=B^{2}=0$$ 让所有更高阶项消失。这与 (3.5) 对照：一般情形里二阶差是 $$\frac{1}{2m^{2}}[A,B]$$，而 $$e^{(A+B)/m}$$ 的二阶项是 $$\frac{(A+B)^{2}}{2m^{2}}=\frac{AB+BA}{2m^{2}}$$（$$A^{2}=B^{2}=0$$），故

$$e^{A/m}e^{B/m}-e^{(A+B)/m}=\frac{AB}{m^{2}}-\frac{AB+BA}{2m^{2}}=\frac{[A,B]}{2m^{2}},$$

与 (3.5) 一致，且这里三阶余项确实为零。

**(c)** 记 $$I+M=\begin{pmatrix}1+\frac{1}{m^{2}}&\frac{1}{m}\\[2pt]\frac{1}{m}&1\end{pmatrix}$$。它的迹与行列式：

$$\operatorname{tr}(I+M)=2+\frac{1}{m^{2}},\qquad
\det(I+M)=\Bigl(1+\frac1{m^{2}}\Bigr)-\frac{1}{m^{2}}=1 .$$

特征值是 $$\mu_{\pm}=\frac{1}{2}\Bigl[\bigl(2+\frac{1}{m^{2}}\bigr)\pm\sqrt{\bigl(2+\frac{1}{m^{2}}\bigr)^{2}-4}\Bigr]$$。化简根号内：

$$\Bigl(2+\frac1{m^{2}}\Bigr)^{2}-4=\frac{4}{m^{2}}+\frac{1}{m^{4}}=\frac{1}{m^{2}}\Bigl(4+\frac{1}{m^{2}}\Bigr),\qquad
\sqrt{\cdot}=\frac{1}{m}\sqrt{4+\frac{1}{m^{2}}} .$$

于是（$$m>0$$）

$$\mu_{\pm}=1+\frac{1}{2m^{2}}\pm\frac{1}{2m}\sqrt{4+\frac{1}{m^{2}}} .$$

取 $$m$$ 次幂。用 $$\sqrt{4+m^{-2}}=2+O(m^{-2})$$：

$$\mu_{+}=1+\frac{1}{m}+O(m^{-2}),\qquad \mu_{-}=1-\frac{1}{m}+O(m^{-2}) .$$

对第一个取对数（$$\ln(1+u)=u-u^{2}/2+O(u^{3})$$，$$u=\frac1m+O(m^{-2})$$）：

$$\ln\mu_+=\frac{1}{m}+O(m^{-2})-\frac{1}{2}\Bigl(\frac{1}{m}+O(m^{-2})\Bigr)^{2}=\frac{1}{m}-\frac{1}{2m^{2}}+O(m^{-3}),$$

故 $$\mu_+^{m}=\exp\bigl[m\ln\mu_+\bigr]=\exp\bigl[1-\frac{1}{2m}+O(m^{-2})\bigr]\to e$$。同理

$$\ln\mu_-=-\frac{1}{m}-\frac{1}{2m^{2}}+O(m^{-3}),\qquad \mu_-^{m}=\exp\bigl[-1-\frac{1}{2m}+O(m^{-2})\bigr]\to e^{-1}.$$

$$(I+M)^m$$ 的特征值趋于 $$e$$ 与 $$e^{-1}$$，特征向量是 $$\frac{1}{\sqrt2}(1,1)^{\mathsf T}$$ 与 $$\frac{1}{\sqrt2}(1,-1)^{\mathsf T}$$（两个特征向量与 $$m$$ 无关，因为 $$I+M$$ 的两个非对角元相等、对角元之差是 $$\frac1{m^{2}}$$ 的高阶——直接验证 $$(I+M)(1,1)^{\mathsf T}=(1+\frac1m+\frac1{m^{2}})(1,1)^{\mathsf T}$$、$$(I+M)(1,-1)^{\mathsf T}=(1-\frac1m+\frac1{m^{2}})(1,-1)^{\mathsf T}$$，这两个恰好就是 $$\mu_\pm$$ 的精确值）。故

$$\lim_{m\to\infty}(I+M)^{m}
=\frac{e}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}+\frac{e^{-1}}{2}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
=\begin{pmatrix}\cosh 1&\sinh 1\\ \sinh 1&\cosh 1\end{pmatrix}.$$

对照 $$e^{A+B}$$：$$A+B=\begin{pmatrix}0&1\\1&0\end{pmatrix}=\sigma_x$$ 满足 $$\sigma_x^{2}=I$$，故

$$e^{A+B}=\sum_{k\ \text{偶}}\frac{I}{k!}+\sum_{k\ \text{奇}}\frac{\sigma_x}{k!}=\cosh(1)\,I+\sinh(1)\,\sigma_x=\begin{pmatrix}\cosh1&\sinh1\\ \sinh1&\cosh1\end{pmatrix},$$

完全一致。**数值上**取 $$m=100$$：$$\mu_+^{100}=e^{1-0.005+O(10^{-4})}\approx2.704$$，与 $$e=2.718$$ 差 $$0.014$$，而定理 3.7 的常数估计给上界 $$\frac{\lVert[A,B]\rVert}{2\cdot100}e^{\lVert A\rVert+\lVert B\rVert}=\frac1{200}e^{2}\approx0.037$$（$$[A,B]=\operatorname{diag}(1,-1)$$，$$\lVert[A,B]\rVert=1$$），把 $$0.014$$ 控住；误差按 $$1/m$$ 压下去，与"(3.5) 的 $$1/m^{2}$$ 二阶差乘上 $$m$$ 次幂得 $$1/m$$"吻合。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 设 $$X$$ 是 Banach 空间、$$A\in\mathcal B(X)$$、$$T(t)=e^{tA}$$。逐条验证 (S1)(S2)(S3)，并证明 $$\lVert T(t)\rVert\le e^{t\lVert A\rVert}$$。

**基2.** 在 $$L^2(\mathbb R^n)$$ 上取 $$H_0=-\Delta$$。证明 $$\lVert e^{-tH_0}\rVert=1$$（$$t\ge0$$），并证明 $$e^{-tH_0}$$ 不是满射。

**基3.** 在 $$\ell^2=\ell^2(\mathbb N)$$ 上取对角算子 $$A(x_1,x_2,x_3,\dots)=(-x_1,-2x_2,-3x_3,\dots)$$。用定理 3.3 算出 $$R(\lambda,A)$$（$$\lambda>0$$），验证 $$\lVert R(\lambda,A)\rVert\le1/\lambda$$，并验证 $$\lambda R(\lambda,A)\to I$$ 强收敛但**不**范数收敛。

### 竞赛（本课目标难度）

**竞1.** 设 $$A,B,C\in\mathbb C^{n\times n}$$。证明

$$\lim_{m\to\infty}\Bigl(e^{A/m}e^{B/m}e^{C/m}\Bigr)^{m}=e^{A+B+C},$$

并算出 $$e^{A/m}e^{B/m}e^{C/m}$$ 与 $$e^{(A+B+C)/m}$$ 的 $$\dfrac{1}{m^{2}}$$ 阶差是什么。

**竞2.** 在 $$L^2(\mathbb R)$$ 上取 $$(T(t)f)(x)=e^{-t}f(x+t)$$，$$t\ge0$$。证明它是强连续压缩半群，求出它的生成元与谱，并说明它为什么是压缩半群而不是酉群。

**竞3.** 设 $$A$$ 是闭稠定算子，$$\lambda,\mu\in\rho(A)$$。
(i) 证明预解恒等式 $$R(\lambda,A)-R(\mu,A)=(\mu-\lambda)R(\lambda,A)R(\mu,A)$$；
(ii) 证明 $$R(\lambda,A)R(\mu,A)=R(\mu,A)R(\lambda,A)$$；
(iii) 证明 $$\dfrac{d}{d\lambda}R(\lambda,A)=-R(\lambda,A)^{2}$$，并推出 $$R(\cdot,A):\rho(A)\to\mathcal B(X)$$ 是解析函数。

**竞4.**（Strang 对称拆分）设 $$A,B\in\mathbb C^{n\times n}$$。证明

$$\lim_{m\to\infty}\Bigl(e^{A/2m}\,e^{B/m}\,e^{A/2m}\Bigr)^{m}=e^{A+B},$$

并且这一次 $$e^{A/2m}e^{B/m}e^{A/2m}$$ 与 $$e^{(A+B)/m}$$ 的差是 $$O(m^{-3})$$，从而误差按 $$1/m^{2}$$ 而不是 $$1/m$$ 衰减。

### 研究（通向下一章）

**研1.**（Feynman–Kac 的 $$N$$ 步构造）设 $$V\ge0$$ 有界连续，$$H=-\dfrac{\hbar^{2}}{2m}\Delta+V$$。用 $$(3.7)$$ 的虚时间版本，逐项完成定理 3.12 的证明：说明 $$N$$ 步截断的期望可以写成 Wiener 测度下一次积分的逼近，并解释为什么"实时间版本"（即 $$(3.11)$$）没有对应的 $$N$$ 步测度。

**研2.**（生成元、对易子与 Lie 代数）设 $$\mathfrak g$$ 是一个有限维实向量空间，$$\{A_1,\dots,A_n\}$$ 是它的一组基，且每个 $$A_j$$ 是 Hilbert 空间 $$H$$ 上的反自伴算子，并设 $$H$$ 上有一个由这些算子生成的单参数酉群 $$\{U_j(t)=e^{tA_j}\}$$。设所有这些群的乘积（任意顺序、任意有限次）在复合下构成群 $$G$$。
(i) 证明 $$[A_j,A_k]$$ 仍落在所有 $$A_j$$ 张成的线性空间中（即该线性空间在对易子下封闭）；
(ii) 由此说明 $$\mathfrak g$$ 是一个 Lie 代数，且 $$e^{\mathfrak g}$$ 给出的元素属于 $$G$$；
(iii) 说明本章的 $$[A,B]$$ 与第 22 章的正则对易关系 $$[Q_j,P_k]=i\hbar\delta_{jk}$$ 是同一件事的两个实例。

### 解答 (Solutions)

**解 基1.** 三件事逐条来。

**级数收敛。** $$\lVert\sum_{k=0}^{K}\frac{t^{k}A^{k}}{k!}\rVert\le\sum_{k=0}^{K}\frac{\lvert t\rvert^{k}\lVert A\rVert^{k}}{k!}\le e^{\lvert t\rvert\lVert A\rVert}<\infty$$，故部分和在 $$\mathcal B(X)$$（完备）中 Cauchy、收敛；且 $$\lVert T(t)\rVert\le e^{\lvert t\rvert\lVert A\rVert}$$，$$t\ge0$$ 时即所要的界。这一步同时表明 $$T(t)$$ 有定义且 $$\lVert T(t)-I\rVert\le e^{t\lVert A\rVert}-1$$。

**(S1)** 级数在 $$t=0$$ 处只剩 $$k=0$$ 项：$$T(0)=A^{0}=I$$。

**(S2)** 两个级数都绝对收敛，Cauchy 乘积可按任意方式重排：

$$T(s)T(t)=\sum_{n\ge0}A^{n}\sum_{j+k=n}\frac{s^{j}t^{k}}{j!k!}
=\sum_{n\ge0}\frac{A^{n}}{n!}\sum_{j+k=n}\binom{n}{j}s^{j}t^{k}
=\sum_{n\ge0}\frac{(s+t)^{n}A^{n}}{n!}=T(s+t),$$

倒数第二步用二项式定理。这一步把 $$A^{j}A^{k}=A^{j+k}=A^{n}$$ 提到求和号外是合法的（$$A$$ 与自己的幂全部可交换），这正是这个例子不需要 Trotter 公式的原因。

**(S3)** $$\lVert T(t)x-x\rVert\le\lVert T(t)-I\rVert\lVert x\rVert\le(e^{t\lVert A\rVert}-1)\lVert x\rVert\to0$$（$$t\to0^{+}$$），故强连续。$$\blacksquare$$

**解 基2.** 由 Fourier 变换（归一化同定理 3.10 的证明），$$H_0=-\Delta$$ 在 Fourier 侧是乘子 $$\lvert k\rvert^{2}$$，故 $$\widehat{e^{-tH_0}f}(k)=e^{-t\lvert k\rvert^{2}}\hat f(k)$$。

**范数。** 由 Plancherel 与 $$e^{-2t\lvert k\rvert^{2}}\le1$$，$$\lVert e^{-tH_0}f\rVert_2\le\lVert f\rVert_2$$，即 $$\lVert e^{-tH_0}\rVert\le1$$。反向：对 $$\varepsilon>0$$ 取 $$\hat f=\chi_{\{\lvert k\rvert<\varepsilon\}}\in L^2$$，在 $$\lvert k\rvert<\varepsilon$$ 上 $$e^{-2t\lvert k\rvert^{2}}\ge e^{-2t\varepsilon^{2}}$$，故

$$\lVert e^{-tH_0}\rVert\ge e^{-t\varepsilon^{2}}\ \xrightarrow[\varepsilon\to0]{}\ 1 .$$

合起来 $$\lVert e^{-tH_0}\rVert=1$$。

**不满射。** $$e^{-tH_0}f=g$$ 在 Fourier 侧等价于 $$\hat f(k)=e^{t\lvert k\rvert^{2}}\hat g(k)$$，故必须 $$e^{t\lvert k\rvert^{2}}\hat g\in L^2$$。取 $$n=1$$、$$\hat g(k)=e^{-\lvert k\rvert}\in L^2$$，则

$$\int_{\mathbb R}e^{2t\lvert k\rvert^{2}}e^{-2\lvert k\rvert}dk=\infty$$

（被积函数的指数是 $$2tk^{2}-2\lvert k\rvert\to+\infty$$），故这个 $$g$$ 不在 $$e^{-tH_0}$$ 的值域中。值域是 $$L^2$$ 的真稠密子空间（稠密：把 $$\hat g$$ 的高频截断后，$$e^{-t\lvert k\rvert^{2}}\hat f$$ 可以任意逼近 $$\hat g$$）。**不可逆性在这里已经显形。** $$\blacksquare$$

**解 基3.** $$A$$ 是乘子：在 $$\ell^2$$ 的标准基上 $$Ae_j=-je_j$$。

由定理 3.3，对 $$\lambda>0$$ 与 $$x=(x_j)\in\ell^2$$，

$$R(\lambda,A)x=\int_0^\infty e^{-\lambda t}e^{tA}x\,dt
=\int_0^\infty e^{-\lambda t}\bigl(e^{-jt}x_j\bigr)_j dt
=\Bigl(\frac{x_j}{\lambda+j}\Bigr)_j .$$

（交换积分与分量合法：$$\lVert e^{tA}x\rVert\le\lVert x\rVert$$ 给出整体可控。）于是 $$R(\lambda,A)$$ 是乘子 $$\bigl(\frac{1}{\lambda+j}\bigr)_{j\in\mathbb N}$$，其范数是乘子序列的上确界：

$$\lVert R(\lambda,A)\rVert=\sup_{j\ge1}\frac{1}{\lambda+j}=\frac{1}{\lambda+1}\le\frac1\lambda .$$

这就是定理 3.4 的界（此处严格取不到等号：谱在 $$-\mathbb N$$ 上，正实轴到它有正距离 $$1$$）。

**强收敛。** $$\lambda R(\lambda,A)x=\bigl(\frac{\lambda}{\lambda+j}x_j\bigr)_j$$，逐分量趋于 $$x_j$$ 且一致有界（$$\le1$$），故由控制收敛（对计数测度）

$$\lVert\lambda R(\lambda,A)x-x\rVert^{2}=\sum_{j\ge1}\Bigl(\frac{j}{\lambda+j}\Bigr)^{2}\lvert x_j\rvert^{2}\to0 .$$

**不是范数收敛。** $$\lambda R(\lambda,A)-I$$ 是对角乘子 $$\frac{-j}{\lambda+j}$$，其范数是 $$\sup_j\frac{j}{\lambda+j}=1$$（$$j\to\infty$$ 时趋 $$1$$），故

$$\lVert\lambda R(\lambda,A)-I\rVert=1\qquad\text{对一切}\ \lambda>0,$$

不趋于 $$0$$。**强收敛与范数收敛在这里的差别，正是"生成元无界"的症状：$$\lambda R(\lambda,A)$$ 逐向量趋于恒等，但把空间里越来越高的分量一起看时，它始终"差一个单位"。** $$\blacksquare$$

**解 竞1.** **关键 leap**：把定理 3.7 的展开从两个因子推到三个因子，并看出二阶差是三个对易子的和的一半。

记 $$\varepsilon=1/m$$，$$T=e^{\varepsilon A}e^{\varepsilon B}e^{\varepsilon C}$$、$$S=e^{\varepsilon(A+B+C)}$$。

**第一步，展开 $$T$$。** 每个因子按余项展开（$$\rho_A=O(\varepsilon^{3})$$ 同定理 3.7 的证明）：

$$e^{\varepsilon A}=I+\varepsilon A+\frac{\varepsilon^{2}A^{2}}{2}+\rho_A .$$

先乘前两个（丢弃 $$\varepsilon^{3}$$ 及以上）：

$$e^{\varepsilon A}e^{\varepsilon B}=I+\varepsilon(A+B)+\frac{\varepsilon^{2}}2\bigl(A^{2}+2AB+B^{2}\bigr)+O(\varepsilon^{3}) .$$

再乘第三个。记 $$P=A+B$$、$$Q=\frac12(A^{2}+2AB+B^{2})$$，则

$$T=\Bigl(I+\varepsilon P+\varepsilon^{2}Q+O(\varepsilon^{3})\Bigr)\Bigl(I+\varepsilon C+\frac{\varepsilon^{2}C^{2}}2+O(\varepsilon^{3})\Bigr)
=I+\varepsilon(P+C)+\varepsilon^{2}\Bigl(Q+PC+\frac{C^{2}}2\Bigr)+O(\varepsilon^{3}).$$

算出 $$Q+PC+\frac{C^{2}}2$$：

$$Q+PC+\frac{C^{2}}2=\frac{A^{2}}2+AB+\frac{B^{2}}2+(A+B)C+\frac{C^{2}}2
=\frac{A^{2}}2+AB+AC+\frac{B^{2}}2+BC+\frac{C^{2}}2 .$$

**第二步，展开 $$S$$。**

$$S=I+\varepsilon(A+B+C)+\frac{\varepsilon^{2}}2(A+B+C)^{2}+O(\varepsilon^{3}),$$

而

$$(A+B+C)^{2}=A^{2}+B^{2}+C^{2}+AB+BA+AC+CA+BC+CB .$$

**第三步，相减。** 一阶项相同，二阶差是

$$T-S=\varepsilon^{2}\Bigl[\underbrace{\Bigl(AB-\frac{AB+BA}2\Bigr)}_{=\frac12[A,B]}+\underbrace{\Bigl(AC-\frac{AC+CA}2\Bigr)}_{=\frac12[A,C]}+\underbrace{\Bigl(BC-\frac{BC+CB}2\Bigr)}_{=\frac12[B,C]}\Bigr]+O(\varepsilon^{3})
=\frac{\varepsilon^{2}}2\Bigl([A,B]+[A,C]+[B,C]\Bigr)+O(\varepsilon^{3}).$$

（$$A^{2},B^{2},C^{2}$$ 的系数是 $$\frac12$$，两边相同，抵消。）**这就是所求的 $$\frac{1}{m^{2}}$$ 阶差。**

**第四步，取 $$m$$ 次幂。** 与定理 3.7 的第二步完全相同：由 $$T^{m}-S^{m}=\sum_{k=0}^{m-1}T^{k}(T-S)S^{m-1-k}$$、$$\lVert T\rVert,\lVert S\rVert\le e^{\lVert A\rVert+\lVert B\rVert+\lVert C\rVert}$$（$$m\varepsilon=1$$ 时的一阶界）与第三步，

$$\lVert T^{m}-S^{m}\rVert\le m\cdot e^{\lVert A\rVert+\lVert B\rVert+\lVert C\rVert}\cdot\frac{\varepsilon^{2}}2\bigl\lVert[A,B]+[A,C]+[B,C]\bigr\rVert
=\frac{\lVert\cdot\rVert}{2m}e^{\lVert A\rVert+\lVert B\rVert+\lVert C\rVert}\to0,$$

因为 $$m\varepsilon^{2}=1/m$$。而 $$S^{m}=\bigl(e^{\varepsilon(A+B+C)}\bigr)^{m}=e^{A+B+C}$$，故 $$\lim_mT^{m}=e^{A+B+C}$$。$$\blacksquare$$

**解 竞2.** **关键 leap**：把这个半群写成"平移群乘上一个纯衰减"，于是生成元就是两个部分的和——平移部分给虚轴上的谱，衰减部分给实轴上的谱。

**半群公理。** 半群律、$$T(0)=I$$ 见 3.1 节的第三个例子。压缩性：$$\lVert T(t)\rVert=e^{-t}\le1$$。强连续：$$\lVert T(t)f-f\rVert_2\le e^{-t}\lVert f(\cdot+t)-f\rVert_2+(e^{-t}-1)\lVert f\rVert_2\to0$$（第一项由经典问题 5.2 的平移强连续，第二项由 $$e^{-t}\to1$$）。故它是强连续压缩半群。

**生成元。** 对 $$f\in H^{1}(\mathbb R)$$，在 Fourier 侧

$$\widehat{T(t)f}(k)=e^{-t}e^{ikt}\hat f(k),$$

（第一个因子是乘法的 Fourier 侧：乘 $$e^{-t}$$ 是常数，第二个因子来自平移，见 经典问题 5.2(b)）。差商：

$$\widehat{\frac{T(t)f-f}{t}}(k)=\frac{e^{-t}e^{ikt}-1}{t}\hat f(k)
=\underbrace{\frac{e^{ikt}-1}{t}}_{\to ik}\hat f(k)-\underbrace{\frac{1-e^{-t}}{t}}_{\to1}\cdot e^{ikt}\hat f(k).$$

第一项趋于 $$ik\hat f(k)$$（经典问题 5.2(b)），第二项趋于 $$\hat f(k)$$（因为 $$e^{ikt}\hat f\to\hat f$$ 于 $$L^2$$，由控制收敛；$$\frac{1-e^{-t}}{t}\to1$$）。故

$$\frac{T(t)f-f}{t}\xrightarrow[t\to0^{+}]{}f'+(-1)f\qquad\text{于}\ L^2,$$

即生成元是

$$A=\frac{d}{dx}-I,\qquad D(A)=H^{1}(\mathbb R).$$

（反向包含同 经典问题 5.2(b)：若差商收敛，则分布意义下收敛到 $$f'-f$$，故 $$f\in H^1$$。）

**谱。** 在 Fourier 侧 $$A$$ 是乘子 $$ik-1$$，故

$$\sigma(A)=\overline{\{ik-1:k\in\mathbb R\}}=-1+i\mathbb R,$$

一条落在左半平面的竖直线。由定理 3.4，$$\operatorname{Re}\lambda>0$$ 全在预解集中；而 $$\sup\operatorname{Re}\sigma(A)=-1=\omega$$ 与 $$\lVert T(t)\rVert=e^{-t}=e^{\omega t}$$ 吻合（$$\omega=\ln\lVert T(1)\rVert=-1$$，与定理 3.1 的界一致且取等号，因为这是正规族）。

**为什么是压缩而不是酉。** 生成元的谱整体落在左半平面而不在虚轴上，正是"压缩"的判据：$$\lVert T(t)\rVert=e^{-t}<1$$ 逐年衰减。若拿掉 $$-I$$，$$A=\frac{d}{dx}$$ 的谱是虚轴，对应平移酉群（经典问题 5.2）——**一项 $$-I$$ 把谱左移了 $$1$$，半群就从"不可逆但保范"变成了"真的耗散"**；$$\operatorname{Re}\sigma(A)<0$$ 正是"有谱隙"的含义。$$\blacksquare$$

**解 竞3.** 全部是代数运算加上范数估计。

**(i)** 在恒等式 $$(\mu I-A)-(\lambda I-A)=(\mu-\lambda)I$$ 的两边左乘 $$R(\lambda,A)$$、右乘 $$R(\mu,A)$$：

$$R(\lambda,A)\bigl[(\mu I-A)-(\lambda I-A)\bigr]R(\mu,A)=(\mu-\lambda)R(\lambda,A)R(\mu,A).$$

左端逐项算：$$R(\lambda,A)(\mu I-A)R(\mu,A)$$ 中 $$(\mu I-A)R(\mu,A)=I$$（在 $$X$$ 上），故它等于 $$R(\lambda,A)$$；同样 $$R(\lambda,A)(\lambda I-A)R(\mu,A)=R(\mu,A)$$（注意 $$(\lambda I-A)$$ 与 $$R(\lambda,A)$$ 在 $$D(A)$$ 上互补，而 $$R(\mu,A)$$ 的值域落在 $$D(A)$$，故 $$(\lambda I-A)R(\mu,A)$$ 与 $$R(\lambda,A)$$ 复合后正好给出 $$R(\mu,A)$$）。于是左端 $$=R(\lambda,A)-R(\mu,A)$$，即

$$R(\lambda,A)-R(\mu,A)=(\mu-\lambda)R(\lambda,A)R(\mu,A).$$

**(ii)** 在 (i) 中交换 $$\lambda,\mu$$：$$R(\mu,A)-R(\lambda,A)=(\lambda-\mu)R(\mu,A)R(\lambda,A)$$。把 (i) 的两边取负：$$R(\mu,A)-R(\lambda,A)=(\lambda-\mu)R(\lambda,A)R(\mu,A)$$。与前一式比较，$$(\lambda-\mu)\bigl[R(\mu,A)R(\lambda,A)-R(\lambda,A)R(\mu,A)\bigr]=0$$。取 $$\lambda\ne\mu$$ 得两乘积相等；$$\lambda=\mu$$ 时平凡。

**(iii)** 由 (i)，$$\frac{R(\lambda,A)-R(\mu,A)}{\lambda-\mu}=-R(\lambda,A)R(\mu,A)$$ 对 $$\lambda\ne\mu$$ 成立。令 $$\mu\to\lambda$$：右端收敛到 $$-R(\lambda,A)^{2}$$，因为由 (i) 取范数得

$$\lVert R(\mu,A)-R(\lambda,A)\rVert\le\lvert\mu-\lambda\rvert\lVert R(\lambda,A)\rVert\lVert R(\mu,A)\rVert,$$

而 $$R(\cdot,A)$$ 在 $$\lambda$$ 附近局部有界（预解集 $$\rho(A)$$ 是开集，这一条也可由 (i) 式本身直接读出）。于是左端收敛，且

$$\frac{d}{d\lambda}R(\lambda,A)=\lim_{\mu\to\lambda}-R(\lambda,A)R(\mu,A)=-R(\lambda,A)^{2}.$$

**解析性。** 上式把导数写成了 $$\rho(A)$$ 上连续的 $$\mathcal B(X)$$ 值函数（$$R(\cdot,A)$$ 连续、算子乘法连续）。"每点复可导且导数连续"正是 $$\mathcal B(X)$$ 值全纯函数的定义（$$\mathcal B(X)$$ 完备），故 $$R(\cdot,A)$$ 在 $$\rho(A)$$ 上解析。$$\blacksquare$$

**解 竞4.** **关键 leap**：把 $$A$$ 拆成两半、夹住 $$B$$，于是 $$A$$ 的一阶项凑成完整的 $$A$$，而 $$A$$ 的二阶项被两半平摊成 $$\frac{A^{2}}{2}$$，正好凑出 $$\frac{(A+B)^{2}}{2}$$。

记 $$\varepsilon=1/m$$，$$T=e^{\varepsilon A/2}e^{\varepsilon B}e^{\varepsilon A/2}$$、$$S=e^{\varepsilon(A+B)}$$。

**第一步，展开 $$T$$ 到二阶。** 由 $$e^{\varepsilon A/2}=I+\frac{\varepsilon A}2+\frac{\varepsilon^{2}A^{2}}8+O(\varepsilon^{3})$$，先把前两个因子相乘：

$$e^{\varepsilon A/2}e^{\varepsilon B}=I+\varepsilon\Bigl(\frac A2+B\Bigr)+\varepsilon^{2}\Bigl(\frac{A^{2}}8+\frac{AB}2+\frac{B^{2}}2\Bigr)+O(\varepsilon^{3}).$$

再乘第三个因子。记 $$P=\frac A2+B$$、$$Q=\frac{A^{2}}8+\frac{AB}2+\frac{B^{2}}2$$：

$$T=\Bigl(I+\varepsilon P+\varepsilon^{2}Q+O(\varepsilon^{3})\Bigr)\Bigl(I+\frac{\varepsilon A}2+\frac{\varepsilon^{2}A^{2}}8+O(\varepsilon^{3})\Bigr)
=I+\varepsilon\Bigl(P+\frac A2\Bigr)+\varepsilon^{2}\Bigl(Q+\frac{PA}2+\frac{A^{2}}8\Bigr)+O(\varepsilon^{3}).$$

**一阶项**：

$$P+\frac A2=\frac A2+B+\frac A2=A+B .$$

**二阶项**：

$$Q+\frac{PA}2+\frac{A^{2}}8=\Bigl(\frac{A^{2}}8+\frac{AB}2+\frac{B^{2}}2\Bigr)+\frac12\Bigl(\frac A2+B\Bigr)A+\frac{A^{2}}8
=\frac{A^{2}}8+\frac{AB}2+\frac{B^{2}}2+\frac{A^{2}}4+\frac{BA}2+\frac{A^{2}}8 .$$

把 $$\frac{A^{2}}8+\frac{A^{2}}4+\frac{A^{2}}8=\frac{A^{2}}8+\frac{2A^{2}}8+\frac{A^{2}}8=\frac{A^{2}}2$$ 合并：

$$Q+\frac{PA}2+\frac{A^{2}}8=\frac{A^{2}}2+\frac{AB+BA}2+\frac{B^{2}}2=\frac{(A+B)^{2}}2 .$$

于是

$$T=I+\varepsilon(A+B)+\frac{\varepsilon^{2}}2(A+B)^{2}+O(\varepsilon^{3})=S+O(\varepsilon^{3}). \tag{**}$$

**二阶项完全吻合，差从三阶开始。** 这就是对称拆分比不对称拆分好一倍的原因：不对称的 $$e^{\varepsilon A}e^{\varepsilon B}$$ 在二阶差了 $$\frac{\varepsilon^{2}}2[A,B]$$（定理 3.7），对称的 $$e^{\varepsilon A/2}e^{\varepsilon B}e^{\varepsilon A/2}$$ 把 $$A$$ 的两半安排在同一阶的两端，反对称部分自动配对。

**第二步，取 $$m$$ 次幂。** 由 $$(**)$$，$$\lVert T-S\rVert\le C\varepsilon^{3}=C/m^{3}$$（常数 $$C$$ 由三阶余项给出）。与定理 3.7 的第二步同样地：

$$\lVert T^{m}-S^{m}\rVert\le m\max(\lVert T\rVert,\lVert S\rVert)^{m-1}\lVert T-S\rVert
\le m\,e^{\lVert A\rVert+\lVert B\rVert}\cdot\frac{C}{m^{3}}=\frac{Ce^{\lVert A\rVert+\lVert B\rVert}}{m^{2}}\to0 .$$

而 $$S^{m}=e^{A+B}$$，故 $$\lim_mT^{m}=e^{A+B}$$，且误差按 $$1/m^{2}$$ 衰减——比定理 3.7 的 $$1/m$$ 快一个量级。$$\blacksquare$$

**解 研1.** 分三层：$$N$$ 步截断是初等的、取极限靠测度、实时间为什么不行。

**第一层：$$N$$ 步截断是初等的有限维积分。** 把 $$(3.7)$$ 换成虚时间版本（$$e^{-itH/\hbar}\to e^{-tH/\hbar}$$，$$S_N\to S_N^{E}=\sum_k\frac tN\bigl(\frac m2\lvert\frac{x_k-x_{k-1}}{t/N}\rvert^{2}+V(x_{k-1})\bigr)$$，即**欧氏作用量**：动能项不变、势能换号），

$$\bigl(e^{-tH/\hbar}f\bigr)(x_0)=\lim_{N\to\infty}\Bigl(\frac{mN}{2\pi\hbar t}\Bigr)^{\frac{nN}{2}}
\int_{(\mathbb R^n)^{N}}e^{-\frac{1}{\hbar}S_N^{E}}f(x_N)\prod_{k=1}^{N}dx_k . \tag{\star}$$

前因子与 Gaussian 指数正是一个概率密度：$$\prod_k\bigl(\frac{mN}{2\pi\hbar t}\bigr)^{n/2}e^{-\frac{mN\lvert x_k-x_{k-1}\rvert^{2}}{2\hbar t}}$$ 是 $$N$$ 个独立增量（在步长 $$\tau=t/N$$ 上服从 $$N\bigl(0,\frac{\hbar\tau}{m}I_n\bigr)$$）的高斯密度之积。取分段线性插值

$$b^{(N)}(s)=x_k+\frac{s-k\tau}{\tau}(x_{k+1}-x_k)\qquad(k\tau\le s\le(k+1)\tau)$$

（这正是构造布朗运动的 **Lévy 插值路线**），则 $$(\star)$$ 读作

$$\bigl(e^{-tH/\hbar}f\bigr)(x_0)=\lim_{N\to\infty}\mathbb E\Bigl[e^{-\frac{1}{\hbar}\sum_{k=0}^{N-1}\frac tNV(b^{(N)}(k\tau))}f(b^{(N)}(t))\Bigr], \tag{\star\star}$$

右边是对那些独立高斯增量取的期望。这一步完全是有限维概率的初等运算。

**第二层：取极限要靠 Wiener 测度。** **(a) 测度本身。** 把 $$b^{(N)}$$ 看成 $$C([0,t];\mathbb R^n)$$ 中的随机元。对固定时刻组 $$s_1<\dots<s_r$$，$$(b^{(N)}(s_1),\dots,b^{(N)}(s_r))$$ 由一列独立高斯增量的线性组合给出，其协方差矩阵趋于 $$\bigl(\min(s_i,s_j)\frac{\hbar}{m}\bigr)_{ij}$$（有限 $$N$$ 的插值偏差随 $$N\to\infty$$ 消失）。这些有限维分布**相容**（协方差族 $$\min(s_i,s_j)$$ 相容），由 **Kolmogorov 延拓定理**得到乘积空间上的概率测度 $$\mu_x$$；再由 **Kolmogorov 连续性判据**（增量四阶矩 $$\mathbb E\lvert b(s)-b(s')\rvert^{4}=3\bigl(\frac{\hbar}{m}\lvert s-s'\rvert\bigr)^{2}<\infty$$）把 $$\mu_x$$ 拉回到 $$C([0,t];\mathbb R^n)$$，即 **Wiener 测度**。**(b) 被积函数。** $$s\mapsto b(s)$$ 沿 $$\mu_x$$-a.e. 轨道连续，故 $$V$$ 有界连续时 $$\frac tN\sum_kV(b^{(N)}(k\tau))\to\int_0^tV(b(s))ds$$ a.e.；由 $$V\ge0$$，$$0<e^{-\frac1\hbar\sum\ldots V}\le1$$ 可作控制函数，$$f(b(t))$$ 可积（$$b(t)$$ 高斯，$$f\in L^2$$ 时由 Cauchy–Schwarz）。控制收敛定理给出期望收敛到 $$\mathbb E_x\bigl[e^{-\frac1\hbar\int_0^tV(b(s))ds}f(b(t))\bigr]$$，与 $$(\star\star)$$ 合并即得 $$(3.12)$$。

**第三层：实时间为什么没有测度。** 把 $$(\star)$$ 当期望来读时，那个"密度"是 $$\bigl(\frac{mN}{2\pi i\hbar t}\bigr)^{n/2}e^{\frac{imN\lvert x_k-x_{k-1}\rvert^{2}}{2\hbar t}}$$，其模处处恒为 $$\bigl(\frac{mN}{2\pi\hbar t}\bigr)^{n/2}$$——**不衰减、不非负、积分不为 $$1$$**；$$N$$ 个相乘后总模正是 $$(3.7)$$ 里那个随 $$N\to\infty$$ 发散的前因子，而除掉它之后剩下的 $$e^{i\frac{mN}{2\hbar t}\lvert\cdot\rvert^{2}}$$ 有振荡符号、总质量不为 $$1$$，仍不是概率密度。于是实时间下那些"有限维分布"根本不是概率分布，相容性、延拓、控制收敛全部无从谈起。Cameron 定理（1960）把这条障碍提升为定理：**不存在 $$C([0,t])$$ 上 $$\sigma$$-可加、使 $$e^{\frac i\hbar S}$$ 可积的复测度**能让 $$(3.11)$$ 成立。所以实时间路径积分的唯一严格形态是 $$(3.7)$$ 那条算子强极限。$$\blacksquare$$

注意与下一章的接口：**这正是第 24 章的起点**——那里的变换群由任意有限维 Lie 代数 $$\mathfrak g$$ 的指数映射给出，本章的 $$t\mapsto e^{tA}$$ 只是 $$G=\mathbb R$$ 的特殊情形。

**解 研2.** 三问分三步。

**(i) 对易子封闭。** 换位子 $$C(t)=U_j(t)U_k(t)U_j(t)^{-1}U_k(t)^{-1}$$ 是 $$G$$ 的元素，$$t\to0$$ 时趋于 $$I$$。把它展开到 $$t^{2}$$ 阶，由 $$U_j(t)^{\pm1}=I\pm tA_j+\frac{t^{2}}2A_j^{2}+O(t^{3})$$：

$$U_j(t)U_k(t)=I+t(A_j+A_k)+t^{2}\Bigl(\frac{A_j^{2}}2+A_jA_k+\frac{A_k^{2}}2\Bigr)+O(t^{3}),$$

$$U_j(t)^{-1}U_k(t)^{-1}=I-t(A_j+A_k)+t^{2}\Bigl(\frac{A_j^{2}}2+A_jA_k+\frac{A_k^{2}}2\Bigr)+O(t^{3}).$$

相乘后一次的 $$t$$ 项抵消，括号里恰好剩下 $$A_jA_k-A_kA_j$$（与定理 3.7 的计算同型）：

$$C(t)=I+t^{2}\Bigl[2\Bigl(\frac{A_j^{2}}2+A_jA_k+\frac{A_k^{2}}2\Bigr)-(A_j+A_k)^{2}\Bigr]+O(t^{3})=I+t^{2}[A_k,A_j]+O(t^{3}).$$

于是 $$t^{-2}\bigl(C(t)-I\bigr)\to[A_j,A_k]$$。这是**群元素组合的极限**，其"无穷小方向"必须落在 $$\mathfrak g$$ 的闭包中——否则换位子会产生 $$\{A_j\}$$ 张成之外的新方向，与 $$G$$ 只由这些单参数群生成矛盾。故 $$[A_j,A_k]=\sum_{\ell}c_{jk}^{\ \ \ell}A_\ell$$：对易子封闭，且给出了 $$\mathfrak g$$ 上的**括号运算** $$[\cdot,\cdot]:\mathfrak g\times\mathfrak g\to\mathfrak g$$。

**(ii) 它是一个 Lie 代数。** 这三条性质都由 $$[X,Y]=XY-YX$$ 直接得到（见第 16 章 定理 3.2）：双线性、反对称 $$[X,Y]=-[Y,X]$$、**Jacobi 恒等式**

$$[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$$

（把括号写成 $$XY-YX$$ 展开，六项两两抵消）。带这三条性质的实向量空间就是**实 Lie 代数**。于是 $$\mathfrak g$$ 是 Lie 代数，$$G$$ 是它的 Lie 群，而指数映射 $$\exp:\mathfrak g\to G$$ 由 $$e^{tA_j}$$ 的乘积实现。定理 3.7 与 3.8 正是这个指数映射的两条结构定理：$$e^{A+B}=\lim(e^{A/m}e^{B/m})^{m}$$ 说的就是"**$$\mathfrak g$$ 中的向量加法，在 $$G$$ 里要经过乘积与极限才能实现**"。

**(iii) 与正则对易关系的关系。** 第 22 章的 $$[Q_j,P_k]=i\hbar\delta_{jk}$$、$$[Q_j,Q_k]=[P_j,P_k]=0$$ 是 (i) 的实例：$$\{Q_j,P_k\}$$ 张成的（$$2n+1$$ 维，含中心元 $$i\hbar I$$）向量空间对对易子封闭且满足 Jacobi 恒等式——这是 **Heisenberg 代数**。本章的 $$[A,B]$$ 出现在 Trotter 公式的误差主项 (3.5) 里，位置与 CCR 出现在正则量子化里的位置相同：**对易子是"两次无穷小操作的顺序差"的度量**。第 22 章用它刻画位置与动量（代数侧），本章用它刻画时间演化的两步拆分（分析侧）——同一件代数的两面。

**下一章的任务**：本章的 $$A,B$$ 都作用在同一个 Hilbert 空间上、且群参数只有一维（时间）。第 24 章要把"空间"也换掉——不再有固定的原点与固定的内积，而是**仿射空间**（丢掉原点，保留平移）上的**变换群**，以及描述它们无穷小结构的 **Lie 群与 Lie 代数**。本章的 $$e^{tA}$$ 在那里会变成 $$\exp:\mathfrak g\to G$$ 的一般公式，而定理 3.7 会变成 Baker–Campbell–Hausdorff 公式的第一项。**这正是第 24 章的起点。**

## 七、Takeaway 与延伸 (Takeaways)

**1. "$$e^{tA}$$"的定义权在 Hille–Yosida，不在级数。** 无界算子不能用幂级数定义指数（$$A^{2}$$ 无意义）。正确路线：先要求 $$t\mapsto T(t)$$ 是强连续半群（定义 3.1），再用差商读出生成元（定义 3.2），最后用预解式条件 $$(*)$$ 判定"哪些 $$A$$ 能当生成元"（定理 3.5）。**全部技术困难来自"$$A$$ 无界而 $$T(t)$$ 有界"这个不对称。**

**2. 预解式是半群的频域像。** 定理 3.3 的 $$R(\lambda,A)=\int_0^\infty e^{-\lambda t}T(t)dt$$ 把时间对象与复分析对象逐点对应起来；Hille–Yosida 的条件因此是"积分收敛 + 双边求逆"的直接产物，不是凭空规定。

**3. 谱的位置决定时间的形态。** 生成元自伴半正定 $$\Leftrightarrow$$ 压缩半群（扩散，不可逆）；生成元反自伴 $$\Leftrightarrow$$ 酉群（波，可逆）。$$e^{-tA}$$ 与 $$e^{-itA}$$ 由 $$t\mapsto-it$$ 相连，这就是 Wick 转动：解析延拓改的只是相位的写法，不动谱。

**4. Trotter 公式的误差是对易子。** $$e^{A/m}e^{B/m}$$ 与 $$e^{(A+B)/m}$$ 的二阶差恰是 $$\frac{1}{2m^{2}}[A,B]$$（(3.5)），取 $$m$$ 次幂后误差按 $$1/m$$ 衰减；对称拆分 $$e^{A/2m}e^{B/m}e^{A/2m}$$ 让二阶差消失，误差按 $$1/m^{2}$$ 衰减（竞4）。**对易子在这里第一次以"可加性的代价"现身：$$e^{A+B}\ne e^{A}e^{B}$$ 的全部内容就是 $$[A,B]\ne0$$。**

**5. 路径积分没有测度，它是算子极限。** (3.11) 的 $$\mathcal D x(\cdot)$$ 不是测度记号：路径空间是无穷维的，平移不变的 $$\sigma$$-有限测度不存在，而 Cameron 定理排除了把它做成 $$\sigma$$-可加复测度。它的严格身份是定理 3.11——**有限维 Lebesgue 积分序列的强极限**；转到虚时间后测度真的出现（Wiener 测度），即 Feynman–Kac 公式 (3.12)。**路径积分不含新公理：它是 Stone 定理 + Stone–von Neumann + Trotter 公式的合成。**

**下一章的悬念。** 本章的 $$A,B$$ 作用在同一个 Hilbert 空间上，群参数只有一维（时间），且有固定的原点与内积。第 24 章要把这两条都拿掉：**仿射空间**丢掉原点但保留平移，**变换群**让"空间"本身动起来，描述它们无穷小结构的就是 **Lie 群与 Lie 代数**；本章的 $$e^{tA}$$ 在那里一般化为 $$\exp:\mathfrak g\to G$$，定理 3.7 的 $$[A,B]$$ 会成为 Baker–Campbell–Hausdorff 公式的第一项。卷三到此收束，卷四从仿射空间重新出发去讲对称性本身。

**延伸阅读。**

- **半群与生成元**：K.-J. Engel, R. Nagel, *One-Parameter Semigroups for Linear Evolution Equations*（GTM 194）第 II、III 章（定理 3.5 与定理 3.9 的完整证明）；T. Kato, *Perturbation Theory for Linear Operators*（GTM 132）第 IX 章（Trotter–Kato）；原始文献 H. F. Trotter, *On the product of semi-groups of operators*, Proc. AMS 10 (1959)。
- **路径积分的数学构造**：B. Simon, *Functional Integration and Quantum Physics*；J. Glimm, A. Jaffe, *Quantum Physics: A Functional Integral Point of View*。Feynman–Kac 公式与 Wiener 测度是这两本的主线。
- **无穷维测度**：Bogachev, *Measure Theory* 中关于无穷维测度的章节——"无穷维没有平移不变测度"与测度论里"可数可加性只在可测集上成立"是同一类现象（把"太大"的族限制掉）。
- **本课程内部**：第 21、22 章是本章的两条输入，第 19 章的谱定理是全部积分的计算工具，第 17 章给出 $$H$$ 的来源。物理侧对照 QFT 的路径积分表述（知识库 `opc2/knowledge/physics/量子场论/`）——那里从 $$(3.11)$$ 出发的大量形式操作，正是本章要分辨"哪些有严格含义、哪些只是渐近展开"的对象。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch22_正则对易关系与Stone_vonNeumann.md">← 第22章 正则对易关系与 Stone–von Neumann 定理</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch24_仿射空间_变换群与Lie群.md">第24章 仿射空间、变换群与 Lie 群 →</a></div>
</div>
