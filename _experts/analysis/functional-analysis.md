# 泛函分析 (Functional Analysis)

> 整理自 Walter Rudin《Functional Analysis》(2nd ed.)；John B. Conway《A Course in Functional Analysis》(GTM 96)；Roman Vershynin《Lectures in Functional Analysis》；IIT Guwahati MA543 讲义；Vahid Shirbisheh《Lectures on C*-algebras》(arXiv:1211.3404)；University of Houston Math 7321。

## 0. 一句话定位

泛函分析研究**无限维线性空间上的连续线性算子**，把线性代数"有限维矩阵对角化"的思想推广到函数空间：范数与内积给出"长度/夹角"，完备性（Banach/Hilbert 空间）给出"极限运算成立"，对偶与弱拓扑给出"紧性在无限维里如何抢救"，谱理论回答"算子何时可对角化"，C\* 代数把这一切代数化终局。

**核心心智模型**：

- **范数/内积** = 无限维里的"大小/夹角"；**完备性**把"柯西列收敛"移植到函数空间，是全部极限论证的地基。
- **对偶** $X^*$ = 把向量换成"在它身上取值的线性泛函"；**Hahn–Banach** 保证泛函足够多。
- **三大基本原理** = 完备性的三种用法（逐点有界 ⇒ 一致有界；满射 ⇒ 开；闭图像 ⇒ 连续），都源自 Baire 纲定理。
- **弱拓扑** = 无限维里造紧性：单位球范数拓扑下不紧，但弱\*拓扑下紧（Banach–Alaoglu）。
- **谱** = 算子"广义特征值"；**谱半径公式** $r(T)=\lim_n\lVert T^n\rVert^{1/n}$。
- **紧算子** = 无限维里最像"有限秩"的算子，谱离散、可作为"对角化"。
- **C\* 代数** = 算子代数的公理化终局；交换 C\* 代数就是连续函数代数。

---

## 1. 赋范空间与巴拿赫空间

**范数**满足正定性、齐次性 $\lVert\alpha x\rVert=\lvert\alpha\rvert\lVert x\rVert$、三角不等式。诱导度量 $d(x,y)=\lVert x-y\rVert$；完备（每个柯西列收敛）的赋范空间称**巴拿赫空间**。

**有界线性算子**：$\lVert T\rVert=\sup_{\lVert x\rVert\le1}\lVert Tx\rVert<\infty$。线性映射**连续 $\iff$ 有界**。全体有界算子记 $\mathcal B(X,Y)$（$Y$ 完备时它完备）；$X^*=\mathcal B(X,\mathbb{C})$ 是**对偶空间**。

**经典例子**：$\ell^p$（$1\le p<\infty$，$\lVert x\rVert_p=(\sum\lvert x_n\rvert^p)^{1/p}$）；$L^p(\mu)$；连续函数空间 $C(K)$（上确界范数），$C_0(X)$（无穷远趋于 0）。

**两个核心不等式**（$1/p+1/q=1$）：**Hölder** $\lVert fg\rVert_1\le\lVert f\rVert_p\lVert g\rVert_q$（引理：Young $ab\le a^p/p+b^q/q$）；**Minkowski** $\lVert f+g\rVert_p\le\lVert f\rVert_p+\lVert g\rVert_p$。

**完备性判据**：赋范空间是 Banach 空间 $\iff$ 每个绝对可和级数 $\sum\lVert x_n\rVert<\infty$ 都收敛。

**有限维 vs 无限维**：有限维空间上任意两范数等价、单位球紧；**Riesz 引理**说明无限维里单位球不紧：对闭真子空间 $Y\subsetneq X$ 与 $\varepsilon>0$，存在 $\lVert x\rVert=1$ 且 $\operatorname{dist}(x,Y)\ge1-\varepsilon$。**推论：单位闭球紧 $\iff$ 空间有限维**。这是无限维分析最根本的现象——紧性必须"另寻出路"（弱拓扑）。

---

## 2. Hahn–Banach 与对偶

**定理（Hahn–Banach，延拓形式）**：$M\subset X$ 子空间，$f\in M^*$，则存在 $F\in X^*$ 使 $F|_M=f$ 且 $\lVert F\rVert=\lVert f\rVert$。证明用 Zorn 引理逐维延拓。

