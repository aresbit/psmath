# 李代数与根系统 (Lie Algebras & Root Systems)

> **整理自**：Humphreys《Introduction to Lie Algebras and Representation Theory》(GTM 9)、Serre《Complex Semisimple Lie Algebras》、剑桥 Grojnowski 课程讲义（Laugwitz–Seidler 笔记）
> **适用触发词**：李代数、括号、Jacobi、理想、导子、伴随表示、可解、幂零、Engel、Lie 定理、Killing 型、Cartan 判据、半单、单、Casimir、完全可约、sl(2)、Cartan 子代数、根、根空间、根系、Weyl 群、Cartan 矩阵、Dynkin 图、最高权、Verma 模、Weyl 特征标公式

## 0. 一句话定位

给定向量空间配上"既非结合又非交换"的李括号，就得到李代数。三个递进问题：结构（可解/幂零 vs 半单/单）、分类（复数域上半单李代数由根系与 Dynkin 图完全编码）、表示（不可约表示由最高权分类，维数与特征标由 Weyl 公式给出）。心智模型是一条编码链：**李代数结构 → 根系 → Dynkin 图 + 最高权**，不断丢失冗余、保留不变量（Weyl 群、Cartan 矩阵）。

## 1. 基本结构（ch01）

- **李代数**：双线性 $$[\cdot,\cdot]$$ 满足反交换 $$[x,x]=0$$ 与 **Jacobi 恒等式** $$[x,[y,z]]+[y,[z,x]]+[z,[x,y]]=0$$。它是矩阵李群切空间的一阶近似，$$[X,Y]=XY-YX$$ 自动满足 Jacobi。
- **经典例子**：$$\mathfrak{gl}(V)$$、$$\mathfrak{sl}(n,F)=\{\operatorname{tr}=0\}$$、$$\mathfrak{so}(n,F)=\{x+x^t=0\}$$、$$\mathfrak{sp}(2n,F)$$、交换李代数（$$[\cdot,\cdot]=0$$）、三维 Heisenberg 代数（$$[x,y]=z$$，幂零非交换的最小例）。
- **理想** $$I$$：$$[L,I]\subseteq I$$（李代数版的核）；商 $$L/I$$ 带诱导括号。**中心** $$Z(L)=\ker\operatorname{ad}$$。
- **导子**：满足 Leibniz 规则；**伴随映射** $$\operatorname{ad}x(y)=[x,y]$$ 是导子，$$\operatorname{ad}:L\to\mathfrak{gl}(L)$$ 是同态，$$\ker\operatorname{ad}=Z(L)$$。**$$\operatorname{ad}$$ 是整门课的万能探针。**
- **结构常数** $$[x_i,x_j]=\sum_k c_{ij}^k x_k$$ 满足 $$c_{ij}^k=-c_{ji}^k$$ 与一组二次关系。
- **单李代数**：非交换且无非平凡理想。

## 2. 可解与幂零（ch02）

- **导出列** $$L^{(0)}=L,\ L^{(i+1)}=[L^{(i)},L^{(i)}]$$ 归零 $$\Rightarrow$$ **可解**。
- **下中心列** $$L^{0}=L,\ L^{i+1}=[L,L^{i}]$$ 归零 $$\Rightarrow$$ **幂零**。因 $$L^{(i)}\subseteq L^{i}$$，**幂零 $$\Rightarrow$$ 可解**（反之不成立：$$[x,y]=x$$ 的二维李代数可解非幂零）。
- **Engel 定理**：$$L$$ 幂零 $$\iff$$ 每个 $$\operatorname{ad}x$$ 幂零。表示论形式：若每个 $$\rho(x)$$ 幂零，则存在公共非零向量被全体零化（可同时严格上三角化）。
- **Lie 定理**：特征 0 代数闭域上，$$\mathfrak{gl}(V)$$ 的可解子代数有公共特征向量，可同时上三角化。推论：可解李代数中 $$[L,L]$$ 幂零。
- **对照**：Engel 管"幂零 + 幂零作用 → 同时严格上三角"；Lie 管"可解 + 代数闭 → 同时上三角"。共同主题是把结构退化翻译成线性变换的谱退化。

