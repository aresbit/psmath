---
layout: default
---

# 第30章: Möbius 群、双重覆盖与射影表示 (The Möbius Group, Double Covers and Projective Representations)

> 对应原专栏: MP107–MP112
> 专家依据: `_experts/algebra/representation-theory.md`（主）+ `_experts/algebra/lie-algebra-root-systems.md`
> 知识库依据: `opc2/knowledge/math/表示论/`（15 篇）、`opc2/knowledge/math/李群/lie-groups/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

本章只做一件事：把「一个群作用在**射影**空间上」这件事讲透。

前三章各埋了一个伏笔，这里是它们的收口。第 26 章算出 $$\pi_1(\mathrm{SO}(3))=\mathbb Z/2$$，并证明「转一整圈」不是零伦闭路；第 22 章发现Heisenberg群 $$H_3(\mathbb R)$$ 是相空间平移群的**中心扩张**，而 Stone–von Neumann 定理的真正含义是「上循环不平凡时，射影表示反而被中心扩张的唯一不可约表示锁死」；第 29 章造出旋量并把 $$\mathrm{Spin}(1,3)\cong\mathrm{SL}(2,\mathbb C)$$ 这笔账记在了「存在一个连通双层覆叠」上。这三件事是同一件事。

本章把那个「同一个动作」抽象成**中心扩张**，给它一个名字叫**射影表示**，再算清它什么时候能被修补成普通表示（答案：上循环是不是**上边界**）。我们会看到 Möbius 群、Lorentz 群、旋转群三者的同构与覆叠关系排成一条链，而**「转 360° 不等于恒等」的最终解释是：那不是几何怪事，而是射影表示的必然**——半整数自旋正是它的产物。

**从哪来**：第 22 章的中心扩张原型、第 26 章的双重覆叠、第 28 章的 $$\mathfrak{sl}(2)$$ 表示分类、第 29 章的旋量。
**到哪去**：第 31 章把「群 » 表示 » 覆叠群」这套语言换成范畴与函子的语言——卷四在此结束，卷五转入范畴论。

## 二、入口：一道具体的问题 (Entry Problem)

**问题 A：同一批矩阵，两副面孔。（来源：自编，母题是 MP107 的 $$\mathrm{SL}(2,\mathbb C)$$ 与光锥，亦见保角几何教材里的标准开场）**

取 $$2\times 2$$ 复矩阵
$$A=\begin{pmatrix}a&b\\ c&d\end{pmatrix},\qquad \det A=ad-bc=1,$$
并定义扩充复平面 $$\widehat{\mathbb C}=\mathbb C\cup\{\infty\}$$ 上的变换
$$f_A(z)=\frac{az+b}{cz+d}.$$

(1) 算出 $$f_A\circ f_B$$ 等于哪一个 $$f_C$$。由此说明全体这样的 $$f$$ 构成一个群。
(2) 不同的 $$A$$ 会不会给出同一个 $$f$$？把所有给出同一个 $$f$$ 的矩阵**全部**找出来。
(3) $$f_A$$ 把「圆或直线」变成什么？
(4) 现在把 $$z=x+iy$$ 的实部与虚部一起编进一个 $$2\times 2$$ 矩阵
$$X=\begin{pmatrix}x_0+x_3&x_1-ix_2\\ x_1+ix_2&x_0-x_3\end{pmatrix}.$$
你会发现 $$f_A$$ 在 $$(x_0,x_1,x_2,x_3)$$ 上诱导了一个四维实线性变换。它保持哪一个二次型？这个变换与 Lorentz 变换是什么关系？

第 (4) 问是本章的主线：它把「复变函数里的分式线性变换」和「相对论里的 Lorentz 变换」认成了同一个群。这不是巧合，而是 $$\mathrm{PSL}(2,\mathbb C)\cong\mathrm{SO}^+(1,3)$$——本节 3.3 的第二条定理。

**问题 B：相位。（来源：自编，母题是 Wigner 定理与中子干涉实验）**

设 $$R_\theta$$ 是 $$\mathbb R^3$$ 中绕固定轴转 $$\theta$$ 的旋转。量子力学告诉你，自旋 $$1/2$$ 的态按
$$U(\theta)=\begin{pmatrix}e^{-i\theta/2}&0\\ 0&e^{i\theta/2}\end{pmatrix}$$
变换。注意两个事实：

- $$U(\theta)U(\varphi)=U(\theta+\varphi)$$，复合的规则没问题；
- 但 $$U(2\pi)=-I\ne I$$，而 $$R_{2\pi}=R_0=I$$。

(1) 这是否意味着「对应规则 $$R_\theta\mapsto U(\theta)$$ 根本不是一个群同态」？如果是，为什么物理上没出问题？
(2) 物理上 $$-I$$ 与 $$I$$ 不可区分（整体相位没有意义）。那么，能不能**连续地、一致地**把每个 $$U(\theta)$$ 乘上一个相位因子，使得对应规则重新变成群同态？如果能，怎么乘；如果不能，为什么？（提示：先想清楚「一致地」三个字在拓扑上是什么意思。）

第 (2) 问就是「射影表示能否线性化」，它的答案在 3.5 节，而否定的证明在定理 3.12。这道题与第 26 章的定理 3.10 是同一个数学事实的两种说法：第 26 章说的是「转一圈的闭路缩不掉」，这里说的是「相位没法一致地选掉」。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 Möbius 变换与 $$\mathrm{PSL}(2,\mathbb C)$$

**定义 3.1（Möbius 变换, Möbius transformation）** 设 $$a,b,c,d\in\mathbb C$$ 满足 $$ad-bc\ne0$$。由
$$f(z)=\frac{az+b}{cz+d}$$
给出的扩充复平面 $$\widehat{\mathbb C}=\mathbb C\cup\{\infty\}$$ 上的变换称为一个 **Möbius 变换**（也叫分式线性变换）。在端点处按连续延拓理解：
$$f(\infty)=\frac ac\ (\text{若 } c\ne0),\qquad f\Bigl(-\frac dc\Bigr)=\infty\ (\text{若 } c\ne0);$$
若 $$c=0$$ 则 $$f(\infty)=\infty$$。

**定理 3.2（Möbius 群 $$\cong\mathrm{PSL}(2,\mathbb C)\cong\mathrm{PGL}(2,\mathbb C)$$）**

**(i)** 若 $$f_A,f_B$$ 分别由矩阵 $$A,B$$ 给出，则 $$f_A\circ f_B=f_{AB}$$。特别地 $$f_A$$ 可逆、逆为 $$f_{A^{-1}}$$。于是全体 Möbius 变换构成一个群，记作 $$\mathrm{Möb}$$。

**(ii)** $$f_A=f_B$$ 当且仅当 $$B=\lambda A$$ 对某个 $$\lambda\in\mathbb C^*$$。因此
$$\mathrm{Möb}\cong \mathrm{PGL}(2,\mathbb C):=\mathrm{GL}(2,\mathbb C)/\mathbb C^*,$$
其中 $$\mathbb C^*=\{\lambda I\}$$ 是标量矩阵群（平凡地中心）。

**(iii)** 每个 $$A\in\mathrm{GL}(2,\mathbb C)$$ 都是某个标量乘以行列式为 $$1$$ 的矩阵。于是
$$\mathrm{Möb}\cong\mathrm{PGL}(2,\mathbb C)\cong\mathrm{PSL}(2,\mathbb C):=\mathrm{SL}(2,\mathbb C)/\{\pm I\}.$$

*证明* **(i)** 记 $$B=\begin{pmatrix}p&q\\ r&s\end{pmatrix}$$。对 $$z$$ 使分母不为零，
$$f_A\bigl(f_B(z)\bigr)=\frac{a\frac{pz+q}{rz+s}+b}{c\frac{pz+q}{rz+s}+d}=\frac{a(pz+q)+b(rz+s)}{c(pz+q)+d(rz+s)}=\frac{(ap+br)z+(aq+bs)}{(cp+dr)z+(cq+ds)}=f_{AB}(z).$$
（第二步是分子分母同乘 $$rz+s$$。）在有限点之外再用连续延拓，等式在 $$\widehat{\mathbb C}$$ 上处处成立。又 $$\det(AB)=\det A\det B\ne0$$，故 $$f_{AB}$$ 仍是 Möbius 变换，$$f_A\circ f_B$$ 落在 $$\mathrm{Möb}$$ 内；$$f_A\circ f_{A^{-1}}=f_{AA^{-1}}=f_I=\operatorname{id}$$ 给出逆元。结合律继承自矩阵乘法。$$\square$$

**(ii)** 设 $$f_A=f_B$$ 在 $$\widehat{\mathbb C}$$ 上成立。则在 $$z$$ 不是任一极点处有
$$(az+b)(rz+s)=(pz+q)(cz+d).$$
这是 $$z$$ 的多项式恒等式，比较系数得三个方程
$$ar=pc,\qquad as+br=qc+pd,\qquad bs=qd.$$
把 $$A$$ 的两列与 $$B$$ 的两列分别看作 $$\mathbb C^2$$ 的向量。上面三式等价于
$$\det\bigl(\mathrm{col}_1A,\ \mathrm{col}_1B\bigr)=0,\qquad \det\bigl(\mathrm{col}_2A,\ \mathrm{col}_2B\bigr)=0,\qquad \det\bigl(\mathrm{col}_1A,\ \mathrm{col}_2B\bigr)=-\det\bigl(\mathrm{col}_2A,\ \mathrm{col}_1B\bigr).$$
因为 $$A$$ 可逆，$$\mathrm{col}_1A,\mathrm{col}_2A$$ 是一组基，把 $$B$$ 的两列在这组基下展开：
$$\mathrm{col}_1B=\alpha\,\mathrm{col}_1A+\beta\,\mathrm{col}_2A,\qquad \mathrm{col}_2B=\gamma\,\mathrm{col}_1A+\delta\,\mathrm{col}_2A.$$
于是 $$\det(\mathrm{col}_1A,\mathrm{col}_1B)=\beta\det A$$，由第一式得 $$\beta=0$$；$$\det(\mathrm{col}_2A,\mathrm{col}_2B)=\gamma\det A$$，由第二式得 $$\gamma=0$$；两个混合式的等式给出 $$\delta\det A=\alpha\det A$$，即 $$\alpha=\delta$$。于是两列都是 $$\alpha$$ 倍对应的列，$$B=\alpha A$$。
反过来若 $$B=\lambda A$$，分子分母同时提出 $$\lambda$$，$$f_B=f_A$$ 显然。$$\square$$

**(iii)** 设 $$\Delta=\det A\ne0$$。在 $$\mathbb C$$ 上取 $$\Delta$$ 的一个平方根 $$\lambda$$（代数基本定理保证存在；$$\mathbb C$$ 的平方根可显式写出或由复数的极坐标形式给出）。令 $$A'=\lambda^{-1}A$$，则 $$\det A'=\lambda^{-2}\Delta=1$$，故 $$A'=\lambda^{-1}A\in\mathrm{SL}(2,\mathbb C)$$ 且 $$A=\lambda A'$$。所以 $$\mathrm{GL}(2,\mathbb C)$$ 中每个元素在 $$\mathrm{PGL}$$ 中的像都等于某个 $$\mathrm{SL}(2,\mathbb C)$$ 元素的像；商映射 $$\mathrm{GL}\to\mathrm{PGL}$$ 限制在 $$\mathrm{SL}$$ 上仍是满的。其核是
$$\mathrm{SL}(2,\mathbb C)\cap\mathbb C^*I=\{cI: c^2=1\}=\{\pm I\}.$$
故 $$\mathrm{PGL}(2,\mathbb C)\cong\mathrm{SL}(2,\mathbb C)/\{\pm I\}=\mathrm{PSL}(2,\mathbb C)$$。$$\blacksquare$$

**注 3.2（这条同构是复数域的恩赐）** $$\mathrm{PSL}\cong\mathrm{PGL}$$ 依赖「$$\mathbb C^*$$ 中每个元素都是平方」。在实数域上这不成立：$$\mathrm{PGL}(2,\mathbb R)\big/\mathrm{PSL}(2,\mathbb R)\cong\mathbb R^*/\mathbb R_{>0}^*\cong\mathbb Z/2$$，两者相差一个行列式的符号。所以定理 3.2(iii) 是复数的特殊性，不是一般现象；阅读时不要把 $$\mathrm{PSL}$$ 与 $$\mathrm{PGL}$$ 在任何域上都等同。

### 3.2 圆到圆与交比

**定理 3.3（圆到圆、三点传递、交比不变）**

**(i)** 每个 Möbius 变换把「圆或直线」映成「圆或直线」（把直线看作过 $$\infty$$ 的圆）。

**(ii)** 给定 $$\widehat{\mathbb C}$$ 中两组互不相同的三点 $$z_1,z_2,z_3$$ 与 $$w_1,w_2,w_3$$，存在**唯一**的 Möbius 变换 $$f$$ 使 $$f(z_i)=w_i$$（$$i=1,2,3$$）；称 Möbius 群在 $$\widehat{\mathbb C}$$ 上是**严格三点传递的 (sharply 3-transitive)**。

**(iii)** 交比
$$[z,z_1,z_2,z_3]=\frac{(z-z_1)(z_2-z_3)}{(z-z_3)(z_2-z_1)}$$
在 Möbius 变换下不变，即 $$[f(z),f(z_1),f(z_2),f(z_3)]=[z,z_1,z_2,z_3]$$。

*证明思路* **(i)** 的关键是**把圆写成一条二次方程**，然后验证代入后形状不变：圆与直线都是 $$\widehat{\mathbb C}$$ 中同一条曲线的两种情形，它们统一写成
$$Az\bar z+\bar Bz+B\bar z+C=0,\qquad A,C\in\mathbb R,\ B\in\mathbb C,\qquad AC-\lvert B\rvert^2<0\ \text{或}\ A=0,\ B\ne0 .$$
**(iii)** 的证明不需要逐项展开，只要注意交比本身就是「把三点送到 $$0,1,\infty$$ 的那个 Möbius 变换」；**(ii)** 的唯一性则归结为「固定 $$0,1,\infty$$ 的 Möbius 变换只有恒等」。

*证明* **(i)** 上述方程中 $$A=0$$ 时是直线，$$A\ne0$$ 时是圆：化为 $$\lvert z+B/A\rvert^2=( \lvert B\rvert^2-AC)/A^2>0$$——圆心 $$-B/A\,$$、半径 $$\sqrt{\lvert B\rvert^2-AC}/\lvert A\rvert$$。条件 $$AC-\lvert B\rvert^2<0$$ 恰是「半径为正」。

把 $$z=\dfrac{b-dw}{cw-a}$$（从 $$w=\dfrac{az+b}{cz+d}$$ 解出：$$w(cz+d)=az+b\Rightarrow z(cw-a)=b-dw$$）代入。先做一件更省力的事：在方程两边乘以 $$\lvert cw-a\rvert^2=(cw-a)(\bar c\bar w-\bar a)>0$$。注意
$$\lvert cw-a\rvert^2\,z\bar z=\lvert b-dw\rvert^2,\qquad \lvert cw-a\rvert^2\, z=(b-dw)(\bar c\bar w-\bar a),\qquad \lvert cw-a\rvert^2\,\bar z=(\bar b-\bar d\bar w)(cw-a),$$
所以左边变成 $$w,\bar w$$ 的一个式子：
$$A\lvert b-dw\rvert^2+\bar B(b-dw)(\bar c\bar w-\bar a)+B(\bar b-\bar d\bar w)(cw-a)+C(cw-a)(\bar c\bar w-\bar a).$$
展开后按 $$w\bar w,\ \bar w,\ w,\ 1$$ 整理，得到
$$A' w\bar w+\bar B'w+B'\bar w+C'=0$$
的形状，其中 $$A',C'$$ 是实数（共轭对称），$$B'\in\mathbb C$$。再把这一式看成一个矩阵恒等式：记
$$H=\begin{pmatrix}A&\bar B\\ B&C\end{pmatrix},\qquad M=\begin{pmatrix}d&-b\\ c&-a\end{pmatrix}\ \ (\text{即把 }(z,1)\text{ 送上 }(w,1)\text{ 的线性部分}),$$
则展开的结果正是 $$H'=M^*HM$$（直接比对系数即可），其中 $$H'=\begin{pmatrix}A'&\bar B'\\ B'&C'\end{pmatrix}$$。$$M$$ 可逆（$$\det M=bc-ad=-1\ne0$$），故
$$\det H'=\lvert\det M\rvert^2\det H=\det H ,$$
于是 $$\det H=AC-\lvert B\rvert^2$$ 只乘了一个正数，符号不变。若原来是圆（$$A\ne0$$、$$\det H<0$$），则新方程表示一条半径为正的圆；若原来是直线（$$A=0$$），则新方程或是直线（$$A'=0$$），或是圆（$$A'\ne0$$）。两种情形都属于「圆或直线」。$$\square$$

**(iii)** 先设 $$z_1,z_2,z_3$$ 互异。由 (ii)（下文将独立证明其存在性）先承认：以 $$g(z):=[z,z_1,z_2,z_3]$$ 记交比，直接代入得 $$g(z_1)=0$$、$$g(z_2)=1$$、$$g(z_3)=\infty$$，且 $$g$$ 作为 $$z$$ 的函数是分式线性的（分子分母都是 $$z$$ 的一次式，分母为 $$(z-z_3)(z_2-z_1)$$ 不为零多项式），故 $$g$$ 是 Möbius 变换。于是 $$g$$ 是**把 $$(z_1,z_2,z_3)$$ 送到 $$(0,1,\infty)$$ 的**那个 Möbius 变换。

现在设 $$f$$ 是任一 Möbius 变换。同样地，$$h(w):=[w,f(z_1),f(z_2),f(z_3)]$$ 是把 $$(f(z_1),f(z_2),f(z_3))$$ 送到 $$(0,1,\infty)$$ 的 Möbius 变换。于是 $$h\circ f$$ 也是把 $$(z_1,z_2,z_3)$$ 送到 $$(0,1,\infty)$$ 的 Möbius 变换。由 (ii) 的唯一性（下面证），$$h\circ f=g$$。在 $$w=f(z)$$ 处取值得
$$[f(z),f(z_1),f(z_2),f(z_3)]=h(f(z))=g(z)=[z,z_1,z_2,z_3].\qquad\square$$

**(ii) 唯一性** 先设 $$z_1,z_2,z_3=0,1,\infty$$，且 $$f$$ 是任一固定这三点的 Möbius 变换 $$f(z)=\dfrac{az+b}{cz+d}$$。由 $$f(\infty)=\infty$$ 得 $$c=0$$（若 $$c\ne0$$ 则 $$f(\infty)=a/c\in\mathbb C\ne\infty$$），于是 $$f(z)=\dfrac{a}{d}z+\dfrac bd$$。由 $$f(0)=0$$ 得 $$b=0$$；由 $$f(1)=1$$ 得 $$a/d=1$$。故 $$f(z)=z$$。

一般情形：设 $$f_1,f_2$$ 都把 $$(z_1,z_2,z_3)$$ 送到 $$(w_1,w_2,w_3)$$，并设 $$g$$ 是把 $$(w_1,w_2,w_3)$$ 送到 $$(0,1,\infty)$$ 的 Möbius 变换（上面已构造出 $$g$$）。则 $$g\circ f_1$$ 与 $$g\circ f_2$$ 都固定 $$0,1,\infty$$，由上一段两者都等于恒等，故 $$f_1=f_2$$。

**存在性** 已在 (iii) 的开头给出：$$z\mapsto[z,z_1,z_2,z_3]$$ 把 $$(z_1,z_2,z_3)$$ 送到 $$(0,1,\infty)$$；再把 $$(w_1,w_2,w_3)\to(0,1,\infty)$$ 的那个变换取逆并复合，即得 $$f$$。$$\blacksquare$$

**注 3.3（交比是「圆的坐标」）** 由定理 3.3(iii)，四点共圆（含共线）这一性质在 Möbius 变换下不变：因为「共圆或共线」等价于交比为实数（这一点在第五节题 2 中证明）。所以 Möbius 变换不只是「把圆映成圆」，它还是**圆几何的对称群**——这正是它出现在双曲几何与共形场论里的原因。

### 3.3 从球面到光锥：$$\mathrm{PSL}(2,\mathbb C)\cong\mathrm{SO}^+(1,3)$$

**定义 3.4（Hermite 矩阵实现, Hermitian matrix realization）** 对 $$x=(x_0,x_1,x_2,x_3)\in\mathbb R^4$$ 记
$$X(x)=\begin{pmatrix}x_0+x_3&x_1-ix_2\\ x_1+ix_2&x_0-x_3\end{pmatrix}.$$
这是一个 $$2\times2$$ **Hermite 矩阵**（$$X^*=X$$），且每个 $$2\times 2$$ Hermite 矩阵都唯一地写成这个形状。记 $$\mathcal H=\{X:\ X^*=X\}$$ 为 $$2\times2$$ Hermite 矩阵的实向量空间，则
$$x\longmapsto X(x)$$
是 $$\mathbb R^4\to\mathcal H$$ 的实线性同构（逆映射：$$x_0=\tfrac12\operatorname{tr}X$$、$$x_3=\tfrac12(X_{11}-X_{22})$$、$$x_1=\operatorname{Re}X_{12}$$、$$x_2=-\operatorname{Im}X_{12}$$）。

**定理 3.5（$$\det$$ 就是 Minkowski 二次型）** 对一切 $$x\in\mathbb R^4$$，
$$\det X(x)=x_0^2-x_1^2-x_2^2-x_3^2=:\langle x,x\rangle_{1,3}.$$

*证明* 直接展开：
$$\det X(x)=(x_0+x_3)(x_0-x_3)-(x_1-ix_2)(x_1+ix_2)=x_0^2-x_3^2-\bigl(x_1^2+x_2^2\bigr).\qquad\square$$

因此定义 3.4 把 $$\mathbb R^4$$ 与「$$\mathcal H$$ 上由 $$-\det$$ 定出的二次空间」等同起来：$$X(x)$$ 的行列式正是 Minkowski 长度平方。注意 $$X$$ 正定（作为矩阵）当且仅当 $$\langle x,x\rangle_{1,3}>0$$ 且 $$x_0>0$$——这是「时间方向」能够被代数地读出来的地方。

**定理 3.6（$$\mathrm{SL}(2,\mathbb C)\to\mathrm{SO}^+(1,3)$$ 是双重覆叠）** 对 $$A\in\mathrm{SL}(2,\mathbb C)$$ 定义
$$\Phi(A):\ \mathcal H\to\mathcal H,\qquad \Phi(A)(X)=AXA^*.$$

**(i)** $$\Phi(A)$$ 是 $$\mathcal H$$ 的实线性自同构，保持 $$\det$$；在定义 3.4 的同构下它就是 $$\mathbb R^4$$ 的一个保持 $$\langle\cdot,\cdot\rangle_{1,3}$$ 的线性变换，即一个 Lorentz 变换。并且它保持时间方向与空间定向，因此 $$\Phi(A)\in\mathrm{SO}^+(1,3)$$（单位连通的 Lorentz 群）。

**(ii)** $$\Phi$$ 是群同态，$$\ker\Phi=\{\pm I\}$$。

**(iii)** $$\Phi$$ 是满射。因此
$$\mathrm{PSL}(2,\mathbb C)=\mathrm{SL}(2,\mathbb C)/\{\pm I\}\cong\mathrm{SO}^+(1,3).$$

*证明* **(i)** 若 $$X^*=X$$ 则 $$(AXA^*)^*=AX^*A^*=AXA^*$$，是 Hermite。$$\Phi(A)$$ 对 $$X$$ 显然是实线性的（$$A$$ 的元素是常数，$$\mathcal H$$ 是实向量空间）。保 $$\det$$：
$$\det(AXA^*)=\det A\cdot\det X\cdot\det A^*=\lvert\det A\rvert^2\det X=\det X .$$
由定理 3.5，$$\Phi(A)$$ 保持二次型 $$\langle\cdot,\cdot\rangle_{1,3}$$，故 $$\Phi(A)\in O(1,3)$$。

再看它落在哪个连通分支。若 $$X$$ 正定，则对任意 $$0\ne v\in\mathbb C^2$$，$$v^*AXA^*v=(A^*v)^*X(A^*v)>0$$（因 $$A^*$$ 可逆，$$A^*v\ne0$$），故 $$AXA^*$$ 正定。由定理 3.5 后的注，「$$X>0$$」等价于「$$\langle x,x\rangle_{1,3}>0$$ 且 $$x_0>0$$」，即 $$x$$ 落在**前向开光锥**（正的类时向量集）内。所以 $$\Phi(A)$$ 把前向开光锥映到自身，属于 $$O(1,3)$$ 中保时间方向的那些元素。$$O(1,3)$$ 有四个连通分支（由时间反演 $$T$$ 与空间反演 $$P$$ 生成），保前向光锥的那些构成两个分支 $$\mathrm{SO}^+(1,3)=O^+(1,3)\cap\mathrm{SL}$$（另一个是 $$\det=-1$$ 的）。最后，$$\mathrm{SL}(2,\mathbb C)$$ 是连通的（它在 $$\mathrm{GL}(2,\mathbb C)$$ 中由 $$\det=1$$ 这一多项式方程切出，是复代数簇的实形式，路径连通；或用 3.4 节的 QR 分解直接看出），而 $$\Phi$$ 连续，故 $$\Phi(\mathrm{SL}(2,\mathbb C))$$ 连通且落在保锥的那部分里；连通的那部分正是单位分支 $$\mathrm{SO}^+(1,3)$$。$$\square$$

**(ii)** 同态：
$$\Phi(AB)(X)=(AB)X(AB)^*=A\bigl(BXB^*\bigr)A^*=\Phi(A)\bigl(\Phi(B)X\bigr).$$
核：设 $$AXA^*=X$$ 对一切 Hermite $$X$$。取秩一的 $$X=vv^*$$（$$v\in\mathbb C^2$$ 非零，$$vv^*$$ 显然 Hermite），得
$$(Av)(Av)^*=vv^* .$$
两个秩一 Hermite 矩阵相等当且仅当它们的非零列向量只差一个单位模的标量：由 $$(Av)(Av)^*=vv^*$$ 两边作用得 $$Av$$ 与 $$v$$ 生成的是一维同一子空间，故 $$Av=\lambda_v v$$ 且 $$\lvert\lambda_v\rvert^2=1$$。于是 $$A$$ 把每一条复直线（每个一维子空间）映到自身。取线性无关的 $$u,w$$：由 $$Au=\lambda_u u$$、$$Aw=\lambda_w w$$、$$A(u+w)=\lambda_{u+w}(u+w)$$ 及 $$A(u+w)=Au+Aw$$，比较 $$u,w$$ 的系数得 $$\lambda_u=\lambda_w=\lambda_{u+w}$$。所以一切 $$\lambda_v$$ 都等于同一个 $$\lambda$$，即 $$A=\lambda I$$。再由 $$\det A=1$$ 得 $$\lambda^2=1$$，$$\lambda=\pm1$$。反之 $$\pm I$$ 显然在核里。$$\square$$

**(iii)** 两个群的维数都是 $$6$$（$$\dim_{\mathbb R}\mathrm{SL}(2,\mathbb C)=3\cdot2=6$$；$$\dim\mathrm{SO}(1,3)=\binom42=6$$）。由 (ii)，$$\ker\Phi$$ 是离散的（$$\{\pm I\}$$ 是有限集），故切映射 $$d\Phi_I:\mathfrak{sl}(2,\mathbb C)\to\mathfrak{so}(1,3)$$ 是单射：若不然，某个非零 $$X\in\mathfrak{sl}(2,\mathbb C)$$ 被送成 $$0$$，则单参数子群 $$t\mapsto\exp(tX)$$ 整个落在核里，与核离散矛盾。单射的两边同维线性映射是同构，故由反函数定理，$$\Phi$$ 在单位元附近是局部微分同胚：$$\Phi(\mathrm{SL}(2,\mathbb C))$$ 包含 $$\mathrm{SO}^+(1,3)$$ 的一个单位邻域 $$U$$。

群论收尾：$$\Phi(\mathrm{SL}(2,\mathbb C))$$ 是 $$\mathrm{SO}^+(1,3)$$ 的子群且含 $$U$$，故含由 $$U$$ 生成的子群；一个拓扑群的单位邻域生成的子群是**开**子群，而开子群同时是闭的（它的补是其余陪集的并，也是开集）。$$\mathrm{SO}^+(1,3)$$ 连通且非空，故没有非平凡的开闭子集，于是 $$\Phi(\mathrm{SL}(2,\mathbb C))=\mathrm{SO}^+(1,3)$$。$$\blacksquare$$

**注 3.6（$$A$$ 与 $$-A$$、Möbius 与 Lorentz 是同一张表）** 把定理 3.2(iii) 与定理 3.6(iii) 拼起来：
$$\mathrm{Möb}=\mathrm{PSL}(2,\mathbb C)=\mathrm{SL}(2,\mathbb C)/\{\pm I\}\cong\mathrm{SO}^+(1,3).$$
$$\pm A$$ 在 Möbius 侧是同一个 $$f_A$$，在 Lorentz 侧是同一个 $$\Phi(A)$$。更具体地，取 $$z=x+iy$$，则 $$X(x_0,x,y,x_3)$$ 的行列式为零恰好对应 $$\lvert z\rvert^2=x_0^2-x_3^2$$，即 **Riemann 球面 = 光锥的截面**：扩充复平面就是 Minkowski 空间的光锥在 $$\mathbb R^3$$ 上的投影（更准确地说，$$\widehat{\mathbb C}$$ 是 $$\mathbb R^{1,3}$$ 的**天球 (celestial sphere)**，即光锥中的射线方向之集）。于是 Möbius 群作用在 $$\widehat{\mathbb C}$$ 上，正是 Lorentz 群作用在光锥上——「分式线性变换把圆变成圆」与「Lorentz 变换把光锥变成光锥」是同一句话。

### 3.4 双重覆叠与中心扩张

**定义 3.7（覆叠群、双重覆叠与中心扩张, covering group, double cover, central extension）**

**(i)** 设 $$\pi:\tilde G\to G$$ 是 Lie 群同态。若 $$\ker\pi$$ 是离散子群，称 $$\tilde G$$ 为 $$G$$ 的**覆叠群 (covering group)**，$$\pi$$ 为**覆叠同态**。若进一步 $$\lvert\ker\pi\rvert=2$$，称这是**双重覆叠 (double cover)**。

**(ii)** 若正合列
$$1\longrightarrow A\longrightarrow\tilde G\xrightarrow{\ \pi\ }G\longrightarrow 1$$
中的 $$A$$ 落在 $$\tilde G$$ 的**中心** $$Z(\tilde G)$$ 内，称它是 $$G$$ 的一个**中心扩张 (central extension)**，$$\tilde G$$ 是 $$G$$ 的中心扩张。

**(iii)** 两个覆叠同态 $$\pi_1:\tilde G_1\to G$$、$$\pi_2:\tilde G_2\to G$$ 称为**同构的**，若存在群同构 $$\theta:\tilde G_1\to\tilde G_2$$ 使 $$\pi_2\circ\theta=\pi_1$$。

**定理 3.8（两次出现的同一个现象）**

**(i)** $$\mathrm{SU}(2)=S^3$$ 单连通，$$\pi_1(\mathrm{SO}(3))=\mathbb Z/2$$，覆叠同态 $$\rho:\mathrm{SU}(2)\to\mathrm{SO}(3)$$ 是**万有覆叠**、是双重覆叠，也是 $$\mathbb Z/2$$ 中心扩张（第 26 章定理 3.10）。

**(ii)** $$\mathrm{SL}(2,\mathbb C)$$ 单连通，覆叠同态 $$\Phi:\mathrm{SL}(2,\mathbb C)\to\mathrm{SO}^+(1,3)$$ 是万有覆叠（由定理 3.6，$$\ker\Phi=\{\pm I\}$$），故 $$\pi_1(\mathrm{SO}^+(1,3))\cong\mathbb Z/2$$；它同样是双重覆叠与 $$\mathbb Z/2$$ 中心扩张。

**(iii)** $$\mathrm{SU}(2)\to\mathrm{SO}(3)$$ 与 $$\mathrm{SL}(2,\mathbb C)\to\mathrm{SO}^+(1,3)$$ 都是第 29 章定理 3.11 的一般自旋覆叠 $$\mathrm{Spin}(V,q)\to SO(q)$$ 的实例：$$\mathrm{Spin}(3)\cong\mathrm{SU}(2)$$、$$\mathrm{Spin}(1,3)\cong\mathrm{SL}(2,\mathbb C)$$。

*证明* **(i)** 是第 26 章定理 3.10 的结论，此处引用。

**(ii)** 只需证 $$\mathrm{SL}(2,\mathbb C)$$ 单连通，其余由定理 3.6 与覆叠空间理论立得。用 **QR 分解**（对 $$2\times2$$ 的显式 Gram–Schmidt）：任取 $$A\in\mathrm{SL}(2,\mathbb C)$$，把它的两列记为 $$u,v$$。令
$$q_1=\frac{u}{\lVert u\rVert},\qquad q_2=\frac{w}{\lVert w\rVert},\qquad w=v-\langle v,q_1\rangle q_1,$$
其中 $$\lVert z\rVert^2=\lvert z_1\rvert^2+\lvert z_2\rvert^2$$、$$\langle\cdot,\cdot\rangle$$ 是 $$\mathbb C^2$$ 上的标准 Hermite 内积。则 $$Q=[q_1\ q_2]\in\mathrm{U}(2)$$（两列标准正交），且
$$A=QR,\qquad R=\begin{pmatrix}\lVert u\rVert&\langle v,q_1\rangle\\ 0&\lVert w\rVert\end{pmatrix}$$
是上三角。$$A$$ 可逆保证 $$u\ne0$$、$$w\ne0$$，故对角元 $$\lVert u\rVert,\lVert w\rVert$$ 都是正实数。取行列式：$$\det A=\det Q\cdot\det R$$，其中 $$\det R=\lVert u\rVert\lVert w\rVert>0$$，而 $$\lvert\det Q\rvert=1$$（$$Q$$ 酉）。由 $$\det A=1>0$$ 得 $$\det Q>0$$，故 $$\det Q=1$$：**不必再做任何调整**，$$Q$$ 自动落在 $$\mathrm{SU}(2)$$ 里；同时 $$\det R=1$$ 给出 $$\lVert w\rVert=\lVert u\rVert^{-1}$$。于是
$$R=\begin{pmatrix}t&s\\ 0&t^{-1}\end{pmatrix},\qquad t=\lVert u\rVert>0,\quad s\in\mathbb C .$$

现在对 $$A=QR$$ 作连续形变：对 $$\lambda\in[0,1]$$ 令
$$R_\lambda=\begin{pmatrix}t^{1-\lambda}&s\\ 0&t^{\lambda-1}\end{pmatrix},\qquad A_\lambda=Q\,R_\lambda .$$
每个 $$A_\lambda$$ 都可逆（对角元非零）且 $$\det A_\lambda=\det Q\cdot t^{1-\lambda}\cdot t^{\lambda-1}=1$$，故 $$A_\lambda\in\mathrm{SL}(2,\mathbb C)$$；$$\lambda=0$$ 给出 $$A$$，$$\lambda=1$$ 给出 $$Q\in\mathrm{SU}(2)$$。映射 $$\lambda\mapsto A_\lambda$$ 连续，且 $$\lambda=1$$ 端的值对每个 $$A$$ 都落在同一个集合 $$\mathrm{SU}(2)$$ 内。于是
$$H:[0,1]\times\mathrm{SL}(2,\mathbb C)\to\mathrm{SL}(2,\mathbb C),\qquad H(\lambda,A)=A_\lambda$$
给出 $$\mathrm{SL}(2,\mathbb C)$$ 到 $$\mathrm{SU}(2)$$ 的**形变收缩**：它连续、$$H(0,A)=A$$、$$H(1,A)\in\mathrm{SU}(2)$$、且 $$H(\lambda,A)=A$$ 当 $$A\in\mathrm{SU}(2)$$（此时 $$t=1$$）。

形变收缩不改变同伦型，故 $$\pi_1(\mathrm{SL}(2,\mathbb C))\cong\pi_1(\mathrm{SU}(2))$$。而 $$\mathrm{SU}(2)=\Bigl\{\begin{pmatrix}\alpha&\beta\\ -\bar\beta&\bar\alpha\end{pmatrix}:\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1\Bigr\}$$ 与单位球面 $$S^3$$ 同胚（把 $$(\alpha,\beta)$$ 读成 $$\mathbb C^2\cong\mathbb R^4$$ 中的单位向量），由第 08 章 $$S^3$$ 单连通。故 $$\mathrm{SL}(2,\mathbb C)$$ 单连通。

最后，由定理 3.6 的 $$\Phi$$ 是满射且核为 $$\pm I$$、而 $$\mathrm{SL}(2,\mathbb C)$$ 单连通，$$\Phi$$ 是**万有覆叠**，覆叠的层数等于基本群的阶，故 $$\pi_1(\mathrm{SO}^+(1,3))\cong\mathbb Z/2$$。$$\blacksquare$$

**(iii)** 由第 29 章定理 3.11 的 $$\rho:\mathrm{Spin}(V,q)\to O(q)$$ 与第 29 章 3.4 节末注（$$\mathrm{Spin}(1,3)\cong\mathrm{SL}(2,\mathbb C)$$）；$$\mathrm{Spin}(3)\cong\mathrm{SU}(2)$$ 是第 26 章的四元数构造。$$\blacksquare$$

**例 3.8（$$\mathrm{Spin}(n)$$ 一族）** 对 $$n\ge3$$，$$\mathrm{Spin}(n)\to\mathrm{SO}(n)$$ 是双重覆叠，$$\pi_1(\mathrm{SO}(n))=\mathbb Z/2$$；进一步，$$n\ge3$$ 时 $$\mathrm{Spin}(n)$$ 单连通，故它是万有覆叠。低维的例外让人一眼看出这件事实的「偶然性」：
$$\mathrm{Spin}(3)\cong\mathrm{SU}(2)\cong S^3,\quad \mathrm{Spin}(4)\cong\mathrm{SU}(2)\times\mathrm{SU}(2),\quad \mathrm{Spin}(5)\cong\mathrm{Sp}(2),\quad \mathrm{Spin}(6)\cong\mathrm{SU}(4).$$
而 $$n=2$$ 时 $$\mathrm{SO}(2)=S^1$$ 的覆叠群是 $$\mathbb R$$（$$\pi_1=\mathbb Z$$），不是双重覆叠——因为 $$\mathrm{SO}(2)$$ 交换，中心的元可以「无穷阶」，与 $$n\ge3$$ 的 $$\mathbb Z/2$$ 属于两类现象。

### 3.5 射影表示、上循环与提升

前三节说明「每个 $$A$$ 与 $$-A$$ 不可区分」。现在把这个「不可区分」本身当成研究的对象。

**定义 3.9（射影表示, projective representation）** 设 $$G$$ 是群，$$V$$ 是 $$\mathbb C$$ 上向量空间。记
$$\mathrm{GL}(V)/\mathbb C^*I=:\mathrm{PGL}(V)$$
（$$\mathbb C^*I$$ 是标量变换群，它是 $$\mathrm{GL}(V)$$ 的中心）。一个**射影表示**是同态
$$\alpha:G\longrightarrow\mathrm{PGL}(V).$$
等价的说法：$$G$$ 作用在射影空间 $$\mathbb P(V)$$ 上，且每个作用由 $$V$$ 的一个线性变换诱导。

**定理 3.10（提升给出上循环）** 设 $$\alpha:G\to\mathrm{PGL}(V)$$ 是射影表示。**任取**一组提升：对每个 $$g\in G$$ 选一个 $$\rho(g)\in\mathrm{GL}(V)$$ 使它的像 $$[\rho(g)]$$ 等于 $$\alpha(g)$$（这只是「选择」，不要求 $$\rho$$ 连续、也不要求是同态；用选择公理即可）。则存在唯一函数 $$c:G\times G\to\mathbb C^*$$ 使
$$\rho(g)\rho(h)=c(g,h)\,\rho(gh)\qquad\text{对一切 }g,h\in G. \tag{30.1}$$
并且 $$c$$ 自动满足**上循环条件 (cocycle condition)**
$$c(g,h)\,c(gh,k)=c(g,hk)\,c(h,k)\qquad\text{对一切 }g,h,k\in G. \tag{30.2}$$
若改选另一组提升 $$\rho'(g)=\beta(g)\rho(g)$$（$$\beta:G\to\mathbb C^*$$ 是任意函数），则对应的上循环变成
$$c'(g,h)=\frac{\beta(g)\beta(h)}{\beta(gh)}\,c(g,h). \tag{30.3}$$
形如 $$\dfrac{\beta(g)\beta(h)}{\beta(gh)}$$ 的上循环称为**上边界 (coboundary)**；两个只差一个上边界的上循环称为**上同调 (cohomologous)**。全体上循环模去上边界记作 $$H^2(G;\mathbb C^*)$$，称为 $$G$$ 的**第 2 上同调群 (second cohomology group)**。

*证明* **存在与唯一**：由 $$[\rho(g)][\rho(h)]=\alpha(g)\alpha(h)=\alpha(gh)=[\rho(gh)]$$，两个可逆算子的像相同，即 $$\rho(g)\rho(h)$$ 与 $$\rho(gh)$$ 只差一个标量，设为 $$c(g,h)\in\mathbb C^*$$；$$\rho(gh)$$ 可逆保证这个标量由两者唯一确定（$$\rho(g)\rho(h)=c\,\rho(gh)$$ 中 $$c=\dfrac{(\rho(g)\rho(h))_{ij}}{(\rho(gh))_{ij}}$$ 对任一非零元素取值）。

**上循环条件**：把 (30.1) 用两种方式结合 $$(\rho(g)\rho(h))\rho(k)$$。
$$
(\rho(g)\rho(h))\rho(k)=c(g,h)\rho(gh)\rho(k)=c(g,h)\,c(gh,k)\,\rho(ghk),
$$
$$
\rho(g)(\rho(h)\rho(k))=\rho(g)\,c(h,k)\rho(hk)=c(h,k)\,c(g,hk)\,\rho(ghk).
$$
标量 $$c$$ 是中心元，可以随意搬运。两式相等而 $$\rho(ghk)$$ 可逆，故 $$c(g,h)c(gh,k)=c(h,k)c(g,hk)$$，即 (30.2)。

**(30.3)**：$$\rho'(g)\rho'(h)=\beta(g)\beta(h)\rho(g)\rho(h)=\beta(g)\beta(h)c(g,h)\rho(gh)$$，而 $$\rho'(gh)=\beta(gh)\rho(gh)$$，故 $$c'(g,h)=\beta(g)\beta(h)c(g,h)/\beta(gh)$$。$$\blacksquare$$

**定理 3.11（可线性化 $$\iff$$ 上循环是上边界）** 设 $$\alpha:G\to\mathrm{PGL}(V)$$ 是射影表示，$$\rho$$ 是一组提升，$$c$$ 是相应的上循环。则存在**线性表示** $$\tilde\rho:G\to\mathrm{GL}(V)$$ 使 $$[\tilde\rho(g)]=\alpha(g)$$ 对一切 $$g$$ 成立，当且仅当 $$c$$ 是上边界。

更一般地，定义
$$\tilde G_\alpha=\{(g,A)\in G\times\mathrm{GL}(V):\ [A]=\alpha(g)\},$$
按分量乘法取群结构。则 $$\tilde G_\alpha$$ 是一个群，投影
$$\pi:\tilde G_\alpha\to G,\qquad \pi(g,A)=g$$
是满同态，其核 $$\{(e,\lambda I):\lambda\in\mathbb C^*\}\cong\mathbb C^*$$ 落在 $$Z(\tilde G_\alpha)$$ 内。于是 $$\tilde G_\alpha$$ 是 $$G$$ 的一个中心扩张；而「$$\alpha$$ 可线性化」等价于「这个扩张存在同态截面 $$\sigma:G\to\tilde G_\alpha$$（即 $$\pi\circ\sigma=\operatorname{id}_G$$）」。

*证明* **(⇐)** 设 $$c(g,h)=\beta(g)\beta(h)/\beta(gh)$$。令 $$\tilde\rho(g)=\beta(g)^{-1}\rho(g)$$。则
$$\tilde\rho(g)\tilde\rho(h)=\beta(g)^{-1}\beta(h)^{-1}c(g,h)\rho(gh)=\beta(g)^{-1}\beta(h)^{-1}\frac{\beta(g)\beta(h)}{\beta(gh)}\rho(gh)=\beta(gh)^{-1}\rho(gh)=\tilde\rho(gh),$$
故 $$\tilde\rho$$ 是同态；又 $$[\tilde\rho(g)]=[\rho(g)]=\alpha(g)$$。

**(⇒)** 设 $$\tilde\rho:G\to\mathrm{GL}(V)$$ 是线性表示且 $$[\tilde\rho(g)]=\alpha(g)$$。则 $$\tilde\rho(g)=\beta(g)\rho(g)$$ 对唯一确定的 $$\beta(g)\in\mathbb C^*$$，代入定理 3.10(30.3) 并注意 $$\tilde\rho$$ 对应的平凡上循环是 $$\beta\equiv1$$ 的 $$c\equiv1$$，得 $$c(g,h)=\beta(g)\beta(h)/\beta(gh)$$，是上边界。

**$$\tilde G_\alpha$$ 是群**：若 $$[A]=\alpha(g)$$、$$[B]=\alpha(h)$$，则 $$[AB]=[A][B]=\alpha(g)\alpha(h)=\alpha(gh)$$，故 $$(g,A)(h,B)=(gh,AB)$$ 仍在 $$\tilde G_\alpha$$ 内；结合律继承自 $$G$$ 与 $$\mathrm{GL}(V)$$；单位元是 $$(e,I)$$；逆元 $$(g,A)^{-1}=(g^{-1},A^{-1})$$（因 $$[A^{-1}]=[A]^{-1}=\alpha(g)^{-1}=\alpha(g^{-1})$$）。核：$$\pi(g,A)=e\iff g=e\iff[A]=\alpha(e)=[I]\iff A=\lambda I$$，故 $$\ker\pi=\{(e,\lambda I)\}\cong\mathbb C^*$$。中心性：$$(g,A)(e,\lambda I)=(g,\lambda A)=(e,\lambda I)(g,A)$$。

**与截面的等价**：给定线性表示 $$\tilde\rho$$，映射 $$\sigma(g)=(g,\tilde\rho(g))$$ 是 $$\tilde G_\alpha$$ 中的元素且 $$\pi\circ\sigma=\operatorname{id}$$，并且 $$\sigma$$ 是同态（$$\sigma(g)\sigma(h)=(gh,\tilde\rho(g)\tilde\rho(h))=(gh,\tilde\rho(gh))=\sigma(gh)$$）。反之给定同态截面 $$\sigma$$，写 $$\sigma(g)=(g,\tilde\rho(g))$$，则 $$\sigma$$ 是同态立即给出 $$\tilde\rho(gh)=\tilde\rho(g)\tilde\rho(h)$$，且 $$[\tilde\rho(g)]=\alpha(g)$$。$$\blacksquare$$

**注 3.11（为什么中心扩张让「唯一性」变强）** 定理 3.11 说：射影表示是「差一个标量」的同态，而把它「提正」的代价是把群换大——换成一个中心扩张。第 22 章已经见过这件事最漂亮的一次兑现：相空间 $$\mathbb R^2$$ 的平移群是交换群，它的射影表示带着相位上循环 $$(s,t)\mapsto e^{-i\hbar st}$$；把它提正得到Heisenberg群 $$H_3(\mathbb R)$$，而 Stone–von Neumann 定理说：固定中心特征（即固定 $$\hbar$$）后，$$H_3(\mathbb R)$$ 的不可约酉表示在等价意义下**唯一**。也就是说，**射影表示的「不唯一」在中心扩张后反而变成了「唯一」**。这是「上同调非平凡 ⇒ 表示反被刚化」的第一个范例。

**定理 3.12（自旋射影表示不可线性化）** 记 $$\rho:\mathrm{SU}(2)\to\mathrm{SO}(3)$$ 为第 26 章的双重覆叠（$$\rho(q)=\rho(-q)$$，$$\ker\rho=\{\pm I\}$$）。对 $$R\in\mathrm{SO}(3)$$ 取 $$\rho^{-1}(R)$$ 中任一元素，记它在 $$\mathrm{PGL}(2,\mathbb C)$$ 中的类为 $$\alpha(R)$$——由 $$-q$$ 与 $$q$$ 同类，这个类与代表元的选取无关。则

**(i)** $$\alpha:\mathrm{SO}(3)\to\mathrm{PGL}(2,\mathbb C)$$ 是射影表示（事实上是同态）；

**(ii)** 不存在线性表示 $$\tilde\rho:\mathrm{SO}(3)\to\mathrm{GL}(2,\mathbb C)$$ 使 $$[\tilde\rho(R)]=\alpha(R)$$ 对一切 $$R$$ 成立。即 $$\alpha$$ **不可线性化**。

*证明* **(i)** 设 $$\rho(q)=R$$、$$\rho(p)=S$$。由 $$\rho$$ 同态，$$\rho(qp)=RS$$，故 $$\alpha(R)\alpha(S)=[q][p]=[qp]=\alpha(RS)$$。（这里 $$[q][p]=[qp]$$ 是 $$\mathrm{PGL}$$ 中乘法的定义。）$$\square$$

**(ii)** 反设存在这样的 $$\tilde\rho$$。令
$$\psi=\tilde\rho\circ\rho:\ \mathrm{SU}(2)\to\mathrm{GL}(2,\mathbb C).$$
$$\psi$$ 是连续同态。又对一切 $$q$$，
$$[\psi(q)]=[\tilde\rho(\rho(q))]=\alpha(\rho(q))=[q],$$
故存在唯一标量 $$\varphi(q)\in\mathbb C^*$$ 使
$$\psi(q)=\varphi(q)\,q. \tag{30.4}$$
（这里把 $$q\in\mathrm{SU}(2)\subset\mathrm{GL}(2,\mathbb C)$$ 本身看成 (30.4) 右端的第二个因子。）

**第一步：$$\varphi$$ 是群同态。** 用 (30.4) 两次：
$$\varphi(qp)\,qp=\psi(qp)=\psi(q)\psi(p)=\varphi(q)\varphi(p)\,qp .$$
矩阵 $$qp$$ 可逆，故 $$\varphi(qp)=\varphi(q)\varphi(p)$$。特别地 $$\varphi(1)=1$$。

**第二步：$$\varphi$$ 连续。** 记 $$\psi(q)=(\psi_{ij}(q))$$、$$q=(q_{ij})$$。集合 $$U=\{q\in\mathrm{SU}(2):q_{11}\ne0\}$$ 是 $$\mathrm{SU}(2)$$ 中的非空开集（例如 $$I\in U$$），且在 $$U$$ 上由 (30.4) 有 $$\varphi=\psi_{11}/q_{11}$$——两个连续函数的商，故 $$\varphi$$ 在 $$U$$ 上连续。对任意的 $$q\in\mathrm{SU}(2)$$，取 $$p\in U$$ 使 $$qp\in U$$（这样的 $$p$$ 存在：$$U$$ 非空开，$$q^{-1}U$$ 也非空开，取 $$p\in q^{-1}U\cap U$$）。于是 $$\varphi(q)=\varphi(qp)/\varphi(p)$$ 在 $$q$$ 的一个邻域内是连续函数的商，故 $$\varphi$$ 在每个点连续。

**第三步：$$\varphi\equiv1$$。** 由第二小步，$$\varphi$$ 连续；由第一步，它是同态。于是它把换位子送到换位子：
$$\varphi\bigl([\mathrm{SU}(2),\mathrm{SU}(2)]\bigr)\subseteq[\mathbb C^*,\mathbb C^*]=\{1\},$$
因为 $$\mathbb C^*$$ 交换。而 $$\mathrm{SU}(2)$$ 是**完美群**，即等于自己的换位子群：它的 Lie 代数 $$\mathfrak{su}(2)$$ 是单 Lie 代数，满足 $$[\mathfrak{su}(2),\mathfrak{su}(2)]=\mathfrak{su}(2)\ne0$$，而连通 Lie 群的换位子群的 Lie 代数是换位子子代数（第 27 章），故 $$[\mathrm{SU}(2),\mathrm{SU}(2)]$$ 的 Lie 代数是整个 $$\mathfrak{su}(2)$$，从而是 $$\mathrm{SU}(2)$$ 的开子群；开子群又闭，而 $$\mathrm{SU}(2)$$ 连通，故它就是 $$\mathrm{SU}(2)$$ 本身。因此
$$\varphi(\mathrm{SU}(2))=\varphi\bigl([\mathrm{SU}(2),\mathrm{SU}(2)]\bigr)=\{1\},$$
即 $$\varphi\equiv1$$。

**第四步：矛盾。** 由第三步，(30.4) 给出 $$\psi(q)=q$$ 对一切 $$q\in\mathrm{SU}(2)$$。但 $$\psi=\tilde\rho\circ\rho$$ 经过 $$\rho$$ 分解，故 $$\psi(q)=\psi(-q)$$。取 $$q=1$$：$$\psi(-1)=\psi(1)=I$$。另一方面 $$\psi(-1)=-1\ne I$$。矛盾。故这样的 $$\tilde\rho$$ 不存在。$$\blacksquare$$

**注 3.12（这个证明只需要三件事实）** 上面用到的只是：$$\mathrm{SU}(2)$$ 连通且完美（第三步）、$$\varphi$$ 连续（第二步）、$$\rho$$ 的核是 $$\{\pm I\}$$。没有任何地方用到维数、显式矩阵或紧性。所以同样的论证适用于 $$\mathrm{SL}(2,\mathbb C)\to\mathrm{SO}^+(1,3)$$——注意 $$\mathrm{SL}(2,\mathbb C)$$ **不紧**，但它仍然连通且完美（其 Lie 代数 $$\mathfrak{sl}(2,\mathbb C)$$ 单，$$[\mathfrak{sl},\mathfrak{sl}]=\mathfrak{sl}$$），这三件事实一条不缺。于是：把同构 $$\mathrm{SO}^+(1,3)\cong\mathrm{PSL}(2,\mathbb C)$$ 看作 $$\mathrm{SO}^+(1,3)$$ 在 $$\mathbb C^2$$ 上的射影表示，它也**不可线性化**。这就回答了入口问题 B 的第 (2) 问在一般维数下的样子。

### 3.6 半整数自旋的来源

现在把入口问题 B 彻底解决：那个「不可线性化的射影表示」为什么在物理上偏偏是自旋 $$1/2$$？

**定理 3.13（$$\mathrm{SU}(2)$$ 的不可约表示与下降判据）**

**(i)** $$\mathrm{SU}(2)$$ 的不可约复表示恰为一列
$$V_j,\qquad j\in\Bigl\{0,\tfrac12,1,\tfrac32,2,\dots\Bigr\},\qquad \dim V_j=2j+1,$$
其中 $$V_j=\operatorname{Sym}^{2j}(\mathbb C^2)$$ 是 $$\mathbb C^2$$ 上 $$2j$$ 次对称张量幂，$$2j$$ 是它在 $$\mathfrak{sl}(2,\mathbb C)$$ 意义下的最高权（第 28 章入口题 (iii) 的分类，$$m=2j$$）。

**(ii)** 中心元 $$-I\in\mathrm{SU}(2)$$ 在 $$V_j$$ 上作用为标量 $$(-1)^{2j}$$。

**(iii)** $$V_j$$ 下降为商群 $$\mathrm{SO}(3)=\mathrm{SU}(2)/\{\pm I\}$$ 的一个（线性）表示，当且仅当 $$j\in\mathbb Z$$。当 $$j\in\tfrac12+\mathbb Z$$ 时，$$V_j$$ 只给出 $$\mathrm{SO}(3)$$ 的一个射影表示，且它不可线性化。

**(iv)** 特别地，$$V_{1/2}\cong\mathbb C^2$$ 正是定理 3.12 里那个自旋射影表示。于是「自旋 $$1/2$$ 的态转 $$360°$$ 变号」这件事的最终解释是：**$$-I\in\mathrm{SU}(2)$$ 在 $$V_{1/2}$$ 上的特征值是 $$(-1)^{2\cdot1/2}=-1$$，而 $$\mathrm{SO}(3)=\mathrm{SU}(2)/\{\pm I\}$$ 把这个 $$-I$$ 与 $$I$$ 认成了同一个元素。** 群论允许「$$-I$$ 与 $$I$$ 等价」而表示论知道「它们作用不同」——这个差额就是射影表示。

*证明* **(i)** 这是第 28 章入口题 (iii)（$$\mathfrak{sl}(2,\mathbb C)$$ 的有限维不可约表示与最高权 $$m\in\mathbb Z_{\ge0}$$ 一一对应、维数 $$m+1$$、权集 $$m,m-2,\dots,-m$$）在紧群 $$\mathrm{SU}(2)$$ 上的实现：$$\mathrm{SU}(2)$$ 的复化 Lie 代数是 $$\mathfrak{sl}(2,\mathbb C)$$，$$\mathrm{SU}(2)$$ 单连通，故 $$\mathrm{SU}(2)$$ 的表示与 $$\mathfrak{sl}(2,\mathbb C)$$ 的表示一一对应（第 27 章的指数映射）。取 $$m=2j$$ 即得 $$V_j=\operatorname{Sym}^{m}\mathbb C^2$$。$$\square$$

**(ii)** 取 $$\mathbb C^2$$ 的标准基 $$e_1,e_2$$。$$-I$$ 把 $$e_1\mapsto-e_1$$、$$e_2\mapsto-e_2$$。$$V_j=\operatorname{Sym}^{2j}\mathbb C^2$$ 由单项式 $$e_1^ae_2^b$$（$$a+b=2j$$）张成。对称幂的作用是
$$(-I)\cdot e_1^ae_2^b=(-e_1)^a(-e_2)^b=(-1)^{a+b}e_1^ae_2^b=(-1)^{2j}e_1^ae_2^b .$$
故 $$-I$$ 在 $$V_j$$ 上就是 $$(-1)^{2j}$$ 倍恒等。$$\square$$

**(iii)** 下降判据：群同态 $$\mathrm{SU}(2)\to\mathrm{GL}(V_j)$$ 经过商 $$\mathrm{SU}(2)\to\mathrm{SU}(2)/\{\pm I\}=\mathrm{SO}(3)$$ 分解，当且仅当它在 $$\ker=\{\pm I\}$$ 上是平凡的，即 $$-I$$ 作用为 $$I$$，由 (ii) 即 $$(-1)^{2j}=1$$，等价于 $$2j$$ 是偶数，等价于 $$j\in\mathbb Z$$。

当 $$j\in\tfrac12+\mathbb Z$$ 时，$$(-1)^{2j}=-1$$，故 $$\rho_j:\mathrm{SU}(2)\to\mathrm{GL}(V_j)$$ 不下降；但它在 $$\mathrm{PGL}(V_j)$$ 中的像下降（因为 $$[-I]=[I]$$ 在 $$\mathrm{PGL}$$ 中成立），得到射影表示
$$\alpha_j:\mathrm{SO}(3)\to\mathrm{PGL}(V_j),\qquad \alpha_j(R)=[\rho_j(q)],\ \rho(q)=R .$$
不可线性化：完全重复定理 3.12 的论证，只把 $$\rho:\mathrm{SU}(2)\to\mathrm{SO}(3)$$ 用上。设 $$\tilde\rho:\mathrm{SO}(3)\to\mathrm{GL}(V_j)$$ 线性且 $$[\tilde\rho(R)]=\alpha_j(R)$$。令 $$\psi=\tilde\rho\circ\rho:\mathrm{SU}(2)\to\mathrm{GL}(V_j)$$。由
$$[\psi(q)]=[\tilde\rho(\rho(q))]=\alpha_j(\rho(q))=[\rho_j(q)]$$
得 $$\psi(q)=\varphi(q)\rho_j(q)$$ 对唯一 $$\varphi(q)\in\mathbb C^*$$。同定理 3.12 的第一步与第二步得 $$\varphi$$ 是连续同态，第三步得 $$\varphi\equiv1$$，于是 $$\psi=\rho_j$$。但 $$\psi$$ 经过 $$\rho$$ 分解，故 $$\psi(q)=\psi(-q)$$；取 $$q=1$$ 得 $$\rho_j(-1)=\rho_j(1)=I$$，即 $$(-1)^{2j}=1$$，与 $$j\in\tfrac12+\mathbb Z$$ 矛盾。$$\square$$

**(iv)** $$j=\tfrac12$$ 时 $$2j=1$$，$$V_{1/2}=\operatorname{Sym}^1\mathbb C^2=\mathbb C^2$$，且 $$\alpha_{1/2}=\alpha$$（定理 3.12 的射影表示）。$$(-1)^{2j}=-1$$ 就是入口问题 B 里 $$U(2\pi)=-I$$ 的来源。$$\blacksquare$$

**注 3.13（「半整数自旋」这个名字的来历）** 在物理文献里，$$j$$ 被称为**自旋 (spin)**，$$V_j$$ 是自旋 $$j$$ 的态空间。定理 3.13(iii) 说的是：**自旋为整数的粒子，其态空间是 $$\mathrm{SO}(3)$$ 的线性表示；自旋为半整数的粒子（电子、质子、中子），其态空间只是 $$\mathrm{SO}(3)$$ 的射影表示**——在 $$\mathrm{O}(3)$$ 或 $$\mathrm{SO}(3)$$ 层面写不出「转 $${360}^{\circ}$$ 之后态变号」这个规则，只有在双重覆叠 $$\mathrm{SU}(2)$$ 上才写得出。这就是「半整数自旋必须用双重覆叠描述」的精确含义。它不是一个关于「电子内部转动」的假设，而是群 $$\mathrm{SO}(3)$$ 的射影表示分类给出的**唯一**半整数选项：$$j$$ 只能取 $$\tfrac12,\tfrac32,\tfrac52,\dots$$。

## 四、几何与物理直觉 (Intuition)

### 4.1 三个空间，一张对应表

本章出现三个「看起来毫不相干」的对象，它们其实是同一件事的三种写法：

| | 群 | 作在什么上 | 覆叠群 |
|---|---|---|---|
| 复分析 | Möbius 群 $$\mathrm{PSL}(2,\mathbb C)$$ | 扩充复平面 $$\widehat{\mathbb C}$$（Riemann 球面） | $$\mathrm{SL}(2,\mathbb C)$$ |
| 相对论 | $$\mathrm{SO}^+(1,3)$$ | Minkowski 空间的前向光锥 | $$\mathrm{SL}(2,\mathbb C)$$ |
| 量子力学 | $$\mathrm{SO}(3)$$ | $$\mathbb R^3$$（或射影 Hilbert 空间） | $$\mathrm{SU}(2)$$ |

中间一列的两个「作在什么上」被同构连起来：$$\widehat{\mathbb C}$$ 是光锥中**射线**的集合（天球），Möbius 变换作用在 $$\widehat{\mathbb C}$$ 上就是 Lorentz 变换作用在光锥的射线上。第三行是第一行的「实数低维版」：把 Hermite 矩阵换成迹为零的 Hermite 矩阵（即 $$\mathfrak{su}(2)\cong\mathbb R^3$$），$$\mathrm{SL}(2,\mathbb C)$$ 换成 $$\mathrm{SU}(2)$$，$$\det$$ 换成 $$-\det$$（欧氏范数平方），定理 3.6 的整套证明逐字搬过去，得到 $$\mathrm{SU}(2)/\{\pm I\}\cong\mathrm{SO}(3)$$（第 26 章）。

### 4.2 「双重」在几何上长什么样

双重覆叠的几何图像是**两叶覆盖**：底空间上的每个点，上方有两叶。以 $$\mathrm{SU}(2)=S^3\to\mathrm{SO}(3)=\mathbb{RP}^3$$ 为例，$$S^3$$ 上对径的两点被粘成同一个旋转（第 26 章已经画过「对径粘合的实心球」）。

$$\mathrm{SL}(2,\mathbb C)\to\mathrm{SO}^+(1,3)$$ 的图像没有这么直观的低维模型，但性质完全相同：底群上的每条闭路，提升到覆叠群上**未必**闭。只要底空间里存在一条「缩不掉的闭路」（即 $$\pi_1\ne0$$），就会有「提升之后从 $$I$$ 走到 $$-I$$」的现象。这正是入口问题 B 的几何内容：转 $$360°$$ 是 $$\mathrm{SO}(3)$$ 中一条非零伦闭路，它的提升从 $$1$$ 走到 $$-1$$。

**关键点：双重覆叠不可拆开。** 不存在连续的映射 $$s:\mathrm{SO}(3)\to\mathrm{SU}(2)$$ 使 $$\rho\circ s=\operatorname{id}$$（否则 $$\mathrm{SU}(2)$$ 会与 $$\mathrm{SO}(3)\times\{\pm1\}$$ 同胚，而后者不连通，与 $$S^3$$ 连通矛盾）。「不可拆开」在射影语言里就是「上循环不是上边界」，在物理语言里就是「相位没法一致地选掉」。这三句话是同一句话。

### 4.3 物理：量子态的空间是射影的

量子力学里，态由 Hilbert 空间 $$\mathcal H$$ 中的**非零向量**描述，但 $$\psi$$ 与 $$\lambda\psi$$（$$\lambda\in\mathbb C^*$$）代表同一个物理态。所以真正的态空间是**射影 Hilbert 空间** $$\mathbb P(\mathcal H)$$。

于是任何对称性只能被实现为 $$\mathcal H$$ 上的**射影表示**：Wigner 定理说，量子对称性是射影空间上保持转移概率（等价地，保持 Hermite 内积的模）的变换，而这样的变换总能被 $$\mathcal H$$ 上的酉或反酉算子在相差一个相位的意义下实现。**相位的不确定性不是缺陷，它是态空间本身的射影性质。**定理 3.11 告诉我们，这个「相位的不确定性」可以被一个整体的**上同调类**精确度量：类平凡，就能一致地消掉相位，得到线性表示；类不平凡，就必须换到中心扩张上去。

自旋 $$1/2$$ 正是「类不平凡」的最小例子。物理上的中子干涉实验（把中子绕一圈，干涉条纹变号；绕两圈才复原）测的就是这个上同调类。

### 4.4 几何 $$\leftrightarrow$$ 物理 $$\leftrightarrow$$ 代数：本章的合流点

本章的收口正是这条主线的一次完整兑现，四个说法指的是同一个数学对象：

1. **几何**：$$\mathrm{SO}(3)$$ 里「转一整圈」的闭路不可收缩（$$\pi_1=\mathbb Z/2$$，第 26 章）；
2. **代数（覆叠）**：存在双重覆叠 $$\mathrm{SU}(2)\to\mathrm{SO}(3)$$，$$\mathrm{SU}(2)$$ 是万有覆叠，$$\mathrm{SO}(3)=\mathrm{SU}(2)/\{\pm I\}$$；
3. **代数（上同调）**：相应的上循环不是上边界，$$H^2(\mathrm{SO}(3);\mathbb C^*)\ne0$$；
4. **物理**：半整数自旋的态空间只是 $$\mathrm{SO}(3)$$ 的射影表示，$$\mathrm{SU}(2)$$ 上的线性表示才是它「真正的家」；实验上表现为转 $$360°$$ 出负号。

第 22 章的Heisenberg群是同一件事的另一个实例（那里底群是 $$\mathbb R^2$$ 的平移群，中心扩张是 $$H_3(\mathbb R)$$，上循环是 $$\exp(-i\hbar st)$$，「不可消掉」体现为 $$\hbar$$ 是一个不能连续变到 $$0$$ 的参数），第 29 章的旋量群是它在一般维数里的推广。这三处合起来说明：**射影表示不是技术细节，而是「群作用在射影空间上」这一普遍情形的名字。**

## 五、经典问题精讲 (Classical Problems)

### 题 1：从矩阵读出 boost 与旋转

**考点** 定理 3.6 的显式计算。**位置** 本节是「Möbius 群 = Lorentz 群」这句等式最具体的一次落地。

**问题** 取 $$A_t=\begin{pmatrix}e^{t/2}&0\\ 0&e^{-t/2}\end{pmatrix}$$（$$t\in\mathbb R$$）与 $$B_\theta=\begin{pmatrix}e^{i\theta/2}&0\\ 0&e^{-i\theta/2}\end{pmatrix}$$。两者都在 $$\mathrm{SL}(2,\mathbb C)$$ 中。算出 $$\Phi(A_t)$$ 与 $$\Phi(B_\theta)$$ 作为 $$\mathbb R^{1,3}$$ 上线性变换的显式形式，并指出它们分别是什么几何变换。

**解** 记 $$X=\begin{pmatrix}x_0+x_3&x_1-ix_2\\ x_1+ix_2&x_0-x_3\end{pmatrix}$$。

**先算 $$A_t$$**（它是实矩阵，且正定）：
$$A_tXA_t^*=\begin{pmatrix}e^{t/2}&0\\ 0&e^{-t/2}\end{pmatrix}\begin{pmatrix}x_0+x_3&x_1-ix_2\\ x_1+ix_2&x_0-x_3\end{pmatrix}\begin{pmatrix}e^{t/2}&0\\ 0&e^{-t/2}\end{pmatrix}=\begin{pmatrix}e^{t}(x_0+x_3)&x_1-ix_2\\ x_1+ix_2&e^{-t}(x_0-x_3)\end{pmatrix}.$$
（中间一步：左乘把第 $$i$$ 行乘 $$(A_t)_{ii}$$，右乘把第 $$j$$ 列乘 $$\overline{(A_t)_{jj}}=(A_t)_{jj}$$，故 $$(i,j)$$ 元乘 $$e^{t/2}e^{-t/2}=1$$ 若 $$i=j$$；对角元分别乘 $$e^{t}$$ 与 $$e^{-t}$$。）
读出：$$x_1,x_2$$ 不变，而
$$x_0+x_3\ \mapsto\ e^{t}(x_0+x_3),\qquad x_0-x_3\ \mapsto\ e^{-t}(x_0-x_3).$$
解出
$$x_0'=\frac{e^{t}(x_0+x_3)+e^{-t}(x_0-x_3)}{2}=x_0\cosh t+x_3\sinh t,\qquad x_3'=x_0\sinh t+x_3\cosh t .$$
这是沿 $$x_3$$ 轴、快度 (rapidity) 为 $$t$$ 的 **Lorentz boost**：它与 $$x_1,x_2$$ 无关，把 $$(x_0,x_3)$$ 平面内的光锥 $$x_0=\pm x_3$$ 映到自身（$$x_0'-x_3'=e^{-t}(x_0-x_3)$$，$$x_0'+x_3'=e^{t}(x_0+x_3)$$，故零向量仍零）。

**再算 $$B_\theta$$**（它是酉矩阵）：
$$B_\theta XB_\theta^*=\begin{pmatrix}x_0+x_3&e^{i\theta}(x_1-ix_2)\\ e^{-i\theta}(x_1+ix_2)&x_0-x_3\end{pmatrix}.$$
读出：$$x_0,x_3$$ 不变，且
$$x_1'+ix_2'=e^{-i\theta}(x_1+ix_2).$$
这是绕 $$x_3$$ 轴转角 $$-\theta$$ 的**空间旋转**。等价地，$$\Phi(B_{-2\phi})$$ 是绕 $$x_3$$ 转 $$2\phi$$；注意 $$B_{\theta+2\pi}=-B_\theta$$，而 $$-B_\theta$$ 给出同一个 $$\Phi$$——这正是双重覆叠在显式公式里的样子。

**结论**：$$\mathrm{SU}(2)$$ 的那部分（$$B_\theta$$）给出旋转，正定 Hermite（实对角）的那部分（$$A_t$$）给出 boost。这是 Cartan 分解 $$\mathrm{SL}(2,\mathbb C)=\mathrm{SU}(2)\cdot\exp(\text{正的 Hermite 迹零})$$ 的物理面貌。

### 题 2：交比为实数 $$\iff$$ 四点共圆

**考点** 定理 3.3。**位置** 把「Möbius 变换保圆」这条几何事实升级成一个**判据**。

**问题** 用标准交比记号
$$(z_1,z_2;z_3,z_4)=\frac{(z_1-z_3)(z_2-z_4)}{(z_1-z_4)(z_2-z_3)}.$$
证明：$$z_1,z_2,z_3,z_4\in\widehat{\mathbb C}$$（互异）四点共圆或共线 $$\iff(z_1,z_2;z_3,z_4)\in\mathbb R$$。

**解** 把两边的定义直接代入比较：由定理 3.3(iii) 的记号 $$[z,z_1,z_2,z_3]=\dfrac{(z-z_1)(z_2-z_3)}{(z-z_3)(z_2-z_1)}$$，取 $$z=z_4$$、$$z_1\to z_1$$、$$z_2\to z_3$$、$$z_3\to z_2$$ 得
$$[z_4,z_1,z_3,z_2]=\frac{(z_4-z_1)(z_3-z_2)}{(z_4-z_2)(z_3-z_1)},$$
其倒数为 $$\dfrac{(z_4-z_2)(z_3-z_1)}{(z_4-z_1)(z_3-z_2)}$$。另一方面，标准交比的四个因子分别是 $$-(z_3-z_1)$$、$$-(z_4-z_2)$$、$$-(z_4-z_1)$$、$$-(z_3-z_2)$$（例如 $$z_1-z_3=-(z_3-z_1)$$），四个负号两两抵消，故
$$(z_1,z_2;z_3,z_4)=\frac{(z_3-z_1)(z_4-z_2)}{(z_4-z_1)(z_3-z_2)}=[z_4,z_1,z_3,z_2]^{-1}.$$
因此由定理 3.3(iii)，$$(z_1,z_2;z_3,z_4)$$ 在 Möbius 变换下也不变（「是否为实数」在取倒数下自反：$$w\ne0$$ 时 $$w\in\mathbb R\iff1/w\in\mathbb R$$）。

**化为特例** 取 Möbius 变换 $$g(z)=\dfrac{1}{z-z_3}$$，它把 $$z_3$$ 送到 $$\infty$$。记 $$w_i=g(z_i)$$。由于 Möbius 变换把「圆或直线」映成「圆或直线」，且把交比保持不变，
$$\text{四点共圆或共线}\iff w_1,w_2,w_4,\infty\ \text{共圆或共线}\iff w_1,w_2,w_4\ \text{共线}$$
（一个圆过 $$\infty$$ 当且仅当它是直线）。于是只需验证：
$$(w_1,w_2;\infty,w_4)\in\mathbb R\iff w_1,w_2,w_4\ \text{共线}.$$
计算这个交比：在公式中令 $$z_3=\infty$$，先把分子分母同除 $$z_3$$ 再取极限。分子含因子 $$(z_1-z_3)$$，分母含因子 $$(z_2-z_3)$$，两者之比 $$(z_1-z_3)/(z_2-z_3)\to1$$，故
$$(z_1,z_2;\infty,z_4)=\frac{z_2-z_4}{z_1-z_4}.$$
（这里用了 $$\lim_{z_3\to\infty}(z_1-z_3)/(z_2-z_3)=1$$。）于是要证：
$$\frac{w_2-w_4}{w_1-w_4}\in\mathbb R\iff w_1,w_2,w_4\ \text{共线}.$$

**这一步是纯复数的**：三个复数 $$w_1,w_2,w_4$$ 共线，等价于向量 $$w_2-w_4$$ 与 $$w_1-w_4$$ 平行，即一个是另一个的实数倍；因为 $$\mathbb C$$ 中「$$u/v\in\mathbb R$$」正是「$$u,v$$ 作为 $$\mathbb R^2$$ 中的向量平行」（$$u=\lambda v$$，$$\lambda=u/v$$）以及「$$u=0$$ 或 $$v=0$$」的边界情形（此时 $$\infty\in\mathbb R\cup\{\infty\}$$ 仍算「实」，与共线一致）。故
$$\frac{w_2-w_4}{w_1-w_4}\in\mathbb R\iff w_1,w_2,w_4\ \text{共线}.$$

**结论** 四步串起来即得所需判据。$$\blacksquare$$

**注（为什么这个判据好用）** 它把「共圆」这个二阶条件变成了「一个比是实数」这个可计算条件：不用解圆的方程，只要算一个复数是不是实的。它也是第五节题 4 里「$$\mathbb H$$ 的自同构」与「双曲等距」之间的那座桥——那里用到的全纯性判据与这里的实性判据是同一件事的两面。

### 题 3：Weyl 上循环不是上边界

**考点** 定理 3.10 与 3.11。**位置** 第 22 章的中心扩张在这里被放回射影表示的框架，并用一个「对称性」技巧一刀切开。

**问题** 设 $$\mathcal H=L^2(\mathbb R)$$，$$U(s),V(t)$$ 是满足 Weyl 关系
$$U(s)V(t)=e^{-i\hbar st}\,V(t)U(s)\qquad(\hbar\ne0)$$
的单参数酉群（第 22 章）。定义 $$\rho(s,t)=U(s)V(t)$$。证明：

(1) (30.1) 中的上循环是 $$c\bigl((s,t),(s',t')\bigr)=e^{i\hbar s't}$$，并验证它满足上循环条件 (30.2)；
(2) $$c$$ 不是上边界，因此相空间平移群的这个射影表示不可线性化。

**解** **(1)** 用 Weyl 关系把 $$V(t)$$ 搬到 $$U(s')$$ 的右边：
$$V(t)U(s')=e^{i\hbar s't}U(s')V(t)$$
（在 $$U(s')V(t)=e^{-i\hbar s't}V(t)U(s')$$ 两边左乘 $$V(t)^{-1}$$、右乘 $$U(s')^{-1}$$，或直接取逆并注意 $$e^{-i\hbar s't}$$ 的逆是 $$e^{i\hbar s't}$$）。于是
$$\rho(s,t)\rho(s',t')=U(s)V(t)U(s')V(t')=e^{i\hbar s't}\,U(s)U(s')V(t)V(t')=e^{i\hbar s't}\,\rho(s+s',t+t').$$
故 $$c\bigl((s,t),(s',t')\bigr)=e^{i\hbar s't}$$。

验证 (30.2)：记 $$g=(s,t)$$、$$h=(s',t')$$、$$k=(s'',t'')$$。
$$\text{左边}=e^{i\hbar s't}\cdot e^{i\hbar s''(t+t')},\qquad \text{右边}=e^{i\hbar(s'+s'')t}\cdot e^{i\hbar s''t'}.$$
左边指数为 $$i\hbar\bigl(s't+s''t+s''t'\bigr)$$，右边指数为 $$i\hbar\bigl(s't+s''t+s''t'\bigr)$$，相等。$$\square$$

**(2)** **关键 leap：上边界必对称。** 若 $$c$$ 是上边界，即存在 $$\beta:\mathbb R^2\to\mathbb C^*$$ 使
$$c(g,h)=\frac{\beta(g)\beta(h)}{\beta(g+h)},$$
则右边在交换 $$g,h$$ 后不变，故 $$c(g,h)=c(h,g)$$ 对一切 $$g,h$$ **必须**成立。但本题的 $$c$$ 不满足：取 $$g=(1,1)$$、$$h=(0,1)$$，
$$c(g,h)=e^{i\hbar\cdot0\cdot1}=1,\qquad c(h,g)=e^{i\hbar\cdot1\cdot1}=e^{i\hbar}\ne1\quad(\hbar\ne0).$$
故 $$c$$ 不对称，因而**不是**上边界。由定理 3.11，这个射影表示不能线性化。$$\blacksquare$$

**注（这说明什么）** 相空间平移群 $$\mathbb R^2$$ 是**交换**群，它的一切线性酉表示都可以在某个基下同时对角化（可交换的酉算子族同时对角化），本质上只是「一组相位」；而 Weyl 系统的 $$U(s),V(t)$$ 明显不能同时对角化（它们不对易）。所以此处「不可线性化」有物理内容：**对易关系 $$[X,P]=i\hbar$$ 与「射影表示的不可线性化」是同一件事**。第 22 章用 Stone–von Neumann 定理说了这句话的另一半：换到中心扩张 $$H_3(\mathbb R)$$ 上，不可线性化消失了，取而代之是不可约表示的**唯一性**。

### 题 4：实版本——$$\mathrm{PSL}(2,\mathbb R)\cong\mathrm{SO}^+(1,2)$$ 与双曲几何

**考点** 定理 3.6 的机制（而非它的结论）。**位置** 说明「复数是特殊情形」，同一台机器在实数上换个输入就给出双曲几何。

**问题** 对 $$x=(x_0,x_1,x_2)\in\mathbb R^3$$ 记实对称矩阵
$$X(x)=\begin{pmatrix}x_0+x_2&x_1\\ x_1&x_0-x_2\end{pmatrix}.$$
(i) 验证 $$\det X(x)=x_0^2-x_1^2-x_2^2$$。
(ii) 证明对 $$A\in\mathrm{SL}(2,\mathbb R)$$，$$X\mapsto AXA^{\mathsf T}$$ 给出同态 $$\Psi:\mathrm{SL}(2,\mathbb R)\to\mathrm{SO}^+(1,2)$$，核为 $$\{\pm I\}$$，像为 $$\mathrm{SO}^+(1,2)$$。
(iii) 解释这与「上半平面上的双曲几何」的关系。

**解** **(i)** $$\det\begin{pmatrix}x_0+x_2&x_1\\ x_1&x_0-x_2\end{pmatrix}=(x_0+x_2)(x_0-x_2)-x_1^2=x_0^2-x_1^2-x_2^2$$。$$\square$$

**(ii)** 保 $$\det$$：$$\det(AXA^{\mathsf T})=(\det A)^2\det X=\det X$$。$$AXA^{\mathsf T}$$ 实对称。故 $$\Psi(A)\in O(1,2)$$。

**保时间方向**：$$X$$ 正定 $$\iff$$ $$x_0>\sqrt{x_1^2+x_2^2}$$ $$\iff$$ 「$$\langle x,x\rangle_{1,2}>0$$ 且 $$x_0>0$$」（对 $$2\times2$$ 实对称阵，正定 $$\iff$$ 迹 $$=2x_0>0$$ 且 $$\det=x_0^2-x_1^2-x_2^2>0$$，由 Silvester 判据）。$$A$$ 可逆时 $$X$$ 正定 $$\iff$$ $$AXA^{\mathsf T}$$ 正定（对任意 $$0\ne v$$，$$v^{\mathsf T}AXA^{\mathsf T}v=(A^{\mathsf T}v)^{\mathsf T}X(A^{\mathsf T}v)>0$$，反之亦然）。故 $$\Psi(A)$$ 保前向开锥，属于 $$O(1,2)$$ 的保时间那一支。

**连通性**：$$\mathrm{SL}(2,\mathbb R)$$ 连通——用与 3.4 节相同的 QR 分解（实 Gram–Schmidt），每个 $$A\in\mathrm{SL}(2,\mathbb R)$$ 写成 $$A=Q R$$（$$Q\in\mathrm{SO}(2)$$、$$R=\begin{pmatrix}t&s\\ 0&t^{-1}\end{pmatrix}$$，$$t>0$$），再令 $$t$$ 连续变到 $$1$$ 即把 $$A$$ 连续收缩到 $$Q$$。故 $$\Psi(\mathrm{SL}(2,\mathbb R))$$ 连通且落在 $$O^+(1,2)$$ 的保锥支内。

**像的维数** $$\dim\mathrm{SL}(2,\mathbb R)=3=\dim\mathrm{SO}(1,2)$$，与定理 3.6(iii) 同样的论证（核离散 $$\Rightarrow$$ 切映射单射 $$\Rightarrow$$ 单位邻域落在像里 $$\Rightarrow$$ 开子群 = 全群）给出 $$\Psi(\mathrm{SL}(2,\mathbb R))=\mathrm{SO}^+(1,2)$$。

**核**：与定理 3.6(ii) 同样的论证：$$AXA^{\mathsf T}=X$$ 对一切对称 $$X$$，取秩一 $$vv^{\mathsf T}$$ 得 $$Av$$ 与 $$v$$ 共线对一切 $$v$$，故 $$A=\lambda I$$；$$\det A=\lambda^2=1$$ 给出 $$\lambda=\pm1$$。$$\square$$

**(iii)** 两边取商：$$\mathrm{PSL}(2,\mathbb R)\cong\mathrm{SO}^+(1,2)$$。

$$\mathrm{PSL}(2,\mathbb R)$$ 作用在上半平面 $$\mathbb H=\{z:\operatorname{Im}z>0\}$$ 上：对 $$A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$$、$$\det A=1$$，直接验证
$$\operatorname{Im}\frac{az+b}{cz+d}=\frac{\operatorname{Im}z}{\lvert cz+d\rvert^2}>0 ,$$
故 $$\mathbb H$$ 被映到自身。（$$\pm A$$ 给出同一个变换，故这是 $$\mathrm{PSL}$$ 的作用。）这个作用给出 $$\mathbb H$$ 的**全纯自同构群** $$\mathrm{Aut}(\mathbb H)\cong\mathrm{PSL}(2,\mathbb R)$$。

而 $$\mathbb H$$ 上带 Poincaré 度量 $$ds^2=\dfrac{dx^2+dy^2}{y^2}$$ 后是双曲平面（常曲率 $$-1$$）；$$\mathrm{PSL}(2,\mathbb R)$$ 保持此度量，是它的**保向等距群**。于是
$$\text{双曲平面的保向等距群}\cong\mathrm{PSL}(2,\mathbb R)\cong\mathrm{SO}^+(1,2),$$
这正是 (ii) 的几何意义，也是 Klein 的 Erlangen 纲领在二维双曲几何里的标准兑现。$$\blacksquare$$

**注** 实版本与复版本的差别只在「$$\mathbb R^*$$ 中不必有平方根」：$$\mathrm{SL}(2,\mathbb R)/\{\pm I\}=\mathrm{PSL}(2,\mathbb R)$$ 是 $$\mathrm{PGL}(2,\mathbb R)$$ 的指数 2 子群，故实版本里的「$$\pm A$$ 同类」要额外承认行列式的符号（见注 3.2）。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 取 $$A=\begin{pmatrix}1&1\\ 0&1\end{pmatrix}$$、$$B=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$$。写出 $$f_A$$、$$f_B$$ 的显式分式形式，算出 $$f_A\circ f_B$$ 与 $$f_B\circ f_A$$，并各写成一个 $$f_C$$ 的形式（给出 $$C$$ 与 $$\det C$$）。再写出 $$f_A^{-1}$$。

**基2.** 先用定理 3.3(i) 的判据判断 $$f(z)=\dfrac1z$$ 把直线 $$\operatorname{Re}z=1$$ 映成圆还是直线（不要先算具体式子），再直接算出它的圆心与半径。

**基3.** 对 $$A=\begin{pmatrix}1&1\\ 0&1\end{pmatrix}\in\mathrm{SL}(2,\mathbb C)$$，算出 $$A\,X(x)\,A^*$$ 并读出对应的四维实线性变换 $$x\mapsto x'$$，写成 $$4\times4$$ 实矩阵。验证这个矩阵的行列式为 $$1$$，并用两组具体向量验证它保持 $$\langle\cdot,\cdot\rangle_{1,3}$$。

**基4.** 设 $$\beta:G\to\mathbb C^*$$ 是任意函数，令 $$c(g,h)=\dfrac{\beta(g)\beta(h)}{\beta(gh)}$$。直接验证 $$c$$ 满足上循环条件 (30.2)，并说明为什么由定理 3.11 立即知道「这个上循环对应的射影表示可线性化」。

### 竞赛（本课目标难度）

**竞1.** 证明不存在连续映射 $$s:\mathrm{SO}(3)\to\mathrm{SU}(2)$$ 使 $$\rho\circ s=\operatorname{id}_{\mathrm{SO}(3)}$$（$$\rho$$ 是第 26 章的双重覆叠）。并说明这个结论与定理 3.12(ii) 的关系。

**竞2.** 用「$$\mathrm{SO}(3)$$ 的不可约复表示维数全为奇数」这一事实，直接证明定理 3.12(ii)：不存在线性表示 $$\tilde\rho:\mathrm{SO}(3)\to\mathrm{GL}(2,\mathbb C)$$ 使 $$[\tilde\rho(R)]=\alpha(R)$$ 对一切 $$R$$ 成立。

**竞3.** 证明循环群 $$\mathbb Z/n$$ 的一切射影表示都可线性化。（提示：设 $$A\in\mathrm{GL}(V)$$ 是 $$\alpha(1)$$ 的任一提升，考察 $$A^n$$。）

**竞4.** 不用定理 3.3(ii) 的三点传递性，直接用代入法证明交比不变性：设 $$f(z)=\dfrac{az+b}{cz+d}$$、$$ad-bc=1$$，证明
$$[f(z),f(z_1),f(z_2),f(z_3)]=[z,z_1,z_2,z_3],$$
其中 $$[w,w_1,w_2,w_3]=\dfrac{(w-w_1)(w_2-w_3)}{(w-w_3)(w_2-w_1)}$$。

**竞5.** 证明 $$\mathrm{PGL}(2,\mathbb R)\big/\mathrm{PSL}(2,\mathbb R)\cong\mathbb Z/2$$，并给出一个**实系数** Möbius 变换作为 $$\mathrm{PSL}(2,\mathbb R)$$ 之外的元素的具体例子；验证它把上半平面 $$\mathbb H$$ 映到下半平面。再说明为什么在 $$\mathbb C$$ 上不存在对应的现象。

### 研究（通向下一章）

**研1.** 设 $$\tilde G$$ 是 $$G$$ 的中心扩张：$$1\to A\xrightarrow{i}\tilde G\xrightarrow{\pi}G\to1$$，$$A\subseteq Z(\tilde G)$$。设 $$\tilde\rho:\tilde G\to\mathrm{GL}(V)$$ 是线性表示，且 $$\tilde\rho(i(a))$$ 对一切 $$a\in A$$ 是标量。

(i) 证明存在唯一射影表示 $$\alpha:G\to\mathrm{PGL}(V)$$ 使 $$\alpha(\pi(\tilde g))=[\tilde\rho(\tilde g)]$$ 对一切 $$\tilde g\in\tilde G$$ 成立。
(ii) 取 $$G=\mathrm{SO}(3)$$、$$\tilde G=\mathrm{SU}(2)$$、$$A=\{\pm I\}$$，把 (i) 与定理 3.13 合起来，说明「$$\mathrm{SO}(3)$$ 的射影表示」与「$$\mathrm{SU}(2)$$ 的、在 $$-I$$ 上作用为标量的线性表示」之间的关系，并解释整数自旋与半整数自旋分别落在哪一边。

**研2.** 设 $$1\to\mathbb C^*\xrightarrow{i}\tilde G\xrightarrow{\pi}G\to1$$ 与 $$1\to\mathbb C^*\xrightarrow{i'}\tilde G'\xrightarrow{\pi'}G\to1$$ 是两个 $$\mathbb C^*$$ 中心扩张。取截面 $$s:G\to\tilde G$$、$$s':G\to\tilde G'$$（只作为映射），记相应的上循环为 $$c$$、$$c'$$。证明：存在使两个扩张交换的同构 $$\theta:\tilde G\to\tilde G'$$（即 $$\pi'\circ\theta=\pi$$ 且 $$\theta\circ i=i'$$）当且仅当 $$c$$ 与 $$c'$$ 上同调。由此说明「$$G$$ 的 $$\mathbb C^*$$ 中心扩张的同构类」被 $$H^2(G;\mathbb C^*)$$ 的元素一一标记。

### 解答 (Solutions)

**解 基1.** $$f_A(z)=\dfrac{1\cdot z+1}{0\cdot z+1}=z+1$$，$$f_B(z)=\dfrac{0\cdot z+(-1)}{1\cdot z+0}=-\dfrac1z$$。

**复合** 由定理 3.2(i)，$$f_A\circ f_B=f_{AB}$$。计算
$$AB=\begin{pmatrix}1&1\\ 0&1\end{pmatrix}\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}=\begin{pmatrix}0+1&-1+0\\ 0+1&0+0\end{pmatrix}=\begin{pmatrix}1&-1\\ 1&0\end{pmatrix},\qquad\det(AB)=1\cdot0-(-1)\cdot1=1 .$$
故 $$f_A\circ f_B=f_{AB}(z)=\dfrac{z-1}{z}=1-\dfrac1z$$。直接验算：$$f_A\bigl(f_B(z)\bigr)=-\dfrac1z+1$$，一致。

同理
$$BA=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}\begin{pmatrix}1&1\\ 0&1\end{pmatrix}=\begin{pmatrix}0&-1\\ 1&1\end{pmatrix},\qquad\det(BA)=0\cdot1-(-1)\cdot1=1,$$
故 $$f_B\circ f_A=f_{BA}(z)=\dfrac{-1}{z+1}$$。直接验算：$$f_B\bigl(f_A(z)\bigr)=-\dfrac{1}{z+1}$$，一致。

两者不同（例如在 $$z=1$$ 处：前者 $$=0$$，后者 $$=-1/2$$），说明 Möbius 群非交换。

**逆** $$A^{-1}=\begin{pmatrix}1&-1\\ 0&1\end{pmatrix}$$，故 $$f_A^{-1}(z)=z-1$$。直接验算：$$f_A^{-1}\bigl(f_A(z)\bigr)=(z+1)-1=z$$。$$\blacksquare$$

**解 基2.** 直线 $$\operatorname{Re}z=1$$ 的方程是 $$z+\bar z-2=0$$，即
$$Az\bar z+\bar Bz+B\bar z+C=0,\qquad A=0,\ B=1,\ C=-2 .$$
（这是定理 3.3(i) 证明中的标准形状，$$A=0$$、$$B\ne0$$ 表示直线；此时 $$\det H=AC-\lvert B\rvert^2=0-1=-1<0$$。）

**用定理 3.3(i) 的判据定位形状。** $$f(z)=1/z$$ 对应矩阵 $$\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$$，即 $$a=0$$、$$b=1$$、$$c=1$$、$$d=0$$。按定理 3.3(i) 证明里的做法，把 $$z=\dfrac{b-dw}{cw-a}=\dfrac1w$$ 代入并整式乘以 $$\lvert cw-a\rvert^2=\lvert w\rvert^2$$：
$$\lvert w\rvert^2\Bigl(0\cdot z\bar z+\bar 1\cdot z+1\cdot\bar z+(-2)\Bigr)\Big\vert_{z=1/w}=w\bar w\Bigl(\frac1w+\frac1{\bar w}-2\Bigr)=\bar w+w-2w\bar w .$$
故像的方程是
$$-2w\bar w+w+\bar w=0\quad\Longleftrightarrow\quad2\lvert w\rvert^2-w-\bar w=0 .$$
对照 $$A'w\bar w+\bar B'w+B'\bar w+C'=0$$，得 $$A'=-2\ne0$$，故像**是圆**（不是直线）；$$B'=\tfrac12$$、$$C'=0$$。验证判别式：$$\det H'=A'C'-\lvert B'\rvert^2=0-\tfrac14<0$$ ✓，与「$$\det H'=\lvert\det M\rvert^2\det H$$（$$\det M=-1$$）」一致。

**直接算，写出圆心与半径。** 令 $$z=1+iy$$（$$y\in\mathbb R$$），
$$w=\frac1{1+iy}=\frac{1-iy}{1+y^2},\qquad u=\operatorname{Re}w=\frac1{1+y^2},\qquad v=\operatorname{Im}w=\frac{-y}{1+y^2}.$$
于是 $$u^2+v^2=\dfrac{1+y^2}{(1+y^2)^2}=\dfrac1{1+y^2}=u$$，即
$$u^2-u+v^2=0\quad\Longleftrightarrow\quad\Bigl(u-\tfrac12\Bigr)^2+v^2=\tfrac14 .$$
两条路线一致：这是一条**圆**，圆心 $$\tfrac12$$、半径 $$\tfrac12$$。（它过原点，也过 $$z=1$$ 的像 $$w=1$$；直线上的 $$\infty$$ 被送到 $$w=0$$，落在圆周上。）$$\blacksquare$$

**解 基3.** 记 $$A^*=\begin{pmatrix}1&0\\ 1&1\end{pmatrix}$$。先算
$$AX=\begin{pmatrix}1&1\\ 0&1\end{pmatrix}\begin{pmatrix}x_0+x_3&x_1-ix_2\\ x_1+ix_2&x_0-x_3\end{pmatrix}=\begin{pmatrix}x_0+x_3+x_1+ix_2&x_1-ix_2+x_0-x_3\\ x_1+ix_2&x_0-x_3\end{pmatrix}.$$
再右乘 $$A^*$$：右乘把第 $$j$$ 列乘 $$\overline{A_{j1}},\overline{A_{j2}}$$ 相加，即新第 1 列 = 旧第 1 列 + 旧第 2 列，新第 2 列 = 旧第 2 列。于是
$$AXA^*=\begin{pmatrix}(x_0+x_3+x_1+ix_2)+(x_0-x_3+x_1-ix_2)&x_0-x_3+x_1-ix_2\\ (x_1+ix_2)+(x_0-x_3)&x_0-x_3\end{pmatrix}=\begin{pmatrix}2x_0+2x_1&x_0+x_1-x_3-ix_2\\ x_0-x_3+x_1+ix_2&x_0-x_3\end{pmatrix}.$$
按定义 3.4 读出：
$$x_0'+x_3'=2x_0+2x_1,\qquad x_0'-x_3'=x_0-x_3,\qquad x_1'-ix_2'=x_0+x_1-x_3-ix_2 .$$
解出
$$x_0'=\frac{3x_0+2x_1-x_3}{2},\qquad x_1'=x_0+x_1-x_3,\qquad x_2'=x_2,\qquad x_3'=\frac{x_0+2x_1+x_3}{2}.$$
故
$$M=\begin{pmatrix}\tfrac32&1&0&-\tfrac12\\ 1&1&0&-1\\ 0&0&1&0\\ \tfrac12&1&0&\tfrac12\end{pmatrix}.$$

**行列式** $$M$$ 关于 $$x_2$$ 那一行/列与其他部分解耦（第 3 行只有对角元 $$1$$、第 3 列非对角元全为 $$0$$），故 $$\det M$$ 等于子式
$$\det\begin{pmatrix}\tfrac32&1&-\tfrac12\\ 1&1&-1\\ \tfrac12&1&\tfrac12\end{pmatrix}=\frac32\Bigl(\frac12+1\Bigr)-1\Bigl(\frac12+\frac12\Bigr)-\frac12\Bigl(1-\frac12\Bigr)=\frac94-1-\frac14=1 .$$
所以 $$\det M=1$$。

**保型检验** 取 $$x=(1,0,0,0)$$（$$\langle x,x\rangle_{1,3}=1$$）：得 $$x'=(3/2,\ 1,\ 0,\ 1/2)$$，$$\langle x',x'\rangle_{1,3}=\tfrac94-1-\tfrac14=1$$ ✓。
取 $$x=(0,0,0,1)$$（$$\langle x,x\rangle_{1,3}=-1$$）：得 $$x'=(-1/2,\ -1,\ 0,\ 1/2)$$，$$\langle x',x'\rangle_{1,3}=\tfrac14-1-\tfrac14=-1$$ ✓。
再取类时前向的 $$x=(1,0,0,0)$$，像的时间分量 $$3/2>0$$，前向性保持 ✓。$$\blacksquare$$

**解 基4.** 记 $$c(g,h)=\beta(g)\beta(h)/\beta(gh)$$。左边
$$c(g,h)c(gh,k)=\frac{\beta(g)\beta(h)}{\beta(gh)}\cdot\frac{\beta(gh)\beta(k)}{\beta(ghk)}=\frac{\beta(g)\beta(h)\beta(k)}{\beta(ghk)},$$
右边
$$c(g,hk)c(h,k)=\frac{\beta(g)\beta(hk)}{\beta(ghk)}\cdot\frac{\beta(h)\beta(k)}{\beta(hk)}=\frac{\beta(g)\beta(h)\beta(k)}{\beta(ghk)} .$$
两者相等，故 (30.2) 成立。

**由定理 3.11 立即可线性化**：定理 3.11 的 (⇐) 方向说的是「上循环 $$c$$ 若是上边界，则 $$\tilde\rho(g)=\beta(g)^{-1}\rho(g)$$ 是线性表示，且 $${[\tilde\rho(g)]=\alpha(g)}$$」。而上边界正是形如 $$\beta(g)\beta(h)/\beta(gh)$$ 的上循环——本题的 $$c$$ 就是这个形状，它的「$$\beta$$」就是给定的那个 $$\beta$$。所以 $$\tilde\rho(g)=\beta(g)^{-1}\rho(g)$$ 直接给出线性提升。$$\blacksquare$$

**解 竞1.** **关键 leap：把「截面存在」变成「覆叠平凡」，再用连通性否定它。**

反设存在连续 $$s:\mathrm{SO}(3)\to\mathrm{SU}(2)$$ 使 $$\rho\circ s=\operatorname{id}$$。

**第一步：$$s$$ 是单射。** 若 $$s(R)=s(S)$$，两边作用 $$\rho$$ 得 $$R=\rho(s(R))=\rho(s(S))=S$$。

**第二步：$$\mathrm{SU}(2)\cong\mathrm{SO}(3)\times\{\pm1\}$$（作为拓扑空间）。** 定义
$$\Theta:\mathrm{SO}(3)\times\{\pm1\}\to\mathrm{SU}(2),\qquad \Theta(R,\varepsilon)=\varepsilon\,s(R).$$
$$\Theta$$ 连续。单射：若 $$\varepsilon s(R)=\varepsilon' s(R')$$，则作用 $$\rho$$ 得 $$R=R'$$（因 $$\rho(\varepsilon s(R))=\rho(s(R))=R$$），再由 $$\varepsilon s(R)=\varepsilon' s(R)$$ 且 $$s(R)\ne0$$ 得 $$\varepsilon=\varepsilon'$$。满射：任取 $$q\in\mathrm{SU}(2)$$，令 $$R=\rho(q)$$；则 $$\rho(s(R))=R=\rho(q)$$，故 $$s(R)=\pm q$$，即 $$q=\pm s(R)=\Theta(R,\pm1)$$。连续双射，且两边的紧 Hausdorff 空间，故 $$\Theta$$ 是同胚。

**第三步：矛盾。** $$\mathrm{SO}(3)\times\{\pm1\}$$ 不连通（$$\{\pm1\}$$ 离散、$$\mathrm{SO}(3)$$ 非空，两个 «切片» 都非空且开）。而 $$\mathrm{SU}(2)\cong S^3$$（第 26 章）连通。同胚保持连通性，矛盾。

**与定理 3.12(ii) 的关系**：由定理 3.11，「$$\alpha$$ 可线性化」等价于「中心扩张 $$\widetilde{\mathrm{SO}(3)}_\alpha$$ 有同态截面」。对自旋射影表示，可以验证（见下）$$\widetilde{\mathrm{SO}(3)}_\alpha\cong\{(R,\lambda q):\lambda\in\mathbb C^*,\ \rho(q)=R\}$$，而其中的子集 $$\{\lambda=1\}\cong\mathrm{SU}(2)$$ 就是 $$\rho$$ 的图；于是「有同态截面」至少要能造出连续截面 $$s$$。本题证明了后者不存在，故定理 3.12(ii) 的结论成立。（也可以直接说：定理 3.12(ii) 的证明与本题证明共用同一件事实——$$\mathrm{SU}(2)$$ 连通而 $$\mathrm{SO}(3)\times\{\pm1\}$$ 不连通，只是分别以「同态截面」和「连续截面」的形式出现。）

**直接验证 $$\widetilde{\mathrm{SO}(3)}_\alpha$$ 的形状**：$$\alpha(R)=[q_R]$$ 对任一 $$q_R\in\rho^{-1}(R)$$。元素 $$(R,A)\in\widetilde{\mathrm{SO}(3)}_\alpha$$ 满足 $$[A]=[q_R]$$，即 $$A=\lambda q_R$$（$$\lambda\in\mathbb C^*$$）。反之每个 $$\lambda q_R$$ 都在其中。故 $$\widetilde{\mathrm{SO}(3)}_\alpha=\{(R,\lambda q_R)\}$$。是的，与上面所说一致。$$\blacksquare$$

**解 竞2.** **关键 leap：用维数奇偶性把 2 维情形逼成「两个平凡表示的直和」。**

由第 26 章与第 28 章，$$\mathrm{SO}(3)$$ 的不可约复表示是 $$V_j$$（$$j\in\mathbb Z_{\ge0}$$），维数 $$2j+1$$（定理 3.13(iii)：$$-I$$ 作用平凡者恰为整数 $$j$$）。

**第一步：$$\mathrm{SO}(3)$$ 完全可约。** $$\mathrm{SO}(3)$$ 紧，用 Haar 测度平均任意内积可得不变内积（第 28 章/第 20 章的紧群完全可约性），故每个有限维表示都是不可约表示的直和。

**第二步：2 维表示只能是两个 1 维表示的直和。** 若 $$\tilde\rho$$ 是 2 维表示，分解为不可约表示，维数全为奇数（$$1,3,5,\dots$$），和为 $$2$$ 迫使只有 $$1+1$$ 一种可能。

**第三步：1 维表示只有平凡。** 1 维表示是群同态 $$\mathrm{SO}(3)\to\mathbb C^*$$，其像交换。而 $$\mathrm{SO}(3)$$ 是它自己 Lie 代数的换位子群（$$\mathfrak{so}(3)$$ 是单 Lie 代数，$$[\mathfrak{so}(3),\mathfrak{so}(3)]=\mathfrak{so}(3)\ne0$$，由第 27 章连通 Lie 群的换位子群等于换位子子代数的指数像），于是同态把换位子送到换位子：像落在 $$\mathbb C^*$$ 的换位子群 $$\{1\}$$ 中。故 1 维表示平凡。

**第四步：结论。** 因此 $$\tilde\rho$$ 必是「$$2$$ 份平凡表示」的直和，即 $$\tilde\rho(R)=I$$ 对一切 $$R$$。但若 $$[\tilde\rho(R)]=\alpha(R)$$ 对一切 $$R$$，取 $$q=\begin{pmatrix}i&0\\ 0&-i\end{pmatrix}\in\mathrm{SU}(2)$$（$$q=\cos\tfrac\pi2+k\sin\tfrac\pi2$$，故由第 26 章的公式 $$\rho(q)$$ 是绕 $$k$$ 轴转 $$\pi$$ 的旋转），令 $$R=\rho(q)$$：则 $$\alpha(R)=[q]$$，而 $$q$$ 不是标量矩阵（$$q\ne\lambda I$$ 对一切 $$\lambda$$），故 $$[q]\ne[I]$$。与 $$\tilde\rho(R)=I$$ 矛盾。故这样的线性表示不存在，定理 3.12(ii) 成立。$$\blacksquare$$

**解 竞3.** **关键 leap：$$A^n$$ 必是标量，而标量可以被 $$n$$ 次方根「调平」。**

设 $$\alpha:\mathbb Z/n\to\mathrm{PGL}(V)$$ 是射影表示。取 $$A\in\mathrm{GL}(V)$$ 使 $$[A]=\alpha(1)$$（任意取一个提升）。

**第一步：$$A^n$$ 是标量。** 由 $$\alpha$$ 是同态，
$$[A^n]=[A]^n=\alpha(1)^n=\alpha(n\cdot1)=\alpha(0)=[I],$$
故 $$A^n=\mu I$$ 对某个 $$\mu\in\mathbb C^*$$。

**第二步：调平。** 取 $$\nu\in\mathbb C^*$$ 使 $$\nu^n=1/\mu$$。这样的 $$\nu$$ 存在：写 $$\mu=re^{i\theta}$$（$$r>0$$），取 $$\nu=r^{-1/n}e^{-i\theta/n}$$ 即可。令 $$B=\nu A$$。则
$$B^n=\nu^nA^n=\frac1\mu\cdot\mu I=I,$$
且 $$[B]=[\nu A]=[A]=\alpha(1)$$。

**第三步：造线性表示。** 定义 $$\tilde\rho(k)=B^k$$（$$k\in\mathbb Z/n$$，良定义因为 $$B^n=I$$）。则 $$\tilde\rho$$ 是同态（$$B^{k+l}=B^kB^l$$），且 $$[\tilde\rho(k)]=[B]^k=[A]^k=\alpha(k)$$。故 $$\alpha$$ 可线性化。

（附注：对 $$\mathbb Z$$ 这件事更平凡——任何 $$A\in\mathrm{GL}(V)$$ 都给出同态 $$k\mapsto A^k$$，无需调平。）$$\blacksquare$$

**解 竞4.** 先算一个基本差：
$$w-w_i=\frac{az+b}{cz+d}-\frac{az_i+b}{cz_i+d}=\frac{(az+b)(cz_i+d)-(az_i+b)(cz+d)}{(cz+d)(cz_i+d)} .$$
分子展开：
$$(az+b)(cz_i+d)-(az_i+b)(cz+d)=acz_iz+adz+bcz_i+bd-aczz_i-adz_i-bcz-bd$$
$$=ad(z-z_i)+bc(z_i-z)=(ad-bc)(z-z_i)=(z-z_i),$$
（用了 $$ad-bc=1$$）。故
$$w-w_i=\frac{z-z_i}{(cz+d)(cz_i+d)} . \tag{30.5}$$

代入交比。分子
$$(w-w_1)(w_2-w_3)=\frac{(z-z_1)(z_2-z_3)}{(cz+d)(cz_1+d)(cz_2+d)(cz_3+d)},$$
分母
$$(w-w_3)(w_2-w_1)=\frac{(z-z_3)(z_2-z_1)}{(cz+d)(cz_3+d)(cz_2+d)(cz_1+d)} .$$
两者的分母完全相同（都是四个因子的乘积，只是次序不同），相除时整个约去：
$$\frac{(w-w_1)(w_2-w_3)}{(w-w_3)(w_2-w_1)}=\frac{(z-z_1)(z_2-z_3)}{(z-z_3)(z_2-z_1)},$$
即 $$[f(z),f(z_1),f(z_2),f(z_3)]=[z,z_1,z_2,z_3]$$。

**这题的关键 leap**：不是去比较交比的四个因子各自怎么变（那样会陷入六个因子的记账），而是发现 (30.5) 里每个差式都带着**同一个**「尾巴」$$(cz+d)$$（在分母里，$$z$$ 与 $$z_i$$ 各出一个），四个因子在分子分母中恰好成对抵消。**先算差，再算比**——这是所有「共形不变量的验证」的通用套路。$$\blacksquare$$

**解 竞5.** **第一步：算商。** 商映射 $$\mathrm{GL}(2,\mathbb R)\to\mathrm{PGL}(2,\mathbb R)$$ 的核是 $$\mathbb R^*I$$。在 $$\mathrm{PGL}(2,\mathbb R)$$ 中，$$\mathrm{PSL}(2,\mathbb R)$$ 是 $$\mathrm{SL}(2,\mathbb R)$$ 的像。由第一同构定理
$$\mathrm{PGL}(2,\mathbb R)\big/\mathrm{PSL}(2,\mathbb R)\cong\mathrm{GL}(2,\mathbb R)\big/\bigl(\mathbb R^*I\cdot\mathrm{SL}(2,\mathbb R)\bigr).$$
而 $$\mathbb R^*I\cdot\mathrm{SL}(2,\mathbb R)=\{A\in\mathrm{GL}(2,\mathbb R):\det A>0\}$$：包含 $$\supseteq$$ 显然（$$\mathrm{SL}$$ 的行列式为 1，$$\lambda I$$ 的行列式为 $$\lambda^2>0$$），包含 $$\subseteq$$ 因为给定 $$\det A=\Delta>0$$，取 $$\lambda=\sqrt\Delta$$，则 $$\lambda^{-1}A\in\mathrm{SL}$$，$$A=\lambda\cdot(\lambda^{-1}A)\in\mathbb R^*I\cdot\mathrm{SL}$$。故
$$\mathrm{PGL}(2,\mathbb R)\big/\mathrm{PSL}(2,\mathbb R)\cong\mathrm{GL}(2,\mathbb R)\big/\{A:\det A>0\}\cong\mathbb R^*/\mathbb R_{>0}\cong\{\pm1\}\cong\mathbb Z/2 .$$

**第二步：具体例子。** 取 $$\tilde A=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$$（$$\det\tilde A=-1$$），对应的变换是
$$g(z)=\frac{1}{z}.$$
它不在 $$\mathrm{PSL}(2,\mathbb R)$$ 中：若 $$g=f_C$$、$$C\in\mathrm{SL}(2,\mathbb R)$$，则 $$C=\mu\tilde A$$ 必须成立（定理 3.2(ii) 的「差一个标量」，且 $$C=\mu\tilde A$$ 给出 $$f_C=f_{\tilde A}=g$$）。但 $$\det C=\mu^2\det\tilde A=-\mu^2=1$$ 要求 $$\mu^2=-1$$，即 $$\mu=\pm i\notin\mathbb R$$，与 $$C$$ 实系数矛盾。

**第三步：它与上半平面。** 令 $$z=x+iy$$，$$y>0$$。则
$$\frac1z=\frac{\bar z}{z\bar z}=\frac{x-iy}{x^2+y^2},\qquad \operatorname{Im}\frac1z=\frac{-y}{x^2+y^2}<0 .$$
故 $$g$$ 把 $$\mathbb H$$ 映到下半平面 $$\operatorname{Im}z<0$$。也就是说它**不是** $$\mathbb H$$ 的自同构，而是一个「反等距」（与复共轭复合后才是等距）；这与它不在保向等距群 $$\mathrm{PSL}(2,\mathbb R)$$ 中一致（第五节题 4(iii)）。

**第四步：$$\mathbb C$$ 上为什么没有这个现象。** 在 $$\mathbb C$$ 上，$$\mathrm{PSL}\cong\mathrm{PGL}$$ 的证明归结为「$$\mathbb C^*$$ 中每个元素都有平方根」（定理 3.2(iii)）：给定 $$\det A=\Delta$$，取 $$\lambda=\sqrt\Delta\in\mathbb C^*$$ 即可把 $$A$$ 调成行列式 $$1$$。而 $$\mathbb R^*$$ 中负数**没有**实平方根，这正是 $$\det\tilde A=-1$$ 的情形（见注 3.2）。$$\blacksquare$$

**解 研1.**

**(i) 存在性与唯一性。** 先证一个有用的观察：若 $$\pi(\tilde g)=\pi(\tilde h)$$，则 $$\tilde h=\tilde g\,i(a)$$ 对某个 $$a\in A$$（因为 $$\pi(\tilde g^{-1}\tilde h)=e$$，故 $$\tilde g^{-1}\tilde h\in\ker\pi=i(A)$$）——同理 $$\tilde h=i(a')\tilde g$$，两者一致因为 $$A$$ 中心。于是
$$\tilde\rho(\tilde h)=\tilde\rho(\tilde g)\tilde\rho(i(a))=\tilde\rho(\tilde g)\chi(a),$$
其中 $$\chi(a)I:=\tilde\rho(i(a))$$ 是标量（题设）。故 $$[\tilde\rho(\tilde h)]=[\tilde\rho(\tilde g)]$$：**类的取值只依赖 $$\pi(\tilde g)$$**。于是
$$\alpha(g):=[\tilde\rho(\tilde g)],\qquad \tilde g\in\pi^{-1}(g)\ \text{任取}$$
是良定义的。

**是同态**：取 $$\tilde g\in\pi^{-1}(g)$$、$$\tilde h\in\pi^{-1}(h)$$，则 $$\pi(\tilde g\tilde h)=gh$$，故
$$\alpha(g)\alpha(h)=[\tilde\rho(\tilde g)][\tilde\rho(\tilde h)]=[\tilde\rho(\tilde g\tilde h)]=\alpha(gh).$$
唯一性：$$\alpha$$ 在每个 $$g$$ 上的值被上式唯一确定（$$\pi$$ 满射）。

**(ii)** 取 $$A=\{\pm I\}$$、$$\chi$$ 为 $$A$$ 上的特征。$$A\cong\mathbb Z/2$$ 只有两个特征：平凡特征 $$\chi_0(i(-1))=1$$ 与符号特征 $$\chi_1(i(-1))=-1$$。

- **$$\chi_1$$ 这边**：$$\mathrm{SU}(2)$$ 的不可约表示 $$V_j$$，其中 $$\tilde\rho(-I)$$ 是标量 $$(-1)^{2j}$$（定理 3.13(ii)）。$$\tilde\rho(-I)=-I$$（即 $$\chi=\chi_1$$）当且仅当 $$2j$$ 是奇数，即 $$j\in\tfrac12+\mathbb Z_{\ge0}$$。由 (i)，每个这样的 $$\tilde\rho$$ 压成 $$\mathrm{SO}(3)$$ 的一个射影表示。特别地 $$j=\tfrac12$$ 压成自旋射影表示 $$\alpha$$。所以**半整数自旋落在 $$\chi_1$$ 这一边**：它们的线性表示只存在于覆盖群 $$\mathrm{SU}(2)$$ 上，在 $$\mathrm{SO}(3)$$ 上只能是射影的。

- **$$\chi_0$$ 这边**：$$\tilde\rho(-I)=I$$，即 $$(-1)^{2j}=1$$，即 $$j\in\mathbb Z_{\ge0}$$。此时 $$\tilde\rho$$ 经过商 $$\mathrm{SU}(2)\to\mathrm{SO}(3)$$ 分解（因 $$\ker=\{\pm I\}$$ 被送到 $$I$$），故它本身就是 $$\mathrm{SO}(3)$$ 的**线性**表示。所以**整数自旋落在 $$\chi_0$$ 这一边**。

- **两边合起来**是 $$\mathrm{SU}(2)$$ 的全部不可约表示（每个 $$j\in\tfrac12\mathbb Z_{\ge0}$$ 落在恰好一边）。于是「$$\mathrm{SO}(3)$$ 的（不可约）射影表示」与「$$\mathrm{SU}(2)$$ 的（不可约）线性表示」在同一层级上是一回事——**多出来的一层（覆盖群）把所有射影表示都变成了线性表示**，而「是否在中心上取平凡特征」把它们分成了整数自旋与半整数自旋两族。

把「$$\mathrm{SO}(3)$$ 的射影表示全体」与「$$\mathrm{SU}(2)$$ 的、在中心上按某个固定特征变换的线性表示全体」各自看成一个整体，(i) 给出的对应在同构意义下是一一的。下一章（第 31 章）把这类「整体之间的对应」抽象成**函子**，并给出判断「两个这样的对应何时自然同构」的语言——那时本节这个对应会变成一句「诱导表示函子与限制函子互为伴随」式的陈述。$$\blacksquare$$

**解 研2.**

**记号与准备。** 截面 $$s:G\to\tilde G$$ 满足 $$\pi\circ s=\operatorname{id}$$（存在性用选择公理），且每个 $$\tilde g\in\tilde G$$ 唯一地写成 $$\tilde g=s(g)i(\lambda)$$（$$\lambda\in\mathbb C^*$$，$$g=\pi(\tilde g)$$）：因为 $$s(g)^{-1}\tilde g\in\ker\pi=i(\mathbb C^*)$$。上循环由
$$s(g)s(h)=i\bigl(c(g,h)\bigr)s(gh),\qquad i'(c'(g,h))=s'(g)s'(h)s'(gh)^{-1}$$
定义（把定理 3.10 的 $$c$$ 用 $$\mathbb C^*$$ 的乘法写法搬过来）。

**(⇒)** 设 $$\theta$$ 是使 $$\pi'\circ\theta=\pi$$、$$\theta\circ i=i'$$ 的同构。令 $$\theta(s(g))=s'(g)i'(\beta(g))$$（正交分解，$$\beta:G\to\mathbb C^*$$ 由 $$\theta$$ 与两个截面唯一确定）。两边作用 $$\pi'$$：左边 $$\pi'(\theta(s(g)))=\pi(s(g))=g$$，右边 $$\pi'(s'(g)i'(\beta(g)))=g$$，一致。

现在算两次乘积：
$$\theta\bigl(s(g)s(h)\bigr)=s'(g)i'(\beta(g))\,s'(h)i'(\beta(h))=s'(g)s'(h)\,i'(\beta(g)\beta(h))=i'\bigl(c'(g,h)\beta(g)\beta(h)\bigr)s'(gh),$$
（第二步用了 $$i'(\beta(g))$$ 中心、可与 $$s'(h)$$ 交换）。另一方面
$$\theta\bigl(s(g)s(h)\bigr)=i\bigl(c(g,h)\bigr)\theta(s(gh))=i'(c(g,h))\,s'(gh)i'(\beta(gh))=i'\bigl(c(g,h)\beta(gh)\bigr)s'(gh).$$
（把 $$\theta\circ i=i'$$ 与 $$\theta(s(gh))=s'(gh)i'(\beta(gh))$$ 代进去。）比较两式（$$\tilde G'$$ 中 $$s'(gh)$$ 的左分解唯一），得
$$c'(g,h)\beta(g)\beta(h)=c(g,h)\beta(gh)\quad\Longrightarrow\quad c(g,h)=\frac{\beta(g)\beta(h)}{\beta(gh)}c'(g,h),$$
即 $$c$$ 与 $$c'$$ 上同调。

**(⇐)** 设 $$c(g,h)=\dfrac{\beta(g)\beta(h)}{\beta(gh)}c'(g,h)$$ 对某个 $$\beta:G\to\mathbb C^*$$。定义
$$\theta:\tilde G\to\tilde G',\qquad \theta\bigl(s(g)i(\lambda)\bigr):=s'(g)i'\bigl(\beta(g)\lambda\bigr).$$
**良定义**：$$\tilde G$$ 中每个元素唯一地写成 $$s(g)i(\lambda)$$，故这是映射。**同态**：由上式与 $$i(\lambda)$$ 中心，
$$\theta\bigl(s(g)i(\lambda)\cdot s(h)i(\mu)\bigr)=\theta\bigl(s(g)s(h)i(\lambda\mu)\bigr)=\theta\bigl(i(c(g,h))s(gh)i(\lambda\mu)\bigr)=\theta\bigl(s(gh)i(c(g,h)\lambda\mu)\bigr)$$
$$=s'(gh)i'\bigl(\beta(gh)c(g,h)\lambda\mu\bigr),$$
而
$$\theta(s(g)i(\lambda))\theta(s(h)i(\mu))=s'(g)i'(\beta(g)\lambda)s'(h)i'(\beta(h)\mu)=i'(c'(g,h)\beta(g)\beta(h)\lambda\mu)s'(gh)=s'(gh)i'\bigl(c'(g,h)\beta(g)\beta(h)\lambda\mu\bigr).$$
两式相等，因为 $$\beta(gh)c(g,h)=c'(g,h)\beta(g)\beta(h)$$ 正是上同调关系。**同构**：完全对称地，用 $$\beta^{-1}$$ 定义逆映射（检验 $$\theta^{-1}(s'(g)i'(\lambda))=s(g)i'(\beta(g)^{-1}\lambda)$$，复合得恒等）。**交换三角形**：$$\pi'(\theta(s(g)i(\lambda)))=\pi'(s'(g))=g=\pi(s(g)i(\lambda))$$，故 $$\pi'\circ\theta=\pi$$。核上的行为：先把两个截面**归一化**，即把 $$s$$ 换成 $$g\mapsto s(g)s(e)^{-1}$$（这仍满足 $$\pi\circ s=\operatorname{id}$$，因为 $$\pi(s(e))=e$$；同理处理 $$s'$$），于是 $$s(e)=s'(e)=e$$。此时 $$\theta(i(\lambda))=\theta(s(e)i(\lambda))=s'(e)i'(\beta(e)\lambda)=i'(\beta(e)\lambda)$$。而由上同调关系在 $$g=h=e$$ 处取值：$$\beta(e)c(e,e)=c'(e,e)\beta(e)^2$$；把提升归一化为 $$\rho(e)=I$$（由 $$[\rho(e)]=[I]$$ 总可做到）给出 $$c(e,e)=1$$，同理 $$c'(e,e)=1$$，故 $$\beta(e)=\beta(e)^2$$，即 $$\beta(e)=1$$。于是 $$\theta(i(\lambda))=i'(\lambda)$$，即 $$\theta\circ i=i'$$。

**结论** 两方向合起来给出：$$\mathbb C^*$$ 中心扩张的同构类与上循环模去上边界一一对应，即被 $$H^2(G;\mathbb C^*)$$ 的元素标记。

**这题的关键 leap**：把「同构」翻译成「两组截面之间的换基函数 $$\beta$$」，于是「上循环之差」正好变成 $$\beta$$ 的上边界。上同调类之所以是「不变量」，就因为它不依赖截面的选择。

第 31 章会把这个现象升格为一条一般原则：一个「整体对象」（这里是 $$G$$）上挂的附加数据（这里是中心扩张），可以用**函子**的语言统一描述，而同调代数（第 35 章）正是这套语言在「何时可提升」问题上的计算工具。本章的 $$H^2(G;\mathbb C^*)$$ 是那条长路的起点。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**1. 一条等式把三块数学焊在一起。**
$$\text{Möbius 群}=\mathrm{PSL}(2,\mathbb C)=\mathrm{PGL}(2,\mathbb C)\cong\mathrm{SO}^+(1,3)=\text{Lorentz 群的单位分支}.$$
左边是复分析的对象（分式线性变换），右边是相对论的对象（保持光锥的线性变换），中间是代数对象（$$2\times2$$ 复矩阵模掉标量）。$$\widehat{\mathbb C}$$ 是光锥的天球，$$\mathrm{SL}(2,\mathbb C)$$ 是它们共同的双重覆叠。这条等式之所以可能，是因为 $$\mathbb C^*$$ 中每个元素都有平方根（定理 3.2(iii)），而这件事在 $$\mathbb R$$ 上失败（注 3.2、练习竞 5）。

**2. 「双重覆盖」= 「中心扩张」= 「射影表示」= 「上同调非平凡」。** 这四个词是同一件事的四种写法：
$$\begin{array}{ccccc}\mathrm{SU}(2)\to\mathrm{SO}(3)&\longleftrightarrow&\mathbb Z/2\hookrightarrow\tilde G\twoheadrightarrow G&\longleftrightarrow&\alpha:G\to\mathrm{PGL}(V)&\longleftrightarrow&[c]\in H^2(G;\mathbb C^*)\ne0 .\end{array}$$
定理 3.11 给出了「可线性化 $$\iff$$ 上循环是上边界」的判据，于是「一个射影表示好不好」变成了一个上同调类的计算问题。第 22 章的 $$H_3(\mathbb R)$$ 是这条链的原型，第 29 章的旋量群是它的一般维数版本。

**3. 「转 360° 变号」的正确读法：不是几何怪事，而是射影性的必然。** 第 26 章把它算成了一个拓扑事实（$$\pi_1(\mathrm{SO}(3))=\mathbb Z/2$$），本章把它解释成了一个表示论事实：态空间只被定义到相位，所以对称群只能射影地作用；$$\mathrm{SO}(3)$$ 的射影表示分类（定理 3.13）给出唯一的两族——整数自旋（下降为线性表示）与半整数自旋（不可线性化）。**半整数自旋的「必须」，来自 $$-I$$ 在 $$V_j$$ 上作用为 $$(-1)^{2j}$$ 这件事。**

**4. 群上同调是「提升问题」的度量。** 定理 3.11 与练习研 2 合起来说：$$G$$ 的 $$\mathbb C^*$$ 中心扩张（等价地，$$G$$ 的射影表示）被 $$H^2(G;\mathbb C^*)$$ 标记。这个「用上同调刻画障碍」的套路在数学里反复出现：de Rham 上同调刻画「闭形式何时是恰当形式」（第 14 章），第 35 章的导出函子会把它推成一般理论。

**5. 本课程的一条大线在此收口。** 第 22 章（$$H_3(\mathbb R)$$ 的中心扩张）$$\to$$ 第 26 章（$$\mathrm{SU}(2)$$ 双重覆盖 $$\mathrm{SO}(3)$$）$$\to$$ 第 28 章（$$\mathfrak{sl}(2)$$ 的表示分类）$$\to$$ 第 29 章（旋量与 $$\mathrm{Spin}(1,3)$$）$$\to$$ 本章（射影表示与中心扩张的一般理论）。这条线的每一站都同时从几何、物理、代数三个方向被触及，而收口处的那句话是：**「群作用在射影空间上」，而不是「群作用在向量空间上」，才是量子力学的默认设置。**

---

**下一章的悬念**：本章反复在做同一件事——把一个环环相扣的「整体」抽象出来（群、表示、中心扩张、上循环），再研究**它们之间的映射**（同态、同构、提升）。当这些「整体」与「它们之间的映射」多到需要一个统一语言时，数学的下一步就是把这些结构本身当成对象：**范畴**。第 31 章将引入范畴与函子，把本章的「Möbius 群 $$\to$$ Lorentz 群」这类对应、以及研 1 里那个「射影表示 $$\leftrightarrow$$ 覆盖群的线性表示」的一一对应，统一成一句可计算的话。卷四在此结束，卷五从范畴论重新出发。

**延伸阅读**

- Fulton–Harris, *Representation Theory: A First Course*，第 1–2 讲（$$\mathrm{SU}(2)$$ 与 $$\mathrm{SL}(2,\mathbb C)$$ 的表示、$$\mathrm{SL}(2,\mathbb C)\cong\mathrm{Spin}(1,3)$$ 的矩阵计算）。
- Brian Hall, *Lie Groups, Lie Algebras, and Representations*，第 1–2 章（矩阵李群与覆叠群）、第 5 章（$$\mathrm{SL}(2,\mathbb C)$$ 的表示）；本章定理 3.6 与 3.8 的标准版本在此。
- Peter Woit, *Quantum Theory, Groups and Representations*（Columbia 讲义）——从射影表示与 Wigner 定理出发讲量子对称性，与本章第 4.3 节直接对应。
- Wigner 的原著 *Group Theory and its Application to the Quantum Mechanics of Atomic Spectra*，关于「射线表示 (ray representation)」的一节是射影表示的物理来源。
- 中子干涉实验（Rauch 等，1975）是「转 $$360°$$ 变号、转 $$720°$$ 复原」的实验证据，任何量子力学期刊的综述里都能找到其与 $$\mathrm{SU}(2)$$ 双重覆盖的关系。


---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch29_Clifford代数与Lorentz群.md">← 第29章 Clifford 代数与 Lorentz 群</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch31_范畴与函子.md">第31章 范畴与函子 →</a></div>
</div>