**推论（分离点）**：对任意 $x_0\ne0$，存在 $f\in X^*$ 使 $\lVert f\rVert=1$、$f(x_0)=\lVert x_0\rVert$——对偶空间"足够大"，能区分向量。

**凸集分离**：不相交凸集（一个有非空内部）可被超平面分离：$\exists f\ne0,\ \alpha$ 使 $f(a)\le\alpha\le f(b)$。这是凸分析、优化对偶、支持超平面的几何基石。

**对偶空间的显式表示**（核心模式："线性泛函 = 与某个对偶对象配对"）：

- $(\ell^p)^*\cong\ell^q$：$f(x)=\sum x_n y_n$，$\lVert f\rVert=\lVert y\rVert_q$；$(\ell^1)^*\cong\ell^\infty$，$c_0^*\cong\ell^1$；
- $(L^p)^*\cong L^q$（$1\le p<\infty$，$\sigma$-有限）：$f(h)=\int hg\,d\mu$，$\lVert f\rVert=\lVert g\rVert_q$；
- $C(K)^*\cong$ 正则 Borel 复测度（Riesz–Markov–Kakutani）：$f(h)=\int_K h\,d\mu$，$\lVert f\rVert=\lvert\mu\rvert(K)$。

**注意**：$(L^\infty)^*$ 严格大于 $L^1$（含有限可加测度等病态对象）；对偶理论在 $p=1,\infty$ 端点总变复杂。

---

## 3. 三大基本原理（同源于 Baire）

**Baire 纲定理**：完备度量空间（或其开子集）是第二纲的；等价地，可数个稠密开集的交仍稠密。它是"存在性 + 定性"论证的引擎。

**一致有界原理（Banach–Steinhaus）**：$X$ Banach、$\mathcal F\subset\mathcal B(X,Y)$，若逐点有界（$\sup_T\lVert Tx\rVert<\infty$ 对每个 $x$），则一致有界（$\sup_T\lVert T\rVert<\infty$）。证明：$E_n=\{x:\sup_T\lVert Tx\rVert\le n\}$ 是闭集且并满 $X$，Baire 给某个 $E_N$ 有非空内部，再线性放大。**推论**：$T_n$ 逐点收敛到 $T$ 则 $T$ 有界且 $\lVert T\rVert\le\liminf\lVert T_n\rVert$。

**开映射定理**：$X,Y$ Banach，$T\in\mathcal B(X,Y)$ 满射 $\Rightarrow$ $T$ 把开集映为开集。**推论（逆算子定理）**：双射 $T\in\mathcal B(X,Y)$ 的逆 $T^{-1}$ 自动有界——"代数可逆 ⇒ 拓扑可逆"。

**闭图像定理**：线性 $T:X\to Y$（$X,Y$ Banach）若图像 $\{(x,Tx)\}$ 闭，则 $T$ 有界。用途：验证算子连续时，"$x_n\to x,\ Tx_n\to y\Rightarrow y=Tx$"常比直接估计范数容易。

**前提警告**：三大定理都要求定义域/值域**完备**；非完备空间里全部失效（如开映射定理要求 $Y$ 完备）。

---

## 4. 对偶与弱拓扑

**弱拓扑**：使一切 $f\in X^*$ 连续的最粗拓扑；$x_n\rightharpoonup x$ 指对一切 $f$ 有 $f(x_n)\to f(x)$。**弱\*拓扑**：$X^*$ 上使一切赋值 $f\mapsto f(x)$ 连续的最粗拓扑；$f_n\xrightarrow{w^*}f$ 指逐点收敛。

**定理（Banach–Alaoglu）**：$X^*$ 的闭单位球在弱\*拓扑下紧。证明：嵌入 $\prod_{x\in X}\overline{\mathbb D}$，由 Tychonoff 定理乘积紧，$B_{X^*}$ 为闭子集。**推论**：任何有界序列 $(f_n)\subset X^*$ 有弱\*收敛子列——广泛用于 PDE 弱解存在性、概率测度弱收敛、最优控制。

**自反空间**：自然嵌入 $J:X\to X^{**}$，$(Jx)(f)=f(x)$ 等距；$J$ 满射则 $X$ **自反**。$L^p,\ell^p$（$1<p<\infty$）与 Hilbert 空间自反；$L^1,L^\infty,c_0,C(K)$ 不自反。**Kakutani**：$X$ 自反 $\iff$ 闭单位球弱紧。

