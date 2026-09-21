---
layout: default
---

# 第24章: 外微分与 Maxwell 方程组·下：完整推导 (Exterior Derivative and Maxwell's Equations · Part II: Full Derivation)

> 配套预备: 见 第23章 外微分与 Maxwell 方程组·上（同一主题的具体铺垫，建议先读）

> 对应原专栏: MP25、MP26、MP36、MP37
> 专家依据: 四专家无专章 —— 主用知识库
> 知识库依据: `opc2/knowledge/physics/电动力学/`（25 篇）、`opc2/knowledge/math/微分几何/differential-geometry/`（ch06、ch08）
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

第 14 章造出了外微分 $$d$$，并证明了全书最重要的一条恒等式 $$d^2=0$$。当时它只是一个代数事实：**分析里的对称（二阶偏导可交换）与代数里的反对称（楔积变号）精确配对，凑出零**。本章要给这条恒等式一个物理名字。

要做三件事。其一，说清**为什么电场 $$\vec E$$ 是 1-形式、磁感应 $$\vec B$$ 是 2-形式**——这不是记号游戏，而是"镜子里左右颠倒"这条中学常识的严格后果（MP25）。其二，引入 **Hodge 星算子 $$\star$$ (Hodge star)**，把 $$\mathbb R^3$$ 上的 grad / curl / div **三个算子统一成同一个 $$d$$**，并证明 $$\operatorname{curl}\circ\operatorname{grad}=0$$ 与 $$\operatorname{div}\circ\operatorname{curl}=0$$ 就是 $$d^2=0$$ 的两种写法（MP26）。其三，把 Maxwell 方程组**从四个压成两个**：

$$dF=0,\qquad d\star F=J,$$

其中 $$F$$ 是把 $$\vec E,\vec B$$ 装在一起的一个 2-形式。$$dF=0$$ 的两个分量，恰好是 $$\nabla\cdot\vec B=0$$ 与 $$\nabla\times\vec E=-\partial_t\vec B$$。一句话点题：**"边界的边界为空"在物理里就叫"不存在磁单极子"**。最后接 MP37：在四维 Minkowski 时空上 $$\star^2=-1$$，$$\star$$ 的特征值为 $$\pm i$$，$$F$$ 分裂成自对偶与反自对偶两部分；由此引出电磁势 $$F=dA$$ 与**规范变换** $$A\mapsto A+df$$。

**从哪来**：第 14 章的 $$d$$ 与 $$d^2=0$$，第 08 章的向量与 1-形式的对偶。**到哪去**：第 26 章的 Stokes 定理——它把 $$d$$、边界、积分焊成一句话，本章的所有物理结论在它那里变成"通量与环量的守恒律"。

## 二、入口：一道具体的问题 (Entry Problem)

**来源**：问题 (a) 取自 MP25 的镜像例子（原文配图），问题 (b) 为自编。**先给题，不给定义。**

### 问题 (a)：镜子里的一辆车

一辆汽车**迎面**朝我们开来。把它关于竖直镜面做镜像，得到的仍是一辆迎面开来的汽车——位置、速度、动量都像所有"正常向量"那样左右翻转。可是把汽车一个车轮的单向旋转也一起镜像，会发现一件怪事：**车轮的角速度向量没有按镜像的预期翻到另一边。** 具体地说，设原车轮自转的角速度向量指向车轴的 A 端，镜像车轮的自转角速度向量**仍然指向 A 端**，而不是镜面反射所要求的 A' 端。于是原车与镜像车并排时，看起来就像"一根轴上装了四个轮子"，四个轮子的角速度都朝同一侧。

同样的事发生在**载流线圈**上：把线圈连同它的磁场一起镜像，镜面两侧的磁场方向一个朝上、一个朝下，而不是按"向量应当满足的镜像规则"翻向另一边。中学老师会说磁场是"轴向量"，可这句话并没有解释任何东西。

**要求**（不许查资料）：

1. 解释为什么角速度和磁场会出现这种不一致；
2. 给出一个**判据**，把物理量分成两类：一类像位移那样规矩镜像，一类像角速度那样反着来；
3. 用你给出的判据说明：为什么 $$\vec E$$ 属于前者、$$\vec B$$ 属于后者。

### 问题 (b)：四个方程里的"零"

中学课本里，真空中的 Maxwell 方程组是四个方程（归一化单位，$$c=1$$）：

$$\begin{cases} \nabla\cdot\vec B=0,\\[3pt] \nabla\times\vec E+\dfrac{\partial\vec B}{\partial t}=0,\\[5pt] \nabla\cdot\vec E=\rho,\\[3pt] \nabla\times\vec B-\dfrac{\partial\vec E}{\partial t}=\vec j.\end{cases}$$

**要求**：

1. 注意前两个方程的形状：它们都是"**某个东西等于零**"，而且是"**某个东西的导数等于零**"。把第 14 章那条 grad / curl / div 与外微分 $$d$$ 的对应关系拿来，把这两个方程改写成 $$d(\text{某个形式})=0$$ 的形状。
2. 设改写成功，那么按第 14 章已经证明的 $$d^2=0$$，你**几乎不必再做计算**，就知道某一类方程必然自动成立。指出是哪一类，并说明为什么这等价于"不存在磁单极子"。
3. 后两个方程（含 $$\rho$$ 与 $$\vec j$$ 的）**不能**写成 $$d(\text{某个东西})=0$$。它们缺什么？本章会补上一个算子 $$\star$$，使它们也被同一个 $$d$$ 写出来。

这道题就是全章的引子：它的第 1 问逼出 Hodge 星算子（第三节 3.2），第 2 问逼出 $$F=dA$$ 与 $$dF=0$$（第五节 3.7），第 3 问逼出 $$d\star F=J$$（第五节 3.8）。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 极向量与轴向量：镜像判据 (Polar and axial vectors)

先解决入口题 (a)。

**定义 3.1（镜像变换 / reflection）**。设 $$P$$ 是 $$\mathbb R^3$$ 的一个正交变换（相对于标准内积保持长度），且 $$\det P=-1$$。称这样的 $$P$$ 为一个**镜像**（更一般地，一个**反常正交变换**）。

**定义 3.2（极向量与轴向量）**。设 $$\vec v$$ 是一个由物理系统决定的、在 $$\mathbb R^3$$ 中取值的量。我们说 $$\vec v$$ 是**极向量 (polar vector)**，如果系统作镜像 $$P$$ 后它变为 $$P\vec v$$；是**轴向量 (axial vector)**，如果它变为 $$(\det P)\,P\vec v=-P\vec v$$。

位移、速度、动量都是极向量。角速度、力矩、磁感应都是轴向量。判据的关键不在"它是不是三个数"，而在**它镜像时是否多出一个负号**。

**命题 3.3（轴向量从何而来：叉乘）**。设 $$\vec a,\vec b$$ 是极向量，则 $$\vec a\times\vec b$$ 是轴向量。

**证明**。只需验证恒等式

$$(P\vec a)\times(P\vec b)=(\det P)\,P(\vec a\times\vec b),\qquad \forall P\in O(3). \tag{24.1}$$

一步步来。对任意正交 $$P$$、任意 $$\vec u\in\mathbb R^3$$，叉乘满足"二阶外积"的变换律：$$(P\vec a)\times(P\vec b)=\det(P)\,P^{-T}(\vec a\times\vec b)$$。这一条可如下验证：两边都是 $$\vec a,\vec b$$ 的双线性反对称映射，取标准基 $$\vec a=\vec e_i,\vec b=\vec e_j$$ 验证即可（此时左边 $$=(P\vec e_i)\times(P\vec e_j)$$ 是 $$P$$ 的第 $$i,j$$ 列的叉乘，正是 $$P$$ 的三个列的任意两列叉乘等于第三列乘行列式，即 $$\det(P)P^{-T}\vec e_k$$）。对 $$P\in O(3)$$ 有 $$P^{-T}=P$$，于是 (24.1) 成立。

现在设 $$P$$ 是镜像（$$\det P=-1$$）。由 (24.1)，$$\vec a\times\vec b$$ 在镜像下变为 $$-P(\vec a\times\vec b)$$，正是定义 3.2 的轴向量要求。$$\square$$

**命题 3.4（轴向量 $$\leftrightarrow$$ 2-形式）**。在 $$\mathbb R^3$$ 中，轴向量与 2-形式有一一对应；极向量与 1-形式有一一对应。

**证明思路**。两个极向量的叉乘产生一个轴向量（命题 3.3），而两个 1-形式的外积产生一个 2-形式（第 14 章 3.4）。对应关系是

$$\vec w=w_1\vec e_1+w_2\vec e_2+w_3\vec e_3\ \longleftrightarrow\ \omega_w=w_1\,dx+w_2\,dy+w_3\,dz\quad(\text{极向量}\leftrightarrow 1\text{-形式}),$$

$$\vec u=u_1\vec e_1+u_2\vec e_2+u_3\vec e_3\ \longleftrightarrow\ \eta_u=u_1\,dy\wedge dz+u_2\,dz\wedge dx+u_3\,dx\wedge dy\quad(\text{轴向量}\leftrightarrow 2\text{-形式}).$$

**证明**。逐点看。设极向量 $$\vec a,\vec b$$ 对应 $$\alpha,\beta\in\Omega^1$$。第 14 章的 3.9 节已把 $$\mathbb R^3$$ 的 1-形式与向量对齐，而 1-形式的外积在坐标下是

$$\alpha\wedge\beta=(a_1b_2-a_2b_1)dx\wedge dy+(a_2b_3-a_3b_2)dy\wedge dz+(a_3b_1-a_1b_3)dz\wedge dx.$$

右端三个系数正是 $$\vec a\times\vec b$$ 的三个分量（按同一顺序）。所以

$$\vec a\times\vec b\ \longleftrightarrow\ \alpha\wedge\beta .$$

叉乘的结果是轴向量（命题 3.3），外积的结果是 2-形式，两者又都是一一对应（$$\mathbb R^3$$ 中 1-形式与 2-形式的维数都是 $$3$$），故轴向量与 2-形式的一一对应成立。极向量与 1-形式的对应是定义。$$\square$$