## 3. 半单性、Killing 型与 Cartan 判据（ch03）

- **根** $$\operatorname{Rad}(L)$$：最大可解理想。**半单**：$$\operatorname{Rad}(L)=0$$。单 $$\Rightarrow$$ 半单。
- **结构定理**：半单 $$L=L_1\oplus\cdots\oplus L_t$$（$$L_i$$ 单），分类半单 $$\iff$$ 分类单。
- **Killing 型** $$\kappa(x,y)=\operatorname{tr}(\operatorname{ad}x\operatorname{ad}y)$$：对称、结合不变（$$\kappa([x,y],z)=\kappa(x,[y,z])$$）；$$\operatorname{Rad}L\subseteq\operatorname{Rad}\kappa$$。
- **Cartan 第一判据**：$$L$$ 可解 $$\iff$$ $$\kappa(x,y)=0$$ 对一切 $$x\in L,\ y\in[L,L]$$。
- **Cartan 第二判据**：$$L$$ 半单 $$\iff$$ $$\kappa$$ 非退化。推论：半单时 $$[L,L]=L$$（无非零交换商）。
- **抽象 Jordan 分解**：半单 $$L$$ 中每个 $$x$$ 唯一写成 $$x=x_s+x_n$$（$$\operatorname{ad}x_s$$ 半单、$$\operatorname{ad}x_n$$ 幂零、$$[x_s,x_n]=0$$），且与任意表示下的 Jordan 分解相容。
- **Levi 分解**：任意有限维李代数（特征 0）$$L=\operatorname{Rad}L\rtimes S$$（可解根 + 半单 Levi 因子）。

## 4. 完全可约性与 $$\mathfrak{sl}(2)$$（ch04）

- **Casimir 算子** $$c_\rho=\sum_i\rho(x_i)\rho(y_i)$$（$$\{x_i\},\{y_i\}$$ 关于 $$\kappa$$ 的对偶基）：与 $$\rho(L)$$ 交换，$$\operatorname{tr}c_\rho=\dim L$$，不可约忠实表示上是非零标量。
- **Weyl 完全可约定理**：半单李代数的有限维表示完全可约（与有限群 Maschke、紧群 Peter–Weyl 同源）。
- **$$\mathfrak{sl}(2)$$ 表示**：标准基 $$h,x,y$$ 满足 $$[h,x]=2x,\ [h,y]=-2y,\ [x,y]=h$$。不可约表示由非负整数 $$m$$ 唯一确定记 $$V(m)$$：$$\dim V(m)=m+1$$，权重 $$m,m-2,\dots,-m$$，最高权向量被 $$x$$ 零化。
  - 心智模型：$$h$$ 是测权尺、$$x$$ 升权、$$y$$ 降权；不可约表示是从最高权 $$m$$ 被 $$y$$ 一路打下来的权链。**$$\mathfrak{sl}(2)$$ 是全部半单表示论的原子模型。**

## 5. 根空间分解与根系公理（ch05）

- **Cartan 子代数** $$H$$：交换、$$\operatorname{ad}$$ 半单、自正规化（$$N_L(H)=H$$）；对半单 $$L$$，等于极大环面子代数。$$\dim H=\ell=\operatorname{rank}L$$。
- **根空间** $$L_\alpha=\{x:[h,x]=\alpha(h)x\ \forall h\in H\}$$；非零 $$\alpha$$ 为**根**，全体记 $$\Phi$$。
- **根空间分解** $$L=H\oplus\bigoplus_{\alpha\in\Phi}L_\alpha$$。关键结构事实：
  1. $$[L_\alpha,L_\beta]\subseteq L_{\alpha+\beta}$$；
  2. $$\kappa(L_\alpha,L_\beta)=0$$ 除非 $$\alpha+\beta=0$$；
  3. $$\alpha\in\Phi\Rightarrow-\alpha\in\Phi$$；
  4. 每个 $$L_\alpha$$ **一维**，$$\pm\alpha$$ 是唯一实数倍根；
  5. 每个根 $$\alpha$$ 配 **余根** $$\alpha^\vee=h_\alpha$$（$$\alpha(h_\alpha)=2$$），$$S_\alpha=L_\alpha\oplus L_{-\alpha}\oplus Fh_\alpha\cong\mathfrak{sl}(2)$$——**把 $$\mathfrak{sl}(2)$$ 理论嵌入任意半单李代数的通道**。
