---
layout: default
---

# 第03章: 平面旋转群 SO(2) 与算子的谱·上：预备与直觉 (The Rotation Group SO(2) and the Spectrum of an Operator · Part I: Warm-up and Intuition)

> 配套深化: 见 第04章 平面旋转群 SO(2) 与算子的谱·下（完整推导），本章是它的具体铺垫，建议先读本章
> 专家依据: algebra/lie-algebra-root-systems.md + analysis/spectral-theory.md（主）；方法论见 algebra/_SKILL.md 与 analysis/_SKILL.md
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

第04章要证明四件事，但对一个认真跟着算的普通读者来说，通往它们的路上各有一步走得太快。第一步：从"$$R^{\mathsf T}R=I$$ 且 $$\det R=1$$"直接跳到"$$R$$ 必然长成 $$\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}$$ 的样子"，中间"给定一个单位向量，与它正交的单位向量只有两个"这句话被当成不言自明。第二步：从"$$J^2=-I$$"跳到"$$R_\theta$$ 可以写成指数级数按奇偶拆开的和"，读者还没有亲眼看过 $$J$$ 的幂在具体角度下是怎么循环的。第三步：从"$$f'=\lambda f$$ 加上 $$2\pi$$ 周期性"一步跳到"$$\lambda$$ 必须是纯虚整数"，这一句压缩了"取模长"和"取辐角"两条独立的推理。第四步：$$D^*=-D$$ 的分部积分证明里，"边界项因为周期性而为零"这句判断常常被读者一带而过、不知道具体在算什么。

本章的任务只有一个：把这四步都先用 2–3 组具体的数字算一遍，让你在看到一般定理之前，已经用手做过一遍同样的事。读完本章，你应该已经能够：写出一个具体的旋转矩阵并验证它属于 $$SO(2)$$；算出 $$J$$ 的幂并发现它的周期性；算出 $$D$$ 在若干具体频率上的特征值，并且亲眼验证"半整数频率"为什么不能是周期函数；验证一个具体的反自伴恒等式。第04章会把这四件"手算过的事"升级成对所有情形都成立的一般定理与证明。

## 二、入口：一道具体的问题 (Entry Problem)

> 题目来源：**自编**，是第04章入口题的预热版——本题只要求算出答案、猜出规律，不要求给出一般证明。

**入口题。**

(a) 验证 $$\left(\dfrac35,\dfrac45\right)$$ 是平面上的一个单位向量。求出与它正交的两个单位向量。把 $$\left(\dfrac35,\dfrac45\right)$$ 作为第一列，把你求出的两个正交单位向量分别作为第二列，得到两个 $$2\times2$$ 矩阵；分别计算它们的行列式，指出哪一个属于 $$SO(2)$$。

(b) 记 $$J=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}$$。直接用矩阵乘法算出 $$J^2,J^3,J^4$$。再分别写出 $$R_{\pi/2},R_\pi,R_{3\pi/2},R_{2\pi}$$ 这四个具体的旋转矩阵，把它们和 $$J^1,J^2,J^3,J^4$$ 逐一对照，你发现了什么规律？

(c) 记 $$D=\dfrac{d}{d\theta}$$。直接求导算出 $$D(e^{i\theta}),\ D(e^{i2\theta}),\ D(e^{-i\theta})$$，把每一个结果写成"某个数乘以原函数"的形式，读出这个数。再检验：$$f(\theta)=e^{i\theta/2}$$ 是不是以 $$2\pi$$ 为周期的函数（即 $$f(\theta+2\pi)$$ 是否等于 $$f(\theta)$$）？根据这个检验，猜一猜"能让 $$e^{\lambda\theta}$$ 成为 $$2\pi$$ 周期函数"的 $$\lambda$$ 只能是哪些数。

(d) 取 $$f(\theta)=\cos\theta$$，$$g(\theta)=\sin\theta$$。直接算出
$$\frac{1}{2\pi}\int_0^{2\pi}f'(\theta)g(\theta)\,d\theta \qquad\text{与}\qquad -\frac{1}{2\pi}\int_0^{2\pi}f(\theta)g'(\theta)\,d\theta,$$
看它们是否相等。

**为什么这是同一道题。** (a) 是"具体验证一个矩阵属于 $$SO(2)$$"；(b) 是"具体验证 $$J$$ 的幂与旋转的关系"；(c) 是"具体验证求导算子的特征值"；(d) 是"具体验证一个积分恒等式"。这四问分别是第04章定理 3.1、定理 3.3–3.6、定理 3.8、定理 3.10 在具体数字下的影子——读完本章，你会看到这四个具体计算各自展开成什么样的一般陈述。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 从正交条件到旋转矩阵：先算三个具体例子

**回忆定义。** 实矩阵 $$R$$ 称为**正交矩阵 (orthogonal matrix)**，如果 $$R^{\mathsf T}R=I$$；如果还有 $$\det R=1$$，称它为**特殊正交矩阵 (special orthogonal matrix)**，全体这样的 $$2\times2$$ 矩阵构成**平面旋转群 (rotation group) $$SO(2)$$**。条件 $$R^{\mathsf T}R=I$$ 翻译成几何语言就是："$$R$$ 的两列是一组标准正交基"——这是因为把 $$R=[u\ v]$$（$$u,v$$ 是列向量）代入直接算，$$R^{\mathsf T}R=\begin{bmatrix}u\cdot u&u\cdot v\\ v\cdot u&v\cdot v\end{bmatrix}$$，这等于 $$I$$ 当且仅当 $$u\cdot u=v\cdot v=1$$ 且 $$u\cdot v=0$$。

在抽象地讨论"一般的单位向量"之前，我们先把这件事对三个具体向量各做一遍。

**例 1**：取 $$u=(1,0)$$。与 $$u$$ 正交的单位向量只有两个：$$(0,1)$$ 和 $$(0,-1)$$（因为与 $$(1,0)$$ 垂直的方向只有竖直方向，长度为 $$1$$ 的只有这两个）。
- 取 $$v=(0,1)$$：矩阵 $$\begin{bmatrix}1&0\\ 0&1\end{bmatrix}=I$$，$$\det=1$$。
- 取 $$v=(0,-1)$$：矩阵 $$\begin{bmatrix}1&0\\ 0&-1\end{bmatrix}$$，$$\det=-1$$。

