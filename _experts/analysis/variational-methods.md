# 变分法 (Calculus of Variations)

> 整理自 Jean-Pierre Bourguignon《Calcul variationnel》(École Polytechnique；法文原著 2007 / 英文版 Springer 2022)。全书三部分：分析框架（无限维空间、Banach/Hilbert、可微映射的线性化）→ 几何框架（构型空间、切向量、临界点）→ 变分法本身（Euler–Lagrange 方程、Hamilton 观点、对称性与守恒律）。

## 0. 一句话定位

变分法解决的核心问题是：当极值问题的"变量"是**一整条曲线或一张曲面**（而非一个向量）时，如何在无限维、通常还是弯曲的空间上严格地做微分、求极值、证存在性，并把结果化成一个可解的微分方程。主线：**空间推广 + 逐字微积分**——先把空间从 $\mathbb{R}^n$ 推广到无限维 Banach/Hilbert 空间，再从向量空间推广到流形，最后把有限维微积分的全部工具（导数、极值、约束、对称）逐字搬运到"曲线构成的无限维流形"上。

**核心洞察**：

- 变分法的舞台是无限维函数空间，**"有界闭集紧"（Heine–Borel）彻底失效**——这是必须引入 Banach/Hilbert 结构的根因；**完备性**是证明极小值存在的第一道关口。
- Hilbert 空间的内积带来正交投影与 Riesz 表示，把"泛函的导数"翻译成"一个梯度向量"——这正是 Euler–Lagrange 方程的代数根。
- "线性化决定局部行为"：反函数/隐函数定理（Banach 不动点/压缩映射原理）是机械化工具。
- **V-直接法**（变分法直接法）：极小化序列有界 → Banach–Alaoglu 取弱收敛子列 → 泛函弱下半连续 → 极限点即极小点。
- **Noether 定理**：连续对称 ⟺ 守恒律。

---

## 1. 分析框架：无限维空间与微分学

**无限维的危机**：$\mathbb{R}^n$ 里 Heine–Borel（有界闭集紧）保证了极值存在；无限维里不成立（$\ell^2$ 单位球有界闭但不紧）。补救：**弱拓扑** + 自反性 + Banach–Alaoglu。完备性则是所有极限论证的地基（$C^0$ 在 sup 范数下完备、Riemann 可积空间不完备，逼出 $L^p$ 与 Sobolev 空间）。

**Banach 与 Hilbert 空间**：Banach = 完备赋范空间；Hilbert = 完备内积空间。Hilbert 空间的关键工具：**Riesz 表示定理**（每个连续泛函由内积表示，$H\cong H^*$）、**正交投影**、**Lax–Milgram 定理**（双线性型有界 + 强制 $\Rightarrow$ 方程有唯一解——椭圆 PDE 弱解的基石）、**Banach–Alaoglu**（$X^*$ 单位球弱\*紧，用于取弱收敛子列）。**Sobolev 空间** $H^1$ 是变分法的标准定义域（完备、含导数信息、极小化序列在此收敛）。

**Fréchet 与 Gâteaux 导数**：Gâteaux 导数 = 沿方向的方向导数（作用量的一阶变分本质是它）；Fréchet 导数更强（一致逼近）。**Fréchet 可微 $\Rightarrow$ Gâteaux 可微，反之不成立**。要动用反函数/隐函数定理时必须有更强的 Fréchet 可微。

**反函数 / 隐函数定理**：导数可逆 $\Rightarrow$ 局部可逆；正则方程局部可解。均由 Banach 不动点 / 压缩映射原理证明。**淹没定理（正则值原像）** 把"方程定义的集合"升级为"子流形"——构造构型空间与约束流形的标准手法。

**无约束/约束极值**：**Lagrange 乘子法**的核心条件是**约束正则性**（$Dg$ 满射）；变分法的等周问题本质是无限维的 Lagrange 乘子法。**凸性 + 强制条件**保证极小值存在。

---

## 2. 几何框架：流形与临界点

