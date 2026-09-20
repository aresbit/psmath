# 同调代数 (Homological Algebra)

> **整理自**：Charles A. Weibel《An Introduction to Homological Algebra》(Cambridge Studies in Advanced Mathematics 38)、Catherine Meusburger《Homological Algebra》(FAU Erlangen-Nürnberg)、Eloisa Grifo《Homological Algebra》、Birgit Richter《An Introduction to Homological Algebra》、Saunders Mac Lane《Homology》、Joseph J. Rotman《An Introduction to Homological Algebra》
> **适用触发词**：同调、上同调、链复形、正合列、蛇引理、长正合列、链同伦、投射模、内射模、平坦模、消解、导出函子、Tor、Ext、扩张、谱序列、滤过、双复形、Grothendieck 谱序列、群上同调、bar 消解、Schur 乘子、同调维数、全局维数、Hilbert 合冲、Koszul

## 0. 一句话定位

同调代数是**用链复形这把尺子度量数学对象"离正合有多远"的理论**。正合性是理想状态，破坏正合性的现象被编码成链复形及其同调群。左正合函子（Hom）与右正合函子（张量积）的缺陷被**导出函子**（$$\operatorname{Ext}$$、$$\operatorname{Tor}$$）逐层量化；谱序列逐页逼近同调；群上同调是经典落地。

## 1. 链复形与同调（ch01）

- **正合**：$$\operatorname{im}f=\ker g$$。**短正合列** $$0\to A\to B\to C\to 0$$：$$A\hookrightarrow B\twoheadrightarrow C$$ 且 $$C\cong B/A$$。
- **链复形** $$C_\bullet$$：$$d_n:C_n\to C_{n-1}$$ 满足 $$d_{n-1}d_n=0$$。
- **同调**：循环 $$Z_n=\ker d_n$$，边缘 $$B_n=\operatorname{im}d_{n+1}$$，$$H_n=Z_n/B_n=\ker d_n/\operatorname{im}d_{n+1}$$。**$$H_n$$ 度量复形在位置 $$n$$ 离正合有多远**：正合 $$\iff H_n=0$$；非零 = 存在"循环但不是边缘"的元素（拓扑里"洞"的代数化身）。
- **链映射** $$f_{n-1}d_n^C=d_n^Df_n$$ 诱导 $$H_n(f)$$，使 $$H_n$$ 成为函子。
- **链同伦** $$f_n-g_n=d_{n+1}^Dh_n+h_{n-1}d_n^C$$；同伦 $$\Rightarrow$$ 同调上相等（$$H_n(f)=H_n(g)$$）。
- **长正合同调列**：短正合列 $$0\to A_\bullet\to B_\bullet\to C_\bullet\to 0$$ 诱导
  $$\cdots\to H_{n+1}(C)\xrightarrow{\partial}H_n(A)\to H_n(B)\to H_n(C)\xrightarrow{\partial}H_{n-1}(A)\to\cdots$$
  连接同态 $$\partial$$ 由追图构造。这是同调代数**最核心的机器**。
- **蛇引理**：行正合的交换图给出 $$\ker f\to\ker g\to\ker h\xrightarrow{\delta}\operatorname{coker}f\to\operatorname{coker}g\to\operatorname{coker}h$$。长正合列是蛇引理逐次应用的结果。

## 2. 投射模、内射模与消解（ch02）

- **投射模** $$P$$：$$\operatorname{Hom}(P,-)$$ 正合，等价于"任意满射可提升"，等价于 $$P$$ 是自由模的直和加项。
- **内射模** $$I$$：$$\operatorname{Hom}(-,I)$$ 正合，等价于"任意单射可扩张"。**Baer 判据**：只需对 $$R$$ 的理想验证。
- 交换群内射 $$\iff$$ **可除**；$$\mathbb{Q}$$、$$\mathbb{Q}/\mathbb{Z}$$ 是内射 $$\mathbb{Z}$$-模（$$\mathbb{Q}/\mathbb{Z}$$ 是内射余生成子）。
- **平坦模**：$$-\otimes N$$ 正合。投射 $$\Rightarrow$$ 平坦（反之不成立，如 $$\mathbb{Q}$$ 作为 $$\mathbb{Z}$$-模平坦但不投射）。平坦 $$\iff\operatorname{Tor}_1=0$$。
- **消解**：投射消解 $$\cdots\to P_1\to P_0\to M\to 0$$；内射消解 $$0\to M\to I^0\to I^1\to\cdots$$。模范畴有足够多投射与内射。
- **比较引理**：投射消解间的提升存在且唯一到链同伦。推论：**消解链同伦等价唯一**——导出函子良定义的根基。
- 标准消解：$$\mathbb{Z}/m$$ 的投射消解长度 1（$$\operatorname{pd}=1$$）；自由模长度 0；群代数的 **bar 消解**；多项式环的 **Koszul 复形**（长度 $$n$$）。

