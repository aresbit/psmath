# 计数与生成函数 (Counting & Generating Functions)

> 整理自：Stanford CS109《Probability for Computer Scientists》第 1 章（计数与组合学）；剑桥 Part IA 概率论第 2 章（组合学与斯特林公式）、第 9 章（概率生成函数）；鸽巢原理的图论用法整理自 Reinhard Diestel《Graph Theory》体系下的入门讲义。

## 1. 地基：分步计数与「或」计数

**分步计数法则（乘积法则）**：实验分两步，第一步 $$m$$ 种结果、第二步无论第一步如何都有 $$n$$ 种，则总数 $$m\cdot n$$。

这一步法则解释了组合爆炸的量级：真彩模型每像素 $$2^{24}\approx1700$$ 万色，12 像素的图片就有约 $$10^{86}$$ 张（比可观测宇宙原子数 $$10^{80}$$ 多一百万倍）；19×19 围棋局面 $$3^{361}\approx10^{172}$$。**任何需要枚举全部局面的算法都不可行**——这是"问题本质上难"的第一课，也是为什么必须用存在性论证而非暴力枚举。

**「或」计数**：互斥时相加 $$\lvert A\cup B\rvert=\lvert A\rvert+\lvert B\rvert$$；重叠时用**容斥**（inclusion–exclusion）

$$\lvert A\cup B\rvert=\lvert A\rvert+\lvert B\rvert-\lvert A\cap B\rvert .$$

容斥推广到任意多集合；当交为空时退化为互斥计数。一般形式为

$$\Big\lvert\bigcup_{i=1}^{k}A_i\Big\rvert=\sum_{\varnothing\ne S\subseteq[k]}(-1)^{\lvert S\rvert+1}\Big\lvert\bigcap_{i\in S}A_i\Big\rvert .$$

**过计数后纠正**：先生成所有结果，再除以重复倍数（各元素重复次数相同时）或减去多余项。这是处理约束的通用手法。

## 2. 六大组合范式

| 范式 | 公式 |
|---|---|
| 不同对象排列 | $$n!$$ |
| 有相同对象的排列 | $$\dfrac{n!}{n_1!\,n_2!\cdots n_r!}$$ |
| 不同对象组合（无序不放回） | $$\dbinom{n}{r}=\dfrac{n!}{r!\,(n-r)!}$$ |
| 不同对象分桶（可区分对象进 $$r$$ 容器） | $$r^n$$ |
| 相同对象分桶（星条法/隔板法） | $$\dbinom{n+r-1}{n}=\dbinom{n+r-1}{r-1}$$ |
| 按固定大小分桶（多项式系数） | $$\dbinom{n}{n_1,\dots,n_r}=\dfrac{n!}{n_1!\cdots n_r!}$$ |

**星条法**把"$$n$$ 个不可区分对象进 $$r$$ 容器"化成"$$n$$ 个星与 $$r-1$$ 个隔板的排列"，即方程 $$x_1+\cdots+x_r=n$$ 的非负整数解数。若允许"不必用完"（不等号约束），加一个"自己"的容器即可。

**大 $$n$$ 渐近**：斯特林公式

$$n!\sim\sqrt{2\pi n}\left(\frac{n}{e}\right)^n ,$$

把阶乘估计化为标准工具，也是 $$\binom{n}{k}\approx n^k/2^{k(k-1)/2}$$ 这类估计的来源（Ramsey 下界就靠它）。

## 3. 鸽巢原理

$$n+1$$ 个对象放进 $$n$$ 个盒子，必有一盒有至少 2 个。这是"纯存在性"论证的最便宜形式，威力却在嵌套使用：$$R(3,3)=6$$ 的证明只用一句"某个顶点 5 条边中至少 3 条同色"（鸽巢）；Erdős–Szekeres 定理 $$n^2+1$$ 项必有长 $$n+1$$ 单调子列，也是把每个元素的两元组（最长递增/递减子列长度）装进 $$n^2$$ 个盒子。**鸽巢常出现在"证明某个阈值足够大"的收尾处。**

## 4. 生成函数：把卷积变成乘法

设 $$X$$ 取值于 $$\mathbb N$$，PMF 为 $$p_r=\mathbb P(X=r)$$。其**概率生成函数（PGF）**

$$p(z)=\mathbb E[z^X]=\sum_{r\ge0}p_rz^r .$$

在 $$\lvert z\rvert\le1$$ 绝对收敛，且**唯一决定分布**（令 $$z\to0$$ 逐项读出 $$p_0,p_1,\dots$$）。

**核心性质：独立和的 PGF = 各 PGF 之积。** 若 $$X_1,\dots,X_n$$ 独立，则

$$p_{X_1+\cdots+X_n}(z)=p_{X_1}(z)\cdots p_{X_n}(z).$$

这条把"求独立和的分布"（卷积）化成"多项式相乘"。推论立刻出来：独立 Bernoulli 之和是二项（$$(pz+1-p)^n$$）、独立 Poisson 之和是 Poisson（$$e^{\lambda_1(z-1)}e^{\lambda_2(z-1)}=e^{(\lambda_1+\lambda_2)(z-1)}$$）。

**由 PGF 求矩**：

$$p'(1^{-})=\mathbb E[X],\qquad p^{(k)}(1^{-})=\mathbb E[X(X-1)\cdots(X-k+1)],$$

$$\operatorname{Var}(X)=p''(1^{-})+p'(1^{-})-\big(p'(1^{-})\big)^2 .$$

**随机个随机变量之和**：$$X_i$$ i.i.d.、$$N$$ 独立于它们，则 $$S_N=\sum_{i=1}^{N}X_i$$ 的 PGF 是**复合**

$$r(z)=\mathbb E[z^{S_N}]=q(p(z)),\qquad q(z)=\mathbb E[z^N],\ p(z)=\mathbb E[z^{X_i}],$$

给出 Wald 型公式 $$\mathbb E[S_N]=\mathbb E[N]\,\mathbb E[X_i]$$ 与条件方差分解

$$\operatorname{Var}(S_N)=\mathbb E[N]\operatorname{Var}(X_i)+\operatorname{Var}(N)\big(\mathbb E[X_i]\big)^2 .$$

**组合学里的同一技术**：Cayley 公式 $$n^{n-2}$$ 靠 Prüfer 编码把标号树与长度 $$n-2$$ 的序列双射；slice-rank 方法里用生成函数上界 $$\inf_{0<x<1}\frac{(1+x+x^2)^n}{x^{2n/3}}\le 2.76^n$$（见 `additive-combinatorics`）。**看到"递归计数""求和""卷积"，先想生成函数。**

## 5. 快速判据：这个问题该用哪个工具

- 出现"或 / 至少一个 / 全部" → 容斥或补集。
- 出现"分步 / 独立选择" → 乘积法则。
- 出现"无序选取 / 方程非负解" → 二项系数 / 星条法。
- 出现"必有一组满足某性质" → 鸽巢。
- 出现"独立和的分布 / 递归计数 / 求矩" → 生成函数。
- 出现"某量从两个角度数" → 双计数（见 `graph-structures-and-matching` 与 `extremal-graph-theory`）。