**弱收敛的几何含义**：弱收敛**不保范数**（$\lVert x\rVert\le\liminf\lVert x_n\rVert$，如 $\ell^2$ 标准基 $e_n\rightharpoonup0$ 但 $\lVert e_n\rVert=1$）；闭凸集弱闭 = 范数闭；**Mazur 定理**：$x_n\rightharpoonup x$ 则存在凸组合范数收敛到 $x$（把弱收敛"修复"成强收敛）。

---

## 5. 希尔伯特空间

**内积**诱导范数 $\lVert x\rVert=\sqrt{\langle x,x\rangle}$；完备则称**希尔伯特空间**。**Cauchy–Schwarz** $\lvert\langle x,y\rangle\rvert\le\lVert x\rVert\lVert y\rVert$。**平行四边形法则** $\lVert x+y\rVert^2+\lVert x-y\rVert^2=2\lVert x\rVert^2+2\lVert y\rVert^2$ 判定范数是否来自内积（故只有 $L^2$ 是希尔伯特空间）。

**投影定理**：$M$ 闭子空间，则对每个 $x$ 存在唯一 $y\in M$ 使 $\lVert x-y\rVert=\operatorname{dist}(x,M)$，由 $x-y\perp M$ 刻画，$H=M\oplus M^\perp$。这是最小二乘、有限元、逼近论的地基。

**Riesz 表示定理**：$y\mapsto\langle\cdot,y\rangle$ 是 $H\to H^*$ 的共轭线性等距同构；每个 $f\in H^*$ 唯一由 $y_f$ 表示 $f(x)=\langle x,y_f\rangle$，$\lVert f\rVert=\lVert y_f\rVert$。故 $H$ 自反，弱拓扑与弱\*拓扑重合。

**正交规范基 (ONB)**：$\langle e_\alpha,e_\beta\rangle=\delta_{\alpha\beta}$ 且张成稠密。**Fourier 展开** $x=\sum_\alpha\langle x,e_\alpha\rangle e_\alpha$，**Bessel** $\sum\lvert\langle x,e_\alpha\rangle\rvert^2\le\lVert x\rVert^2$，**Parseval** $\lVert x\rVert^2=\sum\lvert\langle x,e_\alpha\rangle\rvert^2$。可分希尔伯特空间都等距同构于 $\ell^2$。

---

## 6. 有界算子与伴随

$B(H)$ 在算子范数下是含单位的巴拿赫代数（$\lVert ST\rVert\le\lVert S\rVert\lVert T\rVert$）。

**伴随算子**：对每个 $T\in B(H)$ 存在唯一 $T^*$ 使 $\langle Tx,y\rangle=\langle x,T^*y\rangle$（构造：固定 $y$，$x\mapsto\langle Tx,y\rangle$ 是有界泛函，由 Riesz 表示对应一个向量）。性质：$(ST)^*=T^*S^*$，$T^{**}=T$，**C\* 恒等式** $\lVert T^*T\rVert=\lVert T\rVert^2$。

**算子分类**：

| 算子 | 定义 | 等价刻画 |
|------|------|----------|
| 自伴 self-adjoint | $T^*=T$ | $\langle Tx,x\rangle\in\mathbb{R}\ \forall x$ |
| 正 positive | $\langle Tx,x\rangle\ge0$ | 自伴且 $\sigma(T)\subset[0,\infty)$；有唯一正平方根 $T^{1/2}$ |
| 酉 unitary | $U^*U=UU^*=I$ | 保范等距且满射 |
| 正规 normal | $T^*T=TT^*$ | 自伴与酉都是正规 |
| 投影 | $P^2=P=P^*$ | 到闭子空间的正交投影 |

**闭值域定理**：$\operatorname{ran}(T)$ 闭 $\iff$ $\operatorname{ran}(T^*)$ 闭 $\iff$ $\operatorname{ran}(T)=\ker(T^*)^\perp$ $\iff$ $\operatorname{ran}(T^*)=\ker(T)^\perp$。核心正交分解 $H=\overline{\operatorname{ran}(T^*)}\oplus\ker(T)$。

**极分解**：$T=U\lvert T\rvert$，$\lvert T\rvert=(T^*T)^{1/2}$ 是正算子，$U$ 是部分等距（$\ker U=\ker T$）——复数极分解 $z=e^{i\theta}\lvert z\rvert$ 的算子版。

