# 正则性、伪随机与图极限 (Regularity, Pseudorandomness & Graph Limits)

> 整理自：Szemerédi (1975)、Chung–Graham–Wilson (1989)、Alon–Boppana、Razborov 原始结果；教材框架取自 Yufei Zhao《Graph Theory and Additive Combinatorics》(MIT 18.217) 的 Szemerédi 正则引理、伪随机图、图极限三章（Lecture 6–17）。

## 1. Szemerédi 正则引理：把大图切碎成"近似随机"的块

记 $$e_G(X,Y)$$ 为 $$X,Y$$ 间边数，边密度 $$d_G(X,Y)=e_G(X,Y)/(\lvert X\rvert\lvert Y\rvert)$$。

**定义（$$\varepsilon$$-正则对）**：二部图 $$(X,Y)$$ 是 $$\varepsilon$$-正则的，若对任意 $$A\subseteq X,B\subseteq Y$$ 且 $$\lvert A\rvert\ge\varepsilon\lvert X\rvert,\lvert B\rvert\ge\varepsilon\lvert Y\rvert$$，有

$$\lvert d(A,B)-d(X,Y)\rvert\le\varepsilon .$$

直觉：正则对的任意"够大"子对，其密度都接近整体密度——边分布像随机二部图。

**定义（$$\varepsilon$$-正则划分）**：划分 $$\mathcal P=\{V_1,\dots,V_k\}$$ 是 $$\varepsilon$$-正则的，若所有非正则对的总规模 $$\sum_{\text{not }\varepsilon\text{-reg}}\lvert V_i\rvert\lvert V_j\rvert\le\varepsilon\lvert V(G)\rvert^2$$（允许少量不规则对，只要总规模不大）。有均衡（equitable）版：各部分大小差至多 1。

**定理（Szemerédi 正则引理, 1975）**：对任意 $$\varepsilon>0$$，存在常数 $$M$$，使每个图都有至多 $$M$$ 部分的 $$\varepsilon$$-正则划分。

**证明：能量增量论证（energy increment）**。定义**能量**

$$q(U,W)=\frac{\lvert U\rvert\lvert W\rvert}{n^2}d(U,W)^2,\qquad q(\mathcal P)=\sum_{i,j}q(V_i,V_j),$$

它是 $$d(V_i,V_j)^2$$ 的加权和，介于 0 与 1 之间，是 $$L^2$$ 量。全程两条：
1. **加细不降能量**：$$\mathcal P'$$ 加细 $$\mathcal P$$ 则 $$q(\mathcal P')\ge q(\mathcal P)$$；由卷积/平方给出 $$q(\mathcal P_U,\mathcal P_W)\ge q(U,W)$$。
2. **能量提升引理（"Red Bull"）**：若 $$(U,W)$$ 非 $$\varepsilon$$-正则（由 $$U_1,W_1$$ 见证），则拆成 $$\{U_1,U\setminus U_1\},\{W_1,W\setminus W_1\}$$ 后能量增加至少 $$\varepsilon^4\frac{\lvert U\rvert\lvert W\rvert}{n^2}$$。

于是从平凡划分反复加细，能量每次至少增 $$\varepsilon^5$$ 而能量 $$\le1$$，至多 $$\varepsilon^{-5}$$ 步终止。

**关于部分数**：$$k$$ 部分经一次加细至多 $$k2^k\le2^{2^k}$$ 部分，迭代 $$\varepsilon^{-5}$$ 次给出**塔函数（tower / tetration）**量级的上界。**Gowers 定理**证明这个塔式上界本质最优：存在图，其所有 $$\varepsilon$$-正则划分至少需要 tower 高度 $$\varepsilon^{-c}$$ 个部分——所以由正则引理导出的界常数不可避免地巨大。

## 2. 三角形计数与删除引理：三步"配方"

正则引理的典型用法是 **划分（Partition）→ 清洗（Clean）→ 计数（Count）**。

**三角形计数引理**：若 $$(X,Y),(Y,Z),(Z,X)$$ 都 $$\varepsilon$$-正则，密度 $$d_{XY},d_{XZ},d_{YZ}\ge2\varepsilon$$，则 $$(X,Y,Z)$$-三角形数至少

$$(1-2\varepsilon)(d_{XY}-\varepsilon)(d_{XZ}-\varepsilon)(d_{YZ}-\varepsilon)\lvert X\rvert\lvert Y\rvert\lvert Z\rvert .$$

