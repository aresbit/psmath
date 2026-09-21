---
layout: default
---

# 第23章: 外微分与 Maxwell 方程组·上：预备与直觉 (Exterior Derivative and Maxwell's Equations · Part I: Warm-up and Intuition)

> 配套深化: 见 第24章 外微分与 Maxwell 方程组·下（完整推导），本章是它的具体铺垫，建议先读本章
> 对应原专栏: MP25、MP26、MP36、MP37
> 专家依据: 四专家无专章 —— 主用知识库
> 知识库依据: `opc2/knowledge/physics/电动力学/`（25 篇）、`opc2/knowledge/math/微分几何/differential-geometry/`（ch06、ch08）
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

本章要为第24章那几步"读者最容易在此摔跤"的地方先打好手感。第24章从"镜子里角速度不听话"只用两条命题就跳到"轴向量对应 2-形式"；从"$$\star$$ 是什么"到"grad/curl/div 是同一个 $$d$$"也只隔了一节；从"两个方程等于零"到 $$dF=0$$ 更是几乎没有过渡。这些跳跃在数学上都站得住，每一行也都看得懂，但连起来读，会觉得每一步都同时用了好几条前提——说不出"为什么会这样想"。

本章要打磨四个具体的跳跃点：（一）为什么"镜子里的不听话"能用一个正负号精确抓住；（二）Hodge 星算子 $$\star$$ 到底在做什么、怎么从定义直接解出来，而不是背表；（三）grad、curl、div 为什么其实是同一件事；（四）Maxwell 方程组里那两个"等于零"的方程为什么几乎不用算就自动成立。每一处都先代入 2–3 组具体数字手算，再抽象成一般说法，记号第一次出现时交代清楚它为什么被需要。读完本章，你应该已经能自己算出第24章要证明的大部分结论的具体实例——只是还没有对"任意"情形的一般证明。第24章会把这些手算步骤，原样符号化成严格陈述。

顺序上，本章刻意反着来：第24章是"先给一般定义，再给一般证明，例题放最后核对"；本章是"先算两三个具体的数，观察出规律，再把规律写成一句话"。这个顺序对读者更友好，是因为**一般证明往往只是把手算的步骤换成字母**——只要你先亲手算过 $$\vec a=(1,2,0)$$、$$\vec b=(0,1,3)$$ 这样的具体例子，再看到"设 $$\vec a,\vec b\in\mathbb R^3$$"开头的证明，就知道那些字母指的是什么、下一步该做什么运算，而不会觉得是凭空冒出来的推理。

## 二、入口：一道具体的问题 (Entry Problem)

不给定义，先做两组具体计算。第24章的入口题用的是"镜子里的汽车与车轮"这个生活场景；本章把同一个现象**剥掉物理外壳**，只留下"具体的几个数字"，让你先看清楚数字层面到底发生了什么，再回第24章去读它的物理讲法。

### 问题 (a)：一面具体的镜子

取镜面 $$P:(x,y,z)\mapsto(x,y,-z)$$（关于 $$xy$$ 平面反射，即把每个向量的第三个分量变号）。取两个具体向量 $$\vec a=(1,2,0)$$、$$\vec b=(0,1,3)$$。

1. 计算 $$\vec a\times\vec b$$。
2. 计算 $$P\vec a$$、$$P\vec b$$，再计算 $$(P\vec a)\times(P\vec b)$$。
3. 计算 $$P(\vec a\times\vec b)$$。比较第 2 步与第 3 步的结果——它们差一个什么符号？
4. 换一组数字 $$\vec a=(2,0,1)$$、$$\vec b=(1,3,0)$$，重复 1–3 步，看看第 3 步发现的规律是否再次出现。

**不要求解释原因**，只要求把两组数字都老老实实算完，猜出一条规律。

### 问题 (b)：三个具体的场，猜一条判据

1. 取 $$\vec B_1=(0,0,5)$$（处处相同的常向量场）与 $$\vec B_2=(x,y,-2z)$$（每个分量都是坐标的线性函数）。分别计算 $$\nabla\cdot\vec B_1$$、$$\nabla\cdot\vec B_2$$。
2. 不做计算，只看系数，判断 $$\vec B_3=(3x,-y,-2z)$$ 是否也满足 $$\nabla\cdot\vec B_3=0$$，并说出你用的判据——对形如 $$(ax,by,cz)$$ 的场，判据是什么？
3. 取 $$\vec E=(2x,3y,-5z)$$，计算 $$\nabla\times\vec E$$。再想一想：形如 $$(ax,by,cz)$$ 这种"对角线性"场的旋度，是不是不管 $$a,b,c$$ 取什么都恒为零？

这道题的第 1、2 问在预热"哪些场会让散度自动等于零"，第 3 问在预热"哪些场会让旋度自动等于零"——这正是第24章 $$\nabla\cdot\vec B=0$$ 与（静态情形下）$$\nabla\times\vec E=0$$ 这两条"自动成立"的方程的雏形。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 镜像判据：把"不听话"抓成一个符号

先回来看问题 (a)。第 1 步：

$$\vec a\times\vec b=(2\cdot3-0\cdot1,\ 0\cdot0-1\cdot3,\ 1\cdot1-2\cdot0)=(6,-3,1).$$

