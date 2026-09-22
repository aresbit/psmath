---
layout: default
---

# 第67章: 单子、Abel 范畴与正合·上：预备与直觉 (Monads, Abelian Categories and Exactness · Part I: Warm-up and Intuition)

> 配套深化: 见 第68章 单子、Abel 范畴与正合·下（完整推导），本章是它的具体铺垫，建议先读本章
> 专家依据: `_experts/algebra/category-universal-properties.md` + `_experts/algebra/homological-algebra.md`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

第68章一上来就要证明五件"看起来只要两三行"的事：核自动是单态射（靠"存在唯一"这四个字）、直和同时是积又是余积（靠一个矩阵拼接公式）、像与余像其实是同一个对象（靠两条公理）、蛇引理里连接同态的构造（靠三步追图）、以及"单子不过是自函子范畴里的一个幺半群"这句听起来很吓人的话。每一处都只花两三行翻篇，但每一行背后都压着好几次具体的代数运算——这正是读者反馈里说的"跳步"。

本章的任务只有一个：在看到那些一般证明之前，先把这五件事在**具体的、能摆在纸上验算的对象**上——$$\mathbb R^2$$ 里的两个矩阵、$$\mathbb Z$$ 上的同态、一个三元素集合的幂集——**各手算一遍**。算完你会发现，第68章那几行证明，字字句句都只是把你刚刚做过的事换成了符号；读到蛇引理与单子时，你手上已经有一组具体数字可以对照。

## 二、入口：一道具体的问题 (Entry Problem)

> 题源：第68章入口题的预热版，数字更小、只要求算，不要求证。

设 $$\mathcal H=\mathbb R^2$$，取两个矩阵
$$P_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad P_2=\begin{pmatrix}0&0\\0&1\end{pmatrix}.$$

**(1)** 直接算：验证 $$P_1^2=P_1$$、$$P_2^2=P_2$$（这样的矩阵叫**投影**：作用两次和作用一次结果一样）；再算出乘积 $$P_2P_1$$ 具体是什么矩阵。

**(2)** $$P_1$$ 的像（所有形如 $$P_1v$$ 的向量组成的集合）是哪一条直线？$$P_2$$ 的核（所有满足 $$P_2v=0$$ 的 $$v$$ 组成的集合）是哪一条直线？把两者相比，你发现什么？

**(3)** 换到 $$\mathbb R^3$$，取
$$Q_1=\begin{pmatrix}1&0&0\\0&0&0\\0&0&0\end{pmatrix},\qquad Q_2=\begin{pmatrix}0&0&0\\0&1&0\\0&0&0\end{pmatrix}.$$
重复 (1)(2) 的计算：$$Q_2Q_1$$ 是什么矩阵？$$Q_1$$ 的像是哪条直线？$$Q_2$$ 的核是一条直线还是一个平面？把 $$Q_1$$ 的像与 $$Q_2$$ 的核相比——这次你发现了什么不一样的地方？"多出来的部分"用一个具体向量描述是什么？

**(4)** 只凭 (2)(3) 的计算猜一猜（不必证）：一般地，"$$P_1$$ 的像恰好等于 $$P_2$$ 的核"是不是每次都自动发生？如果不是，"多出来的部分"的维数，能不能用 $$P_1,P_2$$ 像的维数写出一个公式？

这道题不要求你证明任何东西，只要求把矩阵乘出来、把像与核认出来。(2) 里"完全吻合"、(3) 里"有剩余"，正是第68章要给出一般定义和证明的两种情形；第三节会把这两次具体计算变成一般定义。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 核与余核：为什么"存在唯一"能自动保证单态射

先把入口题 (2) 的计算写成一般语言。设 $$f:V\to W$$ 是向量空间之间的线性映射。

**定义 3.1（核与余核，具体版）** $$f$$ 的**核 (kernel)** 是 $$\ker f:=\{v\in V:f(v)=0\}$$，配合含入映射 $$k:\ker f\hookrightarrow V$$；$$f$$ 的**余核 (cokernel)** 是商空间 $$\operatorname{coker}f:=W/\operatorname{im}f$$，配合商映射 $$\pi:W\to W/\operatorname{im}f$$。

**例 3.1** 取入口题里的 $$P_2:\mathbb R^2\to\mathbb R^2$$。由 $$P_2(x,y)=(0,y)$$，$$\ker P_2=\{(x,0):x\in\mathbb R\}$$（$$x$$ 轴）；$$\operatorname{im}P_2=\{(0,y)\}$$（$$y$$ 轴），故 $$\operatorname{coker}P_2=\mathbb R^2/\{(0,y)\}\cong\mathbb R$$（用 $$x$$ 坐标做代表元）。

现在手算 $$k:\ker P_2\hookrightarrow\mathbb R^2$$ 的**万有性质**：任取满足 $$P_2\circ u=0$$ 的线性映射 $$u:X\to\mathbb R^2$$，比如 $$X=\mathbb R$$、$$u(t)=(3t,0)$$（验证 $$P_2u(t)=P_2(3t,0)=(0,0)$$ ✓）。$$u$$ 的像落在 $$x$$ 轴里，于是存在唯一的 $$\bar u:X\to\ker P_2$$（就是把 $$u$$ 看成到 $$x$$ 轴自身的映射 $$\bar u(t)=3t$$）使 $$k\circ\bar u=u$$。"唯一"是因为 $$\bar u(t)$$ 只能取 $$u(t)$$ 的第一个坐标，没有第二种取法。

**定理 3.2（核是单射；"存在唯一"具体地做了什么）** 设 $$u,v:X\to\ker P_2$$ 满足 $$k\circ u=k\circ v$$（作为 $$X\to\mathbb R^2$$ 的映射相等）。则 $$u=v$$。

*证明*：把 $$u,v$$ 都看成到 $$x$$ 轴的数值函数。$$k\circ u=k\circ v$$ 这句话逐坐标写出来，就是"把 $$u(t)$$ 放进第一个坐标、第二个坐标补零"与"把 $$v(t)$$ 放进第一个坐标、第二个坐标补零"给出同一个 $$\mathbb R^2$$ 里的点，即 $$(u(t),0)=(v(t),0)$$，故 $$u(t)=v(t)$$ 对一切 $$t$$ 成立，即 $$u=v$$。$$\blacksquare$$

