# 代数几何、代数拓扑与 K 理论：把代数搬到几何里 (Geometry, Topology & K-theory Bridge)

> **整理自**：MIT 18.725《Algebraic Geometry I》(Bezrukavnikov)、Hartshorne《Algebraic Geometry》(GTM 52)、Frédéric Paulin《Topologie algébrique élémentaire》、《Algebraic Topology》(ENS Paris-Saclay)、Allen Hatcher《Vector Bundles and K-Theory》、Atiyah《K-Theory》、Atiyah–Hirzebruch
> **适用触发词**：代数几何、簇、仿射簇、射影簇、Nullstellensatz、概形、Spec、层、凝聚层、上同调、Serre 对偶、Riemann-Roch、相交理论、Bézout、代数拓扑、基本群、覆盖空间、同调、胞腔同调、cup 积、Hurewicz、Euler 特征、K 理论、向量丛、Grothendieck 群、Bott 周期、Chern 特征标、指标定理

## 0. 一句话定位

这三门学科是交换代数/同调代数的"几何实现"：代数几何把多项式零点几何化并用层与上同调从局部拼出全局不变量；代数拓扑用函子把几何问题代数化，把同胚/同伦分类翻译成群或模的同构判定；K 理论把向量丛按 Grothendieck 群代数化，得到比普通上同调更强的广义上同调理论。

## 1. 代数几何（第一部分）

- **核心字典**：仿射簇 $$\leftrightarrow$$ 有限生成无幂零元的交换 $$k$$-代数（几何点 = 环的极大理想）。这是贯穿全书的第一字典（与交换代数的弱零点定理一致）。
- **Zariski 拓扑与 Nullstellensatz**：零点集给出 Zariski 闭集；Hilbert 零点定理建立"理想 ↔ 簇"的对应。
- **射影簇、Noether 正规化与维数**：维数 = 函数域的超越次数（与交换代数维数理论接口）。
- **态射**：有限态射（对应整扩张）、仿射态射、Grassmannian 是典型模空间。
- **概形**：$$\operatorname{Spec}A$$ 带结构层，允许幂零元与任意素理想，把算术（$$\mathbb{Z}$$、$$\mathbb{F}_q$$）与几何统一。
- **层**：局部数据 + 粘合规则；拟凝聚层、凝聚层（簇上的"广义向量丛"）。可逆层与除子给出 **Picard 群** $$\operatorname{Pic}$$。
- **上同调 = 全局截面函子的导出函子**：整体截面 $$\Gamma$$ 不正合，缺失信息由 $$H^i$$ 度量；$$H^1(\mathcal{O}^*)\cong\operatorname{Pic}$$（用 Čech 上同调算）。
- **Serre 对偶**把 $$H^i$$ 与 $$H^{n-i}$$ 配对，是曲线论与 Riemann–Roch 的引擎。**相交理论**：Bézout 定理、Chern 类——交点个数是扰动不变的拓扑不变量。

## 2. 代数拓扑（第二部分）