**例 2**：取 $$u=(0,1)$$。与它正交的单位向量是 $$(-1,0)$$ 和 $$(1,0)$$。
- 取 $$v=(-1,0)$$：矩阵 $$\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}=J$$，$$\det=0\cdot0-(-1)\cdot1=1$$。
- 取 $$v=(1,0)$$：矩阵 $$\begin{bmatrix}0&1\\ 1&0\end{bmatrix}$$，$$\det=0-1=-1$$。

**例 3**（入口题 (a)）：取 $$u=\left(\dfrac35,\dfrac45\right)$$。先验证它确是单位向量：$$\left(\dfrac35\right)^2+\left(\dfrac45\right)^2=\dfrac9{25}+\dfrac{16}{25}=1$$。与它垂直的方向是"把 $$u$$ 的两个分量互换并改变一个符号"，即 $$\left(-\dfrac45,\dfrac35\right)$$ 和 $$\left(\dfrac45,-\dfrac35\right)$$（两者长度也都是 $$1$$，且都与 $$u$$ 点积为零：$$\dfrac35\cdot\left(-\dfrac45\right)+\dfrac45\cdot\dfrac35=-\dfrac{12}{25}+\dfrac{12}{25}=0$$）。
- 取 $$v=\left(-\dfrac45,\dfrac35\right)$$：矩阵 $$R=\begin{bmatrix}3/5&-4/5\\ 4/5&3/5\end{bmatrix}$$，$$\det R=\dfrac35\cdot\dfrac35-\left(-\dfrac45\right)\cdot\dfrac45=\dfrac9{25}+\dfrac{16}{25}=1$$。这一个属于 $$SO(2)$$。
- 取 $$v=\left(\dfrac45,-\dfrac35\right)$$：矩阵的行列式是 $$\dfrac35\cdot\left(-\dfrac35\right)-\dfrac45\cdot\dfrac45=-\dfrac9{25}-\dfrac{16}{25}=-1$$。这一个不属于 $$SO(2)$$。

**三个例子里都发生了同一件事**：给定单位向量 $$u=(a,c)$$，与它正交、长度为 $$1$$ 的向量只有 $$(-c,a)$$ 和 $$(c,-a)$$ 两个（把 $$u$$ 旋转 $$+90^\circ$$ 或 $$-90^\circ$$）；取 $$(-c,a)$$ 那个，行列式总是 $$a^2+c^2=1$$；取另一个，行列式总是 $$-(a^2+c^2)=-1$$。这不是巧合——把它写成一般的代数式，就是下面的定理。

**定理 3.1**（第04章定理 3.1 的重复推导，记号与之完全一致）。设 $$R=\begin{bmatrix}a&b\\ c&d\end{bmatrix}$$ 是实矩阵。则 $$R\in SO(2)$$ 当且仅当存在 $$\theta\in\mathbb R$$ 使 $$R=R_\theta:=\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}$$。

*证明*：记 $$u=(a,c)$$，$$v=(b,d)$$。由前面的回忆，$$R\in O(2)$$（即 $$R^{\mathsf T}R=I$$）当且仅当 $$u,v$$ 是标准正交基，即 $$a^2+c^2=1$$，$$b^2+d^2=1$$，$$ab+cd=0$$。像三个例子里那样，给定单位向量 $$u=(a,c)$$，与它垂直的单位向量只有 $$(-c,a)$$ 与 $$(c,-a)$$——这是因为 $$\mathbb R^2$$ 中垂直于一条直线的方向只有一条，而长度为 $$1$$ 的点在这条直线上只有两个（互为相反数）。逐一代入算行列式：$$v=(-c,a)$$ 给出 $$\det R=a\cdot a-b\cdot c=a^2+c^2=1$$；$$v=(c,-a)$$ 给出 $$\det R=a\cdot(-a)-c\cdot c=-(a^2+c^2)=-1$$。条件 $$\det R=1$$ 唯一地选出 $$v=(-c,a)$$，即 $$b=-c,d=a$$，于是
$$R=\begin{bmatrix}a&-c\\ c&a\end{bmatrix},\qquad a^2+c^2=1.$$
最后，单位圆上的点 $$(a,c)$$ 总可以写成 $$(\cos\theta,\sin\theta)$$（这正是"角度"这个记号最初的定义：$$\theta$$ 就是从 $$(1,0)$$ 逆时针转到 $$(a,c)$$ 转过的角），代回即得 $$R=R_\theta$$。反向验证：把 $$R_\theta$$ 代回 $$R^{\mathsf T}R$$，用 $$\cos^2\theta+\sin^2\theta=1$$ 直接算出等于 $$I$$，行列式同样等于 $$\cos^2\theta+\sin^2\theta=1$$。$$\blacksquare$$

**为什么要引入 $$\theta$$ 这个记号**：例 1–3 里我们始终在处理"一对满足 $$a^2+c^2=1$$ 的数 $$(a,c)$$"，但这样写不出群的乘法结构（两个矩阵相乘时 $$(a,c)$$ 怎么变，并不直观）。把 $$(a,c)$$ 换成 $$(\cos\theta,\sin\theta)$$ 之后，"矩阵相乘"会翻译成"角度相加"（这是第04章定理 3.2 的内容，本章暂不展开），这才是引入 $$\theta$$ 的真正理由：它不是为了好看，而是为了让群结构显形。

### 3.2 $$J$$ 的幂与旋转：具体角度处的验证

**从入口题 (b) 开始算。** 直接用矩阵乘法：
$$J^2=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}.$$
逐项算：第一行第一列是 $$0\cdot0+(-1)\cdot1=-1$$；第一行第二列是 $$0\cdot(-1)+(-1)\cdot0=0$$；第二行第一列是 $$1\cdot0+0\cdot1=0$$；第二行第二列是 $$1\cdot(-1)+0\cdot0=-1$$。所以
$$J^2=\begin{bmatrix}-1&0\\ 0&-1\end{bmatrix}=-I.$$
接着 $$J^3=J^2\cdot J=(-I)J=-J=\begin{bmatrix}0&1\\ -1&0\end{bmatrix}$$，$$J^4=J^3\cdot J=(-J)J=-J^2=I$$。于是 $$J$$ 的幂以 $$4$$ 为周期循环：$$I,J,-I,-J,I,\dots$$