第 2 步：$$P\vec a=(1,2,0)$$（第三分量本是 $$0$$，变号不变），$$P\vec b=(0,1,-3)$$，于是

$$(P\vec a)\times(P\vec b)=\bigl(2\cdot(-3)-0\cdot1,\ 0\cdot0-1\cdot(-3),\ 1\cdot1-2\cdot0\bigr)=(-6,3,1).$$

第 3 步：$$P(\vec a\times\vec b)=P(6,-3,1)=(6,-3,-1)$$。

比较：$$(P\vec a)\times(P\vec b)=(-6,3,1)$$，而 $$P(\vec a\times\vec b)=(6,-3,-1)$$——两者**恰好互为相反数**：

$$(P\vec a)\times(P\vec b)=-P(\vec a\times\vec b). \tag{23.1}$$

第二组数字 $$\vec a=(2,0,1)$$、$$\vec b=(1,3,0)$$：$$\vec a\times\vec b=(0\cdot0-1\cdot3,\ 1\cdot1-2\cdot0,\ 2\cdot3-0\cdot1)=(-3,1,6)$$；$$P\vec a=(2,0,-1)$$、$$P\vec b=(1,3,0)$$，$$(P\vec a)\times(P\vec b)=\bigl(0\cdot0-(-1)\cdot3,\ (-1)\cdot1-2\cdot0,\ 2\cdot3-0\cdot1\bigr)=(3,-1,6)$$；而 $$P(\vec a\times\vec b)=P(-3,1,6)=(-3,1,-6)$$。再一次，$$(P\vec a)\times(P\vec b)=(3,-1,6)=-P(\vec a\times\vec b)$$。**两组数字给出同一条规律**：叉乘的结果在镜子里比"老老实实跟着镜子走"多出一个负号。

这个负号从哪来？注意 $$P=\operatorname{diag}(1,1,-1)$$ 满足 $$\det P=-1$$。(23.1) 里的负号正是 $$\det P$$——这不是巧合。一般地：

**定义 3.1（镜像 / reflection）**。设 $$P$$ 是 $$\mathbb R^3$$ 上的一个正交变换（保长度），且 $$\det P=-1$$。称这样的 $$P$$ 为一个**镜像**。上面的 $$P=\operatorname{diag}(1,1,-1)$$ 就是一个具体例子；"正交"保证它不改变向量的长度与夹角（否则谈"镜子"就没意义），"$$\det P=-1$$"则是把它和"旋转"（$$\det P=+1$$ 的正交变换）区分开来的那一个数字——这正是我们接下来唯一要用的信息。

一个由物理系统决定的向量 $$\vec v$$，如果做镜像后"老实"变成 $$P\vec v$$，就叫**极向量 (polar vector)**（位移、速度都是）；如果像 (23.1) 那样多出一个 $$-1$$，变成 $$-P\vec v$$，就叫**轴向量 (axial vector)**（角速度、磁感应都是）。判据是"镜像后多不多一个负号"，与这个量"看起来像不像三个数"无关——需要这个记号，是因为初等物理把"位移"和"角速度"都叫"向量"，却从没说清楚它们在镜子里的行为根本不同；极向量/轴向量这两个名字，就是把这条区别钉死。

**命题 3.2（叉乘产生轴向量）**。设 $$\vec a,\vec b$$ 是极向量。则 $$\vec a\times\vec b$$ 是轴向量，即对任意镜像 $$P$$，

$$(P\vec a)\times(P\vec b)=\det(P)\,P(\vec a\times\vec b)=-P(\vec a\times\vec b).$$

上面两组具体数字已经各验证了一遍。**一般证明**（对任意 $$P\in O(3)$$，不止镜像）见第24章 命题 3.3——那里的做法就是把 $$\vec a,\vec b$$ 换成标准基 $$\vec e_i,\vec e_j$$，抽象地重复我们刚才做的事：验证 $$(P\vec e_i)\times(P\vec e_j)$$ 恰好是 $$P$$ 的第 $$i,j$$ 列的叉乘，等于 $$\det(P)$$ 乘 $$P$$ 的第三列。

### 3.2 Hodge 星算子：不背表，自己解出来

轴向量与极向量的"不听话"能被 $$\det P$$ 的符号抓住，但三维向量本身还欠一样东西：轴向量到底是什么"几何对象"？直接说"它是 2-形式"过于突兀——我们先具体解出 $$\star dx$$ 应该是什么，再回头看这句话什么意思。

$$\mathbb R^3$$ 取标准正交余标架 $$(dx,dy,dz)$$，体积 $$\mathrm{vol}=dx\wedge dy\wedge dz$$。**要找的东西**：一个 2-形式 $$\star dx=c_1\,dy\wedge dz+c_2\,dz\wedge dx+c_3\,dx\wedge dy$$，使得对任意 1-形式 $$\alpha$$，

$$\alpha\wedge\star dx=\langle\alpha,dx\rangle\,\mathrm{vol}. \tag{23.2}$$

这是三个未知数 $$c_1,c_2,c_3$$ 的方程组，代 $$\alpha=dx,dy,dz$$ 三次就能解出来：

