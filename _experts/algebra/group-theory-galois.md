# 群论与 Galois 理论 (Group Theory & Galois Theory)

> **整理自**：Dummit & Foote《Abstract Algebra》(3rd ed.)、Artin《Algebra》、J. S. Milne《Fields and Galois Theory》
> **适用触发词**：群、子群、正规子群、商群、同态、Lagrange、Sylow、p-群、共轭类、群作用、轨道、稳定子、可解、合成列、Jordan–Hölder、Galois、域扩张、分裂域、分圆、尺规作图、五次方程、根式可解

## 0. 一句话定位

群论把「对称」抽象成代数对象，再用子群、商群、作用和表示去分类它。Galois 理论则把「方程能否用根式求解」翻译成「某个有限群是否可解」，从而一举证明一般五次方程不可根式求解。

## 1. 群、子群、商（ch01）

- **群**：集合 $$G$$ 带二元运算 $$\cdot$$，满足结合律、单位元 $$e$$、逆元。
- **阶**：$$|G|$$；元素 $$a$$ 的阶是使 $$a^n=e$$ 的最小正整数。
- **循环群**：$$\langle a\rangle$$；无限时 $$\cong\mathbb{Z}$$，$$n$$ 阶时 $$\cong\mathbb{Z}/n\mathbb{Z}$$；$$n$$ 阶循环群有 $$\varphi(n)$$ 个生成元。
- **子群判定**：$$H\ne\varnothing$$ 且 $$a,b\in H\Rightarrow ab^{-1}\in H$$。
- **陪集与 Lagrange 定理**：$$|G|=|H|\cdot[G:H]$$。推论：子群阶整除群阶；素数阶群必循环。
- **正规子群** $$N\trianglelefteq G$$：$$gNg^{-1}=N$$ 对一切 $$g$$；等价刻画是「$$N$$ 是某同态的核」。商群 $$G/N$$ 阶为 $$[G:N]$$。
- **同构定理**：
  - 第一：$$G/\ker\varphi\cong\operatorname{im}\varphi$$（像 = 商掉核）。
  - 第二（钻石）：$$\dfrac{H}{H\cap N}\cong\dfrac{HN}{N}$$。
  - 第三：$$\dfrac{G/N}{H/N}\cong\dfrac{G}{H}$$。
  - 对应定理：含 $$N$$ 的子群与 $$G/N$$ 的子群保序一一对应，正规性对应。
- **构造**：直积 $$G\times H$$；半直积 $$N\rtimes H$$（由同态 $$H\to\operatorname{Aut}(N)$$ 决定），如 $$D_{2n}=\mathbb{Z}/n\rtimes\mathbb{Z}/2$$。

## 2. 群作用与计数（ch02）

- **作用**等价于同态 $$\rho:G\to\operatorname{Sym}(X)$$。
- **轨道-稳定子定理**：$$|G\cdot x|=[G:G_x]$$，故 $$|G|=|G\cdot x|\cdot|G_x|$$。推论（Cayley）：$$G\hookrightarrow\operatorname{Sym}(G)$$。
- **共轭作用**：轨道 = 共轭类，稳定子 = 中心化子 $$C_G(x)$$，不动点集 = 中心 $$Z(G)$$。
- **类方程**：$$|G|=|Z(G)|+\sum_i[G:C_G(x_i)]$$，求和跑遍非中心共轭类代表。
- **$$p$$-群中心非平凡**：$$|G|=p^a\Rightarrow Z(G)\ne\{1\}$$（类方程两边都是 $$p$$ 的倍数）。进一步：$$p^2$$ 阶群必交换；$$p$$-群必有指定阶 $$p^k$$ 的正规子群。
- **陪集作用**：$$G$$ 作用在 $$G/H$$ 上，核为 $$\bigcap_g gHg^{-1}$$（$$H$$ 的 core，最大含于 $$H$$ 的正规子群）。若 $$[G:H]=n$$，得同态 $$G\to S_n$$，核含于 $$H$$——"指标小必有非平凡正规子群"的判定族。
- **Burnside 引理**：轨道数 $$=\dfrac{1}{|G|}\sum_g|\operatorname{Fix}(g)|$$。

## 3. Sylow 定理：有限群的局部解剖刀（ch03）

设 $$|G|=p^a m$$，$$p\nmid m$$。阶为 $$p^a$$ 的子群称 **Sylow $$p$$-子群**，记个数 $$n_p$$。

