# 谱方法 (Spectral Methods in Combinatorics)

> 整理自：Wilf、Hoffman、Alon–Milman、Chung、Alon–Boppana 原始结果；教材框架取自 Daniel A. Spielman《Spectral Graph Theory》(Yale) 与 Reinhard Diestel《Graph Theory》谱图理论章节，及 Yufei Zhao《Graph Theory and Additive Combinatorics》(MIT 18.217) 伪随机图章的谱视角。

## 1. 从图到矩阵

- **邻接矩阵** $$A$$：$$A_{uv}=1\iff u\sim v$$。
- **拉普拉斯矩阵** $$L=D-A$$（$$D=\operatorname{diag}(d(u))$$）；正规化 $$L_{\text{norm}}=I-D^{-1/2}AD^{-1/2}$$。

**心智模型**：特征值不是数字游戏，而是"图上的振动模式"。$$A$$ 的特征值刻画图上的平稳涨落，$$L$$ 的特征值刻画"切断图的难易"。大特征值 = 高度连接/规整；谱间隙 = 图多像一个整体（扩张性）。由此谱方法给出色数、独立数、切割、随机游走收敛的一整套定量工具。

## 2. 邻接谱的基本性质

设 $$A$$ 的特征值 $$\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n$$（$$A$$ 实对称，全实）。

- **Perron–Frobenius / Rayleigh 商**：$$\lambda_1=\max_{x\ne0}\frac{x^TAx}{x^Tx}$$，对应特征向量可取全非负。
- **度数夹逼**：$$\bar d\le\lambda_1\le\Delta(G)$$；$$\lambda_1=\Delta$$ 当且仅当有一个度为 $$\Delta$$ 的正则连通分支。特别地 $$d$$-正则图 $$\lambda_1=d$$。
- **二部性**：$$G$$ 二部 ⟺ 谱关于 0 对称（$$\lambda$$ 是特征值 ⟺ $$-\lambda$$ 也是，重数相同）⟺ $$\lambda_n=-\lambda_1$$。这是"二部 ⟺ 无奇圈 ⟺ 可 2-着色"的谱表达。

## 3. 谱界定图不变量

**Wilf（色数上界）**：

$$\chi(G)\le\lambda_1+1 .$$

证明：贪心着色时每次至少可删去一个度 $$\le\lfloor\lambda_1\rfloor$$ 的顶点。

**Hoffman（独立数上界）**：$$G$$ 是 $$d$$-正则图，则

$$\alpha(G)\le n\cdot\frac{-\lambda_n}{d-\lambda_n}.$$

**无三角形的谱判定（Mantel 的谱证明）**：$$G$$ 无三角形则

$$\lambda_1\le\sqrt{n-1}.$$

由 $$\lambda_1^2\le\sum_i\lambda_i^2=\operatorname{tr}(A^2)=2m$$ 及 Mantel 上界 $$m\le n^2/4$$ 可得——谱方法由此独立复现了 `extremal-graph-theory` 的 Mantel 定理。

## 4. 拉普拉斯谱与谱间隙

$$L$$ 的特征值 $$0=\mu_1\le\mu_2\le\cdots\le\mu_n$$（半正定，全 1 向量是 $$\mu_1=0$$ 的特征向量）。

**连通性判定**：$$\mu_2>0\iff G$$ 连通。$$\mu_2$$ 称**代数连通度**或 **Fiedler 值**，越大图越"难断开"。

**切割的谱刻画**：对 $$S\subseteq V$$，

$$e(S,V\setminus S)=\sum_{v\in S,u\notin S}A_{vu}=\frac14\sum_{uv}(x_u-x_v)^2,\qquad x=\mathbf 1_S-\mathbf 1_{V\setminus S},$$

即切割边数与"指示向量的 Dirichlet 能量"成正比——Cheeger 不等式与谱聚类的源头。

## 5. Cheeger 不等式

**导率（conductance）/等周比**：

$$h(G)=\min_{S\subseteq V,\ \lvert S\rvert\le n/2}\frac{e(S,V\setminus S)}{\lvert S\rvert}.$$

**Cheeger 不等式（Alon–Milman / Dodziuk）**：对 $$d$$-正则图，$$\lambda_2=d-\mu_2$$，

$$\frac{h^2}{2d}\le\lambda_2\le2h\qquad\Big(\text{等价：}\ \frac{h^2}{2\Delta}\le\mu_2\le2h\Big).$$