**注 3.1（这条证明在一般范畴里怎么变得不平凡）** 上面的证明看起来像废话，是因为在 $$\mathbf{Vect}_{\mathbb R}$$ 里我们能直接摸到"元素"，$$k$$ 的单射性肉眼可见。第68章定理 3.3 要在**任意**范畴里证明同一件事——那里没有元素可摸，唯一能用的是核的万有性质本身。诀窍是：把 $$u,v$$ 都塞进**同一条**"存在唯一"的性质里——记 $$h:=k\circ u=k\circ v$$，则 $$u,v$$ 都是满足 $$k\circ\bar h=h$$ 的候选 $$\bar h$$，"唯一"这个词就把两个候选**逼成同一个**，即 $$u=v$$。这正是刚才 $$k$$ 的单射性在做的事，只是换了一套不需要元素的语言。记住这句翻译，第68章几乎所有"某态射是单/满"的证明都用它：**万有性质里的"唯一"＝没有元素语言时的单射性。**

### 3.2 直和为什么既是积又是余积

**定义 3.3（直和的两种角色）** 先取最简单的情形 $$V=W=\mathbb R$$。直和 $$V\oplus W=\mathbb R^2$$ 自带四个映射：投影 $$p_V(x,y):=x$$、$$p_W(x,y):=y$$；含入 $$i_V(x):=(x,0)$$、$$i_W(y):=(0,y)$$。

**例 3.2** 直接验证两件事。(i) 任给一对映射 $$a:X\to\mathbb R$$、$$b:X\to\mathbb R$$，存在唯一的 $$(a,b):X\to\mathbb R^2$$ 使 $$p_V\circ(a,b)=a$$、$$p_W\circ(a,b)=b$$——这是"**积**"的万有性质，"唯一"是因为一对坐标函数只能拼出一个映射。(ii) 任给一对映射 $$c:\mathbb R\to Y$$、$$d:\mathbb R\to Y$$，存在唯一的映射 $$\mathbb R^2\to Y$$，即 $$(x,y)\mapsto c(x)+d(y)$$，使它复合 $$i_V,i_W$$ 分别还原出 $$c,d$$——这是"**余积**"的万有性质。同一个 $$\mathbb R^2$$ 两次担任了不同的角色。

**定理 3.4（两条万有性质给出同一个对象，具体验证）** 令
$$\varphi:=\begin{pmatrix}1&0\\0&1\end{pmatrix}\quad(\text{恒同矩阵}),\qquad \psi:=i_Vp_V+i_Wp_W .$$
算 $$\psi$$ 的矩阵：$$i_Vp_V$$ 是 $$(x,y)\mapsto x\mapsto(x,0)$$，矩阵 $$\begin{pmatrix}1&0\\0&0\end{pmatrix}$$；$$i_Wp_W$$ 是 $$(x,y)\mapsto y\mapsto(0,y)$$，矩阵 $$\begin{pmatrix}0&0\\0&1\end{pmatrix}$$——这正是入口题里的 $$P_1,P_2$$！于是
$$\psi=P_1+P_2=\begin{pmatrix}1&0\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&1\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}=\varphi ,$$
两个矩阵都是单位矩阵，故 $$\varphi\psi=\psi\varphi=I$$：积角色与余积角色由同一个恒同映射互相还原。

**注 3.2** 这个计算不是巧合：**入口题里 $$P_1+P_2=I$$，就是"直和的积角色与余积角色重合"这件事的矩阵版本。** 第68章定理 3.6 要在一般加性范畴里重做这个验证，用的是完全一样的公式 $$\psi=i_Ap_A+i_Bp_B$$——只是那里的 $$A,B$$ 不一定摸得到元素，加号来自"态射集是 Abel 群"这条公理（定义 3.4/3.5），不是坐标相加。在 $$\mathbf{Set}$$ 里这个加号根本写不出来（两个函数不能相加），这正是 $$\mathbf{Set}$$ 里积 $$\{*\}\times\{*\}$$（一个点）与余积 $$\{*\}\sqcup\{*\}$$（两个点）不同构的根源——留作竞1。

### 3.3 像与余像：一个具体的映射

**定义 3.5（像与余像，具体版）** 对线性映射 $$u:V\to W$$，**像**是 $$\operatorname{im}u:=u(V)\subseteq W$$；**余像**是 $$\operatorname{coim}u:=V/\ker u$$。

**例 3.3** 取 $$u:\mathbb R^3\to\mathbb R^2$$，$$u(x,y,z):=(x+y,\,x+y)$$。算：$$\ker u=\{(x,y,z):x+y=0\}$$，是 $$\mathbb R^3$$ 里的一个 2 维平面；$$\operatorname{coim}u=\mathbb R^3/\ker u$$ 是 1 维的（唯一"活下来"的坐标是 $$s:=x+y$$）；$$\operatorname{im}u=\{(t,t):t\in\mathbb R\}\subset\mathbb R^2$$，也是 1 维（对角线）。两个 1 维空间之间的**典范映射** $$\bar u:\operatorname{coim}u\to\operatorname{im}u$$ 由 $$\bar u(s):=(s,s)$$ 给出：单射（$$\bar u(s)=0\Rightarrow s=0$$）、满射（对角线上任一点 $$(t,t)$$ 都等于 $$\bar u(t)$$），故 $$\operatorname{coim}u\cong\operatorname{im}u$$——尽管它们的定义（一个是商、一个是子空间）看起来毫不相干。

**定理 3.6（余像与像总是同构，一般情形）** 对任意线性映射 $$u:V\to W$$，典范映射 $$\bar u:\operatorname{coim}u\to\operatorname{im}u$$，$$\bar u(v+\ker u):=u(v)$$，总是良定义的双射。