**再算四个具体的旋转矩阵**：
$$R_{\pi/2}=\begin{bmatrix}\cos90^\circ&-\sin90^\circ\\ \sin90^\circ&\cos90^\circ\end{bmatrix}=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}=J,$$
$$R_\pi=\begin{bmatrix}-1&0\\ 0&-1\end{bmatrix}=-I=J^2,\qquad R_{3\pi/2}=\begin{bmatrix}0&1\\ -1&0\end{bmatrix}=-J=J^3,\qquad R_{2\pi}=\begin{bmatrix}1&0\\ 0&1\end{bmatrix}=I=J^4.$$
四个都对上了：$$R_{n\pi/2}=J^n$$（$$n=0,1,2,3$$，此后按 $$4$$ 循环）。

**命题 3.2**（$$J$$ 的基本代数性质）。$$J^2=-I$$，$$J^3=-J$$，$$J^4=I$$，且对一切整数 $$n$$，$$R_{n\pi/2}=J^n$$。

*证明*：$$J^2=-I$$ 是上面的直接计算；$$J^3=J^2J=-J$$、$$J^4=J^3J=-J\cdot J=-J^2=I$$ 由此递推得出。$$R_{n\pi/2}=J^n$$ 对 $$n=0,1,2,3$$ 是上面四个矩阵的直接比对，而 $$R_\theta$$ 以 $$2\pi$$（即 $$n$$ 以 $$4$$）为周期、$$J^n$$ 也以 $$4$$ 为周期（由 $$J^4=I$$），两条周期为 $$4$$ 的数列在一个周期内四点都相等，故对一切整数 $$n$$ 相等。$$\blacksquare$$

**这条命题在预告什么**：我们只对"$$90^\circ$$ 的整数倍"验证了"旋转 $$=J$$ 的幂"，但一般的 $$\theta$$（比如 $$\theta=1$$ 弧度）显然不是 $$\pi/2$$ 的整数倍，$$J^\theta$$ 这种写法本身还没有意义。第04章的定理 3.6（指数映射）要做的事，正是把"$$J$$ 的整数次幂"这个只对特殊角度有意义的操作，扩展成对**一切**实数 $$\theta$$ 都有意义的 $$\exp(\theta J)$$——用的正是我们在命题 3.2 里已经用过的那个事实：$$J^2=-I$$。命题 3.2 是那条一般定理在四个点上的"抽查"。

### 3.3 求导算子在具体频率上的特征值：从手算到"为什么必须是整数"

**先复习特征值的定义**：设 $$T$$ 是函数空间上的线性算子。若存在非零函数 $$f$$ 与数 $$\lambda$$ 使 $$Tf=\lambda f$$，称 $$\lambda$$ 为 $$T$$ 的**特征值 (eigenvalue)**，$$f$$ 为对应的**特征函数 (eigenfunction)**。这不是一个凭空的定义：如果 $$T=D=\dfrac{d}{d\theta}$$，那么 $$Df=\lambda f$$ 就是最常见的一阶微分方程 $$f'=\lambda f$$，"求特征值"和"解这个方程、看它有哪些周期解"是同一件事。

**先算几个具体的 $$k$$。** 直接求导：
$$D(e^{i\theta})=ie^{i\theta},\qquad D(e^{i2\theta})=2ie^{i2\theta},\qquad D(e^{-i\theta})=-ie^{-i\theta}.$$
读出来：$$\lambda_1=i,\ \lambda_2=2i,\ \lambda_{-1}=-i$$。规律很明显：$$\lambda_k=ik$$。

**这个规律对所有实数 $$k$$ 都成立吗？** 检验一个非整数的例子，$$k=\dfrac12$$，即 $$f(\theta)=e^{i\theta/2}$$。先确认它满足方程 $$f'=\dfrac i2f$$（直接求导即可看出），问题是它是不是 $$C^\infty_{2\pi}$$（$$2\pi$$ 周期光滑函数）里的元素：
$$f(\theta+2\pi)=e^{i(\theta+2\pi)/2}=e^{i\theta/2}\cdot e^{i\pi}=e^{i\theta/2}\cdot(-1)=-f(\theta).$$
这**不等于** $$f(\theta)$$（除非 $$f\equiv0$$）。所以 $$e^{i\theta/2}$$ 根本不是周期函数，$$\lambda=\dfrac i2$$ 不是 $$D$$（作用在 $$C^\infty_{2\pi}$$ 上）的特征值。再检验一个实数的例子，$$\lambda=1$$，即 $$f(\theta)=e^\theta$$：
$$f(\theta+2\pi)=e^{\theta+2\pi}=e^{2\pi}e^\theta=e^{2\pi}f(\theta),$$
而 $$e^{2\pi}\approx535.5\ne1$$，所以 $$e^\theta$$ 也不是周期函数，$$\lambda=1$$ 同样不是特征值。

**从这两个"反例"里能读出什么？** 两次失败的原因不一样：$$\lambda=i/2$$ 失败在"相位差了一个 $$-1$$ 因子"（模长对，辐角不对）；$$\lambda=1$$ 失败在"模长就不是 $$1$$"（根本不是纯虚数）。这提示我们：要让 $$e^{\lambda\theta}$$ 是 $$2\pi$$ 周期函数，需要 $$e^{2\pi\lambda}=1$$ 这一个条件同时满足"模长为 $$1$$"和"辐角是 $$2\pi$$ 的整数倍"两件事。把这条思路写成一般证明，就是下面的定理。

**定理 3.3**（$$D$$ 在 $$C^\infty_{2\pi}$$ 上的特征值恰是纯虚整数）。$$\sigma_p(D)=\{ik:k\in\mathbb Z\}$$，特征函数为 $$f_k(\theta)=e^{ik\theta}$$。

