---
layout: default
---

# 第43章: 正则对易关系与 Stone–von Neumann·上：预备与直觉 (Canonical Commutation Relations and Stone–von Neumann · Part I: Warm-up and Intuition)

> 配套深化: 见 第44章 正则对易关系与 Stone–von Neumann·下（完整推导），本章是它的具体铺垫，建议先读本章
> 专家依据: `_experts/analysis/spectral-theory.md`（主）+ `_experts/analysis/functional-analysis.md`（主）；`_experts/algebra/lie-algebra-root-systems.md`（对易子的代数侧）
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

第44章要在很短的篇幅里做四件事：证明位置与动量不可能同时有界；把 $$[X,P]=i\hbar$$ 指数化成 Weyl 关系；证明满足 Weyl 关系的不可约实现只有一种（Stone–von Neumann 定理）；并且不断在这些结论之间反复压缩步骤。对"认真的普通自学者"来说，最容易卡住的四个地方是：(i) "不可能同时有界"这件事，靠的是一个跟直觉不太搭边的迹或预解式论证；(ii) 对易子 $$[X,P]=i\hbar$$ 与酉算子的 Weyl 关系之间那个 Baker–Campbell–Hausdorff 的"截断"是怎么来的；(iii) 谐振子的升降算子 $$a,a^\dagger$$ 是怎么"凭空"从 $$X,P$$ 里造出来、又怎么满足 $$[a,a^\dagger]=1$$ 的；(iv) "不可约 Weyl 系统只有一种"这句话到底在说什么，为什么"与所有对称都交换的算子只能是标量"这件事能推出唯一性。

本章的任务，就是把这四处提前在小得多、算得动的对象上做一遍手算：$$2\times2$$、$$3\times3$$ 矩阵，多项式空间上的乘法与求导，$$\hbar=m=\omega=1$$ 的具体谐振子，以及一对 $$2\times2$$ 矩阵充当的"玩具版" Weyl 系统。做完这一章，你应该已经能不查书就写出 $$[a,a^\dagger]=1$$ 的完整展开、能用手验证一个 $$2\times2$$ 矩阵的交换子只能是标量、也已经亲眼见过一个"关系式决定实现（差一个基变换）"的真实例子——第44章要做的，只是把这一切搬到无穷维、连续参数的世界里，并且证明它对任意情形都成立。

## 二、入口：一道具体的问题 (Entry Problem)

**小题（预热版，不要求证明，只要求算/猜）**

**(1)** 试着找两个 $$2\times2$$ 复矩阵 $$A,B$$，使 $$AB-BA=I$$。可以先试试
$$A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad B=\begin{pmatrix}0&0\\1&0\end{pmatrix},$$
算出 $$AB-BA$$ 到底是什么。再换几组别的 $$2\times2$$ 矩阵试试——你能找到一组让 $$AB-BA=I$$ 成立吗？（不要求证明"不存在"，只要求你自己试到怀疑"这大概不存在"。）

**(2)** 在多项式构成的空间上，令 $$(Xf)(t)=t\,f(t)$$（乘 $$t$$）、$$(Df)(t)=f'(t)$$（求导）。对 $$f(t)=t^{2}$$ 和 $$f(t)=t^{3}$$ 分别算出
$$(XD-DX)f(t),$$
然后猜一个对**所有**多项式 $$f$$ 都成立的一般公式。

**(3)** 取两个 $$2\times2$$ 矩阵
$$U_0=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad V_0=\begin{pmatrix}0&1\\1&0\end{pmatrix}.$$
算出 $$U_0V_0$$ 与 $$V_0U_0$$，比较它们——你会发现一个非常干净的关系（一个符号）。现在问本章真正想问的问题：**如果我只告诉你"两个矩阵满足这个关系式"，不告诉你它们具体长什么样，你能不能保证它们（在换一个基之后）就是 $$U_0,V_0$$ 本身？换一组满足同样关系式的矩阵，会不会本质上是"同一对矩阵"换了个坐标系？**

第 (1)(2) 问你已经在用手确认"位置与动量不可能同时有界"和"对易子"这两件事到底是什么感觉；第 (3) 问是 Stone–von Neumann 定理最简化的影子——本章第三节会把它做完整，第44章会把它搬到 $$L^2(\mathbb R)$$ 上、连续参数、无穷维的一般情形。

## 三、结构：定义与完整推导 (Structure & Proof)

本节挑出第44章里四处最容易让人"卡住"的地方，每一处都先算 2–3 个具体例子，再抽象成一般定义或命题。

**有界性为什么不可能：从 $$2\times2$$ 矩阵开始**

先把入口题 (1) 做完。取 $$A,B$$ 是**任意** $$2\times2$$ 矩阵。关键工具是**迹的循环性**：$$\operatorname{tr}(AB)=\operatorname{tr}(BA)$$。用入口题里的具体 $$A,B$$ 验证一下：
$$AB=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad BA=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad AB-BA=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\neq I.$$
但注意 $$\operatorname{tr}(AB)=1$$、$$\operatorname{tr}(BA)=1$$，确实相等——这不是巧合。一般地，写 $$A=(A_{ij})$$、$$B=(B_{ij})$$，则
$$\operatorname{tr}(AB)=\sum_{i,j}A_{ij}B_{ji}=\sum_{i,j}B_{ji}A_{ij}=\operatorname{tr}(BA),$$
中间一步只是把乘法交换（数是可交换的，矩阵不是——这正是问题所在，但两个**数**的乘积当然可交换）。于是对**任意** $$2\times2$$ 矩阵 $$A,B$$：
$$\operatorname{tr}(AB-BA)=\operatorname{tr}(AB)-\operatorname{tr}(BA)=0.$$
而 $$\operatorname{tr}(I)=2\neq0$$（$$I$$ 是 $$2\times2$$ 单位矩阵）。如果 $$AB-BA=I$$，两边取迹就得到 $$0=2$$，矛盾！这就是为什么入口题 (1) 你怎么试都试不出来。