- **Sylow I（存在）**：对每个 $$0\le k\le a$$，存在阶 $$p^k$$ 的子群；每个 $$p$$-子群含于某个 Sylow $$p$$-子群。
- **Sylow II（共轭）**：任意两个 Sylow $$p$$-子群共轭。
- **Sylow III（个数）**：$$n_p\equiv 1\pmod p$$ 且 $$n_p\mid m$$；$$n_p=[G:N_G(P)]$$。
- **推论**：Cauchy 定理（$$p\mid|G|\Rightarrow$$ 有 $$p$$ 阶元）；$$n_p=1\iff$$ Sylow $$p$$-子群正规；Frattini 论证：$$H\trianglelefteq G,\ P\in\operatorname{Syl}_p(H)\Rightarrow G=HN_G(P)$$。

**用法**：$$p^2$$ 阶群 $$\cong\mathbb{Z}/p^2$$ 或 $$\mathbb{Z}/p\times\mathbb{Z}/p$$；$$pq$$ 阶（$$p<q$$）群若 $$q\not\equiv1\pmod p$$ 则循环，否则另有 $$\mathbb{Z}/q\rtimes\mathbb{Z}/p$$。单性判定两把主刀：$$n_p$$ 的算术约束 + 陪集作用嵌入 $$S_n$$ 比较阶。

## 4. 可解群与合成列（ch04）

- **换位子** $$[x,y]=x^{-1}y^{-1}xy$$；**导子群** $$G'=[G,G]\trianglelefteq G$$，且 $$G/G'$$ 是最大交换商。
- **导列**：$$G^{(0)}=G,\ G^{(i+1)}=[G^{(i)},G^{(i)}]$$。$$G$$ **可解** $$\iff$$ 存在 $$n$$ 使 $$G^{(n)}=\{1\}$$ $$\iff$$ 存在交换商的次正规列 $$\iff$$ 合成因子全为 $$\mathbb{Z}/p$$。
- **合成列**：不可加细的次正规列，因子为单群。**Jordan–Hölder**：任意两条合成列的因子多重集同构相同——把群分类约化为单群分类。
- **封闭性**：可解群的子群、商群、可解扩张可解；$$p$$-群、二面体群可解；Burnside 定理：$$p^a q^b$$ 阶群可解。
- **$$S_n$$ 可解 $$\iff n\le4$$**：$$n\ge5$$ 时 $$A_n$$ 单且非交换，是转折点。
- **幂零群**：下中心列 $$\gamma_1=G,\ \gamma_{i+1}=[\gamma_i,G]$$ 有限步归零。幂零 $$\Rightarrow$$ 可解；有限 $$p$$-群幂零；有限群幂零 $$\iff$$ 其 Sylow 子群的直积。

## 5. 域扩张（ch05）

- **次数与塔定理**：$$[K:F]=\dim_F K$$，$$[L:F]=[L:K][K:F]$$。
- **极小多项式**：$$F(x)\cong F[t]/(m_x)$$，$$[F(x):F]=\deg m_x$$。有限 $$\Rightarrow$$ 代数。
- **分裂域**：$$f$$ 的最小完全分解扩张；存在且 $$F$$-同构唯一；$$[K:F]\le(\deg f)!$$。
- **可分** = 无重根（特征 0 自动）；**正规** = 一个根在则全分裂；**Galois 扩张** = 可分 + 正规。
- **有限域**：每个 $$q=p^n$$ 存在唯一 $$\mathbb{F}_q$$，是 $$t^{p^n}-t$$ 的分裂域；$$\mathbb{F}_q^\times$$ 循环；$$\mathbb{F}_{p^m}\subseteq\mathbb{F}_{p^n}\iff m\mid n$$；Frobenius $$\sigma:x\mapsto x^p$$ 生成 $$\operatorname{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p)\cong\mathbb{Z}/n$$。
- **本原元定理**：有限可分扩张是单扩张。

## 6. Galois 基本定理（ch06）

