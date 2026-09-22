---
layout: default
---

# 第48章: 仿射空间、变换群与 Lie 群·下：完整推导 (Affine Spaces, Transformation Groups and Lie Groups · Part II: Full Derivation)

> 专家依据: `_experts/algebra/lie-algebra-root-systems.md`（主）+ `_experts/algebra/_SKILL.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）
> 配套预备: 见 第47章 仿射空间、变换群与 Lie 群·上（同一主题的具体铺垫，建议先读）

## 一、本章概要 (Overview)

读完第47章的具体例子——两点相减而不能相加、一个"转+搬"的仿射变换如何升一维写成齐次矩阵、$$SO(2)$$ 里两个具体角度相乘确实光滑、以及一对具体矩阵的换位子精确测量"顺序颠倒的代价"——之后，这里把同样的四个构造写成一般定义，并给出完整证明：本章的 3.1–3.2 节把第47章 3.1–3.2 节的具体点、具体矩阵换成一般的仿射空间与仿射群；3.3 节把第47章 3.3 节里"角度相减天生光滑"这一个例子，扩展成对任意群都成立的判据；3.4 节把第47章 3.4 节里 $$E,F$$ 的换位子计算，扩展成对任意 Lie 群都成立的一般定理（用到的正是同一个二阶展开的思想，只是从幂零矩阵换成了任意矩阵、任意测试函数）。

到这一章为止，我们手里有两样一直各走各的东西：一卷讲**光滑流形**（第 05、06 章：切空间、纤维丛、余切丛），一卷开头讲**群**（第 01、02 章：$$SO(2)$$ 与它的谱）。本章把它们焊在一起：**Lie 群 (Lie group) = 群 + 光滑流形**。焊接的动机不是数学家嫌例子不够多，而是物理先提出来的——只要讨论「参考系变换」，就同时需要「变换能复合」（群）与「变换能连续光滑地调参」（流形）。

本章三处落点。第一，**仿射空间 (affine space)**：为什么「点」不能与「点」相加，「点」却可以与「向量」相加。这也是一整类「绝对物理量 / 相对物理量」（温度与温差、电压与电势差、势能与势能差、原函数与不定积分常数）的代数结构。第二，**Lie 群的定义**：群结构与流形结构必须相容，相容的精确含义是「乘法与求逆都是光滑映射」。第三，**左不变向量场与 Lie 代数 (Lie algebra)**：在恒等元处对群求导，得到的不是数、不是线性映射，而是一个**代数**（带括号的向量空间）。

与前后章的接口有三条。第 01、02 章的 $$SO(2)$$ 是 Lie 群的最小例子，本章要把那里的逐例计算升成一般理论（定理 3.11 给图册、定理 3.24 给 $$\exp$$ 的一般性质）。第 12 章的主丛与第 26 章的 Stokes 在这里汇合：**Lie 群本身就是一个主丛**，而 Maurer–Cartan 方程就是它在群上的一次外微分运算（定义 3.25 – 定理 3.28）。第 46 章的指数映射——那里是 $$e^{-itH}$$ 与算子半群——在这里第一次有了一般定义（定义 3.23）。

## 二、入口：一道具体的问题 (Entry Problem)

先给题，不给定义。以下三问都是本课程的入口题（(a)(b) 改编自经典力学讨论与 Квант 式的坐标变换训练题，(c) 为自编）。

### 问题 (a)：点和向量

平面上取两点 $$P=(1,2)$$、$$Q=(3,4)$$。向量加法给出 $$P+Q=(4,6)$$。问：$$(4,6)$$ 是什么？它是一个点吗？如果换一个坐标系原点，$$P+Q$$ 的结果会不会变？

再把这事搬到物理上：气温 $$20\,^\circ\mathrm{C}$$ 与 $$30\,^\circ\mathrm{C}$$。$$20\,^\circ\mathrm{C}+30\,^\circ\mathrm{C}$$ 有意义吗？如果把 $$30\,^\circ\mathrm{C}$$ 换算成绝对温标写成 $$303.15\,\mathrm{K}$$，那么 $$20\,^\circ\mathrm{C}+303.15\,\mathrm{K}$$ 又是什么？这两次「加法」的结果一样吗？

### 问题 (b)：旋转和平移能不能都写成矩阵

设 $$R(\theta)$$ 是第 02 章定义 3.1 的绕原点逆时针旋转，$$T_a$$ 是把平面上每一点 $$x$$ 搬到 $$x+a$$ 的平移。$$R(\theta)$$ 可以写成 $$2\times2$$ 矩阵乘 $$x$$。问：$$T_a$$ 能不能也写成 $$2\times2$$ 矩阵乘 $$x$$ 的形式？如果不能，最小的「矩阵化」代价是什么？

### 问题 (c)：一边是群一边是流形，求导会得到什么

设 $$t\mapsto R(t)$$ 是一条光滑曲线，满足 $$R(t)\in SO(2)$$、$$R(0)=I$$。

(i) 证明 $$R'(0)$$ 必是反对称矩阵。

(ii) 记 $$\omega(t)=R(t)^{-1}R'(t)$$。证明：$$\omega(t)$$ 恒等于某个常矩阵 $$A$$，当且仅当 $$R(t)=\exp(tA)$$（矩阵指数）。

(iii) 由此说明第 02 章定理 3.10 里那个把 $$\theta$$ 送到 $$R(\theta)$$ 的映射，与「指数」是同一个东西。

问 (c) 就是本章的引子：$$SO(2)$$ 这个集合上同时有「能相乘」和「能求导」两件事，把它们一起用，能强制出多少结构来。第三、五节的工具就是为回答它准备的。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 仿射空间：点为什么不能加点

第47章用两组具体数字（平面上的两点、两个钟点）反复验证了同一条规律：位置之间只能相减，位置与位移之间才能相加。要把这条规律写成不依赖具体数字的公理，需要同时管住两件事——位移本身如何运算（这交给一个现成的向量空间 $$V$$），以及位移如何"作用"到位置上（这需要一个新映射，且这个映射必须满足"移动零位移不变""先后移动可以合并成一次移动""任意两点之间恰有一个位移把前者搬到后者"这三条，缺一条都会让"点与向量的区分"失效）。

**定义 3.1（仿射空间, affine space）**。设 $$A$$ 是非空集合，$$V$$ 是 $$\mathbb{R}$$ 上的向量空间。若有一个映射

$$A\times V\to A,\qquad (p,v)\mapsto p+v,$$

满足

(A1) 对一切 $$p\in A$$，$$p+0=p$$；

(A2) 对一切 $$p\in A$$、$$u,v\in V$$，$$(p+u)+v=p+(u+v)$$；

(A3) 对任意 $$p,q\in A$$，存在**唯一**的 $$v\in V$$ 使 $$p+v=q$$，

则称 $$A$$ 是**仿射空间 (affine space)**，$$V$$ 是它的**自由向量空间 (space of free vectors)**，记 $$\overrightarrow{A}=V$$；$$\dim V$$ 称为 $$A$$ 的维数。(A3) 中那个唯一的 $$v$$ 记作 $$q-p$$。

**定理 3.1（差向量的基本性质）**。在定义 3.1 下：

(i) $$p-p=0$$；

(ii) $$(p+v)-p=v$$；

(iii) $$(q-p)+(r-q)=r-p$$；

(iv) 若 $$p+v=q+w$$，则 $$q-p=v-w$$。

证明。(i) 由 (A1)，$$p+0=p$$；把它读成 (A3) 的形式 $$p+0=p$$，唯一性给出 $$p-p=0$$。

(ii) 由 (A3)，$$(p+v)-p$$ 是唯一使 $$p+w=p+v$$ 的 $$w$$；取 $$w=v$$ 即可。

(iii) 计算

$$p+\bigl[(q-p)+(r-q)\bigr]=\bigl(p+(q-p)\bigr)+(r-q)=q+(r-q)=r,$$

第一步用 (A2)，后两步用 (A3) 的（存在性方向的）定义。于是 $$(q-p)+(r-q)$$ 是那个唯一把 $$p$$ 送到 $$r$$ 的向量，即 $$r-p$$。

(iv) 由 $$p+v=q+w$$ 得

$$q=p+v-w=p+(v-w),$$

两次用 (A2)；(A3) 的唯一性给出 $$q-p=v-w$$。$$\blacksquare$$

**命题 3.2（与另一套公理清单的对比）**。那套公理给出的是四条：单位元 $$p+0=p$$、结合律 $$(p+v_1)+v_2=p+(v_1+v_2)$$、交换律 $$(p+v_1)+v_2=(p+v_2)+v_1$$、单满（$$v\mapsto p+v$$ 是双射）。这四条与 (A1)–(A3) 是等价的。

证明。$$(\Leftarrow)$$ 单位元与结合律就是 (A1)(A2)。「交换律」不是新公理：由 (A2) 与 $$V$$ 中加法的交换律，

$$(p+v_1)+v_2=p+(v_1+v_2)=p+(v_2+v_1)=(p+v_2)+v_1.$$

「单满」就是 (A3)：满射性是 (A3) 的存在性部分，单射性是唯一性部分（若 $$p+v=p+w$$，则 $$v=w$$，这由 $$(p+v)-p=(p+w)-p$$ 与定理 3.1(ii) 得到）。

$$(\Rightarrow)$$ 反过来，「单满」给出 (A3) 的两条；(A1) 被他写成了「加群 $$\overrightarrow{A}(0,+)$$ 的单位元」，在形式上等价。因此两套公理描述同一类对象，本章用 (A1)–(A3) 是因为它把「$$A$$ 本身的公理」与「$$V$$ 的向量空间公理」分得干净。$$\blacksquare$$

**定义 3.2（平移变换群, translation group）**。对每个 $$v\in V$$，定义 $$A$$ 上的变换

$$t_v:A\to A,\qquad t_v(p)=p+v,$$

称 $$t_v$$ 为沿 $$v$$ 的**平移 (translation)**；集合 $$T(A)=\{t_v\}_{v\in V}$$ 配上映射的复合称为 $$A$$ 的**平移变换群**。

**定理 3.3（$$T(A)\cong(V,+)$$，且 $$A$$ 是主齐性空间）**。映射 $$v\mapsto t_v$$ 是加法群 $$(V,+)$$ 到变换群 $$T(A)$$ 的群同构；$$T(A)$$ 在 $$A$$ 上的作用是**自由且可迁 (free and transitive)** 的，即 $$A$$ 是 $$V$$ 的**主齐性空间 (principal homogeneous space，也叫 torsor)**。

证明。先证同构。由 (A2)，

$$t_{u+v}(p)=p+(u+v)=(p+u)+v=t_v(t_u(p)),$$

故 $$t_{u+v}=t_v\circ t_u$$；又 $$(V,+)$$ 交换，这个式子也写成 $$t_{u+v}=t_u\circ t_v$$，故 $$v\mapsto t_v$$ 是同态。由 (A1)，$$t_0=\mathrm{id}_A$$。逆元：$$t_{-v}\circ t_v(p)=(p+v)+(-v)=p+(v-v)=p$$，这里用了 (A2) 与向量空间里 $$v-v=0$$，故 $$t_{-v}=(t_v)^{-1}$$。单射：若 $$t_v=\mathrm{id}_A$$，则取任一 $$p$$ 得 $$p+v=p=p+0$$，(A3) 的唯一性给出 $$v=0$$。满射由定义。故是同构。

再证作用自由：稳定子 $$\mathrm{Stab}(p)=\{v:t_v(p)=p\}$$ 平凡，这正是上面单射性证明的内容。再证可迁：对任意 $$p,q$$，取 $$v=q-p$$ 有 $$t_{q-p}(p)=q$$。一个既自由又可迁的作用，恰好使全体 $$t_v$$ 与「$$A$$ 到自身的一一搬运」重合，这就是主齐性空间。$$\blacksquare$$

定理 3.3 的物理读法：**$$A$$ 上没有内蕴的原点**。一旦人为选定一点 $$o\in A$$ 当原点，映射 $$p\mapsto p-o$$ 就把 $$A$$ 双射到 $$V$$，$$A$$ 于是**暂时**获得向量空间结构；换一个原点 $$o'=o+b$$，新坐标与原坐标差一个平移 $$v\mapsto v-b$$。「相对结构比绝对结构丰富」，精确含义就是这个：$$V$$ 有加法结构，而 $$A$$ 只有 $$V$$ 作用在它上面的结构，这个作用里没有提供「哪个点特殊」。

**例 3.3（绝对量与相对量）**。

(1) $$A=V=\mathbb{R}^n$$、$$p+v$$ 取向量加法。此时 $$A$$ 是仿射空间，但 $$0\in A$$，所以它**有**内蕴原点——这类对象习惯上叫「向量量」而不是「点」。

(2) $$A=$$ 温度（取绝对温标下的实数），$$V=$$ 温差。正规的物理解释如定义 3.1。$$20\,^\circ\mathrm{C}+30\,^\circ\mathrm{C}$$ 之所以没有意义，是因为「$$+$$」的第二个变元必须取在 $$V$$ 里；若把 $$30\,^\circ\mathrm{C}$$ 读成温度 $$303.15\,\mathrm{K}$$ 当绝对量去加，就得 $$293.15+303.15=596.3\,\mathrm{K}$$，即 $$323.15\,^\circ\mathrm{C}$$；若把它读成温差 $$30\,\mathrm{K}$$ 去加，就得 $$323.15\,\mathrm{K}$$，即 $$50\,^\circ\mathrm{C}$$。两个答案不同，说明这个「加法」依赖你把 $$30\,^\circ\mathrm{C}$$ 往哪一边解释，因而不是一个良定义的运算。

(3) $$A=$$ 平面上的点集，$$V=\mathbb{R}^2$$，$$p+v$$ 是「把点沿 $$v$$ 搬一段」。这时 $$A$$ 就是本章入口题 (a) 的来源：$$P+Q$$ 若按向量加法在坐标里算出 $$(4,6)$$，这个结果依赖原点的选取（换原点后是 $$(4,6)-o$$），而 $$Q-P=(2,2)$$ 不依赖。**差是向量，和不是点。**

(4) $$A=\{\text{$$f$$ 的原函数}\}$$，$$V=\mathbb{R}$$，运算是「$$F\mapsto F+c$$」。$$\int f(x)\,dx=F(x)+C$$ 里那个自由常数 $$C$$ 之所以自由，正因为 $$A$$ 是仿射空间而非向量空间——$$\mathbb{R}$$ 上的加法（常数相加）在 $$A$$ 上作用，但 $$A$$ 上没有自然零点。同理，中学物理里可以任意选势能零点、而只能谈「电势差」，都是这同一件事。

### 3.2 仿射变换与仿射群

仿射空间本身只是"点 + 作用在点上的向量空间"，还没有"变换"的概念。第47章用一个具体的"先转 $$90^\circ$$ 再平移 $$(1,2)$$"的例子说明了：这样的映射不是线性映射（因为它不固定原点），但它把"位移"变成"位移"的方式（先转再看差多少）仍然是线性的。要把"既不是线性映射、又保留了线性结构"这件事说清楚，需要一个新概念——仿射映射：它不要求映射本身线性，只要求它把差向量的变化规律记录在一个线性映射里。

**定义 3.4（仿射变换, affine transformation）**。设 $$A,A'$$ 是仿射空间，自由向量空间分别为 $$V,V'$$。映射 $$f:A\to A'$$ 称为**仿射映射 (affine map)**，若存在线性映射 $$\varphi:V\to V'$$ 使

$$f(p+v)=f(p)+\varphi(v)\qquad\text{对一切 }p\in A,\ v\in V.$$

此时 $$\varphi$$ 被 $$f$$ 唯一确定（由定理 3.1(iv)，$$v=q-p$$ 是两点之差），称为 $$f$$ 的**线性部分 (linear part)**，记 $$\vec f$$ 或 $$Df$$。当 $$A=A'$$、$$\varphi$$ 可逆且 $$f$$ 是双射时，称 $$f$$ 是 $$A$$ 的**可逆仿射变换**。

**定理 3.5（仿射变换 = 线性部分 + 一个平移）**。固定 $$A$$、$$V$$。设 $$f:A\to A$$ 是可逆仿射变换，任取 $$o\in A$$，令 $$b=f(o)-o\in V$$、$$\varphi=Df$$。则

$$f(p)=o+\varphi(p-o)+b\qquad\text{对一切 }p\in A.$$

反过来，任给 $$\varphi\in GL(V)$$ 与 $$b\in V$$，上式定义一个可逆仿射变换；数对 $$(\varphi,b)$$ 由 $$f$$ 唯一确定，且与 $$o$$ 的选取无关。

证明。**唯一性**：给定 $$f$$，取 $$\varphi=Df$$（定义 3.4 已证唯一）、$$b=f(o)-o$$。展开：对 $$p=o+v$$，

$$f(o+v)=f(o)+\varphi(v)=o+b+\varphi(v)=o+\varphi(p-o)+b,$$

最后一步用 $$v=p-o$$。故公式成立。要说明 $$(\varphi,b)$$ 与 $$o$$ 无关：换原点 $$o'=o+w$$，则 $$p-o'=(p-o)-w$$，而

$$f(o')-o'=f(o+w)-(o+w)=\bigl(f(o)+\varphi(w)\bigr)-o-w=b+(\varphi(w)-w),$$

代入公式右边 $$o'+Df(p-o')+(b+\varphi(w)-w)=o+w+\varphi((p-o)-w)+b+\varphi(w)-w=o+\varphi(p-o)+b$$，与 $$o$$ 无关。

**存在性**：给定 $$(\varphi,b)$$，定义 $$f(p)=o+\varphi(p-o)+b$$。则

$$f(p+v)=o+\varphi(p-o)+\varphi(v)+b=f(p)+\varphi(v),$$

故 $$f$$ 是仿射映射；又

$$p\mapsto o+\varphi^{-1}\bigl(p-o-b\bigr)$$

是它的逆（代进去各步消掉），故 $$f$$ 可逆。$$\blacksquare$$

**定义 3.6（仿射群, affine group）**。$$A$$ 上全体可逆仿射变换在复合下构成群（复合的结合律、$$\mathrm{id}_A$$、逆都在集合内），记 $$\mathrm{Aff}(A)$$；当 $$A=\mathbb{R}^n$$ 记 $$\mathrm{Aff}(n)$$。

**定理 3.7（齐次坐标实现：$$\mathrm{Aff}(n)\hookrightarrow GL(n+1,\mathbb{R})$$）**。映射

$$\Psi:\mathrm{Aff}(n)\to GL(n+1,\mathbb{R}),\qquad (M,b)\mapsto\begin{bmatrix} M & b\\ 0 & 1\end{bmatrix}$$

是单射群同态（这里 $$M\in GL(n,\mathbb{R})$$、$$b\in\mathbb{R}^n$$、右下角的 $$1$$ 是 $$1\times1$$ 块）。它的像恰是 $$\{(M,b)\}$$ —— 换句直白的话：**仿射变换可以写成矩阵，代价是把维数升高一维**。

证明。同态性来自分块矩阵乘法：

$$\begin{bmatrix} M & b\\ 0 & 1\end{bmatrix}\begin{bmatrix} M' & b'\\ 0 & 1\end{bmatrix}=\begin{bmatrix} MM' & Mb'+b\\ 0 & 1\end{bmatrix},$$

右边正是「先作用 $$(M',b')$$ 再作用 $$(M,b)$$」的数对：$$x\mapsto M'x+b'\mapsto M(M'x+b')+b=MM'x+(Mb'+b)$$。单位元是 $$(I,0)\leftrightarrow I_{n+1}$$。逆元：由 $$(M,b)^{-1}=(M^{-1},\,-M^{-1}b)$$（代进上面的乘法式即验），而矩阵逆恰好是

$$\begin{bmatrix} M & b\\ 0 & 1\end{bmatrix}^{-1}=\begin{bmatrix} M^{-1} & -M^{-1}b\\ 0 & 1\end{bmatrix}.$$

单射性：从分块形状直接读出 $$(M,b)$$。至于「像恰是全部这种形状的可逆矩阵」：一个分块上三角矩阵 $$\begin{bmatrix}M&b\\0&1\end{bmatrix}$$ 的行列式等于 $$\det M$$，故它可逆当且仅当 $$\det M\neq0$$。$$\blacksquare$$

注意 $$\Psi$$ 的像不是整个 $$GL(n+1,\mathbb{R})$$（例如 $$\begin{bmatrix}I&0\\ c&1\end{bmatrix}$$ 一般不在像里）。它是 $$GL(n+1,\mathbb{R})$$ 的一个由闭合条件（末行 $$=(0,\dots,0,1)$$）切出的子集。$$\mathrm{Aff}(n)$$ 是 Lie 群这一点不必调用任何一般性定理，可以直接看出：作为集合它有坐标 $$(M,b)\in GL(n,\mathbb{R})\times\mathbb{R}^n$$（开集 $$\times$$ 向量空间，是 $$n^2+n$$ 维光滑流形），在这组坐标下

$$(M,b)(M',b')=(MM',\ Mb'+b),\qquad (M,b)^{-1}=(M^{-1},\ -M^{-1}b),$$

右端是矩阵乘法、矩阵乘向量与向量加法的组合，都是光滑的；$$M\mapsto M^{-1}$$ 在 $$GL(n,\mathbb{R})$$ 上光滑（由 Cramer 法则，逆的每个分量是 $$\det M$$ 的有理函数）。故由定义 3.9，$$\mathrm{Aff}(n)$$ 是 $$n^2+n$$ 维 Lie 群。

**例 3.7（Galileo 变换群）**。取 4 维仿射空间 $$A^4$$，它的点叫**事件 (event)**（把「何时」「何地」写进一个坐标）。取定原点与坐标 $$(x,y,z,t)$$。两个以匀速 $$v$$ 沿 $$x$$ 方向相对运动的惯性参考系，坐标关系是

$$\begin{cases} x'=x-vt\\ y'=y\\ z'=z\\ t'=t\end{cases}$$

这称为 **Galileo 变换 (Galilean transformation)**。它是一个**线性**双射，矩阵为

$$\begin{bmatrix} 1&0&0&-v\\ 0&1&0&0\\ 0&0&1&0\\ 0&0&0&1\end{bmatrix},$$

所以是 $$\mathrm{Aff}(4)$$ 的一个子集。把旋转 $$R\in SO(3)$$、速度提升 $$v$$、空间平移 $$a$$、时间平移 $$s$$ 全都算上，变换形如

$$(x,t)\mapsto (Rx+vt+a,\ t+s),$$

它在复合下成群，称为 **Galileo 群 (Galilei group)**。数自由参数：3（旋转）+ 3（提升）+ 3（空间平移）+ 1（时间平移）= **10** 维。第 25、27 章会把它当作一个具体的 Lie 群拿出来分析；那里还会看到它的一个重要异常——这个 10 维 Lie 群在量子力学里的投影表示要比它的 Lie 代数多出一个中心元（质量），那是后话。

### 3.3 Lie 群：两种结构要相容

第47章用 $$SO(2)$$ 里两个具体角度相乘（$$\pi/6$$ 与 $$\pi/3$$）说明了：乘积矩阵的每个入口都由 $$\cos,\sin$$ 的和角公式给出，是光滑函数——但那只是"光滑"这个要求在一个例子上的体现，还不是定义本身。在正式写下"光滑"之前，先写一个更弱、只需要连续性的版本，把框架搭好；随后把"连续"换成"光滑"就得到 Lie 群。

**定义 3.8（拓扑群, topological group）**。拓扑空间 $$G$$ 同时是群，若乘法 $$\mu:G\times G\to G$$（积空间取积拓扑）与求逆 $$\iota:G\to G$$ 都连续，称 $$G$$ 为**拓扑群**。

**定义 3.9（Lie 群, Lie group）**。集合 $$G$$ 若同时满足

(L1) $$G$$ 是群；

(L2) $$G$$ 是光滑流形（第 10 章的意义，实流形、无边界）；

(L3) 乘法 $$\mu(x,y)=xy$$ 与求逆 $$\iota(x)=x^{-1}$$ 都是光滑映射（$$G\times G$$ 取积流形结构），

则称 $$G$$ 是 **Lie 群 (Lie group)**。

(L3) 就是「两种结构相容」的精确含义。相容必须有内容，不能只是并列摆着：如果没有 (L3)，一个集合上可以挂一个群结构和一个流形结构而二者毫无关系（例如 $$\mathbb{R}$$ 上取普通流形结构、取任意一个把群运算搬得乱七八糟的群结构）。

**定理 3.10（光滑性判据）**。在 (L1)(L2) 下，(L3) 等价于单条要求

$$\sigma:G\times G\to G,\qquad \sigma(x,y)=x^{-1}y$$

是光滑映射。

证明。$$(\Rightarrow)$$ $$\sigma(x,y)=\mu(\iota(x),y)$$ 是光滑映射的复合，光滑。$$(\Leftarrow)$$ 先取 $$x=e$$：$$\iota(y)=\sigma(e,y)$$，光滑。再注意 $$xy=(x^{-1})^{-1}y=\sigma(\iota(x),y)$$，由 $$\iota$$ 光滑与 $$\sigma$$ 光滑知 $$\mu$$ 光滑。反之 $$\mu$$ 光滑加 $$\iota$$ 光滑立刻给出 $$\sigma$$ 光滑，故等价。$$\blacksquare$$

验证一个群是不是 Lie 群时，检查 $$\sigma$$ 通常比分别检查 $$\mu$$ 与 $$\iota$$ 省事。

**例 3.10（经典群, classical groups）**。以下都是 Lie 群。记 $$M^{*}=\overline{M}^{\mathsf T}$$（共轭转置）。

| 群 | 元素 | 实维数 |
|---|---|---|
| $$GL(n,\mathbb{R})$$ | 实可逆矩阵 | $$n^2$$ |
| $$GL(n,\mathbb{C})$$ | 复可逆矩阵 | $$2n^2$$ |
| $$SL(n,\mathbb{R})$$ | $$\det M=1$$ | $$n^2-1$$ |
| $$O(n)$$ | $$M^{\mathsf T}M=I$$ | $$n(n-1)/2$$ |
| $$SO(n)$$ | 再加 $$\det M=1$$ | $$n(n-1)/2$$ |
| $$U(n)$$ | $$M^{*}M=I$$ | $$n^2$$ |
| $$SU(n)$$ | 再加 $$\det M=1$$ | $$n^2-1$$ |
| $$\mathrm{Aff}(n)$$ | $$(M,b)$$ 或齐次矩阵 | $$n^2+n$$ |

维数是怎么数出来的：每一个独立的标量方程降低一维。以 $$O(n)$$ 为例，$$M^{\mathsf T}M=I$$ 是一个对称矩阵等式，有 $$n(n+1)/2$$ 个独立标量方程，而 $$GL(n,\mathbb{R})$$ 是 $$\mathbb{R}^{n^2}$$ 中的开集（$$n^2$$ 维），故 $$\dim O(n)=n^2-n(n+1)/2=n(n-1)/2$$。这种「数方程」的办法在 3.4 节会被求导替换成更可靠的做法。另外，$$M\in O(n)$$ 时 $$(\det M)^2=\det(M^{\mathsf T}M)=1$$，所以 $$\det M=\pm1$$，额外的 $$\det M=1$$ 条件把 $$O(n)$$ 劈成两部分，含单位的那个分支就是 $$SO(n)$$。

**定理 3.11（$$SO(2)$$ 是 Lie 群，最小例子）**。第 02 章定义 3.2 的旋转群 $$SO(2)$$ 是 1 维紧 Lie 群；作为 Lie 群它同构于圆周群 $$U(1)=\{z\in\mathbb{C}:\lvert z\rvert=1\}$$，也同构于 $$S^1$$。

证明。**先给图册。** 由第 02 章定理 3.1（$$R(\alpha)R(\beta)=R(\alpha+\beta)$$），映射

$$\Phi:\mathbb{R}\to\mathbb{R}^{2\times2},\qquad \Phi(\theta)=\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}$$

的每个分量是 $$\theta$$ 的 $$\cos/\sin$$，故光滑。**$$\Phi$$ 的像是整个 $$SO(2)$$**：设 $$R\in SO(2)$$，正交性使它保长度，故第一列 $$(a,b)$$ 满足 $$a^2+b^2=1$$；于是存在 $$\theta$$ 使 $$(a,b)=(\cos\theta,\sin\theta)$$（$$\cos,\sin$$ 的值域覆盖单位圆）。由正交性第二列必是 $$(-\sin\theta,\cos\theta)$$（与第一列正交且同长，两个选择里选 $$\det=1$$ 那个，即 $$SO$$ 而非 $$O$$）。所以 $$R=\Phi(\theta)$$，且 $$\Phi$$ 以 $$2\pi$$ 为周期。

取两张坐标卡：$$U_1=\Phi\bigl((-\pi,\pi)\bigr)$$ 与 $$U_2=\Phi\bigl((0,2\pi)\bigr)$$。它们的并是全部 $$SO(2)$$（任一 $$\theta$$ 模 $$2\pi$$ 后必落在 $$(-\pi,\pi)$$ 或 $$(0,2\pi)$$ 之一）。$$\Phi$$ 在 $$(-\pi,\pi)$$ 与 $$(0,2\pi)$$ 上都单射（$$\cos,\sin$$ 在这些区间上决定 $$\theta$$），故 $$\varphi_i=\Phi^{-1}\rvert_{U_i}$$ 是坐标卡。重叠部分分两段：在 $$\Phi\bigl((0,\pi)\bigr)$$ 上 $$\varphi_2\circ\varphi_1^{-1}(\theta)=\theta$$；在 $$\Phi\bigl((\pi,2\pi)\bigr)$$ 上 $$\varphi_2\circ\varphi_1^{-1}(\theta)=\theta-2\pi$$（因为 $$\theta\in(-\pi,0)$$ 与 $$\theta+2\pi\in(\pi,2\pi)$$ 是同一个点）。两个转移映射都光滑。故 $$SO(2)$$ 是 1 维光滑流形。

**再验相容性。** 用定理 3.10 的判据。在坐标里

$$\sigma(\alpha,\beta)=\Phi^{-1}\bigl(\Phi(\alpha)^{-1}\Phi(\beta)\bigr)=\Phi^{-1}\bigl(R(-\alpha)R(\beta)\bigr)=\Phi^{-1}\bigl(R(\beta-\alpha)\bigr)=\beta-\alpha,$$

（模 $$2\pi$$ 理解，在局部卡上就是 $$\beta-\alpha$$ 的连续分支），它是 $$\theta$$ 的光滑函数。故 $$SO(2)$$ 是 Lie 群。

**最后是拓扑。** $$SO(2)$$ 在 $$\mathbb{R}^{2\times2}$$ 里由 $$a^2+b^2=1$$（第一列）定义，是闭且有界的；由 Heine–Borel 定理它紧。把 $$\theta\mapsto e^{i\theta}$$ 与 $$\Phi(\theta)\leftrightarrow(\cos\theta,\sin\theta)$$ 拼起来，得到连续双射 $$SO(2)\to S^1$$；紧空间到 Hausdorff 空间的连续双射是同胚，故 $$SO(2)\cong S^1\cong U(1)$$。$$\blacksquare$$

**接口**：第 02 章把 $$SO(2)$$ 当作「复数乘法群」和「旋转矩阵群」使用，那里它是一个具体例子（$$\theta\mapsto R(\theta)$$ 是一条参数曲线）；定理 3.11 说明它**是** Lie 群，于是第 02 章的全部计算（复合、求逆、单位元）可以逐字搬到任何一个 Lie 群上。$$SO(2)$$ 之所以是最好的入门例子，就因为它的图册只有两张卡、转移映射只是一个平移 $$\theta\mapsto\theta-2\pi$$——这是全书第一次真的把图册写下来。

### 3.4 左不变向量场：求导给出代数

一般流形上，切空间 $$T_pM$$ 与 $$T_qM$$（$$p\neq q$$）之间没有天然的比较方式——选哪个坐标卡来比较都是人为的。但 Lie 群自带一件别的流形没有的工具：群元素之间可以互相乘。用"乘一个固定的 $$g$$"这件事，就能把 $$e$$ 处的切空间搬到 $$g$$ 处，而且这个搬运是规范的（不依赖坐标卡的选取）。第47章第四节里"转两次顺序重不重要"的书本例子，说的正是这类搬运——先固定一个操作，再看它在不同位置生效时是否"整齐划一"。左平移就是这件"搬运工具"本身。

**定义 3.12（左平移, left translation）**。对 $$g\in G$$ 定义 $$L_g:G\to G$$，$$L_g(h)=gh$$。由 (L3)，$$L_g$$ 光滑；$$(L_g)^{-1}=L_{g^{-1}}$$ 也光滑，故 $$L_g$$ 是微分同胚。

**定义 3.13（左不变向量场, left-invariant vector field）**。设 $$X$$ 是 $$G$$ 上的光滑向量场（第 10 章：光滑映射 $$X:G\to TG$$ 满足 $$\pi\circ X=\mathrm{id}_G$$）。称 $$X$$ **左不变**，若对一切 $$g\in G$$

$$(L_g)_{*}X=X\circ L_g,\qquad\text{即}\qquad (dL_g)_h\bigl(X(h)\bigr)=X(gh)\quad(h\in G).$$

**定理 3.14（$$T_eG$$ 与左不变向量场一一对应）**。设 $$\mathfrak{X}_L(G)$$ 是 $$G$$ 上全体左不变向量场。映射

$$\Theta:\mathfrak{X}_L(G)\to T_eG,\qquad \Theta(X)=X(e)$$

是实向量空间的同构；逆映射是

$$\Psi:T_eG\to\mathfrak{X}_L(G),\qquad \Psi(v)=X^v,\qquad X^v(g):=(dL_g)_e\,v.$$

证明。(a) **$$X^v$$ 光滑**：先在坐标里把 $$(dL_g)_e$$ 具体写出来。取 $$G$$ 在 $$e$$ 附近与 $$g$$ 附近的坐标卡，乘法 $$\mu(g,h)=gh$$ 在这组坐标里是光滑函数 $$\mu(x,y)$$（$$x$$ 对应 $$g$$ 的坐标，$$y$$ 对应 $$h$$ 的坐标）；$$(dL_g)_h$$ 按定义就是 $$\mu(x,\cdot)$$ 只对第二个变量 $$y$$ 求偏导得到的 Jacobi 矩阵 $$\partial\mu/\partial y$$，在 $$y$$ 取 $$h$$ 的坐标处求值。由 $$\mu$$ 是 $$(x,y)$$ 的光滑函数，它对 $$y$$ 的每个偏导数 $$\partial\mu/\partial y_j$$ 仍是 $$(x,y)$$ 的光滑函数（光滑函数的偏导数还是光滑函数，这是光滑性定义本身的内容），故整个 Jacobi 矩阵 $$\partial\mu/\partial y(x,y)$$ 光滑依赖 $$(x,y)$$；取 $$y=e$$ 的坐标（一个固定点）代入，$$g\mapsto(dL_g)_e$$ 就是这个光滑矩阵函数固定第二组变量后关于 $$x$$（即 $$g$$）的光滑函数。把它与常向量 $$v$$ 复合（矩阵乘固定向量，是线性运算，不破坏光滑性）即得 $$g\mapsto X^v(g)=(dL_g)_ev$$ 光滑。

(b) **$$X^v$$ 左不变**：对 $$g,h\in G$$，用链式法则与 $$L_g\circ L_h=L_{gh}$$，

$$(dL_g)_h X^v(h)=(dL_g)_h (dL_h)_e v=d(L_g\circ L_h)_e\,v=(dL_{gh})_e\,v=X^v(gh).$$

(c) **$$\Theta\circ\Psi=\mathrm{id}$$**：$$L_e=\mathrm{id}_G$$，故 $$(dL_e)_e=\mathrm{id}_{T_eG}$$，于是 $$X^v(e)=v$$。

(d) **$$\Psi\circ\Theta=\mathrm{id}$$**：设 $$X$$ 左不变。在定义 3.13 里取 $$h=e$$：

$$X(g)=(dL_g)_e X(e)=X^{X(e)}(g),$$

两边对一切 $$g$$ 成立，故 $$X=X^{X(e)}$$。

由 (c)(d)，$$\Theta$$ 是双射，且 $$v\mapsto X^v$$ 与 $$X\mapsto X(e)$$ 都是线性的，故是同构。$$\blacksquare$$

这个定理是本章的枢纽：**群的非线性乘法通过左平移，把「单个点处的线性数据」无损地复制到全群**。没有群，切空间只活在一个点上；有了群，每个切空间都与 $$T_eG$$ 规范地同构，处处「一样」。这就是为什么 Lie 群的几何比一般流形好做。

**定义 3.15（向量场的 Lie 括号）**。第10章已把光滑向量场 $$X$$ 等同于 $$C^\infty(G)$$ 上的一阶求导算子：对 $$f\in C^\infty(G)$$、$$p\in G$$，

$$Xf(p):=df_p\bigl(X(p)\bigr)\qquad(\text{沿切向量 }X(p)\text{ 对 }f\text{ 求方向导数}),$$

这样定义出的 $$Xf$$ 是 $$G$$ 上的光滑函数，且 $$X$$ 满足 Leibniz 律 $$X(fh)=(Xf)h+f(Xh)$$（一阶方向导数对乘积求导的规则）。定理 3.20 的证明里会反复用到这个式子的一个特例：$$X^A(g)=gA$$ 时，$$X^Af(g)=\frac{d}{dt}\big\rvert_{t=0}f(g\exp(tA))$$，正是沿 $$X^A(g)=gA$$ 方向对 $$f$$ 求导的具体写法。两个求导算子 $$X,Y$$ 复合后一般不再是一阶算子（$$XYf$$ 里含 $$f$$ 的二阶导数项），但下面定义

$$[X,Y]f:=X(Yf)-Y(Xf),\qquad f\in C^\infty(G).$$

$$[X,Y]$$ 是 $$G$$ 上的光滑向量场（两个一阶算子之差仍是一阶，且两项的二阶导相消，这由 $$YX$$ 与 $$XY$$ 的二阶部分都是 $$YX$$ 的对称二阶导得出）。

**定理 3.16（左不变性在括号下守恒）**。若 $$X,Y$$ 都左不变，则 $$[X,Y]$$ 左不变。

证明。先证一条一般事实：**$$F$$-相关的向量场保括号**。设 $$F:M\to N$$ 光滑，$$X,X'$$ 满足 $$(dF)_pX(p)=X'(F(p))$$（即 $$X$$ 与 $$X'$$ 是 $$F$$-相关的），$$Y,Y'$$ 也 $$F$$-相关。则对任何 $$g\in C^\infty(N)$$，用「$$X$$ 与 $$X'$$ 相关 $$\iff X(g\circ F)=(X'g)\circ F$$」这一等价刻画：

$$[X,Y](g\circ F)=X\bigl(Y(g\circ F)\bigr)-Y\bigl(X(g\circ F)\bigr)=X\bigl((Y'g)\circ F\bigr)-Y\bigl((X'g)\circ F\bigr)$$

$$\quad=\bigl(X'Y'g\bigr)\circ F-\bigl(Y'X'g\bigr)\circ F=\bigl([X',Y']g\bigr)\circ F.$$

这就是 $$[X,Y]$$ 与 $$[X',Y']$$ $$F$$-相关的定义式。

现在取 $$F=L_g$$。定义 3.13 说的正是：$$X$$ 与 $$X$$ 自己 $$L_g$$-相关，$$Y$$ 与 $$Y$$ 自己也 $$L_g$$-相关。由上面的一般事实，$$[X,Y]$$ 与 $$[X,Y]$$ 自己 $$L_g$$-相关，即 $$(L_g)_*[X,Y]=[X,Y]\circ L_g$$——这正是左不变。$$\blacksquare$$

**定理 3.17（Jacobi 恒等式）**。对任意三个光滑向量场 $$X,Y,Z$$，

$$[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.$$

证明。两侧都是求导算子，只要在任意函数 $$f\in C^\infty(G)$$ 上验证。逐项展开：

$$[X,[Y,Z]]f=X(YZf-ZYf)-YZ(Xf)+ZY(Xf)=XYZf-XZYf-YZXf+ZYXf,$$

$$[Y,[Z,X]]f=Y(ZXf-XZf)-ZX(Yf)+XZ(Yf)=YZXf-YXZf-ZXYf+XZYf,$$

$$[Z,[X,Y]]f=Z(XYf-YXf)-XY(Zf)+YX(Zf)=ZXYf-ZYXf-XYZf+YXZf.$$

三式相加，六个正项 $$XYZf,ZYXf,YZXf,XZYf,ZXYf,YXZf$$ 与六个负项一一配对相消（$$XYZf$$ 与 $$-XYZf$$、$$XZYf$$ 与 $$-XZYf$$，以此类推），总和为 $$0$$。由于 $$f$$ 任意，算子恒等式成立。$$\blacksquare$$

**定义 3.18（Lie 代数, Lie algebra）**。实向量空间 $$\mathfrak{g}$$ 配上双线性映射 $$[\cdot,\cdot]:\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g}$$，若满足

(Lie1) 反交换：$$[X,X]=0$$（等价于 $$[X,Y]=-[Y,X]$$）；

(Lie2) Jacobi 恒等式：$$[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$$，

称 $$\mathfrak{g}$$ 是**Lie 代数 (Lie algebra)**。

**命题 3.19（$$T_eG$$ 上的括号使它成为 Lie 代数）**。定义

$$\mathfrak{g}:=\mathrm{Lie}(G)=T_eG,\qquad [v,w]:=[X^v,X^w](e).$$

则 $$\mathfrak{g}$$ 是 Lie 代数，$$\dim\mathfrak{g}=\dim G$$，称为 $$G$$ 的 **Lie 代数 (Lie algebra)**。

证明。**良定义与双线性**：由定理 3.14，$$v\mapsto X^v$$ 是线性同构；向量场括号在 $$X,Y$$ 上是双线性的，在 $$e$$ 处取值仍双线性。因此 $$[\cdot,\cdot]$$ 是良定义的双线性映射。

**反交换**：(Lie1) 直接由 $$[X,X]=XX-XX=0$$ 型的计算得到，在 $$e$$ 处取值后仍是 $$[v,v]=0$$。

**Jacobi**：定理 3.17 对任意三个向量场成立，取 $$X=X^u,\ Y=X^v,\ Z=X^w$$ 后在 $$e$$ 处取值，即得 $$[u,[v,w]]+[v,[w,u]]+[w,[u,v]]=0$$。

维数：$$e$$ 处的切空间维数就是流形维数（第 10 章），即 $$\dim G$$。$$\blacksquare$$

**定理 3.20（矩阵 Lie 群：括号就是换位子）**。设 $$G\subseteq GL(n,\mathbb{R})$$ 是闭子群。则 $$\mathfrak{g}=T_IG$$ 是 $$M_n(\mathbb{R})$$ 的子空间，且

$$[A,B]=AB-BA\qquad(A,B\in\mathfrak{g}).$$

证明。对矩阵群，$$L_g(h)=gh$$ 是左乘矩阵 $$g$$，其微分就是左乘 $$g$$：$$(dL_g)_h\xi=g\xi$$（$$\xi\in T_hG\subseteq M_n$$，因为 $$GL(n)$$ 是开集，各点切空间都自然地是 $$M_n$$）。于是定理 3.14 里的左不变向量场有极简形状

$$X^A(g)=(dL_g)_I A=gA,$$

即「右乘固定矩阵 $$A$$」。

现在算 $$[X^A,X^B](I)$$。取 $$f\in C^\infty(G)$$。曲线 $$t\mapsto g\exp(tA)$$ 是 $$X^A$$ 过 $$g$$ 的积分曲线，因为它的 $$t$$ 导数是 $$g\exp(tA)A$$（$$\exp$$ 的导数在 $$0$$ 处是 $$I$$），在 $$t=0$$ 处等于 $$gA$$。于是

$$X^Af(g)=\frac{d}{dt}\Big\rvert_{t=0}f\bigl(g\exp(tA)\bigr).$$

两级代入，在 $$e$$ 处

$$X^B(X^Af)(I)=\frac{\partial^2}{\partial s\,\partial t}\Big\rvert_{s=t=0}f\bigl(\exp(sB)\exp(tA)\bigr),$$

$$X^A(X^Bf)(I)=\frac{\partial^2}{\partial t\,\partial s}\Big\rvert_{t=s=0}f\bigl(\exp(tA)\exp(sB)\bigr).$$

把两组二阶展开写出来（$$\lVert(s,t)\rVert^3$$ 项以下略去）：

$$\exp(sB)\exp(tA)=I+sB+tA+st\,BA+O(\lVert(s,t)\rVert^3),$$

$$\exp(tA)\exp(sB)=I+tA+sB+st\,AB+O(\lVert(s,t)\rVert^3).$$

在 $$f$$ 上作用（$$f(I+u)\approx f(I)+Df_I(u)+\frac12D^2f_I(u,u)$$）。线性项 $$sB$$、$$tA$$ 只产生单变量项，在 $$\partial_s\partial_t$$ 下消失；二阶项里 $$D^2f$$ 的交叉项 $$\frac12\cdot2\,st\,D^2f(B,A)$$ 与 $$\frac12\cdot2\,st\,D^2f(A,B)$$ 相等（$$D^2f$$ 对称），于是两个二阶偏导分别是

$$Df_I(BA)+D^2f_I(B,A),\qquad Df_I(AB)+D^2f_I(B,A).$$

相减（注意 $$X^A(X^Bf)-X^B(X^Af)$$ 的次序），二阶项抵消，得

$$[X^A,X^B](I)f=Df_I(AB-BA),$$

这正是沿方向矩阵 $$AB-BA$$ 的求导。故 $$[X^A,X^B](I)=AB-BA$$，即 $$[A,B]=AB-BA$$。$$\blacksquare$$

**推论 3.20（三个具体 Lie 代数）**。

(i) $$\mathfrak{gl}(n,\mathbb{R})=M_n(\mathbb{R})$$，括号 $$[A,B]=AB-BA$$。

(ii) $$\mathfrak{so}(n)=\{A\in M_n:\ A^{\mathsf T}=-A\}$$（反对称矩阵）。**为什么**：把恒等式 $$R(t)^{\mathsf T}R(t)=I$$（$$R(t)\in SO(n)$$、$$R(0)=I$$）在 $$t=0$$ 处求导，得 $$A^{\mathsf T}I+I^{\mathsf T}A=0$$，即 $$A^{\mathsf T}+A=0$$。**括号封闭**：若 $$A,B$$ 反对称，则

$$[A,B]^{\mathsf T}=(AB-BA)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}-A^{\mathsf T}B^{\mathsf T}=(-B)(-A)-(-A)(-B)=BA-AB=-[A,B],$$

故 $$[A,B]$$ 仍反对称。维数：反对称矩阵由严格上三角的 $$n(n-1)/2$$ 个独立分量决定，与例 3.10 数出的 $$\dim SO(n)$$ 一致。

(iii) $$\mathfrak{u}(n)=\{A:\ A^{*}=-A\}$$（反厄米矩阵），$$\mathfrak{su}(n)=\{A\in\mathfrak{u}(n):\operatorname{tr}A=0\}$$。前者由 $$U(t)^{*}U(t)=I$$ 求导得；后者多出的无迹条件来自 $$\det U(t)=1$$，写成 $$\det(\exp(tA))=1$$ 后需要公式 $$\det(\exp X)=\exp(\operatorname{tr}X)$$，这个公式将在第 54 章证明，这里先借用结论。

(iv) $$\mathfrak{aff}(n)=\Bigl\{\begin{bmatrix}A&u\\ 0&0\end{bmatrix}:\ A\in M_n(\mathbb{R}),\ u\in\mathbb{R}^n\Bigr\}$$，维数 $$n^2+n$$，括号

$$\Bigl[\begin{bmatrix}A&u\\ 0&0\end{bmatrix},\begin{bmatrix}A'&u'\\ 0&0\end{bmatrix}\Bigr]=\begin{bmatrix}AA'-A'A & Au'-A'u\\ 0&0\end{bmatrix}.$$

直接从矩阵换位子算得：分块矩阵相乘只需记住右下角是 $$0$$，

$$\begin{bmatrix}A&u\\0&0\end{bmatrix}\begin{bmatrix}A'&u'\\0&0\end{bmatrix}=\begin{bmatrix}AA'&Au'\\0&0\end{bmatrix},\qquad\begin{bmatrix}A'&u'\\0&0\end{bmatrix}\begin{bmatrix}A&u\\0&0\end{bmatrix}=\begin{bmatrix}A'A&A'u\\0&0\end{bmatrix}$$

（每一步都只是分块矩阵乘法：左上角块是 $$A\cdot A'$$，右上角块是 $$A\cdot u'+u\cdot0=Au'$$，左下、右下两块因为右边矩阵的下方两块全是 $$0$$ 而自动为 $$0$$）。两式相减即得正文给出的换位子公式。注意 $$\mathfrak{aff}(n)$$ 里 $$A$$ 与 $$u$$ 都允许为零，故它既含平移方向也含线性方向。

### 3.5 指数映射：从 Lie 代数回到 Lie 群

第47章用幂零矩阵 $$E,F$$ 的例子说明了：给定一个"无穷小方向" $$A$$，$$I+tA$$（更一般地是 $$\sum_kt^kA^k/k!$$）沿这个方向匀速走了 $$t$$ 这么远。现在要把"匀速走"这件事从矩阵群搬到任意 Lie 群上：既然左不变向量场（命题 3.19）已经把 $$\mathfrak{g}=T_eG$$ 中的每个向量 $$v$$ 变成了一个"处处一致的速度场"，沿这个速度场从 $$e$$ 出发走出来的曲线，就应该正是我们想要的"匀速运动"。下面先证明这样的曲线一定是一个把加法变成群乘法的同态，再把 $$t=1$$ 处的取值定义为 $$\exp(v)$$。

**定义 3.21（单参数子群, one-parameter subgroup）**。$$G$$ 的**单参数子群**是光滑同态 $$c:(\mathbb{R},+)\to G$$，即光滑曲线满足

$$c(s+t)=c(s)c(t)\qquad\text{对一切 }s,t\in\mathbb{R}.$$

取 $$s=t=0$$ 得 $$c(0)=c(0)^2$$，故 $$c(0)=e$$。

**定理 3.22（单参数子群与 $$\mathfrak{g}$$ 一一对应）**。对每个 $$v\in\mathfrak{g}$$ 存在唯一单参数子群 $$c_v$$ 使 $$c_v'(0)=v$$；反之任一单参数子群 $$c$$ 的 $$c'(0)$$ 都落在 $$\mathfrak{g}$$ 中。

证明。**存在性**。取对应的左不变向量场 $$X^v$$（定理 3.14）。由常微分方程的基本定理，存在唯一极大积分曲线 $$\phi:(a,b)\to G$$ 满足 $$\phi'(t)=X^v(\phi(t))$$、$$\phi(0)=e$$。

先证极大区间是全部 $$\mathbb{R}$$。设 $$b<+\infty$$，记 $$g=\phi(b/2)$$。由 $$X^v$$ 左不变，曲线 $$t\mapsto g\,\phi(t)$$ 也是 $$X^v$$ 的积分曲线：

$$\frac{d}{dt}\bigl(g\phi(t)\bigr)=g\,\phi'(t)=g\,X^v(\phi(t))=X^v\bigl(g\phi(t)\bigr),$$

末一步正是左不变性。这两条曲线在 $$t=b/2$$ 处都过 $$g$$，由唯一性 $$g\phi(t)=\phi\bigl(b/2+t\bigr)$$。右边在 $$t$$ 可以取到 $$b/2$$（即原曲线的时刻 $$b$$ 之后的 $$b/2$$ 处）仍有定义，与 $$b$$ 是极大值矛盾。故 $$b=+\infty$$；同理 $$a=-\infty$$。

再证同态性。固定 $$s$$，两条曲线 $$t\mapsto\phi(s+t)$$ 与 $$t\mapsto\phi(s)\phi(t)$$ 都满足 $$X^v$$ 的积分方程（后者由上面同样的左不变性论证），且在 $$t=0$$ 处都等于 $$\phi(s)$$。由唯一性它们相等：

$$\phi(s+t)=\phi(s)\phi(t).$$

取 $$s=0$$ 得 $$\phi(0)=e$$（已是初值），故 $$\phi$$ 是单参数子群，且 $$\phi'(0)=X^v(e)=v$$。

**唯一性**。设 $$c$$ 是任一单参数子群。对固定 $$t$$，

$$c'(t)=\frac{d}{ds}\Big\rvert_{s=0}c(t+s)=\frac{d}{ds}\Big\rvert_{s=0}\bigl(c(t)c(s)\bigr)=(dL_{c(t)})_e\,c'(0)=X^{c'(0)}\bigl(c(t)\bigr).$$

故 $$c$$ 是 $$X^{c'(0)}$$ 的积分曲线，初值 $$c(0)=e$$。由 ODE 解的唯一性，$$c$$ 被 $$c'(0)$$ 完全决定。$$\blacksquare$$

**定义 3.23（指数映射, exponential map）**。定义

$$\exp:\mathfrak{g}\to G,\qquad \exp(v):=c_v(1),$$

其中 $$c_v$$ 是定理 3.22 给出的单参数子群。

**定理 3.24（$$\exp$$ 的基本性质）**。对 $$v\in\mathfrak{g}$$、$$s,t\in\mathbb{R}$$：

(i) $$c_v(t)=\exp(tv)$$，从而 $$\exp\bigl((s+t)v\bigr)=\exp(sv)\exp(tv)$$；

(ii) $$\exp(0)=e$$ 与 $$\exp(v)^{-1}=\exp(-v)$$；

(iii) $$\exp$$ 光滑，且 $$(d\exp)_0=\mathrm{id}_{\mathfrak{g}}$$；因此 $$\exp$$ 把 $$0$$ 的一个邻域微分同胚地映到 $$e$$ 的一个邻域；

(iv) **自然性**：若 $$\rho:G\to H$$ 是 Lie 群同态，则 $$\rho(\exp_G v)=\exp_H\bigl((d\rho)_e v\bigr)$$；

(v) **矩阵情形**：$$\exp(A)=\sum_{k\ge0}\dfrac{A^k}{k!}$$。

证明。

(i) 固定 $$v$$，考虑曲线 $$\gamma(t)=c_v(ts)$$。它过 $$e$$（$$\gamma(0)=c_v(0)=e$$），且是单参数子群：

$$\gamma(t_1+t_2)=c_v\bigl((t_1+t_2)s\bigr)=c_v(t_1s)c_v(t_2s)=\gamma(t_1)\gamma(t_2),$$

并且 $$\gamma'(0)=s\,c_v'(0)=sv$$。由定理 3.22 的唯一性，$$\gamma$$ 就是 $$c_{sv}$$；在 $$t=1$$ 处得 $$c_{sv}(1)=c_v(s)$$，即 $$\exp(sv)=c_v(s)$$。取 $$s=t$$ 得 $$c_v(t)=\exp(tv)$$。再由 $$c_v$$ 的同态性，$$\exp((s+t)v)=c_v(s+t)=c_v(s)c_v(t)=\exp(sv)\exp(tv)$$。

(ii) $$t=0$$ 入 (i) 得 $$\exp(0)=c_v(0)=e$$。又 $$e=c_v(0)=c_v(v-v)=c_v(v)c_v(-v)=\exp(v)\exp(-v)$$，故 $$\exp(-v)=\exp(v)^{-1}$$。

(iii) 光滑性：取 $$\mathfrak{g}$$ 的一组基 $$v_1,\dots,v_n$$，令 $$\Phi(x_1,\dots,x_n)=c_{x_1v_1+\cdots+x_nv_n}(1)$$。向量场 $$X^v$$ 线性且光滑地依赖 $$v$$，而 ODE 的解光滑依赖参数，故 $$\Phi$$ 光滑。对 $$v$$ 求方向导数：

$$(d\exp)_0(w)=\frac{d}{dt}\Big\rvert_{t=0}\exp(tw)=c_w'(0)=w,$$

故 $$(d\exp)_0=\mathrm{id}$$ 可逆；由反函数定理，$$\exp$$ 在 $$0$$ 附近是到 $$e$$ 附近邻域的微分同胚。

(iv) 记 $$C(t)=\rho\bigl(c^G_v(t)\bigr)$$。$$C$$ 是 $$H$$ 中的单参数子群，且 $$C'(0)=(d\rho)_e v$$。由定理 3.22 在 $$H$$ 中的唯一性，$$C(t)=c^H_{(d\rho)_e v}(t)$$；取 $$t=1$$ 即得 (iv)。

(v) 矩阵情形：$$\mathfrak{g}\subseteq M_n$$，左不变向量场是 $$X^A(g)=gA$$（定理 3.20 的证明里已算），故积分方程是 $$R'(t)=R(t)A$$、$$R(0)=I$$。幂级数 $$R(t)=\sum_{k\ge0}(tA)^k/k!$$ 逐项求导给出

$$R'(t)=\sum_{k\ge1}\frac{t^{k-1}A^k}{(k-1)!}=R(t)A,$$

故它是满足初值的积分曲线；由唯一性 $$c_A(t)=e^{tA}$$，于是 $$\exp(A)=c_A(1)=e^{A}=\sum_{k\ge0}\dfrac{A^k}{k!}$$。$$\blacksquare$$

**接口（入口题 (c) 的清算）**。第 02 章的定理 3.10 把 $$\theta\mapsto e^{i\theta}$$ 叫做「指数映射」，第 46 章把**同一个符号**用在 $$e^{-itH}$$ 上（那里的 $$H$$ 是无界自伴算子，$$\{e^{-itH}\}$$ 在 Stone 定理保证下构成单参数**算子**群）。两者都是定义 3.23 的特例：

- 取 $$G=U(1)\cong SO(2)$$、$$\mathfrak{g}=\mathfrak{u}(1)=i\mathbb{R}\cong\mathbb{R}$$，则 $$\exp(i\theta)=e^{i\theta}$$ 正是第 02 章的定理 3.10；由入口题 (c)，第 02 章那条具体曲线 $$R(\theta)$$ 就是 $$\exp(\theta J)$$，$$J=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$$。
- 取 $$G$$ 为 Hilbert 空间上的酉算子群、$$\mathfrak{g}$$ 为反自伴算子（第 42 章），则定理 3.24 的 (i)(ii)(iii) 逐字成立，这正是第 46 章算子半群那套 $$\exp(-tA)$$ 的语言。

于是「指数映射」在本课程里不再是一个记号，而是一个**自然**的操作：它把 Lie 代数沿单参数子群送到 Lie 群，并且与一切同态交换（(iv)）。第 54 章会把它的反函数（对数映射）和 BCH 公式补上。

### 3.6 Lie 群本身是一个主丛

到这里为止，本章一直把 Lie 群当成一个整体研究；但很多时候我们只关心群作用之后"剩下多少自由度"——例如 $$SO(3)$$ 里固定住一个方向之后，还剩下绕这个方向转动的自由度。把这类"整体 / 局部剩余自由度"的关系写成一般语言，就是主丛：底空间记录"已经固定住的部分"，纤维记录"还没固定的部分"，而局部截面保证这件事在坐标上是光滑可控的，不是病态的拓扑现象。

**定义 3.25（主丛, principal bundle）**。设 $$H$$ 是 Lie 群，$$P$$ 是光滑流形，$$H$$ 从右边光滑作用在 $$P$$ 上（$$(p,h)\mapsto p\cdot h$$），且作用**自由**（$$p\cdot h=p\Rightarrow h=e$$）。设 $$\pi:P\to B=P/H$$ 是商映射。若 $$\pi$$ 局部有光滑截面——即每个 $$b\in B$$ 有邻域 $$U$$ 与光滑 $$s:U\to P$$ 使 $$\pi\circ s=\mathrm{id}_U$$——则称 $$(P,B,\pi,H)$$ 是**主 $$H$$-丛 (principal $$H$$-bundle)**。此时 $$U\times H\to\pi^{-1}(U)$$、$$(b,h)\mapsto s(b)\cdot h$$ 是微分同胚，称为**局部平凡化**。

**定理 3.26（$$G\to G/H$$ 是主 $$H$$-丛）**。设 $$G$$ 是 Lie 群、$$H\subseteq G$$ 是闭子群。则 $$G/H$$ 有唯一的光滑流形结构使商映射 $$\pi:G\to G/H$$ 是淹没；$$H$$ 从右作用在 $$G$$ 上（$$g\cdot h=gh$$）自由，且 $$(G,G/H,\pi,H)$$ 是主 $$H$$-丛。

证明思路（关键是局部截面从哪里来）。记 $$\mathfrak{h}=\mathrm{Lie}(H)=T_eH\subseteq\mathfrak{g}$$。取 $$\mathfrak{h}$$ 在 $$\mathfrak{g}$$ 中的一个补空间 $$\mathfrak{m}$$，即线性直和 $$\mathfrak{g}=\mathfrak{h}\oplus\mathfrak{m}$$。定义

$$\Psi:\mathfrak{m}\times H\to G,\qquad \Psi(\xi,h)=\exp(\xi)\,h.$$

它在 $$(0,e)$$ 处的微分把 $$T_{(0,e)}(\mathfrak{m}\times H)=\mathfrak{m}\oplus\mathfrak{h}$$ 线性同构地送到 $$T_eG=\mathfrak{g}$$（$$\mathfrak{m}$$ 方向经 $$(d\exp)_0=\mathrm{id}$$ 落在 $$\mathfrak{m}$$，$$\mathfrak{h}$$ 方向经 $$h$$ 的乘法落在 $$\mathfrak{h}$$）。由反函数定理，$$\Psi$$ 在 $$(0,e)$$ 的一个邻域上是微分同胚。于是

$$s\bigl(\pi(\exp\xi)\bigr)=\exp\xi\qquad(\xi\in\mathfrak{m}\text{ 小})$$

是 $$\pi(e)$$ 附近的一个光滑截面。对任意 $$g_0\in G$$，用左平移 $$L_{g_0}$$ 把这张局部截面搬到 $$g_0$$ 附近（因为 $$\pi\circ L_{g_0}=L_{g_0}^{\text{商}}\circ\pi$$），得到整个 $$G/H$$ 上的局部截面族。

从这族局部截面立刻读出：$$\pi$$ 是淹没（局部是投影 $$\mathfrak{m}\times H\to\mathfrak{m}$$）；$$G/H$$ 有唯一的流形结构使其为淹没的商（由淹没的商结构唯一性）；$$H$$ 自由作用（$$gh=g\Rightarrow h=e$$，逆元存在）。局部平凡化就是上面的 $$\Psi$$。$$\blacksquare$$

**例 3.26（三个主丛）**。

(1) $$H=\{e\}$$：$$G\to G$$ 自身是以单点集为纤维的主丛（平凡）。

(2) $$G=SO(n)$$、$$H=SO(n-1)$$（固定第一个基向量的那些旋转）。$$SO(n)$$ 在 $$S^{n-1}$$ 上可迁地作用（任一单位向量可被旋转送到 $$e_1$$），稳定子正是 $$SO(n-1)$$，故 $$SO(n)/SO(n-1)\cong S^{n-1}$$。于是 $$SO(n)\to S^{n-1}$$ 是以 $$SO(n-1)$$ 为纤维的主丛。取 $$n=3$$ 得 $$SO(3)\to S^2$$，纤维 $$SO(2)\cong S^1$$。这就是第 25、26 章会反复使用的那一个丛：它给出 $$SO(3)$$ 的拓扑线索。

(3) $$G=SU(2)$$、$$H=T=\Bigl\{\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}\Bigr\}\cong U(1)$$（**极大环面**）。$$SU(2)/T\cong S^2$$，得到 Hopf 丛 $$S^3\to S^2$$，纤维 $$S^1$$。第 52 章用它解释自旋的双覆盖。

> **注（一个容易写错的地方）**：这里的 $$H$$ **不是** $$\{e^{i\theta}I\}$$——那个集合**不在** $$SU(2)$$ 里：$$\det(e^{i\theta}I)=e^{2i\theta}$$，只有 $$\theta\in\pi\mathbb Z$$ 时才等于 $$1$$。所以 $$\{e^{i\theta}I\}\cap SU(2)=\{\pm I\}$$ 是**离散**的，它是 $$SU(2)$$ 的**中心**，不是环面。而 $$\mathrm{diag}(e^{i\theta},e^{-i\theta})$$ 的行列式恒为 $$1$$，确实是 $$SU(2)$$ 的 $$1$$ 维连通闭子群。商 $$SU(2)/\{\pm I\}\cong SO(3)$$ 与商 $$SU(2)/T\cong S^2$$ 是**两个不同的商**，别混。

一般流形上要写一个 1-形式，必须先额外挑一个度量或一族坐标；但 Lie 群自带一种"把切向量搬回 $$\mathfrak{g}$$"的规范方式——用左平移的微分 $$(dL_{g^{-1}})_g$$ 把 $$T_gG$$ 中的任意切向量送回 $$T_eG=\mathfrak{g}$$（这正是定理 3.14 里 $$\Psi,\Theta$$ 那套对应关系的逆用）。把这件事在每一点都做一遍，就得到一个不需要任何额外数据、只用群结构本身就能写下的 1-形式。

**定义 3.27（Maurer–Cartan 形式, Maurer–Cartan form）**。定义 $$\mathfrak{g}$$-值 1-形式

$$\theta\in\Omega^1(G;\mathfrak{g}),\qquad \theta_g:=(dL_{g^{-1}})_g:T_gG\to\mathfrak{g}.$$

矩阵情形下写成 $$\theta=g^{-1}dg$$。由链式法则，$$L_h^{*}\theta=\theta$$：直接验证

$$(L_h^*\theta)_g=(dL_{(hg)^{-1}})_{hg}\circ(dL_h)_g=d\bigl(L_{(hg)^{-1}}\circ L_h\bigr)_g=d\bigl(L_{g^{-1}}\bigr)_g=\theta_g,$$

其中用了 $$(hg)^{-1}=g^{-1}h^{-1}$$ 与 $$L_{g^{-1}h^{-1}}\circ L_h=L_{g^{-1}h^{-1}h}=L_{g^{-1}}$$。所以 $$\theta$$ 是 $$G$$ 上一个**左不变的、典范的**$$\mathfrak{g}$$-值 1-形式，不需要任何外加数据就能写下。

**定理 3.28（Maurer–Cartan 方程）**。$$\theta$$ 满足

$$d\theta+\tfrac12[\theta\wedge\theta]=0,\qquad\text{其中}\quad [\theta\wedge\theta](X,Y)=[\theta(X),\theta(Y)]-[\theta(Y),\theta(X)].$$

矩阵情形即 $$d\theta+\theta\wedge\theta=0$$。

证明（矩阵情形最直观，且已含全部思想）。设 $$G\subseteq GL(n)$$，$$\theta=g^{-1}dg$$。对 $$gg^{-1}=I$$ 两边取外微分（第 24 章）：$$dg\,g^{-1}+g\,d(g^{-1})=0$$，故

$$d(g^{-1})=-g^{-1}\,dg\,g^{-1}.$$

于是

$$d\theta=d(g^{-1})\wedge dg=-\bigl(g^{-1}dg\,g^{-1}\bigr)\wedge dg=-\bigl(g^{-1}dg\bigr)\wedge\bigl(g^{-1}dg\bigr)=-\theta\wedge\theta,$$

第二步用了 $$g^{-1}$$ 是纯矩阵、与 $$dg$$ 的楔积可自由调整次序，第三步把中间的 $$g^{-1}dg$$ 重新配对。故 $$d\theta+\theta\wedge\theta=0$$。对一般的 Lie 群，把矩阵楔积替换成「先取值再取括号」的 $$[\theta\wedge\theta]$$，同样的计算给出 $$d\theta+\frac12[\theta\wedge\theta]=0$$（矩阵情形 $$[\theta\wedge\theta]=2\theta\wedge\theta$$，两者一致）。$$\blacksquare$$

**接口**：$$\theta$$ 是「$$G$$ 上免费的、左不变的 $$\mathfrak{g}$$-值 1-形式」——与第 12 章 3.6 节「余切丛上有一个免费的 1-形式（辛势）$$\sum p_i\,dx^i$$」是同一现象的两个版本：底空间上带了额外结构（那里是余切丛的丛结构，这里是群结构），就自动冒出一个典范形式。而 Maurer–Cartan 方程 $$d\theta+\frac12[\theta\wedge\theta]=0$$ 就是第 26 章 Stokes 定理在 $$G$$ 上的微分形式版本：对它做路径积分（取路径有序指数）就得到第 46 章路径积分里 $$e^{iS}$$ 的群论母体。至此，卷一（流形、纤维丛）、卷二（外微分、Stokes）、卷三（指数、半群）三条线在 Lie 群上接成一个点。

## 四、几何与物理直觉 (Intuition)

**几何侧：点、箭头与「谁有原点」。** 平面几何里我们同时用两种东西：**点**（位置）与**箭头**（位移）。画图时它们看起来不一样——箭头可以平移到任何地方再画，点不能。这个直觉的代数版本就是定义 3.1：位移构成向量空间，位置构成它的主齐性空间。主齐性空间与向量空间的差别只有一条：**有没有一个被选中的点 $$0$$**。所以「$$A$$ 是仿射空间」不是「$$A$$ 很差」，而是「$$A$$ 上多做一件事就变成向量空间，但那件事（选原点）不是典范的」。物理里满天飞的都是这种「差一件典范选择」的量：温度、电势、势能、原函数、位形空间里的位置。

**群侧：$$e$$ 是一个被选中的点。** 仿射空间里没有特殊的点，Lie 群里却有：单位元 $$e$$。这一条差别极大。因为 $$e$$ 特殊，$$T_eG$$ 才特殊；因为群运算能把这个「特殊」搬运到每一个点（左平移），$$\mathfrak{g}=T_eG$$ 才与每个 $$T_gG$$ 规范同构。于是 Lie 群上有一种别处没有的现象：**你在 $$e$$ 处算出的任何线性数据，都可以无损地搬到全群**。定理 3.14 说的就是这件事，它是整个 Lie 群理论的技术心脏。反过来说，仿射空间之所以难做微积分，正因为没有一个被选中的点来固定「该在哪儿求导」。

**左不变向量场的物理读法。** 把 $$X^v$$ 想成「全场到处都是的同一个速度」。在惯性系里，一个不受力的质点在每个时刻速度相同——如果你把这条速度的「方向 + 大小」视为无穷小位移 $$v$$，那么「把它搬运到任意时刻任意位置」得到的正是左不变向量场。这不是比喻：对 $$G=(\mathbb{R},+)$$（时间轴），左不变向量场就是常向量场 $$\partial_t$$，而它的积分曲线就是匀速直线运动。所以「左不变」= 「不随位置改变的匀速」；定理 3.22（单参数子群的存在唯一）就是「给定初速度，匀速运动存在且唯一」。

**指数映射的物理读法。** $$e^{tX}$$ 这个符号在本课程出现过两次：第 02 章的 $$e^{i\theta}$$（绕着圆周匀速转）与第 46 章的 $$e^{-itH}$$（量子态随时间演化）。定义 3.23 说它们是同一个操作——**给定一个「无穷小速度」$$X$$，沿着它匀速走单位时间**。区别只在于「走」这件事发生在哪个空间里：圆周、Hilbert 空间上的酉群、或矩阵群。定理 3.24(iv)（自然性）保证这个操作与一切同态相容，所以换一个空间来算结果不变。第 54 章会补上反操作（对数），并给出 BCH 公式——「群上先乘后取对数」与「代数上先取对数再相加」差一个括号项，这个差项就是群不交换的全部理由。

**主丛的物理读法。** $$G\to G/H$$ 这个主丛的几何含义是「把群按子群做商」。物理上，最常出现的形状是 $$SO(n)\to S^{n-1}$$：底空间是「方向的集合」，纤维是「绕这个方向转动的自由度」。**这正是参考系的概念**：指定一个方向（在底空间选一点），还剩下绕这个方向的自转没有定（纤维上的运动）。规范场论的整套语言就是把这种「底空间选定后还有纤维自由度」的结构丛化，然后再给纤维加一个「联络」（比较相邻两点纤维的方式）。定义 3.27 的 Maurer–Cartan 形式 $$\theta=g^{-1}dg$$ 就是这套语言在群本身上的原型：它不依赖任何外加选择，自动地告诉你「从 $$g$$ 走到 $$g+dg$$ 时，纤维怎么转」。

**代数侧：为什么求导给出的是「代数」。** 一个群只讲乘法；加上流形结构后才能求导；而在 $$e$$ 处求导得到的 $$T_eG$$ 本身只是一个向量空间——**还不能算代数**。真正多出来的那件东西是**括号**，它来自「两条曲线的二阶交互」（定理 3.20 的证明把这件事算得清清楚楚：括号是 $$AB-BA$$，而 $$AB-BA$$ 恰好是两条指数曲线差到二阶的系数）。所以本章标题里的三个词对应三件递进的事：**仿射空间**给「点与向量之别」，**变换群**给「运算能复合」，**Lie 群**把二者与光滑性缝在一起，最后**求导**在恒等元处留下一个带括号的向量空间。这条链在物理上的终点是守恒律：连续对称性 $$\Leftrightarrow$$ 单参数子群 $$\Leftrightarrow$$ 李代数中的元素 $$\Leftrightarrow$$ 守恒量。第 54 章会把它写成定理。

**三者的对应表**（本课程的主线）：

| 几何 | 物理 | 代数 |
|---|---|---|
| 仿射空间 $$A$$ | 位形/绝对量（温度、电势、位置） | 主齐性空间，作用在 $$V$$ 上 |
| 自由向量空间 $$V$$ | 位移/相对量（温差、电势差） | 加法群；$$T(A)\cong V$$ |
| 平移变换群 | 「加一个位移」 | 加群，交换 |
| 仿射群 $$\mathrm{Aff}(n)$$ | 匀速运动 + 伸缩 | $$GL(n)\ltimes\mathbb{R}^n$$，可解 |
| Lie 群 $$G$$ | 连续对称构成的族 | 群 + 流形 |
| 左不变向量场 | 全场一致的「匀速」 | $$\mathfrak{g}=T_eG$$ |
| 单参数子群/$$\exp$$ | 匀速演化 $$e^{tX}$$ | $$\mathfrak{g}\to G$$，局部同构 |
| 主丛 $$G\to G/H$$ | 参考系：方向 + 剩余自转 | 商群、齐性空间 |
| Maurer–Cartan 形式 $$\theta$$ | 「无外加约定的联络」 | $$\mathfrak{g}$$-值 1-形式，$$d\theta+\frac12[\theta\wedge\theta]=0$$ |

## 五、经典问题精讲 (Classical Problems)

### 题 1：$$SO(2)$$ 上的一条光滑曲线（入口题 (c) 的清算）

**考点**：群结构与流形结构如何一起约束曲线；位置：3.4–3.5 节的直接应用，也是第 02 章定理 3.10 的升级版。

设 $$t\mapsto R(t)\in SO(2)$$ 光滑、$$R(0)=I$$。

(i) 证明 $$R'(0)$$ 反对称；

(ii) 记 $$\omega(t)=R(t)^{-1}R'(t)$$。证明 $$\omega(t)$$ 恒等于常矩阵 $$A$$ 当且仅当 $$R(t)=\exp(tA)$$；

(iii) 由此证明第 02 章定理 3.10 的 $$\theta\mapsto R(\theta)$$ 就是 $$\exp(\theta J)$$，$$J=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$$。

**解**。(i) 对恒等式 $$R(t)^{\mathsf T}R(t)=I$$ 两边在 $$t$$ 求导（左边是乘积，用乘法法则）：

$$R'(t)^{\mathsf T}R(t)+R(t)^{\mathsf T}R'(t)=0.$$

在 $$t=0$$ 代入 $$R(0)=R(0)^{\mathsf T}=I$$：$$R'(0)^{\mathsf T}+R'(0)=0$$，即 $$R'(0)^{\mathsf T}=-R'(0)$$，$$R'(0)$$ 反对称。

(ii) $$(\Longleftarrow)$$ 设 $$R(t)=\exp(tA)$$。$$A$$ 与 $$\exp(tA)$$ 交换（因为 $$A$$ 与 $$A$$ 的每个幂 $$(tA)^k$$ 交换，幂级数逐项亦然），故

$$\omega(t)=\exp(-tA)\cdot\frac{d}{dt}\exp(tA)=\exp(-tA)\cdot A\exp(tA)=A,$$

末一步用交换性。

$$(\Longrightarrow)$$ 设 $$\omega(t)\equiv A$$，即 $$R'(t)=R(t)A$$，且 $$R(0)=I$$。这正是定理 3.24(v) 的证明中出现过的初值问题 $$R'=RA$$、$$R(0)=I$$，其唯一解是 $$R(t)=\exp(tA)$$。故 $$R(t)=\exp(tA)$$。

(iii) 取 $$A=\theta J$$。$$J^2=-I$$，故 $$J^{2m}=(-1)^mI$$、$$J^{2m+1}=(-1)^mJ$$，幂级数分成两支：

$$\exp(\theta J)=\sum_{m\ge0}\frac{\theta^{2m}}{(2m)!}J^{2m}+\sum_{m\ge0}\frac{\theta^{2m+1}}{(2m+1)!}J^{2m+1}=\Bigl(\sum_{m\ge0}\frac{(-1)^m\theta^{2m}}{(2m)!}\Bigr)I+\Bigl(\sum_{m\ge0}\frac{(-1)^m\theta^{2m+1}}{(2m+1)!}\Bigr)J.$$

两个级数分别是 $$\cos\theta$$ 与 $$\sin\theta$$，故

$$\exp(\theta J)=(\cos\theta)I+(\sin\theta)J=\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}=R(\theta).$$

这就是第 02 章那一族矩阵。$$\blacksquare$$

**这道题的 leap**：把「$$SO(2)$$ 是一族光滑矩阵」这一个事实，加上「它是群」这一个事实，用 $$\omega(t)$$ 这个量串起来。注意 (ii) 的 $$(\Longrightarrow)$$ 方向完全来自 ODE 唯一性——这就是定理 3.22 在 $$SO(2)$$ 上的化身。

### 题 2：$$\mathrm{Aff}(n)=\mathrm{GL}(n)\ltimes\mathbb{R}^n$$ 是半直积，但不是直积

**考点**：正规子群、商群、第一同构定理；位置：3.2 节。

记 $$N=\{(I,b):b\in\mathbb{R}^n\}\subseteq\mathrm{Aff}(n)$$，$$L=\{(M,0):M\in GL(n,\mathbb{R})\}$$。

(i) 证明 $$N\trianglelefteq\mathrm{Aff}(n)$$ 且 $$N\cong(\mathbb{R}^n,+)$$；

(ii) 证明 $$\mathrm{Aff}(n)/N\cong GL(n,\mathbb{R})$$；

(iii) 证明 $$\mathrm{Aff}(n)$$ 是半直积 $$N\rtimes L$$，但当 $$n\ge1$$ 时它不是直积。

**解**。(i) 先算乘法与逆（定理 3.7 的证明里已有）：$$(M,b)(M',b')=(MM',\,Mb'+b)$$，$$(M,b)^{-1}=(M^{-1},\,-M^{-1}b)$$。于是

$$(I,b)(I,c)=(I,b+c),\qquad (I,b)^{-1}=(I,-b),$$

故 $$N$$ 是子群，且 $$b\mapsto(I,b)$$ 是到 $$(\mathbb{R}^n,+)$$ 的同构。

正规性：算共轭

$$(M,c)^{-1}(I,b)(M,c)=(M^{-1},-M^{-1}c)(I,b)(M,c)=\bigl(M^{-1},\ M^{-1}b-M^{-1}c\bigr)(M,c).$$

再乘一步，第二分量是 $$M^{-1}c+M^{-1}(b-c)=M^{-1}b$$，故

$$(M,c)^{-1}(I,b)(M,c)=(I,\ M^{-1}b)\in N.$$

既然 $$M,c$$ 任意，任意元素共轭 $$N$$ 中元素都落在 $$N$$ 里，$$N$$ 正规。

(ii) 映射 $$\pi:\mathrm{Aff}(n)\to GL(n,\mathbb{R})$$、$$\pi(M,b)=M$$ 是满同态（由乘法式，$$(MM',Mb'+b)\mapsto MM'$$），核正是 $$N$$。第一同构定理给出 $$\mathrm{Aff}(n)/N\cong GL(n,\mathbb{R})$$。

(iii) 半直积：$$N$$ 正规、$$N\cap L=\{I\}$$（取交集 $$(M,b)=(I,0)$$ 得 $$M=I,b=0$$），且每个元素 $$(M,b)=(I,b)(M,0)$$ 是 $$N\cdot L$$ 中的元素，故 $$\mathrm{Aff}(n)=N\cdot L=N\rtimes L$$。

不是直积：直积要求 $$L$$ 也正规。算 $$L$$ 中元素被 $$(I,b)\in N$$ 共轭：

$$(I,b)^{-1}(M,0)(I,b)=(I,-b)(M,0)(I,b)=(M,-b)(I,b)=(M,\ Mb-b).$$

这落在 $$L$$（即第二分量为 $$0$$）当且仅当 $$Mb=b$$。取 $$M=2I$$、$$b=e_1$$（$$n\ge1$$）得 $$2e_1\neq e_1$$，故该共轭不在 $$L$$ 中，$$L$$ 不正规，不是直积。$$\blacksquare$$

**这道题的 leap**：注意 (iii) 里真正要证的不是「不分裂」（它确实分裂），而是「补空间不正规」。半直积与直积的差别只在这一点上。

### 题 3：温度构成仿射空间

**考点**：定义 3.1 的公理如何对应物理；位置：3.1 节。

设 $$A$$ 是「温度」的集合，取绝对温标使之与 $$\mathbb{R}$$ 一一对应；设 $$V=\mathbb{R}$$ 是「温差」的集合，作用取

$$(\text{温度 }T)+(\text{温差 }\Delta)=T+\Delta\quad(\text{数值相加}).$$

(i) 逐条验证 (A1)(A2)(A3)，从而 $$A$$ 是仿射空间；

(ii) 解释为什么在 $$A$$ 上定义「点加点」会失败，并算清「$$20\,^\circ\mathrm{C}+30\,^\circ\mathrm{C}$$」的两种读法给出什么；

(iii) 说明「势能可以任意选零点」「不定积分要加常数 $$C$$」是同一件事。

**解**。(i) 把温度记成开尔文的实数 $$T$$。$$A=V=\mathbb{R}$$，运算就是实数加法。

(A1) $$T+0=T$$：加零温差温度不变。✓

(A2) $$(T+\Delta_1)+\Delta_2=T+(\Delta_1+\Delta_2)$$：实数加法结合律。✓

(A3) 给定两温度 $$T_1,T_2$$，唯一的温差是 $$\Delta=T_2-T_1\in\mathbb{R}$$，因为 $$T_1+\Delta=T_2$$ 是实数的唯一解。✓

故 $$A$$ 是 1 维仿射空间，$$V$$ 是它的自由向量空间。注意这里 $$A$$ 与 $$V$$ 作为集合都是 $$\mathbb{R}$$，区分它们的是**作用**而不是集合：$$V$$ 作用在 $$A$$ 上，反之不然。

(ii) 若在 $$A$$ 上定义一个「$$\oplus$$」，希望它就是普通的实数加法，那么结果依赖「$$20\,^\circ\mathrm{C}$$ 和 $$30\,^\circ\mathrm{C}$$ 各按什么读」：

- 若把两个都读成**温度**（绝对量 $$293.15$$ 与 $$303.15$$）再相加，得 $$596.3\,\mathrm{K}$$，即 $$323.15\,^\circ\mathrm{C}$$；
- 若把第二个读成**温差**（$$30\,\mathrm{K}$$）再作用，得 $$293.15+30=323.15\,\mathrm{K}$$，即 $$50\,^\circ\mathrm{C}$$。

两个答案不同，所以「$$+$$」不是良定义的。更本质的理由：任何「点加点」的式子都会用到某个选定的原点 $$o$$（例如绝对零度，或 Celsius 冰点 $$273.15\,\mathrm{K}$$），写成 $$T_1\oplus T_2:=T_1+T_2-o$$；换了原点 $$o'=o+w$$ 之后，新值比旧值少 $$w$$，结果随人为选择而变。这正是定理 3.3 说「$$A$$ 上无内蕴原点」的内容。

(iii) 势能：选定零点的操作就是选原点 $$o$$；换了零点，所有势能值同时平移一个常数，而**差**不变。这正是「只有势能差有物理意义」。不定积分：$$F$$ 与 $$F+C$$ 都是 $$f$$ 的原函数，全体原函数构成仿射空间，自由向量空间是「常数的全体」。所以 $$\int f\,dx=F+C$$ 里那个 $$C$$ 不是记号的疏忽，而是「求差问题」的必然产物。$$\blacksquare$$

**这道题的 leap**：把「温度/温差」这对日常词，翻译成「$$A$$ / $$V$$」这对代数对象。一旦翻译过来，「为什么不能加温度」就不再是物理常识而是一条定理。

### 题 4：Galileo 群的 Lie 代数

**考点**：把具体变换群写成微分算子并算括号；位置：3.2 例 3.7 + 3.4 节。

在 $$\mathbb{R}^4$$ 的坐标 $$(x_1,x_2,x_3,t)$$ 上取六个向量场（$$i=1,2,3$$，指标按 $$1\to2\to3\to1$$ 循环求和）

$$P_i=\partial_{x_i},\qquad H=\partial_t,\qquad K_i=-t\,\partial_{x_i},$$

$$J_1=x_3\partial_{x_2}-x_2\partial_{x_3},\quad J_2=x_1\partial_{x_3}-x_3\partial_{x_1},\quad J_3=x_2\partial_{x_1}-x_1\partial_{x_2}.$$

(i) 证明 $$[J_i,J_j]=\varepsilon_{ijk}J_k$$；

(ii) 证明 $$[J_i,K_j]=\varepsilon_{ijk}K_k$$ 与 $$[K_i,H]=P_i$$；

(iii) 证明 $$[K_i,K_j]=0$$、$$[K_i,P_j]=0$$，并说明为什么这个 10 维 Lie 代数既不可解也不半单。

**解**。(i) 以 $$[J_1,J_2]=J_3$$ 为例（其余由循环对称）。逐项算：

$$[x_3\partial_{x_2},\,x_1\partial_{x_3}]=x_3\partial_{x_2}(x_1\partial_{x_3})-x_1\partial_{x_3}(x_3\partial_{x_2})=0-x_1\partial_{x_2}=-x_1\partial_{x_2},$$

（第一项：$$\partial_{x_2}x_1=0$$；第二项：$$\partial_{x_3}x_3=1$$ 抽出 $$\partial_{x_2}$$，剩下 $$x_3\partial_{x_3}\partial_{x_2}$$ 与第一项的同型项相消。）

$$[x_3\partial_{x_2},\,-x_3\partial_{x_1}]=-x_3\partial_{x_2}(x_3\partial_{x_1})+x_3\partial_{x_1}(x_3\partial_{x_2})=0+0=0,$$

（两次都只出现 $$\partial_{x_2}x_3=0$$ 与 $$\partial_{x_1}x_3=0$$。）

$$[-x_2\partial_{x_3},\,x_1\partial_{x_3}]=0,\qquad[-x_2\partial_{x_3},\,-x_3\partial_{x_1}]=x_2\partial_{x_1}-0=x_2\partial_{x_1}.$$

（末项：$$x_2\partial_{x_3}(x_3\partial_{x_1})=x_2\partial_{x_1}+x_2x_3\partial_{x_3}\partial_{x_1}$$，$$x_3\partial_{x_1}(x_2\partial_{x_3})=x_2x_3\partial_{x_1}\partial_{x_3}$$，二者相消后剩 $$x_2\partial_{x_1}$$。）四项相加得

$$[J_1,J_2]=-x_1\partial_{x_2}+x_2\partial_{x_1}=J_3.$$

(ii) 先算 $$[J_3,K_1]=K_2$$（即 $$\varepsilon_{312}=1$$）。用 $$K_1=-t\partial_{x_1}$$、$$K_2=-t\partial_{x_2}$$：

$$[x_2\partial_{x_1},\,-t\partial_{x_1}]=-x_2t\partial_{x_1}^2+tx_2\partial_{x_1}^2=0,$$

（两项都等于 $$-x_2t\partial_{x_1}^2$$，因为 $$\partial_{x_1}t=0$$ 与 $$\partial_{x_1}x_2=0$$。）

$$[x_1\partial_{x_2},\,-t\partial_{x_1}]=-x_1t\partial_{x_2}\partial_{x_1}+t\bigl(\partial_{x_1}x_1\bigr)\partial_{x_2}+tx_1\partial_{x_1}\partial_{x_2}=t\partial_{x_2},$$

（中间那一项 $$\partial_{x_1}x_1=1$$ 留下 $$t\partial_{x_2}$$，两边含二阶导的项相消。）故 $$[J_3,K_1]=0-t\partial_{x_2}=K_2$$。其余指标由循环对称同理。

再算 $$[K_i,H]=\bigl[-t\partial_{x_i},\partial_t\bigr]$$：

$$(-t\partial_{x_i})(\partial_t f)=-t\,f_{x_i t},\qquad \partial_t(-t\partial_{x_i}f)=-\partial_{x_i}f-t\,f_{x_i t},$$

相减得 $$-t f_{x_i t}+f_{x_i}+t f_{x_i t}=f_{x_i}$$，即 $$\bigl[-t\partial_{x_i},\partial_t\bigr]=\partial_{x_i}=P_i$$。

(iii) $$[K_i,K_j]=[-t\partial_{x_i},-t\partial_{x_j}]=t^2\partial_{x_i}\partial_{x_j}-t^2\partial_{x_j}\partial_{x_i}=0$$（混合偏导相等）。$$[K_i,P_j]=[-t\partial_{x_i},\partial_{x_j}]=0$$（$$\partial_{x_i}$$ 与 $$\partial_{x_j}$$ 交换且 $$\partial_{x_j}t=0$$）。

**既不可解也不半单**：记这个 10 维 Lie 代为 $$\mathfrak{gal}$$。由 (ii)，$$[K_i,H]=P_i$$，故 $$[\mathfrak{gal},\mathfrak{gal}]$$ 含全部 $$P_i$$、全部 $$K_i$$（由 $$[J,K]=K$$）与全部 $$J_i$$（由 $$[J,J]=J$$），而 $$H$$ 不在其中（任何括号的第二变元是 $$H$$ 时结果都是 $$P_i$$ 或 $$0$$）。于是

$$\mathfrak{gal}^{(1)}=[\mathfrak{gal},\mathfrak{gal}]=\mathrm{span}\{J_i,K_i,P_i\},$$

而再取一次括号仍在同一个空间里（$$[J,J]=J$$、$$[J,K]=K$$、$$[J,P]=P$$、$$[K,\cdot]=0$$ 或 $$P$$），故导出列 $$\mathfrak{gal}^{(m)}=\mathrm{span}\{J_i,K_i,P_i\}\neq0$$ 对一切 $$m\ge1$$ 成立——**不可解**。

半单性：$$\mathfrak{a}=\mathrm{span}\{P_1,P_2,P_3,H\}$$ 是交换子代数（$$[P_i,P_j]=[P_i,H]=0$$），且由 (ii) 对任意 $$Y$$ 有 $$[Y,\mathfrak{a}]\subseteq\mathfrak{a}$$（$$[K,H]=P\in\mathfrak{a}$$、$$[J,P]\in\mathfrak{a}$$、$$[K,P]=0$$、$$[J,H]=0$$），故 $$\mathfrak{a}$$ 是交换理想，非零。半单要求没有非零可解理想，故 $$\mathfrak{gal}$$ **不半单**。$$\blacksquare$$

**这道题的 leap**：把抽象的 Lie 群元素翻译成微分算子 $$-t\partial_{x}$$。一旦写成算子，括号就是普通的算子交换子，全部计算变成偏导数的机械核对；而那些「零」的地方（$$[K_i,K_j]=0$$）恰恰暴露了 Galileo 群的物理特殊性（不同方向的匀速运动互相交换），这些零是后面量子力学里「质量作为中心荷」出现的位置。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 判断下列集合在给定运算下是否为 Lie 群（若是，说出维数；若不是，给出理由）：

(i) $$\mathbb{R}$$，运算为加法；

(ii) $$\mathbb{Q}$$，运算为加法（取 $$\mathbb{R}$$ 的子空间拓扑）；

(iii) $$S^1=\{z\in\mathbb{C}:\lvert z\rvert=1\}$$，运算为复数乘法；

(iv) $$\{\pm1\}$$，运算为乘法；

(v) $$n\times n$$ 实矩阵全体 $$M_n(\mathbb{R})$$，运算为矩阵加法。

**基2.** 写出 $$\mathfrak{aff}(1)$$（平面仿射群 $$\mathrm{Aff}(1)$$ 的 Lie 代数）的一组基 $$E,T$$，并计算 $$[E,T]$$。再求 $$\dim\mathrm{Aff}(1)$$。

**基3.** 对 $$G=GL(n,\mathbb{R})$$ 验证定理 3.14：写出 $$v\in T_IG$$ 对应的左不变向量场 $$X^v$$ 的显式表达式，并直接验证它左不变。

### 竞赛（本课目标难度）

**竞1.** 证明 $$GL(n,\mathbb{C})$$（$$n\ge1$$）是连通 Lie 群，而 $$GL(n,\mathbb{R})$$ 恰有两个连通分支，并指出这两个分支分别是什么。

**竞2.** 设 $$\rho:G\to H$$ 与 $$\psi:G\to H$$ 是 Lie 群同态，$$G$$ **连通**。证明：若 $$(d\rho)_e=(d\psi)_e$$，则 $$\rho=\psi$$。（即连通 Lie 群的同态由它在恒等元的微分唯一决定。）

**竞3.** 设 $$\sigma_1,\sigma_2,\sigma_3$$ 是 Pauli 矩阵

$$\sigma_1=\begin{bmatrix}0&1\\1&0\end{bmatrix},\quad \sigma_2=\begin{bmatrix}0&-i\\ i&0\end{bmatrix},\quad \sigma_3=\begin{bmatrix}1&0\\ 0&-1\end{bmatrix}.$$

证明 $$\mathfrak{su}(2)=\{A\in M_2(\mathbb{C}):A^{*}=-A,\ \operatorname{tr}A=0\}$$（$$\mathfrak{su}(2)$$ 是 $$SU(2)$$ 的 Lie 代数），求出它的实维数，并把

$$X_k=-\frac{i}{2}\sigma_k\qquad(k=1,2,3)$$

取作一组基，计算 $$[X_1,X_2]$$。

**竞4.** (i) 证明定义 3.27 的 Maurer–Cartan 形式 $$\theta$$ 满足 $$L_h^{*}\theta=\theta$$；

(ii) 对 $$G=SO(2)$$，在坐标 $$\varphi$$ 下（$$R(\varphi)=\cos\varphi\,I+\sin\varphi\,J$$、$$J=\begin{bmatrix}0&-1\\1&0\end{bmatrix}$$）证明 $$\theta=J\,d\varphi$$，并由此验证 $$d\theta=0$$。

### 研究（通向下一章）

**研1.** 设 $$G$$ 是连通的**矩阵** Lie 群，$$\mathfrak{g}$$ 是它的 Lie 代数。证明：$$G$$ 是阿贝尔群当且仅当 $$\mathfrak{g}$$ 是阿贝尔 Lie 代数（即 $$[\cdot,\cdot]\equiv0$$）。

**研2.** 证明 $$\mathfrak{su}(2)\cong\mathfrak{so}(3)$$ 作为 Lie 代数，但 $$SU(2)$$ 与 $$SO(3)$$ **不同构**；具体地，用伴随作用造出满同态 $$SU(2)\to SO(3)$$、证明其核是 $$\{\pm I\}$$，从而 $$SU(2)\to SO(3)$$ 是二重覆盖（以 $$\mathbb{Z}/2$$ 为结构群的主丛）。

### 解答 (Solutions)

**解 基1.**

(i) **是**。加法 $$\mu(x,y)=x+y$$ 与求逆 $$\iota(x)=-x$$ 都是 $$\mathbb{R}^2\to\mathbb{R}$$ 的光滑函数，$$\mathbb{R}$$ 是 1 维流形。故 $$(\mathbb{R},+)$$ 是 1 维 Lie 群。

(ii) **不是**。要成为 $$n$$ 维 Lie 群，它必须局部同胚于 $$\mathbb{R}^n$$。而 $$\mathbb{Q}$$ 在子空间拓扑下是**完全不连通**的：对任意 $$q\in\mathbb{Q}$$，取无理数 $$\alpha>0$$，则 $$\mathbb{Q}\cap(q-\alpha,q+\alpha)$$ 与 $$\mathbb{Q}\cap(q-\alpha,q+\alpha)^{c}$$ 把 $$q$$ 的每个邻域劈成两个非空开集，故 $$q$$ 的任一邻域都不连通。连通的开集只有一个点，它不可能局部同胚于 $$\mathbb{R}^n$$。所以 $$(\mathbb{Q},+)$$ 是群、是拓扑群，但**不是 Lie 群**——这正好说明定义 3.9 里 (L2) 是一条真条件。

(iii) **是**。由定理 3.11，$$S^1\cong SO(2)$$，是 1 维紧 Lie 群。（也可直接给图册：$$z\mapsto\arg z$$，两张卡覆盖。）

(iv) **是**。它是 0 维 Lie 群：$$\{\pm1\}$$ 配离散拓扑，每点是 $$\mathbb{R}^0$$ 的一个邻域；乘法表有限，光滑性是空条件。

(v) **是**。矩阵加法就是 $$\mathbb{R}^{n^2}$$ 上的向量加法，$$\mu(A,B)=A+B$$ 与 $$\iota(A)=-A$$ 都是多项式映射，光滑。故 $$(M_n(\mathbb{R}),+)$$ 是 $$n^2$$ 维 Lie 群。注意这里群运算是**加法**而不是矩阵乘法——Lie 群的定义（3.9）不要求运算写成「乘法」，只要求它是一个群运算且光滑。

**解 基2.** 由定理 3.7，$$\mathrm{Aff}(1)=\Bigl\{\begin{bmatrix}a&b\\0&1\end{bmatrix}:a>0\text{ 或 }a<0,\ b\in\mathbb{R}\Bigr\}$$，维数 $$1^2+1=2$$。它的 Lie 代数是 $$I$$ 处切空间：

$$\mathfrak{aff}(1)=\Bigl\{\begin{bmatrix}s&t\\0&0\end{bmatrix}:s,t\in\mathbb{R}\Bigr\}=\mathrm{span}\Bigl\{E=\begin{bmatrix}1&0\\0&0\end{bmatrix},\ T=\begin{bmatrix}0&1\\0&0\end{bmatrix}\Bigr\}.$$

算换位子（由推论 3.20，矩阵群的括号就是换位子）：

$$ET=\begin{bmatrix}1&0\\0&0\end{bmatrix}\begin{bmatrix}0&1\\0&0\end{bmatrix}=\begin{bmatrix}0&1\\0&0\end{bmatrix}=T,\qquad TE=\begin{bmatrix}0&1\\0&0\end{bmatrix}\begin{bmatrix}1&0\\0&0\end{bmatrix}=\begin{bmatrix}0&0\\0&0\end{bmatrix}=0,$$

故

$$[E,T]=ET-TE=T.$$

这个二维 Lie 代数就是「$$x\mapsto ax+b$$」的代数（$$E$$ 生成伸缩、$$T$$ 生成平移）。$$\blacksquare$$

**解 基3.** $$GL(n,\mathbb{R})$$ 是 $$\mathbb{R}^{n^2}$$ 中的开集，故它在 $$I$$ 处的切空间是全部 $$M_n(\mathbb{R})$$：$$T_IG=M_n(\mathbb{R})$$，把矩阵 $$v\in M_n(\mathbb{R})$$ 认同为一个「方向」。由定理 3.14 的构造

$$X^v(g)=(dL_g)_I v.$$

而 $$L_g(h)=gh$$ 是左乘矩阵 $$g$$，其微分是左乘 $$g$$：对任意 $$h\in GL(n)$$ 与 $$\xi\in T_hGL(n)=M_n(\mathbb{R})$$，有

$$(dL_g)_h\xi=\frac{d}{dt}\Big\rvert_{t=0}g(h+t\xi)=g\xi.$$

故

$$X^v(g)=gv\qquad\text{（右乘固定矩阵 }v\text{）}.$$

左不变性直接验证：对任意 $$h\in G$$

$$(dL_h)_g X^v(g)=(dL_h)_g(gv)=h(gv)=(hg)v=X^v(hg),$$

最后一步用 $$X^v(x)=xv$$。这正是定义 3.13 的条件。$$\blacksquare$$

**解 竞1.**

**关键 leap**：先证一条预备事实——**每个可逆复矩阵都是某个矩阵的指数**。

*预备*：设 $$M\in GL(n,\mathbb{C})$$。由 Jordan 标准形，存在可逆 $$P$$ 使 $$M=PJP^{-1}$$，$$J$$ 是分块对角的 Jordan 形，每块形如 $$\lambda I+N$$（$$\lambda\neq0$$、$$N$$ 幂零且与 $$\lambda I$$ 交换）。对每个块，取 $$z\in\mathbb{C}$$ 使 $$e^{z}=\lambda$$（存在，如 $$z=\ln\lvert\lambda\rvert+i\arg\lambda$$），再令

$$\log(\lambda I+N):=zI+\sum_{m\ge1}\frac{(-1)^{m+1}}{m}\Bigl(\frac{N}{\lambda}\Bigr)^{m}.$$

$$N$$ 幂零使求和有限，故这是定义良好的矩阵；且 $$\exp(zI)\exp\bigl(\log(I+N/\lambda)\bigr)=\lambda(I+N/\lambda)=\lambda I+N$$（用了 $$zI$$ 与 $$N$$ 交换、以及 $$\exp\log(I+A)=I+A$$ 对幂零 $$A$$ 的有限恒等式）。把各块的 $$\log$$ 拼成 $$\log J$$，则

$$M=P\exp(\log J)P^{-1}=\exp\bigl(P(\log J)P^{-1}\bigr).$$

故 $$M=\exp(X)$$，$$X=P(\log J)P^{-1}$$。

**$$GL(n,\mathbb{C})$$ 连通**：对任意 $$M=\exp X$$，曲线 $$t\mapsto\exp(tX)$$（$$t\in[0,1]$$）连续、每点可逆（$$\exp(-tX)$$ 是其逆），把 $$I$$ 连到 $$M$$。故 $$GL(n,\mathbb{C})$$ 道路连通，从而连通。

**$$GL(n,\mathbb{R})$$ 的分支**：$$\det:GL(n,\mathbb{R})\to\mathbb{R}^\times$$ 连续且满（$$\det\mathrm{diag}(a,1,\dots,1)=a$$）。而 $$\mathbb{R}^\times=(-\infty,0)\cup(0,+\infty)$$ 不连通，故

$$GL(n,\mathbb{R})=\det{}^{-1}\bigl((0,+\infty)\bigr)\ \sqcup\ \det{}^{-1}\bigl((-\infty,0)\bigr)$$

是两个非空开集的不交并，至少有两个连通分支。记 $$GL(n,\mathbb{R})^{+}=\{\det>0\}$$。

再证 $$\det>0$$ 的部分道路连通。由**极分解**，任意实可逆 $$M$$ 唯一写成 $$M=QR$$，$$Q\in O(n)$$、$$R$$ 对称正定。且 $$\det M=\det Q\cdot\det R$$，而 $$\det R>0$$（正定），故 $$\det Q=\operatorname{sign}\det M$$：$$\det M>0$$ 时 $$Q\in SO(n)$$。

- $$SO(n)$$ 道路连通：正交矩阵的实标准形（第 04 章 $$SO(2)$$ 谱分析的推广）把 $$Q$$ 写成若干平面旋转块 $$R(\theta_j)$$ 与若干 $$1$$ 的直和。对每块取 $$X_j=\theta_jJ$$ 有 $$R(\theta_j)=\exp(X_j)$$（经典问题 题 1(iii)），拼成反对称 $$X$$ 得 $$Q=\exp X\in SO(n)$$。于是 $$t\mapsto\exp(tX)$$ 在 $$SO(n)$$ 内把 $$I$$ 连到 $$Q$$。
- $$R$$ 对称正定：由谱定理 $$R=\exp(Y)$$，$$Y$$ 实对称。于是 $$t\mapsto\exp(tY)$$ 在对称正定集合内把 $$I$$ 连到 $$R$$。

拼起来，$$t\mapsto\exp(tX)\exp(tY)$$（$$t\in[0,1]$$）把 $$I$$ 连到 $$QR=M$$，且沿路行列式恒为 $$\det(\exp(tX))\det(\exp(tY))=e^{t\operatorname{tr}X}e^{t\operatorname{tr}Y}>0$$。故 $$GL(n,\mathbb{R})^{+}$$ 道路连通。

$$\det<0$$ 的部分与它同胚（右乘 $$\mathrm{diag}(-1,1,\dots,1)$$），也连通。所以 $$GL(n,\mathbb{R})$$ 恰有两个连通分支：$$\det>0$$ 与 $$\det<0$$。$$\blacksquare$$

**解 竞2.**

**关键 leap**：连通性通过「$$\exp$$ 的像生成整个群」这条通道用进来。

*预备引理*：设 $$U$$ 是 $$G$$ 中含 $$e$$ 的开集，令 $$H$$ 为 $$U\cup U^{-1}$$ 生成的子群。则 $$H$$ 开（它是开集的并），从而也闭（$$H$$ 的补集是其余陪集 $$gH$$ 的并，每个 $$gH$$ 是开的），故由 $$G$$ 连通得 $$H=G$$。

回到题目。由定理 3.24(iii)，$$\exp$$ 把 $$\mathfrak{g}$$ 中 $$0$$ 的一个邻域微分同胚到 $$e$$ 的一个邻域 $$U$$；故 $$U\subseteq\exp(\mathfrak{g})$$。由引理，$$\exp(\mathfrak{g})$$ 生成 $$G$$。

现在对任意 $$X\in\mathfrak{g}$$，由定理 3.24(iv)（自然性）

$$\rho(\exp_G X)=\exp_H\bigl((d\rho)_eX\bigr)=\exp_H\bigl((d\psi)_eX\bigr)=\psi(\exp_G X).$$

故 $$\rho$$ 与 $$\psi$$ 在 $$\exp(\mathfrak{g})\supseteq U$$ 上相等。又两者都是群同态，故它们在由 $$U$$ 生成的子群上也相等，而这个子群是 $$G$$。所以 $$\rho=\psi$$。$$\blacksquare$$

（注意连通性是本质的：$$G=O(n)$$ 不连通时，$$\det$$ 与常值同态 $$1$$ 在 $$I$$ 处微分都是零（在 $$I$$ 处两者都等于 $$I$$ 附近），但它们不相等。）

**解 竞3.**

**求 $$\mathfrak{su}(2)$$**。由推论 3.20(iii)，$$\mathfrak{u}(n)=\{A:A^{*}=-A\}$$，$$\mathfrak{su}(n)$$ 再加 $$\operatorname{tr}A=0$$。写出 $$A=\begin{bmatrix}a&b\\ c&d\end{bmatrix}$$，$$A^{*}=\bar A^{\mathsf T}=\begin{bmatrix}\bar a&\bar c\\ \bar b&\bar d\end{bmatrix}$$。条件 $$A^{*}=-A$$ 逐项给出

$$\bar a=-a,\quad \bar d=-d,\quad \bar c=-b,$$

即 $$a,d$$ 为纯虚数、$$c=-\bar b$$。再加上 $$\operatorname{tr}A=a+d=0$$，即 $$d=-a$$。于是

$$\mathfrak{su}(2)=\Bigl\{\begin{bmatrix}a&b\\ -\bar b&-a\end{bmatrix}:\ a\in i\mathbb{R},\ b\in\mathbb{C}\Bigr\}.$$

参数个数：$$a$$ 贡献 1 个实参数，$$b$$ 贡献 2 个实参数，故实维数 $$\dim_{\mathbb{R}}\mathfrak{su}(2)=3$$。

**写出 Pauli 基**。验证 $$X_k=-\frac{i}{2}\sigma_k$$ 满足条件：

$$X_1=-\frac{i}{2}\begin{bmatrix}0&1\\1&0\end{bmatrix}=\begin{bmatrix}0&-i/2\\ -i/2&0\end{bmatrix},\quad X_2=-\frac{i}{2}\begin{bmatrix}0&-i\\ i&0\end{bmatrix}=\begin{bmatrix}0&-1/2\\ 1/2&0\end{bmatrix},\quad X_3=-\frac{i}{2}\begin{bmatrix}1&0\\ 0&-1\end{bmatrix}=\begin{bmatrix}-i/2&0\\ 0&i/2\end{bmatrix}.$$

每个都是反厄米（$$X_k^{*}=-X_k$$）且迹零，故在 $$\mathfrak{su}(2)$$ 中；三个实线性无关，而实维数是 3，所以它们是一组基。

**算括号**。用 $$\sigma_1\sigma_2=i\sigma_3$$，故

$$[\sigma_1,\sigma_2]=\sigma_1\sigma_2-\sigma_2\sigma_1=i\sigma_3-(-i\sigma_3)=2i\sigma_3.$$

又 $$[X_1,X_2]=\Bigl(-\frac{i}{2}\Bigr)^{2}[\sigma_1,\sigma_2]=\Bigl(-\frac14\Bigr)\bigl(2i\sigma_3\bigr)=-\frac{i}{2}\sigma_3=X_3.$$

同理 $$[X_2,X_3]=X_1$$、$$[X_3,X_1]=X_2$$，合并写成

$$[X_i,X_j]=\varepsilon_{ijk}X_k.$$

$$\blacksquare$$

**解 竞4.**

(i) 对 $$g\in G$$，先算链式法则：

$$(L_h^{*}\theta)_g=(dL_h)_g^{*}\theta_{hg}=\theta_{hg}\circ(dL_h)_g=(dL_{(hg)^{-1}})_{hg}\circ(dL_h)_g.$$

两个微分的复合等于复合映射的微分：

$$=d\bigl(L_{(hg)^{-1}}\circ L_h\bigr)_g.$$

现在算复合映射：$$L_{(hg)^{-1}}\circ L_h(x)=(hg)^{-1}(hx)=g^{-1}h^{-1}hx=g^{-1}x=L_{g^{-1}}(x)$$。故

$$(L_h^{*}\theta)_g=d\bigl(L_{g^{-1}}\bigr)_g=\theta_g.$$

两边对任意 $$g$$ 成立，即 $$L_h^{*}\theta=\theta$$。

(ii) 先算 $$R(\varphi)$$ 的切向量。由 $$R(\varphi)=\cos\varphi\,I+\sin\varphi\,J$$，

$$R'(\varphi)=-\sin\varphi\,I+\cos\varphi\,J=R(\varphi)J,$$

末一步直接验证：$$(\cos\varphi\,I+\sin\varphi\,J)J=\cos\varphi\,J+\sin\varphi\,J^{2}=\cos\varphi\,J-\sin\varphi\,I$$（用了 $$J^{2}=-I$$），与左边的 $$-\sin\varphi\,I+\cos\varphi\,J$$ 相同。

于是 $$\theta(\partial_\varphi)=R(\varphi)^{-1}R'(\varphi)=R(\varphi)^{-1}R(\varphi)J=J$$，即

$$\theta=J\,d\varphi.$$

（这里把 $$\mathfrak{g}=\mathfrak{so}(2)=\mathbb{R}J$$ 认同为 $$\mathbb{R}$$，$$J$$ 就是那个基向量。）由此

$$d\theta=d(J\,d\varphi)=J\wedge d(d\varphi)=0,$$

因为 $$J$$ 是常矩阵、$$d\,d\varphi=0$$（第 24 章：外微分的平方为零）。

**验证 Maurer–Cartan 方程**：$$\mathfrak{so}(2)$$ 是交换 Lie 代数（一维），故 $$[\theta\wedge\theta](X,Y)=[\theta(X),\theta(Y)]-[\theta(Y),\theta(X)]=0$$，方程退化为 $$d\theta=0$$，与上面一致。$$\blacksquare$$

**解 研1.**

记「$$G$$ 阿贝尔」为 (a)，「$$\mathfrak{g}$$ 阿贝尔」为 (b)。

$$(a)\Rightarrow(b)$$ 设 $$G$$ 交换，则左、右平移相同：$$L_g=R_g$$。

先记下一个一般事实：**若 $$X$$ 左不变、$$Y$$ 右不变，则 $$[X,Y]=0$$**。证明：左不变场 $$X^v$$ 的流是

$$\phi^X_t(g)=g\exp(tv),$$

这由定理 3.22 证明里的左不变性论证给出（$$t\mapsto g\exp(tv)$$ 是过 $$g$$ 的积分曲线）。右不变场 $$Y^w$$ 的流是 $$\phi^Y_s(g)=\exp(sw)g$$（同理，用右平移）。二者的复合满足

$$\phi^X_t\bigl(\phi^Y_s(g)\bigr)=\exp(sw)\,g\,\exp(tv)=\phi^Y_s\bigl(\phi^X_t(g)\bigr),$$

故流交换。流交换的两个向量场的括号为零（把 $$[X,Y]$$ 看作「沿 $$X$$ 走、沿 $$Y$$ 走」与「先 $$Y$$ 后 $$X$$」的二阶差，交换即差为零；形式地说，$$\frac{d}{dt}\bigl((\phi^X_{-t})_*Y\bigr)=(\phi^X_{-t})_*[X,Y]$$，左边恒为零时右边取 $$t=0$$ 给 $$[X,Y]=0$$）。

现在取 $$\mathfrak{g}$$ 中任意 $$v,w$$。因为 $$G$$ 交换，$$X^w$$ 既左不变（定理 3.14）又右不变（右不变的定义式 $$(dR_g)_hY(h)=Y(hg)$$ 同样成立：$$\frac{d}{dt}\bigl(h\exp(tw)g\bigr)=\frac{d}{dt}\bigl(hg\exp(tw)\bigr)$$）。由上面的一般事实 $$[X^v,X^w]=0$$，取 $$e$$ 处得 $$[v,w]=0$$。故 $$\mathfrak{g}$$ 交换。

$$(b)\Rightarrow(a)$$ 设 $$[v,w]=0$$ 对一切 $$v,w$$。先证**指数交换**：对固定的 $$v,w$$，曲线 $$\gamma(t)=\exp(tv)\exp(tw)$$ 满足

$$\gamma(0)=e,\qquad \gamma'(t)=\exp(tv)(v+w)\exp(tw),$$

（矩阵情形：对乘积求导，用 $$v$$ 与 $$\exp(tv)$$ 交换）。于是左平移后的「对数导数」

$$\gamma(t)^{-1}\gamma'(t)=\exp(-tw)\exp(-tv)\exp(tv)(v+w)\exp(tw)=\exp(-tw)(v+w)\exp(tw).$$

由 $$[v,w]=0$$ 得 $$vw=wv$$，故 $$w$$ 与一切 $$w$$ 的多项式交换，进而与 $$\exp(\pm tw)$$ 交换，于是 $$\exp(-tw)(v+w)\exp(tw)=v+w$$。所以 $$\gamma(t)^{-1}\gamma'(t)=v+w$$ 是常元，由定理 3.22 的唯一性（或经典问题 题 1(ii) 的同一论证）得

$$\gamma(t)=\exp\bigl(t(v+w)\bigr),\qquad\text{特别地}\quad \exp(v)\exp(w)=\exp(v+w).$$

这个式子对 $$v,w$$ 对称，故 $$\exp(v)\exp(w)=\exp(w)\exp(v)$$：**$$\exp(\mathfrak{g})$$ 中任意两元素交换**。

最后用连通性。由定理 3.24(iii)，$$\exp(\mathfrak{g})$$ 含 $$e$$ 的一个开邻域 $$U$$；由解 竞2 的预备引理，$$U$$ 生成 $$G$$。而 $$G$$ 的每个元素是 $$\exp(\mathfrak{g})$$ 中有限多个元素（及其逆）的乘积，这些元素两两交换，故乘积与次序无关，$$G$$ 交换。$$\blacksquare$$

（注：把结论推广到一般连通 Lie 群要用 Ado 定理把任意有限维 Lie 代数嵌入矩阵代数（见第 54 章），这里限于矩阵群已足够诚实。）

**解 研2.**

**关键 leap**：用「伴随作用是共轭在恒等元的线性化」这句话，把一个$$2\times2$$ 复矩阵群的问题转成 $$\mathbb{R}^3$$ 上的旋转群问题。

**(1) $$\mathfrak{su}(2)\cong\mathfrak{so}(3)$$**。由推论 3.20(ii)，$$\mathfrak{so}(3)=\{A\in M_3(\mathbb{R}):A^{\mathsf T}=-A\}$$，取基

$$E_1=\begin{bmatrix}0&0&0\\0&0&-1\\0&1&0\end{bmatrix},\quad E_2=\begin{bmatrix}0&0&1\\0&0&0\\-1&0&0\end{bmatrix},\quad E_3=\begin{bmatrix}0&-1&0\\1&0&0\\0&0&0\end{bmatrix}.$$

逐项算（以 $$[E_1,E_2]$$ 为例）：$$E_1E_2$$ 的第一行是零（$$E_1$$ 第一行为零），第二行是「$$E_1$$ 第二行 $$(0,0,-1)$$ 分别点乘 $$E_2$$ 的三列 $$(0,0,-1),(0,0,0),(1,0,0)$$」，得 $$(1,0,0)$$；第三行是「$$(0,1,0)$$ 点乘三列」，得 $$(0,0,0)$$。故

$$E_1E_2=\begin{bmatrix}0&0&0\\1&0&0\\0&0&0\end{bmatrix},\qquad E_2E_1=\begin{bmatrix}0&1&0\\0&0&0\\0&0&0\end{bmatrix},\qquad [E_1,E_2]=\begin{bmatrix}0&-1&0\\1&0&0\\0&0&0\end{bmatrix}=E_3.$$

循环地有 $$[E_i,E_j]=\varepsilon_{ijk}E_k$$。与解 竞3 的 $$[X_i,X_j]=\varepsilon_{ijk}X_k$$ 比较：结构常数完全相同，故线性映射 $$\varphi:\mathfrak{su}(2)\to\mathfrak{so}(3)$$、$$\varphi(X_k)=E_k$$ 保持括号，是 Lie 代数同构。

**(2) 造出 $$SU(2)\to SO(3)$$ 的满同态**。在 $$\mathfrak{su}(2)$$ 上定义伴随作用

$$\mathrm{Ad}_g(X)=gXg^{-1}\qquad(g\in SU(2),\ X\in\mathfrak{su}(2)).$$

先验 $$\mathrm{Ad}_g$$ 落在 $$\mathfrak{su}(2)$$ 内：$$(gXg^{-1})^{*}=(g^{-1})^{*}X^{*}g^{*}=g(-X)g^{-1}=-(gXg^{-1})$$（用了 $$g^{*}=g^{-1}$$），迹也是零。且 $$\mathrm{Ad}$$ 是群同态（$$\mathrm{Ad}_{gh}=\mathrm{Ad}_g\mathrm{Ad}_h$$）。

再验 $$\mathrm{Ad}_g$$ 保内积。在 $$\mathfrak{su}(2)$$ 上取双线性形式 $$B(X,Y)=\operatorname{tr}(XY)$$。它**负定**：$$X^{*}=-X$$ 写 $$X=iH$$（$$H$$ 厄米），则 $$\operatorname{tr}(X^{2})=-\operatorname{tr}(H^{2})<0$$（$$X\neq0$$ 时 $$H\neq0$$，厄米矩阵的迹平方和为正）。它**$$\mathrm{Ad}$$-不变**：

$$B(gXg^{-1},gYg^{-1})=\operatorname{tr}(gXYg^{-1})=\operatorname{tr}(XY)=B(X,Y).$$

于是 $$\mathrm{Ad}_g$$ 保负定形式，即保内积 $$-B$$，故 $$\mathrm{Ad}_g\in O(\mathfrak{su}(2))\cong O(3)$$。

行列式：$$\det\circ\,\mathrm{Ad}:SU(2)\to\{\pm1\}$$ 连续，而 $$SU(2)\cong S^{3}$$（第 25、26 章会证：$$SU(2)=\{\begin{bmatrix}u&v\\-\bar v&\bar u\end{bmatrix}:\lvert u\rvert^{2}+\lvert v\rvert^{2}=1\}$$，即单位球面）连通，故它取常值 $$\det(\mathrm{Ad}_e)=1$$。所以

$$\mathrm{Ad}(SU(2))\subseteq SO(3).$$

**核**：$$\mathrm{Ad}_g=I$$ 当且仅当 $$gX=Xg$$ 对一切 $$X\in\mathfrak{su}(2)$$，即 $$g$$ 与 $$\mathfrak{su}(2)$$ 中一切元素交换。$$\{X_1,X_2,X_3\}$$ 与 $$\{iX_1,iX_2,iX_3\}$$ 合起来张成 $$M_2(\mathbb{C})$$（实线性），故 $$g$$ 与全部 $$2\times2$$ 矩阵交换。与全部矩阵交换的矩阵是纯量矩阵，故 $$g=\lambda I$$；$$g\in SU(2)$$ 给出 $$\lvert\lambda\rvert=1$$、$$\lambda^2=1$$，即 $$\lambda=\pm1$$。所以

$$\ker\mathrm{Ad}=\{\pm I\}.$$

**满**：$$\mathrm{Ad}$$ 诱导单同态 $$\overline{\mathrm{Ad}}:SU(2)/\{\pm I\}\to SO(3)$$。两边维数都是 3（$$\dim SU(2)/\{\pm I\}=\dim SU(2)=3=\dim SO(3)$$）。单浸入的像在等维数时是开集；像又紧（$$SU(2)$$ 紧）、故闭。$$SO(3)$$ 连通，开且闭的非空子集只能是全体，故

$$\overline{\mathrm{Ad}}:SU(2)/\{\pm I\}\ \cong\ SO(3),$$

即 $$\mathrm{Ad}:SU(2)\to SO(3)$$ 是核为 $$\{\pm I\}\cong\mathbb{Z}/2$$ 的满同态，也就是**二重覆盖**：由定理 3.26（取 $$H=\{\pm I\}$$），$$SU(2)\to SU(2)/\{\pm I\}=SO(3)$$ 是以 $$\mathbb{Z}/2$$ 为结构群的主丛。

**不同构**：$$\mathfrak{su}(2)\cong\mathfrak{so}(3)$$ 但 $$SU(2)\not\cong SO(3)$$（前者单连通、后者有非平凡的基本群，二者基数也不同：覆盖是 2 对 1）。这正是定理 3.24 之后那条注记的具体例证：**Lie 代数只决定局部结构**。

这一现象是第 50 章的起点：典型群的拓扑。$$SU(2)\cong S^{3}$$ 与 $$SO(3)\cong\mathbb{R}P^{3}$$ 的差别，正是「哪些群单连通、基本群是什么」这个问题的第一个也是最重要的例子；而上面用到的 $$SU(2)\to S^{2}$$（固定一个方向、剩下绕它的自转）与 $$SU(2)\to SO(3)$$ 两个主丛，会是那里的主要工具。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**五条核心洞察。**

1. **仿射空间 = 主齐性空间**。「点不能加点、点能加向量」的代数形式是：位置构成主齐性空间而非向量空间，位移才构成向量空间。温度/温差、电势/电势差、势能/势能差、原函数/不定积分常数全是这一个结构（定义 3.1、定理 3.3）。物理上一切「只能谈差」的量都是这么来的。

2. **仿射变换可以矩阵化，代价是升一维**。$$\mathrm{Aff}(n)\hookrightarrow GL(n+1,\mathbb{R})$$、$$(M,b)\mapsto\begin{bmatrix}M&b\\0&1\end{bmatrix}$$，而像是一个闭子群（定理 3.7）。这解释了机器人学里齐次变换矩阵为什么是 $$4\times4$$ 而不是 $$3\times3$$。

3. **Lie 群 = 群 + 光滑流形 + 相容性**。相容性精确为「$$\mu$$ 与 $$\iota$$ 都光滑」，并且可以压缩成一条判据「$$(x,y)\mapsto x^{-1}y$$ 光滑」（定义 3.9、定理 3.10）。$$SO(2)$$ 是全书第一个真的把图册写下来的例子（定理 3.11）。

4. **求导给出的是代数**。$$T_eG$$ 本身只是一个向量空间；加上「左不变向量场在括号下封闭」这件事，它才变成 Lie 代数（定理 3.14、3.16）。矩阵群情形括号就是换位子 $$[A,B]=AB-BA$$，而它恰好是两条指数曲线差到二阶的系数（定理 3.20 的证明）。$$\mathfrak{so}(n)$$、$$\mathfrak{su}(n)$$、$$\mathfrak{aff}(n)$$ 都由此一次算出。

5. **指数映射是一般概念，不是记号**。$$\exp:\mathfrak{g}\to G$$ 由「单参数子群」定义，与一切同态交换（定理 3.24(iv)）。第 02 章的 $$e^{i\theta}$$ 与第 46 章的 $$e^{-itH}$$ 都是它的特例。第 54 章会补上它的反函数与 BCH 公式。

**三条接口的收束。** 第 01、02 章的 $$SO(2)$$ 在本章被升成一般理论（定理 3.11 给图册、题 1 给求导与 $$\exp(\theta J)=R(\theta)$$、定理 3.24 给 $$\exp$$ 的一般性质）。第 12 章的纤维丛与第 26 章的 Stokes 在 3.6 节汇合：**Lie 群本身是主丛** $$G\to G/H$$（定理 3.26），而 Maurer–Cartan 形式 $$\theta=g^{-1}dg$$ 是它上面免费的左不变 1-形式，$$d\theta+\frac12[\theta\wedge\theta]=0$$ 就是外微分版本（定义 3.27、定理 3.28）。第 46 章的指数映射在这里有了一般定义（定义 3.23）。

**下一章的悬念。** 本章反复看到「Lie 代数相同而 Lie 群不同」的现象：$$\mathfrak{su}(2)\cong\mathfrak{so}(3)$$ 但 $$SU(2)\not\cong SO(3)$$（解 研2）；$$GL(n,\mathbb{C})$$ 连通而 $$GL(n,\mathbb{R})$$ 不连通（解 竞1）；$$SO(2)\cong S^{1}$$ 有 $$\pi_1=\mathbb{Z}$$ 而 $$\mathbb{R}$$ 单连通。这些都说明：**Lie 代数只决定局部**，全局拓扑（连通分支、单连通性、基本群）必须另外算。第 50 章「典型群的拓扑」就来算这件事：哪些经典群紧、哪些连通、哪些单连通，$$\pi_1(SO(n))$$、$$\pi_1(SU(n))$$ 是什么。我们本章搭好的主丛机器（定理 3.26）在那里会直接给出递推公式——例如从 $$SO(n)\to S^{n-1}$$ 出发，由长正合列推出 $$SO(n)$$ 的基本群。$$\mathrm{Aff}(n)$$、Galileo 群之类的非紧群，以及「10 维 Galileo 群在量子力学里要多出一个中心元（质量）」这件事，也会在那里第一次被说清楚。

**延伸阅读。**

- J. Stillwell, *Naive Lie Theory* —— 本层次的理想读物，从 $$SO(3)$$ 与四元数讲到 Lie 代数，不假设流形预备知识。
- B. Hall, *Lie Groups, Lie Algebras, and Representations*（GTM 222）—— 矩阵 Lie 群路线，闭子群定理与李的三条定理写得最清楚。
- J. Marsden & T. Ratiu, *Introduction to Mechanics and Symmetry* 第 18 章 —— Lie 群在力学中的用法（伴随、余伴随、动量映射）的入口。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch47_仿射空间_变换群与Lie群_上.md">← 第47章 仿射空间、变换群与 Lie 群·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch49_典型群的拓扑_上.md">第49章 典型群的拓扑·上 →</a></div>
</div>