---

## 7. 紧算子与 Fredholm 择一

**定义（紧算子）**：$T$ 把有界集映为相对紧集。等价刻画（可分希尔伯特空间）：$T$ 紧 $\iff$ 弱收敛 $x_n\rightharpoonup x$ $\Rightarrow$ 强收敛 $Tx_n\to Tx$ $\iff$ $T$ 是有限秩算子在范数下的极限。

**性质**：$\mathcal K(X,Y)$ 是 $\mathcal B(X,Y)$ 的闭子空间；$T$ 紧、$S$ 有界 $\Rightarrow$ $TS,ST$ 紧（$\mathcal K(H)\triangleleft B(H)$ 是闭双侧理想）；$T$ 紧 $\iff$ $T^*$ 紧；无限维上恒等算子**不紧**。

**定理（紧算子谱，Riesz–Schauder）**：$T\in\mathcal K(H)$ 的谱 $\sigma(T)$ 至多可数、除 $0$ 外无聚点；每个非零 $\lambda\in\sigma(T)$ 是**特征值**且特征空间有限维。

**定理（紧正规算子谱定理）**：$T\in\mathcal K(H)$ 正规，则存在正交规范基 $\{e_n\}$ 与 $\lambda_n\to0$ 使 $T=\sum_n\lambda_n P_n$，即 $Tx=\sum_n\lambda_n\langle x,e_n\rangle e_n$。**这是真正的对角化**。

**推论（紧自伴算子，极大极小原理）**：特征值 $\lambda_n\in\mathbb{R}$，$\lvert\lambda_1\rvert\ge\lvert\lambda_2\rvert\ge\cdots\to0$，

$$\lambda_n=\max_{\dim E=n}\min_{0\ne x\in E}\frac{\langle Tx,x\rangle}{\langle x,x\rangle}.$$

Rayleigh 商变分刻画，是有限元法与特征值数值方法的理论基础。

**定理（Fredholm 择一）**：$T\in\mathcal K(H)$、$\lambda\ne0$，则 $(\lambda I-T)x=y$ **要么对每个 $y$ 有唯一解，要么齐次方程有非平凡解**；可解当且仅当 $y\perp\ker(\bar\lambda I-T^*)$。Fredholm 积分方程 $x(t)-\lambda\int K(t,s)x(s)ds=y(t)$（$K$ 平方可积 $\Rightarrow$ 积分算子紧）由此得完全可解性判据。

**Hilbert–Schmidt 与迹类**：$\lVert T\rVert_{HS}^2=\sum_n\lVert Te_n\rVert^2<\infty$（对应 $L^2$ 上的积分算子 $\int K(\cdot,s)f(s)ds$，$K\in L^2$）；迹类 $\lVert T\rVert_1=\operatorname{tr}\lvert T\rvert<\infty$，可定义迹 $\operatorname{tr}T$。关系链：**迹类 $\subset$ Hilbert–Schmidt $\subset$ 紧 $\subset$ 有界**，$\lVert T\rVert\le\lVert T\rVert_{HS}\le\lVert T\rVert_1$。

---

## 8–9. 谱基础与巴拿赫代数

**谱与预解集**：$\rho(T)=\{\lambda:\lambda I-T\text{ 可逆}\}$，$\sigma(T)=\mathbb{C}\setminus\rho(T)$。$\sigma(T)$ 是 $\mathbb{C}$ 的非空紧子集，包含在 $\{\lvert z\rvert\le\lVert T\rVert\}$ 中；预解式满足**预解恒等式** $R_\lambda-R_\mu=(\mu-\lambda)R_\lambda R_\mu$。谱非空来自 Liouville 定理的反证。

**谱半径公式（Gelfand）**：$r(T)=\sup_{\lambda\in\sigma(T)}\lvert\lambda\rvert=\lim_{n\to\infty}\lVert T^n\rVert^{1/n}=\inf_n\lVert T^n\rVert^{1/n}$。**正规算子**满足 $r(T)=\lVert T\rVert$。

**谱的细分**：点谱 $\sigma_p$（非单射，即特征值）、近似点谱 $\sigma_{ap}$（$\exists\lVert x_n\rVert=1$ 使 $(\lambda I-T)x_n\to0$）、连续谱 $\sigma_c$（单射、值域稠密不满）、剩余谱 $\sigma_r$（值域不稠密）。正规算子剩余谱为空。

