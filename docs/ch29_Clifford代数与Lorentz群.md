---
layout: default
---

# 第29章: Clifford 代数与 Lorentz 群 (Clifford Algebras and the Lorentz Group)
> 对应原专栏: MP104–MP106
> 专家依据: `_experts/algebra/representation-theory.md`（主）+ `_experts/algebra/lie-algebra-root-systems.md`
> 知识库依据: `opc2/knowledge/physics/量子场论/tong-qft/`、`opc2/knowledge/math/李代数/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

第 07 章把「外积」做成了一台可以计算的机器：外代数 $$\Lambda(V)$$，它的构造方式是拿张量代数 $$T(V)$$ 商掉「**平方为零**」这个理想。第 26 章把三维旋转讲成了一次双重覆盖 $$S^3\to SO(3)$$，代价是「同一个旋转对应两个四元数」。第 28 章把半单 Lie 代数拆成根系，那是纯粹的结构分类。三条线在本章汇成一条：**把二次型升级成一个代数 $$\mathrm{Cl}(V,q)$$，再用它把 Lorentz 群讲成自旋群的双重覆盖。**

本章要回答两个问题。第一个是代数的：二次型只能告诉你一个向量的「长度」，Clifford 代数要告诉你两个向量的「乘积」。这个升级是怎么做出来的？答案是——**用第 07 章一模一样的商构造，只换一个理想**：外代数商掉 $$v\otimes v$$（于是 $$v^2=0$$），Clifford 代数商掉 $$v\otimes v-q(v)\mathbf 1$$（于是 $$v^2=q(v)$$）。**外代数与 Clifford 代数是同一个构造的两端**：一端把度量忘掉，一端把度量记牢。把这组对照讲清楚，才知道为什么它配得上「代数」这个称呼。

第二个是几何与物理的：相对论的转动群 $$SO(1,3)$$ 为什么有一个「转两圈才回来」的双重覆盖？那个多出来的、不属于任何向量的东西（旋量）究竟是什么？

**从哪来**：第 07 章的商构造（同一个模板，换一个理想）；第 04 章的双线性形式与迷向向量；第 26 章的 $$SU(2)\cong S^3$$ 与 $$S^3\to SO(3)$$（本章把它升级成四维时空版 $$\mathrm{SL}(2,\mathbb C)\to SO(1,3)^{\uparrow}$$）；第 27–28 章的 Lie 代数（$$\gamma$$ 矩阵的反对易关系就是 $$\mathfrak{so}(1,3)$$ 的复化在旋量空间上的一个实现）。

**到哪去**：第 30 章用本章的旋量讲 Möbius 群与射影表示——那里会看到，「多出一层」在量子力学里的名字叫「态矢差一个相位」。

## 二、入口：一道具体的问题 (Entry Problem)

**先给题，不给定义。** 下面两组题，前三问中学生就能动手，最后一问做不动——那个「做不动」的地方，就是本章要长的结构。

### 问题 A：四个矩阵能锁死多大一间屋子（来源：自编，母题是 Dirac 方程里 $$\gamma$$ 矩阵的标准推导）

设 $$n$$ 是正整数，$$A,B$$ 是 $$n\times n$$ 复矩阵，满足

$$A^2=B^2=I,\qquad AB+BA=0.$$

**(A1)** 证明 $$\operatorname{tr}A=\operatorname{tr}B=0$$。

**(A2)** 由此证明 $$n$$ 必为偶数。

**(A3)** 取 $$n=2$$，写出一对满足条件的矩阵。

**(A4)** 现在把条件加码：设 $$\gamma^0,\gamma^1,\gamma^2,\gamma^3$$ 是 $$n\times n$$ 复矩阵，满足

$$\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=2\eta^{\mu\nu}I,\qquad \eta=\operatorname{diag}(1,-1,-1,-1).$$

用 (A2) 的手法证明：$$n$$ 必为 $$4$$ 的倍数，特别地 $$n\ge 4$$。

**(A5)** 取 $$n=4$$，显式构造出这样四个矩阵（给出结果即可，检验留给第六节）。

**为什么这道题重要**：这四个矩阵是 Dirac 方程的骨架。它在物理里看起来只是「四个反交换的矩阵」，但它把表示空间的维数从 $$2$$ 一路撑到 $$4$$，并且——正如本章第三节会证明的——**只要四个向量两两反交换，维数就必须被 $$4$$ 整除，这跟二次型的具体数值无关**。一个看起来只是「反对易」的关系，竟然能锁死维数，这就是题面那句「比它看起来的强得多」的意思。

### 问题 B：绕两圈（来源：自编，母题是中子干涉仪的 $$4\pi$$ 周期）

在平面 $$\mathbb R^2$$ 里考虑绕原点转 $$\theta$$ 的道路

$$R(\theta)=\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix},\qquad \theta\in[0,2\pi].$$

**(B1)** 用第 26 章的四元数语言（或直接用复数）把这条道路**提升**到 $$S^3$$ 上：找一个连续道路 $$q(\theta)\in S^3$$ 使 $$\rho(q(\theta))=R(\theta)$$ 且 $$q(0)=1$$。问 $$q(2\pi)$$ 等于什么？

**(B2)** 现在换到四维时空。取 Minkowski 坐标 $$x=(x^0,x^1,x^2,x^3)$$，定义

$$X=\begin{pmatrix}x^0+x^3 & x^1-ix^2\\ x^1+ix^2 & x^0-x^3\end{pmatrix}.$$

证明 $$X$$ 是 Hermite 矩阵，且 $$\det X=(x^0)^2-(x^1)^2-(x^2)^2-(x^3)^2$$。再证明：对任意 $$A\in \mathrm{SL}(2,\mathbb C)$$，矩阵 $$X'=AXA^*$$ 也是 Hermite 矩阵，且 $$\det X'=\det X$$。

**(B3)** 由 (B2)，每个 $$A\in\mathrm{SL}(2,\mathbb C)$$ 都给出了 $$\mathbb R^4$$ 上一个保持 $$\det$$ 的线性映射 $$\Lambda(A)$$。证明 $$\Lambda(A)=\Lambda(-A)$$。然后问一个做不动的问题：**怎么知道 $$\Lambda$$ 的像恰好是「保持时间方向」的那部分 Lorentz 变换？为什么核只有 $$\pm I$$，却让这个覆盖「要绕两圈」？**

(B3) 的答案需要第三节的两样工具：Clifford 代数给出的自旋群，和覆叠空间的单连通性。做完第三节，回头再看 (A4) 的维数锁死与 (B3) 的「绕两圈」，你会发现它们是同一件事的两面。

## 三、结构：定义与完整推导 (Structure & Proof)

本节按「二次型 → 张量代数 → 商 → Clifford 代数 → 矩阵实现 → 自旋群 → 双重覆盖」的顺序推进。全程取 $$F$$ 是特征不等于 $$2$$ 的域（$$\mathbb R$$、$$\mathbb C$$ 都在内）。

### 3.1 二次型与正交群

**定义 3.1（二次空间, quadratic space）** 设 $$V$$ 是 $$F$$-线性空间。一个**对称双线性形式 (symmetric bilinear form)** 是映射 $$b:V\times V\to F$$，对每个变量线性，且 $$b(x,y)=b(y,x)$$。由它诱导的函数

$$q:\ V\to F,\qquad q(x)=b(x,x)$$

称为 $$b$$ 诱导的**二次型 (quadratic form)**，称 $$(V,q)$$（或 $$(V,b)$$）为**二次空间 (quadratic space)**。

**极化恒等式 (polarization identity)**：反过来，二次型也决定双线性形式，

$$b(x,y)=\tfrac12\bigl(q(x+y)-q(x)-q(y)\bigr).$$

*证明*：直接展开。由双线性，

$$q(x+y)=b(x+y,x+y)=b(x,x)+b(x,y)+b(y,x)+b(y,y)=q(x)+q(y)+2b(x,y).$$

两边解出 $$b(x,y)$$ 即得。**这里用到了 $$2\ne0$$ 这条特征假设**：特征 $$2$$ 时「对称双线性」与「二次型」不再一一对应，整门课会变形，本书不予处理。$$\blacksquare$$

于是「二次型」与「对称双线性形式」在特征 $$\ne2$$ 时是同一份数据的两种说法。**定义 3.1 是第 04 章那个「内积」的放松版**：那里要求 $$q(x)>0$$（正定），这里只要求 $$q$$ 是二次型，允许负值、允许零。

一个向量 $$x\ne0$$ 若满足 $$q(x)=0$$，称为**迷向向量 (isotropic vector)**；含迷向向量的二次空间称为**迷向的 (isotropic)**。这正是入口题 B 里 $$\det X=0$$ 对应的情形——光锥上的向量和自己正交。若恒有：$$q(x)=0\Longrightarrow x=0$$，则称 $$q$$ 是**非退化的 (nondegenerate)**。

**定义 3.2（等距与正交群, isometry and orthogonal group）** 设 $$(V,q)$$ 与 $$(V',q')$$ 是二次空间。一个线性同构 $$\varphi:V\to V'$$ 若满足

$$q'(\varphi x)=q(x)\qquad(\forall x\in V),$$

就称为**等距 (isometry)**，此时称两空间**等距同构**。当 $$V'=V,\ q'=q$$ 时，等距称为**正交变换**，全体构成的群记作 $$O(q)$$。

取 $$V=F^n$$、$$q(x)=\sum_k x_k^2$$，得到熟悉的矩阵群 $$O(n)=\{M: M^{\mathsf T}M=I\}$$；取 $$q$$ 为 Minkowski 二次型 $$(x^0)^2-(x^1)^2-(x^2)^2-(x^3)^2$$，得到 **Lorentz 群 (Lorentz group)** $$O(1,3)$$。**注意 $$\varphi$$ 保持的是 $$q$$ 而不是 $$b$$**——但由极化恒等式，保持 $$q$$ 自动保持 $$b$$，两句话等价。

### 3.2 同一个模板的两端：外代数与 Clifford 代数

**定义 3.3（张量代数, tensor algebra）** 设 $$T^k(V)=\underbrace{V\otimes\cdots\otimes V}_{k\ \text{个}}$$（$$T^0(V)=F$$），并置

$$T(V)=\bigoplus_{k\ge0}T^k(V),$$

乘法取张量积的拼接。这样 $$T(V)$$ 成为含幺结合代数，称为 $$V$$ 上的**张量代数**。

$$T(V)$$ 是「以 $$V$$ 的向量为生成元、除双线性外不附加任何关系」的自由结合代数：它是所有含 $$V$$ 的含幺结合代数里「最松」的那一个。**本章的技术核心只有一句话：想要一个代数，就在 $$T(V)$$ 里挑一个理想商掉它。**

**定理 3.3（外代数 = 商掉「平方为零」；回顾第 07 章的定义 3.4）** 记 $$I_{\wedge}$$ 为 $$T(V)$$ 中由一切 $$v\otimes v\ (v\in V)$$ 生成的**双边理想**（即由这些元素与 $$T(V)$$ 中任意元素的乘积线性张成的最小子空间，它对左乘、右乘封闭）。定义

$$\Lambda(V)=T(V)/I_{\wedge}.$$

则 $$\Lambda(V)$$ 是分次交换的：对 $$\alpha\in\Lambda^k(V)$$、$$\beta\in\Lambda^l(V)$$ 有

$$\alpha\wedge\beta=(-1)^{kl}\beta\wedge\alpha.$$

特别地，$$k=1$$、$$\alpha=\beta=v$$ 时得 $$v\wedge v=0$$：**每个向量的平方都是零**。

*证明思路*：商映射把 $$v\otimes v$$ 送到 $$0$$，即商里 $$v\cdot v=0$$。再由双线性把这条关系对 $$u+v$$ 使用，得到 $$uv+vu=0$$，即反对易。分次交换性是反对易在多次换位下的累加。

*证明*：记 $$\pi:T(V)\to\Lambda(V)$$ 为商映射，$$\wedge$$ 为商里诱导的乘法。由 $$v\otimes v\in I_{\wedge}$$ 得

$$0=\pi(v\otimes v)=\pi(v)\wedge\pi(v),$$

即对一切 $$v$$ 有 $$v\wedge v=0$$（以下省略 $$\pi$$ 的记号）。取 $$x,y\in V$$，对 $$x+y$$ 用这条：

$$0=(x+y)\wedge(x+y)=x\wedge x+x\wedge y+y\wedge x+y\wedge y=x\wedge y+y\wedge x,$$

故 $$x\wedge y=-y\wedge x$$。对一般的齐次元 $$\alpha=x_1\wedge\cdots\wedge x_k$$、$$\beta=y_1\wedge\cdots\wedge y_l$$，把每个 $$y_j$$ 逐个向左穿过全部 $$k$$ 个 $$x_i$$，共发生 $$kl$$ 次换位，每次变号，于是 $$\alpha\wedge\beta=(-1)^{kl}\beta\wedge\alpha$$。$$\blacksquare$$

现在只换一个理想。

**定义 3.4（Clifford 代数, Clifford algebra）** 设 $$(V,q)$$ 是二次空间。记 $$I_q$$ 为 $$T(V)$$ 中由一切

$$v\otimes v-q(v)\mathbf 1,\qquad v\in V$$

生成的双边理想，其中 $$\mathbf 1$$ 是 $$T^0(V)=F$$ 中的单位元。定义

$$\mathrm{Cl}(V,q)=T(V)/I_q,$$

其乘法称为 **Clifford 积 (Clifford product)**，习惯上省去乘号，写成 $$vw$$。

**必须显式点出的一步——两条路的并排对照。** 第 07 章和本章用的是**同一个模板** $$T(V)/I$$，唯一的区别是理想：

| | 外代数 $$\Lambda(V)$$ | Clifford 代数 $$\mathrm{Cl}(V,q)$$ |
|---|---|---|
| 商掉的理想 | 由 $$v\otimes v$$ 生成 | 由 $$v\otimes v-q(v)\mathbf 1$$ 生成 |
| 生成元满足 | $$v^2=0$$ | $$v^2=q(v)\mathbf 1$$ |
| 两个向量 | $$vw=-wv$$ | $$vw+wv=2b(v,w)\mathbf 1$$ |
| 度量地位 | 被遗忘 | 被记住了 |
| 几何对象 | 有向面积、体积 | 长度、夹角、反射 |

一句话：**外代数把度量丢掉（任何向量平方为 $$0$$），Clifford 代数把度量装回去（平方就是二次型）**。两者的连接点是一个极端情形：$$\mathrm{Cl}(V,0)$$ 就是 $$\Lambda(V)$$——当 $$q\equiv0$$ 时，$$v\otimes v-q(v)\mathbf 1=v\otimes v$$，两个理想是同一个，于是 $$\mathrm{Cl}(V,0)=\Lambda(V)$$。**外代数是一族 Clifford 代数里最「松」的那一端。**

**定理 3.4（万有性质, universal property）** 设 $$A$$ 是含幺 $$F$$-结合代数，$$j:V\to A$$ 是线性映射且满足

$$j(v)^2=q(v)\mathbf 1_A\qquad(v\in V).$$

则存在**唯一**的代数同态 $$\tilde j:\mathrm{Cl}(V,q)\to A$$ 使 $$\tilde j\circ i=j$$，其中 $$i:V\to\mathrm{Cl}(V,q)$$ 是复合 $$V\hookrightarrow T(V)\twoheadrightarrow\mathrm{Cl}(V,q)$$。

*证明思路*：先由张量代数的万有性质把 $$j$$ 唯一地延拓成 $$T(V)\to A$$，再证明这个同态在理想 $$I_q$$ 上为零，于是它过商，得到 $$\tilde j$$。

*证明*：$$T(V)$$ 由 $$V$$ 生成，故任何代数同态 $$T(V)\to A$$ 只要在 $$V$$ 上给定就唯一确定。由 $$T(V)$$ 的万有性质，$$j$$ 唯一延拓为同态 $$\Phi:T(V)\to A$$。对 $$v\in V$$，

$$\Phi(v\otimes v-q(v)\mathbf 1)=\Phi(v)^2-q(v)\mathbf 1_A=j(v)^2-q(v)\mathbf 1_A=0.$$

于是 $$\Phi$$ 在生成元 $$v\otimes v-q(v)\mathbf 1$$ 上为零，从而在由它们生成的双边理想 $$I_q$$ 上为零（因为 $$\Phi$$ 是代数同态，$$\Phi(a x b)=\Phi(a)\Phi(x)\Phi(b)$$，$$x$$ 为零则乘积为零）。故 $$\Phi$$ 过商分解出 $$\tilde j:\mathrm{Cl}(V,q)\to A$$，满足 $$\tilde j(i(v))=\Phi(v)=j(v)$$。唯一性：$$i(V)$$ 生成整个 $$\mathrm{Cl}(V,q)$$，同态由其在生成元上的值唯一确定。$$\blacksquare$$

定理 3.4 说了两件事。第一，$$\mathrm{Cl}(V,q)$$ 是**所有**满足 $$v^2=q(v)$$ 的代数里「最一般」的那个——任何别的例子都是它的商。第二，它把「保持二次型」这件事从几何翻译成了代数：一个等距 $$\varphi:V\to V$$ 只要能延拓成代数同态 $$\mathrm{Cl}(V,q)\to\mathrm{Cl}(V,q)$$，就是 Clifford 代数的对称。

**定理 3.5（乘法关系与标准基）** 设 $$(V,q)$$ 是 $$n$$ 维二次空间。

**(i)** 对一切 $$v,w\in V$$，

$$vw+wv=2b(v,w)\mathbf 1.$$

**(ii)** 设 $$e_1,\dots,e_n$$ 是 $$V$$ 的基且两两正交（即 $$i\ne j$$ 时 $$b(e_i,e_j)=0$$）。则 $$2^n$$ 个元素

$$\mathbf 1,\quad e_{i_1}e_{i_2}\cdots e_{i_k}\ (1\le i_1<i_2<\cdots<i_k\le n,\ 1\le k\le n)$$

构成 $$\mathrm{Cl}(V,q)$$ 的一组基。特别地 $$\dim\mathrm{Cl}(V,q)=2^n$$。

*证明 (i)*：由 $$(v+w)^2=q(v+w)\mathbf 1$$ 与 $$(v-w)^2=q(v-w)\mathbf 1$$ 相减，左边用双线性展开：

$$(v+w)^2-(v-w)^2=2(vw+wv),\qquad q(v+w)-q(v-w)=4b(v,w),$$

（第二式由双线性：$$q(v+w)=q(v)+q(w)+2b(v,w)$$，$$q(v-w)=q(v)+q(w)-2b(v,w)$$）。两式相等，两边除以 $$2$$ 得 (i)。$$\blacksquare$$

*证明 (ii)*：**先证「张成」**。由 (i)，$$i\ne j$$ 时 $$e_ie_j=-e_je_i$$，且 $$e_i^2=q(e_i)\mathbf 1$$。于是 $$T(V)$$ 中任一有序词 $$e_{i_1}\otimes\cdots\otimes e_{i_k}$$ 在商里都可以通过反复的「相邻换位」把它整理成「指标严格递增」的乘积：每次换序产生一个符号 $$-1$$，每次出现相同指标 $$e_ie_i$$ 就换成标量 $$q(e_i)$$。因此所有递增单项式（连同 $$\mathbf 1$$）张成 $$\mathrm{Cl}(V,q)$$，于是

$$\dim\mathrm{Cl}(V,q)\le 2^n.$$

**再证「线性无关」**。我们用第 07 章已经证过的结论：递增楔积 $$e_{i_1}\wedge\cdots\wedge e_{i_k}$$ 构成 $$\Lambda(V)$$ 的一组基（第 07 章的定理 3.8）。在向量空间 $$\Lambda(V)$$ 上，对每个指标 $$j$$ 定义线性算子

$$c_j=\varepsilon_j+q(e_j)\,\iota_j,\qquad \varepsilon_j(\omega)=e_j\wedge\omega,$$

其中 $$\iota_j$$ 是缩并（内乘）：它是 $$\Lambda(V)$$ 上唯一的反导子（antiderivation，即满足 $$\iota_j(\omega\wedge\eta)=\iota_j(\omega)\wedge\eta+(-1)^{\deg\omega}\omega\wedge\iota_j(\eta)$$），并规定 $$\iota_j(e_k)=\delta_{jk}$$。由第 07 章的定理 3.6（分次反交换），直接验证得三条关系：

$$\varepsilon_i\varepsilon_j+\varepsilon_j\varepsilon_i=0,\qquad \iota_i\iota_j+\iota_j\iota_i=0,\qquad \varepsilon_i\iota_j+\iota_j\varepsilon_i=\delta_{ij}\operatorname{id}.$$

（第二条用反导子的定义在基上展开；第三条在递增单项式上按 $$\iota_j$$ 从楔积里取出 $$e_j$$ 的符号规则检验。）把这三条代入 $$c_i$$，交叉项只剩 $$\delta_{ij}$$ 那些，得到

$$c_ic_j+c_jc_i=2b(e_i,e_j)\operatorname{id}.$$

对 $$v=\sum a_ie_i$$ 置 $$c(v)=\sum a_ic_i$$，由双线性得 $$c(v)c(w)+c(w)c(v)=2b(v,w)\operatorname{id}$$，特别地 $$c(v)^2=q(v)\operatorname{id}$$。由定理 3.4（万有性质），这给出一个代数同态

$$\rho:\ \mathrm{Cl}(V,q)\longrightarrow\operatorname{End}\bigl(\Lambda(V)\bigr).$$

现在设 $$\sum_I\lambda_I\,e_I=0$$ 是递增单项式之间的一个线性关系（$$I$$ 遍历 $$\{1,\dots,n\}$$ 的所有子集，$$e_I$$ 为对应乘积）。对它用 $$\rho$$，得 $$\sum_I\lambda_I\rho(e_I)=0$$。取所有满足 $$\lambda_I\ne0$$ 的 $$I$$ 中基数最大者 $$k$$，考察算子在**次数 $$k$$ 分量**上的作用：对 $$e_J$$ 满足 $$\#J<k$$ 的项，$$\rho(e_J)$$ 把 $$\Lambda^0$$ 送进次数 $$\le\#J<k$$ 的部分（因为 $$\varepsilon$$ 提次数、$$\iota$$ 降次数，净提升不超过 $$\#J$$）；而对 $$\#I=k$$ 的项，$$\rho(e_I)$$ 作用在 $$1\in\Lambda^0$$ 上，次数 $$k$$ 的分量只有「全用 $$\varepsilon$$」这一条路径，结果是 $$\pm e_I$$。于是把 $$\sum_I\lambda_I\rho(e_I)$$ 作用在 $$1$$ 上，其次数 $$k$$ 分量等于

$$\sum_{\#I=k}\lambda_I\,(\pm e_I).$$

它是 $$0$$（因为总和是零算子）。由第 07 章的定理 3.8，$$k$$ 次楔积 $$e_I$$ 线性无关，故所有 $$\#I=k$$ 的 $$\lambda_I$$ 都是 $$0$$，与 $$I$$ 的选取矛盾。既然 $$\rho(e_I)$$ 线性无关，而 $$\rho$$ 是定义在整个 $$\mathrm{Cl}(V,q)$$ 上的同态，$$e_I$$ 本身也线性无关。结合上界的 $$\dim\le 2^n$$，得 $$\dim=2^n$$，且 $$e_I$$ 是一组基。$$\blacksquare$$

**定理 3.5 读法**：Clifford 代数的大小只由 $$\dim V$$ 决定（$$2^n$$），与二次型的数值无关。**「反对易」这件事本身是硬的，二次型的数值只是松弛的部分。**入口题 A 的维数锁死，本质就在这里。

**定理 3.6（偶子代数，以及与外代数共用的那一组基）**

**(i)** 记 $$\mathrm{Cl}^0(V,q)$$ 为偶数个向量的乘积线性张成的子空间（含 $$\mathbf 1$$），$$\mathrm{Cl}^1(V,q)$$ 为奇数个的。则

$$\mathrm{Cl}(V,q)=\mathrm{Cl}^0\oplus\mathrm{Cl}^1,\qquad \dim\mathrm{Cl}^0=2^{\,n-1},$$

且 $$\mathrm{Cl}^0$$ 是子代数（偶 $$\times$$ 偶 $$=$$ 偶），$$\mathrm{Cl}^0\cdot\mathrm{Cl}^1\subseteq\mathrm{Cl}^1$$，$$\mathrm{Cl}^1\cdot\mathrm{Cl}^1\subseteq\mathrm{Cl}^0$$。

**(ii)** 作为**向量空间**，Clifford 代数与外代数由同一个线性映射联系：

$$\varpi:\ \Lambda(V)\longrightarrow\mathrm{Cl}(V,q),\qquad e_{i_1}\wedge\cdots\wedge e_{i_k}\longmapsto e_{i_1}\cdots e_{i_k}.$$

由定理 3.5，$$\varpi$$ 是线性同构。**但它们不是代数同构**：$$\Lambda$$ 里 $$v\wedge v=0$$，$$\mathrm{Cl}$$ 里 $$v^2=q(v)\mathbf 1$$。

*证明*：(ii) 直接把定理 3.5 的两组基（递增楔积与递增乘积）对应起来，$$2^n$$ 对 $$2^n$$，故 $$\varpi$$ 是线性同构；代数结构不同则由 $$q\ne0$$ 时 $$v^2\ne0=v\wedge v$$ 看出。(i) 是 (ii) 按次数奇偶分块的直接推论：递增乘积按 $$k$$ 的奇偶分入两部分，各占 $$\sum_{k\ \text{偶}}\binom nk=\sum_{k\ \text{奇}}\binom nk=2^{\,n-1}$$ 维，乘法与次数的奇偶加法相容。$$\blacksquare$$

$$\varpi$$ 常被称为「量子化映射」：它保持基底、把反对称的 $$\wedge$$ 换成会「记住度量」的乘积。物理上，$$\Lambda(V)$$ 是「费米子占据数」的态空间，$$\mathrm{Cl}(V,q)$$ 是这些算子本身构成的代数——这是一件值得记住的对应。

### 3.3 Minkowski 空间、$$\gamma$$ 矩阵与最小维数

**定义 3.7（Minkowski 二次空间与 $$\gamma$$ 矩阵）** 取 $$V=\mathbb R^4$$，坐标为 $$x=(x^0,x^1,x^2,x^3)$$，二次型

$$q(x)=(x^0)^2-(x^1)^2-(x^2)^2-(x^3)^2=(x^0)^2-\lvert \vec x\rvert^2,$$

称 $$(V,q)$$ 为 **Minkowski 空间 (Minkowski space)**，记 $$\mathbb R^{1,3}$$；对应的对称双线性形式 $$\eta$$ 的矩阵是 $$\operatorname{diag}(1,-1,-1,-1)$$。（本书采用「时间部分取正」的符号约定；取负只是整体变号，分类不变。）

$$\mathrm{Cl}(\mathbb R^{1,3},q)$$ 中的一组正交基记作 $$e_0,e_1,e_2,e_3$$，满足

$$e_0^2=1,\qquad e_1^2=e_2^2=e_3^2=-1,\qquad e_\mu e_\nu+e_\nu e_\mu=0\ (\mu\ne\nu).$$

一组复矩阵 $$\gamma^0,\gamma^1,\gamma^2,\gamma^3$$（物理文献称 **$$\gamma$$ 矩阵 (gamma matrices)**，也叫 **Dirac 矩阵**）若满足

$$\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=2\eta^{\mu\nu}I$$

就称为 Cl(1,3) 的一个**矩阵实现**——由定理 3.4，它等价于一个代数同态 $$\mathrm{Cl}(1,3)\to M_n(\mathbb C)$$。

**定理 3.7（维数锁死）** 设 $$\gamma^0,\dots,\gamma^3$$ 是 $$n\times n$$ 复矩阵，满足 $$\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=2\eta^{\mu\nu}I$$，且表示空间非零。则 $$n$$ 必为 $$4$$ 的倍数；特别地 $$n\ge4$$。

*证明思路*：入口题 A 的两步劈半。先用 $$\gamma^0$$ 把空间按特征值 $$\pm1$$ 劈成 $$V_+\oplus V_-$$，证两块等维；再用 $$\alpha_3=\gamma^0\gamma^3$$ 把 $$V_+$$ 劈成两块，又等维。两步各出一个因子 $$2$$。

*证明*：记 $$V=\mathbb C^n$$。

**第一步**：$$(\gamma^0)^2=I$$ 说明 $$\gamma^0$$ 的极小多项式整除 $$(t-1)(t+1)$$，它在特征 $$\ne2$$ 的域上有互异单根，故 $$\gamma^0$$ 可对角化。于是

$$V=V_+\oplus V_-,\qquad V_\pm=\{v:\gamma^0v=\pm v\}.$$

**第二步**：对 $$i=1,2,3$$，由 $$\gamma^0\gamma^i=-\gamma^i\gamma^0$$，若 $$v\in V_+$$ 则

$$\gamma^0(\gamma^iv)=-\gamma^i\gamma^0v=-\gamma^iv,$$

故 $$\gamma^iV_+\subseteq V_-$$；同理 $$\gamma^iV_-\subseteq V_+$$。又 $$(\gamma^i)^2=-I$$ 说明 $$\gamma^i$$ 可逆，故它给出 $$V_+$$ 与 $$V_-$$ 之间的线性同构，于是 $$\dim V_+=\dim V_-$$。

**第三步**：置 $$\alpha_i=\gamma^0\gamma^i\ (i=1,2,3)$$。由第二步，$$\gamma^i$$ 把 $$V_+$$ 送进 $$V_-$$、$$\gamma^0$$ 把 $$V_-$$ 送回 $$V_+$$，故 $$\alpha_i$$ 保持 $$V_+$$。直接计算

$$\alpha_i^2=\gamma^0\gamma^i\gamma^0\gamma^i\overset{\gamma^i\gamma^0=-\gamma^0\gamma^i}{=}-\gamma^0\gamma^0\gamma^i\gamma^i=-(\gamma^0)^2(\gamma^i)^2=-1\cdot(-1)I=I.$$

同理 $$i\ne j$$ 时 $$\alpha_i\alpha_j+\alpha_j\alpha_i=0$$。于是 $$\alpha_3$$ 在 $$V_+$$ 上可对角化，$$V_+=W_+\oplus W_-$$（特征值 $$\pm1$$）；而 $$\alpha_1,\alpha_2$$ 与 $$\alpha_3$$ 反交换，把 $$W_+$$ 与 $$W_-$$ 互换，故 $$\dim W_+=\dim W_-$$。因此

$$\dim V=2\dim V_+=4\dim W_+,$$

即 $$4$$ 整除 $$\dim V$$。若 $$V\ne0$$ 则 $$W_+\ne0$$（否则 $$V=0$$），故 $$\dim V\ge4$$。$$\blacksquare$$

**定理 3.8（$$\mathrm{Cl}(1,3)$$ 的复分类与 Dirac 表示）**

**(i)** 一组显式的 $$4\times4$$ 解（**Dirac–Pauli 表示**）是

$$\gamma^0=\begin{pmatrix}I_2 & 0\\ 0 & -I_2\end{pmatrix},\qquad \gamma^i=\begin{pmatrix}0 & \sigma_i\\ -\sigma_i & 0\end{pmatrix}\quad(i=1,2,3),$$

其中 $$\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$、$$\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix}$$、$$\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$$ 是 **Pauli 矩阵 (Pauli matrices)**。

**(ii)** 由它给出的代数同态 $$\Phi:\mathrm{Cl}(1,3)\otimes_{\mathbb R}\mathbb C\to M_4(\mathbb C)$$ 是**同构**。因此

$$\mathrm{Cl}(1,3)\otimes_{\mathbb R}\mathbb C\cong M_4(\mathbb C)\qquad(\text{复维数 }16),$$

它的不可约模在同构意义下**唯一**，维数为 $$4$$；这个不可约模记作 $$S$$，其元素称为 **Dirac 旋量 (Dirac spinor)**。

**(iii)** 更一般地，复化后的 Clifford 代数只依赖维数：若 $$\dim_{\mathbb R}V=n$$，则 $$\mathrm{Cl}(V,q)\otimes_{\mathbb R}\mathbb C\cong\mathrm{Cl}(\mathbb C^n,q_{\mathbb C})$$，右端与 $$q$$ 的具体数值无关。

*证明 (i)*：逐条核对。$$\gamma^0$$ 平方为 $$I_4$$；由 $$\sigma_i^2=I_2$$ 得

$$(\gamma^i)^2=\begin{pmatrix}-\sigma_i^2&0\\0&-\sigma_i^2\end{pmatrix}=-I_4;$$

由 $$\sigma_i\sigma_j+\sigma_j\sigma_i=0\ (i\ne j)$$ 得 $$\gamma^i\gamma^j+\gamma^j\gamma^i=0$$；最后

$$\gamma^0\gamma^i=\begin{pmatrix}0&\sigma_i\\ \sigma_i&0\end{pmatrix},\qquad \gamma^i\gamma^0=\begin{pmatrix}0&-\sigma_i\\ -\sigma_i&0\end{pmatrix},$$

两者之和为零。合起来正是 $$\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu=2\eta^{\mu\nu}I_4$$。$$\blacksquare$$

*证明 (ii)*：由定理 3.4，$$\gamma$$ 矩阵满足的关系保证 $$\Phi$$ 存在（把 $$e_\mu\mapsto\gamma^\mu$$ 线性延拓，再复化）。两边维数相等：由定理 3.5，$$\dim_{\mathbb C}\mathrm{Cl}(1,3)\otimes\mathbb C=2^4=16=\dim_{\mathbb C}M_4(\mathbb C)$$。故只需证 $$\Phi$$ 满射。

把 $$M_4(\mathbb C)$$ 写成 $$2\times2$$ 的块，每块在 $$M_2(\mathbb C)$$ 中。计算给出一批**分块对角**的元素：

$$\gamma^i\gamma^j\ (i\ne j)\ \text{与它们的乘积给出}\ \operatorname{diag}(A,A),\qquad \gamma^0\ \text{给出}\ \operatorname{diag}(I,-I),$$

其中 $$A$$ 跑遍由 $$\{\sigma_i\sigma_j\}$$ 与 $$I$$ 生成的子代数。而 $$\sigma_1\sigma_2=i\sigma_3$$、$$\sigma_2\sigma_3=i\sigma_1$$、$$\sigma_1\sigma_3=-i\sigma_2$$，故这个子代数就是整个 $$M_2(\mathbb C)$$。于是 $$\operatorname{diag}(A,A)$$ 与 $$\operatorname{diag}(A,-A)=\gamma^0\operatorname{diag}(A,A)$$ 都在像里，两者相加相减给出全部 $$\operatorname{diag}(A,D)$$。另一批是**分块反对角**的元素：$$\gamma^i=\begin{pmatrix}0&\sigma_i\\-\sigma_i&0\end{pmatrix}$$ 与 $$\gamma^0\gamma^i=\begin{pmatrix}0&\sigma_i\\ \sigma_i&0\end{pmatrix}$$，由 $$\sigma_i$$ 张成 $$M_2(\mathbb C)$$ 得 $$\begin{pmatrix}0&M\\-M&0\end{pmatrix}$$ 与 $$\begin{pmatrix}0&M\\ M&0\end{pmatrix}$$，其线性组合遍历全部反对角块。四类块任意，故 $$\Phi$$ 满射，从而是同构。

$$M_4(\mathbb C)$$ 的模即 $$\mathbb C^4$$ 的直和，不可约模只有 $$\mathbb C^4$$ 一个（同构意义下），故忠实表示的维数总是 $$4$$ 的倍数。$$\blacksquare$$

*证明 (iii)*：扩标量只是把系数放大：$$T_{\mathbb C}(V_{\mathbb C})=T_{\mathbb R}(V)\otimes_{\mathbb R}\mathbb C$$，理想也相应复化，故

$$\mathrm{Cl}(V,q)\otimes_{\mathbb R}\mathbb C=\frac{T_{\mathbb R}(V)\otimes\mathbb C}{I_q\otimes\mathbb C}=\mathrm{Cl}(V_{\mathbb C},q_{\mathbb C}).$$

又 $$\mathbb C$$ 上每个非零数都有平方根，Gram–Schmidt 之后可把每个对角元开方归一，故同维数的非退化复二次型都等距同构；于是右端只依赖 $$n$$。$$\blacksquare$$

定理 3.8 把入口题 A 收口：$$n=4$$ 的解不但存在，而且在同构意义下**本质唯一**（不可约模唯一），而任何忠实表示都是若干个 $$S$$ 的直和，故维数总是 $$4$$ 的倍数——与定理 3.7 的初等论证完全一致。定理 3.7 用「劈两次」，定理 3.8 用「矩阵代数分类」，两条路殊途同归。

### 3.4 反射、自旋群与双重覆盖

**定义 3.9（反射, reflection）** 设 $$y\in V$$ 满足 $$q(y)\ne0$$（称 $$y$$ 非迷向）。定义

$$\tau_y:\ V\to V,\qquad \tau_y(x)=x-\frac{2b(x,y)}{q(y)}\,y.$$

称 $$\tau_y$$ 为沿 $$y$$ 的**反射**。

*基本性质*：$$\tau_y$$ 在超平面 $$y^{\perp}=\{x:b(x,y)=0\}$$ 上恒等，把 $$y$$ 送到 $$-y$$，是线性对合（$$\tau_y^2=\operatorname{id}$$）。它还是等距：

$$q(\tau_yx)=q(x)-2t\,b(x,y)+t^2q(y)\Big\vert_{t=2b(x,y)/q(y)}=q(x)-\frac{4b(x,y)^2}{q(y)}+\frac{4b(x,y)^2}{q(y)}=q(x).$$

故 $$\tau_y\in O(q)$$，且它的行列式为 $$-1$$（在基 $$(y,e_2,\dots,e_n)$$ 下矩阵是 $$\operatorname{diag}(-1,1,\dots,1)$$）。

**定理 3.9（三明治公式）** 在 $$\mathrm{Cl}(V,q)$$ 中，对非迷向 $$y$$ 与任意 $$x\in V$$，

$$\tau_y(x)=-\,y\,x\,y^{-1}.$$

更一般地，对非迷向 $$v_1,\dots,v_{2k}$$，

$$\tau_{v_1}\cdots\tau_{v_{2k}}(x)=(v_1v_2\cdots v_{2k})\,x\,(v_1v_2\cdots v_{2k})^{-1}.$$

*证明*：由定理 3.5(i)，$$xy+yx=2b(x,y)\mathbf 1$$，故 $$yx=2b(x,y)\mathbf 1-xy$$。又 $$y^2=q(y)\mathbf 1$$ 是标量，所以 $$y^{-1}=y/q(y)$$。于是

$$yxy^{-1}=\bigl(2b(x,y)\mathbf 1-xy\bigr)\frac{y}{q(y)}=\frac{2b(x,y)}{q(y)}y-x\cdot yy^{-1}=\frac{2b(x,y)}{q(y)}y-x.$$

两边取负号即得第一式。第二式由第一式逐步复合：每复合一次外层多乘一个 $$-v_iv_i^{-1}$$，$$2k$$ 个因子给出 $$(-1)^{2k}=1$$；再用乘积的逆公式 $$(v_1\cdots v_m)^{-1}=v_m^{-1}\cdots v_1^{-1}$$。$$\blacksquare$$

**三明治公式是本章的枢纽**：它把「几何的反射」翻译成「代数的共轭」，于是一串反射对应一个积——**自旋群就诞生在这里**。

**定义 3.10（Clifford 群与自旋群, Clifford group and spin group）** 回忆两个映射。**主对合 (main involution)** $$\alpha$$ 由 $$\alpha(v)=-v\ (v\in V)$$ 唯一确定；这是良定义的**代数自同构**，因为 $$\alpha(v)^2=(-v)^2=q(v)\mathbf 1$$，定理 3.4（对 $$j=-\operatorname{id}_V$$ 使用）给出它的存在与唯一性。**反序 (reversal)** $$t$$ 是由

$$t(v_1v_2\cdots v_k)=v_k\cdots v_2v_1\qquad(v_i\in V)$$

线性延拓得到的**代数反自同构**（即 $$t(ab)=t(b)t(a)$$；在 $$V$$ 上 $$t=\operatorname{id}$$）。定义

$$\Gamma(V,q)=\{s\in\mathrm{Cl}(V,q)^{\times}:\ s\,V\,\alpha(s)^{-1}\subseteq V\},$$

$$\mathrm{Spin}(V,q)=\{s\in \mathrm{Cl}^{0}(V,q):\ s\,t(s)=\mathbf 1,\ \ s\,V\,s^{-1}\subseteq V\}.$$

$$\Gamma$$ 称 **Clifford 群**，$$\mathrm{Spin}$$ 称 **自旋群 (spin group)**。（偶元素 $$s\in\mathrm{Cl}^0$$ 满足 $$\alpha(s)=s$$，故对它而言 $$\Gamma$$ 的条件就写成 $$sVs^{-1}\subseteq V$$——这就是第二行里那一句的来源。）对非迷向 $$v\in V$$，$$\alpha(v)=-v$$ 使 $$\Gamma$$ 的条件成为 $$-vVv^{-1}\subseteq V$$，正是定理 3.9 的反射，故所有非迷向向量都属于 $$\Gamma$$。

**定理 3.11（自旋群作用在向量上）** 设 $$(V,q)$$ 非退化、$$\dim V\ge1$$。则

$$\rho:\ \mathrm{Spin}(V,q)\longrightarrow O(q),\qquad \rho(s)(x)=s\,x\,s^{-1}$$

是良定义的群同态，且 $$\ker\rho=\{\mathbf 1,-\mathbf 1\}$$。

*证明*：**良定义**：$$sVs^{-1}\subseteq V$$ 已含在定义里；还需说明 $$\rho(s)$$ 保持 $$q$$。对 $$x\in V$$，因为 $$sxs^{-1}\in V$$，它的平方按定义等于 $$q\bigl(sxs^{-1}\bigr)\mathbf 1$$；另一方面直接算

$$\bigl(sxs^{-1}\bigr)^2=sx^2s^{-1}=s\,q(x)\mathbf 1\,s^{-1}=q(x)\mathbf 1.$$

两式比较即得 $$q(\rho(s)x)=q(x)$$。**同态**：$$\rho(s_1s_2)(x)=s_1s_2x(s_1s_2)^{-1}=\rho(s_1)\bigl(\rho(s_2)(x)\bigr)$$。**保单位**：$$\rho(\mathbf 1)=\operatorname{id}$$。

**核**：设 $$\rho(s)=\operatorname{id}$$，即 $$sx=xs$$ 对一切 $$x\in V$$。取正交基 $$e_1,\dots,e_n$$，把 $$s$$ 写成递增单项式的线性组合 $$s=\sum_I a_Ie_I$$。对固定的 $$j$$，比较 $$se_j=e_js$$ 中各项：若 $$j\notin I$$，则 $$e_Ie_j=(-1)^{\lvert I\rvert}e_je_I=e_je_I$$（$$\lvert I\rvert$$ 偶）；若 $$j\in I$$，则 $$e_je_I=(-1)^{\lvert I\rvert-1}e_Ie_j=-e_Ie_j$$。把两项加起来：

$$\sum_{I\ni j}a_I\,e_Ie_j=-\sum_{I\ni j}a_I\,e_Ie_j\quad\Longrightarrow\quad 2\sum_{I\ni j}a_Ie_Ie_j=0\quad\Longrightarrow\quad a_I=0\ (\forall I\ni j).$$

（末步用了 $$\{e_Ie_j\}$$ 线性无关——定理 3.5 的基。又特征 $$\ne2$$，$$2$$ 可除。）每个非空 $$I$$ 都含某个 $$j$$，故 $$s=a_{\varnothing}\mathbf 1$$ 是标量。再由 $$st(s)=\mathbf 1$$ 得 $$a_{\varnothing}^2=1$$，即 $$a_{\varnothing}=\pm1$$。反之 $$\pm\mathbf 1$$ 都满足 $$(\pm\mathbf 1)V(\pm\mathbf 1)^{-1}=V$$ 与 $$(\pm\mathbf 1)t(\pm\mathbf 1)=\mathbf 1$$，故在 $$\mathrm{Spin}$$ 中，且 $$\rho(\pm\mathbf 1)=\operatorname{id}$$。$$\blacksquare$$

**定理 3.12（$$\mathrm{SL}(2,\mathbb C)$$ 双重覆盖 $$SO(1,3)^{\uparrow}$$）** 记 $$\mathrm{SO}(1,3)^{\uparrow}$$ 为 $$O(1,3)$$ 中行列式为 $$1$$ 且保持时间方向（把前向锥映到自身）的那部分——它是 $$O(1,3)$$ 的单位连通分支。对 $$x\in\mathbb R^{1,3}$$ 定义 Hermite 矩阵

$$X(x)=\begin{pmatrix}x^0+x^3 & x^1-ix^2\\ x^1+ix^2 & x^0-x^3\end{pmatrix}=x^0 I_2+x^1\sigma_1+x^2\sigma_2+x^3\sigma_3.$$

则：

**(i)** $$x\mapsto X(x)$$ 是 $$\mathbb R^{1,3}$$ 到全体 $$2\times2$$ Hermite 矩阵的实线性同构，且 $$\det X(x)=q(x)$$。

**(ii)** 对 $$A\in\mathrm{SL}(2,\mathbb C)$$，$$X'=AX(x)A^*$$ 是 Hermite 矩阵且 $$\det X'=\det X(x)$$；故存在唯一的 $$\Lambda(A)\in O(1,3)$$ 使 $$X(\Lambda(A)x)=AX(x)A^*$$，且 $$\Lambda(A)$$ 线性。

**(iii)** $$\Lambda:\mathrm{SL}(2,\mathbb C)\to\mathrm{SO}(1,3)^{\uparrow}$$ 是**满**群同态，$$\ker\Lambda=\{\pm I_2\}$$。

**(iv)** $$\mathrm{SL}(2,\mathbb C)$$ 连通且单连通（它经极分解形变收缩到 $$\mathrm{SU}(2)\cong S^3$$），综合 (iii) 得

$$\mathrm{SL}(2,\mathbb C)/\{\pm I_2\}\cong\mathrm{SO}(1,3)^{\uparrow},\qquad \pi_1\bigl(\mathrm{SO}(1,3)^{\uparrow}\bigr)=\mathbb Z/2.$$

即 $$\mathrm{SL}(2,\mathbb C)$$ 是 $$\mathrm{SO}(1,3)^{\uparrow}$$ 的**万有覆叠 (universal cover)**，是两层覆叠：**同一时空转动对应两个矩阵 $$A$$ 与 $$-A$$**。

*证明 (i)*：$$X(x)$$ 的对角元 $$x^0+x^3$$、$$x^0-x^3$$ 是实数，非对角元互为共轭，故 $$X(x)$$ 是 Hermite 矩阵。计算行列式：

$$\det X=(x^0+x^3)(x^0-x^3)-(x^1-ix^2)(x^1+ix^2)=(x^0)^2-(x^3)^2-\bigl((x^1)^2+(x^2)^2\bigr)=q(x).$$

线性同构：任一 $$2\times2$$ Hermite 矩阵由四个实参数 $$\bigl(a,d,\operatorname{Re}b,\operatorname{Im}b\bigr)$$ 唯一确定（$$a,d\in\mathbb R$$、$$b\in\mathbb C$$），恰是 $$\mathbb R^{1,3}$$ 的维数；而 $$x\mapsto X(x)$$ 是线性的，且若 $$X(x)=0$$ 则四个参数全为零即 $$x=0$$，故它是单射。两边维数相同，单射即同构。$$\blacksquare$$

*证明 (ii)*：$$(AXA^*)^*=AX^*A^*=AXA^*$$（用 $$X^*=X$$ 与 $$(A^*)^*=A$$）。$$\det(AXA^*)=\det A\cdot\det X\cdot\det A^*=\det X$$（$$\det A=1$$ 且 $$\det A^*=\overline{\det A}=1$$）。第三步：由 (i)，Hermite 矩阵 $$X'$$ 唯一地是某个 $$X(y)$$；映射 $$x\mapsto X(x)\mapsto AXA^*\mapsto y$$ 是三个线性映射的复合，故线性。由 $$\det X(y)=\det X(x)$$ 与 (i) 得 $$q(y)=q(x)$$，故 $$\Lambda(A)\in O(1,3)$$。$$\blacksquare$$

*证明 (iii)*：**同态**：$$(AB)X(AB)^*=A(BXB^*)A^*$$ 给出 $$\Lambda(AB)=\Lambda(A)\Lambda(B)$$。

**核**：若 $$\Lambda(A)=\operatorname{id}$$，则 $$AX=XA$$ 对一切 Hermite $$X$$ 成立。任一复矩阵 $$M$$ 可写成 $$M=H_1+iH_2$$（$$H_1=(M+M^*)/2$$、$$H_2=(M-M^*)/(2i)$$ 都是 Hermite），所以 $$A$$ 与全体 $$M_2(\mathbb C)$$ 交换，即 $$A=\lambda I_2$$。再由 $$\det A=1$$ 得 $$\lambda^2=1$$，$$\lambda=\pm1$$。

**落在 $$\mathrm{SO}(1,3)^{\uparrow}$$**：$$\det\Lambda(A)$$ 是 $$\mathrm{SL}(2,\mathbb C)\to\{\pm1\}$$ 的连续同态（$$\det$$ 与 $$\Lambda$$ 都连续），连通空间到离散空间的连续像是单点，故 $$\det\Lambda(A)=1$$。**保时间方向**：$$X(x)$$ 正定 $$\iff x^0>\lvert\vec x\rvert \iff x$$ 是前向类时向量；而对 $$u\ne0$$，

$$\langle AXA^*u,u\rangle=\langle XA^*u,A^*u\rangle>0\ \ (\text{因 }X\text{ 正定、}A^*\text{ 可逆}),$$

故 $$\Lambda(A)$$ 把前向锥映到自身。

**满射**：$$\Lambda$$ 光滑；其单位元处的微分把 $$\ker\Lambda$$ 的切空间（$$0$$）映到 $$0$$，故 $$\mathrm{d}\Lambda$$ 单射；两边都是 $$6$$ 维实流形，故 $$\mathrm{d}\Lambda$$ 同构，由反函数定理 $$\Lambda$$ 是局部微分同胚，从而是开映射。于是 $$\Lambda(\mathrm{SL}(2,\mathbb C))$$ 是 $$\mathrm{SO}(1,3)^{\uparrow}$$ 的**开子群**；连通拓扑群的开子群等于整个群（开子群既开又闭，连通性迫使它是全集）。故满射。

这里用到 $$\mathrm{SO}(1,3)^{\uparrow}$$ 连通：任一 $$\Lambda\in\mathrm{SO}(1,3)^{\uparrow}$$ 唯一地分解为 $$\Lambda=B\cdot R$$（$$B$$ 是沿某个时间方向的 boost，$$R\in\mathrm{SO}(3)$$），boost 全体同胚于 $$\mathbb R^3$$（可缩），$$\mathrm{SO}(3)$$ 连通，故整体连通。$$\blacksquare$$

*证明 (iv)*：极分解把可逆矩阵写成 $$A=UP$$（$$U$$ 酉、$$P$$ 正定 Hermite）；$$\det A=1$$ 时 $$\det U=1$$，$$U\in \mathrm{SU}(2)$$，而这样的 $$P$$ 全体是 $$\mathbb R^3$$ 中一个凸集（对数映射下是迹为 $$0$$ 的实对称矩阵，凸）。于是 $$\mathrm{SL}(2,\mathbb C)$$ 沿 $$P$$ 收缩到 $$\mathrm{SU}(2)\cong S^3$$（第 26 章的定理 3.4），而 $$S^3$$ 单连通，故 $$\mathrm{SL}(2,\mathbb C)$$ 单连通、连通。由 (iii)，$$\Lambda$$ 是两层覆叠（每点纤维恰两个元素）；单连通的覆叠空间是万有覆叠，覆叠变换群 $$\{\pm I_2\}\cong\mathbb Z/2$$ 同构于底空间的基本群，故 $$\pi_1(\mathrm{SO}(1,3)^{\uparrow})=\mathbb Z/2$$。$$\blacksquare$$

**注（与定义 3.10 的对应）**：定理 3.11 的抽象自旋群与本节这个 $$\mathrm{SL}(2,\mathbb C)$$ 是同一个群：在定理 3.8(iii) 的 Dirac 表示下，偶子代数 $$\mathrm{Cl}^0$$ 的元素恰是分块对角矩阵 $$\operatorname{diag}(A,B)$$，其中自旋群的那部分形如 $$\operatorname{diag}\bigl(A,(A^*)^{-1}\bigr)$$，$$A\in\mathrm{SL}(2,\mathbb C)$$；对两个生成元（旋转 $$e_1e_2$$ 与 boost $$e_0e_3$$）直接验证，再由「$$B=(A^*)^{-1}$$」对乘法封闭推广到全群。故 $$\mathrm{Spin}(1,3)\cong\mathrm{SL}(2,\mathbb C)$$。**这一步的完整展开需要把 $$\mathrm{Cl}(1,3)$$ 的偶部分与 $$M_2(\mathbb C)$$ 的矩阵结构逐块对上，本章只用到它的结论**；第 30 章的射影表示只需要「存在一个连通双层覆叠」这一事实。

**定理 3.13（旋量空间与手征分解, spinor space and chirality）** 记 $$S=\mathbb C^4$$ 为 $$\mathrm{Cl}(1,3)\otimes_{\mathbb R}\mathbb C\cong M_4(\mathbb C)$$ 的唯一不可约模。定义

$$\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3.$$

则 $$\gamma_5^2=I$$，且 $$\gamma_5\gamma^\mu=-\gamma^\mu\gamma_5$$；故 $$\gamma_5$$ 的特征值只能为 $$\pm1$$，并把 $$S=S_+\oplus S_-$$ 分成两个 $$2$$ 维子空间，$$\gamma^\mu$$ 把 $$S_\pm$$ 互换。称 $$S_+$$、$$S_-$$ 中的元素为 **Weyl 旋量 (Weyl spinors)** 或**手征旋量**，投影 $$P_\pm=\tfrac12(I\pm\gamma_5)$$ 为**手征投影 (chirality projectors)**。

*证明*：先算 $$\bigl(\gamma^0\gamma^1\gamma^2\gamma^3\bigr)^2$$。对两两反交换的 $$a_1,\dots,a_m$$ 有

$$(a_1a_2\cdots a_m)^2=(-1)^{\binom m2}a_1^2a_2^2\cdots a_m^2$$

（把后半串逐个穿过前半串，共 $$\binom m2$$ 次换位，每次一次变号；同一位置的因子交换不变号）。取 $$m=4$$、$$a_\mu=\gamma^\mu$$：

$$\bigl(\gamma^0\gamma^1\gamma^2\gamma^3\bigr)^2=(-1)^{6}(\gamma^0)^2(\gamma^1)^2(\gamma^2)^2(\gamma^3)^2=1\cdot1\cdot(-1)\cdot(-1)\cdot(-1)=-1,$$

故 $$\gamma_5^2=i^2\cdot(-1)=(-1)(-1)=1$$。再算 $$\gamma_5\gamma^\mu$$：在 $$i\gamma^0\gamma^1\gamma^2\gamma^3$$ 中，$$\gamma^\mu$$（与它反交换的）共有 $$3$$ 个（$$\mu$$ 自身那一个是同一个因子，交换时不变号），把 $$\gamma^\mu$$ 从左端搬到右端要越过这 $$3$$ 个，共 $$3$$ 次变号，故

$$\gamma_5\gamma^\mu=-\gamma^\mu\gamma_5.$$

特征值只能是 $$\pm1$$（$$\gamma_5$$ 满足 $$t^2-1$$，该多项式无重根，故 $$\gamma_5$$ 可对角化）。由反交换性，若 $$\gamma_5v=\lambda v$$ 则

$$\gamma_5(\gamma^\mu v)=-\gamma^\mu\gamma_5v=-\lambda(\gamma^\mu v),$$

即 $$\gamma^\mu$$ 把特征空间 $$S_\lambda$$ 映入 $$S_{-\lambda}$$；又 $$(\gamma^\mu)^2=\pm I$$ 使 $$\gamma^\mu$$ 可逆，故它是同构，$$\dim S_+=\dim S_-$$。两者之和为 $$\dim S=4$$，故各为 $$2$$。最后

$$P_\pm^2=\tfrac14\bigl(I\pm\gamma_5\bigr)^2=\tfrac14\bigl(I\pm2\gamma_5+\gamma_5^2\bigr)=\tfrac14\bigl(2I\pm2\gamma_5\bigr)=P_\pm,$$

即 $$P_\pm$$ 是投影。$$\blacksquare$$

$$\gamma_5$$ 的具体形状依赖基的选择。在 Dirac–Pauli 表示（定理 3.8(i)）下一次算得 $$\gamma^0\gamma^1\gamma^2\gamma^3=\begin{pmatrix}0&-iI_2\\-iI_2&0\end{pmatrix}$$（用 $$\sigma_1\sigma_2\sigma_3=iI_2$$），故 $$\gamma_5=\begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix}$$——它**不是**对角的。若作基变换换成 **Weyl 表示**

$$\gamma^0=\begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix},\qquad \gamma^i=\begin{pmatrix}0&\sigma_i\\ -\sigma_i&0\end{pmatrix},$$

则 $$\gamma_5=\operatorname{diag}(-I_2,I_2)$$ 变成对角，两个手征子空间就是上下两个坐标块，$$\gamma^\mu$$ 的块结构使得它把上下两块互换。第六节的练习会给这个计算。

**定理 3.14（「绕两圈」）** 在定理 3.12 的对应下，$$\mathrm{SO}(1,3)^{\uparrow}$$ 中绕 $$x^3$$ 轴转 $$\theta$$ 的单参数子群，其 $$\mathrm{SL}(2,\mathbb C)$$ 提升为

$$A(\theta)=\begin{pmatrix}e^{i\theta/2}&0\\ 0&e^{-i\theta/2}\end{pmatrix}\in\mathrm{SL}(2,\mathbb C).$$

因此 $$\theta:0\to2\pi$$ 给出 $$\mathrm{SL}(2,\mathbb C)$$ 中从 $$I_2$$ 到 $$-I_2$$ 的道路，它的像在 $$\mathrm{SO}(1,3)^{\uparrow}$$ 中是一条从 $$\operatorname{id}$$ 出发的闭路，而且是 $$\pi_1=\mathbb Z/2$$ 中非平凡的类。**要在 $$\mathrm{SL}(2,\mathbb C)$$ 里回到单位元，必须转满 $$4\pi$$（绕两圈）。**

*证明*：在定理 3.12 的模型里取 $$A=A(\theta)$$，对 $$X=x^0I+x^1\sigma_1+x^2\sigma_2+x^3\sigma_3$$ 计算 $$A(\theta)XA(\theta)^*$$，只有含 $$\sigma_1,\sigma_2$$ 的项受相位影响：

$$e^{i\theta/2}(x^1-ix^2)e^{i\theta/2}=e^{i\theta}(x^1-ix^2),\qquad e^{-i\theta/2}(x^1+ix^2)e^{-i\theta/2}=e^{-i\theta}(x^1+ix^2),$$

而对角项不变，且 $$x^0,x^3$$ 的项也不变。这恰是 $$(x^1,x^2)$$ 平面内转 $$\theta$$ 的变换，且 $$x^0,x^3$$ 不动——即说 $$\Lambda(A(\theta))$$ 是绕 $$x^3$$ 的转动。$$\theta=0$$ 给 $$A=I_2$$，$$\theta=2\pi$$ 给 $$A=\operatorname{diag}(-1,-1)=-I_2\ne I_2$$，两者在 $$\mathrm{SO}(1,3)^{\uparrow}$$ 中却是同一个元（定理 3.12(iii) 的核）。由定理 3.12(iv)，$$\pi_1(\mathrm{SO}(1,3)^{\uparrow})=\mathbb Z/2$$，故这条路闭路非平凡；$$\theta:0\to4\pi$$ 才使 $$A$$ 回到 $$I_2$$。$$\blacksquare$$

用 Clifford 语言看同一件事：$$\theta\mapsto \exp\bigl(\tfrac\theta2 e_1e_2\bigr)$$ 在 $$\theta=2\pi$$ 时等于 $$\cos\pi+\sin\pi\, e_1e_2=-\mathbf 1$$，而 $$-\mathbf 1$$ 在向量上的共轭作用是恒等（定理 3.11 的核）。**「转两圈」不是比喻，它是 $$\mathrm{Spin}$$ 到 $$SO$$ 的核在具体单参数子群上的显形。**

### 3.5 反射生成正交群，Witt 理论

**定理 3.15（Cartan–Dieudonné）** 设 $$(V,q)$$ 非退化、$$\dim V=n$$。则 $$O(q)$$ 中每个元素都是**不超过 $$n$$ 个**反射的复合；行列式为 $$1$$ 的那部分（旋转）是**偶数个**反射的复合。

*证明思路*：对 $$n$$ 作归纳，作用于向量被移动的数目。若 $$\varphi=\operatorname{id}$$ 则用零个反射。否则取 $$v$$ 使 $$\varphi(v)\ne v$$；由于 $$\varphi\in O(q)$$，可验证 $$y=\varphi(v)-v$$ 是**非迷向**的（若 $$q(y)=0$$，则 $$q(\varphi(v))=q(v)$$ 会导出 $$q(\varphi(v)-v)=2q(v)-2b(\varphi v,v)=0$$ 与另一条关系冲突，除非 $$\varphi v=v$$）。于是 $$\tau_y$$ 把 $$\varphi(v)$$ 送到 $$v$$：先用 $$\tau_y$$ 的显式公式验算 $$\tau_y(\varphi(v))=v$$，再看 $$\tau_y\varphi$$ 固定 $$v$$ 且仍需处理其余 $$n-1$$ 维（它在 $$v^{\perp}$$ 上仍正交），归纳即得。$$\blacksquare$$

把三明治公式（定理 3.9）与 Cartan–Dieudonné 拼起来，得到一个漂亮的结论：**$$O(q)$$ 的每个元素都是 $$\Gamma(V,q)$$ 中某个 $$s$$ 的共轭作用**；行列式为 $$1$$ 的那部分来自偶长的乘积，正是 $$\mathrm{Spin}(V,q)$$ 的像。这就是定理 3.11 的 $$\rho$$ 在几何上的意义。

**定理 3.16（Witt 消去与分解）** 设 $$(V,q)$$ 非退化。

**(i)（Witt 消去）** 若 $$(V_1,q_1)\perp(V,q)\cong(V_2,q_2)\perp(V,q)$$（正交直和），则 $$(V_1,q_1)\cong(V_2,q_2)$$。

**(ii)（Witt 分解）** $$(V,q)$$ 可分解为

$$(V,q)\cong(H_1\perp H_2\perp\cdots\perp H_m)\perp(W,q),$$

其中每个 $$H_i$$ 是 $$2$$ 维**双曲平面 (hyperbolic plane)**，由一对迷向向量 $$x,y$$ 张成（$$q(x)=q(y)=0$$，$$b(x,y)\ne0$$），而 $$W$$ 是**非迷向**（不含非零迷向向量）的部分；在同构意义下 $$m$$ 与 $$W$$ 唯一。

*证明思路 (i)*：对 $$\dim V$$ 归纳。把两个正交直和看成同一个二次空间 $$(U,q)$$ 的两种分解；取 $$V$$ 中非迷向向量并适度选择，用反射把 $$V_1$$ 与 $$V_2$$ 的一个共同直和分量对齐，再在正交补上归纳——反射是这里的关键工具。$$\blacksquare$$

*证明思路 (ii)*：若 $$(V,q)$$ 不含非零迷向向量，取 $$m=0,\ W=V$$。否则取迷向 $$x\ne0$$，因 $$q$$ 非退化存在 $$y$$ 使 $$b(x,y)\ne0$$，把 $$y$$ 减去 $$x$$ 的倍数使 $$q(y)=0$$，则 $$H_1=\operatorname{span}(x,y)$$ 是双曲平面且 $$(V,q)\cong(H_1)\perp(H_1^{\perp})$$；对 $$H_1^{\perp}$$ 重复（维数下降），有限步停止。唯一性由 (i) 与维数计数给出。$$\blacksquare$$

在 $$\mathbb R^{1,3}$$ 里，$$m=1$$：Minkowski 空间恰由一个双曲平面（由两个光向量的组合给出）加上一个 $$2$$ 维非迷向部分构成——这就是「光锥的存在」在代数上的精确表达。这正是第 04 章的迷向向量与本章的 Clifford 代数在同一个地方碰头。

## 四、几何与物理直觉 (Intuition)

**一幅图：同一个模板的两端。** 把本章与第 07 章并排放在一起看：

$$T(V)\ \xrightarrow{\ \text{商掉 }v\otimes v\ }\ \Lambda(V)\quad(\text{度量被遗忘}),\qquad T(V)\ \xrightarrow{\ \text{商掉 }v\otimes v-q(v)\mathbf 1\ }\ \mathrm{Cl}(V,q)\quad(\text{度量被记住}).$$

外代数的乘法是「有向面积」的乘法：它只关心**次序**（交换变号），不关心长度。Clifford 乘法则同时记住次序与长度：$$vw+wv=2b(v,w)$$ 里的 $$b(v,w)$$ 就是长度与夹角。**「为什么叫代数」在这里有了答案**：因为它有乘法、有单位元、满足结合律，而且乘法规则里整个二次型都封存进去了。第 07 章的 $$\Lambda(V)$$ 与本章的 $$\mathrm{Cl}(V,q)$$ 是同一台机器装了两个不同的「关系模块」——把它们并排看，才看出「外代数」这个名字其实是一族结构里最松的那一端。

**反射是几何进入代数的通道。** 定理 3.9 说，反射这个最朴素的几何操作，在 Clifford 代数里就是一次共轭 $$-y\,x\,y^{-1}$$。于是「一串反射」变成「一个积」，而「偶长串」构成的集合就是自旋群。**几何的反射群与代数的可逆元群在这一行公式上对上了**；Cartan–Dieudonné 反过来告诉你，这个群的像已经覆盖了旋转的全部。这不是巧合，而是三明治公式的必然。

**物理：为什么自旋 $$1/2$$ 的粒子要「绕两圈」。** 一个自旋 $$1/2$$ 的粒子（电子、中子）的**态**不是由空间转动直接作用的，而是由它的双层覆叠中的元素（第 26 章的 $$q\in S^3$$、本章的 $$A\in\mathrm{SL}(2,\mathbb C)$$）作用的；$$A$$ 与 $$-A$$ 给出同一个转动，但在态上**作用差一个符号**。所以把粒子转 $$360^\circ$$ 会让态变成相反数，只有转 $$720^\circ$$ 才真正复原。中子干涉仪把这个符号测了出来——这是「多出的一层」在实验室里被看见的少数例子之一。

**Lorentz 群的分量。** $$O(1,3)$$ 由两个不变量切成四块：$$\det$$ 的符号（$$\pm1$$）与是否保持时间方向（把前向锥映到自身还是相反）。$$\mathrm{SO}(1,3)^{\uparrow}$$ 是含单位元的那一块，是连通的，也是物理上唯一可实现的部分（时间不能倒流）。本章的覆叠正是它的覆叠：$$\mathrm{SL}(2,\mathbb C)\to\mathrm{SO}(1,3)^{\uparrow}$$。**光锥对应「迷向锥」**——$$\det X=0$$ 的 $$x$$ 全体，也就是与自己正交的非零向量，即定理 3.16 里那个双曲平面 $$H_1$$ 张成的对象。

**三段对应的第四条链。** 几何：等距群 $$O(q)$$、反射、双曲平面与 Witt 分解；物理：Lorentz 不变性、$$\gamma$$ 矩阵、Dirac 旋量、手征；代数：$$\mathrm{Cl}(V,q)$$、$$\mathrm{Spin}(V,q)$$、偶子代数 $$\mathrm{Cl}^0$$。第 26 章那条链（$$SO(2)\cong S^1$$ 与 $$SO(3)\cong S^3/\{\pm1\}$$）在这里升级成第四条、也是最后一条：$$SO(1,3)^{\uparrow}\cong\mathrm{SL}(2,\mathbb C)/\{\pm I\}$$——**同一个「对径折叠」动作，第四个维度**。

## 五、经典问题精讲 (Classical Problems)

**问题 5.1（考点：定理 3.9 三明治公式、定理 3.15）** 设 $$u,v$$ 是欧氏平面 $$\mathbb R^2$$ 中的单位向量，夹角为 $$\theta$$（故 $$b(u,v)=\cos\theta$$）。求 $$\tau_u\tau_v$$ 的几何意义。

*解*：由定理 3.9 的第二式（取 $$2k=2$$），

$$\tau_u\tau_v(x)=(uv)\,x\,(uv)^{-1},$$

所以只要看清乘积 $$uv$$ 的作用。取一组正交归一基使 $$u=(1,0)$$、$$v=(\cos\theta,\sin\theta)$$。

先算 $$\tau_v(u)$$。由定义 3.9，

$$\tau_v(u)=u-2b(u,v)v=u-2\cos\theta\,v=(1,0)-2\cos\theta(\cos\theta,\sin\theta)=(1-2\cos^2\theta,\,-2\sin\theta\cos\theta)=(-\cos2\theta,\,-\sin2\theta).$$

再作用 $$\tau_u$$：对任意 $$w=(a,b)$$，因 $$u=(1,0)$$、$$b(w,u)=a$$，有 $$\tau_u(w)=w-2a\,u=(a,b)-2a(1,0)=(-a,b)$$。于是

$$\tau_u\tau_v(u)=(\cos2\theta,\,-\sin2\theta).$$

再算 $$\tau_u\tau_v(0,1)$$：

$$\tau_v(0,1)=(0,1)-2\sin\theta(\cos\theta,\sin\theta)=(-2\sin\theta\cos\theta,\,1-2\sin^2\theta)=(-\sin2\theta,\,\cos2\theta),$$

$$\tau_u(-\sin2\theta,\cos2\theta)=(\sin2\theta,\cos2\theta).$$

两个像合起来说明 $$\tau_u\tau_v$$ 在标准基下的矩阵是

$$\begin{pmatrix}\cos2\theta&-\sin2\theta\\ \sin2\theta&\cos2\theta\end{pmatrix}=R_{-2\theta},$$

即**绕原点旋转 $$2\theta$$**（方向取决于基底定向）。特别地 $$\tau_u\tau_v$$ 的行列式为 $$1$$，与定理 3.15 「偶数个反射给旋转」一致。$$\blacksquare$$

**关键 leap**：不要硬算两次投影公式再化简（那会糊成一团），而要用三明治公式把「反射的复合」换成「**乘积的共轭**」，于是只需盯住 $$uv$$ 这一个元素。平面几何里「两次反射合成旋转、转角等于两向量夹角的两倍」是经典结论；本章给出的证明只有两行。

**问题 5.2（考点：定理 3.12 的模型）** 取 $$A=\begin{pmatrix}e^{\varphi/2}&0\\ 0&e^{-\varphi/2}\end{pmatrix}$$（$$\varphi\in\mathbb R$$，故 $$\det A=1$$）。求 $$\Lambda(A)$$ 作用在 $$(x^0,x^1,x^2,x^3)$$ 上的显式公式，并说明它是沿 $$x^3$$ 方向的 boost。

*解*：$$A$$ 是实对角矩阵，故 $$A^*=A$$，且对角相位只打在对角块上：

$$AXA^*=\begin{pmatrix}e^{\varphi/2}&0\\ 0&e^{-\varphi/2}\end{pmatrix}\begin{pmatrix}x^0+x^3&x^1-ix^2\\ x^1+ix^2&x^0-x^3\end{pmatrix}\begin{pmatrix}e^{\varphi/2}&0\\ 0&e^{-\varphi/2}\end{pmatrix}=\begin{pmatrix}e^{\varphi}(x^0+x^3)&x^1-ix^2\\ x^1+ix^2&e^{-\varphi}(x^0-x^3)\end{pmatrix}.$$

非对角块没被改变，对角块被缩放。与标准形状比较：

$$x'^0+x'^3=e^{\varphi}(x^0+x^3),\qquad x'^0-x'^3=e^{-\varphi}(x^0-x^3).$$

两式相加除以 $$2$$、相减除以 $$2$$：

$$x'^0=x^0\cosh\varphi+x^3\sinh\varphi,\qquad x'^3=x^0\sinh\varphi+x^3\cosh\varphi,\qquad x'^1=x^1,\quad x'^2=x^2.$$

这正是沿 $$x^3$$ 方向、**快度 (rapidity)** 为 $$\varphi$$ 的标准 Lorentz boost。$$\varphi=0$$ 给恒等；$$\det\Lambda(A)=1$$ 由定理 3.12(iii) 保证。$$\blacksquare$$

**读法**：「转 $$\theta$$」与「boost $$\varphi$$」在这套语言里是同一件事——取

$$A=\operatorname{diag}\bigl(e^{(\varphi+i\theta)/2},\,e^{-(\varphi+i\theta)/2}\bigr)$$

就把二者同时装进一个对角矩阵。**Lorentz 群的六维 Lie 代数在这套坐标下被压成两个对角入口**，这是 $$\mathrm{SL}(2,\mathbb C)$$ 记号好用的根本原因。

**问题 5.3（考点：定理 3.13 手征分解）** 在 **Weyl 表示**

$$\gamma^0=\begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix},\qquad \gamma^i=\begin{pmatrix}0&\sigma_i\\ -\sigma_i&0\end{pmatrix}$$

下，求 $$\gamma_5$$、$$P_\pm$$ 的显式矩阵，并验证 $$\gamma^\mu$$ 把两个手征子空间互换。

*解*：先算 $$\gamma^1\gamma^2$$（它与 $$\gamma^0$$ 的选法无关）：

$$\gamma^1\gamma^2=\begin{pmatrix}0&\sigma_1\\ -\sigma_1&0\end{pmatrix}\begin{pmatrix}0&\sigma_2\\ -\sigma_2&0\end{pmatrix}=\begin{pmatrix}-\sigma_1\sigma_2&0\\ 0&-\sigma_1\sigma_2\end{pmatrix}.$$

再左乘 $$\gamma^0$$、右乘 $$\gamma^3$$：

$$\gamma^0(\gamma^1\gamma^2)=\begin{pmatrix}0&-\sigma_1\sigma_2\\ -\sigma_1\sigma_2&0\end{pmatrix},\qquad \gamma^0\gamma^1\gamma^2\gamma^3=\begin{pmatrix}0&-\sigma_1\sigma_2\\ -\sigma_1\sigma_2&0\end{pmatrix}\begin{pmatrix}0&\sigma_3\\ -\sigma_3&0\end{pmatrix}=\begin{pmatrix}\sigma_1\sigma_2\sigma_3&0\\ 0&-\sigma_1\sigma_2\sigma_3\end{pmatrix}.$$

由 $$\sigma_1\sigma_2=i\sigma_3$$、$$\sigma_3^2=I_2$$ 得 $$\sigma_1\sigma_2\sigma_3=iI_2$$，所以

$$\gamma^0\gamma^1\gamma^2\gamma^3=\begin{pmatrix}iI_2&0\\ 0&-iI_2\end{pmatrix},\qquad \gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3=\begin{pmatrix}-I_2&0\\ 0&I_2\end{pmatrix}.$$

$$\gamma_5$$ 对角、$$\gamma_5^2=I$$ 一目了然。于是

$$P_+=\tfrac12(I+\gamma_5)=\begin{pmatrix}0&0\\ 0&I_2\end{pmatrix},\qquad P_-=\tfrac12(I-\gamma_5)=\begin{pmatrix}I_2&0\\ 0&0\end{pmatrix},$$

即 $$S_+=\Bigl\{\binom{0}{w}\Bigr\}$$（下半块）、$$S_-=\Bigl\{\binom{u}{0}\Bigr\}$$（上半块）。互换性直接看块结构：

$$\gamma^0\begin{pmatrix}u\\ 0\end{pmatrix}=\begin{pmatrix}0\\ u\end{pmatrix},\qquad \gamma^i\begin{pmatrix}u\\ 0\end{pmatrix}=\begin{pmatrix}0\\ -\sigma_iu\end{pmatrix},$$

两者都落在下半块；反向同理。$$\blacksquare$$

**关键 leap**：先算 $$\gamma^1\gamma^2$$ 这个**块对角**的量，再乘 $$\gamma^0$$（交换上下块）与 $$\gamma^3$$，比逐元素硬乘 4×4 快得多。手征分解之所以在物理里重要，是因为弱相互作用只作用在其中一个手征分量上——**$$\gamma_5$$ 的特征空间不是技术细节，而是守恒律的载体**。

**问题 5.4（考点：定理 3.14、定理 3.12(iv)）** 证明不存在连续映射 $$s:\mathrm{SO}(1,3)^{\uparrow}\to\mathrm{SL}(2,\mathbb C)$$ 使 $$\Lambda\circ s=\operatorname{id}$$（这样的 $$s$$ 称为这个覆叠的一个**连续截面**）。由此说明「绕两圈」不是约定的产物，而是拓扑强制的。

*解*：设这样的 $$s$$ 存在。取 $$A(\theta)=\operatorname{diag}\bigl(e^{i\theta/2},e^{-i\theta/2}\bigr)\in\mathrm{SL}(2,\mathbb C)$$，$$\theta\in[0,2\pi]$$，并置

$$\gamma(\theta)=\Lambda\bigl(A(\theta)\bigr)\in\mathrm{SO}(1,3)^{\uparrow}.$$

由定理 3.12(iii) 的核 $$\Lambda(-I_2)=\Lambda(I_2)=\operatorname{id}$$ 与定理 3.14，$$\gamma(0)=\operatorname{id}$$、$$\gamma(2\pi)=\operatorname{id}$$，故 $$\gamma$$ 是一条**闭路**。

现在看 $$s(\gamma(\theta))$$。由 $$\Lambda(s(\gamma(\theta)))=\gamma(\theta)=\Lambda(A(\theta))$$ 与 $$\ker\Lambda=\{\pm I_2\}$$，

$$s(\gamma(\theta))=\pm A(\theta)\qquad(\forall\theta).$$

左端随 $$\theta$$ 连续，而核是离散的两点集，故符号必须与 $$\theta$$ 无关：存在 $$\varepsilon\in\{\pm1\}$$ 使 $$s(\gamma(\theta))=\varepsilon A(\theta)$$ 对一切 $$\theta$$。取 $$\theta=2\pi$$：

$$s(\gamma(2\pi))=\varepsilon A(2\pi)=-\varepsilon I_2.$$

但 $$\gamma(2\pi)=\gamma(0)$$，故 $$s(\gamma(2\pi))=s(\gamma(0))=\varepsilon A(0)=\varepsilon I_2$$。两式相加得 $$-\varepsilon I_2=\varepsilon I_2$$，即 $$2\varepsilon=0$$，与 $$\varepsilon=\pm1$$ 矛盾。**结论：连续截面不存在。**$$\blacksquare$$

**关键 leap**：矛盾不在几何而在**连通性**——$$\{\pm A(\theta)\}$$ 这一对随 $$\theta$$ 连续地转过 $$360^\circ$$ 时交换了身份，而连续函数不能在中途跳变。$$\mathrm{SL}(2,\mathbb C)$$ 是 $$\mathrm{SO}(1,3)^{\uparrow}$$ 的**非平凡**双层覆叠：局部可拆、整体不可拆，「绕两圈」正是这个不可拆性的长度。



## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 计算一维二次空间 $$\mathrm{Cl}(\mathbb R,q_+)$$ 与 $$\mathrm{Cl}(\mathbb R,q_-)$$，其中 $$q_+(x)=x^2$$、$$q_-(x)=-x^2$$。给出乘法表，并说出它们分别同构于哪个熟悉的代数。

**基2.** 在 $$\mathrm{Cl}(1,1)$$（生成元 $$e_0,e_1$$，$$e_0^2=1$$、$$e_1^2=-1$$、$$e_0e_1+e_1e_0=0$$）中：(a) 计算 $$(e_0e_1)^2$$；(b) 给出实代数同构 $$\mathrm{Cl}(1,1)\cong M_2(\mathbb R)$$ 的显式实现。

**基3.** 对 $$V=\mathbb R^{1,3}$$，写出 $$\mathrm{Cl}(V,q)$$ 的偶子代数 $$\mathrm{Cl}^0$$ 的一组基，算出 $$\dim\mathrm{Cl}^0$$，并说明为什么 $$\mathrm{Cl}^0$$ 对乘法封闭。

**基4.** 在 $$\mathbb R^{1,3}$$ 中取 $$x=(1,1,0,0)$$、$$y=(1,-1,0,0)$$。(a) 验证 $$q(x)=q(y)=0$$ 而 $$b(x,y)\ne0$$；(b) 它们张成的平面里有没有非迷向向量？给出一个；(c) 说明为什么 $$\mathbb R^{1,3}$$ 中不存在二维的「全迷向」子空间（每个非零向量都迷向）。

### 竞赛（本课目标难度）

**竞1.** 设 $$v_1,\dots,v_k\in V$$ 线性无关、两两正交且各非迷向。证明 $$s=v_1v_2\cdots v_k$$ 在 $$\mathrm{Cl}(V,q)$$ 中可逆，并求出 $$s^{-1}$$。

**竞2.** 对 $$\mathbb R^{1,3}$$ 取标准正交基 $$e_0,e_1,e_2,e_3$$。计算 $$\tau_{e_0}\tau_{e_1}\tau_{e_2}\tau_{e_3}$$，并回答：它属于 $$\mathrm{SO}(1,3)^{\uparrow}$$ 吗？再验证三明治公式给出的结果是 $$\omega x\omega^{-1}$$（$$\omega=e_0e_1e_2e_3$$），并由此说明 $$\mathrm{SO}(1,3)$$ 不是连通的。

**竞3.** 设 $$\omega=e_0e_1e_2e_3\in\mathrm{Cl}(1,3)$$。(a) 证明 $$\omega$$ 与每个 $$e_\mu$$ 反交换，且 $$\omega^2=-1$$；(b) 证明 $$\omega$$ 与 $$\mathrm{Cl}^0$$ 中每个元素交换，而与 $$\mathrm{Cl}^1$$ 中每个元素反交换。

**竞4.** 用定理 3.12 的 Hermite 矩阵模型证明：$$x\in\mathbb R^{1,3}$$ 满足 $$q(x)>0$$ 当且仅当 $$X(x)$$ 正定或负定；进一步，$$q(x)>0$$ 且 $$x^0>0$$ 当且仅当 $$X(x)$$ 正定。

**竞5.** 证明定理 3.12 的覆叠限制在 $$\mathrm{SU}(2)=\{A\in M_2(\mathbb C):AA^*=I,\ \det A=1\}$$ 上，给出第 26 章的双重覆叠 $$\mathrm{SU}(2)\to\mathrm{SO}(3)$$。也就是说，第 26 章是本章在 $$x^0=0$$ 截面上的特例。

### 研究（通向下一章）

**研1.** 设 $$T\subseteq\mathbb R^{1,3}$$ 是**全迷向**子空间（每个向量都迷向）。(a) 证明 $$\dim T\le1$$；(b) 证明定理 3.16 的 Witt 分解在 $$\mathbb R^{1,3}$$ 上给出 $$m=1$$，并说出其中的非迷向部分 $$W$$（即双曲因子之外的那一块）的符号差。

**研2.** 记 $$S=\mathbb C^4$$ 为 Dirac 旋量空间，并记 $$\mathrm{SL}(2,\mathbb C)$$ 通过 $$A\mapsto\operatorname{diag}\bigl(A,(A^*)^{-1}\bigr)$$ 作用在 $$S$$ 上。证明：这个作用**不能**下降为 $$\mathrm{SO}(1,3)^{\uparrow}$$ 的表示（即不存在连续同态 $$\mathrm{SO}(1,3)^{\uparrow}\to\mathrm{GL}(S)$$ 与它相容），但**可以**下降为到射影线性群 $$\mathrm{PGL}(S)$$ 的同态。解释这为什么正是量子力学里「态矢差一个相位」的数学形态。

### 解答 (Solutions)

**解 基1.** 一维时 $$\mathrm{Cl}$$ 由 $$\mathbf 1$$ 与 $$e$$ 张成（定理 3.5，$$2^1=2$$ 维），且 $$e^2=q(e)\mathbf 1$$。

对 $$q_+$$：取 $$A=\mathbb R\oplus\mathbb R$$，线性映射 $$j:\mathbb R\to A$$ 为 $$j(1)=(1,-1)$$。它满足

$$j(1)^2=(1,-1)^2=(1,1)=q_+(1)\mathbf 1_A,$$

故由定理 3.4（万有性质）唯一延拓为代数同态 $$\tilde j:\mathrm{Cl}(\mathbb R,q_+)\to\mathbb R\oplus\mathbb R$$，$$e\mapsto(1,-1)$$。像含有 $$\mathbf 1=(1,1)$$ 与 $$(1,-1)$$，而这两者张成 $$\mathbb R\oplus\mathbb R$$，故 $$\tilde j$$ 满射；两边都是 $$2$$ 维实代数，满射必是单射。于是

$$\mathrm{Cl}(\mathbb R,q_+)\cong\mathbb R\oplus\mathbb R.$$

（顺带可见它是零因子代数：$$(\mathbf 1+e)(\mathbf 1-e)=\mathbf 1-e^2=0$$，而 $$\mathbf 1\pm e\ne0$$。）

对 $$q_-$$：取 $$A=\mathbb C$$、$$j(1)=i$$，则 $$j(1)^2=-1=q_-(1)\mathbf 1_{\mathbb C}$$，同样得到满射同态 $$\mathrm{Cl}(\mathbb R,q_-)\to\mathbb C$$（像含 $$1$$ 与 $$i$$），两边 $$2$$ 维，故是同构：

$$\mathrm{Cl}(\mathbb R,q_-)\cong\mathbb C.$$

**一句话对照**：$$e^2=1$$ 给出 $$\mathbb R\oplus\mathbb R$$，$$e^2=-1$$ 给出 $$\mathbb C$$——**二次型的符号直接决定了代数长什么样**，这正是定义 3.4 里那个 $$q(v)\mathbf 1$$ 的作用。$$\blacksquare$$

**解 基2.** (a) 反复用 $$e_0e_1=-e_1e_0$$ 与 $$e_0^2=1,e_1^2=-1$$：

$$(e_0e_1)^2=e_0e_1e_0e_1=(-e_1e_0)e_0e_1=-e_1e_0^2e_1=-e_1^2=1.$$

(b) 取

$$E_0=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\qquad E_1=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}.$$

验证：$$E_0^2=I$$；$$E_1^2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}^2=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}=-I$$。反交换：

$$E_0E_1=\begin{pmatrix}-1&0\\ 0&1\end{pmatrix},\qquad E_1E_0=\begin{pmatrix}1&0\\ 0&-1\end{pmatrix},$$

两者之和为零。于是 $$e_0\mapsto E_0$$、$$e_1\mapsto E_1$$ 满足 $$e_i^2=q(e_i)$$ 与反交换，由定理 3.4（万有性质）延拓为同态 $$\mathrm{Cl}(1,1)\to M_2(\mathbb R)$$。它是单射：$$1,E_0,E_1,E_0E_1$$ 四个矩阵线性无关（写出矩阵即为

$$I,\quad \begin{pmatrix}0&1\\1&0\end{pmatrix},\quad \begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad \begin{pmatrix}-1&0\\0&1\end{pmatrix},$$

写出矩阵即可看出四个矩阵线性无关），张成 $$M_2(\mathbb R)$$ 的 $$4$$ 维子空间即全体。故是同构。$$\blacksquare$$

**解 基3.** 取定正交基 $$e_0,e_1,e_2,e_3$$。由定理 3.6，递增乘积按长度奇偶分块，偶数长度的有 $$\binom40+\binom42+\binom44=1+6+1=8$$ 个：

$$\mathbf 1;\qquad e_\mu e_\nu\ (0\le\mu<\nu\le3),\ \text{共 }6\text{ 个};\qquad e_0e_1e_2e_3.$$

故 $$\dim\mathrm{Cl}^0=8=2^{4-1}$$。对乘法封闭：两个偶数长度乘积的拼接长度是偶数；再用 $$e_\mu e_\nu=-e_\nu e_\mu$$ 与 $$e_\mu^2=q(e_\mu)$$ 化简，得到的仍是偶数长度递增乘积的线性组合，落在 $$\mathrm{Cl}^0$$ 内。$$\blacksquare$$

**解 基4.** (a) 直接代入 $$q(x)=(x^0)^2-(x^1)^2-(x^2)^2-(x^3)^2$$：

$$q(x)=1-1=0,\qquad q(y)=1-1=0,\qquad b(x,y)=1\cdot1-(1)(-1)-0-0=2\ne0.$$

（$$b$$ 由极化恒等式给出，对 $$\eta=\operatorname{diag}(1,-1,-1,-1)$$ 即 $$b(x,y)=x^0y^0-x^1y^1-x^2y^2-x^3y^3$$。）

(b) 有。取 $$x+y=(2,0,0,0)$$，$$q(x+y)=4\ne0$$；也可取 $$x-y=(0,2,0,0)$$，$$q=0-4=-4\ne0$$。所以 span$$\{x,y\}$$ 里有非迷向向量，它不是全迷向的。

(c) 设 $$W$$ 全迷向，则 $$q\vert_W\equiv0$$；由极化恒等式（定理 3.1 的公式），$$b\vert_W\equiv0$$ 也成立。若 $$\dim W\ge2$$，取线性无关的 $$x,y\in W$$，则 $$W\subseteq W^{\perp}$$（因为 $$b(x,y)=0$$ 对一切 $$x,y\in W$$ 成立），于是 $$\dim W\le\dim W^{\perp}=4-\dim W$$，即 $$\dim W\le2$$。若 $$\dim W=2$$，则 $$W=W^{\perp}$$，把 $$\mathbb R^{1,3}=W\oplus W'$$ 按此分解写下来，形式为 $$\begin{pmatrix}0&M\\ M^{\mathsf T}&N\end{pmatrix}$$（$$M$$ 可逆，因 $$W'$$ 与 $$W$$ 的配对非退化）。计算这种形式的符号差：取基把 $$M$$ 化为单位阵、$$N$$ 化为 $$\operatorname{diag}(n_1,n_2)$$，则二次型是 $$2u_1v_1+2u_2v_2+n_1u_1^2+n_2u_2^2$$，配方后符号差为 $$(2,2)$$。但 $$\mathbb R^{1,3}$$ 的符号差是 $$(1,3)$$，矛盾。故 $$\dim W\le1$$。事实上 $$W=\operatorname{span}\{(1,1,0,0)\}$$ 给出 $$1$$ 维全迷向子空间的例子。$$\blacksquare$$

**解 竞1.** **思路**：把 $$s$$ 与它的「反序」相乘，中间的因子成对消成标量。

证明：记 $$\bar s=v_kv_{k-1}\cdots v_1$$（反序）。由 $$v_iv_j+v_jv_i=2b(v_i,v_j)=0\ (i\ne j)$$ 与 $$v_i^2=q(v_i)\mathbf 1$$，逐个把 $$\bar s$$ 中的因子向左穿过：

$$s\bar s=(v_1v_2\cdots v_k)(v_kv_{k-1}\cdots v_1)=v_1\cdots v_{k-1}\bigl(v_k^2\bigr)v_{k-1}\cdots v_1=q(v_k)\,v_1\cdots v_{k-1}v_{k-1}\cdots v_1.$$

（用 $$v_k$$ 与 $$v_1,\dots,v_{k-1}$$ 反交换，把 $$v_k$$ 移到 $$v_{k-1}$$ 右侧共发生 $$k-1$$ 次换位；但反序乘积里 $$v_k$$ 本来就在最左，所以直接相邻，把 $$v_k$$ 与 $$v_k$$ 相乘得到 $$v_k^2$$，其余因子顺序不变。）继续归纳：

$$s\bar s=q(v_1)q(v_2)\cdots q(v_k)\mathbf 1.$$

每个 $$q(v_i)\ne0$$（非迷向），故右端是标量 $$\mathbf 1$$ 的非零倍数，记 $$c=q(v_1)q(v_2)\cdots q(v_k)$$（$$\mathbb R$$ 或 $$\mathbb C$$ 中非零）。于是

$$s^{-1}=c^{-1}\bar s=\frac{v_kv_{k-1}\cdots v_1}{q(v_1)q(v_2)\cdots q(v_k)}.$$

**关键 leap**：不要试图解析地求逆，而要想到「反序乘积」。这个技巧正是定义 3.10 里 $$t(s)$$ 的来源——$$\mathrm{Spin}$$ 的定义条件 $$st(s)=\mathbf 1$$ 就是要求这个标量恰好为 $$1$$。$$\blacksquare$$

**解 竞2.** 先直接算每个反射。对 $$v=e_0$$：$$q(e_0)=1$$、$$b(x,e_0)=x^0$$，故

$$\tau_{e_0}(x)=x-2x^0e_0,$$

即只把 $$x^0$$ 换成 $$-x^0$$。对 $$v=e_i\ (i=1,2,3)$$：$$q(e_i)=-1$$、$$b(x,e_i)=-x^i$$，故

$$\tau_{e_i}(x)=x-\frac{2(-x^i)}{-1}e_i=x-2x^ie_i,$$

即只把 $$x^i$$ 换成 $$-x^i$$。四次复合依次翻转四个坐标，结果是

$$\tau_{e_0}\tau_{e_1}\tau_{e_2}\tau_{e_3}=-\operatorname{id}.$$

**它属于 $$\mathrm{SO}(1,3)^{\uparrow}$$ 吗？** 行列式为 $$(-1)^4=1$$，所以在 $$\mathrm{SO}(1,3)$$ 里；但它把前向锥（$$x^0>\lvert\vec x\rvert$$）送到后向锥（$$x^0<-\lvert\vec x\rvert$$），所以**不保时间方向**，不在 $$\mathrm{SO}(1,3)^{\uparrow}$$ 中。这说明 $$\mathrm{SO}(1,3)$$ 至少有两个连通分支（$$\pm\operatorname{id}$$ 各在一个分支），故不连通。

**三明治验证**：由定理 3.9 的第二式（$$2k=4$$），

$$\tau_{e_0}\tau_{e_1}\tau_{e_2}\tau_{e_3}(x)=(e_0e_1e_2e_3)x(e_0e_1e_2e_3)^{-1}=\omega x\omega^{-1}.$$

与直接的 $$-\operatorname{id}$$ 比较，得 $$\omega x\omega^{-1}=-x$$，即 $$\omega x=-x\omega$$：**体积元与每个向量反交换**。（也可直接数：把 $$x$$ 从 $$\omega$$ 右侧搬到左侧要越过 $$4$$ 个因子，其中与 $$x$$ 反交换的是另外 $$3$$ 个，共 $$3$$ 次变号。）两边一致，验证通过。$$\blacksquare$$

**解 竞3.** (a) $$\omega=e_0e_1e_2e_3$$。把 $$e_\mu$$ 从 $$\omega$$ 的右侧移到左侧，需要越过四个因子中与它反交换的另外三个（与 $$e_\mu$$ 自己相邻时交换不变号），故共 $$3$$ 次变号：

$$\omega e_\mu=(-1)^3e_\mu\omega=-e_\mu\omega.$$

平方：用「两两反交换乘积的平方」公式（定理 3.13 的证明里用过，$$m=4$$ 时符号为 $$(-1)^{\binom42}=(-1)^6=1$$），

$$\omega^2=(-1)^{6}\,e_0^2e_1^2e_2^2e_3^2=1\cdot1\cdot(-1)\cdot(-1)\cdot(-1)=-1.$$

(b) $$\mathrm{Cl}^0$$ 由偶数长度乘积线性张成，其中每个乘积与 $$\omega$$ 的换位次数为偶数（每个因子贡献一次变号，偶数个因子共偶数次），故与 $$\omega$$ 交换；同理 $$\mathrm{Cl}^1$$ 由奇数长度乘积张成，换位次数为奇数，与 $$\omega$$ 反交换。用 (a) 的逐因子规则，对长度为 $$m$$ 的乘积累乘得 $$(-1)^m$$。$$\blacksquare$$

**解 竞4.** 记 $$X=X(x)$$ 为 Hermite 矩阵。

**先证「$$q(x)>0$$ $$\Rightarrow$$ $$X$$ 正定或负定」**：Hermite 矩阵的两个特征值 $$\lambda_1,\lambda_2$$ 都是实数，$$\det X=\lambda_1\lambda_2=q(x)>0$$，故两特征值同号且均非零，于是 $$X$$ 正定（$$\lambda_{1,2}>0$$）或负定（$$\lambda_{1,2}<0$$）。

**再证「$$X$$ 正定或负定 $$\Rightarrow$$ $$q(x)>0$$」**：$$\det X=\lambda_1\lambda_2>0$$，而由 (i) $$\det X=q(x)$$，故 $$q(x)>0$$。

**进一步**：$$\operatorname{tr}X=x^0+x^3+x^0-x^3=2x^0$$。若 $$q(x)>0$$ 且 $$x^0>0$$，则 $$\operatorname{tr}X>0$$，而 $$\lambda_1\lambda_2>0$$ 且 $$\lambda_1+\lambda_2>0$$，故 $$\lambda_1,\lambda_2>0$$，$$X$$ 正定。反之若 $$X$$ 正定，则 $$\operatorname{tr}X>0$$ 即 $$x^0>0$$，且 $$\det X>0$$ 即 $$q(x)>0$$。$$\blacksquare$$

（这就是定理 3.12(iii) 里「保时间方向」那一步的实质：$$A$$ 的作用把正定 Hermite 矩阵送到正定 Hermite 矩阵，而正定对应前向类时锥。）

**解 竞5.** 设 $$A\in\mathrm{SU}(2)$$。

**第一步：$$x^0$$ 不变。** $$\operatorname{tr}(AXA^*)=\operatorname{tr}(XA^*A)=\operatorname{tr}X$$（用了 $$\operatorname{tr}(PQ)=\operatorname{tr}(QP)$$ 与 $$A^*A=I$$）。又 $$\operatorname{tr}X=2x^0$$，故 $$x'^0=x^0$$。

**第二步：空间部分保长度。** 由定理 3.12(ii)，$$q(x')=q(x)$$，即 $$(x'^0)^2-\lvert\vec x'\rvert^2=(x^0)^2-\lvert\vec x\rvert^2$$；由第一步 $$x'^0=x^0$$，故 $$\lvert\vec x'\rvert^2=\lvert\vec x\rvert^2$$。

**第三步：得到一个正交变换。** 把 $$(x^1,x^2,x^3)$$ 看成 $$\mathbb R^3$$，第一、二步说明 $$\Lambda(A)$$ 限制在 $$x^0=0$$ 截面上是一个 $$\mathbb R^3$$ 的正交变换，记作 $$R_A\in O(3)$$。

**第四步：$$\det R_A=1$$。** $$A\mapsto R_A$$ 是连续映射（它是线性映射 $$A\mapsto\Lambda(A)$$ 的限制），$$\mathrm{SU}(2)$$ 连通（它是 $$S^3$$），而 $$\det$$ 取值在离散集 $$\{\pm1\}$$ 中，故 $$\det R_A$$ 为常数；取 $$A=I$$ 得 $$\det R_I=1$$。于是 $$R_A\in\mathrm{SO}(3)$$。

**第五步：核为 $$\{\pm I\}$$。** 由定理 3.12(iii)，$$\Lambda(A)=\operatorname{id}$$ 当且仅当 $$A=\pm I$$；而 $$\Lambda(A)=\operatorname{id}$$ 当且仅当 $$R_A=I$$。（后一等价性：$$\Lambda(A)$$ 由它在 $$x^0=0$$ 截面与 $$x^0$$ 方向上的作用确定，而 $$A\in\mathrm{SU}(2)$$ 时 $$x^0$$ 方向自动不变。）故 $$\ker(R_\bullet)=\{\pm I\}$$。

**第六步：满射。** $$R_\bullet:\mathrm{SU}(2)\to\mathrm{SO}(3)$$ 的像是连通闭子群。$$\mathrm{SU}(2)$$ 与 $$\mathrm{SO}(3)$$ 都是 $$3$$ 维；由第五步，$$\ker R_\bullet=\{\pm I\}$$ 是 $$0$$ 维的，故 $$\dim\operatorname{im}R_\bullet=\dim\mathrm{SU}(2)-\dim\ker=3$$（同态基本定理在 Lie 群层面的维数形式）。$$\mathrm{SO}(3)$$ 是连通的 $$3$$ 维 Lie 群，它唯一的 $$3$$ 维连通子群是它自己（同维数的闭子群是开子群，连通群的非常数开子群不存在），故 $$R_\bullet$$ 满射。

综上，$$A\mapsto R_A$$ 是连续满同态 $$\mathrm{SU}(2)\to\mathrm{SO}(3)$$，核 $$\{\pm I\}$$——这正是第 26 章的定理 3.7 与定理 3.9。**第 26 章是本章在时间坐标冻结时的截面。**$$\blacksquare$$

**解 研1.** (a) 设 $$T$$ 全迷向。则 $$q\vert_T\equiv0$$，由极化恒等式 $$b\vert_T\equiv0$$，即 $$T\subseteq T^{\perp}$$。于是

$$\dim T\le\dim T^{\perp}=4-\dim T\quad\Longrightarrow\quad \dim T\le2.$$

若 $$\dim T=2$$，则 $$T=T^{\perp}$$。取补空间 $$\mathbb R^{1,3}=T\oplus T'$$（$$\dim T'=2$$）。由 $$T=T^{\perp}$$ 知 $$T'$$ 上形式非退化，且配对 $$T\times T'\to\mathbb R$$ 非退化（不然存在 $$t'\in T'$$ 与整个 $$T$$ 正交，即 $$t'\in T^{\perp}=T$$，与 $$t'\notin T$$ 矛盾）。于是有基使矩阵为

$$\begin{pmatrix}0&M\\ M^{\mathsf T}&N\end{pmatrix},\qquad M\ \text{可逆}.$$

作合同变换把 $$M$$ 化为 $$I_2$$、$$N$$ 化为 $$\operatorname{diag}(n_1,n_2)$$，二次型成为

$$2u_1v_1+2u_2v_2+n_1u_1^2+n_2u_2^2.$$

再对每个 $$i$$ 作坐标剪切，把 $$v_i$$ 换成 $$v_i+\tfrac{n_i}{2}u_i$$（配方：$$2u_iv_i+n_iu_i^2=2u_i\bigl(v_i+\tfrac{n_i}{2}u_i\bigr)$$），二次型化为

$$2u_1v_1+2u_2v_2,$$

即两个标准双曲平面的正交和，符号差为 $$(2,2)$$。但 $$\mathbb R^{1,3}$$ 的符号差是 $$(1,3)\ne(2,2)$$，矛盾。故 $$\dim T\le1$$。下界由 $$T=\operatorname{span}\{(1,1,0,0)\}$$ 达到（$$q(1,1,0,0)=0$$）。$$\blacksquare$$

(b) 取迷向 $$x=(1,1,0,0)\ne0$$。因 $$q$$ 非退化，存在 $$y$$ 使 $$b(x,y)\ne0$$；取 $$y=(1,-1,0,0)$$ 时 $$b(x,y)=2$$。把 $$y$$ 换成 $$y-\frac{q(y)}{2b(x,y)}x$$ 可使新向量也迷向（$$q(y-tx)=q(y)-2tb(x,y)+t^2q(x)=q(y)-2tb(x,y)$$，取 $$t=q(y)/(2b(x,y))$$ 使之为 $$0$$）。于是 $$H_1=\operatorname{span}\{x,y'\}$$ 是双曲平面，且 $$\mathbb R^{1,3}=H_1\perp H_1^{\perp}$$。计算 $$H_1^{\perp}$$ 的符号差：$$(1,3)-(1,1)=(0,2)$$，即 $$H_1^{\perp}$$ 是负定的 $$2$$ 维空间，**不含非零迷向向量**。故 Witt 分解为

$$\mathbb R^{1,3}=H_1\perp W,\qquad \dim W=2,\quad W\ \text{负定},$$

即 $$m=1$$、非迷向部分 $$W$$ 的符号差为 $$(0,2)$$。$$\blacksquare$$

**解 研2.** 记 $$\sigma(A)=\operatorname{diag}\bigl(A,(A^*)^{-1}\bigr)\in\mathrm{GL}(S)$$，$$A\in\mathrm{SL}(2,\mathbb C)$$。先验证 $$\sigma$$ 是同态：$$\sigma(AB)=\operatorname{diag}\bigl(AB,((AB)^*)^{-1}\bigr)=\operatorname{diag}(A,(A^*)^{-1})\operatorname{diag}(B,(B^*)^{-1})$$（用 $$(AB)^*=B^*A^*$$ 与 $$(B^*A^*)^{-1}=(A^*)^{-1}(B^*)^{-1}$$）。

**下降为 $$\mathrm{SO}(1,3)^{\uparrow}$$ 的表示？** 若存在连续同态 $$\rho:\mathrm{SO}(1,3)^{\uparrow}\to\mathrm{GL}(S)$$ 使 $$\rho\circ\Lambda=\sigma$$，则取 $$A=-I_2\in\mathrm{SL}(2,\mathbb C)$$：$$\Lambda(-I_2)=\operatorname{id}$$（定理 3.12(iii)），故

$$\sigma(-I_2)=\rho(\Lambda(-I_2))=\rho(\operatorname{id})=I_4.$$

但 $$\sigma(-I_2)=\operatorname{diag}\bigl(-I_2,(-I_2^*)^{-1}\bigr)=\operatorname{diag}(-I_2,-I_2)=-I_4\ne I_4$$。矛盾。故不存在这样的同态。

**下降为射影表示：可以。** 在射影线性群 $$\mathrm{PGL}(S)$$ 里，非零标量倍被等同，故 $$\pm\operatorname{diag}(A,(A^*)^{-1})$$ 给出同一个类。定义

$$\bar\sigma:\ \mathrm{SL}(2,\mathbb C)\longrightarrow\mathrm{PGL}(S),\qquad A\longmapsto\bigl[\sigma(A)\bigr].$$

由 $$\sigma(-A)=-\sigma(A)$$ 与 $$\Lambda(-A)=\Lambda(A)$$ 知 $$\bar\sigma$$ 在 $$\Lambda$$ 的纤维上取常值，于是 $$\bar\sigma=\bar\rho\circ\Lambda$$，其中 $$\bar\rho:\mathrm{SO}(1,3)^{\uparrow}\to\mathrm{PGL}(S)$$ 是良定义的同态。它连续（因为 $$\Lambda$$ 是局部微分同胚、$$\sigma$$ 连续），于是我们得到一个真正的同态 $$\bar\rho$$。

**为什么这正是量子力学的「相位」**：$$\rho$$ 与 $$\bar\rho$$ 的差别恰好是每个元素被允许附上一个非零标量。物理上，量子态由 $$\mathbb C^4$$ 中的**射线**（一维子空间）描述，而不是矢量；把 $$v$$ 与 $$\lambda v$$ 视为同一个态，正是从 $$\mathrm{GL}(S)$$ 走到 $$\mathrm{PGL}(S)$$ 的那一步商。旋量表示只下降为 $$\mathrm{SO}(1,3)^{\uparrow}$$ 的射影表示，而「多出来的符号」就是 $$\mathrm{SL}(2,\mathbb C)$$ 这个双层覆叠的指纹。

注意 $$\bar\rho$$ 的非平凡性来自 $$\sigma$$ 的核：$$\sigma(A)=I_4$$ 只在 $$A=I_2$$ 时成立（对 $$A=-I_2$$ 有 $$\sigma=-I_4\ne I_4$$），所以这个射影表示不是从任何一个普通表示「贴着」来的——它只活在这一层。**一般地，一个群的射影表示由它的万有覆叠的中心扩张来分类，这正是第 30 章（Möbius 群、双重覆盖与射影表示）的起点。**$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

1. **Clifford 代数与外代数是同一个构造的两端。** 两者都是 $$T(V)$$ 商掉一个由二次型数据写出的双边理想：外代数商 $$v\otimes v$$（记住次序、忘掉长度），Clifford 商 $$v\otimes v-q(v)\mathbf 1$$（次序与长度都记住）。$$\mathrm{Cl}(V,0)=\Lambda(V)$$ 说明外代数是一族结构里最松的那个。

2. **维数锁死是「反对易」自己造成的。** 只要 $$\gamma^\mu$$ 两两反交换，表示空间维数就必须被 $$4$$ 整除（定理 3.7 的两次劈半），与二次型的具体数值无关。定理 3.8 从另一个方向给出同一个数：$$\mathrm{Cl}(1,3)\otimes\mathbb C\cong M_4(\mathbb C)$$ 的不可约模唯一。

3. **反射是几何与代数之间的通道。** 三明治公式 $$\tau_y(x)=-yxy^{-1}$$ 把「一串反射」变成「一个积」；偶长的积构成 $$\mathrm{Spin}(V,q)$$，它的共轭作用覆盖 $$O(q)$$ 的旋转部分（Cartan–Dieudonné、Witt 分解都在这一框架内）。

4. **「绕两圈」是拓扑强制的。** $$\mathrm{SL}(2,\mathbb C)$$ 单连通、$$\mathrm{SO}(1,3)^{\uparrow}$$ 有 $$\pi_1=\mathbb Z/2$$，故 $$\mathrm{SL}(2,\mathbb C)\to\mathrm{SO}(1,3)^{\uparrow}$$ 是非平凡的双层覆叠；连续截面不存在（问题 5.4）。

5. **旋量只承载射影表示。** $$-I_2\in\mathrm{SL}(2,\mathbb C)$$ 在向量上作用平凡、在旋量上作用为 $$-I_4$$，于是旋量不能给出 $$\mathrm{SO}(1,3)^{\uparrow}$$ 的普通表示，只能给出射影表示（研究题 2）。

**下一章的悬念**：第 30 章把这一层「多出来的相位」独立出来讲——Möbius 群怎么把 $$\mathrm{SL}(2,\mathbb C)$$ 的作用看成球面上的共形变换？为什么「射影表示」是量子力学里唯一合理的表示概念？本章的 $$\mathrm{Spin}(1,3)$$ 与覆叠，将在那里升级为任意维的 Möbius 群与它的双重覆叠。

**延伸阅读**：Lawson–Michelsohn《Spin Geometry》第一、二章（Clifford 代数与自旋群的系统处理）；Woit《Quantum Theory, Groups and Representations》第 12–15 讲（旋量与射影表示，与本章接口最直接）；Tong《Quantum Field Theory》第 4–5 章（$$\gamma$$ 矩阵与 Dirac 方程的物理用法）。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch28_复半单Lie代数与根系.md">← 第28章 复半单 Lie 代数与根系</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch30_Möbius群_双重覆盖与射影表示.md">第30章 Möbius 群、双重覆盖与射影表示 →</a></div>
</div>