- $$\alpha=dx$$：左边 $$dx\wedge\star dx=c_1\,dx\wedge dy\wedge dz$$（另两项含重复的 $$dx$$，为零）；右边 $$\langle dx,dx\rangle\,\mathrm{vol}=1\cdot\mathrm{vol}$$。比较系数，$$c_1=1$$。
- $$\alpha=dy$$：左边 $$dy\wedge\star dx=c_2\,dy\wedge dz\wedge dx=c_2\,dx\wedge dy\wedge dz$$（$$dy\wedge dz\wedge dx$$ 是把 $$dx$$ 挪到最前，经过两次对换，为偶置换）；右边 $$\langle dy,dx\rangle\,\mathrm{vol}=0$$。故 $$c_2=0$$。
- $$\alpha=dz$$：同理左边 $$=c_3\,dz\wedge dx\wedge dy=c_3\,\mathrm{vol}$$；右边 $$=0$$，故 $$c_3=0$$。

于是 $$\star dx=dy\wedge dz$$——**不是背出来的，是解一个三元一次方程组解出来的**。同样的三步能解出 $$\star dy=dz\wedge dx$$、$$\star dz=dx\wedge dy$$，以及反过来把 2-形式送回 1-形式的三个式子，与第24章 (24.7) 的表完全一致。

**用一个具体线性组合验一遍**：设 $$\omega=2\,dx-3\,dy$$。由线性性，$$\star\omega=2\,dy\wedge dz-3\,dz\wedge dx$$。算 $$\omega\wedge\star\omega$$：

$$\omega\wedge\star\omega=(2\,dx-3\,dy)\wedge(2\,dy\wedge dz-3\,dz\wedge dx)=4\,dx\wedge dy\wedge dz+9\,dy\wedge dz\wedge dx=(4+9)\,\mathrm{vol}=13\,\mathrm{vol}$$

（中间两个交叉项各含重复的 $$dx$$ 或 $$dy$$，为零；$$dy\wedge dz\wedge dx=dx\wedge dy\wedge dz$$ 是偶置换）。而 $$\langle\omega,\omega\rangle=2^2+(-3)^2=13$$，恰好对上——这正是 (23.2) 那条定义式，只是现在用在了一个不是基向量的例子上，说明它对任意 1-形式都成立，不只是对 $$dx,dy,dz$$ 这三个基元素。

**定义 3.3（Hodge 星算子，$$\mathbb R^3$$ 情形）**。$$\star:\Omega^k(\mathbb R^3)\to\Omega^{3-k}(\mathbb R^3)$$ 是唯一满足 (23.2) 型定义式（把 $$dx$$ 换成任意 $$k$$-形式 $$\beta$$、$$\alpha$$ 取遍 $$\Omega^k$$）的线性映射。我们已经对 $$k=1$$ 的三个基元素解出了它。一般维数、一般（伪）黎曼度量下的定义见第24章 定义 3.5——那里把我们刚才"解三元方程组"这件事搬到一般的正交余标架下，逐条基元素重复了一遍（第24章 引理 3.6），结论就是我们已经验证过的表。

**对合性，具体算一遍**：$$\star\star dx=\star(dy\wedge dz)=dx$$，$$\star\star(dy\wedge dz)=\star dx=dy\wedge dz$$——转两次回到自己。

**命题 3.4（$$\star\star=+1$$，$$\mathbb R^3$$ 情形）**。在 $$\mathbb R^3$$ 上，对任意 $$k=0,1,2,3$$，$$\star\star=+1$$（对 $$\Omega^k$$ 上的任意形式）。我们已经对 $$\Omega^1$$ 的基元素验证过；这不是巧合，而是第24章 定理 3.7 给出的一般公式 $$\star\star\omega=(-1)^{k(n-k)}\operatorname{sgn}(g)\,\omega$$ 在 $$n=3$$、度量正定（$$\operatorname{sgn}(g)=+1$$）、$$k(3-k)$$ 恒为偶数时的特例。

### 3.3 grad、curl、div：同一件事，算两个例子看穿它

先算两个具体向量场，观察 $$d$$ 与 $$\star$$ 联手能算出什么。

**例（curl）**。取 $$\vec F=(y,z,x)$$，对应 1-形式 $$\omega_F=y\,dx+z\,dy+x\,dz$$。直接按向量分析公式：

$$\nabla\times\vec F=(\partial_yF_z-\partial_zF_y,\ \partial_zF_x-\partial_xF_z,\ \partial_xF_y-\partial_yF_x)=(0-1,\ 0-1,\ 0-1)=(-1,-1,-1).$$

现在换一条路：先求 $$d\omega_F$$，再作用 $$\star$$。

$$d\omega_F=d(y)\wedge dx+d(z)\wedge dy+d(x)\wedge dz=dy\wedge dx+dz\wedge dy+dx\wedge dz=-dx\wedge dy-dy\wedge dz-dz\wedge dx.$$

用 3.2 节已经解出的表 $$\star(dx\wedge dy)=dz$$、$$\star(dy\wedge dz)=dx$$、$$\star(dz\wedge dx)=dy$$：

$$\star\,d\omega_F=-dz-dx-dy,$$

对应向量 $$(-1,-1,-1)$$——**与直接算的 $$\nabla\times\vec F$$ 完全一致**。

**例（div）**。取 $$\vec F=(x,y,z)$$，对应 $$\omega_F=x\,dx+y\,dy+z\,dz$$。直接算 $$\nabla\cdot\vec F=1+1+1=3$$。换一条路：$$\star\omega_F=x\,dy\wedge dz+y\,dz\wedge dx+z\,dx\wedge dy$$，取 $$d$$：