**构型空间**：拓扑/光滑流形（局部 $\mathbb{R}^n$ + 光滑转移映射），是"可做微积分的弯曲空间"。力学位形空间（$SO(3)$、环面、约束曲面）是变分法的自然定义域。

**切向量与向量场**：切空间（曲线等价类 / 导子两种等价刻画）、切丛、向量场与流、**Lie 括号**（度量流的可交换性）。**Frobenius 定理**判定一个约束分布能否积分成曲面（完整约束理论）。

**临界点理论**：**Sard 定理**（正则值几乎处处）；**Morse 引理**（非退化临界点局部等价于标准二次型，指标 = 下降方向个数）。二者是二阶变分判别法的几何本质，并把临界点结构与流形拓扑（欧拉数）联系起来。

---

## 3. Euler–Lagrange 方程

**作用量泛函**：给定 Lagrange 函数 $L:[a,b]\times\mathbb{R}^n\times\mathbb{R}^n\to\mathbb{R}$（变量 $t,q,\dot q$），$S[q]=\int_a^bL(t,q(t),\dot q(t))dt$，在固定端点路径空间上求极值。

**一阶变分**：对扰动 $q+\varepsilon\eta$（$\eta(a)=\eta(b)=0$），

$$\delta S[q;\eta]=\frac{d}{d\varepsilon}\Big|_{\varepsilon=0}S[q+\varepsilon\eta]=\int_a^b\left(\frac{\partial L}{\partial q}\cdot\eta+\frac{\partial L}{\partial\dot q}\cdot\dot\eta\right)dt.$$

**分部积分**（用 $\eta(a)=\eta(b)=0$ 消边界项）：

$$\delta S[q;\eta]=\int_a^b\left(\frac{\partial L}{\partial q}-\frac{d}{dt}\frac{\partial L}{\partial\dot q}\right)\cdot\eta\,dt.$$

**定理（变分法基本引理）**：$f\in C^0([a,b])$ 且 $\int_a^bf\eta=0$ 对一切光滑紧支 $\eta$ 成立，则 $f\equiv0$。

**定理（Euler–Lagrange 方程）**：$q$ 是 $S$ 的 $C^2$ 极值点 $\Rightarrow$

$$\boxed{\ \frac{\partial L}{\partial q_i}-\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}=0,\qquad i=1,\dots,n\ }$$

这是关于 $q(t)$ 的**二阶常微分方程组**。

**自然边界条件**：端点不固定时，边界项 $[\frac{\partial L}{\partial\dot q}\cdot\eta]_a^b$ 要求 $\frac{\partial L}{\partial\dot q}\big|_{t=a}=\frac{\partial L}{\partial\dot q}\big|_{t=b}=0$。物理上 $\partial L/\partial\dot q$ 是**广义动量**，故自由端点处动量为零。

**Legendre 条件（二阶必要条件）**：二阶变分 $\delta^2S=\int(\frac{\partial^2L}{\partial\dot q^2}[\eta',\eta']+\cdots)dt$，极小值必要条件 $\frac{\partial^2L}{\partial\dot q^2}\succeq0$（$L$ 关于速度凸）。

**典型例子**：

1. **测地线**：$L=\frac12\lVert\dot q\rVert^2$（能量），$\mathbb{R}^n$ 中给出 $\ddot q=0$（直线），曲面上给出测地线方程；
2. **最速降线 (brachistochrone)**：$L=\sqrt{(1+\dot y^2)/2gy}$，解为**旋轮线 (cycloid)**；
3. **悬链线 (catenary)**：极小化势能 $\int y\sqrt{1+\dot y^2}dx$，解 $y=a\cosh(x/a)$；
4. **极小曲面**：极小化面积 $\iint\sqrt{1+u_x^2+u_y^2}dxdy$，给出极小曲面方程 $\nabla\cdot(\nabla u/\sqrt{1+\lvert\nabla u\rvert^2})=0$。

---

## 4. Hamilton 观点

**广义动量** $p_i=\partial L/\partial\dot q_i$。**Legendre 变换**把 Lagrange 力学化为 Hamilton 力学：$H(q,p)=\sum_ip_i\dot q_i-L(q,\dot q)$（$L$ 关于 $\dot q$ 凸时是凸对偶）。

