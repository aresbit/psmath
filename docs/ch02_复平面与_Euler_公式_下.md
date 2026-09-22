---
layout: default
---

# 第02章: 复平面与 Euler 公式·下：完整推导 (The Complex Plane and Euler's Formula · Part II: Full Derivation)

> 专家依据: analysis-master（`_experts/analysis/complex-analysis.md` §1；方法论见 `_experts/analysis/_SKILL.md`）
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）
> 配套预备: 见 第01章 复平面与 Euler 公式·上（同一主题的具体铺垫，建议先读）

## 一、本章概要 (Overview)

读完第01章的具体例子后（你已经用手算过"转30°再转60°等于转90°""$$(1,2)\cdot(3,-1)=(5,5)$$""$$i^2=-1$$""模相乘幅角相加"这四件事），这里把同样的构造写成一般定义、给出对任意角度与任意复数都成立的完整证明。

这一章只解决一个问题：**复数的乘法到底是什么？**

标准教材把三样东西当定义塞给你：虚数单位 $$i=\sqrt{-1}$$、乘法法则 $$(a+ib)(c+id)=(ac-bd)+i(ad+bc)$$、Euler 公式 $$e^{i\theta}=\cos\theta+i\sin\theta$$。然后就在一堆计算里往前推。本章反过来做——**从"平面旋转"这个几何事实出发，把乘法结构推出来，再推出 Euler 公式**。三条"定义"最后会显形为同一件事的三张脸。

这件事给全书定下主线：

$$\text{平面旋转群 } SO(2)\ \longleftrightarrow\ \text{复数乘法的代数}\ \longleftrightarrow\ \text{指数映射 } \theta\mapsto e^{i\theta}.$$

**从哪来**：从中学的复数（解方程的副产品）与实平面向量出发；这是全书的第 02 章，起点是中学数学。
**到哪去**：第 04 章会问一个本章回避掉的问题——把旋转写成矩阵之后，它有没有"特征方向"？答案会把我们逼出复特征值，逼出 $$SO(2)$$ 的**谱 (spectrum)**。这条线一路长到 Lie 群与表示论。

## 二、入口：一道具体的问题 (Entry Problem)

**先给题，不给定义。** 下面两个小问是一件事的两面。

### 问题 (a)：三个正三角形（来源：Квант 常见的几何题，亦是奥赛几何训练题）

在平面上任取一个三角形 $$ABC$$。以它的三条边 $$AB$$、$$BC$$、$$CA$$ 为边，分别向形外作正三角形，共得三个正三角形。记这三个正三角形的中心（重心）依次为 $$C_1,C_2,C_3$$（$$C_1$$ 对应边 $$AB$$，依此类推）。

证明：$$C_1C_2C_3$$ 本身也是正三角形。

用综合几何去做这道题要绕不少弯（要连辅助线、要证全等、要处理三种形状的三角形）。本章后面你会看到，用复数写下来只要三行——而且三行里没有一处需要看图。

### 问题 (b)：反过来的追问

在 (a) 的复数解法里，我们必然要用到这样一个操作：**"把一条线段绕它的端点转过 $$60^\circ$$"**。现在把这个操作本身当成研究对象来问：

> 平面上"绕原点旋转 $$\theta$$ 角"这个几何操作，能不能等价于"乘上某个固定的对象"？也就是说，是否存在一个东西 $$X(\theta)$$，使得对平面上任意点 $$z$$ 都有
> $$\text{旋转 }\theta\text{ 后的点}=X(\theta)\cdot z,$$
> 并且复合规则成立：$$X(\alpha)X(\beta)=X(\alpha+\beta)$$（先转 $$\alpha$$ 再转 $$\beta$$，等于一次转过 $$\alpha+\beta$$）？
>
> **(b1)** 如果存在，它的坐标表达式是什么？
> **(b2)** 转过 $$90^\circ$$ 时那个对象是什么？把它和自己相乘，得到什么？

(b2) 的答案会让你看清一件事：中学课本里那个来历不明的 $$i^2=-1$$，不是谁拍脑袋立的规定，而是**旋转 $$90^\circ$$ 的必然结果**。而 (b) 的完整答案，就是 Euler 公式。

现在开始建结构。

## 三、结构：定义与完整推导 (Structure & Proof)

### 3.1 平面旋转与旋转群 SO(2)

先把几何对象立住。

**定义 3.1（绕原点的旋转）** 设 $$\theta\in\mathbb{R}$$。线性映射 $$R(\theta):\mathbb{R}^2\to\mathbb{R}^2$$ 把每一点绕原点逆时针转过 $$\theta$$，称为**旋转 (rotation)**。

因为它是线性映射，只需要知道它对一组基的作用。取标准基 $$\mathbf{e}_1=(1,0),\ \mathbf{e}_2=(0,1)$$。按角的定义（从正 $$x$$ 轴逆时针量角），

$$R(\theta)\mathbf{e}_1=(\cos\theta,\ \sin\theta),\qquad R(\theta)\mathbf{e}_2=(-\sin\theta,\ \cos\theta).$$

把这两列拼起来，得到 $$R(\theta)$$ 的矩阵：

$$R(\theta)=\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}.$$

**定理 3.1（旋转的复合）** 对任意 $$\alpha,\beta\in\mathbb{R}$$，

$$R(\alpha)R(\beta)=R(\alpha+\beta).$$

**证明思路**：把左边按矩阵乘法硬算，得到的矩阵再用三角函数的和角公式收拾，正好是 $$R(\alpha+\beta)$$。关键点是**和角公式在这里不是被引用的，而是被验证的**——它就是旋转复合的代数影子。

**证明**：

$$R(\alpha)R(\beta)=\begin{pmatrix}\cos\alpha & -\sin\alpha\\ \sin\alpha & \cos\alpha\end{pmatrix}\begin{pmatrix}\cos\beta & -\sin\beta\\ \sin\beta & \cos\beta\end{pmatrix}.$$

逐项算四个元素（记 $$c_\alpha=\cos\alpha,\ s_\alpha=\sin\alpha$$，其余同理）：

- 左上：$$c_\alpha c_\beta-s_\alpha s_\beta$$；
- 右上：$$c_\alpha(-s_\beta)+(-s_\alpha)c_\beta=-(c_\alpha s_\beta+s_\alpha c_\beta)$$；
- 左下：$$s_\alpha c_\beta+c_\alpha s_\beta=c_\alpha s_\beta+s_\alpha c_\beta$$；
- 右下：$$s_\alpha(-s_\beta)+c_\alpha c_\beta=c_\alpha c_\beta-s_\alpha s_\beta$$。

再用和角公式 $$c_{\alpha+\beta}=c_\alpha c_\beta-s_\alpha s_\beta$$、$$s_{\alpha+\beta}=s_\alpha c_\beta+c_\alpha s_\beta$$，上面四个元素正是 $$c_{\alpha+\beta},\ -s_{\alpha+\beta},\ s_{\alpha+\beta},\ c_{\alpha+\beta}$$。故左边等于 $$R(\alpha+\beta)$$。$$\blacksquare$$

**推论 3.1** (i) $$R(0)=I$$；(ii) $$R(\theta)^{-1}=R(-\theta)$$；(iii) $$R(\alpha)R(\beta)=R(\beta)R(\alpha)$$。

**证明**：(i) 令 $$\theta=0$$，矩阵变成单位阵。(ii) 由定理取 $$\beta=-\theta$$，得 $$R(\theta)R(-\theta)=R(0)=I$$，两边同时是逆的条件，故 $$R(\theta)^{-1}=R(-\theta)$$。(iii) 定理两边各交换 $$\alpha,\beta$$ 都给出 $$R(\alpha+\beta)$$，而实数加法可交换，故 $$R(\alpha)R(\beta)=R(\beta)R(\alpha)$$。$$\blacksquare$$

**定义 3.2（旋转群, rotation group）** 集合
$$SO(2):=\{R(\theta):\theta\in\mathbb{R}\}$$
按矩阵乘法构成一个**交换群**（推论 3.1 逐条给出了结合律的继承、单位元、逆元、交换律），称为**平面旋转群 (rotation group)**。

> **注 3.1** 记号 $$SO(2)$$ 的一般定义是
> $$SO(2)=\{A\in M_2(\mathbb{R}):A^{\mathsf T}A=I,\ \det A=1\},$$
> 即"正交且行列式为 $$1$$"的矩阵。行列式等于 $$1$$ 这一条排除了反射 $$(x,y)\mapsto(x,-y)$$（它的行列式是 $$-1$$）。请读者自行验证 $$R(\theta)^{\mathsf T}R(\theta)=I$$、$$\det R(\theta)=\cos^2\theta+\sin^2\theta=1$$，且 $$R(\theta)R(\theta)^{\mathsf T}=I$$。

### 3.2 从旋转到复数：把乘法定义出来

现在做入口题 (b)。$$SO(2)$$ 是一个群，我们希望把"复合"这个几何操作翻译成"某类数之间的乘法"。

**做法**：把每个点 $$z=(a,b)\in\mathbb{R}^2$$ 连同它诱导的一个线性映射打包在一起。对 $$z=(a,b)$$ 定义矩阵

$$M_z:=\begin{pmatrix}a & -b\\ b & a\end{pmatrix}.$$

之所以选这种形状：它正是 3.1 节里 $$R(\theta)$$ 的形状（取 $$a=\cos\theta,\ b=\sin\theta$$），也就是"旋转 $$+$$ 伸缩"的形状。记 $$\mathcal{S}:=\{M_z:z\in\mathbb{R}^2\}$$。

**引理 3.2（封闭性）** 对任意 $$z=(a,b)$$、$$w=(c,d)$$，

$$M_zM_w=\begin{pmatrix}ac-bd & -(ad+bc)\\ ad+bc & ac-bd\end{pmatrix}=M_{(ac-bd,\ ad+bc)}.$$

**证明**：按矩阵乘法逐项展开（左边矩阵取行、右边矩阵取列，对应位置相乘再相加）：

- 左上（第 1 行 $$\times$$ 第 1 列）：$$a\cdot c+(-b)\cdot d=ac-bd$$；
- 右上（第 1 行 $$\times$$ 第 2 列）：$$a\cdot(-d)+(-b)\cdot c=-ad-bc$$；
- 左下（第 2 行 $$\times$$ 第 1 列）：$$b\cdot c+a\cdot d=bc+ad$$；
- 右下（第 2 行 $$\times$$ 第 2 列）：$$b\cdot(-d)+a\cdot c=-bd+ac$$。

拼起来：
$$M_zM_w=\begin{pmatrix}a & -b\\ b & a\end{pmatrix}\begin{pmatrix}c & -d\\ d & c\end{pmatrix}=\begin{pmatrix}ac-bd & -ad-bc\\ bc+ad & -bd+ac\end{pmatrix}.$$
左上与右下都等于 $$ac-bd$$，右上与左下互为相反数（$$-(ad+bc)$$ 与 $$ad+bc$$），这正是 $$M_{(ac-bd,\ ad+bc)}$$ 的形状（把 $$(ac-bd,\ ad+bc)$$ 代入 $$M$$ 的定义逐项核对即可）。这与所写矩阵逐元素相同。$$\blacksquare$$

引理的意义：**$$M_zM_w$$ 仍属于 $$\mathcal{S}$$**。这允许我们把乘法"下放"到点上。

**定义 3.3（复数乘法）** 对 $$z=(a,b)$$、$$w=(c,d)\in\mathbb{R}^2$$，规定

$$z\cdot w:=(ac-bd,\ ad+bc).$$

这个定义不是凭空立的：它是引理 3.2 中"矩阵乘积仍是 $$\mathcal{S}$$ 中元素"的唯一读法。换句话说，**乘法法则由"旋转可以复合"这件事逼出来**——这正是入口题 (b1) 的答案。

**定理 3.3（$$\mathbb{C}$$ 是域, field）** $$(\mathbb{R}^2,+,\ \cdot)$$ 是一个**域**，记作 $$\mathbb{C}$$。其中 $$+$$ 是向量加法。

**为什么要证这个**：定义 3.3 只给出了乘法的公式，还没有说这个乘法"讲不讲道理"——结合律成不成立？有没有单位元、逆元？能不能像有理数、实数一样自由做加减乘除？如果不验证，后面写 $$z^2,\ 1/z,\ e^z$$ 这些式子时就都是空中楼阁。这正是要证的内容。

**证明思路**：域的公理很多，逐个硬验会很累。聪明的做法是**把 $$\mathcal{S}$$ 中的矩阵搬来当证人**：加法、乘法、结合律、分配律在 $$M_2(\mathbb{R})$$ 里早就成立，我们只需证明"点上的运算"与"矩阵上的运算"完全同构，公理就整体继承过来。只有交换律和逆元需要单独看一下（交换律其实也是继承的，见下）。