$$d(\star\omega_F)=dx\wedge dy\wedge dz+dy\wedge dz\wedge dx+dz\wedge dx\wedge dy=3\,dx\wedge dy\wedge dz$$

（三项都是 $$dx\wedge dy\wedge dz$$ 的偶置换，系数各为 $$1$$）。再 $$\star$$ 一次，$$\star(3\,\mathrm{vol})=3$$——与直接算的 $$\nabla\cdot\vec F=3$$ 一致。

两个例子的算法完全平行：**先用 $$d$$，再按需要夹一次或两次 $$\star$$**。一般地：

**定理 3.5（三个算子，一个 $$d$$，具体版）**。设 $$f\in\mathcal C^\infty(\mathbb R^3)$$、$$\vec F$$ 是光滑向量场、$$\omega_F$$ 是它对应的 1-形式。则 $$\nabla f\leftrightarrow df$$、$$\nabla\times\vec F\leftrightarrow\star\,d\omega_F$$、$$\nabla\cdot\vec F=\star\,d\star\omega_F$$——我们刚才对两个具体的 $$\vec F$$ 各验证了一条。**为什么必须夹 $$\star$$**：$$d$$ 本身只会把次数升高（$$0\to1\to2\to3$$），而 curl、div 在向量分析里都"回到"向量或标量，$$\star$$ 的任务就是把升次后的结果按 3.2 节解出的表"换算回"熟悉的次数。一般证明（对任意 $$f,\vec F$$，不只是我们选的两个例子）见第24章 定理 3.8——做法就是把系数换成一般的 $$F_x,F_y,F_z$$，逐项重复我们刚才的两步计算。

### 3.4 两个"自动成立"的方程：具体验证

回到入口题 (b)。$$\vec B_2=(x,y,-2z)$$：$$\nabla\cdot\vec B_2=1+1-2=0$$。这不是巧合，而是系数之和为零：一般地，$$(ax,by,cz)$$ 型的场满足 $$\nabla\cdot(ax,by,cz)=a+b+c$$，为零当且仅当 $$a+b+c=0$$。$$\vec B_3=(3x,-y,-2z)$$ 的系数和 $$3+(-1)+(-2)=0$$，所以不用算就知道 $$\nabla\cdot\vec B_3=0$$——这就是入口题第 2 问要猜的判据。$$\vec B_1=(0,0,5)$$ 满足 $$\nabla\cdot\vec B_1=0$$ 则是另一条更简单的理由：**常数的偏导数恒为零**，与"系数和"无关。

$$\vec E=(2x,3y,-5z)$$：$$\nabla\times\vec E=(\partial_y(-5z)-\partial_z(3y),\ \partial_z(2x)-\partial_x(-5z),\ \partial_x(3y)-\partial_y(2x))=(0,0,0)$$。这也不是巧合：**"对角线性"场** $$(ax,by,cz)$$（每个分量只依赖同名坐标）的旋度**恒为零**，因为旋度的每一项都是"一个分量对另一个坐标求偏导"，而对角线性场里这种交叉偏导恒为零。

这两条"自动成立"，背后是同一件事的两面。把 $$\vec B_2=(x,y,-2z)$$ 换算成 2-形式 $$\tilde B_2=x\,dy\wedge dz+y\,dz\wedge dx-2z\,dx\wedge dy$$，取 $$d$$：

$$d\tilde B_2=dx\wedge dy\wedge dz+dy\wedge dz\wedge dx-2\,dz\wedge dx\wedge dy=(1+1-2)\,\mathrm{vol}=0.$$

**系数之和恰好就是 $$d\tilde B_2$$ 里唯一那个系数**——3.3 节的定理已经告诉我们 $$\star d\tilde B_2=\nabla\cdot\vec B_2$$，所以 $$d\tilde B_2=0$$ 与 $$\nabla\cdot\vec B_2=0$$ 说的是同一件事，只是语言不同。同样，$$\vec E$$ 换算成 1-形式 $$\omega_E=2x\,dx+3y\,dy-5z\,dz$$，$$d\omega_E=0$$（每一项如 $$d(2x)\wedge dx=2\,dx\wedge dx=0$$，其余同理，因为每个系数只依赖"自己的"坐标）正是 $$\nabla\times\vec E=0$$ 的形式语言。

**定理 3.6（静态"自动成立"的两个方程，具体版）**。在不随时间变化的情形下，$$\nabla\cdot\vec B=0$$ 与 $$\nabla\times\vec E=0$$ 都可以写成"某个形式的 $$d$$ 等于零"。我们已经对 $$\vec B_2,\vec B_3,\vec E$$ 这样的具体场各验证了一遍。**为什么这两条会"自动成立"**：设想 $$\vec B$$ 本身来自某个向量势 $$\vec A$$（即 $$\vec B=\nabla\times\vec A$$），由 3.3 节的定理，$$\nabla\cdot\vec B=\star d\star(\star d\omega_A)\overset{\star\star=+1}{=}\star d^2\omega_A$$，而"求两次 $$d$$"结构性地等于零（第 14 章已证 $$d^2=0$$）——这正是"两次求差自动抵消"的具体机制，不是巧合。第24章会补上时间依赖（$$\partial_t\vec B\ne0$$ 时怎么办），把 $$\vec E,\vec B$$ 合并成 $$\mathbb R^{3,1}$$ 上的一个 2-形式 $$F$$，证明这两条一起恰好就是 $$dF=0$$（第24章 定理 3.11），并进一步解释"$$dF=0$$"为什么在物理里就叫"不存在磁单极子"。

