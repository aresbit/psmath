# 交换代数 (Commutative Algebra)

> **整理自**：Atiyah–MacDonald《Introduction to Commutative Algebra》、J. S. Milne《A Primer of Commutative Algebra》、MIT 18.705 课程讲义
> **适用触发词**：环、理想、素理想、极大理想、局部环、幂零根、雅各布森根、模、正合、Nakayama、张量积、平坦、诺特、Hilbert 基定理、局部化、整闭、零点定理、Krull 维数、主理想定理、参数系、Artin 环、Dedekind 整环

## 0. 一句话定位

交换代数研究交换环及其上的模，回答三个问题：一个环有多少理想、理想如何分解、素理想链能有多长。几何对象的函数环与数域的整数环都是交换环，因此它是代数几何与代数数论的公共地基。

## 1. 环与理想（ch01）

- **整环**：无零因子；**域**：非零元皆单位。
- **素理想** $$\mathfrak{p}\subsetneq A$$：$$xy\in\mathfrak{p}\Rightarrow x\in\mathfrak{p}$$ 或 $$y\in\mathfrak{p}$$，等价于 $$A/\mathfrak{p}$$ 是整环。**极大理想** $$\mathfrak{m}$$：$$A/\mathfrak{m}$$ 是域；极大必素。
- **Zorn 引理**：每个真理想含于某个极大理想，故非零环必有极大理想。
- **幂零根** $$\mathfrak{N}(A)=\{x:x^n=0\}=\bigcap_{\mathfrak{p}\ \text{素}}\mathfrak{p}$$。
- **雅各布森根** $$J(A)=\bigcap_{\mathfrak{m}\ \text{极大}}\mathfrak{m}=\{x:1-xy\ \text{是单位}\ \forall y\}$$。
- **局部环**：恰有一个极大理想 $$\mathfrak{m}$$；等价于非单位元全体构成理想。剩余域 $$k=A/\mathfrak{m}$$。$$k[[x]]$$、$$A_{\mathfrak{p}}$$ 是局部环。
- **Spec**：$$\operatorname{Spec}(A)=\{\text{素理想}\}$$，带 Zariski 拓扑。素理想 ↔ 不可约子簇，极大理想 ↔ 点，局部化 $$A_{\mathfrak{p}}$$ ↔ 芽环。
- **素理想回避**：$$\mathfrak{a}\subseteq\bigcup_i\mathfrak{p}_i$$（$$\mathfrak{p}_i$$ 素）$$\Rightarrow\mathfrak{a}\subseteq$$ 某个 $$\mathfrak{p}_i$$。

## 2. 模与正合序列（ch02）

- **模** = 环上的向量空间；理想是子模，商 $$A/\mathfrak{a}$$ 是模。
- **正合**：$$\operatorname{im}f=\ker g$$；**短正合列** $$0\to M'\to M\to M''\to 0$$（单 + 满 + 像 = 核）。例：$$0\to\mathfrak{a}\to A\to A/\mathfrak{a}\to 0$$。
- **Nakayama 引理**：$$M$$ 有限生成，$$\mathfrak{a}\subseteq J(A)$$，若 $$\mathfrak{a}M=M$$ 则 $$M=0$$（行列式技巧：$$\det(I-(a_{ij}))\equiv1\pmod{\mathfrak{a}}$$ 是单位）。
  - 常用形式 1：$$M=\mathfrak{a}M+N\Rightarrow M=N$$。
  - 常用形式 2：$$(A,\mathfrak{m})$$ 局部环、$$M$$ f.g.，则 $$m_1,\dots,m_n$$ 生成 $$M$$ $$\iff$$ 其像在 $$k$$-向量空间 $$M/\mathfrak{m}M$$ 中生成。**把"是否生成"降维到线性代数。**
- **张量积** $$M\otimes_A N$$：双线性配对的万有对象。$$A\otimes_A M\cong M$$；张量积**右正合**。
- **平坦模**：$$-\otimes N$$ 保持正合（$$S^{-1}A$$ 是平坦的典型例）。
- 自由模的秩良定义（商极大理想化成向量空间维数一致——Nakayama 的妙用）。