*证明*：良定义：若 $$v+\ker u=v'+\ker u$$ 则 $$v-v'\in\ker u$$，故 $$u(v)=u(v')$$。单射：$$\bar u(v+\ker u)=0\Rightarrow u(v)=0\Rightarrow v\in\ker u\Rightarrow v+\ker u=0$$。满射：$$\operatorname{im}u=u(V)$$ 本身就是 $$\bar u$$ 的像。$$\blacksquare$$

**注 3.3** 例 3.3、定理 3.6 在 $$\mathbf{Vect}$$、$$\mathbf{Ab}$$ 里几乎是重言式——我们能直接摸到元素，"良定义、单、满"一眼可验。第68章定理 3.9 要在一般阿贝尔范畴里重证同一件事，那时 $$\operatorname{Im}u$$、$$\operatorname{Coim}u$$ 分别**被定义成**核与余核的复合（$$\operatorname{Im}u:=\ker(\operatorname{coker}u)$$，$$\operatorname{Coim}u:=\operatorname{coker}(\ker u)$$），"它们同构"不再是显然事实，要靠两条公理（(A2)(A3)）才能证明——这两条公理翻译成 $$\mathbf{Vect}$$ 的语言，正是"子空间可以用商的核描述、商空间可以用子空间的余核描述"这件我们在具体空间里习以为常、从不多想的事。

### 3.4 正合列：一个手算的短正合列 + 幂集预告

**定义 3.7（在中间处正合，具体版）** 序列 $$A\xrightarrow{f}B\xrightarrow{g}C$$（线性映射）称在 $$B$$ 处**正合 (exact)**，若 $$\operatorname{im}f=\ker g$$（作为 $$B$$ 的子空间相等）。

**例 3.4** 取 $$0\to\mathbb R\xrightarrow{f}\mathbb R^2\xrightarrow{g}\mathbb R\to0$$，$$f(t):=(t,t)$$，$$g(x,y):=x-y$$。算：$$\operatorname{im}f=\{(t,t)\}$$（对角线）；$$\ker g=\{(x,y):x=y\}$$（也是对角线）。两者相等，序列在 $$\mathbb R^2$$ 处正合；且 $$f$$ 单射（$$f(t)=0\Rightarrow t=0$$）、$$g$$ 满射（$$g(c,0)=c$$）。这正是入口题 (2) "完全吻合"那种情形的一般版本：$$B$$ 里被 $$g$$ 杀掉的部分，恰好等于被 $$f$$ 造出来的部分，序列不漏信息也不多信息。

若改用 $$f'(t):=(t,0)$$（其余不变）呢？$$\operatorname{im}f'=\{(t,0)\}$$（$$x$$ 轴），$$\ker g=\{(x,y):x=y\}$$（对角线），两者不相等——序列在 $$\mathbb R^2$$ 处**不**正合，"多出来"的部分是商 $$\ker g/\operatorname{im}f'$$，可算出是 1 维的（用 $$(1,1)$$ 的类代表）。这正是入口题 (3) "有剩余"那种情形的一般版本；这个剩余量在第68章会被叫作**同调**。

**例 3.5（预告：单子的"打包"与"摊平"，幂集上手算一遍）** 取三元素集合 $$S=\{1,2,3\}$$，$$\mathcal P(X)$$ 记 $$X$$ 的幂集。定义两个操作：$$\eta_S:S\to\mathcal P(S)$$，$$\eta_S(1):=\{1\}$$（把元素"打包"成单点集）；$$\mu_S:\mathcal P(\mathcal P(S))\to\mathcal P(S)$$，把"一堆子集组成的集合"**摊平**成这些子集的并。

手算一次"摊平"：取 $$\mathcal U:=\bigl\{\{1,2\},\{2,3\}\bigr\}\in\mathcal P(\mathcal P(S))$$，则 $$\mu_S(\mathcal U)=\{1,2\}\cup\{2,3\}=\{1,2,3\}$$。再手算一次"打包再摊平"：取 $$A=\{1,3\}\subseteq S$$，先把 $$A$$ 的每个元素打包（记这一步为 $$\mathcal P(\eta_S)$$），得到 $$\{\{1\},\{3\}\}$$；再摊平：$$\mu_S\bigl(\{\{1\},\{3\}\}\bigr)=\{1\}\cup\{3\}=\{1,3\}=A$$——打包、摊平，原地不动。

这两个操作——"打包"（$$\eta$$）与"摊平"（$$\mu$$）——就是第68章定义 3.18 里单子的两个部件，那里会补上抽象记号和两条一致性条件；现在你已经在一个三元素集合上用手验证过它们各自在做什么。

## 四、几何与物理直觉 (Intuition)

**核与余核：筛子。** 把 $$f:V\to W$$ 想成一把筛子：$$\ker f$$ 是"筛不掉、原地不动就等于零"的那部分——从筛子背面看，这些输入什么都没留下。$$\operatorname{coker}f=W/\operatorname{im}f$$ 是反过来看：筛子筛出来的东西（$$\operatorname{im}f$$）只占了 $$W$$ 的一部分，剩下**没被筛出来的空隙**就是余核。入口题里 $$P_2$$ 把 $$xy$$ 平面压扁到 $$y$$ 轴，"压扁前后没变化"的输入正是 $$x$$ 轴（核）。

**直和：两个独立抽屉合成一个柜子。** $$V\oplus W$$ 既能"拆开看"（积：给我一个柜子，我能分别读出两个抽屉的内容，对应 $$p_V,p_W$$），又能"拼起来放"（余积：分别往两个抽屉塞东西，柜子就自动装好了，对应 $$i_V,i_W$$）。定理 3.4 说的是：**只要能把两个抽屉的内容相加**（这是"加性"的全部意义），"拆开看"与"拼起来放"就是同一个柜子的两种用法，不需要区分。

**像与余像：从两头看同一个漏斗。** 把 $$u:V\to W$$ 想成一个漏斗。从上往下看，"真正流出来的东西"是像 $$\operatorname{im}u$$；从下往上看，"把入口按流出结果分类、忽略掉哪些输入会混成同一滴水"给出的分类方式是余像 $$\operatorname{coim}u$$。两种看法描述的是同一个漏斗，理应给出同一个东西——这正是定理 3.6 要说的话，只是"理应"两个字在一般范畴里要靠公理去证。

**正合列：一条没有漏水也没有凭空多水的管道。** $$A\to B\to C$$ 在 $$B$$ 处正合，说的是：从 $$A$$ 灌进来的水（$$\operatorname{im}f$$），恰好填满了会被 $$C$$ 那一头"卡住"的部分（$$\ker g$$）——不多不少。第五节的蛇引理要做的事，是当**两条**这样的管道叠在一起、又用竖直的阀门（$$a,b,c$$）连接时，追踪"一滴水从上面漏到下面"最终会流到哪里；这正是"连接同态"这个名字的字面意思。

**单子：打包与拆封。** 网购时，商品先被装进一个包裹（$$\eta$$：打包）；如果你收到的是"包裹里还有包裹"（比如合并订单），拆开外层后你要把里面所有包裹的东西倒进同一个购物袋——这就是 $$\mu$$：摊平。第68章会说：**只要你在别处见过一对"自由生成 / 遗忘"这样的搭档**（先尽量自由地打包、再靠一个规则拆封），你就自动得到一个单子——它不是额外发明出来的结构，是这种"打包-拆封"模式本身的名字。

## 五、经典问题精讲 (Classical Problems)

**问题 5.1（手算一次连接同态：乘 3 的追图）**
**考点**：追图的四个动作——取原像、往下推、找原像、落进商——先在数字上做一遍。**位置**：为第68章定理 3.15（蛇引理）打地基。

考虑行正合、方块交换的图（两行都是"乘 3 再取模 3"的短正合列）：
$$\begin{array}{ccccccc}
\mathbb Z & \xrightarrow{\ \times3\ } & \mathbb Z & \xrightarrow{\ \bmod3\ } & \mathbb Z/3 & \xrightarrow{\ \ }\ & 0\\[4pt]
{\scriptstyle\times3}\big\downarrow & & {\scriptstyle\times3}\big\downarrow & & {\scriptstyle0}\big\downarrow & & \\[4pt]
0 & \xrightarrow{\ \ }\ & \mathbb Z & \xrightarrow{\ \times3\ } & \mathbb Z & \xrightarrow{\ \bmod3\ } & \mathbb Z/3
\end{array}$$
算出六个对象：$$\operatorname{Ker}(\times3)=0$$（两处）；$$\operatorname{Ker}(0:\mathbb Z/3\to\mathbb Z/3)=\mathbb Z/3$$；$$\operatorname{Coker}(\times3)=\mathbb Z/3$$（两处）；$$\operatorname{Coker}(0)=\mathbb Z/3$$。再对生成元 $$x=1\in\mathbb Z/3$$ 手算"连接同态" $$\delta(1)$$ 的值。

**解**：六个对象已算出，六项序列的形状是 $$0\to0\to\mathbb Z/3\xrightarrow{\delta}\mathbb Z/3\to\mathbb Z/3\to\mathbb Z/3$$。计算 $$\delta(1)$$，一步步来：
① **取原像**：$$x=1\in\mathbb Z/3$$ 是上排右下角箭头（$$\bmod3$$）的像，取原像 $$y=1\in\mathbb Z$$（$$1\bmod3=1$$）。
② **往下推**：沿竖直箭头 $$\times3$$ 把 $$y=1$$ 送到下一层：$$3\cdot1=3\in\mathbb Z$$（这是下排中间的 $$\mathbb Z$$）。因为下排左边的 $$\times3:\mathbb Z\to\mathbb Z$$ 是满到 $$3\mathbb Z$$ 的（下排在此处正合），找它的原像：$$z\in\mathbb Z$$ 使 $$3z=3$$，得 $$z=1$$。
③ **落进商**：$$\delta(1):=z+\operatorname{Im}(\times3)=1+3\mathbb Z\in\mathbb Z/3=\operatorname{Coker}(a)$$，即 $$\delta(1)=1$$。
生成元被送到生成元，$$\delta$$ 是同构。**这与第68章竞3 里 $$n=2$$ 的情形是同一个模式**：乘 $$n$$ 的对角图给出的连接同态，总是"生成元到生成元"的同构——第68章会证明这不是巧合，而是短正合列 $$0\to\mathbb Z\xrightarrow{\times n}\mathbb Z\to\mathbb Z/n\to0$$ 自我复合时的必然结果。$$\blacksquare$$

**问题 5.2（入口题的收口：$$P_1+P_2=I$$ 给出一个分裂的短正合列）**
**考点**：短正合列不一定"分裂"（即能拆成直和），但入口题里的例子恰好分裂——找出那个让它分裂的映射。**位置**：为第68章问题 5.3（分裂引理）打地基。

回到入口题 (1)(2) 的 $$P_1,P_2$$（$$P_1+P_2=I$$，$$P_2P_1=0$$）。考虑序列
$$0\to\operatorname{im}P_1\xrightarrow{\ \iota\ }\mathbb R^2\xrightarrow{\ P_2\ }\operatorname{im}P_2\to0 ,$$
其中 $$\iota$$ 是含入映射。证明它正合，并找出一个映射 $$s:\operatorname{im}P_2\to\mathbb R^2$$ 使 $$P_2\circ s=1_{\operatorname{im}P_2}$$（这样的 $$s$$ 称**截面**）。

**解**：**正合性**：$$\operatorname{im}P_1=x\text{ 轴}$$，这正是 $$\iota$$ 的像；$$\ker P_2=x\text{ 轴}$$（例 3.1 已算）；两者相等，序列在 $$\mathbb R^2$$ 处正合。$$\iota$$ 单射显然；$$P_2$$ 限制在陪域 $$\operatorname{im}P_2=y$$ 轴上是满射（任给 $$(0,c)$$，$$P_2(0,c)=(0,c)$$）。
**找截面**：令 $$s:\operatorname{im}P_2\to\mathbb R^2$$ 为含入映射本身，即 $$s(0,c):=(0,c)$$。验证 $$P_2\circ s(0,c)=P_2(0,c)=(0,c)$$ ✓，故 $$P_2\circ s=1_{\operatorname{im}P_2}$$。
**这为什么值得注意**：截面的存在等价于 $$\mathbb R^2$$ 能写成 $$\operatorname{im}P_1\oplus\operatorname{im}P_2$$——这正是矩阵等式 $$P_1+P_2=I$$ 的几何含义（3.2 节注 3.2）。第68章问题 5.3 要证明的是**一般情形**：任何短正合列，只要能找到一个截面（或对称地一个"收缩"），中间对象就必是两端的直和；但**不是所有短正合列都有截面**（比如 $$0\to\mathbb Z\xrightarrow{\times2}\mathbb Z\to\mathbb Z/2\to0$$ 就没有——否则 $$\mathbb Z\cong\mathbb Z\oplus\mathbb Z/2$$ 会有挠元，矛盾）。入口题的例子之所以"自动"分裂，是因为两个投影本身就带着一个现成的截面。$$\blacksquare$$

**问题 5.3（手算一次单子的结合律）**
**考点**：把"打包再摊平两次，顺序不同结果一样"这条结合律在具体集合上算一遍。**位置**：为第68章定理 3.18 的结合律、竞4 打地基。

沿用例 3.5 的 $$S=\{1,2,3\}$$。取 $$\mathcal V:=\bigl\{\{\{1\},\{2\}\},\ \{\{2,3\}\}\bigr\}\in\mathcal P\bigl(\mathcal P(\mathcal P(S))\bigr)$$（$$\mathcal V$$ 有两个元素：$$U_1=\{\{1\},\{2\}\}$$ 与 $$U_2=\{\{2,3\}\}$$，各自是 $$\mathcal P(\mathcal P(S))$$ 里的元素）。分别按"先摊平里层、再摊平外层"与"先摊平外层、再摊平内层"两种顺序算出 $$\mathcal V$$ 的"三层摊平"结果，验证两者相等。

**解**：**顺序一（先对每个 $$U_i$$ 摊平，再摊平结果）**：
$$\mu(U_1)=\{1\}\cup\{2\}=\{1,2\},\qquad \mu(U_2)=\{2,3\} .$$
把 $$\mathcal V$$ 里的每一项换成摊平结果，得到 $$\{\{1,2\},\{2,3\}\}\in\mathcal P(\mathcal P(S))$$，再摊平一次：
$$\{1,2\}\cup\{2,3\}=\{1,2,3\}.$$
**顺序二（先把 $$\mathcal V$$ 本身看成 $$\mathcal P(S)$$ 上的一族子集、直接取并，再摊平一次）**：
$$\bigcup\mathcal V=U_1\cup U_2=\{\{1\},\{2\}\}\cup\{\{2,3\}\}=\{\{1\},\{2\},\{2,3\}\}\in\mathcal P(\mathcal P(S)),$$
再摊平：
$$\{1\}\cup\{2\}\cup\{2,3\}=\{1,2,3\}.$$
两种顺序都得到 $$\{1,2,3\}$$，相等。**这就是结合律 $$\mu\circ\mathcal P\mu=\mu\circ\mu\mathcal P$$ 在具体三元素集合上的样子**："先展开内层括号再展开外层"与"先合并外层括号再展开"给出同一个并集——这不奇怪，因为两种顺序算的本来就是同一堆元素 $$\{1,2,3\}$$ 的并，只是**分组方式不同**，而"取并"这个操作根本不在乎分组。第68章竞4 要证的就是这句话对**任意** $$S$$、**任意** $$\mathcal U\in\mathcal P^3(S)$$ 都成立，证明手法与这里逐字一致，只是把具体的 $$U_1,U_2$$ 换成抽象的记号。$$\blacksquare$$

## 六、练习 (Exercises)
### 基础（巩固定义）

**基1.** 取 $$f:\mathbb R^2\to\mathbb R^3$$，$$f(x,y):=(x,y,0)$$。求 $$\ker f$$ 与 $$\operatorname{coker}f$$（连同它们的代表元描述）；再取 $$v:\mathbb R^3\to\mathbb R$$，$$v(x,y,z):=z$$，验证 $$v$$ 满足 $$v\circ f=0$$ 并写出它穿过 $$\operatorname{coker}f$$ 的那个唯一映射。

**基2.** 在 $$\mathbb R^3$$ 中取 $$R_1=\begin{pmatrix}0&0&0\\0&1&0\\0&0&0\end{pmatrix}$$（投影到 $$y$$ 轴）、$$R_2=\begin{pmatrix}0&0&0\\0&0&0\\0&0&1\end{pmatrix}$$（投影到 $$z$$ 轴）。算 $$R_2R_1$$、$$\ker R_2$$、$$\operatorname{im}R_1$$，并算出 $$H:=\ker R_2/\operatorname{im}R_1$$ 的维数。

**基3.** 把定理 3.4 的验证搬到 $$\mathbb R^3=\mathbb R^2\oplus\mathbb R$$（前两个坐标记一组、第三个坐标记另一组）：写出 $$p_V,p_W,i_V,i_W$$ 的矩阵，算出 $$\varphi,\psi$$ 的 $$3\times3$$ 矩阵，验证 $$\varphi\psi=\psi\varphi=I_3$$。

### 竞赛（本课目标难度）

**竞1.** 取 $$u:\mathbb R^3\to\mathbb R^3$$，$$u(x,y,z):=(x+y,\,x+y,\,z)$$。求 $$\ker u$$、$$\operatorname{coim}u$$、$$\operatorname{im}u$$（各给出维数与一组代表元），写出典范映射 $$\bar u:\operatorname{coim}u\to\operatorname{im}u$$ 的具体公式，并验证它是双射。

**竞2.** 取 $$f:\mathbb Z\to\mathbb Z^2$$，$$f(n):=(n,3n)$$；$$g:\mathbb Z^2\to\mathbb Z$$，$$g(a,b):=b-3a$$。证明 $$0\to\mathbb Z\xrightarrow{f}\mathbb Z^2\xrightarrow{g}\mathbb Z\to0$$ 正合，并写出 $$\operatorname{coker}f\xrightarrow{\ \sim\ }\mathbb Z$$ 这个同构具体是怎么由 $$g$$ 给出的。

**竞3.** 沿用例 3.5 的 $$S=\{1,2,3\}$$，取 $$A=\{2,3\}\subseteq S$$。分别验证单位律的两条：(i) $$\mu_S\bigl(\mathcal P(\eta_S)(A)\bigr)=A$$；(ii) $$\mu_S\bigl(\eta_{\mathcal P(S)}(A)\bigr)=A$$（这里 $$\eta_{\mathcal P(S)}(A)=\{A\}\in\mathcal P(\mathcal P(S))$$）。说明这两条为什么都值得叫"单位律"——它们分别对应哪种"什么都没做"。

### 研究（通向下一章）

**研1.** 设 $$P_1,P_2\in\operatorname{End}(\mathbb R^n)$$ 是两个投影（$$P_i^2=P_i$$，不必正交），只假设 $$P_2P_1=0$$。
(i) 说明为什么 $$P_2P_1=0$$ 自动保证 $$\operatorname{im}P_1\subseteq\ker P_2$$，从而 $$H:=\ker P_2/\operatorname{im}P_1$$ 总有意义。
(ii) 猜一个只用 $$n$$、$$\dim\operatorname{im}P_1$$、$$\dim\operatorname{im}P_2$$ 表达 $$\dim H$$ 的公式，并在入口题的 $$P_1,P_2$$（$$n=2$$）、$$Q_1,Q_2$$（$$n=3$$）、基2 的 $$R_1,R_2$$（$$n=3$$）三个例子上验证。
(iii) 用秩-零化度定理证明这个公式对任意满足 $$\operatorname{im}P_1\subseteq\ker P_2$$ 的线性映射 $$P_1,P_2$$（不必是投影）都成立。

**研2.** 考虑与问题 5.1 相同的两行（都是"乘 3 再取模 3"的短正合列），但把竖直映射换成 $$a=b=\times2$$（$$\mathbb Z\to\mathbb Z$$ 乘以 2），$$c$$ 取为 $$\mathbb Z/3\to\mathbb Z/3$$ 上"乘以 2"诱导的映射。
(i) 验证两个方块交换。
(ii) 算出六个对象 $$\operatorname{Ker}a,\operatorname{Ker}b,\operatorname{Ker}c,\operatorname{Coker}a,\operatorname{Coker}b,\operatorname{Coker}c$$。
(iii) 不做任何进一步计算，只凭 (ii) 的结果，说明连接同态 $$\delta$$ 必然是什么映射（提示：$$\delta$$ 的定义域是哪个对象）；再直接验证 $$\operatorname{Coker}a\to\operatorname{Coker}b$$ 确实是同构。

### 解答 (Solutions)

**解 基1.** $$f$$ 单射（$$f(x,y)=0\Rightarrow x=y=0$$），故 $$\ker f=\{(0,0)\}=0$$。$$\operatorname{im}f=\{(x,y,0):x,y\in\mathbb R\}$$ 是 $$xy$$ 平面，故 $$\operatorname{coker}f=\mathbb R^3/(xy\text{ 平面})\cong\mathbb R$$，用 $$z$$ 坐标做代表元（即 $$(x,y,z)$$ 的类只由 $$z$$ 决定）。验证 $$v\circ f=0$$：$$v(f(x,y))=v(x,y,0)=0$$ ✓。$$v$$ 穿过 $$\operatorname{coker}f$$ 的唯一映射就是 $$\bar v:\operatorname{coker}f\to\mathbb R$$，$$\bar v(z\text{ 的类}):=z$$——这就是 $$v$$ 本身在 $$z$$ 坐标上的取值，"唯一"是因为 $$v$$ 在 $$xy$$ 平面上取零，能读出的信息只剩 $$z$$。

**解 基2.** $$R_2R_1$$：先算 $$R_1(x,y,z)=(0,y,0)$$，再 $$R_2(0,y,0)=(0,0,0)$$，故 $$R_2R_1=0$$（零矩阵）。$$\ker R_2=\{(x,y,0):x,y\in\mathbb R\}$$（$$xy$$ 平面，2 维）。$$\operatorname{im}R_1=\{(0,y,0)\}$$（$$y$$ 轴，1 维），且 $$\operatorname{im}R_1\subset\ker R_2$$（$$y$$ 轴确实躺在 $$xy$$ 平面里）。故 $$H=\ker R_2/\operatorname{im}R_1$$ 维数为 $$2-1=1$$（用 $$x$$ 坐标做代表元）。

**解 基3.** 把 $$\mathbb R^3$$ 的坐标记 $$(x,y,z)$$，$$V:=\mathbb R^2$$（前两坐标）、$$W:=\mathbb R$$（第三坐标）。$$p_V(x,y,z)=(x,y)$$、$$p_W(x,y,z)=z$$；$$i_V(x,y)=(x,y,0)$$、$$i_W(z)=(0,0,z)$$。矩阵：
$$p_V=\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix},\quad p_W=\begin{pmatrix}0&0&1\end{pmatrix},\quad i_V=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix},\quad i_W=\begin{pmatrix}0\\0\\1\end{pmatrix}.$$
$$\varphi:=I_3$$（恒同）。$$\psi:=i_Vp_V+i_Wp_W$$：$$i_Vp_V=\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}$$，$$i_Wp_W=\begin{pmatrix}0&0&0\\0&0&0\\0&0&1\end{pmatrix}$$，相加得 $$\psi=I_3$$。故 $$\varphi\psi=\psi\varphi=I_3$$，两个矩阵都是恒同，积角色与余积角色由同一个恒同映射互相还原。$$\blacksquare$$

