---
layout: default
---

# 第04章: 平面旋转群 SO(2) 与算子的谱·下：完整推导 (The Rotation Group SO(2) and the Spectrum of an Operator · Part II: Full Derivation)

> 对应原专栏: MP2–MP3
> 专家依据: algebra/lie-algebra-root-systems.md + analysis/spectral-theory.md（主）；方法论见 algebra/_SKILL.md 与 analysis/_SKILL.md
> 知识库依据: opc2/knowledge/math/李群/lie-groups/（ch01–ch03、ch08）、opc2/knowledge/math/谱理论/（ch01–ch02）
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）
> 配套预备: 见 第03章 平面旋转群 SO(2) 与算子的谱·上（同一主题的具体铺垫，建议先读）

## 一、本章概要 (Overview)

第 02 章我们已经看见三件事是同一件事：平面旋转、复数乘法、以及 $$i^2=-1$$。它还留下了一个悬念：旋转矩阵 $$R_\theta$$ 在实数域里没有特征方向，可一旦允许复特征值，它的谱是 $$\{e^{\pm i\theta}\}$$——**为什么恰好落在单位圆上？** 本章要把这条线索推进一步，回答一个看似更荒谬的问题：**「求导」凭什么能给出「谱」？**

链条是这样的：平面旋转全体构成一个 Lie 群 $$SO(2)$$；对它求导，得到它的 Lie 代数（一维，生成元是一个反对称矩阵 $$J$$）；让这个生成元作用在函数空间上，它就成了一个算子；求这个算子的特征值，我们得到纯虚数 $$ik$$——于是 $$i$$ 从「一个被假设存在的数」变成「求导算子的一条谱线」。而第 02 章悬而未决的那条"单位圆上的谱"，正是这条谱线在指数映射下的像。

这条线是全书的技术起点：第 54 章（Lie 代数与指数映射）会把它推广到非交换的 $$SO(3)$$，第 36 章（有界算子与谱）会把它升级成完整的算子谱理论。本章只做一件事——把 $$SO(2)$$ 这一个例子彻底做穿。

## 二、入口：一道具体的问题 (Entry Problem)

> 题目来源：**自编**。母题（"$$A^2=-I$$ 的实矩阵长什么样"）是线性代数教材的经典例题；把它与周期函数空间并置，是本章的设计。

**入口题。**

(a) 求所有满足 $$A^2=-I$$ 的 $$2\times 2$$ 实矩阵 $$A$$，其中 $$I$$ 是 $$2\times 2$$ 单位矩阵。

(b) 设 $$C^\infty_{2\pi}$$ 表示 $$\mathbb{R}$$ 上以 $$2\pi$$ 为周期的光滑函数全体（复值）。记 $$D=\dfrac{d}{d\theta}$$。求 $$D^2$$ 的**全部**特征值（eigenvalue，物理文献中也称本征值）与相应的特征函数。

(c) 承 (b)：在子空间 $$W=\mathrm{span}_\mathbb{R}\{\cos\theta,\sin\theta\}$$ 上（$$W$$ 在 $$D$$ 下不变），写出 $$D$$ 的矩阵并判断它是否是一个"平方等于 $$-1$$"的结构。

(d) 再把问题问精确：把 $$D$$ 看成整个 $$C^\infty_{2\pi}$$ 上的算子，$$D^2=-I$$ 成立吗？如果不成立，具体坏在哪一条谱线上？

**为什么这是同一道题。** (a) 是有限维的、纯代数的；(b)(c)(d) 是无限维的、分析的。但四者问的是同一个东西：**一个"平方等于 $$-1$$"的结构能活在哪里。** 读完本章你会看到，(a) 的答案是"$$J$$ 的共轭类"，(b) 的答案是"整数 $$k$$ 的平方"，(c) 的答案是"$$W$$ 上一个活生生的复结构，等于 $$-J$$"，(d) 的答案是"不成立；坏在 $$k=0$$ 那条谱线上——常数把 $$D$$ 杀死了"。(a) 里的那个 $$J$$，会以三种面孔在 (b)(c)(d) 里重现。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 $$SO(2)$$ 的定义与显式分类

**定义（特殊正交群）**。称实矩阵 $$R$$ 为**正交矩阵 (orthogonal matrix)**，若 $$R^{\mathsf{T}}R=I$$；若进一步 $$\det R=1$$，称 $$R$$ 为**特殊正交矩阵 (special orthogonal matrix)**。全体 $$2\times 2$$ 特殊正交矩阵在矩阵乘法下构成**平面旋转群 (rotation group) $$SO(2)$$**。

（定义与参数化见第 02 章 §3.1；此处重述以求记号统一。）

我们先把 $$SO(2)$$ 的元素写干净——这一步不能省，后面所有计算都建立在它上面。

**定理 3.1**。设 $$R=\begin{bmatrix}a&b\\ c&d\end{bmatrix}$$ 是实矩阵。则 $$R\in SO(2)$$ 当且仅当存在 $$\theta\in\mathbb{R}$$ 使

$$R=R_\theta:=\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}.$$

*证明思路*：把 $$R^{\mathsf{T}}R=I$$ 翻译成"两列是标准正交基"，再用 $$\det R=1$$ 从两个可能的定向中挑出一个。

*证明*：记 $$u=\begin{bmatrix}a\\ c\end{bmatrix}$$，$$v=\begin{bmatrix}b\\ d\end{bmatrix}$$。条件 $$R^{\mathsf{T}}R=I$$ 等价于 $${u}\cdot{u}={v}\cdot{v}=1$$ 且 $${u}\cdot{v}=0$$（正交矩阵的列是标准正交基）。于是 $$\{u,v\}$$ 是 $$\mathbb{R}^2$$ 的标准正交基。

给定单位向量 $$u=\begin{bmatrix}a\\ c\end{bmatrix}$$，与它正交的单位向量只有两个：$$\begin{bmatrix}-c\\ a\end{bmatrix}$$ 与 $$\begin{bmatrix}c\\ -a\end{bmatrix}$$（因为 $$(-c,a)\cdot(a,c)=-ca+ac=0$$，且 $$c^2+a^2=1$$）。分别代入计算行列式：

$$v=(-c,a)^{\mathsf{T}}:\qquad a\cdot a-b\cdot c=a^2+c^2=1,$$
$$v=(c,-a)^{\mathsf{T}}:\qquad a\cdot(-a)-c\cdot c=-(a^2+c^2)=-1.$$

条件 $$\det R=1$$ 唯一地挑出 $$v=(-c,a)^{\mathsf{T}}$$，即 $$b=-c,\ d=a$$。于是

$$R=\begin{bmatrix}a&-c\\ c&a\end{bmatrix},\qquad a^2+c^2=1.$$

最后一步：把单位向量 $$(a,c)$$ 写成 $$(\cos\theta,\sin\theta)$$——这就是"用角参数化单位圆"，$$\theta$$ 在模 $$2\pi$$ 意义下唯一。代回即得 $$R=R_\theta$$。反向的验证是直接的：$$\cos^2\theta+\sin^2\theta=1$$ 给出正交性，行列式为 $$\cos^2\theta+\sin^2\theta=1$$。$$\blacksquare$$

**注**：定理 3.1 只用到两个事实：单位圆上的点可以写成 $$(\cos\theta,\sin\theta)$$，以及三角函数的定义本身。我们没有用到任何三角恒等式——恒等式将在下一小节作为**计算结果**出现。

### 3.2 群同态 $$\rho$$ 与圆环群的结构

**定理 3.2**。映射

$$\rho:\mathbb{R}\to SO(2),\qquad \theta\mapsto R_\theta$$

是满群同态，其核为 $$\ker\rho=2\pi\mathbb{Z}$$。因此 $$SO(2)\cong\mathbb{R}/2\pi\mathbb{Z}$$（**圆环群 (circle group)**）。

*证明思路*：满射性是定理 3.1；同态性是直接矩阵乘法，其副产品正是余弦、正弦的和角公式；核用 $$\cos\theta=1,\sin\theta=0$$ 定出。（第 02 章 §3.4 已证过该同构链，本节补出 $$SO(2)$$ 一侧的证明。）

*证明*：满射性由定理 3.1 给出。同态性：直接作矩阵乘法，

$$R_\alpha R_\beta=\begin{bmatrix}\cos\alpha&-\sin\alpha\\ \sin\alpha&\cos\alpha\end{bmatrix}\begin{bmatrix}\cos\beta&-\sin\beta\\ \sin\beta&\cos\beta\end{bmatrix}
=\begin{bmatrix}\cos\alpha\cos\beta-\sin\alpha\sin\beta&-(\cos\alpha\sin\beta+\sin\alpha\cos\beta)\\ \sin\alpha\cos\beta+\cos\alpha\sin\beta&\cos\alpha\cos\beta-\sin\alpha\sin\beta\end{bmatrix}.$$

把这个矩阵与 $$R_{\alpha+\beta}$$ 逐项比较，就得到

$$\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta,\qquad \sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta.$$

（所以：**和角公式不是前提，是同态性的推论**。）于是 $$R_\alpha R_\beta=R_{\alpha+\beta}$$，同态性成立。

核：$$\theta\in\ker\rho$$ 当且仅当 $$\cos\theta=1$$ 且 $$\sin\theta=0$$（单位矩阵的对角元与副对角元同时取零值），当且仅当 $$\theta\in2\pi\mathbb{Z}$$。由第一同构定理，$$\mathbb{R}/2\pi\mathbb{Z}\cong SO(2)$$。$$\blacksquare$$

**两点必须记住**：

1. $$SO(2)$$ 是**交换群 (abelian group)**——因为 $$\mathbb{R}$$ 的加法交换，而 $$\rho$$ 满。矩阵乘法在这里是可交换的，这不是巧合，是 $$\rho$$ 满射的推论。
2. $$\rho$$ **不是**单射（$$\rho(0)=\rho(2\pi)=I$$）。因此 $$SO(2)$$ 与实数加群 $$\mathbb{R}$$ 只是**局部**同构，整体上差一个离散群 $$2\pi\mathbb{Z}$$。这个"差一个离散群"会在第 25、27 章变成核心话题（局部同构 vs 整体同构）。

### 3.3 求导：$$so(2)$$ 与指数映射

现在开始本章的主戏。我们让 $$\theta$$ 动起来，对 $$\rho$$ 求导。

**定理 3.3（求导产生 Lie 代数）**。记

$$J:=R_{\pi/2}=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}.$$

则对一切 $$\theta$$，

$$\frac{d\rho}{d\theta}(\theta)=J\,\rho(\theta)=\rho(\theta)\,J.$$

*证明*：直接逐项求导，

$$\frac{d}{d\theta}\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}=\begin{bmatrix}-\sin\theta&-\cos\theta\\ \cos\theta&-\sin\theta\end{bmatrix}.$$

另一方面，$$J R_\theta=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}=\begin{bmatrix}-\sin\theta&-\cos\theta\\ \cos\theta&-\sin\theta\end{bmatrix}$$，与上式逐项相等。右乘的情形 $$R_\theta J$$ 算出来是同一个矩阵；这也顺便**重新验证了 $$SO(2)$$ 交换**（$$J\rho=\rho J$$）。$$\blacksquare$$

**这句式子是全章的心脏，值得逐字读三遍**：$$\dfrac{d\rho}{d\theta}=J\cdot\rho$$。它的意思是——**在 $$SO(2)$$ 上求导，等价于"乘以一个固定的矩阵 $$J$$"**。求导这个"分析操作"被化归成"代数操作"。

**推论 3.4**。$$J^2=-I$$，从而 $$\dfrac{d^2\rho}{d\theta^2}=-I\cdot\rho=-\rho$$。

*证明*：$$J^2=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}=\begin{bmatrix}-1&0\\ 0&-1\end{bmatrix}=-I$$，直接计算。再由定理 3.3 对 $$\theta$$ 再求一次导：$$\dfrac{d^2\rho}{d\theta^2}=J\dfrac{d\rho}{d\theta}=J^2\rho=-\rho$$。$$\blacksquare$$

**定义（切空间与 Lie 代数 $$so(2)$$）**。$$SO(2)$$ 在单位元 $$I$$ 处的**切空间 (tangent space)** 定义为

