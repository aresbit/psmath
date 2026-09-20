---
layout: default
---

# 第39章: Galois 群与 Galois 对应 (The Galois Group and the Galois Correspondence)

> 对应原专栏: MP149
> 专家依据: `_experts/algebra/group-theory-galois.md`（主）+ `_experts/numbertheory/algebraic-number-theory.md`
> 知识库依据: `opc2/knowledge/math/群论/`、`opc2/knowledge/math/代数数论/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

本章要解决一个核心问题：**怎样把「对称性」变成一台可计算的机器**。

第 38 章我们造出了扩域：给定多项式，可以构造出装下它全部根的域 $$L$$。但那个 $$L$$ 只是一个「装根的口袋」，我们对它的内部结构几乎一无所知。本章给它装上对称性——把 $$L$$ 中所有固定基域 $$K$$ 不动的自同构收集成群 $$\operatorname{Gal}(L/K)$$，然后证明一条惊人的定理：**$$L$$ 与 $$K$$ 之间的一切中间域，与这个群的一切子群一一对应，而且包含关系完全翻转**。这就是 Galois 对应。

有了这台机器，「方程能否用根式求解」这个关于**域**的问题，被完整翻译成「某个有限群是否可解」这个关于**群**的问题。一般五次方程没有根式求根公式，就是这台机器算出来的一句话。

本章是全书域论一侧的终点站。第 40 章从它出发，走向现代数学。这是全书串联得最短的一条线：Galois 出现得最晚，却把前面所有伏笔一次收拢。

## 二、入口：一道具体的问题 (Entry Problem)

**入口题（自编，题面取自 Квант 的「数对称」传统）**

在**不给定义**的前提下，先做五小问。前四问只用第 38 章的扩域概念就能做；第五问要等本章全部机器装配完毕。

**(1)** 设 $$L=\mathbb{Q}(\sqrt2,\sqrt3)$$。把 $$L$$ 到自身、且保持每个有理数不动的域同构（这样的同构叫 $$L$$ 的对称）全部找出来，数一数有几个。

**(2)** 设 $$L=\mathbb{Q}(\sqrt[3]{2})$$。同样的「对称」有几个？

**(3)** 算出 $$[\mathbb{Q}(\sqrt2,\sqrt3):\mathbb{Q}]$$ 与 $$[\mathbb{Q}(\sqrt[3]{2}):\mathbb{Q}]$$，各是多少？

**(4)** 把 (1)(2)(3) 的答案并排看：什么时候「对称的个数」等于「扩张的次数」，什么时候严格小于？两种情形各举一例。**请给出一个判断标准**——如果给不出，先记下这个困惑，它是本章的主定理。

**(5)** 【本章终点】设 $$f(t)=t^5-6t+3\in\mathbb{Q}[t]$$。先证明它不可约、且恰有三个实根（这一步是纯计算，读者现在就能做）。然后回答：**为什么「$$f$$ 不可约 + $$f$$ 恰有三个实根」这两件事，加上本章的机器，就足以证明 $$f$$ 的五个根不可能用加、减、乘、除与开方（不带任何数值迭代）写出来？**

第 (5) 问是本章全部努力的用途。注意它**不是一个「找不到公式」的惊叹**，而是一条**可以写下来、逐步检验的证明**。本章的任务，就是把这条证明搭起来。

## 三、结构：定义与完整推导 (Structure & Proof)

**回顾（第 38 章）** 设 $$L/K$$ 是域扩张，即 $$K$$ 是基域、$$L\supseteq K$$ 是扩域。$$[L:K]$$ 是 $$L$$ 作为 $$K$$-线性空间的维数，称**扩张次数**。若 $$L=K(\alpha_1,\dots,\alpha_m)$$ 且各 $$\alpha_i$$ 都是 $$K$$ 上的代数元，称 $$L/K$$ 为代数扩张，此时每个 $$\alpha_i$$ 有唯一的首一极小多项式。**塔定理**：对 $$K\subseteq E\subseteq L$$ 有 $$[L:K]=[L:E]\cdot[E:K]$$。**本原元定理**：有限可分扩张必是单扩张，即 $$L=K(\gamma)$$ 对某个 $$\gamma$$。下面凡说「自同构」而不加限定，都指 $$L$$ 到自身的域自同构。

### 3.1 对称、群、固定域

**定义 3.1（$$K$$-自同构, $$K$$-automorphism）** 设 $$L/K$$ 是域扩张。$$L$$ 的域自同构 $$\sigma:L\to L$$ 称为 **$$K$$-自同构**，若它固定 $$K$$ 的每个元素，即 $$\sigma(a)=a$$ 对一切 $$a\in K$$ 成立。全体 $$K$$-自同构记作 $$\operatorname{Aut}_K(L)$$。

自同构是「与域运算交换」的可逆映射：$$\sigma(a+b)=\sigma(a)+\sigma(b)$$，$$\sigma(ab)=\sigma(a)\sigma(b)$$，$$\sigma(1)=1$$。它对复合封闭：若 $$\sigma,\tau\in\operatorname{Aut}_K(L)$$，则 $$\sigma\circ\tau$$ 也是 $$K$$-自同构（$$\sigma(\tau(a))=\sigma(a)=a$$ 对 $$a\in K$$）；$$\mathrm{id}$$ 是单位元；$$\sigma^{-1}$$ 也是（因为 $$\sigma$$ 是双射，且 $$a=\sigma(\sigma^{-1}(a))$$ 配合 $$\sigma(a)=a$$ 给出 $$\sigma^{-1}(a)=a$$）。**所以 $$\operatorname{Aut}_K(L)$$ 在复合下自动成群。** 群结构不是外加的，它是「自同构」这个概念自身的产物。

**定义 3.2（Galois 群, Galois group；伽罗瓦群）** 域扩张 $$L/K$$ 的 **Galois 群**是 $$\operatorname{Aut}_K(L)$$，记作 $$\operatorname{Gal}(L/K)$$。（第 38 章与术语表用「伽罗瓦群」，与本章的「Galois 群」是同一个对象。）

**定义 3.3（固定域, fixed field）** 设 $$H\subseteq\operatorname{Aut}(L)$$ 是自同构的子群。$$H$$ 的**固定域**是

$$L^H=\{a\in L:\ \sigma(a)=a\ \text{对一切}\ \sigma\in H\}.$$

$$L^H$$ 是 $$L$$ 的子域：若 $$a,b\in L^H$$ 且 $$\sigma\in H$$，则 $$\sigma(a\pm b)=\sigma(a)\pm\sigma(b)=a\pm b$$，$$\sigma(ab)=\sigma(a)\sigma(b)=ab$$，$$a\ne0$$ 时 $$\sigma(a^{-1})=\sigma(a)^{-1}=a^{-1}$$，且 $$\sigma(1)=1$$，故 $$a\pm b,ab,a^{-1},1\in L^H$$。

两个方向要分清：$$\operatorname{Gal}(L/K)$$ 是**由域造群**（给定扩张，收集它的对称）；$$L^H$$ 是**由群造域**（给定一族对称，问它们共同钉住了谁）。本章的主定理说，在合适的条件下这两个方向互为逆映射。

**例 3.3（入口题 (1) 的答案）** 取 $$L=\mathbb{Q}(\sqrt2,\sqrt3)$$，$$K=\mathbb{Q}$$。由第 38 章，

$$L=\{a+b\sqrt2+c\sqrt3+d\sqrt6:\ a,b,c,d\in\mathbb{Q}\},\qquad [L:\mathbb{Q}]=4,$$

因为 $$\sqrt2,\sqrt3,\sqrt6$$ 在 $$\mathbb{Q}$$ 上线性无关（若 $$(a+b\sqrt2)+(c+d\sqrt2)\sqrt3=0$$，则两个系数都为零，再对 $$\sqrt2\notin\mathbb{Q}$$ 用一次即得 $$a=b=c=d=0$$）。

任何 $$\sigma\in\operatorname{Gal}(L/\mathbb{Q})$$ 由它在生成元上的取值决定：因为 $$\sigma$$ 保持有理数与运算，

$$\sigma\bigl(a+b\sqrt2+c\sqrt3+d\sqrt6\bigr)=a+b\,\sigma(\sqrt2)+c\,\sigma(\sqrt3)+d\,\sigma(\sqrt2)\sigma(\sqrt3).$$

又 $$\sigma(\sqrt2)^2=\sigma(2)=2$$，故 $$\sigma(\sqrt2)$$ 是 $$t^2-2$$ 在域 $$L$$ 中的根，即 $$\sqrt2$$ 或 $$-\sqrt2$$；同理 $$\sigma(\sqrt3)=\pm\sqrt3$$。于是自同构至多有 $$2\times2=4$$ 个，而下面四个都确实可行：

$$\sigma_1=\mathrm{id};\quad \sigma_2:\sqrt2\mapsto\sqrt2,\ \sqrt3\mapsto-\sqrt3;\quad \sigma_3:\sqrt2\mapsto-\sqrt2,\ \sqrt3\mapsto\sqrt3;\quad \sigma_4:\sqrt2\mapsto-\sqrt2,\ \sqrt3\mapsto-\sqrt3.$$

（每个 $$\sigma_i$$ 都是「把 $$\sqrt2\mapsto\pm\sqrt2$$、$$\sqrt3\mapsto\pm\sqrt3$$ 按保持运算的方式延拓到 $$L$$」，这由 $$L$$ 的表达式唯一确定且确有定义，因为它只是把 $$L$$ 的两个生成元送到 $$t^2-2$$、$$t^2-3$$ 的根。）因此

$$\lvert\operatorname{Gal}(L/\mathbb{Q})\rvert=4=[L:\mathbb{Q}],\qquad \operatorname{Gal}(L/\mathbb{Q})\cong\mathbb{Z}/2\times\mathbb{Z}/2,$$

四个元素里除单位元外每个都满足 $$\sigma^2=\mathrm{id}$$——入口题里说它们是「对合」。

**例 3.4（入口题 (2) 的答案：对称会不够）** 取 $$M=\mathbb{Q}(\sqrt[3]{2})$$。由 Eisenstein 判别法（$$p=2$$ 整除除首项外一切系数、且 $$2^2\nmid 2$$），$$t^3-2$$ 在 $$\mathbb{Q}$$ 上不可约，故 $$[M:\mathbb{Q}]=3$$。

设 $$\sigma\in\operatorname{Gal}(M/\mathbb{Q})$$。由 $$\sigma(\sqrt[3]{2})^3=\sigma(2)=2$$，$$\sigma(\sqrt[3]{2})$$ 是 $$t^3-2$$ 在 $$M$$ 中的根。但 $$M\subseteq\mathbb{R}$$，而 $$t^3-2$$ 在 $$\mathbb{R}$$ 中只有唯一的实根 $$\sqrt[3]{2}$$（$$t\mapsto t^3-2$$ 严格递增）。故 $$\sigma(\sqrt[3]{2})=\sqrt[3]{2}$$，从而 $$\sigma=\mathrm{id}$$。于是

$$\lvert\operatorname{Gal}(M/\mathbb{Q})\rvert=1<3=[M:\mathbb{Q}].$$

**两个例子的对比就是入口题 (4)。** 关键差别是：$$t^3-2$$ 的**另外两个根不住在 $$M$$ 里**（它们在 $$\mathbb{C}\setminus\mathbb{R}$$ 中）。$$\lvert\operatorname{Gal}\rvert=[L:K]$$ 不是自动的，它要求「一个根在，则全族根都在」——这正是正规性。

**定义 3.4（可分扩张, separable extension）** 设 $$\alpha$$ 在 $$K$$ 上代数，极小多项式为 $$m\in K[t]$$。若 $$m$$ 在其分裂域中无重根，称 $$\alpha$$ 在 $$K$$ 上**可分**。若代数扩张 $$L/K$$ 的每个元素都可分，称 $$L/K$$ **可分**。

**注 3.4（特征 $$0$$ 的礼物）** 若 $$\operatorname{char}K=0$$，则每个代数元素都可分。理由：设极小多项式 $$m$$ 有重根，则 $$\gcd(m,m')\ne1$$；但 $$m$$ 不可约、$$\deg m\ge1$$，而 $$\operatorname{char}K=0$$ 保证 $$m'\ne0$$ 且 $$\deg m'<\deg m$$，故 $$\gcd(m,m')=1$$，矛盾。因此本章在 $$\mathbb{Q}$$、$$\mathbb{Q}(\zeta_n)$$ 等特征 $$0$$ 域上的一切例子中，**Galois 就等于正规**；可分性只在有限域（定理 3.14）那里需要单独点名。有限域也是完全域 (perfect field)，所以可分性在那里同样自动成立。

**定义 3.5（正规扩张, normal extension）** 代数扩张 $$L/K$$ 称为**正规**，若 $$K[t]$$ 中每个在 $$L$$ 内有根的不可约多项式，在 $$L$$ 内**完全分裂**（所有根都在 $$L$$ 内）。等价地：$$L$$ 是 $$K$$ 上某一族多项式的（最小）分裂域。

**例 3.5（正规性的失败与成功）** $$\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$$ 不正规：$$t^3-2$$ 有根 $$\sqrt[3]{2}$$ 在其中，另两根 $$\sqrt[3]{2}\omega,\sqrt[3]{2}\omega^{2}$$（$$\omega=e^{2\pi i/3}$$）不在其中，因为它们非实而该域 $$\subseteq\mathbb{R}$$。而 $$\mathbb{Q}(\sqrt2)/\mathbb{Q}$$ 正规（$$t^2-2$$ 的两根 $$\pm\sqrt2$$ 都在），$$\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q}$$ 也正规（它是 $$(t^2-2)(t^2-3)$$ 的分裂域）。

**定义 3.6（Galois 扩张, Galois extension）** 有限扩张 $$L/K$$ 称为 **Galois 扩张**，若它**既可分又正规**。

### 3.2 两条引理：把「对称的个数」钉死

要证明 $$\lvert\operatorname{Gal}(L/K)\rvert=[L:K]$$，需要两个纯线性的引理。它们都不涉及域的特殊结构，只用到「自同构是线性无关的函数」。

**引理 3.7（Dedekind 引理：自同构线性无关）** 设 $$\sigma_1,\dots,\sigma_n:L\to L$$ 是两两不同的域自同构，$$c_1,\dots,c_n\in L$$。若 $$\sum_{i=1}^{n}c_i\sigma_i(x)=0$$ 对一切 $$x\in L$$ 成立，则 $$c_1=\cdots=c_n=0$$。

**证明（思路：极小反例 + 用乘法把项数减少）** 反设存在非平凡关系，取项数最少的一组，即 $$\sum_{i=1}^{n}c_i\sigma_i=0$$ 且 $$n$$ 最小、每个 $$c_i\ne0$$。把等式整体乘 $$c_1^{-1}$$，可设 $$c_1=1$$。

因 $$\sigma_1\ne\sigma_2$$，存在 $$x_0\in L$$ 使 $$\sigma_1(x_0)\ne\sigma_2(x_0)$$（若对所有 $$x$$ 都有 $$\sigma_1(x)=\sigma_2(x)$$，则两个映射相同）。任取 $$y\in L$$，先用 $$x=x_0y$$ 代入原式：

$$\sigma_1(x_0)\sigma_1(y)+\sum_{i=2}^{n}c_i\sigma_i(x_0)\sigma_i(y)=0.$$

再把原式（$$x=y$$）乘 $$\sigma_1(x_0)$$：

$$\sigma_1(x_0)\sigma_1(y)+\sum_{i=2}^{n}c_i\sigma_1(x_0)\sigma_i(y)=0.$$

两式相减，第一项消去：

$$\sum_{i=2}^{n}c_i\bigl(\sigma_i(x_0)-\sigma_1(x_0)\bigr)\sigma_i(y)=0\quad\text{对一切}\ y\in L.$$

这是项数 $$n-1$$ 的关系，且第 2 项的系数 $$c_2(\sigma_2(x_0)-\sigma_1(x_0))\ne0$$（$$c_2\ne0$$，且括号非零），与 $$n$$ 的最小性矛盾。故不存在非平凡关系。$$\blacksquare$$

**引理 3.7 的用法**：它把「$$\sigma$$ 们的取值」变成了一组线性无关的坐标，从而能对它们做线性代数。下面这条引理是本章的引擎。

**定理 3.8（Artin 引理）** 设 $$H\subseteq\operatorname{Aut}(L)$$ 是**有限**自同构群，则 $$[L:L^H]\le\lvert H\rvert$$。

**证明** 记 $$\lvert H\rvert=n$$，设 $$[L:L^H]=r$$，取 $$L$$ 作为 $$L^H$$-线性空间的一组基 $$x_1,\dots,x_r$$。反设 $$r>n$$。对每个 $$\sigma\in H$$ 写下一个线性方程（未知量 $$a_1,\dots,a_r\in L$$）：

$$\sum_{j=1}^{r}a_j\,\sigma(x_j)=0,\qquad \sigma\in H.$$

这是 $$n$$ 个方程、$$r$$ 个未知量的齐次线性方程组（系数在域 $$L$$ 中）。因 $$r>n$$，它有非零解。在所有非零解中取一个**非零分量个数最少**的 $$\mathbf{a}=(a_1,\dots,a_r)$$，重排下标使 $$a_1\ne0$$，并把整个解乘 $$a_1^{-1}$$，于是 $$a_1=1$$。

**第一步：每个 $$a_j$$ 都被 $$H$$ 固定。** 任取 $$\tau\in H$$。把 $$\tau$$ 作用到上面的方程组上：由 $$\sum_j a_j\sigma(x_j)=0$$ 得 $$\sum_j\tau(a_j)\,\tau\sigma(x_j)=0$$。当 $$\sigma$$ 跑遍 $$H$$ 时 $$\tau\sigma$$ 也跑遍 $$H$$（$$H$$ 是群），所以 $$\mathbf{a}':=(\tau(a_1),\dots,\tau(a_r))$$ 也是方程组的解。于是差 $$\mathbf{a}-\mathbf{a}'$$ 也是解，且它的第一个分量是 $$a_1-\tau(a_1)=1-1=0$$，非零分量个数严格少于 $$\mathbf{a}$$。由最小性，$$\mathbf{a}-\mathbf{a}'=\mathbf{0}$$，即 $$\tau(a_j)=a_j$$ 对一切 $$j$$。因 $$\tau\in H$$ 任意，$$a_j\in L^H$$ 对一切 $$j$$。

**第二步：导出矛盾。** 现在 $$a_j\in L^H$$，取 $$\sigma=\mathrm{id}\in H$$ 对应的那个方程，得 $$\sum_j a_j x_j=0$$。但 $$a_1=1\ne0$$，这与 $$x_1,\dots,x_r$$ 是 $$L^H$$-基（因而 $$L^H$$-线性无关）矛盾。故 $$r\le n$$，即 $$[L:L^H]\le\lvert H\rvert$$。$$\blacksquare$$

### 3.3 Galois 扩张的等价刻画

**定理 3.9（Galois 扩张的等价刻画）** 设 $$L/K$$ 是**有限**扩张，$$G=\operatorname{Gal}(L/K)$$。则下列四条等价：

1. $$L/K$$ 是 Galois 扩张（可分 + 正规）；
2. $$L$$ 是 $$K$$ 上某个**可分**多项式的分裂域；
3. $$\lvert G\rvert=[L:K]$$；
4. $$K=L^{G}$$（基域恰是全体 $$K$$-自同构的固定域）。

**证明（思路）** 一般地只有 $$\lvert G\rvert\le[L:K]$$，取等就是 Galois——所以 (3) 是最常用的判定。四条之间的路线是 $$1\Rightarrow2\Rightarrow3\Rightarrow4\Rightarrow1$$。

**$$1\Rightarrow2$$：** 由本原元定理（第 38 章），有限可分扩张是单扩张，$$L=K(\gamma)$$。正规性说：$$\gamma$$ 的极小多项式 $$m$$（不可约、有根 $$\gamma\in L$$）在 $$L$$ 内完全分裂。故 $$L$$ 是 $$m$$ 的分裂域；可分性给出 $$m$$ 无重根。∎

**$$2\Rightarrow3$$：** 设 $$L$$ 是可分多项式 $$f\in K[t]$$ 的分裂域，$$\alpha_1,\dots,\alpha_m$$ 为其全部互异根，$$L=K(\alpha_1,\dots,\alpha_m)$$。核心事实是：**任取 $$K$$-嵌入 $$\phi:L\hookrightarrow\bar K$$（$$\bar K$$ 为 $$K$$ 的代数闭包），$$\phi(L)\subseteq L$$**。理由：$$\phi$$ 把每个 $$\alpha_i$$ 送到 $$f$$ 的某个根（$$\phi$$ 固定 $$K$$ 的系数，故 $$f(\phi(\alpha_i))=\phi(f(\alpha_i))=0$$），而 $$f$$ 的根全在 $$L$$ 内，故 $$\phi$$ 把生成元集 $$\{\alpha_1,\dots,\alpha_m\}$$ 映入 $$L$$，从而 $$\phi(L)\subseteq L$$；又 $$\phi$$ 是单射、$$[L:K]$$ 有限，故 $$\phi(L)=L$$。

于是 $$\operatorname{Hom}_K(L,\bar K)=\operatorname{Aut}_K(L)=G$$，只需数嵌入。数法：把 $$L/K$$ 拆成一串单扩张 $$K=K_0\subseteq K_1\subseteq\cdots\subseteq K_m=L$$，由可分性，每个 $$K$$-嵌入 $$K_i\hookrightarrow\bar K$$ 延拓到 $$K_{i+1}$$ 的方式数恰为 $$[K_{i+1}:K_i]$$（把新生成元送到其极小多项式的根，根互异故一个个数）；连乘由塔定理得 $$\lvert\operatorname{Hom}_K(L,\bar K)\rvert=[L:K]$$，故 $$\lvert G\rvert=[L:K]$$。∎

**$$3\Rightarrow4$$：** 令 $$H=G$$，$$K\subseteq L^G\subseteq L$$。对扩张 $$L/L^G$$ 用 Artin 引理（定理 3.8）：$$[L:L^G]\le\lvert G\rvert=[L:K]$$。另一方面由塔定理 $$[L:K]=[L:L^G]\cdot[L^G:K]$$，而 $$[L^G:K]\ge1$$，故 $$[L:L^G]\ge[L:K]$$（有限扩张的次数为整数且 $$\ge1$$）。两边夹出 $$[L:L^G]=[L:K]$$，于是 $$[L^G:K]=1$$，即 $$L^G=K$$。∎

**$$4\Rightarrow1$$：** 设 $$K=L^{G}$$。对 $$L/K$$ 用 Artin 引理得 $$[L:K]=[L:L^G]\le\lvert G\rvert$$；又由注 3.10 给出的一般上界 $$\lvert G\rvert\le[L:K]$$。两边夹得 $$\lvert G\rvert=[L:K]$$，即条件 (3) 成立。

再证正规与可分。任取 $$\alpha\in L$$，它的轨道是有限集，把其中元素两两不同地写成

$$\beta_1=\alpha,\ \beta_2,\ \dots,\ \beta_r,\qquad \{\beta_1,\dots,\beta_r\}=\{\sigma(\alpha):\sigma\in G\},$$

并令

$$g(t)=\prod_{i=1}^{r}(t-\beta_i)\in L[t].$$

任取 $$\tau\in G$$。因 $$\tau(\beta_i)=(\tau\sigma)(\alpha)$$ 仍在轨道内、且 $$\beta_i$$ 两两不同，$$\tau$$ 只是置换 $$g$$ 的因子；于是 $$g$$ 的每个系数都被 $$\tau$$ 固定。由 $$\tau\in G$$ 任意，系数属于 $$L^G=K$$，即 $$g\in K[t]$$ 且 $$g(\alpha)=0$$。

设 $$m\in K[t]$$ 为 $$\alpha$$ 的极小多项式，则 $$m\mid g$$（因 $$g\in K[t]$$ 以 $$\alpha$$ 为根、$$m$$ 极小）。于是 $$m$$ 的每个根都是某个 $$\beta_i$$，而 $$\beta_i\in L$$——这给出**正规性**。又 $$g$$ 的根 $$\beta_i$$ 两两不同，故 $$g$$ 无重根，作为其因子的 $$m$$ 也无重根——这给出**可分性**。∎

**注 3.9（根的可迁性是其推论）** 由上面同一套计数可得一条常用事实：$$G$$ 在 $$f$$ 的根集上**传递 (transitively)** 地作用，且 $$\deg f\mid\lvert G\rvert$$。理由：轨道-稳定子定理给出 $$\lvert G\cdot\alpha_i\rvert=[G:\operatorname{Stab}(\alpha_i)]$$；而 $$\operatorname{Stab}(\alpha_i)=\operatorname{Gal}(L/K(\alpha_i))$$（固定 $$\alpha_i$$ 等价于固定 $$K(\alpha_i)$$），其大小为 $$[L:K(\alpha_i)]$$，因 $$L/K(\alpha_i)$$ 仍是 Galois 扩张（定理 3.11 (i) 的论证）。于是

$$\lvert G\cdot\alpha_i\rvert=\frac{[L:K]}{[L:K(\alpha_i)]}=[K(\alpha_i):K]=\deg m_{\alpha_i},$$

而极小多项式的全部根恰是这条轨道，故作用传递；再对 $$\alpha_i$$ 是 $$f$$ 任一根的情形取 $$m_{\alpha_i}\mid f$$，得 $$\deg f\mid\lvert G\rvert$$。这条事实正是后面「$$G$$ 嵌入 $$S_n$$」（定理 3.13）的来源。

**注 3.10（一般的上界）** 对**任意**有限扩张 $$L/K$$ 都有 $$\lvert\operatorname{Gal}(L/K)\rvert\le[L:K]$$，且等号成立 $$\iff L^{\operatorname{Gal}(L/K)}=K$$。证明：设 $$H=\operatorname{Gal}(L/K)$$。取 $$L$$ 作为 $$K$$-线性空间的一组基 $$x_1,\dots,x_r$$，$$r=[L:K]$$。把引理 3.7 的证明逐字搬来（把那里的 $$L$$ 换成 $$K$$、把「$$H$$ 的固定域」换成 $$K$$）：若 $$\lvert H\rvert>r$$，则齐次方程组 $$\sum_j a_j\sigma(x_j)=0\ (\sigma\in H)$$ 有非零解，取非零分量最少者并归一化 $$a_1=1$$；由「解集在 $$H$$ 作用下封闭」推出全部 $$a_j\in K$$，代入 $$\sigma=\mathrm{id}$$ 得 $$\sum_j a_jx_j=0$$，与基的线性无关矛盾。故 $$\lvert H\rvert\le r=[L:K]$$。

再由 Artin 引理，$$[L:L^H]\le\lvert H\rvert\le[L:K]$$，而 $$[L:K]=[L:L^H]\cdot[L^H:K]$$，故 $$[L^H:K]\le1$$，即 $$K=L^H$$ 时取等。

### 3.4 主定理：Galois 对应

**定理 3.11（Galois 基本定理 / Galois 对应, Galois correspondence）** 设 $$L/K$$ 是有限 Galois 扩张，$$G=\operatorname{Gal}(L/K)$$。记

$$\mathcal{F}=\{E: K\subseteq E\subseteq L\}\ (\text{中间域}),\qquad \mathcal{S}=\{H: H\le G\}\ (\text{子群}).$$

则映射

$$\Phi:\mathcal{F}\to\mathcal{S},\quad E\mapsto\operatorname{Gal}(L/E);\qquad \Psi:\mathcal{S}\to\mathcal{F},\quad H\mapsto L^H$$

互为逆映射（因而都是双射），并且满足四条结构性质：

1. **序反 (order-reversing)**：$$E_1\subseteq E_2\iff \operatorname{Gal}(L/E_1)\supseteq\operatorname{Gal}(L/E_2)$$；
2. **次数 / 指标换算**：$$[L:E]=\lvert\operatorname{Gal}(L/E)\rvert$$，且 $$[E:K]=[G:\operatorname{Gal}(L/E)]$$；
3. **共轭对应**：对 $$\sigma\in G$$，$$\sigma(E)$$ 对应 $$\sigma\operatorname{Gal}(L/E)\sigma^{-1}$$；
4. **正规性对应**：$$E/K$$ 是 Galois 扩张 $$\iff \operatorname{Gal}(L/E)\trianglelefteq G$$；此时

$$\operatorname{Gal}(E/K)\cong\frac{G}{\operatorname{Gal}(L/E)}.$$

**证明** 分五步。

**（i）$$\Psi\circ\Phi=\mathrm{id}$$。** 任取中间域 $$E$$。要证 $$L^{\operatorname{Gal}(L/E)}=E$$。关键观察：**$$L/E$$ 也是 Galois 扩张**。可分性由定义继承：$$L$$ 中元素 $$\alpha$$ 在 $$K$$ 上的极小多项式无重根，而它在 $$E$$ 上的极小多项式整除前者，故也无重根。正规性：若不可约 $$f\in E[t]$$ 在 $$L$$ 中有根 $$\alpha$$，则 $$\alpha$$ 在 $$K$$ 上的极小多项式在 $$L$$ 中分裂（$$L/K$$ 正规），而 $$f$$ 整除该多项式，故 $$f$$ 的根也都在 $$L$$ 中。于是对扩张 $$L/E$$ 使用定理 3.9 的条件 (4)（那里已证 $$\lvert\operatorname{Gal}(L/E)\rvert=[L:E]$$），得 $$E=L^{\operatorname{Gal}(L/E)}$$。

**（ii）$$\Phi\circ\Psi=\mathrm{id}$$。** 任取子群 $$H\le G$$。由固定域的定义，$$H\subseteq\operatorname{Gal}(L/L^H)$$（$$H$$ 的每个元素都固定 $$L^H$$ 的元素，从而是 $$L^H$$-自同构）。由 (i) 的论证，$$L/L^H$$ 也是 Galois 扩张，故 $$\lvert\operatorname{Gal}(L/L^H)\rvert=[L:L^H]$$（定理 3.9）。另一方面 Artin 引理给 $$[L:L^H]\le\lvert H\rvert$$。合并：

$$\lvert\operatorname{Gal}(L/L^H)\rvert=[L:L^H]\le\lvert H\rvert\le\lvert\operatorname{Gal}(L/L^H)\rvert.$$

中间的 $$\lvert H\rvert\le\lvert\operatorname{Gal}(L/L^H)\rvert$$ 由包含关系 $$H\subseteq\operatorname{Gal}(L/L^H)$$ 给出。故处处取等，$$H=\operatorname{Gal}(L/L^H)$$。

**（iii）序反。** 若 $$E_1\subseteq E_2$$，则固定 $$E_2$$ 的自同构必固定 $$E_1$$，故 $$\operatorname{Gal}(L/E_2)\subseteq\operatorname{Gal}(L/E_1)$$。反过来，若 $$H_2\subseteq H_1$$，则被 $$H_1$$ 固定的元素必被 $$H_2$$ 固定，故 $$L^{H_1}\subseteq L^{H_2}$$。因 $$\Phi,\Psi$$ 互逆，这两个方向合起来给出「$$\iff$$」。

**（iv）次数与指标。** $$[L:E]=\lvert\operatorname{Gal}(L/E)\rvert$$ 就是 (i) 中已用的 $$\lvert\operatorname{Gal}(L/E)\rvert=[L:E]$$。再算指数：由塔定理与定理 3.9，

$$[L:K]=\lvert G\rvert,\qquad [L:K]=[L:E]\cdot[E:K]=\lvert\operatorname{Gal}(L/E)\rvert\cdot[E:K].$$

而由 Lagrange 定理 $$\lvert G\rvert=\lvert\operatorname{Gal}(L/E)\rvert\cdot[G:\operatorname{Gal}(L/E)]$$。两式相除得 $$[E:K]=[G:\operatorname{Gal}(L/E)]$$。

**（v）共轭对应。** 固定 $$\sigma\in G$$，记 $$H=\operatorname{Gal}(L/E)$$。先算 $$\operatorname{Gal}(L/\sigma(E))$$。$$\tau\in G$$ 固定 $$\sigma(E)$$，即对一切 $$a\in E$$ 有 $$\tau(\sigma(a))=\sigma(a)$$，等价于 $$\sigma^{-1}\tau\sigma(a)=a$$ 对一切 $$a\in E$$，即 $$\sigma^{-1}\tau\sigma\in H$$，即 $$\tau\in\sigma H\sigma^{-1}$$。故

$$\operatorname{Gal}\bigl(L/\sigma(E)\bigr)=\sigma\operatorname{Gal}(L/E)\sigma^{-1}.$$

特别地，$$E/K$$ 正规（即 $$\sigma(E)=E$$ 对一切 $$\sigma\in G$$）等价于 $$H=\sigma H\sigma^{-1}$$ 对一切 $$\sigma$$，即 $$H\trianglelefteq G$$——这就是性质 4 的一半。

**（vi）性质 4 的商群部分。** 设 $$H=\operatorname{Gal}(L/E)\trianglelefteq G$$。定义限制映射

$$\rho:G\to\operatorname{Gal}(E/K),\qquad \rho(\sigma)=\sigma\vert_E.$$

它确实落在 $$\operatorname{Gal}(E/K)$$：$$\sigma$$ 固定 $$K$$（因 $$\sigma\in G$$），且由 $$H\trianglelefteq G$$ 与 (v)，$$\sigma(E)=E$$，故 $$\sigma\vert_E$$ 是 $$E$$ 的自同构。核为 $$\{\sigma:\sigma\vert_E=\mathrm{id}\}=H$$。由第一同构定理，$$G/H\cong\operatorname{im}\rho\subseteq\operatorname{Gal}(E/K)$$。又

$$\lvert\operatorname{im}\rho\rvert=[G:H]=[E:K]=\lvert\operatorname{Gal}(E/K)\rvert$$

（中间一步用了 (iv)，最后一步用了 $$E/K$$ 是 Galois 扩张——它在 $$H\trianglelefteq G$$ 时成立，见下面的注）。故 $$\rho$$ 满射，$$\operatorname{Gal}(E/K)\cong G/H$$。$$\blacksquare$$

**注 3.11（这条对应为什么叫「基本定理」）** 定理 3.11 说：**域的子结构（中间域）与群的子结构（子群）是同一件事的两种写法**，而且「大域对小群」；「中间域本身是否 Galois」完全等价于「对应子群是否正规」；「扩域的次数」就是「群的指数」。于是任何关于中间域的命题，都可以翻译成关于子群的命题，反之亦然。这就是把「方程」翻译成「群」的字典。

**例 3.11（把字典查一遍：$$\mathbb{Q}(\sqrt2,\sqrt3)$$）** 取 $$L=\mathbb{Q}(\sqrt2,\sqrt3)$$，$$G=\{1,\sigma_2,\sigma_3,\sigma_4\}\cong(\mathbb{Z}/2)^2$$（例 3.3）。由定理 3.9 的 (3)，$$\lvert G\rvert=4=[L:\mathbb{Q}]$$，故 $$L/\mathbb{Q}$$ 是 Galois 扩张，字典可用。

$$\mathbb{Z}/2\times\mathbb{Z}/2$$ 的子群恰有五个：$$\{1\}$$、$$\langle\sigma_2\rangle$$、$$\langle\sigma_3\rangle$$、$$\langle\sigma_4\rangle$$、$$G$$。于是中间域也恰有五个，且对应如下（大域对小群）：

| 子群 $$H$$ | 固定域 $$L^H$$ | $$[L^H:\mathbb{Q}]$$ |
|---|---|---|
| $$G$$ | $$\mathbb{Q}$$ | $$1$$ |
| $$\langle\sigma_2\rangle$$ | $$\mathbb{Q}(\sqrt2)$$ | $$2$$ |
| $$\langle\sigma_3\rangle$$ | $$\mathbb{Q}(\sqrt3)$$ | $$2$$ |
| $$\langle\sigma_4\rangle$$ | $$\mathbb{Q}(\sqrt6)$$ | $$2$$ |
| $$\{1\}$$ | $$L$$ | $$4$$ |

验证一行：$$\sigma_2$$ 固定 $$\sqrt2$$、把 $$\sqrt3\mapsto-\sqrt3$$，故它固定 $$\mathbb{Q}(\sqrt2)$$；反过来若 $$a+b\sqrt2+c\sqrt3+d\sqrt6$$ 被 $$\sigma_2$$ 固定，则 $$c=d=0$$（因为 $$\sigma_2$$ 把它变成 $$a+b\sqrt2-c\sqrt3-d\sqrt6$$，相等迫使 $$c=d=0$$），故固定域恰是 $$\mathbb{Q}(\sqrt2)$$。其余三行同理。**这张表就是入口题 (1)(3) 的完整答案**：$$\lvert G\rvert=4=[L:\mathbb{Q}]$$（例 3.3），且每个中间域都来自一个子群。

### 3.5 Galois 群的格结构（MP149 的组合定理）

**定理 3.12（Galois 群与域的合成）** 设 $$K$$ 有两种 Galois 扩张 $$(L_1,G_1)$$、$$(L_2,G_2)$$，其中 $$G_i=\operatorname{Gal}(L_i/K)$$，并设 $$L_1,L_2$$ 落在同一个代数闭包中。记 $$L_1L_2$$ 为包含两者的最小子域（合成域，compositum）。则限制映射诱导**单射**

$$\operatorname{Gal}(L_1L_2/K)\hookrightarrow G_1\times G_2,\qquad \sigma\mapsto(\sigma\vert_{L_1},\sigma\vert_{L_2}),$$

且当 $$L_1\cap L_2=K$$ 时它是同构：

$$\operatorname{Gal}(L_1L_2/K)\cong G_1\times G_2.$$

归纳得：对 $$n$$ 个两两「交为 $$K$$」的 Galois 扩张，有

$$\operatorname{Gal}(L_1\cdots L_n/K)\cong\prod_{i=1}^{n}G_i.$$

**证明（思路与关键步骤）** 记 $$\rho:\sigma\mapsto(\sigma\vert_{L_1},\sigma\vert_{L_2})$$。

**（a）$$\rho$$ 有定义。** $$L_1$$ 是某可分多项式 $$f_1$$ 的分裂域，而 $$\sigma$$ 把 $$f_1$$ 的根送到根，故 $$\sigma(L_1)\subseteq L_1$$；又 $$\sigma$$ 是单射、$$[L_1:K]$$ 有限，故 $$\sigma(L_1)=L_1$$，即 $$\sigma\vert_{L_1}\in\operatorname{Aut}_K(L_1)=G_1$$。对 $$L_2$$ 同理。

**（b）$$\rho$$ 是单射。** 若 $$\rho(\sigma)=(\mathrm{id},\mathrm{id})$$，则 $$\sigma$$ 固定 $$L_1$$ 与 $$L_2$$，从而固定它们生成的 $$L_1L_2$$，即 $$\sigma=\mathrm{id}$$。

**（c）$$L_1\cap L_2=K$$ 时 $$\rho$$ 满射。** 此时 $$[L_1L_2:K]=[L_1:K]\cdot[L_2:K]$$：$$L_1L_2$$ 是 $$L_2$$ 上多项式 $$f_1$$ 的分裂域，而 $$L_1\cap L_2=K$$ 配合正规性保证 $$f_1$$ 的不可约因子搬到 $$L_2$$ 上后不继续分裂、次数不变，故 $$[L_1L_2:L_2]=[L_1:K]$$。再由定理 3.11 (iv)，

$$[L_1L_2:K]=[L_1:K]\cdot[L_2:K]=\lvert G_1\rvert\cdot\lvert G_2\rvert=\lvert G_1\times G_2\rvert.$$

结合 (b) 的单射，$$\rho$$ 是阶数相等的单射，故为同构。$$\blacksquare$$

**例 3.12（入口题 (1) 的第二次验证）** 取 $$L_1=\mathbb{Q}(\sqrt2)$$、$$L_2=\mathbb{Q}(\sqrt3)$$。两者都是 $$\mathbb{Q}$$ 的二次 Galois 扩张（$$t^2-2$$、$$t^2-3$$ 各自分裂、特征 $$0$$ 可分），$$G_1\cong G_2\cong\mathbb{Z}/2$$。又

$$\mathbb{Q}(\sqrt2)\cap\mathbb{Q}(\sqrt3)=\mathbb{Q},$$

理由：交域次数同时整除 $$2$$ 与 $$2$$，故 $$\in\{1,2\}$$；若为 $$2$$ 则 $$\sqrt3\in\mathbb{Q}(\sqrt2)$$，写成 $$\sqrt3=a+b\sqrt2$$ 后平方得 $$3=a^2+2b^2+2ab\sqrt2$$，故 $$ab=0$$，两种取值都立刻矛盾。故交为 $$\mathbb{Q}$$，定理 3.12 给出

$$\operatorname{Gal}(\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q})\cong\mathbb{Z}/2\times\mathbb{Z}/2,$$

与例 3.3 的逐个计算一致。**推广**：对两两不同的素数 $$p_1,\dots,p_n$$（的平方根），

$$\operatorname{Gal}\bigl(\mathbb{Q}(\sqrt{p_1},\dots,\sqrt{p_n})/\mathbb{Q}\bigr)\cong(\mathbb{Z}/2)^n,$$

且每个非平凡子群都对应一个由部分 $$\sqrt{p_i}$$ 生成的中间域——这正是 MP149 里那条「互不相等的素数的平方根给出 $$(\mathbb{Z}/2)^n$$」的结论，现在它是定理 3.12 的直接推论。

### 3.6 判别式：Galois 群嵌进 $$A_n$$ 的判据

**定理 3.13（判别式与 $$A_n$$）** 设 $$f\in K[t]$$ 可分，$$\deg f=n$$，根为 $$\alpha_1,\dots,\alpha_n$$，$$L=K(\alpha_1,\dots,\alpha_n)$$ 为其分裂域，$$G=\operatorname{Gal}(L/K)\hookrightarrow S_n$$（$$G$$ 作用在 $$n$$ 个根上）。定义**判别式 (discriminant)**

$$\Delta=\prod_{1\le i<j\le n}(\alpha_i-\alpha_j)^2\in L.$$

则 $$\Delta\in K$$；且

$$G\subseteq A_n\iff \sqrt{\Delta}:=\prod_{i<j}(\alpha_i-\alpha_j)\in K\iff \Delta\ \text{在}\ K\ \text{中是平方}.$$

**证明** **（a）$$\Delta\in K$$：** 置换 $$\alpha_i$$ 只是重排乘积中的因子，故每个 $$\sigma\in G$$ 固定 $$\Delta$$，于是 $$\Delta\in L^G=K$$（定理 3.9 的 (4)）。

**（b）$$\sqrt\Delta$$ 的符号：** 记 $$\delta=\prod_{i<j}(\alpha_i-\alpha_j)$$。偶置换保持 $$\delta$$，奇置换把 $$\delta$$ 变成 $$-\delta$$（因为每个对换 $$(i\,j)$$ 恰好翻转一个因子的符号，其余因子配对改变：$$\prod_{m}(\alpha_i-\alpha_m)(\alpha_j-\alpha_m)$$ 在交换 $$\alpha_i\leftrightarrow\alpha_j$$ 时整体变号）。于是对 $$\sigma\in G$$，

$$\sigma(\delta)=\operatorname{sgn}(\sigma)\cdot\delta.$$

**（c）等价性：** 若 $$G\subseteq A_n$$，则所有 $$\sigma$$ 都是偶置换，$$\sigma(\delta)=\delta$$，故 $$\delta\in L^G=K$$。反之若 $$\delta\in K$$，则对一切 $$\sigma\in G$$ 有 $$\sigma(\delta)=\delta$$，代入 (b) 得 $$\operatorname{sgn}(\sigma)=1$$（因 $$\delta\ne0$$，$$f$$ 可分），即 $$\sigma\in A_n$$。于是 $$G\subseteq A_n\iff\delta\in K\iff\delta^2=\Delta$$ 是 $$K$$ 中的平方。$$\blacksquare$$

**例 3.13（三次多项式的判别式）** $$f=t^3+pt+q$$ 的判别式为 $$\Delta=-4p^3-27q^2$$（可直接代入定义展开，或对 $$f=t^3-3t+1$$ 先算）。对 $$f=t^3-2$$（$$p=0,q=-2$$）得 $$\Delta=-108$$，不是 $$\mathbb{Q}$$ 中的平方，故其 Galois 群含奇置换，即 $$G=S_3$$（而不是 $$A_3$$）。对 $$f=t^3-3t+1$$（$$p=-3,q=1$$）得 $$\Delta=81=9^2$$，是平方，故 $$G\subseteq A_3$$，于是 $$G\cong\mathbb{Z}/3$$。这两个小例子在题 2 与题 4 里会用到。

### 3.7 两个结构性例子：有限域与单位根

**定理 3.14（有限域：Frobenius 生成一切）** 设 $$p$$ 为素数，$$q=p^n$$，$$\mathbb{F}_q$$ 为 $$q$$ 元域（第 38 章：对每个 $$q=p^n$$ 存在唯一 $$\mathbb{F}_q$$，它是 $$t^{q}-t$$ 的分裂域）。则 $$\mathbb{F}_q/\mathbb{F}_p$$ 是 Galois 扩张，且由 **Frobenius 自同构**

$$\varphi:\mathbb{F}_q\to\mathbb{F}_q,\qquad \varphi(x)=x^{p}$$

生成的循环群给出

$$\operatorname{Gal}(\mathbb{F}_q/\mathbb{F}_p)=\langle\varphi\rangle\cong\mathbb{Z}/n,\qquad \lvert\operatorname{Gal}(\mathbb{F}_q/\mathbb{F}_p)\rvert=n=[\mathbb{F}_q:\mathbb{F}_p].$$

等价地，$$\operatorname{Gal}(\mathbb{F}_{p^m}/\mathbb{F}_{p^n})\cong\mathbb{Z}/(m/n)$$（当 $$n\mid m$$），且 $$\mathbb{F}_{p^n}\subseteq\mathbb{F}_{p^m}\iff n\mid m$$。

**证明** **（a）$$\varphi$$ 是自同构：** 在特征 $$p$$ 下 $$(x+y)^p=x^p+y^p$$（二项式系数 $$\binom{p}{k}$$ 被 $$p$$ 整除，中间项全消失），$$(xy)^p=x^py^p$$，且 $$x^p=0\Rightarrow x=0$$，故 $$\varphi$$ 是单射；$$\mathbb{F}_q$$ 有限，单射即双射。又 $$\varphi(a)=a^p=a$$ 对 $$a\in\mathbb{F}_p$$（Fermat 小定理），故 $$\varphi\in\operatorname{Gal}(\mathbb{F}_q/\mathbb{F}_p)$$。

**（b）阶为 $$n$$：** $$\varphi^n(x)=x^{p^n}=x$$ 对一切 $$x\in\mathbb{F}_q$$（因 $$x^{q}=x$$），故 $$\varphi^n=\mathrm{id}$$；而若 $$\varphi^k=\mathrm{id}$$，则 $$x^{p^k}=x$$ 对一切 $$x\in\mathbb{F}_q$$，即 $$t^{p^k}-t$$ 在 $$\mathbb{F}_q$$ 中有 $$q=p^n$$ 个根，但它的次数是 $$p^k$$，故 $$p^k\ge p^n$$，$$k\ge n$$。所以 $$\varphi$$ 的阶恰为 $$n$$。

**（c）群的大小：** 由塔定理 $$[\mathbb{F}_q:\mathbb{F}_p]=n$$；由定理 3.9 的 (3) 得 $$\lvert\operatorname{Gal}\rvert=n$$，而 $$\langle\varphi\rangle$$ 已是 $$n$$ 阶子群，故二者相等。

**（d）子域对应：** 由定理 3.11，子域 $$\leftrightarrow$$ $$\mathbb{Z}/n$$ 的子群；$$\mathbb{Z}/n$$ 的子群与 $$n$$ 的正因子（每个 $$d\mid n$$ 唯一对应一个 $$\mathbb{Z}/(n/d)$$ 阶子群）一一对应，而它固定 $$\mathbb{F}_{p^d}$$。$$\blacksquare$$

**定理 3.15（分圆域：Galois 群是单位群）** 设 $$\zeta_n$$ 为 $$n$$ 次本原单位根（$$\zeta_n=e^{2\pi i/n}$$），$$L=\mathbb{Q}(\zeta_n)$$。则

$$L/\mathbb{Q}\ \text{是 Galois 扩张},\quad \operatorname{Gal}(L/\mathbb{Q})\cong(\mathbb{Z}/n\mathbb{Z})^{\times},\quad [L:\mathbb{Q}]=\varphi(n),$$

其中同构由 $$\sigma_a\ (\gcd(a,n)=1)$$ 给出：

$$\sigma_a(\zeta_n)=\zeta_n^{\,a}.$$

**证明** **（a）$$L$$ 是分裂域：** $$t^n-1$$ 的根恰为 $$1,\zeta_n,\zeta_n^2,\dots,\zeta_n^{n-1}$$，全都住在 $$L$$ 中，故 $$L$$ 是 $$t^n-1$$ 的分裂域。特征 $$0$$ 下 $$t^n-1$$ 无重根（$$(t^n-1)'=nt^{n-1}\ne0$$），故 $$L/\mathbb{Q}$$ 可分且正规，是 Galois 扩张。

**（b）自同构由 $$\zeta_n$$ 的像决定：** 任意 $$\sigma\in\operatorname{Gal}(L/\mathbb{Q})$$ 把 $$\zeta_n$$ 送到 $$t^n-1$$ 的某个根，即 $$\sigma(\zeta_n)=\zeta_n^{a}$$。因 $$\sigma$$ 可逆，$$\zeta_n^a$$ 仍须是本原 $$n$$ 次单位根，故 $$\gcd(a,n)=1$$（否则 $$\zeta_n^a$$ 的阶为 $$n/\gcd(a,n)<n$$）。于是得到映射

$$\operatorname{Gal}(L/\mathbb{Q})\to(\mathbb{Z}/n)^{\times},\qquad \sigma\mapsto a\ (\text{若}\ \sigma(\zeta_n)=\zeta_n^a).$$

**（c）它是双射：** 保乘法（$$\sigma\tau(\zeta_n)=\sigma(\zeta_n^b)=(\zeta_n^a)^b=\zeta_n^{ab}$$）；单射（$$a=1$$ 时 $$\sigma$$ 固定 $$\zeta_n$$ 与 $$\mathbb{Q}$$，从而固定 $$L$$）；满射（对每个 $$\gcd(a,n)=1$$，$$\zeta_n\mapsto\zeta_n^a$$ 把 $$t^n-1$$ 的根置换，延拓为 $$L$$ 的自同构 $$\sigma_a$$）。

**（d）次数：** 记 $$\Phi_n$$ 为 $$\zeta_n$$ 的极小多项式，称 **$$n$$ 次分圆多项式 (cyclotomic polynomial)**。由 (a) 与定理 3.9 的 (3)，

$$\lvert\operatorname{Gal}(L/\mathbb{Q})\rvert=[L:\mathbb{Q}]=\deg\Phi_n=\varphi(n)=\lvert(\mathbb{Z}/n)^{\times}\rvert$$

（最后的等号就是 Euler $$\varphi$$ 函数的定义）。$$\blacksquare$$

**例 3.15（$$\mathbb{Q}(\zeta_7)$$ 的唯一二次子域）** $$n=7$$：$$(\mathbb{Z}/7)^\times\cong\mathbb{Z}/6$$。循环群 $$\mathbb{Z}/6$$ 的子群与 $$6$$ 的正因子 $$1,2,3,6$$ 一一对应；特别地它恰有一个 $$3$$ 阶（指数 $$2$$）子群 $$\{1,2,4\}$$，故 $$\mathbb{Q}(\zeta_7)$$ 恰有一个二次中间域 $$E$$，且 $$[E:\mathbb{Q}]=6/3=2$$。

$$E$$ 是哪个二次域？对素数 $$p$$，$$\mathbb{Q}(\zeta_p)$$ 的唯一二次子域是 $$\mathbb{Q}\bigl(\sqrt{p^*}\bigr)$$，$$p^*=(-1)^{(p-1)/2}p$$（可由判别式 $$\Delta_{\mathbb{Q}(\zeta_p)}=(-1)^{(p-1)/2}p^{\,p-2}$$ 与导子-判别式关系读出，也可直接算，见竞 2）。取 $$p=7$$：$$p^*=(-1)^3\cdot7=-7$$，故 $$E=\mathbb{Q}(\sqrt{-7})$$。**注意**：$$\zeta_7+\zeta_7^{-1}=2\cos\frac{2\pi}{7}$$ 生成的是次数 $$3$$ 的**实**子域（它是 $$\mathbb{Q}(\sqrt{-7})$$ 之上的那个三次扩张），不要与二次子域混淆；真正的生成元是 $$\alpha=\zeta_7+\zeta_7^2+\zeta_7^4$$（完整计算见竞 2）。

### 3.8 可解群与根式解

**定义 3.16（根式可解, solvable by radicals）** 设 $$f\in K[t]$$（$$\operatorname{char}K=0$$）。称 $$f$$ **根式可解**，若它的全部根都落在某个域塔

$$K=F_0\subseteq F_1\subseteq\cdots\subseteq F_m=L$$

之中，其中每步 $$F_i=F_{i-1}(a_i)$$ 且 $$a_i^{\,n_i}\in F_{i-1}$$ 对某个正整数 $$n_i$$ 成立（即 $$a_i$$ 是 $$F_{i-1}$$ 中某元素的 $$n_i$$ 次根），并且 $$f$$ 在 $$L$$ 上完全分裂。

「根式可解」的形式化很直白：允许的运算就是加减乘除（造 $$F(a)$$ 时用）与开方（$$a^{n}\in F$$），这正是一般求根公式能写出的东西。

**定理 3.17（Galois 定理：根式可解 $$\iff$$ Galois 群可解）** 设 $$f\in K[t]$$，$$\operatorname{char}K=0$$，$$L$$ 为 $$f$$ 的分裂域，$$G=\operatorname{Gal}(L/K)$$。则

$$f\ \text{根式可解}\iff G\ \text{是可解群}\ (\text{即导列}\ G^{(m)}=\{1\}\ \text{对某}\ m).$$

**证明（思路）** 两个方向各用一个关键引理。

**（$$\Rightarrow$$）** 设 $$f$$ 有一根式塔。不妨设每步都是 Galois 扩张：若某步 $$F_i/F_{i-1}$$ 不 Galois，可先把它换成该步多项式的分裂域，并配合第 38 章的「足够多单位根」策略。核心引理是：**若 $$F$$ 含有 $$n$$ 次本原单位根且 $$M=F(\sqrt[n]{a})$$ 是 $$F$$ 的 Galois 扩张，则 $$\operatorname{Gal}(M/F)$$ 是循环群**（阶整除 $$n$$）。证明：取 $$\sigma\in\operatorname{Gal}(M/F)$$ 与一个 $$n$$ 次根 $$b=\sqrt[n]{a}$$，则 $$\sigma(b)=\zeta b$$ 对某个 $$n$$ 次单位根 $$\zeta$$（因 $$\sigma(b)^n=\sigma(a)=a=b^n$$），于是 $$\sigma\mapsto\zeta$$ 是 $$\operatorname{Gal}(M/F)\to\mu_n$$ 的单同态，其像循环。把这些循环（因而交换）因子沿塔拼起来，$$G$$ 就有一条交换商的次正规列，由可解群的判据（第 04 章）$$G$$ 可解。

**（$$\Leftarrow$$）** 设 $$G$$ 可解，取合成列/导列 $$G=G_0\trianglerighteq G_1\trianglerighteq\cdots\trianglerighteq G_m=\{1\}$$ 使每个 $$G_i/G_{i+1}$$ 交换（导列即满足此性质）。先扩大基域：令 $$K'\supseteq K$$ 含足量单位根（比如含 $$\lvert G\rvert$$ 次本原单位根），$$L'=LK'$$。由定理 3.11 的共轭对应与定理 3.12，$$\operatorname{Gal}(L'/K')$$ 仍是 $$G$$ 的一个子群（扩张基域只会缩小 Galois 群），故也可解。

再由定理 3.11（性质 4）逐步降：每个商 $$G_i/G_{i+1}$$ 交换，对应一个 Abel 扩张；对 Abel 扩张用 Kummer 理论（上一步引理的反向版本）：**$$F$$ 含 $$n$$ 次本原单位根、$$\operatorname{Gal}(M/F)$$ 为阶整除 $$n$$ 的循环群时，$$M=F(\sqrt[n]{a})$$ 对某个 $$a\in F$$**。于是每一层 $$L_i/L_{i+1}$$ 都是一次开方，逐步搭出根式域塔。最后回到 $$K$$（单位根本身也是一次根式扩张，$$\zeta_n$$ 是 $$t^n-1$$ 的根），$$f$$ 的全部根落在其内。$$\blacksquare$$

**注 3.17（这台机器做了什么）** 定理 3.17 把「逐次开方」这个**域论动作**，精确翻译成「逐层剥离交换商」这个**群论动作**。一个关于域的解析/构造问题，化归为一个有限群的结构问题。这是 19 世纪代数学最深刻的一次翻译。

**定理 3.18（$$n\ge5$$ 时 $$S_n$$ 不可解）** 设 $$n\ge5$$。则 $$S_n$$ 的导列从第 $$1$$ 项起恒等于 $$A_n$$，永不归零；特别地 $$S_n$$ 不可解，$$A_n$$ 也非交换、非可解。

**证明** **（a）三轮换生成 $$A_n$$（$$n\ge3$$），且 $$A_n$$ 非交换：** 任一偶置换是偶数个对换之积，而两个对换之积总能写成三轮换之积（以下复合按右到左）：

$$(a\,b)(b\,c)=(a\,b\,c),\qquad (a\,b)(c\,d)=(a\,c\,b)(a\,c\,d)\qquad(a,b,c,d\ \text{互异}).$$

逐点验证：第一式中 $$a\mapsto b\mapsto c$$、$$c\mapsto b\mapsto a$$，恰是三轮换；第二式把两条链合并后仍得 $$(a\,b)(c\,d)$$。故 $$A_n=\langle\text{三轮换}\rangle$$。又 $$n\ge4$$ 时 $$A_n$$ 非交换：$$(1\,2\,3)(1\,2\,4)=(1\,3)(2\,4)$$ 而反向复合得 $$(1\,4)(2\,3)$$，两者不同。

**（b）$$n\ge5$$ 时三轮换是 $$A_n$$ 中两个三轮换的换位子，故 $$A_n'=A_n$$：** 取互异的五点 $$a,b,c,d,e$$，则

$$(a\,b\,d)=[(a\,b\,c),\,(a\,d\,e)]=(a\,b\,c)(a\,d\,e)(a\,c\,b)(a\,e\,d).$$

**验证**：取 $$a,b,c,d,e=1,2,3,4,5$$，按右到左复合逐点计算

$$1\mapsto 5\mapsto 5\mapsto 1\mapsto 2,\qquad 2\mapsto 2\mapsto 1\mapsto 4\mapsto 4,\qquad 4\mapsto 1\mapsto 3\mapsto 3\mapsto 1,\qquad 3\mapsto 3,\quad 5\mapsto 5,$$

故结果恰是 $$(1\,2\,4)$$；一般情形由「置换共轭只改名」即得。于是五点的任意三点都能写成三轮换的换位子，而 $$n\ge5$$ 时这些三轮换生成 $$A_n$$（由 (a)），故

$$A_n'\supseteq\langle\text{三轮换}\rangle=A_n;\qquad A_n'\subseteq A_n\ \text{自动成立};\qquad\text{故}\ A_n'=A_n.$$

也就是说 $$A_n$$ 是**完全群 (perfect group)**：它没有非平凡的交换商。（注意 $$n=5$$ 是这条恒等式需要的最小点数：它要五个互异点。）

**（c）$$S_n'=A_n$$：** 一方面 $$S_n/A_n\cong\mathbb{Z}/2$$ 交换，故 $$S_n'\subseteq A_n$$；另一方面 $$A_n\le S_n$$ 蕴含 $$A_n'=A_n\subseteq S_n'$$。故 $$S_n'=A_n$$。

**（d）导列停住：** $$S_n^{(0)}=S_n$$、$$S_n^{(1)}=A_n$$，此后 $$S_n^{(2)}=(S_n^{(1)})'=A_n'=A_n$$，归纳得 $$S_n^{(k)}=A_n\ne\{1\}$$ 对一切 $$k\ge1$$。导列永不归零，$$S_n$$ 不可解。$$\blacksquare$$

**注 3.18（这个证明刻意绕开了什么）** 更强的标准事实是 $$A_n$$（$$n\ge5$$）**单**（没有非平凡真正规子群）。上面的论证用不到它：判定「不可解」只需要「$$A_n$$ 没有非平凡交换商」，即 $$A_n'=A_n$$，而这一条从「三点可由五点拼出换位子」直接落出。单性的证明要长得多（要做共轭类的型分析），本章不需要。

**定理 3.19（Abel–Ruffini：一般 $$n\ge5$$ 次方程无根式解）** 设 $$t_1,\dots,t_n$$ 是未定元，$$s_1,\dots,s_n$$ 为它们的初等对称函数，$$f(t)=t^n+s_1t^{n-1}+\cdots+s_n=\prod(t-t_i)$$，视其为 $$F=\mathbb{Q}(s_1,\dots,s_n)$$ 上的多项式。则

$$\operatorname{Gal}(f/F)=S_n\ (n\ \text{任意}),$$

因此当 $$n\ge5$$ 时 $$f$$ 不根式可解。

**证明** **（a）$$S_n\subseteq\operatorname{Gal}$$：** 设 $$\sigma\in S_n$$ 置换下标，令它作用在 $$t_i$$ 上为 $$t_i\mapsto t_{\sigma(i)}$$。因 $$f$$ 的系数 $$s_j$$ 是 $$t_i$$ 的对称函数，被任何置换固定，故这个作用固定 $$F$$，即 $$\sigma\in\operatorname{Aut}_F(L)$$，$$L=\mathbb{Q}(t_1,\dots,t_n)$$ 是 $$f$$ 的分裂域。

**（b）$$\operatorname{Gal}\subseteq S_n$$：** Galois 群作用在 $$n$$ 个根上，每个自同构由根上的置换决定（根生成 $$L$$），故 $$\operatorname{Gal}(f/F)\hookrightarrow S_n$$。

**（c）合起来：** 由 (a)(b)，$$\operatorname{Gal}(f/F)=S_n$$。于是 $$f$$ 根式可解 $$\iff S_n$$ 可解（定理 3.17）$$\iff n\le4$$（定理 3.18），故 $$n\ge5$$ 时不可根式求解。$$\blacksquare$$

**注 3.19（从「否定」到「刻画」）** Abel–Ruffini 只否定了一般公式的存在。Galois 理论的真正力量在于**对每个具体多项式给出判据**：$$t^5-6t+3$$ 不可解（它的 Galois 群是 $$S_5$$，见第 5 题），而 $$t^5-1=(t-1)\Phi_5(t)$$ 可解（其分裂域是 $$\mathbb{Q}(\zeta_5)$$，$$\operatorname{Gal}\cong(\mathbb{Z}/5)^\times\cong\mathbb{Z}/4$$ 循环）。同一个次数，两种命运——这就是 Galois 对应比 Abel–Ruffini 更深的地方。

## 四、几何与物理直觉 (Intuition)

### 4.1 图像：两座格，面对面倒着摆

Galois 对应是一张**图**。画两列点：左边一列是中间域，从下到上按包含排列（最下面是 $$K$$，最上面是 $$L$$）；右边一列是 $$G$$ 的子群，从上到下按包含排列（最上面是 $$G$$，最下面是 $$\{1\}$$）。连线只用一条：$$E$$ 连到 $$\operatorname{Gal}(L/E)$$。定理 3.11 说这张图是**完美对称**的——左边每一根上升的线段，右边恰有一根下降的线段与之对应。

以 $$L=\mathbb{Q}(\sqrt2,\sqrt3)$$ 为例（例 3.11），左边是一座「五层塔」：$$\mathbb{Q}\subset\mathbb{Q}(\sqrt2),\mathbb{Q}(\sqrt3),\mathbb{Q}(\sqrt6)\subset L$$；右边是 $$(\mathbb{Z}/2)^2$$ 的子群格——一个菱形加上下两个端点，也是五个点、三根链。左右点数相同、每个点的「高度」彼此互补。**这就是「域的子结构 = 群的子结构」的几何含义**：不是两个相似的图，而是同一张图的两种标注。

### 4.2 为什么「域越大，对称越少」

序反性 (1) 在直觉上很自然：域 $$E$$ 越大，「必须保持不动」的元素越多；约束越多，满足约束的映射越少。这与几何中「图形越复杂、对称群越小」完全平行。反过来，$$\{1\}$$（最小群）对应最大域 $$L$$——不要求保留任何额外东西；$$G$$（最大群）对应最小域 $$K$$——要求保留全部。

### 4.3 物理：对称破缺与「剩余对称」

把 $$L/K$$ Galois 读成物理语言：$$L$$ 是全对称的母相、$$G$$ 是完整对称群。选一个中间域 $$E$$ 相当于**对称破缺 (symmetry breaking)**，$$H=\operatorname{Gal}(L/E)$$ 是**剩余对称群**，被破缺掉的是商 $$G/H$$。由定理 3.11 (iv)，$$[E:K]=[G:H]$$：**破缺出的「相」的复杂程度，恰好等于被破缺掉的对称的量**。而当 $$H\trianglelefteq G$$ 时 $$\operatorname{Gal}(E/K)\cong G/H$$——**剩余对称正规，等价于这个相自己是一个自洽的物理系统**（$$E/K$$ 本身也是 Galois 扩张，有自己的对称群）。这正是规范理论中「自发破缺后有效理论由商群 $$G/H$$ 描述」的代数骨架。

### 4.4 一个矩阵图像（MP149 的写法）

对最简单的例子 $$\mathbb{C}/\mathbb{R}$$，把复数写成实矩阵（第 01 章）：$$a+bi\leftrightarrow\begin{pmatrix}a&-b\\ b&a\end{pmatrix}$$，而 $$a+bi\mapsto a-bi$$ 就是左乘 $$\sigma_2=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$$。于是

$$\operatorname{Gal}(\mathbb{C}/\mathbb{R})\cong\mathbb{Z}/2\cong O(2)/SO(2).$$

「Galois 群」在这里就是「保持 $$\mathbb{R}$$ 不动的矩阵对称」——第 24 章「变换群」的最小实例。这个视角是本章所有例子的精神：**把域的扩张翻译成线性空间上的（半）线性变换群**。

## 五、经典问题精讲 (Classical Problems)

### 题 1（完整的对应表：$$\mathbb{Q}(\sqrt2,\sqrt3,\sqrt5)$$）

**考点**：定理 3.12（合成域）给出 Galois 群，定理 3.11 (iv)（$$\lvert H\rvert$$ 与 $$[E:K]$$ 互换）给出计数。
**在本章结构中的位置**：把「查字典」这件事做到极致——先算出群，再从群的子群反推全部中间域。

**问题**：设 $$L=\mathbb{Q}(\sqrt2,\sqrt3,\sqrt5)$$。求 $$\operatorname{Gal}(L/\mathbb{Q})$$，并算出 $$L/\mathbb{Q}$$ 的中间域总数、二次中间域全表、四次中间域全表。

**解** 三步。

**第一步：Galois 群。** 用与例 3.12 完全相同的论证（交域次数同时整除 2 与 2，若为 2 则两个二次域相等，而那需要 $$\sqrt{p}\in\mathbb{Q}(\sqrt{q})$$，平方后立刻矛盾），三个二次域两两交为 $$\mathbb{Q}$$；再用定理 3.12 的归纳版本得

$$L/\mathbb{Q}\ \text{Galois},\qquad G=\operatorname{Gal}(L/\mathbb{Q})\cong(\mathbb{Z}/2)^3.$$

具体地，$$G=\{\sigma_{v}: v\in\mathbb{F}_2^3\}$$，其中 $$\sigma_v(\sqrt2)=(-1)^{v_1}\sqrt2,\ \sigma_v(\sqrt3)=(-1)^{v_2}\sqrt3,\ \sigma_v(\sqrt5)=(-1)^{v_3}\sqrt5$$。这是**初等交换** $$2$$-群：每个非单位元都是对合。

**第二步：数中间域。** 由定理 3.11，中间域 $$\leftrightarrow$$ $$G$$ 的子群；而 $$(\mathbb{Z}/2)^3=\mathbb{F}_2^3$$ 的子群就是 $$\mathbb{F}_2$$-线性子空间。三维 $$\mathbb{F}_2$$-空间的 $$k$$ 维子空间个数为高斯二项式系数 $$\binom{3}{k}_2$$，逐代得 $$1,7,7,1$$（也可以直接数：非零向量有 $$7$$ 个，每个生成一条 $$\mathbb{F}_2$$-直线，故一维子空间 $$7$$ 个；维度互补给出二维子空间也是 $$7$$ 个）。故

$$\text{中间域总数}=1+7+7+1=16.$$

**第三步：二次与四次中间域全表。** 由 $$[E:\mathbb{Q}]=[G:\operatorname{Gal}(L/E)]$$：

- $$[E:\mathbb{Q}]=2\iff[G:H]=2\iff\lvert H\rvert=4\iff H$$ 是二维子空间。二维子空间是某个非零线性泛函 $$\lambda$$ 的核，对应 $$\mathbb{Q}\bigl(\sqrt{\textstyle\prod_{i\in S}}p_i\bigr)$$，其中 $$S$$ 是 $$\lambda$$ 在标准基上取值 $$1$$ 的位置集。于是 7 个二次域恰为

$$\mathbb{Q}(\sqrt2),\ \mathbb{Q}(\sqrt3),\ \mathbb{Q}(\sqrt5),\ \mathbb{Q}(\sqrt6),\ \mathbb{Q}(\sqrt{10}),\ \mathbb{Q}(\sqrt{15}),\ \mathbb{Q}(\sqrt{30}).$$

- $$[E:\mathbb{Q}]=4\iff H$$ 是一维子空间（共 7 个）。逐个写出固定域（$$\sigma_v$$ 固定所有满足 $$v_i=0$$ 的 $$\sqrt{p_i}$$，并且固定那些「被翻转两次」的乘积）：

| $$v$$ | $$\sigma_v$$ 翻转 | $$L^{\langle\sigma_v\rangle}$$（四次域） |
|---|---|---|
| $$(1,0,0)$$ | $$\sqrt2$$ | $$\mathbb{Q}(\sqrt3,\sqrt5)$$ |
| $$(0,1,0)$$ | $$\sqrt3$$ | $$\mathbb{Q}(\sqrt2,\sqrt5)$$ |
| $$(0,0,1)$$ | $$\sqrt5$$ | $$\mathbb{Q}(\sqrt2,\sqrt3)$$ |
| $$(1,1,0)$$ | $$\sqrt2,\sqrt3$$ | $$\mathbb{Q}(\sqrt5,\sqrt6)$$ |
| $$(1,0,1)$$ | $$\sqrt2,\sqrt5$$ | $$\mathbb{Q}(\sqrt3,\sqrt{10})$$ |
| $$(0,1,1)$$ | $$\sqrt3,\sqrt5$$ | $$\mathbb{Q}(\sqrt2,\sqrt{15})$$ |
| $$(1,1,1)$$ | 三者 | $$\mathbb{Q}(\sqrt6,\sqrt{10})$$ |

以第四行为例核对：$$\sigma_{(1,1,0)}$$ 把 $$\sqrt2\mapsto-\sqrt2$$、$$\sqrt3\mapsto-\sqrt3$$，于是 $$\sqrt6=\sqrt2\sqrt3$$ 与 $$\sqrt5$$ 都被固定，故 $$\mathbb{Q}(\sqrt5,\sqrt6)\subseteq L^{\langle\sigma\rangle}$$；两边次数都是 $$[G:\langle\sigma\rangle]=8/2=4$$（左边是两两交为 $$\mathbb{Q}$$ 的二次域合成），故相等。最后一行为例：$$\sigma_{(1,1,1)}$$ 翻转三者，而 $$\sqrt6,\sqrt{10},\sqrt{15}$$ 都被固定，故固定域 $$\supseteq\mathbb{Q}(\sqrt6,\sqrt{10})$$，次数同为 $$4$$，故相等。

**答**：$$G\cong(\mathbb{Z}/2)^3$$；中间域共 $$16$$ 个（含 $$L$$ 与 $$\mathbb{Q}$$）；其中二次域 $$7$$ 个（上表第二组）、四次域 $$7$$ 个（上表）。注意 $$16$$ 与 $$7+7+2=16$$ 吻合，且没有别次数的中间域——因为 $$\lvert G\rvert=8$$ 的因子只有 $$1,2,4,8$$。

### 题 2（$$t^3-2$$：把 $$S_3$$ 的六个子群全部翻译出来）

**考点**：用判别式（定理 3.13）定出 Galois 群，再用定理 3.11 列出全部中间域，并观察「不正规的子群对应不 Galois 的中间域」。
**位置**：定理 3.11 性质 (4) 的最完整一次演练。

**问题**：设 $$f(t)=t^3-2$$，$$L$$ 为其分裂域。求 $$[L:\mathbb{Q}]$$、$$\operatorname{Gal}(L/\mathbb{Q})$$，并列出全部中间域及其次数。

**解** 记 $$\beta=\sqrt[3]{2}$$，$$\omega=e^{2\pi i/3}$$，三根为 $$\alpha_1=\beta,\ \alpha_2=\beta\omega,\ \alpha_3=\beta\omega^2$$。

**（1）分裂域与次数。** $$L=\mathbb{Q}(\beta,\omega)$$。其中 $$[\mathbb{Q}(\beta):\mathbb{Q}]=3$$（Eisenstein，$$p=2$$），而 $$\omega=\alpha_2/\alpha_1\in L$$，$$\omega\notin\mathbb{Q}(\beta)\subseteq\mathbb{R}$$，故 $$[L:\mathbb{Q}(\beta)]=2$$，塔定理给 $$[L:\mathbb{Q}]=6$$。

**（2）Galois 群。** $$f$$ 在 $$\mathbb{Q}$$ 上不可约，故 $$G$$ 在 $$\{\alpha_1,\alpha_2,\alpha_3\}$$ 上传递（注 3.9），于是 $$3\mid\lvert G\rvert$$；又 $$G\hookrightarrow S_3$$，故 $$\lvert G\rvert\in\{3,6\}$$。用判别式排除 $$\lvert G\rvert=3$$：由 $$t^3+pt+q$$ 的判别式公式 $$\Delta=-4p^3-27q^2$$，取 $$p=0,q=-2$$ 得 $$\Delta=-108$$，它不是 $$\mathbb{Q}$$ 中的平方，故由定理 3.13 得 $$G\not\subseteq A_3$$，即 $$\lvert G\rvert\ne3$$。于是

$$\lvert G\rvert=6=[L:\mathbb{Q}],\qquad G\cong S_3,$$

（$$\lvert G\rvert=[L:\mathbb{Q}]$$ 也顺带确认了 $$L/\mathbb{Q}$$ 是 Galois 扩张——事实上特征 $$0$$ 下 $$L$$ 是分裂域，本就正规可分。）$$S_3$$ 的六个子群是：$$\{1\}$$、$$\langle(1\,2)\rangle$$、$$\langle(1\,3)\rangle$$、$$\langle(2\,3)\rangle$$、$$A_3=\{1,(1\,2\,3),(1\,3\,2)\}$$、$$S_3$$，故中间域恰有六个。

**（3）逐个翻译。** 由 $$[L:E]=\lvert\operatorname{Gal}(L/E)\rvert$$ 与 $$[E:\mathbb{Q}]=[G:\operatorname{Gal}(L/E)]$$：

- $$\operatorname{Gal}(L/E)=S_3\Rightarrow E=L^{S_3}=\mathbb{Q}$$（次数 $$1$$）；
- $$\operatorname{Gal}(L/E)=\{1\}\Rightarrow E=L$$（次数 $$6$$）；
- $$\operatorname{Gal}(L/E)=A_3\Rightarrow[E:\mathbb{Q}]=6/3=2$$：$$A_3$$ 循环置换三根，而 $$\omega=\alpha_2/\alpha_1\mapsto\alpha_3/\alpha_2=\omega$$ 被固定，故 $$L^{A_3}=\mathbb{Q}(\omega)=\mathbb{Q}(\sqrt{-3})$$；
- $$\operatorname{Gal}(L/E)=\langle(2\,3)\rangle\Rightarrow[E:\mathbb{Q}]=6/2=3$$：$$(2\,3)$$ 交换 $$\alpha_2,\alpha_3$$、固定 $$\alpha_1=\beta$$，故 $$E=\mathbb{Q}(\beta)=\mathbb{Q}(\sqrt[3]{2})$$；
- $$\operatorname{Gal}(L/E)=\langle(1\,3)\rangle$$：固定 $$\alpha_2=\beta\omega$$，故 $$E=\mathbb{Q}(\beta\omega)$$，次数 $$3$$；
- $$\operatorname{Gal}(L/E)=\langle(1\,2)\rangle$$：固定 $$\alpha_3=\beta\omega^2$$，故 $$E=\mathbb{Q}(\beta\omega^{2})$$，次数 $$3$$。

**（4）与正规性对应核对。** $$A_3\trianglelefteq S_3$$，故 $$\mathbb{Q}(\sqrt{-3})/\mathbb{Q}$$ 应是 Galois 扩张——它是二次扩张，确实如此（$$\operatorname{Gal}\cong S_3/A_3\cong\mathbb{Z}/2$$，与定理 3.11 性质 4 的商群公式一致）。三个 $$2$$ 阶子群都不正规（$$S_3$$ 中 $$2$$ 阶子群共轭类大小 $$3$$），故 $$\mathbb{Q}(\sqrt[3]{2}),\mathbb{Q}(\beta\omega),\mathbb{Q}(\beta\omega^2)/\mathbb{Q}$$ 都不是 Galois 扩张——这正是例 3.5 中「$$\mathbb{Q}(\sqrt[3]{2})$$ 不正规」的再一次现身，而且这次我们看清了它的**原因在群里**：对应的子群不正规。

### 题 3（$$\mathbb{F}_{16}/\mathbb{F}_2$$：Frobenius 的对应表）

**考点**：定理 3.14——有限域的 Galois 群由 Frobenius 生成，子域由整除关系控制。
**位置**：把 Galois 对应搬到特征 $$p$$ 的舞台，检验「可分性自动成立」这一注记。

**问题**：求 $$\operatorname{Gal}(\mathbb{F}_{16}/\mathbb{F}_2)$$，列出 $$\mathbb{F}_{16}$$ 的全部子域，并验证 $$\operatorname{Gal}(\mathbb{F}_{16}/\mathbb{F}_4)\cong\operatorname{Gal}(\mathbb{F}_4/\mathbb{F}_2)$$。

**解** $$16=2^4$$，故 $$\mathbb{F}_{16}/\mathbb{F}_2$$ 的次数为 $$4$$。由定理 3.14，$$\operatorname{Gal}(\mathbb{F}_{16}/\mathbb{F}_2)=\langle\varphi\rangle\cong\mathbb{Z}/4$$，$$\varphi(x)=x^2$$，且 $$\varphi$$ 的阶为 $$4$$（$$\varphi^k=\mathrm{id}\iff x^{2^k}=x$$ 对一切 $$x\in\mathbb{F}_{16}\iff 2^k\ge2^4$$）。

$$\mathbb{Z}/4$$ 的子群恰有三个：$$\{1\}$$、$$\langle\varphi^2\rangle$$（阶 $$2$$）、$$\langle\varphi\rangle$$（阶 $$4$$）。于是中间域也恰有三个：

- $$H=\langle 1\rangle$$：固定域为 $$\mathbb{F}_{16}$$ 本身（次数 $$4$$）；
- $$H=\langle\varphi^2\rangle$$：$$\varphi^2(x)=x^4$$，条件 $$x^4=x$$ 的根恰是 $$t^4-t$$ 的全部 $$4$$ 个根，即 $$\mathbb{F}_4$$。故固定域是 $$\mathbb{F}_4$$，次数 $$[G:H]=4/2=2$$；
- $$H=\langle\varphi\rangle$$：$$\varphi(x)=x^2$$，条件 $$x^2=x$$ 给出 $$\mathbb{F}_2$$，次数 $$[G:H]=4/4=1$$。

所以 $$\mathbb{F}_{16}$$ 的子域只有 $$\mathbb{F}_2\subset\mathbb{F}_4\subset\mathbb{F}_{16}$$ 三个（含自身）。这与一般事实「$$\mathbb{F}_{p^m}\subseteq\mathbb{F}_{p^n}\iff m\mid n$$」一致（$$4$$ 的正因子是 $$1,2,4$$）。

最后验证商群：$$\langle\varphi^2\rangle\trianglelefteq\langle\varphi\rangle$$（$$\mathbb{Z}/4$$ 交换），故 $$\mathbb{F}_4/\mathbb{F}_2$$ 是 Galois 扩张，且由定理 3.11 性质 4，

$$\operatorname{Gal}(\mathbb{F}_4/\mathbb{F}_2)\cong\langle\varphi\rangle/\langle\varphi^2\rangle\cong\mathbb{Z}/2.$$

直接验算：$$\mathbb{F}_4/\mathbb{F}_2$$ 的 Frobenius 是 $$x\mapsto x^2$$，在 $$\mathbb{F}_4$$ 上阶为 $$2$$，确实同构于 $$\mathbb{Z}/2$$。整个计算中没有出现「可分性」这一步——有限域是完全域，可分性免费送出（注 3.4）。

### 题 4（$$t^3-3t+1$$：判别式与循环群）

**考点**：定理 3.13 的反向使用——判别式是平方时 Galois 群落进 $$A_n$$。
**位置**：与题 2 成对照：同一个次数，判别式决定群从 $$S_3$$ 缩到 $$A_3$$，中间域随之从 $$6$$ 个缩到 $$2$$ 个。

**问题**：设 $$f(t)=t^3-3t+1$$。求 $$\operatorname{Gal}(f)$$、分裂域的次数，并列出全部中间域。

**解** **（1）不可约。** 有理根只能是 $$\pm1$$：$$f(1)=1-3+1=-1\ne0$$，$$f(-1)=-1+3+1=3\ne0$$。三次无有理根即无一次因子，故不可约。

**（2）判别式。** $$t^3+pt+q$$ 的判别式是 $$\Delta=-4p^3-27q^2$$。取 $$p=-3,\ q=1$$：

$$\Delta=-4(-27)-27=108-27=81=9^2,$$

是 $$\mathbb{Q}$$ 中的平方。由定理 3.13，$$\operatorname{Gal}(f)\subseteq A_3$$。

**（3）群。** 不可约 + $$G\hookrightarrow S_3$$ 传递 $$\Rightarrow3\mid\lvert G\rvert$$（注 3.9）；而 $$G\subseteq A_3$$、$$\lvert A_3\rvert=3$$，故 $$G=A_3\cong\mathbb{Z}/3$$。于是 $$\lvert G\rvert=3=[L:\mathbb{Q}]$$，$$L/\mathbb{Q}$$ 是次数 $$3$$ 的 Galois 扩张。

**（4）中间域。** $$\mathbb{Z}/3$$ 是素数阶循环群，只有两个子群，故中间域只有 $$L$$ 与 $$\mathbb{Q}$$——**没有任何真中间域**。

**（5）$$L$$ 是什么？** 令 $$t=2\cos\theta$$，用三倍角恒等式 $$(2\cos\theta)^3-3(2\cos\theta)=2\cos3\theta$$ 得

$$f(2\cos\theta)=2\cos3\theta+1,$$

故 $$f(t)=0\iff\cos3\theta=-\tfrac12\iff\theta=\tfrac{2\pi}{9},\tfrac{4\pi}{9},\tfrac{8\pi}{9}$$（在 $$[0,\pi]$$ 内）。三根为 $$2\cos\frac{2\pi}{9},2\cos\frac{4\pi}{9},2\cos\frac{8\pi}{9}$$，于是

$$L=\mathbb{Q}\Bigl(2\cos\tfrac{2\pi}{9}\Bigr)=\mathbb{Q}(\zeta_9)^{+},$$

后者是 $$\mathbb{Q}(\zeta_9)$$ 的实子域。核对：$$(\mathbb{Z}/9)^{\times}\cong\mathbb{Z}/6$$（定理 3.15），把 $$\{1,-1\}$$ 商掉得 $$\mathbb{Z}/3$$，正是 $$L/\mathbb{Q}$$ 的 Galois 群——与 (3) 的 $$A_3\cong\mathbb{Z}/3$$ 吻合。这条「用余弦写出循环三次域」的路线是分圆域理论的标准副产品。

### 题 5（入口题收官：$$t^5-6t+3$$ 不可根式求解）

**考点**：定理 3.13、注 3.9、定理 3.17、定理 3.18 的联合使用。
**位置**：全章的用途。它同时回答了入口题 (5)。

**问题**：设 $$f(t)=t^5-6t+3\in\mathbb{Q}[t]$$。证明 $$f$$ 的全部根不能用加减乘除与开方表示。

**解** 分五步。

**（1）$$f$$ 在 $$\mathbb{Q}$$ 上不可约。** 先看模 $$2$$：$$f\equiv t^5+1=(t+1)\Phi_5(t)\pmod 2$$，其中 $$\Phi_5(t)=t^4+t^3+t^2+t+1$$。$$t+1$$ 在 $$\mathbb{F}_2$$ 上不可约；$$\Phi_5$$ 在 $$\mathbb{F}_2$$ 上也不可约——$$\Phi_5$$ 的根在 $$\mathbb{F}_{2^d}$$ 中当且仅当 $$2^d\equiv1\pmod 5$$（$$d$$ 是 $$2$$ 在 $$(\mathbb{Z}/5)^\times$$ 中的阶），而 $$2,4,3,1$$ 的阶为 $$4$$，故 $$d=4$$。

设 $$f=gh$$ 在 $$\mathbb{Q}$$ 上非平凡分解，可设 $$g,h$$ 首一。由 Gauss 引理，模 $$2$$ 后 $$\bar f=\bar g\bar h$$。$$\bar f$$ 的不可约因子只有 $$t+1$$ 与 $$\Phi_5$$，次数为 $$1$$ 与 $$4$$；而 $$\bar g$$ 的不可约因子只能从这两个中取（$$\mathbb{F}_2[t]$$ 是唯一分解环），故 $$\deg\bar g\in\{0,1,4,5\}$$。若 $$\deg\bar g=1$$，则 $$\bar g=t+1$$，即 $$g$$ 的根模 $$2$$ 为 $$1$$，于是 $$g$$ 有一个奇整数根（Gauss 引理：首一整系数因子的根是有理根，且由 $$\bar g=t+1$$ 知其模 $$2$$ 余 $$1$$）；但 $$f$$ 的有理根只能是 $$\pm1,\pm3$$，而

$$f(1)=-2,\quad f(-1)=8,\quad f(3)=228,\quad f(-3)=-222,$$

全非零，矛盾。若 $$\deg\bar g=4$$，则 $$\deg\bar h=1$$，同法矛盾。$$\deg\bar g\in\{0,5\}$$ 即 $$\bar g=1$$ 或 $$\bar f$$，说明 $$g$$ 是常数或 $$f$$ 本身。故 $$f$$ 不可约。

**（2）$$f$$ 恰有三个实根。** $$f'=5t^4-6$$ 在 $$t=\pm c$$（$$c=(6/5)^{1/4}\approx1.046$$）处为零，且 $$f'$$ 在 $$(-\infty,-c)$$ 与 $$(c,\infty)$$ 上为正、在 $$(-c,c)$$ 上为负。于是 $$f$$ 在 $$(-\infty,-c]$$ 上递增、在 $$[-c,c]$$ 上递减、在 $$[c,\infty)$$ 上递增。

由 $$5c^4=6$$ 得 $$c^5=\tfrac{6c}{5}$$，于是

$$f(-c)=-c^5+6c+3=\tfrac{24c}{5}+3>0,\qquad f(c)=c^5-6c+3=3-\tfrac{24c}{5}<0$$

又 $$f(t)\to-\infty\ (t\to-\infty)$$、$$f(t)\to+\infty\ (t\to+\infty)$$。由介值定理，三个单调区间 $$(-\infty,-c]$$、$$[-c,c]$$、$$[c,\infty)$$ 上各有且仅有一个实根（每个区间上 $$f$$ 严格单调，故根唯一），共**三个实根**；剩下两个根是**非实共轭复数**。

**（3）Galois 群含一个对换。** 设 $$L$$ 为 $$f$$ 的分裂域，$$G=\operatorname{Gal}(L/\mathbb{Q})$$。对 $$z\in L$$ 取复共轭 $$\bar z$$：因为 $$f$$ 的系数是实数，$$\bar z$$ 仍是 $$f$$ 的根；又 $$L$$ 由 $$f$$ 的根生成，故复共轭是 $$L$$ 的一个自同构，且固定 $$\mathbb{Q}$$。由 (2)，它固定三个实根、交换那两个非实复根，故对应根集上的一个**对换 (transposition)**——一个奇置换。

**（4）Galois 群含一个 5-循环，从而 $$G=S_5$$。** 由 (1) 与注 3.9，$$G$$ 在五个根上传递，故 $$5\mid\lvert G\rvert$$；由 Cauchy 定理（第 03 章），$$G$$ 含一个 5 阶元，它在五个字母上只能是 **5-循环**。

现在用一条标准引理：**设 $$p$$ 素数，$$H\le S_p$$ 传递，且 $$H$$ 同时含一个对换与一个 $$p$$-循环，则 $$H=S_p$$。** 证明如下。共轭不改变结论，故可设 $$p$$-循环是 $$\sigma=(1\,2\,\cdots\,p)$$，对换是 $$\tau=(a\,b)$$。考察

$$\rho=\sigma^{\,b-a}\,\tau\,\sigma^{-(b-a)}=(b,\ 2b-a),$$

（共轭公式：$$\sigma^{k}(a\,b)\sigma^{-k}=(a+k,\ b+k)$$，取 $$k=b-a$$）。$$\rho$$ 与 $$\tau$$ 在点 $$b$$ 处相交，故乘积

$$\tau\rho=(a\,b)(b,\ 2b-a)$$

是一个三轮换（两个共享一点的对换之积是三轮换）。因此 $$H$$ 含三轮换。又 $$H$$ 传递且次数为素数 $$p$$，其不动点块的大小必整除 $$p$$，即块大小只能是 $$1$$ 或 $$p$$——所以 $$H$$ 是本原群 (primitive group)。**Jordan 定理**：含三轮换的本原 $$n$$ 阶群（$$n\ge5$$）必含 $$A_n$$。于是 $$A_p\subseteq H\le S_p$$。若 $$H=A_p$$，则 $$H$$ 不含对换（$$A_p$$ 的元素都是偶置换），与 $$\tau\in H$$ 矛盾；故 $$H=S_p$$。

代 $$p=5$$：$$G$$ 传递、含对换、含 5-循环，故 $$G=S_5$$。

**（5）收尾。** 由定理 3.18，$$S_5$$ 不可解（其导列从 $$A_5$$ 起恒定，永不归零）。由定理 3.17（Galois 定理），$$f$$ 根式可解 $$\iff$$ $$\operatorname{Gal}(f)$$ 可解。既然 $$\operatorname{Gal}(f)=S_5$$ 不可解，**$$f$$ 的五个根不能用加减乘除与开方表示**。$$\blacksquare$$

**关键 leap 在哪**：(1)(2) 是普通微积分与模运算，(4) 的组合引理也很短；真正的跳跃是 **(3) 到 (5) 的翻译**——「复共轭是一个对换」这条纯几何事实，经过 Galois 对应变成群里的一条代数事实，再经过可解性判据变成「无根式解」。这条链子上的每一环都可检验，这正是入口题 (5) 所要求的「可写下来的证明」。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 把 $$\operatorname{Gal}(\mathbb{Q}(\sqrt2)/\mathbb{Q})$$ 与 $$\operatorname{Gal}(\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q})$$ 的全部元素写出来，并各算 $$\lvert\operatorname{Gal}\rvert$$ 与 $$[K:\mathbb{Q}]$$。

**基2.** 判断 $$L=\mathbb{Q}(\sqrt2,\sqrt5)/\mathbb{Q}$$ 是否为 Galois 扩张；写出 $$\operatorname{Gal}(L/\mathbb{Q})$$（作为抽象群），并列出全部子群与对应的中间域。

**基3.** 设 $$L=\mathbb{Q}(\zeta_5)$$。写出 $$\operatorname{Gal}(L/\mathbb{Q})$$ 的阶与结构、它的全部子群、全部中间域，并指认唯一的二次子域。

**基4.** 举一个非 Galois 的有限扩张 $$L/K$$ 的例子，算出 $$\lvert\operatorname{Gal}(L/K)\rvert$$ 与 $$[L:K]$$ 并验证严格小于。再说明：在特征 $$0$$ 下，「不 Galois」为什么就等于「不正规」。

### 竞赛（本课目标难度）

**竞1.** 设 $$L/K$$ 是有限 Galois 扩张，$$G=\operatorname{Gal}(L/K)$$ 且 $$\lvert G\rvert=p^2$$（$$p$$ 素数）。证明：存在中间域 $$E$$ 使 $$[E:K]=p$$。

**竞2.** 证明 $$\mathbb{Q}(\zeta_7)$$ 有唯一的二次子域，并确定它是 $$\mathbb{Q}(\sqrt{-7})$$。

**竞3.** 设 $$f(t)=t^4-2$$，$$L$$ 为其分裂域。求 $$[L:\mathbb{Q}]$$ 与 $$\operatorname{Gal}(L/\mathbb{Q})$$（给出生成元与关系），并列出全部中间域及其次数。

**竞4.** 设 $$f\in\mathbb{Q}[t]$$ 不可约，$$\deg f=p$$ 为素数，且 $$f$$ 在 $$\mathbb{R}$$ 中恰有 $$p-2$$ 个根。证明 $$\operatorname{Gal}(f)=S_p$$；并用它独立地推出 $$t^5-6t+3$$ 不可根式求解。

**竞5.** 设 $$n\ge2$$，$$\sigma_a\in\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})$$ 由 $$\sigma_a(\zeta_n)=\zeta_n^{\,a}$$ 定义。证明 $$\sigma_a$$ 的阶等于 $$a$$ 在 $$(\mathbb{Z}/n)^{\times}$$ 中的阶。并由此求出 $$\operatorname{Gal}(\mathbb{Q}(\zeta_8)/\mathbb{Q})$$ 的结构与 $$\mathbb{Q}(\zeta_8)$$ 的全部中间域。

### 研究（通向下一章）

**研1.** 设 $$f\in\mathbb{Q}[t]$$ 不可约、$$\deg f=5$$。
(a) 证明 $$\operatorname{Gal}(f)$$ 在五根上传递，从而 $$5\mid\lvert\operatorname{Gal}(f)\rvert$$，故含 5-循环。
(b) 设 $$\Delta$$ 为判别式。证明 $$\operatorname{Gal}(f)\subseteq A_5\iff\sqrt\Delta\in\mathbb{Q}$$。
(c) 利用 (a)(b)，列出 $$S_5$$ 的全部传递子群（可以共轭归类），并由此给出「五次方程何时可根式解」的完整判据。

**研2.** 证明 Kronecker–Weber 定理的二次情形：$$\mathbb{Q}$$ 的每个二次扩张都含于某个分圆域 $$\mathbb{Q}(\zeta_n)$$。

### 解答 (Solutions)

**解 基1.** **（i）** $$L_1=\mathbb{Q}(\sqrt2)$$：任何 $$\sigma\in\operatorname{Gal}(L_1/\mathbb{Q})$$ 满足 $$\sigma(\sqrt2)^2=2$$，故 $$\sigma(\sqrt2)=\pm\sqrt2$$；而 $$\{1,\sqrt2\}$$ 是 $$\mathbb{Q}$$-基，故 $$\sigma$$ 由 $$\sigma(\sqrt2)$$ 唯一决定。于是恰有两个元素：恒等映射，以及 $$\sigma:\sqrt2\mapsto-\sqrt2$$（自同构由生成元的像按域运算唯一延拓，故只需确认它保加法与乘法）。故

$$\lvert\operatorname{Gal}(L_1/\mathbb{Q})\rvert=2=[L_1:\mathbb{Q}],\qquad \operatorname{Gal}\cong\mathbb{Z}/2.$$

**（ii）** $$M=\mathbb{Q}(\sqrt[3]{2})$$：任何 $$\sigma$$ 满足 $$\sigma(\sqrt[3]2)^3=2$$，故 $$\sigma(\sqrt[3]2)$$ 是 $$t^3-2$$ 在 $$M$$ 中的根。但 $$M\subseteq\mathbb{R}$$，而 $$t^3-2$$ 在 $$\mathbb{R}$$ 中的根只有 $$\sqrt[3]2$$ 一个（函数 $$t\mapsto t^3-2$$ 严格递增），故 $$\sigma(\sqrt[3]2)=\sqrt[3]2$$，$$\sigma=\mathrm{id}$$（因为 $$\sqrt[3]2$$ 生成 $$M$$）。而 $$[M:\mathbb{Q}]=3$$（Eisenstein，$$p=2$$）。故

$$\lvert\operatorname{Gal}(M/\mathbb{Q})\rvert=1<3=[M:\mathbb{Q}].$$

**讨论**：两例的次数与「对称数」分别是 $$(2,2)$$ 与 $$(3,1)$$。差别在于 $$t^3-2$$ 的另两个根不在 $$M$$ 内——这正是非正规性的定义。

**解 基2.** **（i）是否 Galois。** $$L=\mathbb{Q}(\sqrt2,\sqrt5)$$ 是 $$(t^2-2)(t^2-5)$$ 的分裂域（该多项式的四个根 $$\pm\sqrt2,\pm\sqrt5$$ 全在 $$L$$ 中，且 $$L$$ 由它们生成），特征 $$0$$ 下该多项式可分，故 $$L/\mathbb{Q}$$ 是 Galois 扩张。又由塔定理与 $$\sqrt5\notin\mathbb{Q}(\sqrt2)$$（若 $$\sqrt5=a+b\sqrt2$$，平方得 $$5=a^2+2b^2+2ab\sqrt2$$，故 $$ab=0$$，两种情形都立刻矛盾），得 $$[L:\mathbb{Q}]=4$$。故 $$\lvert\operatorname{Gal}(L/\mathbb{Q})\rvert=4$$（定理 3.9）。

**（ii）群。** 任何 $$\sigma$$ 满足 $$\sigma(\sqrt2)=\pm\sqrt2,\ \sigma(\sqrt5)=\pm\sqrt5$$，且由四个基元素 $$1,\sqrt2,\sqrt5,\sqrt{10}$$ 决定，故至多四个；结合 $$\lvert\operatorname{Gal}\rvert=4$$ 可知恰是四个：

$$\mathrm{id},\quad \sigma_2:\sqrt2\mapsto-\sqrt2,\ \sqrt5\mapsto\sqrt5,\quad \sigma_5:\sqrt2\mapsto\sqrt2,\ \sqrt5\mapsto-\sqrt5,\quad \sigma_{10}=\sigma_2\sigma_5.$$

每个非单位元的平方为恒等，且群交换，故

$$\operatorname{Gal}(L/\mathbb{Q})\cong\mathbb{Z}/2\times\mathbb{Z}/2.$$

**（iii）子群与中间域。** 子群共五个（一维子空间三个 + $$\{1\}$$ + 全体），对应关系如下：

| 子群 | 固定域 | $$[E:\mathbb{Q}]$$ |
|---|---|---|
| $$\{1\}$$ | $$L=\mathbb{Q}(\sqrt2,\sqrt5)$$ | $$4$$ |
| $$\langle\sigma_2\rangle$$ | $$\mathbb{Q}(\sqrt2)$$ | $$2$$ |
| $$\langle\sigma_5\rangle$$ | $$\mathbb{Q}(\sqrt5)$$ | $$2$$ |
| $$\langle\sigma_{10}\rangle$$ | $$\mathbb{Q}(\sqrt{10})$$ | $$2$$ |
| $$G$$ | $$\mathbb{Q}$$ | $$1$$ |

以 $$\langle\sigma_{10}\rangle$$ 一行核对：$$\sigma_{10}(\sqrt2)=-\sqrt2,\ \sigma_{10}(\sqrt5)=-\sqrt5$$，故 $$\sigma_{10}(\sqrt{10})=\sqrt{10}$$，故 $$\mathbb{Q}(\sqrt{10})\subseteq L^{\langle\sigma_{10}\rangle}$$；两边次数都是 $$[G:H]=2$$，故相等。

**解 基3.** $$n=5$$，$$\zeta=\zeta_5=e^{2\pi i/5}$$。由定理 3.15，$$L/\mathbb{Q}$$ 是 Galois 扩张且

$$\operatorname{Gal}(L/\mathbb{Q})\cong(\mathbb{Z}/5)^{\times}=\{1,2,3,4\}\cong\mathbb{Z}/4,\qquad \lvert\operatorname{Gal}\rvert=4=[L:\mathbb{Q}]=\varphi(5).$$

（$$(\mathbb{Z}/5)^\times$$ 是 $$4$$ 阶群；$$4$$ 阶群有 $$\mathbb{Z}/4$$ 与 $$(\mathbb{Z}/2)^2$$ 两种，但 $$\mathbb{Z}/5$$ 的单位群是循环群，生成元取 $$2$$：$$2^1=2,2^2=4,2^3=3,2^4=1$$。）

**子群**（$$\mathbb{Z}/4$$ 只有两个真子群）：$$\{1\}$$、$$\{1,4\}=\{1,-1\}$$（阶 $$2$$）、$$\mathbb{Z}/4$$ 全体。故**中间域恰有三个**：

- $$H=\mathbb{Z}/4$$：固定域 $$\mathbb{Q}$$；
- $$H=\{1\}$$：固定域 $$L$$；
- $$H=\{1,-1\}$$：对应 $$\sigma_{-1}:\zeta\mapsto\zeta^{-1}$$，故固定域是 $$\mathbb{Q}(\zeta+\zeta^{-1})$$，次数 $$[\mathbb{Z}/4:\{1,-1\}]=2$$。

**唯一二次子域。** 由上，它是 $$\mathbb{Q}(\zeta+\zeta^{-1})=\mathbb{Q}(2\cos\frac{2\pi}{5})$$。令 $$\eta=\zeta+\zeta^{-1}$$，用 $$\zeta^2+\zeta+1+\zeta^{-1}+\zeta^{-2}=0$$（两边乘 $$\zeta^2$$ 得 $$\zeta^4+\zeta^3+\zeta^2+\zeta+1=0$$）得

$$\eta^2+\eta-1=0\ \Longrightarrow\ \eta=\frac{-1\pm\sqrt5}{2},$$

判别式 $$1+4=5$$，故 $$\mathbb{Q}(\eta)=\mathbb{Q}(\sqrt5)$$。所以唯一的二次子域是 $$\mathbb{Q}(\sqrt5)$$——这也与「$$\mathbb{Q}(\zeta_p)$$ 的唯一二次子域是 $$\mathbb{Q}(\sqrt{p^*})$$，$$p=5$$ 时 $$p^*=(-1)^2\cdot5=5$$」一致。

**解 基4.** **例子**：取 $$K=\mathbb{Q}$$、$$L=\mathbb{Q}(\sqrt[3]{2})$$。由基1，$$\lvert\operatorname{Gal}(L/K)\rvert=1<3=[L:K]$$，故不 Galois。

**为什么「不 Galois $$=$$ 不正规」**：Galois 扩张的定义是「可分 + 正规」。在特征 $$0$$ 的基域上，每个代数元素都可分（注 3.4：若极小多项式 $$m$$ 不可分，则 $$\gcd(m,m')$$ 是它的非平凡因子，与不可约性矛盾）。所以特征 $$0$$ 下

$$L/K\ \text{不 Galois}\iff L/K\ \text{不正规}.$$

在本例中可具体验出：不可约多项式 $$t^3-2\in\mathbb{Q}[t]$$ 在 $$L$$ 中有根 $$\sqrt[3]2$$，但另两根 $$\sqrt[3]2\,\omega,\sqrt[3]2\,\omega^2$$ 非实、不在 $$L\subseteq\mathbb{R}$$ 中，故 $$L/\mathbb{Q}$$ 不正规。

**解 竞1.** **思路**：先证明 $$p^2$$ 阶群必交换，再找出一个指数 $$p$$ 的子群，最后用定理 3.11 (iv) 把指数换成次数。

**第一步：$$p^2$$ 阶群是交换群。** 由类方程

$$\lvert G\rvert=\lvert Z(G)\rvert+\sum_i[G:C_G(x_i)],$$

（求和跑遍非中心共轭类代表，每项是 $$p$$ 的正幂且 $$>1$$，因而是 $$p$$ 的倍数），得 $$p^2\equiv\lvert Z(G)\rvert\pmod p$$；又 $$p$$-群中心非平凡（第 02 章），故 $$\lvert Z(G)\rvert\in\{p,p^2\}$$。若 $$\lvert Z(G)\rvert=p$$，则 $$G/Z(G)$$ 是 $$p$$ 阶循环群，而「$$G/Z(G)$$ 循环 $$\Rightarrow$$ $$G$$ 交换」是标准事实（取 $$\bar g$$ 生成 $$G/Z(G)$$，任意 $$x=g^az,\ y=g^bw$$ 且 $$z,w\in Z(G)$$ 给出 $$xy=g^{a+b}zw=yx$$），这与 $$\lvert Z(G)\rvert<\lvert G\rvert$$ 矛盾。故 $$G$$ 交换。

**第二步：找指数 $$p$$ 的子群。** 交换 $$p$$ 群（由第一步，$$G$$ 交换）只有两种结构：$$G\cong\mathbb{Z}/p^2$$ 或 $$G\cong(\mathbb{Z}/p)^2$$。

- 若 $$G=\langle g\rangle\cong\mathbb{Z}/p^2$$：取 $$H=\langle g^{p}\rangle$$，这是 $$p$$ 阶子群，$$[G:H]=p^2/p=p$$；
- 若 $$G\cong(\mathbb{Z}/p)^2$$：取任一非零线性泛函 $$\lambda:G\to\mathbb{Z}/p$$（存在，因 $$G$$ 是 $$\mathbb{F}_p$$-向量空间），令 $$H=\ker\lambda$$，则 $$\lvert H\rvert=\lvert G\rvert/p=p$$，$$[G:H]=p$$。

**第三步：翻译。** 令 $$E=L^H$$。由 Galois 对应（定理 3.11 (iv)），

$$[E:K]=[G:H]=p.$$

**附注**：因为 $$G$$ 交换，每个 $$H$$ 都正规，故这个 $$E/K$$ 还是 Galois 扩张，且 $$\operatorname{Gal}(E/K)\cong G/H\cong\mathbb{Z}/p$$。**关键 leap**：$$p^2$$ 阶群的分类（交换性）是纯群论，而「指数变成次数」这一步是 Galois 对应提供的——两个世界在这里对接。

**解 竞2.** 记 $$\zeta=\zeta_7$$。

**第一步：群。** 由定理 3.15，$$\operatorname{Gal}(\mathbb{Q}(\zeta_7)/\mathbb{Q})\cong(\mathbb{Z}/7)^{\times}\cong\mathbb{Z}/6$$（$$(\mathbb{Z}/7)^\times$$ 是 $$6$$ 阶群；取生成元 $$3$$：$$3,2,6,4,5,1$$，故确实循环）。

**第二步：二次子域 $$\leftrightarrow$$ 指数 $$2$$ 的子群。** 由定理 3.11 (iv)，$$[E:\mathbb{Q}]=2\iff[G:\operatorname{Gal}(L/E)]=2$$。$$\mathbb{Z}/6$$ 是循环群，对每个整除 $$6$$ 的阶恰有一个子群；指数 $$2$$ 的子群是唯一的 $$3$$ 阶子群。因此**二次子域唯一**。

**第三步：把它算出来。** $$3$$ 阶子群是 $$\mathbb{Z}/6$$ 的**平方**子群（$$G/G^2$$ 是 $$2$$ 阶群），即

$$\{1,2,4\}\ (\subseteq(\mathbb{Z}/7)^\times).$$

取 $$\alpha=\zeta+\zeta^2+\zeta^4\in\mathbb{Q}(\zeta_7)$$。任一 $$\sigma_a\ (a\in\{1,2,4\})$$ 只是置换集合 $$\{\zeta,\zeta^2,\zeta^4\}$$（乘以 $$2$$ 或 $$4$$ 视为模 $$7$$）故固定 $$\alpha$$；反之若 $$\sigma_a$$ 固定 $$\alpha$$，则（用下面会算出的 $$\alpha$$ 的二次极小多项式）$$a\in\{1,2,4\}$$。故

$$\mathbb{Q}(\alpha)=L^{\{1,2,4\}}=[\text{那个唯一的二次子域}].$$

**第四步：算 $$\alpha$$ 的极小多项式。** 记 $$\bar\alpha=\zeta^3+\zeta^5+\zeta^6$$（非剩余之和）。而 $$\{\zeta,\dots,\zeta^6\}$$ 是全部非 $$1$$ 的 $$7$$ 次单位根，其和为 $$-1$$，故

$$\alpha+\bar\alpha=-1.$$

又逐项展开（$$\zeta^7=1$$，$$\zeta^{k}=\zeta^{k-7}$$）：

$$\alpha\bar\alpha=(\zeta+\zeta^2+\zeta^4)(\zeta^3+\zeta^5+\zeta^6)=\zeta^4+\zeta^6+1+\zeta^5+1+\zeta+1+\zeta^2+\zeta^3=(\zeta+\cdots+\zeta^6)+3=-1+3=2.$$

于是 $$\alpha,\bar\alpha$$ 是 $$t^2-(\alpha+\bar\alpha)t+\alpha\bar\alpha=t^2+t+2$$ 的两根。该二次式的判别式为 $$1-8=-7$$，故

$$\alpha=\frac{-1\pm\sqrt{-7}}{2},\qquad \mathbb{Q}(\alpha)=\mathbb{Q}(\sqrt{-7}).$$

**结论**：$$\mathbb{Q}(\zeta_7)$$ 的唯一二次子域是 $$\mathbb{Q}(\sqrt{-7})$$。**关键 leap**：把「二次子域」翻译成「指数 $$2$$ 的子群」，再用循环群「每个阶只有一个子群」这一唯一性事实——群论的一次性回答替代了对域的直接枚举。

**解 竞3.** 记 $$\alpha=\sqrt[4]{2}$$，四根为 $$\pm\alpha,\ \pm i\alpha$$。

**（1）分裂域与次数。** $$L=\mathbb{Q}(\alpha,i)$$。$$t^4-2$$ 在 $$\mathbb{Q}$$ 上不可约（Eisenstein，$$p=2$$：$$2\mid 0,0,0,-2$$ 而 $$2^2\nmid-2$$），故 $$[\mathbb{Q}(\alpha):\mathbb{Q}]=4$$；又 $$i\notin\mathbb{Q}(\alpha)\subseteq\mathbb{R}$$，故 $$[L:\mathbb{Q}(\alpha)]=2$$，塔定理给 $$[L:\mathbb{Q}]=8$$。

**（2）Galois 群。** 定义

$$\sigma:\ \alpha\mapsto i\alpha,\ i\mapsto i;\qquad \tau:\ \alpha\mapsto\alpha,\ i\mapsto-i.$$

两者都由生成元的像唯一决定（$$\sigma(\alpha)^4=i^4\alpha^4=2$$、$$\sigma(i)^2=1$$，故它们确实是域自同构），$$\sigma$$ 的阶为 $$4$$，$$\tau$$ 的阶为 $$2$$，且

$$\tau\sigma\tau^{-1}=\sigma^{-1}\quad(\text{在 }\alpha\text{ 上}:\ \tau\sigma\tau(\alpha)=\tau\sigma(\alpha)=\tau(i\alpha)=(-i)\alpha=-i\alpha=\sigma^{-1}(\alpha)\ \checkmark;\ \text{在 }i\text{ 上两者都是恒等}).$$

于是 $$\langle\sigma,\tau\rangle$$ 是 $$8$$ 阶二面体群，且 $$\lvert G\rvert=8=[L:\mathbb{Q}]$$，故

$$\operatorname{Gal}(L/\mathbb{Q})=\langle\sigma,\tau\mid\sigma^4=\tau^2=1,\ \tau\sigma\tau=\sigma^{-1}\rangle\cong D_8.$$

**（3）全部中间域。** $$D_8$$ 有 $$10$$ 个子群，故有 $$10$$ 个中间域。

*退化情形*：$$\{1\}\leftrightarrow L$$（次数 $$8$$），$$D_8\leftrightarrow\mathbb{Q}$$（次数 $$1$$）。

*次数 $$2$$（对应 $$3$$ 个阶 $$4$$ 子群）*：

- $$H=\langle\sigma\rangle$$（$$\sigma$$ 固定 $$i$$），故 $$L^{\langle\sigma\rangle}$$ 含 $$i$$，次数 $$[G:H]=2$$ 故等于 $$\mathbb{Q}(i)$$；
- $$H=\langle\sigma^2,\tau\rangle$$（两者都固定 $$\alpha^2=\sqrt2$$）：$$L^{H}=\mathbb{Q}(\sqrt2)$$；
- $$H=\langle\sigma^2,\sigma\tau\rangle$$（两者都固定 $$i\alpha^2=i\sqrt2$$）：$$L^{H}=\mathbb{Q}(i\sqrt2)=\mathbb{Q}(\sqrt{-2})$$。

*次数 $$4$$（对应 $$5$$ 个阶 $$2$$ 子群）*：

- $$\langle\sigma^2\rangle$$（$$\alpha\mapsto-\alpha,\ i\mapsto i$$），固定域 $$\mathbb{Q}(i,\sqrt2)$$；
- $$\langle\tau\rangle$$（固定 $$\alpha$$），固定域 $$\mathbb{Q}(\alpha)=\mathbb{Q}(\sqrt[4]{2})$$；
- $$\langle\sigma^2\tau\rangle$$（$$\alpha\mapsto-\alpha,\ i\mapsto-i$$）固定 $$\alpha i$$，固定域 $$\mathbb{Q}(i\sqrt[4]{2})$$；
- $$\langle\sigma\tau\rangle$$（$$\alpha\mapsto i\alpha,\ i\mapsto-i$$）：$$\sigma\tau(\alpha(1+i))=i\alpha(1-i)=\alpha(1+i)$$，固定域 $$\mathbb{Q}(\alpha(1+i))$$；
- $$\langle\sigma^3\tau\rangle$$（$$\alpha\mapsto-i\alpha,\ i\mapsto-i$$）：$$\sigma^3\tau(\alpha(1-i))=-i\alpha(1+i)=\alpha(1-i)$$，固定域 $$\mathbb{Q}(\alpha(1-i))$$。

**核对**：三个二次域 $$\mathbb{Q}(i),\mathbb{Q}(\sqrt2),\mathbb{Q}(\sqrt{-2})$$ 两两不同，与三个阶 $$4$$ 子群一一对应；$$10=1+1+3+5$$ 与子群计数吻合。特别地 $$\langle\sigma\rangle\trianglelefteq D_8$$（阶 $$4$$ 子群），故 $$\mathbb{Q}(i)/\mathbb{Q}$$ 是 Galois 扩张。

**解 竞4.** **（1）含对换。** $$f$$ 恰有 $$p-2$$ 个实根，其余 $$2$$ 个是非实根且互为共轭（实系数多项式的根成共轭对）。复共轭是分裂域 $$L$$ 的一个 $$\mathbb{Q}$$-自同构（$$L$$ 由 $$f$$ 的根生成，且共轭置换根），它固定 $$p-2$$ 个实根、交换那对共轭复根，故是根集上的一个**对换**。

**（2）含 $$p$$-循环。** $$f$$ 不可约 $$\Rightarrow$$ $$G=\operatorname{Gal}(f)$$ 在 $$p$$ 个根上传递（注 3.9）$$\Rightarrow$$ $$p\mid\lvert G\rvert$$ 由 Cauchy 定理，$$G$$ 含 $$p$$ 阶元，它在 $$p$$ 个字母上只能是 $$p$$-循环。

**（3）标准引理：** 设 $$p$$ 素数，$$H\le S_p$$ 传递且含对换与 $$p$$-循环，则 $$H=S_p$$。证明与题 5 第 (4) 步完全相同：共轭使 $$p$$-循环为 $$\sigma=(1\,2\,\cdots\,p)$$，对换为 $$\tau=(a\,b)$$，则 $$\sigma^{b-a}\tau\sigma^{-(b-a)}=(b,\ 2b-a)$$ 与 $$\tau$$ 共享点 $$b$$，乘积是三轮换；$$H$$ 传递且次数为素数故本原；由 Jordan 定理 $$A_p\subseteq H$$；$$A_p$$ 不含对换，故 $$H=S_p$$。

由 (1)(2)(3)：$$\operatorname{Gal}(f)=S_p$$。

**（4）应用到 $$t^5-6t+3$$。** 由第 5 题 (1)(2)（或直接计算）：$$\mathbb{Q}[t]$$ 中的不可约性来自模 $$2$$ 分解 $$t^5+1=(t+1)\Phi_5$$ 与 $$\Phi_5$$ 在 $$\mathbb{F}_2$$ 上不可约；恰有三个实根来自 $$f'=5t^4-6$$ 的临界点分析。取 $$p=5$$，由 (1)(2)(3) 得 $$\operatorname{Gal}(f)=S_5$$。再由定理 3.18（$$S_5$$ 不可解）与定理 3.17（根式可解 $$\iff$$ Galois 群可解），$$f$$ 不可根式求解。

**关键 leap**：把「根的实/复分布」这种**分析**信息（复共轭的几何作用）翻译成群里的置换型（对换），再把「不可约」翻译成传递性（5-循环）。分析信息 $$\to$$ 置换型 $$\to$$ 群 $$\to$$ 可解性，这条链是 Galois 理论的标准套路。

**解 竞5.** **（1）阶的计算。** 由 $$\sigma_a(\zeta_n)=\zeta_n^{\,a}$$ 用归纳得 $$\sigma_a^{\,k}(\zeta_n)=\zeta_n^{\,a^k}$$。因为 $$\zeta_n$$ 生成 $$\mathbb{Q}(\zeta_n)$$（它是单扩张），$$\sigma_a^{\,k}=\mathrm{id}\iff\zeta_n^{\,a^k}=\zeta_n\iff n\mid(a^k-1)\iff a^k\equiv1\pmod n$$。故 $$\operatorname{ord}(\sigma_a)=\min\{k\ge1:\ a^k\equiv1\pmod n\}=a$$ 在 $$(\mathbb{Z}/n)^\times$$ 中的阶。

**（2）$$\mathbb{Q}(\zeta_8)$$。** $$(\mathbb{Z}/8)^\times=\{1,3,5,7\}$$，且每个元素的平方都是 $$1$$（$$3^2=9\equiv1,\ 5^2\equiv1,\ 7^2\equiv1$$），故由 (1) 每个 $$\sigma_a\ (a\ne1)$$ 都是对合。于是

$$\operatorname{Gal}(\mathbb{Q}(\zeta_8)/\mathbb{Q})\cong(\mathbb{Z}/8)^{\times}\cong\mathbb{Z}/2\times\mathbb{Z}/2,\qquad [\mathbb{Q}(\zeta_8):\mathbb{Q}]=\varphi(8)=4.$$

**（3）全部子群与中间域。** $$(\mathbb{Z}/2)^2$$ 的五个子群是 $$\{1\}$$、$$\langle3\rangle,\langle5\rangle,\langle7\rangle$$（三个阶 $$2$$ 子群）、全体。先识别域本身：$$\zeta_8=e^{\pi i/4}=\frac{1+i}{\sqrt2}$$ 给出 $$\zeta_8^2=i$$、$$\zeta_8+\zeta_8^{-1}=\sqrt2$$，故 $$\mathbb{Q}(\zeta_8)=\mathbb{Q}(i,\sqrt2)$$。中间域共五个：

- $$\{1\}\leftrightarrow\mathbb{Q}(\zeta_8)$$（次数 $$4$$），全体 $$\leftrightarrow\mathbb{Q}$$（次数 $$1$$）；
- $$\langle\sigma_3\rangle$$：$$\sigma_3(\zeta_8)=i\zeta_8$$，故 $$\sigma_3(i)=-i,\ \sigma_3(\sqrt2)=-\sqrt2$$，固定 $$i\sqrt2$$，固定域 $$\mathbb{Q}(\sqrt{-2})$$；
- $$\langle\sigma_5\rangle$$：$$\sigma_5(\zeta_8)=-\zeta_8$$，故 $$\sigma_5(\sqrt2)=-\sqrt2$$ 而 $$\sigma_5(i)=i$$，固定域 $$\mathbb{Q}(i)$$；
- $$\langle\sigma_7\rangle$$：$$\sigma_7(\zeta_8)=\zeta_8^{-1}$$，故 $$\sigma_7(\sqrt2)=\sqrt2$$ 而 $$\sigma_7(i)=-i$$，固定域 $$\mathbb{Q}(\sqrt2)$$。

**核对**：三个二次域 $$\mathbb{Q}(i),\mathbb{Q}(\sqrt2),\mathbb{Q}(\sqrt{-2})$$ 正是 $$\mathbb{Q}(i,\sqrt2)$$ 的三个二次子域，且因为 $$G$$ 交换、每个子群正规，它们全都是 $$\mathbb{Q}$$ 的 Galois 扩张（定理 3.11 (4)）。这与「$$\mathbb{Q}(\zeta_8)$$ 是 $$\mathbb{Q}$$ 的 Abel 扩张」这一事实一致。

**解 研1.**

**（a）传递性与 $$5\mid\lvert G\rvert$$。** $$f$$ 在 $$\mathbb{Q}$$ 上不可约，由注 3.9，$$G=\operatorname{Gal}(f)$$ 在根集上的作用传递且 $$\deg f\mid\lvert G\rvert$$，即 $$5\mid\lvert G\rvert$$（注 3.9 用的是轨道-稳定子定理与 $$[L:K(\alpha_i)]=[L:K]/[K(\alpha_i):K]$$，不依赖 $$f$$ 的具体形状）。由 Cauchy 定理，$$G$$ 含一个 $$5$$ 阶元；$$5$$ 阶元在五个字母上恰是 5-循环。

**（b）判别式判据。** 由定理 3.13：$$\Delta=\prod_{i<j}(\alpha_i-\alpha_j)^2\in\mathbb{Q}$$，且

$$\operatorname{Gal}(f)\subseteq A_5\iff\sqrt\Delta=\prod_{i<j}(\alpha_i-\alpha_j)\in\mathbb{Q}\iff\Delta\ \text{是}\ \mathbb{Q}\ \text{中的平方}.$$

（证明已在定理 3.13：$$\sigma(\sqrt\Delta)=\operatorname{sgn}(\sigma)\sqrt\Delta$$，故 $$\sqrt\Delta$$ 被全群固定当且仅当所有 $$\sigma$$ 都是偶置换。）

**（c）$$S_5$$ 的传递子群分类。** 设 $$H\le S_5$$ 传递。由 (a) 的推理，$$5\mid\lvert H\rvert$$，故含 5-循环 $$\sigma$$；共轭后设 $$\sigma=(1\,2\,3\,4\,5)$$。$$\sigma$$ 的循环群在 $$S_5$$ 中的正规化子为

$$N=N_{S_5}(\langle\sigma\rangle)=\langle\sigma\rangle\rtimes\langle\beta\rangle,\qquad \beta:(1\,2\,3\,4\,5)\mapsto(1\,3\,5\,2\,4)\ (\text{即}\ i\mapsto2i\bmod5),$$

它是 $$\mathbb{Z}/5\rtimes\mathbb{Z}/4$$，阶为 $$5\cdot4=20$$（因为 $$5$$ 阶子群共有 $$24/4=6$$ 个，故每个的正规化子阶为 $$120/6=20$$），记作 $$F_{20}$$。

- **情形一：$$H\le F_{20}$$。** $$F_{20}$$ 中阶被 $$5$$ 整除的子群（再由传递性筛选）只有 $$\mathbb{Z}/5$$、$$\mathbb{Z}/5\rtimes\mathbb{Z}/2\cong D_5$$（阶 $$10$$）、$$F_{20}$$（阶 $$20$$）三个，故 $$H\in\{\mathbb{Z}/5,\ D_5,\ F_{20}\}$$；
- **情形二：$$H\not\le F_{20}$$。** 此时存在 $$h\in H$$ 使 $$h\sigma h^{-1}\notin\langle\sigma\rangle$$，于是 $$H$$ 在有序点对上传递，即 **2-传递**；而 $$S_5$$ 的 2-传递子群只有 $$F_{20},A_5,S_5$$（标准分类：2-传递群必本原，含 $$5$$-循环时由 Jordan 定理给出 $$A_5$$）。结合 $$H\not\le F_{20}$$ 得 $$H\in\{A_5,S_5\}$$。

**结论**：$$S_5$$ 的传递子群（共轭意义下）恰五个：

$$\mathbb{Z}/5,\quad D_5=\mathbb{Z}/5\rtimes\mathbb{Z}/2,\quad F_{20}=\mathbb{Z}/5\rtimes\mathbb{Z}/4,\quad A_5,\quad S_5.$$

相应的阶为 $$5,10,20,60,120$$。

**（d）五次方程的完整判据。** 对不可约的五次 $$f$$，$$\operatorname{Gal}(f)$$ 必是上述五个之一。其中可解性（第 04 章的判据）：$$\mathbb{Z}/5,D_5,F_{20}$$ 可解（它们的导列分别在一步或两步内降到 $$\{1\}$$：$$F_{20}$$ 的导子群是 $$\mathbb{Z}/5$$，再下一步为 $$\{1\}$$）；$$A_5$$、$$S_5$$ 不可解（定理 3.18）。由定理 3.17，

$$\boxed{f\ \text{根式可解}\iff\operatorname{Gal}(f)\in\{\mathbb{Z}/5,\ D_5,\ F_{20}\}.}$$

进一步，由 (b)：$$\Delta$$ 是平方 $$\iff$$ $$\operatorname{Gal}(f)\subseteq A_5$$，此时 $$\operatorname{Gal}(f)\in\{\mathbb{Z}/5,\ D_5,\ A_5\}$$。所以**不可根式解**的五次方程分两类：

- **$$S_5$$ 型**：$$\Delta$$ 非平方（例如 $$t^5-6t+3$$，$$\Delta$$ 不是平方；复共轭给出的对换是奇置换）；
- **$$A_5$$ 型**：$$\Delta$$ 是平方，而群既不是 $$\mathbb{Z}/5$$ 也不是 $$D_5$$。

从「系数空间计数」的启发式看，$$A_5$$ 型更少见：$$\Delta$$ 是平方是系数上的**一个**代数条件（一个超曲面），而通有的五次多项式给出的群是 $$S_5$$。（这里只提供直觉：严格的比例陈述属于几何 Galois 理论，见第 40 章。）

**（e）接下一章。** 上面 (d) 只列出「哪些群能出现」；反过来问「哪些群能实现为 $$\mathbb{Q}$$ 上多项式的 Galois 群」，就是**逆 Galois 问题 (inverse Galois problem)**——它是第 40 章的第一站。$$\blacksquare$$

**解 研2.** **思路**：把 $$\mathbb{Q}(\sqrt d)$$ 拆成「基本块」（$$\mathbb{Q}(i)$$、$$\mathbb{Q}(\sqrt2)$$、$$\mathbb{Q}(\sqrt{-2})$$、以及奇素数对应的 $$\mathbb{Q}(\sqrt{p^*})$$），每一块都装在一个分圆域里，再用合成（定理 3.12）与 $$\mathbb{Q}(\zeta_m)\mathbb{Q}(\zeta_n)=\mathbb{Q}(\zeta_{\mathrm{lcm}(m,n)})$$ 打包。

**第一步：四个基本块。**

(i) $$\mathbb{Q}(i)=\mathbb{Q}(\sqrt{-1})=\mathbb{Q}(\zeta_4)$$。

(ii) $$\mathbb{Q}(\sqrt2)\subseteq\mathbb{Q}(\zeta_8)$$：由 $$\zeta_8+\zeta_8^{-1}=2\cos\frac{\pi}{4}=\sqrt2$$。

(iii) $$\mathbb{Q}(\sqrt{-2})\subseteq\mathbb{Q}(\zeta_8)$$：由 $$\zeta_8-\zeta_8^{-1}=2i\sin\frac{\pi}{4}=i\sqrt2$$，其平方是 $$-2$$。

(iv) 对奇素数 $$p$$：$$\mathbb{Q}(\sqrt{p^*})\subseteq\mathbb{Q}(\zeta_p)$$，其中 $$p^*=(-1)^{(p-1)/2}p$$。证明如下。令

$$\alpha=\sum_{a\in QR}\zeta_p^{\,a},\qquad \bar\alpha=\sum_{a\in QNR}\zeta_p^{\,a},$$

其中 $$QR$$、$$QNR$$ 分别是模 $$p$$ 的二次剩余与非剩余。因为 $$QR\cup QNR=\{1,\dots,p-1\}$$ 而 $$\sum_{a=1}^{p-1}\zeta_p^a=-1$$（等比求和），得

$$\alpha+\bar\alpha=-1.$$

再由二次 Gauss 和的标准恒等式（把 $$\sum_a\bigl(\frac a p\bigr)\zeta_p^a$$ 平方并用特征的正交性展开）得

$$\alpha-\bar\alpha=\sum_{a=1}^{p-1}\Bigl(\frac{a}{p}\Bigr)\zeta_p^{\,a}=:g,\qquad g^2=p^*.$$

两式联立：

$$\alpha\bar\alpha=\frac{(\alpha+\bar\alpha)^2-(\alpha-\bar\alpha)^2}{4}=\frac{1-p^*}{4}.$$

于是 $$\alpha,\bar\alpha$$ 是 $$t^2+t+\frac{1-p^*}{4}$$ 的两根，该二次式的判别式是 $$1-4\cdot\frac{1-p^*}{4}=p^*$$，故

$$\mathbb{Q}(\alpha)=\mathbb{Q}\bigl(\sqrt{p^*}\bigr)\subseteq\mathbb{Q}(\zeta_p).$$

（$$p=7$$ 时正好回到竞 2：$$p^*=-7$$，$$\alpha\bar\alpha=\frac{1+7}{4}=2$$，方程 $$t^2+t+2=0$$，与那里的计算逐字一致。）

**第二步：合成。** 设 $$d$$ 平方自由，写 $$d=\varepsilon\cdot 2^{\delta}\cdot p_1\cdots p_k$$，其中 $$\varepsilon=\pm1$$、$$\delta\in\{0,1\}$$、$$p_i$$ 为互异奇素数。由第一步，$$\mathbb{Q}(\zeta_{p_i})\supseteq\mathbb{Q}(\sqrt{p_i^*})$$；再取 $$\mathbb{Q}(\zeta_4)$$（含 $$\sqrt{-1}$$）或 $$\mathbb{Q}(\zeta_8)$$（含 $$\sqrt2$$ 与 $$\sqrt{-2}$$）补齐 $$\pm1$$、$$\pm2$$ 的因子。合成域

$$M=\mathbb{Q}\bigl(\zeta_{p_1}\bigr)\cdots\mathbb{Q}\bigl(\zeta_{p_k}\bigr)\cdot\mathbb{Q}(\zeta_4\ \text{或}\ \zeta_8)=\mathbb{Q}(\zeta_N),\qquad N=\mathrm{lcm}\bigl(4\ \text{或}\ 8,\ p_1,\dots,p_k\bigr),$$

这里用了定理 3.12 与 $$\mathbb{Q}(\zeta_m)\mathbb{Q}(\zeta_n)=\mathbb{Q}(\zeta_{\mathrm{lcm}(m,n)})$$。此时 $$M$$ 含 $$\sqrt{-1},\sqrt{\pm2}$$ 与各 $$\sqrt{p_i^*}=\sqrt{\pm p_i}$$，而**二次域的合成仍是二次域**（$$K_1K_2=\mathbb{Q}(\sqrt{d_1},\sqrt{d_2})\supseteq\mathbb{Q}(\sqrt{d_1d_2})$$），故选出若干因子相乘、配合 $$\sqrt{-1}$$ 调整符号，即可得到 $$\sqrt d\in M$$：

$$\mathbb{Q}(\sqrt d)\subseteq M=\mathbb{Q}(\zeta_N).$$

（例：$$d=-15$$ 时 $$p_1=3,p_2=5$$，$$3^*=3,5^*=5$$，$$M=\mathbb{Q}(\zeta_4,\zeta_3,\zeta_5)=\mathbb{Q}(\zeta_{60})\ni\sqrt{-1}\cdot\sqrt3\cdot\sqrt5=\sqrt{-15}$$ ✓。）

**第三步：为什么这通向第 40 章。** 由定理 3.15，$$\operatorname{Gal}(\mathbb{Q}(\zeta_N)/\mathbb{Q})\cong(\mathbb{Z}/N)^\times$$ 交换，故分圆域的每个子域（包括 $$\mathbb{Q}(\sqrt d)$$）都是 $$\mathbb{Q}$$ 的 **Abel 扩张**。Kronecker–Weber 定理给出反过来的完整刻画：**$$\mathbb{Q}$$ 的每个有限 Abel 扩张都含于某个分圆域**。追问「把 $$\mathbb{Q}$$ 换成别的数域 $$F$$，该用什么对象参数化 $$F$$ 的 Abel 扩张」，就是**类域论**，也是第 40 章的起点——在那里 Galois 对应会升格为「射影有限群 ↔ 有限 étale 覆盖」。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**Takeaway 1（一副可查的字典）** 有限 Galois 扩张 $$L/K$$ 的中间域与 $$G=\operatorname{Gal}(L/K)$$ 的子群一一对应，包含关系反号；$$[L:E]=\lvert\operatorname{Gal}(L/E)\rvert$$，$$[E:K]=[G:\operatorname{Gal}(L/E)]$$；$$E/K$$ 是 Galois $$\iff$$ $$\operatorname{Gal}(L/E)\trianglelefteq G$$，此时 $$\operatorname{Gal}(E/K)\cong G/\operatorname{Gal}(L/E)$$。

**Takeaway 2（最快的筛子）** $$\lvert\operatorname{Gal}(L/K)\rvert=[L:K]$$ 是判定 Galois 扩张最顺手的工具；一般只有 $$\le$$，而缺口 $$[L^{\operatorname{Gal}(L/K)}:K]$$ 恰好度量了「不正规」。

**Takeaway 3（判别式是开关）** $$\sqrt\Delta\in K\iff\operatorname{Gal}(f)\subseteq A_n$$。它把「群落在 $$A_n$$ 还是 $$S_n$$」这个群论问题，换成了「这个数是不是平方」这个算术问题。

**Takeaway 4（根式可解 $$\iff$$ 可解群）** 开方对应循环扩张、域塔对应次正规列，于是 Abel–Ruffini 成为「$$S_n$$ 可解 $$\iff$$ $$n\le4$$」的一句话推论。同样次数 $$5$$，$$t^5-6t+3$$ 不可解（$$S_5$$），而 $$t^5-1$$ 的分裂域是 $$\mathbb{Q}(\zeta_5)$$、Galois 群 $$\mathbb{Z}/4$$，可解——Galois 理论比 Abel–Ruffini 多给的，正是「每个方程一条判据」。

**Takeaway 5（对称性的可计算化）** 本章可以概括成一句话：**对称可以被装进一个有限群，而这个群与原来的域携带同样的信息**。

### 显式收口：全书最短的一条线

**收口 1：第 38 章的扩域在这里获得「对称性」。** 第 38 章造出的 $$L$$ 只是一个装根的口袋：我们知道它是域、知道次数，却对内部结构一无所知。本章给它装上 $$\operatorname{Gal}(L/K)$$，并证明这两个对象携带**完全相同**的信息。「扩域」这个词从此同时装着域与群。

**收口 2：与第 10 / 35 章的同调代数并排。** 同调代数是一台**保序函子**：复形 $$\to$$ 链群 $$\to$$ 同调群，用 $$\ker/\operatorname{im}$$ 把几何信息压成不变量；Galois 对应是**另一种结构对应**，但它是**反变、反序的双射**——域越大群越小。两者共享同一个句型「一侧的结构 $$\cong$$ 另一侧的（不）变量」，差别只在保序还是反序。第 31–34 章的范畴语言正是描写这类对应的通用工具：Galois 对应可以写成「$$\{\text{中间域}\}^{\mathrm{op}}\cong\{\text{子群}\}$$」这样一个反变等价。

**收口 3：第 26 / 30 章的「双重覆盖与射影表示」在这里回响。** 那里 $$SU(2)\to SO(3)$$ 是二对一，量子态只能承载**射影表示**（差一个相位）；本章的 Galois 群则是「方程的对称群」的**忠实**版本：它作用在根集上，是根的置换，不带多余相位。并排看：物理的对称作用是射影的，代数的对称作用是置换的。第 40 章会用「基本群 / 覆叠空间 / Galois 群」的统一语言把这两种面貌收进同一个框架。

### 下一章

第 40 章《尾声：从 Galois 到现代数学》接住本章：**逆 Galois 问题**（哪些有限群能实现为 $$\mathbb{Q}$$ 上多项式的 Galois 群，即研 1 (d) 的另一半）、**Kronecker–Weber 与类域论**（研 2 推开的那扇门）、**Grothendieck 的 Galois 理论**（把「Galois 扩张」换成「有限 étale 覆盖」，把「Galois 群」换成射影有限基本群），以及这套语言如何在代数几何与数论中通用。

### 延伸阅读

- J. S. Milne, *Fields and Galois Theory* (v5.10)，第 3–5 章：Galois 对应的标准证明与根式可解性。
- D. S. Dummit, R. M. Foote, *Abstract Algebra* (3rd ed.)，§14.2（Galois 对应）、§14.7（根式可解，含 $$t^5-6t+3$$ 的例子）。
- И. Р. Шафаревич, *Основы алгебры*（Shafarevich，《代数基础》）：Galois 理论一章从 Abel–Ruffini 讲起，是俄罗斯数学物理高中的标准写法。
- Квант 1970 年代关于 Abel 与 Galois 的历史文章；J. S. Milne, *Lectures on Étale Cohomology*，§I.5（Grothendieck 的 Galois 理论）。


---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch38_扩域与代数数.md">← 第38章 扩域与代数数</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch40_尾声_从Galois到现代数学.md">第40章 尾声：从 Galois 到现代数学 →</a></div>
</div>