## 四、几何与物理直觉 (Intuition)

**镜子判据像什么**：把一支铅笔立在桌上，笔尖朝上，这是"位移型"的量——镜子里它老老实实立着。现在让笔在桌面上打转（像风扇叶片），转动的方向可以用"右手螺旋"定成一个箭头。把这支转笔和它的镜像并排放：镜子里的笔转动方向不会跟着翻转成"左手螺旋"，而是保持原来的转向——这就是命题 3.2 说的"多一个负号"在生活里的样子。磁场（由电流环产生）与转笔是同一类，电场（由电荷产生）与位移的笔是同一类。

**Hodge 星像什么**：一根尺子只能量一个方向的长度，一张渔网能量一片面积。$$\star$$ 做的事，是把"量一个方向"换算成"量剩下的那些方向"：在三维里，量一条边（1-形式）和量与它垂直的一张面（2-形式）说的是同一件事的两种读数方式，因为三维空间里"选 1 个方向"和"选 2 个（互补）方向"数目一样多（都是 3 种）。$$\star$$ 只是把这两种读数方式之间的换算写成公式，而不是凭空变出来的一个新算子。

**grad/curl/div 像同一把可换头的螺丝刀**：三个算子看起来像三种不同工具，实际上是同一个"升次"动作 $$d$$，配上不同的"换算头"（要不要夹 $$\star$$、夹几次）。这也是为什么向量分析教材里那几条恒等式看起来各不相干，实际上只是同一句话换了两次螺丝刀头。

**"自动成立"像检查一份账**：如果一笔钱的进出账目本身就是从另一笔总账"求差"得到的，那么这笔账的"总和"自动为零，不需要再验算——因为"求两次差"结构性地抵消了。3.4 节里 $$\nabla\cdot\vec B=0$$ 的直觉正是如此：$$\vec B$$ 如果是"从 $$\vec A$$ 求旋度"得到的，"$$\vec B$$ 的散度"就是在"求两次差"，账目结构性地清零，不需要逐点验算。

**"边界的边界为空"像一个封了口的信封**：把一张纸卷成一个没有缺口的信封（比如一个球面），它本身没有边——你摸不到"信封的边缘"在哪里，因为根本没有。反过来，如果这张纸只是卷成一个筒（没封口），它就有两条边界圆。"求一次边界"可能得到东西，但"边界再求一次边界"永远空的——一个圆圈没有端点，一个封了口的球面没有边缘。这句听起来像文字游戏的话，翻成公式就是 $$\partial\partial=\varnothing$$（第 09–10 章）或 $$d^2=0$$（第 14 章），而 3.4 节里 $$\nabla\cdot\vec B=0$$ 之所以能"自动成立"，用的正是这同一条机制——只是这次它换了个物理的名字：**不存在磁单极子**。第24章会把这句直觉说清楚：为什么"没有单极子"和"边界没有边界"其实是同一件事换了两种语言。

## 五、经典问题精讲 (Classical Problems)

下面四题分别对应 3.1–3.4 节的四个知识点，但都换了一组新的具体数字，逼着你重复一遍"代数运算"而不是"背结论"——这也是检验自己是不是真的会算、而不是记住了本章例子答案的办法。

### 经典题 1：换一面镜子，验证轴向量判据

**题**。取镜面 $$P=\operatorname{diag}(-1,1,1)$$（关于 $$yz$$ 平面反射），$$\vec a=(1,1,0)$$、$$\vec b=(0,2,1)$$。验证 $$(P\vec a)\times(P\vec b)=\det(P)\,P(\vec a\times\vec b)$$。

**解**。$$\vec a\times\vec b=(1\cdot1-0\cdot2,\ 0\cdot0-1\cdot1,\ 1\cdot2-1\cdot0)=(1,-1,2)$$。$$P\vec a=(-1,1,0)$$、$$P\vec b=(0,2,1)$$，$$(P\vec a)\times(P\vec b)=\bigl(1\cdot1-0\cdot2,\ 0\cdot0-(-1)\cdot1,\ (-1)\cdot2-1\cdot0\bigr)=(1,1,-2)$$。$$P(\vec a\times\vec b)=P(1,-1,2)=(-1,-1,2)$$，$$\det(P)=-1$$，故 $$\det(P)\,P(\vec a\times\vec b)=(1,1,-2)$$——与 $$(P\vec a)\times(P\vec b)$$ 一致。$$\square$$

### 经典题 2：不查表，解出 $$\star(dz\wedge dx)$$

**题**。仿照 3.2 节"解方程组"的方法（不查表），从定义式直接解出 $$\star(dz\wedge dx)$$（应该是一个 1-形式）。

**解**。设 $$\star(dz\wedge dx)=c_1\,dx+c_2\,dy+c_3\,dz$$，要求对任意 2-形式 $$\alpha$$，$$\alpha\wedge\star(dz\wedge dx)=\langle\alpha,dz\wedge dx\rangle\,\mathrm{vol}$$。代三个基 2-形式：