$$\mathfrak{so}(2):=\big\{\,\gamma'(0)\ :\ \gamma:\mathbb{R}\to SO(2)\ \text{smooth},\ \ \gamma(0)=I\,\big\}.$$

**定理 3.5**。$$\mathfrak{so}(2)=\{X:\ X^{\mathsf{T}}=-X\}=\mathbb{R}\cdot J=\{aJ:\ a\in\mathbb{R}\}$$，特别地 $$\dim\mathfrak{so}(2)=1$$。

*证明思路*：对约束 $$R^{\mathsf{T}}R=I$$ 求导得到 $$X^{\mathsf{T}}+X=0$$（这是必要条件）；反过来，任给反对称 $$X$$，用指数映射造一条曲线（这是充分条件）。

*证明*：（必要性）设 $$\gamma(t)\in SO(2)$$，$$\gamma(0)=I$$。对恒等式 $$\gamma(t)^{\mathsf{T}}\gamma(t)=I$$ 两边求导：

$$\gamma'(t)^{\mathsf{T}}\gamma(t)+\gamma(t)^{\mathsf{T}}\gamma'(t)=0.$$

代入 $$t=0$$ 并用 $$\gamma(0)=I$$，得 $$\gamma'(0)^{\mathsf{T}}+\gamma'(0)=0$$。所以每个切向量都反对称。

（充分性）设 $$X^{\mathsf{T}}=-X$$，即 $$X=\begin{bmatrix}p&q\\ r&s\end{bmatrix}$$ 满足 $$p=0,\ s=0,\ r=-q$$，也即 $$X=\begin{bmatrix}0&q\\ -q&0\end{bmatrix}=qJ$$（对某个 $$q\in\mathbb{R}$$）。取 $$\gamma(t)=\exp(tX)$$（指数级数的绝对收敛见定理 3.6 的证明），则 $$\gamma(0)=I$$、$$\gamma'(0)=X$$，且由 $$\exp(tX)^{\mathsf{T}}=\exp(tX^{\mathsf{T}})=\exp(-tX)=\exp(tX)^{-1}$$ 知 $$\gamma(t)\in O(2)$$；再由 $$\det\exp(tX)=\exp(t\,\mathrm{tr}\,X)=\exp(0)=1$$ 知 $$\gamma(t)\in SO(2)$$。所以 $$X$$ 确在切空间里。

综上，$$\mathfrak{so}(2)=\{aJ\}$$，一维。$$\blacksquare$$

**定义（Lie 代数与 Lie 括号）**。切空间 $$\mathfrak{so}(2)$$ 配上**Lie 括号 (Lie bracket)** $$[X,Y]=XY-YX$$（矩阵换位子），称为 $$SO(2)$$ 的 **Lie 代数 (Lie algebra)**。（一般定义与 Jacobi 恒等式见第 54 章；本章只需矩阵情形。）

因为 $$\mathfrak{so}(2)$$ 一维，$$[aJ,bJ]=ab(J^2-J^2)=0$$——**$$so(2)$$ 的括号恒为零**。这个"平凡性"很重要：一维 Lie 代数只有这一种，它的全部内容都藏在指数映射里，而不在括号里。第 54 章会看到，一旦换成非交换的 $$SO(3)$$，括号立刻变得非平凡。

**定理 3.6（指数映射）**。对一切 $$\theta\in\mathbb{R}$$，

$$\exp(\theta J)=\sum_{k=0}^{\infty}\frac{(\theta J)^k}{k!}=R_\theta.$$

*证明思路*：用 $$J^2=-I$$ 把幂级数按奇偶拆成两支，分别认出 $$\cos$$ 与 $$\sin$$ 的 Taylor 级数。

*证明*：由 $$J^2=-I$$ 立得 $$J^3=-J$$、$$J^4=I$$，之后以周期 4 循环：$$J^{2m}=(-1)^mI$$，$$J^{2m+1}=(-1)^mJ$$。于是

$$\exp(\theta J)=\sum_{m=0}^{\infty}\frac{\theta^{2m}J^{2m}}{(2m)!}+\sum_{m=0}^{\infty}\frac{\theta^{2m+1}J^{2m+1}}{(2m+1)!}
=I\sum_{m=0}^{\infty}\frac{(-1)^m\theta^{2m}}{(2m)!}+J\sum_{m=0}^{\infty}\frac{(-1)^m\theta^{2m+1}}{(2m+1)!}=I\cos\theta+J\sin\theta.$$

而 $$I\cos\theta+J\sin\theta=\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}=R_\theta$$。$$\blacksquare$$

**推论 3.7**。$$\exp:\mathfrak{so}(2)\to SO(2)$$ 是满射但**不是单射**：$$\exp(0)=\exp(2\pi J)=I$$。直线 $$\mathfrak{so}(2)\cong\mathbb{R}$$ 被整数 $$2\pi k$$ 一格一格地**缠绕 (wrap)** 到圆上，缠绕的层数正是整数——请记住这个图像，第 3.4 节里"整数 $$k$$"会从这里长出来。

**与复数的对照**。第 02 章的 $$e^{i\theta}=\cos\theta+i\sin\theta$$ 在这里得到了代数解释——同构把 $$J$$ 对应到"乘以 $$i$$"：

$$R_\theta\ \longleftrightarrow\ e^{i\theta},\qquad J\ \longleftrightarrow\ i,\qquad J^2=-I\ \longleftrightarrow\ i^2=-1.$$

### 3.4 从群同态到算子：$$D=\dfrac{d}{d\theta}$$

上一节我们把求导作用在"矩阵值函数 $$\rho$$"上。现在把它作用在**整个函数空间**上，看会发生什么。

**定义（求导算子）**。在 $$C^\infty_{2\pi}$$（$$\mathbb{R}$$ 上 $$2\pi$$ 周期光滑复值函数）上定义线性算子

$$D:C^\infty_{2\pi}\to C^\infty_{2\pi},\qquad Df=f'.$$

（"线性"是导数线性性的直接翻译：$$D(af+bg)=aDf+bDg$$。）

**关键观察（三条链同时成立）**：

1. **在矩阵值函数上**：$$D\rho=J\rho$$（定理 3.3）。
2. **在复值函数上**：记 $$\tau(\theta)=e^{i\theta}$$，则 $$D\tau=i\tau$$。这是直接求导：$$\dfrac{d}{d\theta}e^{i\theta}=ie^{i\theta}$$。
3. **在实函数上**：$$D(\cos\theta)=-\sin\theta$$，$$D(\sin\theta)=\cos\theta$$。

这三条其实是一条。理由是 $$\rho(\theta)=I\cos\theta+J\sin\theta$$：**$$\rho$$ 的四条元素恰好是 $$\cos\theta$$ 与 $$\sin\theta$$**，所以"对矩阵求导"就是"对它的四条元素分别求导"。而 $$\{\cos\theta,\sin\theta\}$$ 张成的实二维空间，与 $$\{e^{i\theta}\}$$ 张成的复一维空间，是同一个东西（$$\cos\theta=\mathrm{Re}\,e^{i\theta}$$，$$\sin\theta=\mathrm{Im}\,e^{i\theta}$$）。第 3.6 节会把这条统一说清楚。

**定义（特征值与特征函数）**。设 $$T$$ 是函数空间上的线性算子。若存在非零函数 $$f$$ 与数 $$\lambda$$ 使

$$Tf=\lambda f,$$

称 $$\lambda$$ 为 $$T$$ 的**特征值 (eigenvalue)**，$$f$$ 为相应的**特征函数 (eigenfunction)**。全部特征值组成的集合记为 $$\sigma_p(T)$$，称为 $$T$$ 的**点谱 (point spectrum)**。

**这一步为什么重要**：把 $$T=D$$ 代入，$$Df=\lambda f$$ 就是微分方程 $$f'=\lambda f$$。**算子语言下的"特征值问题"和古典语言下的"常微分方程"是同一件事。** 算子的特征值就是微分方程的"本征频率"。

（第 02 章 注 3.3 已经预告过这一点："$$e^{i\theta}$$ 是求导算子 $$\frac{d}{d\theta}$$ 的特征向量，特征值是 $$i$$"。本节把它从"一个例子"升级成"一类定理"——下一个定理给出 $$D$$ 的**全部**特征值。）

**定理 3.8（$$D$$ 的特征值恰好是纯虚整数）**。

$$\sigma_p(D)=\{\,ik\ :\ k\in\mathbb{Z}\,\}.$$

其相应的特征函数为 $$f_k(\theta)=e^{ik\theta}$$。

*证明思路*：先用"解一阶线性方程"的标准技巧求出方程的全部解；再用 $$2\pi$$ 周期性（即单值性）筛出允许的 $$\lambda$$。

*证明*：设 $$f\in C^\infty_{2\pi}$$ 且 $$f'=\lambda f$$，$$\lambda\in\mathbb{C}$$。令 $$g(\theta)=f(\theta)e^{-\lambda\theta}$$。则

