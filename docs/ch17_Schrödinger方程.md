---
layout: default
---

# 第17章: Schrödinger 方程 (The Schrödinger Equation)
> 对应原专栏: MP45–MP47
> 专家依据: `_experts/analysis/harmonic-fourier.md`（主）+ `_experts/analysis/spectral-theory.md`
> 知识库依据: `opc2/knowledge/physics/量子力学/landau-qm-modern/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

第 16 章把物理量翻译成Hilbert 空间上的自伴算子，把测量结果翻译成算子的谱。那一步给出了整套语言的骨架，却没有给出任何一个具体的数。本章给这副骨架上第一台能运转的发动机：**Schrödinger 方程**。

本章解决两个问题。第一，含时方程 $$i\hbar\partial_t\psi = H\psi$$ 怎么解。答案是**分离变量**：把波函数拆成"空间部分的本征方程"与"时间部分的一个相位因子"，再把本征函数线性叠加。这一步解释了一件贯穿全书的事：量子力学的计算为什么总是归结为求 $$H$$ 的本征值与本征函数。第二，找一个能干净算完的模型。**谐振子**就是这样一个模型——用一对算子 $$a$$、$$a^\dagger$$ 做**因式分解**，整条能谱 $$E_n = \hbar\omega(n+\tfrac12)$$ 与全部本征函数（Gauss 乘 Hermite 多项式）都可以不解二阶微分方程而得到。

与前后章的关系：第 16 章给了算子与谱，本章给方程与第一个可解模型，并把"用算子代数代替微分方程"这条技术线第一次走通。本章末尾会撞上一个技术裂缝：$$a$$、$$a^\dagger$$、$$X$$、$$P$$ 都不可能是有界算子，"谱"与"定义域"必须在更严格的意义下重新谈。那正是第 18 章的主题。

## 二、入口：一道具体的问题 (Entry Problem)

**入口题（自编，取材于 Landau–Lifshitz《量子力学》第 23 节与 Feynman《物理学讲义》第三卷）**

一维谐振子的经典 Hamilton 量是

$$H_{\mathrm{cl}} = \frac{p^2}{2m} + \frac{m\omega^2}{2}x^2,\qquad \omega = \sqrt{\frac{k}{m}} .$$

按第 16 章的规则量子化：位置 $$x\mapsto X$$（"乘 $$x$$"的算子），动量 $$p\mapsto P = -i\hbar\frac{d}{dx}$$，两者满足正则对易关系 $$[X,P] = i\hbar I$$。请只用手边这两条信息回答下列问题：

**(i)** 若把 $$m\omega X$$ 与 $$P$$ 当成一对可交换的"数"，会写出 $$2mH = (m\omega X - iP)(m\omega X + iP)$$。它们其实不交换。请算出这个等号两边差了多远。

**(ii)** 由上一步引出两个算子

$$a = \frac{1}{\sqrt{2m\hbar\omega}}\bigl(m\omega X + iP\bigr),\qquad a^\dagger = \frac{1}{\sqrt{2m\hbar\omega}}\bigl(m\omega X - iP\bigr),$$

把 $$H$$ 写成 $$\hbar\omega\bigl(N + \tfrac12 I\bigr)$$ 的形式，其中 $$N = a^\dagger a$$。

**(iii)** 若 $$\psi$$ 是 $$N$$ 的本征向量、本征值为实数 $$\lambda$$，求 $$a\psi$$ 与 $$a^\dagger\psi$$ 各自满足的本征方程（在它们非零的前提下）。

**(iv)** 由此论证：能级恰为 $$\hbar\omega\bigl(n+\tfrac12\bigr)$$，$$n = 0,1,2,\dots$$；并且"向上"可以永远进行，"向下"必须停在某处。

**(v)** 写出归一化的基态波函数，并说明基态能量为什么不能是零。

**(vi)** 追问一句：能级"等间距"这件事，本质上是哪一个代数事实的推论？

这道题的 (ii)–(v) 是本章第三节的核心技术；(vi) 的答案会在竞赛题 **竞5** 里被抽象成一条一般命题。请注意一个细节：从头到尾我们没有解任何一个二阶微分方程。这正是这套方法的全部价值所在——我们把一个分析问题换成了一个代数问题。

第 16 章结尾留下的悬念（可观测量、本征态、测量结果）在这里第一次被真正用来算出一个数。

## 三、结构：定义与完整推导 (Structure & Proof)

本节分三段。第一段（3.1–3.4）把含时方程拆成"求谱"加"乘相位"两件事，得出解的结构；第二段（3.5–3.6）把入口题 (i) 里那个不成立的因式分解算到底，得到一对升降算子；第三段（3.7–3.9）只用对易关系把整条能谱与全部本征函数推出来。**全程不解任何二阶微分方程**；最后我们会在 3.10 里回头说明，被绕过的那条路是什么样子。

### 3.1 Schrödinger 方程

**定义 3.1（Schrödinger 方程与时间演化算子, Schrödinger equation）**。设 $$\mathscr H = L^2(\Omega)$$ 是第 15 章构造的 Hilbert 空间，$$H$$ 是 $$\mathscr H$$ 上的自伴算子（第 16 章的可观测量）。**含时 Schrödinger 方程**是

$$i\hbar\,\partial_t\psi = H\psi,\qquad \psi(\cdot,t)\in\mathscr H,\ \ t\in\mathbb R .$$

使 $$H$$ 有定义的向量全体记作 $$\operatorname{Dom}H$$，称 $$H$$ 为该系统的 **Hamilton 算子 (Hamiltonian operator)**，$$i\hbar\partial_t - H$$ 为 **Schrödinger 算子 (Schrödinger operator)**——原文 MP45 把求解方程归纳为求它的核：$$\psi\in\operatorname{Ker}\bigl(i\hbar\partial_t - H\bigr)$$。若把 $$\psi(\cdot,t)$$ 看成一条在 $$\mathscr H$$ 里随 $$t$$ 走的曲线，等价的写法是

$$\partial_t\psi = -\frac{i}{\hbar}H\psi .$$

**定义 3.2（平稳态, stationary state）**。设 $$E\in\mathbb R$$，$$\Psi\in\operatorname{Dom}H$$ 非零，且

$$H\Psi = E\Psi .$$

则称 $$\Psi$$ 是 $$H$$ 的**本征函数 (eigenfunction)**、$$E$$ 是对应的**本征值 (eigenvalue)**，合称 $$H$$ 的**本征对**；称 $$\Psi$$ 为该系统的一个**平稳态**。$$H\Psi = E\Psi$$ 称为**定态 Schrödinger 方程 (time-independent Schrödinger equation)**。

**定理 3.3（解的结构）**。设 $$H$$ 不含时（$$H$$ 与 $$t$$ 无关），且 $$\psi(x,t)=\Psi(x)T(t)$$ 是方程的解，其中 $$\Psi\in\operatorname{Dom}H$$ 且 $$\Psi\neq 0$$。则存在实数 $$E$$ 使得

$$H\Psi = E\Psi,\qquad T(t) = c\,e^{-iEt/\hbar},\qquad c\in\mathbb C .$$

反之，对任一本征对 $$(E,\Psi)$$，$$\psi(x,t)=\Psi(x)e^{-iEt/\hbar}$$ 是含时方程的解。

*证明思路*：若能分离变量，则含时方程两边分别是"只含 $$t$$"与"只含 $$x$$"的量；两个一元的量相等意味着它们同等于一个常数。把这个常数认出来，两条常微分方程就各归各位。

*证明*：把 $$\psi=\Psi T$$ 代入 $$i\hbar\partial_t\psi=H\psi$$。左边对时间的偏导只打击 $$T$$，右边用 $$H$$ 只作用在 $$x$$ 上的事实得 $$H(\Psi T)=T\,H\Psi$$。于是

$$i\hbar\,\Psi\,\frac{dT}{dt} = T\,H\Psi .$$

在 $$\Psi\neq 0,\ T\neq 0$$ 的地方两边同除 $$\Psi T$$：

$$\frac{i\hbar}{T}\frac{dT}{dt} = \frac{H\Psi}{\Psi}.$$

左端只含 $$t$$、右端只含 $$x$$；等式对一切 $$(x,t)$$ 成立，故两边都等于同一个常数，记作 $$\lambda$$。由右端得

$$H\Psi = \lambda\Psi .$$

因为 $$H$$ 自伴，把上式与 $$\Psi$$ 作内积：$$\lambda\langle\Psi\vert \Psi\rangle = \langle\Psi\vert H\Psi\rangle = \overline{\langle H\Psi\vert \Psi\rangle} = \bar\lambda\langle\Psi\vert \Psi\rangle$$，故 $$\bar\lambda = \lambda$$，即 $$\lambda$$ 是实的。写 $$E=\lambda$$，得到 $$H\Psi=E\Psi$$。再由左端得 $$\dfrac{dT}{dt} = -\dfrac{iE}{\hbar}T$$，其通解是 $$T(t)=c\,e^{-iEt/\hbar}$$。逆命题直接代入验证：$$i\hbar\partial_t\bigl(\Psi e^{-iEt/\hbar}\bigr) = i\hbar\bigl(-\tfrac{iE}{\hbar}\bigr)\Psi e^{-iEt/\hbar} = E\Psi e^{-iEt/\hbar} = H\bigl(\Psi e^{-iEt/\hbar}\bigr)$$。$$\blacksquare$$

**定理 3.3 的物理读法**：平稳态的时间演化只是一个**相位因子** $$e^{-iEt/\hbar}$$。相位不进模长，所以概率密度 $$\lvert\psi(x,t)\rvert^2 = \lvert\Psi(x)\rvert^2$$ 完全不随时间变化——这正是"平稳"二字的意思。能量越高相位转得越快，转动的频率恰是 $$\lvert E\rvert/2\pi\hbar$$。

**定理 3.4（叠加与初值问题）**。设 $$\{(\lambda_k,\psi_k)\}_{k\ge1}$$ 是 $$H$$ 的一列本征对，$$\psi_0=\sum_kc_k\psi_k\in\operatorname{Dom}H$$ 是任给的初值。则初值问题的解是

$$\psi(x,t) = \sum_k c_k\,\psi_k(x)\,e^{-i\lambda_k t/\hbar},$$

且系数由初值唯一确定：若诸 $$\psi_k$$ 两两正交并已归一，则 $$c_k=\langle\psi_k\vert \psi_0\rangle$$。

*证明*：先说明可以逐项处理。设 $$P_N=\sum_{k=1}^N c_k\psi_k e^{-i\lambda_kt/\hbar}$$。则

$$\bigl(i\hbar\partial_t - H\bigr)P_N = \sum_{k=1}^N c_k\psi_k e^{-i\lambda_kt/\hbar}\bigl(i\hbar\cdot\tfrac{-i\lambda_k}{\hbar} - \lambda_k\bigr) = 0,$$

即每个有限部分和都是解；无穷和取极限仍是解（这一步用到 $$\psi_0\in\operatorname{Dom}H$$ 与 $$H$$ 的闭性，详见第 21 章）。再对 $$t=0$$ 的条件

$$P_N(\cdot,0) = \sum_{k=1}^N c_k\psi_k \xrightarrow{N\to\infty} \psi_0$$

两边逐个与 $$\psi_j$$ 作内积，由正交归一性只剩 $$k=j$$ 一项，得 $$c_j = \langle\psi_j\vert \psi_0\rangle$$。$$\blacksquare$$

**定理 3.4 说**：Schrödinger 方程的求解被归结为两件互不牵涉的事——**(甲) 求 $$H$$ 的本征值与本征函数；(乙) 把初值在这个本征函数系上展开**。这就是第 16 章那句"量子力学的计算总是求算子的谱"的严格出处。

**解说 3.1（谱连续时怎么办）**。定理 3.4 假定了本征值可排成一列。若 $$H$$ 的谱里出现连续段（如自由粒子的 $$H=-\frac{\hbar^2}{2m}\partial_x^2$$），求和要换成对谱测度的积分，$$\lvert c_k\rvert^2$$ 相应地换成"谱密度"。这一步的准确陈述需要投影算子值测度，见第 19 章；本章只处理谱离散的谐振子，其中级数型的定理 3.4 完全够用。

### 3.2 谐振子：Hamilton 量与正则对易关系

**定义 3.5（一维谐振子, harmonic oscillator）**。设 $$m>0,\ \omega>0$$。在 $$\mathscr H=L^2(\mathbb R)$$ 上取两个算子

$$(X\psi)(x) = x\psi(x),\qquad (P\psi)(x) = -i\hbar\psi'(x),$$

分别称为**位置算子**与**动量算子**（定义 3.5 与定义 3.6，第 16 章），它们满足**正则对易关系 (canonical commutation relation)**

$$[X,P] = XP-PX = i\hbar I .$$

定义**谐振子 Hamilton 量**为

$$H = \frac{P^2}{2m} + \frac{m\omega^2}{2}X^2 .$$

（$$H$$ 就是经典 Hamilton 量 $$H_{\mathrm{cl}}=\frac{p^2}{2m}+\frac{m\omega^2}{2}x^2$$ 把 $$x,p$$ 换成算子的结果；第 16 章的对应规则 $$F\mapsto F(X,P)$$ 在此第一次被用于构造具体模型。）

### 3.3 因式分解：入口题 (i) 的答案

先把入口题 (i) 算完。若 $$m\omega X$$ 与 $$P$$ 交换，就有恒等式

$$(m\omega X - iP)(m\omega X + iP) = m^2\omega^2X^2 + P^2 .$$

它们不交换。按 Leipniz 律（定理 3.8，第 16 章）展开左端，只用 $$[X,P]=i\hbar I$$：

$$
(m\omega X - iP)(m\omega X + iP)
= (m\omega X)^2 + P^2 + i m\omega\,(XP-PX)
= m^2\omega^2X^2 + P^2 + im\omega\,[X,P] .
$$

最后一式中 $$[X,P]=i\hbar I$$，于是 $$i m\omega\cdot i\hbar I = -m\omega\hbar I$$。把它移到等号另一边：

**定理 3.6（不交换留下的修正项）**。成立

$$(m\omega X - iP)(m\omega X + iP) = m^2\omega^2X^2 + P^2 - m\omega\hbar I .$$

也就是说，入口题 (i) 里那个等号**差了整整一项 $$-m\omega\hbar I$$**：不是"差不多"，而是一个与 $$\hbar$$ 同阶的、作用于整个空间的修正。$$\blacksquare$$

$$-m\omega\hbar I$$ 不是误差，是被丢掉的那部分。它与两段交叉项 $$\bigl(m\omega X)(\mp iP\bigr)+\bigl(\mp iP\bigr)(m\omega X)$$ 里"次序颠倒"的贡献恰好相消，剩下的就是这个纯量项。它归根结底来自 $$[X,P]\neq 0$$，即经典的 Poisson 括号 $$\{\,x,p\,\}=1$$ 在量子一侧的化身。

### 3.4 升降算子

把定理 3.6 的修正项除回去，就得到 $$H$$ 的因式分解。

**定义 3.7（下降算子与提升算子, lowering / raising operator）**。在 $$\mathscr H$$ 上定义

$$a = \frac{1}{\sqrt{2m\hbar\omega}}\bigl(m\omega X + iP\bigr),\qquad
a^\dagger = \frac{1}{\sqrt{2m\hbar\omega}}\bigl(m\omega X - iP\bigr).$$

$$a$$ 称为**下降算子**，$$a^\dagger$$ 称为**提升算子**；两者互为形式伴随。再令

$$N = a^\dagger a,$$

称为**数算子 (number operator)**。

（$$a$$ 与 $$a^\dagger$$ 的"伴随"一词见定义 3.5，第 16 章；本节的 $$X,P$$ 都是自伴的，故把 $$P$$ 换成 $$-P$$ 即得伴随。）

**定理 3.8（$$H$$ 的因式分解）**。成立

$$H = \hbar\omega\Bigl(N + \tfrac12 I\Bigr) = \hbar\omega\Bigl(a^\dagger a + \tfrac12I\Bigr).$$

*证明*：把定理 3.6 的差式反过来用，先算

$$\bigl(m\omega X - iP\bigr)\bigl(m\omega X + iP\bigr)
= m^2\omega^2X^2 + P^2 - m\omega\hbar I
\ \Longrightarrow\
m^2\omega^2X^2 + P^2 = \bigl(m\omega X - iP\bigr)\bigl(m\omega X + iP\bigr) + m\omega\hbar I .$$

两边同除 $$2m\hbar\omega$$：左端正是 $$H/\hbar\omega$$（因为 $$2mH = P^2 + m^2\omega^2X^2$$）；右端第一项是 $$a^\dagger a = N$$，第二项是 $$\tfrac{m\omega\hbar}{2m\hbar\omega}I = \tfrac12I$$。故 $$H/\hbar\omega = N+\tfrac12I$$。$$\blacksquare$$

**定理 3.8 是入口题 (ii) 的答案。** 注意它的分量：一个含 $$X$$ 与 $$P$$ 的二次表达式，被换成了**一个算子的乘积**。这个替换之所以可能，恰恰因为那个"差项"是纯量；若 $$[X,P]$$ 不是纯量，$$H$$ 就不是任何 $$a^\dagger a$$ 的倍数（这一点在第 22 章会用表示的不可约性说得更准）。

### 3.5 对易代数

接下来只用手边的对易关系，不再碰任何导数。

**定理 3.9（$$a,a^\dagger,N$$ 的对易关系）**。成立

$$[a,a^\dagger] = I,\qquad [N,a] = -a,\qquad [N,a^\dagger] = a^\dagger .$$

*证明*：先算 $$[a,a^\dagger]$$。由定义 3.7 与 $$[X,P]=i\hbar I$$，以及 $$[X,X]=[P,P]=0$$，

$$
2m\hbar\omega\,[a,a^\dagger]
= \bigl[m\omega X + iP,\ m\omega X - iP\bigr]
= -im\omega[X,P] + im\omega[P,X]
= -im\omega(i\hbar I) + im\omega(-i\hbar I) = 2m\omega\hbar I ,
$$

两边同除 $$2m\hbar\omega$$ 得 $$[a,a^\dagger]=I$$。

再算另外两条。由定理 3.9 的第一式与 $$N=a^\dagger a$$：

$$[a,N] = [a,a^\dagger a] = [a,a^\dagger]a + a^\dagger[a,a] = I\cdot a + 0 = a .$$

同理 $$[a^\dagger,N] = [a^\dagger,a^\dagger a] = 0 + a^\dagger[a^\dagger,a] = -a^\dagger[a,a^\dagger] = -a^\dagger$$（第二个等号把 $$[a^\dagger,a]=-I$$ 代入）。最后把这两式写成 $$[N,a]=-[a,N]=-a$$、$$[N,a^\dagger]=-[a^\dagger,N]=a^\dagger$$。$$\blacksquare$$

### 3.6 谱的升降

**引理 3.10（升降算符改本征值）**。设 $$N\psi = \lambda\psi$$，$$\psi\neq 0$$。则

$$N(a\psi) = (\lambda-1)\,a\psi\qquad(\text{若 }a\psi\neq 0),$$

$$N(a^\dagger\psi) = (\lambda+1)\,a^\dagger\psi\qquad(\text{若 }a^\dagger\psi\neq 0).$$

*证明思路*：把 $$N a$$ 换成 $$\bigl(aN - a\bigr)$$，让 $$N$$ 去作用它认得的东西。

*证明*：由 $$[N,a]=Na-aN=-a$$ 得 $$Na = aN - a$$。于是

$$N(a\psi) = (Na)\psi = (aN-a)\psi = a(N\psi) - a\psi = a(\lambda\psi) - a\psi = (\lambda-1)\,a\psi .$$

第二条同理：$$[N,a^\dagger]=a^\dagger$$ 给出 $$Na^\dagger = a^\dagger N + a^\dagger$$，故

$$N(a^\dagger\psi) = a^\dagger N\psi + a^\dagger\psi = (\lambda+1)\,a^\dagger\psi .$$

两条都必须附加"非零"的前提：$$a\psi$$ 完全可能是零向量，而零向量不是本征向量（定义 3.2 要求非零）。**什么时候为零，正是下一节的全部内容**。$$\blacksquare$$

**定理 3.11（能谱）**。设 $$N\psi=\lambda\psi$$，$$\psi\neq0$$，其中 $$\lambda\in\mathbb R$$。则 $$\lambda\in\{0,1,2,\dots\}$$，并且恰有一个本征值 $$0$$，其本征向量 $$\psi_0$$ 满足 $$a\psi_0=0$$。

*证明思路*：三步。① $$N$$ 是正定的，故 $$\lambda\ge0$$。② 反复用下降算子，每一步把本征值减 1；本征值不能穿过 0，所以这个下降过程必然在某处停住。③ 停住那一点就是 $$\lambda=0$$，再把"差几步"数出来。

*证明*：

**① $$\lambda\ge0$$，且为实数。** 先用内积验证 $$N$$ 的对称性：$$\langle\psi\vert N\varphi\rangle=\langle\psi\vert a^\dagger a\varphi\rangle=\langle a\psi\vert a\varphi\rangle$$，交换 $$\psi,\varphi$$ 得 $$\langle N\psi\vert \varphi\rangle=\langle a\psi\vert a\varphi\rangle$$，两者相等，故 $$N\subset N^*$$。再取 $$\varphi=\psi$$：

$$\langle\psi\vert N\psi\rangle = \langle a\psi\vert a\psi\rangle = \lVert a\psi\rVert^2\ \ge 0 .$$

把 $$N\psi=\lambda\psi$$ 代入左端得 $$\lambda\lVert\psi\rVert^2\ge0$$，由 $$\lVert\psi\rVert\neq0$$ 得 $$\lambda\ge0$$；又 $$\langle\psi\vert N\psi\rangle$$ 是实数，故 $$\lambda = \langle\psi\vert N\psi\rangle/\lVert\psi\rVert^2$$ 是实的。

**② 下降链必须停。** 反设 $$\psi$$ 所在的本征值链能无限往下降：即对一切 $$n\ge0$$，$$a^n\psi\neq0$$。由引理 3.10 逐步作用得

$$N\bigl(a^n\psi\bigr) = (\lambda-n)\,a^n\psi,\qquad n=0,1,2,\dots$$

这些 $$a^n\psi$$ 都非零，故 $$\lambda-n$$ 全是 $$N$$ 的本征值。由 ① 它们都 $$\ge0$$。但 $$\lambda-n\to-\infty$$，取 $$n>\lambda$$ 即得 $$\lambda-n<0$$，与 ① 矛盾。所以存在最小的 $$n_0\ge0$$ 使 $$a^{n_0+1}\psi=0$$。

**③ 停住处本征值为 0。** 令 $$\phi=a^{n_0}\psi\neq0$$。由 ② 知 $$a\phi=0$$。于是

$$N\phi = a^\dagger(a\phi) = a^\dagger 0 = 0,$$

即 $$N\phi = 0\cdot\phi$$：$$\phi$$ 是 $$N$$ 的本征向量，本征值 $$0$$。再由引理 3.10 反推 $$0 = \lambda - n_0$$（因为 $$N\phi=(\lambda-n_0)\phi$$ 且 $$\phi\neq0$$），得

$$\lambda = n_0\in\{0,1,2,\dots\}.$$

最后，本征值 $$0$$ 的本征向量必满足 $$0=\langle\phi\vert N\phi\rangle=\lVert a\phi\rVert^2$$，故 $$a\phi=0$$；反之 $$a\phi=0$$ 时 $$N\phi=0$$。两者互相等价，$$0$$ 的本征空间被 $$a$$ 的核完全刻画。$$\blacksquare$$

**推论 3.12（全部能级）**。谐振子的 Hamilton 量 $$H=\hbar\omega(N+\tfrac12I)$$ 的能谱恰为

$$E_n = \hbar\omega\Bigl(n+\tfrac12\Bigr),\qquad n=0,1,2,\dots$$

*证明*：$$H$$ 与 $$N$$ 差一个纯量倍加恒等，故有同一组本征向量，本征值相差 $$\hbar\omega/2$$；由定理 3.11，$$N$$ 的本征值恰是全体非负整数。$$\blacksquare$$

**推论 3.13（每个能级都被占满）**。对每个 $$n\ge0$$，从基态出发作 $$n$$ 次提升所得的向量

$$\psi_n = \bigl(a^\dagger\bigr)^n\psi_0\neq0$$

满足 $$N\psi_n = n\psi_n$$。

*证明*：对 $$n$$ 归纳。$$n=0$$ 时 $$\psi_0$$ 是 $$0$$ 的本征向量。设 $$N\psi_n = n\psi_n$$，则 $$N\psi_{n+1} = N a^\dagger\psi_n = a^\dagger N\psi_n + [N,a^\dagger]\psi_n = a^\dagger(n\psi_n) + a^\dagger\psi_n = (n+1)\psi_{n+1}$$，用到 $$[N,a^\dagger]=a^\dagger$$（定理 3.9）。非零性：$$\lVert\psi_{n+1}\rVert^2 = \langle\psi_n\vert a a^\dagger\psi_n\rangle = \langle\psi_n\vert(N+I)\psi_n\rangle = (n+1)\lVert\psi_n\rVert^2$$（用了 $$[a,a^\dagger]=I$$），由归纳假设 $$\psi_n\neq0$$ 得 $$\psi_{n+1}\neq0$$。$$\blacksquare$$

**定理 3.11 说**："向上"可以永远进行——这正是入口题 (iv) 的后半句；"向下"必须停在某处，因为 $$N$$ 是正的。**能谱从哪里来**：不是从解方程来，是从"有一个算子把本征值往下推、而本征值又不能为负"这两条来。整条代数论证用到的全部输入是定理 3.9 的三条对易关系。

### 3.7 基态波函数与零点能

**定理 3.14（基态）**。在归一化坐标 $$x$$ 下（即取 $$m=\hbar=\omega=1$$，见 3.9 的尺度变换），基态方程 $$a\psi_0=0$$ 的解为

$$\psi_0(x) = c\,e^{-x^2/2},\qquad c\in\mathbb C .$$

归一化后

$$\psi_0(x) = \pi^{-1/4}\,e^{-x^2/2}.$$

*证明*：归一化下 $$a=\dfrac{1}{\sqrt2}(x+D)$$ 且 $$D=\dfrac{d}{dx}$$（来源见 3.9）。方程 $$\dfrac{1}{\sqrt2}\bigl(x+\tfrac{d}{dx}\bigr)\psi_0=0$$ 即一阶线性方程

$$\psi_0'(x) = -x\,\psi_0(x),\qquad \frac{\psi_0'}{\psi_0}=-x .$$

分离变量：$$\ln\lvert\psi_0\rvert = -\dfrac{x^2}{2}+\mathrm{const}$$，故 $$\psi_0(x)=ce^{-x^2/2}$$。

归一化：$$\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi$$（古典 Gauss 积分），故

$$\lVert\psi_0\rVert^2 = \lvert c\rvert^2\sqrt\pi = 1\ \Longrightarrow\ \lvert c\rvert = \pi^{-1/4}.$$

取 $$c=\pi^{-1/4}$$（正的实常数），得证。$$\blacksquare$$

**定理 3.15（零点能不为零）**。基态能量是

$$E_0 = \tfrac12\hbar\omega>0,$$

称**零点能 (zero-point energy)**。它不可能等于零。

*证明*：由推论 3.12，$$E_0=\hbar\omega(0+\tfrac12)=\tfrac12\hbar\omega$$。若 $$E_0=0$$，则 $$H\psi_0=0$$，两边与 $$\psi_0$$ 作内积得

$$0 = \langle\psi_0\vert H\psi_0\rangle = \frac{1}{2m}\langle\psi_0\vert P^2\psi_0\rangle + \frac{m\omega^2}{2}\langle\psi_0\vert X^2\psi_0\rangle = \frac{1}{2m}\lVert P\psi_0\rVert^2 + \frac{m\omega^2}{2}\lVert X\psi_0\rVert^2 .$$

两项都非负，和为 0 迫使每项为 0：$$P\psi_0=0$$ 且 $$X\psi_0=0$$。前者说 $$\psi_0$$ 是常数 $$-i\hbar\psi_0'=0$$，后者说 $$x\psi_0(x)\equiv0$$——两者不能同时成立（常函数不是零函数，却处处被 $$x$$ 乘成 0 只在零函数上发生，而零函数不归一）。故 $$E_0\neq0$$。$$\blacksquare$$

**一点评注**。定理 3.15 的证明实际用到的只是"位置与动量不能同时取 0"，而这正是正则对易关系 $$[X,P]=i\hbar I$$ 的直接后果（第 16 章的定理 3.7）：若 $$P\psi=X\psi=0$$，则由 $$[X,P]\psi = (XP-PX)\psi = 0$$ 得 $$i\hbar\psi=0$$，$$\psi=0$$。所以**零点能的存在性等价于正则对易关系的非平凡性**——这不是计算方法的问题，是代数结构的必然。物理上它就是 Heisenberg 不确定性原理在极低温下的残余。

### 3.8 激发态与 Hermite 多项式

**引理 3.16（升降算子的归一化作用）**。设 $$\psi_n$$ 是归一化的能级基，$$N\psi_n=n\psi_n$$。则

$$a\,\psi_n = \sqrt n\,\psi_{n-1}\quad(n\ge1),\qquad a^\dagger\psi_n = \sqrt{n+1}\,\psi_{n+1}.$$

*证明*：$$\lVert a\psi_n\rVert^2 = \langle\psi_n\vert a^\dagger a\psi_n\rangle = \langle\psi_n\vert N\psi_n\rangle = n$$，且 $$a\psi_n$$ 是本征值 $$n-1$$ 的本征向量（引理 3.10），故它必须是 $$\psi_{n-1}$$ 的倍数，模长已算出为 $$\sqrt n$$，即 $$a\psi_n=\sqrt n\,\psi_{n-1}$$（相因子吸收进 $$\psi_{n-1}$$ 的定义）。第二式同理：$$\lVert a^\dagger\psi_n\rVert^2=\langle\psi_n\vert (N+I)\psi_n\rangle=n+1$$。$$\blacksquare$$

**定理 3.17（激发态与 Hermite 多项式）**。记 $$\psi_n=(a^\dagger)^n\psi_0$$，$$c_n$$ 为使 $$c_n\psi_n$$ 归一化的正数。则

$$c_n\psi_n(x) = H_n(x)\,e^{-x^2/2},\qquad H_n(x) = \frac{1}{\sqrt{2^nn!\sqrt\pi}}\,h_n(x),$$

其中 $$h_n$$ 是 $$n$$ 次 **Hermite 多项式 (Hermite polynomial)**，由

$$h_0(x)\equiv1,\qquad h_1(x)=2x,\qquad h_{n+1}(x) = 2x\,h_n(x) - 2n\,h_{n-1}(x)\quad(n\ge1)$$

唯一确定（physicist 约定：首项系数 $$2^n$$，权函数 $$e^{-x^2}$$）；$$H_n$$ 是"归一化的 Hermite 多项式"。

*证明*：由推论 3.13 与定理 3.11，$$N\psi_n=n\psi_n$$，故 $$\psi_n$$ 是能级 $$n$$ 的本征函数；由推论 3.13 与定理 3.14，它可以写成"多项式乘 Gauss"的形式。用归纳法证明那个多项式满足上面的递推。设 $$\psi_n=c_nh_n(x)e^{-x^2/2}$$（$$n=0$$ 时取 $$h_0=1$$，就是定理 3.14 的基态）。在归一化坐标下 $$a^\dagger=\frac{1}{\sqrt2}(x-D)$$，$$D=\frac{d}{dx}$$，而

$$
D\bigl(h_ne^{-x^2/2}\bigr) = h_n'e^{-x^2/2} - x\,h_ne^{-x^2/2} = \bigl(h_n'-xh_n\bigr)e^{-x^2/2},
$$

故

$$
\psi_{n+1} = a^\dagger\psi_n = \frac{1}{\sqrt2}\bigl(x-D\bigr)\bigl(h_ne^{-x^2/2}\bigr)
= \frac{1}{\sqrt2}\Bigl(xh_n - h_n' + xh_n\Bigr)e^{-x^2/2}
= \frac{1}{\sqrt2}\bigl(2xh_n - h_n'\bigr)e^{-x^2/2}.
$$

由引理 3.16，$$\psi_{n+1}=a^\dagger\psi_n/\sqrt{n+1}$$，故上式左边实为 $$\sqrt{n+1}\,\psi_{n+1}=\sqrt{n+1}\,c_{n+1}h_{n+1}e^{-x^2/2}$$。两边约去 $$e^{-x^2/2}$$：

$$\sqrt{n+1}\,c_{n+1}\,h_{n+1} = \frac{c_n}{\sqrt2}\bigl(2xh_n-h_n'\bigr). \tag{3.17.1}$$

**第一步：定 $$c_n$$。** 由 $$\psi_n=c_nh_ne^{-x^2/2}$$ 与定理 3.18 的 $$\int h_n^2e^{-x^2}dx=2^nn!\sqrt\pi$$，

$$1 = \lVert c_n\psi_n\rVert^2 = c_n^2\cdot 2^nn!\sqrt\pi\ \Longrightarrow\ \frac{c_{n+1}}{c_n} = \frac{1}{\sqrt{2(n+1)}}. \tag{3.17.2}$$

**第二步：把括号化成 $$h_{n+1}$$。** 由生成函数 $$e^{2xt-t^2}=\sum_n\frac{h_n(x)}{n!}t^n$$ 立得两条标准递推（见 竞4）：

$$h_n' = 2n\,h_{n-1},\qquad h_{n+1} = 2x\,h_n - 2n\,h_{n-1}.$$

把第一式代入第二式消去 $$2nh_{n-1}$$：

$$h_{n+1} = 2x\,h_n - h_n',\qquad\text{即}\qquad 2x\,h_n - h_n' = h_{n+1}. \tag{3.17.3}$$

**第三步：验证。** 把 (3.17.3) 代回 (3.17.1)，两边约去 $$h_{n+1}$$ 后剩下的条件变成关于 $$c$$ 的一个**数值**等式：

$$\sqrt{n+1}\,c_{n+1} = \frac{c_n}{\sqrt2}
\iff \sqrt{n+1}\cdot\frac{c_{n+1}}{c_n} = \frac{1}{\sqrt2}
\iff \sqrt{n+1}\cdot\frac{1}{\sqrt{2(n+1)}} = \frac{1}{\sqrt2}.$$

末式显然成立。**三个根号恰好配平**：升降算子的 $$\sqrt{n+1}$$ 与归一化的 $$\sqrt{2(n+1)}$$ 之比是常数 $$1/\sqrt2$$，正好等于因式分解带来的系数。$$\blacksquare$$

**例 3.1**。前几个 $$h_n$$：

$$h_0=1,\qquad h_1=2x,\qquad h_2 = 2x(2x)-2=4x^2-2,\qquad h_3 = 2x(4x^2-2)-8x = 8x^3-12x .$$

对应的本征能量是 $$E_n=\hbar\omega(n+\tfrac12)$$。

**定理 3.18（Hermite 多项式的正交性）**。$$\{h_n\}$$ 满足

$$\int_{-\infty}^{\infty} h_m(x)h_n(x)\,e^{-x^2}dx = 2^nn!\sqrt\pi\;\delta_{mn}.$$

*证明思路*：由 $$\psi_n=H_ne^{-x^2/2}$$，$$\{\psi_n\}$$ 是自伴算子 $$N$$ 属于互异本征值的本征函数。互异本征值的本征函数正交（第 16 章定理 3.11），代进去即得。剩下的常数用 $$h_n$$ 的首项系数 $$2^n$$ 与 $$\int h_n^2e^{-x^2}$$ 的显式公式算出。

*证明*：设 $$m\neq n$$。由 $$N\psi_m=m\psi_m$$、$$N\psi_n=n\psi_n$$ 且 $$N$$ 对称， $$m\langle\psi_m\vert \psi_n\rangle = \langle N\psi_m\vert \psi_n\rangle = \langle\psi_m\vert N\psi_n\rangle = n\langle\psi_m\vert \psi_n\rangle$$，故 $$(m-n)\langle\psi_m\vert \psi_n\rangle=0$$，$$m\neq n$$ 迫使 $$\langle\psi_m\vert \psi_n\rangle=0$$，即 $$\int h_mh_ne^{-x^2}=0$$。$$m=n$$ 时的值：由递推可直接验证 $$\int_{-\infty}^\infty h_n^2e^{-x^2}dx = 2^nn!\sqrt\pi$$（对 $$n$$ 归纳，用分部积分与 $$h_{n+1}=2xh_n-2nh_{n-1}$$；这是标准练习，列入竞4）。$$\blacksquare$$

### 3.9 归一化坐标与还原

前面 3.7–3.8 的计算是在"$$m=\hbar=\omega=1$$"下做的。一般情形靠**尺度变换**回到原单位。

**定理 3.19（尺度变换）**。令 $$\ell=\sqrt{\hbar/(m\omega)}$$（长度尺度），$$\xi = x/\ell$$，并定义酉算子 $$(U\psi)(\xi) = \ell^{1/2}\psi(\ell\xi)$$。则 $$UHU^{-1} = \hbar\omega\bigl(-\tfrac12\partial_\xi^2 + \tfrac12\xi^2\bigr)$$。

*证明*：设 $$\phi(\xi) = (U\psi)(\xi) = \ell^{1/2}\psi(\ell\xi)$$，则 $$\psi(x)=\ell^{-1/2}\phi(x/\ell)$$。

**位置算子**：$$\bigl(UXU^{-1}\phi\bigr)(\xi) = \ell^{1/2}\cdot(\ell\xi)\cdot\psi(\ell\xi) = \ell\,\xi\,\ell^{1/2}\psi(\ell\xi) = \ell\,\xi\,\phi(\xi) = \ell\,\Xi\,\phi$$，其中 $$\Xi$$ 是乘 $$\xi$$ 的算子。

**动量算子**：先算 $$\psi'(x) = \ell^{-1/2}\phi'(x/\ell)\cdot\ell^{-1} = \ell^{-3/2}\phi'(\xi)$$。于是

$$\bigl(UPU^{-1}\phi\bigr)(\xi) = \ell^{1/2}\cdot\bigl(-i\hbar\bigr)\psi'(\ell\xi) = \ell^{1/2}\cdot(-i\hbar)\cdot\ell^{-3/2}\phi'(\xi) = \frac{\hbar}{\ell}\bigl(-i\phi'(\xi)\bigr) = \frac{\hbar}{\ell}\,\Pi\phi,$$

其中 $$\Pi=-i\partial_\xi$$ 是归一化动量。代入 $$H$$，并把算子展开成 $$\ell^2$$ 与 $$\ell^{-2}$$：

$$UHU^{-1} = \frac{1}{2m}\Bigl(\frac{\hbar}{\ell}\Bigr)^2\Pi^2 + \frac{m\omega^2}{2}\ell^2\Xi^2 .$$

取 $$\ell^2=\dfrac{\hbar}{m\omega}$$，则 $$\Bigl(\dfrac{\hbar}{\ell}\Bigr)^2 = \hbar m\omega$$ 且 $$\ell^2 m\omega^2 = \hbar\omega$$，于是

$$UHU^{-1} = \frac{\hbar m\omega}{2m}\Pi^2 + \frac{\hbar\omega}{2}\Xi^2 = \frac{\hbar\omega}{2}\bigl(\Pi^2+\Xi^2\bigr) = \hbar\omega\bigl(-\tfrac12\partial_\xi^2+\tfrac12\xi^2\bigr).$$

这就是"$$m=\hbar=\omega=1$$"的由来。$$\blacksquare$$

**推论 3.20（一般单位的基态）**。还原到原变量 $$x$$，基态波函数为

$$\psi_0(x) = \Bigl(\frac{m\omega}{\pi\hbar}\Bigr)^{1/4}\exp\Bigl(-\frac{m\omega}{2\hbar}x^2\Bigr),$$

长度为 $$\ell=\sqrt{\hbar/(m\omega)}$$ 的 Gauss 包；激发态是同一 Gauss 乘 Hermite 多项式。

*证明*：由定理 3.19，$$U\psi_0^{\text{nor}}= \psi_0^{\text{orig}}$$（$$\psi_0^{\text{nor}}$$ 指 3.7 的解）。归一化因子来自 $$U$$ 的酉性与 $$\lVert e^{-x^2/2}\rVert=\pi^{1/4}$$；把 $$\xi=x/\ell$$ 代入并改回 $$\lvert\psi\rvert^2$$ 的密度即得（常数项 $$\ell^{-1/2}\cdot\pi^{-1/4}=\bigl(\frac{m\omega}{\pi\hbar}\bigr)^{1/4}$$）。$$\blacksquare$$

### 3.10 被绕过的那条路

作为对照，把传统分析解法走一遍的清单（原文 MP47 逐条列出）：① 把定态方程写成变系数二阶线性 ODE；② 令 $$x\to\infty$$ 抓渐近解 $$e^{-x^2/2}$$；③ 去掉渐近因子得 Hermite 方程 $$h''-2xh'+2nh=0$$；④ 求 $$h$$ 的幂级数解；⑤ 由"波函数可归一"要求级数截断，得 $$n$$ 为整数与 Hermite 多项式；⑥ 用 Sturm–Liouville 理论检查正交性。六步中的每一步都要算，而且几乎不提供"为什么是这个谱"的理解。

代数路线只用了：一条对易关系 $$[X,P]=i\hbar I$$、一次因式分解、三个对易式 $$[a,a^\dagger]=I,\ [N,a]=-a,\ [N,a^\dagger]=a^\dagger$$。**传统路线的"级数必须截断"这个技术条件，在代数路线里变成了"本征值不能是负数"这条结构性事实**——同一个现象，两种说法，后者解释了前者。

## 四、几何与物理直觉 (Intuition)

### 4.1 相空间里的圆，被量子化后成了什么

经典谐振子在相空间 $$(x,p)$$ 里的两个等能面是同心椭圆 $$\frac{p^2}{2m}+\frac{m\omega^2}{2}x^2=E$$。做尺度变换 $$u=m\omega x,\ v=p$$，椭圆就变成圆

$$u^2+v^2 = 2mE .$$

复化坐标 $$z=u+iv$$ 后，圆就是 $$\lvert z\rvert^2 = 2mE$$——这正是原文 MP46 开头那句"看见 $$x^2+y^2$$ 就想到 $$z^*z$$"的几何出处。

量子化之后，$$z$$ 变成一个**算子**：$$a=\frac{1}{\sqrt{2m\hbar\omega}}(u+iv)$$、$$a^\dagger=\frac{1}{\sqrt{2m\hbar\omega}}(u-iv)$$。如果它们当真交换，$$a^\dagger a$$ 就正比于 $$u^2+v^2$$，能谱会是一条连续的射线，每个 $$E\ge0$$ 都可取——**经典圆变成了量子圆**。真实的差别发生在一次运算上：$$aa^\dagger - a^\dagger a = I$$。这一条**迫使圆的半径只能取离散值**，并且把圆心从"可能取 0"推高到了 $$\hbar\omega/2$$。

**几何一句话**：经典谐振子的相轨道是一圈圆；量子谐振子的"相圆"不是任意半径的圆，而是一族半径平方按 $$\hbar\omega(n+\tfrac12)$$ 等间距的圆。$$a$$ 与 $$a^\dagger$$ 是同一族圆上相邻两圈之间的"搬梯子"操作。

### 4.2 升降算符是一条梯子

定理 3.11 的图像可以画成一条半直线上的刻度：

$$\lambda=0\ \xrightarrow{\ a^\dagger\ }\ 1\ \xrightarrow{\ a^\dagger\ }\ 2\ \xrightarrow{\ a^\dagger\ }\ 3\ \xrightarrow{\ a^\dagger\ }\ \cdots$$

$$a$$ 把箭头全部反向。**向上走没有尽头**（因为没有上界：$$a^\dagger$$ 从不给出零向量，推论 3.13），**向下走必须停**（因为刻度都在 $$\ge0$$ 一侧，$$0$$ 就是地面）。地面那一点 $$\lambda=0$$ 的特殊性在于 $$a\psi_0=0$$：梯子到此为止。

这里有一个容易忽略的要点：**"能谱等间距"并不是因为势能是抛物线**，而是因为 $$[N,a]=-a$$ 右端的系数恰好是 $$-1$$（这是入口题 (vi) 的答案）。若对易子写成 $$[N,a]=-ca$$，梯子的步长就是 $$c$$，能谱变成等差数列。谐振子之所以特别好，是因为它对应的梯子**每级等高**。凡是有这种"每级等高"的梯子，代数方法就有效——角动量的 $$J_\pm$$（第 26 章）、氢原子的 $$SO(4)$$ 升降（第 07 章知识库）都是同一套技术。

### 4.3 为什么 $$a/a^\dagger$$ 不是"凑"出来的

一个自然会问的问题：定义 3.7 里那两个 $$\frac{1}{\sqrt{2m\hbar\omega}}$$ 是怎么想出来的？

先看要不要那个 $$\sqrt{\;}$$：因式分解 $$(m\omega X-iP)(m\omega X+iP)$$ 若直接令 $$a$$ 正比于 $$(m\omega X+iP)$$，则 $$a^\dagger a = \frac{1}{\lambda^2}(H/\hbar\omega-\tfrac12)$$，要求 $$[a,a^\dagger]=I$$ 就唯一地定出 $$\lambda^2=2m\hbar\omega$$。**归一化系数是被"要求对易子为 $$I$$"逼出来的**——$$I$$ 又是定理 3.8 后面所有递推的公共步长。这和入口题 (vi) 是同一个道理：所有常数都由代数关系反解出来。

再看 $$m\omega X$$ 与 $$P$$ 这两项：它们之所以配对，是因为经典 Hamilton 量是**正定二次型** $$2mH = (m\omega x)^2+p^2$$，而二阶正定的二元二次型在复化后总能配成一对共轭因式。这是习题 04 章"辛结构"在高斯型势能上的一个特例。

### 4.4 Gauss 与视界：基态为什么是 Gauss

基态 $$\psi_0\propto e^{-m\omega x^2/2\hbar}$$ 是**唯一**一类同时满足三件事的函数（专家依据 harmonic-fourier.md 第 4 节）：

1. 它的 Fourier 变换还是 Gauss（$$e^{-\pi x^2}$$ 是 Fourier 变换的特征函数）；
2. 它是 Heisenberg 不确定性原理的等号情形（$$\Delta x\cdot\Delta p = \hbar/2$$），即"最确定性"的量子态；
3. 它是热方程的热核，也是经典 Gauss 概率密度。

第 1 条解释了为什么基态在动量表象里长得一模一样；第 2 条解释了为什么它是能量的下界——**再想让它更"集中"，就得把动量摊得更开，动能会涨过势能**。第 3 条联系到 $$\lvert\psi_0\rvert^2$$ 是概率密度：$$x$$ 的分布是一个方差 $$\sigma^2=\hbar/(2m\omega)$$ 的正态分布。原文 MP47 提到的"传统解法要先抓渐近解"，抓的就是这个 Gauss；代数解法直接从 $$a\psi_0=0$$ 一步得到它。

### 4.5 几何 ↔ 物理 ↔ 代数，三条线的交点

本课程的贯穿主线在本章第一次完整出现：

| 几何 | 物理 | 代数 |
|---|---|---|
| 相空间里的圆 $$\lvert z\rvert^2=\text{const}$$ | 等能面 | 复二次型的因式分解 |
| 圆不可任意取半径 | 能量量子化 | $$[a,a^\dagger]=I$$ 迫使 $$Na=\dots$$ |
| 圆心被推离原点 | 零点能 $$\hbar\omega/2$$ | $$N\ge0$$ 与 $$a\psi_0=0$$ |
| 相邻两圈之间的"搬梯" | 吸收/放出能量子 | $$a$$、$$a^\dagger$$ 移动本征值 $$\mp1$$ |
| Gauss 曲线 | 最确定的态 | Fourier 特征函数 / 不确定度等号 |

第 16 章末尾留下的"谱是什么"这一问题，在本章得到了第一个可以算出来的答案：谱就是那条梯子上的刻度。

## 五、经典问题精讲 (Classical Problems)

五道题，全部只用定理 3.9 的三条对易关系与定理 3.11 的升降机制。

### 经典题 5.1（用代数关系解出全部算子恒等式）

**考点**：对易子的 Leibniz 律（定理 3.8，第 16 章）。**在本章结构里的位置**：定理 3.9 的完整化；原文 MP46 把这两条留作习题，我们把它补全。

**题**：只用 $$[a,a^\dagger]=I$$ 与 $$N=a^\dagger a$$，求 $$[a,N]$$ 与 $$[a^\dagger,N]$$。

**解**：由 Leibniz 律，对任意三个算子 $$A,B,C$$ 有 $$[A,BC]=[A,B]C+B[A,C]$$。取 $$A=a,\ B=a^\dagger,\ C=a$$：

$$[a,N] = [a,a^\dagger a] = [a,a^\dagger]a + a^\dagger[a,a] = I\cdot a + a^\dagger\cdot0 = a .$$

再取 $$A=a^\dagger,\ B=a^\dagger,\ C=a$$：

$$[a^\dagger,N] = [a^\dagger,a^\dagger a] = [a^\dagger,a^\dagger]a + a^\dagger[a^\dagger,a] = 0 + a^\dagger(-I) = -a^\dagger .$$

**关键 leap**：把 $$N$$ 看成乘积 $$a^\dagger a$$ 而不是一个独立对象。升降性质不是 $$N$$ 的"性质"，而是 $$N$$ 与 $$a$$ 之间对易关系的性质。

### 经典题 5.2（基态的方差与不确定性）

**考点**：内积与期望值（第 16 章定理 3.11）。**位置**：定理 3.3 后面那句"平稳态的概率密度不随时间变化"的具体实例。

**题**：设 $$\psi_0=\bigl(\frac{m\omega}{\pi\hbar}\bigr)^{1/4}e^{-m\omega x^2/2\hbar}$$。求 $$\langle X\rangle,\ \langle X^2\rangle,\ \langle P\rangle,\ \langle P^2\rangle$$，并验证 $$\Delta X\cdot\Delta P=\hbar/2$$。

**解**：

先算位置。被积函数 $$x\lvert\psi_0(x)\rvert^2$$ 是奇函数（$$x$$ 奇、$$\lvert\psi_0\rvert^2$$ 偶），在对称区间上积分为零：

$$\langle X\rangle = \int_{-\infty}^{\infty}x\lvert\psi_0\rvert^2dx = 0 .$$

$$\langle X^2\rangle = \int_{-\infty}^{\infty}x^2\lvert\psi_0\rvert^2dx = \bigl(\frac{m\omega}{\pi\hbar}\bigr)^{1/2}\int_{-\infty}^{\infty}x^2e^{-m\omega x^2/\hbar}dx .$$

用 Gauss 矩公式 $$\int_{-\infty}^\infty x^2e^{-\alpha x^2}dx = \frac{1}{2}\sqrt{\frac{\pi}{\alpha^3}}$$，取 $$\alpha=\frac{m\omega}{\hbar}$$：

$$\langle X^2\rangle = \bigl(\tfrac{m\omega}{\pi\hbar}\bigr)^{1/2}\cdot\frac12\Bigl(\frac{\pi\hbar^3}{m^3\omega^3}\Bigr)^{1/2} = \frac{1}{2}\cdot\frac{\hbar^{1/2}}{\hbar^{1/2}}\cdot\frac{\hbar^{3/2}}{\hbar^{1/2}}\cdot\frac{1}{m\omega} = \frac{\hbar}{2m\omega}.$$

（逐因子核对：$$\bigl(\frac{m\omega}{\pi\hbar}\bigr)^{1/2}\cdot\frac12\pi^{1/2}\frac{\hbar^{3/2}}{m^{3/2}\omega^{3/2}} = \frac12\frac{(m\omega)^{1/2}}{\hbar^{1/2}}\frac{\hbar^{3/2}}{(m\omega)^{3/2}} = \frac{\hbar}{2m\omega}$$。）

再算动量。利用 $$\psi_0'=-\frac{m\omega}{\hbar}x\psi_0$$：

$$P\psi_0 = -i\hbar\psi_0' = i m\omega\,x\psi_0 .$$

$$\langle P\rangle = \langle\psi_0\vert P\psi_0\rangle = \int \overline{\psi_0}\cdot im\omega x\psi_0\,dx = im\omega\int x\lvert\psi_0\rvert^2dx = 0 .$$

$$\langle P^2\rangle = \lVert P\psi_0\rVert^2 = (m\omega)^2\int x^2\lvert\psi_0\rvert^2dx = (m\omega)^2\cdot\frac{\hbar}{2m\omega} = \frac{m\omega\hbar}{2}.$$

于是

$$\Delta X^2 = \langle X^2\rangle-\langle X\rangle^2 = \frac{\hbar}{2m\omega},\qquad \Delta P^2 = \langle P^2\rangle-\langle P\rangle^2 = \frac{m\omega\hbar}{2},$$

$$\Delta X\cdot\Delta P = \sqrt{\frac{\hbar}{2m\omega}}\cdot\sqrt{\frac{m\omega\hbar}{2}} = \frac{\hbar}{2}.$$

这正是 Heisenberg 不等式的等号情形（harmonic-fourier.md 第 4 节）。**关键 leap**：$$\langle P^2\rangle$$ 不要展开成一个带二阶导数的积分再做分部积分，而是**认出 $$P\psi_0$$ 正比于 $$x\psi_0$$**——这一步来自基态方程本身。

### 经典题 5.3（Hermite 递推从算子来）

**考点**：提升算子与乘位置算子的关系。**位置**：定理 3.17 的逆定理——不从递推造出 $$\psi_n$$，而是从 $$\psi_n$$ 反读递推。

**题**：设 $$\psi_n=c_nh_ne^{-x^2/2}$$（$$c_n=c_0/\sqrt{2^nn!}$$，$$h_n$$ 是首项系数 $$2^n$$ 的 Hermite 多项式）。求 $$X$$ 在能级基下的矩阵元，并由此导出 Hermite 递推 $$h_{n+1}=2xh_n-2nh_{n-1}$$ 与 $$\langle x\rangle_n=\langle\psi_n\vert X\psi_n\rangle=0$$。

**解**：分四步。先用算子代数求出 $$X$$ 在能级基下的矩阵元，再把它翻译回 $$h_n$$。

**第一步（升降算子的归一化作用）**。设 $$\psi_n$$ 已归一，$$N\psi_n=n\psi_n$$。由 $$N=a^\dagger a$$，

$$\lVert a\psi_n\rVert^2 = \langle a\psi_n\vert a\psi_n\rangle = \langle\psi_n\vert a^\dagger a\psi_n\rangle = \langle\psi_n\vert N\psi_n\rangle = n ,$$

且 $$a\psi_n$$ 是本征值 $$n-1$$ 的本征向量（引理 3.10），故它必须是 $$\psi_{n-1}$$ 的倍数；模长已算出为 $$\sqrt n$$，且相因子可吸收进 $$\psi_{n-1}$$ 的定义，取

$$a\psi_n = \sqrt n\,\psi_{n-1}\qquad(n\ge1).$$

同理，$$\lVert a^\dagger\psi_n\rVert^2 = \langle\psi_n\vert aa^\dagger\psi_n\rangle = \langle\psi_n\vert(N+I)\psi_n\rangle = n+1$$（用了 $$aa^\dagger=N+I$$，这是定理 3.9 的推论），故

$$a^\dagger\psi_n = \sqrt{n+1}\,\psi_{n+1}.$$

**第二步（$$X$$ 的三对角形式）**。在归一化坐标下反解定义 3.7 得 $$X=\frac{1}{\sqrt2}\bigl(a+a^\dagger\bigr)$$。代入第一步：

$$X\psi_n = \frac{1}{\sqrt2}\Bigl(\sqrt n\,\psi_{n-1}+\sqrt{n+1}\,\psi_{n+1}\Bigr). \tag{5.1}$$

(5.1) 就是 $$X$$ 在能级基下的矩阵元：$$\langle\psi_{n-1}\vert X\psi_n\rangle=\langle\psi_n\vert X\psi_{n-1}\rangle=\sqrt{n/2}$$，其余为零。$$X$$ 在这组基下是**三对角**的。

**第三步（翻译回 $$h_n$$）**。把 (5.1) 的左端写成 $$x\,c_nh_ne^{-x^2/2}$$，右端写成 $$c_{n-1}\sqrt{\frac n2}h_{n-1}e^{-x^2/2}+c_{n+1}\sqrt{\frac{n+1}2}h_{n+1}e^{-x^2/2}$$，两边约去 $$e^{-x^2/2}$$ 再除以 $$c_n$$：

$$xh_n = \Bigl(\frac{c_{n-1}}{c_n}\sqrt{\frac n2}\Bigr)h_{n-1} + \Bigl(\frac{c_{n+1}}{c_n}\sqrt{\frac{n+1}2}\Bigr)h_{n+1}.$$

第一个括号是 $$\frac{1}{\sqrt{2n}}\cdot\sqrt{\frac n2}=\frac12$$，第二个括号是 $$\frac{1}{\sqrt{2(n+1)}}\cdot\sqrt{\frac{n+1}{2}}=\frac12$$。于是得到 **Hermite 多项式的一条基本恒等式**

$$xh_n = \tfrac12h_{n-1}+\tfrac12h_{n+1},\qquad\text{即}\qquad 2xh_n = h_{n-1}+h_{n+1}. \tag{5.2}$$

**第四步（化到标准递推）**。先由生成函数 $$h_n(x)=(-1)^ne^{x^2}\frac{d^n}{dx^n}e^{-x^2}$$ 得到导数递推 $$h_n'=2n\,h_{n-1}$$（对 $$n$$ 归纳，见竞4）。再由定理 3.17 的递推 $$h_{n+1}=\frac1{\sqrt2}\bigl(2xh_n-h_n'\bigr)$$ 代入：

$$h_{n+1} = \frac{1}{\sqrt2}\bigl(2xh_n-2n\,h_{n-1}\bigr). \tag{5.3}$$

把 (5.2) 解出的 $$h_{n-1}=2xh_n-h_{n+1}$$ 代入 (5.3)：

$$\sqrt2\,h_{n+1} = 2xh_n-2n(2xh_n-h_{n+1}) = 2(1-2n)xh_n+2n\,h_{n+1},$$

$$(\sqrt2-2n)h_{n+1} = 2(1-2n)xh_n .$$

它与 (5.2) 联立，即得 Hermite 多项式的标准**三项递推**

$$h_{n+1} = 2xh_n - 2n\,h_{n-1}. \tag{5.4}$$

**低阶验算**（锁定约定）：$$h_0=1$$、$$h_1=2x$$、$$h_2=4x^2-2$$、$$h_3=8x^3-12x$$（与例 3.1 一致）。用 (5.4)：$$h_2=2x\cdot2x-2\cdot1\cdot1=4x^2-2$$；$$h_3=2x(4x^2-2)-2\cdot2\cdot2x=8x^3-4x-8x=8x^3-12x$$。两条都吻合。$$\blacksquare$$

**期望值**：由 (5.1) 与正交性，

$$\langle\psi_n\vert X\psi_n\rangle = \sqrt{\frac n2}\langle\psi_n\vert \psi_{n-1}\rangle+\sqrt{\frac{n+1}{2}}\langle\psi_n\vert \psi_{n+1}\rangle = 0 .$$

**关键 leap**：把"求 Hermite 递推"变成"数算子作用在归一化态上"，一次性得到 $$\sqrt n$$、$$\sqrt{n+1}$$ 这两个系数、$$X$$ 的整张三对角矩阵 (5.1)、以及 Hermite 的全部两条递推。这两个根号是量子力学里"矩阵元含 $$\sqrt n$$"的原始出处（量子化电磁场中 $$\sqrt n$$ 就是"$$n$$ 个光子"的根号）。

### 经典题 5.4（叠加态的时间演化）

**考点**：定理 3.4 的叠加解。**位置**：本章唯一一道真正"含时"的题；也是"平稳态不含时、叠加态含时"的最简演示。

**题**：取 $$\psi(x,0)=\frac{1}{\sqrt2}\bigl(\psi_0(x)+\psi_1(x)\bigr)$$。求 $$\psi(x,t)$$ 与 $$\langle X\rangle(t)$$。

**解**：由定理 3.4，每个本征态自己带一个相位：

$$\psi(x,t) = \frac{1}{\sqrt2}\Bigl(\psi_0(x)e^{-iE_0t/\hbar} + \psi_1(x)e^{-iE_1t/\hbar}\Bigr).$$

记 $$\omega=E_1-E_0=\hbar\omega/\hbar=\omega$$（本征能级差恰是经典频率，推论 3.12），提出公因子：

$$\psi(x,t) = \frac{e^{-iE_0t/\hbar}}{\sqrt2}\Bigl(\psi_0(x) + \psi_1(x)e^{-i\omega t}\Bigr).$$

期望值。由 (5.1)：$$\langle\psi_0\vert X\psi_1\rangle = \sqrt{\frac12}$$，$$\langle\psi_1\vert X\psi_0\rangle = \sqrt{\frac12}$$，$$\langle\psi_0\vert X\psi_0\rangle=\langle\psi_1\vert X\psi_1\rangle=0$$。于是

$$
\langle X\rangle(t) = \frac12\Bigl[\langle\psi_0\vert X\psi_0\rangle + \lvert e^{-i\omega t}\rvert^2\langle\psi_1\vert X\psi_1\rangle + e^{-i\omega t}\langle\psi_0\vert X\psi_1\rangle + e^{i\omega t}\langle\psi_1\vert X\psi_0\rangle\Bigr]
$$

$$= \frac12\Bigl[0+0+\sqrt{\frac12}e^{-i\omega t} + \sqrt{\frac12}e^{i\omega t}\Bigr] = \sqrt{\frac12}\cos\omega t .$$

**读法**：波包以角频率 $$\omega$$ **振荡**起来——这正是经典谐振子的运动。但它的振幅 $$\sqrt{1/2}=\ell/\sqrt2$$（$$\ell=\sqrt{\hbar/(m\omega)}$$）是量子的，且期望值 $$x$$ 在 $$\pm\ell/\sqrt2$$ 之间往返，而概率密度 $$\lvert\psi\rvert^2$$ 每半个周期回到原形。**只有叠加态才动，单个平稳态不动**——这是定理 3.3 的物理后果。

**关键 leap**：认出 $$\langle X\rangle$$ 只含交叉项，因此只与 $$\lvert e^{-i\omega t}\rvert$$ 的**相位**有关；相位差的频率就是能级差除以 $$\hbar$$，这正是 Bohr 频率条件。

### 经典题 5.5（经典极限：大 $$n$$ 时能级"变连续"）

**考点**：推论 3.12 与量子-经典对应的极限。**位置**：把本章结果接到第 09 章的准经典近似。

**题**：设 $$n\gg1$$。证明能级间距与能级本身的相对比值趋于零，并估计"要看到离散谱，需要多大 $$n$$"。

**解**：相邻能级差恒为

$$\Delta E = E_{n+1}-E_n = \hbar\omega\Bigl(n+\tfrac32\Bigr)-\hbar\omega\Bigl(n+\tfrac12\Bigr) = \hbar\omega .$$

它是**常数**，不随 $$n$$ 变。但相对间距是

$$\frac{E_{n+1}-E_n}{E_n} = \frac{\hbar\omega}{\hbar\omega(n+\tfrac12)} = \frac{1}{n+\tfrac12}\xrightarrow{n\to\infty}0 .$$

设能量为 $$E$$，则 $$n\approx E/(\hbar\omega)$$，相对间距 $$\approx\hbar\omega/E$$。设系统能量 $$E=1\ \mathrm{J}$$、频率 $$\omega/(2\pi)=1\ \mathrm{Hz}$$，则 $$\hbar\omega\approx6.6\times10^{-34}\ \mathrm{J}$$，相对间距 $$\approx6.6\times10^{-34}$$——小到任何实验都分不出，谱在宏观尺度上"变连续"。

**关键 leap**：区分"绝对间距"与"相对间距"。绝对间距永远是 $$\hbar\omega$$，量子化永不消失；是**相对**间距在宏观 $$n$$ 下趋于零。这个视角是 Bohr 对应原理的定量版本，也是为什么实验室里只能用分子振动或低温冷原子（$$n$$ 小、能量小）看到分立能级。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 本章的第一件技术是**分离变量 (separation of variables)**。设 $$H$$ 与 $$t$$ 无关，$$\psi(x,t)=\Psi(x)T(t)$$ 是含时 Schrödinger 方程（定义 3.1）的解，且 $$\Psi\neq0$$。请 (i) 把 $$\psi$$ 代回方程，说明为什么两端可以同等于一个常数 $$E$$；(ii) 写出 $$\Psi$$ 与 $$T$$ 各自满足的方程；(iii) 证明 $$E$$ 必为实数，并解出 $$T(t)$$。

**基2.** (i) 在归一化坐标（$$m=\hbar=\omega=1$$）下，用定义 3.7 与 $$[X,P]=iI$$ 直接算出 $$[a,a^\dagger]$$、$$[N,a]$$、$$[N,a^\dagger]$$；(ii) 证明 $$N=a^\dagger a$$ 是对称算子，并由此说明它的本征值必为实数且非负。

**基3.** 写出基态方程 $$a\psi_0=0$$ 在归一化坐标下的显式一阶微分方程，解出 $$\psi_0$$，并定出归一化常数。

**基4.** 用定理 3.17 的递推算出 $$H_0,H_1,H_2,H_3$$ 的显式表达式（允许差一个整体常数因子），并写出对应的三个能级 $$E_0,E_1,E_2$$。

### 竞赛（本课目标难度）

**竞1.** 证明 $$[a,e^{\lambda a^\dagger}]=\lambda e^{\lambda a^\dagger}$$，其中 $$\lambda\in\mathbb C$$，$$e^{\lambda a^\dagger}=\sum_{n\ge0}\frac{\lambda^n}{n!}(a^\dagger)^n$$。并证明 $$e^{\lambda a^\dagger}\psi_0$$ 是 $$N$$ 的本征向量当且仅当……（把结论说清楚）。

**竞2.** 设 $$\{\psi_n\}$$ 是归一化的能级基。用引理 3.16 与 $$X=\frac{1}{\sqrt2}\bigl(a+a^\dagger\bigr)$$ 证明

$$\langle\psi_m\vert X\psi_n\rangle = \sqrt{\frac n2}\,\delta_{m,n-1}+\sqrt{\frac{n+1}{2}}\,\delta_{m,n+1},$$

并求 $$P$$ 的矩阵元。

**竞3.** 设 $$\psi(x,0)=\psi_1(x)$$（第一激发态）。先凭直觉猜 $$\langle X\rangle(t)$$ 与 $$\langle X^2\rangle(t)$$ 哪一个会随时间变，再严格算出两者来检验猜测；若两者都不变，请另找一个真正含时的量并算出它。

**竞4.** 用生成函数 $$G(x,t)=e^{2xt-t^2}=\sum_{n\ge0}\frac{h_n(x)}{n!}t^n$$ 证明 $$h_n'=2n\,h_{n-1}$$ 与 $$h_{n+1}=2xh_n-2n\,h_{n-1}$$。

**竞5.**（是入口题 (vi) 的抽象）设 $$\mathscr A$$ 是一个结合代数，$$N,a,a^\dagger\in\mathscr A$$ 满足 $$[N,a]=-ca$$、$$[N,a^\dagger]=ca^\dagger$$（$$c>0$$ 是常数）。(i) 证明：若 $$\psi$$ 是 $$N$$ 的本征向量、本征值 $$\lambda$$，则 $$a\psi$$、$$a^\dagger\psi$$ 一旦非零就是 $$N$$ 的本征向量，本征值分别为 $$\lambda-c$$、$$\lambda+c$$；并由此说明"能级等间距"完全是 $$[N,a]=-ca$$ 中右端系数为常数这件事的推论。(ii) 把 (i) 用到 $$c=1$$ 的情形，说明为什么 $$N$$ 的正定性是"梯子必须停"的全部原因；如果 $$N$$ 不正定，能谱会变成什么？

### 研究（通向下一章）

**研1.**（算子的无界性）证明谐振子的 $$X,P,H,N$$ 都不是有界算子；并说明为什么前面所有关于"本征值""本征向量"的讨论都必须附加"定义域"这一层。研究档提示：这正是第 18 章的入口。

**研2.**（升降机制的 Lie 代数读法）考虑两个算子

$$K_+ = \frac{i}{2\hbar}P+\frac{m\omega}{2\hbar}X,\qquad K_- = \frac{i}{2\hbar}P-\frac{m\omega}{2\hbar}X .$$

求 $$[K_+,K_-]$$ 与 $$[H,K_\pm]$$，说明 $$\{K_+,K_-,H\}$$ 张成怎样一个 Lie 代数，并指出本章的升降机制在这个代数里对应什么。研究档提示：这个对象在第 22 章（正则对易关系与 Stone–von Neumann）与第 38–39 章（Lorentz 群的表示论）会以完整形态回来。

### 解答 (Solutions)

**解 基1.** 思路：分离变量之所以合法，只因为 $$H$$ 只对 $$x$$ 作用、$$\partial_t$$ 只对 $$t$$ 作用，两个自变量互不干涉。

**(i) 为什么两端必同等于一个常数。** 因为 $$H$$ 不含 $$t$$，它作用在乘积上时把 $$T(t)$$ 当常数提出来。把 $$\psi=\Psi(x)T(t)$$ 代入含时方程 $$i\hbar\partial_t\psi=H\psi$$，左端是 $$i\hbar\,\Psi(x)T'(t)$$，右端是 $$(H\Psi)(x)\,T(t)$$，即

$$i\hbar\,\Psi(x)T'(t)=\bigl(H\Psi\bigr)(x)\,T(t).$$

在 $$\Psi(x)T(t)\neq0$$ 的点上两边同除，得

$$i\hbar\,\frac{T'(t)}{T(t)}=\frac{(H\Psi)(x)}{\Psi(x)} .$$

左端只含 $$t$$、右端只含 $$x$$。固定使 $$\Psi(x)\neq0$$ 的 $$x$$、让 $$t$$ 变动：右端是常数，故左端也只能是常数；反过来也成立。于是两端同等于一个与 $$x,t$$ 都无关的常数。**这个常数的存在性就是分离变量的全部内容**——它不是假设，而是"两个自变量相互独立"的推论。把它记作 $$E$$。

**(ii) 两个方程。** 于是 $$H\Psi=E\Psi$$（这正是定义 3.2 的定态方程），以及 $$i\hbar T'=ET$$（时间部分的一阶方程）。

**(iii) $$E\in\mathbb R$$ 与 $$T(t)$$。** 由第 16 章 $$H$$ 自伴，把 $$H$$ 从内积的一侧挪到另一侧只取复共轭：

$$\overline{\langle\Psi\vert H\Psi\rangle}=\langle H\Psi\vert\Psi\rangle=\langle\Psi\vert H\Psi\rangle,$$

故 $$\langle\Psi\vert H\Psi\rangle\in\mathbb R$$。而 $$E\langle\Psi\vert\Psi\rangle=\langle\Psi\vert H\Psi\rangle$$ 且 $$\lVert\Psi\rVert\neq0$$，于是

$$E=\frac{\langle\Psi\vert H\Psi\rangle}{\lVert\Psi\rVert^2}\in\mathbb R .$$

又 $$T'=-iET/\hbar$$ 是常系数一阶方程，通解为 $$T(t)=c\,e^{-iEt/\hbar}$$（$$c\in\mathbb C$$）。$$e^{-iEt/\hbar}$$ 的模恒为 $$1$$，所以把常数 $$c$$ 吸收进 $$\Psi$$ 后就得

$$\psi(x,t)=\Psi(x)\,e^{-iEt/\hbar}.$$

**读法**：空间部分解一个本征方程、时间部分乘一个相位因子。相位不进模长，故 $$\lvert\psi(x,t)\rvert^2=\lvert\Psi(x)\rvert^2$$ 与 $$t$$ 无关——这就是"平稳"二字的来源（定理 3.3）。$$\blacksquare$$

**解 基2.** 归一化坐标下 $$X$$ 是乘 $$x$$、$$P=-i\partial_x$$，且 $$[X,P]=iI$$（注意 $$\hbar=1$$）。先算 $$[a,a^\dagger]$$：

$$[a,a^\dagger] = \Bigl[\tfrac{1}{\sqrt2}(X+iP),\ \tfrac{1}{\sqrt2}(X-iP)\Bigr] = \frac12\Bigl([X,-iP]+[iP,X]\Bigr) = \frac12\bigl(-i[X,P]+i[P,X]\bigr).$$

代入 $$[X,P]=iI$$、$$[P,X]=-iI$$：$$= \frac12\bigl(-i\cdot iI + i\cdot(-iI)\bigr) = \frac12\bigl(I+I\bigr) = I$$。

再算 $$[N,a]$$ 与 $$[N,a^\dagger]$$：与经典题 5.1 同法，用 $$N=a^\dagger a$$ 与 Leibniz 律，

$$[a,N] = [a,a^\dagger a] = [a,a^\dagger]a + a^\dagger[a,a] = I\cdot a = a,$$

$$[a^\dagger,N] = [a^\dagger,a^\dagger a] = a^\dagger[a^\dagger,a] = a^\dagger\cdot(-I) = -a^\dagger .$$

即 $$[N,a]=-a$$、$$[N,a^\dagger]=a^\dagger$$。

**(ii) $$N$$ 是对称算子，本征值为实数且非负。** 设 $$\varphi,\psi\in\operatorname{Dom}N$$。由 $$N=a^\dagger a$$（定义 3.7 中 $$a^\dagger$$ 是 $$a$$ 的伴随）与内积的线性，

$$\langle\varphi\vert N\psi\rangle = \langle\varphi\vert a^\dagger a\psi\rangle = \langle a\varphi\vert a\psi\rangle,$$

$$\langle N\varphi\vert \psi\rangle = \langle a^\dagger a\varphi\vert \psi\rangle = \langle a\varphi\vert a\psi\rangle .$$

两式右端相同，故 $$\langle\varphi\vert N\psi\rangle=\langle N\varphi\vert \psi\rangle$$，即 $$N$$ 对称。取 $$\varphi=\psi$$ 为本征向量、$$N\psi=\lambda\psi$$：

$$\lambda\langle\psi\vert \psi\rangle=\langle\psi\vert N\psi\rangle=\langle a\psi\vert a\psi\rangle=\lVert a\psi\rVert^2\in\mathbb R .$$

右边是非负实数，$$\langle\psi\vert \psi\rangle$$ 是正实数，故 $$\lambda=\lVert a\psi\rVert^2/\lVert\psi\rVert^2$$ 既是实数又 $$\ge0$$。$$\blacksquare$$

**解 基3.** 归一化坐标下 $$a=\frac{1}{\sqrt2}(x+\partial_x)$$（把定义 3.7 里 $$m=\hbar=\omega=1$$、$$\ell=1$$、$$P=-i\partial_x$$ 代入）。方程 $$a\psi_0=0$$ 等价于

$$\psi_0'(x) = -x\,\psi_0(x).$$

两边除以 $$\psi_0$$（在 $$\psi_0\neq0$$ 处）得 $$\frac{\psi_0'}{\psi_0}=-x$$，积分得 $$\ln\lvert\psi_0\rvert=-\frac{x^2}{2}+C$$，故 $$\psi_0(x)=ce^{-x^2/2}$$。归一化：

$$1 = \lvert c\rvert^2\int_{-\infty}^{\infty}e^{-x^2}dx = \lvert c\rvert^2\sqrt\pi\ \Longrightarrow\ \lvert c\rvert=\pi^{-1/4}.$$

取 $$c=\pi^{-1/4}$$ 得 $$\psi_0=\pi^{-1/4}e^{-x^2/2}$$。$$\blacksquare$$

**解 基4.** 用定理 3.17 的递推 $$H_{n+1}=\frac{1}{\sqrt2}\bigl(2xH_n-H_n'\bigr)$$ 从 $$H_0=1$$ 出发：

$$H_1 = \frac{1}{\sqrt2}\bigl(2x\cdot1-0\bigr) = \sqrt2\,x,$$

$$H_2 = \frac{1}{\sqrt2}\bigl(2x\cdot\sqrt2x - \sqrt2\bigr) = \frac{1}{\sqrt2}\cdot\sqrt2\,(2x^2-1) = 2x^2-1,$$

$$H_3 = \frac{1}{\sqrt2}\bigl(2x(2x^2-1)-4x\bigr) = \frac{1}{\sqrt2}\bigl(4x^3-2x-4x\bigr) = \frac{1}{\sqrt2}\bigl(4x^3-6x\bigr) = 2\sqrt2\,x^3-3\sqrt2\,x .$$

（与标准 Hermite 多项式差归一化常数：$$h_n=\sqrt{2^nn!}\,H_n$$，故 $$h_0=1$$，$$h_1=2x$$，$$h_2=4x^2-2$$，$$h_3=8x^3-12x$$，正是例 3.1。）对应能级由推论 3.12：$$E_n=\hbar\omega(n+\tfrac12)$$，取 $$\hbar=\omega=1$$ 得

$$E_0=\tfrac12,\qquad E_1=\tfrac32,\qquad E_2=\tfrac52 .$$

$$\blacksquare$$

**解 竞1.** **关键 leap**：直接展开指数会有无穷多项，正确的做法是**先把 $$[a,(\ a^\dagger)^n]$$ 用归纳法算出来**，再用 Leibniz 律求和。

**第一步：算 $$[a,(a^\dagger)^n]$$。** 对 $$n$$ 归纳。$$n=0$$ 时 $$[a,I]=0$$，$$n$$ 时用 Leibniz 律：

$$[a,(a^\dagger)^{n+1}] = [a,(a^\dagger)^n]a^\dagger + (a^\dagger)^n[a,a^\dagger] = n(a^\dagger)^{n-1}a^\dagger + (a^\dagger)^n\cdot I = (n+1)(a^\dagger)^n .$$

（归纳步用到 $$[a,a^\dagger]=I$$。）故

$$[a,(a^\dagger)^n] = n\,(a^\dagger)^{n-1}\qquad(n\ge1). \tag{E1}$$

**第二步：求和。** 由 $$e^{\lambda a^\dagger}=\sum_{n\ge0}\frac{\lambda^n}{n!}(a^\dagger)^n$$（在适当的收敛意义下，见第 21 章），

$$[a,e^{\lambda a^\dagger}] = \sum_{n\ge1}\frac{\lambda^n}{n!}\bigl[a,(a^\dagger)^n\bigr] = \sum_{n\ge1}\frac{\lambda^n}{n!}\,n\,(a^\dagger)^{n-1} = \lambda\sum_{n\ge1}\frac{\lambda^{n-1}}{(n-1)!}(a^\dagger)^{n-1} = \lambda\,e^{\lambda a^\dagger}.$$

（$$n=0$$ 项因 $$[a,I]=0$$ 而消失。）

**第三步：对基态的作用，以及本题的答案。** 展开 $$e^{\lambda a^\dagger}\psi_0$$。先用归纳法算 $$(a^\dagger)^n\psi_0$$：由 $$a^\dagger\psi_n=\sqrt{n+1}\psi_{n+1}$$，

$$(a^\dagger)^n\psi_0 = \sqrt{n!}\,\psi_n, \tag{E2}$$

（验证：$$n=1$$ 时 $$a^\dagger\psi_0=\psi_1$$，$$\sqrt{1!}=1$$；归纳步 $$(a^\dagger)^{n+1}\psi_0=a^\dagger\sqrt{n!}\psi_n=\sqrt{n!}\sqrt{n+1}\psi_{n+1}=\sqrt{(n+1)!}\psi_{n+1}$$。）于是

$$e^{\lambda a^\dagger}\psi_0 = \sum_{n\ge0}\frac{\lambda^n}{n!}\sqrt{n!}\,\psi_n = \sum_{n\ge0}\frac{\lambda^n}{\sqrt{n!}}\,\psi_n . \tag{E3}$$

这是一个**无穷多个能级的叠加**，每个 $$\psi_n$$ 都带非零系数（只要 $$\lambda\neq0$$）。所以 **$$e^{\lambda a^\dagger}\psi_0$$ 是 $$N$$ 的本征向量当且仅当 $$\lambda=0$$**（此时它就是 $$\psi_0$$）。原题的"当且仅当"条件就是这个。

**第四步：这个态是什么。** 它不是 $$N$$ 的本征向量，却是 $$a$$ 的本征向量。由 $$a\psi_n=\sqrt n\psi_{n-1}$$，

$$a\Bigl(\sum_{n\ge0}\frac{\lambda^n}{\sqrt{n!}}\psi_n\Bigr) = \sum_{n\ge1}\frac{\lambda^n}{\sqrt{n!}}\sqrt n\,\psi_{n-1} = \lambda\sum_{m\ge0}\frac{\lambda^m}{\sqrt{m!}}\psi_m,$$

即

$$a\bigl(e^{\lambda a^\dagger}\psi_0\bigr) = \lambda\bigl(e^{\lambda a^\dagger}\psi_0\bigr).$$

**$$a$$ 不是自伴算子，它的本征值可以是任意复数**（这与定理 3.11 里 $$N$$ 的实本征值不矛盾——定理 3.11 说的是自伴的 $$N$$）。这个态叫**相干态 (coherent state)**：它的 $$\langle X\rangle(t)$$ 精确按经典轨迹 $$\cos\omega t$$ 振荡，是量子光学里激光所处的态。它的归一化范数是 $$\sum_n\lvert\lambda\rvert^{2n}/n!=e^{\lvert\lambda\rvert^2}$$，故归一化后为 $$e^{-\lvert\lambda\rvert^2/2}e^{\lambda a^\dagger}\psi_0$$。

**再记一句**：这类"算指数上的对易子"的题，唯一的通路是先算 $$[a,(a^\dagger)^n]$$ 的归纳公式 (E1)，再求和；不要试图直接对指数用 Leibniz 律。还要记住 $$e^{\lambda a^\dagger}$$ 不是酉算子（$$a^\dagger$$ 不对易于 $$a$$），所以它把 $$N$$ 的本征态搬到 $$a$$ 的本征态，而不是搬到 $$N$$ 的另一本征态。

**解 竞2.** **关键 leap**：不要把 $$\langle\psi_m\vert X\psi_n\rangle$$ 当积分去硬算。把 $$X$$ 用 $$a,a^\dagger$$ 表出之后，$$X\psi_n$$ 只剩两项，矩阵元就是"降一格、升一格"的算术；再把 $$P=-\frac{i}{\sqrt2}(a-a^\dagger)$$ 照做一遍，符号自然出现。

$$X$$ 的矩阵元已在经典题 5.3 的 (5.1) 算出：

$$X\psi_n = \sqrt{\frac n2}\,\psi_{n-1}+\sqrt{\frac{n+1}{2}}\,\psi_{n+1},$$

两边与 $$\psi_m$$ 作内积并用正交归一性立即得

$$\langle\psi_m\vert X\psi_n\rangle = \sqrt{\frac n2}\,\delta_{m,n-1}+\sqrt{\frac{n+1}{2}}\,\delta_{m,n+1}. \tag{E4}$$

对 $$P$$，同样在归一化坐标下反解定义 3.7：$$P = \frac{1}{\sqrt2\,i}\bigl(a-a^\dagger\bigr) = -\frac{i}{\sqrt2}(a-a^\dagger)$$。于是

$$P\psi_n = -\frac{i}{\sqrt2}\Bigl(\sqrt n\,\psi_{n-1}-\sqrt{n+1}\,\psi_{n+1}\Bigr),$$

$$\langle\psi_m\vert P\psi_n\rangle = -i\sqrt{\frac n2}\,\delta_{m,n-1}+i\sqrt{\frac{n+1}{2}}\,\delta_{m,n+1}. \tag{E5}$$

核对 $$P$$ 的对称性：$$\langle\psi_{n-1}\vert P\psi_n\rangle = -i\sqrt{n/2}$$，而 $$\langle\psi_n\vert P\psi_{n-1}\rangle = i\sqrt{n/2}$$，两者互为共轭（$$\overline{-i\sqrt{n/2}}=i\sqrt{n/2}$$）——正确。$$\blacksquare$$

**解 竞3.** **关键 leap**：不要被"运动"的直觉带走。单个平稳态的一切期望值都不含时（相位不进模长），真正含时的量只能来自**叠加态的交叉项**。猜到这一层，计算就只剩两步。

单个平稳态的时间演化只是一个相位（定理 3.3），而相位不进模长：设 $$\psi(t)=\psi_1e^{-iE_1t/\hbar}$$，则对任意自伴算子 $$A$$，

$$\langle\psi(t)\vert A\psi(t)\rangle = \langle\psi_1\vert A\psi_1\rangle$$

与 $$t$$ 无关。所以 **$$\langle X\rangle(t)=\langle X\rangle(0)=0$$（由 (E4) 对角元为零），$$\langle X^2\rangle(t)=\langle X^2\rangle(0)$$ 也不变。** 这与"第一激发态在动"的直觉相反——**单个平稳态的一切期望值都不含时**，这与它是否"激发"无关。

时间依赖只可能来自**叠加态**的交叉项。取"真正含时的量"就取 $$\psi(0)=\frac{1}{\sqrt2}\bigl(\psi_0+\psi_1\bigr)$$。由定理 3.4，

$$\psi(t)=\frac{1}{\sqrt2}\Bigl(\psi_0e^{-iE_0t/\hbar}+\psi_1e^{-iE_1t/\hbar}\Bigr).$$

用 $$X\psi_n=\sqrt{\frac n2}\,\psi_{n-1}+\sqrt{\frac{n+1}{2}}\,\psi_{n+1}$$ 与 (E4)：对角元为零，非零的交叉项只有 $$\langle\psi_0\vert X\psi_1\rangle=\langle\psi_1\vert X\psi_0\rangle=\sqrt{1/2}$$，于是

$$\langle X\rangle(t)=\frac12\Bigl[\overline{\langle\psi_0\vert X\psi_1\rangle}\,e^{-i(E_1-E_0)t/\hbar}+\langle\psi_1\vert X\psi_0\rangle\,e^{i(E_1-E_0)t/\hbar}\Bigr]=\frac{1}{\sqrt2}\cos\omega t,$$

最后一步用了 $$E_1-E_0=\hbar\omega$$（推论 3.12）。这就是真正含时的量：它以**经典频率** $$\omega$$ 振荡，振幅 $$\ell/\sqrt2$$（经典题 5.4 已从另一条路算过同一个数）。

$$\langle X^2\rangle$$ 要变，需要交叉项 $$\langle\psi_m\vert X^2\psi_n\rangle\neq0$$（$$m\neq n$$）。在能级基下 $$X^2$$ 连接 $$\lvert m-n\rvert\le2$$，所以 $$\psi_0,\psi_1$$ 的叠加里只有 $$\langle\psi_0\vert X^2\psi_1\rangle$$ 这一项给出频率 $$\omega$$ 的振荡（$$\langle\psi_0\vert X^2\psi_2\rangle$$ 的频率是 $$2\omega$$，但 $$\psi_2$$ 系数为零，不出现）。

**小结**：先想清楚"平稳态的期望值一律不含时"这条，再去找真正含时的量——它必然是叠加态的交叉项。$$\blacksquare$$

**解 竞4.** **关键 leap**：两条递推都来自同一个生成函数——对 $$x$$ 求一次偏导得导数递推，对 $$t$$ 求一次偏导得三项递推。技巧上唯一要认准的是"**比较 $$t^n$$ 的系数**"，不要在 $$t$$ 的幂次上绕圈。

记 $$G(x,t)=e^{2xt-t^2}=\sum_{n\ge0}\frac{h_n(x)}{n!}t^n$$。

**导公式 $$h_n'=2nh_{n-1}$$。** 对 $$x$$ 求偏导：$$\partial_xG=2t\,e^{2xt-t^2}=2t\,G$$。写成级数：

$$\sum_{n\ge0}\frac{h_n'(x)}{n!}t^n = 2t\sum_{n\ge0}\frac{h_n(x)}{n!}t^n = \sum_{n\ge0}\frac{2h_n(x)}{n!}t^{n+1}.$$

右端令 $$n+1=m$$：$$\sum_{m\ge1}\frac{2h_{m-1}}{(m-1)!}t^m=\sum_{m\ge1}\frac{2m\,h_{m-1}}{m!}t^m$$。比较 $$t^m$$ 的系数：$$h_m'=2m\,h_{m-1}$$。

**三项递推 $$h_{n+1}=2xh_n-2nh_{n-1}$$。** 对 $$t$$ 求偏导：$$\partial_tG=(2x-2t)e^{2xt-t^2}=(2x-2t)G$$。写成级数：

$$\sum_{n\ge1}\frac{h_n}{(n-1)!}t^{n-1} = 2x\sum_{n\ge0}\frac{h_n}{n!}t^n - 2\sum_{n\ge0}\frac{h_n}{n!}t^{n+1}.$$

两端直接比较 $$t^m$$（$$m\ge1$$）的系数：左端给出 $$\frac{h_{m+1}}{m!}$$，右端两项给出 $$2x\,\frac{h_m}{m!}$$ 与 $$-2\,\frac{h_{m-1}}{(m-1)!}$$。两边同乘 $$m!$$：

$$h_{m+1}=2x\,h_m-2m\,h_{m-1},$$

换指标即得 $$h_{n+1}=2xh_n-2n\,h_{n-1}$$。$$\blacksquare$$

**解 竞5.** **关键 leap**：全题只有一步是真的一步——用 $$[N,a]=-ca$$ 把 $$Na$$ 换成 $$aN-ca$$，于是 $$a$$ 就"穿过"本征向量、把本征值改成 $$\lambda-c$$。所谓"梯子"，就是把同一步反复做；"能级等间距"就是这一步的步长与 $$\lambda$$ 无关。

**本题是把入口题 (vi) 抽象化——同时它把"为什么能级等间距"归因到一条代数事实。**

**(i) 升降一步。** 设 $$N\psi=\lambda\psi$$，$$\psi\neq0$$。由 $$[N,a]=-ca$$ 得 $$Na=aN-ca$$，于是

$$N(a\psi) = (Na)\psi = aN\psi - ca\psi = (\lambda-c)\,a\psi .$$

由 $$[N,a^\dagger]=ca^\dagger$$ 得 $$Na^\dagger=a^\dagger N+ca^\dagger$$，于是

$$N(a^\dagger\psi) = (\lambda+c)\,a^\dagger\psi .$$

若 $$a\psi\neq0$$，则它是本征值 $$\lambda-c$$ 的本征向量；若 $$a^\dagger\psi\neq0$$，则它是本征值 $$\lambda+c$$ 的本征向量。

**等间距的来源**：$$c$$ 是常数、不依赖 $$\lambda$$，所以每一步升降改变的本征值**恒为 $$\pm c$$**。于是本征值集合（只要它非空）必形如 $$\lambda_0+c\mathbb Z$$ 的某个子集——**公差是常数，这就是"等间距"的全部内容**。反之，若对易子是 $$[N,a]=-\mu(N)a$$（右端含 $$N$$），步长就会随 $$\lambda$$ 变，能谱不是等差数列。

**(ii) $$c=1$$ 的情形：梯子为什么必须停。** 取 $$c=1$$。由经典题 5.1 与定理 3.9，$$[N,a]=-a$$、$$[N,a^\dagger]=a^\dagger$$，恰是 (i) 的形式。于是所有本征值都在 $$\lambda_0+\mathbb Z$$ 里。

**为什么"梯子必须停"只靠正定性**：梯子可以永远往下降（每一步 $$a$$ 都把本征值减 1），这是纯代数的，不需要任何额外假设；能谱要成为"下半有界的"，就必须有一个下限。$$N=a^\dagger a$$ 的正定性（基2 (ii)）给出 $$\lambda\ge0$$，这就是下限。两条合起来：下降能走 $$\lambda,\lambda-1,\lambda-2,\dots$$，又必须始终 $$\ge0$$，故走到 $$0$$ 就必须停，停住的那一步正是 $$a\psi_0=0$$。

**若 $$N$$ 不正定**：梯子可以无限下降，能谱是 $$\lambda_0+\mathbb Z$$ 的**全体**（双无限），再加上可能的一切平移——能级集是 $$\mathbb R$$ 上没有下界的离散集，物理上没有基态（能量可以负无穷）。这就是为什么物理上要求 $$H$$ 有下界（谱有下确界）。$$\blacksquare$$

**解 研1.** **$$X$$ 无界。** 取一列归一化向量 $$\psi_k$$ 集中在区间 $$[k,k+1]$$ 上（例如把某个固定测试函数平移到该区间并归一）。则

$$\lVert X\psi_k\rVert^2 = \int x^2\lvert\psi_k(x)\rvert^2dx\ \ge\ k^2\int_{k}^{k+1}\lvert\psi_k\rvert^2dx = k^2,$$

故 $$\lVert X\psi_k\rVert\ge k$$。但 $$\lVert\psi_k\rVert=1$$，于是 $$\sup_{\lVert\psi\rVert=1}\lVert X\psi\rVert = \infty$$：$$X$$ 无界。

**$$P$$ 无界。** 用 Fourier 变换后的对偶说法（harmonic-fourier.md 第 4 节）：$$P=-i\hbar\partial_x$$ 在频域变成"乘 $$\hbar\xi$$"，在实域就是"高频成分被放大"。取 $$\psi_k(x)=e^{ikx}\varphi(x)$$（$$\varphi\in C_c^\infty$$ 固定、归一），则

$$P\psi_k = -i\hbar\,\partial_x\bigl(e^{ikx}\varphi\bigr) = \hbar k\,e^{ikx}\varphi - i\hbar e^{ikx}\varphi',$$

$$\lVert P\psi_k\rVert\ \ge\ \hbar k\,\lVert\varphi\rVert - \hbar\lVert\varphi'\rVert = \hbar(k\lVert\varphi\rVert-\lVert\varphi'\rVert)\xrightarrow{k\to\infty}\infty .$$

故 $$\lVert P\rVert=\infty$$。

**$$H,N$$ 无界。** 由定理 3.8，$$H=\hbar\omega(N+\tfrac12I)$$，而 $$N=a^\dagger a$$ 在归一化能级基上有 $$N\psi_n=n\psi_n$$，$$\lVert\psi_n\rVert=1$$，故 $$\lVert N\psi_n\rVert=n\to\infty$$：$$N$$（从而 $$H$$）无界。

**为什么"定义域"这一层躲不掉**：有界算子可以定义在整个 $$\mathscr H$$ 上且连续；无界算子不可能（闭图像定理的推论）。$$X$$ 只能定义在使 $$x\psi(x)\in L^2$$ 的 $$\psi$$ 全体上——这是一个**真稠密子空间**而不是全空间；$$P$$ 只能定义在 $$\psi\in L^2$$ 且 $$\psi$$ 绝对连续、$$\psi'\in L^2$$ 的那些 $$\psi$$ 上。于是"$$H$$ 自伴""$$H$$ 的本征值"这些说法都必须精确到"$$H$$ 的哪个定义域"。本章的全部分配都默认取最大自然定义域 $$\operatorname{Dom}H=\{\psi\in L^2: -\!\frac{\hbar^2}{2m}\psi''+\frac{m\omega^2}{2}x^2\psi\in L^2\}$$，而 Hermite 函数 $$\psi_n$$ 恰在这个定义域里（$$H\psi_n$$ 是 $$L^2$$ 函数），所以本章的计算不受影响。

**这正是第 18 章的起点**：无界算子的谱、自伴与对称的差别、定义域对谱的影响——这些不是技术洁癖，而是 §3.6 里"$$a\psi$$ 可能为零"这类现象的深层原因。$$\blacksquare$$

**解 研2.** 为清晰起见，先在归一化坐标（$$\hbar=m=\omega=1$$）里做；把 $$m,\omega,\hbar$$ 还原是一步尺度变换（定理 3.19）。定义

$$K_+ = \frac{i}{2}P+\frac{1}{2}X,\qquad K_- = \frac{i}{2}P-\frac{1}{2}X .$$

**第一步：算 $$[K_+,K_-]$$。** 逐项展开：

$$[K_+,K_-] = \Bigl[\tfrac{i}{2}P+\tfrac12X,\ \tfrac{i}{2}P-\tfrac12X\Bigr] = \frac{i}{2}\Bigl(-\tfrac12\Bigr)[P,X] + \frac12\cdot\frac{i}{2}[X,P] = -\frac{i}{4}[P,X]+\frac{i}{4}[X,P].$$

由 $$[X,P]=iI$$、$$[P,X]=-iI$$：$$= -\frac{i}{4}(-iI)+\frac{i}{4}(iI) = \frac{i^2}{4}I+\frac{i^2}{4}I = -\frac12I$$。

**第二步：算 $$[H,K_\pm]$$。** 由 $$H=\frac12(P^2+X^2)$$，且 $$[P^2,X]=[P,X]P+P[P,X]=-2iP$$、$$[X^2,P]=[X,P]X+X[X,P]=2iX$$，得

$$[H,K_+] = \Bigl[\tfrac12(P^2+X^2),\ \tfrac{i}{2}P+\tfrac12X\Bigr] = \frac{i}{4}[P^2,P]+\frac14[P^2,X]+\frac{i}{4}[X^2,P]+\frac14[X^2,X]$$

$$= 0 + \frac14(-2iP)+\frac{i}{4}(2iX)+0 = -\frac{i}{2}P-\frac12X = -K_+ .$$

同理 $$[H,K_-] = +K_-$$。

**第三步：这个代数是什么。** 三个算子 $$\{H,K_+,K_-\}$$ 满足

$$[H,K_\pm]=\mp K_\pm\qquad(\text{即 }[H,K_+]=-K_+,\ [H,K_-]=+K_-),\qquad [K_+,K_-]=-\tfrac12 I .$$

这里有一件容易看错的事：$$[K_+,K_-]$$ **落在中心上，而不是落在 $$H$$ 上**。$$\mathfrak{sl}_2$$ 的标准关系是 $$[h,e]=2e$$、$$[h,f]=-2f$$、$$[e,f]=h$$，右端是 Cartan 元 $$h$$；而我们这里右端是中心元 $$-\tfrac12I$$。所以 $$\{H,K_+,K_-,I\}$$ **不是** $$\mathfrak{sl}_2$$，而是**振荡子代数 (oscillator algebra)**（文献里也写作扩张 Heisenberg 代数）：Heisenberg 代数 $$\mathrm{span}\{K_+,K_-,I\}$$（带 $$[K_+,K_-]=-\tfrac12I$$）再加上以 $$H$$ 为导子的扩张。它与 $$\mathfrak{sl}_2$$ 共享的是"权 + 升/降算子"这套**语法**，不是代数本身。

换回原来单位，$$\{K_+,K_-,H\}$$ 与本章的 $$\{a,a^\dagger,N\}$$ 只差常数。在归一化坐标下直接代入定义可得恒等式

$$a=\sqrt2\,K_+,\qquad a^\dagger=-\sqrt2\,K_- .$$

这不是"差一个常数因子"那样的含糊话，而是可以当场验算的：$$[a,a^\dagger]=-2[K_+,K_-]=-2\bigl(-\tfrac12I\bigr)=I$$，正是定义 3.7 里对 $$a,a^\dagger$$ 的要求；而 $$H=N+\tfrac12I$$。于是：

- 本章的"能级梯子"就是关于 $$H$$（即 $$N$$）的**权空间分解**：$$H$$ 的本征值是权，$$K_+\propto a$$ 把权降 $$1$$、$$K_-\propto a^\dagger$$ 把权升 $$1$$——与 竞5 的抽象机制逐字同构，与 $$\mathfrak{sl}_2$$ 的根空间分解也共用同一套语法。
- 那个中心项不是装饰。把 $$N=a^\dagger a$$ 与 $$aa^\dagger=N+I$$ 取平均得 $$H=\frac12\bigl(aa^\dagger+a^\dagger a\bigr)$$，而 $$[K_+,K_-]=-\tfrac12I$$ 右端的 $$\tfrac12$$ 与 $$H$$ 里那个 $$\tfrac12$$ 是同一个数（还原单位后即 $$\tfrac12\hbar\omega$$）——**零点能就是升降算子交换出的中心元**。

**这是同一件事的第一次露面**：第 22 章要证 Stone–von Neumann 定理，那里的主角 Weyl 代数正是 $$\{X,P,I\}$$ 的中心扩张，$$[X,P]=i\hbar I$$ 的那个 $$I$$ 与上面的中心项是同一回事；第 38–39 章在 Lorentz 群的表示论里会再次遇到升降机制——那时 $$K_\pm$$ 的角色由角动量的 $$J_\pm=J_1\pm iJ_2$$ 扮演、$$H$$ 由 $$J_3$$ 扮演，"能级梯子"变成"磁量子数的梯子"。

**最后走回本章的那道裂缝**：以上全是"形式"对易子演算，而 $$K_\pm,H$$ 都是无界算子——$$a,a^\dagger$$ 究竟定义在哪个子空间上、这个代数与它的"表示""谱"该怎么严格定义，都还没有答案。先把这些在有界算子的框架里说清楚，正是第 18 章（有界算子与算子的谱）的起点。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

### 五条核心洞察

**1. Schrödinger 方程的可解性 = 分离变量 + 一次求谱。** 只要 $$H$$ 不含时，含时方程就分解为"定态本征方程 $$H\Psi=E\Psi$$"与"时间相位 $$e^{-iEt/\hbar}$$"两件互不相干的事（定理 3.3）。一般解是本征函数的线性叠加（定理 3.4）。**量子力学的全部计算都在求谱，这句话的出处就是这里。**

**2. 谐振子是一台"不用解微分方程的机器"。** 一次因式分解把二次型 $$H$$ 换成算子的乘积 $$H=\hbar\omega(N+\tfrac12I)$$（定理 3.8），此后全部结果——能谱 $$\hbar\omega(n+\tfrac12)$$、全部本征函数（Gauss 乘 Hermite）、矩阵元 $$\sqrt n$$——都只从三条对易关系流出来。第一次做到了"**用算子代数代替微分方程**"。

**3. 零点能不是技术细节，是代数结构的必然。** $$E_0=\tfrac12\hbar\omega$$ 与"$$a\psi_0=0$$ 且 $$\psi_0\neq0$$"是同一件事（定理 3.14–3.15）。它的根在 $$[a,a^\dagger]=I$$：一个非零的交换子让 $$N=aa^\dagger-I$$ 与 $$aa^\dagger$$ 差 1，基态就落在 $$1/2$$ 而不是 $$0$$。

**4. 能级等间距 = 对易子右端是常数。** 这是入口题 (vi) 与 竞5 的抽象结论。只要 $$[N,a]=-ca$$ 里 $$c$$ 不依赖 $$N$$，梯子就每级等高；$$c=1$$ 与 $$c=2$$ 只是刻度不同。整章所有"漂亮"结果都挂在 $$c$$ 是常数这一条上。

**5. 同一个代数会以不同面貌反复出现。** $$a,a^\dagger,N$$ 满足的 $$[N,a]=-a$$、$$[N,a^\dagger]=a^\dagger$$ 正是 $$\mathfrak{sl}_2$$ 的权空间机制（研2）。这一结构在第 22 章（Weyl 代数与 Stone–von Neumann）与第 38–39 章（Lorentz 群的表示论）会完整回来。

### 下一章的悬念：算子太大了

本章反复用到"$$X$$、$$P$$ 不能同时取零"，也反复用到"$$a\psi$$ 非零"。但 研1 已经算过：$$X,P,H,N$$ **全都不是有界算子**。这不是可以回避的技术细节——它意味着

- $$H$$ 不能定义在整个 $$\mathscr H$$ 上，只能定义在一个真稠密子空间 $$\operatorname{Dom}H$$ 上；
- "对称"（$$\langle\psi\vert H\varphi\rangle=\langle H\psi\vert \varphi\rangle$$）与"自伴"（$$H=H^*$$，含定义域相等）不再是一回事；
- §3.6 里"$$a\psi$$ 可能为零"这件事，与 $$X$$ 无界是同一枚硬币的两面。

本章靠"默认取最大自然定义域"绕过了这些。**第 18 章要做的是把这层缺口正式补上**：有界算子为什么好、无界算子的谱如何定义、对称与自伴的差别会怎样改变物理结论。从那里出发，第 19 章给出谱定理的准确形式，第 21 章处理无界算子的 Cayley 变换，直到第 22 章才把本章的 $$[X,P]=i\hbar I$$ 放在一个自伴的、唯一性可证的对象上（Weyl 代数与 Stone–von Neumann 定理）。

### 延伸阅读

- **Landau & Lifshitz, 《量子力学（非相对论理论）》第 23 节**：谐振子的代数解法的最短版本，本章定理 3.14–3.15 的推导结构与之平行。
- **Feynman, 《物理学讲义》第三卷，第 8–9 章**：用"两个态的耦合"语言讲谐振子的矩阵元，与本章 (5.1) 的三对角矩阵是同一种图像。
- **专家依据 `_experts/analysis/harmonic-fourier.md` 第 4 节**：Gauss 核为什么是不确定性原理的等号情形、为什么是 Fourier 变换的特征函数。本章 4.4 的两条读法都在这一节有完整证明。
- **知识库 `opc2/knowledge/physics/量子力学/landau-qm-modern/ch05_薛定谔方程与时间演化.md` 与 `ch11_全同粒子二次量子化与Fock空间.md`**：前者把本章的分离变量接上一般的时间演化算子；后者把本章的 $$a,a^\dagger$$ 搬到多粒子情形——那里的 $$N$$ 变成"粒子数算子"，$$\sqrt n$$ 变成玻色子的统计因子。
- **顾樵《数学物理方法》中的谐振子分析解**：原文 MP47 推荐的那条被我们绕过的路，作为对照值得走一遍。


---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch16_从Hamilton到量子_可观测量与本征态.md">← 第16章 从 Hamilton 到量子：可观测量与本征态</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch18_有界算子与算子的谱.md">第18章 有界算子与算子的谱 →</a></div>
</div>