**物理落点**。电势 $$U$$ 是 0-形式，$$\vec E=-\nabla U=-dU$$ 是 $$d$$ 作用在 0-形式上的结果，是 1-形式，所以 $$\vec E$$ 是极向量——与镜面实验一致（电荷在镜中不换号，电场如实翻转）。而 $$\vec B$$ 由闭合电流产生，电流 $$\vec j$$ 是极向量，$$\vec B$$ 与 $$\vec j$$ 通过左手/右手规则的"叉乘型"关系联系，于是 $$\vec B$$ 是轴向量，对应 2-形式：

$$\boxed{\;\vec E=E_x\,dx+E_y\,dy+E_z\,dz\in\Omega^1,\qquad \vec B=B_x\,dy\wedge dz+B_y\,dz\wedge dx+B_z\,dx\wedge dy\in\Omega^2.\;}$$

**注**。$$\mathbb R^3$$ 中 1-形式与 2-形式维数相同（都是 $$3$$），所以初等教材里把 $$\vec B$$ 当成向量场从不区分——这正是 MP26 说"磁场表现非常像一般向量场"的原因。但在 $$\mathbb R^4$$ 或一般流形上，这个巧合消失，$$\vec B$$ 的 2-形式身份就再也藏不住了（见 3.7 与 3.9）。

### 3.2 Hodge 星算子：定义

3.1 节把"轴向量"翻译成 2-形式，但还欠一个交代：2-形式与向量之间那座桥是什么？它叫 Hodge 星算子。

**设定**。设 $$(M,g)$$ 是 $$n$$ 维**可定向**的伪黎曼流形，定向已取定。在正向正交标架余标架 $$(\theta^1,\dots,\theta^n)$$ 中，体积形式为

$$\mathrm{vol}=\theta^1\wedge\theta^2\wedge\cdots\wedge\theta^n .$$

度量 $$g$$ 在余切空间上诱导内积，并延拓到 $$\Lambda^k T_p^*M$$：若 $$\alpha=\alpha_{i_1\cdots i_k}dx^{i_1}\wedge\cdots\wedge dx^{i_k}$$、$$\beta=\beta_{j_1\cdots j_k}dx^{j_1}\wedge\cdots\wedge dx^{j_k}$$，定义

$$\langle\alpha,\beta\rangle_g:=\frac1{k!}\,g^{i_1j_1}\cdots g^{i_kj_k}\,\alpha_{i_1\cdots i_k}\beta_{j_1\cdots j_k}.$$

在正交余标架下，$$\langle\theta^{i_1}\wedge\cdots\wedge\theta^{i_k},\ \theta^{i_1}\wedge\cdots\wedge\theta^{i_k}\rangle_g=g^{i_1i_1}\cdots g^{i_ki_k}$$，不同多重指标的基元素互相正交。

**定义 3.5（Hodge 星算子 / Hodge star operator）**。$$\star:\Omega^k(M)\to\Omega^{n-k}(M)$$ 是唯一满足下式的线性映射：

$$\alpha\wedge\star\beta=\langle\alpha,\beta\rangle_g\,\mathrm{vol},\qquad \forall\,\alpha,\beta\in\Omega^k(M). \tag{24.2}$$

**为什么存在且唯一**。固定 $$\alpha$$，右端 $$\beta\mapsto\langle\alpha,\beta\rangle_g$$ 是 $$\Omega^k$$ 上的线性泛函；而 $$\beta\mapsto\alpha\wedge\beta$$ 给出 $$\Omega^k\to\Omega^n$$ 的线性映射。楔积的配对

$$\Omega^k\times\Omega^{n-k}\longrightarrow\Omega^n,\qquad (\gamma,\delta)\longmapsto\gamma\wedge\delta$$

是**非退化**的（在每点，$$\Lambda^k$$ 与 $$\Lambda^{n-k}$$ 的维数相同，且楔积到一维空间 $$\Lambda^n$$ 的配对是完美配对；正交余标架的基 $$\theta^I$$ 与互补的 $$\theta^J$$ 配对给出 $$\pm\mathrm{vol}\ne0$$）。因此存在唯一的 $$\star\beta\in\Omega^{n-k}$$ 使 (24.2) 对一切 $$\alpha$$ 成立。$$\square$$

**引理 3.6（正交余标架下的显式公式）**。设 $$I=(i_1<\cdots<i_k)$$，$$J$$ 是其互补指标按递增排列，$$\varepsilon(I,J)$$ 是把 $$(i_1,\dots,i_k,j_1,\dots,j_{n-k})$$ 排成递增序的置换符号。则

$$\star\,\theta^{i_1}\wedge\cdots\wedge\theta^{i_k}=\varepsilon(I,J)\cdot\langle\theta^{I},\theta^{I}\rangle_g\;\theta^{j_1}\wedge\cdots\wedge\theta^{j_{n-k}}. \tag{24.3}$$

**证明**。记 $$\theta^I=\theta^{i_1}\wedge\cdots\wedge\theta^{i_k}$$。由 $$\theta^I\wedge\theta^J=\varepsilon(I,J)\,\mathrm{vol}$$。设 $$\star\theta^I=c\,\theta^J$$，代入 (24.2)。对 $$\alpha=\theta^I$$：

$$\theta^I\wedge\star\theta^I=c\,\theta^I\wedge\theta^J=c\,\varepsilon(I,J)\,\mathrm{vol}=\langle\theta^I,\theta^I\rangle_g\,\mathrm{vol}.$$

故 $$c=\langle\theta^I,\theta^I\rangle_g/\varepsilon(I,J)=\varepsilon(I,J)\langle\theta^I,\theta^I\rangle_g$$（用了 $$\varepsilon^{-1}=\varepsilon$$）。对 $$\alpha$$ 取别的基元素时两边同为零，唯一性由定义已保证。$$\square$$

（约定：本书用 $$\langle\theta^I,\theta^I\rangle_g^{-1}=\langle\theta^I,\theta^I\rangle_g$$，因为正交标架下该量取值 $$\pm1$$。）

**定理 3.7（$$\star$$ 的平方）**。对 $$\omega\in\Omega^k(M)$$，

$$\star\star\omega=(-1)^{k(n-k)}\operatorname{sgn}(g)\,\omega,\qquad \operatorname{sgn}(g):=\frac{\det(g_{ij})}{\lvert\det(g_{ij})\rvert}\in\{\pm1\}. \tag{24.4}$$

**证明思路**。对正交余标架基元素用 (24.3) 两次。第一次：$$\star\theta^I=\varepsilon\langle\theta^I,\theta^I\rangle\theta^J$$。第二次，$$\theta^J$$ 的互补指标正是 $$I$$，且把 $$(j_1,\dots,j_{n-k},i_1,\dots,i_k)$$ 排成递增序的置换，与第一次的置换相差一个 $$k(n-k)$$ 个对换（每个 $$i$$ 要越过 $$n-k$$ 个 $$j$$），故符号相乘为 $$(-1)^{k(n-k)}$$；而 $$\langle\theta^J,\theta^J\rangle\langle\theta^I,\theta^I\rangle=\det(g)$$ 的符号即 $$\operatorname{sgn}(g)$$。两次相乘得 (24.4)。$$\square$$

**两个要用的特例**：

- $$\mathbb R^3$$（欧氏，正定）：$$\operatorname{sgn}(g)=+1$$，且 $$k(3-k)\in\{0,2,2,0\}$$ 恒为偶，所以

$$\boxed{\star\star\omega=+\omega\quad\text{在 }\Omega^k(\mathbb R^3)\text{ 上},\ k=0,1,2,3.} \tag{24.5}$$

- 四维 Minkowski 时空（号差取 $$(+,-,-,-)$$）：$$\operatorname{sgn}(g)=-1$$，在 $$k=2$$ 时 $$k(n-k)=4$$ 为偶，所以

$$\boxed{\star\star\omega=-\omega\quad\text{在 }\Omega^2(\mathbb R^{3,1})\text{ 上}.} \tag{24.6}$$

（12.6）是 MP37 反复用到的 $$\star^2=-1$$，它将在 3.9 节给出 $$\star$$ 的特征值 $$\pm i$$。

### 3.3 $$\mathbb R^3$$ 中的 $$\star$$：显式表

取 $$\mathbb R^3$$ 坐标 $$(x,y,z)$$、标准定向，$$(dx,dy,dz)$$ 是正向正交余标架，$$\mathrm{vol}=dx\wedge dy\wedge dz$$。用 (24.3) 逐一算（$$\langle\theta^I,\theta^I\rangle=1$$）：

$$\begin{aligned} &\star 1=dx\wedge dy\wedge dz, && \star(dx\wedge dy\wedge dz)=1,\\ &\star dx=dy\wedge dz, && \star(dy\wedge dz)=dx,\\ &\star dy=dz\wedge dx, && \star(dz\wedge dx)=dy,\\ &\star dz=dx\wedge dy, && \star(dx\wedge dy)=dz. \end{aligned} \tag{24.7}$$

例如 $$\star dy$$：指标 $$I=(2)$$，互补 $$(1,3)$$，置换 $$(2,1,3)$$ 是偶置换的相反数（一个对换），$$\varepsilon=-1$$，故 $$\star dy=\varepsilon\,dx\wedge dz=-dx\wedge dz=dz\wedge dx$$，与表中一致。

**Hodge 星算子在 $$\mathbb R^3$$ 中就是"取互补指标"这件事**：

$$\Omega^0\ \xrightarrow{\ \star\ }\ \Omega^3,\qquad \Omega^1\ \xrightarrow{\ \star\ }\ \Omega^2,\qquad \Omega^2\ \xrightarrow{\ \star\ }\ \Omega^1,\qquad \Omega^3\ \xrightarrow{\ \star\ }\ \Omega^0 .$$

它把 $$3$$ 维的 1-形式与 2-形式对调，而这两个空间的维数都是 $$\binom31=\binom32=3$$——**"取一个坐标"与"取两个互补坐标"数目相同**，这就是 $$\vec B$$ 能伪装成向量的全部秘密。

### 3.4 高潮之一：grad / curl / div 是同一个 $$d$$

现在把第 14 章的外微分 $$d$$ 与经典向量分析对齐。回忆第 14 章 3.9 节：$$d$$ 作用在 0-形式上是梯度、作用在 1-形式上是旋度、作用在 2-形式上是散度。用 $$\star$$ 可以把结果"搬回"熟悉的向量/标量，得到 MP26 的公式。

**定理 3.8（三个算子，一个 $$d$$）**。设 $$f\in\Omega^0(\mathbb R^3)$$、$$\vec F$$ 是光滑向量场，记 $$\omega_F=F_xdx+F_ydy+F_zdz\in\Omega^1$$。则