**Hamilton 方程**：$\dot q_i=\partial H/\partial p_i$，$\dot p_i=-\partial H/\partial q_i$——一阶方程组，等价于 EL 方程。

**辛形式与 Poisson 括号**：相空间是辛流形，Hamilton 流**保持辛形式**（Liouville 定理：相体积守恒）。Poisson 括号 $\{f,g\}$ 是守恒量的代数结构。

**能量守恒**：$\partial_tL=0\Rightarrow H$ 守恒。

---

## 5. 对称性与守恒律（Noether 定理）

**对称性**：作用量 $S[q]=\int L\,dt$ 在单参数变换群 $\Phi_s$ 下不变，指 $S[\Phi_s\circ q]=S[q]\ \forall s$（$L$ 在由生成向量场 $X=\sum_i\xi^i(q)\partial_{q^i}$ 诱导的提升变换下不变）。

**定理（Noether）**：设 $L(q,\dot q)$ 在 $\Phi_s$ 下不变，则

$$J(q,\dot q)=\sum_i\frac{\partial L}{\partial\dot q_i}\xi^i(q)=\langle p,\xi\rangle$$

沿任一 EL 解守恒：$\frac{dJ}{dt}=0$。

**证明（链式法则 + EL 方程，一步到位）**：对 $L(\Phi_s(q),T\Phi_s(\dot q))=L(q,\dot q)$ 关于 $s$ 在 $s=0$ 求导得 $\sum_i(\frac{\partial L}{\partial q_i}\xi^i+\frac{\partial L}{\partial\dot q_i}\dot\xi^i)=0$；沿 EL 解代入 $\frac{\partial L}{\partial q_i}=\frac{d}{dt}(\frac{\partial L}{\partial\dot q_i})$，得 $\frac{dJ}{dt}=0$。

**三大守恒律**：

| 对称性 | 无穷小生成元 | 守恒量 |
|--------|--------------|--------|
| 时间平移 $t\mapsto t+s$ | $\partial_t$ | 能量 $H=\sum p_i\dot q_i-L$ |
| 空间平移 $q_i\mapsto q_i+s$ | $\partial_{q_i}$ | 线动量 $p_i=\partial L/\partial\dot q_i$ |
| 旋转 $\theta\mapsto\theta+s$ | $\partial_\theta$ | 角动量 $J$ |

**定理（Clairaut 关系）**：旋转曲面上的测地线，由绕轴旋转对称得守恒量 $r\sin\alpha=\text{const}$（$r$ 为到轴距离，$\alpha$ 为测地线与经线夹角）。

**典型例子**：自由粒子（空间平移 ⇒ 动量守恒；时间平移 ⇒ 能量守恒）；中心力场（绕原点旋转不变 ⇒ 角动量 $mr^2\dot\theta$ 守恒，即 Kepler 第二定律）。

**心智模型**：**连续对称性 ⟺ 守恒律**；证明只用链式法则 + EL 方程，但内涵极深，是现代场论与规范理论（规范对称 ⟹ 电荷守恒）的母模板。

---

## 关键结论速查

- **变分法的变量是几何对象**，其全体构成无限维流形；求作用量临界点 = 把有限维微积分逐字推广到无限维弯曲空间。
- **V-直接法**：极小化序列有界 → 弱收敛子列 → 弱下半连续 → 极限点即极小点（三者缺一不可）。
- **Euler–Lagrange**：一阶变分 → 分部积分 → 变分法基本引理，把泛函极值化为 ODE/PDE。
- **自然边界条件** ⟺ 自由端点 ⟺ 广义动量为零；**Legendre 条件**（$L$ 关于 $\dot q$ 凸）是极小值二阶必要条件。
- **Noether 定理**：连续对称 ⟺ 守恒律（时间/空间/旋转 ⟹ 能量/动量/角动量）。
- **Riesz 表示 + Lax–Milgram + Banach–Alaoglu** 是变分法存在性论证的三大工具（内积 → 梯度向量 → 弱紧性）。