**三角形删除引理（Ruzsa–Szemerédi）**：对任意 $$\varepsilon>0$$ 存在 $$\delta>0$$，使 $$n$$ 顶点图中若三角形数少于 $$\delta n^3$$，则删去至多 $$\varepsilon n^2$$ 条边即可无三角形。

**证明（三步配方）**：取 $$\varepsilon/4$$-正则划分，删除三类"坏"对之间的边：(a) 不规则对（$$\le(\varepsilon/4)n^2$$）；(b) 低密度对（密度 $$<\varepsilon/2$$，$$\le(\varepsilon/2)n^2$$）；(c) 小部分（$$\le(\varepsilon/4M)n$$，$$\le(\varepsilon/4)n^2$$）。合计 $$<\varepsilon n^2$$。若清洗后仍有三角形，由计数引理它诱导 $$\ge\delta n^3$$ 个三角形，与假设矛盾。**$$\delta$$ 对塔函数常数 $$M$$ 的依赖使 $$1/\delta$$ 是高度约 $$\varepsilon^{-O(1)}$$ 的塔**——这是图论重大开放问题（最好下界 $$1/\delta$$ 需 $$\varepsilon^{-O(\log1/\varepsilon)}$$）。

**推论（每条边恰在唯一三角形中）**：若 $$G$$ 每条边恰在唯一三角形中，则 $$e(G)=o(n^2)$$。证明：三角形数 $$m/3=o(n^3)$$，删 $$o(n^2)$$ 条边即可无三角形，但每条边至少删掉一个三角形，故 $$m/3\le o(n^2)$$。

**更大的删除/计数/嵌入引理**：图嵌入引理（正则对密度 $$>2\varepsilon^{1/\Delta}$$ 则含任意 bounded-degree $$r$$-部 $$H$$ 拷贝）；图计数引理（拷贝数接近 $$\prod d(V_i,V_j)\prod\lvert V_i\rvert$$）；图删除引理（$$H$$ 拷贝少则删 $$\varepsilon n^2$$ 条边可无 $$H$$）。**诱导**删除引理允许增删边（编辑距离），需**强正则引理**，常数是塔函数的迭代（"wowzer" 函数，Ackermann 层级再上一级）。超图正则性沿 Ackermann 层级攀升：2-图需 TOWER，3-图需 WOWZER，4-图再上一级。

**应用·Roth 定理的图论证明**：取 $$M=2N+1$$，把无 3-AP 集 $$A\subseteq[N]$$ 嵌入 $$\mathbb Z/M\mathbb Z$$，构造三部图（三部都是 $$\mathbb Z/M\mathbb Z$$ 的拷贝，$$x\sim y\iff y-x\in A$$ 等）。若 $$x,y,z$$ 成三角形则对应平凡 AP，于是 $$G$$ 每条边恰在唯一三角形中，由推论得 $$e(G)=o(M^2)$$；而 $$e(G)=3M\lvert A\rvert$$，故 $$\lvert A\rvert=o(N)$$（界为 $$N/\log^*N$$）。**无 3-AP 集的下界构造**：Stanley 序列（三进制只含 0,1，大小 $$N^{\log_3 2}$$）；Behrend 构造（高维格子球面无 3-AP，嵌入得 $$>Ne^{-C\sqrt{\log N}}$$，自 1940 年代几乎未被改进）。

## 3. 拟随机图：最弱的 C4 条件蕴含全部随机性

**定理（Chung–Graham–Wilson）**：图序列 $$\{G_n\}$$ 满足 $$\lvert V(G_n)\rvert=n$$、边数 $$(p+o(1))\binom n2$$（$$0<p<1$$ 固定）。以下六条**等价**：

| 判据 | 内容 |
|---|---|
| DISC | 对所有 $$X,Y$$，$$\lvert e(X,Y)-p\lvert X\rvert\lvert Y\rvert\rvert=o(n^2)$$ |
| DISC' | 对所有 $$X$$，$$\lvert e(X)-p\binom{\lvert X\rvert}2\rvert=o(n^2)$$ |
| COUNT | 对所有图 $$H$$，带标号 $$H$$ 拷贝数 $$=(p^{e(H)}+o(1))n^{v(H)}$$ |
| C4 | $$C_4$$ 带标号拷贝数至多 $$(p^4+o(1))n^4$$ |
| CODEG | $$\sum_{u,v}\lvert\text{codeg}(u,v)-p^2n\rvert=o(n^3)$$ |
| EIG | 邻接矩阵特征值 $$\lambda_1=pn+o(n)$$ 且 $$\max_{i\ne1}\lvert\lambda_i\rvert=o(n)$$ |