**解 竞1.** $$\ker u=\{(x,y,z):x+y=0,\ z=0\}=\{(t,-t,0):t\in\mathbb R\}$$，1 维，由 $$(1,-1,0)$$ 张成。$$\operatorname{coim}u=\mathbb R^3/\ker u$$，2 维，坐标可取 $$(s,z)$$，其中 $$s:=x+y$$（$$z$$ 本身已在商中保留，因为 $$\ker u$$ 不改变 $$z$$）。$$\operatorname{im}u=\{(t,t,z):t,z\in\mathbb R\}$$，2 维，由 $$(1,1,0)$$ 与 $$(0,0,1)$$ 张成。典范映射 $$\bar u(s,z):=(s,s,z)$$。验证双射：单射（$$\bar u(s,z)=0\Rightarrow s=0,z=0$$）；满射（$$\operatorname{im}u$$ 中任一点 $$(t,t,z)$$ 都等于 $$\bar u(t,z)$$）。$$\blacksquare$$

**解 竞2.** **正合性**：$$f$$ 单射（$$f(n)=0\Rightarrow n=0$$）。$$\operatorname{im}f=\{(n,3n):n\in\mathbb Z\}$$。$$\ker g=\{(a,b):b-3a=0\}=\{(a,3a):a\in\mathbb Z\}=\operatorname{im}f$$，两者相等，故在中间处正合。$$g$$ 满射：给定 $$c\in\mathbb Z$$，取 $$(a,b)=(0,c)$$，则 $$g(0,c)=c-0=c$$ ✓。于是 $$0\to\mathbb Z\to\mathbb Z^2\to\mathbb Z\to0$$ 正合。
**同构 $$\operatorname{coker}f\cong\mathbb Z$$**：由满-单分解（或直接验证），$$g$$ 在 $$\ker g=\operatorname{im}f$$ 上取零，故 $$g$$ 唯一地下降为 $$\bar g:\mathbb Z^2/\operatorname{im}f\to\mathbb Z$$，$$\bar g\bigl((a,b)+\operatorname{im}f\bigr):=g(a,b)=b-3a$$。这是良定义的（若 $$(a,b)-(a',b')\in\operatorname{im}f$$，则差形如 $$(n,3n)$$，$$g$$ 在其上取零，故 $$g(a,b)=g(a',b')$$）；它就是本题给出的 $$\operatorname{coker}f\xrightarrow{\sim}\mathbb Z$$，且是同构，因为 $$g$$ 本身满、且核恰是要商掉的 $$\operatorname{im}f$$（第68章定理 3.11(iii) 的具体版本）。$$\blacksquare$$