*证明*：设 $$f\in C^\infty_{2\pi}$$ 非零，$$f'=\lambda f$$，$$\lambda\in\mathbb C$$。令 $$g(\theta)=f(\theta)e^{-\lambda\theta}$$，求导：
$$g'(\theta)=f'(\theta)e^{-\lambda\theta}+f(\theta)\cdot(-\lambda)e^{-\lambda\theta}=\bigl(f'(\theta)-\lambda f(\theta)\bigr)e^{-\lambda\theta}=0$$
（这一步用了 $$f'=\lambda f$$ 与指数函数的求导公式 $$(e^{-\lambda\theta})'=-\lambda e^{-\lambda\theta}$$）。所以 $$g$$ 是常数，记 $$g\equiv c$$（$$c\ne0$$，因为 $$f\not\equiv0$$），即 $$f(\theta)=ce^{\lambda\theta}$$——这正是我们在"反例"里用过的那个形式。施加 $$2\pi$$ 周期性：
$$ce^{\lambda(\theta+2\pi)}=f(\theta+2\pi)=f(\theta)=ce^{\lambda\theta}\quad\Longrightarrow\quad e^{2\pi\lambda}=1$$
（两边约去非零的 $$ce^{\lambda\theta}$$）。写 $$\lambda=\alpha+i\beta$$（$$\alpha,\beta\in\mathbb R$$），则 $$e^{2\pi\lambda}=e^{2\pi\alpha}e^{2\pi i\beta}$$，其模长是 $$e^{2\pi\alpha}$$、辐角是 $$2\pi\beta$$。等于 $$1$$ 当且仅当模长为 $$1$$ 且辐角是 $$2\pi$$ 的整数倍：
$$e^{2\pi\alpha}=1\ \Longleftrightarrow\ \alpha=0,\qquad 2\pi\beta\in2\pi\mathbb Z\ \Longleftrightarrow\ \beta\in\mathbb Z.$$
（这正是上面两个反例分别违反的那一半条件：$$\lambda=1$$ 违反了 $$\alpha=0$$；$$\lambda=i/2$$ 违反了 $$\beta\in\mathbb Z$$。）于是 $$\lambda=i\beta=ik$$（$$k\in\mathbb Z$$）。反过来，$$f_k(\theta)=e^{ik\theta}$$ 确实以 $$2\pi$$ 为周期（因为 $$k$$ 是整数，$$e^{ik\cdot2\pi}=1$$），且 $$Df_k=ikf_k$$，验证了它确是特征函数。$$\blacksquare$$

### 3.4 $$D$$ 是反自伴的：先验证一个具体恒等式

**为什么要问这个问题**：定理 3.3 告诉我们 $$D$$ 的特征值都是纯虚数 $$ik$$，没有一个是普通的实数或者带正实部/负实部的复数。这不是巧合——它来自 $$D$$ 在下面这个内积意义下的一种对称性。我们先在具体的 $$f,g$$ 上验证这个对称性，再给出一般定义与证明。

回忆内积 $$\langle f,g\rangle=\dfrac1{2\pi}\displaystyle\int_0^{2\pi}f(\theta)\overline{g(\theta)}\,d\theta$$（本章只用到 $$f,g$$ 为实函数的情形，此时 $$\overline{g}=g$$）。

**入口题 (d) 的计算**：取 $$f=\cos\theta$$，$$g=\sin\theta$$，$$Df=-\sin\theta$$。
$$\langle Df,g\rangle=\frac1{2\pi}\int_0^{2\pi}(-\sin\theta)(\sin\theta)\,d\theta=-\frac1{2\pi}\int_0^{2\pi}\sin^2\theta\,d\theta=-\frac1{2\pi}\cdot\pi=-\frac12$$
（用了 $$\int_0^{2\pi}\sin^2\theta\,d\theta=\pi$$，这是把 $$\sin^2\theta=\frac{1-\cos2\theta}2$$ 在一个整周期上积分、余弦项积分为零得到的标准结果）。另一边，$$Dg=\cos\theta$$：
$$-\langle f,Dg\rangle=-\frac1{2\pi}\int_0^{2\pi}\cos\theta\cdot\cos\theta\,d\theta=-\frac1{2\pi}\int_0^{2\pi}\cos^2\theta\,d\theta=-\frac1{2\pi}\cdot\pi=-\frac12.$$
两边都等于 $$-\dfrac12$$，相等！再换一组角色验证：取 $$f=\sin\theta,g=\cos\theta$$，$$Df=\cos\theta$$：
$$\langle Df,g\rangle=\frac1{2\pi}\int_0^{2\pi}\cos^2\theta\,d\theta=\frac12,\qquad -\langle f,Dg\rangle=-\frac1{2\pi}\int_0^{2\pi}\sin\theta\cdot(-\sin\theta)\,d\theta=\frac1{2\pi}\int_0^{2\pi}\sin^2\theta\,d\theta=\frac12.$$
又相等。两次验证提示：$$\langle Df,g\rangle=-\langle f,Dg\rangle$$ 对这两对函数都成立，而且证明的关键步骤都是"用一个积分恒等式把 $$\sin^2$$ 或 $$\cos^2$$ 的积分求出来"——这一步在一般证明里会被"分部积分 + 周期性消去边界项"取代。

**定理 3.4**（$$D$$ 是反自伴的）。对一切 $$f,g\in C^\infty_{2\pi}$$，$$\langle Df,g\rangle=-\langle f,Dg\rangle$$。

*证明*：分部积分：
$$\langle Df,g\rangle=\frac1{2\pi}\int_0^{2\pi}f'(\theta)\overline{g(\theta)}\,d\theta=\frac1{2\pi}\Bigl[f(\theta)\overline{g(\theta)}\Bigr]_0^{2\pi}-\frac1{2\pi}\int_0^{2\pi}f(\theta)\overline{g'(\theta)}\,d\theta.$$
边界项 $$\Bigl[f\overline g\Bigr]_0^{2\pi}=f(2\pi)\overline{g(2\pi)}-f(0)\overline{g(0)}$$。因为 $$f,g$$ 都以 $$2\pi$$ 为周期，$$f(2\pi)=f(0)$$、$$g(2\pi)=g(0)$$，两项相同，边界项恰好为零——这正是我们在具体例子里"没有算边界项"的原因：$$\cos\theta,\sin\theta$$ 在 $$0$$ 与 $$2\pi$$ 处取值相同，边界项自动抵消。剩下的积分就是 $$-\langle f,Dg\rangle$$（因为 $$\overline{g'}=\overline{Dg}$$）。$$\blacksquare$$

满足 $$T^*=-T$$（即 $$\langle Tf,g\rangle=-\langle f,Tg\rangle$$）的算子称为**反自伴算子 (skew-adjoint operator)**。这条性质立刻能解释定理 3.3 里"为什么偏偏是纯虚数"：若 $$Df=\lambda f$$ 且 $$\lVert f\rVert=1$$，则
$$\lambda=\langle Df,f\rangle=-\langle f,Df\rangle=-\overline{\langle Df,f\rangle}=-\overline\lambda,$$
而 $$\lambda=-\overline\lambda$$ 恰好是"$$\lambda$$ 的实部为零"的代数表达。第04章会把这条论证再走一遍，并且指出它和定理 3.3 里"周期性论证"是从两个不同角度看到的同一件事。

### 3.5 小结：四步准备对应第04章的什么

到这里，本节的四段计算依次对应第04章的：定理 3.1（旋转矩阵的分类）、定理 3.3–3.6（求导得到 $$J$$、$$J^2=-I$$、指数映射）、定理 3.8（$$D$$ 的谱）、定理 3.10（$$D$$ 反自伴）。第04章会把"取 $$3$$ 个具体角度""算 $$4$$ 个具体幂""检验 $$2$$ 个具体 $$\lambda$$""验证 $$2$$ 组具体 $$(f,g)$$"这些手算，升级成对**一切**角度、**一切**整数、**一切**函数都成立的定理，并且补上我们在这里跳过的部分——比如"为什么单位圆上除了 $$(-c,a)$$ 和 $$(c,-a)$$ 真的没有第三个垂直单位向量"这种几何事实的严格代数证明，以及"谱"这个概念本身的严格定义（我们目前只谈到了"特征值"，"谱"是比它更大的一个集合，第04章会说明二者在 $$D$$ 这个例子里恰好相等）。

## 四、几何与物理直觉 (Intuition)

**类比一：钟表的分针。** 想象一个分针，从 $$12$$ 点位置出发，匀速转动。$$\theta$$ 就是分针转过的角度，$$R_\theta$$ 把"分针指向的方向"变成了矩阵。分针转一整圈（$$\theta$$ 增加 $$2\pi$$）之后回到原处——这正是命题 3.2 里 $$R_{2\pi}=I=J^4$$ 说的事：转够整数圈，矩阵变回单位矩阵。定理 3.3 里"$$\lambda$$ 必须是整数乘以 $$i$$"，说的是同一件事在另一种语言下的样子：一个以钟面为周期的"振动"，只能以整数个"转一圈"为一个周期振荡，不能转半圈就重新开始——半圈之后指针指向了完全相反的方向（这就是 $$e^{i\theta/2}$$ 在 $$\theta$$ 增加 $$2\pi$$ 后变号的几何画面）。

**类比二：缠绕在柱子上的绳子。** 把一根绳子的一端固定在柱子上的一点，绳子从这一点开始一圈一圈往上缠。绳子上"缠了几圈"是一个只能取整数值的量——你不能缠"半圈又回到起点"，因为半圈之后绳子的落点已经移到了柱子的另一侧。命题 3.2 里"$$J$$ 的幂以 $$4$$ 为周期"，正是"缠绕"在四个特殊角度（$$90^\circ$$ 的倍数）上的取样；第04章会把这幅"缠绕"图像用于一般的角度，说明"整数"这件事从根本上是几何的、拓扑的，不是代数凑出来的。

**类比三：一根弹簧的振动。** 一个挂在弹簧上的重物，位移 $$x(t)$$ 满足 $$\ddot x=-x$$（选取合适的单位）。这个方程的解 $$x=a\cos t+b\sin t$$ 是周期性的、来回振荡的，永远不会飞走也不会停下——这背后的代数原因，正是"$$-1$$"这个负号：它使得对应的特征值是纯虚数（$$D^2$$ 作用在 $$\cos t,\sin t$$ 上的特征值是 $$-1$$，对应 $$D$$ 本身的特征值是 $$\pm i$$），纯虚特征值对应的运动必然是有界的圆周运动，而不是指数增长或衰减。这条"负号 $$\leftrightarrow$$ 振荡"的对应，是第04章"物理直觉"一节要仔细展开的主线：三种符号（负、零、正）对应三种截然不同的运动方式。

## 五、经典问题精讲 (Classical Problems)

### 问题 1：满足 $$A^2=-I$$ 的 $$2\times2$$ 实矩阵，迹与行列式必须是多少？

**解**：先看两个具体例子。$$J=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}$$ 满足 $$J^2=-I$$（3.2 节已验证），$$\mathrm{tr}\,J=0+0=0$$，$$\det J=0\cdot0-(-1)\cdot1=1$$。