1. **梯度**：$$\nabla f\ \longleftrightarrow\ df$$（作为 1-形式）。即 $$df=\partial_xf\,dx+\partial_yf\,dy+\partial_zf\,dz$$。
2. **旋度**：$$\nabla\times\vec F\ \longleftrightarrow\ \star\,d\,\omega_F\in\Omega^1$$。
3. **散度**：$$\nabla\cdot\vec F=\star\,d\star\omega_F\in\Omega^0$$。

**证明**。第一条就是 $$d$$ 在 0-形式上的定义（第 14 章定理 3.17.1）。

**第二条**。先算 $$d\omega_F$$：

$$d\omega_F=\sum_{i}\sum_{j}\partial_jF_i\,dx^j\wedge dx^i=\sum_{i<j}\bigl(\partial_iF_j-\partial_jF_i\bigr)dx^i\wedge dx^j .$$

把三项写开（对照 (24.7)）：

$$d\omega_F=(\partial_xF_y-\partial_yF_x)\,dx\wedge dy+(\partial_yF_z-\partial_zF_y)\,dy\wedge dz+(\partial_zF_x-\partial_xF_z)\,dz\wedge dx .$$

用 (24.7) 作用 $$\star$$：$$\star(dx\wedge dy)=dz$$、$$\star(dy\wedge dz)=dx$$、$$\star(dz\wedge dx)=dy$$，于是

$$\star d\omega_F=(\partial_yF_z-\partial_zF_y)\,dx+(\partial_zF_x-\partial_xF_z)\,dy+(\partial_xF_y-\partial_yF_x)\,dz=\nabla\times\vec F .$$

（把 $$dy\wedge dz\mapsto dx$$：由置换 $$(2,3,1)$$ 偶，符号为 $$+1$$；$$dz\wedge dx\mapsto dy$$：$$(3,1,2)$$ 偶，$$+1$$；$$dx\wedge dy\mapsto dz$$：$$(1,2,3)$$ 偶，$$+1$$。）

**第三条**。先算 $$\star\omega_F=F_x\,dy\wedge dz+F_y\,dz\wedge dx+F_z\,dx\wedge dy$$。取外微分，只有系数微分非零：

$$d\star\omega_F=(\partial_xF_x+\partial_yF_y+\partial_zF_z)\,dx\wedge dy\wedge dz .$$

再用 (24.7) 的 $$\star(dx\wedge dy\wedge dz)=1$$，得 $$\star d\star\omega_F=\nabla\cdot\vec F$$。$$\square$$

**注（为什么必须夹一个 $$\star$$）**：不加 $$\star$$ 时，$$d$$ 是"升次"的：$$0\to1\to2\to3$$。经典向量分析里的 curl 与 div 却都把向量场（或 1-形式）映回向量场（或标量），也就是"次数不变"或"回到 0 次"。$$\star$$ 的任务就是把升次后的结果用互补指标"搬回去"。3.2 节那句 $$\binom31=\binom32$$ 在这里第二次付利息。

### 3.5 高潮之二：$$d^2=0$$ 的物理名字

**推论 3.9（向量分析的恒等式）**。

$$\operatorname{curl}(\operatorname{grad}f)=\vec 0,\qquad \operatorname{div}(\operatorname{curl}\vec F)=0,\qquad \forall f,\ \vec F\in\mathcal C^\infty(\mathbb R^3).$$

**证明**。第一条：由定理 3.8.1，$$\operatorname{grad}f\leftrightarrow df$$；由定理 3.8.2，$$\operatorname{curl}(\operatorname{grad}f)\leftrightarrow\star d(df)=\star\,d^2f=0$$（第 14 章定理 3.18），故向量为零。

第二条：由定理 3.8.2，$$\operatorname{curl}\vec F\leftrightarrow\star d\omega_F$$；再由定理 3.8.3 作用在它上面，

$$\operatorname{div}(\operatorname{curl}\vec F)=\star\,d\star(\star d\omega_F)=\star\,d\bigl(\star\star d\omega_F\bigr)\overset{(24.5)}{=}\star\,d^2\omega_F=0.\qquad\square$$

（(24.5) 给出 $$\star\star d\omega_F=d\omega_F$$，因为 $$d\omega_F\in\Omega^2$$、$$\star\star=+1$$。在 $$\mathbb R^3$$ 上这一步不需要额外符号；在一般维度上要换成 $$(-1)^{k(n-k)}$$。）

这两条恒等式在向量分析课上通常靠"逐项算一遍"证明，算完也没人告诉你**为什么必须如此**。现在的答案是：它们与第 14 章的 $$d^2=0$$、第 09–10 章链复形的 $$\partial^2=0$$（"边界的边界为空"）是**同一句话**，分别写在形式世界和链世界。第 26 章的 Stokes 定理会把两个世界焊在一起。

### 3.6 时变情形：$$F=B+E\wedge dt$$ 与 $$dF=0$$

回到入口题 (b)。静态时两个"零方程"就是 $$dE=0$$（即 $$\nabla\times\vec E=0$$）与 $$dB=0$$（即 $$\nabla\cdot\vec B=0$$）。时变时差一个 $$\partial_t\vec B$$ 项。MP26 的补救办法是**把时间也当成一个坐标**，在 $$\mathbb R^{3,1}$$（坐标 $$(t,x,y,z)$$）上把 $$\vec E,\vec B$$ 合成一个 2-形式：

**定义 3.10（电磁场 2-形式 / field strength）**。

$$F:=B+E\wedge dt\ \in\Omega^2(\mathbb R^{3,1}), \tag{24.8}$$

其中 $$B=B_x\,dy\wedge dz+B_y\,dz\wedge dx+B_z\,dx\wedge dy$$、$$E\wedge dt=E_x\,dx\wedge dt+E_y\,dy\wedge dt+E_z\,dz\wedge dt$$。

把 $$F=\tfrac12F_{\mu\nu}dx^\mu\wedge dx^\nu$$（$$x^0=t$$，$$x^1=x$$，$$x^2=y$$，$$x^3=z$$）展开成分量矩阵：

$$F_{\mu\nu}=\begin{pmatrix} 0 & -E_x & -E_y & -E_z\\ E_x & 0 & B_z & -B_y\\ E_y & -B_z & 0 & B_x\\ E_z & B_y & -B_x & 0 \end{pmatrix}. \tag{24.9}$$

**验算**：由 $$\tfrac12F_{\mu\nu}dx^\mu\wedge dx^\nu=\sum_{\mu<\nu}F_{\mu\nu}dx^\mu\wedge dx^\nu$$，逐对读：$$F_{01}dx^0\wedge dx^1=-E_x\,dt\wedge dx=E_x\,dx\wedge dt$$；$$F_{12}dx\wedge dy=B_z\,dx\wedge dy$$；$$F_{13}dx\wedge dz=-B_y\,dx\wedge dz=B_y\,dz\wedge dx$$；其余同理。相加正是 (24.8)。$$\square$$

**定理 3.11（齐次方程 = $$dF=0$$）**。$$dF=0$$ 等价于

$$\nabla\cdot\vec B=0\qquad\text{与}\qquad \nabla\times\vec E+\dfrac{\partial\vec B}{\partial t}=0 .$$

**证明思路**。$$F$$ 是空间 2-形式 $$B$$ 与"空间 1-形式 $$\wedge\,dt$$"两项之和。分别求 $$d$$：空间部分用空间外微分 $$d_S$$，时间部分必然多出一个 $$dt$$ 因子。$$dF=0$$ 是 3-形式方程，而 $$\Omega^3(\mathbb R^{3,1})$$ 按"含不含 $$dt$$"分裂成 $$\Omega^3_S\oplus(\Omega^2_S\wedge dt)$$，所以可以逐块令零。

**证明**。记 $$d_S=\partial_xdx+\partial_ydy+\partial_zdz$$ 为空间外微分（它把空间 $$k$$-形式变空间 $$(k+1)$$-形式）。由 $$d$$ 的线性与反导子法则（第 14 章定理 3.17.3），

$$dF=dB+d(E\wedge dt).$$

先算 $$dB$$（$$B$$ 不含 $$dt$$）：$$dB=d_SB+dt\wedge\partial_tB$$。由 $$\deg B=2$$、$$\deg dt=1$$，反交换律 $$dt\wedge\partial_tB=(-1)^{1\cdot2}\partial_tB\wedge dt=\partial_tB\wedge dt$$。

再算 $$d(E\wedge dt)=dE\wedge dt+(-1)^1E\wedge d(dt)=dE\wedge dt$$（$$d^2t=0$$）。而 $$dE=d_SE+dt\wedge\partial_tE$$，故

$$d(E\wedge dt)=(d_SE+dt\wedge\partial_tE)\wedge dt=d_SE\wedge dt+\underbrace{dt\wedge\partial_tE\wedge dt}_{=0}.$$

相加：

$$dF=d_SB+\bigl(\partial_tB+d_SE\bigr)\wedge dt . \tag{24.10}$$

右端两项分别是空间 3-形式与（空间 2-形式 $$\wedge\,dt$$）。它们张成 $$\Omega^3$$ 的两个互补子空间（由微分因子的不同区分），故 $$dF=0$$ 等价于两块分别为零：

$$d_SB=0, \tag{24.11}$$

$$\partial_tB+d_SE=0. \tag{24.12}$$

**第一块**：由定理 3.8.3，$$\star d_SB=\nabla\cdot\vec B$$，故 (24.11) 即 $$\nabla\cdot\vec B=0$$。

**第二块**：对 (24.12) 两边作用空间 $$\star$$。左边第二项 $$\star d_SE=\nabla\times\vec E$$（定理 3.8.2）；第一项 $$\star\partial_tB=\partial_t(\star B)$$，而 $$\star B=B_xdx+B_ydy+B_zdz$$ 即 $$\vec B$$ 对应的 1-形式。所以 (24.12) 即

$$\partial_t\vec B+\nabla\times\vec E=0\ \Longleftrightarrow\ \nabla\times\vec E=-\dfrac{\partial\vec B}{\partial t}.\qquad\square$$

**这条定理是本章的题眼**。在 (24.10) 里，$$d^2=0$$ 提供了一件事：对任意 $$A$$，$$F=dA$$ 自动满足 $$dF=0$$（因为 $$d^2A=0$$，第 14 章定理 3.18）。而 (24.11) 说 $$d_SB=0$$，它**不含时间**，是纯粹的空间陈述。于是：

