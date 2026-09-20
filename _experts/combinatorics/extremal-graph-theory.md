# 极值图论 (Extremal Graph Theory)

> 整理自：Mantel (1907)、Turán (1941)、Erdős–Stone–Simonovits (1946) 原始结果；教材框架取自 Yufei Zhao《Graph Theory and Additive Combinatorics》(MIT 18.217) 禁止子图章（Lecture 2–5），并含 Diestel《Graph Theory》极值图论章的经典表述。

## 1. 问题与心智模型

**极值问题**：给定禁子图 $$H$$，$$n$$ 个顶点且不含 $$H$$ 的图最多有多少条边？记**极值数**

$$\mathrm{ex}(n,H)=\max\{\lvert E(G)\rvert:\lvert V(G)\rvert=n,\ H\not\subseteq G\}.$$

范式固定三步：**先猜极值图**（结构最规整的图），**再证任何 $$H$$-free 图的边数不超过它**，**最后证明等号只由极值图达到**。最深层的结论（Erdős–Stone）说明极值数的一阶主项**只由 $$H$$ 的色数决定**。

## 2. Mantel 定理：禁止三角形

**定理（Mantel, 1907）**：$$n$$ 顶点无三角形图至多 $$\lfloor n^2/4\rfloor$$ 条边，等号仅当 $$G=K_{\lfloor n/2\rfloor,\lceil n/2\rceil}$$。

**证明 1（Cauchy–Schwarz）**：无三角形时相邻顶点 $$x,y$$ 无公共邻点，故 $$d(x)+d(y)\le n$$，求和 $$\sum_x d(x)^2=\sum_{xy\in E}(d(x)+d(y))\le mn$$。由握手引理 $$\sum_x d(x)=2m$$，Cauchy–Schwarz 给 $$4m^2\le n\sum_x d(x)^2\le mn^2$$，故 $$m\le n^2/4$$。

**证明 2（最大独立集）**：无三角形时每个邻域 $$N(x)$$ 都是独立集。取最大独立集 $$A$$，则所有 $$x$$ 有 $$d(x)\le\lvert A\rvert$$，且每条边都与 $$B=V\setminus A$$ 相交，故 $$e(G)\le\sum_{x\in B}d(x)\le\lvert A\rvert\lvert B\rvert\le n^2/4$$。

**谱证明见 `spectral-methods`**（$$\lambda_1^2\le 2m$$ 与 Mantel 上界推出 $$\lambda_1\le\sqrt{n-1}$$）。

## 3. Turán 定理：禁止团

**Turán 图** $$T_r(n)$$：$$n$$ 顶点完全 $$r$$-部图，各部分大小尽量相等（差至多 1）。

**定理（Turán, 1941）**：若 $$G$$ 不含 $$K_{r+1}$$，则 $$e(G)\le e(T_r(n))$$，等号仅当 $$G\cong T_r(n)$$。记 $$n=qr+s,\ 0\le s<r$$，则

$$e(T_r(n))=\Big(1-\frac1r\Big)\frac{n^2}{2}-\frac{s(r-s)}{2r},$$

渐近主项 $$\mathrm{ex}(n,K_{r+1})=\big(1-\tfrac1r\big)\tfrac{n^2}{2}+O(n)$$。$$r=2$$ 退回 Mantel。