**证明**：

**(1) $$\mathbb{C}\cong\mathcal{S}$$ 作为环。** 映射 $$\phi:z\mapsto M_z$$ 是双射（$$M_z$$ 的第一列就是 $$z$$），且
$$\phi(z+w)=\phi(z)+\phi(w),\qquad \phi(z\cdot w)=\phi(z)\phi(w).$$
第一条由 $$M$$ 对 $$(a,b)$$ 线性可得：$$M_{(a_1+a_2,\ b_1+b_2)}=M_{(a_1,b_1)}+M_{(a_2,b_2)}$$（逐元素验）。第二条就是引理 3.2。

**(2) 加法群。** $$(\mathbb{R}^2,+)$$ 是交换群（分量各自相加，满足结合、交换，零元 $$(0,0)$$，逆元 $$-z$$）。

**(3) 结合律与分配律。** 以结合律 $$(z\cdot w)\cdot u=z\cdot(w\cdot u)$$ 为例说明"拉回"具体怎么操作。由 (1)，$$\phi(z\cdot w)=\phi(z)\phi(w)=M_zM_w$$，故
$$\phi\bigl((z\cdot w)\cdot u\bigr)=\phi(z\cdot w)\phi(u)=(M_zM_w)M_u.$$
同理 $$\phi\bigl(z\cdot(w\cdot u)\bigr)=M_z(M_wM_u)$$。而 $$\mathcal{S}\subset M_2(\mathbb{R})$$，矩阵乘法满足结合律（这是线性代数里已经证过的事实，与 $$z,w,u$$ 是什么无关），故 $$(M_zM_w)M_u=M_z(M_wM_u)$$，即 $$\phi\bigl((z\cdot w)\cdot u\bigr)=\phi\bigl(z\cdot(w\cdot u)\bigr)$$。又 $$\phi$$ 是双射（(1) 中已说明），双射保证"像相等 $$\Rightarrow$$ 原像相等"，故 $$(z\cdot w)\cdot u=z\cdot(w\cdot u)$$。分配律 $$z\cdot(w+u)=z\cdot w+z\cdot u$$ 逐字同样的三步（用 $$\phi$$ 保加法、矩阵乘法对加法分配、$$\phi$$ 是双射）即得。

**(4) 交换律。** 记 $$J:=M_{(0,1)}=\begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}$$，则 $$M_z=aI+bJ$$。由 $$J^2=\begin{pmatrix}-1 & 0\\ 0 & -1\end{pmatrix}=-I$$ 知 $$z\mapsto M_z$$ 与"把 $$J$$ 代入实多项式"是一回事。于是 $$M_zM_w=(aI+bJ)(cI+dJ)$$ 与 $$M_wM_z=(cI+dJ)(aI+bJ)$$ 都是 $$J$$ 的同一个多项式 $$acI+(ad+bc)J+bdJ^2$$，故相等。**（同一个矩阵的多项式总是交换的。）**

**(5) 单位元与逆元。** 单位元 $$1:=(1,0)$$，$$M_1=I$$。若 $$z=(a,b)\ne 0$$，则
$$\det M_z=a^2+b^2>0,$$
故 $$M_z$$ 可逆，且直接验算
$$M_zM_{(a,-b)}=(a^2+b^2)M_{(1,0)},$$
即
$$z^{-1}=\left(\frac{a}{a^2+b^2},\ \frac{-b}{a^2+b^2}\right).$$
（这条式子请展开验一遍。）故每个非零元可逆。

综上，$$(\mathbb{R}^2,+,\cdot)$$ 是交换域。$$\blacksquare$$

**定义 3.4（虚数单位, imaginary unit）** $$i:=(0,1)$$。

**定理 3.4（$$i^2=-1$$ 是定理，不是公理）**
$$i^2=(0,1)\cdot(0,1)=(0\cdot 0-1\cdot 1,\ 0\cdot 1+1\cdot 0)=(-1,0)=-1.$$

这就是入口题 (b2) 的答案。$$i$$ 不是"平方等于负一的怪数"，它是**旋转 $$90^\circ$$** 这件事在乘法记号下的名字。

**记号约定** 有了定理 3.4，可写 $$(a,b)=(a,0)+(0,b)=a\cdot 1+b\cdot i=:a+bi$$。于是定义 3.3 的乘法就是熟悉的样子：

$$(a+bi)(c+di)=(ac-bd)+(ad+bc)i.$$

到目前为止乘法还只是一条代数公式——$$(ac-bd,ad+bc)$$ 这个式子本身看不出任何几何含义。但本章的出发点是"旋转"，所以有必要把乘法翻译回几何：乘以一个固定的复数，到底是平面上的什么操作？下面这条定理给出精确答案。

**定理 3.5（乘法 $$=$$ 旋转 $$+$$ 伸缩）** 对 $$\theta\in\mathbb{R}$$ 记
$$X(\theta):=(\cos\theta,\ \sin\theta)\in\mathbb{C}.$$
则

(i) $$M_{X(\theta)}=R(\theta)$$，即"乘以单位点 $$X(\theta)$$"就是"旋转 $$\theta$$"；
(ii) $$X(\alpha)X(\beta)=X(\alpha+\beta)$$；
(iii) 每个 $$z\ne0$$ 唯一地写作 $$z=rX(\theta)$$，其中 $$r=\lvert z\rvert:=\sqrt{a^2+b^2}>0$$、$$\theta\in\mathbb{R}/2\pi\mathbb{Z}$$；于是
$$z\cdot w=(rs)\,X(\alpha+\beta)\quad\text{当 } z=rX(\alpha),\ w=sX(\beta).$$
用一句话说：**复数乘法 $$=$$ 模相乘、幅角相加**。

**证明**：(i) 比较矩阵：$$M_{X(\theta)}=\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}=R(\theta)$$，逐元素相同。
(ii) $$M_{X(\alpha)}M_{X(\beta)}=R(\alpha)R(\beta)=R(\alpha+\beta)=M_{X(\alpha+\beta)}$$（第二步用定理 3.1），两边取下标的点即得。
(iii) 存在性：给定 $$z=(a,b)\ne0$$，令 $$r=\sqrt{a^2+b^2}>0$$，则 $$(a/r)^2+(b/r)^2=1$$，故存在 $$\theta$$ 使 $$\cos\theta=a/r,\ \sin\theta=b/r$$，即 $$z=rX(\theta)$$。唯一性（在模 $$2\pi$$ 意义下）：若 $$rX(\theta)=r'X(\theta')$$ 且 $$r,r'>0$$，取模（模平方等于两分量平方和）得 $$r=r'$$，再比较两分量得 $$\cos\theta=\cos\theta'$$、$$\sin\theta=\sin\theta'$$，故 $$\theta-\theta'\in2\pi\mathbb{Z}$$。最后，$$M_{z\cdot w}=M_zM_w=M_{rX(\alpha)}M_{sX(\beta)}$$，而 $$M_{rX(\alpha)}=rR(\alpha)$$（因为 $$M$$ 对 $$(a,b)$$ 线性），于是 $$M_{z\cdot w}=rsR(\alpha)R(\beta)=rsR(\alpha+\beta)=M_{rsX(\alpha+\beta)}$$，两边取下标的点。$$\blacksquare$$

**定义 3.5（模与幅角）** $$r=\lvert z\rvert$$ 称 $$z$$ 的**模 (modulus)**，$$\theta$$ 称 $$z$$ 的**幅角 (argument)**，记 $$\theta=\arg z$$。注意 $$\arg$$ 只在模 $$2\pi$$ 的意义下确定。

下面这个记号会在几乎每一条后续证明里出现——原因很简单：模的平方 $$a^2+b^2$$ 无法直接从 $$z$$ 一个数写出来，但如果配上"把虚部变号"的搭档，$$z$$ 与搭档相乘就正好凑出 $$a^2+b^2$$（见推论 3.6 之后的注）。

**定义 3.6（共轭, conjugate）** $$\bar z:=(a,-b)$$，即 $$\overline{a+bi}=a-bi$$。

**推论 3.6（模的乘性——一个免费礼物）** $$\lvert zw\rvert=\lvert z\rvert\lvert w\rvert$$。

**证明**：由 (1) 中 $$\phi$$ 保乘法，$$\det M_{zw}=\det(M_zM_w)=\det M_z\cdot\det M_w$$。而 $$\det M_z=a^2+b^2=\lvert z\rvert^2$$，故 $$\lvert zw\rvert^2=\lvert z\rvert^2\lvert w\rvert^2$$；两边取正平方根（模非负）即得。$$\blacksquare$$

> 也请自己用 $$\lvert z\rvert^2=z\bar z$$ 再证一次：$$z\bar z=(a+bi)(a-bi)=a^2+b^2$$，于是 $$\lvert zw\rvert^2=zw\overline{zw}=zw\bar z\bar w=(z\bar z)(w\bar w)=\lvert z\rvert^2\lvert w\rvert^2$$。这一路更短，但用到了"共轭对乘法可交换"（$$\overline{zw}=\bar z\bar w$$），需要另证一次。

### 3.3 Euler 公式

现在处理指数。目标是把 $$\theta\mapsto X(\theta)=(\cos\theta,\sin\theta)$$ 写成一个**指数**。

**定义 3.7（复指数, complex exponential）** 对 $$z\in\mathbb{C}$$，规定
$$e^z:=\sum_{n=0}^{\infty}\frac{z^n}{n!}.$$

写下这个级数只是第一步——一个无穷和要能用，先得确认它真的加得起来（收敛），否则后面"逐项求导""指数律"这些操作全都没有立足点。下面这条引理把这件事一次性确认掉。

**引理 3.7（收敛性）** 上述级数对每个 $$z\in\mathbb{C}$$ 绝对收敛；在任意紧集上一致收敛，故定义一个连续函数 $$\mathbb{C}\to\mathbb{C}$$。

**证明思路**：与实数情形逐字相同——把每一项取模，跟 $$\sum \lvert z\rvert^n/n!$$ 比，后者收敛。要的只是"三角不等式"和"实指数级数收敛"这两件事。

**证明**：对 $$N$$ 与 $$M>N$$，
$$\left\lvert\sum_{n=N}^{M}\frac{z^n}{n!}\right\rvert\le\sum_{n=N}^{M}\frac{\lvert z\rvert^n}{n!}.$$
右边是收敛级数 $$\sum\lvert z\rvert^n/n!$$（实指数级数）的尾段，随 $$N\to\infty$$ 趋于 $$0$$。故部分和是 Cauchy 序列，$$\mathbb{C}$$ 完备（$$\mathbb{C}$$ 与 $$\mathbb{R}^2$$ 同构，$$\mathbb{R}^2$$ 完备），故收敛。一致收敛：若 $$\lvert z\rvert\le R$$，则 $$\lvert z^n/n!\rvert\le R^n/n!$$，而 $$\sum R^n/n!$$ 与 $$z$$ 无关且收敛，由 Weierstrass 判别法一致收敛。连续性是"一致收敛保持连续"的直接推论。$$\blacksquare$$

> **注 3.2** 完整的复级数理论（幂级数的收敛半径、逐项求导、Cauchy 乘积的严格处理）见**第 06 章**。本章只用到"$$\theta$$ 是实数"这一情形，因此下面的逐项求导可以在**实分析**的框架内完成，读者已有的工具（Gap1、Gap2）足够。

有了收敛性，$$e^z$$ 才是一个诚实的函数；但本章真正要用的不是"$$e^z$$ 存在"，而是"指数律"——因为 3.2 节的主线是"角相加对应乘法"，如果 $$e^ze^w\ne e^{z+w}$$，$$e^{i\theta}$$ 就不可能承担起"把加法翻译成乘法"的角色，整条主线会断掉。

**定理 3.7（指数律）** 对任意 $$z,w\in\mathbb{C}$$，$$e^{z}e^{w}=e^{z+w}$$。

**证明思路**：两个绝对收敛级数相乘，可以按"$$n+m=k$$"重新分组（Cauchy 乘积，绝对收敛时合法），再对每组用二项式定理。

**证明**：由引理 3.7，$$\sum z^n/n!$$ 与 $$\sum w^m/m!$$ 都绝对收敛，故其 Cauchy 乘积可按任意方式重排：
$$e^ze^w=\sum_{k=0}^{\infty}\left(\sum_{n+m=k}\frac{z^n}{n!}\frac{w^m}{m!}\right)=\sum_{k=0}^{\infty}\frac{1}{k!}\sum_{n=0}^{k}\binom{k}{n}z^nw^{k-n}=\sum_{k=0}^{\infty}\frac{(z+w)^k}{k!}=e^{z+w},$$
中间一步用了二项式定理。$$\blacksquare$$