**命题 3.1（有限维不可能性，热身版）** 设 $$n\ge1$$，$$A,B$$ 是 $$n\times n$$ 复矩阵。则 $$AB-BA=I_n$$ 不可能成立；更一般地，对任何非零常数 $$c$$，$$AB-BA=cI_n$$ 也不可能成立。

**证明** 与 $$n=2$$ 的情形完全一样：$$\operatorname{tr}(AB)=\operatorname{tr}(BA)$$ 对一切 $$n\times n$$ 矩阵成立（同样的指标交换），故 $$\operatorname{tr}(AB-BA)=0$$；而 $$\operatorname{tr}(cI_n)=cn\neq0$$（因为 $$c\neq0$$、$$n\ge1$$）。两边取迹得矛盾。$$\blacksquare$$

第44章的引理 3.4（Wielandt–Wintner）要处理的是**无穷维**情形——那里矩阵变成了一般的有界算子，"迹"这个工具本身就可能没有意义（无穷维空间上 $$\operatorname{tr}(I)=\infty$$），所以需要换一套武器（预解式 + 阶乘增长）。但"结论不可能成立"这件事，你已经在有限维里用手确认过了。

**对易子：从两个具体多项式算起**

再来做入口题 (2)。取 $$(Xf)(t)=tf(t)$$、$$(Df)(t)=f'(t)$$。

对 $$f(t)=t^{2}$$：
$$(DXf)(t)=\frac{d}{dt}\bigl(t\cdot t^{2}\bigr)=\frac{d}{dt}(t^{3})=3t^{2},\qquad (XDf)(t)=t\cdot\frac{d}{dt}(t^{2})=t\cdot2t=2t^{2}.$$
所以 $$(DX-XD)f(t)=3t^{2}-2t^{2}=t^{2}=f(t)$$。

对 $$f(t)=t^{3}$$：
$$(DXf)(t)=\frac{d}{dt}(t^{4})=4t^{3},\qquad (XDf)(t)=t\cdot3t^{2}=3t^{3},\qquad (DX-XD)f(t)=4t^{3}-3t^{3}=t^{3}=f(t).$$