**解 竞3.** (i) $$\mathcal P(\eta_S)(A)$$ 把 $$A=\{2,3\}$$ 的每个元素打包：$$\{\eta_S(2),\eta_S(3)\}=\{\{2\},\{3\}\}$$。摊平：$$\mu_S\bigl(\{\{2\},\{3\}\}\bigr)=\{2\}\cup\{3\}=\{2,3\}=A$$ ✓。
(ii) $$\eta_{\mathcal P(S)}(A)=\{A\}=\{\{2,3\}\}$$（把 $$A$$ 这个"点"打包成单点集，这里的"点"本身就是子集 $$\{2,3\}$$）。摊平：$$\mu_S\bigl(\{\{2,3\}\}\bigr)=\{2,3\}=A$$ ✓。
**两条单位律的区别**：(i) 说的是"先把 $$A$$ 里每个**元素**各自打包、再摊平，等于什么都没做"——打包发生在 $$S$$ 这一层；(ii) 说的是"把整个 $$A$$（已经是 $$\mathcal P(S)$$ 里的一个点）打包成一个单点集、再摊平，也等于什么都没做"——打包发生在 $$\mathcal P(S)$$ 这一层。两条律分别保证"从里面打包"与"从外面打包"都不会制造出多余的信息，这正是第68章定义 3.18 里 $$\mu\circ T\eta=1_T=\mu\circ\eta T$$ 两个等式的由来（$$T\eta$$ 对应 (i)，$$\eta T$$ 对应 (ii)）。$$\blacksquare$$