## 3. 诺特环（ch03）

- **ACC**：子模升链稳定。$$M$$ 诺特 $$\iff$$ 每个子模有限生成 $$\iff$$ 非空子模族有极大元。
- 短正合列 $$0\to M'\to M\to M''\to 0$$ 中 $$M$$ 诺特 $$\iff$$ $$M',M''$$ 都诺特。
- **Hilbert 基定理**：$$A$$ 诺特 $$\Rightarrow$$ $$A[x]$$ 诺特（首项理想升链 + ACC）。推论：$$A[x_1,\dots,x_n]$$ 诺特；仿射空间的每个理想簇由有限个方程定义。
- **反例**：$$k[x_1,x_2,\dots]$$（升链 $$(x_1)\subsetneq(x_1,x_2)\subsetneq\cdots$$ 不停）。

## 4. 局部化（ch04）

- **分式环** $$S^{-1}A$$（$$S$$ 乘法封闭）：$$\dfrac{a}{s}=\dfrac{b}{t}\iff\exists u\in S,\ u(at-bs)=0$$（$$u$$ 的存在是传递性的关键）。
- **两个特例**：$$A_{\mathfrak{p}}=(A\setminus\mathfrak{p})^{-1}A$$（局部环，唯一极大理想 $$\mathfrak{p}A_{\mathfrak{p}}$$）；$$\operatorname{Frac}(A)=(A\setminus\{0\})^{-1}A$$（分式域）。
- **理想对应**：$$\{\mathfrak{p}\in\operatorname{Spec}(A):\mathfrak{p}\cap S=\varnothing\}\xrightarrow{\cong}\operatorname{Spec}(S^{-1}A)$$。故 $$\operatorname{Spec}(A_{\mathfrak{p}})\cong\{\mathfrak{q}:\mathfrak{q}\subseteq\mathfrak{p}\}$$，$$\dim A_{\mathfrak{p}}=\operatorname{ht}(\mathfrak{p})$$。
- **局部化正合**：$$S^{-1}$$ 保核、保像、保单射；$$S^{-1}M\cong S^{-1}A\otimes_A M$$（故 $$S^{-1}A$$ 平坦）。
- **局部-整体原理**：$$M=0\iff M_{\mathfrak{m}}=0$$ 对每个极大理想 $$\mathfrak{m}$$。

## 5. 整性（ch05）

- **整元**：满足首一多项式 $$x^n+a_{n-1}x^{n-1}+\cdots+a_0=0$$（$$a_i\in A$$）。$$B/A$$ 整、整闭包、整闭（在其分式域中整闭的整环称正规）。
- **等价条件**：$$x$$ 在 $$A$$ 上整 $$\iff$$ $$A[x]$$ 作为 $$A$$-模有限生成 $$\iff$$ 存在忠实 f.g. $$A[x]$$-模 $$M$$。
- **关键推论**：有限 $$\Rightarrow$$ 整；**整 + 有限型 $$\Rightarrow$$ 有限**；整性传递。
- **三大谱定理**：**lying over**（$$\operatorname{Spec}(B)\to\operatorname{Spec}(A)$$ 满射）；**going up**（链可逐级抬升）；**going down**（需 $$A$$ 整闭）。推论：**整扩张保维数** $$\dim B=\dim A$$。
- **Noether 正规化**：有限生成域代数 $$A$$ 在某个多项式子环 $$k[y_1,\dots,y_d]$$ 上有限（从而整），$$d$$ 唯一且等于 $$\dim A$$。
- **Zariski 引理**：有限生成代数且是域 $$\Rightarrow$$ 是基域的有限代数扩张。**弱零点定理**：$$k$$ 代数闭时极大理想 $$\mathfrak{m}=(x_1-a_1,\dots,x_n-a_n)$$，点 $$\leftrightarrow$$ 极大理想。
- **正规化** = 去奇异点；$$A=\mathbb{Z}$$ 在数域中的整闭包 $$\mathcal{O}_K$$ 是整数环；一维正规诺特整环 = Dedekind 整环。