**三个证明**：
1. **对 $$n$$ 归纳**：边数极大的 $$K_{r+1}$$-free 图必含 $$K_r$$（否则可加边）；取 $$r$$-团 $$A$$、$$B=V\setminus A$$，每个 $$v\in B$$ 在 $$A$$ 内至多 $$r-1$$ 个邻点，得 $$e(G)\le\binom r2+(r-1)\lvert B\rvert+e(T_{n-r,r})=e(T_{n,r})$$。
2. **Zykov 对称化**：证明边数极大的 $$K_{r+1}$$-free 图非边构成等价关系，补图是团之并，故 $$G$$ 完全多部；再调整各部大小。核心操作"克隆"：若 $$xy\notin E$$ 且 $$d(y)<d(x)$$，把 $$y$$ 换成 $$x$$ 的克隆，边数增加且仍 $$K_{r+1}$$-free，矛盾。
3. **概率方法**：取顶点均匀随机排序 $$\sigma$$，令 $$X=\{v:v\text{ 与所有更早顶点相邻}\}$$（$$X$$ 是团）。$$\Pr(v\in X)=1/(n-d(v))$$，故 $$r\ge\mathbb E\lvert X\rvert=\sum_v 1/(n-d(v))\ge n/(n-2m/n)$$（凸性），整理得 $$m\le(1-\frac1r)\frac{n^2}{2}$$。

## 4. Erdős–Stone（–Simonovits）：只读色数

**定理（Erdős–Stone, 1946）**：对固定图 $$H$$，$$\chi(H)=r+1\ge3$$，则

$$\mathrm{ex}(n,H)=\Big(1-\frac1r\Big)\frac{n^2}{2}+o(n^2).$$

**定量形式（ESS）**：

$$\mathrm{ex}(n,H)=\Big(1-\frac1{\chi(H)-1}\Big)\binom n2+o(n^2).$$

**深意**：极值数一阶主项**只依赖色数**，与 $$H$$ 的其它结构（大小、形状）无关。色数越大，$$H$$ 越"难被禁止"，可容纳的边越多。例如 Petersen 图色数 3，极值数与三角形相同——反直觉但正确。这是极值图论最重要的单条定理，把整个领域归约为"读出色数"。

## 5. Kővári–Sós–Turán：禁止完全二分图

$$H$$ 二部（$$\chi=2$$）时 ESS 只给平凡的 $$o(n^2)$$，真正的难度是定出 $$n^{2-\varepsilon}$$ 型精确指数，即 **Zarankiewicz 问题**：$$n$$ 顶点不含 $$K_{s,t}$$ 的图最多多少边？

**定理（KST, 1954）**：对 $$1\le s\le t$$，

$$\mathrm{ex}(n,K_{s,t})\le\frac12(t-1)^{1/s}n^{2-1/s}+\frac{s-1}{2}n=O(n^{2-1/s}).$$

**证明（双计数）**：记 $$K_{s,1}$$ 的拷贝数。
- 上界：枚举"左边" $$s$$ 顶点子集，其公共邻点数至多 $$t-1$$，故 $$\#K_{s,1}\le\binom ns(t-1)$$。
- 下界：每个顶点 $$v$$ 作为"右边"贡献 $$\binom{d(v)}s$$，故 $$\#K_{s,1}=\sum_v\binom{d(v)}s\ge n\binom{2m/n}s$$（凸性）。
- 合并得 $$m\le(\frac12+o(1))(t-1)^{1/s}n^{2-1/s}$$。

**应用·单位距离问题**：$$n$$ 个平面点最多形成多少单位距离？单位距离图 $$K_{2,3}$$-free，给 $$O(n^{3/2})$$ 上界；最好下界是 Erdős 的 $$n^{1+c/\log\log n}$$，最好上界 $$O(n^{4/3})$$（交叉数不等式）。对偶的**不同距离问题**由 Guth–Katz 定理给 $$\Omega(n/\log n)$$。

## 6. 三种下界构造