**引理 3.8（$$e^{i\theta}$$ 是 $$X'=iX$$ 的解）** 对实变量 $$\theta$$，
$$\frac{d}{d\theta}e^{i\theta}=i\,e^{i\theta},\qquad e^{i\cdot0}=1.$$

**证明**：$$e^{i\theta}=\sum_{n\ge0}i^n\theta^n/n!$$ 是 $$\theta$$ 的整幂级数，各项系数有界，故可在收敛区间（此处为全实轴）内逐项求导：
$$\frac{d}{d\theta}\sum_{n\ge0}\frac{i^n\theta^n}{n!}=\sum_{n\ge1}\frac{i^n\,n\theta^{n-1}}{n!}=i\sum_{n\ge1}\frac{i^{n-1}\theta^{n-1}}{(n-1)!}=i\sum_{k\ge0}\frac{i^k\theta^k}{k!}=i\,e^{i\theta}.$$
（中间的 $$n/n!=1/(n-1)!$$ 是实数运算。）$$e^{i\cdot0}=1$$ 由级数首项给出。$$\blacksquare$$

**定理 3.9（Euler 公式, Euler's formula）** 对一切 $$\theta\in\mathbb{R}$$，
$$e^{i\theta}=\cos\theta+i\sin\theta.$$

**证明思路（两条路，都记下来）**。路一是**唯一性论证**：$$e^{i\theta}$$ 与 $$\cos\theta+i\sin\theta$$ 满足同一个一阶方程、同一初值，因此相等——这条路揭示结构。路二是**级数比较**：把 $$e^{i\theta}$$ 的级数按奇偶项拆开，正好拼出 $$\cos\theta$$ 与 $$\sin\theta$$ 的级数——这条路给出显式恒等。

**证明（路一：一阶方程的唯一性）** 记 $$g(\theta):=\cos\theta+i\sin\theta$$。

第一步，$$g$$ 满足同一个方程。由 3.2 节的乘法公式，
$$g'(\theta)=-\sin\theta+i\cos\theta=i(\cos\theta+i\sin\theta)=i\,g(\theta),$$
其中第一步是逐分量求导，第二步用 $$i\cos\theta=i\cos\theta$$、$$i\cdot i\sin\theta=-\sin\theta$$ 整理。又 $$g(0)=1+i\cdot0=1$$。

第二步，差一个因子。由定理 3.7（取 $$z=i\theta$$、$$w=-i\theta$$，注意 $$z+w=0$$）得 $$e^{i\theta}e^{-i\theta}=e^{0}=1$$；这里 $$e^{-i\theta}:=e^{i(-\theta)}$$。令 $$h(\theta):=e^{-i\theta}g(\theta)$$，则
$$h'(\theta)=-i\,e^{-i\theta}g(\theta)+e^{-i\theta}g'(\theta)=\bigl(-i+i\bigr)e^{-i\theta}g(\theta)=0.$$
导数恒为零的光滑函数是常数（实分析中的中值定理推论），故 $$h\equiv h(0)=e^{0}\cdot g(0)=1$$。两边乘 $$e^{i\theta}$$（并再用一次指数律）得 $$g(\theta)=e^{i\theta}$$。$$\blacksquare$$

**证明（路二：级数按奇偶项拆开）** 把 $$i^n$$ 按 $$n$$ 的奇偶分开：$$i^{2k}=(i^2)^k=(-1)^k$$，$$i^{2k+1}=(-1)^k i$$。于是
$$e^{i\theta}=\sum_{n\ge0}\frac{i^n\theta^n}{n!}=\underbrace{\sum_{k\ge0}\frac{(-1)^k\theta^{2k}}{(2k)!}}_{\text{偶项}}+\ i\underbrace{\sum_{k\ge0}\frac{(-1)^k\theta^{2k+1}}{(2k+1)!}}_{\text{奇项}}.$$
偶项正是 $$\cos\theta$$ 的 Taylor 级数，奇项正是 $$\sin\theta$$ 的 Taylor 级数（Gap2 已用过这两个展开）。故 $$e^{i\theta}=\cos\theta+i\sin\theta$$。$$\blacksquare$$

