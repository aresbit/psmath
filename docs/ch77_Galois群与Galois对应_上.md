---
layout: default
---

# 第77章: Galois 群与 Galois 对应·上：预备与直觉 (The Galois Group and the Galois Correspondence · Part I: Warm-up and Intuition)

> 配套深化: 见 第78章 Galois 群与 Galois 对应·下（完整推导），本章是它的具体铺垫，建议先读本章
> 专家依据: `_experts/algebra/group-theory-galois.md`（主）+ `_experts/numbertheory/algebraic-number-theory.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

第 78 章要证明两件不那么直观的事：一是「自同构」全体自动成群（不需要额外假设），二是「中间域」与「子群」之间存在一一对应，而且大小完全翻转。那一章的证明里有两处对普通读者最容易"跟着符号走却不知道在干什么"：**一是「自同构互相线性无关」这条纯线性代数事实（Dedekind 引理、Artin 引理都建立在它上面）；二是"固定域"这个新记号本身**——它是什么、为什么要引进它、算出来是什么样子。

本章要打磨的就是这两个点，外加一次"手算对应表"的预演。我们会在 $$\mathbb{Q}(\sqrt2)$$、$$\mathbb{Q}(\sqrt2,\sqrt3)$$、$$\mathbb{Q}(\sqrt[3]2)$$ 这三个具体的域上，把"自同构""固定域""对称个数 vs 扩张次数""对应表"逐一手算一遍。读完本章，你应该已经能不看书、直接口算出 $$\operatorname{Gal}(\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q})$$ 的四个元素、它的五个子群，以及五个子群各自对应的中间域——第 78 章要做的，只是把这些你已经算过的东西写成一般定义和证明。

## 二、入口：一道具体的问题 (Entry Problem)

**不给定义，先动手算。**

**(1)** 设 $$L=\mathbb{Q}(\sqrt2)=\{a+b\sqrt2:a,b\in\mathbb{Q}\}$$。找出 $$L$$ 到自身、保持每个有理数不动、且与加法乘法都相容的双射，一共有几个？把它们都写出来。

**(2)** 设 $$M=\mathbb{Q}(\sqrt[3]2)\subseteq\mathbb{R}$$（只取实数意义下的立方根）。同样的映射有几个？

**(3)** 分别算出 $$[\mathbb{Q}(\sqrt2):\mathbb{Q}]$$ 与 $$[\mathbb{Q}(\sqrt[3]2):\mathbb{Q}]$$。把 (1)(2) 里数出的"映射个数"与这两个次数并排放在一起看，你发现了什么？

**(4)** 【猜测，不要求证明】设 $$L=\mathbb{Q}(\sqrt2,\sqrt3)$$。基于 (1)(3) 的模式，先猜一猜：这样的映射会有几个？$$[L:\mathbb{Q}]$$ 又是多少？猜完之后，试着把候选映射一个个写下来验证你的猜测（不必写出严格证明，能验证"确实保持加法乘法"就够）。

这四问里，(1)(2) 是纯手算，(3) 是复习第 76 章，(4) 是本章真正要培养的直觉——第 78 章会把这个直觉变成一条可以证明的一般定理（定理 3.9）。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 一个具体的"对称"，逐步拆开

先回答入口题 (1)。取 $$L=\mathbb{Q}(\sqrt2)$$。我们要找的映射 $$\sigma:L\to L$$ 要满足三条：(i) 是双射；(ii) $$\sigma(a)=a$$ 对每个有理数 $$a$$；(iii) $$\sigma(x+y)=\sigma(x)+\sigma(y)$$、$$\sigma(xy)=\sigma(x)\sigma(y)$$。

**第一步：$$\sigma$$ 由它在 $$\sqrt2$$ 上的取值唯一决定。** $$L$$ 里每个元素都写成 $$a+b\sqrt2$$（$$a,b\in\mathbb{Q}$$）的形式，于是由 (ii)(iii)：

$$\sigma(a+b\sqrt2)=\sigma(a)+\sigma(b)\sigma(\sqrt2)=a+b\,\sigma(\sqrt2).$$

只要知道 $$\sigma(\sqrt2)$$ 是什么，整个 $$\sigma$$ 就确定了。

**第二步：$$\sigma(\sqrt2)$$ 只能是 $$\pm\sqrt2$$。** 因为 $$\sqrt2\cdot\sqrt2=2$$，两边用 $$\sigma$$：$$\sigma(\sqrt2)^2=\sigma(2)=2$$（第二个等号用 (ii)）。所以 $$\sigma(\sqrt2)$$ 是方程 $$t^2=2$$ 在 $$L$$ 中的解，而 $$L\subseteq\mathbb{R}$$ 中这个方程只有两个解：$$\sqrt2$$ 与 $$-\sqrt2$$。

**第三步：两种取值都确实给出合法的 $$\sigma$$。** 取 $$\sigma(\sqrt2)=\sqrt2$$ 显然给出恒等映射 $$\mathrm{id}$$。取 $$\sigma(\sqrt2)=-\sqrt2$$，定义 $$\sigma(a+b\sqrt2)=a-b\sqrt2$$；直接验证它保持加法（逐项相加即可）与乘法：

$$\sigma\bigl((a+b\sqrt2)(c+d\sqrt2)\bigr)=\sigma\bigl((ac+2bd)+(ad+bc)\sqrt2\bigr)=(ac+2bd)-(ad+bc)\sqrt2,$$

$$\sigma(a+b\sqrt2)\cdot\sigma(c+d\sqrt2)=(a-b\sqrt2)(c-d\sqrt2)=(ac+2bd)-(ad+bc)\sqrt2.$$

两边相等，故 $$\sigma$$ 确实与乘法相容；它显然是双射（自己是自己的逆）。

**结论（入口题 (1) 的答案）**：恰有两个这样的映射，$$\mathrm{id}$$ 与 $$\sigma:\sqrt2\mapsto-\sqrt2$$。

**第四步：这两个映射自动构成一个群。** 复合 $$\sigma\circ\sigma$$：先把 $$\sqrt2$$ 送到 $$-\sqrt2$$，再送到 $$-(-\sqrt2)=\sqrt2$$，故 $$\sigma\circ\sigma=\mathrm{id}$$。于是 $$\{\mathrm{id},\sigma\}$$ 在复合运算下是一个二阶群，同构于 $$\mathbb{Z}/2$$。这不是巧合——两个满足 (i)(ii)(iii) 的映射复合后仍满足 (i)(ii)(iii)（逐条检查：复合仍是双射；仍固定有理数，因为两次都固定；仍与运算相容，因为两次都相容），恒等映射满足这三条，且每个 $$\sigma$$ 的逆映射也满足这三条（因为 $$\sigma$$ 是双射，且 $$\sigma(\sigma^{-1}(a))=a$$ 配合 $$\sigma$$ 固定有理数，可推出 $$\sigma^{-1}$$ 也固定有理数）。**群结构是"对称"这个概念自带的，不是外加的。**

现在可以放心地给这类映射、以及它们的全体，起正式的名字。

**定义 3.1（$$K$$-自同构与 Galois 群）** 设 $$L/K$$ 是域扩张。满足 (i)(ii)(iii) 的映射 $$\sigma:L\to L$$ 称为 $$L$$ 的一个 **$$K$$-自同构**；全体 $$K$$-自同构在复合下构成的群，记作 $$\operatorname{Gal}(L/K)$$，称为 $$L/K$$ 的 **Galois 群**（第 76 章称"伽罗瓦群"，是同一个对象）。

由第一步到第四步，$$\operatorname{Gal}(\mathbb{Q}(\sqrt2)/\mathbb{Q})=\{\mathrm{id},\sigma\}\cong\mathbb{Z}/2$$。

### 3.2 另一个具体例子：对称会"不够用"

再算入口题 (2)。取 $$M=\mathbb{Q}(\sqrt[3]2)\subseteq\mathbb{R}$$。同样的推理：任何 $$\tau\in\operatorname{Gal}(M/\mathbb{Q})$$ 满足 $$\tau(\sqrt[3]2)^3=\tau(2)=2$$，故 $$\tau(\sqrt[3]2)$$ 是方程 $$t^3=2$$ 在 $$M$$ 中的解。

**关键的差别来了**：$$t^3=2$$ 在复数域里有三个解 $$\sqrt[3]2,\ \sqrt[3]2\,\omega,\ \sqrt[3]2\,\omega^2$$（$$\omega=e^{2\pi i/3}$$ 是复数），但 $$M\subseteq\mathbb{R}$$，而后两个解都不是实数（$$\omega\notin\mathbb{R}$$）。所以在 $$M$$ 内，$$t^3=2$$ 只有唯一解 $$\sqrt[3]2$$ 本身：函数 $$t\mapsto t^3-2$$ 在实数上严格递增，不可能有第二个实根。于是 $$\tau(\sqrt[3]2)=\sqrt[3]2$$，而 $$\sqrt[3]2$$ 生成整个 $$M$$，故 $$\tau=\mathrm{id}$$。

**结论（入口题 (2) 的答案）**：$$\operatorname{Gal}(M/\mathbb{Q})=\{\mathrm{id}\}$$，只有一个元素。

由第 76 章，$$t^3-2$$ 由 Eisenstein 判别法（$$p=2$$）不可约，故 $$[M:\mathbb{Q}]=3$$。并排看：

| | 映射个数 $$\lvert\operatorname{Gal}\rvert$$ | 次数 $$[L:\mathbb{Q}]$$ |
|---|---|---|
| $$\mathbb{Q}(\sqrt2)$$ | $$2$$ | $$2$$ |
| $$\mathbb{Q}(\sqrt[3]2)$$ | $$1$$ | $$3$$ |

**这正是入口题 (3)(4) 要你发现的模式**：有时相等，有时严格小于。差别出在哪？$$t^2-2$$ 的两个根 $$\pm\sqrt2$$ **都**在 $$\mathbb{Q}(\sqrt2)$$ 里；而 $$t^3-2$$ 的三个根里，只有一个在 $$\mathbb{Q}(\sqrt[3]2)$$ 里，另外两个"跑到了域外面"，自同构没法把 $$\sqrt[3]2$$ 送到它们那里去（送过去就飞出了 $$M$$，不再是 $$M$$ 到自身的映射）。第 78 章会把"一个根在，则同类根全在"这条件正式命名为**正规性**（定义 3.5），并证明：

$$\lvert\operatorname{Gal}(L/K)\rvert=[L:K]\iff L/K\ \text{正规（且可分，特征 }0\text{ 下可分自动成立）}.$$

本章不证明这条一般定理，但你已经用手算验证了它的两个实例——这就是第 78 章定理 3.9 要交付给你的东西。

### 3.3 固定域：反过来，由群造域

$$\operatorname{Gal}$$ 是"由域造群"。第 78 章还需要反过来的操作："由群造域"。这个记号第一次出现前，先看它在具体例子里长什么样，再问要不要给它起名字。

取 $$L=\mathbb{Q}(\sqrt2)$$，$$H=\{\mathrm{id},\sigma\}=\operatorname{Gal}(L/\mathbb{Q})$$（3.1 节算出的那个群）。问：$$L$$ 中哪些元素被 $$H$$ 的**每一个**元素都固定？

$$\mathrm{id}$$ 固定所有元素，这条不提供信息；真正的约束来自 $$\sigma$$。设 $$x=a+b\sqrt2\in L$$，要求 $$\sigma(x)=x$$，即

$$a-b\sqrt2=a+b\sqrt2\ \Longrightarrow\ -b\sqrt2=b\sqrt2\ \Longrightarrow\ 2b\sqrt2=0\ \Longrightarrow\ b=0.$$

于是被 $$H$$ 固定的元素恰是 $$\{a:a\in\mathbb{Q}\}=\mathbb{Q}$$——**正好等于我们出发的基域** $$K=\mathbb{Q}$$。这不是巧合，而是"用群里的映射能唯一确定基域"的一个具体验证。

**这类"由一族映射反推出被它们共同固定的域"的操作值得起个名字**，因为它马上会在更大的例子里反复用到（见下面 3.4 节的对应表）。

**定义 3.2（固定域）** 设 $$H$$ 是 $$L$$ 的一族自同构。$$H$$ 的**固定域**是

$$L^H=\{x\in L:\ h(x)=x\ \text{对一切}\ h\in H\}.$$

（它确实是 $$L$$ 的子域：若 $$x,y\in L^H$$、$$h\in H$$，则 $$h(x\pm y)=h(x)\pm h(y)=x\pm y$$，$$h(xy)=h(x)h(y)=xy$$，逐条验证域运算封闭。）

上面的手算给出 $$L^{\{\mathrm{id},\sigma\}}=\mathbb{Q}$$，即 $$L^H=K$$。第 78 章的 Galois 对应（定理 3.11）说：在合适条件下，"造群"与"造域"这两个方向**互为逆操作**——这正是我们刚刚在一个最小的例子里亲手验证过的那一半。

### 3.4 为什么两个不同的自同构"够不成"一条关系式

第 78 章证明 $$\lvert\operatorname{Gal}(L/K)\rvert=[L:K]$$ 时，第一块基石是"互异的自同构线性无关"（Dedekind 引理）。这条陈述听起来抽象，但它的核心意思很朴素：**几个不同的映射，不可能靠"加权求和"互相抵消成零函数**。先在能画出图的最小例子里看清楚。

取 $$L=\mathbb{C}$$、$$K=\mathbb{R}$$，两个 $$\mathbb{R}$$-自同构 $$\mathrm{id}$$ 与复共轭 $$c:z\mapsto\bar z$$。问：能否找到不全为零的 $$p,q\in\mathbb{C}$$，使得

$$p\cdot\mathrm{id}(z)+q\cdot c(z)=0\quad\text{对一切}\ z\in\mathbb{C}\ \text{成立？}$$

代入 $$z=1$$：$$p\cdot1+q\cdot1=p+q=0$$。

代入 $$z=i$$：$$p\cdot i+q\cdot(-i)=i(p-q)=0$$，故 $$p=q$$。

两条合起来：$$p+q=0$$ 且 $$p=q$$，代入得 $$2p=0$$，故 $$p=q=0$$。**没有非平凡的关系式。**

这个手算里的机制值得提炼：$$\mathrm{id}$$ 与 $$c$$ 在 $$z=i$$ 处的取值不同（$$i\ne-i$$），仅这一个"不同点"就足够把任何试图让它们抵消的系数逼到 $$0$$——代入两个恰当的点，就把"两个未知系数"用两条线性方程钉死。第 78 章的**引理 3.7（Dedekind 引理）**把这件事一般化到**任意有限多个**互异自同构：结论仍是"唯一让它们线性组合恒为零的方式是所有系数都是零"，证明的机制完全一样（取一个见证两个映射不同的点，代入消去一项，把 $$n$$ 个映射的关系式降到 $$n-1$$ 个，反复做下去）——只是从"两个映射、两个方程"变成"$$n$$ 个映射、需要反复约化"，本质的手法你已经在上面亲手做过一次。

### 3.5 把对应表摆出来，看规律

回到入口题 (4)。取 $$L=\mathbb{Q}(\sqrt2,\sqrt3)$$。仿照 3.1 节的推理：任何 $$\rho\in\operatorname{Gal}(L/\mathbb{Q})$$ 满足 $$\rho(\sqrt2)=\pm\sqrt2$$、$$\rho(\sqrt3)=\pm\sqrt3$$（同样由 $$\rho(\sqrt2)^2=2$$、$$\rho(\sqrt3)^2=3$$），至多 $$2\times2=4$$ 种组合，而四种组合确实都给出合法的自同构（逐条验证保运算的方式与 3.1 节第三步完全一样，此处从略）：

$$\rho_1=\mathrm{id},\quad \rho_2:\sqrt3\mapsto-\sqrt3,\quad \rho_3:\sqrt2\mapsto-\sqrt2,\quad \rho_4:\text{both}\mapsto-.$$

又 $$[L:\mathbb{Q}]=4$$（第 76 章：$$1,\sqrt2,\sqrt3,\sqrt6$$ 线性无关）。故 $$\lvert\operatorname{Gal}(L/\mathbb{Q})\rvert=4=[L:\mathbb{Q}]$$——**入口题 (4) 的猜测在这里得到验证**：与 $$\mathbb{Q}(\sqrt2)$$ 一样"够用"，因为 $$t^2-2$$ 与 $$t^2-3$$ 的全部根都落在 $$L$$ 内。

四个映射复合起来是什么群？逐一验证 $$\rho_2^2=\rho_3^2=\rho_4^2=\mathrm{id}$$（每个都是对合），且两两复合给出第三个非单位元（例如 $$\rho_2\rho_3=\rho_4$$），故 $$\operatorname{Gal}(L/\mathbb{Q})\cong\mathbb{Z}/2\times\mathbb{Z}/2$$。

**现在按 3.3 节的做法，把每个子群的固定域都手算一遍**（方法与 3.3 节逐字相同：设 $$x=a+b\sqrt2+c\sqrt3+d\sqrt6$$，代入子群的每个生成元、令系数相等）：

| 子群 | 固定域 | 次数 |
|---|---|---|
| $$\{\mathrm{id}\}$$ | $$L$$ | $$4$$ |
| $$\langle\rho_2\rangle$$ | $$\mathbb{Q}(\sqrt2)$$ | $$2$$ |
| $$\langle\rho_3\rangle$$ | $$\mathbb{Q}(\sqrt3)$$ | $$2$$ |
| $$\langle\rho_4\rangle$$ | $$\mathbb{Q}(\sqrt6)$$ | $$2$$ |
| $$\{\rho_1,\rho_2,\rho_3,\rho_4\}$$ | $$\mathbb{Q}$$ | $$1$$ |

（验证一行：$$\rho_2$$ 固定 $$\sqrt2$$、翻转 $$\sqrt3$$，故 $$a+b\sqrt2+c\sqrt3+d\sqrt6$$ 被 $$\rho_2$$ 固定要求 $$c=d=0$$，固定域恰是 $$\{a+b\sqrt2\}=\mathbb{Q}(\sqrt2)$$；其余三行同理。）

**看规律**：子群越大，固定域越小；子群越小，固定域越大——两端 $$\{\mathrm{id}\}\leftrightarrow L$$ 与全群 $$\leftrightarrow\mathbb{Q}$$ 互补对齐，中间三个二阶子群对应三个二次子域。子群的阶乘上固定域的次数，永远等于 $$4$$。这张表不是巧合，也不是特例——它是第 78 章 **Galois 对应（定理 3.11）** 的一个完整实例，只是那里会证明"任意有限 Galois 扩张都有这样一张表，而且左右两边的项数总相等"。你现在已经亲手搭出了最简单的那一张。

## 四、几何与物理直觉 (Intuition)

### 4.1 房间里的家具

想象一个完全空的圆形房间：把它绕中心转任意角度，看起来都一样——它有"无穷多"种对称。现在往房间正中间放一张桌子（仍然对称），对称性不变；但如果把桌子挪到偏离中心的位置，大部分旋转都会让房间"看起来不一样"了，只剩下极少数（比如根本不转，即恒等）还保持一致。

**摆一件家具，就是在选一个"中间状态"；对称群则跟着缩小。** 这正是 3.5 节表格里发生的事：$$L=\mathbb{Q}(\sqrt2,\sqrt3)$$ 是"空房间"（对称最多，$$4$$ 个自同构）；选定中间域 $$\mathbb{Q}(\sqrt2)$$，相当于"摆了一件只关心 $$\sqrt3$$ 的家具"——容许的对称立刻从 $$4$$ 个降到 $$2$$ 个（只剩下能动 $$\sqrt3$$、不动 $$\sqrt2$$ 的那些）；选到底层的 $$\mathbb{Q}$$（什么都不摆），对称最大；选到顶层的 $$L$$ 本身（摆满家具，一点空隙都不留），只剩下恒等一种对称。**域越大，允许保留的自由度越小，对称群越小**——这就是第 78 章"序反 (order-reversing)"性质的日常版本。

### 4.2 密码锁的比喻

把 $$\sqrt2$$ 和 $$\sqrt3$$ 想成密码锁上的两个独立拨轮，每个拨轮只有两个位置（正、负）。"自同构"就是"允许拨动这些轮子、但拨完之后锁仍然合法"的动作。两个拨轮互不干扰（拨 $$\sqrt2$$ 那一轮不影响 $$\sqrt3$$ 那一轮，反之亦然），于是总共 $$2\times2=4$$ 种合法拨法，这正是 3.5 节里数出的四个 $$\rho_i$$。而 $$\mathbb{Q}(\sqrt[3]2)$$ 之所以只有 $$1$$ 种拨法，是因为它对应的"另外两个根"（$$\sqrt[3]2\,\omega,\sqrt[3]2\,\omega^2$$）根本不在锁的可拨范围内——锁上没有这两个位置，拨轮自然也就没法转到那里去。第 78 章会把"锁上有没有这个位置"精确定义为**正规性**。

## 五、经典问题精讲 (Classical Problems)

### 题 1（$$\mathbb{Q}(i)$$：最短的一个例子）

**问题**：求 $$\operatorname{Gal}(\mathbb{Q}(i)/\mathbb{Q})$$，并与 $$[\mathbb{Q}(i):\mathbb{Q}]$$ 比较。

**解** 设 $$\tau\in\operatorname{Gal}(\mathbb{Q}(i)/\mathbb{Q})$$。由 $$i^2=-1$$ 得 $$\tau(i)^2=\tau(-1)=-1$$，故 $$\tau(i)=\pm i$$，两种取值都给出合法映射：$$\mathrm{id}$$ 与复共轭 $$c:i\mapsto-i$$（保运算的验证与 3.1 节第三步完全一样）。而 $$t^2+1$$ 不可约（无实根），$$[\mathbb{Q}(i):\mathbb{Q}]=2$$。故

$$\operatorname{Gal}(\mathbb{Q}(i)/\mathbb{Q})=\{\mathrm{id},c\}\cong\mathbb{Z}/2,\qquad \lvert\operatorname{Gal}\rvert=2=[\mathbb{Q}(i):\mathbb{Q}].$$

**这与 $$\mathbb{Q}(\sqrt2)$$ 是同一种情形**：$$t^2+1$$ 的两个根 $$\pm i$$ 都落在 $$\mathbb{Q}(i)$$ 内，"对称够用"。

### 题 2（$$\mathbb{Q}(i,\sqrt2)$$：把两个独立拨轮拼在一起）

**问题**：求 $$\operatorname{Gal}(\mathbb{Q}(i,\sqrt2)/\mathbb{Q})$$，并列出全部子群与对应的固定域。

**解** 记 $$L=\mathbb{Q}(i,\sqrt2)$$。任何 $$\rho\in\operatorname{Gal}(L/\mathbb{Q})$$ 满足 $$\rho(i)=\pm i$$、$$\rho(\sqrt2)=\pm\sqrt2$$（同题 1 与 3.1 节的论证），至多 $$4$$ 种组合。$$[L:\mathbb{Q}]=4$$：因为 $$\mathbb{Q}(\sqrt2)\subseteq\mathbb{R}$$ 而 $$i\notin\mathbb{R}$$，故 $$i\notin\mathbb{Q}(\sqrt2)$$，$$[L:\mathbb{Q}(\sqrt2)]=2$$，塔定理给 $$[L:\mathbb{Q}]=2\times2=4$$。于是四种组合都确实可行，记

$$\rho_1=\mathrm{id},\quad \rho_i:i\mapsto-i,\ \sqrt2\mapsto\sqrt2,\quad \rho_2:i\mapsto i,\ \sqrt2\mapsto-\sqrt2,\quad \rho_{12}=\rho_i\rho_2.$$

与 3.5 节完全同样的计算给出 $$\operatorname{Gal}(L/\mathbb{Q})\cong\mathbb{Z}/2\times\mathbb{Z}/2$$，以及（逐行验证的方法与 3.5 节表格相同，此处从略）：

| 子群 | 固定域 | 次数 |
|---|---|---|
| $$\{\mathrm{id}\}$$ | $$L$$ | $$4$$ |
| $$\langle\rho_i\rangle$$ | $$\mathbb{Q}(\sqrt2)$$ | $$2$$ |
| $$\langle\rho_2\rangle$$ | $$\mathbb{Q}(i)$$ | $$2$$ |
| $$\langle\rho_{12}\rangle$$ | $$\mathbb{Q}(i\sqrt2)=\mathbb{Q}(\sqrt{-2})$$ | $$2$$ |
| 全群 | $$\mathbb{Q}$$ | $$1$$ |

**为什么值得单独做一遍**：$$\mathbb{Q}(i)$$ 与 $$\mathbb{Q}(\sqrt2)$$ 是两个互不相干的二次域（$$\mathbb{Q}(i)\cap\mathbb{Q}(\sqrt2)=\mathbb{Q}$$，因为 $$\mathbb{Q}(\sqrt2)\subseteq\mathbb{R}$$ 不含 $$i$$），它们的 Galois 群"拼"成了乘积群 $$\mathbb{Z}/2\times\mathbb{Z}/2$$——与 3.5 节的 $$\mathbb{Q}(\sqrt2,\sqrt3)$$ 逐字同构。第 78 章会把这条"拼接"规律写成一般定理（定理 3.12：Galois 群与域的合成），到时候你不需要再重新数一遍自同构，直接用两个小群的乘积就知道答案。

### 题 3（判别式初探：$$t^3-2$$ 的一个数字）

**问题**：设 $$f(t)=t^3-2$$，三个根为 $$\alpha_1,\alpha_2,\alpha_3\in\mathbb{C}$$（$$\alpha_1=\sqrt[3]2$$，$$\alpha_2=\sqrt[3]2\,\omega$$，$$\alpha_3=\sqrt[3]2\,\omega^2$$，$$\omega=e^{2\pi i/3}$$）。计算 $$\Delta=\prod_{i<j}(\alpha_i-\alpha_j)^2$$，并判断它是不是有理数中的平方。

**解** 对形如 $$t^3+pt+q$$ 的三次式，判别式有现成公式 $$\Delta=-4p^3-27q^2$$（把三个根的差之积直接展开可以验证这个公式，此处先承认它，第 78 章定理 3.13 会给出不依赖公式、直接从根的置换出发的证明）。这里 $$f=t^3-2$$，即 $$p=0,q=-2$$：

$$\Delta=-4\cdot0^3-27\cdot(-2)^2=-27\times4=-108.$$

$$-108$$ 是负数，不可能是任何实数（更不用说有理数）的平方。

**这个数字在第 78 章会被派上大用场**（题 2、例 3.13）：$$\Delta$$ 是否为 $$\mathbb{Q}$$ 中的平方，将被证明恰好决定 $$\operatorname{Gal}(f)$$ 是坐落在 $$S_3$$ 里还是坐落在它的一半——偶置换构成的子群 $$A_3$$ 里。这里你只需要记住一个具体的数字：**$$-108$$，非平方**。

### 题 4（两个二次域为什么不会"重叠"）

**问题**：证明 $$\mathbb{Q}(\sqrt2)\cap\mathbb{Q}(\sqrt3)=\mathbb{Q}$$。

**解** 交集显然包含 $$\mathbb{Q}$$。反过来，交集的次数同时整除 $$[\mathbb{Q}(\sqrt2):\mathbb{Q}]=2$$ 与 $$[\mathbb{Q}(\sqrt3):\mathbb{Q}]=2$$（交集是两者的公共子域），故只能是 $$1$$ 或 $$2$$。若是 $$2$$，则交集本身是一个二次域，同时含于 $$\mathbb{Q}(\sqrt2)$$ 与 $$\mathbb{Q}(\sqrt3)$$，于是 $$\sqrt3\in\mathbb{Q}(\sqrt2)$$。写 $$\sqrt3=p+q\sqrt2$$（$$p,q\in\mathbb{Q}$$），两边平方：

$$3=p^2+2q^2+2pq\sqrt2.$$

因 $$\sqrt2\notin\mathbb{Q}$$，必须 $$pq=0$$。若 $$q=0$$ 则 $$p^2=3$$，无有理解；若 $$p=0$$ 则 $$2q^2=3$$，同样无有理解。两种情形都矛盾，故交集次数只能是 $$1$$，即 $$\mathbb{Q}(\sqrt2)\cap\mathbb{Q}(\sqrt3)=\mathbb{Q}$$。

**这条"不重叠"是 3.5 节里 $$4=2\times2$$ 能对上的根本原因**：正是因为两个二次域除了 $$\mathbb{Q}$$ 之外再没有公共部分，它们的自同构才能"各自独立地"拼成 $$2\times2=4$$ 个，而不会因为重叠而少算或重复。第 78 章定理 3.12 会把"两个 Galois 扩张的交恰是基域时，Galois 群是两者的直积"写成一般定理——这里你已经亲手验证了它成立的前提条件。

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 把 $$\operatorname{Gal}(\mathbb{Q}(\sqrt3)/\mathbb{Q})$$ 的全部元素写出来，并算 $$\lvert\operatorname{Gal}\rvert$$ 与 $$[\mathbb{Q}(\sqrt3):\mathbb{Q}]$$。

**基2.** 把 $$\operatorname{Gal}(\mathbb{Q}(\sqrt[3]3)/\mathbb{Q})$$ 的全部元素写出来（$$\mathbb{Q}(\sqrt[3]3)\subseteq\mathbb{R}$$），并算 $$\lvert\operatorname{Gal}\rvert$$ 与 $$[\mathbb{Q}(\sqrt[3]3):\mathbb{Q}]$$。

**基3.** 在 $$L=\mathbb{Q}(\sqrt2,\sqrt3)$$ 中，设 $$\rho_4:\sqrt2\mapsto-\sqrt2,\ \sqrt3\mapsto-\sqrt3$$（3.5 节表格里的第四个非单位元）。直接算出固定域 $$L^{\langle\rho_4\rangle}$$，并验证它就是表格里写的 $$\mathbb{Q}(\sqrt6)$$。

### 竞赛（本课目标难度）

**竞1.** 设 $$L=\mathbb{Q}(i,\sqrt5)$$。求 $$\operatorname{Gal}(L/\mathbb{Q})$$（作为抽象群），并列出全部子群与对应的固定域（仿 3.5 节 / 题 2 的表格）。

**竞2.** 在 $$L=\mathbb{Q}(\sqrt2,\sqrt3)$$ 上取三个自同构 $$\mathrm{id},\rho_2,\rho_3$$（$$\rho_2:\sqrt3\mapsto-\sqrt3$$，$$\rho_3:\sqrt2\mapsto-\sqrt2$$，符号同 3.5 节）。证明：若 $$a\cdot\mathrm{id}(x)+b\cdot\rho_2(x)+c\cdot\rho_3(x)=0$$ 对一切 $$x\in L$$ 成立（$$a,b,c\in L$$），则 $$a=b=c=0$$。

**竞3.** 设 $$f(t)=t^3-7t+7$$。用 $$\Delta=-4p^3-27q^2$$ 算出它的判别式，判断是不是 $$\mathbb{Q}$$ 中的平方，并与题 3（$$t^3-2$$）的结果对比。

### 研究（通向下一章）

**研1.** 回顾 3.2 节的表格（$$\mathbb{Q}(\sqrt2)$$：$$2=2$$；$$\mathbb{Q}(\sqrt[3]2)$$：$$1<3$$）与 3.5 节、题 1、题 2 的例子。用你自己的话写一条猜想：**$$\lvert\operatorname{Gal}(L/\mathbb{Q})\rvert=[L:\mathbb{Q}]$$ 到底在什么条件下成立？**（提示：想想每个例子里，"生成元的极小多项式的全部根"是不是都落在 $$L$$ 里面。不要求证明，只要求把条件说准确。）

**研2.** 设 $$M=\mathbb{Q}(\sqrt[3]2)$$（3.2 节算出 $$\lvert\operatorname{Gal}(M/\mathbb{Q})\rvert=1<3=[M:\mathbb{Q}]$$）。试构造一个更大的域 $$M'\supseteq M$$（仍是 $$\mathbb{Q}$$ 上有限扩张），使得 $$t^3-2$$ 的三个根都落在 $$M'$$ 里。算出 $$[M':\mathbb{Q}]$$，并猜一猜这一次 $$\lvert\operatorname{Gal}(M'/\mathbb{Q})\rvert$$ 会不会追上 $$[M':\mathbb{Q}]$$。

### 解答 (Solutions)

**解 基1.** 任何 $$\sigma\in\operatorname{Gal}(\mathbb{Q}(\sqrt3)/\mathbb{Q})$$ 满足 $$\sigma(\sqrt3)^2=\sigma(3)=3$$，故 $$\sigma(\sqrt3)=\pm\sqrt3$$；两种取值都给出合法自同构（验证方式与 3.1 节第三步逐字相同）：$$\mathrm{id}$$ 与 $$\tau:\sqrt3\mapsto-\sqrt3$$。$$t^2-3$$ 无有理根故不可约，$$[\mathbb{Q}(\sqrt3):\mathbb{Q}]=2$$。故

$$\operatorname{Gal}(\mathbb{Q}(\sqrt3)/\mathbb{Q})=\{\mathrm{id},\tau\}\cong\mathbb{Z}/2,\qquad \lvert\operatorname{Gal}\rvert=2=[\mathbb{Q}(\sqrt3):\mathbb{Q}].$$

**解 基2.** 任何 $$\sigma\in\operatorname{Gal}(\mathbb{Q}(\sqrt[3]3)/\mathbb{Q})$$ 满足 $$\sigma(\sqrt[3]3)^3=3$$，故 $$\sigma(\sqrt[3]3)$$ 是 $$t^3-3$$ 在 $$\mathbb{Q}(\sqrt[3]3)\subseteq\mathbb{R}$$ 中的根。函数 $$t\mapsto t^3-3$$ 在 $$\mathbb{R}$$ 上严格递增，只有唯一实根 $$\sqrt[3]3$$，故 $$\sigma(\sqrt[3]3)=\sqrt[3]3$$，从而 $$\sigma=\mathrm{id}$$（$$\sqrt[3]3$$ 生成整个域）。由 Eisenstein（$$p=3$$）$$t^3-3$$ 不可约，$$[\mathbb{Q}(\sqrt[3]3):\mathbb{Q}]=3$$。故

$$\operatorname{Gal}(\mathbb{Q}(\sqrt[3]3)/\mathbb{Q})=\{\mathrm{id}\},\qquad \lvert\operatorname{Gal}\rvert=1<3=[\mathbb{Q}(\sqrt[3]3):\mathbb{Q}].$$

**解 基3.** 设 $$x=a+b\sqrt2+c\sqrt3+d\sqrt6\in L$$（$$a,b,c,d\in\mathbb{Q}$$）。$$\rho_4$$ 把 $$\sqrt2,\sqrt3$$ 都变号，而 $$\sqrt6=\sqrt2\cdot\sqrt3$$ 的符号不变（两个负号相乘抵消）：

$$\rho_4(x)=a-b\sqrt2-c\sqrt3+d\sqrt6.$$

要求 $$\rho_4(x)=x$$，即 $$-b\sqrt2-c\sqrt3=b\sqrt2+c\sqrt3$$，由 $$1,\sqrt2,\sqrt3,\sqrt6$$ 线性无关（第 76 章）得 $$b=c=0$$。于是 $$L^{\langle\rho_4\rangle}=\{a+d\sqrt6:a,d\in\mathbb{Q}\}=\mathbb{Q}(\sqrt6)$$，与表格一致。

**解 竞1.** 任何 $$\rho\in\operatorname{Gal}(L/\mathbb{Q})$$（$$L=\mathbb{Q}(i,\sqrt5)$$）满足 $$\rho(i)=\pm i$$、$$\rho(\sqrt5)=\pm\sqrt5$$（同题 1、基 1 的论证），至多 $$4$$ 种。因 $$\mathbb{Q}(\sqrt5)\subseteq\mathbb{R}$$ 不含 $$i$$，$$[L:\mathbb{Q}(\sqrt5)]=2$$，塔定理给 $$[L:\mathbb{Q}]=4$$，故 $$4$$ 种组合都确实可行：

$$\rho_1=\mathrm{id},\quad \rho_i:i\mapsto-i,\sqrt5\mapsto\sqrt5,\quad \rho_5:i\mapsto i,\sqrt5\mapsto-\sqrt5,\quad \rho_{i5}=\rho_i\rho_5.$$

每个非单位元都满足平方为 $$\mathrm{id}$$，群交换，故 $$\operatorname{Gal}(L/\mathbb{Q})\cong\mathbb{Z}/2\times\mathbb{Z}/2$$。固定域表（方法与题 2 完全相同）：

| 子群 | 固定域 | 次数 |
|---|---|---|
| $$\{\mathrm{id}\}$$ | $$L$$ | $$4$$ |
| $$\langle\rho_i\rangle$$ | $$\mathbb{Q}(\sqrt5)$$ | $$2$$ |
| $$\langle\rho_5\rangle$$ | $$\mathbb{Q}(i)$$ | $$2$$ |
| $$\langle\rho_{i5}\rangle$$ | $$\mathbb{Q}(i\sqrt5)=\mathbb{Q}(\sqrt{-5})$$ | $$2$$ |
| 全群 | $$\mathbb{Q}$$ | $$1$$ |

**解 竞2.** 代入 $$x=1$$：三个自同构都固定 $$1$$，得 $$a+b+c=0$$。

代入 $$x=\sqrt2$$：$$\mathrm{id}(\sqrt2)=\sqrt2$$，$$\rho_2(\sqrt2)=\sqrt2$$（$$\rho_2$$ 只翻转 $$\sqrt3$$），$$\rho_3(\sqrt2)=-\sqrt2$$，得 $$a\sqrt2+b\sqrt2-c\sqrt2=0$$，即 $$a+b-c=0$$。

代入 $$x=\sqrt3$$：$$\mathrm{id}(\sqrt3)=\sqrt3$$，$$\rho_2(\sqrt3)=-\sqrt3$$，$$\rho_3(\sqrt3)=\sqrt3$$，得 $$a\sqrt3-b\sqrt3+c\sqrt3=0$$，即 $$a-b+c=0$$。

三个方程联立：$$a+b+c=0$$，$$a+b-c=0$$，$$a-b+c=0$$。前两式相减得 $$2c=0\Rightarrow c=0$$；代回第一式得 $$a+b=0$$；第三式（$$c=0$$）给 $$a-b=0\Rightarrow a=b$$；与 $$a+b=0$$ 合并得 $$a=b=0$$。故 $$a=b=c=0$$——三个互异自同构之间不存在非平凡线性关系，与 3.4 节的两自同构情形是同一机制的下一步（第 78 章引理 3.7 把它推广到任意有限多个）。

**解 竞3.** $$p=-7,q=7$$：

$$\Delta=-4(-7)^3-27\cdot7^2=-4\times(-343)-27\times49=1372-1323=49=7^2.$$

$$49$$ 是完全平方数，即 $$\Delta$$ 是 $$\mathbb{Q}$$ 中的平方。**对比**：题 3 中 $$t^3-2$$ 给出 $$\Delta=-108$$（负数，非平方）；这里 $$t^3-7t+7$$ 给出 $$\Delta=49$$（平方）。第 78 章定理 3.13 会证明：这个差别恰好对应 Galois 群是坐落在 $$S_3$$ 里（非平方的情形）还是坐落在更小的 $$A_3$$ 里（平方的情形）——同一条公式、两个数字，就能提前分辨两类完全不同的对称结构。

**解 研1.** 观察三组数据：$$\mathbb{Q}(\sqrt2)$$（$$t^2-2$$ 的两个根 $$\pm\sqrt2$$ 都在域内，$$2=2$$）；$$\mathbb{Q}(i)$$（$$t^2+1$$ 的两个根 $$\pm i$$ 都在域内，$$2=2$$）；$$\mathbb{Q}(\sqrt2,\sqrt3)$$（$$t^2-2$$、$$t^2-3$$ 的全部根都在域内，$$4=4$$）；$$\mathbb{Q}(\sqrt[3]2)$$（$$t^3-2$$ 的另两个根不在域内，$$1<3$$）。

**猜想**：$$\lvert\operatorname{Gal}(L/\mathbb{Q})\rvert=[L:\mathbb{Q}]$$ 成立，当且仅当对 $$L$$ 的每个生成元 $$\alpha$$，它的极小多项式的**全部**根都落在 $$L$$ 内部（不只是 $$\alpha$$ 自己这一个根）；一旦有某个生成元的"同类根"漏在 $$L$$ 外面，等号就会变成严格小于号。（这正是第 78 章定义 3.5"正规扩张"的手感版本：第 78 章会证明，这个条件配合"根不重复"（可分性，特征 $$0$$ 下自动成立），恰好等价于 $$\lvert\operatorname{Gal}(L/K)\rvert=[L:K]$$，见定理 3.9。）

**解 研2.** 取 $$M'=\mathbb{Q}(\sqrt[3]2,\omega)$$，$$\omega=e^{2\pi i/3}$$（$$t^2+t+1$$ 的根，即 $$t^3-2$$ 另外两个根 $$\sqrt[3]2\,\omega,\sqrt[3]2\,\omega^2$$ 都可以由 $$\sqrt[3]2$$ 与 $$\omega$$ 乘出来）。$$[\mathbb{Q}(\sqrt[3]2):\mathbb{Q}]=3$$（基 2 / 3.2 节）；$$\omega\notin\mathbb{Q}(\sqrt[3]2)$$（后者 $$\subseteq\mathbb{R}$$ 而 $$\omega$$ 非实），且 $$\omega$$ 满足二次方程 $$t^2+t+1=0$$，故 $$[M':\mathbb{Q}(\sqrt[3]2)]=2$$，塔定理给

$$[M':\mathbb{Q}]=3\times2=6.$$

**猜测**：这一次 $$t^3-2$$ 的三个根 $$\sqrt[3]2,\sqrt[3]2\,\omega,\sqrt[3]2\,\omega^2$$ 全都落在 $$M'$$ 里了（"同类根一个不漏"），按研 1 的猜想，这次对称应该"够用"，即 $$\lvert\operatorname{Gal}(M'/\mathbb{Q})\rvert$$ 应该追上 $$[M':\mathbb{Q}]=6$$。第 78 章题 2 会把这个猜测严格算一遍：那里证明 $$\operatorname{Gal}(M'/\mathbb{Q})\cong S_3$$，恰好 $$6$$ 个元素。

## 七、Takeaway 与延伸 (Takeaways)

**Takeaway 1（对称是可以数出来的）** $$\operatorname{Gal}(L/K)$$ 不是一个模糊的"对称性"概念，而是一个可以逐一列出元素、逐一验证保运算的具体有限群——3.1、3.5 节里你已经亲手数过两次。

**Takeaway 2（对称个数 $$\le$$ 次数，何时取等看"根在不在家"）** $$\lvert\operatorname{Gal}(L/K)\rvert$$ 永远不超过 $$[L:K]$$；取等的条件，从手算的例子里已经能猜出雏形（研 1）：生成元的极小多项式的全部根都要留在域内。第 78 章会把这条猜想升格为定理 3.9，并给它起正式的名字——正规性。

**Takeaway 3（固定域是"由群造域"的具体操作）** $$L^H$$ 不是凭空的记号：它就是"代入、令系数相等、解方程"这几步手算的结果（3.3 节、基 3）。第 78 章会证明"造群"与"造域"这两个方向互为逆操作，而你已经在最小的例子里亲眼验证过。

**Takeaway 4（对应表不是巧合）** 3.5 节与题 2 里的两张表——子群越大固定域越小、阶数与次数处处互补——会在第 78 章被证明对**任意**有限 Galois 扩张都成立，这就是 Galois 对应（定理 3.11）。

**Takeaway 5（线性无关是全部证明的地基）** 3.4 节、竞 2 里"几个不同自同构凑不出非平凡关系式"这件事，看似是一条孤立的小观察，第 78 章的 Artin 引理、Galois 扩张的等价刻画（定理 3.9）全都建立在它之上。

**交棒**：现在你已经能手算出 $$\operatorname{Gal}(L/K)$$ 的具体元素、固定域、以及完整的对应表，也已经从数据里猜出了"正规性"该长什么样，还亲手验证过两个二次域"不重叠"是拼接公式成立的前提。下一章（第 78 章）不会引入任何你没见过的新对象——它只是把这些你已经算过的东西，写成一般的定义，并证明它们对任意有限 Galois 扩张都成立。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch76_扩域与代数数_下.md">← 第76章 扩域与代数数·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch78_Galois群与Galois对应_下.md">第78章 Galois 群与 Galois 对应·下 →</a></div>
</div>