## 6. 维数理论（ch06）

- **Krull 维数**：$$\dim A=\sup\{n:\mathfrak{p}_0\subsetneq\cdots\subsetneq\mathfrak{p}_n\}$$。$$A_{\mathfrak{p}}$$ 维数 = $$\operatorname{ht}(\mathfrak{p})$$；整扩张保维数；域 0、$$\mathbb{Z}$$/$$k[x]$$ 为 1。
- **Krull 主理想定理**：诺特环中非单位非零因子 $$x$$，$$(x)$$ 的极小素理想满足 $$\operatorname{ht}(\mathfrak{p})=1$$（一个方程削一维）。
- **广义主理想定理**：$$\mathfrak{a}=(x_1,\dots,x_r)$$ 的极小素理想 $$\operatorname{ht}(\mathfrak{p})\le r$$。推论：$$\dim A\le\dim_k\mathfrak{m}/\mathfrak{m}^2$$（嵌入维数）。
- **参数系**：$$x_1,\dots,x_d$$ 满足 $$\sqrt{(x_1,\dots,x_d)}=\mathfrak{m}$$，$$d=\dim A$$ 是最小长度。**正则局部环**：$$\dim A=\dim_k\mathfrak{m}/\mathfrak{m}^2$$（光滑点的代数化身）。
- **f.g. 域代数**：$$\dim A=\operatorname{tr.deg}_k\operatorname{Frac}(A)$$（Noether 正规化 + 整扩张保维数）。推论 $$\dim k[x_1,\dots,x_n]=n$$。
- **Hilbert 多项式**：分次模 $$H_M(n)=\ell(M_n)$$ 对充分大 $$n$$ 是多项式，$$\deg P_M=\dim M-1$$。**Hilbert–Samuel**：$$\ell(A/\mathfrak{m}^n)$$ 的次数 = $$\dim A$$，首项系数给重数 $$e(A)$$。

## 7. Artin 环与数论接口（ch07）

- **DCC**：子模降链稳定。**Artin 环**：作为自身模的 DCC 成立。
- **结构定理**：**Artin $$\iff$$ 诺特 + 零维**。Artin 环有有限个极大理想；幂零根幂零（$$J(A)^n=0$$）。
- **中国剩余定理**：$$\mathfrak{a}_i$$ 两两互素时 $$A/\bigcap\mathfrak{a}_i\cong\prod A/\mathfrak{a}_i$$。
- **直积分解**：每个 Artin 环 $$\cong\prod_{i=1}^r A_{\mathfrak{m}_i}\cong\prod A/\mathfrak{m}_i^{n_i}$$（有限个点 + 各阶无穷小）。
- **长度**：合成列的公长度 $$\ell(M)$$；$$M$$ 有合成列 $$\iff$$ 诺特且 Artin。短正合列中 $$\ell(M)=\ell(M')+\ell(M'')$$（长度是加法函数）。
- **Dedekind 整环** = 一维诺特整闭整环，每个非零理想唯一分解为素理想幂之积；$$\mathcal{O}_K/\mathfrak{a}$$ 是 Artin 环。

## 8. 代数大师的解题清单（交换代数侧）

1. **先看理想**：素 vs 极大、幂零根、雅各布森根，理想之并/交/积如何交互。
2. **模问题先正合化**：把"核/像/商"塞进短正合列，再用长正合列串联。
3. **要生成元结论就上 Nakayama**：商掉极大理想降维到线性代数，再拉回。
4. **要局部结论就局部化**：$$A_{\mathfrak{p}}$$ 是显微镜，$$\operatorname{Spec}(A_{\mathfrak{p}})$$ 收窄到 $$\mathfrak{p}$$ 以下。
5. **要维数结论就找参数系或做 Noether 正规化**：主理想定理给下界，超越次数给上界。
6. **有限性用诺特**：理想有限生成、$$A[x]$$ 诺特、子模 f.g. 自动传递。