再看一个不那么"标准"的例子，$$A=\begin{bmatrix}1&-2\\ 1&-1\end{bmatrix}$$。先算 $$A^2$$：第一行第一列 $$=1\cdot1+(-2)\cdot1=1-2=-1$$；第一行第二列 $$=1\cdot(-2)+(-2)\cdot(-1)=-2+2=0$$；第二行第一列 $$=1\cdot1+(-1)\cdot1=1-1=0$$；第二行第二列 $$=1\cdot(-2)+(-1)\cdot(-1)=-2+1=-1$$。于是
$$A^2=\begin{bmatrix}-1&0\\ 0&-1\end{bmatrix}=-I.$$
$$\mathrm{tr}\,A=1+(-1)=0$$，$$\det A=1\cdot(-1)-(-2)\cdot1=-1+2=1$$。两个例子的迹都是 $$0$$、行列式都是 $$1$$——这提示一般结论也是如此。

**一般论证**：设 $$A^2=-I$$。若 $$A$$ 有实特征值 $$t$$、实特征向量 $$v\ne0$$，即 $$Av=tv$$，两边再作用一次 $$A$$：$$A^2v=t^2v$$，即 $$-v=t^2v$$，得 $$t^2=-1$$，这在实数范围内无解。所以 $$A$$**没有实特征值**，它的两个特征值 $$\lambda_1,\lambda_2$$（作为复数）必是一对共轭复数（因为 $$A$$ 是实矩阵，特征多项式是实系数的，非实根必成对共轭出现）。又 $$A^2=-I$$ 意味着每个特征值 $$\lambda$$ 满足 $$\lambda^2=-1$$，即 $$\lambda=\pm i$$；结合"必须共轭成对"，只能是 $$\lambda_1=i,\lambda_2=-i$$。于是
$$\mathrm{tr}\,A=\lambda_1+\lambda_2=i+(-i)=0,\qquad \det A=\lambda_1\lambda_2=i\cdot(-i)=1.$$
**结论**：满足 $$A^2=-I$$ 的 $$2\times2$$ 实矩阵，迹恒为 $$0$$、行列式恒为 $$1$$，与两个例子吻合。（第04章的问题 1 会把这个结论推广到一般的 $$n\times n$$ 情形，并且给出"所有这样的 $$A$$ 互相相似"这个更强的结论，用到的工具是极小多项式与有理标准形——比这里的特征值计数论证更系统。）