- $$\operatorname{Gal}(K/F)=\{\sigma\in\operatorname{Aut}(K):\sigma|_F=\operatorname{id}\}$$；固定域 $$K^H=\{a:\sigma(a)=a\ \forall\sigma\in H\}$$。
- **Galois 扩张等价刻画**（有限 $$K/F$$）：可分 + 正规 $$\iff$$ 可分多项式分裂域 $$\iff$$ $$|\operatorname{Gal}(K/F)|=[K:F]$$（最常用判定）$$\iff$$ $$F=K^{\operatorname{Gal}(K/F)}$$。
- **基本定理**：中间域 $$E$$ 与子群 $$H\le G$$ 之间**序反双射**：
  1. $$E_1\subseteq E_2\iff\operatorname{Gal}(K/E_1)\supseteq\operatorname{Gal}(K/E_2)$$；
  2. $$[K:E]=|\operatorname{Gal}(K/E)|$$，$$[E:F]=[G:\operatorname{Gal}(K/E)]$$；
  3. 共轭对应 $$\sigma(E)\leftrightarrow\sigma\operatorname{Gal}(K/E)\sigma^{-1}$$；
  4. $$E/F$$ 是 Galois $$\iff$$ $$\operatorname{Gal}(K/E)\trianglelefteq G$$，此时 $$\operatorname{Gal}(E/F)\cong G/\operatorname{Gal}(K/E)$$。
- **判别式** $$\Delta=\prod_{i<j}(\alpha_i-\alpha_j)^2\in F$$；$$G\subseteq A_n\iff\sqrt{\Delta}\in F\iff\Delta$$ 是平方。**根的传递作用**：$$G\hookrightarrow S_n$$ 传递，$$\deg f\mid|G|$$。

## 7. 应用（ch07–ch08）

- **Galois 群计算流程**：找分裂域 → 传递子群 $$\le S_n$$ → 判别式判 $$A_n$$ vs $$S_n$$ → 根的代数关系 → Sylow 计数 + 中间域对应。
  - $$t^3-2$$：分裂域 $$\mathbb{Q}(\sqrt[3]{2},\omega)$$，次数 6，$$\Delta=-108$$ 非平方 $$\Rightarrow G=S_3$$。
  - $$t^3-3t+1$$：$$\Delta=81$$ 平方 $$\Rightarrow G\cong\mathbb{Z}/3$$。
- **尺规作图**：$$\alpha$$ 可作 $$\iff$$ 存在 2-幂次扩张塔。倍立方（$$\sqrt[3]{2}$$，次数 3）不可；三等分任意角不可；化圆为方（$$\pi$$ 超越）不可。正 $$n$$ 边形可作 $$\iff$$ $$n=2^k\cdot$$互异 Fermat 素数（$$17=2^{2^2}+1$$ 可作，7 不可）。
- **分圆域**：$$\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})\cong(\mathbb{Z}/n\mathbb{Z})^\times$$，由 $$\sigma_a:\zeta_n\mapsto\zeta_n^a$$（$$\gcd(a,n)=1$$）给出；$$\deg\Phi_n=\varphi(n)$$。
- **根式可解性（ch08）**：根式可解 $$\iff$$ 存在根式域塔；含足够单位根时根式扩张 $$\leftrightarrow$$ 循环 Galois 群。
  - **Galois 定理**：$$f$$（特征 0）根式可解 $$\iff\operatorname{Gal}(f)$$ 可解。
  - 一般 $$n$$ 次多项式（系数为根的对称函数）的 Galois 群 $$=S_n$$。
  - **Abel–Ruffini**：$$n\ge5$$ 一般 $$n$$ 次方程不可根式求解（$$A_n$$（$$n\ge5$$）单非交换 $$\Rightarrow S_n$$ 不可解）。
  - 具体例：$$t^5-6t+3$$ 不可约 + 恰 3 实 2 复根 $$\Rightarrow$$ 含对换 + 5-循环 $$\Rightarrow G=S_5$$，不可解。判据：不可约 + 恰 2 个复根 + 素数次 $$\Rightarrow G=S_n$$。
  - 逆 Galois 问题：哪些有限群可实现为 $$\mathbb{Q}$$ 上多项式的 Galois 群。

## 8. 代数大师的解题清单（群论侧）

1. **先数**：用 Lagrange / 类方程 / 轨道-稳定子把 $$|G|$$ 的因子关系钉死。
2. **再切**：对每个素因子用 Sylow III 枚举 $$n_p$$，凡 $$n_p=1$$ 就是正规子群（非单）。
3. **单性**：$$n_p$$ 全 $$\ne1$$ 时，用陪集作用 $$G\to S_n$$ 比较阶，或数元素个数逼矛盾（$$A_5$$ 模式）。
4. **定结构**：正规 Sylow 子群 + 半直积/直积分解，或用合成列 + Jordan–Hölder 定位单因子。
5. **Galois 侧**：先算扩张次数，再算 Galois 群大小；$$\deg f\mid|G|$$ 与判别式是两道最快的筛子。