**解 研1.** (i) 对任意 $$v\in\operatorname{im}P_1$$，写 $$v=P_1w$$，则 $$P_2v=P_2P_1w=0$$（用了假设 $$P_2P_1=0$$），故 $$v\in\ker P_2$$。于是 $$\operatorname{im}P_1\subseteq\ker P_2$$ 自动成立，商 $$H$$ 总有意义，不需要额外验证。
(ii) 猜测：$$\dim H=n-\dim\operatorname{im}P_1-\dim\operatorname{im}P_2$$。验证：入口题 $$P_1,P_2$$（$$n=2$$）：$$\dim\operatorname{im}P_1=\dim\operatorname{im}P_2=1$$，公式给 $$2-1-1=0$$，与例 3.1 算出的 $$H=0$$ 一致。$$Q_1,Q_2$$（$$n=3$$）：同样各 1 维，公式给 $$3-1-1=1$$，与入口题 (3) 算出的"1 维剩余"一致。基2 的 $$R_1,R_2$$（$$n=3$$）：各 1 维，公式给 $$3-1-1=1$$，与解基2 算出的 $$\dim H=1$$ 一致。三例全部吻合。
(iii) 一般证明：$$P_2$$ 是线性映射 $$\mathbb R^n\to\mathbb R^n$$，由秩-零化度定理，$$\dim\ker P_2=n-\dim\operatorname{im}P_2$$（这一步不需要 $$P_2$$ 是投影，对任意线性映射都成立）。又 $$\operatorname{im}P_1\subseteq\ker P_2$$（由 (i)），故
$$\dim H=\dim(\ker P_2/\operatorname{im}P_1)=\dim\ker P_2-\dim\operatorname{im}P_1=\bigl(n-\dim\operatorname{im}P_2\bigr)-\dim\operatorname{im}P_1 ,$$
即 $$\dim H=n-\dim\operatorname{im}P_1-\dim\operatorname{im}P_2$$，与 (ii) 猜测一致，且证明全程只用了 $$\operatorname{im}P_1\subseteq\ker P_2$$，不需要正交性、也不需要 $$P_1,P_2$$ 是投影。$$\blacksquare$$