**推论 3.9** (i) $$e^{i\theta}$$ 的模恒为 $$1$$；(ii) $$\overline{e^{i\theta}}=e^{-i\theta}=1/e^{i\theta}$$；(iii) $$e^{i\pi}=-1$$，$$e^{i\pi/2}=i$$，$$e^{2\pi i}=1$$；(iv)（de Moivre）$$(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta$$；(v) 每个 $$z\ne0$$ 唯一写成 $$z=re^{i\theta}$$（$$r>0$$，$$\theta\in\mathbb{R}/2\pi\mathbb{Z}$$）。

**证明**：(i) $$\lvert e^{i\theta}\rvert^2=\cos^2\theta+\sin^2\theta=1$$。(ii) 共轭对实系数运算封闭，故 $$\overline{e^{i\theta}}=\overline{\cos\theta+i\sin\theta}=\cos\theta-i\sin\theta=e^{-i\theta}$$；再由 (i) 与 $$z\bar z=\lvert z\rvert^2=1$$ 得 $$e^{-i\theta}=1/e^{i\theta}$$。(iii) 直接代 $$\theta$$ 值。(iv) $$n$$ 次用定理 3.7（或对 $$(e^{i\theta})^n=e^{in\theta}$$ 再用 Euler 公式）。(v) 即定理 3.5(iii)。$$\blacksquare$$

> **注 3.3（这是本章的技术核心，也是全书的种子）** 定理 3.9 的路一里，我们真正用到的是：$$e^{i\theta}$$ 是求导算子 $$\frac{d}{d\theta}$$ 的**特征向量 (eigenvector)**，**特征值 (eigenvalue)** 是 $$i$$。Gap2 里"$$\sin'=\cos,\ \cos'=-\sin$$ 交错配对"的直观，说的就是同一件事——$$\cos\theta+i\sin\theta$$ 把这对实函数打包成一个复特征向量，交错配对随之变成"乘一个数"。这个视角在第 04 章会被正面讲透。

### 3.4 指数映射与旋转群的同构

把上面三节收成一句结构性的陈述。

**定理 3.10（指数映射, exponential map）** 映射
$$\exp:\mathbb{R}\to S^1,\qquad \theta\mapsto e^{i\theta}$$
（$$S^1:=\{z:\lvert z\rvert=1\}$$ 是单位圆）满足：
(i) 它是**群同态 (group homomorphism)**：$$\exp(\alpha+\beta)=\exp\alpha\cdot\exp\beta$$；
(ii) 它是满射；
(iii) 它的核是 $$\ker\exp=2\pi\mathbb{Z}$$
（**核 (kernel)** = 被映到单位元 $$1$$ 的那些元素）。因此存在群同构
$$S^1\ \cong\ \mathbb{R}/2\pi\mathbb{Z}.$$

**证明**：(i) 由定理 3.7（指数律）直接取 $$z=i\alpha,\ w=i\beta$$。(ii) 给定 $$\lvert z\rvert=1$$，由定理 3.5(iii) 写 $$z=1\cdot X(\theta)=e^{i\theta}$$（末一步用 Euler 公式）。(iii) $$e^{i\theta}=1\iff\cos\theta=1,\ \sin\theta=0\iff\theta\in2\pi\mathbb{Z}$$。(iv) 由群同态基本定理，满同态诱导同构 $$\mathbb{R}/\ker\exp\cong S^1$$。$$\blacksquare$$

把 3.1 与 3.4 拼起来，本章主线显形：

$$SO(2)\ \cong\ S^1\ \cong\ U(1)\ \cong\ \mathbb{R}/2\pi\mathbb{Z}.$$

右端是**数**（单位复数）、第三是**代数对象**（酉群 $$U(1)$$）、第二是**几何对象**（圆）、左端是**变换**（旋转）。四个名字，一个对象。

> **注 3.4（悬在这里的线头）** $$\exp:\mathbb{R}\to S^1$$ 把一条直线"卷"到圆上，是**覆叠映射 (covering map)**，且 $$\mathbb{R}$$ 是 $$S^1$$ 的单连通覆叠。这就是第 40 章前后**覆盖群 (covering group)** 的雏形。另外，$$\arg z$$ 之所以只能定到模 $$2\pi$$，本质上就是因为这个卷绕——多值性不是缺陷，是拓扑。

## 四、几何与物理直觉 (Intuition)

**几何**。乘以 $$z=re^{i\theta}$$ 就是"伸缩 $$r$$ 倍 $$+$$ 逆时针转 $$\theta$$"。因此复乘法有一个实线性代数里看不出来的性质：**它保持任意两条线的夹角**——平面上过 $$z_0$$ 的两条曲线，在 $$w\mapsto zw$$ 下被同一个因子 $$z$$ 缩放，夹角（大小与方向）原样不变。这就是**保角 (conformal)** 的最简单例子；第 05、06 章的共形映射理论从这里长出来。

单位圆 $$S^1$$ 是"全部的旋转"，它在圆上的运算是"角度相加模 $$2\pi$$"。群 $$\mathbb{R}/2\pi\mathbb{Z}$$ 的几何就是一个圆：**加法群被卷成了圆**。

**物理**。自然界的问题提炼为线性微分方程后，解常常带指数函数：

- **实指数** $$e^{at}$$ 描述**衰减或增长**——只有数量在变，方向不变；
- **虚指数** $$e^{i\omega t}$$ 描述**振荡**——数量不变（$$\lvert e^{i\omega t}\rvert=1$$），方向在转；
- 两者合起来 $$e^{(a+i\omega)t}=e^{at}e^{i\omega t}$$，是**阻尼振荡**的通用形状：阻尼振子、RLC 电路、量子力学的波函数，都长这样。

具体地，一维简谐振动 $$\ddot x=-\omega^2x$$ 的解是 $$x(t)=A\cos\omega t+B\sin\omega t=\operatorname{Re}\bigl(Ce^{i\omega t}\bigr)$$——一个二阶实方程，被一对复指数统一（对照定理 3.9 的路一：$$e^{i\omega t}$$ 恰好是 $$\frac{d^2}{dt^2}$$ 的特征向量，特征值 $$-\omega^2$$）。

再看**角速度**。若点在单位圆上匀速转，位置 $$z(t)=e^{i\omega t}$$，则
$$\dot z=i\omega\,e^{i\omega t}=i\omega\,z.$$
"速度 $$=i\omega$$ 乘位置"——正是**速度垂直于位置、大小 $$\omega\lvert z\rvert$$** 的代数写法。Gap2 里"速度矢量与坐标矢量垂直，故有交错配对形式"的说法，在这里变成一行乘法。

工程上的**相量法**是同一件事的实用版：把 $$\cos(\omega t+\varphi)$$ 记成 $$e^{i\varphi}$$，一切"同频率振动相加"就退化成复数加法，三角恒等式变成复数乘法（练习里的题 4 就是它的算术骨架）。

**三者的对应**（本课主线）：几何上是旋转；代数上是单位复数乘法的"角相加"；物理上是相位与振荡。同一件事。

## 五、经典问题精讲 (Classical Problems)

### 题 1：三个正三角形（入口题 (a) 的清算）

**考点**：单位复数 $$=$$ 旋转；正三角形第三顶点的复坐标。
**在本章结构里的位置**：定理 3.5(ii) 的直接应用，用到的 $$\omega=e^{i\pi/3}$$ 由 3.3 节供给。

**解**。把平面与 $$\mathbb{C}$$ 等同。记
$$\omega:=e^{i\pi/3}=\cos60^\circ+i\sin60^\circ=\tfrac12+\tfrac{\sqrt3}{2}i.$$
先用它算一次：
$$\omega^2=\left(\tfrac12+\tfrac{\sqrt3}{2}i\right)^2=\tfrac14-\tfrac34+\tfrac{\sqrt3}{2}i=-\tfrac12+\tfrac{\sqrt3}{2}i,$$
于是
$$\omega^2-\omega+1=\left(-\tfrac12+\tfrac{\sqrt3}{2}i\right)-\left(\tfrac12+\tfrac{\sqrt3}{2}i\right)+1=0. \tag{A}$$

**引理（正三角形第三顶点）** 给定两点 $$a,b\in\mathbb{C}$$，以 $$ab$$ 为一边、位于有向线段 $$a\to b$$ **左侧**的那个正三角形，其第三顶点为
$$p=a+\omega(b-a).$$

**验证**：$$p-a=\omega(b-a)$$，故 $$\lvert p-a\rvert=\lvert\omega\rvert\cdot\lvert b-a\rvert=\lvert b-a\rvert$$（用推论 3.9(i)）。又
$$p-b=a+\omega(b-a)-b=(\omega-1)(b-a),$$
而 $$\omega-1=-\tfrac12+\tfrac{\sqrt3}{2}i=e^{2\pi i/3}$$，其模为 $$1$$，故 $$\lvert p-b\rvert=\lvert b-a\rvert$$。三边相等，且三点不共线（$$\omega$$ 不是实数），故是正三角形。$$\square$$

**引理（正三角形的中心）** 顶点 $$a,b,p$$ 的重心为
$$g(a,b)=\frac{a+b+p}{3}=\frac{a+b+a+\omega(b-a)}{3}=\frac{(2-\omega)a+(1+\omega)b}{3}.$$

三条边的中心（都用同一个转向的 $$\omega$$）依次是
$$c_1=\frac{(2-\omega)a+(1+\omega)b}{3},\quad c_2=\frac{(2-\omega)b+(1+\omega)c}{3},\quad c_3=\frac{(2-\omega)c+(1+\omega)a}{3}.$$

**比较 $$c_2-c_1$$ 与 $$c_3-c_1$$**。令 $$x=b-a$$，$$y=c-b$$，则 $$c-a=x+y$$。第一式：

$$c_2-c_1=\frac{(2-\omega)(b-a)+(1+\omega)(c-b)}{3}=\frac{(2-\omega)x+(1+\omega)y}{3}.$$

第二式（把 $$\varphi(c)-\varphi(a)$$ 写成 $$\varphi((c-a))$$ 并展开）：

$$c_3-c_1=\frac{(2-\omega)(c-a)+(1+\omega)(a-b)}{3}=\frac{(2-\omega)(x+y)-(1+\omega)x}{3}=\frac{(1-2\omega)x+(2-\omega)y}{3}.$$

**断言** $$c_2-c_1=\omega\,(c_3-c_1)$$。只需比较系数。右边

$$\omega(c_3-c_1)=\frac{\omega(1-2\omega)x+\omega(2-\omega)y}{3}=\frac{(\omega-2\omega^2)x+(2\omega-\omega^2)y}{3}.$$

用关系 (A) 即 $$\omega^2=\omega-1$$：

- $$x$$ 的系数：$$\omega-2\omega^2=\omega-2(\omega-1)=2-\omega$$，与左边一致；
- $$y$$ 的系数：$$2\omega-\omega^2=2\omega-(\omega-1)=1+\omega$$，与左边一致。

故断言成立。于是 $$\lvert c_2-c_1\rvert=\lvert\omega\rvert\cdot\lvert c_3-c_1\rvert=\lvert c_3-c_1\rvert$$，且从 $$c_1$$ 到 $$c_2$$、$$c_3$$ 的夹角恰为 $$60^\circ$$。**$$C_1C_2C_3$$ 是正三角形**。$$\blacksquare$$

**顺带**：把三式相加，每个顶点的系数都是 $$(2-\omega)+(1+\omega)=3$$，故
$$c_1+c_2+c_3=a+b+c.$$
即"三个中心的重心 $$=$$ 原三角形的重心"。这解释了为什么答案看起来那么"整齐"。

> 用 $$\bar\omega$$ 代替 $$\omega$$ 是三个三角形翻到另一侧的情形，同样的计算逐字成立（$$\bar\omega$$ 满足同一个关系 (A)）。

### 题 2：三倍角与 $$\cos36^\circ$$

**考点**：de Moivre 公式；把三角问题翻译成代数方程。
**在本章结构里的位置**：推论 3.9(iv) 的应用；关系 (A) 型"单位根关系"的味道。

**解**。由推论 3.9(iv)（取 $$n=3$$），
$$\cos3\theta+i\sin3\theta=(\cos\theta+i\sin\theta)^3.$$
右边用二项式展开，取实部（$$i^2=-1$$）：
$$(\cos\theta+i\sin\theta)^3=\cos^3\theta+3\cos^2\theta(i\sin\theta)+3\cos\theta(i\sin\theta)^2+(i\sin\theta)^3$$
实部 $$=\cos^3\theta-3\cos\theta\sin^2\theta$$。故
$$\cos3\theta=\cos^3\theta-3\cos\theta\sin^2\theta=\cos^3\theta-3\cos\theta(1-\cos^2\theta)=4\cos^3\theta-3\cos\theta.$$

现在算 $$\cos36^\circ$$。令 $$x=\cos36^\circ$$。由上式，
$$\cos108^\circ=4x^3-3x.$$
另一方面 $$108^\circ=180^\circ-72^\circ$$，故 $$\cos108^\circ=-\cos72^\circ=-(2\cos^2 36^\circ-1)=-(2x^2-1)$$（用了二倍角公式）。两式相等：
$$4x^3-3x=-(2x^2-1)\ \Longrightarrow\ 4x^3+2x^2-3x-1=0.$$
因式分解（把 $$x=-1$$ 代入左边得 $$-4+2+3-1=0$$，故 $$x+1$$ 是因子）：
$$4x^3+2x^2-3x-1=(x+1)(4x^2-2x-1).$$
$$x=\cos36^\circ$$ 是正数，故取 $$4x^2-2x-1=0$$，得
$$x=\frac{2\pm\sqrt{4+16}}{8}=\frac{1\pm\sqrt5}{4}.$$
由 $$x>0$$ 舍去负根：
$$\boxed{\ \cos36^\circ=\frac{1+\sqrt5}{4}\ }\approx0.8090.$$
这个数是黄金分割比的一半——正五边形的可作图性（Euclid）最终就归到它上面。同一多项式 $$4x^2-2x-1$$ 在题 3 的 $$n=5$$ 情形会以单位根的形式再出现一次。

### 题 3：单位根与正多边形

**考点**：**单位根 (root of unity)**；等比求和；"复数方程的根"与"几何对称"的互译。
**在本章结构里的位置**：定理 3.5(iii)（极坐标）与推论 3.9(v) 的组合应用。

**解**。设 $$n\ge2$$，$$\zeta:=e^{2\pi i/n}$$。

**(i) $$\zeta^0,\zeta^1,\dots,\zeta^{n-1}$$ 恰是 $$x^n-1$$ 的全部根，且互不相同。**

代入：$$(\zeta^k)^n=\zeta^{kn}=e^{2\pi i k}=1$$，故都是根。互不相同：若 $$\zeta^j=\zeta^k$$（$$0\le j<k\le n-1$$），则 $$\zeta^{k-j}=1$$，即 $$e^{2\pi i(k-j)/n}=1$$，故 $$k-j$$ 是 $$n$$ 的倍数（见定理 3.10(iii) 的同款论证）；但 $$0<k-j<n$$，矛盾。一个 $$n$$ 次多项式至多 $$n$$ 个不同的根，故这 $$n$$ 个就是全部。$$\square$$

**(ii) 和为零：** 对 $$n\ge2$$，
$$\sum_{k=0}^{n-1}\zeta^k=\frac{\zeta^n-1}{\zeta-1}=\frac{1-1}{\zeta-1}=0,$$
其中第一个等号是等比求和公式（$$\zeta\ne1$$，因为 $$n\ge2$$）。

**(iii) 正 $$n$$ 边形的重心在原点。** 第 (i) 条给出
$$x^n-1=\prod_{k=0}^{n-1}\left(x-\zeta^k\right).$$
比较两边 $$x^{n-1}$$ 的系数：左边是 $$0$$，右边是 $$-\sum_{k=0}^{n-1}\zeta^k$$，故 $$\sum\zeta^k=0$$。（这与 (ii) 是同一件事的两种说法。）几何上，$$S^1$$ 上的点 $$\zeta^k$$ 是内接正 $$n$$ 边形的顶点，而顶点坐标的算术平均是零——顶点之和为零。$$\blacksquare$$

$$n=3$$ 时得到 $$1+\omega'+\omega'^2=0$$（$$\omega'=e^{2\pi i/3}=\omega^2$$），正是题 1 里关系 (A) 在 $$\omega^2=\omega-1$$ 之外的另一种写法。$$n=5$$ 时把它与题 2 对照，可以算出 $$\cos72^\circ$$、$$\cos36^\circ$$ 的另一条路。

### 题 4：三角级数的封闭形式（通往 Fourier）

**考点**：把实三角和翻译成等比级数；取实部/虚部。
**在本章结构里的位置**：定理 3.5(ii) 与推论 3.9(iv) 的联合应用；它是第 15–17 章 Fourier 分析的算术前身。

**解**。设 $$0<\theta<2\pi$$，$$z=e^{i\theta}\ne1$$。由等比求和，
$$\sum_{k=1}^{n}z^k=\frac{z(z^n-1)}{z-1}.$$
用 $$e^{i\psi}-1=2i\,e^{i\psi/2}\sin\frac{\psi}{2}$$（这是把差写成"半角提公因子"的标准技巧），得
$$z-1=2i\,e^{i\theta/2}\sin\frac{\theta}{2},\qquad z^n-1=2i\,e^{in\theta/2}\sin\frac{n\theta}{2}.$$
代入并约掉 $$2i$$：
$$\sum_{k=1}^{n}e^{ik\theta}=e^{i\theta}\cdot\frac{e^{in\theta/2}\sin\frac{n\theta}{2}}{e^{i\theta/2}\sin\frac{\theta}{2}}=e^{i\frac{(n+1)\theta}{2}}\cdot\frac{\sin\frac{n\theta}{2}}{\sin\frac{\theta}{2}}.$$
两边取实部与虚部：
$$\sum_{k=1}^{n}\cos k\theta=\frac{\sin\frac{n\theta}{2}\cos\frac{(n+1)\theta}{2}}{\sin\frac{\theta}{2}},\qquad \sum_{k=1}^{n}\sin k\theta=\frac{\sin\frac{n\theta}{2}\sin\frac{(n+1)\theta}{2}}{\sin\frac{\theta}{2}}.$$

**物理含义**：$$n$$ 个频率相同、相位等间隔、振幅相等的振动相加，结果仍是**同频率**的振动——只是振幅与相位被一个"核"调制了。当 $$\theta=2\pi/N$$ 时，$$\left(\frac{\sin(n\theta/2)}{\sin(\theta/2)}\right)^2$$ 就是多缝干涉的强度公式骨架；在 Fourier 分析里同一个量叫 **Dirichlet 核**，它的 $$L^1$$ 范数随 $$\log n$$ 增长，正是 Fourier 级数逐点收敛"不稳定"的根源（见专家依据 `harmonic-fourier`）。$$\blacksquare$$

> **技巧评注**：整道题只做了两件事——把 $$\cos$$、$$\sin$$ 换成 $$e^{i\theta}$$ 的实部虚部（推论 3.9），把"同一件事做 $$n$$ 次"换成 $$z$$ 的幂次和。这就是复数的全部威力所在。

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 把下列复数写成 $$a+bi$$ 形式：$$(3+2i)(1-4i)$$；$$\dfrac{1+i}{1-i}$$；$$(\sqrt3+i)^6$$。

**基2.** 证明 $$\lvert z_1z_2\rvert=\lvert z_1\rvert\lvert z_2\rvert$$ 与 $$\arg(z_1z_2)\equiv\arg z_1+\arg z_2\pmod{2\pi}$$（$$z_1,z_2\ne0$$），并由此推出 $$\lvert 1/z\rvert=1/\lvert z\rvert$$（$$z\ne0$$）与 $$\lvert z^n\rvert=\lvert z\rvert^n$$（$$n\in\mathbb{Z}$$）。

**基3.** 求 $$z^4=-1$$ 的全部解，把它们画在复平面上，并说明这四点的对称性。

**基4.** 用共轭证明：$$z\in\mathbb{R}\iff z=\bar z$$；$$z\in i\mathbb{R}\iff z=-\bar z$$。

### 竞赛（本课目标难度）

**竞1.** 用复数证明：平面上的三点 $$a,b,c$$（互不相同）构成正三角形，当且仅当
$$a^2+b^2+c^2=ab+bc+ca.$$

**竞2.** 设 $$a,b,c$$ 都在单位圆上（$$\lvert a\rvert=\lvert b\rvert=\lvert c\rvert=1$$）。证明：以 $$a,b,c$$ 为顶点的三角形是正三角形，当且仅当 $$a+b+c=0$$。

**竞3.** 设整数 $$n\ge2$$。计算 $$\prod_{k=1}^{n-1}\sin\dfrac{k\pi}{n}$$，并证明结果恰为 $$\dfrac{n}{2^{n-1}}$$。

**竞4.** （几何）用复数证明 **van Aubel 定理**：以任意四边形的四条边为边，一致地向外各作一个正方形；则连接"相对两边上正方形中心"的两条线段互相垂直且等长。

**竞5.** 设 $$a,b,c$$ 是单位圆上互不相同的三点，$$\triangle abc$$ 的垂心 (orthocenter) 记作 $$h$$。证明
$$h=a+b+c.$$
并由此证明：外心 (circumcenter) $$O$$、重心 $$G$$、垂心 (orthocenter) $$H$$ 三点共线，且 $$OG:GH=1:2$$。

### 研究（通向下一章）

**研1.** **旋转算子的谱 (spectrum)**。设 $$R_\theta$$ 是 3.1 节的旋转矩阵，$$\theta$$ 不是 $$\pi$$ 的整数倍。

(a) 证明：作为实矩阵，$$R_\theta$$ 在 $$\mathbb{R}$$ 上没有特征值、没有实特征向量。也就是说，方程
$$R_\theta v=\lambda v\qquad(\lambda\in\mathbb{R},\ v\in\mathbb{R}^2,\ v\ne0)$$
无解。几何上这意味着：**没有一个非零方向在旋转下保持自身**。

(b) 允许复特征值后，求出 $$R_\theta$$ 的全部特征值，证明它们恰是
$$\lambda_\pm=e^{\pm i\theta},$$
并求出对应的特征向量（**答案会落在 $$\mathbb{C}^2$$ 里，且与 $$(1,\pm i)$$ 有关**）。

(c) 解释这句话：为什么说"在实平面里看不到旋转的伸缩方向，是因为它的伸缩方向指向复方向"？请把 $$R_\theta$$ 在复基下的作用写出来，并与 $$M_{e^{i\theta}}$$ 对照。

**悬念**：这就是第 04 章的开头。一个在实数域里漂亮但"无法对角化"的算子，一进入复域立刻分裂成两个纯伸缩，伸缩因子是 $$e^{\pm i\theta}$$。$$SO(2)$$ 的**谱**是 $$\{e^{i\theta},e^{-i\theta}\}$$ —— 谱为什么比"特征值集合"更基本？为什么它长在单位圆上？

**研2.** **连续同态的分类**（更难，可选）。证明：若 $$\gamma:\mathbb{R}\to S^1$$ 是**连续**群同态（即 $$\gamma(s+t)=\gamma(s)\gamma(t)$$），则存在常数 $$c\in\mathbb{R}$$ 使
$$\gamma(t)=e^{ict}\quad\text{对一切 }t\in\mathbb{R}.$$

**悬念**：结论说"指数映射是旋转群的唯一连续参数化"。这正是 Lie 代数 $$\to$$ Lie 群 的 $$\exp$$ 的起点（第 20–23 章会把这个"唯一性"升级为 Lie 群基本定理）。

### 解答 (Solutions)

**解 基1.** 逐个算。

(1) 直接展开：
$$(3+2i)(1-4i)=3\cdot1+3\cdot(-4i)+2i\cdot1+2i\cdot(-4i)=3-12i+2i-8i^2.$$
由定理 3.4（$$i^2=-1$$），$$-8i^2=8$$，故
$$(3+2i)(1-4i)=3-12i+2i+8=11-10i.$$

(2) 分母实化：分子分母同乘 $$1+i$$（$$1-i$$ 的共轭，定义 3.6；$$(1-i)(1+i)=1-i^2=2$$）：
$$\frac{1+i}{1-i}=\frac{(1+i)^2}{(1-i)(1+i)}=\frac{1+2i+i^2}{1-i^2}=\frac{2i}{2}=i.$$

(3) 先化成极坐标（定理 3.5(iii)、推论 3.9(v)）：$$\lvert\sqrt3+i\rvert=\sqrt{3+1}=2$$，且
$$\frac{\sqrt3+i}{2}=\frac{\sqrt3}{2}+\frac12 i=\cos\frac\pi6+i\sin\frac\pi6=e^{i\pi/6},$$
故 $$\sqrt3+i=2e^{i\pi/6}$$。于是由推论 3.9(iv)（de Moivre）与定理 3.7（指数律），
$$(\sqrt3+i)^6=\left(2e^{i\pi/6}\right)^6=2^6e^{i\pi}=64\cdot(-1)=-64,$$
末一步用推论 3.9(iii)。核对：由推论 3.6，$$\lvert(\sqrt3+i)^6\rvert=2^6=64$$，幅角是 $$6\cdot\frac\pi6=\pi$$，即该数等于 $$-64$$，与上式一致。

**解 基2.** 思路：把两个因子都写成极坐标，乘法的两条规则就退化成模与幅角的算术；而 $$\arg$$ 只在模 $$2\pi$$ 的意义下确定（定义 3.5），所以幅角那一条只能写成同余式。若某个因子为零，两边模都是 $$0$$，结论平凡，以下设 $$z_1,z_2\ne0$$。

按定理 3.5(iii)（或推论 3.9(v)），每个非零复数唯一写作 $$z=re^{i\alpha}$$，其中 $$r=\lvert z\rvert>0$$、$$\alpha=\arg z$$。设
$$z_1=r_1e^{i\alpha_1},\qquad z_2=r_2e^{i\alpha_2}.$$
由定理 3.5(iii) 的最后一条（"模相乘、幅角相加"）：
$$z_1z_2=r_1r_2\,e^{i(\alpha_1+\alpha_2)}.$$
这条式子已经是极坐标形式，而极坐标形式的"模"与"幅角"是唯一确定的（定理 3.5(iii) 的唯一性部分），于是读出
$$\lvert z_1z_2\rvert=r_1r_2=\lvert z_1\rvert\lvert z_2\rvert,\qquad\arg(z_1z_2)\equiv\alpha_1+\alpha_2\equiv\arg z_1+\arg z_2\pmod{2\pi}.$$
第二式必须写 $$\equiv$$：例如 $$z_1=z_2=-1$$ 时左边 $$\arg 1=0$$，右边 $$2\pi$$。（这与推论 3.6 是同一个结论的两条路，那条路走行列式，可以互为验算。）

再取 $$w=1/z$$（$$z\ne0$$）：由已证的模的乘性，
$$1=\lvert1\rvert=\left\lvert z\cdot\frac1z\right\rvert=\lvert z\rvert\cdot\left\lvert\frac1z\right\rvert,$$
两端除以正数 $$\lvert z\rvert$$ 得 $$\lvert 1/z\rvert=1/\lvert z\rvert$$。

最后证 $$\lvert z^n\rvert=\lvert z\rvert^n$$（$$n\in\mathbb{Z}$$）。$$n\ge1$$ 用归纳：$$n=1$$ 平凡；若 $$\lvert z^n\rvert=\lvert z\rvert^n$$，则
$$\lvert z^{n+1}\rvert=\lvert z^n\cdot z\rvert=\lvert z^n\rvert\lvert z\rvert=\lvert z\rvert^{n+1}.$$
$$n=0$$：$$\lvert z^0\rvert=\lvert1\rvert=1=\lvert z\rvert^0$$。$$n<0$$ 时令 $$m=-n>0$$，则
$$\lvert z^n\rvert=\left\lvert\frac1{z^m}\right\rvert=\frac1{\lvert z^m\rvert}=\frac1{\lvert z\rvert^m}=\lvert z\rvert^n. \blacksquare$$

**解 基3.** 由推论 3.9(iii)，$$-1=e^{i\pi}$$。设 $$z=re^{i\theta}$$（$$z\ne0$$，因 $$0^4\ne-1$$；定理 3.5(iii)）。由定理 3.5(iii) 的乘法规则，
$$z^4=r^4e^{i4\theta}.$$
比较模：$$r^4=\lvert z^4\rvert=\lvert-1\rvert=1$$，又 $$r>0$$，故 $$r=1$$，即四个解都在单位圆上。比较幅角：
$$4\theta\equiv\pi\pmod{2\pi}\iff\theta=\frac\pi4+\frac{k\pi}{2},\qquad k\in\mathbb{Z}.$$
$$k$$ 取 $$0,1,2,3$$ 四个值即可（再增大 $$k$$，$$\theta$$ 只差 $$2\pi$$ 的整数倍，是同一个点；定理 3.5(iii) 的唯一性保证没有别解）。四个解是
$$z_0=e^{i\pi/4}=\frac{\sqrt2}{2}(1+i),\quad z_1=e^{3i\pi/4}=\frac{\sqrt2}{2}(-1+i),\quad z_2=e^{5i\pi/4}=\frac{\sqrt2}{2}(-1-i),\quad z_3=e^{7i\pi/4}=\frac{\sqrt2}{2}(1-i).$$
逐个核对：$$z_k^4=e^{i(\pi+2k\pi)}=e^{i\pi}=-1$$ ✓。

**对称性**。四点的模都是 $$1$$，都在单位圆上；并且相邻两个只差一个因子 $$i$$：
$$z_{k+1}=i\,z_k,\qquad z_3\cdot i=e^{i(7\pi/4+\pi/2)}=e^{i\pi/4}=z_0,$$
即相邻两点的幅角差恒为 $$\pi/2$$。由定理 3.5(i)（取 $$\theta=\frac\pi2$$，此时 $$X\left(\frac\pi2\right)=(0,1)=i$$，见定义 3.4），乘 $$i$$ 就是绕原点转 $$90^\circ$$，所以这四点是单位圆的内接正方形顶点，全部边长为 $$\lvert z_{k+1}-z_k\rvert=2\sin\frac\pi4=\sqrt2$$。由此该图形关于实轴、虚轴、原点都对称，并且在"乘 $$i$$"生成的循环群 $$\{1,i,-1,-i\}$$ 下不变。
（另一种读法：$$z^4=-1\iff z^8=1$$ 且 $$z^4\ne1$$，即这四点是八个八次单位根里去掉四个四次单位根后剩下的部分，也就是**本原八次单位根**。）

**解 基4.** 设 $$z=a+bi$$（$$a,b\in\mathbb{R}$$）。由定义 3.6，$$\bar z=a-bi$$。

- $$z=\bar z\iff a+bi=a-bi\iff 2bi=0\iff b=0\iff z\in\mathbb{R}$$。
- $$z=-\bar z\iff a+bi=-a+bi\iff 2a=0\iff a=0\iff z=bi\in i\mathbb{R}$$。

（两个等价都是"比较实部与虚部"，实部虚部相等当且仅当差为 $$0$$，用的是 $$\mathbb{C}$$ 中加法与实数乘法的定义，定义 3.3 与记号约定。）几何上，$$z\mapsto\bar z$$ 是关于实轴的反射，其不动点集正是实轴；而 $$z=-\bar z$$ 的不动点集是虚轴。$$\blacksquare$$

**解 竞1.** **关键 leap 有两处。**

第一处：**不要去硬碰 $$a^2+b^2+c^2=ab+bc+ca$$ 这个二次式，而要换变量**——把"顶点"换成"边向量" $$p=a-b,\ q=b-c,\ r=c-a$$。换完之后，"等边"这个几何条件变成 $$p,q,r$$ **等模**（三边长相等），而题设的二次式用一个恒等式恰好变成 $$p^2+q^2+r^2=0$$。两个条件都只涉及 $$p,q,r$$，就能互相翻译了。

第二处（真正的卡点）：$$a,b,c$$ 是**复数**，所以 $$p^2+q^2+r^2=0$$ **不能**推出 $$p,q,r$$ 各自为零——复数的"平方和为 $$0$$"讲的是**方向**（三项两两成 $$120^\circ$$），不是大小。正确的动作是：由 $$r=-(p+q)$$ 把三个变元压成两个，令 $$u=p/q$$，两边同除 $$q^2$$ 就得到一个**二次方程** $$u^2+u+1=0$$，解出 $$u$$ 是三次单位根，于是 $$\lvert u\rvert=1$$ 给出等模，$$u$$ 的幅角 $$\pm120^\circ$$ 给出夹角。这一步是整道题唯一"需要想到"的地方。

**证明。** 记 $$p=a-b$$、$$q=b-c$$、$$r=c-a$$，则
$$p+q+r=0,$$
且由 $$a,b,c$$ 互不相同，$$p,q,r$$ 都非零。

**(1) 题设条件改写成边向量的语言。** 展开恒等式
$$(a-b)^2+(b-c)^2+(c-a)^2=2\left(a^2+b^2+c^2-ab-bc-ca\right),$$
逐项展开左边：$$(a^2-2ab+b^2)+(b^2-2bc+c^2)+(c^2-2ca+a^2)=2(a^2+b^2+c^2)-2(ab+bc+ca)$$，与右边相同。故
$$a^2+b^2+c^2=ab+bc+ca\iff p^2+q^2+r^2=0.\tag{B}$$
另一方面 $$p,q,r$$ 是三角形的三条有向边，三角形的三边长是 $$\lvert p\rvert,\lvert q\rvert,\lvert r\rvert$$，故
$$\triangle abc\ \text{等边}\iff\lvert p\rvert=\lvert q\rvert=\lvert r\rvert.\tag{C}$$

**(2) 等模 $$\Rightarrow$$ 平方和为 $$0$$。** 设 $$\lvert p\rvert=\lvert q\rvert=\lvert r\rvert=:L>0$$。由 $$p+q=-r$$ 取模得 $$\lvert p+q\rvert=L$$，两边平方（用 $$\lvert\zeta\rvert^2=\zeta\bar\zeta$$ 与 $$\lvert p+q\rvert^2=\lvert p\rvert^2+2\operatorname{Re}(p\bar q)+\lvert q\rvert^2$$）：
$$L^2+2\operatorname{Re}(p\bar q)+L^2=L^2\Longrightarrow\operatorname{Re}(p\bar q)=-\frac{L^2}{2}.$$
令 $$u:=p/q$$（$$q\ne0$$）。由 $$\lvert u\rvert=\lvert p\rvert/\lvert q\rvert=1$$，把 $$p=uq$$ 代入得 $$p\bar q=u\lvert q\rvert^2=L^2u$$，于是 $$\operatorname{Re}u=-\frac12$$；再由 $$\lvert u\rvert=1$$ 得 $$\operatorname{Im}u=\pm\frac{\sqrt3}{2}$$，即 $$u=-\frac12\pm\frac{\sqrt3}{2}i$$，它满足
$$u^2+u+1=0\Longrightarrow p^2+pq+q^2=q^2\left(u^2+u+1\right)=0.$$
最后
$$p^2+q^2+r^2=p^2+q^2+(p+q)^2=2\left(p^2+pq+q^2\right)=0.$$

**(3) 平方和为 $$0$$ $$\Rightarrow$$ 等模。** 设 $$p^2+q^2+r^2=0$$。把 $$r=-(p+q)$$ 代入：
$$0=p^2+q^2+(p+q)^2=2\left(p^2+pq+q^2\right)\Longrightarrow p^2+pq+q^2=0.$$
令 $$u=p/q$$，得 $$u^2+u+1=0$$。两边乘 $$u-1$$：
$$u^3-1=(u-1)(u^2+u+1)=0\Longrightarrow u^3=1,$$
且 $$u\ne1$$（把 $$u=1$$ 代回得 $$3\ne0$$）。故 $$\lvert u\rvert^3=1$$，即 $$\lvert u\rvert=1$$，从而 $$\lvert p\rvert=\lvert u\rvert\lvert q\rvert=\lvert q\rvert$$。又由 $$1+u+u^2=0$$ 得 $$-(1+u)=u^2$$，于是
$$r=-(p+q)=-(u+1)q=u^2q\Longrightarrow\lvert r\rvert=\lvert u\rvert^2\lvert q\rvert=\lvert q\rvert.$$
所以 $$\lvert p\rvert=\lvert q\rvert=\lvert r\rvert$$。

(2)(3) 合起来给出 (B) $$\iff$$ (C)，即题设等式 $$\iff$$ 三角形等边。$$\blacksquare$$

**顺带**：第 (3) 步其实多给了一点信息——$$p=uq$$、$$r=u^2q$$，三个有向边依次相差一个 $$u$$（幅角 $$\pm120^\circ$$，正是等边三角形的外角）。这也说明：等边三角形的判别最终落在"三次单位根"上，与第五节题 1、题 3 用的是同一个 $$\omega$$。

**解 竞2.** **关键 leap**：两个方向各有一处，都不在计算量上。

充分性的卡点是"三点都在单位圆上"这条信息怎么用：答案是 $$\lvert z\rvert=1\Rightarrow\bar z=1/z$$（由推论 3.9(ii) 与 (v)）。于是把 $$c=-1-b$$ 代入 $$\lvert c\rvert^2=1$$ 之后，式中出现的 $$\bar b$$ 可以用 $$\bar b=1/b$$ 消掉，方程立刻退化成关于 $$\operatorname{Re}b$$ 的一次方程 $$2\operatorname{Re}b=-1$$。

必要性的卡点是"圆"从哪来：三点既然都在单位圆上，原点 $$0$$ 到三顶点等距，故 $$0$$ 就是**外心**；而等边三角形的外心与重心重合，重心是顶点算术平均——于是 $$a+b+c=0$$ 一步到位。

**充分性。** 设 $$a+b+c=0$$。由 $$\lvert a\rvert=1$$ 知 $$a\ne0$$，两边同除以 $$a$$：
$$1+\frac ba+\frac ca=0.$$
记 $$b':=\frac ba$$、$$c':=\frac ca$$。由推论 3.6，$$\lvert b'\rvert=\lvert b\rvert/\lvert a\rvert=1$$，同理 $$\lvert c'\rvert=1$$；且 $$b'+c'=-1$$，即 $$c'=-1-b'$$。由 $$\lvert c'\rvert^2=1$$：
$$1=\lvert-1-b'\rvert^2=(1+b')\overline{(1+b')}=(1+b')(1+\bar b')=1+b'+\bar b'+\lvert b'\rvert^2=2+b'+\bar b',$$
末一步用了 $$\lvert b'\rvert=1$$。于是 $$2\operatorname{Re}b'=b'+\bar b'=-1$$，即 $$\operatorname{Re}b'=-\frac12$$；又 $$\lvert b'\rvert=1$$，故
$$b'=-\frac12\pm\frac{\sqrt3}{2}i=\omega\ \text{或}\ \omega^2,\qquad\omega:=e^{2\pi i/3}$$
（$$\omega=e^{2\pi i/3}$$ 的实部正是 $$-\frac12$$，虚部为 $$+\frac{\sqrt3}{2}$$；$$\omega^2$$ 取另一个符号。$$\omega,\omega^2$$ 恰是 $$u^2+u+1=0$$ 的两根。）对应地 $$c'=-1-b'$$ 取另一个：$$b'=\omega$$ 时 $$c'=-1-\omega=\omega^2$$。所以
$$\{1,b',c'\}=\{1,\omega,\omega^2\}.$$

再看这个三角形：三点都在单位圆上，相邻幅角差为 $$\frac{2\pi}{3}$$，用恒等式 $$\lvert1-e^{i\psi}\rvert=2\lvert\sin\frac\psi2\rvert$$（几何上就是单位圆上两点的弦长，可由 $$1-e^{i\psi}=-2ie^{i\psi/2}\sin\frac\psi2$$ 得到），
$$\lvert1-\omega\rvert=2\sin\frac\pi3=\sqrt3,\quad\lvert\omega-\omega^2\rvert=\lvert\omega\rvert\lvert1-\omega\rvert=\sqrt3,\quad\lvert1-\omega^2\rvert=2\sin\frac{2\pi}{3}=\sqrt3.$$
三边等长，故 $$\{1,\omega,\omega^2\}$$ 是正三角形。最后由定理 3.5(i)，$$z\mapsto az$$（$$\lvert a\rvert=1$$）是绕原点的旋转，而 $$\{a,b,c\}=a\cdot\{1,b',c'\}$$，旋转保持一切距离，故 $$\{a,b,c\}$$ 也是正三角形。

**必要性。** 设 $$\triangle abc$$ 等边。三点都在 $$\lvert z\rvert=1$$ 上，故 $$\lvert0-a\rvert=\lvert0-b\rvert=\lvert0-c\rvert=1$$，即原点 $$0$$ 到三顶点等距，是外心（到三个不共线点等距的只有一个点；而 $$a,b,c$$ 都在一个圆上，就不可能共线——一条直线与圆至多交于两点）。等边三角形的外心与重心重合：沿一条中线剪开所得两个小三角形有两组对应边相等、公共边相等（SSS），故中线垂直于对边，即三条中线就是三条垂直平分线，其交点（重心）到三顶点等距，正是外心。而重心是顶点坐标的算术平均，于是
$$\frac{a+b+c}{3}=0\Longrightarrow a+b+c=0. \blacksquare$$

**解 竞3.** **关键 leap**：把 $$\sin\frac{k\pi}{n}$$ 认出来——它是**单位圆上两点之间弦长的一半**，即
$$\lvert 1-e^{i\psi}\rvert=2\left\lvert\sin\frac\psi2\right\rvert.$$
用这条恒等式，正弦的连乘积就变成 $$\lvert1-\zeta^k\rvert$$ 的连乘积；而后者由第五节题 3(i) 的因式分解令 $$x=1$$ 直接给出，一步到位。整道题只需要"分解 $$x^n-1$$、令 $$x=1$$、两边取模"三下，不需要任何求和技巧。

（第二个小卡点本来是符号：如果走"先算乘积的平方、再开方"的路，就要论证 $$\sin\frac{k\pi}{n}>0$$。下面这条路从头到尾只对非负的模取等式，**符号问题根本不出现**。）

**证明。** 设 $$\zeta=e^{2\pi i/n}$$。由第五节题 3(i)（已证）：
$$x^n-1=\prod_{k=0}^{n-1}\left(x-\zeta^k\right).$$
两边除以 $$x-1$$（用 $$\zeta^0=1$$ 与 $$x^n-1=(x-1)(1+x+\dots+x^{n-1})$$）：
$$1+x+\dots+x^{n-1}=\prod_{k=1}^{n-1}\left(x-\zeta^k\right).$$
令 $$x=1$$，左边是 $$n$$：
$$n=\prod_{k=1}^{n-1}\left(1-\zeta^k\right).$$
两边取模，并用模的乘性（推论 3.6）：
$$n=\left\lvert\prod_{k=1}^{n-1}\left(1-\zeta^k\right)\right\rvert=\prod_{k=1}^{n-1}\left\lvert1-\zeta^k\right\rvert.$$
对每个 $$1\le k\le n-1$$，写 $$\psi=\frac{2\pi k}{n}\in(0,2\pi)$$，则 $$\frac\psi2=\frac{k\pi}{n}\in(0,\pi)$$，故 $$\sin\frac{k\pi}{n}>0$$，于是
$$\left\lvert1-\zeta^k\right\rvert=\left\lvert1-e^{i\psi}\right\rvert=2\left\lvert\sin\frac\psi2\right\rvert=2\sin\frac{k\pi}{n}.$$
代回：
$$n=2^{\,n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}\Longrightarrow\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}=\frac{n}{2^{\,n-1}}.$$
（核对 $$n=2$$：左边 $$\sin\frac\pi2=1$$，右边 $$\frac22=1$$ ✓；$$n=3$$：左边 $$\frac{\sqrt3}{2}\cdot\frac{\sqrt3}{2}=\frac34$$，右边 $$\frac34$$ ✓。）$$\blacksquare$$

**解 竞4.** **关键 leap**：正方形中心有一个**统一**的写法，不必分四种情形画图。把边看成有向段 $$x\to y$$，绕 $$x$$ 逆时针转 $$90^\circ$$ 就是乘 $$i$$（定理 3.5(i) 取 $$\theta=\frac\pi2$$，其中 $$X\left(\frac\pi2\right)=i$$；定义 3.4），于是中心是"中点加上半个转好的边向量"：
$$m=\frac{x+y}{2}+\frac i2(y-x)=\frac{(1-i)x+(1+i)y}{2}.$$
第二个 leap：要证的"垂直且等长"本身可以整体写成一个复等式 $$m_1-m_3=i\,(m_2-m_4)$$（乘 $$i$$ 是转 $$90^\circ$$，取模是长度）。换成这个形式之后，$$a,b,c,d$$ 会自动两两相消——四个中心的转向只要统一，正负号就不必操心。

**证明。** 设四边形的四顶点依次为 $$a,b,c,d$$。约定四个正方形都长在同一个转向的一侧（例如都长在有向边 $$a\to b$$、$$b\to c$$、$$c\to d$$、$$d\to a$$ 的左侧；长在右侧是镜像情形，见后面的说明）。由上面的公式，四个中心依次是
$$m_1=\frac{(1-i)a+(1+i)b}{2},\quad m_2=\frac{(1-i)b+(1+i)c}{2},\quad m_3=\frac{(1-i)c+(1+i)d}{2},\quad m_4=\frac{(1-i)d+(1+i)a}{2}.$$
（核对公式：取 $$a=0,b=1$$，得 $$m_1=\frac{1+i}{2}=\frac12+\frac i2$$，正是边 $$0\to1$$ 上正方形 $$0,1,1+i,i$$ 的中心。）

记 $$X:=a-c$$、$$Y:=b-d$$。把 $$m_1-m_3$$ 与 $$m_2-m_4$$ 算出来：
$$m_1-m_3=\frac{(1-i)(a-c)+(1+i)(b-d)}{2}=\frac{(1-i)X+(1+i)Y}{2},$$
$$m_2-m_4=\frac{(1-i)(b-d)+(1+i)(c-a)}{2}=\frac{(1-i)Y-(1+i)X}{2}.$$
对第二式乘 $$i$$：
$$i\,(m_2-m_4)=\frac{i(1-i)Y-i(1+i)X}{2}=\frac{(1+i)Y+(1-i)X}{2}=m_1-m_3,$$
中间两步用了 $$i(1-i)=i-i^2=1+i$$ 与 $$-i(1+i)=-i-i^2=1-i$$。于是
$$m_1-m_3=i\,(m_2-m_4).$$
由定理 3.5(i)（$$i=X\left(\frac\pi2\right)$$，定义 3.4），乘 $$i$$ 是逆时针转 $$90^\circ$$，故直线 $$M_1M_3\perp M_2M_4$$；又由推论 3.6，$$\lvert m_1-m_3\rvert=\lvert i\rvert\cdot\lvert m_2-m_4\rvert=\lvert m_2-m_4\rvert$$，即两线段等长。$$\blacksquare$$

**两点说明。** 其一，整个证明对 $$a,b,c,d$$ 不作任何假设——四边形可以不凸、可以自交，因为只用到了乘法分配律。其二，若四个正方形都改画在另一侧，则四个中心公式里的 $$i$$ 都要换成 $$-i$$，上式随之变成 $$m_1-m_3=-i\,(m_2-m_4)$$，同样给出垂直且等长。

**解 竞5.** **关键 leap**：把"垂直"翻译成一个复数方程。点 $$z$$ 落在"过 $$a$$ 且垂直于 $$bc$$"的直线上，当且仅当
$$\frac{z-a}{b-c}\in i\mathbb{R}\iff\frac{z-a}{b-c}=-\overline{\left(\frac{z-a}{b-c}\right)},$$
（因为 $$\xi\in i\mathbb{R}\iff\xi=-\bar\xi$$。）第二个卡点是这个方程里出现的 $$\bar z$$ 看起来很碍事：但三点都在单位圆上时 $$\bar x=1/x$$（推论 3.9(ii)），代进去后分母变成 $$(b-c)$$ 的常数倍，方程整理成 $$\bar z$$ 的**一次式**，把候选 $$h=a+b+c$$ 一验就完事了。第三步的关键观察是：这个一次式对 $$a,b,c$$ 是**轮换对称**的，所以验一次等于验三次。

**证明。** 设 $$\lvert a\rvert=\lvert b\rvert=\lvert c\rvert=1$$，且 $$a,b,c$$ 互不相同（特别地 $$b\ne c$$，故以下分母都不为零）。

**(1) 一条高的方程。** 设 $$z\in\mathbb{C}$$。由共轭的基本性质（定义 3.6，逐分量验证）$$\overline{\xi/\eta}=\bar\xi/\bar\eta$$，条件 $$\frac{z-a}{b-c}=-\overline{\left(\frac{z-a}{b-c}\right)}$$ 即
$$\frac{z-a}{b-c}=-\frac{\bar z-\bar a}{\bar b-\bar c}.$$
由推论 3.9(ii) 与 (v)，单位复数取共轭就是取倒数：若 $$\lvert x\rvert=1$$ 则 $$x=e^{i\theta}$$，故 $$\bar x=e^{-i\theta}=1/x$$。于是 $$\bar a=\frac1a,\ \bar b=\frac1b,\ \bar c=\frac1c$$，从而
$$\bar b-\bar c=\frac1b-\frac1c=\frac{c-b}{bc}=-\frac{b-c}{bc}.$$
代入并化简右边：
$$-\frac{\bar z-\bar a}{\bar b-\bar c}=\frac{bc\,(\bar z-\bar a)}{b-c}.$$
两边乘 $$b-c$$（非零），得
$$z-a=bc\,\bar z-bc\,\bar a\iff z-bc\,\bar z=a-bc\,\bar a.\tag{D}$$
注意 $$bc\,\bar a=\frac{bc}{a}$$。所以
$$\text{点 }z\text{ 落在过 }a\text{ 的高上}\iff\text{(D)}.$$

**(2) $$h$$ 满足 (D)。** 直接代入。先用共轭保加法（定义 3.6）得 $$\bar h=\bar a+\bar b+\bar c$$，于是
$$h-bc\,\bar h=(a+b+c)-bc\left(\frac1a+\frac1b+\frac1c\right)=(a+b+c)-\frac{bc}{a}-c-b=a-\frac{bc}{a}=a-bc\,\bar a,$$
其中用了 $$bc\cdot\frac1b=c$$、$$bc\cdot\frac1c=b$$。这正是 (D)，故 $$h$$ 在过 $$a$$ 的高上。

**(3) 三条高都过 $$h$$。** 把 (2) 的计算在 $$a,b,c$$ 上轮换（$$a$$ 配 $$bc$$、$$b$$ 配 $$ca$$、$$c$$ 配 $$ab$$），逐字得到
$$h-bc\,\bar h=a-bc\,\bar a,\qquad h-ca\,\bar h=b-ca\,\bar b,\qquad h-ab\,\bar h=c-ab\,\bar c,$$
三条都是同一次对消。而"过 $$b$$ 的高"与"过 $$c$$ 的高"对应的方程分别是第二、第三条，故 $$h$$ 同时在三条高上。三条高中任意两条必相交：过 $$a$$ 的高与过 $$b$$ 的高分别垂直于 $$bc$$ 与 $$ca$$，若二者平行则 $$bc\parallel ca$$，即 $$b=a$$（两边约去单位复数 $$c$$），与互不相同矛盾。所以三条高交于唯一一点，即垂心
$$h=a+b+c.$$

**(4) 欧拉线 (Euler line)。** 重心是顶点算术平均：
$$g=\frac{a+b+c}{3}=\frac h3.$$
外心是原点：$$\lvert0-a\rvert=\lvert0-b\rvert=\lvert0-c\rvert=1$$，而到三个不共线点等距的只有一个点。于是 $$\vec{OG}=\frac13\vec{OH}$$，故 $$O,G,H$$ 共线，且 $$OG:GH=1:2$$。$$\blacksquare$$

**顺带**：这个 $$a+b+c$$ 既是"重心的三倍"，又是垂心——第五节题 1 的"顺带"结论（$$c_1+c_2+c_3=a+b+c$$）里出现的是同一个量。这不是巧合：在单位圆上的三角形里，$$a+b+c$$ 是整章反复出现的"顶点和"的化身。

**解 研1.** (a) **没有实特征值。** 反设存在 $$\lambda\in\mathbb{R}$$ 与 $$v\ne0$$ 满足 $$R_\theta v=\lambda v$$，则 $$v$$ 是齐次方程组 $$(R_\theta-\lambda I)v=0$$ 的非零解，故系数矩阵奇异：
$$\det(R_\theta-\lambda I)=0.$$
由 3.1 节的 $$R_\theta=\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix}$$，
$$\det\begin{pmatrix}\cos\theta-\lambda & -\sin\theta\\ \sin\theta & \cos\theta-\lambda\end{pmatrix}=(\cos\theta-\lambda)^2+\sin^2\theta.$$
这是两个非负实数之和，等于 $$0$$ 必须两者同时为零：$$\sin\theta=0$$ 且 $$\lambda=\cos\theta$$。但 $$\sin\theta=0$$ 给出 $$\theta\in\pi\mathbb{Z}$$，与假设矛盾。故 $$\mathbb{R}$$ 上没有这样的 $$\lambda$$。