$$g'(\theta)=f'(\theta)e^{-\lambda\theta}-\lambda f(\theta)e^{-\lambda\theta}=(f'(\theta)-\lambda f(\theta))e^{-\lambda\theta}=0.$$

（这里用了 $$e^{-\lambda\theta}$$ 的导数是 $$-\lambda e^{-\lambda\theta}$$，即指数函数的求导法则。）于是 $$g$$ 是常数，设 $$g\equiv c$$，则

$$f(\theta)=c\,e^{\lambda\theta}.$$

现在施加 $$2\pi$$ **周期性这一唯一的外部条件**：对一切 $$\theta$$，

$$c\,e^{\lambda(\theta+2\pi)}=f(\theta+2\pi)=f(\theta)=c\,e^{\lambda\theta}.$$

$$f$$ 非零意味着 $$c\ne0$$，两边约掉 $$c\,e^{\lambda\theta}$$ 得

$$e^{2\pi\lambda}=1.$$

写 $$\lambda=\alpha+i\beta$$（$$\alpha,\beta\in\mathbb{R}$$），则 $$e^{2\pi\lambda}=e^{2\pi\alpha}e^{2\pi i\beta}$$，其模为 $$e^{2\pi\alpha}$$、辐角为 $$2\pi\beta$$。等于 $$1$$ 当且仅当 $$e^{2\pi\alpha}=1$$ 且 $$2\pi\beta\in2\pi\mathbb{Z}$$，即

$$\alpha=0,\qquad \beta\in\mathbb{Z}.$$

所以 $$\lambda=i\beta=ik$$（$$k\in\mathbb{Z}$$），相应的特征函数为 $$e^{ik\theta}$$。反之 $$f_k(\theta)=e^{ik\theta}$$ 确实以 $$2\pi$$ 为周期，且 $$Df_k=ike^{ik\theta}$$。定理证毕。$$\blacksquare$$

**这是本章最需要被记住的一步**：$$\lambda=ik$$ 里的"整数性"**不是**来自 $$e^{ik\theta}$$ 这个写法（那只是记号），而是来自 **$$e^{2\pi\lambda}=1$$ 这个单值性条件**。它是拓扑的，不是代数的：它来自函数定义在**圆** $$S^1$$ 上而不是直线上。同一件事在第 50 章会以 $$\pi_1(S^1)=\mathbb{Z}$$ 的面目重新出现。

**推论 3.9**。$$D^2$$ 的特征值与特征函数为

$$\sigma_p(D^2)=\{\,-k^2\ :\ k\in\mathbb{Z}\,\}=\{0,-1,-4,-9,\dots\}.$$

相应的特征函数还是 $$e^{ik\theta}$$。

特别地 $$D^2$$ 的核是常数函数（$$k=0$$），$$\ker D^2=\mathbb{C}\cdot1$$。

*证明*：$$D^2e^{ik\theta}=D(ike^{ik\theta})=i^2k^2e^{ik\theta}=-k^2e^{ik\theta}$$。反过来说"$$D^2$$ 的特征值只有这些"，需要一点一般性论证：设 $$D^2f=\mu f$$。若 $$\mu=0$$ 则 $$f''=0$$，故 $$f'=\gamma$$ 是常数，$$f=\gamma\theta+\delta$$；周期性逼出 $$\gamma=0$$，即 $$f$$ 必为常数。若 $$\mu\ne0$$，则记 $$\mu=-k^2$$（$$k\ne0$$）；把 $$(D-ik)(D+ik)f=D^2f+k^2f=0$$ 展开，只能得到 $$(D+ik)f$$ 落在 $$D-ik$$ 的核里，还要再解一次一阶方程。为避免重复劳动，我们改用第 3.5 节的 Fourier 论证一次性处理全部情形。$$\blacksquare$$

（上面最后一个"避免重复劳动"是诚实的：推论 3.9 的完整证明在定理 3.11 之后。）

### 3.5 谱：一个算子，而不是一堆特征值

要谈"算子的谱"，我们需要一个内积空间。这属于第 30 章；本章只用它在圆上的最简形式。

**定义（$$L^2(S^1)$$ 与其内积）**。记

$$L^2(S^1)=\Big\{\,f:S^1\to\mathbb{C}\ :\ \int_0^{2\pi}\lvert f(\theta)\rvert^2\,d\theta<\infty\,\Big\}$$

（把 $$2\pi$$ 周期函数与圆上的函数等同）。内积为

$$\langle f,g\rangle=\frac{1}{2\pi}\int_0^{2\pi}f(\theta)\overline{g(\theta)}\,d\theta,$$

$$\lVert f\rVert^2=\langle f,f\rangle$$。在此内积下 $$\{e^{ik\theta}\}_{k\in\mathbb{Z}}$$ 是**标准正交系**：

$$\langle e^{ik\theta},e^{im\theta}\rangle=\frac{1}{2\pi}\int_0^{2\pi}e^{i(k-m)\theta}\,d\theta=\begin{cases}1,&k=m,\\ 0,&k\ne m.\end{cases}$$

（$$k\ne m$$ 时被积函数是 $$e^{i(k-m)\theta}$$，在一个完整周期上积分为零。）这个正交系在 $$L^2(S^1)$$ 中是**完备的**，即每个 $$f\in L^2(S^1)$$ 有 Fourier 展开 $$f=\sum_{k\in\mathbb{Z}}c_k e^{ik\theta}$$，$$c_k=\langle f,e^{ik\theta}\rangle$$，且 $$\lVert f\rVert^2=\sum_k\lvert c_k\rvert^2$$。（完备性属于第 30 章。）

**定理 3.10（$$D$$ 是反自伴的）**。对 $$f,g\in C^\infty_{2\pi}$$，

$$\langle Df,g\rangle=-\langle f,Dg\rangle.$$

即作为（无界）算子，$$D^*=-D$$。满足 $$T^*=-T$$ 的算子称为**反自伴算子 (skew-adjoint operator)**（亦称反厄米算子）。

*证明*：用分部积分，周期性保证边界项为零：

$$\langle Df,g\rangle=\frac{1}{2\pi}\int_0^{2\pi}f'(\theta)\overline{g(\theta)}\,d\theta
=\frac{1}{2\pi}\Big[f\overline{g}\Big]_0^{2\pi}-\frac{1}{2\pi}\int_0^{2\pi}f(\theta)\overline{g'(\theta)}\,d\theta.$$

因为 $$f,g$$ 均为 $$2\pi$$ 周期，$$f(2\pi)\overline{g(2\pi)}=f(0)\overline{g(0)}$$，边界项相减为零。剩下的积分是 $$-\langle f,Dg\rangle$$，因为 $$\overline{g'}=\overline{Dg}$$。$$\blacksquare$$

**推论**：$$D^*=-D$$ 立刻给出 $$D$$ 的任一特征值必为纯虚数。理由：若 $$Df=\lambda f$$，$$\lVert f\rVert=1$$，则

$$\lambda=\langle Df,f\rangle=-\langle f,Df\rangle=-\overline{\langle Df,f\rangle}=-\overline{\lambda}.$$

$$\lambda=-\overline\lambda$$ 当且仅当 $$\mathrm{Re}\,\lambda=0$$。这从"内积几何"的角度**再一次**解释了 $$ik$$ 里的那个 $$i$$。

**定理 3.11（$$D$$ 的谱）**。记 $$H^1=\{\,f\in L^2(S^1):\ \sum_k (1+k^2)\lvert c_k\rvert^2<\infty\,\}$$（Fourier 系数衰减足够快的函数，即满足 $$Df\in L^2$$ 的那些 $$f$$）。

这里第一次用到"**谱 (spectrum)**"这个词：**$$\lambda$$ 属于 $$D$$ 的谱，意思是 $$\lambda I-D$$ 不可逆**（完整定义与一般理论见第 36 章）。则

$$\sigma(D):=\{\,\lambda\in\mathbb{C}\ :\ \lambda I-D\ \text{not invertible}\,\}=\{\,ik:k\in\mathbb{Z}\,\}=i\mathbb{Z},$$

且每个 $$\lambda=ik$$ 都是特征值。换句话说，$$D$$ 的谱**只有点谱**。

*证明思路*：定理 3.8 已给出 $$i\mathbb{Z}\subseteq\sigma(D)$$（那儿的分母为零）。要证反向，只需对 $$\lambda\notin i\mathbb{Z}$$ 显式解 $$(\lambda I-D)f=g$$ 并证明解算子有界。Fourier 基把 $$D$$ 对角化，使这一步变成逐频率的除法。

*证明*：（$$i\mathbb{Z}\subseteq\sigma(D)$$ 这一半已在定理 3.8 完成：$$\lambda=ik$$ 时 $$(\lambda I-D)e^{ik\theta}=0$$，故 $$\lambda I-D$$ 不可逆。）

（另一半）设 $$\lambda\notin i\mathbb{Z}$$。因为 $$i\mathbb{Z}$$ 是 $$\mathbb{C}$$ 中的闭子集，存在 $$\delta>0$$ 使 $$\lvert ik-\lambda\rvert\ge\delta$$ 对一切 $$k\in\mathbb{Z}$$ 成立。

任取 $$g=\sum_k g_k e^{ik\theta}\in L^2(S^1)$$。**定义**

$$f:=\sum_k\frac{g_k}{ik-\lambda}\,e^{ik\theta}.$$

由 $$\lvert ik-\lambda\rvert\ge\delta$$ 得 $$\lvert f_k\rvert\le\lvert g_k\rvert/\delta$$，于是

$$\lVert f\rVert^2=\sum_k\Big\lvert\frac{g_k}{ik-\lambda}\Big\rvert^2\le\frac{1}{\delta^2}\sum_k\lvert g_k\rvert^2=\frac{\lVert g\rVert^2}{\delta^2},$$

所以 $$f\in L^2(S^1)$$ 且 $$\lVert f\rVert\le\delta^{-1}\lVert g\rVert$$。写成 $$\lambda=\alpha+i\beta$$，则 $$\lvert ik-\lambda\rvert^2=\alpha^2+(k-\beta)^2$$，于是

$$k^2\le2\big((k-\beta)^2+\beta^2\big)\le2\Big(1+\frac{\beta^2}{\delta^2}\Big)\lvert ik-\lambda\rvert^2,$$

从而 $$\sum_k k^2\lvert f_k\rvert^2\le2\big(1+\beta^2\delta^{-2}\big)\delta^{-2}\lVert g\rVert^2<\infty$$，即 $$f\in H^1$$。逐项求导是合法的：$$f\in H^1$$ 等价于 $$f$$ 绝对连续且 $$f'\in L^2$$，此时 $$f'$$ 的 Fourier 系数恰为 $$ik\,f_k$$。于是

$$Df=\sum_k \frac{ik\,g_k}{ik-\lambda}e^{ik\theta},\qquad (\lambda I-D)f=\sum_k\frac{\lambda-ik}{ik-\lambda}g_k e^{ik\theta}=\sum_k g_k e^{ik\theta}=g.$$

最后验证单射：若 $$(\lambda I-D)f=0$$，对 Fourier 系数作用得 $$(\lambda-ik)f_k=0$$；$$\lambda\notin i\mathbb{Z}$$ 故每个 $$f_k=0$$，$$f=0$$。所以 $$\lambda I-D$$ 是双射且有界逆，$$\lambda\notin\sigma(D)$$。$$\blacksquare$$

**由此，推论 3.9 也被补全**：$$D^2f=\mu f$$ 时把 $$f$$ 按 Fourier 展开，逐频率得 $$(ik)^2f_k=\mu f_k$$，故 $$f_k=0$$ 除非 $$-k^2=\mu$$；所以 $$\sigma(D^2)=\{-k^2:k\in\mathbb{Z}\}$$，一个不漏。

**三点必须说清（诚实清单）**：

1. **$$D$$ 是无界算子**。因为 $$D e^{ik\theta}=ik\,e^{ik\theta}$$ 而 $$\lvert ik\rvert\to\infty$$：特征值无界，算子必无界。无界算子的完整理论（图像、闭性、预解式）见第 42 章。本章只用到"预解式 $$\lambda\mapsto(\lambda I-D)^{-1}$$ 存在且范数被 $$\delta^{-1}$$ 控制"这一半，且是显式构造的，不依赖任何一般定理。
2. **"谱"的完整定义**（含"谱非空且紧"）见第 36 章；定理 3.11 是它可直接手算的实例。对照点：乘法算子会出现**无特征值的连续谱**（第 36 章），而 $$D$$ 的谱干净得只有特征值。
3. **$$\{e^{ik\theta}\}$$ 的完备性**是用到的、但本章不证的事实，属于第 30 章。

### 3.6 复结构：$$i$$ 的真身

现在回答入口题的 (a) 与 (c)，并给 $$i$$ 一个坐标无关的定义。

**定义（复结构）**。设 $$V$$ 是有限维实向量空间。一个**复结构 (complex structure)** 是线性映射 $$J:V\to V$$ 满足

$$J^2=-\mathrm{id}_V.$$

**定理 3.12**。若 $$V\ne0$$ 存在复结构，则 $$\dim V$$ 为偶数。

*证明思路*：对 $$J^2=-\mathrm{id}$$ 两边取行列式，左边必然是"某实数的平方"，右边是 $$\pm1$$，比较符号。

*证明*：$$\det(J)^2=\det(J^2)=\det(-\mathrm{id}_V)=(-1)^n$$，其中 $$n=\dim V$$（因为 $$n\times n$$ 的 $$-\mathrm{id}$$ 相当于把每一行乘 $$-1$$，行列式是 $$(-1)^n$$）。而 $$\det J$$ 是实数，故 $$\det(J)^2\ge0$$。于是 $$(-1)^n\ge0$$，即 $$n$$ 为偶数。$$\blacksquare$$

反向也成立：$$n=2m$$ 时取 $$m$$ 个 $$J$$ 的直和即可（见经典问题 1）。

**定理 3.13**。复结构 $$J$$ 使 $$V$$ 成为一个复向量空间。具体地，定义

$$(a+bi)\cdot v:=av+b\,Jv\qquad(a,b\in\mathbb{R},\ v\in V),$$

则此作用满足复向量空间的全部公理。

*证明思路*：只需验证$$(a+bi)(c+di)=((ac-bd)+(ad+bc)i)$$这个乘法关系在作用上保持——也就是验证两种结合顺序给出同一结果。$$J^2=-\mathrm{id}$$ 正是为此而设。

*证明*：向量加法与实数数乘的公理由 $$V$$ 本身的向量空间结构直接继承（逐项验算 $$(a+bi)\cdot(v+w)=av+aw+bJv+bJw$$ 即可）。剩下的关键是验证复标量乘法的**结合律**：

$$\big((a+bi)(c+di)\big)\cdot v=\big((ac-bd)+(ad+bc)i\big)\cdot v=(ac-bd)v+(ad+bc)Jv,$$

而

$$(a+bi)\cdot\big((c+di)\cdot v\big)=(a+bi)\cdot(cv+dJv)=a(cv+dJv)+bJ(cv+dJv)$$
$$=ac\,v+ad\,Jv+bc\,Jv+bd\,J^2v=(ac-bd)v+(ad+bc)Jv.$$

两者相等（倒数第二步把 $$bdJ^2v$$ 换成 $$-bd\,v$$，这正是 $$J^2=-\mathrm{id}$$）。乘法单位元是 $$1+0i$$，其作用为恒同；分配律逐项展开即得。故 $$V$$ 是复向量空间，$$\dim_\mathbb{C}V=\tfrac12\dim_\mathbb{R}V$$。$$\blacksquare$$

**于是**：

- 定理 3.5 的生成元 $$J=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}$$ **就是 $$\mathbb{R}^2$$ 上的标准复结构**。配了 $$J$$ 的 $$\mathbb{R}^2$$ 就是 $$\mathbb{C}$$：对应关系是 $$\begin{bmatrix}a\\ b\end{bmatrix}\leftrightarrow a+bi$$，"作用 $$J$$"就是"乘以 $$i$$"。
- 定理 3.3 的 $$\dfrac{d\rho}{d\theta}=J\rho$$ 于是可以读作：**在 $$SO(2)$$ 上求导 = 乘以虚数单位。**
- 定理 3.11 的谱线 $$\lambda=ik$$ 则是同一件事在函数空间上的展开：$$D e^{i\theta}=i\,e^{i\theta}$$，$$i$$ 现身了。

**所以"$$i$$ 从哪来"的答案是**：$$i$$ **不是**从"$$\sqrt{-1}$$ 这个不存在的数"来的，$$i$$ 是 $$\mathbb{R}^2$$ 上的一个**线性算子**（旋转 $$90^\circ$$）。当这个算子被写成"数"时，我们叫它 $$i$$；当它被写成矩阵时，我们叫它 $$J$$；当它作为求导算子的特征值时，我们叫它 $$ik$$ 里的那个因子。第 02 章从"复数乘法"一侧看到 $$i^2=-1$$；本章从"求导"一侧看见同一个东西——**两条线在复结构上会合。**

**偿还第 02 章的悬念：$$R_\theta$$ 的谱为什么落在单位圆上。**

第 02 章 §3.1 与研究题 1 观察到一件事：$$R_\theta$$ 在实方向上"看不见"特征方向（$$\theta\notin\pi\mathbb{Z}$$ 时它没有实特征值），可是一旦允许复特征值，它立刻分裂成两个纯伸缩，伸缩因子是 $$e^{\pm i\theta}$$——两个都落在**单位圆**上。第 02 章把它作为悬念留给了本章。

这个悬念现在可以精确地回答，而且它和本章的 $$D$$ 是同一句话的两种说法。

**第一步，直接验证谱。** 两个向量 $$\begin{bmatrix}1\\ -i\end{bmatrix}$$ 与 $$\begin{bmatrix}1\\ i\end{bmatrix}$$ 是 $$R_\theta$$ 的复特征向量：

$$R_\theta\begin{bmatrix}1\\ -i\end{bmatrix}=\begin{bmatrix}\cos\theta+i\sin\theta\\ \sin\theta-i\cos\theta\end{bmatrix}=e^{i\theta}\begin{bmatrix}1\\ -i\end{bmatrix},\qquad
R_\theta\begin{bmatrix}1\\ i\end{bmatrix}=\begin{bmatrix}\cos\theta-i\sin\theta\\ \sin\theta+i\cos\theta\end{bmatrix}=e^{-i\theta}\begin{bmatrix}1\\ i\end{bmatrix}$$

（两处都用 $$\sin\theta\mp i\cos\theta=\mp i(\cos\theta\pm i\sin\theta)$$ 与 $$e^{\pm i\theta}=\cos\theta\pm i\sin\theta$$ 整理）。因此

$$\sigma(R_\theta)=\{\,e^{i\theta},\ e^{-i\theta}\,\}\subseteq S^1.$$

**第二步，说明"恰好"落在单位圆上——这才是悬念的答案。** 由定理 3.6，$$R_\theta=\exp(\theta J)$$；而 $$\theta J$$ 满足 $$(\theta J)^2=-\theta^2I$$，故它的特征值 $$\lambda$$ 必满足 $$\lambda^2=-\theta^2$$，即

$$\sigma(\theta J)=\{\,i\theta,\ -i\theta\,\}\subset i\mathbb{R}\qquad(\text{purely imaginary}).$$

指数映射把加法变成乘法、并按**谱映射定理 (spectral mapping theorem)**（见第 36 章）把谱也搬上指数：

$$\exp:\ i\mathbb{R}\ \longrightarrow\ S^1,\qquad i\omega\ \mapsto\ e^{i\omega}$$

（虚轴被指数映射卷成单位圆）。于是链条是：

$$\sigma(\theta J)=\{\pm i\theta\}\subset i\mathbb{R}\ \xrightarrow{\ \exp\ }\ \sigma(R_\theta)=\{e^{\pm i\theta}\}\subset S^1.$$

**第三步，这和 $$D$$ 是什么关系。** $$D$$ 的谱是 $$i\mathbb{Z}$$（定理 3.11）——同样在虚轴上。这不是巧合：$$\theta J$$ 是 $$D$$ 的"无穷小版本"（§3.7 的链条第 2、4 步），两者都活在 Lie 代数一侧；而 $$R_\theta$$ 活在群一侧。**谱在虚轴上（Lie 代数侧）$$\longleftrightarrow$$ 谱在单位圆上（群侧），$$\exp$$ 就是这座桥。**

由此也能校准第 02 章那句"$$SO(2)$$ 的谱恰好铺满单位圆"的**精确含义**：单个 $$R_\theta$$ 的谱只有两个点 $$\{\pm e^{i\theta}\}$$；是**让 $$\theta$$ 跑遍 $$\mathbb{R}$$** 时，这族二点集才扫满 $$S^1$$。而 $$D$$ 一侧的"整数频率" $$\sigma(D)=i\mathbb{Z}$$ 只对应单位圆上一串**离散**的点 $$\{e^{ik}:k\in\mathbb{Z}\}$$——那是**频率的量子化**（单值性的产物），与"铺满"是两回事。

**一句话**：$$R_\theta$$ 的谱 $$\{e^{\pm i\theta}\}$$ 与 $$D$$ 的谱 $$i\mathbb{Z}$$ 不是两个结果，而是同一个复结构在两个尺度下的影子——一个是"转一圈"（群层面），一个是"求一次导"（Lie 代数层面），$$\exp$$ 位于两者之间。

**入口题的 (a)(b)(c)(d) 现在可以一次解掉**：

- (a)：$$A^2=-I$$ 的 $$2\times2$$ 实矩阵，**就是 $$\mathbb{R}^2$$ 上的复结构**（按定理 3.12 的证明，$$n=2$$ 是允许的最小偶数）。所有这样的 $$A$$ 都相似于 $$J$$（经典问题 1）。而 $$SO(2)$$ 的 Lie 代数生成元是这个集合中最特殊的一个：它是 $$\rho$$ 在 $$I$$ 处的速度（定理 3.3），也是 $$\exp$$ 的生成元（定理 3.6）。
- (b)：$$D$$ 的特征值是 $$ik$$（$$k\in\mathbb{Z}$$），本征函数 $$e^{ik\theta}$$；$$D^2$$ 的特征值是 $$-k^2$$（定理 3.8、推论 3.9）。
- (c)：在 $$W=\mathrm{span}_\mathbb{R}\{\cos\theta,\sin\theta\}$$ 上（$$W$$ 在 $$D$$ 下不变，因为 $$D\cos\theta=-\sin\theta$$、$$D\sin\theta=\cos\theta$$），以 $$(\cos\theta,\sin\theta)$$ 为基，$$D$$ 的矩阵是

  $$\begin{bmatrix}0&1\\ -1&0\end{bmatrix}=-J,\qquad(-J)^2=-I.$$

  所以 **$$D$$ 限制在 $$W$$ 上恰好是一个复结构**（等于 $$-J$$，差一个定向）。$$D$$ 的两个复特征向量是 $$e^{i\theta}$$（特征值 $$i$$）与 $$e^{-i\theta}$$（特征值 $$-i$$），特征值集合 $$\{\pm i\}$$ 正好是 $$x^2=-1$$ 的两个根。
- (d)：**在整个 $$C^\infty_{2\pi}$$ 上 $$D^2\ne-I$$。** 理由：$$D1=0$$（常数的导数为零），故 $$D^2$$ 不是单射，而 $$-I$$ 是单射。等价地看谱：$$\sigma(D^2)=\{0,-1,-4,-9,\dots\}$$ 含 $$0$$，而 $$\sigma(-I)=\{-1\}$$——**"多出来的那条 $$k=0$$ 谱线"就是全部障碍。**

  **一个必须说清的分辨**：若只问"$$C^\infty_{2\pi}$$ 上**是否存在某个**线性算子 $$T$$ 使 $$T^2=-I$$"，答案是"存在"——例如令 $$T e^{ik\theta}=i\,e^{ik\theta}$$（$$k\ge0$$）、$$T e^{ik\theta}=-i\,e^{ik\theta}$$（$$k<0$$），这是一个合法的复结构。所以 (d) 问的**不是**"存在性"，而是"**$$D$$ 本身是不是**"。不是。$$D$$ 与复结构的差别可以被精确定位：**复结构要求在每一条谱线上都取 $$\pm i$$，而 $$D$$ 把 $$k=0$$ 那条送给了 $$0$$。** $$D$$ 的谱比 $$\{\pm i\}$$ 多了无穷多条线，这是它"不是复结构"的全部内容。

  换句话说：**复结构没有消失，它被"分摊"到了无穷多条谱线上；唯有最低的两条 $$\pm i$$ 合起来构成一个 $$2\times2$$ 的真复结构。** 这正是原专栏的话："为了实现两次求导得到特征值 $$\lambda=-1$$，需要让一次求导为复结构。"

**命名提醒**：$$D$$ 在 $$W$$ 上等于 $$-J$$ 而非 $$J$$，只是定向（orientation）问题——$$J$$ 与 $$-J$$ 都满足 $$J^2=-\mathrm{id}$$，都给出复结构。取基 $$(\sin\theta,\cos\theta)$$ 即得 $$+J$$。

### 3.7 一次总结：求导为什么给出谱

把这条链条完整写出：

1. $$SO(2)$$ 是一个 Lie 群（定理 3.1、3.2）；
2. 在单位元处求导，得到一维 Lie 代数 $$\mathfrak{so}(2)=\mathbb{R}J$$（定理 3.5）；
3. 生成元 $$J$$ 的作用被 $$J^2=-I$$ 完全刻画（推论 3.4）；
4. 把"沿群求导"搬到函数空间，得到算子 $$D$$（3.4 节）；
5. 求 $$D$$ 的特征值，得 $$\lambda=ik$$，$$k\in\mathbb{Z}$$（定理 3.8）；
6. 整数的来源是圆的单值性；$$i$$ 的来源是 $$J$$ 是复结构（3.6 节）；
7. 在群一侧，同一件事表现为 $$R_\theta$$ 的谱 $$\{e^{\pm i\theta}\}$$ 落在单位圆上——第 02 章的悬念由此还清（3.6 节末）。

一句话：**群的结构在求导下被线性化，线性化后的结构就是一个算子；算子的特征值与被特征函数反过来编码了群的几何。** 这就是"Lie 群的表示论"的原型，也是"算子谱理论"的原型——它们是同一件事的两端。

## 四、几何与物理直觉 (Intuition)

**几何：圆、直线与缠绕。**

$$SO(2)$$ 几何上就是圆周 $$S^1$$：把 $$R_\theta$$ 对应到角度 $$\theta$$ 就是圆上的坐标。$$\mathfrak{so}(2)$$ 是单位元处的切空间，几何上是 $$I$$ 点的一条切线，一条无限长的直线。指数映射

$$\exp:\ \mathbb{R}\ \longrightarrow\ S^1,\qquad \theta J\mapsto R_\theta$$

（左端是 $$\mathfrak{so}(2)$$ 这条直线，右端是 $$SO(2)$$ 这个圆）是把直线**匀速缠绕**到圆上的过程（定理 3.6）。缠一圈需要的长度是 $$2\pi$$，所以直线上的 $$0,\pm2\pi,\pm4\pi,\dots$$ 全部落到圆上的同一点 $$I$$。**整数 $$k$$ 就是"绕了几圈"。** 定理 3.8 说 $$D$$ 的特征值是 $$ik$$——也就是说，**圆上函数的"频率"是被圆的拓扑限定的，而不是被微分方程限定的**；这里的拓扑量正是 **绕数 (winding number)**。同一个方程 $$f'=\lambda f$$ 在直线上有任意复频率 $$\lambda$$，在圆上却只剩纯虚整数。这就是"几何约束谱"的第一个例子。

$$\rho$$ 的求导 $$\dfrac{d\rho}{d\theta}=J\rho$$ 也有一个漂亮的几何读法：$$SO(2)$$ 是一条曲线（参数 $$\theta$$），它的速度向量处处等于"把位置向左转 $$90^\circ$$"。**"位置 + 速度垂直"就是圆的特征方程**，而这里它被写成矩阵等式 $$J\rho$$。于是 $$J^2=-I$$ 就是"转两次 $$90^\circ$$ 等于反向"——这正是圆之所以为圆的原因。

**物理：振动与相空间。**

$$SO(2)$$ 是所有波动现象的骨架。物理里的自变量是时间 $$t$$，与角度 $$\theta$$ 只差一个单位换算（$$\theta=\omega t$$），于是 $$\rho(t)=R_{\omega t}$$、$$\tau(t)=e^{i\omega t}$$，而

$$D\rho=J\rho,\qquad D^2\rho=-\rho;\qquad D\tau=i\tau,\qquad D^2\tau=-\tau.$$

把 $$D$$ 作用在物理量 $$x(t)$$ 上，方程 $$\ddot x=\lambda x$$ 就是一个特征值问题。三种符号给出三种定性行为：

- **$$\lambda<0$$**：特征值 $$\pm i\omega$$（纯虚），解为 $$\cos\omega t$$ 与 $$\sin\omega t$$，相空间 $$(x,\dot x)$$ 上的轨道是**圆**（周期运动、简谐振动）；
- **$$\lambda=0$$**：特征值 $$0$$（二重），解为 $$1$$ 与 $$t$$，轨道是**直线**（惯性、匀速）；
- **$$\lambda>0$$**：特征值 $$\pm\omega$$（实），解为 $$e^{\pm\omega t}$$，轨道是**双曲线**（指数增长或衰减）。

中间的桥梁正是复结构：**$$\lambda<0$$ 对应于 $$D$$ 落在实轴外（纯虚谱），于是相空间上的向量场是 $$90^\circ$$ 旋转场，轨道必是圆。** 水平弹簧 $$m\ddot x=-kx$$ 在 $$k/m=1$$ 时就写作 $$\ddot x=-x$$，即 $$D^2=-I$$——**这个负号就是复结构**。反过来，倒扣的碗（不稳定平衡）给 $$\ddot x=+x$$，$$D^2=+I$$，解是实指数，轨道是双曲线。

阻尼振动是同样两条谱线的线性化：$$D$$ 的特征值从 $$i\omega$$ 挪到 $$-\gamma+i\omega$$（$$\gamma>0$$），**实部 = 衰减率，虚部 = 振荡频率**。量子力学里 $$e^{-iEt/\hbar}$$ 是同一读法：能量的实部决定相位、虚部决定寿命。

**三者的对应（本课程的主线）**：

- **几何**（圆 $$S^1$$、旋转）$$\longleftrightarrow$$ **物理**（周期运动、振动）$$\longleftrightarrow$$ **代数**（$$J^2=-I$$、$$\mathbb{C}$$）；
- **几何**（切空间、缠绕）$$\longleftrightarrow$$ **物理**（频率、角速度）$$\longleftrightarrow$$ **代数**（$$\mathfrak{so}(2)$$、$$\exp$$）；
- **几何**（圆上函数、特征模态）$$\longleftrightarrow$$ **物理**（谐波、Fourier 模态）$$\longleftrightarrow$$ **代数**（$$D$$ 的谱 $$i\mathbb{Z}$$）。

**前瞻（一句话）**：单参数酉群可写成 $$e^{itA}$$（$$A$$ 自伴）——这是 Stone 定理，它把 Schrödinger 演化与本章的指数映射接起来（第 19、23 章）。第 54 章把 $$SO(2)$$ 换成 $$SO(3)$$，那时 $$[X,Y]\ne0$$，BCH 公式出场。

## 五、经典问题精讲 (Classical Problems)

### 问题 1（入口题 (a) 的推广）：$$A^2=-I$$ 的 $$n\times n$$ 实矩阵

**考点**：极小多项式 (minimal polynomial) 与有理标准形 (rational canonical form)；复结构的分类。位置：定理 3.12 的自然延伸。

**解**：设 $$A$$ 是 $$n\times n$$ 实矩阵且 $$A^2=-I$$。于是 $$A$$ 满足多项式 $$x^2+1$$，故**极小多项式 (minimal polynomial)** $$\mu_A(x)$$ 整除 $$x^2+1$$。

因为 $$x^2+1$$ 在 $$\mathbb{R}$$ 上不可约，$$\mu_A$$ 只能是 $$x^2+1$$ 或 $$1$$。若 $$\mu_A=1$$ 则 $$A=0$$，与 $$A^2=-I$$ 矛盾；故 $$\mu_A(x)=x^2+1$$。

这立即说明 $$A$$ **没有实特征值**：若有实 $$\lambda$$ 与 $$v\ne0$$ 使 $$Av=\lambda v$$，则 $$\lambda^2v=A^2v=-v$$，故 $$\lambda^2=-1$$，与 $$\lambda\in\mathbb{R}$$ 矛盾。所以**特征多项式 (characteristic polynomial)** $$\chi_A$$ 没有实根，而它是实系数多项式，故每个不可约因子是二次的；又 $$\mu_A\mid\chi_A$$（极小多项式整除特征多项式），于是

$$\chi_A(x)=(x^2+1)^{n/2},$$

特别地 $$n$$ 必为**偶数**。由**有理标准形 (rational canonical form)**定理，实矩阵在相似下由**不变因子 (invariant factor)** 决定。因为 $$x^2+1$$ 在 $$\mathbb{R}$$ 上不可约，**初等因子 (elementary divisor)** 与不变因子一致，都只能是 $$x^2+1$$ 的方幂；而 $$\mu_A=x^2+1$$ 说明没有高于一次的方幂，于是初等因子恰是 **$$\tfrac n2$$ 个 $$x^2+1$$**。每个初等因子 $$x^2+1$$ 对应的块是它的**伴侣矩阵 (companion matrix)**，即 $$J$$。故

$$A\ \sim\ \underbrace{J\oplus J\oplus\cdots\oplus J}_{n/2\ \text{copies}},\qquad J=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}.$$

**结论**：$$A^2=-I$$ 有解当且仅当 $$n$$ 偶；此时"$$\mathbb{R}^n$$ 上复结构"全体在 $$GL(n,\mathbb{R})$$ 作用下构成**一个**共轭类，代表元是 $$\mathrm{diag}(J,\dots,J)$$。特别地：**同一个阶数的所有解都互相相似**（这是有理标准形的"唯一性"给出的，不是巧合）。

行列式：由 $$A\sim\mathrm{diag}(J,\dots,J)$$ 与 $$\det J=1$$ 立得 $$\det A=1$$（也可直接验算：$$\det(A)^2=\det(A^2)=\det(-I)=(-1)^n$$，$$n$$ 偶时给出 $$\det A=\pm1$$；再加上"与 $$\mathrm{diag}(J,\dots,J)$$ 相似"就定出符号为 $$+$$）。注意 **$$\det A$$ 永远等于 $$1$$**，与 $$n\equiv0$$ 还是 $$2\pmod4$$ 无关。

$$n=2$$ 的特例即入口题：$$A=\begin{bmatrix}p&q\\ r&-p\end{bmatrix}$$，$$p^2+qr=-1$$（等价于 $$\mathrm{tr}\,A=0$$、$$\det A=1$$），全部与 $$J$$ 相似。

### 问题 2：$$SO(2)$$ 与 $$\mathbb{R}$$ 不同构

**考点**：局部同构 vs 整体同构；覆盖群。位置：定理 3.2、3.7；通向第 25、27 章。

**解**：$$\rho:\mathbb{R}\to SO(2)$$ 是满同态（定理 3.2），且是光滑的、在 $$0$$ 处导数非零（$$\rho'(0)=J\ne0$$）。由反函数定理，$$\rho$$ 在 $$0$$ 附近是局部微分同胚。所以两者**局部同构**。

但它们**整体不同构**：若是群同构，则必是单射；而 $$\rho(0)=\rho(2\pi)=I$$，$$\rho$$ 不单。等价地，$$\ker\rho=2\pi\mathbb{Z}\ne0$$。

一般原则：从 $$\mathbb{R}$$ 到群 $$G$$ 的**单参数子群 (one-parameter subgroup)** $$\gamma$$ 若不单，其核必是 $$\mathbb{R}$$ 的离散子群，即 $$a\mathbb{Z}$$（$$a>0$$）。理由是 $$\mathbb{R}$$ 的加法结构的离散子群只有 $$\{0\}$$ 与 $$a\mathbb{Z}$$（对任意非零元取最小的正元 $$a$$，再做除法）。于是 $$\gamma$$ 诱导同构 $$\mathbb{R}/a\mathbb{Z}\cong\mathrm{im}\,\gamma$$，而 $$\mathbb{R}/a\mathbb{Z}\cong S^1$$（重标度 $$\theta\mapsto a\theta$$）。所以**任何非单的单参数子群都落在某个圆上**——这就是"指数映射把直线卷成圆"的一般定理。

### 问题 3：$$D$$ 的反自伴性与 $$\sigma(D)=i\mathbb{Z}$$

**考点**：分部积分；谱的可逆性定义；Fourier 对角化。位置：定理 3.10、3.11 的重做，但要求把每一步的理由写清。

**解**：

（1）反自伴。设 $$f,g\in C^\infty_{2\pi}$$。

$$\langle Df,g\rangle=\frac{1}{2\pi}\int_0^{2\pi}f'\overline{g}\,d\theta=\frac{1}{2\pi}\Big[f\overline{g}\Big]_0^{2\pi}-\frac{1}{2\pi}\int_0^{2\pi}f\overline{g'}\,d\theta=-\langle f,Dg\rangle.$$