两次都得到 $$(DX-XD)f=f$$。猜想：$$DX-XD=I$$ 对一切多项式成立。**一般证明**：对任意可微函数 $$f$$，
$$(DXf)(t)=\frac{d}{dt}\bigl(tf(t)\bigr)=f(t)+tf'(t),\qquad (XDf)(t)=t f'(t).$$
两式相减：
$$(DXf)(t)-(XDf)(t)=\bigl(f(t)+tf'(t)\bigr)-tf'(t)=f(t).$$
即 $$DX-XD=I$$，也就是 $$XD-DX=-I$$。

这就有必要引入一个记号：我们反复要算"$$XD-DX$$"或"$$AB-BA$$"这种"两个算子复合的顺序之差"，每次都写全会很啰嗦，于是把它简记为一个符号。

**定义 3.2（对易子, commutator）** 设 $$A,B$$ 是同一个向量空间上的两个线性算子（在必要的公共定义域上有定义）。定义 $$[A,B]:=AB-BA$$，称为 $$A,B$$ 的**对易子 (commutator)**。用这个记号，刚才算出的就是
$$[D,X]=I.$$
这正是第44章定义 3.2（正则对易关系）里 $$[X,P]=i\hbar I$$ 的"实数、无 $$i$$"版本：把 $$P$$ 换成 $$D$$、把 $$i\hbar$$ 换成 $$1$$，结构完全一样——**两个算子的对易子是一个标量（不是别的算子）**，这正是"正则"二字的分量。

**命题 3.3（Leibniz 法则，先具体后一般）** 先验证一个具体情形：对 $$f(t)=t^{3}=X\cdot(t^{2})$$，把 $$[D,X^{2}]$$ 算出来——
$$(DX^{2}f)(t)=\frac{d}{dt}(t^{2}f)=2tf+t^{2}f',\qquad (X^{2}Df)(t)=t^{2}f',$$
故 $$[D,X^{2}]f=2tf=2(Xf)$$，即 $$[D,X^{2}]=2X$$。另一方面，按恒等式 $$[D,X\cdot X]=[D,X]X+X[D,X]$$ 直接算：$$[D,X]X+X[D,X]=I\cdot X+X\cdot I=2X$$——两种算法给出同一个答案，这不是巧合，而是一般的 **Leibniz 法则**
$$[A,BC]=[A,B]C+B[A,C]$$
在 $$A=D,B=C=X$$ 时的特例。

**证明（一般 Leibniz 法则）** 直接展开：
$$[A,BC]=A(BC)-(BC)A=(ABC-BAC)+(BAC-BCA)=(AB-BA)C+B(AC-CA)=[A,B]C+B[A,C].\quad\blacksquare$$

由此可以递推出 $$[D,X^{n}]=nX^{n-1}$$（对 $$n$$ 归纳：$$[D,X^{n+1}]=[D,X^{n}]X+X^{n}[D,X]=nX^{n-1}\cdot X+X^{n}\cdot I=(n+1)X^{n}$$）——这正是第44章引理 3.4 证明里 $$[A,B^{n}]=nB^{n-1}$$ 那一步的"无 $$i$$、有限维安全版"，你在这里已经亲手推过一遍。

**从对易关系到 Weyl 关系：一次具体的相位计算**

第44章命题 3.6 说：只要 $$[X,P]=i\hbar$$ 在合适的定义域上成立，指数化后 $$U(s)=e^{isX}$$、$$V(t)=e^{itP}$$ 就满足 Weyl 关系 $$U(s)V(t)=e^{-i\hbar st}V(t)U(s)$$。这一步用了 Baker–Campbell–Hausdorff 公式的截断，光看符号很难有实感。我们先在一个具体、可以完全手算的例子上把这件事算一遍。

取 $$\hbar=1$$，$$\mathsf P=-iD$$（$$D=\dfrac{d}{dx}$$），并取一个具体的（形式上的）测试函数 $$\psi(x)=x^{2}$$——用多项式是因为这样一来 Taylor 展开在有限项就截断，不需要担心收敛问题（第44章在 $$L^2(\mathbb R)$$ 上处理的是真正的 Schwartz 函数，这里先用多项式练手）。

**第一步：算出 $$e^{it\mathsf P}$$ 的具体作用。** $$it\mathsf P=it(-iD)=tD$$，所以 $$e^{it\mathsf P}=e^{tD}$$。按 Taylor 级数
$$e^{tD}\psi(x)=\psi(x)+t\psi'(x)+\frac{t^{2}}{2}\psi''(x)=x^{2}+2tx+t^{2}=(x+t)^{2}=\psi(x+t)$$
（$$\psi=x^2$$ 的三阶以上导数为零，级数自动截断）——这正是"求导算子的指数是平移"这条事实的手算版本。

**第二步：代入具体的 $$s=1,\ t=2$$，比较两种顺序。** $$U(s)=e^{isX}$$ 是乘 $$e^{isx}$$。取 $$s=1,t=2$$：
$$\bigl(U(1)V(2)\psi\bigr)(x)=e^{ix}\cdot\psi(x+2)=e^{ix}(x+2)^{2},$$
$$\bigl(V(2)U(1)\psi\bigr)(x)=\bigl(U(1)\psi\bigr)(x+2)=e^{i(x+2)}(x+2)^{2}.$$
在 $$x=0$$ 处代入数字：
$$\bigl(U(1)V(2)\psi\bigr)(0)=e^{0}\cdot4=4,\qquad \bigl(V(2)U(1)\psi\bigr)(0)=e^{2i}\cdot4=4e^{2i}.$$
两者相差因子 $$e^{-2i}$$：$$4=4e^{2i}\cdot e^{-2i}$$。

**第三步：认出这个相位，写成一般命题。**

**命题 3.4（Weyl 相位的具体来源）** 设 $$\hbar=1$$，$$\mathsf P=-iD$$，$$U(s)=e^{isX}$$（乘 $$e^{isx}$$）、$$V(t)=e^{tD}$$（平移 $$\psi(x)\mapsto\psi(x+t)$$）。则对一切 $$s,t\in\mathbb R$$ 与一切（形式上的）测试函数 $$\psi$$，
$$U(s)V(t)\psi(x)=e^{-ist}\,V(t)U(s)\psi(x).$$

**证明** 直接计算两边：
$$U(s)V(t)\psi(x)=e^{isx}\psi(x+t),\qquad V(t)U(s)\psi(x)=\bigl(U(s)\psi\bigr)(x+t)=e^{is(x+t)}\psi(x+t).$$
两式相除即得 $$\dfrac{U(s)V(t)\psi(x)}{V(t)U(s)\psi(x)}=\dfrac{e^{isx}}{e^{is(x+t)}}=e^{-ist}$$，即所要证的等式。$$\blacksquare$$

取 $$s=1,t=2$$ 正是 $$e^{-i\cdot1\cdot2}=e^{-2i}$$，与第二步的数字计算完全吻合。这个 $$e^{-ist}$$（把 $$\hbar$$ 放回就是 $$e^{-i\hbar st}$$）就是第44章 Weyl 关系 $$U(s)V(t)=e^{-i\hbar st}V(t)U(s)$$ 的全部内容——**它不是凭空冒出来的相位，而是"先乘 $$e^{isx}$$ 再平移"与"先平移再乘 $$e^{isx}$$"这两个操作，因为相位里的 $$x$$ 被平移过一次，比原来多算了一个 $$e^{ist}$$**。这正是第44章命题 3.6 里 Baker–Campbell–Hausdorff 截断在做的事，只是那里用指数级数的代数恒等式一次性说完，这里我们代入了具体的 $$s,t,x$$，一步步看着它发生。

**谐振子升降算子：从 $$[X,P]=i\hbar$$ 里造出 $$[a,a^\dagger]=1$$**

取最简单的参数 $$\hbar=m=\omega=1$$。定义
$$a=\frac{1}{\sqrt2}(X+iP),\qquad a^{\dagger}=\frac{1}{\sqrt2}(X-iP).$$
这两个记号第一次出现，需要交代它们的来历：$$X,P$$ 各自都是自伴的（对应"物理可观测量"），把它们凑成 $$X\pm iP$$ 是想造出**不自伴**的一对——$$a^\dagger$$ 恰是 $$a$$ 的伴随——这样它们才可能像"升一格、降一格"那样，把一个本征向量变成另一个本征向量（自伴算子做不到这件事：自伴算子的谱投影相互正交，不会把一个本征子空间"移动"到另一个本征子空间上去）。

**直接展开验证 $$[a,a^\dagger]=I$$**（不用简写技巧，把每一项都摆出来）：
$$a\,a^{\dagger}=\frac12(X+iP)(X-iP)=\frac12\bigl(X^{2}-iXP+iPX+P^{2}\bigr)=\frac12(X^{2}+P^{2})-\frac{i}{2}(XP-PX),$$
$$a^{\dagger}a=\frac12(X-iP)(X+iP)=\frac12\bigl(X^{2}+iXP-iPX+P^{2}\bigr)=\frac12(X^{2}+P^{2})+\frac{i}{2}(XP-PX).$$
两式相减，$$\frac12(X^2+P^2)$$ 那一半完全抵消：
$$[a,a^{\dagger}]=a a^{\dagger}-a^{\dagger}a=-\frac{i}{2}(XP-PX)-\frac{i}{2}(XP-PX)=-i(XP-PX)=-i[X,P].$$
代入 $$[X,P]=i$$（$$\hbar=1$$）：$$[a,a^{\dagger}]=-i\cdot i=1=I.$$

**同一批展开顺手给出 Hamiltonian。** 把 $$a^\dagger a$$ 的展开式整理：
$$a^{\dagger}a=\frac12(X^{2}+P^{2})+\frac{i}{2}[X,P]=\frac12(X^{2}+P^{2})+\frac{i}{2}(i)=\frac12(X^{2}+P^{2})-\frac12.$$
记 $$N=a^{\dagger}a$$，则 $$X^{2}+P^{2}=2N+1$$，即 $$\tfrac12(P^{2}+X^{2})=N+\tfrac12$$——这正是 $$\hbar=m=\omega=1$$ 时第44章命题里 $$\hbar\omega(N+\tfrac12)$$ 的具体数值版本，你用手算把它推了出来，没有用到任何"代入化简即得"的跳步。

**命题 3.5（谐振子升降算子的对易关系）** 设 $$\hbar=m=\omega=1$$，$$[X,P]=iI$$，$$a=\frac1{\sqrt2}(X+iP)$$，$$a^\dagger=\frac1{\sqrt2}(X-iP)$$。则 $$[a,a^\dagger]=I$$，且 $$\frac12(X^2+P^2)=a^\dagger a+\frac12I$$。

**证明** 即上面的展开计算。$$\blacksquare$$

一般 $$\hbar,m,\omega$$ 的版本（第44章题 3(a) 的完整展开）留给第六节竞 2 练习——你已经在这里看过这套代数的每一步，一般情形只是把系数配平。

**一个"玩具版" Stone–von Neumann：矩阵里的唯一性**

回到入口题 (3)。取 $$U_0=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$$、$$V_0=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$。直接算：
$$U_0V_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad V_0U_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=-U_0V_0.$$
所以 $$U_0V_0=-V_0U_0$$——这是第44章 Weyl 关系 $$U(s)V(t)=e^{-i\hbar st}V(t)U(s)$$ 在"离散、只有一个相位 $$-1=e^{i\pi}$$"情形下的影子。

**命题 3.6（玩具版：交换子只有标量）** 设 $$T=\begin{pmatrix}a&b\\c&d\end{pmatrix}$$ 与 $$U_0$$ 和 $$V_0$$ 都交换。则 $$T=aI$$（即 $$a=d$$，且 $$b=c=0$$）。

**证明** 先用 $$TU_0=U_0T$$：
$$TU_0=\begin{pmatrix}a&-b\\c&-d\end{pmatrix},\qquad U_0T=\begin{pmatrix}a&b\\-c&-d\end{pmatrix}.$$
两者相等要求 $$-b=b$$（即 $$b=0$$）和 $$c=-c$$（即 $$c=0$$）。于是 $$T=\begin{pmatrix}a&0\\0&d\end{pmatrix}$$。再用 $$TV_0=V_0T$$：
$$TV_0=\begin{pmatrix}0&a\\d&0\end{pmatrix},\qquad V_0T=\begin{pmatrix}0&d\\a&0\end{pmatrix}.$$
相等要求 $$a=d$$。故 $$T=aI$$。$$\blacksquare$$

这正是第44章定理 3.10 证明的核心骨架——"与全体 $$U(s)$$ 交换蕴含是乘法算子，再与全体 $$V(t)$$ 交换蕴含是标量"——搬到 $$2\times2$$ 矩阵上，两行代数就做完了。它告诉我们：$$(U_0,V_0)$$ 这一对矩阵是**不可约**的（没有非平凡的公共不变子空间），因为如果有一个非平凡的公共不变子空间，它的正交投影就会是一个与 $$U_0,V_0$$ 都交换、又不是标量的算子，与命题 3.6 矛盾。

**这就是 Stone–von Neumann 定理在最小维数上的完整影子**：只要一对（酉）矩阵满足"反对易"这条关系式且不可约，它们的交换子只能是标量；第44章定理 3.11 要做的，就是证明——即便把"$$2\times2$$"换成"任意可分 Hilbert 空间"、把"反对易的一个符号"换成"连续参数 $$s,t$$ 的相位 $$e^{-i\hbar st}$$"——同样的论证骨架依然成立，而且不可约实现在酉等价意义下**唯一**（第六节竞 1 会用一个显式的基变换矩阵，具体验证"唯一"两个字究竟什么意思）。

## 四、几何与物理直觉 (Intuition)

**顺序会改变结果，这件事本身并不神秘。** 你在纸上先向右走一步、再向上走一步，和先向上、再向右，落点是同一个地方——这两个操作**可交换**。但如果操作换成"把一张纸转 90°"和"把它翻个面"，先转后翻和先翻后转，纸上图案朝向的方向是不一样的——这两个操作**不可交换**。位置与动量之间的对易子 $$[X,P]=i\hbar$$ 说的正是同一件事：**"先测位置再测动量"和"先测动量再测位置"，在算符的意义上不是同一个操作**，差的这一点点，就是 $$i\hbar$$。

**测不准是"分辨率的此消彼长"，日常生活里也有。** 想确定一次极短促的敲击声发生在**哪一刻**，你几乎不需要等待——它本身就很短；但想确定这次敲击的**音高**，你必须让声音持续足够多个周期才能分辨出频率，而这恰恰要求它不能太短。"越确定时刻，越不确定音高；越确定音高，越不确定时刻"——这正是位置与动量的测不准原理（第44章推论 3.12）的日常版本，本章第五节会在一个具体的 Gauss 波包上把这条关系亲手算出来。

**换个视角，不改变实质。** 用摄氏度还是华氏度记录同一个温度，数字不同，但那锅水一样烫——温度计的读数只是"换了个坐标系"，物理事实没变。第44章推论 3.13 说的"Schrödinger 图景与 Heisenberg 图景由一个酉变换联系"，本质上就是这件事：**只要变换是酉的（可逆、保内积），换个视角描述同一个系统，关系式（比如 $$[X,P]=i\hbar$$）照样成立**。第三节最后一部分的矩阵例子（见第六节竞 1 的 Hadamard 矩阵）就是这件事最具体的版本：同一对"反对易"矩阵，换一个基就能长成另一副面孔。

**"关系式决定实现"意味着什么。** 想象你只被告知"这两个操作满足某条代数关系"，却不知道它们具体作用在什么对象上——这有点像只知道两把钥匙"转动的手感差一个固定的角度"，却没看到锁本身。Stone–von Neumann 定理说的是：**只要关系式足够刚性（不可约），这把"锁"其实只有一种（差一个换基）**。第三节命题 3.6 已经在最小的例子上验证了这件事；第44章要做的，是把它扩展到"锁"是整个 $$L^2(\mathbb R)$$ 的情形。

## 五、经典问题精讲 (Classical Problems)

**题 1（具体波函数上的正则对易关系）** 取 $$\hbar=1$$，$$\psi(x)=e^{-x^{2}}$$（不要求归一化）。直接算出 $$(\mathsf X\mathsf P\psi)(x)$$、$$(\mathsf P\mathsf X\psi)(x)$$，验证 $$[\mathsf X,\mathsf P]\psi(x)=i\psi(x)$$，并在 $$x=1$$ 处代入数字核对。

**解** $$\mathsf P\psi(x)=-i\psi'(x)=-i\cdot(-2x)e^{-x^{2}}=2ix\,e^{-x^{2}}$$。于是
$$(\mathsf X\mathsf P\psi)(x)=x\cdot2ixe^{-x^{2}}=2ix^{2}e^{-x^{2}}.$$
另一边，$$\mathsf X\psi(x)=xe^{-x^{2}}$$，故
$$(\mathsf P\mathsf X\psi)(x)=-i\frac{d}{dx}\bigl(xe^{-x^{2}}\bigr)=-i\Bigl(e^{-x^{2}}+x\cdot(-2x)e^{-x^{2}}\Bigr)=-i(1-2x^{2})e^{-x^{2}}.$$
两者相减：
$$[\mathsf X,\mathsf P]\psi(x)=2ix^{2}e^{-x^{2}}-\bigl(-i(1-2x^{2})e^{-x^{2}}\bigr)=ie^{-x^{2}}\bigl(2x^{2}+1-2x^{2}\bigr)=ie^{-x^{2}}=i\,\psi(x).$$
在 $$x=1$$ 处：左边代入上式得 $$ie^{-1}$$；右边 $$i\psi(1)=ie^{-1}$$，两者一致。$$\blacksquare$$

**题 2（Gauss 积分的配方热身，为第44章的 von Neumann 投影铺路）** 计算积分
$$I(x)=\int_{\mathbb R}e^{-(x-y)^{2}/4}\,e^{-y^{2}/2}\,dy$$
作为 $$x$$ 的函数。

**考点位置**：第44章引理 3.11 要算的是一个更复杂的双重高斯积分（先对 $$s$$ 积、再对 $$t$$ 换元配方），这里先做单个变量、单次配方的简化版，把"两个高斯指数合并、配方、分离变量"这套手法练熟。

**解** 先把指数合并：
$$-\frac{(x-y)^{2}}{4}-\frac{y^{2}}{2}=-\frac{x^{2}-2xy+y^{2}}{4}-\frac{y^{2}}{2}=-\frac{x^{2}}{4}+\frac{xy}{2}-\frac{y^{2}}{4}-\frac{y^{2}}{2}=-\frac{x^{2}}{4}+\frac{xy}{2}-\frac{3y^{2}}{4}.$$
对 $$y$$ 配方（把含 $$y$$ 的项凑成完全平方）：
$$-\frac34y^{2}+\frac{x}{2}y=-\frac34\Bigl(y^{2}-\frac{2x}{3}y\Bigr)=-\frac34\Bigl(y-\frac{x}{3}\Bigr)^{2}+\frac34\cdot\frac{x^{2}}{9}=-\frac34\Bigl(y-\frac{x}{3}\Bigr)^{2}+\frac{x^{2}}{12}.$$
故总指数为
$$-\frac{x^{2}}{4}+\frac{x^{2}}{12}-\frac34\Bigl(y-\frac{x}{3}\Bigr)^{2}=-\frac{x^{2}}{6}-\frac34\Bigl(y-\frac{x}{3}\Bigr)^{2}$$
（因为 $$-\tfrac14+\tfrac1{12}=-\tfrac3{12}+\tfrac1{12}=-\tfrac2{12}=-\tfrac16$$）。于是被积函数对 $$y$$ 的部分与 $$x$$ 完全分离：
$$I(x)=e^{-x^{2}/6}\int_{\mathbb R}e^{-\frac34\left(y-\frac{x}{3}\right)^{2}}dy=e^{-x^{2}/6}\sqrt{\frac{\pi}{3/4}}=\frac{2\sqrt\pi}{\sqrt3}\,e^{-x^{2}/6}.\qquad\blacksquare$$

这正是第44章引理 3.11 里"两个高斯凑在一起、配方之后指数对 $$x,y$$ 完全分离"这一步的单变量彩排；那里因为多了一次对 $$s$$ 的积分、又多了一个变量 $$t$$，配方要做两轮，但手法与这里逐字相同。

**题 3（谐振子第一激发态，从升降算子直接算出）** 取 $$\hbar=m=\omega=1$$，$$\Omega(x)=\pi^{-1/4}e^{-x^{2}/2}$$。计算 $$a^{\dagger}\Omega$$ 的显式表达式，并验证它与 $$\Omega$$ 正交、且已经自动归一化。

**解** 由 $$a^{\dagger}=\frac1{\sqrt2}(X-iP)$$ 且 $$P=-iD$$，得 $$-iP=-i(-iD)=-D$$，故 $$a^{\dagger}=\frac1{\sqrt2}(X-D)$$。于是
$$a^{\dagger}\Omega(x)=\frac1{\sqrt2}\bigl(x\Omega(x)-\Omega'(x)\bigr).$$
由 $$\Omega(x)=\pi^{-1/4}e^{-x^{2}/2}$$ 得 $$\Omega'(x)=-x\Omega(x)$$，代入：
$$a^{\dagger}\Omega(x)=\frac1{\sqrt2}\bigl(x\Omega(x)-(-x\Omega(x))\bigr)=\frac1{\sqrt2}\cdot2x\Omega(x)=\sqrt2\,x\,\Omega(x)=\sqrt2\,\pi^{-1/4}x\,e^{-x^{2}/2}.$$

**正交性**：$$\langle\Omega,a^{\dagger}\Omega\rangle=\sqrt2\int_{\mathbb R}x\,\lvert\Omega(x)\rvert^{2}\,dx=0$$，因为被积函数是奇函数（$$\lvert\Omega\rvert^2$$ 是偶函数，乘 $$x$$ 变成奇函数，对称区间上积分为零）。

**归一化**：先算 $$\int_{\mathbb R}x^{2}\lvert\Omega(x)\rvert^{2}\,dx=\pi^{-1/2}\int_{\mathbb R}x^{2}e^{-x^{2}}\,dx=\pi^{-1/2}\cdot\frac{\sqrt\pi}{2}=\frac12$$（用了 Gauss 积分的标准值 $$\int x^{2}e^{-x^{2}}dx=\sqrt\pi/2$$）。于是
$$\lVert a^{\dagger}\Omega\rVert^{2}=2\int_{\mathbb R}x^{2}\lvert\Omega(x)\rvert^{2}\,dx=2\cdot\frac12=1.$$
所以 $$a^{\dagger}\Omega$$ 已经是单位向量，且与 $$\Omega$$ 正交。$$\blacksquare$$

**注** 这正是第44章题 3(b) 里一般归纳公式 $$\lVert\psi_{k}\rVert^{2}=k\lVert\psi_{k-1}\rVert^{2}$$ 在 $$k=1$$ 时的具体数值：$$\lVert a^\dagger\Omega\rVert^2=1\cdot\lVert\Omega\rVert^2=1$$。

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 用前面定义的 $$X,D$$（乘 $$t$$、求导），把 $$[D,X^{3}]$$ 用两种方式各算一遍：(a) 直接对 $$f(t)$$ 展开计算；(b) 用 Leibniz 法则 $$[D,X\cdot X^2]=[D,X]X^{2}+X[D,X^{2}]$$ 结合前面已经算出的 $$[D,X^{2}]=2X$$。验证两种算法给出同一个答案。

**基2.** 用递推关系 $$[D,X^{n+1}]=[D,X^{n}]X+X^{n}[D,X]$$，从 $$[D,X^{3}]=3X^{2}$$ 出发算出 $$[D,X^{4}]$$，并核对是否等于 $$4X^{3}$$。

**基3.** 对 $$f(t)=t^{3}$$，把 $$e^{sD}f(t)$$ 按 Taylor 级数展开到 $$f'''$$ 项（更高阶导数为零），验证结果等于 $$(t+s)^{3}=f(t+s)$$。

### 竞赛（本课目标难度）

**竞1.** 取 Hadamard 矩阵 $$H=\dfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$$（满足 $$H=H^{-1}=H^{*}$$）。直接计算 $$HU_0H^{-1}$$ 与 $$HV_0H^{-1}$$（$$U_0,V_0$$ 取第三节最后一部分的定义），验证
$$HU_0H^{-1}=V_0,\qquad HV_0H^{-1}=U_0.$$
用这个结果说明："位置类矩阵" $$U_0$$ 与"动量类矩阵" $$V_0$$ 只是同一个代数关系换了个基而已。

**竞2.** 对一般的 $$\hbar,m,\omega$$，令 $$a=\sqrt{\dfrac{m\omega}{2\hbar}}\Bigl(X+\dfrac{i}{m\omega}P\Bigr)$$、$$a^{\dagger}=\sqrt{\dfrac{m\omega}{2\hbar}}\Bigl(X-\dfrac{i}{m\omega}P\Bigr)$$。仿照第三节的展开（不要用简写技巧，把每一项都写出来），完整证明 $$[a,a^{\dagger}]=I$$。

**竞3.** 取 $$\hbar=m=\omega=1$$，$$\Omega(x)=\pi^{-1/4}e^{-x^{2}/2}$$。
**(a)** 验证 $$a\Omega=0$$。
**(b)** 分别算出 $$\langle\Omega,X^{2}\Omega\rangle$$ 与 $$\langle\Omega,P^{2}\Omega\rangle$$，验证两者都等于 $$\tfrac12$$，从而 $$\Delta X=\Delta P=1/\sqrt2$$，$$\Delta X\cdot\Delta P=\tfrac12$$（等号成立）。

### 研究（通向下一章）

**研1.** 把命题 3.1 的证明推广：证明对**任意** $$n\times n$$ 复矩阵 $$A,B$$ 和任意非零常数 $$c$$，$$AB-BA=cI_{n}$$ 都不可能成立（这正是命题 3.1 已经写出的一般形式，这里要求你独立重述一遍完整证明，不看讲义）。

**研2.** 取 $$\omega=e^{2\pi i/3}$$，定义 $$3\times3$$ 矩阵 $$C=\operatorname{diag}(1,\omega,\omega^{2})$$（作用在基向量 $$e_{0},e_{1},e_{2}$$ 上为 $$Ce_{j}=\omega^{j}e_{j}$$）与循环移位矩阵 $$S$$（$$Se_{j}=e_{j+1\bmod3}$$）。
**(a)** 直接计算 $$CSe_j$$ 与 $$SCe_j$$（$$j=0,1,2$$），验证 $$CS=\omega\,SC$$。
**(b)** 验证 $$C^{3}=S^{3}=I$$。
**(c)** 把这个关系与第三节算出的 $$U(s)V(t)=e^{-i\hbar st}V(t)U(s)$$ 相比较，说出哪个符号对应哪个符号。

### 解答 (Solutions)

**解 基1.** **(a)** 直接展开：$$(DX^{3}f)(t)=\dfrac{d}{dt}(t^{3}f)=3t^{2}f+t^{3}f'$$，$$(X^{3}Df)(t)=t^{3}f'$$，相减得 $$[D,X^{3}]f=3t^{2}f=3X^{2}f$$，即 $$[D,X^{3}]=3X^{2}$$。
**(b)** 用 Leibniz 法则：$$[D,X^{3}]=[D,X\cdot X^{2}]=[D,X]X^{2}+X[D,X^{2}]=I\cdot X^{2}+X\cdot(2X)=X^{2}+2X^{2}=3X^{2}$$。两种算法一致。$$\blacksquare$$

**解 基2.** $$[D,X^{4}]=[D,X^{3}]X+X^{3}[D,X]=3X^{2}\cdot X+X^{3}\cdot I=3X^{3}+X^{3}=4X^{3}$$，与公式 $$nX^{n-1}$$ 在 $$n=4$$ 时的预测 $$4X^{3}$$ 一致。$$\blacksquare$$

**解 基3.** $$f(t)=t^{3}$$，$$f'(t)=3t^{2}$$，$$f''(t)=6t$$，$$f'''(t)=6$$，四阶及以上导数为零。故
$$e^{sD}f(t)=f(t)+sf'(t)+\frac{s^{2}}{2}f''(t)+\frac{s^{3}}{6}f'''(t)=t^{3}+3st^{2}+3s^{2}t+s^{3}.$$
而 $$(t+s)^{3}=t^{3}+3t^{2}s+3ts^{2}+s^{3}$$，与上式逐项相同。所以 $$e^{sD}f(t)=(t+s)^{3}=f(t+s)$$。$$\blacksquare$$

**解 竞1.** 先算 $$U_0H$$：
$$U_0H=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\cdot\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}=\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}.$$
再左乘 $$H$$：
$$H(U_0H)=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\cdot\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\frac12\begin{pmatrix}1-1&1+1\\1+1&1-1\end{pmatrix}=\frac12\begin{pmatrix}0&2\\2&0\end{pmatrix}=\begin{pmatrix}0&1\\1&0\end{pmatrix}=V_0.$$
因为 $$H=H^{-1}$$，上式就是 $$HU_0H^{-1}=V_0$$。