$$\boxed{\ \text{"边界的边界为空" }(\partial\partial=\varnothing,\ d^2=0)\ \Longleftrightarrow\ \text{"不存在磁单极子" }(\nabla\cdot\vec B=0).\ }$$

理由如下。若存在磁单极子（磁荷密度 $$\rho_m$$），则磁场满足 $$\nabla\cdot\vec B=4\pi\rho_m$$，此时 $$B$$ 不再是闭形式：$$d_SB=4\pi\rho_m\,dx\wedge dy\wedge dz\ne0$$。所以"没有任何单极子"精确地就是"$$B$$ 总可以写成某个 1-形式的 $$d$$"，即 $$B=dA$$。而 $$d^2=0$$ 保证 $$d(dA)=0$$ 自动成立——**单极子的不存在，是外代数的一条恒等式**（第 14 章已在 $$d^2=0$$ 的证明里见过它的代数根）。

### 3.7 另外两个方程：$$d\star F=J$$

后两个方程含 $$\rho$$ 与 $$\vec j$$，右边不为零，所以不能是 $$d(\text{某物})=0$$。补救：**夹一个 $$\star$$**，把"散度"变成"升次后的导数"，右边再配一个对偶次数的形式。

**定义 3.12（电流 1-形式 / current one-form）**。在 $$\mathbb R^{3,1}$$ 上取

$$J:=\rho\,dt+j_x\,dx+j_y\,dy+j_z\,dz\ \in\Omega^1,\qquad j=j_xdx+j_ydy+j_zdz\ \text{为空间 1-形式}. \tag{24.13}$$

**定理 3.13（非齐次方程 = $$d\star F=J$$，即 $$\star d\star F=J$$ 的等价写法）**。用号差 $$(+,-,-,-)$$、体积形式 $$\mathrm{vol}=dt\wedge dx\wedge dy\wedge dz$$，则

$$\star\,d\star F=J$$

等价于

$$\nabla\cdot\vec E=\rho\qquad\text{与}\qquad \nabla\times\vec B-\dfrac{\partial\vec E}{\partial t}=\vec j .$$

**证明思路**。先在四维里把 $$\star F$$ 用 $$\vec E,\vec B$$ 写出来（用 3.2 的定义与 (24.3)），再求 $$d$$，最后再作用一次 $$\star$$ 并整理成空间 $$d_S,\star_S$$ 的组合。

**证明**。四维正交余标架取 $$(\theta^0,\theta^1,\theta^2,\theta^3)=(dt,dx,dy,dz)$$。由 (24.3)，对 2-形式（$$k=2$$，$$\langle dt\wedge dx,dt\wedge dx\rangle_g=g^{00}g^{11}=(+1)(-1)=-1$$，纯空间 $$\langle dy\wedge dz,dy\wedge dz\rangle=(+1)$$）：

$$\star(dt\wedge dx)=-dy\wedge dz,\quad \star(dt\wedge dy)=-dz\wedge dx,\quad \star(dt\wedge dz)=-dx\wedge dy,$$

$$\star(dy\wedge dz)=dt\wedge dx,\quad \star(dz\wedge dx)=dt\wedge dy,\quad \star(dx\wedge dy)=dt\wedge dz. \tag{24.14}$$

把 (24.14) 作用在 $$F=B+E\wedge dt$$（其中 $$dx\wedge dt=-dt\wedge dx$$，等）：

$$\star F=-(E_x\,dy\wedge dz+E_y\,dz\wedge dx+E_z\,dx\wedge dy)+\bigl(B_x\,dt\wedge dx+B_y\,dt\wedge dy+B_z\,dt\wedge dz\bigr)$$

$$=-\tilde E+\tilde B\wedge dt, \tag{24.15}$$

这里 $$\tilde E=E_x\,dy\wedge dz+E_y\,dz\wedge dx+E_z\,dx\wedge dy$$ 是 $$\vec E$$ 对应的空间 2-形式，$$\tilde B=B_x\,dx+B_y\,dy+B_z\,dz$$ 是 $$\vec B$$ 对应的空间 1-形式。检验 (24.6) 的一个实例：$$\star(dt\wedge dx)=-dy\wedge dz$$，再作用一次 $$\star(-dy\wedge dz)=-dt\wedge dx$$，故 $$\star^2=-1$$，与 (24.6) 相符。

求 $$d(\star F)$$（$$\tilde E$$ 与 $$\tilde B$$ 均不含 $$dt$$）：

$$d(\star F)=-d_S\tilde E-dt\wedge\partial_t\tilde E+d\tilde B\wedge dt=-d_S\tilde E+\partial_t\tilde E\wedge dt+d_S\tilde B\wedge dt,$$

其中用了 $$-dt\wedge\partial_t\tilde E=\partial_t\tilde E\wedge dt$$（$$\deg\partial_t\tilde E=2$$）与 $$d\tilde B\wedge dt=(d_S\tilde B+dt\wedge\partial_t\tilde B)\wedge dt=d_S\tilde B\wedge dt$$。合并：

$$d(\star F)=-d_S\tilde E+\bigl(\partial_t\tilde E+d_S\tilde B\bigr)\wedge dt. \tag{24.16}$$

再作用 $$\star$$。两块：

- $$-d_S\tilde E$$ 是空间 3-形式，$$d_S\tilde E=(\nabla\cdot\vec E)\,dx\wedge dy\wedge dz$$，而 $$\star(dx\wedge dy\wedge dz)=\langle dxdydz,dxdydz\rangle\star_w(dxdydz)=(-1)(-dt)=dt$$（其中 $$\star_w$$ 取互补指标并算置换符号：$$(1,2,3,0)$$ 是 3 个对换，符号 $$-1$$）。故 $$\star(-d_S\tilde E)=(\nabla\cdot\vec E)\,dt$$。
- $$\bigl(\partial_t\tilde E+d_S\tilde B\bigr)\wedge dt$$：对空间 2-形式 $$\alpha$$ 有 $$\star(\alpha\wedge dt)=\star_S\alpha$$（$$\star_S$$ 为 3.3 节的空间 $$\star$$，逐项可验证，如 $$\star(dx\wedge dy\wedge dt)=dz=\star_S(dx\wedge dy)$$）。故 $$\star\bigl((\partial_t\tilde E+d_S\tilde B)\wedge dt\bigr)=\partial_t\star_S\tilde E+\star_Sd_S\tilde B=\partial_t\vec E+\nabla\times\vec B$$（把 1-形式与向量认同）。

合起来：

$$\star\,d\star F=(\nabla\cdot\vec E)\,dt+\bigl(\partial_t\vec E+\nabla\times\vec B\bigr). \tag{24.17}$$

设定 (24.17) $$=J=\rho\,dt+j$$，按 $$dt$$ 分量与空间 1-形式分量分别相等：

$$\nabla\cdot\vec E=\rho,\qquad \partial_t\vec E+\nabla\times\vec B=\vec j\ \Longleftrightarrow\ \nabla\times\vec B-\partial_t\vec E=\vec j.\qquad\square$$

**注（符号约定）**。不同教材对 $$F=B+E\wedge dt$$ 还是 $$F=B-E\wedge dt$$、号差取 $$(+,-,-,-)$$ 还是 $$(-,+,+,+)$$ 各有选择，$$\star F$$ 于是相差整体符号。本章固定 (24.8)、(24.13) 与 $$\mathrm{vol}=dt\wedge dx\wedge dy\wedge dz$$，全程自洽：定理 3.11 与 3.13 同时给出正确的四个方程。

**至此四个方程压成两个**：

$$\boxed{\ dF=0\ \Longleftrightarrow\ \begin{cases}\nabla\cdot\vec B=0\\ \nabla\times\vec E=-\partial_t\vec B\end{cases},\qquad \star\,d\star F=J\ \Longleftrightarrow\ \begin{cases}\nabla\cdot\vec E=\rho\\ \nabla\times\vec B-\partial_t\vec E=\vec j\end{cases}.\ } \tag{24.18}$$

### 3.8 电磁势与规范变换

$$dF=0$$ 还有一层结构：它让 $$F$$ 成为**闭形式 (closed form)**。在 $$\mathbb R^{3,1}$$（可缩，见第 14 章与第 28 章的 Poincaré 引理）上，闭 $$\Longrightarrow$$ 恰当，于是存在 1-形式 $$A$$ 使

$$F=dA. \tag{24.19}$$

写开 $$A=A_x\,dx+A_y\,dy+A_z\,dz-\phi\,dt$$（$$\phi$$ 为标量势 (scalar potential)，$$\vec A=(A_x,A_y,A_z)$$ 为向量势 (vector potential)）。则 $$dA=d_SA_1+(\partial_tA_1-d_S\phi)\wedge dt$$（$$A_1=A_xdx+A_ydy+A_zdz$$），与 $$F=B+E\wedge dt$$ 逐块对照给出

$$B=d_SA_1\ \Longleftrightarrow\ \vec B=\nabla\times\vec A,\qquad E=\partial_tA_1-d_S\phi\ \Longleftrightarrow\ \vec E=\partial_t\vec A-\nabla\phi .$$

（静态时 $$\partial_t\vec A=0$$，退化为物理课本的 $$\vec E=-\nabla\phi$$；$$\phi$$ 的整体符号只是约定，本章取 MP37 "数学上不用负号"的写法。）

**规范自由度 (gauge freedom)**。若把 $$A$$ 换成 $$A'=A+df$$（$$f\in\Omega^0$$），则

$$dA'=dA+d^2f=dA+0=dA,$$

即 $$F$$ 不变。于是同一个电磁场 $$F$$ 对应**一整族**势 $$A$$，彼此相差一个恰当形式。$$\{A+df:\ f\in\Omega^0\}$$ 称为 $$A$$ 的**规范等价类 (gauge class)**，变换 $$A\mapsto A+df$$ 称为**规范变换 (gauge transformation)**。

**为什么这条自由度有用**。可以借它给 $$A$$ 加条件使方程变简单。常见的选择：

- **Lorentz 规范 (Lorentz gauge)**：$$d\star A=0$$；（等价于 $$\partial_t\phi-\nabla\cdot\vec A=0$$）。
- **Coulomb 规范 (Coulomb gauge)**：$$\nabla\cdot\vec A=0$$；
- 时间规范、Feynman 规范、Landau 规范等。