- **纲领 = 函子化**：构造从拓扑空间范畴到群/模范畴的（协变或反变）函子，使同胚乃至同伦等价的空间有同构的不变量。基本群、奇异同调、上同调都是这一纲领的实现。
- **基本群** $$\pi_1$$：第一个非交换不变量，只依赖同伦型；连续映射拉回为同态、同伦等价拉回为同构。基点产生共轭歧义，只在阿贝尔时才典范。
- **覆盖空间**：纤维离散的局部平凡纤维丛；离散群的**真、自由作用**产生覆盖（群作用 ↔ 多叶覆盖一一对应）。提升理论（路径/同伦/映射提升）是技术心脏：$$f$$ 可提升 $$\iff f_*\pi_1(Y,y)\subseteq p_*\pi_1(X,x)$$。
- **覆盖分类定理**：连通覆盖的同构类 ↔ 基本群子群的共轭类；**正规子群 ↔ Galois 覆盖**；万有覆盖使 $$\operatorname{Aut}\cong\pi_1$$。这是第一个完整的"拓扑 ↔ 代数"对应。
- **van Kampen 定理**：$$X=U_1\cup U_2$$ 时 $$\pi_1(X)\cong\pi_1(U_1)*_{\pi_1(U_0)}\pi_1(U_2)$$（沿交叠融合）。
- **CW 复形**：基本群只由 2-骨架决定；1-胞腔 = 生成元、2-胞腔的粘合环路 = 关系，给出群展示的几何来源；Cayley 复形把任意群展示实现为二维 CW 复形（拓扑地证明 Schreier 定理）。
- **同调** = 奇异单形链的线性化，$$\partial^2=0$$ 是核心恒等式；同调度量"闭链 ≠ 边界"的障碍。棱柱分解证同伦不变性；小链定理（重心重分）是切除与 Mayer–Vietoris 的来源，这两条长正合列是后续计算的引擎。
- **Hurewicz 定理**衔接非交换与交换不变量：$$H_1(X;\mathbb{Z})\cong\pi_1(X)^{\mathrm{ab}}$$。球面同调 $$H_p(S^n)$$ 是原子数据；Brouwer 不动点、Jordan–Brouwer 分离都是"球面同调 + 函子性"的推论。
- **胞腔同调**把计算化为"数胞腔 + 算球面映射的度"，边界算子纯组合；Euler 特征 $$=\sum(-1)^i n_i$$ 是最经济的拓扑不变量。
- **上同调**：经对偶（反变 Hom）获得乘法 **cup 积**，使 $$H^*$$ 成为分次反交换代数——比同调携带更精细的拓扑信息（可区分 $$S^2\vee S^4$$ 与 $$P^2(\mathbb{C})$$）。

## 3. K 理论（第三部分）

- **向量丛**：拓扑空间每点参数化地附一个线性空间；局部像 $$U\times\mathbb{C}^n$$，整体靠扭转（转移函数 / clutching 函数）编码。
- **K 群 = 向量丛的 Grothendieck 群**：$$K(X)$$ 由形式差 $$E-E'$$ 生成，加法来自直和 $$\oplus$$，乘法来自张量积 $$\otimes$$；约化 $$\widetilde{K}(X)$$，环结构由基本乘积定理给出。
- **Bott 周期定理**：$$\widetilde{K}(X)\cong\widetilde{K}(S^2X)$$，同构由 $$a\mapsto(H-1)*a$$ 给出（$$H$$ 为 $$\mathbb{CP}^1=S^2$$ 上的典型线丛）。复周期 2、实周期 8；这是 K 理论延拓为上同调理论的"心脏"，也是"除环代数只有维数 $$1,2,4,8$$"的简洁证明来源。
- **K 理论是广义上同调理论**：由 Atiyah 与 Hirzebruch 基于 Bott 周期建立，球面周期 2（复）/ 8（实）。
- **Chern 特征标**：$$\operatorname{ch}:K^*(X)\otimes\mathbb{Q}\xrightarrow{\cong}H^*(X;\mathbb{Q})$$——有理系数下 K 理论与普通上同调同构；**Atiyah–Singer 指标定理**即"解析指标 = 拓扑指标（用 $$\operatorname{ch}$$ 与 Todd 类算出）"。
- **与代数的接口**：K 理论与表示环 $$R(G)$$（见表示论）同构于群的 K 理论 $$K_G(\mathrm{pt})$$，是"表示论 ↔ 上同调"的桥梁。

## 4. 代数大师的解题清单（几何/拓扑侧）

1. **先把几何对象翻译成环/代数**：仿射簇 ↔ 有限生成域代数，素理想 ↔ 不可约子簇，局部化 ↔ 芽环。
2. **局部数据用层粘合**：要全局不变量就用 $$\Gamma$$ 的导出函子 $$H^i$$；$$H^1(\mathcal{O}^*)=\operatorname{Pic}$$、Serre 对偶、Riemann–Roch 是标准引擎。
3. **要分类空间就用函子**：$$\pi_1$$（非交换）、$$H_*$$（交换化）、$$H^*$$（带 cup 积）。Hurewicz 把 $$\pi_1$$ 与 $$H_1$$ 接起来。
4. **覆盖与 Galois 是同一件事的两种语言**：子群 ↔ 覆盖、正规子群 ↔ Galois 覆盖——与域扩张的 Galois 对应完全平行。
5. **要更强的上同调就用 K 理论**：向量丛的 Grothendieck 群 + Bott 周期；Chern 特征标在有理性上退回普通上同调。
