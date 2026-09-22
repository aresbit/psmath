---
layout: default
---

# 第59章: Möbius 群、双重覆盖与射影表示·上：预备与直觉 (The Möbius Group, Double Covers and Projective Representations · Part I: Warm-up and Intuition)

> 配套深化: 见 第60章 Möbius 群、双重覆盖与射影表示·下（完整推导），本章是它的具体铺垫，建议先读本章
> 专家依据: `_experts/algebra/representation-theory.md`（主）+ `_experts/algebra/lie-algebra-root-systems.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

本章要打磨的，是第60章开篇就会用到、但只用一两行代数就滑过去的三个"跳跃点"：

1. 为什么不同的 $$2\times2$$ 矩阵会给出同一个 Möbius 变换（第60章定理 3.2 的 (ii)、(iii) 一步到位，第一次看很难判断这是巧合还是必然）；
2. 为什么把一个实四维向量塞进一个 $$2\times2$$ Hermite 矩阵之后，矩阵的行列式恰好就是 Minkowski 长度平方（第60章定理 3.5、定理 3.6 直接给出一般公式，没有先算一两个具体向量）；
3. "同一个物理转动，两个不同的矩阵表示"这件事背后到底是什么样的代数结构——上循环 (cocycle) 第一次出现时（第60章定理 3.10）就是一般定义，没有先算一个具体例子看它长什么样。

本章不证第60章要证的一般定理，只做一件事：把这三处压缩的步骤，用具体的、可以直接验算的数字例子拆开算一遍。读完本章，你应该已经能：手算验证"矩阵乘以标量、乘以 $$-1$$ 不改变对应的 Möbius 变换"；对若干具体向量手算验证"Hermite 矩阵的行列式 $$=$$ Minkowski 长度平方"；并在一个只有 $$4$$ 个元素的具体群（$$\mathbb Z/4$$，绕固定轴转 $$90°$$ 的倍数）上，亲手算出一个"上循环"，验证它满足上循环条件，甚至把它"修好"。第60章会把这三件事分别写成定理 3.2、定理 3.6、定理 3.10——到那时，你看到的一般证明只是把这里的手算符号化。

## 二、入口：一道具体的问题 (Entry Problem)

**入口问题 A′：同一个函数，两副面孔（预热版）**

取两个具体的 $$2\times2$$ 矩阵
$$A=\begin{pmatrix}1&0\\ 1&1\end{pmatrix},\qquad B=\begin{pmatrix}2&0\\ 0&\tfrac12\end{pmatrix},$$
以及它们对应的变换 $$f_A(z)=\dfrac{1\cdot z+0}{1\cdot z+1}$$、$$f_B(z)=\dfrac{2z+0}{0\cdot z+\frac12}$$。

(1) 化简 $$f_A(z)$$、$$f_B(z)$$，再算出 $$f_A\bigl(f_B(z)\bigr)$$。
(2) 算出矩阵乘积 $$AB$$，写出 $$f_{AB}(z)$$ 的最简形式，与 (1) 的答案比较。
(3) 分别算出 $$f_{2A}(z)$$ 与 $$f_{-A}(z)$$，与 $$f_A(z)$$ 比较。你发现了什么规律？先猜，不要求证明——完整的证明留给第60章定理 3.2。

**入口问题 B′：转一个直角，还是转一整圈？**

设
$$U(\theta)=\begin{pmatrix}e^{-i\theta/2}&0\\ 0&e^{i\theta/2}\end{pmatrix}$$
（与第60章入口问题 B 相同的公式），$$R_\theta$$ 是绕固定轴转 $$\theta$$ 的空间旋转。

(1) 直接算出 $$U\bigl(\tfrac\pi2\bigr)$$，再依次算出 $$U\bigl(\tfrac\pi2\bigr)^2$$、$$U\bigl(\tfrac\pi2\bigr)^3$$、$$U\bigl(\tfrac\pi2\bigr)^4$$，把每一步的结果都写成 $$U(\cdot)$$ 的形式。
(2) 物理上，转四个直角的旋转 $$R_{\pi/2}$$ 应该回到 $$R_0=$$ 恒等。你在 (1) 里算出的 $$U\bigl(\tfrac\pi2\bigr)^4$$ 是恒等矩阵吗？

第 (2) 问的答案会让你意外：转四个直角"应该"回到原地，矩阵算出来的答案却不是 $$I$$。这不是计算错误——它正是第60章要解释的"射影表示"现象，在最小、最具体的情形里的样子；本章 3.3 节会把这件事彻底算清楚。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 标量与符号：为什么两个矩阵能给出同一个变换

先把入口问题 A′算完整。

**(1)(2) 的手算。** $$f_A(z)=\dfrac{z}{z+1}$$，$$f_B(z)=\dfrac{2z}{1/2}=4z$$。代入：
$$f_A\bigl(f_B(z)\bigr)=f_A(4z)=\frac{4z}{4z+1}.$$
矩阵乘积
$$AB=\begin{pmatrix}1&0\\ 1&1\end{pmatrix}\begin{pmatrix}2&0\\ 0&\tfrac12\end{pmatrix}=\begin{pmatrix}2&0\\ 2&\tfrac12\end{pmatrix}$$
（第一行：$$1\cdot2+0\cdot0=2$$，$$1\cdot0+0\cdot\frac12=0$$；第二行：$$1\cdot2+1\cdot0=2$$，$$1\cdot0+1\cdot\frac12=\frac12$$）。于是
$$f_{AB}(z)=\frac{2z}{2z+\frac12}=\frac{4z}{4z+1}$$
（分子分母同乘 $$2$$）。与 $$f_A(f_B(z))$$ 完全一致：**复合两个矩阵对应的变换，就是把矩阵相乘后再取对应的变换**——这是第60章定理 3.2(i) 要证的一般事实，这里先对一组具体数字验证了一遍。

**(3) 的手算。** $$2A=\begin{pmatrix}2&0\\ 2&2\end{pmatrix}$$，
$$f_{2A}(z)=\frac{2z}{2z+2}=\frac{z}{z+1}=f_A(z).$$
$$-A=\begin{pmatrix}-1&0\\ -1&-1\end{pmatrix}$$，
$$f_{-A}(z)=\frac{-z}{-z-1}=\frac{z}{z+1}=f_A(z).$$
两个都等于 $$f_A(z)$$！猜测：**把矩阵乘以任意非零标量 $$\lambda$$，对应的变换不变。**

**为什么会这样——一般证明只是把上面的约分再做一遍。** 设 $$A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$$、$$\lambda\ne0$$，则
$$f_{\lambda A}(z)=\frac{\lambda az+\lambda b}{\lambda cz+\lambda d}=\frac{\lambda(az+b)}{\lambda(cz+d)}=\frac{az+b}{cz+d}=f_A(z).$$

**命题 3.1（标量不改变 Möbius 变换）** 对任意 $$\lambda\in\mathbb C^*$$ 与可逆矩阵 $$A$$，$$f_{\lambda A}=f_A$$。

*证明* 即上面的约分，对一切使分母不为零的 $$z$$ 成立；在极点与 $$\infty$$ 处用连续延拓，两端仍相等。$$\blacksquare$$

**注 3.1（这只是"如果"的方向）** 命题 3.1 说的是"矩阵相差一个标量 $$\Rightarrow$$ 变换相同"。反过来——"变换相同 $$\Rightarrow$$ 矩阵相差一个标量"——要难得多：需要说明分式线性变换的分子分母系数几乎是唯一确定的。这是第60章定理 3.2(ii) 的内容，那里用比较多项式系数的办法证明了"当且仅当"。你现在已经从"如果"的方向对具体数字验证过它，看那个证明时会容易很多。

### 3.2 把四维向量塞进一个 $$2\times2$$ 矩阵

**记号从哪来。** 我们想让"矩阵乘法"自动算出"Lorentz 变换"，而 Lorentz 变换保持的是二次型 $$x_0^2-x_1^2-x_2^2-x_3^2$$，不是一个线性量。行列式恰好是关于矩阵元素的二次式，这提示我们：如果能把 $$(x_0,x_1,x_2,x_3)$$ 编码进一个矩阵 $$X$$，使 $$\det X$$ 正好等于这个二次型，那么"矩阵作用保持行列式"就会自动给出"变换保持 Minkowski 长度"。下面这个编码正是为此设计的：
$$X(x)=\begin{pmatrix}x_0+x_3&x_1-ix_2\\ x_1+ix_2&x_0-x_3\end{pmatrix}.$$

**先算三个具体向量，验证猜测。**

$$x=(1,0,0,0)$$：$$X=\begin{pmatrix}1&0\\ 0&1\end{pmatrix}$$，$$\det X=1$$；而 $$x_0^2-x_1^2-x_2^2-x_3^2=1$$。一致。

$$x=(0,0,0,1)$$：$$X=\begin{pmatrix}1&0\\ 0&-1\end{pmatrix}$$，$$\det X=-1$$；而 $$0-0-0-1=-1$$。一致。

$$x=(2,1,0,1)$$：$$X=\begin{pmatrix}3&1\\ 1&1\end{pmatrix}$$，$$\det X=3\cdot1-1\cdot1=2$$；而 $$4-1-0-1=2$$。一致。

三个例子都对上了，猜测：$$\det X(x)=x_0^2-x_1^2-x_2^2-x_3^2$$ 对一切 $$x$$ 成立。

**一般证明（只是展开）：**
$$\det X(x)=(x_0+x_3)(x_0-x_3)-(x_1-ix_2)(x_1+ix_2)=(x_0^2-x_3^2)-(x_1^2+x_2^2)=x_0^2-x_1^2-x_2^2-x_3^2$$
（用了 $$(x_1-ix_2)(x_1+ix_2)=x_1^2-(ix_2)^2=x_1^2+x_2^2$$）。

**定理 3.2（$$\det$$ 就是 Minkowski 长度平方，具体验证＋一般证明）** 对一切 $$x\in\mathbb R^4$$，$$\det X(x)=x_0^2-x_1^2-x_2^2-x_3^2$$。

*证明* 即上面的展开。$$\blacksquare$$

**现在让一个具体矩阵作用一次，看看会发生什么。** 取 $$A=\begin{pmatrix}\sqrt2&0\\ 0&1/\sqrt2\end{pmatrix}$$（实矩阵，故 $$A^*=A^{\mathsf T}=A$$；$$\det A=\sqrt2\cdot\frac1{\sqrt2}=1$$），作用在 $$x=(1,0,0,1)$$ 对应的 $$X=\begin{pmatrix}2&0\\ 0&0\end{pmatrix}$$ 上：
$$AXA^*=\begin{pmatrix}\sqrt2&0\\ 0&\frac1{\sqrt2}\end{pmatrix}\begin{pmatrix}2&0\\ 0&0\end{pmatrix}\begin{pmatrix}\sqrt2&0\\ 0&\frac1{\sqrt2}\end{pmatrix}=\begin{pmatrix}2\sqrt2&0\\ 0&0\end{pmatrix}\begin{pmatrix}\sqrt2&0\\ 0&\frac1{\sqrt2}\end{pmatrix}=\begin{pmatrix}4&0\\ 0&0\end{pmatrix}.$$
读出新向量：$$x_0'+x_3'=4$$，$$x_0'-x_3'=0$$，$$x_1'-ix_2'=0$$，故 $$x_1'=x_2'=0$$、$$x_0'=x_3'=2$$，即 $$x'=(2,0,0,2)$$。验证长度：原向量 $$1-0-0-1=0$$，新向量 $$4-0-0-4=0$$——都是 $$0$$（这是光锥上的一个方向，即一条"光线"），长度保持住了，向量本身却从 $$(1,0,0,1)$$ 拉伸成了 $$(2,0,0,2)$$。这正是相对论里"boost"的样子：沿 $$x_3$$ 方向的光线保持在光锥上，坐标却被拉伸了（第60章经典问题精讲题1会用一般的 $$t$$ 重做这个计算，那里你会看到本例中的 $$\sqrt2=e^{t/2}$$ 恰好对应 $$t=\ln2$$；本章练习研2 把这个计算一般化到任意 $$t$$）。

**为什么 $$AXA^*$$ 总保持 $$\det$$（一般论证，为定理 3.6 作准备）。**
$$\det(AXA^*)=\det A\cdot\det X\cdot\det A^*.$$
对 $$2\times2$$ 矩阵，$$\det(A^*)=\overline{\det A}$$（共轭转置的行列式是原行列式的共轭：转置不改变行列式，逐个元素取共轭把 $$\det A=ad-bc$$ 变成 $$\bar a\bar d-\bar b\bar c=\overline{ad-bc}$$）。故
$$\det(AXA^*)=\det A\cdot\overline{\det A}\cdot\det X=\lvert\det A\rvert^2\det X.$$
若 $$A\in\mathrm{SL}(2,\mathbb C)$$（即 $$\det A=1$$），则 $$\lvert\det A\rvert^2=1$$，于是：

**命题 3.3（$$A\in\mathrm{SL}(2,\mathbb C)$$ 时 $$AXA^*$$ 保持 $$\det$$）** 对 Hermite 矩阵 $$X$$ 与 $$A\in\mathrm{SL}(2,\mathbb C)$$，$$\det(AXA^*)=\det X$$。

*证明* 即上面的计算，取 $$\det A=1$$。$$\blacksquare$$

结合定理 3.2，$$X\mapsto AXA^*$$ 保持 $$\det X=x_0^2-x_1^2-x_2^2-x_3^2$$，也就是保持 Minkowski 长度——这正是"Lorentz 变换"的定义。第60章定理 3.6 会补上两件本节没有证的事：这个变换到底落在 $$\mathrm O(1,3)$$ 的哪个连通分支里（不是任意保长度的变换都行，还要保持时间方向），以及对应 $$\mathrm{SL}(2,\mathbb C)\to\mathrm{SO}^+(1,3)$$ 是不是**满**的——这需要一般的连通性论证，不是手算能替代的。

**注 3.3（换一种矩阵会怎样）** 上面选的 $$A$$ 是正定的实对角矩阵，给出的是"boost"。若换成酉矩阵（比如把对角元换成模长为 $$1$$ 的复数），会给出**旋转**而不是拉伸——第60章经典问题精讲题1把这两种情形放在一起比较；本章练习竞2也会算一个具体的旋转例子。

### 3.3 同一个旋转，两个矩阵：上循环长什么样

回到入口问题 B′。绕固定轴转 $$90°$$ 的旋转记作 $$R_{\pi/2}$$，转四次回到 $$R_0=\mathrm{id}$$——这四个旋转 $$\{R_0,R_{\pi/2},R_\pi,R_{3\pi/2}\}$$ 构成一个只有 $$4$$ 个元素的群，同构于 $$\mathbb Z/4$$（加法群，$$k\leftrightarrow R_{k\pi/2}$$）。

**取一组"代表矩阵"。** 对每个 $$k\in\{0,1,2,3\}$$，选
$$\rho(k):=U\Bigl(\frac{k\pi}2\Bigr)=\begin{pmatrix}e^{-ik\pi/4}&0\\ 0&e^{ik\pi/4}\end{pmatrix}$$
作为 $$R_{k\pi/2}$$ 的一个"提升"（lift）——即 $$\rho(k)$$ 在旋转群里对应的正是 $$R_{k\pi/2}$$。这不是唯一的选法（也可以选 $$-\rho(k)$$），只是任取一个代表。

**手算乘法表，看看哪里出了问题。** 因为 $$U(\theta)U(\varphi)=U(\theta+\varphi)$$ 对一切实数 $$\theta,\varphi$$ 精确成立（对角矩阵相乘、指数相加），所以
$$\rho(k)\rho(l)=U\Bigl(\frac{k\pi}2\Bigr)U\Bigl(\frac{l\pi}2\Bigr)=U\Bigl(\frac{(k+l)\pi}2\Bigr).$$
若 $$k+l\le3$$，右边就是 $$\rho(k+l)$$，两个代表矩阵的乘积正好是第三个代表矩阵，没有任何"意外"。但若 $$k+l\ge4$$（这时旋转群里 $$R_{k\pi/2}R_{l\pi/2}=R_{m\pi/2}$$，$$m=k+l-4\in\{0,1,2,3\}$$ 是 $$k+l$$ 在 $$\mathbb Z/4$$ 里的代表），情况不同：
$$U\Bigl(\frac{(k+l)\pi}2\Bigr)=U\Bigl(\frac{m\pi}2+2\pi\Bigr)=U\Bigl(\frac{m\pi}2\Bigr)U(2\pi)=\rho(m)\cdot(-I)$$
（用了 $$U(2\pi)=\mathrm{diag}(e^{-i\pi},e^{i\pi})=\mathrm{diag}(-1,-1)=-I$$，这正是入口问题 B′算出来的那个"不该出现的负号"）。

**具体验算一次。** 取 $$k=3,l=2$$（对应 $$R_{3\pi/2}\cdot R_\pi$$）：$$k+l=5\ge4$$，$$m=1$$。直接算：
$$\rho(3)\rho(2)=U\Bigl(\frac{3\pi}2\Bigr)U(\pi)=U\Bigl(\frac{5\pi}2\Bigr)=U\Bigl(\frac\pi2+2\pi\Bigr)=U\Bigl(\frac\pi2\Bigr)U(2\pi)=\rho(1)\cdot(-I)=-\rho(1).$$
而在旋转群里 $$R_{3\pi/2}R_\pi=R_{\pi/2}$$，对应代表应该是 $$\rho(1)$$——但矩阵算出来是 $$-\rho(1)$$，差了一个 $$-1$$。

**把这个差记下来，就是"上循环"。** 定义
$$c(k,l):=\begin{cases}1,&k+l\le3,\\ -1,&k+l\ge4,\end{cases}\qquad\text{使得}\quad\rho(k)\rho(l)=c(k,l)\,\rho\bigl((k+l)\bmod4\bigr).$$
这个 $$c$$ 恰好是"代表矩阵的乘积"与"代表矩阵本身"之间差的那个标量——它记录了"选定的代表矩阵"未能构成一个真正的同态这件事，差多少、在哪里差，$$c$$ 全部记着。

**定义 3.4（射影表示与上循环，预习版）** 设 $$G$$ 是群。若对每个 $$g\in G$$ 选定一个可逆矩阵 $$\rho(g)$$，使得对一切 $$g,h\in G$$ 存在标量 $$c(g,h)\ne0$$ 满足
$$\rho(g)\rho(h)=c(g,h)\,\rho(gh),$$
就说 $$\rho$$（更准确地说，$$g\mapsto[\rho(g)]$$，把矩阵看成"差一个标量"的等价类）是 $$G$$ 的一个**射影表示**，$$c$$ 是相应的**上循环**。

上面 $$\mathbb Z/4$$ 上的 $$c(k,l)$$ 就是这个一般定义在一个只有 $$4$$ 个元素的具体群上的样子。

**上循环必须满足一个"结合律"式的相容条件——具体验算两次。** 三个矩阵相乘时，先乘哪两个不应该影响最终结果，这个"不应该"翻译成 $$c$$ 的一个恒等式。取 $$g=h=k=3$$：
$$g+h=6\equiv2,\quad c(g,h)=c(3,3)=-1\ (6\ge4);\qquad c(g+h,k)=c(2,3)=-1\ (5\ge4);$$
左边 $$c(g,h)\,c(g+h,k)=(-1)(-1)=1$$。另一边
$$h+k=6\equiv2,\quad c(h,k)=c(3,3)=-1;\qquad c(g,h+k)=c(3,2)=-1\ (5\ge4);$$
右边 $$c(h,k)\,c(g,h+k)=(-1)(-1)=1$$。两边都是 $$1$$，相等。

再取 $$g=1,h=3,k=2$$：
$$g+h=4\equiv0,\quad c(1,3)=-1\ (4\ge4);\qquad c(g+h,k)=c(0,2)=1\ (2\le3);$$
左边 $$=(-1)(1)=-1$$。另一边
$$h+k=5\equiv1,\quad c(h,k)=c(3,2)=-1\ (5\ge4);\qquad c(g,h+k)=c(1,1)=1\ (2\le3);$$
右边 $$=(-1)(1)=-1$$。两边都是 $$-1$$，相等。

**命题 3.5（$$\mathbb Z/4$$ 上循环满足相容条件）** 上面定义的 $$c$$ 对一切 $$g,h,k\in\mathbb Z/4$$ 满足
$$c(g,h)\,c(g+h,k)=c(h,k)\,c(g,h+k).$$

*证明思路* 两边都等于 $$\dfrac{\rho(g)\rho(h)\rho(k)}{\rho(g+h+k)}$$（把矩阵结合律 $$(\rho(g)\rho(h))\rho(k)=\rho(g)(\rho(h)\rho(k))$$ 两边各自用定义 3.4 展开两次，标量部分自动相等）——这正是第60章定理 3.10 里 (60.2) 式的证明思路，这里先对 $$\mathbb Z/4$$ 手算验证了两组三元组，一般证明只是把手算的括号搬到符号里。$$\blacksquare$$

**注 3.5（这个具体的 $$c$$ 能不能被"修好"）** 你可能会问：既然 $$c$$ 不恒为 $$1$$，是不是就说明"转 $$90°$$ 的旋转群"天生没法用普通（非射影）的矩阵表示？对这个**有限循环群**而言，答案是否定的——换一组代表矩阵，就能把 $$c$$ 全部变成 $$1$$。第五节题3会具体演算怎么换；本章练习研1把这件事对任意 $$\mathbb Z/n$$ 证到底，第60章练习竞3则对任意有限循环群重新证一遍。但对**真正的**转动群 $$\mathrm{SO}(3)$$（它不是循环群，是一个连通的连续群），同样的修补办法会失败——这正是第60章定理 3.12 要证明的：自旋 $$1/2$$ 的射影表示**不可**线性化。本章只到"有限群总能修好"为止；"连续群可能修不好"是下一章的正题。

## 四、几何与物理直觉 (Intuition)

### 4.1 分数约分：标量歧义的日常版本

命题 3.1 说"矩阵乘以标量不改变对应的 Möbius 变换"，这和小学就学过的一件事是同一回事：分数 $$\dfrac24$$ 与 $$\dfrac12$$ 是同一个数，因为分子分母同时乘了 $$2$$。矩阵 $$A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$$ 就像是把"分式线性变换"的分子 $$az+b$$、分母 $$cz+d$$ 的系数打包放在一起；乘一个标量就是"分子分母同时扩分/约分"，变换本身（这个"数"）不变。第60章把"所有能约分成同一个变换的矩阵"打包成一个等价类，起名叫 $$\mathrm{PGL}(2,\mathbb C)$$——这和"所有能约分成 $$\frac12$$ 的分数"打包成一个等价类是同一个思路。

### 4.2 一张"身份证"：行列式作为不变的编号

Hermite 矩阵 $$X(x)$$ 把一个四维时空点变成一张 $$2\times2$$ 的表格，而 $$\det X(x)$$ 是这张表格上一个"刻死了"的数字：不管你用哪个 $$A\in\mathrm{SL}(2,\mathbb C)$$ 去搅动这张表格（$$X\mapsto AXA^*$$），这个数字都不变——就像一张身份证被复印、被折叠、被各种方式传阅，证件号码本身却是不变的编号。物理学家管这个"不变编号"叫 Minkowski 长度平方；命题 3.3 已经用具体数字验证过一次：搅动前后行列式都没变。

### 4.3 转盘与皮带：为什么"转一整圈"不总是回到原地

想象一个转盘，盘面上画着一个箭头。转盘本身转一整圈（$$360°$$）当然回到原来的样子——这是入口问题 B′里"物理旋转 $$R_{2\pi}=R_0$$"说的那件事。但如果箭头上还系了一根皮带，皮带的另一头固定在转盘外面，转盘转一整圈后，皮带会打上一个结，需要转**两整圈**才能把结解开——转盘本身"看起来"回到了原处，但皮带记录了转盘"走过的路"。$$U(\theta)$$ 这个矩阵就像那根皮带：它记录的不只是转盘现在指向哪，还记录了"走了多远"；$$U(2\pi)=-I\ne I$$ 正是"皮带打了结"的代数说法，而 3.3 节里那个上循环 $$c(k,l)$$，记的正是"结"出现在哪一步相乘上。第60章 4.2 节会把这个直觉与"$$\mathrm{SU}(2)$$ 是 $$\mathrm{SO}(3)$$ 的双重覆叠"这一严格陈述对齐。

## 五、经典问题精讲 (Classical Problems)

### 题 1：矩阵求逆，对应函数求逆

**题目**：设 $$C=\begin{pmatrix}2&1\\ 1&1\end{pmatrix}$$。求 $$C^{-1}$$，写出 $$f_{C^{-1}}(z)$$，并验证 $$f_C\bigl(f_{C^{-1}}(z)\bigr)=z$$。

**解**：$$\det C=2\cdot1-1\cdot1=1$$，故 $$C^{-1}=\begin{pmatrix}1&-1\\ -1&2\end{pmatrix}$$（$$2\times2$$ 矩阵求逆公式：交换主对角、副对角变号，再除以行列式；这里行列式是 $$1$$）。验算 $$CC^{-1}=\begin{pmatrix}2\cdot1+1\cdot(-1)&2\cdot(-1)+1\cdot2\\ 1\cdot1+1\cdot(-1)&1\cdot(-1)+1\cdot2\end{pmatrix}=\begin{pmatrix}1&0\\ 0&1\end{pmatrix}$$。

$$f_C(z)=\dfrac{2z+1}{z+1}$$，$$f_{C^{-1}}(z)=\dfrac{z-1}{-z+2}$$。代入：

$$f_C\bigl(f_{C^{-1}}(z)\bigr)=\dfrac{2\cdot\frac{z-1}{2-z}+1}{\frac{z-1}{2-z}+1}=\dfrac{2(z-1)+(2-z)}{(z-1)+(2-z)}=\dfrac{2z-2+2-z}{z-1+2-z}=\dfrac{z}{1}=z.$$

$$\blacksquare$$ 这不是巧合：命题 3.1 与 $$CC^{-1}=I$$ 合起来就保证了 $$f_{C^{-1}}$$ 是 $$f_C$$ 的复合逆——第60章把"$$\mathrm{GL}(2,\mathbb C)$$ 模去标量" 组织成一个**群**，靠的正是这条。

### 题 2：换一对光锥外的向量，再核验一次 $$\det=$$ 长度平方

**题目**：取 $$x=(3,1,2,0)$$。写出 $$X(x)$$，算出 $$\det X(x)$$，并与 $$x_0^2-x_1^2-x_2^2-x_3^2$$ 比较。

**解**：$$X(x)=\begin{pmatrix}x_0+x_3&x_1-ix_2\\ x_1+ix_2&x_0-x_3\end{pmatrix}=\begin{pmatrix}3&1-2i\\ 1+2i&3\end{pmatrix}$$（$$x_3=0$$，故对角两元都是 $$3$$）。

$$\det X=3\cdot3-(1-2i)(1+2i)=9-(1-(2i)^2)=9-(1+4)=9-5=4.$$

而 $$x_0^2-x_1^2-x_2^2-x_3^2=9-1-4-0=4$$。一致。$$\blacksquare$$（这个 $$x$$ 满足 $$x_0^2>x_1^2+x_2^2+x_3^2$$，即"类时"——练习基2 再核验一个"类空"的例子。）

### 题 3：把 $$\mathbb Z/4$$ 上的上循环修好

**题目**：3.3 节算出 $$\rho(k)=U(k\pi/2)$$ 满足 $$\rho(k)\rho(l)=c(k,l)\rho\bigl((k+l)\bmod4\bigr)$$，其中 $$c(k,l)=-1$$（当 $$k+l\ge4$$）或 $$1$$（否则）。找一组新的代表矩阵 $$\rho'(k)=\lambda_k\rho(k)$$（$$\lambda_k\ne0$$ 是标量，$$\lambda_0=1$$），使得 $$\rho'(k)\rho'(l)=\rho'\bigl((k+l)\bmod4\bigr)$$**恰好**成立（上循环变成恒 $$1$$）。

**解**：**先猜 $$\lambda_k$$ 该满足什么方程。** 代入待定的 $$\rho'(k)=\lambda_k\rho(k)$$：

$$\rho'(k)\rho'(l)=\lambda_k\lambda_l\,\rho(k)\rho(l)=\lambda_k\lambda_l\,c(k,l)\,\rho\bigl((k+l)\bmod4\bigr).$$

要让这等于 $$\rho'\bigl((k+l)\bmod4\bigr)=\lambda_{(k+l)\bmod4}\,\rho\bigl((k+l)\bmod4\bigr)$$，只需

$$\lambda_k\lambda_l\,c(k,l)=\lambda_{(k+l)\bmod4}. \tag{★}$$

**试探 $$\lambda_k=e^{ik\pi/4}$$。** 逐一核验 (★)（$$k,l\in\{0,1,2,3\}$$，共 $$10$$ 组无序对，这里挑最关键的两组，其余同法）：

- $$k=l=1$$：$$c(1,1)=1$$（$$1+1=2\le3$$）。左边 $$=e^{i\pi/4}e^{i\pi/4}\cdot1=e^{i\pi/2}$$；右边 $$\lambda_2=e^{i2\pi/4}=e^{i\pi/2}$$。相等。
- $$k=l=2$$：$$c(2,2)=-1$$（$$4\ge4$$）。左边 $$=e^{i\pi/2}e^{i\pi/2}\cdot(-1)=e^{i\pi}\cdot(-1)=(-1)(-1)=1$$；右边 $$\lambda_0=1$$。相等。

（其余 $$8$$ 组——$$(0,l)$$ 四组、$$(1,2),(1,3),(2,3),(3,3)$$——用完全相同的代入方式逐一核验，全部满足 (★)；读者可自行补完，这是 §六 竞1 的内容之一。）

**化简 $$\rho'(k)$$，看清它的真面目。**

$$\rho'(k)=e^{ik\pi/4}\begin{pmatrix}e^{-ik\pi/4}&0\\ 0&e^{ik\pi/4}\end{pmatrix}=\begin{pmatrix}1&0\\ 0&e^{ik\pi/2}\end{pmatrix}=\begin{pmatrix}1&0\\ 0&i^k\end{pmatrix}$$

（用了 $$e^{i\pi/2}=i$$）。于是 $$\rho'(0)=I,\ \rho'(1)=\mathrm{diag}(1,i),\ \rho'(2)=\mathrm{diag}(1,-1),\ \rho'(3)=\mathrm{diag}(1,-i)$$——这正是 $$\mathbb Z/4$$ 的一个**普通**（非射影）表示：$$\rho'(k)\rho'(l)=\mathrm{diag}\bigl(1,i^{k+l}\bigr)=\mathrm{diag}\bigl(1,i^{(k+l)\bmod4}\bigr)=\rho'\bigl((k+l)\bmod4\bigr)$$，因为 $$i^4=1$$ 把多出来的整数圈自动吃掉了。$$\blacksquare$$

**为什么这不违反物理直觉。** $$\rho(k)$$ 与 $$\rho'(k)$$ 描述的是**同一个**物理转动 $$R_{k\pi/2}$$——差一个标量的矩阵对应同一个 $$SO(3)$$ 元素（这正是 $$SU(2)\to SO(3)$$ 这类"双重覆盖"映射的核心机制：核是 $$\{\pm1\}$$ 或更一般的标量）。3.3 节选的 $$\rho(k)=U(k\pi/2)$$ 只是**恰好选了一组"坏"的代表**，换一组"好"的代表 $$\rho'(k)$$，射影现象就消失了——这正是"有限群的射影表示总能拉直"这条一般定理（练习研1 会把这个方法对任意 $$\mathbb Z/n$$ 重做一遍）在具体数字上的样子。

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 设 $$D=\begin{pmatrix}1&2\\ 0&1\end{pmatrix}$$。写出 $$f_D(z)$$，并验证 $$f_{5D}(z)=f_D(z)$$。

**基2.** 取 $$x=(1,2,0,0)$$（满足 $$x_1^2+x_2^2+x_3^2>x_0^2$$，即"类空"）。写出 $$X(x)$$，算出 $$\det X(x)$$，并与 $$x_0^2-x_1^2-x_2^2-x_3^2$$ 比较（结果应为负数）。

**基3.** 直接验证 $$U(\pi/3)U(\pi/6)=U(\pi/2)$$（把两个对角矩阵相乘、比较指数）。

**基4.** 用 3.3 节的公式，直接算出 $$\rho(1)\rho(3)$$（$$k=1,l=3$$），并验证结果是 $$-\rho(0)=-I$$。

### 竞赛（本课目标难度）

**竞1.** 补完题3里没有验算的 $$8$$ 组 $$(k,l)$$，确认 $$\lambda_k=e^{ik\pi/4}$$ 对**一切** $$k,l\in\{0,1,2,3\}$$ 都满足 (★)。

**竞2.** 取 $$A=\begin{pmatrix}e^{i\pi/4}&0\\ 0&e^{-i\pi/4}\end{pmatrix}$$（酉矩阵，$$\det A=1$$）。对 $$x=(0,1,0,0)$$（即 $$X=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$$），算出 $$AXA^*$$，读出新向量 $$x'$$，并指出这是绕哪个方向转了多少度（提示：与 §五 题2 对比，$$A$$ 是酉矩阵而非正定实矩阵，$$注 3.3$$ 说这会给出旋转而不是拉伸）。

**竞3.** 取 $$A=\begin{pmatrix}2&0\\ 0&1\end{pmatrix}$$（**不属于** $$\mathrm{SL}(2,\mathbb C)$$，$$\det A=2$$）。对 $$x=(1,0,0,0)$$（$$X=I$$），算出 $$AXA^*$$ 与 $$\det(AXA^*)$$，并验证它等于 $$\lvert\det A\rvert^2\det X$$，而**不**等于 $$\det X$$——说明为什么 3.2 节要求 $$A\in\mathrm{SL}(2,\mathbb C)$$（而不是任意可逆矩阵）才能保长度。

### 研究（通向下一章）

**研1.** 把题3的方法对一般的 $$\mathbb Z/n$$（$$n\ge2$$）重做一遍：取 $$\rho(k)=U(2\pi k/n)$$（$$k=0,\dots,n-1$$），写出对应的上循环 $$c(k,l)$$，猜出并验证一组 $$\lambda_k$$ 使 $$\rho'(k):=\lambda_k\rho(k)$$ 满足 $$\rho'(k)\rho'(l)=\rho'\bigl((k+l)\bmod n\bigr)$$ 恰好成立。

**研2.** 把 3.2 节"$$\sqrt2$$"那个具体的 boost 换成一般参数：取 $$A(t)=\begin{pmatrix}e^{t/2}&0\\ 0&e^{-t/2}\end{pmatrix}$$（$$t\in\mathbb R$$），对 $$x=(1,0,0,1)$$（$$X=\begin{pmatrix}2&0\\ 0&0\end{pmatrix}$$），算出 $$A(t)XA(t)^*$$ 对应的新向量 $$x'(t)$$，并验证对**一切** $$t$$ 都有 $$x_0'^2-x_3'^2=x_0^2-x_3^2$$（$$0=0$$）。取 $$t=\ln2$$，核对是否与 3.2 节里 $$A=\mathrm{diag}(\sqrt2,1/\sqrt2)$$ 算出的 $$x'=(2,0,0,2)$$ 一致。

### 解答 (Solutions)

**解 基1.** $$f_D(z)=\dfrac{z+2}{1}=z+2$$（$$c=0,d=1$$，分母恒为 $$1$$）。$$5D=\begin{pmatrix}5&10\\ 0&5\end{pmatrix}$$，$$f_{5D}(z)=\dfrac{5z+10}{5}=z+2=f_D(z)$$。$$\blacksquare$$

**解 基2.** $$x=(x_0,x_1,x_2,x_3)=(1,2,0,0)$$，故 $$x_0+x_3=1$$，$$x_0-x_3=1$$，$$x_1-ix_2=2$$，$$x_1+ix_2=2$$（$$x_2=0$$，不出现虚部）。

$$X(x)=\begin{pmatrix}1&2\\ 2&1\end{pmatrix},\qquad\det X=1\cdot1-2\cdot2=1-4=-3.$$

而 $$x_0^2-x_1^2-x_2^2-x_3^2=1-4-0-0=-3$$。一致（负数，"类空"）。$$\blacksquare$$

**解 基3.** $$U(\pi/3)=\mathrm{diag}(e^{-i\pi/6},e^{i\pi/6})$$，$$U(\pi/6)=\mathrm{diag}(e^{-i\pi/12},e^{i\pi/12})$$。乘积对角元相加：$$e^{-i\pi/6}e^{-i\pi/12}=e^{-i(\pi/6+\pi/12)}=e^{-i\pi/4}$$（$$\pi/6+\pi/12=2\pi/12+\pi/12=3\pi/12=\pi/4$$），同理另一元为 $$e^{i\pi/4}$$。而 $$U(\pi/2)=\mathrm{diag}(e^{-i\pi/4},e^{i\pi/4})$$，一致。$$\blacksquare$$

**解 基4.** 由 3.3 节公式（$$k+l=4\ge4$$）：$$\rho(1)\rho(3)=U(\pi/2)U(3\pi/2)=U(2\pi)=\mathrm{diag}(e^{-i\pi},e^{i\pi})=\mathrm{diag}(-1,-1)=-I=-\rho(0)$$。$$\blacksquare$$

**解 竞1.** 逐组代入 (★)（记 $$\omega:=e^{i\pi/4}$$，故 $$\lambda_k=\omega^k$$，$$\omega^8=1$$）：

- $$(0,0),(0,1),(0,2),(0,3)$$：$$c(0,l)=1$$（$$0+l\le3$$），左边 $$=\omega^0\omega^l\cdot1=\omega^l$$，右边 $$=\lambda_l=\omega^l$$，恒等（$$\lambda_0=\omega^0=1$$ 自动满足）。
- $$(1,2)$$：$$c=1$$（$$3\le3$$）。左边 $$\omega^1\omega^2=\omega^3$$；右边 $$\lambda_3=\omega^3$$。相等。
- $$(1,3)$$：$$c=-1$$（$$4\ge4$$）。左边 $$\omega^1\omega^3\cdot(-1)=\omega^4\cdot(-1)$$；$$\omega^4=e^{i\pi}=-1$$，故左边 $$=(-1)(-1)=1$$；右边 $$\lambda_0=1$$（因为 $$(1+3)\bmod4=0$$）。相等。
- $$(2,3)$$：$$c=-1$$（$$5\ge4$$）。左边 $$\omega^2\omega^3\cdot(-1)=\omega^5\cdot(-1)$$；$$\omega^5=\omega^4\cdot\omega=-\omega$$，故左边 $$=(-\omega)(-1)=\omega$$；右边 $$\lambda_1=\omega$$（$$(2+3)\bmod4=1$$）。相等。
- $$(3,3)$$：$$c=-1$$（$$6\ge4$$）。左边 $$\omega^3\omega^3\cdot(-1)=\omega^6\cdot(-1)$$；$$\omega^6=\omega^4\omega^2=-\omega^2=-i$$，故左边 $$=(-i)(-1)=i=\omega^2$$；右边 $$\lambda_2=\omega^2=i$$（$$(3+3)\bmod4=2$$）。相等。

连同正文已验的 $$(1,1),(2,2)$$，共 $$10$$ 组全部满足 (★)。$$\blacksquare$$

**解 竞2.** $$A^*=\begin{pmatrix}e^{-i\pi/4}&0\\ 0&e^{i\pi/4}\end{pmatrix}$$（$$A$$ 对角，共轭转置就是逐元素取共轭）。

$$AX=\begin{pmatrix}e^{i\pi/4}&0\\ 0&e^{-i\pi/4}\end{pmatrix}\begin{pmatrix}0&1\\ 1&0\end{pmatrix}=\begin{pmatrix}0&e^{i\pi/4}\\ e^{-i\pi/4}&0\end{pmatrix}.$$

$$(AX)A^*=\begin{pmatrix}0&e^{i\pi/4}\\ e^{-i\pi/4}&0\end{pmatrix}\begin{pmatrix}e^{-i\pi/4}&0\\ 0&e^{i\pi/4}\end{pmatrix}=\begin{pmatrix}0&e^{i\pi/4}e^{i\pi/4}\\ e^{-i\pi/4}e^{-i\pi/4}&0\end{pmatrix}=\begin{pmatrix}0&e^{i\pi/2}\\ e^{-i\pi/2}&0\end{pmatrix}=\begin{pmatrix}0&i\\ -i&0\end{pmatrix}.$$

读出 $$x'$$：$$x_0'+x_3'=0$$，$$x_0'-x_3'=0\Rightarrow x_0'=x_3'=0$$；$$x_1'-ix_2'=i\Rightarrow x_1'=0,\ x_2'=-1$$（验证 $$x_1'+ix_2'=0+i(-1)=-i$$，与矩阵左下角一致）。故 $$x'=(0,0,-1,0)$$。

原向量 $$x=(0,1,0,0)$$ 指向 $$x_1$$ 轴，新向量指向 $$-x_2$$ 轴——**$$x_1$$ 轴转到了 $$-x_2$$ 轴**，这是 $$(x_1,x_2)$$ 平面里的 $$90°$$ 旋转（$$x_0,x_3$$ 分量始终为 $$0$$，不参与）。$$A$$ 的相位是 $$\pi/4$$（"半角"），对应的物理转角是 $$2\times45°=90°$$——与"半角"规律一致（§五 题2 的注 3.4 已经预告过这个倍角关系）。核验长度：$$\det X=0-1=-1$$；$$\det X'=0-i(-i)=0-1=-1$$，保持。$$\blacksquare$$

**解 竞3.** $$X=I$$，$$A^*=A$$（$$A$$ 是实对角矩阵）。$$AXA^*=AA=\begin{pmatrix}4&0\\ 0&1\end{pmatrix}$$。$$\det(AXA^*)=4$$。

而 $$\lvert\det A\rvert^2\det X=2^2\cdot1=4$$——两者相等，**但这个 $$4$$ 不等于 $$\det X=1$$**：$$X\mapsto AXA^*$$ 并没有保持行列式。读出对应向量：原 $$x=(1,0,0,0)$$（长度 $$1$$）；新向量由 $$AXA^*=\mathrm{diag}(4,1)$$ 读出 $$x_0'+x_3'=4,\ x_0'-x_3'=1$$，解得 $$x_0'=2.5,\ x_3'=1.5$$，长度 $$x_0'^2-x_3'^2=6.25-2.25=4\ne1$$——长度被放大了 $$4=\lvert\det A\rvert^2$$ 倍。**这正是命题 3.3 的证明里 $$\det(AXA^*)=\lvert\det A\rvert^2\det X$$ 这一步的意义**：只有 $$\lvert\det A\rvert=1$$（尤其是 $$\det A=1$$，$$A\in\mathrm{SL}(2,\mathbb C)$$）才能保证 Minkowski 长度不变；一般的可逆矩阵只保证长度按 $$\lvert\det A\rvert^2$$ 这个固定比例缩放。$$\blacksquare$$

**解 研1.** 记 $$\zeta:=e^{2\pi i/n}$$（$$n$$ 次单位根）。$$\rho(k)=U(2\pi k/n)=\mathrm{diag}\bigl(\zeta^{-k/2},\zeta^{k/2}\bigr)$$——更方便的写法是直接用角度：$$\rho(k)=\mathrm{diag}\bigl(e^{-ik\pi/n},e^{ik\pi/n}\bigr)$$。同 3.3 节的推导：

$$\rho(k)\rho(l)=U\Bigl(\frac{(k+l)\pi}n\Bigr)\qquad\text{（角度直接相加）}.$$

若 $$k+l<n$$，这就是 $$\rho(k+l)$$；若 $$k+l\ge n$$，则 $$\dfrac{(k+l)\pi}n=\dfrac{(k+l-n)\pi}n+\pi$$，故

$$\rho(k)\rho(l)=U\Bigl(\frac{(k+l-n)\pi}n\Bigr)U(\pi)=\rho\bigl((k+l)\bmod n\bigr)\cdot\mathrm{diag}(e^{-i\pi},e^{i\pi})=-\rho\bigl((k+l)\bmod n\bigr)$$

（注意 $$U(\pi)=\mathrm{diag}(-1,-1)=-I$$——**和 $$n$$ 无关，这是因为 $$U$$ 的周期永远是 $$4\pi$$，与 $$n$$ 无关，$$n$$ 只决定"多大的 $$k$$ 才会跨过一圈"）。故 $$c(k,l)=1$$（$$k+l<n$$）或 $$-1$$（$$k+l\ge n$$）——与 3.3 节 $$n=4$$ 的情形逐字相同，只是判据里的 $$4$$ 换成了 $$n$$。

**猜 $$\lambda_k$$。** 仿照题3，试 $$\lambda_k:=e^{ik\pi/n}$$。则

$$\rho'(k):=\lambda_k\rho(k)=e^{ik\pi/n}\mathrm{diag}\bigl(e^{-ik\pi/n},e^{ik\pi/n}\bigr)=\mathrm{diag}\bigl(1,e^{2ik\pi/n}\bigr)=\mathrm{diag}(1,\zeta^k).$$

验证：$$\rho'(k)\rho'(l)=\mathrm{diag}\bigl(1,\zeta^{k+l}\bigr)$$。由 $$\zeta^n=1$$，$$\zeta^{k+l}=\zeta^{(k+l)\bmod n}\cdot\zeta^{n\lfloor(k+l)/n\rfloor}=\zeta^{(k+l)\bmod n}\cdot1$$，故 $$\rho'(k)\rho'(l)=\mathrm{diag}\bigl(1,\zeta^{(k+l)\bmod n}\bigr)=\rho'\bigl((k+l)\bmod n\bigr)$$，**恰好**成立，上循环被拉直为恒 $$1$$。$$\blacksquare$$（$$n=4$$ 时 $$\zeta=i$$，$$\rho'(k)=\mathrm{diag}(1,i^k)$$，与题3完全一致——题3是本题的特例。）

**解 研2.** $$A(t)^*=A(t)$$（实对角矩阵）。$$A(t)XA(t)^*=\mathrm{diag}(e^{t/2},e^{-t/2})\begin{pmatrix}2&0\\ 0&0\end{pmatrix}\mathrm{diag}(e^{t/2},e^{-t/2})=\begin{pmatrix}2e^{t/2}&0\\ 0&0\end{pmatrix}\mathrm{diag}(e^{t/2},e^{-t/2})=\begin{pmatrix}2e^{t}&0\\ 0&0\end{pmatrix}.$$

读出：$$x_0'+x_3'=2e^t,\ x_0'-x_3'=0\Rightarrow x_0'=x_3'=e^t$$，$$x_1'=x_2'=0$$。即 $$x'(t)=(e^t,0,0,e^t)$$。

验证长度不变：$$x_0'^2-x_3'^2=e^{2t}-e^{2t}=0$$，与原长度 $$x_0^2-x_3^2=1-1=0$$ 一致，对**一切** $$t\in\mathbb R$$ 成立（这条光线永远留在光锥上，只是沿着它被拉伸或压缩）。

取 $$t=\ln2$$：$$e^t=2$$，$$x'(\ln2)=(2,0,0,2)$$——与 3.2 节用 $$A=\mathrm{diag}(\sqrt2,1/\sqrt2)$$（即 $$e^{t/2}=\sqrt2\Rightarrow t=\ln2$$）算出的结果完全一致。$$\blacksquare$$ 这就是 boost 参数 $$t$$（**快度, rapidity**）的由来：它比速度 $$v$$ 更自然的地方在于，两个 boost 复合时快度**直接相加**（$$A(t_1)A(t_2)=A(t_1+t_2)$$，与 $$U(\theta)$$ 的角度相加是同一个代数结构，只是 $$i\theta$$ 换成了实数 $$t$$）——第60章会把这个观察系统化。

## 七、Takeaway 与延伸 (Takeaways)

1. **"矩阵模去标量"这件事，贯穿了本章的每一节，不是孤立的技巧。** §3.1 说它让 Möbius 变换有歧义（题1 用求逆又核验了一次）；§3.2 说它恰好是 $$\mathrm{SL}(2,\mathbb C)$$（限定 $$\det=1$$）存在的理由（竞3 反过来演示了"不限定"会发生什么）；§3.3 说它是"射影表示"现象的根源。三处表面上不相关的"跳步"，其实是同一件事的三张脸——第60章会把它们统一成 $$\mathrm{PGL}(2,\mathbb C)$$、$$\mathrm{SL}(2,\mathbb C)\to\mathrm{SO}^+(1,3)$$、$$H^2(G,\mathbb C^*)$$ 这三个看似不同的对象，但本章已经让你在数字层面看到它们共享的机制。

2. **行列式不是任意选的公式，是"用代数量编码几何不变量"这个想法的具体实现。** $$\det X(x)=$$ Minkowski 长度平方（定理 3.2），$$\det(AXA^*)=\lvert\det A\rvert^2\det X$$（竞3 具体验证了 $$\det A\ne1$$ 时会发生什么），两条合在一起才逼出"为什么偏偏要 $$\mathrm{SL}(2,\mathbb C)$$"——这是"用一个好记号，让该证的定理自动成立"的典型例子。

3. **上循环 $$c(g,h)$$ 不是抽象定义凭空冒出来的记号，它就是"选定的代表矩阵未能构成同态"这件事本身，写成了一个函数。** 题3、竞1、研1 把 $$\mathbb Z/4$$（以及一般的 $$\mathbb Z/n$$）上的这个"未能"**修好**了——这也是一条一般规律的具体样本：**有限群的射影表示，总能通过换一组代表消掉上循环**（因为 $$\mathbb C^*$$ "足够大、足够可除"）。第60章定理 3.12 会说明：这条规律对**连续**群（比如真正的 $$SO(3)$$）不成立，$$SU(2)\to SO(3)$$ 的"半整数自旋"现象正是这条规律失效之后剩下的东西。

4. **快度（研2 里的参数 $$t$$）与角度 $$\theta$$ 是同一个代数结构的两个化身。** $$U(\theta)U(\varphi)=U(\theta+\varphi)$$ 与 $$A(t_1)A(t_2)=A(t_1+t_2)$$ 形式完全相同，只差 $$i\theta$$ 换成实数 $$t$$——这正是"旋转"与"boost"作为 $$\mathrm{SL}(2,\mathbb C)$$ 里两族单参数子群，代数上何其相似的原因，第60章会把两者统一在同一个 Lie 代数 $$\mathfrak{sl}(2,\mathbb C)$$ 里。

5. **"转一整圈不回家、转两整圈才回家"（入口问题 B′）不是量子力学专属的怪现象，它是一个纯代数事实，在只有 $$4$$ 个元素的最小例子里就能看得一清二楚。** 这是本章最重要的直觉：读完第60章严格的覆叠空间论证之后，回头看这个 $$\mathbb Z/4$$ 的小例子，会发现那里的每一步——道路提升、同伦提升、核的计算——本章都已经用手算走过一遍了。

**下一章的悬念。** 本章处理的都是**离散**或**具体单点**的情形：一对矩阵、几个具体向量、一个 $$4$$ 元素的循环群。第60章要问的是**一般**的问题：对**任意** $$A,B\in\mathrm{SL}(2,\mathbb C)$$，$$f_A=f_B$$ 到底何时成立（定理 3.2 的完整证明，不只是"如果"的方向）？$$\mathrm{SL}(2,\mathbb C)\to\mathrm{SO}^+(1,3)$$ 是不是**处处**满射、核**恰好**是 $$\{\pm1\}$$（定理 3.6）？**连续**群 $$SU(2)$$ 的射影表示，是不是像 $$\mathbb Z/4$$ 一样总能修好（定理 3.10、3.12——答案是"不能"，这正是"自旋"存在的代数原因）？本章的每一个具体计算，都是第60章对应定理的一个样本点。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch58_Clifford代数与Lorentz群_下.md">← 第58章 Clifford 代数与 Lorentz 群·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch60_Möbius群_双重覆盖与射影表示_下.md">第60章 Möbius 群、双重覆盖与射影表示·下 →</a></div>
</div>