**解 研2.** (i) **左方块**：需验证 $$b\circ(\times3)=(\times3)\circ a$$，即对一切 $$x$$，$$2\cdot(3x)=3\cdot(2x)$$，即 $$6x=6x$$ ✓。**右方块**：需验证 $$c\circ(\bmod3)=(\bmod3)\circ b$$，即对一切 $$x$$，$$c(x\bmod3)=(2x)\bmod3$$——而 $$c$$ 被定义为"乘以 2 诱导的映射"，即 $$c(x\bmod3):=(2x)\bmod3$$，两边逐字相等，方块交换。
(ii) $$\operatorname{Ker}a=\operatorname{Ker}(\times2:\mathbb Z\to\mathbb Z)=0$$（$$\mathbb Z$$ 无挠）；同理 $$\operatorname{Ker}b=0$$。$$c$$ 是 $$\mathbb Z/3$$ 上乘以 2 的映射：因为 $$\gcd(2,3)=1$$，$$2$$ 在 $$\mathbb Z/3$$ 中可逆（$$2\times2=4\equiv1$$），故 $$c$$ 是双射，$$\operatorname{Ker}c=0$$。$$\operatorname{Coker}a=\mathbb Z/2\mathbb Z$$（乘 2 的余核总是 $$\mathbb Z/2$$）；同理 $$\operatorname{Coker}b=\mathbb Z/2\mathbb Z$$。$$c$$ 双射，故 $$\operatorname{Coker}c=0$$。
(iii) 六项序列的形状是 $$0\to0\to0\xrightarrow{\delta}\mathbb Z/2\to\mathbb Z/2\to0$$（把 (ii) 的六个对象代入定理 3.15 的六项序列）。$$\delta$$ 的**定义域**是 $$\operatorname{Ker}c=0$$——一个只有一个元素的对象，从 $$0$$ 出发的映射只能是零映射，不需要计算构造过程中的任何一步就能断定 $$\delta=0$$。于是六项序列在 $$\operatorname{Coker}a$$ 处正合（$$\operatorname{im}\delta=0=\ker(\operatorname{Coker}a\to\operatorname{Coker}b)$$）意味着 $$\operatorname{Coker}a\to\operatorname{Coker}b$$ **单射**；而序列在最后一项之前又正合到 $$0$$（$$\operatorname{Coker}b\to\operatorname{Coker}c=0$$ 处，$$\operatorname{im}=\ker(\to0)=\operatorname{Coker}b$$ 整体），迫使 $$\operatorname{Coker}b\to\operatorname{Coker}c$$ 是零映射，但这不直接给满射性；改用六项序列本身首尾皆为 $$0$$ 这一事实：中间那三项 $$0\to\mathbb Z/2\to\mathbb Z/2\to0$$ 单独就是一个短正合列（两端是 $$0$$），故 $$\operatorname{Coker}a\to\operatorname{Coker}b$$ 既单又满，是同构。直接验证：这个映射由下排的 $$f'=\times3:\mathbb Z\to\mathbb Z$$ 诱导到 $$\mathbb Z/2$$ 上，即 $$\overline{f'}(x\bmod2):=3x\bmod2=x\bmod2$$（$$3$$ 是奇数），也就是恒同映射——确实是同构。**这个例子的教训**：连接同态是不是零映射，往往不需要算它的构造式，只需要看它的定义域或陪域是不是零对象；第68章的蛇引理会把这条"零对象逼出零映射"的推理常态化。$$\blacksquare$$