最惊人的是**最弱的 C4 条件（只控制 4-环数）蕴含其余全部**。证明是 Cauchy–Schwarz 的连续应用；EIG ⟺ C4 通过 $$\operatorname{tr}(A_G^4)=\sum_i\lambda_i^4$$ 与 Courant–Fischer 极小极大定理双向推导。**关键限制：只对稠密图（$$p$$ 常数）成立**。稀疏图（$$p=p_n\to0$$）的类比不等价——计数引理失效（如 $$p=o(n^{-1/2})$$ 时从 $$G(n,p)$$ 删掉每个三角形的一条边，仍满足稀疏 DISC 却无三角形）。

**扩张混合引理（Alon）**：$$G$$ 是 $$n$$ 顶点 $$d$$-正则，$$\lambda=\max\{\lvert\lambda_2\rvert,\lvert\lambda_n\rvert\}$$，则对所有 $$X,Y\subseteq V$$，

$$\Big\lvert e(X,Y)-\frac dn\lvert X\rvert\lvert Y\rvert\Big\rvert\le\lambda\sqrt{\lvert X\rvert\lvert Y\rvert}.$$

**含义**：实际边数与"随机 $$d$$-正则图应出现的期望边数"之差被 $$\lambda$$ 控制；$$\lambda$$ 相对 $$d$$ 越小，图越像随机图（**伪随机**）。**Chung 判据**：$$d$$-正则图族准随机 ⟺ $$\lambda_2=o(d)$$。

**Alon–Boppana 界**：固定 $$d$$，$$n$$ 顶点 $$d$$-正则图有 $$\lambda_2\ge2\sqrt{d-1}-o(1)$$。证明一（Rayleigh 商）构造 $$x_u=(d-1)^{-i/2}$$（$$u$$ 距中心 $$v$$ 距离 $$i$$）再线性组合正交化；证明二（矩方法）用 $$d$$-正则树中长 $$2k$$ 闭游走数 $$\ge$$ Catalan 数 $$\frac1{k+1}\binom{2k}k(d-1)^k$$。$$2\sqrt{d-1}$$ 正是无限 $$d$$-正则树的谱半径。

**Ramanujan 图**：$$d$$-正则图若 $$\lvert\lambda_2\rvert,\lvert\lambda_n\rvert\le2\sqrt{d-1}$$（达到 Alon–Boppana 下界）。猜想对所有 $$d\ge3$$ 存在无穷多个；$$d-1$$ 为素数（Lubotzky–Phillips–Sarnak、Margulis, 1988）或素数幂（Morgenstern, 1994）时成立，$$d=7$$ 仍开放；Marcus–Spielman–Srivastava (2015) 对所有 $$d$$ 构造无穷多二分 Ramanujan 图。

**Paley 图**：$$Cay(\mathbb Z/p\mathbb Z,S)$$（$$S$$ 为非零二次剩余），非平凡特征值 $$\le\frac{\sqrt p+1}2$$（Gauss 和）——揭示 Cayley 图特征值与群上 Fourier 系数其实是同一回事。**稀疏正则与 Green–Tao**：素数含任意长 AP，策略是把素数以高相对密度嵌入"伪素数"（无小素因子数），用筛法验证其足够伪随机，再套稀疏超图删除引理。

## 4. 图极限：稠密图的"完备化"

正如有理数完备化为实数，图的完备化是 **graphon**。动机：固定边密度 $$p$$ 时最小化 $$C_4$$ 密度，极小值 $$p^4$$ 由拟随机图序列取到，**没有单个有限图能达到**。

**定义（graphon）**：对称可测函数 $$W:[0,1]^2\to[0,1]$$（值域放宽到 $$\mathbb R$$ 时称 kernel）。图的 graphon：把 $$[0,1]$$ 分成 $$n$$ 个等测度区间，$$W_G(x,y)=1$$ 若 $$(x,y)\in I_i\times I_j$$ 且 $$i,j$$ 相邻。