第一个等号是内积定义；第二个等号是分部积分（$$(f\overline g)'=f'\overline g+f\overline{g'}$$ 移项）；第三个等号用了周期性。于是 $$D^*=-D$$，特别地 $$iD$$ 是自伴的（$$(iD)^*=\overline{i}D^*=(-i)(-D)=iD$$）。**这是把 $$D$$ 搬进自伴算子理论的标准手法**，第 38 章的谱定理因此可以作用于 $$iD$$。

（2）谱。由定理 3.8，$$\{ik\}\subseteq\sigma_p(D)\subseteq\sigma(D)$$。反之，若 $$\lambda=\alpha+i\beta\notin i\mathbb{Z}$$（$$\alpha\ne0$$ 或 $$\beta\notin\mathbb{Z}$$），则 $$d_\lambda:=\min_k\lvert ik-\lambda\rvert>0$$（因 $$i\mathbb{Z}$$ 闭、$$ik\to\infty$$）。对 $$g=\sum g_ke^{ik\theta}$$ 取 $$f=\sum g_k(ik-\lambda)^{-1}e^{ik\theta}$$，有 $$\lVert f\rVert\le d_\lambda^{-1}\lVert g\rVert$$ 且 $$(\lambda I-D)f=g$$；同法得单射。故 $$\lambda\notin\sigma(D)$$。

**结论**：$$\sigma(D)=i\mathbb{Z}$$，全部是特征值，特征函数 $$e^{ik\theta}$$。

**一个副产品**（值得单独记住）：$$\lVert(\lambda I-D)^{-1}\rVert\le\mathrm{dist}(\lambda,i\mathbb{Z})^{-1}$$。这恰好是第 36 章一般定理 $$\lVert(\lambda I-T)^{-1}\rVert\ge\mathrm{dist}(\lambda,\sigma(T))^{-1}$$ 取等号的情形——对正规算子（$$iD$$ 自伴），预解式的范数**恰由到谱的距离控制**。

### 问题 4：三种符号，三种运动

**考点**：特征值与微分方程定性行为的对应。位置：第四节那三条定性描述的严格化。

**解**：设 $$x\in C^\infty(\mathbb{R})$$ 满足 $$\ddot x=\lambda x$$，$$\lambda\in\mathbb{R}$$。

$$\lambda<0$$：写 $$\lambda=-\omega^2$$（$$\omega>0$$）。由推论 3.9 的算法（此处在直线上），$$e^{\pm i\omega t}$$ 都是解，且通解为

$$x(t)=a\cos\omega t+b\sin\omega t.$$

能量 $$E=x^2+\dot x^2/\omega^2$$ 满足 $$\dot E=2x\dot x+2\dot x\ddot x/\omega^2=2\dot x(x+\ddot x/\omega^2)=0$$，故轨道在相平面 $$(x,\dot x)$$ 上是一条椭圆（换标度后是圆）——**有界、周期**。

$$\lambda=0$$：$$\ddot x=0$$，$$x=a+bt$$，**匀速直线运动**，无界。

$$\lambda>0$$：写 $$\lambda=\omega^2$$，通解 $$x=ae^{\omega t}+be^{-\omega t}$$——**除 $$a=b=0$$ 外都指数发散或衰减**。

$$\lambda<0$$ 的情形还可以换个坐标看：把 $$y=\dot x/\omega$$ 当作第二坐标，则 $$\dot x=\omega y$$、$$\dot y=\ddot x/\omega=-\omega x$$，即

$$\frac{d}{dt}\begin{bmatrix}x\\ y\end{bmatrix}=\omega\begin{bmatrix}0&1\\ -1&0\end{bmatrix}\begin{bmatrix}x\\ y\end{bmatrix}=-\omega J\begin{bmatrix}x\\ y\end{bmatrix}.$$

方程右端的矩阵是 $$-\omega J$$，$$(-\omega J)^2=-\omega^2I$$——**相空间上的速度场就是一个复结构的倍数**，所以轨道是圆。这就是"$$\lambda<0$$ 时为什么必然振动"的代数原因。

### 问题 5：算子 $$T=aD^2+bD+cI$$ 的谱与可逆性

**考点**：谱 = 可逆性的语言；微分方程解的存在唯一性。位置：第 3.5 节的直接应用；通向第 36 章。

**解**：设 $$a,b,c\in\mathbb{R}$$，$$T=aD^2+bD+cI$$。由定理 3.8、3.11，

$$Te^{ik\theta}=(-ak^2+ibk+c)\,e^{ik\theta},$$

故 $$\sigma(T)=\{\,c-ak^2+ibk\ :\ k\in\mathbb{Z}\,\}$$，且每个都是特征值。**$$T$$ 可逆当且仅当 $$0\notin\sigma(T)$$**，即

$$c-ak^2+ibk\ne0\qquad(\text{for all}\ k\in\mathbb{Z}).$$

分情形：

- 若 $$b\ne0$$：$$c-ak^2+ibk=0$$ 要求虚部 $$bk=0$$，即 $$k=0$$；代回得 $$c=0$$。所以 **$$b\ne0$$ 时 $$T$$ 可逆 $$\iff c\ne0$$**。
- 若 $$b=0$$：条件为 $$c\ne ak^2$$ 对一切 $$k\in\mathbb{Z}$$。$$k=0$$ 给出 $$c\ne0$$；$$k\ne0$$ 给出（$$a\ne0$$ 时）$$c/a\notin\{1,4,9,\dots\}$$。所以 **$$b=0$$ 时 $$T$$ 可逆 $$\iff c\ne0$$ 且（$$a=0$$ 或 $$c/a\notin\{k^2:k\ge1\}$$）**。

当 $$T$$ 可逆时，解 $$Tu=g$$ 就是逐频率相除：$$u=\sum_k g_k/(c-ak^2+ibk)\,e^{ik\theta}$$，且范数控制在 $$\mathrm{dist}(0,\sigma(T))^{-1}$$ 内。**注意 $$T$$ 可逆性的判据是"$$\lambda=0$$ 是不是特征值"——这已经是谱理论的完整语言了，只是还差一个抽象定义（第 36 章）。**

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 用定义验证 $$R_\alpha R_\beta=R_{\alpha+\beta}$$ 与 $$R_\theta^{-1}=R_{-\theta}$$，并指出这两条分别对应 $$SO(2)$$ 的哪两条群公理。

**基2.** 验证 $$\mathfrak{so}(2)=\{aJ:a\in\mathbb{R}\}$$，写出 $$\exp(aJ)$$ 的显式形式，并说明 $$\exp:\mathfrak{so}(2)\to SO(2)$$ 不是单射。

**基3.** 求 $$J$$ 的极小多项式与特征多项式（作为实矩阵与作为复矩阵分别回答），并用它核对定理 3.12 在 $$n=2$$ 时的结论。

### 竞赛（本课目标难度）

**竞1.** 设 $$A,B$$ 是 $$2\times2$$ 实矩阵，$$A^2=B^2=-I$$。证明存在 $$P\in GL(2,\mathbb{R})$$ 使 $$B=P^{-1}AP$$。再作对比：$$A^2=B^2=I$$ 的 $$2\times2$$ 实矩阵**不**都具有这一性质——给出两个都满足 $$C^2=I$$ 却互不相似的例子，并指出极小多项式在两种情形里分别起了什么作用。

**竞2.** 不用 Fourier 级数，证明：若 $$f\in C^2(\mathbb{R})$$ 满足 $$f''=-f$$，则 $$f(t)=f(0)\cos t+f'(0)\sin t$$。

**竞3.** 设 $$f\in C^\infty_{2\pi}$$ 满足 $$f'=\lambda f$$，$$\lambda\in\mathbb{C}$$。**不使用**本章任何结论，从头证明 $$\lambda\in i\mathbb{Z}$$。

**竞4.** 对 $$\alpha\in\mathbb{R}$$ 定义平移算子 $$(T_\alpha f)(\theta)=f(\theta+\alpha)$$。

(i) 求 $$T_\alpha$$ 的全部特征值与特征函数；

(ii) 证明 $$T_\alpha$$ 与 $$D$$ 交换（即 $$T_\alpha D=DT_\alpha$$），并说明此处由"交换 + 可对角化"能否推出它们有共同的 Fourier 特征函数组；

(iii) 证明 $$T_\alpha$$ 是酉算子：$$\langle T_\alpha f,T_\alpha g\rangle=\langle f,g\rangle$$；并说明 $$T_\alpha$$ 有界而 $$D$$ 无界，为什么这件事不影响 (ii) 的交换性结论。

### 研究（通向下一章）

**研1.** **对偶空间上的复结构：逆变与协变的第一次分裂。**

设 $$V=\mathbb{R}^2$$，$$J=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}$$ 是它的复结构。对偶空间 $$V^*$$ 是全体线性泛函 $$\varphi:V\to\mathbb{R}$$。