## 3. 导出函子（ch03）

- **左正合/右正合**：协变 $$\operatorname{Hom}(M,-)$$ 左正合，反变 $$\operatorname{Hom}(-,N)$$ 左正合；张量积 $$M\otimes-$$ 右正合。
  - 缺陷示例：$$0\to\mathbb{Z}\xrightarrow{\cdot2}\mathbb{Z}\to\mathbb{Z}/2\to0$$ 作用 $$\operatorname{Hom}(-,\mathbb{Z}/2)$$ 后丢满射端，作用 $$-\otimes\mathbb{Z}/2$$ 后丢单射端。
- **左导出函子** $$L_iF(M)=H_i(FP_\bullet)$$（$$F$$ 右正合，用投射消解）。**右导出函子** $$R^iG(N)=H^i(GI^\bullet)$$（$$G$$ 左正合，用内射消解）。
- **锚点**：$$L_0F\cong F$$，$$R^0G\cong G$$；好对象上消没 $$L_iF(P)=0$$（$$i>0$$，$$P$$ 投射），$$R^iG(I)=0$$（$$I$$ 内射）。
- **导出函子长正合列**：右正合 $$F$$ 给 $$\cdots\to L_1F(C)\to F(A)\to F(B)\to F(C)\to0$$；左正合 $$G$$ 给 $$0\to G(A)\to G(B)\to G(C)\to R^1G(A)\to\cdots$$。
- **$$\delta$$-函子与万有性**：导出函子是万有 $$\delta$$-函子；若 $$T^0\cong G$$ 且在足够多内射对象上消没，则 $$T^i\cong R^iG$$（最常用的验证判据）。

## 4. Tor 与 Ext（ch04）

- **定义**：$$\operatorname{Tor}_n^R(M,N)=(L_n(M\otimes-))(N)$$；$$\operatorname{Ext}_R^n(M,N)=(R^n\operatorname{Hom}(M,-))(N)$$。零阶项：$$\operatorname{Tor}_0\cong M\otimes N$$，$$\operatorname{Ext}^0\cong\operatorname{Hom}(M,N)$$。
- **平衡性**：用哪个变量消解都得到同一族函子（$$\operatorname{Tor}_n\cong H_n(P_\bullet\otimes N)\cong H_n(M\otimes Q_\bullet)$$）——可挑好算的变量。
- **长正合列**：Tor 与 Ext 各自给出两条长正合列（协变/反变 Hom 的缺口补在不同端）。
- **计算**：
  - $$P$$ 投射 $$\Rightarrow\operatorname{Ext}^n(P,N)=0$$；$$I$$ 内射 $$\Rightarrow\operatorname{Ext}^n(M,I)=0$$；$$P$$ 投射或 $$N$$ 平坦 $$\Rightarrow\operatorname{Tor}_n(P,N)=0$$。
  - **PID 上**：$$\operatorname{Ext}^n=\operatorname{Tor}_n=0$$（$$n\ge2$$）；$$\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/m,\mathbb{Z}/n)=\operatorname{Ext}_{\mathbb{Z}}^1(\mathbb{Z}/m,\mathbb{Z}/n)=\mathbb{Z}/\gcd(m,n)$$。