**命题 3.14（Lorentz 规范可达）**。设 $$A$$ 是任一势。若 $$A$$ 与 $$A+df$$ 视为等价，则可选 $$f$$ 使 $$\square\,f=-d\star A$$，从而 $$d\star(A+df)=0$$。

**证明**。$$\star(A+df)=\star A+\star df$$，故 $$d\star(A+df)=d\star A+d\star df$$。标量函数 $$f$$ 的余微分是 $$\square f:=\star d\star df$$（Laplace–de Rham 算子作用在 0-形式上，见第 28 章延伸）。于是条件 $$d\star(A+df)=0$$ 即

$$\star d\star df=-\star d\star A\ \Longleftrightarrow\ \square f=\star d\star A,$$

这是 $$\mathbb R^{3,1}$$ 上（波算子）的一个线性方程，对给定右端总有解。$$\square$$

（这里用到了余微分 $$\delta=\pm\star d\star$$ 的语言，第 28 章会正式引入；本章只需知道它是一个可解的线性算子。）

### 3.9 四维 Hodge 星算子与自对偶分解（接 MP37）

(24.6) 说：在 $$\mathbb R^{3,1}$$ 的 2-形式上 $$\star^2=-1$$。这带来一个漂亮的结论。把 $$\star$$ 线性延拓到**复化**的 2-形式上，则 $$\star$$ 的极小多项式是 $$t^2+1$$，**特征值为 $$\pm i$$**，对应的特征子空间是

$$\Omega^2_+=\{\omega:\ \star\omega=i\omega\}\ (\text{自对偶 / self-dual}),\qquad \Omega^2_-=\{\omega:\ \star\omega=-i\omega\}\ (\text{反自对偶 / anti-self-dual}).$$

任何复化 2-形式唯一分解为

$$\omega=\underbrace{\tfrac12(\omega+i\star\omega)}_{\in\Omega^2_+}+\underbrace{\tfrac12(\omega-i\star\omega)}_{\in\Omega^2_-}.$$

对实形式，$$F$$ 本身不是自对偶的（否则 $$\star F=iF$$ 会给出复系数），但 $$\star$$ 给出对偶关系

$$F=B+E\wedge dt\ \xrightarrow{\ \star\ }\ -\tilde E+\tilde B\wedge dt\qquad(\text{由 (24.15)}),$$

即 $$B\mapsto-\star_SE$$、$$E\mapsto\star_SB$$。**齐次方程组与非齐次方程组是同一个 $$F$$ 的对偶两面**：$$dF=0$$ 与 $$d\star F=0$$ 在真空 ($$J=0$$) 时形式完全对称，这种"电与磁的对称性"就是 MP26 说的"电和磁相似性的根源"。有源时 $$J\ne0$$ 打破对称——这正是"为什么自然界有电荷而无磁荷"这个悬案的数学形状。

## 四、几何与物理直觉 (Intuition)

**一、$$k$$-形式是"每点一个 $$k$$ 维有向测量仪"，$$\star$$ 是"取余"。** $$\star$$ 把"测量 $$k$$ 个方向"换成"测量剩下的 $$n-k$$ 个互补方向"。在 $$\mathbb R^3$$ 里，测一条边（1-形式）与测一张面（2-形式）是对偶的两种描述：一条有向边的补偿是一张有向面。所以"向量"与"面元"在三维里可以互相冒充——这就是 $$\vec B$$ 被误当成向量的全部原因。

**二、镜像判据是一条**代数**判据。** 命题 3.4 说：极向量 $$\leftrightarrow$$ 1-形式，轴向量 $$\leftrightarrow$$ 2-形式。这条对应不依赖任何物理，只看"这个量在镜面下多不多一个负号"。把初等物理里的"右手定则量"（力矩、角速度、磁感应、角动量）统一收进 2-形式，是微分形式给物理做的第一件实事。

**三、三个算子，一个 $$d$$。** $$\mathbb R^3$$ 上的 grad / curl / div 在向量分析课上是三个各有公式的算子；本章把它们还原成同一个 $$d$$ 加两种夹 $$\star$$ 的方式 (定理 3.8)。**当三个看似不同的算子服从同一套代数法则时，去找那个统一的源头**——这里的源头是 $$d$$，而 $$d^2=0$$ 就是 $$\operatorname{curl}\circ\operatorname{grad}=0$$ 与 $$\operatorname{div}\circ\operatorname{curl}=0$$。

**四、物理里最著名的"零"是拓扑。** $$\nabla\cdot\vec B=0$$ 在中学里靠"磁感线闭合"这种画法说明；本章给出的严格版本是 $$dF=0$$，即 $$F$$ 闭。**"磁单极子不存在"与"边界的边界为空"是同一条定理**，写在物理与代数两个语言里。第 09–10 章的 $$\partial^2=0$$、第 14 章的 $$d^2=0$$、本章的"无单极子"，三者是一件事的三张脸。

**五、势的存在性是上同调问题。** $$F=dA$$ 要求闭形式恰好；这在 $$\mathbb R^{3,1}$$ 上成立，因为空间可缩。若空间有"洞"（比如挖掉一条磁通量管），闭形式未必恰当，于是出现"不可积相位"与 Aharonov–Bohm 效应。第 13–14 章的 Stokes 定理与 de Rham 上同调正是处理它的工具。

## 五、经典问题精讲 (Classical Problems)

### 经典题 1：$$\mathbb R^3$$ 中 $$\star$$ 的完整计算与对偶往返

**考点**：定义 3.5、引理 3.6、定理 3.7。**位置**：3.2–3.3 节的验证。

**题**。设 $$\omega=2\,dx-y\,dz$$、$$\eta=x\,dy\wedge dz+z\,dx\wedge dy$$。

(a) 求 $$\star\omega$$、$$\star\eta$$、$$\star\star\omega$$、$$\star\star\eta$$；(b) 验证 $$\star\star=+1$$；(c) 求 $$\omega\wedge\star\omega$$ 与 $$\eta\wedge\star\eta$$，并与 $$\langle\omega,\omega\rangle\mathrm{vol}$$、$$\langle\eta,\eta\rangle\mathrm{vol}$$ 比较。

**解**。

(a) $$\omega=2\,dx-y\,dz$$ 是 1-形式。由 (24.7)：$$\star dx=dy\wedge dz$$、$$\star dz=dx\wedge dy$$，线性给出

$$\star\omega=2\,dy\wedge dz-y\,dx\wedge dy .$$

$$\eta=x\,dy\wedge dz+z\,dx\wedge dy$$ 是 2-形式。由 (24.7)：$$\star(dy\wedge dz)=dx$$、$$\star(dx\wedge dy)=dz$$，故 $$\star\eta=x\,dx+z\,dz$$。

再作用一次：$$\star\star\omega=2\,\star(dy\wedge dz)-y\,\star(dx\wedge dy)=2\,dx-y\,dz=\omega$$。同理 $$\star\star\eta=x\,dy\wedge dz+z\,dx\wedge dy=\eta$$。

(b) 由上，$$\star\star\omega=\omega$$、$$\star\star\eta=\eta$$。这与 (24.5) 一致：$$\omega\in\Omega^1$$，$$k(3-k)=1\cdot2=2$$，(24.4) 给出 $$(-1)^2(+1)=+1$$；$$\eta\in\Omega^2$$，$$k(3-k)=2$$，同为 $$+1$$。

(c) 用正交基的内积：$$\langle dx,dx\rangle=1,\langle dz,dz\rangle=1$$，$$\langle dx,dz\rangle=0$$，故 $$\langle\omega,\omega\rangle=2^2+(-y)^2=4+y^2$$。于是

$$\omega\wedge\star\omega=(2\,dx-y\,dz)\wedge(2\,dy\wedge dz-y\,dx\wedge dy)=4\,dx\wedge dy\wedge dz-y^2\,dz\wedge dx\wedge dy$$

$$=(4+y^2)\,dx\wedge dy\wedge dz=\langle\omega,\omega\rangle\,\mathrm{vol}.$$

（第二项 $$dz\wedge dx\wedge dy=dx\wedge dy\wedge dz$$。）这正好验证了定义 3.5 的 (24.2)。对 $$\eta$$：$$\langle\eta,\eta\rangle=x^2+z^2$$，而

$$\eta\wedge\star\eta=(x\,dy\wedge dz+z\,dx\wedge dy)\wedge(x\,dx+z\,dz)=x^2\,dx\wedge dy\wedge dz+z^2\,dx\wedge dy\wedge dz,$$

（其余项含重复微分，为零），也是 $$\langle\eta,\eta\rangle\mathrm{vol}$$。$$\square$$

### 经典题 2：curl grad = 0 与 div curl = 0 的一行证明

**考点**：$$d^2=0$$ 与定理 3.8。**位置**：3.5 节的应用。

**题**。用定理 3.8 与 $$d^2=0$$ 证明：对 $$\mathbb R^3$$ 上任意 $$\mathcal C^\infty$$ 函数 $$f$$ 与向量场 $$\vec F$$，

$$\operatorname{curl}(\operatorname{grad}f)=\vec0,\qquad \operatorname{div}(\operatorname{curl}\vec F)=0 .$$

**解**。见推论 3.9 的完整证明：第一式对应 $$d^2f=0$$（第 14 章定理 3.18）作用在 $$\Omega^0$$；第二式对应 $$d^2\omega_F=0$$ 作用在 $$\Omega^1$$，中间用 $$\star\star=+1$$（(24.5)）把两次 $$\star$$ 消去。关键 leap：**不要分别去算六个偏导，而要看出两式的左边都是"对一个升次结果再升一次次"**——一次 $$d$$ 把 0-形式抬到 1-形式（grad），第二次 $$d$$ 再抬到 2-形式（curl），复合是 $$d^2$$；散度那条则是 $$d\to\star\to d\to\star$$ 的把戏。$$\square$$

### 经典题 3：从 $$dF=0$$ 拆出两个齐次方程

**考点**：定理 3.11。**位置**：3.6 节的完整重做。

**题**。设 $$F=B+E\wedge dt$$，其中 $$B,E$$ 是 $$\mathbb R^3$$ 上的形式，$$E$$ 为 1-形式、$$B$$ 为 2-形式。完成定理 3.11 的推导，并**逐项**指出 (24.10) 中每一项的来源。

