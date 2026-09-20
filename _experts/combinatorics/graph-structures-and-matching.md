# 图的结构与匹配 (Graph Structure & Matching)

> 整理自：Reinhard Diestel《Graph Theory》(5th ed., Springer GTM 173) 与 Yufei Zhao《Graph Theory and Additive Combinatorics》所覆盖的图论基础（度与握手引理、路/圈/连通与 Menger、树与 Cayley、矩阵树定理、匹配 Hall/Kőnig/Tutte、着色 Brooks/Vizing、平面图 Euler/Kuratowski）。

## 1. 度与握手引理：最便宜的计数工具

图 $$G=(V,E)$$，$$n=\lvert V\rvert$$，$$m=\lvert E\rvert$$，顶点度 $$d(v)$$。

**握手引理**：$$\displaystyle\sum_{v\in V}d(v)=2m$$。

推论：奇度顶点个数必为偶数；$$d$$-正则图满足 $$m=nd/2$$。这条引理几乎只用来"排除某类图存在"，是所有双计数论证的原型。最大/最小度记 $$\Delta(G),\ \delta(G)$$。

**基本对偶对象**：独立数 $$\alpha(G)$$（内部无边的最大点集）、团数 $$\omega(G)$$（两两相邻的最大点集）、顶点覆盖数 $$\tau(G)$$（与每条边相交的最小点集）。三者在匹配与谱理论里反复出现（见第 3、4 节与 `spectral-methods`）。

## 2. 路、圈与连通：Menger 的 max–min 对偶

- 二部图 ⟺ 不含奇圈（最常用判定）。
- **Menger 定理（顶点版）**：$$s,t$$ 间内部不相交路径的最大条数 = 分离 $$s,t$$ 所需删去的最少顶点数。
- **Menger 定理（边版）**：$$s,t$$ 间边不相交路径的最大条数 = 分离 $$s,t$$ 所需删去的最少边数。
- Whitney：$$\kappa(G)\le\lambda(G)\le\delta(G)$$。
- **Euler 定理**：连通图有 Euler 回路 ⟺ 每个顶点度为偶数（柯尼斯堡七桥：四顶点皆奇度，故无解）。
- **Dirac/Ore**：$$\delta(G)\ge n/2$$（或任意不相邻 $$u,v$$ 有 $$d(u)+d(v)\ge n$$）⟹ 含 Hamilton 圈。

**心智模型**：Menger 与最大流–最小割本质是同一件事——"能同时容纳多少条互不相交的连接 = 要花多大代价切断它们"。这是全组合学 "max = min" 型对偶的源头，与 Kőnig 定理、线性规划对偶一脉相承。

## 3. 树：最省的连通结构

$$n$$ 顶点树恰好 $$n-1$$ 条边。**等价刻画**：连通 + $$n-1$$ 边 ⟺ 无圈 + $$n-1$$ 边 ⟺ 连通且每条边是桥 ⟺ 任意两点间恰有一条路 ⟺ 无圈且加任意一条边恰成一个圈。任何非平凡树至少两个叶子。

**Cayley 公式**：$$n$$ 个标号顶点上的树共有 $$n^{\,n-2}$$ 棵。证明用 **Prüfer 编码**建立树与长 $$n-2$$ 序列的双射：反复删去当前最小标号叶子并记录其邻居；反之从序列逐位重建。因为 $$K_n$$ 的生成树恰是全部标号树，这也给出 $$K_n$$ 的生成树计数 $$n^{n-2}$$。

**矩阵树定理（Kirchhoff）**：生成树个数 = 拉普拉斯矩阵 $$L=D-A$$ 的任意余子式。谱形式：若 $$L$$ 的非零特征值为 $$\mu_2,\dots,\mu_n$$，则

$$\tau(G)=\frac1n\prod_{i=2}^{n}\mu_i .$$

（$$L$$ 必有特征值 0，全 1 向量是其核。）对 $$K_n$$：$$\tau(K_n)=\frac1n n^{n-1}=n^{n-2}$$，与 Cayley 一致——这是"计数 → 线性代数"的桥。

**MST 贪心正确性**：割性质（横跨割的最轻边必在某棵 MST）与圈性质（某圈中最重的边不在任何 MST）。Kruskal 用并查集，$$O(m\log m)$$；Prim 用堆，$$O(m\log n)$$。贪心即最优的底层原因是树结构满足**拟阵（matroid）**交换性质。

## 4. 匹配：存在性判据与构造算法

匹配 $$M$$ 是不共享端点的边集；$$d$$-正则二部图必有完美匹配。两条主线：**增广路**（怎么求）与 **Hall/Tutte 型条件**（何时存在）。

**Berge 定理**：$$M$$ 是最大匹配 ⟺ 不存在关于 $$M$$ 的增广路（起止于未匹配顶点、边在内外交替）。沿增广路翻转使 $$\lvert M\rvert$$ 加 1；二部图上反复找增广路（Hopcroft–Karp，$$O(\sqrt n\,m)$$）。