实特征向量同样不存在：若 $$v\ne0$$ 是实向量且 $$R_\theta v=\lambda v$$，取 $$v$$ 的某个非零分量 $$v_i$$，则 $$\lambda=\frac{(R_\theta v)_i}{v_i}$$ 是两个实数之比，必为实数——这就回到上面排除过的情形。几何读法：$$\theta$$ 不是 $$\pi$$ 的整数倍时，旋转不把任何一条过原点的直线映到自身。

(b) **复特征值。** 把 $$\lambda$$ 看成复变量，特征多项式是
$$\chi(\lambda)=\det(R_\theta-\lambda I)=(\cos\theta-\lambda)^2+\sin^2\theta=\lambda^2-2\cos\theta\,\lambda+1.$$
由求根公式，
$$\lambda_\pm=\frac{2\cos\theta\pm\sqrt{4\cos^2\theta-4}}{2}=\cos\theta\pm\sqrt{\cos^2\theta-1}=\cos\theta\pm i\lvert\sin\theta\rvert,$$
其中 $$\cos^2\theta-1=-\sin^2\theta$$，而 $$\sin\theta\ne0$$，故 $$\sqrt{-\sin^2\theta}=\pm i\lvert\sin\theta\rvert\ne0$$。两个根合起来正好是 $$\{e^{i\theta},e^{-i\theta}\}$$：若 $$\sin\theta>0$$，则 $$\cos\theta\pm i\lvert\sin\theta\rvert=\cos\theta\pm i\sin\theta=e^{\pm i\theta}$$；若 $$\sin\theta<0$$，两个根只是符号互换，集合仍是 $$\{e^{i\theta},e^{-i\theta}\}$$（由 Euler 公式，定理 3.9）。

