---
layout: default
---

# 第56章: 复半单 Lie 代数与根系·下：完整推导 (Complex Semisimple Lie Algebras and Root Systems · Part II: Full Derivation)

> 专家依据: `_experts/algebra/lie-algebra-root-systems.md`（主，主场）+ `_experts/algebra/_SKILL.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）
> 配套预备: 见 第55章 复半单 Lie 代数与根系·上（同一主题的具体铺垫，建议先读）

## 一、本章概要 (Overview)

读完第55章的具体例子——三维表示里的权链、一个退化与一个非退化的 Killing 型、$$\mathfrak{sl}(3,\mathbb C)$$ 的六个根、一对不等长向量的 Cartan 整数——之后，这里把同样的构造写成一般定义，并给出完整证明。

上一章把 Lie 代数从 Lie 群的切空间里生出来，并给出了指数映射。可是拿到一个 Lie 代数之后，能用它做什么？本章回答的是结构问题：**哪些 Lie 代数是「原子的」，以及这些原子能不能被列成一张表。**

答案是能，而且表小得惊人。本章要把「半单」这个词从一个否定性定义（「没有可解理想」）变成一个**可分类的结构**：用 Cartan 判据判定半单性，用 Cartan 子代数把 $$\operatorname{ad}$$ 同时对角化，把整个代数拆成根空间 $$L = H \oplus \bigoplus_{\alpha} L_\alpha$$，再把根的集合抽出来当成一个独立的欧氏几何对象（根系），最后压成一张**只能有九种形状**的图（Dynkin 图）。这条链的终点是一条分类定理：复单 Lie 代数恰有 $$A_n,B_n,C_n,D_n$$ 四族与 $$E_6,E_7,E_8,F_4,G_2$$ 五个例外。

与前后章的关系：从第 54 章来（那里是 Lie 群与指数映射的微分侧），本章走的是**结构侧**。第 34 章的谐振子升降算子与第 52 章的 $$SU(2)$$ 会在本章被**认领**——但不是按最省事的那个猜法认领。入口题 (iv)–(v) 要破除一个几乎人人都会犯的误认：谐振子的 $$a,a^\dagger$$ **不是** $$\mathfrak{sl}(2)$$ 的 $$E,F$$。它们是**振荡子代数 (oscillator algebra)** 的生成元，与 $$\mathfrak{sl}(2)$$ 共享「升权 / 降权」的语法却不是同一个代数（见 入口题 (iv) 与 4.3 节）。而第 52 章的 $$SU(2)$$ 则是货真价实的 $$A_1$$。往第 58 章去（Clifford 代数与 Lorentz 群），会把「几何对象的不同表示」这件事从根系的整性约束里再抽一次。

## 二、入口：一道具体的问题 (Entry Problem)

> 题目来源：**自编**。母题有二：一是第 34 章谐振子那道题的最后一问（「能级等间距是哪个代数事实的推论？」），二是 Lie 理论史上真实存在过的猜想——Killing 在 1888 年列出的「所有单 Lie 代数」表里多算了几个、又漏了几个，直到 Cartan 用根系的整性约束重算才定稿。把「算一个具体例子」与「证明一张表是完备的」并成一道题，是本章的设计。

**(i)** 考虑 $$\mathfrak{sl}(2,\mathbb C)$$，即全体迹为零的 $$2\times 2$$ 复矩阵。取

$$E = \begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad F = \begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad H = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

逐个算出三个换位子 $$[H,E]$$、$$[H,F]$$、$$[E,F]$$。

**(ii)** 设 $$V$$ 是 $$\mathfrak{sl}(2,\mathbb C)$$ 的有限维表示，且 $$V\neq 0$$。利用 (i) 的换位子，证明：存在 $$v\neq 0$$ 与复数 $$\lambda$$，使

$$H v = \lambda v,\qquad E v = 0 .$$

（提示：先证明 $$E_v := \{w : Ew=0\}$$ 非零——考虑 $$E$$ 的一个特征向量与 $$H$$ 的介入；再在 $$E_v$$ 上让 $$H$$ 对角化。）

**(iii)** 承 (ii)，令 $$v_k = F^k v$$（约定 $$F^0 v = v$$），$$k = 0,1,2,\dots$$。证明

$$H v_k = (\lambda - 2k)v_k,\qquad E v_k = k(\lambda - k + 1)\,v_{k-1}\quad(k\ge 1).$$

并由此论证：若 $$V$$ 不可约，则 $$\lambda$$ 必是**非负整数** $$m$$，且

$$V = \operatorname{span}\{v_0,v_1,\dots,v_m\},\qquad \dim V = m+1 .$$

也就是说，$$\mathfrak{sl}(2,\mathbb C)$$ 的全部有限维不可约表示由**一个非负整数**完全标记。

**(iv) 先破除一个几乎人人都会犯的误认。** 现在看第 34 章的谐振子：

$$a = \frac{1}{\sqrt{2m\hbar\omega}}\bigl(m\omega X + iP\bigr),\qquad a^\dagger = \frac{1}{\sqrt{2m\hbar\omega}}\bigl(m\omega X - iP\bigr),$$

数算子 $$N = a^\dagger a$$，Hamilton 量 $$H_{\mathrm{osc}} = \hbar\omega\bigl(N+\tfrac12 I\bigr)$$，第 34 章的定理给出

$$[N,a] = -a,\qquad [N,a^\dagger] = a^\dagger,\qquad [a,a^\dagger] = I .$$

看一眼这三条，几乎必然会产生一个念头：**「$$a^\dagger$$ 升、$$a$$ 降、$$N$$ 量权——这不就是 $$\mathfrak{sl}(2)$$ 的 $$E,F,H$$ 吗？」** 这个念头是错的，而且错得很值得当场拆开。

**证明它错（最干净的论证：那个三元素张成的空间根本不是子代数）**：注意 $$[a,a^\dagger]=I$$ 的右端是**单位算子** $$I$$，而 $$I\notin\operatorname{span}\{a,a^\dagger,N\}$$：$$a,a^\dagger,N$$ 都改变或保持能级（分别是 $$-1,+1,0$$），而 $$I$$ 保持一切不动，不可能是三者的非平凡线性组合。于是

$$[a,a^\dagger] = I\ \notin\ \operatorname{span}\{a,a^\dagger,N\},$$

即 $$\operatorname{span}\{a,a^\dagger,N\}$$ **对换位子不封闭，不是 $$\mathfrak{gl}(\mathscr H)$$ 的 Lie 子代数**，更谈不上同构于 $$\mathfrak{sl}(2)$$。要得到真正的 Lie 代数必须把 $$I$$ 补进去：

$$\mathfrak{osc} = \operatorname{span}\{a,\ a^\dagger,\ N,\ I\},\qquad [N,a]=-a,\quad [N,a^\dagger]=a^\dagger,\quad [a,a^\dagger]=I,\quad I\ \text{中心}.$$

它**不是** $$\mathfrak{sl}(2)$$，两条独立的理由：**（维数与中心）** $$\dim\mathfrak{osc}=4$$、中心 $$Z(\mathfrak{osc})=\mathbb C I\neq0$$，而 $$\mathfrak{sl}(2)$$ 是三维**单**代数、中心为零；**（可解理想）** $$\mathbb C I$$ 是 $$\mathfrak{osc}$$ 的非零交换理想，与半单不相容，而 $$\mathfrak{sl}(2)$$ 半单（解 题 1(1) 已验证）。

**结构上的说法**：$$\mathfrak{osc} = \mathfrak h\rtimes\mathbb C N$$，其中

$$\mathfrak h=\operatorname{span}\{a,a^\dagger,I\}\cong\text{Heisenberg 代数}$$

是理想（由 $$[N,a]=-a$$、$$[N,a^\dagger]=a^\dagger$$，$$\operatorname{ad}N$$ 把 $$\mathfrak h$$ 映到自身），而 $$N$$ 通过 $$\operatorname{ad}N$$ 作用在 $$\mathfrak h$$ 上（特征值 $$\pm1$$ 与 $$0$$）。用第 54 章的话说，这是一个**中心扩张**：那条 $$[a,a^\dagger]=I$$ 落在中心维里。

$$\mathfrak{osc}$$ 与 $$\mathfrak{sl}(2)$$ **共享升降语法**（都有「升权算子」「降权算子」「测权算子」三个角色），但**不是同一个代数**——差别就在那个换位子的落点：$$\mathfrak{sl}(2)$$ 的 $$[E,F]=H$$ 落在**可对角化的 Cartan 元**上，$$\mathfrak{osc}$$ 的 $$[a,a^\dagger]=I$$ 落在**中心**上。这个差别不是技术细节，它决定了两者表示论的根本不同（见 (vi)）。

**(v) 那么 $$\mathfrak{sl}(2)$$ 到底藏在哪里？** 答案：藏在这三个算子的**平方**里。令

$$\tilde E = \tfrac12 a^{\dagger\,2},\qquad \tilde F = -\tfrac12 a^{2},\qquad \tilde H = N + \tfrac12 I .$$

由 $$[N,a^\dagger]=a^\dagger$$ 与 $$[N,a]=-a$$ 得 $$[N,a^{\dagger\,2}]=2a^{\dagger\,2}$$、$$[N,a^2]=-2a^2$$，于是

$$[\tilde H,\tilde E] = \tfrac12[N,a^{\dagger\,2}] = a^{\dagger\,2} = 2\tilde E,\qquad [\tilde H,\tilde F] = -\tfrac12[N,a^{2}] = a^{2} = -2\tilde F .$$

第三个关系要算一下。由 $$[a,a^\dagger]=I$$ 可证 $$[a^{\dagger\,2},a^2] = -4N-2$$（反复使用 $$a^{\dagger\,n}a = a\,a^{\dagger\,n}-n a^{\dagger\,n-1}$$ 即可；或者用第 34 章的定理 3.9 先算 $$a^{\dagger\,2}a^2 = N^2-N$$、$$a^2a^{\dagger\,2}=N^2+3N+2$$，相减得 $$-4N-2$$）。于是

$$[\tilde E,\tilde F] = -\tfrac14[a^{\dagger\,2},a^2] = -\tfrac14(-4N-2) = N+\tfrac12 I = \tilde H .$$

所以 $$\operatorname{span}\{\tilde E,\tilde F,\tilde H\}\cong\mathfrak{sl}(2,\mathbb C)$$——**但不是 $$\{a,a^\dagger,N\}$$，而是另外三个二次算子。**

**(vi) 「能级等间距」该归给谁？** 归给**振荡子代数加 $$N$$ 的正性**，不要归给 $$\mathfrak{sl}(2)$$ 的表示论。完整地说：

- $$N=a^\dagger a$$ 是正算子（对任何 $$\psi$$，$$\langle\psi,N\psi\rangle=\lVert a\psi\rVert^2\ge0$$），故其谱含于 $$[0,\infty)$$；
- 由 $$[N,a]=-a$$，若 $$N\psi=\lambda\psi$$ 则 $$N(a\psi)=(\lambda-1)a\psi$$，故 $$a$$ 把本征值降 $$1$$，且由正性必须停在 $$\lambda=0$$（否则得到负本征值），此时 $$a\psi=0$$；
- 由 $$[N,a^\dagger]=a^\dagger$$，$$a^\dagger$$ 把本征值升 $$1$$，可无限进行。

三步合起来，谱恰为 $$\{0,1,2,\dots\}$$——**公差为 $$1$$ 的等差链，且只能向一侧延伸**。能级 $$E_n=\hbar\omega(n+\tfrac12)$$ 因此等间距。

**为什么不能用 $$\mathfrak{sl}(2)$$ 的表示论说这件事？** 因为 $$\mathfrak{sl}(2)$$ 不可约表示的权链是 $$m,m-2,\dots,-m$$——**有限、两端有界**；而谐振子的谱是**无限、单侧、无上界**的。「形状不符」正是 $$\mathfrak{osc}\neq\mathfrak{sl}(2)$$ 的物理印记：只看「等间距」就断言「这是 $$\mathfrak{sl}(2)$$」，就丢掉了「谱有下界、无上界」这件最重要的事。（那两块 $$\mathfrak{sl}(2)$$ 模其实都**无限维**——偶块的权为 $$\frac12,\frac52,\dots$$——属于**最低权模**，不在 (iii) 分类的有限维不可约模之内；(iii) 的论证恰恰用到了有限性。）

**正确的并排图景**：谐振子的阶梯算子是振荡子代数的生成元；它们的**平方**各承载一个 $$\mathfrak{sl}(2)$$ 作用。教训是——**表示论里「看起来一样」的东西，代数结构可能不同；鉴别要看换位子落在哪里（中心 vs Cartan），而不是看它长得像什么。**

**(vii)** 换一个完全不同的方向。设 $$\Phi$$ 是某个半单 Lie 代数 $$L$$ 的根组成的有限集合。证明：从中任取两根 $$\alpha,\beta$$，它们的夹角 $$\theta$$ 只能取有限的七个值

$$90^\circ,\ 60^\circ,\ 120^\circ,\ 45^\circ,\ 135^\circ,\ 30^\circ,\ 150^\circ .$$

并说明：为什么这条「角度只有七种」的限制，足以让「单 Lie 代数的个数有限」这件事变成一个**组合枚举问题**。

**(viii)** 最后，把 (i)–(iii) 与 (vii) 放在一起看。$$\mathfrak{sl}(2,\mathbb C)$$ 的根系只有一根 $$\alpha$$ 与它的负根 $$-\alpha$$（加上反射封闭性），画成「一张图」就是一个孤立的顶点。猜想：$$\mathfrak{sl}(3,\mathbb C)$$ 的「图」长什么样？一般 $$\mathfrak{sl}(n+1,\mathbb C)$$ 呢？在本章第五节这个问题会被彻底解掉。

**本题的地位**：(i)–(iii) 是本章全部表示论的原子模型；(iv)–(vi) 是把量子力学的「等间距能谱」**正确地**归位——不是归给 $$\mathfrak{sl}(2)$$，而是归给振荡子代数，并当场拆穿那个看起来天经地义的误认；(vii)–(viii) 是分类定理的入口。三部分合起来，正是本章要建立的那条链：**具体矩阵 → 换位子 → 权链 → 根的几何 → 一张图**。

## 三、结构：定义与完整推导 (Structure & Proof)

本节分五段：3.1–3.2 建立**判定工具**（可解、幂零、半单怎么定义，怎么用 Killing 型去测）；3.3 建立**结构分解**（Cartan 子代数把 $$\operatorname{ad}$$ 同时对角化，把代数拆成根与根空间）；3.4–3.5 建立**分类**（把根的集合抽成一个几何对象，压成一张图，再枚举这张图）。

贯穿全节的原则：**每个抽象定义后面立刻跟一个能动手算的矩阵例子。** 复 Lie 代数的一切，最后都要能在 $$\mathfrak{sl}(n,\mathbb C)$$ 里用手对出来。

### 3.1 可解与幂零

**定义 3.1（导出列与可解, derived series and solvable）**。设 $$L$$ 是有限维 Lie 代数。递归定义

$$L^{(0)} = L,\qquad L^{(i+1)} = [L^{(i)}, L^{(i)}]\qquad(i\ge 0).$$

这里 $$[L^{(i)},L^{(i)}]$$ 表示由全体 $$[x,y]$$（$$x,y\in L^{(i)}$$）张成的子空间。若存在 $$n$$ 使 $$L^{(n)} = 0$$，称 $$L$$ 为**可解**的 (solvable)。

**定义 3.2（下中心列与幂零, lower central series and nilpotent）**。递归定义

$$L^{0} = L,\qquad L^{i+1} = [L, L^{i}]\qquad(i\ge 0).$$

若存在 $$n$$ 使 $$L^{n}=0$$，称 $$L$$ 为**幂零**的 (nilpotent)。

两条序列的差别只在一步：可解取的是「与**自己**的换位子」，幂零取的是「与**整个 $$L$$** 的换位子」。由此立刻有：

**命题 3.3（幂零蕴含可解）**。对每个 $$i$$ 有 $$L^{(i)}\subseteq L^{i}$$。特别地，$$L$$ 幂零 $$\Rightarrow$$ $$L$$ 可解。

*证明*：对 $$i$$ 归纳。$$i=0$$ 时 $$L^{(0)}=L=L^{0}$$，成立。设 $$L^{(i)}\subseteq L^{i}$$。则

$$L^{(i+1)} = [L^{(i)},L^{(i)}]\subseteq [L,L^{i}] = L^{i+1},$$

第一个包含号是因为换位子对被含项单调：若 $$A\subseteq B$$，则 $$[A,A]\subseteq [B,B]\subseteq [B,L]$$（最后一步用了 $$[B,B]\subseteq[B,L]$$）。故归纳完成。至于结论：若 $$L^{n}=0$$ 则 $$L^{(n)}\subseteq L^{n}=0$$，故 $$L^{(n)}=0$$。$$\blacksquare$$

**反例 3.4（可解不必幂零）**。设 $$L=\operatorname{span}\{x,y\}$$，$$[x,y]=x$$，其余由反交换与双线性补全。$$L$$ 是 Lie 代数：$$\dim L=2$$，故 Jacobi 恒等式的三个自变量中必有重复（取 $$z=x$$）：$$[x,[y,x]]+[y,[x,x]]+[x,[x,y]]=[x,-x]+0+[x,x]=0$$，其余重复情形同理。

$$L^{(1)}=[L,L]=\mathbb C x$$、$$L^{(2)}=[\mathbb C x,\mathbb C x]=0$$，故 $$L$$ 可解。但 $$L^{1}=\mathbb C x$$、$$L^{2}=[L,\mathbb C x]=\mathbb C x$$，归纳得 $$L^{i}=\mathbb C x\neq0$$ 对一切 $$i$$，故 $$L$$ **不幂零**。

**定义 3.5（中心）**。$$Z(L) = \{x\in L : [x,L]=0\}$$。

**定理 3.6（Engel 定理, Engel's theorem）**。设 $$L$$ 是有限维 Lie 代数。则

$$L\ \text{幂零}\iff \text{每个}\ \operatorname{ad} x\ (x\in L)\ \text{都是幂零线性变换}.$$

*证明思路*：主定理是表示论形式——「若 $$V$$ 有限维非零、$$L\subseteq\mathfrak{gl}(V)$$ 且每个 $$x\in L$$ 幂零，则存在被全体 $$x\in L$$ 零化的非零向量」；等价地，$$V$$ 有一面被 $$L$$ 保持的完备旗（$$L$$ 可同时严格上三角化）。$$\Leftarrow$$ 由它推出，$$\Rightarrow$$ 是几步直算。

*证明（$$\Leftarrow$$，对 $$\dim L$$ 归纳）*：$$\dim L=0$$ 时任取 $$v\neq0$$。设 $$\dim L>0$$，取**极大真子代数** $$K\subsetneq L$$。

**引理（极大真子代数余维 1）**：由 $$K$$ 的极大性，若正规化子 $$N_L(K)\supsetneq K$$ 则 $$N_L(K)=L$$，即 $$K\lhd L$$ 是理想，于是 $$L/K$$ 无真子代数。若 $$\dim(L/K)\ge2$$，取 $$0\neq\bar x\in L/K$$，则 $$\mathbb C\bar x$$ 是 $$L/K$$ 的真子代数（一维代数交换），其原像 $$K+\mathbb Cx$$ 是 $$L$$ 的真子代数且严格大于 $$K$$，与极大性矛盾。故 $$\dim(L/K)=1$$，$$L=K+\mathbb Cz$$。

**归纳步**：对 $$k\in K$$，$$\operatorname{ad}_L k$$ 幂零，故其在不变子空间 $$K$$ 上的限制 $$\operatorname{ad}_K k$$ 也幂零。由归纳假设（$$\dim K<\dim L$$）存在 $$0\neq v\in V$$ 使 $$Kv=0$$。令 $$W:=\{v\in V : Kv=0\}\neq0$$。

对 $$x\in L$$、$$v\in W$$、$$k\in K$$，用 $$K\lhd L$$（故 $$[k,x]\in K$$）：

$$k(xv) = x(kv)+[k,x]v = 0+0 = 0 .$$

故 $$W$$ 是 $$L$$-不变子空间。又 $$L=K+\mathbb Cz$$，而 $$z\vert_W$$ 幂零（$$z\in L$$ 幂零），故 $$z\vert_W$$ 有非零核向量 $$v_0$$。于是 $$Kv_0=0$$（$$v_0\in W$$）且 $$zv_0=0$$，即 $$Lv_0=0$$。表示论形式证毕。

*证明（$$\Rightarrow$$）*：设 $$L^{n}=0$$。对 $$x\in L$$，由 $$L^{i+1}=[L,L^{i}]$$ 得

$$\operatorname{ad}x\,(L^{i}) = [x,L^{i}]\subseteq [L,L^{i}] = L^{i+1},$$

故 $$(\operatorname{ad}x)^{n}(L)\subseteq L^{n}=0$$，即每个 $$\operatorname{ad}x$$ 幂零。$$\blacksquare$$

**定理 3.7（Lie 定理, Lie's theorem）**。设 $$F$$ 是特征 $$0$$ 的代数闭域，$$L\subseteq\mathfrak{gl}(V)$$ 是可解子代数，$$V$$ 有限维非零。则 $$L$$ 有公共特征向量（等价地，可取 $$V$$ 的基使 $$L$$ 同时上三角化）。

*证明思路*：对 $$\dim L$$ 归纳，取理想 $$I\lhd L$$ 使 $$\dim(L/I)=1$$（可解性给出 $$[L,L]\subsetneq L$$）。对 $$I$$ 用归纳假设得特征子空间 $$V_\lambda=\{v : xv=\lambda(x)v\ \forall x\in I\}\neq0$$。关键一步是证它被 $$L$$ 保持：由 $$x(yv)=y(xv)+[x,y]v=\lambda(x)yv+\lambda([x,y])v$$，只需 $$\lambda([x,y])=0$$；后者由在 $$W=\operatorname{span}\{v,yv,y^2v,\dots\}$$ 上取迹得到（$$x\in I$$ 在基 $$\{v,yv,\dots\}$$ 下上三角、对角元全为 $$\lambda(x)$$，故 $$\operatorname{tr}([x,y]\vert_W)=(\dim W)\lambda([x,y])$$，而 $$[x,y]\in I$$ 使其为 $$\lambda([x,y])$$ 的倍数，特征 $$0$$ 迫使 $$\lambda([x,y])=0$$）。最后在非零的 $$V_\lambda$$ 上取 $$L$$ 的公共特征向量。$$\blacksquare$$

**推论 3.8（可解代数的导出理想幂零）**。设 $$L$$ 是特征 $$0$$ 代数闭域上的可解 Lie 代数，则 $$[L,L]$$ 幂零。

### 3.2 Killing 型与 Cartan 判据

**为什么要定义"半单"**：可解与幂零描述的是"坏"的一端（一路做换位子最终归零）；我们真正想研究的是它们的对立面——完全没有可解理想拖后腿的代数。直接说"没有可解理想"是一句否定性描述，不方便下手，所以先给它起名字，再想办法把它变成可计算的条件（下面的 Cartan 第二判据）。

**定义 3.9（根与半单, radical and semisimple）**。$$L$$ 的**根** (radical) $$\operatorname{Rad}(L)$$ 是 $$L$$ 的最大可解理想（全体可解理想之和仍是可解理想，故最大者存在）。$$L$$ 称为**半单**的 (semisimple)，若 $$\operatorname{Rad}(L)=0$$。

**定义 3.10（单）**。$$L$$ 称为**单**的 (simple)，若 $$L$$ 非交换且不含非平凡真理想（即 $$\{0\}$$ 与 $$L$$ 之外的理想）。

**命题 3.11（单蕴含半单）**。$$L$$ 单 $$\Rightarrow$$ $$L$$ 半单。

*证明*：设 $$I\lhd L$$ 可解。由单性 $$I=0$$ 或 $$I=L$$。若 $$I=L$$，则 $$L$$ 可解；但可解且非交换的 $$L$$ 必有 $$[L,L]\lhd L$$ 且 $$[L,L]\subsetneq L$$（若 $$[L,L]=L$$，导出列就是恒等不降、永不归零），由单性得 $$[L,L]=0$$，即 $$L$$ 交换，与单性要求的非交换矛盾。故一切可解理想为 $$0$$，即 $$\operatorname{Rad}(L)=0$$。$$\blacksquare$$

**定理 3.12（半单的结构定理）**。设 $$L$$ 半单。则 $$L$$ 可唯一（不计次序）分解为单理想的直和

$$L = L_1\oplus L_2\oplus\cdots\oplus L_t,\qquad L_i\ \text{单}.$$

并且 $$L$$ 的每个理想都是其中若干个 $$L_i$$ 之和。

*证明思路*：由 $$L$$ 非可解知存在极小非零理想。若 $$I,J$$ 是两个不同的极小理想，则 $$I\cap J=0$$ 且 $$[I,J]\subseteq I\cap J=0$$，故 $$I\oplus J$$ 是理想；对正交补 $$I^\perp$$（关于 $$\kappa$$）用同一套论证，最后用 $$I\cap I^\perp=0$$（下面的 定理 3.17）拼出直和。每个极小非零理想自动是单的：若 $$J\lhd I$$ 且 $$J\neq I,0$$，则 $$I$$ 中任何其他理想与之正交，矛盾于极小性。$$\blacksquare$$

**为什么这样定义 Killing 型**：$$\operatorname{ad}x$$ 是 $$L\to L$$ 的线性变换，两个线性变换复合再取迹，是从一对元素 $$(x,y)$$ 榨出一个数字最朴素的办法（比行列式线性、比特征值好计算），而且第55章 3.2 节已经在两个最小的例子里验证过：这样定义出的双线性型，退化与否恰好对应"可解/不可解"这类结构性质。下面先证明它有一个关键的代数性质（结合不变性），再用它推出两条可计算的判据。

**定义 3.13（Killing 型, Killing form）**。$$L$$ 上的双线性型

$$\kappa(x,y) = \operatorname{tr}(\operatorname{ad} x\circ \operatorname{ad} y).$$

**定理 3.14（Killing 型的结合不变性, invariance）**。对一切 $$x,y,z\in L$$，

$$\kappa([x,y],z) = \kappa(x,[y,z]).$$

*证明*：由 $$\operatorname{ad}$$ 是同态与 Jacobi 恒等式，

$$\operatorname{ad}[x,y] = [\operatorname{ad}x,\operatorname{ad}y] = \operatorname{ad}x\,\operatorname{ad}y - \operatorname{ad}y\,\operatorname{ad}x .$$

于是

$$\kappa([x,y],z) = \operatorname{tr}\bigl((\operatorname{ad}x\,\operatorname{ad}y - \operatorname{ad}y\,\operatorname{ad}x)\operatorname{ad}z\bigr) = \operatorname{tr}(\operatorname{ad}x\,\operatorname{ad}y\,\operatorname{ad}z) - \operatorname{tr}(\operatorname{ad}y\,\operatorname{ad}x\,\operatorname{ad}z).$$

对第二项用迹的循环性 $$\operatorname{tr}(ABC)=\operatorname{tr}(CAB)$$：$$\operatorname{tr}(\operatorname{ad}y\,\operatorname{ad}x\,\operatorname{ad}z) = \operatorname{tr}(\operatorname{ad}x\,\operatorname{ad}z\,\operatorname{ad}y)$$。于是

$$\kappa([x,y],z) = \operatorname{tr}\bigl(\operatorname{ad}x(\operatorname{ad}y\,\operatorname{ad}z - \operatorname{ad}z\,\operatorname{ad}y)\bigr) = \operatorname{tr}\bigl(\operatorname{ad}x\,\operatorname{ad}[y,z]\bigr) = \kappa(x,[y,z]).$$

最后一个等号用了 $$\operatorname{ad}[y,z]=[\operatorname{ad}y,\operatorname{ad}z]$$。$$\blacksquare$$

**定理 3.15（Cartan 第一判据, 可解性）**。$$L$$ 可解 $$\iff$$ $$\kappa(x,y)=0$$ 对一切 $$x\in L,\ y\in[L,L]$$。

**定理 3.16（Cartan 第二判据, 半单性）**。$$L$$ 半单 $$\iff$$ $$\kappa$$ 非退化。

*证明（$$\Leftarrow$$）*：设 $$\kappa$$ 非退化而 $$L$$ 非半单，即存在非零可解理想 $$I$$。沿 $$I$$ 的导出列取最后一个非零项 $$A:=I^{(n)}$$（$$n$$ 最大且 $$I^{(n)}\neq0$$），则

$$[A,A] = I^{(n+1)} = 0,$$

即 $$A$$ 是非零交换理想。取 $$a\in A$$ 与任意 $$x\in L$$。因 $$A$$ 是理想，$$\operatorname{ad}a$$ 把 $$L$$ 打进 $$A$$；又因 $$[A,A]=0$$，$$\operatorname{ad}a$$ 零化 $$A$$。于是在复合

$$L\xrightarrow{\ \operatorname{ad}x\ }L\xrightarrow{\ \operatorname{ad}a\ }A\xrightarrow{\ \operatorname{ad}x\ }L\xrightarrow{\ \operatorname{ad}a\ }A$$

中最后一步为零，故 $$(\operatorname{ad}a\operatorname{ad}x)^2=0$$，即 $$\operatorname{ad}a\operatorname{ad}x$$ 幂零。幂零算子的迹为零，故 $$\kappa(a,x)=\operatorname{tr}(\operatorname{ad}a\operatorname{ad}x)=0$$ 对一切 $$x\in L$$，与 $$\kappa$$ 非退化矛盾（$$a\neq0$$ 却与全体正交）。故 $$L$$ 半单。

*证明（$$\Rightarrow$$）*：设 $$L$$ 半单。用结合不变性可证 $$\kappa$$ 的根 $$\operatorname{Rad}\kappa=\{x : \kappa(x,L)=0\}$$ 是理想：若 $$x\in\operatorname{Rad}\kappa$$，则对一切 $$y,z\in L$$ 有 $$\kappa([x,y],z)=\kappa(x,[y,z])=0$$，故 $$[x,y]\in\operatorname{Rad}\kappa$$。再把第一判据用于 $$\operatorname{Rad}\kappa$$：取 $$x\in\operatorname{Rad}\kappa$$、$$y\in[\operatorname{Rad}\kappa,\operatorname{Rad}\kappa]\subseteq L$$ 有 $$\kappa(x,y)=0$$，故 $$\operatorname{Rad}\kappa$$ 可解。它是可解理想，而 $$L$$ 半单意味着没有非零可解理想，故 $$\operatorname{Rad}\kappa=0$$。$$\blacksquare$$

**推论 3.17**。设 $$L$$ 半单，$$I\lhd L$$。则 $$\kappa\vert_I$$ 等于 $$I$$ 作为独立 Lie 代数的 Killing 型；特别地 $$I\cap I^\perp = 0$$（$$I^\perp$$ 是 $$I$$ 关于 $$\kappa$$ 的正交补）。

*证明思路*：对 $$x,y\in I$$，$$\operatorname{ad}_L x\operatorname{ad}_L y$$ 把 $$L$$ 打进 $$I$$（$$I$$ 是理想），故在 $$L/I$$ 上给出的算子为零（$$x,y\in I$$ 使两者在商上为 $$0$$），迹的贡献全来自 $$I$$ 内部：$$\operatorname{tr}_L(\operatorname{ad}x\operatorname{ad}y)=\operatorname{tr}_I(\operatorname{ad}_Ix\operatorname{ad}_Iy)=\kappa_I(x,y)$$。至于 $$I\cap I^\perp$$：取 $$x\in I\cap I^\perp$$，则 $$\kappa(x,I)=0$$，同 定理 3.16 的论证可知 $$I\cap I^\perp$$ 可解，故为 $$0$$。$$\blacksquare$$

**定理 3.18（抽象 Jordan 分解, abstract Jordan decomposition）**。设 $$L$$ 半单，$$x\in L$$。则存在唯一的一对 $$x_s,x_n\in L$$ 使

$$x = x_s+x_n,\qquad \operatorname{ad}x_s\ \text{半单},\quad \operatorname{ad}x_n\ \text{幂零},\quad [x_s,x_n]=0,$$

并且对任意有限维表示 $$\rho$$ 有 $$\rho(x_s)=\rho(x)_s$$、$$\rho(x_n)=\rho(x)_n$$。

*为什么重要*：半单 Lie 代数的每个元素自带一个不依赖任何表示的分解。$$x_s$$（可对角化部分）正是 Cartan 子代数的原料，$$x_n$$（幂零部分）负责根空间的非零性。它是我们能对 $$\operatorname{ad}$$ 同时对角化的合法性来源。

### 3.3 Cartan 子代数与根空间分解

从这一段起，假设 $$L$$ 是半单复 Lie 代数。**目标是什么**：$$\operatorname{ad}x$$ 对单个 $$x$$ 不一定能对角化（它可能有幂零部分），但我们想找一族"够大、又能同时对角化"的元素，把 $$L$$ 整体按共同本征空间拆开（第55章 3.3 节已经用两个具体的对角矩阵 $$h_1,h_2$$ 在 $$\mathfrak{sl}(3,\mathbb C)$$ 里做过一次）。下面的定义就是在精确化"够大"与"能同时对角化"这两个要求。

**定义 3.19（环面子代数与 Cartan 子代数, toral subalgebra and Cartan subalgebra）**。称子代数 $$H\subseteq L$$ 是**环面的** (toral)，若每个 $$h\in H$$ 的 $$\operatorname{ad}_L h$$ 半单（可对角化）。称 $$H$$ 是 **Cartan 子代数** (Cartan subalgebra, CSA)，若 $$H$$ 幂零且自正规化，即

$$N_L(H) := \{x\in L : [x,H]\subseteq H\} = H .$$

记 $$\ell = \dim H$$，称为 $$L$$ 的**秩** (rank)。

**定理 3.20（Cartan 子代数的基本性质）**。设 $$L$$ 半单，$$H$$ 是 Cartan 子代数。则

**(i)** $$H$$ 交换，且每个 $$\operatorname{ad}h$$（$$h\in H$$）可同时对角化；

**(ii)** $$H$$ 等于某个极大环面子代数，且 $$L$$ 中所有极大环面子代数都互相共轭（故 $$\ell$$ 与 $$H$$ 的选取无关）；

**(iii)** $$\kappa\vert_H$$ 非退化。

*说明*：这是一条「存在性 + 唯一性 + 良好性」的定理。(i) 的理由：$$H$$ 幂零使 $$\operatorname{ad}_H h$$ 幂零，环面性使 $$\operatorname{ad}_L h$$（从而其限制）半单；半单且幂零的算子必为零，故 $$[H,H]=0$$，即 $$H$$ 交换。三条均作为本课采用的基本事实（完整证明见 Humphreys §15–16），下面的推导只用到它们。

**(iii) 的证明**：设 $$h\in H$$ 且 $$\kappa(h,H)=0$$，证 $$h=0$$。由 定理 3.22 的分解（下面给证）$$L = H\oplus\bigoplus_{\alpha\neq 0}L_\alpha$$。取 $$x\in L_\alpha$$（$$\alpha\neq0$$）：$$\operatorname{ad}h\operatorname{ad}x$$ 把权空间 $$L_\beta$$ 送进 $$L_{\beta+\alpha}$$，权重集有限而每步严格平移，故该算子幂零，迹为零，于是

$$\kappa(h,x) = \operatorname{tr}(\operatorname{ad}h\operatorname{ad}x) = 0 .$$

又由假设 $$\kappa(h,H)=0$$，而 $$L=H\oplus\bigoplus_{\alpha\neq0}L_\alpha$$，故 $$\kappa(h,L)=0$$。由 定理 3.16 的 $$\kappa$$ 非退化得 $$h=0$$。$$\blacksquare$$

**从"同时对角化"到"根"**：定理 3.20(i) 说全体 $$\operatorname{ad}h$$（$$h\in H$$）可以同时对角化，于是 $$L$$ 的每个共同本征空间由"每个 $$h$$ 上取值多少"这一整条规则决定，而不是由单个数字决定——这条规则本身就是 $$H$$ 上的一个线性泛函。第55章 3.3 节用两个具体的对角矩阵 $$h_1,h_2$$ 给 $$\mathfrak{sl}(3,\mathbb C)$$ 的六个方向各配了一对坐标 $$(c_1,c_2)$$；这里把"配一对坐标"精确化成"配一个线性泛函 $$\alpha\in H^*$$"。

**定义 3.21（根与根空间, roots and root spaces）**。对 $$\alpha\in H^*$$ 定义

$$L_\alpha = \{x\in L : [h,x]=\alpha(h)x\ \ \forall h\in H\}.$$

若 $$\alpha\neq 0$$ 且 $$L_\alpha\neq 0$$，称 $$\alpha$$ 为**根** (root)，$$L_\alpha$$ 为**根空间** (root space)。全体根记 $$\Phi\subset H^*$$。

**定理 3.22（根空间分解, root space decomposition）**。$$L = H\oplus\bigoplus_{\alpha\in\Phi}L_\alpha$$，即 $$L_0=H$$ 且 $$L$$ 是这些（互相独立的）特征空间的直和。

*证明*：由 定理 3.20(i)，$$\{\operatorname{ad}h\}_{h\in H}$$ 是一族可同时对角化的算子。故 $$L=\bigoplus_{\alpha\in H^*}L_\alpha$$ 是直和分解。$$L_0 = \{x : [H,x]=0\} = C_L(H)$$（$$H$$ 的中心化子）。余下只需证 $$C_L(H)=H$$。

一方面 $$H\subseteq C_L(H)$$（由 $$H$$ 交换）。另一方面设 $$x\in C_L(H)$$，用 定理 3.18 写 $$x = x_s+x_n$$。

**$$x_s\in H$$**：把 $$\operatorname{ad}x$$ 限制在交换子代数 $$H$$ 上，它是零算子，而 $$\operatorname{ad}x\vert_H = \operatorname{ad}x_s\vert_H+\operatorname{ad}x_n\vert_H$$ 是「半单 + 幂零」且两者交换，故和为零迫使两者各自为零（把两者同时化为 Jordan 型：半单的是对角、幂零的是严格上三角）。于是 $$[x_s,H]=[x_n,H]=0$$。又 $$\operatorname{ad}x_s$$ 半单，故 $$H+\mathbb Cx_s$$ 是环面子代数（交换性来自 $$[x_s,H]=0$$，半单性来自两个交换的可对角化算子之和），由 $$H$$ 极大（定理 3.20(ii)）得 $$x_s\in H$$。

**$$x_n=0$$**：此时 $$x_n\in C_L(H)$$、$$\operatorname{ad}x_n$$ 幂零、$$[x_n,H]=0$$。若 $$x_n\neq0$$，则 $$K:=H+\mathbb Cx_n$$ 满足 $$[K,K]\subseteq\mathbb Cx_n$$，故 $$K^{2}=0$$，即 $$K$$ 交换。但 $$H$$ 是极大环面子代数，而「极大环面子代数在含它的任意子代数中仍是该子代数的极大环面」（标准事实，同样由抽象 Jordan 分解与极大性给出，见 Humphreys §15.3），于是 $$K$$ 中一切元素必须 $$\operatorname{ad}$$ 半单；而 $$x_n\neq0$$ 时 $$\operatorname{ad}x_n$$ 幂零且非零（它在某个根空间上作非零平移），矛盾。故 $$x_n=0$$。

于是 $$C_L(H)\subseteq H$$，与 $$H\subseteq C_L(H)$$ 合起来得 $$C_L(H)=H$$，即 $$L_0=H$$。$$\blacksquare$$

**定理 3.23（根空间的结构事实）**。设 $$\alpha,\beta\in\Phi\cup\{0\}$$。

**(i)** $$[L_\alpha,L_\beta]\subseteq L_{\alpha+\beta}$$；

**(ii)** $$\kappa(L_\alpha,L_\beta)=0$$，除非 $$\alpha+\beta=0$$；

**(iii)** $$\alpha\in\Phi\Rightarrow-\alpha\in\Phi$$，且 $$\kappa\vert_{L_\alpha\oplus L_{-\alpha}}$$ 非退化；

**(iv)** 每个 $$L_\alpha$$（$$\alpha\in\Phi$$）是**一维**的。

*证明*：**(i)** 对 $$x\in L_\alpha$$、$$y\in L_\beta$$、$$h\in H$$，用 Jacobi 恒等式：

$$[h,[x,y]] = [[h,x],y] + [x,[h,y]] = \alpha(h)[x,y] + \beta(h)[x,y] = (\alpha+\beta)(h)\,[x,y],$$

这正是说 $$[x,y]\in L_{\alpha+\beta}$$（若 $$\alpha+\beta$$ 不是权，则相应空间为零，$$[x,y]=0$$）。

**(ii)** 取 $$x\in L_\alpha$$、$$y\in L_\beta$$。由 (i)，$$\operatorname{ad}x\circ\operatorname{ad}y$$ 把每个 $$L_\gamma$$ 送进 $$L_{\gamma+\alpha+\beta}$$。若 $$\alpha+\beta\neq 0$$，把 $$\Phi\cup\{0\}$$ 按映射 $$\gamma\mapsto\gamma+\alpha+\beta$$ 分成有限条轨道（每条轨道是 $$L$$ 的若干权空间排成的一个有限链，链的末端之后为零）。$$\operatorname{ad}x\circ\operatorname{ad}y$$ 保持每条轨道的张成空间并把它沿链推进一步，故在这条链上的矩阵是严格上三角的，迹为零。把 $$L$$ 按轨道分解成直和，$$\kappa(x,y)=\operatorname{tr}(\operatorname{ad}x\circ\operatorname{ad}y)$$ 是这些零迹算子之和，故为零。

**(iii)** 若 $$\alpha\in\Phi$$ 而 $$-\alpha\notin\Phi$$，则 $$L_{-\alpha}=0$$。由 (ii)，$$\kappa(L_\alpha,L_\gamma)=0$$ 对一切 $$\gamma\neq-\alpha$$ 成立，而 $$\gamma=-\alpha$$ 时 $$L_\gamma=0$$；又 $$\kappa(L_\alpha,L_0)=\kappa(L_\alpha,H)=0$$（$$0+\alpha=\alpha\neq0$$ 仍由 (ii)）。故 $$\kappa(L_\alpha,L)=0$$，与 $$\kappa$$ 非退化（定理 3.16）矛盾。所以 $$-\alpha\in\Phi$$。至于非退化性：$$\kappa$$ 在 $$L_\alpha\oplus L_{-\alpha}$$ 上的限制是这一块与其余部分的正交配对的「对角块」，整体非退化迫使每块非退化。

**(iv)** 我们先搭出 $$\mathfrak{sl}(2)$$ 的三元组，再用入口题 (ii)(iii) 的结论。

**第一小步：$$[L_\alpha,L_{-\alpha}]$$ 是一维的。** 由 (iii)，$$\kappa\vert_{L_\alpha\oplus L_{-\alpha}}$$ 非退化，故存在 $$x\in L_\alpha$$、$$y\in L_{-\alpha}$$ 使 $$\kappa(x,y)\neq 0$$。对任意 $$h\in H$$，用结合不变性：

$$\kappa\bigl(h,[x,y]\bigr) = \kappa\bigl([h,x],y\bigr) = \alpha(h)\,\kappa(x,y) .$$

注意 $$\kappa(x,y)\neq 0$$，而 $$h\mapsto \alpha(h)$$ 是 $$H^*$$ 中的固定元素。由 定理 3.20(iii)，$$\kappa\vert_H$$ 非退化，故存在唯一 $$t_\alpha\in H$$ 使 $$\alpha(h)=\kappa(t_\alpha,h)$$ 对一切 $$h$$ 成立。于是上式读作

$$\kappa\bigl(h,[x,y]\bigr) = \kappa(x,y)\,\kappa(t_\alpha,h) = \kappa\bigl(\kappa(x,y)t_\alpha,\ h\bigr).$$

由于 $$\kappa\vert_H$$ 非退化，这给出 $$[x,y]=\kappa(x,y)\,t_\alpha$$。所以 $$[L_\alpha,L_{-\alpha}]\subseteq\mathbb C t_\alpha$$；又上面已取到 $$\kappa(x,y)\neq0$$，故

$$[L_\alpha,L_{-\alpha}] = \mathbb C t_\alpha,\qquad \dim [L_\alpha,L_{-\alpha}]=1 .$$

**第二小步：三元组。** 由 $$\kappa(t_\alpha,t_\alpha)\neq 0$$（否则 $$\alpha(t_\alpha)=\kappa(t_\alpha,t_\alpha)=0$$，与 $$\alpha\neq0$$ 矛盾），令

$$h_\alpha := \frac{2\,t_\alpha}{\kappa(t_\alpha,t_\alpha)},\qquad\text{则}\ \alpha(h_\alpha)=2 .$$

取 $$x\in L_\alpha$$ 非零。由第一小步，$$[x,L_{-\alpha}]\subseteq\mathbb C t_\alpha$$，且映射 $$y\mapsto[x,y]$$ 从 $$L_{-\alpha}$$ 到 $$\mathbb C t_\alpha$$ 不为零（否则 $$\kappa(x,L_{-\alpha})=0$$，与 $$[x,y]=\kappa(x,y)t_\alpha$$ 中取 $$\kappa(x,y)\neq0$$ 矛盾）。故存在 $$y\in L_{-\alpha}$$ 使 $$[x,y]=h_\alpha$$。三个元素满足

$$[h_\alpha,x]=\alpha(h_\alpha)x=2x,\qquad [h_\alpha,y]=-\alpha(h_\alpha)y=-2y,\qquad [x,y]=h_\alpha,$$

与 入口题 (i) 里 $$\mathfrak{sl}(2,\mathbb C)$$ 的三条标准关系逐字相同。故 $$S_\alpha:=\mathbb C x\oplus\mathbb Cy\oplus\mathbb Ch_\alpha\cong\mathfrak{sl}(2,\mathbb C)$$。

**第三小步：$$\dim L_\alpha=1$$。** 令 $$W$$ 为 $$x$$ 在 $$S_\alpha$$ 作用下生成的子模。$$x$$ 是权 $$2$$ 的权向量，故 $$W$$ 由最高权向量生成，因而同构于某个不可约模 $$V(m)$$ 的商。$$W\ni x,\ [y,x]=-h_\alpha\neq0,\ [y,[y,x]]=2y\neq0$$，故 $$\dim W\ge3$$；而 $$V(2)$$ 是三维的、$$V(m)$$（$$m\ge3$$）维数更大，商只使维数下降，故 $$m=2$$、$$W=V(2)$$，从而 $$W$$ 的权 $$2$$ 空间 $$W_2=\mathbb C x$$ 一维。由 $$W_2\subseteq L_\alpha$$ 得 $$\dim L_\alpha=1$$。$$\blacksquare$$

**定理 3.24（每个根配一个 $$\mathfrak{sl}(2)$$）**。对每个 $$\alpha\in\Phi$$，可取 $$x_\alpha\in L_\alpha$$、$$y_\alpha\in L_{-\alpha}$$ 使 $$[x_\alpha,y_\alpha]=h_\alpha$$ 且 $$\alpha(h_\alpha)=2$$，并且

$$S_\alpha := \mathbb C x_\alpha\oplus \mathbb C y_\alpha\oplus \mathbb C h_\alpha\cong\mathfrak{sl}(2,\mathbb C),$$

同构由 $$x_\alpha\mapsto E$$、$$y_\alpha\mapsto F$$、$$h_\alpha\mapsto H$$ 给出。

*意义*：这是「把 $$\mathfrak{sl}(2)$$ 理论嵌入任意半单 Lie 代数」的唯一通道——**本章后面每个关于根的论断，最终都靠它退化到入口题 (ii)(iii)。**

**例 3.25（$$\mathfrak{sl}(n+1,\mathbb C)$$ 的根空间分解）**。取 $$L=\mathfrak{sl}(n+1,\mathbb C)$$，$$H=$$ 迹零对角矩阵（秩 $$n$$ 的 Cartan 子代数）。令 $$E_{ij}$$（$$i\neq j$$）为矩阵单位，并定义 $$\varepsilon_i(\operatorname{diag}(a_1,\dots,a_{n+1}))=a_i$$。对 $$h=\operatorname{diag}(a_1,\dots,a_{n+1})$$ 直算得

$$[h,E_{ij}] = (a_i-a_j)E_{ij} = (\varepsilon_i-\varepsilon_j)(h)\,E_{ij},\qquad\text{故}\ \Phi = \{\varepsilon_i-\varepsilon_j : i\neq j\},\ \lvert\Phi\rvert=n(n+1).$$

取 $$n=1$$：$$\Phi=\{\pm(\varepsilon_1-\varepsilon_2)\}$$，两根互为相反向量——正是入口题 (viii) 里那个「孤立顶点」。

取 $$n=2$$：$$\Phi$$ 有 $$6$$ 根，且 $$\varepsilon_1-\varepsilon_3=(\varepsilon_1-\varepsilon_2)+(\varepsilon_2-\varepsilon_3)$$。六个向量两两成 $$60^\circ$$ 或 $$120^\circ$$、均匀分布在一个平面里——这就是 $$A_2$$（精确内积在 题 2 里算）。

### 3.4 根系：把根抽成独立的几何对象

现在做本章最关键的一次「抽象」：把 $$H$$ 和 $$\kappa$$ 丢掉，只留下 $$\Phi$$ 与它上面由 $$\kappa$$ 诱导的内积。**为什么可以丢掉 $$L$$ 本身**：下面四条公理只谈论一个有限向量集合与它的内积，不再提到 Lie 括号；这是因为定理 3.23、3.24 已经把 $$L$$ 的全部结构信息（哪些和是根、每个根空间多大、根的相反数是不是根）翻译成了纯几何陈述。第55章 3.4 节用一对具体的不等长向量算过 Cartan 整数与反射，这里把那次具体计算里用到的全部规则收进四条公理，使它们对任意根系都成立。

**定义 3.26（根系, root system）**。设 $$E$$ 是有限维实欧氏空间（内积记 $$(\cdot,\cdot)$$）。称有限集合 $$\Phi\subset E$$ 为**根系**，若

**(R1)** $$\Phi$$ 有限、张成 $$E$$，且 $$0\notin\Phi$$；

**(R2)** 若 $$\alpha\in\Phi$$，则 $$\alpha$$ 的实数倍数中只有 $$\pm\alpha$$ 落在 $$\Phi$$ 里；

**(R3)** 对 $$\alpha,\beta\in\Phi$$，反射

$$\sigma_\alpha(\beta) = \beta - \langle\beta,\alpha\rangle\alpha,\qquad \langle\beta,\alpha\rangle := \frac{2(\beta,\alpha)}{(\alpha,\alpha)}$$

满足 $$\sigma_\alpha(\beta)\in\Phi$$；

**(R4)**（整性, integrality）$$\langle\beta,\alpha\rangle\in\mathbb Z$$ 对一切 $$\alpha,\beta\in\Phi$$。

这里 $$\langle\beta,\alpha\rangle$$ 称为 **Cartan 整数** (Cartan integer) 或 **Cartan 配对**。

**定理 3.27（半单 Lie 代数的根集是根系）**。设 $$L$$ 半单，$$\Phi$$ 是它的根集。把 $$\kappa$$ 搬到 $$H^*$$ 上：对 $$\alpha\in H^*$$，令 $$t_\alpha\in H$$ 由 $$\alpha(\cdot)=\kappa(t_\alpha,\cdot)$$ 唯一确定，再定义

$$(\alpha,\beta) := \kappa(t_\alpha,t_\beta),\qquad E := \mathbb R\Phi .$$

则 $$E$$ 是实欧氏空间，$$(\cdot,\cdot)$$ 在其上正定，且 $$\Phi$$ 满足 (R1)–(R4)。

*证明思路*：$$E=\mathbb R\Phi$$ 是实向量空间，$$(\cdot,\cdot)$$ 正定来自 $$\kappa$$ 在实形式上的正定性（要用到 $$\kappa$$ 是迹型且 $$L$$ 半单）。(R1)（有限、张成、不含 $$0$$）与 (R2)（只有 $$\pm\alpha$$）已由 定理 3.23 与我们上面的证明给出。(R3) 的反射 $$\sigma_\alpha$$ 对应于自同构 $$\exp(\operatorname{ad}x_\alpha)\exp(\operatorname{ad}y_\alpha)\exp(\operatorname{ad}x_\alpha)$$（Weil 的 $$\mathfrak{sl}(2)$$ 技巧）在 $$H^*$$ 上的作用，而自同构保根集。(R4) 是 定理 3.28 的整性。

**定理 3.28（整性：$$\alpha$$-弦公式）**。设 $$\alpha,\beta\in\Phi$$，且 $$\beta\notin\mathbb Z\alpha$$（即 $$\beta$$ 不是 $$\alpha$$ 的整数倍）。把形如 $$\beta+k\alpha$$ 的根排成一串连续整数：

$$\beta-q\alpha,\ \beta-(q-1)\alpha,\ \dots,\ \beta,\ \dots,\ \beta+p\alpha$$

（即 $$q\ge 0$$、$$p\ge 0$$ 是使这些项都在 $$\Phi$$ 中的最大范围）。则

$$\langle\beta,\alpha\rangle = q-p\qquad\Longleftrightarrow\qquad p-q = -\langle\beta,\alpha\rangle .$$

（记法约定：$$q$$ 沿 $$-\alpha$$ 方向、$$p$$ 沿 $$+\alpha$$ 方向。本章统一用 $$\langle\beta,\alpha\rangle=q-p$$，与 $$\sigma_\alpha(\beta)=\beta-\langle\beta,\alpha\rangle\alpha$$、$$\langle\beta,\alpha\rangle=\frac{2(\beta,\alpha)}{(\alpha,\alpha)}$$ 及标准 Cartan 矩阵（$$A_2$$ 的 $$\langle\alpha_1,\alpha_2\rangle=-1$$）一致。）

*证明*：**第一步（弦是连续的一段）。** 记 $$K := \{k\in\mathbb Z : \beta+k\alpha\in\Phi\}$$、$$M := \bigoplus_{k\in K}L_{\beta+k\alpha}$$。由 定理 3.24 取出 $$S_\alpha\cong\mathfrak{sl}(2,\mathbb C)$$：其升权算子 $$x\in L_\alpha$$ 把 $$L_{\beta+k\alpha}$$ 送进 $$L_{\beta+(k+1)\alpha}$$、降权算子 $$y\in L_{-\alpha}$$ 送进 $$L_{\beta+(k-1)\alpha}$$、$$h_\alpha$$ 保持每项（定理 3.23(i)），故 $$M$$ 是 $$S_\alpha$$-模。

把 $$M$$ 分解为不可约 $$S_\alpha$$-模的直和。由 入口题 (iii)，每块的权集是步长 $$2$$、关于 $$0$$ 对称的等差链 $$\{m_j,m_j-2,\dots,-m_j\}$$；而 $$h_\alpha$$ 在 $$M$$ 上的本征值恰是 $$\{\beta(h_\alpha)+2k : k\in K\}$$，即若干条这样的对称链之并。若 $$K$$ 在相邻两项间有空隙，并集中就出现一个无法由对称等差链拼出的洞（相邻权值之差 $$\ge4$$ 时没有步长 $$2$$ 的链能跨越它）。故 $$K$$ 是连续区间：

$$K = \{-q,-q+1,\dots,p\},\qquad q,p\ge 0 .$$

**第二步（对称性定出端点）。** 权集最大的那块记为 $$V(m)$$，其最大权 $$m$$ 就是 $$M$$ 的最大权值；该块关于 $$0$$ 对称，故 $$-m$$ 也是 $$M$$ 的权值，即 $$M$$ 的最小权值。由于 $$k\mapsto\beta(h_\alpha)+2k$$ 单调递增，最大、最小分别取在 $$k=p$$ 与 $$k=-q$$，于是

$$\beta(h_\alpha)+2p = m,\qquad \beta(h_\alpha)-2q = -m\ \Longrightarrow\ 2\beta(h_\alpha)+2(p-q)=0\ \Longrightarrow\ \beta(h_\alpha)=q-p .$$

**第三步（认出 $$\beta(h_\alpha)$$）。** 由 定理 3.24，$$h_\alpha=\frac{2t_\alpha}{\kappa(t_\alpha,t_\alpha)}$$，其中 $$t_\alpha$$ 是 $$\alpha$$ 在 $$\kappa$$ 下的对偶。于是

$$\beta(h_\alpha) = \frac{2\kappa(t_\beta,t_\alpha)}{\kappa(t_\alpha,t_\alpha)} = \frac{2(\beta,\alpha)}{(\alpha,\alpha)} = \langle\beta,\alpha\rangle .$$

代入第二步即得 $$\langle\beta,\alpha\rangle=q-p$$。**证毕。**$$\blacksquare$$

*由定理 3.28 立即得到 **(R4)**：$$\langle\beta,\alpha\rangle=q-p\in\mathbb Z$$。*（方向：弦「向下」的步数 $$q$$ 减去「向上」的步数 $$p$$ 等于 $$\langle\beta,\alpha\rangle$$。）

**（R2）对 Lie 代数的根成立：证明**。设 $$\alpha\in\Phi$$，记 $$K=\{j\in\mathbb Z : j\alpha\in\Phi\}$$、$$M=\max K\ (\ge1)$$。由 定理 3.23(iii)，$$K$$ 关于 $$0$$ 对称，故只需证 $$M=1$$。

**第一步：$$M\mid2$$。** 把 定理 3.28 用于配对 $$(\beta,\alpha')=(\alpha,M\alpha)$$（$$M\ge2$$ 时 $$\alpha\notin\mathbb Z(M\alpha)$$，定理适用；所需的模 $$\bigoplus_kL_{(1+kM)\alpha}$$ 确实是 $$S_{M\alpha}$$-模，且不含 $$L_0$$，与定理证明的要求一致）。定理给出

$$\langle\alpha,M\alpha\rangle = \frac{2(\alpha,M\alpha)}{(M\alpha,M\alpha)} = \frac{2M}{M^2} = \frac2M \in\mathbb Z\ \Longrightarrow\ M\mid2 .$$

**第二步：$$M\ne2$$。** 设 $$M=2$$，取非零 $$z\in L_{2\alpha}$$。因 $$3\alpha\notin\Phi$$，$$[x,z]\in L_{3\alpha}=0$$（$$x\in L_\alpha$$），故 $$z$$ 是 $$S_\alpha$$ 的**最高权向量**，权为 $$(2\alpha)(h_\alpha)=4$$。由泛性质，$$v_0\mapsto z$$ 给出 $$S_\alpha$$-模同态 $$V(4)\to L$$，像即 $$z$$ 生成的子模。$$V(4)$$ 不可约、维数 $$5$$、权集 $$\{4,2,0,-2,-4\}$$，像非零故 $$\cong V(4)$$；于是像中有权 $$-4$$ 的非零向量，即 $$-4\alpha\in\Phi$$。再由 定理 3.23(iii)，$$4\alpha\in\Phi$$，与 $$M=2$$ 是最大者矛盾。

故 $$M=1$$，即 $$K=\{\pm1\}$$。(R2) 证毕。$$\blacksquare$$

（把这一条与 (R1)(R3)(R4) 合起来即得 定理 3.27：半单 Lie 代数的根集满足根系的全部四条公理。本章后面的分类只用四条公理，不再回头用 Lie 代数。）

**定理 3.29（夹角只有七种）**。设 $$\alpha,\beta\in\Phi$$ 不共线。则

$$\langle\alpha,\beta\rangle\langle\beta,\alpha\rangle = 4\cos^2\theta\in\{0,1,2,3\},$$

其中 $$\theta$$ 是 $$\alpha,\beta$$ 的夹角。**去掉 $$\langle\alpha,\beta\rangle\langle\beta,\alpha\rangle = 4$$ 的情形**（那只在 $$\alpha$$ 与 $$\beta$$ 共线、即 $$\beta=\pm\alpha$$ 时发生）。于是 $$\theta$$ 只能取

$$90^\circ,\ 60^\circ,\ 120^\circ,\ 45^\circ,\ 135^\circ,\ 30^\circ,\ 150^\circ .$$

若 $$\lvert\alpha\rvert\le\lvert\beta\rvert$$，则对应的 $$\langle\beta,\alpha\rangle,\langle\alpha,\beta\rangle$$ 依次为

$$\frac{\lvert\beta\rvert}{\lvert\alpha\rvert}\in\{1,\sqrt2,\sqrt3\}\ \text{按角度分配}:\quad (\theta=90^\circ):(0,0);\quad(\theta=120^\circ,60^\circ):(-1,-1);\quad(\theta=135^\circ,45^\circ):(-2,-1);\quad(\theta=150^\circ,30^\circ):(-3,-1).$$

（符号由「$$\alpha\neq\beta$$ 非共线时可取二者夹角为钝角」的约定给出；交换 $$\alpha,\beta$$ 则两个整数互换。）

*证明*：由 (R4)，$$\langle\alpha,\beta\rangle,\langle\beta,\alpha\rangle$$ 都是整数。设 $$\lvert\alpha\rvert\le\lvert\beta\rvert$$ 且夹角 $$\theta$$ 为钝角（若为锐角则把 $$\beta$$ 换成 $$-\beta$$，$$\langle-\beta,\alpha\rangle=-\langle\beta,\alpha\rangle$$，仍为整数）。于是

$$0\ge \langle\beta,\alpha\rangle = \frac{2\lvert\beta\rvert\lvert\alpha\rvert\cos\theta}{\lvert\alpha\rvert^2} = 2\frac{\lvert\beta\rvert}{\lvert\alpha\rvert}\cos\theta,$$

$$\langle\alpha,\beta\rangle = 2\frac{\lvert\alpha\rvert}{\lvert\beta\rvert}\cos\theta .$$

两者都是非正整数，且乘积

$$\langle\alpha,\beta\rangle\langle\beta,\alpha\rangle = 4\cos^2\theta .$$

令 $$r=\lvert\beta\rvert/\lvert\alpha\rvert\ge 1$$，则 $$\langle\beta,\alpha\rangle = -n$$（$$n$$ 非负整数），$$\langle\alpha,\beta\rangle = -m$$（$$m$$ 非负整数），且

$$4\cos^2\theta = nm,\qquad r = \sqrt{\frac{n}{m}},\qquad r\ge 1\Rightarrow n\ge m .$$

由 $$\cos^2\theta<1$$（非共线）得 $$nm\in\{0,1,2,3\}$$。逐个枚举（$$r\ge1$$ 故 $$n\ge m$$）：

- $$nm=0$$：$$\cos\theta=0$$，$$\theta=90^\circ$$，$$r$$ 任意；
- $$nm=1$$：$$m=n=1$$，$$\theta=120^\circ$$ 或 $$60^\circ$$，$$r=1$$（等长）；
- $$nm=2$$：$$\{m,n\}=\{1,2\}$$，$$\theta=135^\circ$$ 或 $$45^\circ$$，$$r=\sqrt2$$；
- $$nm=3$$：$$\{m,n\}=\{1,3\}$$，$$\theta=150^\circ$$ 或 $$30^\circ$$，$$r=\sqrt3$$。

（$$nm=4$$ 给出 $$\cos^2\theta=1$$，即共线，由 (R2) 已排除。）枚举完毕。$$\blacksquare$$

*这正是入口题 (vii) 的完整解答。*而它立刻带来分类上的后果：**两根的相对长度比只能是 $$1,\sqrt2,\sqrt3$$，且夹角落在七个值里。** 有限个长度比、有限个角度，意味着「画出一张有限图」是可能的——这就是 3.5 段要做的事。

### 3.5 单根、Dynkin 图与分类定理

**为什么要从 $$\Phi$$ 里再挑出一个"基"**：$$\Phi$$ 本身有 $$n(n+1)$$ 个（甚至更多）根，直接罗列所有根很冗余——第55章 3.3 节的六个根里，其实只要两个（$$\alpha_1=\varepsilon_1-\varepsilon_2,\ \alpha_2=\varepsilon_2-\varepsilon_3$$）就能把其余四个（包括它们各自的相反数）用整系数组合表示出来。下面的定义把"最省的一组生成元"精确化。

**定义 3.30（基与单根, base and simple roots）**。$$\Phi$$ 的子集 $$\Delta$$ 称为一个**基** (base)，若

**(B1)** $$\Delta$$ 是 $$E$$ 的一组基；

**(B2)** 每个 $$\beta\in\Phi$$ 可唯一地写成 $$\beta = \sum_{\alpha\in\Delta}k_\alpha\alpha$$，其中系数 **要么全为非负整数，要么全为非正整数**。

$$\Delta$$ 中的元素称**单根** (simple root)；系数全非负的根组成**正根集** $$\Phi^+$$，全非正的组成**负根集** $$\Phi^-$$。

**命题 3.31（基的存在性）**。$$E$$ 中存在不与任何根正交的向量 $$\gamma$$（称**正则元**, regular element）。对这样的 $$\gamma$$ 令

$$\Phi^+(\gamma) = \{\alpha\in\Phi : (\alpha,\gamma)>0\},\qquad \Delta(\gamma) = \{\alpha\in\Phi^+(\gamma) : \alpha\ \text{不能写成}\ \Phi^+(\gamma)\ \text{中两个元素之和}\}.$$

则 $$\Delta(\gamma)$$ 是一个基，且 $$\Phi^+(\gamma)$$ 是对应的正根集。

*证明思路*：正则元存在，因为有限个超平面 $$\alpha^\perp$$（$$\alpha\in\Phi$$）的并是有限个真子空间之并，不可能覆盖 $$E$$（它是一个测度为零的闭集）。剩下两步：先证每个正根都是 $$\Delta(\gamma)$$ 的非负整组合（对根的高度 $$(\alpha,\gamma)$$ 归纳：若 $$\alpha\notin\Delta(\gamma)$$ 则 $$\alpha=\alpha_1+\alpha_2$$，两者都是正根且高度更小）；再证 $$\Delta(\gamma)$$ 线性无关（引理：一族两两内积 $$\le0$$ 的向量，若某个非负实系数组合为零，则除一项外系数全为 $$0$$）。两句合起来给出 (B1)(B2)。$$\blacksquare$$

**命题 3.32（单根的两条基本性质）**。

**(i)** 若 $$\alpha\neq\beta\in\Delta$$，则 $$(\alpha,\beta)\le 0$$（即 $$\langle\alpha,\beta\rangle\in\{0,-1,-2,-3\}$$，夹角为钝角或直角）。

**(ii)** $$\Phi^+$$ 恰是 $$\Delta$$ 的非负整组合中非零的那些，$$\Phi^-$$ 恰是负组合。

*证明*：**(i)** 设 $$\alpha\neq\beta$$ 都是单根而 $$(\alpha,\beta)>0$$，则 $$\langle\beta,\alpha\rangle=2(\beta,\alpha)/(\alpha,\alpha)\ge1$$。把 $$\sigma_\alpha(\beta)=\beta-\langle\beta,\alpha\rangle\alpha$$ 按基 $$\Delta$$ 展开：$$\beta$$ 的系数在 $$\beta$$ 处为 $$1$$、其余为 $$0$$，减去 $$\langle\beta,\alpha\rangle\alpha$$ 后 $$\beta$$ 处仍为 $$1>0$$、而 $$\alpha$$ 处为 $$-\langle\beta,\alpha\rangle<0$$。同时出现正负系数违反 (B2)，与 (R3) 要求的 $$\sigma_\alpha(\beta)\in\Phi$$ 矛盾。故 $$(\alpha,\beta)\le0$$。

**(ii)** 是 (B2) 与 $$\Phi=\Phi^+\sqcup\Phi^-$$ 的直接重述。$$\blacksquare$$

**为什么把单根的两两配对写成一个矩阵**：命题 3.32 说单根两两之间只剩下有限几种可能的 Cartan 整数（$$0,-1,-2,-3$$），而单根的个数就是秩 $$\ell$$——把这 $$\ell^2$$ 个数排成一个方阵，是把"全部结构信息"打包成一个能直接判定正定性、从而驱动分类定理（3.36）的对象，这正是下面要做的事。

**定义 3.33（Cartan 矩阵, Cartan matrix）**。取 $$\Delta=\{\alpha_1,\dots,\alpha_\ell\}$$ 并任意编号。矩阵

$$A = \bigl(\langle\alpha_i,\alpha_j\rangle\bigr)_{i,j=1}^{\ell}$$

称为 $$\Phi$$（或 $$L$$）的 **Cartan 矩阵**。由 命题 3.32，对角元恒为 $$2$$，非对角元取自 $$\{0,-1,-2,-3\}$$。

**为什么再把矩阵画成图**：Cartan 矩阵已经是有限的数据，但矩阵的具体数值——$$0,-1,-2,-3$$——比读者真正需要记住的信息更细：分类定理只关心"连不连"、"连几条边"、"哪端短"。把矩阵翻译成一张图（每个数值对应边的重数），比矩阵更直观，也是 Killing、Cartan、Dynkin 分类九加五型时实际使用的语言。

**定义 3.34（Dynkin 图, Dynkin diagram）**。$$\Phi$$ 的 Dynkin 图构造如下：每个单根 $$\alpha_i$$ 画一个顶点；顶点 $$i\neq j$$ 之间连

$$n_{ij} := \langle\alpha_i,\alpha_j\rangle\langle\alpha_j,\alpha_i\rangle = 4\cos^2\theta_{ij}\in\{0,1,2,3\}$$

条边；若 $$n_{ij}\ge 2$$（即两单根长度不同，比值 $$\sqrt2$$ 或 $$\sqrt3$$），在重边/三重边上画一个**箭头指向短根**。

**定理 3.35（根系 $$\leftrightarrow$$ Dynkin 图：信息不丢失）**。$$\Phi$$ 的 Dynkin 图完全决定：
**(i)** 每个根长与短根长的平方比；

**(ii)** 全部夹角，从而决定 Cartan 矩阵 $$A$$；

**(iii)** 由此（再由下面的 定理 3.36 的重建）决定 $$\Phi$$ 自身，进而决定单 Lie 代数 $$L$$（在 $$L$$ 单时）。

*证明思路*：**(i)** 由 定理 3.29 的枚举，$$n_{ij}=1,2,3$$ 分别给出长度比 $$1,\sqrt2,\sqrt3$$（$$n_{ij}=1$$ 时两根等长），箭头指出哪端短。**(ii)** 夹角由 $$n_{ij}=4\cos^2\theta$$ 与「钝角」（命题 3.32(i)）共同定死；$$A$$ 的元 $$\langle\alpha_i,\alpha_j\rangle$$ 的大小由 $$n_{ij}$$ 与长度比给出（$$\langle\alpha_i,\alpha_j\rangle\langle\alpha_j,\alpha_i\rangle=n_{ij}$$ 且两者之比 $$=\lvert\alpha_j\rvert^2/\lvert\alpha_i\rvert^2$$），符号由钝角给出。**(iii)** 由 $$\Delta$$ 与 $$A$$ 可重建 $$\Phi$$（每个根由 $$\Delta$$ 展开、系数由 $$A$$ 与整性确定），进而由 Serre 定理（用 $$A$$ 写出 $$3\ell$$ 条生成关系）重建 $$L$$。$$\blacksquare$$

**定理 3.36（Killing–Cartan 分类定理, classification）**。不可约（图连通）根系、等价地**复单 Lie 代数**，恰有九类：

$$\underbrace{A_n\ (n\ge 1)}_{\mathfrak{sl}(n+1,\mathbb C)},\quad \underbrace{B_n\ (n\ge 2)}_{\mathfrak{so}(2n+1,\mathbb C)},\quad \underbrace{C_n\ (n\ge 3)}_{\mathfrak{sp}(2n,\mathbb C)},\quad \underbrace{D_n\ (n\ge 4)}_{\mathfrak{so}(2n,\mathbb C)},$$

以及五个**例外型** (exceptional)：

$$E_6,\ E_7,\ E_8,\ F_4,\ G_2 .$$

低秩重合：$$B_2 = C_2$$、$$A_3=D_3$$、$$D_2 = A_1\times A_1$$（后者不连通，是两个 $$A_1$$ 的并）。

*分类的证明骨架*：由 定理 3.35，分类不可约根系 = 分类连通的 Dynkin 图。关键是把几何换成矩阵：Cartan 矩阵 $$A=\bigl(\langle\alpha_i,\alpha_j\rangle\bigr)$$ **正定**（它是 $$E$$ 上正定内积在基 $$\Delta$$ 下的 Gram 矩阵经正对角矩阵重新标度：$$A=\operatorname{diag}\!\bigl(\tfrac{2}{(\alpha_i,\alpha_i)}\bigr)\cdot\bigl((\alpha_i,\alpha_j)\bigr)$$）。于是分类化为「哪些连通的加权图给出正定矩阵」，下面四条纯组合结论（每条都靠「取一个测试向量、直接算二次型为 $$\le0$$」）即可排除掉其余一切图。

**（E1）无环**：含环的图不正定（环上交替赋权 $$1,-1,1,-1,\dots$$），故 Dynkin 图是**树**。

**（E2）度 $$\le3$$**：任一顶点的（加权）度不超过 $$3$$。

**（E3）重边只在链上、至多一条**：三重边只在 $$\ell=2$$；双重边不出现在分叉树里。

**（E4）分叉树的三臂不等式**：若树无重边、恰有一个三度顶点，三条臂上（**含**该分叉顶点）各有 $$p,q,r$$ 个顶点，则 $$A$$ 正定当且仅当 $$\frac1p+\frac1q+\frac1r>1$$。枚举 $$2\le p\le q\le r$$ 的整数解：$$p=q=2$$ 给出 $$(2,2,r)$$（一切 $$r$$）；$$p=2,q=3$$ 要求 $$\frac56+\frac1r>1$$，即 $$r=3,4,5$$；$$p=2,q\ge4$$ 与 $$p\ge3$$ 无解。故分叉型只剩

$$(2,2,r)\Rightarrow D\ \text{族};\qquad (2,3,3),(2,3,4),(2,3,5)\Rightarrow E_6,E_7,E_8 .$$

（换成「不含分叉顶点」的臂长记法即 $$(1,2,2),(1,2,3),(1,2,4)$$。）综合 (E1)–(E4)：单链给出 $$A_n$$；链上带一条重边给出 $$B_n,C_n,F_4,G_2$$；分叉树给出 $$D_n,E_6,E_7,E_8$$。**枚举完毕。** $$\blacksquare$$

**例 3.37（小秩的显式清单）**。把 $$\ell\le 3$$ 的 Dynkin 图逐个画出来（用顶点与边描述）：

- $$A_1$$：一个孤立顶点，$$L=\mathfrak{sl}(2)$$。这就是入口题 (viii) 的答案。
- $$A_2$$：两个顶点、一条边，$$L=\mathfrak{sl}(3)$$；两单根夹角 $$120^\circ$$（钝角，符合 命题 3.32(i)）。
- $$A_3$$：三顶点单链。恒有 $$A_3\cong D_3$$，故 $$\mathfrak{sl}(4)\cong\mathfrak{so}(6)$$。
- $$B_2$$：两个顶点、一条**双重边**、箭头指向短根，$$L=\mathfrak{so}(5)$$；恒有 $$B_2\cong C_2$$（故 $$\mathfrak{so}(5)\cong\mathfrak{sp}(4)$$），夹角 $$135^\circ$$、长度比 $$\sqrt2$$。
- $$G_2$$：两个顶点、一条**三重边**、箭头指向短根；夹角 $$150^\circ$$、长度比 $$\sqrt3$$，共 $$12$$ 个根，Weyl 群阶 $$12$$。
- $$A_1\times A_1$$：两个孤立顶点，$$L=\mathfrak{sl}(2)\oplus\mathfrak{sl}(2)$$——**半单但不单**的最小例子。

**定理 3.38（Weyl 群与它的阶）**。**Weyl 群** (Weyl group) $$W$$ 定义为由全体根反射生成的群

$$W = \langle\sigma_\alpha : \alpha\in\Phi\rangle\subseteq GL(E).$$

它有以下性质：**(i)** $$W$$ 有限，且保持 $$\Phi$$（故嵌入 $$\Phi$$ 的置换群）；**(ii)** $$W$$ 由**单反射** $$s_i=\sigma_{\alpha_i}$$（$$\alpha_i\in\Delta$$）生成；**(iii)** $$W$$ 在 $$\Phi$$ 上传递，在基集合上单传递；**(iv)** $$W$$ 是 Coxeter 群，由 $$s_1,\dots,s_\ell$$ 与关系 $$(s_is_j)^{m_{ij}}=1$$ 给出，其中 $$m_{ii}=1$$，$$m_{ij}\in\{2,3,4,6\}$$ 依次对应夹角 $$90^\circ,60^\circ,45^\circ,30^\circ$$。

*证明思路*：**(i)** 由 (R3) 生成元保持 $$\Phi$$，而 $$\Phi$$ 有限，故 $$W\to\operatorname{Sym}(\Phi)$$ 是同态；核中元素是「逐点固定 $$\Phi$$」的反射之积，固定张成 $$E$$ 的集合故为单位，于是 $$W$$ 有限。**(ii)** 先验证共轭关系 $$\sigma_{w(\alpha_i)}=w\sigma_{\alpha_i}w^{-1}$$（代入定义直接算），再用 (iii) 的传递性得知每个 $$\sigma_\alpha$$ 都是某个单反射的共轭，故由单反射生成。**(iii)** 对高度 $$(\alpha,\gamma)$$ 归纳：若 $$\alpha$$ 非单根，则 $$\alpha=\alpha_1+\alpha_2$$（两个正根），由 命题 3.32(i) 可证某个 $$\sigma_{\alpha_i}$$ 使高度严格下降。**(iv)** 这是 Coxeter 群的标准结论：$$s_is_j$$ 的阶 $$m_{ij}$$ 与夹角 $$\theta_{ij}$$ 的关系为 $$m_{ij}=\frac{\pi}{\pi-\theta_{ij}}$$（$$i\neq j$$），代入七个允许角得 $$m_{ij}\in\{2,3,4,6\}$$（钝角给出同一个 $$m$$）。$$\blacksquare$$

**例 3.39（Weyl 群的显式结构）**。

$$A_n:\ W\cong S_{n+1},\ \lvert W\rvert=(n+1)!;\qquad B_n=C_n:\ W\cong(\mathbb Z/2)^n\rtimes S_n,\ \lvert W\rvert=2^nn!;$$

$$D_n:\ W\cong(\mathbb Z/2)^{n-1}\rtimes S_n,\ \lvert W\rvert=2^{n-1}n!;\qquad G_2:\ W\cong D_6\ (\text{正六边形二面体群}),\ \lvert W\rvert=12 .$$

（$$A_n$$ 的 $$W$$ 是置换群：$$\sigma_{\varepsilon_i-\varepsilon_{i+1}}$$ 就是在坐标 $$i,i+1$$ 上做交换，故 $$\lvert W\rvert=(n+1)!$$。）

## 四、几何与物理直觉 (Intuition)

### 4.1 根系的几何：一个房和一面镜子

先看 $$A_2$$（即 $$\mathfrak{sl}(3,\mathbb C)$$）：根是平面上均匀分布的六个向量，两两成 $$60^\circ$$ 或 $$120^\circ$$，画出来是一个**正六边形**（例 3.25）。但被记进 Dynkin 图的只有两个顶点：选一个 $$120^\circ$$ 扇区（Weyl 房），其两条边界就是单根 $$\alpha_1,\alpha_2$$。$$A_2$$ 的正根只有三个：$$\alpha_1,\ \alpha_2,\ \alpha_1+\alpha_2$$（最高根），按 $$\Delta$$ 展开都得到非负整系数——这正是 (B2)。

几何图景：**整个根系 = 一个基本房 + 一面镜子墙**。Weyl 群 $$W$$ 由反射超平面 $$\alpha^\perp$$ 生成，把一个基本房 $$\{x : (\alpha_i,x)>0\ \forall i\}$$ 反复镜像，拼出整个空间；根系就是这些镜面的法向量的全体。此图景对任何 $$\ell$$ 成立，只是 $$\ell\ge3$$ 时画不出来，只能靠 Dynkin 图记录。

**一句能背下来的对偶**：根系是「几何侧」的对象（一组向量 + 一个有限反射群），Dynkin 图是「组合侧」的对象（一张图）。定理 3.35 说两者互相决定——这就把无穷连续的 Lie 代数压成了一张有限图。

### 4.2 权与晶体：表示论的几何像

把根系换成「权格」。设 $$V(\lambda)$$ 是不可约表示，两条事实：

**(a)** $$V(\lambda)$$ 的权集在 $$W$$ 下不变（每个 $$\sigma_\alpha$$ 由 Lie 代数的一个自同构实现，而自同构把表示带到同构表示）。

**(b)** 权集含于 $$\lambda-\mathbb Z_{\ge0}\Phi^+$$ 中，即从最高权 $$\lambda$$ 沿负根方向「往下掉」（正根算子零化最高权向量，其余一切权由降权算子反复作用生成）。

两条合起来，$$V(\lambda)$$ 的权集像嵌在权格里的**晶体**：$$\lambda$$ 是顶端，反射群把它翻来翻去，(b) 的锥形约束把它夹成有界形状。$$\mathfrak{sl}(2)$$ 的情形是一条竖直等差链（入口题 (iii)），$$\mathfrak{sl}(3)$$ 的情形是平面上的六边形或三角形点阵。物理学把 $$\mathfrak{sl}(3)$$ 的这张权图叫**八重道 (Eightfold Way)**——它不是比喻，就是权图本身。

### 4.3 物理：从能级到标准模型

**接口一（第 34 章 → 本章）：一个必须当场拆穿的误认。** 谐振子的 $$a,a^\dagger,N$$ **不是** $$\mathfrak{sl}(2)$$ 的 $$E,F,H$$（详见 入口题 (iv)–(vi)），它们是**振荡子代数** $$\mathfrak{osc}=\operatorname{span}\{a,a^\dagger,N,I\}$$（四维）的生成元。区别是结构性的：

| | $$\mathfrak{sl}(2)$$ | $$\mathfrak{osc}$$ |
|---|---|---|
| 维数 | $$3$$ | $$4$$（必须把 $$I$$ 补进去才封闭） |
| 关键换位子 | $$[E,F]=H$$（落在 **Cartan 元**上） | $$[a,a^\dagger]=I$$（落在**中心**上） |
| 中心 | $$0$$ | $$\mathbb C I$$ |
| 半单？ | 是（单） | 否（含交换理想 $$\mathbb C I$$） |

两者**共享升降语法**（都有「升权 / 降权 / 测权」三个角色）——这就是误认的来源。**鉴别只需看一件事：关键换位子落在中心还是落在可对角化的 Cartan 元上。** 「能级等间距」应归给**振荡子代数** $$[N,a]=\pm a$$ **加上** $$N\ge0$$，不归给 $$\mathfrak{sl}(2)$$ 的表示论：$$\mathfrak{sl}(2)$$ 的权链 $$m,m-2,\dots,-m$$ 有限且两端有界，与「下界有、上界无」的谐振子谱形状不符；真正的联系是偶/奇宇称两部分各自承载一个由 $$a^{\dagger\,2},a^2,N+\frac12I$$ 生成的 $$\mathfrak{sl}(2)$$ 作用（无限维最低权模），它们的权链与能级链重合，但生成元不是 $$a,a^\dagger$$。

这条辨析在原子物理里的对应物是**谱生成代数 (spectrum generating algebra)**：氢原子的能级 $$E_n=-1/n^2$$ 并不等间距，但它的 $$n^2$$ 重简并由 $$\mathfrak{so}(4)$$ 的表示论解释，而 $$\mathfrak{so}(4)\cong\mathfrak{sl}(2)\oplus\mathfrak{sl}(2)$$——又是 $$A_1\times A_1$$（例 3.37）。**注意逻辑方向**：不是因「能级等间距」才去找 $$\mathfrak{sl}(2)$$，而是发现一个**额外**的对称代数作用在谱上、它的权链给出了简并结构。

**接口二（第 52 章 → 本章）**：$$SU(2)$$ 的 Lie 代数 $$\mathfrak{su}(2)$$ 复化后是 $$\mathfrak{sl}(2,\mathbb C)$$，其 Dynkin 图是**一个孤立顶点** $$A_1$$。第 52 章用四元数与双重覆盖算出的「不可约表示维数 $$\lambda+1$$」在本章就是 入口题 (iii) 的分类定理，来源是一个**组合数据**（整数的最高权），与 $$S^3$$ 的拓扑无关：第 52 章看**整体拓扑**（$$S^3$$ 双重覆盖 $$SO(3)$$），本章看**局部代数**（$$\mathfrak{sl}(2)$$ 的权链）。

**接口三（本章 → 标准模型）**：强相互作用的规范群 $$SU(3)$$ 对应 $$\mathfrak{sl}(3,\mathbb C)=A_2$$。夸克的三种「色」张成基础表示 $$V(\omega_1)$$（三维），胶子构成伴随表示 $$V(\omega_1+\omega_2)$$（八维，故称「八重态」）。从两个顶点的一张图出发、用最高权格点读出维数，就解释了两个最基本的粒子多重态——这是 Dynkin 图在实验物理里最直接的兑现。

**接口四（本章 → 例外型）**：$$E_8$$ 的 Dynkin 图有 $$8$$ 个顶点、$$248$$ 维，出现在杂化弦的规范群 $$E_8\times E_8$$ 里。分类定理说它不是凑出来的：它和 $$A_n$$ 一样，是「正定 Cartan 矩阵」这一有限枚举里必须出现的一格。

### 4.4 一张对照表

| 层面 | $$A_1$$ | $$A_2$$ | 一般 $$A_n$$ |
|---|---|---|---|
| Lie 代数 | $$\mathfrak{sl}(2)$$ | $$\mathfrak{sl}(3)$$ | $$\mathfrak{sl}(n+1)$$ |
| 物理 | 自旋 / 谐振子 | 色 $$SU(3)$$ | —— |
| 根系 | $$\{\pm\alpha\}$$ | 正六边形（6 根） | $$\varepsilon_i-\varepsilon_j$$（$$n(n+1)$$ 根） |
| Dynkin 图 | 一个孤立点 | 两个点一条边 | 一条 $$n$$ 个点的链 |
| Weyl 群 | $$S_2$$ | $$S_3$$ | $$S_{n+1}$$（阶 $$(n+1)!$$） |

## 五、经典问题精讲 (Classical Problems)

四道题按「原子模型 → 具体算根 → 判定半单 → 群与图」的顺序排列，覆盖本章全部工具。

### 题 1：把 $$\mathfrak{sl}(2,\mathbb C)$$ 表示论算干净

**考点**：入口题 (i)–(iii) 的完整实现；Casimir 算子作为验证工具。
**位置**：3.23(iv) 与 3.24 的「一维根空间」与「每根配一个 $$\mathfrak{sl}(2)$$」全靠它提供。

**题面**：取 $$\mathfrak{sl}(2,\mathbb C)$$ 的标准基 $$E,F,H$$，关系 $$[H,E]=2E,\ [H,F]=-2F,\ [E,F]=H$$。

**(1)** 求 $$\mathfrak{sl}(2)$$ 的 Killing 型在这组基下的矩阵。
**(2)** 求出全部有限维不可约表示，并验证维数公式 $$\dim V(m)=m+1$$。
**(3)** 计算 Casimir 算子 $$c = E F + F E + \frac12 H^2$$ 在 $$V(m)$$ 上的作用。

**解**：

**(1)** 以基 $$(E,H,F)$$ 的顺序，由 $$\operatorname{ad}\!\cdot\!(H)=[\,\cdot,H]$$ 等逐列填得

$$\operatorname{ad}H = \begin{pmatrix}2&0&0\\0&0&0\\0&0&-2\end{pmatrix},\quad
\operatorname{ad}E = \begin{pmatrix}0&0&0\\-2&0&0\\0&1&0\end{pmatrix},\quad
\operatorname{ad}F = \begin{pmatrix}0&0&0\\0&0&2\\-1&0&0\end{pmatrix}.$$

（例：$$\operatorname{ad}E(H)=[E,H]=-2E$$ 给第一列第二个元素 $$-2$$；$$\operatorname{ad}E(F)=H$$ 给第三列第二个元素 $$1$$。）逐对算迹：

$$\kappa(H,H)=\operatorname{tr}(\operatorname{ad}H)^2=8,\quad
\operatorname{ad}E\operatorname{ad}F=\begin{pmatrix}0&0&0\\-2&0&0\\0&1&0\end{pmatrix}\begin{pmatrix}0&0&0\\0&0&2\\-1&0&0\end{pmatrix}=\begin{pmatrix}0&0&0\\0&0&-4\\0&0&2\end{pmatrix},$$

后者的迹为 $$2$$，故 $$\kappa(E,F)=2$$；同理 $$\kappa(E,E)=\kappa(F,F)=\kappa(H,E)=\kappa(H,F)=0$$。于是

$$\kappa = \begin{pmatrix}0&0&2\\0&8&0\\2&0&0\end{pmatrix}\quad(\text{行序 }E,H,F),\qquad \det\kappa = -32\neq0 .$$

$$\kappa$$ 非退化，由 Cartan 第二判据（定理 3.16）得 $$\mathfrak{sl}(2,\mathbb C)$$ 半单。

**(2)** 设 $$V$$ 是有限维不可约表示。由 入口题 (ii)，取权向量 $$v\neq0$$ 使 $$Hv=\lambda v,\ Ev=0$$。令 $$v_k=F^kv$$。

*基本关系*：由 $$[H,F]=-2F$$ 得 $$H F^k = F^k H - 2kF^k$$（对 $$k$$ 归纳：$$HF^k = F(HF^k) - 2F^k$$，再用归纳假设把 $$HF^{k-1}$$ 展开），作用在 $$v$$ 上给出

$$Hv_k = (\lambda-2k)v_k .$$

由 $$[E,F]=H$$ 得 $$EF^k = F^kE + kF^{k-1}(H - (k-1)I)$$（同样归纳：$$k=1$$ 时 $$EF = FE+H$$ 即 $$EF = F E + H$$，成立；归纳步用 $$EF^k=EF\cdot F^{k-1}$$）。作用在 $$v$$ 上（$$Ev=0$$、$$Hv=\lambda v$$）：

$$Ev_k = k\bigl(\lambda-(k-1)\bigr)v_{k-1} = k(\lambda-k+1)v_{k-1}.$$

*有限性*：$$v_0,v_1,v_2,\dots$$ 是权互不相同的向量，若全部非零则张成无限维空间，与 $$\dim V<\infty$$ 矛盾。故存在最小的 $$m\ge0$$ 使 $$v_{m+1}=0$$。此时 $$0=v_{m+1}=Fv_m$$，而 $$v_m\neq0$$（$$m$$ 是最小的）。又 $$Ev_{m+1}=0$$（因 $$v_{m+1}=0$$），而 $$Ev_{m+1}=(m+1)(\lambda-m)v_m$$，故

$$(m+1)(\lambda-m)=0\ \Longrightarrow\ \lambda=m.$$

*不可约性*：$$v_0,\dots,v_m$$ 张成的子空间被 $$E,F,H$$ 保持（$$E$$ 降低下标、$$F$$ 升高下标且到 $$v_{m+1}=0$$ 为止、$$H$$ 对角），故是 $$V$$ 的非零子模；由不可约性它就是 $$V$$。于是 $$\dim V=m+1$$，权为 $$m,m-2,\dots,-m$$。不同 $$m$$ 给出不同表示（最高权 $$m$$ 是 $$H$$ 的本征值，是不变量），故 $$\mathfrak{sl}(2)$$ 的有限维不可约表示与 $$m\in\mathbb Z_{\ge0}$$ 一一对应。

**(3)** 先验证 $$c$$ 与整个作用交换（即 $$c$$ 是 Casimir 元）。由 $$[H,E]=2E,\ [H,F]=-2F$$：

$$[EF+FE,\,E]=-EH-HE,\qquad [\tfrac12H^2,\,E]=\tfrac12\bigl(H[H,E]+[H,E]H\bigr)=HE+EH,$$

两者相加为零，故 $$[c,E]=0$$，同理 $$[c,F]=0$$；而 $$[c,H]=0$$（$$[H^2,H]=0$$，且由 $$[E,H]=-2E$$、$$[F,H]=2F$$ 得 $$[EF,H]=[FE,H]=0$$）。于是 $$c$$ 在每个不可约模上是标量（Schur 引理）。

求这个标量。在最高权向量上（$$Ev_0=0$$，故 $$FEv_0=0$$；而 $$EFv_0=Ev_1=mv_0$$）：

$$c\,v_0 = EFv_0+FEv_0+\tfrac12H^2v_0 = mv_0+0+\tfrac12m^2v_0 = \tfrac12m(m+2)\,v_0 .$$

**自检**：在 $$v_1$$ 上算。$$EFv_1=Ev_2=2(m-1)v_1$$、$$FEv_1=F(mv_0)=mv_1$$、$$\tfrac12H^2v_1=\tfrac12(m-2)^2v_1$$，相加得

$$2(m-1)+m+\tfrac12(m-2)^2 = \tfrac12m^2+m = \tfrac12 m(m+2),$$

与 $$v_0$$ 上一致 ✓。故 $$c$$ 在 $$V(m)$$ 上的特征值是 $$\boxed{\tfrac12 m(m+2)}$$（也写作 $$2j(j+1)$$，其中 $$j=m/2$$ 是自旋）。$$\blacksquare$$

### 题 2：把 $$\mathfrak{sl}(3,\mathbb C)$$ 的根、Cartan 矩阵与 Dynkin 图算出来

**考点**：根空间分解的计算；从根系读出 Dynkin 图。
**位置**：把 3.3 段的抽象分解落成矩阵（对接 例 3.25 与 3.5 段的分类数据）。

**题面**：取 $$L=\mathfrak{sl}(3,\mathbb C)$$，$$H=$$ 迹零对角矩阵。求全部根、Cartan 矩阵、Dynkin 图与最高根。

**解**：

**(1) 根空间。** 对 $$h=\operatorname{diag}(a_1,a_2,a_3)$$（$$a_1+a_2+a_3=0$$）与矩阵单位 $$E_{ij}$$（$$i\neq j$$）：

$$[h,E_{ij}] = (a_i-a_j)E_{ij} = (\varepsilon_i-\varepsilon_j)(h)\,E_{ij},\qquad \varepsilon_i(h):=a_i .$$

故每个 $$\varepsilon_i-\varepsilon_j$$ 都是根，根空间 $$\mathbb C E_{ij}$$ 一维；$$\dim H=2=\ell$$。略作检查：非对角矩阵共 $$6$$ 个，加上 $$\dim H=2$$，$$6+2=8=3^2-1=\dim\mathfrak{sl}(3)$$ ✓，分解完整。于是

$$\Phi = \{\pm(\varepsilon_1-\varepsilon_2),\ \pm(\varepsilon_2-\varepsilon_3),\ \pm(\varepsilon_1-\varepsilon_3)\},\qquad \lvert\Phi\rvert=6 .$$

**(2) 单根与内积。** 取 $$\gamma$$ 使 $$(\alpha,\gamma)>0$$ 者恰好是 $$\varepsilon_1-\varepsilon_2,\ \varepsilon_2-\varepsilon_3,\ \varepsilon_1-\varepsilon_3$$，其中不可分解为两个正根之和的只有前两个，故

$$\Delta = \{\alpha_1,\alpha_2\},\qquad \alpha_1:=\varepsilon_1-\varepsilon_2,\quad \alpha_2:=\varepsilon_2-\varepsilon_3 .$$

在 $$E=\{\alpha\in H^* : \sum a_i=0\}$$ 上，$$\varepsilon_i$$ 的欧氏内积为 $$(\varepsilon_i,\varepsilon_j)=\delta_{ij}-\frac13$$（把 $$\mathbb R^3$$ 的标准内积投影到 $$\sum a_i=0$$ 上得到）。逐项算：

$$(\alpha_1,\alpha_1)=(\varepsilon_1,\varepsilon_1)-2(\varepsilon_1,\varepsilon_2)+(\varepsilon_2,\varepsilon_2)=\tfrac23+\tfrac23+\tfrac23=2,$$

同理 $$(\alpha_2,\alpha_2)=2$$，而

$$(\alpha_1,\alpha_2)=(\varepsilon_1,\varepsilon_2)-(\varepsilon_1,\varepsilon_3)-(\varepsilon_2,\varepsilon_2)+(\varepsilon_2,\varepsilon_3)=-\tfrac13+\tfrac13-\tfrac23-\tfrac13=-1 .$$

**(3) Cartan 矩阵。** 由定义 $$\langle\alpha_i,\alpha_j\rangle=2(\alpha_i,\alpha_j)/(\alpha_j,\alpha_j)$$：

$$\langle\alpha_1,\alpha_1\rangle = 2,\quad \langle\alpha_2,\alpha_2\rangle=2,\quad \langle\alpha_1,\alpha_2\rangle = \frac{2(-1)}{2}=-1,\quad \langle\alpha_2,\alpha_1\rangle=-1 .$$

$$A = \begin{pmatrix}2&-1\\-1&2\end{pmatrix}.$$

检验正定性：主子式 $$2>0$$，$$\det A = 4-1=3>0$$ ✓，与「$$A$$ 正定」一致（分类定理第一步）。

**(4) Dynkin 图。** 顶点 $$\{\alpha_1,\alpha_2\}$$；边数 $$n_{12}=\langle\alpha_1,\alpha_2\rangle\langle\alpha_2,\alpha_1\rangle=(-1)(-1)=1$$，故**两个顶点连一条边**；$$\lvert\alpha_1\rvert=\lvert\alpha_2\rvert$$ 故无箭头。夹角：$$\cos\theta=(\alpha_1,\alpha_2)/(\lvert\alpha_1\rvert\lvert\alpha_2\rvert)=-1/2$$，$$\theta=120^\circ$$ ✓（与 命题 3.32(i) 的钝角一致）。这就是 $$A_2$$。

**(5) 最高根。** 正根为 $$\alpha_1,\ \alpha_2,\ \alpha_1+\alpha_2$$。取 $$\theta=\alpha_1+\alpha_2=\varepsilon_1-\varepsilon_3$$ ✓。由 $$(\theta,\alpha_1)=(\varepsilon_1-\varepsilon_3,\varepsilon_1-\varepsilon_2)=\tfrac23+\tfrac13+\tfrac13-\tfrac13=1$$ 得 $$\langle\theta,\alpha_1\rangle=1\ge0$$，同理 $$\langle\theta,\alpha_2\rangle=1$$；而 $$\theta+\alpha_1=2\varepsilon_1-\varepsilon_2-\varepsilon_3\notin\Phi$$，故 $$\theta$$ 是最高根。

$$\blacksquare$$

### 题 3：用 Cartan 判据证明 $$\mathfrak{sl}(n,\mathbb C)$$ 半单

**考点**：Killing 型的显式计算 + 第二判据。
**位置**：3.2 段工具的第一次真实使用；也验证了 例 3.25 的参数化合法。

**题面**：证明 $$\mathfrak{gl}(n,\mathbb C)$$ 的 Killing 型为

$$\kappa(X,Y) = 2n\operatorname{tr}(XY) - 2\operatorname{tr}(X)\operatorname{tr}(Y),$$

并由此证明 $$\mathfrak{sl}(n,\mathbb C)$$ 半单。

**解**：

**(1) $$\operatorname{ad}$$ 在矩阵单位上的作用。** 由 $$[E_{ij},E_{kl}]=\delta_{jk}E_{il}-\delta_{li}E_{kj}$$（直接乘矩阵可验），对 $$X=\sum_{i,j}x_{ij}E_{ij}$$ 有

$$\operatorname{ad}X\ (E_{kl}) = \sum_i x_{ik}E_{il} - \sum_j x_{lj}E_{kj} .$$

**(2) 求迹。** 要算 $$\operatorname{tr}(\operatorname{ad}X\operatorname{ad}Y)=\sum_{k,l}\bigl(\operatorname{ad}Y\operatorname{ad}X(E_{kl})\bigr)$$ 在 $$E_{kl}$$ 上的系数之和。把 (1) 的公式里 $$X$$ 换成 $$Y$$，再复合一次、读出 $$E_{kl}$$ 的系数（第一项 $$\sum_ix_{ik}E_{il}$$ 在 $$\operatorname{ad}Y$$ 下给出 $$E_{kl}$$ 当且仅当 $$i=k$$，贡献 $$x_{ik}y_{ki}$$ 与 $$-x_{kk}y_{ll}$$；第二项 $$-\sum_jx_{lj}E_{kj}$$ 给出 $$E_{kl}$$ 当且仅当 $$j=l$$，贡献 $$-x_{ll}y_{kk}$$ 与 $$+\sum_jx_{lj}y_{jl}$$）：

$$\bigl[\operatorname{ad}Y\operatorname{ad}X\bigr]_{kl} = \sum_i x_{ik}y_{ki} - x_{kk}y_{ll} - x_{ll}y_{kk} + \sum_j x_{lj}y_{jl} .$$

对 $$(k,l)$$ 求和。第一项与第四项各给出因子 $$n$$（对另一个下标求和得到 $$n$$）：

$$\sum_{k,l}\sum_i x_{ik}y_{ki} = n\sum_{i,k}x_{ik}y_{ki} = n\operatorname{tr}(XY),\qquad \sum_{k,l}\sum_j x_{lj}y_{jl} = n\operatorname{tr}(XY);$$

第二、三项各是 $$-(\operatorname{tr}X)(\operatorname{tr}Y)$$。合计

$$\kappa(X,Y) = 2n\operatorname{tr}(XY) - 2\operatorname{tr}(X)\operatorname{tr}(Y).$$

**自检**：取 $$X=Y=E_{11}$$。公式给 $$2n-2$$；直接算：$$\operatorname{ad}E_{11}$$ 的特征值为 $$+1$$（重数 $$n-1$$，作用于 $$E_{12},\dots,E_{1n}$$）、$$-1$$（重数 $$n-1$$，作用于 $$E_{21},\dots,E_{n1}$$）、$$0$$（其余），故 $$(\operatorname{ad}E_{11})^2$$ 的迹为 $$2n-2$$ ✓。

**(3) $$\mathfrak{sl}(n)$$ 上的限制。** $$\mathfrak{sl}(n)\lhd\mathfrak{gl}(n)$$，故由 定理 3.17，$$\kappa_{\mathfrak{sl}} = \kappa_{\mathfrak{gl}}\lvert_{\mathfrak{sl}}$$。对 $$X,Y\in\mathfrak{sl}(n)$$（即 $$\operatorname{tr}X=\operatorname{tr}Y=0$$）：

$$\kappa(X,Y) = 2n\operatorname{tr}(XY) .$$

**(4) 非退化性。** 设 $$X\in\mathfrak{sl}(n)$$ 且 $$\operatorname{tr}(XY)=0$$ 对一切 $$Y\in\mathfrak{sl}(n)$$。取 $$Y=E_{ii}-E_{nn}$$（$$i<n$$）：$$0=\operatorname{tr}(X(E_{ii}-E_{nn}))=x_{ii}-x_{nn}$$，故 $$x_{11}=x_{22}=\dots=x_{nn}$$，即 $$X$$ 是数量矩阵 $$\lambda I$$。又 $$\operatorname{tr}X=0$$ 给出 $$n\lambda=0$$，故 $$\lambda=0$$，$$X=0$$。于是 $$\kappa\vert_{\mathfrak{sl}(n)}$$ 非退化，由 Cartan 第二判据（定理 3.16），$$\mathfrak{sl}(n,\mathbb C)$$ 半单。

（注意：$$\mathfrak{gl}(n)$$ **不**半单——它的中心 $$\mathbb C I$$ 是非零交换理想，故可解；上面的 $$\kappa_{\mathfrak{gl}}$$ 也确实退化，因为 $$\kappa(I,Y)=2n\operatorname{tr}Y-2n\operatorname{tr}Y=0$$ 对一切 $$Y$$。这正是「半单 = 中心为零」的一个现身说法。）

$$\blacksquare$$

### 题 4：$$A_2$$ 的 Weyl 群与「八重道」

**考点**：Weyl 群的显式计算；权图的几何。
**位置**：4.1、4.2 两段几何内容的可验证版本；例 3.39 在 $$n=2$$ 时的展开。

**题面**：对 $$A_2$$，**(1)** 算出 Weyl 群 $$W$$ 的阶与结构；**(2)** 说明 $$W$$ 在根上的作用轨道；**(3)** 解释 $$\mathfrak{sl}(3)$$ 的伴随表示（八维）的权图。

**解**：

**(1)** $$\sigma_{\alpha_1}$$ 固定超平面 $$a_1=a_2$$ 并交换 $$\{a_1,a_2\}$$：验证 $$\sigma_{\alpha_1}(\alpha_1)=-\alpha_1$$，且 $$\sigma_{\alpha_1}(\varepsilon_1-\varepsilon_3)=(\varepsilon_1-\varepsilon_3)-\langle\varepsilon_1-\varepsilon_3,\alpha_1\rangle\alpha_1=(\varepsilon_1-\varepsilon_3)-(\varepsilon_1-\varepsilon_2)=\varepsilon_2-\varepsilon_3$$（用了 $$\langle\varepsilon_1-\varepsilon_3,\alpha_1\rangle=2(1)/2=1$$）。同理 $$\sigma_{\alpha_2}$$ 交换 $$\{a_2,a_3\}$$。故

$$W\cong S_3,\qquad \lvert W\rvert=3!=6 .$$

**(2)** 基本房是 $$\Delta$$ 决定的 $$60^\circ$$ 开扇区 $$C=\{\lambda : (\lambda,\alpha_1)>0,\ (\lambda,\alpha_2)>0\}$$；$$W$$ 的六个元素把它映成六个楔形，拼成整个平面——这就是「六个根均匀分布」的来源。$$S_3$$ 传递地置换 $$\varepsilon_1,\varepsilon_2,\varepsilon_3$$，而根是 $$\varepsilon_i-\varepsilon_j$$，故六个根构成**一个**轨道（$$W$$ 在 $$\Phi$$ 上传递 ✓，定理 3.38(iii)）。

**(3)** 伴随表示是 $$L$$ 自身，$$\dim\mathfrak{sl}(3)=8$$。它的权是：六个非零根 $$\pm(\varepsilon_i-\varepsilon_j)$$ 各重数 $$1$$，加上原点、重数 $$\dim H=2$$。所以权图是

$$\{\text{六个根（正六边形）}\}\ \cup\ \{\text{原点，重数 }2\}.$$

**不是六边形加一个点，而是六边形加两个重合的点**——对照 $$\mathfrak{sl}(2)$$ 的伴随表示（$$\{2,0,-2\}$$，中心重数 1）可以看出，原点处的重数正是 $$\dim H=\ell$$。物理上这八个权就是八个胶子，而中心的两个量子数给出 $$SU(3)$$ 的两种可交换标记。

$$\blacksquare$$

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 把 $$\mathfrak{sl}(2,\mathbb C)$$ 的三元组写成显式矩阵，验证 $$[H,E]=2E,\ [H,F]=-2F,\ [E,F]=H$$，并写出 $$\operatorname{ad}H$$ 在以 $$(E,H,F)$$ 为基的矩阵、求出它的特征值。

**基2.** 判定三维 Heisenberg 代数（基 $$x,y,z$$，唯一非零括号 $$[x,y]=z$$）的可解性、幂零性、以及半单性（半单性用 Killing 型判定）。

**基3.** 写出 $$\mathfrak{sl}(2,\mathbb C)\oplus\mathfrak{sl}(2,\mathbb C)$$ 的 Cartan 子代数的维数与 Dynkin 图，并说明它为什么半单但不单。

**基4.** 对 $$A_2$$ 的 Cartan 矩阵 $$A=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$$，验证 $$A$$ 正定，并解释为什么「$$A$$ 不连通（分块对角）」对应「$$L$$ 半单但不单」。

### 竞赛（本课目标难度）

**竞1.** 取 $$\mathfrak{so}(3,\mathbb C)=\{X\in\mathfrak{gl}(3,\mathbb C) : X+X^t=0\}$$。求它的一个 Cartan 子代数与全部根，识别它的 Dynkin 图，并解释为什么这与「$$\mathfrak{so}(3)\cong\mathfrak{su}(2)$$ 的复化是 $$\mathfrak{sl}(2,\mathbb C)$$」不矛盾。

**竞2.** 设 $$V=V(m)$$ 是 $$\mathfrak{sl}(2,\mathbb C)$$ 的最高权为 $$m$$ 的不可约表示，其权为 $$m,m-2,\dots,-m$$。证明：权的和 $$\sum_k\lambda_k=0$$，且权的平方和

$$\sum_k\lambda_k^2 = \frac{m(m+1)(m+2)}{3}.$$

（用 $$m=1,2,3$$ 手算核对。）

**竞3.** 在平面 $$\mathbb R^2$$ 中取一组标准正交基 $$u,v$$，令

$$\alpha_1=u-v\ (\text{长根}),\qquad \alpha_2=v\ (\text{短根}).$$

验证 $$\alpha_1,\alpha_2$$ 的夹角与长度比（与 定理 3.29 的枚举对照），写出 Cartan 矩阵与 Dynkin 图，并列出 $$B_2$$（即 $$\mathfrak{so}(5,\mathbb C)$$）的全部 8 个根。用 $$\dim\mathfrak{so}(5)=10$$ 核对「秩 + 根数 = 维数」。

**竞4.** 设 $$L$$ 半单，$$I\lhd L$$ 是理想。证明 $$L=I\oplus I^{\perp}$$（$$I^{\perp}$$ 是关于 Killing 型的正交补），并说明 $$I^{\perp}$$ 也是理想。

### 研究（通向下一章）

**研1.** 从 $$G_2$$ 的 Dynkin 图（两个顶点、连接一条**三重边**、箭头指向短根）出发，重建 Cartan 矩阵，验证它正定，并写出 $$G_2$$ 的 12 个根的最简显式描述。

**研2.** 观察 $$B_n$$ 与 $$D_n$$ 的 Dynkin 图：$$B_n$$ 是一条链，$$D_n$$ 的链有一端分出**两个**端点。证明（或说明）：这个「分叉与不分叉」的差别，正是 $$\mathfrak{so}(2n+1)$$ 与 $$\mathfrak{so}(2n)$$ 的**旋量表示**个数不同（一个 vs 两个）在 Dynkin 图上的印记。

### 解答 (Solutions)

**解 基1.** 显式矩阵为

$$E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad F=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad H=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

逐个验算（矩阵乘法直接做）：

$$HE-EH = \begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix}-\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}0&1\\0&0\end{pmatrix}-\begin{pmatrix}0&-1\\0&0\end{pmatrix}=\begin{pmatrix}0&2\\0&0\end{pmatrix}=2E;$$

$$HF-FH = \begin{pmatrix}0&0\\-1&0\end{pmatrix}-\begin{pmatrix}0&0\\1&0\end{pmatrix}=\begin{pmatrix}0&0\\-2&0\end{pmatrix}=-2F;$$

$$EF-FE = \begin{pmatrix}1&0\\0&0\end{pmatrix}-\begin{pmatrix}0&0\\0&1\end{pmatrix}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}=H .$$

$$\operatorname{ad}H$$ 在基 $$(E,H,F)$$ 上的矩阵：$$\operatorname{ad}H(E)=2E$$ 给第一列 $$(2,0,0)^t$$；$$\operatorname{ad}H(H)=0$$ 给第二列 $$(0,0,0)^t$$；$$\operatorname{ad}H(F)=-2F$$ 给第三列 $$(0,0,-2)^t$$。故

$$\operatorname{ad}H = \operatorname{diag}(2,0,-2),$$

特征值为 $$2,0,-2$$。非零的两个就是两个根 $$\pm\alpha$$（取 $$\alpha(H)=2$$）；$$0$$ 来自 $$H$$ 自身（即 $$L_0=H$$）。这与「$$A_1$$ 只有一对根」一致。$$\blacksquare$$

**解 基2.** *可解*：$$L^{(1)}=[L,L]=\mathbb C z$$，$$L^{(2)}=[\mathbb C z,\mathbb C z]=0$$。故可解。

*幂零*：$$L^{1}=[L,L]=\mathbb C z$$，$$L^{2}=[L,\mathbb C z]=\mathbb C[L,z]=0$$（因 $$z$$ 与一切交换）。故幂零。

*半单*：算 Killing 型。$$\operatorname{ad}x$$ 在基 $$(x,y,z)$$ 下：$$[x,x]=0,\ [x,y]=z,\ [x,z]=0$$，故 $$\operatorname{ad}x(z)=0$$、$$\operatorname{ad}x(y)=z$$，矩阵为

$$\operatorname{ad}x=\begin{pmatrix}0&0&0\\0&0&0\\0&1&0\end{pmatrix},\quad \operatorname{ad}y=\begin{pmatrix}0&0&0\\0&0&0\\-1&0&0\end{pmatrix},\quad \operatorname{ad}z=0 .$$

$$\operatorname{ad}x\operatorname{ad}y = \begin{pmatrix}0&0&0\\0&0&0\\0&1&0\end{pmatrix}\begin{pmatrix}0&0&0\\0&0&0\\-1&0&0\end{pmatrix}=0,\quad \operatorname{ad}x\operatorname{ad}x=0,$$

故 $$\kappa(x,x)=\kappa(x,y)=\kappa(y,y)=0$$，且 $$\kappa(\cdot,z)=0$$（因 $$\operatorname{ad}z=0$$）。于是 $$\kappa\equiv0$$，退化，由 Cartan 第二判据（定理 3.16）**不半单**。这也符合直觉：它有非零中心 $$Z(L)=\mathbb C z$$，而 $$Z(L)$$ 是可解理想。$$\blacksquare$$

**解 基3.** 记 $$L=L_1\oplus L_2$$，$$L_i\cong\mathfrak{sl}(2)$$，Cartan 子代数 $$H=H_1\oplus H_2$$（每个 $$H_i$$ 一维），故 $$\dim H = 2$$，秩 $$\ell=2$$。根集是每个单因子的根集之并：

$$\Phi = \{\pm\alpha^{(1)}\}\cup\{\pm\alpha^{(2)}\},$$

其中 $$\alpha^{(1)}$$ 只作用在 $$L_1$$ 上（在 $$L_2$$ 上为零）、$$\alpha^{(2)}$$ 反之。两个根正交（$$(\alpha^{(1)},\alpha^{(2)})=0$$，因为内积由 $$\kappa$$ 给出、而 $$\kappa$$ 在直和上分块对角）。于是 Dynkin 图是**两个互不相连的孤立顶点**，即 $$A_1\times A_1$$（也叫 $$D_2$$），与 例 3.37 的最后一条一致。

*半单*：$$L$$ 是单理想的直和，由 定理 3.12 的反面（或直接：若 $$I\lhd L$$ 可解，则它到每个 $$L_i$$ 的投影是 $$L_i$$ 的可解理想，故为零，于是 $$I=0$$）得 $$\operatorname{Rad}L=0$$。

*不单*：$$L_1$$ 是 $$L$$ 的非平凡真理想（既非 $$0$$ 也非 $$L$$）。故 $$L$$ 半单但不单。$$\blacksquare$$

**解 基4.** **正定性**：对称矩阵 $$A$$ 正定 $$\iff$$ 各阶顺序主子式为正。一阶：$$2>0$$。二阶：$$\det A=4-1=3>0$$。故正定。（另一个算法：特征值 $$1,3>0$$。）

**连通性与单性的对应**：Cartan 矩阵的块分解与 Dynkin 图的连通分量一一对应。若 $$A$$ 分块对角成 $$A=A'\oplus A''$$，则 Dynkin 图不连通，分裂成两个连通子图；每个连通子图对应一个**单**理想，而整体是它们直和。故：

$$\text{Dynkin 图连通}\iff\text{根系不可约}\iff L\ \text{单};$$

$$\text{Dynkin 图有 }k\text{ 个连通分量}\iff L=L_1\oplus\cdots\oplus L_k\ (\text{每块单}).$$

（分类定理 3.36 只枚举连通的图，正是因为它枚举的是单 Lie 代数；半单的一般情形由 定理 3.12 拆成单理想直和。）$$\blacksquare$$

**解 竞1.** **关键 leap**：$$\mathfrak{so}(3,\mathbb C)$$ 是三维的，但要看到它的 Cartan 子代数只是一维——不要以为「三维的代数秩也是三」。

取基

$$L_1=\begin{pmatrix}0&0&0\\0&0&-1\\0&1&0\end{pmatrix},\ L_2=\begin{pmatrix}0&0&1\\0&0&0\\-1&0&0\end{pmatrix},\ L_3=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix}.$$

直接乘可验 $$[L_1,L_2]=L_3,\ [L_2,L_3]=L_1,\ [L_3,L_1]=L_2$$（循环对称）。取

$$H:=\mathbb C L_3 .$$

$$H$$ 一维、交换，且 $$\operatorname{ad}L_3$$ 在复化上可对角化（下面显式对角化），故 $$H$$ 是环面的；由维数它是极大的（任何交换子代数若含 $$L_1,L_2$$ 的组合，则其括号给出 $$L_3$$，破坏交换性）。故 $$\ell=1$$。

**对角化**：令

$$E:=L_1+iL_2,\qquad F:=L_1-iL_2 .$$

则

$$[L_3,E] = [L_3,L_1]+i[L_3,L_2] = L_2 + i(-L_1) = -i(L_1+iL_2) = -iE,$$

$$[L_3,F] = L_2-i(-L_1) = i(L_1-iL_2) = iF,\qquad [E,F]=-2iL_3 .$$

故两个根是 $$\pm\alpha$$，其中 $$\alpha(L_3)=: -i$$（取 $$E$$ 的根为 $$-i$$，则 $$F$$ 的根为 $$i$$）。**只有一对根，故 Dynkin 图是一个孤立顶点：$$A_1$$。**

**为什么与「$$\mathfrak{so}(3)\cong\mathfrak{su}(2)$$」不矛盾**：$$A_1$$ 正是 $$\mathfrak{sl}(2,\mathbb C)$$ 的图，而 $$\mathfrak{so}(3,\mathbb C)$$ 与 $$\mathfrak{sl}(2,\mathbb C)$$ 都是 $$\mathfrak{su}(2)$$ 的复化（$$\mathfrak{so}(3)$$ 与 $$\mathfrak{su}(2)$$ 是同一个紧 Lie 代数的两个实现）。**复 Lie 代数的分类里同一个图只有一个代数；不同的实形式（$$\mathfrak{su}(2)$$、$$\mathfrak{so}(3)$$、$$\mathfrak{sl}(2,\mathbb R)$$）在复化后合并成同一个 $$\mathfrak{sl}(2,\mathbb C)$$。** 重标度即可看出同构：$$[E,F]=-2iL_3$$ 与 $$\mathfrak{sl}(2)$$ 的 $$[E,F]=H$$ 只差常数因子。$$\blacksquare$$

**解 竞2.** 由 入口题 (iii)，权是 $$\lambda_k=m-2k$$（$$k=0,1,\dots,m$$），共 $$m+1$$ 项。

**和**：这是公差 $$-2$$ 的等差列，首项 $$m$$、末项 $$-m$$，故

$$\sum_{k=0}^{m}(m-2k) = (m+1)\cdot\frac{m+(-m)}{2} = 0 .$$

**平方和**：把 $$\lambda_k^2=(m-2k)^2$$ 展开：

$$\sum_{k=0}^{m}(m^2-4mk+4k^2) = (m+1)m^2 - 4m\cdot\frac{m(m+1)}{2} + 4\cdot\frac{m(m+1)(2m+1)}{6} .$$

三项分别化简为 $$(m+1)m^2$$、$$-2m^2(m+1)$$、$$\frac{2m(m+1)(2m+1)}{3}$$。通分（分母 $$3$$）：

$$\frac{3m^2(m+1)-6m^2(m+1)+2m(m+1)(2m+1)}{3} = \frac{m(m+1)\bigl[3m-6m+2(2m+1)\bigr]}{3} = \frac{m(m+1)\cdot(m+2)}{3},$$

因为方括号里是 $$-3m+4m+2=m+2$$。

**核对**：$$m=1$$：权 $$1,-1$$，平方和 $$2$$，公式给 $$\frac{1\cdot2\cdot3}{3}=2$$ ✓。$$m=2$$：权 $$2,0,-2$$，平方和 $$8$$，公式给 $$\frac{2\cdot3\cdot4}{3}=8$$ ✓。$$m=3$$：权 $$3,1,-1,-3$$，平方和 $$20$$，公式给 $$\frac{3\cdot4\cdot5}{3}=20$$ ✓。$$\blacksquare$$

**解 竞3.** **关键 leap**：$$B_2$$ 的根系是二维的，不要在一个「看起来是 $$\mathbb R^3$$」的坐标里算——直接取 $$\mathbb R^2$$ 的标准正交基 $$u,v$$，全部根就是 $$\pm u,\pm v,\pm(u\pm v)$$（下面验证）。

**夹角与长度比**：

$$(\alpha_1,\alpha_1)=2,\qquad (\alpha_2,\alpha_2)=1,\qquad (\alpha_1,\alpha_2)=(u-v,v)=0-1=-1 .$$

$$\cos\theta=\frac{-1}{\sqrt{2\cdot1}}=-\frac{\sqrt2}{2}\ \Longrightarrow\ \theta=135^\circ,\qquad \frac{\lvert\alpha_1\rvert}{\lvert\alpha_2\rvert}=\frac{\sqrt2}{1}=\sqrt2 .$$

与 定理 3.29 的枚举对照：$$nm=2$$、$$\{m,n\}=\{1,2\}$$、$$r=\sqrt2$$、$$\theta=135^\circ$$ ✓（恰好落在「七个允许角」里）。

**Cartan 矩阵**：

$$\langle\alpha_1,\alpha_2\rangle=\frac{2(-1)}{1}=-2,\qquad \langle\alpha_2,\alpha_1\rangle=\frac{2(-1)}{2}=-1,\qquad A=\begin{pmatrix}2&-2\\-1&2\end{pmatrix}.$$

$$2>0,\ \det A=4-2=2>0$$，正定 ✓。

**Dynkin 图**：边数 $$n_{12}=\langle\alpha_1,\alpha_2\rangle\langle\alpha_2,\alpha_1\rangle=(-2)(-1)=2$$，故是**双重边**；箭头指向**短根** $$\alpha_2=v$$。即 $$B_2$$ 的图（也等于 $$C_2$$ 的图，见下）。

**8 个根**：

$$\pm u,\qquad \pm v,\qquad \pm(u+v),\qquad \pm(u-v).$$

逐个确认是根并在同一平面里：$$u$$ 与 $$v$$ 是短根（平方长 $$1$$），$$u\pm v$$ 是长根（平方长 $$2$$）；两两内积为 $$0,\pm1,\pm2$$，对应的夹角都是 $$90^\circ,45^\circ,135^\circ,0^\circ/180^\circ$$ 中的值（共线只出现在同一族里）✓。共 $$8$$ 个。

**维数核对**：$$\mathfrak{so}(5,\mathbb C)$$ 的秩为 $$2$$（Cartan 子代数二维），加上 $$8$$ 个一维根空间：

$$\underbrace{2}_{H}\ +\ \underbrace{8}_{L_\alpha}\ =\ 10\ =\ \dim\mathfrak{so}(5)\ \checkmark .$$

（$$\mathfrak{so}(5)$$ 的维数是 $$\frac{5\cdot4}{2}=10$$ ✓。）

**附注（$$B_2=C_2$$）**：把长短根对调、重选 $$u,v$$ 就得到 $$\mathfrak{sp}(4,\mathbb C)$$ 的根系，两者 Dynkin 图只差箭头方向——这就是 $$\mathfrak{so}(5,\mathbb C)\cong\mathfrak{sp}(4,\mathbb C)$$。区分 $$B_2$$（双重边，$$A=\begin{pmatrix}2&-2\\-1&2\end{pmatrix}$$，$$\det=2$$）与 $$G_2$$（三重边，$$\det=1$$）要看**非对角元的大小**，不是根的坐标。$$\blacksquare$$

**解 竞4.** **思路**：用 $$I$$ 自身的 Killing 型非退化（$$I$$ 半单）+ 维数计算。

**第一步：$$I$$ 半单，故 $$\kappa\vert_I$$ 非退化。** 若 $$I$$ 有非零可解理想 $$J$$，则 $$J$$ 也是 $$L$$ 的理想（$$[L,J]\subseteq[I,J]\subseteq J$$，用了 $$J\lhd I$$ 与 $$I\lhd L$$）且可解，与 $$L$$ 半单矛盾，故 $$\operatorname{Rad}I=0$$。由 定理 3.17，$$\kappa\vert_I=\kappa_I$$；再由 Cartan 第二判据（定理 3.16）得 $$\kappa_I$$ 非退化。

**第二步：$$I\cap I^{\perp}=0$$。** 设 $$x\in I\cap I^{\perp}$$，则 $$\kappa_I(x,I)=0$$；由第一步得 $$x=0$$。

**第三步：$$L=I\oplus I^{\perp}$$。** 线性映射 $$x\mapsto\kappa(x,\cdot)\vert_I$$ 从 $$I$$ 到 $$I^*$$ 是单射（第二步），故是双射。于是对任意 $$y\in L$$，泛函 $$\kappa(y,\cdot)\vert_I$$ 有唯一原像 $$y'\in I$$，即 $$y-y'\in I^{\perp}$$，故 $$L=I+I^{\perp}$$，由第二步是直和。

**第四步：$$I^{\perp}$$ 是理想。** 取 $$x\in I^{\perp}$$、$$y\in L$$、$$z\in I$$，由结合不变性 $$\kappa([x,y],z)=\kappa(x,[y,z])=0$$（因 $$[y,z]\in I$$），故 $$[x,y]\in I^{\perp}$$，即 $$I^{\perp}\lhd L$$。$$\blacksquare$$

**解 研1.** **第一步：从图读 Cartan 矩阵。** $$G_2$$ 的图：两个顶点、**三重边**、箭头指向短根。设 $$\alpha_1$$ 在箭头尾（长根）、$$\alpha_2$$ 在箭头头（短根）。边数给出

$$\langle\alpha_1,\alpha_2\rangle\langle\alpha_2,\alpha_1\rangle=3 .$$

长度比由箭头给出：$$\frac{(\alpha_1,\alpha_1)}{(\alpha_2,\alpha_2)}=\left(\sqrt3\right)^2=3$$。而

$$\frac{\langle\alpha_1,\alpha_2\rangle}{\langle\alpha_2,\alpha_1\rangle}=\frac{(\alpha_1,\alpha_1)}{(\alpha_2,\alpha_2)}=3 .$$

设 $$\langle\alpha_1,\alpha_2\rangle=-3k,\ \langle\alpha_2,\alpha_1\rangle=-k$$（符号为负：非共线单根夹角为钝角，见 命题 3.32(i)），则 $$3k^2=3$$，$$k=1$$。故

$$A=\begin{pmatrix}2&-3\\-1&2\end{pmatrix}.$$

**第二步：正定性。** $$2>0$$，$$\det A=4-3=1>0$$。故 $$A$$ 正定 ✓（与「单 Lie 代数的 Cartan 矩阵必正定」一致）。

**第三步：12 个根。** 在 $$\mathbb R^3$$ 中取平面 $$P:\varepsilon_1+\varepsilon_2+\varepsilon_3=0$$（内积取 $$\mathbb R^3$$ 标准内积在 $$P$$ 上的限制），则

$$\Phi_{G_2}=\underbrace{\{\pm(\varepsilon_i-\varepsilon_j)\ :\ 1\le i<j\le3\}}_{\text{短根，6 个}}\ \cup\ \underbrace{\{\pm(\varepsilon_i+\varepsilon_j-2\varepsilon_k)\ :\ \{i,j,k\}=\{1,2,3\}\}}_{\text{长根，6 个}} .$$

**计数**：第一族有 $$3$$ 对 $$(i,j)$$，正负各一，共 $$6$$ 个；第二族中 $$\varepsilon_i+\varepsilon_j-2\varepsilon_k$$ 在交换 $$i\leftrightarrow j$$ 下不变，故对 $$\{i,j,k\}=\{1,2,3\}$$ 只有 $$3$$ 个不同的根，正负各一，共 $$6$$ 个。总计 $$12$$ 个 ✓。

**长度比**：$$(\varepsilon_1-\varepsilon_2,\varepsilon_1-\varepsilon_2)=2$$，$$(\varepsilon_1+\varepsilon_2-2\varepsilon_3,\varepsilon_1+\varepsilon_2-2\varepsilon_3)=1+1+4=6$$。比值 $$\sqrt6:\sqrt2=\sqrt3:1$$ ✓，正是箭头所指。

**单根与最高根**：取 $$\alpha_2=(0,1,-1)=\varepsilon_2-\varepsilon_3$$（短，平方长 $$2$$）、$$\alpha_1=(-1,-1,2)=\varepsilon_2+\varepsilon_3-2\varepsilon_1$$（长，平方长 $$6$$）。则 $$(\alpha_1,\alpha_2)=-3$$，故 $$\cos\theta=-3/(\sqrt2\cdot\sqrt6)=-\sqrt3/2$$，$$\theta=150^\circ$$ ✓。

**验证这一对确实是单根**（即 $$\Phi$$ 恰由它们的非负整组合加上负号组成）：枚举 $$m\alpha_1+n\alpha_2$$（$$m,n\ge0$$）落在 $$\Phi$$ 里的情形，恰好得到六个正根

$$(0,1),\ (1,0)\ \text{（高 1）},\ (1,1)\ \text{（高 2）},\ (1,2)\ \text{（高 3）},\ (1,3)\ \text{（高 4）},\ (2,3)\ \text{（高 5）},$$

它们加上各自的负向量成 $$12$$ 个根 ✓。其中 $$(1,3)\to(-1,2,-1)$$ 与 $$(2,3)\to(-2,1,1)$$ 是长根、其余四个是短根（与两族各 $$6$$ 个一致）。**最高根**是唯一不能再加任何单根的那个：

$$\theta=2\alpha_1+3\alpha_2=(-2,1,1)=\varepsilon_2+\varepsilon_3-2\varepsilon_1\quad(\text{长根，高 }5),$$

因为 $$\theta+\alpha_1=(-3,0,3)$$ 与 $$\theta+\alpha_2=(-2,2,0)=2(\varepsilon_2-\varepsilon_1)$$ 都**不是**根 ✓。$$\blacksquare$$

**解 研2.** **思路**：这道题的结论会在第 58 章被完整兑现，这里只给结构上的推理。

**第一步：两个图。** 由 3.5 段，$$B_n$$ 是一条链（末端一条双边，箭头指向末端的短根），$$D_n$$ 是一条链在最右端**分叉成两个端点**。

**第二步：端点对应的权。** 图的**端点**（度数 $$1$$ 的顶点）对应的基本权是**极小维表示**的最高权：$$B_n$$ 只有一个端点（末端短根 $$\alpha_n$$），对应基本权 $$\omega_n$$；$$D_n$$ 有**两个**端点，对应两个基本权 $$\omega_{n-1},\omega_n$$。

**第三步：为什么「两个端点 = 两个旋量表示」。** 旋量表示是 $$\mathfrak{so}(N)$$ 的**不能**由张量积构造、只能由 Clifford 代数构造的表示。关键事实（第 58 章会证）：$$\mathrm{Cl}(2n+1)$$ 有**唯一的**不可约模（维数 $$2^n$$），故 $$\mathfrak{so}(2n+1)$$ 只有一个旋量表示——图一个端点；而 $$\mathrm{Cl}(2n)$$ 有**两个**不等价的不可约模（维数各 $$2^{n-1}$$），因为复体积元 $$\omega_{\mathbb C}=\prod_j(e_{2j-1}+ie_{2j})$$ 在模上作用为 $$\pm1$$，给出手性分裂——图两个端点。

**第四步（机制）**：从 $$D_n$$ 的图分叉处切掉一个端点，图变成 $$B_{n-1}$$ 的链——这是**限制到子代数**的分支规则在图形上的影子；两个手性模在限制到 $$B_{n-1}$$ 时都变成同一个旋量模的像。**这恰好是第 58 章要展开的起点**：$$\mathrm{Cl}(V,Q)$$ 的不可约模「一个还是两个」，由 $$\dim V$$ 的奇偶决定，也就是由 Dynkin 图末端分不分叉决定。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

**1. 半单 = Killing 型非退化 = 可以分类。** Cartan 第二判据（定理 3.16）把「没有可解理想」这个无从下手的否定性条件换成一个**可计算的条件**：算 $$\kappa$$ 的矩阵、看行列式。这一步之后，半单 Lie 代数才从「一类对象」变成「可做定理的对象」。

**2. 分类链是一条不断丢弃冗余的编码链。** $$L\ (\infty\ \text{维连续})\to\Phi\ (\text{有限欧氏图形})\to\Delta+W\ (\text{有限反射群})\to A\ (\text{一张有限图})$$。每步丢掉一部分信息、留下不变量，而最终丢到只剩一张图时，**这张图仍然完全决定 $$L$$**（定理 3.35）：**代数的分类问题变成了有限图的枚举问题**。

**3. 枚举只有九加五。** $$A_n,B_n,C_n,D_n$$ 四族无限加 $$E_6,E_7,E_8,F_4,G_2$$ 五个例外。力量不在「算出来」，而在**排他性**：「不可能有别的」。排除的引擎只有 (R4) 的整性与 定理 3.29 的七个允许角——**有限性来自整性**。

**4. $$\mathfrak{sl}(2)$$ 是原子，而且能直接验算。** 整个半单理论都靠「每根配一个 $$S_\alpha\cong\mathfrak{sl}(2)$$」（定理 3.24）把问题降维，所以 $$\mathfrak{sl}(2)$$ 的表示论要熟到能做心算（入口题 (i)–(iii) 与 题 1 值得自己重推一遍）。

**5. 一个当场拆穿的误认（本章的额外收获）。** 谐振子的升降算子**不是** $$\mathfrak{sl}(2)$$，而是**振荡子代数**的生成元；区别在于关键换位子落在中心还是落在 Cartan 元上。「能级等间距」应归给振荡子代数加 $$N$$ 的正性。一般教训：**判断两个 Lie 代数是否同构，不要看生成元「长得像什么」（「升权/降权/测权」这类角色命名是表示论层面的，可以被不同代数共享），要看换位子的落点（中心？Cartan？理想？）——这是结构层面、可验证的。**

**下一章的悬念**：$$D_n$$（$$\mathfrak{so}(2n,\mathbb C)$$）的 Dynkin 图末端**分叉成两个端点**，而 $$B_n$$（$$\mathfrak{so}(2n+1)$$）是一条链。研 2 说过这对应「$$\mathfrak{so}(2n)$$ 有两个半旋量表示、$$\mathfrak{so}(2n+1)$$ 只有一个」。这个「两个 vs 一个」从哪来？答案是 **Clifford 代数 $$\mathrm{Cl}(V,Q)$$ 的不可约模个数**：维数为偶时复体积元给出 $$\pm1$$ 的手性分裂，为奇时不存在。第 58 章（Clifford 代数与 Lorentz 群）将把这套结构完整建立起来，并顺手给出相对论旋量（Dirac / Weyl / Majorana）的代数定义。**从 Dynkin 图的一个分叉，到电子的相对论波动方程——中间要走的正是第 58 章。**

**延伸阅读**：

- **J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (GTM 9)** —— 本章的结构来源：第 3–6、8–10 章覆盖本章全部内容，弦公式见 §9.4、Cartan 判据见 §5。每个抽象定理后几乎立刻跟一个 $$\mathfrak{sl}(2)$$ 或 $$\mathfrak{sl}(3)$$ 的例子。
- **J.-P. Serre, *Complex Semisimple Lie Algebras*** —— 用「根系 + Serre 关系」从一张图重建 Lie 代数（定理 3.35(iii) 的严谨版本）。薄、狠、几乎没有废话。
- **N. Bourbaki, *Lie Groups and Lie Algebras*, Ch. 4–6** —— 根系的「字典」：九加五型的根、Weyl 群、基本权一览表，适合当查询手册。
- **R. Carter, *Lie Algebras of Finite and Affine Type*** —— 想走到 Kac–Moody 与仿射型从这里接着走；仿射 Dynkin 图正是本章「正定」放松为「半正定」时多出来的那批。
- **H. Georgi, *Lie Algebras in Particle Physics*** —— 物理侧对照：八重道、电弱、$$\mathfrak{so}(10)$$ / $$E_6$$ 大统一模型，全是本章分类表的直接使用。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch55_复半单Lie代数与根系_上.md">← 第55章 复半单 Lie 代数与根系·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch57_Clifford代数与Lorentz群_上.md">第57章 Clifford 代数与 Lorentz 群·上 →</a></div>
</div>