- **$$\operatorname{Ext}^1$$ 与扩张**：$$0\to N\to X\to M\to 0$$ 的等价类 $$\leftrightarrow\operatorname{Ext}_R^1(M,N)$$，零元对应分裂扩张 $$N\oplus M$$，加法由 **Baer 和**给出。例：$$\operatorname{Ext}^1_{\mathbb{Z}}(\mathbb{Z}/2,\mathbb{Z}/2)=\mathbb{Z}/2$$（分裂 $$\mathbb{Z}/2\oplus\mathbb{Z}/2$$ 与非分裂 $$\mathbb{Z}/4$$）。
- **Yoneda Ext**：$$\operatorname{Ext}_R^n(M,N)$$ 描述长度 $$n$$ 的扩张按 Yoneda 等价分类——"元素即长正合列"。

## 5. 谱序列（ch05）

- **定义**：双分次模 $$E_r^{p,q}$$ 带微分 $$d_r:E_r^{p,q}\to E_r^{p+r,q-r+1}$$（双次数 $$(r,1-r)$$，$$d_rd_r=0$$），$$E_{r+1}^{p,q}\cong H(E_r^{p,q})$$。**第 $$r+1$$ 页是第 $$r$$ 页的同调**——唯一必须记的公式。
- **收敛**：$$r$$ 充分大时微分进出为零，$$E_r^{p,q}$$ 稳定为 $$E_\infty^{p,q}$$，写作 $$E_r^{p,q}\Rightarrow H^{p+q}$$，意思是 $$E_\infty^{p,q}\cong F^pH^{p+q}/F^{p+1}H^{p+q}$$（即 $$E_\infty$$ 是目标同调关于滤过的相伴分次）。
- **滤过复形**：$$E^1_{p,q}=H_{p+q}(F_pC/F_{p-1}C)\Rightarrow H_{p+q}(C)$$（有界滤过）。**边缘同态**常给出单射/满射/短正合列。
- **双复形**：带 $$d^h,d^v$$ 满足 $$d^hd^h=d^vd^v=0$$ 与反对易 $$d^hd^v+d^vd^h=0$$；**全复形** $$\operatorname{Tot}(C)_n=\bigoplus_{p+q=n}C_{p,q}$$，$$d=d^h+d^v$$（反对易恰保证 $$d^2=0$$）。
- **两个谱序列夹击**：$$E^I$$（先垂直后水平）与 $$E^{II}$$（先水平后垂直）都收敛到 $$H_*(\operatorname{Tot}C)$$：
  $$E^2_{p,q}=H_p(H_q(C))\Rightarrow H_{p+q}(\operatorname{Tot}C),\qquad E^2_{p,q}=H_q(H_p(C))\Rightarrow H_{p+q}(\operatorname{Tot}C).$$
- **应用**：
  - **Grothendieck 谱序列**：$$E_2^{p,q}=R^pG(R^qF(X))\Rightarrow R^{p+q}(G\circ F)(X)$$（把复合函子的导出拆成两层，是所有具体谱序列的母版）。
  - **Lyndon–Hochschild–Serre**：$$E_2^{p,q}=H^p(G/N,H^q(N,M))\Rightarrow H^{p+q}(G,M)$$。
  - **Künneth 谱序列**：$$E^2_{p,q}=\bigoplus_{s+t=q}\operatorname{Tor}_p^R(H_s(A),H_t(B))\Rightarrow H_{p+q}(A\otimes B)$$（$$R$$ 为域时退化为经典 Künneth 公式）。

## 6. 群同调与上同调（ch06）

- **群代数** $$k[G]$$；左 $$k[G]$$-模 ↔ $$G$$ 的 $$k$$-线性表示。增广映射 $$\varepsilon:k[G]\to k$$，核为增广理想 $$IG$$；平凡模 $$k$$ 是基本系数模。
- **定义**：$$H_n(G,M)=\operatorname{Tor}_n^{k[G]}(k,M)$$，$$H^n(G,M)=\operatorname{Ext}^n_{k[G]}(k,M)$$。等价地 $$H^n=R^n(-)^G$$（不变量函子的右导出），$$H_n=L_n(-)_G$$（余不变量函子的左导出）。
- **bar 消解**：$$B_n=k[G^{n+1}]$$ 自由，$$d_n(g_0,\dots,g_n)=\sum_i(-1)^i(g_0,\dots,\widehat{g_i},\dots,g_n)$$——把抽象导出函子翻译成显式（上）链复形，可直接手算。
- **低维解释**：
  - $$H^0(G,M)=M^G$$（不变量），$$H_0(G,M)=M_G$$（余不变量）。
  - $$H^1(G,M)=\operatorname{Der}(G,M)/\operatorname{InnDer}(G,M)=\operatorname{Hom}(G^{\mathrm{ab}},M)$$（平凡模）。
  - $$H_1(G,\mathbb{Z})=G^{\mathrm{ab}}$$；$$H_2(G,\mathbb{Z})$$ = **Schur 乘子**（中心扩张的万有障碍）。
  - $$H^2(G,M)$$ 分类中心扩张 $$0\to M\to E\to G\to 0$$（零元对应分裂）；$$H^2=0$$ 时所有扩张分裂。