**特征向量。** 对 $$\lambda_+=e^{i\theta}=\cos\theta+i\sin\theta$$，
$$R_\theta-\lambda_+I=\begin{pmatrix}-i\sin\theta & -\sin\theta\\ \sin\theta & -i\sin\theta\end{pmatrix},$$
第一行给出 $$-i\sin\theta\,x-\sin\theta\,y=0$$；因 $$\sin\theta\ne0$$，即 $$y=-ix$$。所以 $$\lambda_+=e^{i\theta}$$ 的全部特征向量是
$$v=t\begin{pmatrix}1\\-i\end{pmatrix},\qquad 0\ne t\in\mathbb{C}.$$
核对：$$R_\theta\begin{pmatrix}1\\-i\end{pmatrix}=\begin{pmatrix}\cos\theta+i\sin\theta\\ \sin\theta-i\cos\theta\end{pmatrix}=e^{i\theta}\begin{pmatrix}1\\-i\end{pmatrix}$$（第二行：$$-i\,e^{i\theta}=-i\cos\theta+\sin\theta$$ ✓）。
同理，$$\lambda_-=e^{-i\theta}$$ 的特征向量是 $$v=t(1,i)^{\mathsf T}$$：
$$R_\theta\begin{pmatrix}1\\ i\end{pmatrix}=\begin{pmatrix}\cos\theta-i\sin\theta\\ \sin\theta+i\cos\theta\end{pmatrix}=e^{-i\theta}\begin{pmatrix}1\\ i\end{pmatrix}.$$
即特征向量确实与 $$(1,\pm i)$$ 有关。