(i) 由 $$(J^*\varphi)(v):=\varphi(Jv)$$ 定义 $$J^*:V^*\to V^*$$。证明 $$(J^*)^2=-\mathrm{id}$$，即 $$V^*$$ 也获得一个复结构。

(ii) 取 $$V$$ 的基 $$e_1,e_2$$ 与对偶基 $$e^1,e^2$$（$$e^i(e_j)=\delta^i_j$$），写出 $$J$$ 与 $$J^*$$ 在这两组基下的矩阵，并比较二者。

(iii) 设基变换为 $$e_i'=\sum_j a_i^{\ j}e_j$$，把系数记成矩阵 $$A=(a_i^{\ j})$$（第 $$i$$ 行第 $$j$$ 列元素为 $$a_i^{\ j}$$）。把 $$v\in V$$ 与 $$\varphi\in V^*$$ 分别写成 $$v=\sum_j v^je_j=\sum_i v'^ie_i'$$ 与 $$\varphi=\sum_j\varphi_je^j=\sum_i\varphi'_ie'^i$$。**证明**：

$$v'=(A^{-1})^{\mathsf{T}}v,\qquad \varphi'=A\varphi.$$

也就是说，两套分量的变换矩阵互为**逆转置**（$$A$$ 与 $$(A^{-1})^{\mathsf{T}}$$）。

