---
layout: default
---

# 第29章: Hilbert 空间与内积结构·上：预备与直觉 (Hilbert Spaces and Inner Product Structure · Part I: Warm-up and Intuition)

> 配套深化: 见 第30章 Hilbert 空间与内积结构·下（完整推导），本章是它的具体铺垫，建议先读本章
> 专家依据: `_experts/analysis/functional-analysis.md` + `_experts/analysis/_SKILL.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

读第30章你会发现，从「内积公理」跳到 Cauchy–Schwarz 不等式，只用了一次"减去一个投影分量"的代数技巧；从"范数由内积诱导"跳到"平行四边形法则"，中间压缩了两次展开与合并；从"内积空间"跳到"完备化"，柯西列这个论证需要读者自己脑补一个具体的、真实"跑不出多项式空间"的例子；从"闭凸集"跳到"投影定理"，那个求导式 $$g'(0)=0$$ 的技巧看似突然。本章的任务只有一个：把这四处跳跃在一般证明登场之前，先用你能亲手算完的具体数字过一遍。

具体来说，本章准备好四件事：**(1)** Cauchy–Schwarz 不等式那个"减去投影"的技巧，先在 $$\mathbb{R}^2$$ 里、再在函数空间里各验证一遍，让你在看到一般证明之前已经知道这一步在算什么；**(2)** 平行四边形法则——用同一对向量在两种不同范数下算出"符合"与"不符合"两个截然不同的结果，亲眼看到"范数是否来自内积"是可以用一个恒等式检验的；**(3)** 柯西列与"完备"是什么意思——构造一列具体的多项式，算出相邻项之间的距离越缩越小，却发现这列多项式"想收敛到"一个根本不是多项式的函数，这正是第30章要补救的漏洞；**(4)** 正交投影与最小二乘——用一个具体的 Gram 矩阵，把"求最佳逼近"这件事从一道二元线性方程组算到底，再看清楚"最优解与子空间正交"这条性质是怎么从求导算出来的。

读完本章，你应该已经能手算出第30章要证明的大部分具体断言——只是还没有把"对任意内积空间、任意闭子空间都成立"写成一般定理，那是第30章的事。

## 二、入口：一道具体的问题 (Entry Problem)

> 题目来源：改编自第30章入口题 2.1（同一个空间、同一个内积），把要求从"证明"降到"算出/猜出"，数字与例子也更具体。

**问题 2.1.** 取 $$V=\mathbb{R}[x]$$（实系数多项式全体），仍用第30章的内积

$$\langle f,g\rangle=\int_0^1 f(x)g(x)\,dx,\qquad \lVert f\rVert=\sqrt{\langle f,f\rangle}.$$

回答下列四问——**只要求算出答案或猜出规律，不要求给出一般证明**（一般证明留给下一章）。

**(i)** 取 $$f(x)=1$$、$$g(x)=x$$。算出 $$\langle f,g\rangle$$、$$\lVert f\rVert$$、$$\lVert g\rVert$$，验证 $$\lvert\langle f,g\rangle\rvert\le\lVert f\rVert\lVert g\rVert$$ 对这一组数确实成立，并算出两边差多少。

**(ii)** 取多项式列

$$f_n(x)=1+x+\frac{x^2}{2!}+\cdots+\frac{x^n}{n!}\qquad(n=1,2,3,4),$$

即 $$e^x$$ 在 $$x=0$$ 处 Taylor 展开的截断。算出 $$\lVert f_2-f_1\rVert,\ \lVert f_3-f_2\rVert,\ \lVert f_4-f_3\rVert$$ 这三个具体数值，观察它们是否越来越小。如果这列多项式真的有一个"极限"，你能猜出极限是谁吗？它还会是一个多项式吗？

**(iii)** 取子空间 $$M=\operatorname{span}\lbrace1,x\rbrace$$（一次多项式全体）与 $$f(x)=x^2$$。先凭直觉猜一组 $$a,b$$（比如让 $$a+bx$$ 在 $$x=0,1$$ 两个端点与 $$f$$ 吻合），算出 $$\lVert f-(a+bx)\rVert^2$$；这是不是最小的？

**(iv)**（预告，第30章会证明）三角函数 $$1,\cos x,\sin x$$ 在 $$L^2([-\pi,\pi])$$（内积改为 $$\int_{-\pi}^\pi fg\,dx$$）上两两正交。只用 $$\sin x$$ 这一个方向，你能把 $$f(x)=x$$ 逼近到多好？

**为什么这道题是全章的引子。** (i) 是 Cauchy–Schwarz 最朴素的样子；(ii) 是"完备"这个词要解决的具体麻烦——一列看似收敛的多项式，极限却溜出了多项式的世界；(iii) 是正交投影／最小二乘的具体样子；(iv) 提前露一手第30章 3.4 节的 Fourier 展开。本章第三节会把这四问一一算透，并从算完的数字里抽出一般定义。

## 三、结构：定义与完整推导 (Structure & Proof)

本节分四步，对应入口题的四问：先算 Cauchy–Schwarz（3.1），再判定哪些范数"配得上"内积（3.2），再看柯西列与完备（3.3），最后算一个真正的最小二乘投影（3.4）。

### 3.1 长度、夹角与 Cauchy–Schwarz：先算两组具体的数

先解决入口题 (i)。

**例 3.1（$$\mathbb{R}^2$$ 里的具体验证）。** 取 $$x=(3,4)$$、$$y=(1,2)$$，用通常的点积 $$\langle x,y\rangle=x_1y_1+x_2y_2$$。直接算：

$$\langle x,y\rangle=3\cdot1+4\cdot2=11,\qquad \lVert x\rVert=\sqrt{3^2+4^2}=5,\qquad \lVert y\rVert=\sqrt{1^2+2^2}=\sqrt5.$$

于是 $$\lVert x\rVert\lVert y\rVert=5\sqrt5\approx11.18$$，而 $$\lvert\langle x,y\rangle\rvert=11$$。确实 $$11\le11.18$$，但不相等——因为 $$x,y$$ 不共线（$$3/1\ne4/2$$）。**这两个数为什么会满足这个不等式？** 下面用一个具体的代数技巧把原因挖出来。

取

$$z:=x-\frac{\langle x,y\rangle}{\lVert y\rVert^2}y=x-\frac{11}{5}y=\Big(3-\frac{11}{5},\ 4-\frac{22}{5}\Big)=\Big(\frac45,-\frac25\Big).$$

**为什么减这个特定的倍数？** 因为这样构造出来的 $$z$$ 恰好与 $$y$$ 垂直（不信可以算一下：$$\langle z,y\rangle=\frac45\cdot1+\big(-\frac25\big)\cdot2=\frac45-\frac45=0$$）——$$z$$ 就是把 $$x$$ 沿 $$y$$ 的方向"甩掉"之后剩下的那一段。直接算

$$\lVert z\rVert^2=\Big(\frac45\Big)^2+\Big(-\frac25\Big)^2=\frac{16}{25}+\frac4{25}=\frac{20}{25}=\frac45.$$

另一方面，展开 $$\lVert z\rVert^2$$ 的定义也能算到同一个数：

$$\lVert z\rVert^2=\lVert x\rVert^2-\frac{\langle x,y\rangle^2}{\lVert y\rVert^2}=25-\frac{121}{5}=\frac{125-121}5=\frac45.$$

两种算法吻合。**关键的一步在这里**：长度的平方永远 $$\ge0$$，所以

$$0\le\lVert z\rVert^2=\lVert x\rVert^2-\frac{\langle x,y\rangle^2}{\lVert y\rVert^2}\ \Longrightarrow\ \langle x,y\rangle^2\le\lVert x\rVert^2\lVert y\rVert^2,$$

代入数字就是 $$121\le125$$——这正是入口题 (i) 里 $$11\le11.18$$ 平方之后的样子。**这个论证完全没有用到 $$x,y$$ 是 $$\mathbb{R}^2$$ 里的向量这件事**：只用了「长度平方非负」与几步代数展开。这正是它能推广到任意内积空间的原因。

**定义 3.1（内积空间, inner product space）。** 设 $$V$$ 是 $$\mathbb{R}$$ 上的线性空间。映射 $$\langle\cdot,\cdot\rangle:V\times V\to\mathbb{R}$$ 称为**内积 (inner product)**，若对一切 $$x,y,z\in V$$、$$\alpha,\beta\in\mathbb{R}$$：

1. **对称**：$$\langle x,y\rangle=\langle y,x\rangle$$；
2. **双线性**（由对称性，只需对一个变元写）：$$\langle\alpha x+\beta y,z\rangle=\alpha\langle x,z\rangle+\beta\langle y,z\rangle$$；
3. **正定**：$$\langle x,x\rangle\ge0$$，且 $$\langle x,x\rangle=0\iff x=0$$。

带内积的线性空间称为**内积空间 (inner product space)**。$$\mathbb{R}^2$$ 带点积（例 3.1）、$$\mathbb{R}[x]$$ 带 $$\int_0^1fg$$（入口题）都是内积空间——你已经在这两个空间里各自验证过一遍。**为什么需要这个记号 $$\langle\cdot,\cdot\rangle$$？** 因为"点积""函数乘积再积分"表面上是完全不同的运算，但它们满足**同一组代数规则**；把它们用同一个符号写，正是为了让下面每一条推导（包括马上要证的不等式）对两者**同时**成立，不用重复证两遍。（第30章会补上复数情形，那里对称性要换成共轭对称。）

**定理 3.2（Cauchy–Schwarz 不等式）。** 设 $$(V,\langle\cdot,\cdot\rangle)$$ 是内积空间，$$x,y\in V$$。则

$$\lvert\langle x,y\rangle\rvert\le\lVert x\rVert\,\lVert y\rVert,\qquad\text{其中 }\lVert x\rVert:=\sqrt{\langle x,x\rangle}. \tag{29.1}$$

*证明（把例 3.1 的算法原样搬过来）。* 若 $$y=0$$ 两边都是 $$0$$，不等式平凡成立。设 $$y\ne0$$，仿照例 3.1，令

$$z:=x-\frac{\langle x,y\rangle}{\lVert y\rVert^2}y.$$

先验证 $$z\perp y$$（这是"减去投影"这一步的全部用意）：

$$\langle z,y\rangle=\langle x,y\rangle-\frac{\langle x,y\rangle}{\lVert y\rVert^2}\langle y,y\rangle=\langle x,y\rangle-\langle x,y\rangle=0.$$

再展开 $$\lVert z\rVert^2$$（与例 3.1 逐字相同的代数，只是不再代具体数字）：

$$\lVert z\rVert^2=\langle z,z\rangle=\big\langle z,x\big\rangle-\frac{\langle x,y\rangle}{\lVert y\rVert^2}\langle z,y\rangle=\langle z,x\rangle=\Big\langle x-\frac{\langle x,y\rangle}{\lVert y\rVert^2}y,\ x\Big\rangle=\lVert x\rVert^2-\frac{\langle x,y\rangle^2}{\lVert y\rVert^2}$$

（第二个等号用了 $$\langle z,y\rangle=0$$，直接消掉后一项）。由正定性 $$\lVert z\rVert^2\ge0$$，移项即得 $$\langle x,y\rangle^2\le\lVert x\rVert^2\lVert y\rVert^2$$，开方得 (29.1)。$$\blacksquare$$

**例 3.2（回到入口题 (i)：函数版本）。** 取 $$f(x)=1$$、$$g(x)=x$$，$$\langle f,g\rangle=\int_0^1fg\,dx$$：

$$\langle f,g\rangle=\int_0^1x\,dx=\frac12,\qquad \lVert f\rVert^2=\int_0^11\,dx=1,\qquad \lVert g\rVert^2=\int_0^1x^2dx=\frac13.$$

定理 3.2 断言 $$\big(\frac12\big)^2\le1\cdot\frac13$$，即 $$\frac14\le\frac13$$——成立，差 $$\frac1{12}$$。按证明里的构造，$$z=f-\frac{1/2}{1/3}x=1-\frac32x$$，直接算

$$\lVert z\rVert^2=\int_0^1\Big(1-\frac32x\Big)^2dx=\int_0^1\Big(1-3x+\frac94x^2\Big)dx=1-\frac32+\frac34=\frac14,$$

与 $$\lVert f\rVert^2-\langle f,g\rangle^2/\lVert g\rVert^2=1-\frac{1/4}{1/3}=1-\frac34=\frac14$$ 吻合。**入口题 (i) 到这里就算完整解出来了。**

**定理 3.3（内积诱导范数与三角不等式）。** $$\lVert x\rVert:=\sqrt{\langle x,x\rangle}$$ 满足 $$\lVert x+y\rVert\le\lVert x\rVert+\lVert y\rVert$$。

*证明。* 展开

$$\lVert x+y\rVert^2=\langle x+y,x+y\rangle=\lVert x\rVert^2+2\langle x,y\rangle+\lVert y\rVert^2\le\lVert x\rVert^2+2\lVert x\rVert\lVert y\rVert+\lVert y\rVert^2=(\lVert x\rVert+\lVert y\rVert)^2$$

（中间的 $$\le$$ 用了定理 3.2），开方即得。$$\blacksquare$$

用例 3.1 的 $$x,y$$ 核对一次：$$x+y=(4,6)$$，$$\lVert x+y\rVert=\sqrt{52}=2\sqrt{13}\approx7.21$$；$$\lVert x\rVert+\lVert y\rVert=5+\sqrt5\approx7.24$$。确实 $$7.21\le7.24$$，而且很接近——这不是巧合：$$x,y$$ 的方向本就相差不远，三角不等式越接近共线就越接近取等。

**注 3.1（为什么要单独引入 $$\lVert\cdot\rVert$$ 这个记号）。** $$\sqrt{\langle x,x\rangle}$$ 每次都要写内积、开根号，太啰嗦；更重要的是，一旦证明了定理 3.3，$$\lVert\cdot\rVert$$ 就满足"长度"该有的全部代数性质（非负、只有零向量长度为零、三角不等式），可以把它当成普通的"距离"来使用，不用每次都回头翻内积的定义。**这正是从更多结构里提炼出更少但足够用的结构的标准动作**：内积空间自动是一个赋范空间。

### 3.2 什么样的范数"配得上"内积：平行四边形法则

**例 3.3（$$\mathbb{R}^2$$ 里，标准范数满足一个隐藏的恒等式）。** 取 $$x=(1,1)$$、$$y=(1,-1)$$（标准点积）。算

$$x+y=(2,0),\ \lVert x+y\rVert^2=4;\qquad x-y=(0,2),\ \lVert x-y\rVert^2=4;\qquad \lVert x\rVert^2=2,\ \lVert y\rVert^2=2.$$

于是

$$\lVert x+y\rVert^2+\lVert x-y\rVert^2=4+4=8,\qquad 2\lVert x\rVert^2+2\lVert y\rVert^2=2\cdot2+2\cdot2=8.$$

两边相等！**这不是这一对向量的巧合**——换成例 3.1 的 $$x=(3,4),y=(1,2)$$ 也一样成立：$$\lVert x+y\rVert^2+\lVert x-y\rVert^2=52+8=60=2\cdot25+2\cdot5=2\lVert x\rVert^2+2\lVert y\rVert^2$$。任何由内积诱导的范数都满足这条恒等式（马上证明）。

**例 3.4（换一种范数，恒等式立刻碎掉）。** 还是 $$x=(1,1)$$、$$y=(1,-1)$$，这次改用 $$\ell^1$$ 范数 $$\lVert(a,b)\rVert_1=\lvert a\rvert+\lvert b\rvert$$：

$$\lVert x\rVert_1=2,\ \lVert y\rVert_1=2,\qquad \lVert x+y\rVert_1=\lVert(2,0)\rVert_1=2,\qquad \lVert x-y\rVert_1=\lVert(0,2)\rVert_1=2.$$

左边 $$\lVert x+y\rVert_1^2+\lVert x-y\rVert_1^2=4+4=8$$；右边 $$2\lVert x\rVert_1^2+2\lVert y\rVert_1^2=2\cdot4+2\cdot4=16$$。$$8\ne16$$！**同一对向量，换一种"长度"的量法，这条恒等式就不成立了。** 这说明 $$\ell^1$$ 范数不可能是某个内积诱导出来的——如果它是，例 3.3 的算法（对任意向量都成立）就该给出相等，但这里给出的是 $$8\ne16$$。

**定理 3.4（平行四边形法则，必要性方向）。** 若 $$\lVert\cdot\rVert$$ 由内积 $$\langle\cdot,\cdot\rangle$$ 诱导，则对一切 $$x,y$$

$$\lVert x+y\rVert^2+\lVert x-y\rVert^2=2\lVert x\rVert^2+2\lVert y\rVert^2. \tag{29.2}$$

*证明。* 分别展开两边（跟例 3.3 里做的计算一字不差，只是不代具体数字）：

$$\lVert x+y\rVert^2=\lVert x\rVert^2+2\langle x,y\rangle+\lVert y\rVert^2,\qquad \lVert x-y\rVert^2=\lVert x\rVert^2-2\langle x,y\rangle+\lVert y\rVert^2.$$

两式相加，$$\pm2\langle x,y\rangle$$ 抵消，剩下 (29.2)。$$\blacksquare$$

**注 3.2（反过来呢？）。** 定理 3.4 只说了"内积 $$\Rightarrow$$ 平行四边形法则"这一个方向；例 3.4 用它的**逆否命题**排除了 $$\ell^1$$ 范数。**更难也更有用的方向是反过来**：只要一个范数满足 (29.2)，就一定能从它反推出一个内积（用 $$\langle x,y\rangle=\frac14\big(\lVert x+y\rVert^2-\lVert x-y\rVert^2\big)$$ 这条"极化恒等式 (polarization identity)"）。这个反方向需要验证反推出来的 $$\langle\cdot,\cdot\rangle$$ 满足定义 3.1 的三条公理——尤其"双线性"这一条并不显然，第30章 定理 3.5 会给出完整证明。

### 3.3 柯西列与「完备」：为什么 $$\mathbb{R}[x]$$ 不够用

回到入口题 (ii)。

**例 3.5（Taylor 截断的具体距离）。** 记 $$f_n(x)=1+x+\dfrac{x^2}{2!}+\cdots+\dfrac{x^n}{n!}$$。相邻两项之差总是"多出最后一项"：$$f_{n+1}-f_n=\dfrac{x^{n+1}}{(n+1)!}$$。算它的范数：

$$\lVert f_{n+1}-f_n\rVert^2=\int_0^1\Big(\frac{x^{n+1}}{(n+1)!}\Big)^2dx=\frac1{\big((n+1)!\big)^2}\int_0^1x^{2n+2}dx=\frac1{\big((n+1)!\big)^2(2n+3)}.$$

代 $$n=1,2,3$$：

$$\lVert f_2-f_1\rVert=\frac1{2!\sqrt5}=\frac1{2\sqrt5}\approx0.2236,\quad \lVert f_3-f_2\rVert=\frac1{3!\sqrt7}\approx0.0630,\quad \lVert f_4-f_3\rVert=\frac1{4!\sqrt9}=\frac1{72}\approx0.0139.$$

每一步都在急剧缩小（分母里的阶乘增长远快于根号项）。**这正是"柯西"的意思**：越往后，相邻项之间的距离越接近 $$0$$。

**定义 3.5（柯西列, Cauchy sequence；完备, complete）。** 内积空间 $$V$$ 中的序列 $$(x_n)$$ 称为**柯西列 (Cauchy sequence)**，若对任意 $$\varepsilon>0$$，存在 $$N$$，使得 $$m,n\ge N$$ 时 $$\lVert x_m-x_n\rVert<\varepsilon$$（不只是相邻项接近，是"从某处往后任何两项都接近"）。若 $$V$$ 中每个柯西列都收敛到 $$V$$ 里的一个元素，则称 $$V$$**完备 (complete)**；完备的内积空间就是 Hilbert 空间（第30章 定义 3.4）。

**为什么"相邻项接近"还不够、需要"任何两项都接近"。** 只知道 $$\lVert f_{n+1}-f_n\rVert\to0$$ 并不能自动保证 $$\lVert f_m-f_n\rVert\to0$$（$$m,n$$ 都很大但相差很多）——但这里的差距是可以用三角不等式加起来控制的：可以验证对一切 $$n\ge1$$ 都有 $$\lVert f_{n+2}-f_{n+1}\rVert\le\frac13\lVert f_{n+1}-f_n\rVert$$（因为多除了一个 $$\ge3$$ 的阶乘因子，练习 竞2 给出完整证明），于是对 $$m>n$$，

$$\lVert f_m-f_n\rVert\le\sum_{k=n}^{m-1}\lVert f_{k+1}-f_k\rVert\le\lVert f_{n+1}-f_n\rVert\sum_{j=0}^\infty3^{-j}=\frac32\lVert f_{n+1}-f_n\rVert\xrightarrow[n\to\infty]{}0.$$

所以 $$(f_n)$$ 确实是柯西列——这一段小小的等比放缩，正是第30章 定理 3.6 第二步"证明 $$\langle x_n,y_n\rangle$$ 的极限存在"要用的同一种手法（只是那里换成一般的柯西估计）。

**命题 3.6（$$(\mathbb{R}[x],\lVert\cdot\rVert)$$ 不完备）。** $$(f_n)$$ 是 $$\mathbb{R}[x]$$ 中的柯西列，但**不存在**多项式 $$p$$ 使 $$\lVert f_n-p\rVert\to0$$。

*论证。* 微积分里的标准事实是：$$e^x$$ 的 Taylor 余项在 $$[0,1]$$ 上一致趋于 $$0$$，即 $$f_n\to e^x$$ 关于 $$\sup$$-范数（因而也关于这里的 $$L^2([0,1])$$ 范数，因为 $$\lVert h\rVert\le\lVert h\rVert_\infty$$）。所以**如果**有多项式 $$p$$ 使 $$\lVert f_n-p\rVert\to0$$，由极限的唯一性，$$p$$ 与 $$e^x$$ 在这个范数意义下"相等"，两者又都连续，故 $$p(x)=e^x$$ 对一切 $$x\in[0,1]$$ 成立。但这不可能：若 $$p$$ 次数为 $$N$$，则 $$\dfrac{d^{N+1}}{dx^{N+1}}p\equiv0$$，而 $$\dfrac{d^{N+1}}{dx^{N+1}}e^x=e^x>0$$——矛盾。所以这样的 $$p$$ 不存在。$$\blacksquare$$

**这就是入口题 (ii) 的答案**：$$(f_n)$$ 越走越"密"（柯西），却在朝着一个多项式空间里根本不存在的方向走——$$e^x$$ 是超越函数，不是多项式。**这正是第30章第 3.2 节要解决的问题**：完备化就是把这类"该有极限却没地方安放"的柯西列，正式地补成新的向量（第30章 定理 3.6）。

**注 3.3（完备化预告）。** 第30章会证明：把 $$\mathbb{R}[x]$$ 的全体柯西列"模去零列"补齐，得到的恰好是 $$L^2([0,1])$$。$$e^x$$ 正是补进来的那些新元素之一。

### 3.4 正交投影与最小二乘：一个具体的 Gram 矩阵

回到入口题 (iii)：在 $$M=\operatorname{span}\lbrace1,x\rbrace$$ 里找 $$f(x)=x^2$$ 的最佳逼近。

**先试一次直觉猜测。** 若让 $$a+bx$$ 在端点 $$x=0,1$$ 处与 $$x^2$$ 吻合，得 $$a=0$$（因为 $$0^2=0$$）、$$a+b=1$$（因为 $$1^2=1$$），即猜 $$a=0,b=1$$，也就是 $$p(x)=x$$。算它的误差：

$$\lVert x^2-x\rVert^2=\int_0^1(x^2-x)^2dx=\int_0^1(x^4-2x^3+x^2)dx=\frac15-\frac12+\frac13=\frac{6-15+10}{30}=\frac1{30}\approx0.0333.$$

这猜得还不错，但是不是最好的？下面用微积分把"最好"找出来。

**为什么"最小化"会给出一个线性方程组。** 记 $$\varphi(a,b)=\lVert x^2-a-bx\rVert^2=\int_0^1(x^2-a-bx)^2dx$$，这是关于 $$a,b$$ 的二元函数，要找它的最小值点，对 $$a,b$$ 分别求偏导并令其为零：

$$\frac{\partial\varphi}{\partial a}=\int_0^1-2(x^2-a-bx)\,dx=0\ \Longrightarrow\ \langle x^2-a-bx,\,1\rangle=0,$$

$$\frac{\partial\varphi}{\partial b}=\int_0^1-2x(x^2-a-bx)\,dx=0\ \Longrightarrow\ \langle x^2-a-bx,\,x\rangle=0.$$

**这两条偏导数为零的条件，翻译过来就是"误差与 $$1$$、$$x$$ 都正交"**——微积分的求导最小化和"正交"这个几何概念，在这里是同一件事的两种说法。

**定义 3.7（正交, orthogonal；正交补, orthogonal complement，有限维版本）。** 称 $$u\perp v$$（$$u,v$$ **正交**），若 $$\langle u,v\rangle=0$$。对子空间 $$M=\operatorname{span}\lbrace e_1,\dots,e_k\rbrace$$，称 $$u\perp M$$，若 $$u\perp e_j$$ 对每个 $$j$$ 成立（等价于 $$u$$ 与 $$M$$ 里每一个向量都正交，由内积的双线性逐项展开即得）。

**例 3.6（把方程组解出来）。** 取 $$e_1=1,e_2=x$$。算 Gram 矩阵的三个入口与右端两个数：

$$\langle e_1,e_1\rangle=\int_0^11\,dx=1,\quad \langle e_1,e_2\rangle=\int_0^1x\,dx=\frac12,\quad \langle e_2,e_2\rangle=\int_0^1x^2dx=\frac13,$$

$$\langle f,e_1\rangle=\int_0^1x^2dx=\frac13,\qquad \langle f,e_2\rangle=\int_0^1x^3dx=\frac14.$$

正交条件 $$\langle f-a-bx,e_1\rangle=0$$、$$\langle f-a-bx,e_2\rangle=0$$ 展开就是

$$a+\frac12b=\frac13,\qquad \frac12a+\frac13b=\frac14.$$

由第一式 $$a=\frac13-\frac12b$$，代入第二式：$$\frac12\big(\frac13-\frac12b\big)+\frac13b=\frac14\ \Longrightarrow\ \frac16-\frac14b+\frac13b=\frac14\ \Longrightarrow\ \frac16+\frac1{12}b=\frac14\ \Longrightarrow\ b=12\Big(\frac14-\frac16\Big)=12\cdot\frac1{12}=1.$$

代回得 $$a=\frac13-\frac12=-\frac16$$。所以**真正的最佳逼近**是

$$Pf(x)=-\frac16+x,$$

比刚才凭直觉猜的 $$p(x)=x$$ 多了一个常数修正 $$-\frac16$$。验证正交性：$$\langle x^2-Pf,1\rangle=\int_0^1\big(x^2-x+\frac16\big)dx=\frac13-\frac12+\frac16=0$$；$$\langle x^2-Pf,x\rangle=\int_0^1x\big(x^2-x+\frac16\big)dx=\frac14-\frac13+\frac1{12}=0$$。两条都成立。

**验证勾股关系**（这是"正交"在几何上最直接的含义）：

$$\lVert f\rVert^2=\int_0^1x^4dx=\frac15,\qquad \lVert Pf\rVert^2=\int_0^1\Big(x-\frac16\Big)^2dx=\frac13-\frac16+\frac1{36}=\frac{7}{36},$$

$$\lVert f-Pf\rVert^2=\int_0^1\Big(x^2-x+\frac16\Big)^2dx=\frac1{180}\quad(\text{展开成 }x^4-2x^3+\tfrac43x^2-\tfrac13x+\tfrac1{36}\text{ 后逐项积分即得}).$$

核对：$$\lVert Pf\rVert^2+\lVert f-Pf\rVert^2=\frac{7}{36}+\frac1{180}=\frac{35}{180}+\frac1{180}=\frac{36}{180}=\frac15=\lVert f\rVert^2$$——与 $$\lVert f\rVert^2$$ 完全吻合。**误差 $$\frac1{180}\approx0.0056$$ 确实比直觉猜测的 $$\frac1{30}\approx0.0333$$ 小**，说明"正交"给出的才是真正的最优解，直觉的端点吻合法不是。

**定理 3.8（最佳逼近就是正交投影）。** 设 $$M=\operatorname{span}\lbrace e_1,\dots,e_k\rbrace$$ 是有限维子空间（$$e_j$$ 线性无关），$$f\in V$$。则 $$\min_{p\in M}\lVert f-p\rVert$$ 在唯一的 $$Pf\in M$$ 处取到，且 $$Pf$$ 由"$$f-Pf$$ 与每个 $$e_j$$ 都正交"这一条件唯一确定（即解例 3.6 那样的 Gram 矩阵方程组）。

*证明思路。* 例 3.6 的推导对一般的 $$f$$、一般的基 $$\lbrace e_1,\dots,e_k\rbrace$$ 逐字成立：对 $$\varphi(a_1,\dots,a_k)=\big\lVert f-\sum_ja_je_j\big\rVert^2$$ 求各个偏导并令其为零，得到线性方程组 $$\sum_j\langle e_i,e_j\rangle a_j=\langle f,e_i\rangle$$（$$i=1,\dots,k$$），恰是"$$f-\sum_ja_je_j\perp e_i$$ 对每个 $$i$$"的展开。这个方程组的系数矩阵（Gram 矩阵）在 $$\lbrace e_j\rbrace$$ 线性无关时可逆，故解唯一存在。$$\blacksquare$$

**注 3.4（这就是第30章"投影定理"的有限维影子）。** 第30章 定理 3.10 会把 $$M$$ 换成**任意闭子空间**（不一定有有限维基），把"求偏导数"换成"取闭凸集里离原点最近的一点"（定理 3.9），并证明：只要 $$M$$ 闭，$$Pf$$ 一定存在——但如果 $$M$$ 不闭（比如把 $$\mathbb{R}[x]$$ 全体看作 $$L^2([0,1])$$ 的子空间），最佳逼近可能根本不存在（第30章 经典题4，用的正是 $$e^x$$，与本章 3.3 节的命题 3.6 是同一件事的两面）。

## 四、几何与物理直觉 (Intuition)

**投影就是影子。** 想象阳光垂直照在地面上，一根斜插着的木棍在地面投下一道影子：影子的长度永远不超过木棍本身的长度，只有木棍恰好躺平（与地面平行，即已经在 $$M$$ 里）时影子才等于木棍。3.4 节里 $$Pf$$ 就是"$$f$$ 投在子空间 $$M$$ 上的影子"，勾股关系 $$\lVert f\rVert^2=\lVert Pf\rVert^2+\lVert f-Pf\rVert^2$$ 说的正是"木棍长度的平方 $$=$$ 影子长度的平方 $$+$$ 木棍离地面的高度的平方"。

**最小二乘就是"众口难调时找一个折中"。** 一组测量数据几乎从不恰好落在一条直线上；3.4 节的 $$Pf(x)=x-\frac16$$ 不是"穿过某两个特殊点的直线"，而是"到所有数据点的（平方）误差之和最小"的那条直线——GPS 定位、天气预报的参数拟合、机器学习里的线性回归，用的都是同一个 Gram 矩阵方程组。

**柯西列就是"一条越走越密的路"。** 3.3 节的 $$(f_n)$$ 一步比一步近，像是在沿着一条路稳步逼近终点；但如果这条路铺在一片有洞的地面上（$$\mathbb{R}[x]$$ 就是这样一片"有洞"的地面，洞的位置正是 $$e^x$$ 这类超越函数），走的人会发现自己越走越"该"到达，却永远也摸不到地面上的那个点——因为那个点根本不在这片地面里。完备化（第30章 定理 3.6）就是把所有这些洞都填平：**凡是"该收敛"的地方，都补一个点进去**。

**正交就是"互不干扰的独立方向"。** $$x,y,z$$ 三个坐标轴互相垂直，沿一个轴移动完全不影响另外两个轴上的读数——这正是"正交"在物理测量里的意义：两个正交的信号（或误差来源）不会互相"泄露"信息。3.4 节里 $$f-Pf\perp1$$ 与 $$f-Pf\perp x$$ 就是说，逼近的"残差"里不再含有任何"常数方向"或"一次方向"的成分——所有能用 $$1,x$$ 解释的部分都已经被 $$Pf$$ 拿走了。

**下一章的物理落点。** 第30章第四节会把这套几何语言直接搬进量子力学：态矢量的"归一化"就是 $$\lVert\psi\rVert=1$$，"测量"就是把态投影到某个子空间上（正是本章 3.4 节的 $$P$$），而"态之间互不干涉"就是本节说的"正交"。声音的谐波分解（把复杂声波拆成一系列纯音的叠加）也是同一个几何：入口题 (iv) 里用 $$\sin x$$ 逼近 $$f(x)=x$$，正是"用一个纯音去凑一段复杂波形"的最简单版本——练习 研1 会把这件事算一遍。

## 五、经典问题精讲 (Classical Problems)

### 经典题 1（考点：Cauchy–Schwarz 的等号条件；位置：3.1）

**题。** 在 $$\mathbb{R}^3$$（标准点积）中取 $$u=(2,-1,2)$$、$$v=(4,-2,4)$$。验证 Cauchy–Schwarz 不等式对 $$u,v$$ 取等号，并解释为什么。再取 $$w=(1,0,1)$$，验证不等式对 $$u,w$$ **不**取等号。

**解。** 注意 $$v=2u$$。直接算：$$\langle u,v\rangle=2\cdot4+(-1)(-2)+2\cdot4=8+2+8=18$$；$$\lVert u\rVert=\sqrt{4+1+4}=3$$，$$\lVert v\rVert=\sqrt{16+4+16}=6$$，$$\lVert u\rVert\lVert v\rVert=18$$。恰好 $$\lvert\langle u,v\rangle\rvert=\lVert u\rVert\lVert v\rVert=18$$，取等号。**原因**：定理 3.2 的证明里，等号成立当且仅当那个"减去投影"之后剩下的 $$z=u-\frac{\langle u,v\rangle}{\lVert v\rVert^2}v$$ 恰好是零向量；这里 $$z=u-\frac{18}{36}\cdot2u=u-u=0$$——因为 $$v$$ 本身就是 $$u$$ 的倍数，"投影"已经把 $$u$$ 全部吸收了，没有剩余。

再看 $$u,w$$：$$\langle u,w\rangle=2\cdot1+(-1)\cdot0+2\cdot1=4$$；$$\lVert w\rVert=\sqrt2$$，$$\lVert u\rVert\lVert w\rVert=3\sqrt2\approx4.24$$。$$4<4.24$$，严格小于——因为 $$w$$ 不是 $$u$$ 的倍数。$$\blacksquare$$

**注释。** 这题把定理 3.2 的等号条件"$$x,y$$ 线性相关"落到了实处：**共线才能取等，这不是巧合，是"投影后一无所剩"的代数翻译。**

### 经典题 2（考点：向一条直线做正交投影；位置：3.4）

**题。** 在 $$\mathbb{R}^3$$ 中，把向量 $$w=(1,2,2)$$ 投影到直线 $$L=\operatorname{span}\lbrace(2,1,2)\rbrace$$ 上，求投影 $$Pw$$，并验证 $$w-Pw\perp L$$ 与勾股关系。

**解。** 记 $$e=(2,1,2)$$。由 3.4 节同样的公式（$$M$$ 是一维时 Gram 矩阵退化成一个数）：

$$Pw=\frac{\langle w,e\rangle}{\langle e,e\rangle}e.$$

算 $$\langle w,e\rangle=1\cdot2+2\cdot1+2\cdot2=2+2+4=8$$，$$\langle e,e\rangle=4+1+4=9$$。故

$$Pw=\frac89(2,1,2)=\Big(\frac{16}9,\frac89,\frac{16}9\Big).$$

残差 $$w-Pw=\Big(1-\frac{16}9,\ 2-\frac89,\ 2-\frac{16}9\Big)=\Big(-\frac79,\frac{10}9,\frac29\Big)$$。验证正交：

$$\langle w-Pw,e\rangle=-\frac79\cdot2+\frac{10}9\cdot1+\frac29\cdot2=-\frac{14}9+\frac{10}9+\frac49=0.$$

验证勾股：$$\lVert w\rVert^2=1+4+4=9$$；$$\lVert Pw\rVert^2=\big(\frac89\big)^2\cdot9=\frac{64}9$$；$$\lVert w-Pw\rVert^2=\frac{49+100+4}{81}=\frac{153}{81}=\frac{17}9$$。核对：$$\frac{64}9+\frac{17}9=\frac{81}9=9=\lVert w\rVert^2$$。$$\blacksquare$$

**注释。** 一维子空间的投影公式 $$Pw=\dfrac{\langle w,e\rangle}{\langle e,e\rangle}e$$ 正是 3.1 节里"减去投影"那个技巧里用到的同一个表达式——Cauchy–Schwarz 的证明和"求最近点"用的是同一条公式，只是问的问题不同。

### 经典题 3（考点：用平行四边形法则排除一个范数；位置：3.2）

**题。** 在 $$\mathbb{R}^2$$ 上定义 $$\lVert(a,b)\rVert_\ast:=\lvert a\rvert+2\lvert b\rvert$$。用具体向量判断：这个范数会是某个内积诱导出来的吗？

**解。** 取 $$x=(1,0)$$、$$y=(0,1)$$。算：$$\lVert x\rVert_\ast=1$$，$$\lVert y\rVert_\ast=2$$；$$x+y=(1,1)$$，$$\lVert x+y\rVert_\ast=1+2=3$$；$$x-y=(1,-1)$$，$$\lVert x-y\rVert_\ast=1+2=3$$。平行四边形法则左边 $$3^2+3^2=18$$，右边 $$2\cdot1^2+2\cdot2^2=2+8=10$$。$$18\ne10$$，法则不成立。由定理 3.4 的逆否命题，**这个范数不可能来自任何内积**。$$\blacksquare$$

**注释。** 这类"加权 $$\ell^1$$"范数在数据分析里很常见（给不同坐标不同的权重），但只要权重不是"处处相同的常数倍"，它一般都不满足平行四边形法则——第30章 定理 3.5 会把这件事一般化到 $$\ell^p,L^p$$ 整个家族。

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 在 $$\mathbb{R}^3$$（标准点积）中取 $$u=(1,2,-1)$$、$$v=(0,3,2)$$、$$w=(1,0,1)$$。验证 $$\langle u,v\rangle=\langle v,u\rangle$$，并验证 $$\langle2u-v,w\rangle=2\langle u,w\rangle-\langle v,w\rangle$$（双线性的具体例子）。

**基2.** 取 $$p(x)=x$$、$$q(x)=1-x$$，内积为 $$\int_0^1pq\,dx$$。算出 $$\langle p,q\rangle$$、$$\lVert p\rVert^2$$、$$\lVert q\rVert^2$$，验证 Cauchy–Schwarz 不等式成立。

**基3.** 取 $$u=(1,0,2)$$、$$v=(2,1,0)$$（标准点积）。验证平行四边形法则 (29.2) 成立。

**基4.** 在 $$\mathbb{R}^2$$ 中把 $$w=(3,1)$$ 投影到直线 $$\operatorname{span}\lbrace(1,1)\rbrace$$ 上，求投影 $$Pw$$，验证 $$w-Pw\perp(1,1)$$ 与勾股关系。

### 竞赛（本课目标难度）

**竞1.** 在 $$M=\operatorname{span}\lbrace1,x\rbrace\subset\mathbb{R}[x]$$（内积 $$\int_0^1fg$$）里，求 $$f(x)=x^3$$ 的最佳逼近 $$a+bx$$（仿照例 3.6 解 Gram 矩阵方程组），并验证正交条件。

**竞2.** 沿用 3.3 节的记号 $$d_n:=\lVert f_{n+1}-f_n\rVert=\dfrac1{(n+1)!\sqrt{2n+3}}$$。算出 $$d_4=\lVert f_5-f_4\rVert$$ 的具体数值；再证明对一切 $$n\ge1$$ 都有 $$d_{n+1}\le\frac13d_n$$，并用这条不等式估计 $$\lVert f_{10}-f_5\rVert$$ 的一个上界。

### 研究（通向下一章）

**研1.** 用入口题 (iv) 的思路：算出 $$f(x)=x$$ 在 $$[-\pi,\pi]$$ 上沿 $$\sin x$$ 方向的投影系数 $$c=\dfrac{\langle f,\sin x\rangle}{\langle\sin x,\sin x\rangle}$$（内积为 $$\int_{-\pi}^\pi fg\,dx$$），并算出残差 $$\lVert f-c\sin x\rVert^2$$，与 $$\lVert f\rVert^2$$ 比较，说明只用一个方向逼近得还不够好。

**研2.** 设 $$M_3=\operatorname{span}\lbrace1,x,x^2\rbrace\subset\mathbb{R}[x]$$（同样的内积 $$\int_0^1fg$$）。$$(M_3,\lVert\cdot\rVert)$$ 是完备的吗？这与 3.3 节"$$(\mathbb{R}[x],\lVert\cdot\rVert)$$ 不完备"的结论矛盾吗？说明理由。

### 解答 (Solutions)

**解 基1.** $$\langle u,v\rangle=1\cdot0+2\cdot3+(-1)\cdot2=0+6-2=4$$；$$\langle v,u\rangle=0\cdot1+3\cdot2+2\cdot(-1)=0+6-2=4$$，两者相等。$$2u-v=(2,4,-2)-(0,3,2)=(2,1,-4)$$，故 $$\langle2u-v,w\rangle=2\cdot1+1\cdot0+(-4)\cdot1=-2$$。另一边：$$\langle u,w\rangle=1\cdot1+2\cdot0+(-1)\cdot1=0$$，$$\langle v,w\rangle=0\cdot1+3\cdot0+2\cdot1=2$$，故 $$2\langle u,w\rangle-\langle v,w\rangle=0-2=-2$$。两边都是 $$-2$$，一致。$$\blacksquare$$

**解 基2.** $$\langle p,q\rangle=\int_0^1x(1-x)dx=\int_0^1(x-x^2)dx=\frac12-\frac13=\frac16$$。$$\lVert p\rVert^2=\int_0^1x^2dx=\frac13$$；$$\lVert q\rVert^2=\int_0^1(1-x)^2dx=\int_0^1(1-2x+x^2)dx=1-1+\frac13=\frac13$$。Cauchy–Schwarz：$$\big(\frac16\big)^2=\frac1{36}$$ 与 $$\lVert p\rVert^2\lVert q\rVert^2=\frac13\cdot\frac13=\frac19=\frac4{36}$$，确有 $$\frac1{36}\le\frac4{36}$$。$$\blacksquare$$

**解 基3.** $$\lVert u\rVert^2=1+0+4=5$$，$$\lVert v\rVert^2=4+1+0=5$$。$$u+v=(3,1,2)$$，$$\lVert u+v\rVert^2=9+1+4=14$$；$$u-v=(-1,-1,2)$$，$$\lVert u-v\rVert^2=1+1+4=6$$。左边 $$14+6=20$$；右边 $$2\cdot5+2\cdot5=20$$，相等。$$\blacksquare$$

**解 基4.** $$e=(1,1)$$。$$\langle w,e\rangle=3\cdot1+1\cdot1=4$$，$$\langle e,e\rangle=2$$，故 $$Pw=\frac42e=(2,2)$$。残差 $$w-Pw=(1,-1)$$，$$\langle w-Pw,e\rangle=1\cdot1+(-1)\cdot1=0$$，正交成立。勾股：$$\lVert w\rVert^2=9+1=10$$，$$\lVert Pw\rVert^2=4+4=8$$，$$\lVert w-Pw\rVert^2=1+1=2$$，核对 $$8+2=10$$。$$\blacksquare$$

**解 竞1.** 仿例 3.6，$$e_1=1,e_2=x$$ 的 Gram 矩阵不变：$$\langle e_1,e_1\rangle=1,\langle e_1,e_2\rangle=\frac12,\langle e_2,e_2\rangle=\frac13$$。右端：$$\langle f,e_1\rangle=\int_0^1x^3dx=\frac14$$，$$\langle f,e_2\rangle=\int_0^1x^4dx=\frac15$$。方程组

$$a+\frac12b=\frac14,\qquad \frac12a+\frac13b=\frac15.$$

由第一式 $$a=\frac14-\frac12b$$，代入第二式：$$\frac12\big(\frac14-\frac12b\big)+\frac13b=\frac15\ \Longrightarrow\ \frac18-\frac14b+\frac13b=\frac15\ \Longrightarrow\ \frac18+\frac1{12}b=\frac15$$，故

$$b=12\Big(\frac15-\frac18\Big)=12\cdot\frac{8-5}{40}=12\cdot\frac3{40}=\frac9{10},\qquad a=\frac14-\frac12\cdot\frac9{10}=\frac14-\frac9{20}=\frac{5-9}{20}=-\frac15.$$

故 $$Pf(x)=-\frac15+\frac9{10}x$$。验证：$$\langle f-Pf,1\rangle=\int_0^1\big(x^3+\frac15-\frac9{10}x\big)dx=\frac14+\frac15-\frac9{20}=\frac{5+4-9}{20}=0$$；$$\langle f-Pf,x\rangle=\int_0^1\big(x^4+\frac15x-\frac9{10}x^2\big)dx=\frac15+\frac1{10}-\frac3{10}=\frac{2+1-3}{10}=0$$。两条都成立。$$\blacksquare$$

**解 竞2.** $$d_4=\lVert f_5-f_4\rVert=\dfrac1{5!\sqrt{11}}=\dfrac1{120\sqrt{11}}\approx\dfrac1{397.99}\approx0.002513$$。

**证明 $$d_{n+1}\le\frac13d_n$$：**

$$\frac{d_{n+1}}{d_n}=\frac{(n+1)!\sqrt{2n+3}}{(n+2)!\sqrt{2n+5}}=\frac1{n+2}\sqrt{\frac{2n+3}{2n+5}}.$$

右边的根号部分小于 $$1$$（因为 $$2n+3<2n+5$$），而 $$n\ge1$$ 时 $$\dfrac1{n+2}\le\dfrac13$$，两者相乘自然 $$\le\dfrac13$$。$$\blacksquare$$

**估计 $$\lVert f_{10}-f_5\rVert$$：** 由三角不等式与上面的比值控制，

$$\lVert f_{10}-f_5\rVert\le\sum_{k=5}^{9}d_k\le d_5\sum_{j=0}^{4}3^{-j}<d_5\cdot\frac32.$$

而 $$d_5\le\frac13d_4\approx0.000838$$，故 $$\lVert f_{10}-f_5\rVert\lesssim0.00126$$——远小于 $$d_1\approx0.2236$$，说明这个序列确实越走越"密"。$$\blacksquare$$

**解 研1.** $$\langle f,\sin x\rangle=\int_{-\pi}^\pi x\sin x\,dx$$。$$x\sin x$$ 是偶函数，故 $$=2\int_0^\pi x\sin x\,dx$$。分部积分（$$u=x,dv=\sin x\,dx,v=-\cos x$$）：

$$\int_0^\pi x\sin x\,dx=[-x\cos x]_0^\pi+\int_0^\pi\cos x\,dx=-\pi\cos\pi+[\sin x]_0^\pi=\pi+0=\pi.$$

故 $$\langle f,\sin x\rangle=2\pi$$。又 $$\langle\sin x,\sin x\rangle=\int_{-\pi}^\pi\sin^2x\,dx=\pi$$，故 $$c=\dfrac{2\pi}\pi=2$$，即最好的单方向逼近是 $$2\sin x$$。

残差（用勾股关系，因为 $$f-c\sin x\perp\sin x$$）：

$$\lVert f-2\sin x\rVert^2=\lVert f\rVert^2-c^2\lVert\sin x\rVert^2=\int_{-\pi}^\pi x^2dx-4\pi=\frac{2\pi^3}3-4\pi.$$

数值上 $$\frac{2\pi^3}3\approx20.67$$，$$4\pi\approx12.57$$，故残差平方 $$\approx8.10$$，$$\lVert f\rVert^2\approx20.67$$——残差占了原来长度平方的三分之一以上，**说明只用一个方向远远不够**，需要像第30章 3.4 节那样加入 $$\sin2x,\sin3x,\dots$$ 无穷多个方向才能让残差趋于零。$$\blacksquare$$

**解 研2.** $$(M_3,\lVert\cdot\rVert)$$ **是完备的**。$$M_3$$ 是三维空间（有限维），而**任何有限维赋范空间都是完备的**（标准事实，本质原因是有限维空间上所有范数等价，柯西列在坐标分量上退化成普通实数列的柯西列，而 $$\mathbb{R}$$ 本身完备）。

这**不矛盾**：3.3 节的柯西列 $$(f_n)$$ 的次数 $$n$$ 随 $$n$$ 增大而增大——一旦 $$n>3$$，$$f_n$$ 根本不在 $$M_3$$ 里（它含有 $$x^4,x^5,\dots$$ 这些高次项）。所以"$$(f_n)$$ 是柯西列却没有极限"这件事发生在**整个** $$\mathbb{R}[x]$$ 里，而不是发生在任何一个固定的有限维子空间 $$M_N$$ 里——完备性的失败，根源恰恰是 $$\mathbb{R}[x]$$ 的**维数无穷**（"次数可以任意大"），这与第30章 定理 3.14 里"$$\dim V=\aleph_0$$ 而 $$\dim V^*=\mathfrak c$$"的无穷维现象是同一条断层线。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**1. Cauchy–Schwarz 的证明只有一个动作：减去投影、看非负性。** 例 3.1、例 3.2、定理 3.2 用的是完全同一个代数技巧——先猜"$$z=x-\frac{\langle x,y\rangle}{\lVert y\rVert^2}y$$ 应该与 $$y$$ 垂直"，验证它确实垂直，再用 $$\lVert z\rVert^2\ge0$$ 反推不等式。这个技巧不挑维数、不挑是向量还是函数。

**2. 平行四边形法则是一把"体检尺"，量出范数是不是内积生的。** 例 3.3、例 3.4、经典题3 用同一对向量在不同范数下算出"符合"与"不符合"，直接把 $$\ell^1$$ 之类的范数排除在 Hilbert 家族之外——不用碰触任何一般性证明，一次具体计算就够。

**3. 柯西 $$\ne$$ 收敛，除非空间"没有洞"。** 命题 3.6 的多项式列 $$(f_n)$$ 是本章最重要的一个具体反例：它满足柯西列的全部要求，却在 $$\mathbb{R}[x]$$ 里"走投无路"。**完备性不是一句空话，而是"这片空间里没有缺口"的精确表述**——第30章要做的完备化，就是把 $$e^x$$ 这类缺口正式地补进空间。

**4. 求最佳逼近 $$=$$ 求偏导为零 $$=$$ 正交。** 3.4 节的 $$Pf$$ 出现了三次面孔：一次是"离 $$f$$ 最近的点"，一次是"二元函数 $$\varphi(a,b)$$ 的最小值点"，一次是"使残差与 $$M$$ 正交的点"——这三句话说的是同一件事。Gram 矩阵就是把这件事翻译成可以直接解的线性方程组的工具。

**5. 无穷维的"病"总是同一种病。** 命题 3.6（完备性失败）与研2（有限维子空间反而完备）合起来说明：本章遇到的每一处"跳步困难"，根源都是 $$\mathbb{R}[x]$$ 的维数无穷——这条线索会在第30章反复出现，从"柯西列走出空间"到"$$g^\flat$$ 未必是满射"，都是同一件事的不同面孔。

**交棒**：现在你已经能手算出 Cauchy–Schwarz 不等式的等号条件、平行四边形法则的成立与失效、一个具体的"柯西列却没有极限"的例子，以及一个真正的最小二乘投影（连 Gram 矩阵都解过了）。下一章会把这四件事升级成对**任意**内积空间、**任意**闭子空间都成立的一般定义与证明——正定性公理会换成复数版本的共轭对称，"有限维子空间"会换成"完备空间里的任意闭子空间"，$$Pf$$ 的存在性会从"解线性方程组"升级为"闭凸集里找最近点"（第30章 定理 3.9、3.10），而 Riesz 表示定理会告诉你：**这套"投影"的几何，恰好就是量子力学里"测量"这件事的数学骨架。**

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch28_de_Rham上同调_下.md">← 第28章 de Rham 上同调·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch30_Hilbert空间与内积结构_下.md">第30章 Hilbert 空间与内积结构·下 →</a></div>
</div>