## 七、Takeaway 与延伸 (Takeaways)

**1. "存在唯一"这四个字，是把元素语言翻译成范畴语言的关键。** 核是单态射、余核是满态射，本质上都是把两个候选态射塞进同一条万有性质、靠"唯一"把它们逼成同一个（定理 3.2 & 注 3.1）。以后见到"由万有性质，唯一地存在……"这种句子，先问自己：这里的"唯一"消灭的是哪两个候选。

**2. 加性结构把"拆开看"与"拼起来放"合并成同一个对象。** 只要态射能相加，直和 $$V\oplus W$$ 的积角色与余积角色就能用矩阵公式 $$\psi=i_Vp_V+i_Wp_W$$ 互相还原（定理 3.4）；这条公式在一般加性范畴里逐字成立，只是"加号"不再是坐标相加，而是态射集上的群运算。

**3. 像与余像"应该相等"，但这件事需要证明，不是定义。** 在具体的向量空间里，从子空间看（像）与从商空间看（余像）描述的是同一个东西，肉眼可见（定理 3.6）；第68章要在没有元素的一般范畴里重新证明这件事，靠的是两条专门写出来的公理，而不是直觉。

**4. 正合是"没有信息被多杀"，连接同态是追一滴水从上层管道漏到下层的过程。** 问题 5.1 手算出的连接同态，把一个具体的整数追踪到另一个具体的整数；第68章的蛇引理只是把这个手算过程写成了对任意阿贝尔范畴都成立的构造与证明。

**5. 单子的"打包"与"摊平"不是凭空冒出来的记号，而是"自由生成再折叠回去"这个模式本身的名字。** 幂集的并、自由 Abel 群的线性组合展开、张量代数的拼接，都是同一件事的不同外衣；第68章会说：**只要你见过一对"自由 / 遗忘"式的搭档，你就自动拥有一个单子**。

**交棒**：现在你已经能在 $$\mathbb R^2$$、$$\mathbb R^3$$ 与三元素集合上，手算出核、双积、像与余像、短正合列、连接同态与单子的单位/结合律。第68章会把这些手算过的例子逐条搬进一般的阿贝尔范畴与自函子范畴，证明它们对任意对象、任意维数都成立，并进一步引出蛇引理给出的长正合列——这正是同调代数真正开始发力的地方。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch66_伴随函子与Yoneda引理_下.md">← 第66章 伴随函子与Yoneda 引理·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch68_单子_Abel范畴与正合_下.md">第68章 单子、Abel 范畴与正合·下 →</a></div>
</div>