同理算 $$HV_0H^{-1}$$：
$$V_0H=\begin{pmatrix}0&1\\1&0\end{pmatrix}\cdot\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}=\frac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix},$$
$$H(V_0H)=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\cdot\frac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}=\frac12\begin{pmatrix}1+1&-1+1\\1-1&-1-1\end{pmatrix}=\frac12\begin{pmatrix}2&0\\0&-2\end{pmatrix}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}=U_0.$$
所以 $$HV_0H^{-1}=U_0$$。**这说明** $$U_0$$ 与 $$V_0$$ 满足的关系式（反对易、平方为 $$I$$）完全对称，换一个基（这里是 Hadamard 基变换）就能把"位置类"矩阵变成"动量类"矩阵——正是第44章推论 3.13"酉变换只是换视角"的 $$2\times2$$ 具体实例，也呼应第44章竞 1 里 Fourier 变换把 $$\mathsf X$$ 换成 $$-\mathsf P$$ 的做法。$$\blacksquare$$

**解 竞2.** 记 $$c=\sqrt{\dfrac{m\omega}{2\hbar}}$$、$$k=\dfrac1{m\omega}$$，则 $$a=c(X+ikP)$$、$$a^{\dagger}=c(X-ikP)$$。展开：
$$aa^{\dagger}=c^{2}(X+ikP)(X-ikP)=c^{2}\bigl(X^{2}-ikXP+ikPX+k^{2}P^{2}\bigr)=c^{2}(X^{2}+k^{2}P^{2})-ikc^{2}(XP-PX),$$
$$a^{\dagger}a=c^{2}(X-ikP)(X+ikP)=c^{2}\bigl(X^{2}+ikXP-ikPX+k^{2}P^{2}\bigr)=c^{2}(X^{2}+k^{2}P^{2})+ikc^{2}(XP-PX).$$
相减：
$$[a,a^{\dagger}]=aa^{\dagger}-a^{\dagger}a=-2ikc^{2}(XP-PX)=-2ikc^{2}[X,P].$$
代入 $$[X,P]=i\hbar$$：
$$[a,a^{\dagger}]=-2ikc^{2}\cdot i\hbar=2kc^{2}\hbar.$$
代入 $$k=\dfrac1{m\omega}$$、$$c^{2}=\dfrac{m\omega}{2\hbar}$$：
$$2kc^{2}\hbar=2\cdot\frac1{m\omega}\cdot\frac{m\omega}{2\hbar}\cdot\hbar=2\cdot\frac12=1.$$
故 $$[a,a^{\dagger}]=I$$，对一切 $$\hbar,m,\omega>0$$ 成立。$$\blacksquare$$