**深意**：谱间隙小（$$\lambda_2$$ 小 ⟺ $$\mu_2$$ 大）与"图难以切成两块"严格等价。**扩张图（expander）**就是谱间隙有界于常数的稀疏图——稀疏却极难切割，是网络、编码、随机游走快速混合、去随机化的基石。

## 6. 伪随机性的谱判据

**$$(n,d,\lambda)$$-图**：$$n$$ 顶点 $$d$$-正则，且除 $$\lambda_1=d$$ 外所有特征值 $$\lvert\lambda_i\rvert\le\lambda$$。

**扩展混合引理（Alon）**：对任意 $$S,T\subseteq V$$，

$$\Big\lvert e(S,T)-\frac{d\lvert S\rvert\lvert T\rvert}{n}\Big\rvert\le\lambda\sqrt{\lvert S\rvert\lvert T\rvert}.$$

**含义**：实际边数与随机 $$d$$-正则图期望边数之差被 $$\lambda$$ 控制；$$\lambda$$ 越小图越像随机图。**Chung 的准随机刻画**：$$d$$-正则图族准随机 ⟺ $$\lambda_2=o(d)$$——与正则引理的 $$\varepsilon$$-正则对一脉相承。

**Alon–Boppana 界**：固定 $$d$$，$$n$$ 顶点 $$d$$-正则图有 $$\lambda_2\ge2\sqrt{d-1}-o(1)$$。达到此下界的图称 **Ramanujan 图**（$$\lvert\lambda_2\rvert,\lvert\lambda_n\rvert\le2\sqrt{d-1}$$），是"最优伪随机"的极限；$$2\sqrt{d-1}$$ 正是无限 $$d$$-正则树的谱半径。

## 7. 随机游走与谱

转移矩阵 $$P=D^{-1}A$$（平稳分布 $$\pi$$）。收敛速率由第二特征值决定的谱间隙控制：

$$\lVert P^t\pi_0-\pi\rVert_2\le\Big(\frac{\lambda_2}{\lambda_1}\Big)^t .$$

谱间隙越大，游走混合越快。这一框架统一了 PageRank、谱聚类、扩张图上的采样与近似计数。

## 8. 矩阵树定理（谱形式的计数）

生成树个数 = 拉普拉斯矩阵 $$L$$ 的任意余子式（Kirchhoff）；若 $$L$$ 的非零特征值为 $$\mu_2,\dots,\mu_n$$，则

$$\tau(G)=\frac1n\prod_{i=2}^{n}\mu_i .$$

对 $$K_n$$：$$\tau(K_n)=\frac1n n^{n-1}=n^{n-2}$$，与 Cayley 公式一致（见 `graph-structures-and-matching`）。这是"计数 → 线性代数"最干净的桥。

## 9. 正则引理的谱证明（Tao 的正则分解视角）

把邻接矩阵谱分解 $$A_G=\sum_i\lambda_i u_iu_i^T$$，按"结构/小/伪随机"三层分解：

$$A_G=A_{str}+A_{sml}+A_{psr}=\sum_{i<J}\lambda_i u_iu_i^T+\sum_{J\le i<F(J)}\lambda_i u_iu_i^T+\sum_{i\ge F(J)}\lambda_i u_iu_i^T,$$

选 $$J$$ 使 $$\sum_{J\le i<F(J)}\lambda_i^2\le\varepsilon n^2$$。$$A_{str}$$ 对应有界划分（大特征值向量确定的分区），$$A_{sml}$$ 对应不规则对（Frobenius 范数小），$$A_{psr}$$ 对应对间伪随机性。这给出与能量增量论证平行的谱版本正则引理证明，是 Tao 倡导的正则分解视角（详见 `regularity-and-graph-limits`）。

## 10. 速查

- $$\bar d\le\lambda_1\le\Delta$$；$$d$$-正则 $$\lambda_1=d$$；二部 ⟺ 谱对称。
- $$\chi\le\lambda_1+1$$；$$d$$-正则 $$\alpha\le n\frac{-\lambda_n}{d-\lambda_n}$$；无三角形 $$\lambda_1\le\sqrt{n-1}$$。
- $$\mu_2>0\iff$$ 连通；切割 = Dirichlet 能量。
- Cheeger：$$\frac{h^2}{2d}\le\lambda_2\le2h$$。
- 扩展混合引理：$$\lvert e(S,T)-\frac dn\lvert S\rvert\lvert T\rvert\rvert\le\lambda\sqrt{\lvert S\rvert\lvert T\rvert}$$；$$\lambda_2=o(d)\iff$$ 准随机。
- 矩阵树：$$\tau(G)=\frac1n\prod_{i\ge2}\mu_i$$。