**经典例子**：乘法算子 $(M_\varphi f)(t)=\varphi(t)f(t)$ 正规、$\sigma(M_\varphi)=\varphi([0,1])$、无特征值（谱全连续）；单侧移位 $S$ 等距非酉，$\sigma(S)=\overline{\mathbb D}$、无特征值、$\sigma_{ap}(S)$ 是单位圆周、$\sigma_r(S)$ 是开单位圆盘——非正规算子谱不平凡的经典例。

**巴拿赫代数**：$\lVert ab\rVert\le\lVert a\rVert\lVert b\rVert$、$\lVert e\rVert=1$。**Gelfand–Mazur**：巴拿赫除环 $\cong\mathbb{C}$。**Gelfand 变换** $a\mapsto\hat a$（$\hat a(\varphi)=\varphi(a)$，$\varphi$ 遍历全体特征）是保范同态到 $C(\Delta(\mathcal A))$，且 $\sigma(a)=\hat a(\Delta)$，$r(a)=\lVert\hat a\rVert_\infty$。**Wiener 定理**：绝对收敛 Fourier 级数处处非零 $\Rightarrow$ 倒数也有绝对收敛 Fourier 级数——Gelfand 理论把分析问题化为代数可逆性问题的典范。

---

## 10. C\* 代数与正规算子谱定理

**C\* 代数**：带对合、满足 **C\* 恒等式** $\lVert a^*a\rVert=\lVert a\rVert^2$ 的巴拿赫代数。推论：$\lVert a^*\rVert=\lVert a\rVert$；正规元满足 $r(a)=\lVert a\rVert$；自伴元满足 $\lVert a^2\rVert=\lVert a\rVert^2$。

**定理（Gelfand–Naimark，交换情形）**：交换 C\* 代数经 Gelfand 变换**等距 \*-同构**于 $C_0(\Delta)$。含单位的 $\cong C(K)$，无单位的 $\cong C_0(X)$。

**连续函数演算**：$T$ 正规 $\Rightarrow$ 存在唯一等距 \*-同态 $\Phi:C(\sigma(T))\to B(H)$，$f\mapsto f(T)$，$\Phi(1)=I$、$\Phi(\mathrm{id})=T$。满足 $\lVert f(T)\rVert=\lVert f\rVert_\infty$；**谱映射定理** $\sigma(f(T))=f(\sigma(T))$。

**谱测度与 Borel 函数演算**：谱测度（投影值测度, PVM）$E:\mathcal B\to B(H)$ 满足 $E(\varnothing)=0$、$E(\mathbb{C})=I$、可数可加、$E(\Delta_1\cap\Delta_2)=E(\Delta_1)E(\Delta_2)$。

**定理（正规算子谱定理，终结形态）**：$T$ 正规 $\Rightarrow$ 存在唯一谱测度 $E$（支撑在 $\sigma(T)$）使

$$T=\int_{\sigma(T)}z\,dE(z),\qquad f(T)=\int f(z)\,dE(z).$$

**谱定理的阶梯**：有限维（对角化）→ 紧正规（求和 $T=\sum\lambda_n P_n$）→ 一般正规（积分 $T=\int z\,dE(z)$）。"谱离散则求和、谱连续则积分"，PVM 是全部的统一语言。

---

## 关键结论速查

- **完备性是开关**：极限、级数、不动点、三大原理都要求 Banach 空间。
- **Hahn–Banach**：延拓 + 保范，定义伴随、分离凸集、造见证泛函的万能工具。
- **三大原理同源**：Baire 纲定理 $\Rightarrow$ 逐点有界⇒一致有界、满射⇒开、闭图像⇒连续。
- **弱\*紧性复活**：Banach–Alaoglu（$X^*$ 单位球弱\*紧）、Kakutani（自反 $\iff$ 弱紧）。
- **紧算子 = 有限秩闭包**，谱除 0 外离散；Fredholm 择一把可解性归结为有限维核空间。
- **谱定理阶梯**：对角化 → $\sum\lambda_n P_n$ → $\int z\,dE(z)$。
- **C\* 恒等式** $\lVert a^*a\rVert=\lVert a\rVert^2$ 是范数与对合的婚配，锁死整个理论结构。