- **LHS 五步正合序列**：$$0\to H^1(G/N,M^N)\to H^1(G,M)\to H^1(N,M)^{G/N}\to H^2(G/N,M^N)\to H^2(G,M)$$——计算群上同调最常用的工具。

## 7. 同调维数（ch07）

- **投射维数** $$\operatorname{pd}(M)$$ = 最短投射消解长度；**内射维数** $$\operatorname{id}(M)$$；**平坦维数** $$\operatorname{fd}(M)$$。
- **消没判定**：$$\operatorname{pd}(M)\le n\iff\operatorname{Ext}^{n+1}(M,-)=0$$；$$\operatorname{id}(M)\le n\iff\operatorname{Ext}^{n+1}(-,M)=0$$；$$\operatorname{fd}(M)\le n\iff\operatorname{Tor}_{n+1}(M,-)=0$$。且 $$\operatorname{fd}\le\operatorname{pd}$$（有限表现时等号）。
- **全局维数**：$$\operatorname{gl.dim}(R)=\sup\{\operatorname{pd}(M)\}=\sup\{\operatorname{pd}(R/\mathfrak{a})\}=\sup\{n:\operatorname{Ext}^n\ne0\}$$。Noether 环上左右相等。
- **Schanuel 引理**：$$0\to K\to P\to M\to0$$ 与 $$0\to K'\to P'\to M\to0$$（$$P,P'$$ 投射）$$\Rightarrow K\oplus P'\cong K'\oplus P$$。
- **零维环 = 半单环**：$$\operatorname{gl.dim}(R)=0\iff$$ 每个模投射 $$\iff$$ $$R$$ 半单（Artin–Wedderburn）。
- **经典例子**：域/半单环维数 0；PID（$$\mathbb{Z}$$、$$k[x]$$）与 Dedekind 域维数 1；$$k[x_1,\dots,x_n]$$ 维数 $$n$$；维数 $$d$$ 的局部正则环维数 $$d$$（Auslander–Buchsbaum）。
- **Hilbert 合冲定理**：$$R=k[x_1,\dots,x_n]$$ 上每个有限生成模 $$\operatorname{pd}(M)\le n$$（Koszul 复形 + Tor 消没）。推论 $$\operatorname{gl.dim}(k[x_1,\dots,x_n])=n$$；对域上有限生成环 $$\operatorname{gl.dim}(R)=\operatorname{pd}_R(k)$$。

## 8. 代数大师的解题清单（同调侧）

1. **先问"什么算循环、什么算边缘"**：任何同调理论都先明确这两者，$$H=Z/B$$ 就是"离正合的距离"。
2. **难算的量塞进短正合列**：用长正合列把未知量与已知量通过连接同态串起来。
3. **要算导出函子就选短的消解**：平衡性让你挑好算的变量；投射/内射/平坦对象上高阶消没。
4. **$$\operatorname{Ext}^1$$ = 扩张分类**：把抽象的导出函子翻译成短正合列 + Baer 和；$$\operatorname{Ext}^n$$ 是长度 $$n$$ 的长扩张。
5. **要复杂同调就上谱序列**：$$E_2$$ 通常好算（两个已知同调的复合），配合收敛与边缘同态给出结论；双复形用两个谱序列夹击同一目标。
6. **维数是"离自由有多远"的量化**：用 $$\operatorname{Ext}/\operatorname{Tor}$$ 的消没等价语言计算 $$\operatorname{pd}/\operatorname{gl.dim}$$。