### 问题 2：$$SO(2)$$ 与 $$(\mathbb R,+)$$ 不是同构的——一个具体反例

**解**：映射 $$\rho:\theta\mapsto R_\theta$$ 把加法群 $$\mathbb R$$ 映到 $$SO(2)$$。若 $$\rho$$ 是群同构，它首先必须是单射（不同的 $$\theta$$ 给出不同的矩阵）。但具体验证：
$$\rho(0)=R_0=\begin{bmatrix}1&0\\ 0&1\end{bmatrix}=I,\qquad \rho(2\pi)=R_{2\pi}=\begin{bmatrix}\cos2\pi&-\sin2\pi\\ \sin2\pi&\cos2\pi\end{bmatrix}=\begin{bmatrix}1&0\\ 0&1\end{bmatrix}=I.$$
$$\rho(0)=\rho(2\pi)$$，但 $$0\ne2\pi$$，所以 $$\rho$$ 不是单射，因而不可能是群同构。**结论**：尽管 $$\mathbb R$$ 和 $$SO(2)$$ "看起来都是一维的、都能连续变化"，它们作为群并不同构——$$SO(2)$$ 比 $$\mathbb R$$ "多绕了一圈就回到原地"这件事，是它和 $$\mathbb R$$ 的根本区别。（第04章会证明这是唯一的区别：$$\rho$$ 在 $$0$$ 附近是局部同构，只是整体上"差一个整数倍 $$2\pi$$"。）

### 问题 3：$$D^2$$ 作用在一个含常数项的函数上，哪里"坏"了

**解**：取 $$f(\theta)=3\cos\theta-2\sin\theta+5$$。先求一阶导数：$$Df=-3\sin\theta-2\cos\theta$$（常数 $$5$$ 的导数是 $$0$$）。再求二阶导数：
$$D^2f=D(-3\sin\theta-2\cos\theta)=-3\cos\theta-2\cdot(-\sin\theta)=-3\cos\theta+2\sin\theta.$$
现在把 $$D^2f$$ 与 $$-f$$ 比较：
$$-f=-3\cos\theta+2\sin\theta-5.$$
两者相差：$$D^2f-(-f)=(-3\cos\theta+2\sin\theta)-(-3\cos\theta+2\sin\theta-5)=5.$$
也就是说 $$D^2f=-f+5\ne-f$$。**差出来的恰好是原来的常数项 $$5$$**——这不是巧合：$$D^2$$ 作用在常数上给出 $$0$$（常数的导数是 $$0$$），而 $$-1$$ 倍常数给出 $$-5$$，两者相差 $$5$$；$$D^2$$ 作用在 $$\cos\theta,\sin\theta$$ 这两部分上则确实等于 $$-1$$ 倍自身，不产生任何误差。**结论**：$$D^2=-I$$ 这条等式，只在"没有常数项"的函数上成立；一旦函数里混入常数项（对应"频率 $$k=0$$"），等式就会在常数那一部分上失效。这正是第04章入口题 (d) 要问的问题："在整个 $$C^\infty_{2\pi}$$ 上 $$D^2=-I$$ 成立吗？"——本例已经具体地看到答案是否定的，且"坏"在哪一条谱线上。

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 写出 $$R_{\pi/2}$$ 的矩阵，直接验证 $$R_{\pi/2}^{\mathsf T}R_{\pi/2}=I$$ 且 $$\det R_{\pi/2}=1$$。

**基2.** 求与 $$\left(\dfrac35,\dfrac45\right)$$ 正交的两个单位向量，分别与 $$\left(\dfrac35,\dfrac45\right)$$ 拼成 $$2\times2$$ 矩阵，计算两个矩阵各自的行列式，指出哪一个属于 $$SO(2)$$。

**基3.** 直接求导算出 $$D(e^{i3\theta})$$，并验证 $$e^{i3\theta}$$ 确以 $$2\pi$$ 为周期。

### 竞赛（本课目标难度）

**竞1.** 证明 $$\lambda=\dfrac i3$$ 不是 $$D$$（作用在 $$C^\infty_{2\pi}$$ 上）的特征值：即证明不存在非零的 $$2\pi$$ 周期光滑函数 $$f$$ 使 $$f'=\dfrac i3f$$。

**竞2.** 取 $$f=\sin\theta,g=\cos\theta$$（与正文 3.4 节的例子交换角色），直接验证 $$\langle Df,g\rangle=-\langle f,Dg\rangle$$，并说明一般恒等式对"所有 $$f,g$$"成立这件事，为什么已经自动保证了"交换 $$f,g$$ 之后"仍然成立。

**竞3.** 直接算出 $$R_0,R_{\pi/2},R_\pi,R_{3\pi/2}$$ 这四个矩阵，把它们分别与 $$J^0,J^1,J^2,J^3$$ 比较，写出你观察到的对应关系（不要求证明对一般 $$\theta$$ 成立，只需验证这四个点）。

### 研究（通向下一章）