(iv) 取 $$A=R_\theta$$（旋转），验证 $$(A^{-1})^{\mathsf{T}}=A$$，于是 (iii) 中两套变换律**恰好相同**——旋转群上你根本看不出区别。再取非正交的剪切 $$A=\begin{bmatrix}1&\tau\\ 0&1\end{bmatrix}$$（$$\tau\ne0$$），算出 $$(A^{-1})^{\mathsf{T}}$$ 并指出两套变换律在哪里分道扬镳。

**研2.** **环面上的 $$D$$（通向流形）。** 设 $$\mathbb{T}^2=S^1\times S^1$$，$$D=\dfrac{\partial}{\partial\theta_1}+\dfrac{\partial}{\partial\theta_2}$$。求 $$D$$ 的全部特征函数与特征值，计算 $$\ker D$$ 的维数，并回答：在 $$\mathbb{T}^2$$ 上，"$$D$$ 在某个 2 维实平面上等于一个复结构"这句话还成立吗？

### 解答 (Solutions)

**解 基1.** 直接作矩阵乘法（与定理 3.2 的证明同一个算式）：

$$R_\alpha R_\beta=\begin{bmatrix}\cos\alpha\cos\beta-\sin\alpha\sin\beta&-(\cos\alpha\sin\beta+\sin\alpha\cos\beta)\\ \sin\alpha\cos\beta+\cos\alpha\sin\beta&\cos\alpha\cos\beta-\sin\alpha\sin\beta\end{bmatrix}=R_{\alpha+\beta},$$

第二个等号是把这四个元素与 $$R_{\alpha+\beta}$$ 逐项比较得来的。右端仍形如 $$R_\gamma$$，故仍是 $$SO(2)$$ 的元素：这条验证的是**封闭性公理**，同时它就是定理 3.2 中 $$\rho$$ 的同态性。

在这条恒等式中取 $$\beta=-\alpha$$，得 $$R_\alpha R_{-\alpha}=R_0=I$$；再把 $$\alpha$$ 换成 $$-\alpha$$ 用一次，得 $$R_{-\alpha}R_\alpha=I$$。两式合起来即 $$R_{-\alpha}=R_\alpha^{-1}$$：这条验证的是**逆元公理**（并顺带说明 $$SO(2)$$ 对取逆封闭）。$$\blacksquare$$

**解 基2.** 两个方向都做，才能得到"等于"。

（必要性）设 $$\gamma(0)=I$$、$$\gamma$$ 光滑、$$X=\gamma'(0)$$。对恒等式 $$\gamma(t)^{\mathsf{T}}\gamma(t)=I$$ 求导并取 $$t=0$$，得 $$X^{\mathsf{T}}+X=0$$。写 $$X=\begin{bmatrix}p&q\\ r&s\end{bmatrix}$$，则

$$X^{\mathsf{T}}+X=\begin{bmatrix}2p&q+r\\ q+r&2s\end{bmatrix}=0\ \Longrightarrow\ p=s=0,\ r=-q,\ \text{即}\ X=qJ.$$

（充分性）任给 $$q\in\mathbb{R}$$，取 $$\gamma(t)=\exp(tqJ)$$。由定理 3.6，$$\exp(tqJ)=R_{qt}\in SO(2)$$；$$\gamma$$ 光滑、$$\gamma(0)=I$$，且由定理 3.3 求导得 $$\gamma'(t)=qJ\,R_{qt}$$，故 $$\gamma'(0)=qJ$$。所以每个 $$qJ$$ 都在切空间里。

于是 $$\mathfrak{so}(2)=\{qJ:q\in\mathbb{R}\}=\mathbb{R}J$$，一维。再任取 $$a\in\mathbb{R}$$，由定理 3.6（取 $$\theta=a$$）：

$$\exp(aJ)=I\cos a+J\sin a=\begin{bmatrix}\cos a&-\sin a\\ \sin a&\cos a\end{bmatrix}=R_a.$$

非单射：$$R_a=I$$ 当且仅当 $$\cos a=1$$ 且 $$\sin a=0$$（与单位矩阵逐项比较），即 $$a\in2\pi\mathbb{Z}$$。取 $$a=0$$ 与 $$a=2\pi$$，得到 $$\exp(0)=\exp(2\pi J)=I$$，而 $$0\ne2\pi$$，所以 $$\exp$$ 不是单射。$$\blacksquare$$

**解 基3.** （作为复矩阵）$$\chi_J(x)=\det(xI-J)=\det\begin{bmatrix}x&1\\ -1&x\end{bmatrix}=x^2+1$$，故 $$J$$ 在 $$\mathbb{C}$$ 上恰有两个特征值 $$i$$ 与 $$-i$$，互异，于是 $$J$$ 可对角化，极小多项式是这两个根的一次式之积：

$$\mu_J(x)=(x-i)(x+i)=x^2+1.$$

（作为实矩阵）同一个算式给出实系数特征多项式 $$\chi_J(x)=x^2+1$$。它在 $$\mathbb{R}$$ 上不可约，故 $$J$$ 没有实特征值。极小多项式整除 $$\chi_J$$ 且不为常数（$$J\ne0$$，不满足 $$\mu\equiv1$$），所以仍为 $$\mu_J=x^2+1$$。

核对定理 3.12：$$n=2$$ 时

$$\det(J)^2=\det(J^2)=\det(-I_2)=(-1)^2=1\ge0,$$

与定理 3.12 的证明中"$$(-1)^n$$ 必须非负"这一步一致；$$n=2$$ 正是不为零的最小偶数，而 $$J$$ 本身就给出了 $$\mathbb{R}^2$$ 上一个实打实的复结构（定理 3.13）。$$\blacksquare$$

**解 竞1.** **关键 leap**：决定一切的只有一句话——**$$x^2+1$$ 在 $$\mathbb{R}$$ 上不可约**。不可约意味着 $$A$$ 的极小多项式没有可挑的余地，于是 $$A^2=-I$$ 只有**一个**相似类；而 $$x^2-1=(x-1)(x+1)$$ 分裂，极小多项式可以在 $$x-1$$、$$x+1$$、$$(x-1)(x+1)$$ 三者之间挑，于是至少出现三个相似类。全部对比都落在这个点上。

第一部分。设 $$A^2=-I$$。若 $$Av=tv$$（$$v\ne0$$，$$t\in\mathbb{R}$$），两边再作用一次 $$A$$ 得 $$-v=A^2v=t^2v$$，即 $$t^2=-1$$，无实解。所以 $$A$$ **没有实特征向量**，特别地没有非零的 $$v$$ 使 $$Av$$ 与 $$v$$ 共线。

任取 $$v\ne0$$。由上一段，$$Av$$ 不是 $$v$$ 的实倍数，故 $$\{v,Av\}$$ 线性无关，构成 $$\mathbb{R}^2$$ 的一组基。在这组基下

$$A(v)=Av,\qquad A(Av)=A^2v=-v,$$

即 $$A$$ 的矩阵是 $$\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}=J$$。记 $$Q_A$$ 为以 $$v,Av$$ 为两列的矩阵（可逆），则 $$A=Q_AJQ_A^{-1}$$。对 $$B$$ 同样取 $$w\ne0$$，得 $$B=Q_BJQ_B^{-1}$$。令 $$P=Q_AQ_B^{-1}$$，则

$$P^{-1}AP=Q_BQ_A^{-1}\,A\,Q_AQ_B^{-1}=Q_BJQ_B^{-1}=B.$$

（这条推理与有理标准形是同一条：$$\{v,Av\}$$ 正是伴侣矩阵对应的循环基，而 $$x^2+1$$ 不可约迫使有理标准形只有唯一的不变因子。）

第二部分。取 $$C_1=I_2$$ 与 $$C_2=\mathrm{diag}(1,-1)$$，两者都满足 $$C^2=I$$。它们**不相似**：相似保持特征值集合不变，而 $$\sigma(C_1)=\{1\}$$（二重）、$$\sigma(C_2)=\{1,-1\}$$，两个集合不相等。

极小多项式的作用：$$\mu_{C_1}(x)=x-1$$，它是 $$(x-1)(x+1)$$ 的**真因子**；$$\mu_{C_2}(x)=(x-1)(x+1)$$ 才是完整的那一个。两者都分解为互异的一次因子（故都可对角化），但极小多项式不同，就落在不同的相似类里。

对照：$$x^2+1$$ 不可约，"取因子"没有自由度，所以只有一个类；$$x^2-1$$ 分裂，极小多项式有三种取法，于是有三个类（$$C=I$$、$$C=-I$$、$$C\sim\mathrm{diag}(1,-1)$$）。$$\blacksquare$$