(c) **在复基下对角化。** 记
$$v_+=\begin{pmatrix}1\\-i\end{pmatrix},\qquad v_-=\begin{pmatrix}1\\ i\end{pmatrix}.$$
它们线性无关（若 $$\alpha v_++\beta v_-=0$$，第二行给 $$-i\alpha+i\beta=0$$，即 $$\alpha=\beta$$；第一行给 $$\alpha+\beta=0$$；合起来 $$\alpha=\beta=0$$）。把两列拼成 $$P=\begin{pmatrix}1 & 1\\ -i & i\end{pmatrix}$$，则 $$P$$ 可逆，且按列作用（$$P$$ 的两列正是特征向量）立刻得到
$$P^{-1}R_\theta P=\begin{pmatrix}e^{i\theta} & 0\\ 0 & e^{-i\theta}\end{pmatrix}.$$
也就是说：在实标准基下 $$R_\theta$$ 是"转 $$\theta$$"，在复特征基下它变成**两个互不干扰的纯伸缩**，伸缩因子分别是 $$e^{i\theta}$$ 与 $$e^{-i\theta}$$。核对两个不变量：迹 $$e^{i\theta}+e^{-i\theta}=2\cos\theta$$、行列式 $$e^{i\theta}e^{-i\theta}=1$$，与直接算 $$R_\theta$$ 的结果一致。

**与 $$M_{e^{i\theta}}$$ 对照。** 由定理 3.5(i)，$$M_{e^{i\theta}}=M_{X(\theta)}=R(\theta)$$，两者作为实 $$2\times2$$ 矩阵**逐元素相同**。差别在于我们把同一张表当成什么：