- **根系公理**（欧氏空间 $$E=\mathbb{R}\Phi$$）：(R1) 有限、张成、不含 0；(R2) 实数倍只有 $$\pm\alpha$$；(R3) 关于反射 $$\sigma_\alpha(\beta)=\beta-\langle\beta,\alpha\rangle\alpha$$ 封闭；(R4) 整性 $$\langle\beta,\alpha\rangle=\dfrac{2(\beta,\alpha)}{(\alpha,\alpha)}\in\mathbb{Z}$$。
- 由 Cauchy–Schwarz，$$\langle\alpha,\beta\rangle\langle\beta,\alpha\rangle=4\cos^2\theta\in\{0,1,2,3,4\}$$，故夹角只能取 $$90^\circ,60^\circ,120^\circ,45^\circ,135^\circ,30^\circ,150^\circ$$。
- **$$\alpha$$-弦公式**：通过 $$\beta$$ 的弦 $$\beta-q\alpha,\dots,\beta+p\alpha$$ 满足 $$p-q=\langle\beta,\alpha\rangle$$——整性的几何来源，是分类的引擎。

## 6. 单根、Weyl 群、Dynkin 图与分类（ch06）

- **基（单根）** $$\Delta$$：$$E$$ 的基，每个根可唯一写成 $$\sum k_\alpha\alpha$$（系数全非负或全非正）。不同单根 $$(\alpha,\beta)\le0$$。
- **Weyl 群** $$W$$：反射 $$\sigma_\alpha$$ 生成，有限，由单反射生成，在根上传递、在基集合上单传递，是 **Coxeter 群**（$$(s_is_j)^{m_{ij}}=1$$，$$m_{ij}\in\{2,3,4,6\}$$）。**Weyl 房**是被反射超平面切出的连通分量，$$W$$ 单传递作用其上。
- **Cartan 矩阵** $$(\langle\alpha_i,\alpha_j\rangle)$$：对角 2，非对角 $$0,-1,-2,-3$$。
- **Dynkin 图**：每个单根一个顶点，顶点 $$i,j$$ 连 $$4\cos^2\theta_{ij}\in\{0,1,2,3\}$$ 条边，根长不同时箭头指向短根。
- **Killing–Cartan 分类**：不可约根系 / 单李代数的 Dynkin 图恰为
  $$A_n\ (\mathfrak{sl}(n+1)),\ B_n\ (\mathfrak{so}(2n+1)),\ C_n\ (\mathfrak{sp}(2n)),\ D_n\ (\mathfrak{so}(2n)),\ E_6,E_7,E_8,F_4,G_2$$
  （低秩重合：$$B_2=C_2,\ A_3=D_3,\ D_2=A_1\times A_1$$）。分类 = 正定 Cartan 矩阵的有限枚举。
- **Weyl 群例子**：$$A_n$$ 的 $$W\cong S_{n+1}$$（阶 $$(n+1)!$$）；$$B_n=C_n$$ 的 $$W\cong(\mathbb{Z}/2)^n\rtimes S_n$$（阶 $$2^nn!$$）；$$D_n$$ 的 $$W\cong(\mathbb{Z}/2)^{n-1}\rtimes S_n$$；$$G_2$$ 的 $$W=D_6$$（阶 12）。

## 7. 表示论：最高权与 Weyl 特征标公式（ch07）