**解**。见定理 3.11 的证明。逐项对照 (24.10) 的 $$dF=d_SB+(\partial_tB+d_SE)\wedge dt$$：

- $$d_SB$$：$$B$$ 的空间系数求空间偏导，产生空间 3-形式（含 $$dx\wedge dy\wedge dz$$）。
- $$\partial_tB\wedge dt$$：$$B$$ 的系数求时间偏导，再楔 $$dt$$。来源是 $$dB$$ 里的 $$dt\wedge\partial_tB$$，由反交换化成 $$\partial_tB\wedge dt$$。
- $$d_SE\wedge dt$$：$$E$$ 的空间系数求空间偏导，楔 $$dt$$。来源是 $$d(E\wedge dt)=dE\wedge dt$$ 中 $$dt\wedge\partial_tE\wedge dt=0$$ 消去的那半。

$$dF=0$$ 按"含不含 $$dt$$"分成 (24.11)、(24.12)，再用定理 3.8 翻译成 $$\nabla\cdot\vec B=0$$、$$\nabla\times\vec E=-\partial_t\vec B$$。**关键 leap**：看出 $$\Omega^3(\mathbb R^{3,1})=\Omega^3_S\oplus(\Omega^2_S\wedge dt)$$ 这个**分次分解**，它把"一个 4 维方程"拆成"两个 3 维方程"。$$\square$$

### 经典题 4：$$d\star F=J$$ 的逆运算与守恒律

**考点**：定理 3.13 与电荷守恒。**位置**：3.7 节的延伸。

**题**。(a) 完成定理 3.13 的计算；(b) 证明由 Maxwell 方程自动推出**电荷守恒** $$\partial_t\rho+\nabla\cdot\vec j=0$$。

**解**。(a) 见定理 3.13 的完整证明（用 (24.14) 算 $$\star F$$，算 $$d\star F$$，再算 $$\star d\star F$$，与 $$J=\rho\,dt+j$$ 逐块对照）。

(b) 对 $$\star d\star F=J$$ 两边作用 $$d$$：左端 $$d\star d\star F=0$$？不对——要注意 $$d$$ 与 $$\star$$ 的位置。正确做法：由 (24.18)，$$\star d\star F=J$$ 等价于 $$\mathrm{div}\vec E=\rho$$ 与 $$\nabla\times\vec B-\partial_t\vec E=\vec j$$。对第二式取散度：

$$\nabla\cdot(\nabla\times\vec B)-\partial_t(\nabla\cdot\vec E)=\nabla\cdot\vec j .$$

第一项 $$\nabla\cdot(\nabla\times\vec B)=0$$（推论 3.9）。故 $$-\partial_t(\nabla\cdot\vec E)=\nabla\cdot\vec j$$，代入第一式 $$\nabla\cdot\vec E=\rho$$，得

$$-\partial_t\rho=\nabla\cdot\vec j\ \Longleftrightarrow\ \partial_t\rho+\nabla\cdot\vec j=0.$$

从形式语言看更干净：$$0=dJ=d\star d\star F$$ 给出 $$dJ=0$$，而 $$J=\rho\,dt+j$$，$$dJ=(\partial_t\rho+\nabla\cdot\vec j)\,dt\wedge dx\wedge dy\wedge dz$$，故 $$dJ=0$$ 即电荷守恒。**关键 leap**：把"守恒律"认出来是"$$J$$ 闭"，而 $$J$$ 闭又是 $$J=\star d\star F$$ 与 $$d^2=0$$ 的直接推论。$$\square$$

### 经典题 5：规范不变性与 Lorentz 规范

**考点**：$$F=dA$$、$$d^2=0$$、规范自由度。**位置**：3.8 节的应用。

**题**。(a) 证明 $$A\mapsto A+df$$ 使 $$F=dA$$ 不变；(b) 设 $$A=A_1-\phi\,dt$$，写出 $$B,E$$ 与 $$\phi,\vec A$$ 的关系并验证静态时 $$\vec E=-\nabla\phi$$；(c) 说明为什么可以用规范自由度取 $$\nabla\cdot\vec A=0$$（Coulomb 规范）。

**解**。(a) $$d(A+df)=dA+d^2f=dA$$（第 14 章定理 3.18）。故 $$F$$ 不变。

(b) 由定理 3.11 的证明同款计算：$$dA=d_SA_1+(\partial_tA_1-d_S\phi)\wedge dt$$。与 $$F=B+E\wedge dt$$ 比较得 $$B=d_SA_1$$，即 $$\vec B=\nabla\times\vec A$$；及 $$E=\partial_tA_1-d_S\phi$$，即 $$\vec E=\partial_t\vec A-\nabla\phi$$。静态时 $$\partial_t\vec A=0$$，$$\vec E=-\nabla\phi$$（本章取 MP37 的不带负号约定；换成物理惯用符号 $$\phi\to-\phi$$ 即得常见的 $$\vec E=-\nabla\phi$$）。

(c) 给定任一势 $$A$$，令 $$A'=A+df$$。要 $$0=\nabla\cdot\vec A'=\nabla\cdot\vec A+\nabla\cdot\nabla f=\nabla\cdot\vec A+\Delta f$$，只需解 Poisson 方程 $$\Delta f=-\nabla\cdot\vec A$$。$$\mathbb R^3$$ 上该方程总有解（第 28 章会给出显式解），故 Coulomb 规范可达。$$\square$$

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 写出 $$\mathbb R^3$$ 中 $$\star$$ 在四个空间 $$\Omega^0,\Omega^1,\Omega^2,\Omega^3$$ 的自然基上的作用全表，并逐个验证 $$\star\star=+1$$（对照 (24.5)）。

**基2.** 设 $$\omega=x\,dy+z\,dz$$。计算 $$d\omega$$、$$\star d\omega$$、$$\star d\star\omega$$，并说明这三个结果分别对应向量分析里的哪个算子、作用于哪个向量场。

**基3.** 对 $$f=xyz$$，先求 $$\operatorname{grad}f$$，再求 $$\operatorname{curl}(\operatorname{grad}f)$$，并指出它在 (24.4)–(24.5) 的 $$d^2=0$$ 里对应哪一步。

**基4.** 设 $$F=B+E\wedge dt$$。数出 $$2$$-形式 $$F$$ 在四维中的独立分量个数，与 $$\vec E,\vec B$$ 共 $$6$$ 个分量比较，并解释为什么二者相等（提示：$$\binom42=6$$）。

### 竞赛（本课目标难度）

**竞1.** 设 $$\vec a,\vec b$$ 是 $$\mathbb R^3$$ 上任意两个极向量场。用命题 3.3 与命题 3.4 证明：$$\vec a\times\vec b$$ 对应的 2-形式恰为 $$\alpha\wedge\beta$$（其中 $$\alpha,\beta$$ 是 $$\vec a,\vec b$$ 对应的 1-形式），并据此解释为什么"磁感线环绕电流"是 2-形式而非向量的必然行为。

**竞2.** 用 $$d$$ 与 $$\star$$ 证明：对 $$\mathbb R^3$$ 上任意向量场 $$\vec F$$，
(a) $$\operatorname{div}(\operatorname{curl}\vec F)=0$$；(b) $$\operatorname{curl}(\operatorname{grad}f)=\vec0$$；(c) 求 $$\operatorname{div}(\operatorname{grad}f)$$ 的形式表达式（即 $$\star d\star df$$），并说明它是 Laplacian。

**竞3.** 设 $$J=\rho\,dt+j$$、$$F=B+E\wedge dt$$。证明 $$d\star F=J$$ 蕴含 $$dJ=0$$，并把它翻译成电荷守恒 $$\partial_t\rho+\nabla\cdot\vec j=0$$。

**竞4.** 证明：若 $$A$$ 与 $$A'=A+df$$ 都满足 Lorentz 规范 $$d\star A=d\star A'=0$$，则 $$f$$ 满足波动方程 $$\square f:=\star d\star df=0$$。

**竞5.** 在 $$\mathbb R^{3,1}$$ 上，设 $$\omega$$ 是实 2-形式。证明 $$\omega+i\star\omega$$ 与 $$\omega-i\star\omega$$ 分别是 $$+i$$ 与 $$-i$$ 的特征形式（即 $$\star(\omega+i\star\omega)=i(\omega+i\star\omega)$$），并由此写出 $$\omega$$ 的自对偶/反自对偶分解。

### 研究（通向下一章）

**研1.** （悬念：Maxwell 方程的积分形式从哪来）把 $$dF=0$$ 的分量 $$\nabla\times\vec E=-\partial_t\vec B$$ 写成**积分形式**

$$\oint_{\partial S}\vec E\cdot d\vec l=-\frac{d}{dt}\iint_S\vec B\cdot d\vec S .$$

说明这个等式左边是某个 1-形式沿**边界** $$\partial S$$ 的积分、右边是它的 $$d$$ 在 $$S$$ 上的积分，于是它是一条"边界上的积分等于内部 $$d$$ 的积分"的定理的特例。指出这条定理是什么、它在第几章出现。

**研2.** （悬念：磁单极子与上同调）在 $$M=\mathbb R^3\setminus\{0\}$$ 上定义

$$\omega=\frac{1}{r^3}\bigl(x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy\bigr),\qquad r=\sqrt{x^2+y^2+z^2}.$$

(a) 证明 $$d\omega=0$$；(b) 直接计算 $$\iint_{S^2}\omega=4\pi$$（$$S^2$$ 为单位球面，取外向定向）；(c) 证明 $$\omega$$ **不**是恰当形式，从而说明"磁单极子的存在"对应 $$H^2(M)\ne0$$，而"$$dF=0\Rightarrow F=dA$$"来自 $$\mathbb R^{3,1}$$ 的可缩性；(d) 说明 (b)(c) 用到的关键定理是第 26 章的 Stokes 定理。

### 解答 (Solutions)

**解 基1.** 四个空间的自然基与 $$\star$$ 的作用（全部来自 (24.7)）：

$$\Omega^0:\ 1\ \xrightarrow{\star}\ dx\wedge dy\wedge dz;\qquad \Omega^3:\ dx\wedge dy\wedge dz\ \xrightarrow{\star}\ 1;$$

$$\Omega^1:\ dx\mapsto dy\wedge dz,\quad dy\mapsto dz\wedge dx,\quad dz\mapsto dx\wedge dy;$$