**研1.** 分别计算 $$D^2$$ 作用在 $$\cos\theta$$、$$\sin\theta$$、常数函数 $$1$$、$$e^{i2\theta}$$ 上的结果，读出对应的特征值，猜一猜 $$D^2$$ 的全部特征值集合一般长什么样（不要求证明，只要求猜）。

**研2.** 取矩阵 $$A=\begin{bmatrix}0&1\\ -1&0\end{bmatrix}$$。验证 $$A^2=-I$$。$$A$$ 与 $$J$$ 相等吗？找出 $$A$$ 与 $$J$$ 之间的关系（提示：试着比较 $$A$$ 与 $$-J$$，以及 $$A$$ 与 $$J$$ 的转置）。

### 解答 (Solutions)

**解 基1.** $$R_{\pi/2}=\begin{bmatrix}\cos90^\circ&-\sin90^\circ\\ \sin90^\circ&\cos90^\circ\end{bmatrix}=\begin{bmatrix}0&-1\\ 1&0\end{bmatrix}$$。转置 $$R_{\pi/2}^{\mathsf T}=\begin{bmatrix}0&1\\ -1&0\end{bmatrix}$$。相乘：第一行第一列 $$=0\cdot0+1\cdot1=1$$；第一行第二列 $$=0\cdot(-1)+1\cdot0=0$$；第二行第一列 $$=-1\cdot0+0\cdot1=0$$；第二行第二列 $$=-1\cdot(-1)+0\cdot0=1$$。所以 $$R_{\pi/2}^{\mathsf T}R_{\pi/2}=\begin{bmatrix}1&0\\ 0&1\end{bmatrix}=I$$。行列式 $$\det R_{\pi/2}=0\cdot0-(-1)\cdot1=1$$。两条都验证成立。$$\blacksquare$$

**解 基2.** 与 $$\left(\dfrac35,\dfrac45\right)$$ 正交的单位向量是 $$\left(-\dfrac45,\dfrac35\right)$$ 与 $$\left(\dfrac45,-\dfrac35\right)$$（互为相反数，都与原向量点积为零、长度为 $$1$$，验证见正文 3.1 节例 3）。
- 取第二列为 $$\left(-\dfrac45,\dfrac35\right)$$：矩阵 $$\begin{bmatrix}3/5&-4/5\\ 4/5&3/5\end{bmatrix}$$，行列式 $$=\dfrac35\cdot\dfrac35-\left(-\dfrac45\right)\cdot\dfrac45=\dfrac9{25}+\dfrac{16}{25}=1$$，属于 $$SO(2)$$。
- 取第二列为 $$\left(\dfrac45,-\dfrac35\right)$$：矩阵 $$\begin{bmatrix}3/5&4/5\\ 4/5&-3/5\end{bmatrix}$$，行列式 $$=\dfrac35\cdot\left(-\dfrac35\right)-\dfrac45\cdot\dfrac45=-\dfrac9{25}-\dfrac{16}{25}=-1$$，不属于 $$SO(2)$$。$$\blacksquare$$

**解 基3.** $$D(e^{i3\theta})=3ie^{i3\theta}$$（直接求导，指数函数求导法则）。周期性：$$e^{i3(\theta+2\pi)}=e^{i3\theta}\cdot e^{i6\pi}$$。因为 $$6\pi$$ 是 $$2\pi$$ 的整数倍（$$6\pi=3\cdot2\pi$$），$$e^{i6\pi}=\cos6\pi+i\sin6\pi=1+0i=1$$，所以 $$e^{i3(\theta+2\pi)}=e^{i3\theta}$$，确以 $$2\pi$$ 为周期。$$\blacksquare$$