- $$\alpha=dy\wedge dz$$：左边 $$(dy\wedge dz)\wedge(c_1dx+c_2dy+c_3dz)=c_1\,dy\wedge dz\wedge dx=c_1\,\mathrm{vol}$$（$$dy\wedge dz\wedge dx$$ 把 $$dx$$ 挪到最前需两次对换，偶置换，等于 $$\mathrm{vol}$$）；右边 $$\langle dy\wedge dz,\,dz\wedge dx\rangle\,\mathrm{vol}=0$$（不同基 2-形式正交）。故 $$c_1=0$$。
- $$\alpha=dz\wedge dx$$：左边 $$(dz\wedge dx)\wedge(c_1dx+c_2dy+c_3dz)=c_2\,dz\wedge dx\wedge dy=c_2\,\mathrm{vol}$$；右边 $$\langle dz\wedge dx,\,dz\wedge dx\rangle\,\mathrm{vol}=1\cdot\mathrm{vol}$$。故 $$c_2=1$$。
- $$\alpha=dx\wedge dy$$：左边 $$=c_3\,dx\wedge dy\wedge dz=c_3\,\mathrm{vol}$$；右边 $$=0$$。故 $$c_3=0$$。

于是 $$\star(dz\wedge dx)=dy$$。$$\square$$

### 经典题 3：curl grad = 0、div curl = 0 各算一个具体例子

**题**。(a) 设 $$f=x^2+yz^2$$，求 $$\nabla f$$ 与 $$\operatorname{curl}(\nabla f)$$；(b) 设 $$\vec F=(y,-x,0)$$，求 $$\operatorname{curl}\vec F$$ 与 $$\operatorname{div}(\operatorname{curl}\vec F)$$。

**解**。(a) $$\nabla f=(2x,z^2,2yz)$$。

$$\operatorname{curl}(\nabla f)=\bigl(\partial_y(2yz)-\partial_z(z^2),\ \partial_z(2x)-\partial_x(2yz),\ \partial_x(z^2)-\partial_y(2x)\bigr)=(2z-2z,\ 0-0,\ 0-0)=(0,0,0).$$

(b) $$\operatorname{curl}\vec F=\bigl(\partial_y0-\partial_z(-x),\ \partial_z y-\partial_x0,\ \partial_x(-x)-\partial_yy\bigr)=(0,0,-2)$$（一个常向量场）。

$$\operatorname{div}(\operatorname{curl}\vec F)=\partial_x0+\partial_y0+\partial_z(-2)=0.$$

两条都符合第24章推论 3.9 的一般结论；这里只是各代了一组具体数字，把"两次升次抵消"或"常场的偏导为零"看得清清楚楚。$$\square$$

### 经典题 4：给一个均匀磁场找一个向量势

**题**。设 $$\vec B=(0,0,4)$$（均匀磁场）。验证 $$\vec A=(-2y,2x,0)$$ 满足 $$\nabla\times\vec A=\vec B$$。

**解**。$$\nabla\times\vec A=\bigl(\partial_y0-\partial_z(2x),\ \partial_z(-2y)-\partial_x0,\ \partial_x(2x)-\partial_y(-2y)\bigr)=(0,0,2+2)=(0,0,4)=\vec B.$$

这就是 3.4 节"$$\vec B$$ 若来自势 $$\vec A$$ 则 $$\nabla\cdot\vec B$$ 自动为零"的一个具体实例（读者可自行验证 $$\nabla\cdot\vec B=0$$）：这里我们反过来，先给定 $$\vec B$$，具体**造出**一个 $$\vec A$$。第24章 3.8 节会证明：只要 $$\vec B$$ 满足 $$\nabla\cdot\vec B=0$$，这样的 $$\vec A$$ 就总能找到，而且相差一个"规范变换"。$$\square$$

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 取镜面 $$P=\operatorname{diag}(1,-1,1)$$（关于 $$xz$$ 平面反射），$$\vec a=(1,0,2)$$、$$\vec b=(2,1,0)$$。验证 $$(P\vec a)\times(P\vec b)=\det(P)\,P(\vec a\times\vec b)$$。

**基2.** 设 $$\omega=5\,dz$$。用 3.2 节解出的表求 $$\star\omega$$，再求 $$\star\star\omega$$，验证它等于 $$\omega$$。

**基3.** 设 $$f=xy^2z$$。求 $$\nabla f$$ 在点 $$(1,2,1)$$ 处的值；再求一般的 $$\operatorname{curl}(\nabla f)$$（不代入具体点），验证它恒为零向量。

**基4.** 判断下列各量是极向量还是轴向量，并说明理由（可引用命题 3.2）：(a) 一个质点的位移 $$\Delta\vec r$$；(b) 角动量 $$\vec L=\vec r\times\vec p$$（$$\vec r,\vec p$$ 都是极向量）；(c) 磁矩 $$\vec m$$（由"电流环围出的面积向量"定义，面积向量本身由两条边向量叉乘给出）。

### 竞赛（本课目标难度）

**竞1.** 设 $$\vec F=(y^2,xz,-xy)$$。求 $$\operatorname{curl}\vec F$$，再求 $$\operatorname{div}(\operatorname{curl}\vec F)$$，验证结果为零。