$$\Omega^2:\ dx\wedge dy\mapsto dz,\quad dy\wedge dz\mapsto dx,\quad dz\wedge dx\mapsto dy .$$

**逐个验证 $$\star\star=+1$$**：

- $$\Omega^0$$：$$\star\star 1=\star(dx\wedge dy\wedge dz)=1$$。
- $$\Omega^1$$：$$\star\star dx=\star(dy\wedge dz)=dx$$（对 $$dy,dz$$ 同理）。
- $$\Omega^2$$：$$\star\star(dx\wedge dy)=\star dz=dx\wedge dy$$（对另两个基同理）。注意此式用到了 $$\star dz=dx\wedge dy$$，而 $$\star dz$$ 由 (24.7) 给出，其符号来自置换 $$(3,1,2)$$ 为偶（$$\varepsilon=+1$$）。
- $$\Omega^3$$：$$\star\star(dx\wedge dy\wedge dz)=\star 1=dx\wedge dy\wedge dz$$。

与 (24.5) 一致：$$\mathbb R^3$$ 上恒 $$\star\star=+1$$。$$\square$$

**解 基2.** $$\omega=x\,dy+z\,dz$$ 是 1-形式，对应向量场 $$\vec F=(0,x,z)$$。

$$d\omega=dx\wedge dy+dz\wedge dz=dx\wedge dy$$（$$dz\wedge dz=0$$）。

$$\star d\omega=\star(dx\wedge dy)=dz .$$

$$\star d\star\omega$$：先算 $$\star\omega=x\,dz\wedge dx+z\,dx\wedge dy$$（$$\star dy=dz\wedge dx$$、$$\star dz=dx\wedge dy$$）。再 $$d\star\omega=dx\wedge dz\wedge dx+dz\wedge dx\wedge dy=0+dx\wedge dy\wedge dz$$，注意 $$dx\wedge dz\wedge dx$$ 含重复 $$dx$$ 故为零；$$dz\wedge dx\wedge dy=dx\wedge dy\wedge dz$$。于是 $$\star d\star\omega=1$$，即 $$\nabla\cdot\vec F=1$$。

对照定理 3.8：$$\star d\omega=\nabla\times\vec F$$，而 $$\nabla\times\vec F=\nabla\times(0,x,z)=(\partial_yz-\partial_zx,\ \partial_zz-\partial_x0,\ \partial_xx-\partial_y0)=(0,1,1)$$，其对应 1-形式是 $$dy+dz\ne dz$$。**这里发现不一致——回查：** $$\vec F=(0,x,z)$$ 的 curl 应为 $$(\partial_yF_z-\partial_zF_y,\ \partial_zF_x-\partial_xF_z,\ \partial_xF_y-\partial_yF_x)=(0-0,\ 0-0,\ \partial_xx-0)=(0,0,1)$$。所以 $$\nabla\times\vec F$$ 对应 1-形式 $$dz$$，与 $$\star d\omega=dz$$ 一致。

$$\nabla\cdot\vec F=\partial_x0+\partial_xx+\partial_zz=1$$，与 $$\star d\star\omega=1$$ 一致。$$\square$$

**解 基3.** $$f=xyz$$，$$\operatorname{grad}f=(yz,xz,xy)$$，对应 $$df=yz\,dx+xz\,dy+xy\,dz$$。求 curl：

$$\operatorname{curl}(\operatorname{grad}f)=\bigl(\partial_y(xy)-\partial_z(xz),\ \partial_z(yz)-\partial_x(xy),\ \partial_x(xz)-\partial_y(yz)\bigr)=(x-x,\ y-y,\ z-z)=\vec0 .$$

在 $$d^2=0$$ 里：$$\operatorname{curl}(\operatorname{grad}f)\leftrightarrow\star d(df)=\star d^2f=0$$，即第 14 章定理 3.18 在 $$\Omega^0$$ 上的情形（$$d^2$$ 作用在函数上为零）。$$\square$$

**解 基4.** 四维中 2-形式的独立分量数是 $$\binom42=6$$。$$\vec E,\vec B$$ 各有 3 个分量，共 $$6$$。二者相等是因为 $$\vec E$$ 的 3 个分量给出 $$F$$ 中含 $$dt$$ 的三个分量（$$E_i\leftrightarrow F_{0i}$$），$$\vec B$$ 的 3 个分量给出纯空间的三个分量（$$B_x\leftrightarrow F_{23}$$、$$B_y\leftrightarrow F_{31}$$、$$B_z\leftrightarrow F_{12}$$），正好铺满 6 个。**这也解释了为什么不变量只有两个**（$$\lvert\vec E\rvert^2-\lvert\vec B\rvert^2$$ 与 $$\vec E\cdot\vec B$$），它们是 6 维向量在 Lorentz 群下的两个不变量。$$\square$$

**解 竞1.** **关键 leap**：不要分别算叉乘的分量，而是把"两个极向量的有序对"直接认成"两个 1-形式的外积"。

设 $$\alpha=a_1dx+a_2dy+a_3dz$$、$$\beta=b_1dx+b_2dy+b_3dz$$。由第 14 章的楔积展开（见命题 3.4 的证明），

$$\alpha\wedge\beta=(a_1b_2-a_2b_1)dx\wedge dy+(a_2b_3-a_3b_2)dy\wedge dz+(a_3b_1-a_1b_3)dz\wedge dx .$$

右端三个系数正是 $$\vec a\times\vec b$$ 的三分量，故 $$\vec a\times\vec b\leftrightarrow\alpha\wedge\beta$$（作为 2-形式）。由命题 3.4，轴向量 $$\leftrightarrow$$ 2-形式，因此"叉乘出的轴向量"与"外积出的 2-形式"是同一对象。

物理含义：闭合电流产生磁场，磁场线的环绕方式由"电流 1-形式"与"位移 1-形式"的**外积**给出——它天然是一个"面量"（2-形式），描述的是"沿某个面元的环量"，而不是"沿某个方向的读数"。把 $$\vec B$$ 硬写成向量只是三维的维数巧合（$$\binom31=\binom32$$），一旦离开三维就必须回到 2-形式。$$\square$$

**解 竞2.** (a) 由定理 3.8.2，$$\operatorname{curl}\vec F\leftrightarrow\star d\omega_F$$；再对它用定理 3.8.3（散度公式作用在对应 1-形式上）：

$$\operatorname{div}(\operatorname{curl}\vec F)=\star\,d\star(\star d\omega_F)=\star\,d(\star\star d\omega_F)\overset{(24.5)}{=}\star\,d^2\omega_F=0 .$$

(b) 由定理 3.8.1，$$\operatorname{grad}f\leftrightarrow df$$；再对它用定理 3.8.2：$$\operatorname{curl}(\operatorname{grad}f)\leftrightarrow\star d(df)=\star d^2f=0$$。

(c) $$\operatorname{div}(\operatorname{grad}f)=\star\,d\star(df)=\star\,d\star df$$。展开：$$\star df=f_x\,dy\wedge dz+f_y\,dz\wedge dx+f_z\,dx\wedge dy$$，$$d\star df=(f_{xx}+f_{yy}+f_{zz})dx\wedge dy\wedge dz$$，再 $$\star$$ 得 $$f_{xx}+f_{yy}+f_{zz}=\Delta f$$。这就是 Laplacian，而 $$\star d\star d$$ 是它在形式语言里的写法（**Laplace–de Rham 算子** $$\square=\star d\star d$$ 作用在 0-形式上，第 28 章正式引入）。$$\square$$

**解 竞3.** 由 $$\star d\star F=J$$，两边作用 $$d$$：$$d\star d\star F=dJ$$。**关键**：左端 $$d\star d\star F$$ 中，把 $$\star d\star F$$ 记作 $$G\in\Omega^1$$；要证 $$dJ=0$$，直接用 (24.18) 的等价分量更省事。由定理 3.13，$$\star d\star F=J$$ 等价于两条分量方程。对第二式求散度并代入第一式：

$$\nabla\cdot(\nabla\times\vec B)-\partial_t(\nabla\cdot\vec E)=\nabla\cdot\vec j\ \Longrightarrow\ 0-\partial_t\rho=\nabla\cdot\vec j\ \Longrightarrow\ \partial_t\rho+\nabla\cdot\vec j=0 .$$

形式版本：$$J=\rho\,dt+j$$，故

$$dJ=\sum_i\partial_i\rho\,dx^i\wedge dt+dt\wedge\partial_tj+\dots=(\partial_t\rho+\nabla\cdot\vec j)\,dt\wedge dx\wedge dy\wedge dz,$$

（空间部分 $$dj$$ 无 $$dt$$、时间部分产生 $$dt\wedge dx^i$$，与 $$dx^i\wedge dt=-dt\wedge dx^i$$ 合并后系数为 $$\partial_t\rho+\partial_i j_i$$），故 $$dJ=0\Longleftrightarrow\partial_t\rho+\nabla\cdot\vec j=0$$。$$\square$$

**解 竞4.** $$d\star(A+df)=d\star A+d\star df$$。已知 $$d\star A=0$$，故需 $$d\star df=0$$。用它作用 $$\star$$：$$\star d\star df=0$$，即 $$\square f=0$$。所以两次都取 Lorentz 规范的势之差，是波动方程的解决；这也说明 Lorentz 规范没有完全钉死 $$A$$，还剩下"满足 $$\square f=0$$ 的 $$f$$"这一自由度。$$\square$$

**解 竞5.** 由 (24.6)，$$\star^2=-1$$ 在 $$\Omega^2(\mathbb R^{3,1})$$ 上（这是本章的约定，已在 (24.14) 后验证过一次）。设 $$\omega$$ 实。

$$\star(\omega+i\star\omega)=\star\omega+i\star^2\omega=\star\omega-i\omega=i(\omega+i\star\omega),$$

因为 $$i(\omega+i\star\omega)=i\omega-\star\omega$$，与 $$\star\omega-i\omega$$ 相等（用 $$i^2=-1$$ 移项）。同理

$$\star(\omega-i\star\omega)=\star\omega-i\star^2\omega=\star\omega+i\omega=-i(\omega-i\star\omega).$$

故分解为

$$\omega=\frac{\omega+i\star\omega}{2}+\frac{\omega-i\star\omega}{2},\qquad \text{第一部分}\in\Omega^2_+,\ \text{第二部分}\in\Omega^2_-.$$