**解 竞1.** 设 $$f\in C^\infty_{2\pi}$$ 非零且 $$f'=\dfrac i3f$$。与定理 3.3 证明同样的做法：令 $$g(\theta)=f(\theta)e^{-i\theta/3}$$，求导得 $$g'=(f'-\tfrac i3f)e^{-i\theta/3}=0$$，故 $$f(\theta)=ce^{i\theta/3}$$（$$c\ne0$$）。检验周期性：
$$f(\theta+2\pi)=ce^{i(\theta+2\pi)/3}=ce^{i\theta/3}\cdot e^{i2\pi/3}.$$
而 $$e^{i2\pi/3}=\cos120^\circ+i\sin120^\circ=-\dfrac12+i\dfrac{\sqrt3}2\ne1$$。所以 $$f(\theta+2\pi)=e^{i2\pi/3}f(\theta)\ne f(\theta)$$（因为 $$c\ne0$$），与 $$f$$ 周期矛盾。故不存在这样的非零 $$f$$，$$\lambda=i/3$$ 不是特征值。$$\blacksquare$$

**解 竞2.** $$f=\sin\theta,g=\cos\theta$$，$$Df=\cos\theta$$：
$$\langle Df,g\rangle=\frac1{2\pi}\int_0^{2\pi}\cos\theta\cdot\cos\theta\,d\theta=\frac1{2\pi}\int_0^{2\pi}\cos^2\theta\,d\theta=\frac1{2\pi}\cdot\pi=\frac12.$$
$$Dg=-\sin\theta$$：
$$-\langle f,Dg\rangle=-\frac1{2\pi}\int_0^{2\pi}\sin\theta\cdot(-\sin\theta)\,d\theta=\frac1{2\pi}\int_0^{2\pi}\sin^2\theta\,d\theta=\frac1{2\pi}\cdot\pi=\frac12.$$
两边都等于 $$\dfrac12$$，相等。一般说明：恒等式 $$\langle Df,g\rangle=-\langle f,Dg\rangle$$ 里的 $$f,g$$ 本来就是任意两个 $$C^\infty_{2\pi}$$ 中的函数——它不是针对某个特定的 $$(f,g)$$ 对写出来的，而是对**每一对** $$(f,g)$$ 都成立的恒等式。因此把 $$f,g$$ 互换角色，只是把恒等式里的记号重新代入了一遍（相当于把 $$(f,g)=(\sin\theta,\cos\theta)$$ 代进同一条对一切 $$(f,g)$$ 成立的式子），结论自动成立，不需要另外证明。$$\blacksquare$$

**解 竞3.** $$R_0=I$$，$$R_{\pi/2}=J$$，$$R_\pi=-I$$，$$R_{3\pi/2}=\begin{bmatrix}0&1\\ -1&0\end{bmatrix}$$（这些矩阵在正文 3.1、3.2 节已逐一算出）。而 $$J^0=I$$，$$J^1=J$$，$$J^2=-I$$，$$J^3=-J=\begin{bmatrix}0&1\\ -1&0\end{bmatrix}$$（3.2 节算出）。逐一比较：$$R_0=J^0$$，$$R_{\pi/2}=J^1$$，$$R_\pi=J^2$$，$$R_{3\pi/2}=J^3$$——四点处 $$R_{n\pi/2}=J^n$$ 都成立，这正是命题 3.2 的内容。$$\blacksquare$$

**解 研1.** $$D^2\cos\theta=D(-\sin\theta)=-\cos\theta$$，特征值 $$-1$$。$$D^2\sin\theta=D(\cos\theta)=-\sin\theta$$，特征值 $$-1$$。$$D^2(1)=D(0)=0$$，特征值 $$0$$。$$D^2(e^{i2\theta})=D(2ie^{i2\theta})=(2i)^2e^{i2\theta}=-4e^{i2\theta}$$，特征值 $$-4$$。四个特征值是 $$\{0,-1,-1,-4\}$$，去重后是 $$\{0,-1,-4\}$$。这些数都形如 $$-k^2$$（$$k=0,1,2$$）。**猜测**：$$D^2$$ 的全部特征值集合是 $$\{-k^2:k\in\mathbb Z\}=\{0,-1,-4,-9,\dots\}$$——这与 3.3 节定理 3.3 里 $$D$$ 的特征值 $$ik$$ 平方后自然得到的集合一致。（第04章推论 3.9 会证明这就是全部答案，不多不少。）

**解 研2.** $$A^2=\begin{bmatrix}0&1\\ -1&0\end{bmatrix}\begin{bmatrix}0&1\\ -1&0\end{bmatrix}$$：第一行第一列 $$=0\cdot0+1\cdot(-1)=-1$$；第一行第二列 $$=0\cdot1+1\cdot0=0$$；第二行第一列 $$=-1\cdot0+0\cdot(-1)=0$$；第二行第二列 $$=-1\cdot1+0\cdot0=-1$$。所以 $$A^2=\begin{bmatrix}-1&0\\ 0&-1\end{bmatrix}=-I$$，验证成立。$$A\ne J$$（逐项比较：$$J$$ 的第一行是 $$(0,-1)$$，$$A$$ 的第一行是 $$(0,1)$$，符号相反）。但 $$A=-J$$（把 $$J$$ 的每一项都取相反数正好得到 $$A$$），同时 $$A$$ 也等于 $$J$$ 的转置 $$J^{\mathsf T}=\begin{bmatrix}0&1\\ -1&0\end{bmatrix}$$（因为 $$J$$ 是反对称矩阵，$$J^{\mathsf T}=-J$$，这两个说法是一回事）。所以 $$A$$ 和 $$J$$ 都满足同一个代数方程 $$X^2=-I$$，但代表相反方向的 $$90^\circ$$ 旋转——$$J$$ 是"逆时针转 $$90^\circ$$"，$$A=-J$$ 是"顺时针转 $$90^\circ$$"。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

1. **一个单位向量决定的旋转矩阵是唯一的（差一个方向选择）。** 给定单位向量 $$(a,c)$$，能配成行列式为 $$1$$ 的矩阵只有一种取法（$$v=(-c,a)$$）；这就是 $$SO(2)$$ 里每个元素都能写成 $$R_\theta$$ 的代数原因，本章例 1–3 已经在三个具体向量上验证过。

2. **$$J^2=-I$$ 是贯穿全章的代数心脏。** 它使得 $$J$$ 的幂以 $$4$$ 为周期循环，恰好对应旋转 $$90^\circ$$ 的整数倍；下一章会把这条代数事实升级成对**一切**角度都成立的指数映射公式。

3. **"整数"来自周期性，不是凭空规定的。** 定理 3.3 的证明里，"$$\lambda$$ 必须是纯虚整数"这件事，是"模长为 $$1$$"和"辐角是 $$2\pi$$ 的整数倍"这两个条件共同逼出来的——我们已经用两个反例（$$\lambda=1$$ 和 $$\lambda=i/2$$）亲眼看到这两个条件各自失效时会发生什么。

4. **反自伴性解释了"为什么偏偏是纯虚数"。** 3.4 节的两组具体验证与一般证明，说明 $$\langle Df,g\rangle=-\langle f,Dg\rangle$$ 不是巧合，而是分部积分加上周期性（边界项为零）的直接推论；下一章会用它重新推导"$$D$$ 的特征值必为纯虚数"这个结论，作为定理 3.3 之外的第二条独立证据。

5. **"$$D^2=-I$$"只在没有常数项的函数上成立。** 问题 3 已经具体算出，常数项恰好是打破这条等式的地方——这就是下一章要精确回答的"$$i$$ 从哪里来、又在哪里失效"这个问题的第一手证据。

**现在交棒。** 你已经能够：写出并验证一个具体的旋转矩阵、算出 $$J$$ 的幂并发现它的周期性、算出 $$D$$ 在若干具体频率上的特征值（并且验证了非整数频率为什么不行）、验证了一条具体的反自伴恒等式。下一章会把这四件"手算过的事"分别升级成定理 3.1（$$SO(2)$$ 的完整分类）、定理 3.3–3.6（求导产生 Lie 代数、指数映射）、定理 3.8（$$D$$ 的谱）、定理 3.10（$$D$$ 反自伴的一般证明），并且第一次回答"$$i$$ 到底是什么"这个问题——它不是一个被假设存在的数，而是一个具体的、可以用矩阵写出来的线性算子。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch02_复平面与_Euler_公式_下.md">← 第02章 复平面与 Euler 公式·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch04_平面旋转群_SO_2_与算子的谱_下.md">第04章 平面旋转群 SO(2) 与算子的谱·下 →</a></div>
</div>