**解 竞2.** **关键 leap**：卡点不在"解二阶方程"，而在**造一个非负的守恒量**。把 $$h$$ 配出来之后，$$h''=-h$$ 恰好让 $$h^2+h'^2$$ 的导数恒为零，"解唯一"就被换成了"能量为零"。这个能量正是本章第三节的复结构在起作用：$$t\mapsto(h,h')$$ 的导数就是把向量 $$(h,h')$$ 旋转 $$90^\circ$$，而 $$h^2+h'^2$$ 是旋转不变量。全程不用级数、不用 Fourier。

证明。令

$$h(t)=f(t)-f(0)\cos t-f'(0)\sin t.$$

由 $$\dfrac{d^2}{dt^2}\cos t=-\cos t$$ 与 $$\dfrac{d^2}{dt^2}\sin t=-\sin t$$，

$$h''(t)=f''(t)+f(0)\cos t+f'(0)\sin t=-f(t)+f(0)\cos t+f'(0)\sin t=-h(t).$$

初值：$$h(0)=f(0)-f(0)\cdot1-f'(0)\cdot0=0$$；又 $$h'(t)=f'(t)+f(0)\sin t-f'(0)\cos t$$，故 $$h'(0)=f'(0)-f'(0)=0$$。

令 $$E(t)=h(t)^2+h'(t)^2\ge0$$。则

$$E'(t)=2h(t)h'(t)+2h'(t)h''(t)=2h'(t)\bigl(h(t)+h''(t)\bigr)=2h'(t)\cdot0=0,$$

所以 $$E$$ 是常数，$$E(t)\equiv E(0)=0^2+0^2=0$$。两个平方项之和为零意味着两项都为零，即 $$h(t)=h'(t)=0$$ 对一切 $$t$$ 成立，故 $$h\equiv0$$，即

$$f(t)=f(0)\cos t+f'(0)\sin t.\qquad\blacksquare$$

**解 竞3.** **关键 leap**：一个积分因子 $$e^{-\lambda\theta}$$ 就把微分方程降成"导数等于零"，于是 $$f$$ 被逼成一只纯指数；剩下要做的只有一句话 $$e^{2\pi\lambda}=1$$——**整数是从这一步、从圆里长出来的，不是从方程里长出来的**。

证明。（若 $$f\equiv0$$，则任意 $$\lambda$$ 都满足方程，没有可证的内容；下文设 $$f\not\equiv0$$，这正是"特征函数必须非零"的要求。）令

$$g(\theta)=f(\theta)e^{-\lambda\theta}.$$

用指数函数求导法则 $$(e^{-\lambda\theta})'=-\lambda e^{-\lambda\theta}$$ 与题设 $$f'=\lambda f$$：

$$g'(\theta)=f'(\theta)e^{-\lambda\theta}+f(\theta)\bigl(-\lambda e^{-\lambda\theta}\bigr)=\bigl(f'(\theta)-\lambda f(\theta)\bigr)e^{-\lambda\theta}=0,$$

最后一个等号用了 $$f'=\lambda f$$。于是 $$g$$ 取常数值，记 $$g\equiv c$$，即 $$f(\theta)=ce^{\lambda\theta}$$；$$f\not\equiv0$$ 给出 $$c\ne0$$。

施加周期性（把 $$\theta$$ 换成 $$\theta+2\pi$$）：

$$c\,e^{\lambda(\theta+2\pi)}=f(\theta+2\pi)=f(\theta)=c\,e^{\lambda\theta}\ \Longrightarrow\ e^{2\pi\lambda}=1$$

（两边约去 $$ce^{\lambda\theta}$$，它不为零）。写 $$\lambda=\alpha+i\beta$$（$$\alpha,\beta\in\mathbb{R}$$），则 $$e^{2\pi\lambda}=e^{2\pi\alpha}e^{2\pi i\beta}$$ 的模是 $$e^{2\pi\alpha}$$、辐角是 $$2\pi\beta$$（模 $$2\pi$$）。它等于 $$1$$ 当且仅当模为 $$1$$ 且辐角为 $$0$$（模 $$2\pi$$）：$$e^{2\pi\alpha}=1\iff\alpha=0$$，且 $$2\pi\beta\in2\pi\mathbb{Z}\iff\beta\in\mathbb{Z}$$。因此 $$\lambda=i\beta\in i\mathbb{Z}$$。反之 $$\lambda=ik$$ 时 $$f=e^{ik\theta}$$ 确为非零的 $$2\pi$$ 周期解，故 $$i\mathbb{Z}$$ 就是全部答案。$$\blacksquare$$

**解 竞4.** **关键 leap**：三小问共用一个卡点——**交换性是纯代数的事（把两个映射复合一下即可），而公共特征基是要把基造出来的事**。(i) 的卡点在于"全部特征值"不能靠"猜一族解"得到，必须用 Fourier 系数的唯一性把可能的 $$\mu$$ 逐个筛掉；(ii) 的卡点是不许把有限维的"同时对角化"定理直接搬到无穷维（$$D$$ 无界、$$T_\alpha$$ 的特征子空间可以无限维），只能显式拿出 $$\{e^{ik\theta}\}$$；(iii) 的卡点是"积分在平移下不变"——这条正是酉性，也解释了为什么有界性根本不进入 (ii)。

(i) 直接代入：$$T_\alpha e^{ik\theta}=e^{ik(\theta+\alpha)}=e^{ik\alpha}e^{ik\theta}$$，所以 $$e^{ik\theta}$$ 是特征函数、$$e^{ik\alpha}$$ 是特征值。

证明"全部"：设 $$T_\alpha f=\mu f$$ 且 $$f\ne0$$。把 $$f$$ 展开为 Fourier 级数 $$f=\sum_kc_ke^{ik\theta}$$（$$\{e^{ik\theta}\}$$ 在 $$L^2(S^1)$$ 中完备，见 3.5 节），则

$$T_\alpha f=\sum_kc_ke^{ik\alpha}e^{ik\theta},\qquad \mu f=\sum_k\mu c_ke^{ik\theta}.$$

逐项比较 $$k$$-次 Fourier 系数（$$c_k=\langle f,e^{ik\theta}\rangle$$，3.5 节），得

$$(e^{ik\alpha}-\mu)c_k=0\qquad(k\in\mathbb{Z}).$$

$$f\ne0$$ 说明某个 $$c_k\ne0$$，于是 $$\mu=e^{ik\alpha}$$。所以

$$\sigma_p(T_\alpha)=\{\,e^{ik\alpha}:k\in\mathbb{Z}\,\}.$$

（重数：若 $$\alpha\notin2\pi\mathbb{Q}$$，这些值互不相同，每条谱线重数一；若 $$\alpha\in2\pi\mathbb{Q}$$，则 $$\{e^{ik\alpha}\}$$ 是有限循环群，每个成员都是特征值，且特征子空间是无穷维的。）

(ii) 对 $$f\in C^\infty_{2\pi}$$，

$$(T_\alpha Df)(\theta)=(Df)(\theta+\alpha)=f'(\theta+\alpha),$$
$$(DT_\alpha f)(\theta)=\frac{d}{d\theta}f(\theta+\alpha)=f'(\theta+\alpha).$$

两式逐点相等，故 $$T_\alpha D=DT_\alpha$$；这就是"求导是平移不变的"。

关于"交换 + 可对角化能否推出公共特征基"：**有限维**时成立。设 $$T,D$$ 交换且各自可对角化，取 $$T$$ 关于特征值 $$\mu$$ 的特征子空间 $$E_\mu$$；若 $$v\in E_\mu$$ 则 $$T(Dv)=D(Tv)=\mu(Dv)$$，故 $$Dv\in E_\mu$$，即 $$E_\mu$$ 是 $$D$$-不变子空间；$$D$$ 在其上的极小多项式仍分解为互异一次因子，故 $$D\rvert_{E_\mu}$$ 可对角化；把各 $$E_\mu$$ 的 $$D$$-特征基并起来就是公共特征基。

**无穷维**时这个论证不能照搬：此处 $$T_\alpha$$ 有界而 $$D$$ 无界，"$$D$$ 可对角化"本身就要用完备特征基来定义；而且有限维论证里还默认了一件事实——$$V$$ 是各特征子空间的直和（这正是"可对角化"的另一种说法），"并起来"才等于整个空间；对无界算子，特征子空间的代数直和一般不等于整个空间。本题不需要这个一般定理：$$\{e^{ik\theta}\}$$ 已是 $$L^2(S^1)$$ 的完备正交基（3.5 节），而它同时对角化 $$T_\alpha$$（上一条）与 $$D$$（定理 3.8），所以公共特征基是**显式构造**出来的。

(iii) 记 $$h(\theta)=f(\theta)\overline{g(\theta)}$$，它是 $$2\pi$$ 周期的。换元 $$u=\theta+\alpha$$：

$$\langle T_\alpha f,T_\alpha g\rangle=\frac{1}{2\pi}\int_0^{2\pi}h(\theta+\alpha)\,d\theta=\frac{1}{2\pi}\int_\alpha^{\alpha+2\pi}h(u)\,du.$$

由 $$h$$ 的 $$2\pi$$ 周期性，$$\int_\alpha^{\alpha+2\pi}h=\int_0^{2\pi}h$$（把区间按整周期切开再平移），故

$$\langle T_\alpha f,T_\alpha g\rangle=\frac{1}{2\pi}\int_0^{2\pi}f(u)\overline{g(u)}\,du=\langle f,g\rangle.$$

取 $$f=g$$ 得 $$\lVert T_\alpha f\rVert=\lVert f\rVert$$：$$T_\alpha$$ 是等距，因而有界，$$\lVert T_\alpha\rVert=1$$。

为什么有界与无界的差别不影响 (ii)：交换性 $$T_\alpha D=DT_\alpha$$ 是**复合算子**在公共定义域 $$C^\infty_{2\pi}$$ 上的恒等式（$$D$$ 与 $$T_\alpha$$ 都把 $$C^\infty_{2\pi}$$ 映入自身），验证它只用链式法则，不需要任何范数估计；有界性讲的是 $$L^2$$ 范数，是另一件事。$$\blacksquare$$

**解 研1.** (i) 对任意 $$\varphi\in V^*$$ 与 $$v\in V$$，

$$\bigl((J^*)^2\varphi\bigr)(v)=(J^*\varphi)(Jv)=\varphi\bigl(J(Jv)\bigr)=\varphi(J^2v)=\varphi(-v)=-\varphi(v).$$

右端对一切 $$v$$ 成立，故 $$(J^*)^2\varphi=-\varphi$$，即 $$(J^*)^2=-\mathrm{id}_{V^*}$$：$$V^*$$ 上也活着一个复结构。（这个论证没有用到 $$\mathbb{R}^2$$ 的特殊性，也没有用到内积——对任意线性 $$T$$ 都有 $$(T^*)^2=(T^2)^*$$。注意 $$J^*$$ 是**对偶映射**，与**伴随**不是同一件事。）

(ii) 取 $$e_1,e_2$$ 为标准基、$$e^1,e^2$$ 为对偶基（$$e^i(e_j)=\delta^i_j$$）。

$$J$$ 的矩阵：$$Je_1=e_2$$、$$Je_2=-e_1$$，故

$$[J]=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}=J.$$

$$J^*$$ 的矩阵：$$J^*e^i$$ 的坐标由"在 $$e_j$$ 上求值"读出，

$$(J^*e^1)(e_1)=e^1(Je_1)=e^1(e_2)=0,\qquad (J^*e^1)(e_2)=e^1(Je_2)=e^1(-e_1)=-1\ \Longrightarrow\ J^*e^1=-e^2,$$
$$(J^*e^2)(e_1)=e^2(e_2)=1,\qquad (J^*e^2)(e_2)=e^2(-e_1)=0\ \Longrightarrow\ J^*e^2=e^1,$$

故在对偶基下

$$[J^*]=\begin{bmatrix}0&1\\ -1&0\end{bmatrix}=J^{\mathsf{T}}=-J.$$

**比较**：$$[J]\ne[J^*]$$。要害不在那个符号，而在**它们是不同空间上的算子**：$$[J^*]$$ 作用在 $$V^*$$ 上，只有再选一个内积把 $$V^*$$ 与 $$V$$ 识别，才能与 $$V$$ 上的算子相比；在内积识别下 $$J^*$$ 对应的是 $$J$$ 的伴随，而 $$J$$ 反对称使伴随等于 $$J^{\mathsf{T}}=-J$$。这与定理 3.10 的 $$D^*=-D$$ 是同一件事。

(iii) 记 $$A=(a_i^{\ j})$$，即 $$e_i'=\sum_ja_i^{\ j}e_j=\sum_jA_{ij}e_j$$。

**向量**。把 $$v$$ 在两套基下写出并代入：

$$\sum_iv'^ie_i'=\sum_iv'^i\sum_jA_{ij}e_j=\sum_j\Bigl(\sum_iA_{ij}v'^i\Bigr)e_j.$$

与 $$\sum_jv^je_j$$ 比较（$$\{e_j\}$$ 是基，坐标唯一），得

$$v^j=\sum_iA_{ij}v'^i\qquad(j=1,2).$$