**Hall 婚姻定理**：二部图 $$G=(A,B)$$ 存在饱和 $$A$$ 的匹配 ⟺ 对任意 $$S\subseteq A$$，

$$\lvert N(S)\rvert\ge\lvert S\rvert .$$

缺陷形式：$$A$$ 中无法匹配的最大顶点数 $$=\max_{S\subseteq A}(\lvert S\rvert-\lvert N(S)\rvert)$$。

**Kőnig 定理**：二部图中 $$\nu(G)=\tau(G)$$（最大匹配 = 最小顶点覆盖），二者互为 LP 对偶。非二部图一般不成立（$$C_5$$：$$\nu=2,\tau=3$$）。

**Tutte 定理（一般图完美匹配）**：$$G$$ 有完美匹配 ⟺ 对任意 $$S\subseteq V$$，$$o(G-S)\le\lvert S\rvert$$（$$o$$ 为奇分支数）。推广的 **Tutte–Berge 公式**：

$$\nu(G)=\frac12\min_{S\subseteq V}\big(n+\lvert S\rvert-o(G-S)\big).$$

推论（Petersen）：无桥 3-正则图有完美匹配。

**Gale–Shapley 稳定婚姻**：延迟接受算法 $$O(n^2)$$ 必得稳定匹配，且对主动方最优、对被动方最劣。

## 5. 着色：把点集切成独立集

**色数** $$\chi(G)$$ = 最少颜色数。每个色类是独立集，故

$$\chi(G)\ge\frac{n}{\alpha(G)},\qquad \chi(G)\ge\omega(G).$$

**贪心上界** $$\chi\le\Delta+1$$。**Brooks 定理**：连通非完全、非奇圈图满足 $$\chi\le\Delta$$。

**平面图**：五色定理可构造（归纳删除度 $$\le5$$ 的顶点 + Kempe 链交换两色）；四色定理（Appel–Haken 1976，计算机穷举，2005 年 Gonthier 用 Coq 形式化）。

**边着色**：$$\chi'(G)\ge\Delta$$；**Vizing**：$$\Delta\le\chi'\le\Delta+1$$（简单图只有两类）；**Kőnig 边着色**：二部图 $$\chi'=\Delta$$。边着色可转为线图 $$L(G)$$ 的顶点着色：$$\chi'(G)=\chi(L(G))$$。

**色多项式** $$P_G(k)$$：$$P_{K_n}(k)=k(k-1)\cdots(k-n+1)$$；删除–收缩递推 $$P_G(k)=P_{G-e}(k)-P_{G/e}(k)$$；$$\chi(G)$$ 是使 $$P_G(k)>0$$ 的最小正整数。系数交错变号（Birkhoff–Lewis）；$$\lvert P_G(-1)\rvert$$ = 无圈定向数（Stanley）。

**Mycielski 警示**：$$\chi\ge\omega$$ 但可差任意大（无三角形图色数可任意大）——色数是全局量。

## 6. 平面图：Euler 公式与禁子图

**Euler 公式**：连通平面图 $$n-m+f=2$$（$$f$$ 为面数）。推论：

$$m\le3n-6,\qquad \delta(G)\le5,\qquad \text{无三角形时 } m\le 2n-4 .$$

由此立得 $$K_5$$（$$10>9$$）与 $$K_{3,3}$$（$$9>8$$）非平面。

**Kuratowski 定理**：$$G$$ 平面 ⟺ 不含 $$K_5$$ 或 $$K_{3,3}$$ 的细分。**Wagner（子式版）**：$$G$$ 平面 ⟺ 不以 $$K_5,K_{3,3}$$ 为子式。这就是平面性的"禁子图刻画"，与极值图论（禁 $$H$$ 定 $$\mathrm{ex}(n,H)$$）同一思想。

**子式定理（Robertson–Seymour）**：任何取子式封闭的性质由有限个禁子式刻画——20 世纪组合数学里程碑。

**对偶图** $$G^*$$：$$G$$ 的圈 ↔ $$G^*$$ 的割；$$n^*=f,\ m^*=m,\ f^*=n$$。平面性是全局拓扑性质，可线性时间判定（Hopcroft–Tarjan 1974）。

## 7. 速查不等式

- 握手 $$\sum d(v)=2m$$；Cayley $$n^{n-2}$$；Hall $$\lvert N(S)\rvert\ge\lvert S\rvert$$。
- Kőnig $$\nu=\tau$$（二部）；Tutte $$o(G-S)\le\lvert S\rvert$$；Euler $$n-m+f=2$$。
- Brooks $$\chi\le\Delta$$（例外：$$K_n$$、奇圈）；Vizing $$\Delta\le\chi'\le\Delta+1$$。
- Menger：路径数 = 割数（顶点版/边版）。