- **泛包络代数** $$U(L)=T(L)/I$$（$$I$$ 由 $$x\otimes y-y\otimes x-[x,y]$$ 生成），使 $$L$$-模 = $$U(L)$$-模。**PBW 定理**：有序基的单项式 $$x_1^{a_1}\cdots x_n^{a_n}$$ 构成 $$U(L)$$ 的基。
- **权空间** $$V_\lambda=\{v:h\cdot v=\lambda(h)v\}$$；$$V=\bigoplus_\lambda V_\lambda$$；$$L_\alpha\cdot V_\lambda\subseteq V_{\lambda+\alpha}$$。
- **最高权**：存在最高权向量 $$v^+$$ 使 $$x_\alpha\cdot v^+=0$$（$$\alpha\in\Phi^+$$），$$h\cdot v^+=\lambda(h)v^+$$。
- **权格与根格**：$$\Lambda=\{\lambda:\langle\lambda,\alpha^\vee\rangle\in\mathbb{Z}\ \forall\alpha\}$$，$$\Lambda_r=\mathbb{Z}\Phi$$。**支配整权**：$$\langle\lambda,\alpha_i^\vee\rangle\ge0$$ 对所有单根，是基本权 $$\omega_i$$（$$\langle\omega_i,\alpha_j^\vee\rangle=\delta_{ij}$$）的非负整组合。
- **分类定理**：有限维不可约表示 $$\leftrightarrow$$ 支配整权 $$\lambda=\sum a_i\omega_i$$（$$a_i\in\mathbb{Z}_{\ge0}$$），同构 $$\iff$$ 最高权相同。
- **Verma 模** $$M(\lambda)=U(L)\otimes_{U(\mathfrak{b})}\mathbb{C}_\lambda$$（Borel $$\mathfrak{b}=H\oplus\bigoplus_{\alpha>0}L_\alpha$$），唯一不可约商 $$V(\lambda)$$；$$\lambda$$ 支配整 $$\iff$$ $$V(\lambda)$$ 有限维。
- **Weyl 特征标公式**：记 $$\rho=\frac{1}{2}\sum_{\alpha>0}\alpha$$，
  $$\operatorname{ch}V(\lambda)=\dfrac{\sum_{w\in W}(-1)^{\ell(w)}e^{w(\lambda+\rho)}}{\sum_{w\in W}(-1)^{\ell(w)}e^{w\rho}}=\dfrac{\sum_w(-1)^{\ell(w)}e^{w(\lambda+\rho)}}{\prod_{\alpha>0}(e^{\alpha/2}-e^{-\alpha/2})}.$$
  **Weil 分母公式**（$$\lambda=0$$）：$$\sum_w(-1)^{\ell(w)}e^{w\rho}=\prod_{\alpha>0}(e^{\alpha/2}-e^{-\alpha/2})$$。
- **Weyl 维数公式**：$$\dim V(\lambda)=\prod_{\alpha>0}\dfrac{\langle\lambda+\rho,\alpha^\vee\rangle}{\langle\rho,\alpha^\vee\rangle}$$。
  - $$\mathfrak{sl}(2)$$：$$\dim V(m)=m+1$$。
  - $$\mathfrak{sl}(3)$$（权 $$a\omega_1+b\omega_2$$）：$$\dim V=\dfrac{(a+1)(b+1)(a+b+2)}{2}$$。

## 8. 代数大师的解题清单（李代数侧）

1. **先问退化性**：可解/幂零 vs 半单/单——用导出列、下中心列、$$\operatorname{ad}$$ 的谱性质（Engel）判断。
2. **要半单判定就上 Killing 型**：Cartan 第二判据（$$\kappa$$ 非退化）。
3. **半单就分解到单理想**：分类化归为单李代数，即 Dynkin 图分类。
4. **要结构就找 Cartan 子代数 + 根空间分解**：每个根配一个 $$\mathfrak{sl}(2)$$ 子代数，把问题降到 $$\mathfrak{sl}(2)$$ 理论再拼回。
5. **要分类就画 Dynkin 图**：$$A_n,B_n,C_n,D_n,E_6,E_7,E_8,F_4,G_2$$ 是全部指纹。
6. **要表示就用最高权**：不可约表示 $$\leftrightarrow$$ 支配整权；维数用 Weyl 维数公式，特征标用 Weyl 特征标公式。