- 当成 $$\mathbb{R}$$-线性算子（2 维实空间）时，它一个实特征方向都没有；
- 把 $$\mathbb{C}$$ 看成 1 维复空间、把它看成 $$z\mapsto e^{i\theta}z$$（即 $$M_{e^{i\theta}}$$ 的本来身份）时，它**只有一个**特征值 $$e^{i\theta}$$，而且每个非零 $$z\in\mathbb{C}$$ 都是特征向量——取 $$\lambda=e^{i\theta}$$，等式 $$e^{i\theta}z=\lambda z$$ 对一切 $$z$$ 恒成立。

于是那句话的意思就清楚了：$$R_\theta$$ 的"伸缩方向"确实存在，但它们是**复的**，就是 $$v_+$$ 与 $$v_-$$；要在实平面里找一个实特征方向，等于要求一个复方向恰好落进实子空间，当然找不到。而两个伸缩因子 $$e^{\pm i\theta}$$ 的模都是 $$1$$——所谓"伸缩"其实仍是旋转，只不过在复方向上，旋转被看成了一件"乘一个数"的平常事。

最后一个核对（实域里为什么看不见这两个因子）：实矩阵的两个基本不变量是 $$e^{i\theta}$$ 与 $$e^{-i\theta}$$ 的**和**与**积**，
$$\operatorname{tr}R_\theta=2\cos\theta=e^{i\theta}+e^{-i\theta},\qquad\det R_\theta=1=e^{i\theta}\cdot e^{-i\theta},$$
它们在实域里正好是二次多项式 $$\lambda^2-2\cos\theta\,\lambda+1$$ 的系数；而 $$\sin\theta\ne0$$ 时它的判别式 $$4\cos^2\theta-4=-4\sin^2\theta<0$$——没有实根。实域只允许我们看到这两个复伸缩因子的对称组合，看不到它们各自。

**接下一章**：上面这套计算就是第 04 章的开场——把 $$R_\theta$$ 放到复特征基下对角化，得到的就是它的**谱 (spectrum)** $$\{e^{i\theta},e^{-i\theta}\}$$。第 04 章会回答这里留下的两个问题：为什么"谱"比"特征值集合"更基本（在无限维里两者会分家），以及 $$SO(2)$$ 的谱为什么恰好铺满单位圆——那正是下一章的起点。

**解 研2.** **关键 leap**：不要试图直接去"解"函数方程 $$\gamma(s+t)=\gamma(s)\gamma(t)$$——那不是代数方程。正确的动作是**先证明 $$\gamma$$ 可导**（连续性是全部假设，而连续性居然够用，这是这题的意外之处），把它变成一个微分方程 $$\gamma'=c\gamma$$，而后者有唯一解 $$e^{ct}$$。证明可导的工具只是一个积分：同态性能把一个积分恒等式变成 $$\gamma$$ 的显式表达式。

**证明（五步）。**

**第一步：$$\gamma(0)=1$$。** 由同态性，$$\gamma(0)=\gamma(0+0)=\gamma(0)^2$$，即 $$\gamma(0)\left(\gamma(0)-1\right)=0$$。而 $$\gamma$$ 取值在 $$S^1$$ 中，$$\lvert\gamma(0)\rvert=1\ne0$$，故 $$\gamma(0)=1$$。

**第二步：积分恒等式。** 因 $$\gamma$$ 连续，$$G(t):=\int_0^t\gamma(s)\,ds$$ 对一切 $$t\in\mathbb{R}$$ 有意义，且由微积分基本定理 $$G$$ 可导、$$G'=\gamma$$。断言：对一切 $$t,\varepsilon\in\mathbb{R}$$，
$$G(t+\varepsilon)-G(t)=\gamma(t)G(\varepsilon).\tag{E}$$
证明：作换元 $$u=t+s$$（$$du=ds$$，$$s$$ 从 $$0$$ 到 $$\varepsilon$$），
$$G(t+\varepsilon)-G(t)=\int_t^{t+\varepsilon}\gamma(u)\,du=\int_0^{\varepsilon}\gamma(t+s)\,ds=\int_0^{\varepsilon}\gamma(t)\gamma(s)\,ds=\gamma(t)\int_0^{\varepsilon}\gamma(s)\,ds=\gamma(t)G(\varepsilon),$$
第三、四步分别用了同态性与积分的线性。$$\varepsilon<0$$ 时有向积分的定义让整条链逐字成立。

**第三步：$$\gamma$$ 可导。** 由 $$G'(0)=\gamma(0)=1$$ 与导数的定义，
$$\frac{G(\varepsilon)}{\varepsilon}=\frac{G(\varepsilon)-G(0)}{\varepsilon}\xrightarrow[\varepsilon\to0]{}1.$$
取 $$\varepsilon_0\ne0$$ 小到 $$\left\lvert\frac{G(\varepsilon_0)}{\varepsilon_0}-1\right\rvert<\frac12$$，则 $$\lvert G(\varepsilon_0)\rvert>\frac{\lvert\varepsilon_0\rvert}{2}>0$$，特别地 $$G(\varepsilon_0)\ne0$$。在 (E) 中取 $$\varepsilon=\varepsilon_0$$ 并解出 $$\gamma(t)$$：
$$\gamma(t)=\frac{G(t+\varepsilon_0)-G(t)}{G(\varepsilon_0)}.$$
右端是 $$t$$ 的可导函数（$$G$$ 是 $$C^1$$），故 $$\gamma$$ 可导，且
$$\gamma'(t)=\frac{G'(t+\varepsilon_0)-G'(t)}{G(\varepsilon_0)}=\frac{\gamma(t+\varepsilon_0)-\gamma(t)}{G(\varepsilon_0)}=\gamma(t)\cdot\frac{\gamma(\varepsilon_0)-1}{G(\varepsilon_0)}=c\,\gamma(t),$$
其中 $$c:=\dfrac{\gamma(\varepsilon_0)-1}{G(\varepsilon_0)}\in\mathbb{C}$$ 与 $$t$$ 无关（第三步又用了一次同态性 $$\gamma(t+\varepsilon_0)=\gamma(t)\gamma(\varepsilon_0)$$）。

**第四步：解方程。** 令 $$F(t):=\gamma(t)e^{-ct}$$。由乘积法则与第三步，
$$F'(t)=\gamma'(t)e^{-ct}-c\,\gamma(t)e^{-ct}=\left(\gamma'(t)-c\,\gamma(t)\right)e^{-ct}=0.$$
导数恒为零的可导函数是常数（中值定理推论，与定理 3.9 路一用的是同一条），故
$$F(t)\equiv F(0)=\gamma(0)e^{0}=1\Longrightarrow\gamma(t)=e^{ct}.$$

**第五步：定出 $$c$$。** $$\gamma$$ 的值都在 $$S^1$$ 上，故对一切 $$t\in\mathbb{R}$$，
$$1=\lvert\gamma(t)\rvert=\left\lvert e^{ct}\right\rvert=e^{t\operatorname{Re}c}.$$
取 $$t=1$$ 得 $$e^{\operatorname{Re}c}=1$$，故 $$\operatorname{Re}c=0$$；写 $$c=i\omega$$（$$\omega=\operatorname{Im}c\in\mathbb{R}$$），即得题断
$$\gamma(t)=e^{i\omega t}. \blacksquare$$

**补一句反方向。** 反过来，每个 $$\gamma(t)=e^{i\omega t}$$（$$\omega\in\mathbb{R}$$）确实是连续群同态：同态性是定理 3.7（指数律），连续性是复指数函数的连续性。所以上面的分类是**恰好**的。又因 $$e^{2\pi i}=1$$（推论 3.9(iii)），$$\omega$$ 与 $$\omega+2\pi$$ 给出同一个 $$\gamma$$，故这类同态被 $$\omega\in\mathbb{R}/2\pi\mathbb{Z}\cong S^1$$ 一一参数化。
（另有一条路——先用 $$\gamma(t)^n=\gamma(nt)$$ 定出 $$\gamma$$ 在 $$\mathbb{Q}$$ 上的值，再用连续性把 $$t\in\mathbb{R}$$ 用有理数逼近——也能走通，但中间要先花力气排除"模长不取 $$\lvert\gamma(1)\rvert^q$$"的坏分支；上面这条积分—ODE 的路把这件事交给微分方程解的唯一性一次解决。）

**接下一章**：第三步真正做的事情，是把 $$\gamma$$ 在单位元 $$0$$ 处**线性化**——得到的是**一个数** $$c=i\omega$$，而 $$\gamma$$ 被这个数完全决定。第 04 章会把同一种"在不动点处只看线性部分"的动作用到旋转算子身上：那里被线性化的是旋转 $$R_\theta$$ 本身，它交出来的数就是它的谱 $$\{e^{i\theta},e^{-i\theta}\}$$——群的线性化给出一个数，算子的线性化给出一对数，两者是同一个动作在不同尺度上的样子。（这个"线性化"一路长下去就是 Lie 代数与 Lie 群，第 20–23 章。）

## 七、Takeaway 与延伸 (Takeaways)

1. **三条"定义"是一条定理的三张脸。** $$i^2=-1$$、复数乘法法则、Euler 公式不是互相独立的公理；它们全都是同一个几何事实——**平面旋转群 $$SO(2)$$** ——在代数记号下的显形。本章的顺序（旋转 $$\to$$ 乘法 $$\to$$ 指数）比教材的顺序（公理 $$\to$$ 计算）多花了一点力气，换来的是"为什么"。

2. **复数乘法的内容是"模相乘、幅角相加"，其矩阵形式是 $$M_z=\begin{pmatrix}a & -b\\ b & a\end{pmatrix}$$。** 乘以 $$z$$ 就是"转 $$\arg z$$、伸 $$\lvert z\rvert$$"。由此立刻得到模的乘性 $$\lvert zw\rvert=\lvert z\rvert\lvert w\rvert$$ 与保角性。把"数"和"线性变换"绑定（$$\phi:z\mapsto M_z$$）是从这一步开始贯穿全书的动作。

3. **Euler 公式最经济的证法是唯一性**：$$e^{i\theta}$$ 与 $$\cos\theta+i\sin\theta$$ 都满足 $$X'=iX,\ X(0)=1$$。这里的 $$i$$ 是求导算子 $$\frac{d}{d\theta}$$ 作用在 $$e^{i\theta}$$ 上的**特征值**。记住这句话，第 04 章、第 15–17 章的谱理论都从这里长出来。

4. **$$\exp:\mathbb{R}\to S^1$$ 是同态，核是 $$2\pi\mathbb{Z}$$，给出 $$SO(2)\cong S^1\cong U(1)\cong\mathbb{R}/2\pi\mathbb{Z}$$。** "加法群被卷到圆上"这件事是覆叠理论、相位多值性、日后覆盖群与表示论的共同种子。

5. **物理上：实指数是衰减，虚指数是振荡，$$e^{(a+i\omega)t}$$ 是两者的统一。** 相量法、角速度 $$\dot z=i\omega z$$、多缝干涉的 $$(\sin(n\theta/2)/\sin(\theta/2))^2$$，都是同一个复指数在不同外衣下的样子。

**下一章悬念**：研究题 1 埋了引线——旋转矩阵 $$R_\theta$$ 在实方向上"看不见"特征方向，可一旦允许复特征值，它立刻分裂成两个伸缩方向，因子是 $$e^{\pm i\theta}$$。第 04 章就把这件事讲透：什么是算子的**谱 (spectrum)**，为什么"谱"比"特征值集合"更基本（无限维里谱可以连续），以及 $$SO(2)$$ 的谱为什么恰好铺满单位圆。

**延伸阅读**：

- Lars Ahlfors,《Complex Analysis》第 1 章。复数几何与拓扑的经典处理，紧凑、严格。
- Stein & Shakarchi,《Complex Analysis》第 1 章。Euler 公式与"收敛半径由复平面上的奇点决定"的第一印象。
- Tristan Needham,《Visual Complex Analysis》第 1 章。把"乘法 $$=$$ 旋转 $$+$$ 伸缩"画成图，与本章 §四完全同构。
- Квант 杂志复数几何专题；任何一本奥赛几何教材里的"旋转法"章节。对照题 1 的综合几何解法与复数解法，看两者的分工。
---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch01_复平面与_Euler_公式_上.md">← 第01章 复平面与 Euler 公式·上</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch03_平面旋转群_SO_2_与算子的谱_上.md">第03章 平面旋转群 SO(2) 与算子的谱·上 →</a></div>
</div>