右端正是 $$A^{\mathsf{T}}v'$$ 的第 $$j$$ 个分量，即 $$v=A^{\mathsf{T}}v'$$。两边左乘 $$(A^{\mathsf{T}})^{-1}=(A^{-1})^{\mathsf{T}}$$，得

$$v'=(A^{-1})^{\mathsf{T}}v.$$

**泛函**。先注意对任意 $$\varphi$$ 与 $$w$$ 有 $$\varphi(w)=\sum_j\varphi_jw^j=\sum_i\varphi'_iw'^i$$（因为 $$e^j(w)=w^j$$、$$e'^i(w)=w'^i$$）。把已得的 $$v^j=\sum_ia_i^{\ j}v'^i$$ 代入 $$\sum_j\varphi_jv^j$$：

$$\sum_j\varphi_jv^j=\sum_j\varphi_j\sum_ia_i^{\ j}v'^i=\sum_i\Bigl(\sum_ja_i^{\ j}\varphi_j\Bigr)v'^i.$$

与 $$\sum_i\varphi'_iv'^i$$ 比较，得 $$\varphi'_i=\sum_ja_i^{\ j}\varphi_j=(A\varphi)_i$$，即

$$\varphi'=A\varphi.$$

两套律互为**逆转置**：$$A$$ 与 $$(A^{-1})^{\mathsf{T}}$$。

(iv) $$A=R_\theta$$：由 $$R_\theta^{\mathsf{T}}R_\theta=I$$ 得 $$R_\theta^{-1}=R_\theta^{\mathsf{T}}$$，故

$$(A^{-1})^{\mathsf{T}}=(A^{\mathsf{T}})^{\mathsf{T}}=A.$$

于是 (iii) 的两条律都化成 $$v'=Av$$、$$\varphi'=A\varphi$$，**逐字相同**：在保内积的变换上，逆变与协变无从分辨。

剪切 $$A=\begin{bmatrix}1&\tau\\ 0&1\end{bmatrix}$$（$$\tau\ne0$$）：$$\det A=1$$，故

$$A^{-1}=\begin{bmatrix}1&-\tau\\ 0&1\end{bmatrix},\qquad (A^{-1})^{\mathsf{T}}=\begin{bmatrix}1&0\\ -\tau&1\end{bmatrix}.$$

于是

$$v'=\begin{bmatrix}1&0\\ -\tau&1\end{bmatrix}v:\quad v'^1=v^1,\ \ v'^2=-\tau v^1+v^2;$$
$$\varphi'=\begin{bmatrix}1&\tau\\ 0&1\end{bmatrix}\varphi:\quad \varphi'_1=\varphi_1+\tau\varphi_2,\ \ \varphi'_2=\varphi_2.$$

两个矩阵不同（$$\tau\ne0$$），分道扬镳**就在这里**：向量分量被反向剪切，泛函分量被同向剪切。唯一不变的是两者的**配对**：

$$\sum_i\varphi'_iv'^i=(\varphi')^{\mathsf{T}}v'=(A\varphi)^{\mathsf{T}}\bigl((A^{-1})^{\mathsf{T}}v\bigr)=\varphi^{\mathsf{T}}A^{\mathsf{T}}(A^{-1})^{\mathsf{T}}v=\varphi^{\mathsf{T}}(A^{-1}A)^{\mathsf{T}}v=\varphi^{\mathsf{T}}v=\sum_i\varphi_iv^i$$

（用了 $$(XY)^{\mathsf{T}}=Y^{\mathsf{T}}X^{\mathsf{T}}$$，故 $$A^{\mathsf{T}}(A^{-1})^{\mathsf{T}}=(A^{-1}A)^{\mathsf{T}}=I$$）。$$\blacksquare$$

**接到第 06 章**：泛函一侧"按 $$A$$ 变"叫**协变 (covariant)**，向量一侧"按 $$(A^{-1})^{\mathsf{T}}$$ 变"叫**逆变 (contravariant)**；$$[J^*]=J^{\mathsf{T}}=-J$$ 是这种分裂在复结构上的第一次露面。正因为 $$SO(2)$$ 满足 $$A^{\mathsf{T}}=A^{-1}$$，整个第一卷都把两者压成了同一个东西。**为什么要两套分量法则、它们各自对应哪种几何对象**——第 06 章（对偶、逆变与协变）正是从这里开始。

**解 研2.** 设 $$m,n\in\mathbb{Z}$$。$$\mathbb{T}^2$$ 上的 Fourier 基是 $$e^{i(m\theta_1+n\theta_2)}$$，而

$$De^{i(m\theta_1+n\theta_2)}=im\,e^{i(m\theta_1+n\theta_2)}+in\,e^{i(m\theta_1+n\theta_2)}=i(m+n)\,e^{i(m\theta_1+n\theta_2)}.$$

所以特征函数是 $$e^{i(m\theta_1+n\theta_2)}$$，特征值是 $$i(m+n)$$，集合为

$$\sigma_p(D)=\{\,i(m+n):m,n\in\mathbb{Z}\,\}=\{\,ik:k\in\mathbb{Z}\,\}=i\mathbb{Z},$$

**作为集合与 $$S^1$$ 上的完全一样**。变的是重数：特征值 $$ik$$ 的特征子空间是

$$E_k=\overline{\mathrm{span}}\{\,e^{i(m\theta_1+n\theta_2)}:m+n=k\,\}=\overline{\mathrm{span}}\{\,e^{im(\theta_1-\theta_2)}e^{ik\theta_2}:m\in\mathbb{Z}\,\},$$

它由可数无穷多个线性无关的函数张成，维数是 $$\aleph_0$$。（对照 $$S^1$$：那里每条谱线是一维的。）

（一个容易搞错的地方：$$E_k$$ 的维数**不随** $$\lvert k\rvert$$ 增长，它对每个 $$k$$ 都是可数无穷维。随 $$\lvert k\rvert$$ 线性增长的是**截断计数**：在 $$\lvert m\rvert,\lvert n\rvert\le N$$ 内满足 $$m+n=k$$ 的格点数是 $$2N+1-\lvert k\rvert$$（$$\lvert k\rvert\le N$$），它是 $$N$$ 的线性函数。这是 $$\mathbb{Z}^2$$ 上的格点计数，与谱的重数是两回事。）

$$\ker D$$：$$Df=0$$ 等价于全部 $$m+n\ne0$$ 的 Fourier 系数为零，即

$$\ker D=\overline{\mathrm{span}}\{\,e^{im(\theta_1-\theta_2)}:m\in\mathbb{Z}\,\}=\{\,f: f=f(\theta_1-\theta_2)\,\},$$

"只依赖 $$\theta_1-\theta_2$$ 的 $$2\pi$$ 周期函数"全体。（也可直接换元：令 $$u=\theta_1+\theta_2$$、$$w=\theta_1-\theta_2$$，则 $$\partial_{\theta_1}+\partial_{\theta_2}=2\partial_u$$，于是 $$Df=0\iff\partial_uf=0\iff f=f(w)$$。）它的维数是 $$\aleph_0$$。对照 $$S^1$$ 上的 $$\ker D=\mathbb{C}\cdot1$$（定理 3.8 中 $$k=0$$ 的那一条），$$k=0$$ 这条线在 $$\mathbb{T}^2$$ 上膨胀了整整一个无穷维。

最后的问题："$$D$$ 在某个二维实平面上等于一个复结构"**仍然成立**。取

$$W=\mathrm{span}_\mathbb{R}\{\cos\theta_1,\ \sin\theta_1\}.$$

$$W$$ 在 $$D$$ 下不变：$$\partial_{\theta_2}\cos\theta_1=0$$、$$\partial_{\theta_1}\cos\theta_1=-\sin\theta_1$$，故 $$D\cos\theta_1=-\sin\theta_1\in W$$；同理 $$D\sin\theta_1=\cos\theta_1\in W$$。以 $$(\cos\theta_1,\sin\theta_1)$$ 为基，

$$D\rvert_W=\begin{bmatrix}0&1\\ -1&0\end{bmatrix}=-J,\qquad(-J)^2=-I,$$

所以 $$D\rvert_W$$ 是一个复结构。（一般地，在 $$W_{m,n}=\mathrm{span}_\mathbb{R}\{\cos(m\theta_1+n\theta_2),\ \sin(m\theta_1+n\theta_2)\}$$ 上 $$D$$ 的矩阵是 $$-(m+n)J$$，它是复结构当且仅当 $$\lvert m+n\rvert=1$$。）真正被 $$\mathbb{T}^2$$ "改坏"的不是这条二维平面，而是 $$k=0$$：复结构依旧活在那两条 $$\pm i$$ 谱线上，只是 $$0$$ 从一维长成了无穷维。

**接到第 06 章**：$$D=\partial_{\theta_1}+\partial_{\theta_2}$$ 是一个**向量场**（逆变对象），而它的谱来自它与特征函数 $$\varphi_{m,n}=m\theta_1+n\theta_2$$ 的微分（一个 1-形式，协变对象）的配对：

$$De^{i\varphi_{m,n}}=i\bigl\langle d\varphi_{m,n},\ \partial_{\theta_1}+\partial_{\theta_2}\bigr\rangle e^{i\varphi_{m,n}},\qquad \bigl\langle d\varphi_{m,n},\ \partial_{\theta_1}+\partial_{\theta_2}\bigr\rangle=m+n.$$

**向量场与 1-形式是两类不同的对象、它们的配对为什么不需要坐标**——第 06 章（对偶、逆变与协变）从这里接着讲。

## 七、Takeaway 与延伸 (Takeaways)

1. **求导 = 局部线性化。** $$\dfrac{d\rho}{d\theta}=J\rho$$ 把"分析操作（求导）"翻译成"代数操作（乘 $$J$$）"。这一招在第 54 章会升级成 Lie 代数的一般理论：**群的局部结构由一群矩阵（Lie 代数）编码**，而 $$SO(2)$$ 的 Lie 代数是一维的、括号恒为零的、最平凡也最基础的那一个。

2. **$$i$$ 是一个算子，不是一个数。** $$i$$ 的真身是 $$\mathbb{R}^2$$ 上的复结构 $$J$$（$$J^2=-\mathrm{id}$$）。它有三张脸：矩阵 $$J$$、虚数 $$i$$、求导算子的谱线 $$ik$$。第 02 章与本章从两侧夹逼到同一个对象。

3. **整数来自拓扑，不来自代数。** $$D$$ 的谱是 $$i\mathbb{Z}$$ 而不是整个虚轴，唯一的原因是函数活在一个**圆**上：单值性条件 $$e^{2\pi\lambda}=1$$ 把连续参数切成整数份。**谱在记录几何。**

4. **谱 = 可逆性的量度**，不只是"特征值清单"。定理 3.11 的证明（$$\lambda\notin\sigma\iff\lambda I-D$$ 有有界逆）已经是第 36 章谱定义的完整形态；第 38 章的谱定理会把 $$D$$ 这样的自伴/反自伴算子写成 $$\int\lambda\,dE(\lambda)$$。

5. **复结构 $$\leftrightarrow$$ 简谐振动。** $$\ddot x=-x$$ 里的那个负号就是复结构；它强制相空间轨道是圆。$$\ddot x=+x$$ 没有复结构可用，轨道是双曲线。物理中"振动"与"指数"的分野，代数上是"谱在虚轴上"与"谱在实轴上"的分野。

**下一章的悬念。** 本章我们把 $$J$$ 既当"向量上的算子"用，也当"作用于线性泛函的算子"用——练习研究题 1 让你亲手算出：$$V$$ 上的 $$J$$ 与 $$V^*$$ 上的 $$J^*$$ 用不同的变换律写分量，而这种分裂在 $$SO(2)$$ 里被正交性掩盖了。**同一个几何对象为什么需要两套分量法则？哪个是"逆变 (contravariant)"、哪个是"协变 (covariant)"？** 第 06 章（对偶、逆变与协变）从这个问题开始。

**延伸阅读。**

- 原专栏：MP2（平面旋转群 $$SO(2)$$ 的代数结构、群同构、指数函数）、MP3（$$SO(2)$$ 的求导、算子谱分析、复结构）。本章的链条取自 MP3 的核心论证。
- Chern, S.-S., *Complex Manifolds without Potential Theory*——原专栏引用此书记载复结构的定义。它指向的"近复结构 / Kähler 几何"本课程不单独设章；**辛结构**一支见第 08 章。
- Arnol'd, V. I., *Ordinary Differential Equations*——振动、相平面与特征值的几何图像，对应本章第四、五节。
- 专家参考：`algebra/lie-algebra-root-systems.md` §1（Lie 代数、括号、ad 映射）、`analysis/spectral-theory.md` §1、§3（谱、预解式、正规算子谱分类）。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch03_平面旋转群_SO_2_与算子的谱_上.md">← 第03章 平面旋转群 SO(2) 与算子的谱·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch05_对偶_逆变与协变_上.md">第05章 对偶、逆变与协变·上 →</a></div>
</div>