**同态密度** $$t(H,G)=\lvert\operatorname{Hom}(H,G)\rvert/\lvert V(G)\rvert^{\lvert V(H)\rvert}$$；对 graphon

$$t(H,W)=\int_{[0,1]^{\lvert V(H)\rvert}}\prod_{ij\in E(H)}W(x_i,x_j)\prod_i dx_i .$$

**割范数** $$\lVert W\rVert_\square=\sup_{S,T\subseteq[0,1]}\lvert\int_{S\times T}W\rvert$$；**割距离** $$\delta_\square(U,W)=\inf_\varphi\lVert U-W^\varphi\rVert_\square$$（$$\varphi$$ 保测双射，即"重标号顶点"，还允许分裂/合并顶点）。

**三个主定理**：
- **收敛等价**：图列收敛（每个 $$H$$ 的 $$t(H,G_n)$$ 收敛）⟺ 它是割距离下的 Cauchy 列。
- **极限存在**：每个收敛图列都有极限 graphon。
- **紧性**：graphon 空间（模割距离为 0 的等价类）$$\widetilde{\mathcal W}_0$$ 在割度量下是紧度量空间。

紧性可看作正则引理的"定性版本"：图的本质不同空间其实很小。

**W-随机图**：均匀取 $$x_1,\dots,x_n$$，顶点 $$i,j$$ 以概率 $$W(x_i,x_j)$$ 相连（推广 Erdős–Rényi 与随机块模型）。**定理**：$$G_n$$ 独立取自 $$W$$-随机图则 $$G_n\to W$$ 几乎必然（Azuma 不等式）。**计数引理**：$$\lvert t(F,W)-t(F,U)\rvert\le\lvert E(F)\rvert\,\delta_\square(W,U)$$。**弱正则引理**：任意 graphon $$W$$ 存在至多 $$4^{1/\varepsilon^2}$$ 个可测集的分划使 $$\lVert W-W_{\mathcal P}\rVert_\square\le\varepsilon$$（$$L^2$$ 能量增量证明）。**应用·MAXCUT**：给稠密图 MAXCUT 的加性 $$\varepsilon n^2$$ 近似（与 Goemans–Williamson 0.878 及 Unique Games 猜想对照）。

**graphon 强正则引理**：每个 $$W$$ 可分解 $$W=W_{str}+W_{psr}+W_{sml}$$（结构阶梯 + 伪随机 + 小块）；取 $$\varepsilon_k=\varepsilon/k^2$$ 恢复 Szemerédi 正则引理，取 $$\varepsilon_k=\varepsilon$$ 恢复弱正则引理。

## 5. 子图密度不等式与旗代数

可行区域

$$D_{2,3}=\{(t(K_2,W),t(K_3,W)):W\text{ graphon}\}\subseteq[0,1]^2 .$$

- Mantel（graphon 形式）：$$t(K_3,W)=0\Rightarrow t(K_2,W)\le1/2$$。
- 上边界：$$t(K_3,W)\le t(K_2,W)^{3/2}$$（谱：$$\sum\lambda_i^3\le(\sum\lambda_i^2)^{3/2}$$）。
- 下边界凸包极值点由团 $$K_m$$ 给出（**Bollobás 定理**：线性不等式对所有图成立 ⟺ 对所有 $$G=K_m$$ 成立），点 $$p_m=(\frac{m-1}m,\frac{(m-1)(m-2)}{m^2})$$ 落在 $$y=x(2x-1)$$ 上。
- 完整区域 $$D_{2,3}$$ 由 **Razborov 的旗代数（flag algebras）** 确定，下边界有凹"扇贝"形状。

**判定问题的深浅**：多项式非负性对 $$\mathbb R^n$$ 可判定（Tarski），对 $$\mathbb Z^n$$ 不可判定（Matiyasevich，Hilbert 第 10 问题）；图密度线性不等式是否对所有图成立**不可判定**（Hatami–Norine），但带 $$\varepsilon$$-误差可行（弱正则引理化为有限加权图）。

**Sidorenko 猜想**：若 $$H$$ 二分，则 $$t(H,W)\ge t(K_2,W)^{e(H)}$$。对 $$H=C_4$$ 成立，但对 Möbius 带图（$$K_{5,5}$$ 去掉一个 10-环）仍开放。