**（a）随机/改动法**：对至少 2 条边的 $$H$$，取随机 $$G(n,p)$$，删掉每个 $$H$$ 拷贝中的一条边，选 $$p$$ 使 $$\mathbb E[\#H]\le\frac12\mathbb E[e(G)]$$，得

$$\mathrm{ex}(n,H)\ge cn^{2-\frac{v(H)-2}{e(H)-1}},\qquad\text{即}\quad \mathrm{ex}(n,H)\ge cn^{2-1/m_2(H)},$$

其中 2-密度 $$m_2(H)=\max_{H'\subseteq H}\frac{e(H')-1}{v(H')-2}$$。

**（b）代数构造·极性图（Erdős–Rényi–Sós）**：$$\mathrm{ex}(n,K_{2,2})\ge(\frac12-o(1))n^{3/2}$$。取 $$n=p^2-1$$，顶点集 $$\mathbb F_p^2\setminus\{(0,0)\}$$，边 $$(x,y)\sim(a,b)\iff ax+by=1$$。任意两顶点至多一个公共邻点（两条直线至多一个交点），故 $$K_{2,2}$$-free；每点度数 $$p$$ 或 $$p-1$$。

**（c）代数构造·范数图（Alon–Kollár–Rónyai–Szabó）**：若 $$t\ge(s-1)!+1$$，则 $$\mathrm{ex}(n,K_{s,t})=\Theta(n^{2-1/s})$$。构造 $$NormGraph_{p,s}$$：顶点集 $$\mathbb F_{p^s}$$，边 $$\{a,b\}$$ 当 $$N(a+b)=1$$，其中范数 $$N(x)=x^{1+p+\cdots+p^{s-1}}=x^{(p^s-1)/(p-1)}\in\mathbb F_p$$，用代数几何的 Lang–Weil 界证明 $$K_{s,s!+1}$$-free。

**（d）随机代数混合（Bukh, 2015）**：结合随机多项式 $$f$$ 与 Lang–Weil 界，对 $$t>t_0(s)$$ 也得 $$\mathrm{ex}(n,K_{s,t})=\Theta(n^{2-1/s})$$。

**对 $$K_{2,2}$$**：随机下界 $$n^{4/3}\le\mathrm{ex}(n,K_{2,2})\le n^{3/2}$$，上界接近紧。

## 7. 禁止稀疏二分图与偶环

**定理（Füredi；Alon–Krivelevich–Sudakov）**：$$H$$ 二部，其一部分每点度数至多 $$r$$，则 $$\mathrm{ex}(n,H)\le Cn^{2-1/r}$$。工具是**依赖随机选择**引理：边多则存在大子集 $$U$$，其所有小 $$r$$ 元子集都有很多公共邻点，从而可逐点嵌入 $$H$$。

**偶环弱版本**：$$n$$ 顶点图边数至少 $$Cn^{1+1/k}$$ 则含长度至多 $$2k$$ 的偶环。证明先做两个清洗引理（"平均度 → 大最小度子图""随机二染色取半数边"），再沿 BFS 层次 $$A_0,A_1,\dots$$ 递推 $$\lvert A_i\rvert\ge(\delta-1)\lvert A_{i-1}\rvert$$，最终 $$\lvert A_k\rvert>n$$ 矛盾。

还有 $$1$$-细分 clique 的界 $$\mathrm{ex}(n,K_t^{1\text{-sub}})=O(n^{3/2-c_t})$$（Janzer）。

## 8. 超图 Turán（开放前沿）

**问题**：$$n$$ 顶点 3-均匀超图不含四面体（$$K_4^{(3)}$$）时最多多少三元组？Turán 给出边密度 $$5/9$$ 的构造（猜想最优），目前最好上界约 $$0.562$$（旗代数方法）。这是极值超图论最著名的开放问题之一。

## 9. 速查

- Mantel：$$\mathrm{ex}(n,K_3)=\lfloor n^2/4\rfloor$$。
- Turán：$$\mathrm{ex}(n,K_{r+1})=(1-\frac1r)\frac{n^2}{2}+O(n)$$。
- ESS：$$\mathrm{ex}(n,H)=(1-\frac1{\chi(H)-1})\binom n2+o(n^2)$$。
- KST：$$\mathrm{ex}(n,K_{s,t})=O(n^{2-1/s})$$；$$K_{2,2}$$ 下界 $$\Theta(n^{3/2})$$，一般 $$K_{s,t}$$（$$s,t\ge3$$）开放。
- 正则引理（上界机器）见 `regularity-and-graph-limits`。