**解 竞3.** **(a)** $$a=\dfrac1{\sqrt2}(X+iP)$$，$$iP=i(-iD)=D$$，故 $$a=\dfrac1{\sqrt2}(X+D)$$。作用在 $$\Omega$$ 上：
$$a\Omega(x)=\frac1{\sqrt2}\bigl(x\Omega(x)+\Omega'(x)\bigr).$$
由 $$\Omega'(x)=-x\Omega(x)$$，得 $$x\Omega+\Omega'=x\Omega-x\Omega=0$$，故 $$a\Omega=0$$。

**(b)** $$\langle\Omega,X^{2}\Omega\rangle=\displaystyle\int_{\mathbb R}x^{2}\lvert\Omega(x)\rvert^{2}dx=\pi^{-1/2}\int_{\mathbb R}x^{2}e^{-x^{2}}dx=\pi^{-1/2}\cdot\frac{\sqrt\pi}{2}=\frac12$$（用了标准 Gauss 积分 $$\int x^{2}e^{-x^{2}}dx=\sqrt\pi/2$$）。

对 $$P$$：先算 $$P\Omega(x)=-i\Omega'(x)=-i(-x\Omega(x))=ix\Omega(x)$$。由 $$P$$ 自伴，$$\langle\Omega,P^{2}\Omega\rangle=\lVert P\Omega\rVert^{2}=\displaystyle\int_{\mathbb R}\lvert ix\Omega(x)\rvert^{2}dx=\int_{\mathbb R}x^{2}\lvert\Omega(x)\rvert^{2}dx=\frac12$$，与上面同一个积分。

故 $$\Delta X^{2}=\langle\Omega,X^2\Omega\rangle-\langle\Omega,X\Omega\rangle^2=\tfrac12-0=\tfrac12$$（$$\langle\Omega,X\Omega\rangle=0$$ 因被积函数为奇函数），同理 $$\Delta P^{2}=\tfrac12$$。于是 $$\Delta X=\Delta P=1/\sqrt2$$，$$\Delta X\cdot\Delta P=\tfrac12=\dfrac{\hbar}{2}$$（$$\hbar=1$$）——测不准原理在这里**取等号**。$$\blacksquare$$

**解 研1.** 对一般 $$n\times n$$ 矩阵 $$A=(A_{ij})$$、$$B=(B_{ij})$$，迹的定义是 $$\operatorname{tr}(M)=\sum_i M_{ii}$$。计算
$$\operatorname{tr}(AB)=\sum_{i}(AB)_{ii}=\sum_i\sum_jA_{ij}B_{ji}=\sum_{i,j}A_{ij}B_{ji},$$
$$\operatorname{tr}(BA)=\sum_i\sum_jB_{ij}A_{ji}=\sum_{i,j}B_{ij}A_{ji}.$$
把第二式里的哑标 $$i,j$$ 互换名字（$$i\leftrightarrow j$$），$$\operatorname{tr}(BA)=\sum_{i,j}B_{ji}A_{ij}=\sum_{i,j}A_{ij}B_{ji}=\operatorname{tr}(AB)$$。故 $$\operatorname{tr}(AB-BA)=0$$ 对一切 $$n\times n$$ 矩阵成立。若 $$AB-BA=cI_n$$，两边取迹得 $$0=cn$$；因 $$n\ge1$$，必有 $$c=0$$。所以当 $$c\neq0$$ 时方程无解。$$\blacksquare$$

**解 研2.** **(a)** 按定义 $$Ce_j=\omega^j e_j$$、$$Se_j=e_{j+1\bmod3}$$：
$$CSe_j=C(e_{j+1})=\omega^{j+1}e_{j+1},\qquad SCe_j=S(\omega^j e_j)=\omega^j e_{j+1}.$$
两者之比：$$CSe_j=\omega^{j+1}e_{j+1}=\omega\cdot\bigl(\omega^{j}e_{j+1}\bigr)=\omega\cdot SCe_j$$，对 $$j=0,1,2$$ 都成立，故 $$CS=\omega\,SC$$。

**(b)** $$C^{3}e_j=\omega^{3j}e_j=(\omega^3)^{j}e_j=1^{j}e_j=e_j$$（因 $$\omega^{3}=e^{2\pi i}=1$$），故 $$C^{3}=I$$。$$S$$ 把 $$e_0\to e_1\to e_2\to e_0$$ 循环一周，三次复合回到原位，故 $$S^{3}=I$$。

**(c)** 把 $$C$$ 对应 $$U(s)$$、$$S$$ 对应 $$V(t)$$，则 $$CS=\omega SC$$ 对应 $$U(s)V(t)=e^{-i\hbar st}V(t)U(s)$$——**只不过这里的"相位"$$\omega=e^{2\pi i/3}$$ 是离散、取值在有限集合 $$\{1,\omega,\omega^2\}$$ 里的，而第44章里的相位 $$e^{-i\hbar st}$$ 是连续参数 $$s,t\in\mathbb R$$ 遍历出来的一整条圆周**。离散版本三步一循环（因为 $$C^3=S^3=I$$），连续版本永不回到单位元（因为 $$s,t$$ 取遍全体实数）——这正是"有限维玩具模型"与"无穷维 Stone–von Neumann"之间唯一的本质差别：**关系式的代数骨架完全一样，只是相位的取值范围从有限群换成了整条实直线**。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**1. "不可能有界"不是抽象论证，是手算迹得到的矛盾。** $$2\times2$$、$$n\times n$$ 矩阵的迹循环性 $$\operatorname{tr}(AB)=\operatorname{tr}(BA)$$ 直接排除了 $$AB-BA=cI$$（$$c\neq0$$）的所有有限维实现——这是第44章引理 3.4（无穷维版本，靠预解式与阶乘增长）的具体缩影。

**2. 对易子是"顺序之差"的简写，正则对易关系是"这个差是一个标量"。** 在多项式空间上手算 $$[D,X]=I$$，与第44章 $$[X,P]=i\hbar I$$ 结构完全一致——只是把复数 $$i\hbar$$ 换成了实数 $$1$$。

**3. Weyl 关系里的相位不是变魔术变出来的。** 代入具体的 $$s=1,t=2$$ 和具体的测试函数，亲手验证了"先乘相位再平移"和"先平移再乘相位"相差 $$e^{-i\hbar st}$$——第44章命题 3.6 的 Baker–Campbell–Hausdorff 截断，只是把这个具体计算符号化。

**4. 谐振子升降算子 $$[a,a^{\dagger}]=1$$ 是 $$[X,P]=i\hbar$$ 的直接推论，不是新假设。** 把 $$a,a^{\dagger}$$ 的定义完全展开（不用简写技巧）就能亲手推出这个式子，以及 Hamiltonian 与 $$N=a^{\dagger}a$$ 的关系。

**5. Stone–von Neumann 定理在 $$2\times2$$ 矩阵上已经有一个完整、可以亲手验证的版本。** 命题 3.6 用两行线性代数证明了"与 $$U_0,V_0$$ 都交换的矩阵只能是标量"，竞 1 用 Hadamard 矩阵具体展示了"换个基就能把一种实现变成另一种"——这正是第44章定理 3.11"不可约实现唯一"的最小、最具体的例子。

**交棒给第44章。** 现在你已经能手算出：有限维里 $$AB-BA=I$$ 为什么不可能、$$[X,P]$$ 如何指数化成一个具体的相位、升降算子的对易子从哪里来、以及一个 $$2\times2$$ 的"唯一性"实例。第44章要做的，是把这一切从"矩阵、多项式、离散相位"搬到"无穷维 Hilbert 空间、真正的无界自伴算子、连续参数 $$s,t\in\mathbb R$$"，并且证明——**即便舞台换成了无穷维，结论依然是：满足 $$[X,P]=i\hbar$$ 的不可约实现，差一个酉变换，只有一种**，这就是 Stone–von Neumann 定理。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch42_无界算子与Cayley变换_下.md">← 第42章 无界算子与 Cayley 变换·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch44_正则对易关系与Stone_vonNeumann_下.md">第44章 正则对易关系与 Stone–von Neumann·下 →</a></div>
</div>