**竞2.** 设 $$\vec A=(-yz,xz,0)$$。求 $$\vec B:=\operatorname{curl}\vec A$$ 的显式表达式，并验证 $$\nabla\cdot\vec B=0$$。

**竞3.** 仿照经典题 2 的方法（解方程组，不查表），求 $$\star(dx\wedge dy)$$。

### 研究（通向下一章）

**研1.** 设 $$\vec E=(0,0,E_0\sin(\omega t))$$（处处相同，只随时间变化）。
(a) 计算 $$\nabla\times\vec E$$（对任意固定 $$t$$）。
(b) 若 Maxwell 方程 $$\nabla\times\vec E=-\partial_t\vec B$$ 成立，由 (a) 能推出 $$\partial_t\vec B$$ 的什么结论？
(c) 由 (b) 说明：如果要求 $$\vec B$$ 本身也是"处处相同"的均匀场且随时间变化，会出现什么矛盾——这说明了什么？

**研2.** 设 $$\vec A=(0,x,0)$$，$$f=xyz$$，$$\vec A'=\vec A+\nabla f$$。
(a) 分别求 $$\operatorname{curl}\vec A$$ 与 $$\operatorname{curl}\vec A'$$，比较两者。
(b) 这个结果说明了什么——同一个磁场 $$\vec B$$ 能不能来自不止一个向量势 $$\vec A$$？

### 解答 (Solutions)

**解 基1.** $$\vec a\times\vec b=(0\cdot0-2\cdot1,\ 2\cdot2-1\cdot0,\ 1\cdot1-0\cdot2)=(-2,4,1)$$。$$P\vec a=(1,0,2)$$、$$P\vec b=(2,-1,0)$$，$$(P\vec a)\times(P\vec b)=\bigl(0\cdot0-2\cdot(-1),\ 2\cdot2-1\cdot0,\ 1\cdot(-1)-0\cdot2\bigr)=(2,4,-1)$$。$$P(\vec a\times\vec b)=P(-2,4,1)=(-2,-4,1)$$，$$\det P=-1$$，$$\det(P)\,P(\vec a\times\vec b)=(2,4,-1)$$，与 $$(P\vec a)\times(P\vec b)$$ 一致。$$\square$$

**解 基2.** 由 3.2 节的表 $$\star dz=dx\wedge dy$$，线性给出 $$\star(5\,dz)=5\,dx\wedge dy$$。再 $$\star(5\,dx\wedge dy)=5\,\star(dx\wedge dy)=5\,dz$$（用表 $$\star(dx\wedge dy)=dz$$）。故 $$\star\star\omega=5\,dz=\omega$$，与命题 3.4 的 $$\star\star=+1$$ 一致。$$\square$$

**解 基3.** $$\nabla f=(y^2z,\,2xyz,\,xy^2)$$。在 $$(1,2,1)$$：$$y^2z=4\cdot1=4$$，$$2xyz=2\cdot1\cdot2\cdot1=4$$，$$xy^2=1\cdot4=4$$，故 $$\nabla f\vert_{(1,2,1)}=(4,4,4)$$。

一般地：

$$\operatorname{curl}(\nabla f)=\bigl(\partial_y(xy^2)-\partial_z(2xyz),\ \partial_z(y^2z)-\partial_x(xy^2),\ \partial_x(2xyz)-\partial_y(y^2z)\bigr)=(2xy-2xy,\ y^2-y^2,\ 2yz-2yz)=(0,0,0).$$

恒为零向量，与第24章推论 3.9 一致。$$\square$$

**解 基4.** (a) $$\Delta\vec r$$ 是极向量：位移本身就是"镜像老实变成 $$P\Delta\vec r$$"的典型例子（定义 3.1 之后的说明）。

(b) $$\vec L=\vec r\times\vec p$$ 是两个极向量的叉乘，由命题 3.2，轴向量。

(c) 磁矩 $$\vec m$$ 由"电流环围出的面积向量"定义，而面积向量本身是两条边向量的叉乘，故也是两个极向量叉乘的产物，由命题 3.2 是轴向量。$$\square$$

**解 竞1.** $$\operatorname{curl}\vec F=\bigl(\partial_y(-xy)-\partial_z(xz),\ \partial_z(y^2)-\partial_x(-xy),\ \partial_x(xz)-\partial_y(y^2)\bigr)=(-x-x,\ 0+y,\ z-2y)=(-2x,\,y,\,z-2y)$$。

$$\operatorname{div}(\operatorname{curl}\vec F)=\partial_x(-2x)+\partial_y(y)+\partial_z(z-2y)=-2+1+1=0.\qquad\square$$

**解 竞2.** $$\vec B=\operatorname{curl}\vec A=\bigl(\partial_y0-\partial_z(xz),\ \partial_z(-yz)-\partial_x0,\ \partial_x(xz)-\partial_y(-yz)\bigr)=(-x,\,-y,\,2z)$$。

$$\nabla\cdot\vec B=\partial_x(-x)+\partial_y(-y)+\partial_z(2z)=-1-1+2=0.\qquad\square$$