（对实 $$\omega$$，两个部分互为共轭，$$\Omega^2_-=\overline{\Omega^2_+}$$；它们也都是复值形式。）$$\square$$

**解 研1.** 关键 leap：**"环量"与"通量"是同一个 $$d$$ 在边界与内部两处的读数。**

取 1-形式 $$\omega_E=E_xdx+E_ydy+E_zdz$$。由定理 3.11，$$d\omega_E=-(\partial_t\vec B)$$ 对应的 2-形式，即 $$d\omega_E=-\partial_t\tilde B$$（$$\tilde B=B_xdy\wedge dz+B_ydz\wedge dx+B_zdx\wedge dy$$）。对一个有定向的光滑曲面 $$S\subset\mathbb R^3$$（边界 $$\partial S$$ 取诱导定向）：

$$\oint_{\partial S}\omega_E=\iint_S d\omega_E=-\iint_S\partial_t\tilde B=-\frac{d}{dt}\iint_S\tilde B .$$

左边是 $$\omega_E$$ 沿 $$\partial S$$ 的积分，用度量把 1-形式与向量认同即 $$\oint_{\partial S}\vec E\cdot d\vec l$$；右边用 (24.7) 的 $$\star$$ 把 2-形式恢复到面元，即 $$-\frac{d}{dt}\iint_S\vec B\cdot d\vec S$$。这正是 Faraday 定律的积分形式。

所以它是一条"**沿边界的积分等于内部 $$d$$ 的积分**"的定理的特例。这条定理是**广义 Stokes 定理** $$\displaystyle\int_{\partial M}\omega=\int_M d\omega$$，将在**第 26 章**给出。本章只用了它的"分量版本"，它的统一形式与证明是下一章的任务。$$\square$$

**解 研2.** (a) 记 $$\alpha=x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy$$，$$\omega=\alpha/r^3$$。先算 $$d\alpha$$：$$dx\wedge dy\wedge dz$$ 的系数是 $$(\partial_xx+\partial_yy+\partial_zz)=3$$，故 $$d\alpha=3\,dx\wedge dy\wedge dz$$。而 $$d(1/r^3)=(-3/r^4)\,dr=(-3/r^4)(x\,dx+y\,dy+z\,dz)/r$$。于是

$$d\omega=d(1/r^3)\wedge\alpha+(1/r^3)d\alpha=\frac{-3}{r^5}(x\,dx+y\,dy+z\,dz)\wedge\alpha+\frac{3}{r^3}dx\wedge dy\wedge dz .$$

第一项中 $$(x\,dx+y\,dy+z\,dz)\wedge\alpha$$ 的 $$dx\wedge dy\wedge dz$$ 系数为 $$x\cdot x+y\cdot y+z\cdot z=r^2$$（其余项含重复微分），故第一项 $$=\frac{-3r^2}{r^5}dx\wedge dy\wedge dz=\frac{-3}{r^3}dx\wedge dy\wedge dz$$。与第二项相加，$$d\omega=0$$。

(b) 记 $$\alpha=x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy$$。用球坐标 $$(r,\theta,\varphi)$$。注意 $$\alpha$$ 正是用位置向量 $$\vec r=(x,y,z)$$ 去**内乘 (interior product)** 体积形式：$$\alpha=\iota_{\vec r}(dx\wedge dy\wedge dz)$$（内乘 $$\iota$$ 的定义：把一个向量塞进外积的第一个槽位，$$\iota_v(\beta\wedge\gamma)=\iota_v\beta\wedge\gamma+(-1)^{\deg\beta}\beta\wedge\iota_v\gamma$$）。而

$$dx\wedge dy\wedge dz=r^2\sin\theta\,dr\wedge d\theta\wedge d\varphi,$$

$$\iota_{\vec r}\bigl(r^2\sin\theta\,dr\wedge d\theta\wedge d\varphi\bigr)=\iota_{r\partial_r}\bigl(r^2\sin\theta\,dr\wedge d\theta\wedge d\varphi\bigr)=r^3\sin\theta\,d\theta\wedge d\varphi .$$

故 $$\alpha=r^3\sin\theta\,d\theta\wedge d\varphi$$，从而

$$\omega=\frac{\alpha}{r^3}=\sin\theta\,d\theta\wedge d\varphi\qquad(r>0),$$

在任意半径的球面上表达式都相同。于是

$$\iint_{S^2}\omega=\int_0^{2\pi}\!\!\int_0^{\pi}\sin\theta\,d\theta\,d\varphi=2\pi\cdot 2=4\pi .$$

（独立复核：由 $$d\alpha=3\,dx\wedge dy\wedge dz$$ 与散度定理于球体 $$B_R$$，$$\iint_{\partial B_R}\alpha=\iiint_{B_R}3\,dV=4\pi R^3$$，而 $$\alpha\rvert_{\partial B_R}=R^3\sin\theta\,d\theta\wedge d\varphi$$ 积出 $$4\pi R^3$$，两边相符；除以 $$r^3$$ 后与 $$R$$ 无关，正是 $$\omega$$ 的归一化所保证的。）

(c) 若 $$\omega=d\eta$$（$$\eta$$ 是 $$M$$ 上的 1-形式），则由 (b) 与**第 26 章的 Stokes 定理**，

$$\iint_{S^2}\omega=\iint_{S^2}d\eta=\oint_{\partial S^2}\eta=0,$$

因 $$S^2$$ 无边界 ($$\partial S^2=\varnothing$$，$$S^2$$ 本身是闭曲面)。这与 (b) 的 $$4\pi\ne0$$ 矛盾，故 $$\omega$$ 闭而不恰当：$$H^2(M)\ne0$$。物理含义：$$\omega$$ 正是"位于原点的磁单极子"产生的磁场 2-形式，它的存在等价于 $$\mathbb R^3\setminus\{0\}$$ 的二维上同调非零；而在可缩的 $$\mathbb R^{3,1}$$ 上 $$H^2=0$$，闭形式必恰当，于是 $$dF=0\Rightarrow F=dA$$——**"磁单极子不存在"被翻译成"$$H^2(\text{时空})=0$$"**。(b)(c) 的关键步骤都是"把边界上的积分与内部 $$d$$ 的积分互换"，其严格形式是**第 26 章的 Stokes 定理**——那正是下一章的起点：我们将在那里把 $$d$$、边界 $$\partial$$、积分三者焊成同一句话，本章所有"积分形式的 Maxwell 方程"都会在它下面统一。$$\square$$

## 七、Takeaway 与延伸 (Takeaways)

1. **$$\vec E$$ 是 1-形式，$$\vec B$$ 是 2-形式，这不是约定而是镜面实验的后果。** 极向量 $$\leftrightarrow$$ 1-形式、轴向量 $$\leftrightarrow$$ 2-形式（命题 3.4）。初等教材混淆二者，只因三维里 $$\binom31=\binom32=3$$。
2. **Hodge 星算子 $$\star$$ 是"取互补指标"**（定义 3.5、引理 3.6）。它满足 $$\star\star=(-1)^{k(n-k)}\operatorname{sgn}(g)$$：在 $$\mathbb R^3$$ 上恒为 $$+1$$，在四维 Minkowski 的 2-形式上为 $$-1$$。
3. **grad / curl / div 是同一个 $$d$$**：$$\nabla f\leftrightarrow df$$、$$\nabla\times\vec F\leftrightarrow\star d\omega_F$$、$$\nabla\cdot\vec F=\star d\star\omega_F$$（定理 3.8）。于是 $$\operatorname{curl}\circ\operatorname{grad}=0$$、$$\operatorname{div}\circ\operatorname{curl}=0$$ 就是 $$d^2=0$$（推论 3.9）。
4. **Maxwell 四个方程压成两个**：$$dF=0\iff\{\nabla\cdot\vec B=0,\ \nabla\times\vec E=-\partial_t\vec B\}$$，$$\star d\star F=J\iff\{\nabla\cdot\vec E=\rho,\ \nabla\times\vec B-\partial_t\vec E=\vec j\}$$（(24.18)）。**"边界的边界为空"在物理里就叫"不存在磁单极子"**。
5. **$$F=dA$$ 与规范变换**：$$A\mapsto A+df$$ 由 $$d^2=0$$ 保持 $$F$$ 不变；四维中 $$\star^2=-1$$ 给出特征值 $$\pm i$$，$$F$$ 分解为自对偶与反自对偶两部分（MP37）。

**下一章的悬念**。本章反复出现"边界上的积分"与"内部 $$d$$ 的积分"这对话（研1、研2），也反复出现 $$\oint_{\partial S}$$、$$\iint_{S^2}$$ 这类符号，但**始终没有证明它们可以互换**。那一条 $$\displaystyle\int_{\partial M}\omega=\int_M d\omega$$ 就是**第 26 章的 Stokes 定理**——它把 $$d$$（微分）、$$\partial$$（边界）、$$\int$$（积分）三者焊成一句话，是本章所有"积分形式 Maxwell 方程"的统一出生地，也是第 28 章 de Rham 上同调的门票。

**延伸阅读**。

- 文集里与本课对应的四篇：MP25（镜像、极/轴向量、叉乘、nabla 算子与外微分算子——本章入口题 (a) 与 3.1 节的原型）、MP26（Maxwell 方程组、电场与磁场、Hodge 星算子——命题 3.4、定义 3.5、定理 3.8 的来源）、MP36（Maxwell 方程的外微分形式——定理 3.11、3.13 与 (24.18) 的来源）、MP37（四维 Hodge 星算子、电磁势、规范变换——3.8、3.9 节的来源）。
- 陈省身《微分几何讲义》：Hodge 星算子与 Laplace–de Rham 算子的标准写法，$$\star^2$$ 与余微分 $$\delta$$ 的符号约定最干净的出处。
- Bott & Tu, *Differential Forms in Algebraic Topology*：第 1–2 章的 Poincaré 引理与 Mayer–Vietoris，是研2 中 $$H^2(\mathbb R^3\setminus\{0\})\ne0$$ 的标准处理。
- 朗道《场论》§25–§28：电磁场张量 $$F_{\mu\nu}$$ 与势 $$A_\mu$$ 的物理约定；对照本章 (24.9) 与 3.8 节。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch23_外微分与Maxwell方程组_上.md">← 第23章 外微分与 Maxwell 方程组·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch25_Stokes定理_上.md">第25章 Stokes 定理·上 →</a></div>
</div>