**解 竞3.** 设 $$\star(dx\wedge dy)=c_1dx+c_2dy+c_3dz$$。代 $$\alpha=dy\wedge dz$$：左边 $$(dy\wedge dz)\wedge(c_1dx+c_2dy+c_3dz)=c_1\,dy\wedge dz\wedge dx=c_1\,\mathrm{vol}$$；右边 $$\langle dy\wedge dz,dx\wedge dy\rangle\,\mathrm{vol}=0$$，故 $$c_1=0$$。代 $$\alpha=dz\wedge dx$$：左边 $$=c_2\,dz\wedge dx\wedge dy=c_2\,\mathrm{vol}$$；右边 $$=0$$，故 $$c_2=0$$。代 $$\alpha=dx\wedge dy$$：左边 $$=c_3\,dx\wedge dy\wedge dz=c_3\,\mathrm{vol}$$；右边 $$=1\cdot\mathrm{vol}$$，故 $$c_3=1$$。于是 $$\star(dx\wedge dy)=dz$$，与 3.2 节的表一致。$$\square$$

**解 研1.** (a) $$\vec E$$ 处处相同（不依赖 $$x,y,z$$），旋度的每一项都是对空间坐标求偏导，故 $$\nabla\times\vec E=(0,0,0)$$，对任意固定 $$t$$ 都成立。

(b) 由 $$\nabla\times\vec E=-\partial_t\vec B$$ 及 (a)，得 $$\partial_t\vec B=\vec 0$$，即 $$\vec B$$ **不随时间变化**。

(c) 若同时要求 $$\vec B$$ 处处相同**且**随时间变化，就与 (b) 的 $$\partial_t\vec B=\vec 0$$ 矛盾（除非 $$\vec B$$ 本身恒为零向量）。这说明：一个"处处相同、随时间变化"的电场，不能配一个同样"处处相同、随时间变化"的磁场——时变的场必须带上空间结构，这正是第24章要把 $$\vec E,\vec B$$ 装进依赖全部四个坐标 $$(t,x,y,z)$$ 的一个 2-形式 $$F$$ 的原因之一。$$\square$$

**解 研2.** (a) $$\operatorname{curl}\vec A=\bigl(\partial_y0-\partial_zx,\ \partial_z0-\partial_x0,\ \partial_xx-\partial_y0\bigr)=(0,0,1)$$。

$$\nabla f=(yz,xz,xy)$$，$$\vec A'=(yz,\,x+xz,\,xy)$$。

$$\operatorname{curl}\vec A'=\bigl(\partial_y(xy)-\partial_z(x+xz),\ \partial_z(yz)-\partial_x(xy),\ \partial_x(x+xz)-\partial_y(yz)\bigr)=(x-x,\ y-y,\ (1+z)-z)=(0,0,1).$$

两者相等：$$\operatorname{curl}\vec A'=\operatorname{curl}\vec A$$。

(b) 说明同一个磁场 $$\vec B=(0,0,1)$$ 既来自 $$\vec A$$ 也来自 $$\vec A'=\vec A+\nabla f$$——向量势不唯一，加上任意一个函数的梯度都不改变它给出的磁场（因为 $$\operatorname{curl}(\nabla f)=\vec 0$$，见经典题 3(a) 的同款计算）。第24章会把这件事正式命名为**规范变换**，并证明背后的机制正是 $$d^2=0$$。$$\square$$

## 七、Takeaway 与延伸 (Takeaways)

1. **镜像判据是一个符号问题**：极向量老实跟镜子走，轴向量多一个负号（命题 3.2）；两个极向量叉乘，出来的总是轴向量。
2. **Hodge 星 $$\star$$ 不是要背的表，是解线性方程组解出来的**——在 $$\mathbb R^3$$ 上 $$\star$$ 把"选一个方向"换算成"选另外两个方向"，且 $$\star\star=+1$$。
3. **grad、curl、div 是同一个 $$d$$ 配不同次数的 $$\star$$**——我们已经对具体的向量场各验证过一条对应关系。
4. **"自动成立"的方程背后是"求两次差自动抵消"**：常场或线性系数和为零的场，散度、旋度自动为零，来自代数结构而不是巧合，根源正是 $$d^2=0$$。
5. **交棒**：现在你已经能手算镜像判据、Hodge 星、grad/curl/div 之间的相互转换，也已经在具体例子里验证过两个"自动成立"的方程，还亲手给一个具体磁场造出过一个向量势。下一章会把时间也当作第四个坐标，把 $$\vec E,\vec B$$ 合并成一个 2-形式 $$F$$，证明这一切对任意（不只是我们选的）函数、任意向量场、在任意时刻都成立，并进一步用它把 Maxwell 方程组从四个压成两个，引出规范变换与自对偶分解。

带着几个具体问题去读第24章会更有效率：$$\vec a\times\vec b$$ 的镜像规律，对**任意**极向量 $$\vec a,\vec b$$、**任意**镜像 $$P$$ 都成立吗（命题 3.2 到第24章 命题 3.3 的推广）？$$\star dx=dy\wedge dz$$ 这套解方程组的手法，换到四维 Minkowski 时空、换成不定号的度量，还能照搬吗（3.2 节到第24章 3.2–3.3 节）？3.4 节里"系数和为零"的具体判据，一般化之后究竟是什么样的方程（第24章定理 3.11）？把这几个问题带着走，第24章的证明就会读成"哦，原来是这样"，而不是"这一步是怎么想到的"。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch22_张量与张量丛_下.md">← 第22章 张量与张量丛·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch24_外微分与Maxwell方程组_下.md">第24章 外微分与 Maxwell 方程组·下 →</a></div>
</div>
