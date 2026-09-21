---
layout: default
---

# 第40章: 尾声：从 Galois 到现代数学 (Epilogue: From Galois to Modern Mathematics)

> 对应原专栏: 补（原专栏 MP149 结束于 Galois 群；本章是本书收束章）
> 专家依据: `_experts/algebra/algebraic-geometry-topology-k.md` + `_experts/algebra/category-universal-properties.md` + `_experts/numbertheory/analytic-number-theory.md`
> 知识库依据: `opc2/knowledge/math/代数数论/`、`opc2/knowledge/math/解析数论/`（23 篇）、`opc2/knowledge/math/K理论/`（14 篇）、`opc2/knowledge/math/代数几何/`
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

本章不引入新领地。前 39 章每一章攻一座山；这一章站在山顶，把那 39 章画成一张图。

具体做三件事。**第一**，指出全书里反复出现、却被分在六卷里的四条主线——对偶与反变、$$D^2=0$$ 的两副面孔、谱与表示、几何—物理—代数的三角，并逐条列出每条主线经过哪几章。**第二**，把这四条主线背后的四条**共同定理**写出来并证明：它们才是 39 章里那些"巧合"的真正原因（第 3 节）。**第三**，指出现代数学的四个入口，每个三五句话，点到即止（第 7 节）。

**从哪来**：第 39 章的 Galois 对应是全书的最后一块拼图，也是最古老的一块——Galois 在 1832 年写下它时 20 岁，遗稿里留下的是**群与域的对应**，也就是本章定义 3.4 与定理 3.4 的最初形态。
**到哪去**：本书没有第 41 章。这一章的第 7 节是一封给读者的信。

## 二、入口：一道具体的问题 (Entry Problem)

**入口题（自编；本章的性质是"回望"，不是"攻坚"）**

下面的六个箭头来自六章，它们都是同一个构造的化身。请对每一个回答：把谁映到谁？

(a) 第 03 章：有限维 $$k$$-向量空间 $$V\mapsto V^*=\operatorname{Hom}_k(V,k)$$；
(b) 第 15 章：Hilbert 空间 $$H\mapsto H^*$$（Riesz 表示）；
(c) 第 20 章：交换 $$\mathrm{C}^*$$ 代数 $$A\mapsto\widehat A=\operatorname{Hom}_{\text{alg}}(A,\mathbb C)$$（Gelfand 谱）；
(d) 第 31 章：范畴 $$\mathcal C\mapsto\mathcal C^{\mathrm{op}}$$；
(e) 第 36 章：交换环 $$A\mapsto\operatorname{Spec} A$$（素理想集，带 Zariski 拓扑）；
(f) 第 37 章：开覆盖 $$\mathfrak U\mapsto\check H^\bullet(\mathfrak U;\mathbb Z)$$。

**(i)** 六个箭头里，哪些在"自然"意义下是同构，哪些只是配对（有配对但不一一对应）？

**(ii)** (a) 里要写出 $$V\cong V^*$$ 必须选一组基；(b) 里写出 $$H\cong H^*$$ 不必选基（Riesz 直接给 $$x\mapsto\langle x,-\rangle$$）。这个差别是"选基的偶然"，还是本质的？

**(iii)** 验证 (e) 的反变性。设 $$\varphi:A\to B$$ 是交换环同态，$$\mathfrak p\subseteq A$$ 是素理想。先证明 $$\varphi^{-1}(\mathfrak p)$$ 是 $$B$$ 的素理想，因而
$$\operatorname{Spec}\varphi:\operatorname{Spec} B\to\operatorname{Spec} A,\qquad \mathfrak p\mapsto\varphi^{-1}(\mathfrak p)$$
有意义；再说明为什么这个箭头**必须**反向，而不能改成同向。

**(iv)** 用一句话说出这六个箭头共有的名字。

**题面为什么这样设计。** 这一题不要求新工具，它要求"回想"。四个问各自的落点：

- **(i)(iv)** 对应第 3 节的定义 3.1 与定理 3.1：六个箭头的共同名字是**反变函子 (contravariant functor)**；"是同构还是配对"取决于它有没有逆——这正是第 31 章 Yoneda 的立场：一个对象由它与所有对象的关系决定。
- **(ii)** 对应定义 3.1 与定理 3.1：$$V\cong V^*$$ 依赖选基（不自然），而 $$V\mapsto V^{**}$$ 才是自然的；$$\mathcal C^{\mathrm{op}}$$ 是一个货真价实的范畴，不是"$$V$$ 的翻版"。
- **(iii)** 对应第 3.4 节的 Galois 连接：环同态掉头成谱的连续映射，与"扩域掉头成群"是同一台机器的两个输出。

(iii) 的最后一句现在还答不出——它正是定理 3.1（对偶原理）要说的事。

## 三、结构：定义与完整推导 (Structure & Proof)

这一节不造新对象。它要证明四条**共同定理**——39 章里那些"又见面了"的现象，都是它们的特例。

### 3.1 对偶与反变

**定义 3.1（对偶范畴, dual category）** 设 $$\mathcal C$$ 是一个范畴。**对偶范畴** $$\mathcal C^{\mathrm{op}}$$ 定义如下：

- 对象类相同：$$\operatorname{Ob}(\mathcal C^{\mathrm{op}})=\operatorname{Ob}(\mathcal C)$$；
- 对任意对象 $$X,Y$$，态射集**掉头**：$$\operatorname{Hom}_{\mathcal C^{\mathrm{op}}}(X,Y)=\operatorname{Hom}_{\mathcal C}(Y,X)$$；
- 若 $$f\in\operatorname{Hom}_{\mathcal C^{\mathrm{op}}}(X,Y)$$（即 $$\mathcal C$$ 中的 $$f:Y\to X$$）与 $$g\in\operatorname{Hom}_{\mathcal C^{\mathrm{op}}}(Y,Z)$$（即 $$\mathcal C$$ 中的 $$g:Z\to Y$$），定义
$$g\circ^{\mathrm{op}}f=f\circ g\in\operatorname{Hom}_{\mathcal C}(Z,X)=\operatorname{Hom}_{\mathcal C^{\mathrm{op}}}(X,Z);$$
- 恒等态射 $$1_X$$ 保持不变。

**定理 3.1（对偶原理, duality principle）** 设 $$S$$ 是关于范畴的、由"对象、态射、复合、恒等、交换图"写成的陈述。把 $$S$$ 中每个箭头的方向掉头，得**对偶陈述** $$S^{\mathrm{op}}$$。则 $$S$$ 对一切范畴成立，当且仅当 $$S^{\mathrm{op}}$$ 对一切范畴成立。更精确地，对每个范畴 $$\mathcal C$$：
$$S\ \text{在}\ \mathcal C\ \text{中成立}\iff S^{\mathrm{op}}\ \text{在}\ \mathcal C^{\mathrm{op}}\ \text{中成立}.$$

**证明思路**：定义 3.1 的每一条都只是把 $$\mathcal C$$ 的公理"重读"一遍，所以 $$\mathcal C$$ 的公理在 $$\mathcal C^{\mathrm{op}}$$ 里逐字仍是公理。于是把 $$S$$ 的证明逐步掉头，就得到 $$S^{\mathrm{op}}$$ 在 $$\mathcal C^{\mathrm{op}}$$ 中的证明。

**证明**：分两步。

*第一步：范畴公理自对偶。* 范畴公理是三条：(A1) 复合结合；(A2) 恒等是双边单位；(A3) 态射集按端点分块、复合类型相容。逐条核对定义 3.1。

(A1) 在 $$\mathcal C^{\mathrm{op}}$$ 中要证 $$(h\circ^{\mathrm{op}}g)\circ^{\mathrm{op}}f=h\circ^{\mathrm{op}}(g\circ^{\mathrm{op}}f)$$。按定义，左边 $$=(f\circ g)\circ h$$，右边 $$=f\circ(g\circ h)$$；二者在 $$\mathcal C$$ 中因结合律相等。

(A2) $$1_Y\circ^{\mathrm{op}}f=f\circ 1_Y=f$$，同样由 $$\mathcal C$$ 的单位律。

(A3) 定义 3.1 直接搬运，没有改动任何"端点"信息。

所以 $$\mathcal C^{\mathrm{op}}$$ 确实是范畴，而且公理是**逐字**照搬的。

*第二步：对证明的长度归纳。* 设 $$S$$ 的证明是一串推导 $$S_1,\dots,S_m=S$$，每条 $$S_i$$ 或是公理 (A1)–(A3)，或是由前面的某条经"复合"或"代入已知结论"得到。归纳假设 $$S_i^{\mathrm{op}}$$ 在 $$\mathcal C^{\mathrm{op}}$$ 中成立。推理规则自对偶："$$g\circ f$$ 有定义且等于 $$h$$"掉头后是"$$f\circ^{\mathrm{op}}g$$ 有定义且等于 $$h$$"，仍是同一形式的陈述；代入规则与箭头方向无关。故 $$S_{i+1}^{\mathrm{op}}$$ 在 $$\mathcal C^{\mathrm{op}}$$ 中成立。归纳完毕。$$\blacksquare$$

**例 3.1（对偶原理的四个化身）**

(1) **积 ↔ 余积**（第 31 章）。积的万有性质是"存在唯一的 $$h$$ 使一切投影图交换"；把这句里的箭头全部掉头，得到的正是余积的万有性质。所以"积在同构意义下唯一"与"余积在同构意义下唯一"只需要证一遍。

(2) **同调 ↔ 上同调**（第 09、14、35 章）。同调 $$H_n=\ker\partial_n/\operatorname{im}\partial_{n+1}$$ 关于链映射是协变的；把链复形整体送进 $$\operatorname{Hom}_A(-,M)$$ 这一反变函子，得到的是**上同调** $$H^n=\ker\delta^n/\operatorname{im}\delta^{n-1}$$。定理 3.2 的证明掉头之后逐字给出上同调的函子性。

(3) **$$\operatorname{Spec}$$ 的反变性**（第 36 章）。见入口题 (iii)：$$\varphi:A\to B$$ 掉头成连续映射 $$\operatorname{Spec} B\to\operatorname{Spec} A$$。

(4) **Galois 对应**（第 39 章）。中间域越大，Galois 群越小；两个偏序集之间是**反序**对应。把偏序集看成范畴（$$x\le y$$ 即一条态射），这也是一个反变函子。

### 3.2 $$D^2=0$$ 与"两副面孔"

**定义 3.2（链复形与同调, chain complex and homology）** 设 $$A$$ 是环。$$A$$-模范畴中的**链复形**是一列 $$A$$-模与 $$A$$-线性映射
$$\cdots\xrightarrow{\ \partial_{n+1}\ }C_n\xrightarrow{\ \partial_n\ }C_{n-1}\xrightarrow{\ \partial_{n-1}\ }\cdots$$
使 $$\partial_n\circ\partial_{n+1}=0$$ 对一切 $$n$$ 成立，简记 $$\partial^2=0$$。称 $$Z_n=\ker\partial_n$$ 中的元素为 **$$n$$-闭链 (cycle)**，$$B_n=\operatorname{im}\partial_{n+1}$$ 中的元素为 **$$n$$-边界 (boundary)**。$$\partial^2=0$$ 与包含 $$B_n\subseteq Z_n$$ 是同一件事，于是可以定义
$$H_n(C,\partial)=Z_n/B_n=\ker\partial_n\ /\ \operatorname{im}\partial_{n+1}.$$

**定理 3.2（同调是函子, homology is functorial）** 设 $$(C,\partial)$$、$$(D,d)$$ 是链复形，$$f=\{f_n:C_n\to D_n\}$$ 是一族 $$A$$-线性映射且满足 $$d_n\circ f_n=f_{n-1}\circ\partial_n$$（这时称 $$f$$ 为**链映射 (chain map)**）。则

(i) $$f_n(Z_n(C))\subseteq Z_n(D)$$、$$f_n(B_n(C))\subseteq B_n(D)$$，因此 $$f_n$$ 诱导出良定义的 $$A$$-线性映射
$$H_n(f):H_n(C)\to H_n(D),\qquad [c]\mapsto[f_n(c)];$$
(ii) 若 $$g:(D,d)\to(E,e)$$ 也是链映射，则 $$H_n(g\circ f)=H_n(g)\circ H_n(f)$$，且 $$H_n(\mathrm{id}_C)=\mathrm{id}_{H_n(C)}$$。

**证明**：

(i) 设 $$c\in Z_n(C)$$，即 $$\partial_nc=0$$。由链映射条件，
$$d_n(f_nc)=f_{n-1}(\partial_nc)=f_{n-1}(0)=0,$$
故 $$f_nc\in\ker d_n=Z_n(D)$$。设 $$c\in B_n(C)$$，写 $$c=\partial_{n+1}c'$$。则
$$f_nc=f_n(\partial_{n+1}c')=d_{n+1}(f_{n+1}c')\in\operatorname{im}d_{n+1}=B_n(D).$$
所以 $$f_n$$ 把 $$Z_n(C)$$ 送进 $$Z_n(D)$$、把 $$B_n(C)$$ 送进 $$B_n(D)$$；由商模的万有性质，$$f_n$$ 诱导出 $$Z_n(C)/B_n(C)\to Z_n(D)/B_n(D)$$ 的线性映射。

良定义（这一步不能省）：设 $$[c]=[c']$$，即 $$c-c'\in B_n(C)$$，写 $$c-c'=\partial_{n+1}w$$。则
$$f_nc-f_nc'=f_n(\partial_{n+1}w)=d_{n+1}(f_{n+1}w)\in B_n(D),$$
故 $$[f_nc]=[f_nc']$$。线性由 $$f_n$$ 线性与商的线性结构直接继承。

(ii) 链映射的复合仍是链映射，因为 $$(g\circ f)_n=g_n\circ f_n$$ 使
$$e_n(g_nf_n)=(e_ng_n)f_n=(g_{n-1}d_n)f_n=g_{n-1}(d_nf_n)=g_{n-1}f_{n-1}\partial_n.$$
逐元素计算：
$$H_n(g\circ f)[c]=[(g\circ f)_nc]=[g_nf_nc]=H_n(g)[f_nc]=\big(H_n(g)\circ H_n(f)\big)[c].$$
恒等式情形由 $$\mathrm{id}_n$$ 的定义直接给出：$$H_n(\mathrm{id})[c]=[\mathrm{id}_nc]=[c]$$。$$\blacksquare$$

**注 3.2（为什么这一条是"$$D^2=0$$ 的三副面孔"）** 定理 3.2 的全部内容其实只有一句话：**$$\partial^2=0$$ 使"闭链模边界"可以定义，"与 $$\partial$$ 交换"使它可被搬运。** 全书至少三处是它的原样复述：

- 第 07 章：外微分满足 $$d^2=0$$（因为混合偏导可交换、而楔积反交换），于是有 de Rham 复形与 $$H^\bullet_{dR}$$；
- 第 09 章：边界算子满足 $$\partial^2=0$$（"边界的边界为零"），于是有同调群 $$H_n$$；
- 第 35 章：内射消解 $$0\to M\to I^0\to I^1\to\cdots$$ 是链复形，对它取反变 $$\operatorname{Hom}$$ 后再取同调，得导出函子 $$\operatorname{Ext}^n$$。

三处的差别只在"$$D$$ 是谁"：$$d$$ 是导子、$$\partial$$ 是组合算子、$$\delta$$ 是上边界。构造逐字相同。至于"另一副面孔"——第 07 章的 $$v^2=0$$ 与第 29 章的 $$v^2=q(v)$$——关系是：**外代数是 Clifford 代数在 $$q\equiv0$$ 时的特例**，因为两者的泛性质只差一个关系式（见精讲 2）。

### 3.3 谱

**定义 3.3（预解集与谱, resolvent set and spectrum）** 设 $$X\ne\{0\}$$ 是复 Banach 空间，$$T\in\mathcal B(X)$$。**预解集**是
$$\rho(T)=\{\lambda\in\mathbb C:\lambda I-T\ \text{是}\ X\ \text{上的有界可逆算子}\},$$
**谱 (spectrum)** 是它的补集 $$\sigma(T)=\mathbb C\setminus\rho(T)$$。对 $$\lambda\in\rho(T)$$ 记 $$R(\lambda)=(\lambda I-T)^{-1}$$，称为**预解式 (resolvent)**。

**定理 3.3（谱非空）** 设 $$X\ne\{0\}$$ 是复 Banach 空间，$$T\in\mathcal B(X)$$。则 $$\sigma(T)\ne\varnothing$$。

**证明思路**：若谱为空，预解式 $$R(\lambda)$$ 就是全平面上的解析函数；又由 Neumann 级数，$$\lVert R(\lambda)\rVert\to0$$（$$\lvert\lambda\rvert\to\infty$$），于是它是有界整函数。Liouville 定理迫使它恒为常数，而常数不可能既非零、又在无穷远处趋于零——矛盾。

**证明**：分四步。

*第一步：大圆之外可逆，且范数衰减。* 设 $$\lvert\lambda\rvert>\lVert T\rVert$$。则 $$\lambda I-T=\lambda(I-\lambda^{-1}T)$$，而 $$\lVert\lambda^{-1}T\rVert<1$$。几何级数 $$\sum_{k\ge0}(\lambda^{-1}T)^k$$ 在算子范数下绝对收敛（第 $$N$$ 个部分和的范数被 $$\sum_{k\le N}\lVert\lambda^{-1}T\rVert^k\le(1-\lVert\lambda^{-1}T\rVert)^{-1}$$ 控制），记其和为 $$S(\lambda)$$，则
$$S(\lambda)(I-\lambda^{-1}T)=(I-\lambda^{-1}T)S(\lambda)=I$$
（展开后中间项两两相消）。于是 $$\lambda\in\rho(T)$$，且
$$R(\lambda)=\lambda^{-1}S(\lambda)=\lambda^{-1}\sum_{k\ge0}\lambda^{-k}T^k,\qquad \lVert R(\lambda)\rVert\le\frac{\lvert\lambda\rvert^{-1}}{1-\lVert\lambda^{-1}T\rVert}=\frac{1}{\lvert\lambda\rvert-\lVert T\rVert}.$$
特别地 $$\lVert R(\lambda)\rVert\to0$$（$$\lvert\lambda\rvert\to\infty$$）。

*第二步：预解恒等式。* 对 $$\lambda,\mu\in\rho(T)$$，
$$R(\lambda)-R(\mu)=(\mu-\lambda)R(\lambda)R(\mu).$$
理由：在恒等式 $$A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}$$ 中取 $$A=\lambda I-T$$、$$B=\mu I-T$$，则 $$B-A=(\mu-\lambda)I$$，两边左乘 $$A^{-1}$$ 右乘 $$B^{-1}$$ 即得。

*第三步：$$R$$ 在 $$\rho(T)$$ 上解析。* 由第二步，
$$\frac{R(\mu)-R(\lambda)}{\mu-\lambda}=-R(\lambda)R(\mu).$$
先看连续性：仍由第二步，$$\lVert R(\mu)-R(\lambda)\rVert\le\lvert\mu-\lambda\rvert\,\lVert R(\lambda)\rVert\,\lVert R(\mu)\rVert$$；若 $$\lvert\mu-\lambda\rvert\,\lVert R(\lambda)\rVert\le\tfrac12$$，则
$$\lVert R(\mu)\rVert\le\lVert R(\lambda)\rVert+\tfrac12\lVert R(\lambda)\rVert\lVert R(\mu)\rVert\le\lVert R(\lambda)\rVert+\tfrac12\lVert R(\mu)\rVert,$$
故 $$\lVert R(\mu)\rVert\le2\lVert R(\lambda)\rVert$$，从而 $$\mu\to\lambda$$ 时 $$R(\mu)\to R(\lambda)$$。于是右端 $$\to-R(\lambda)^2$$，即 $$R$$ 在 $$\lambda$$ 处复可导且 $$R'(\lambda)=-R(\lambda)^2$$。又 $$\rho(T)$$ 是开集：若 $$\lvert\lambda-\lambda_0\rvert\lVert R(\lambda_0)\rVert<1$$，则 $$\lambda I-T=(\lambda_0I-T)\big(I-(\lambda_0-\lambda)R(\lambda_0)\big)$$ 可逆。所以 $$R$$ 在 $$\rho(T)$$ 上处处复可导。

*第四步：收尾。* 反设 $$\sigma(T)=\varnothing$$，则 $$\rho(T)=\mathbb C$$，$$R$$ 是整函数。由第一步，$$\lvert\lambda\rvert>\lVert T\rVert$$ 时 $$\lVert R(\lambda)\rVert\le1$$；在紧集 $$\lvert\lambda\rvert\le\lVert T\rVert$$ 上 $$\lVert R(\lambda)\rVert$$ 连续因而有界。所以 $$\lVert R(\lambda)\rVert$$ 在全平面有界。
对每个 $$\varphi\in X^*$$ 与 $$x\in X$$，标量函数 $$\lambda\mapsto\varphi(R(\lambda)x)$$ 是整函数，且被 $$\lVert\varphi\rVert\lVert x\rVert$$ 界住；由（标量）Liouville 定理它是常数。因这对一切 $$\varphi$$ 成立，$$R(\lambda)x$$ 关于 $$\lambda$$ 是常向量——若不然，取两个不同的值 $$u\ne v$$，由 Hahn–Banach 存在 $$\varphi$$ 使 $$\varphi(u)\ne\varphi(v)$$，与"$$\varphi(R(\lambda)x)$$ 是常数"矛盾。又这对一切 $$x$$ 成立，故 $$R(\lambda)$$ 是常算子。
但第一步给出 $$\lVert R(\lambda)\rVert\to0$$，常数只能取 $$0$$，即 $$R(\lambda)\equiv0$$。这与 $$R(\lambda)$$ 处处可逆矛盾：零算子不是可逆算子（$$X\ne\{0\}$$）。故 $$\sigma(T)\ne\varnothing$$。$$\blacksquare$$

**例 3.3（三个谱）**

(a) 第 02 章。$$R_\theta\in SO(2)$$（看作 $$\mathbb C^2$$ 上的实线性算子，或 $$\mathbb C$$ 上的乘 $$e^{i\theta}$$）的特征值是 $$e^{\pm i\theta}$$，故 $$\sigma(R_\theta)=\{e^{i\theta},e^{-i\theta}\}$$；而 $$t\mapsto R_t$$ 在 $$0$$ 处的导数给出 $$\mathfrak{so}(2)$$ 的生成元。这是"谱"在全书中最早出现的地方。

(b) 第 20 章。取 $$A=C(S^1)$$、$$f\in A$$、$$T=M_f$$（乘 $$f$$）。则 $$\sigma(M_f)=f(S^1)$$：算子 $$M_f-\lambda I=M_{f-\lambda}$$ 可逆当且仅当 $$f-\lambda$$ 在 $$S^1$$ 上无处为零（此时 $$1/(f-\lambda)$$ 连续）。而 Gelfand 谱 $$\widehat A=\operatorname{Hom}_{\text{alg}}(A,\mathbb C)$$ 与 $$S^1$$ 一一对应——每个特征就是某个赋值 $$\mathrm{ev}_z$$。谱集与参数集在这里第一次合而为一。

(c) 第 19 章。自伴算子 $$T=T^*$$ 的谱是 $$\mathbb R$$ 中的非空紧集（定理 3.3 保证非空）；谱定理进一步把它写成 $$\sigma(T)$$ 上某个**投影算子值测度**的积分。这是"谱"从有限个特征值长成一般对象的那一步。

### 3.4 Galois 连接：一条定理，两门学科

**定义 3.4（Galois 连接, Galois connection）** 设 $$(P,\le)$$、$$(Q,\le)$$ 是偏序集，$$F:P\to Q$$、$$G:Q\to P$$ 是**反序**映射（即 $$x\le x'\Rightarrow Fx\ge Fx'$$，$$y\le y'\Rightarrow Gy\ge Gy'$$）。称 $$(F,G)$$ 是一对 **Galois 连接**，若对一切 $$x\in P$$、$$y\in Q$$
$$y\le F(x)\iff x\le G(y).$$

**定理 3.4（Galois 连接的基本定理）** 设 $$(F,G)$$ 如定义 3.4。则

(i) 对一切 $$x\in P$$ 有 $$x\le G(F(x))$$；对一切 $$y\in Q$$ 有 $$F(G(y))\ge y$$；
(ii) $$F\circ G\circ F=F$$，$$G\circ F\circ G=G$$；
(iii) 记 $$P_0=\{x\in P:G(F(x))=x\}$$、$$Q_0=\{y\in Q:F(G(y))=y\}$$（称为**闭元**）。则 $$P_0=G(Q)$$、$$Q_0=F(P)$$，且 $$F$$ 与 $$G$$ 限制在 $$P_0$$ 与 $$Q_0$$ 上互为逆映射，特别地 $$F(P_0)=Q_0$$。

**证明**：

(i) 在等价式 $$y\le F(x)\iff x\le G(y)$$ 中取 $$y=F(x)$$：左边 $$F(x)\le F(x)$$ 恒真，故 $$x\le G(F(x))$$。取 $$x=G(y)$$：右边 $$G(y)\le G(y)$$ 恒真，故 $$F(G(y))\ge y$$。

(ii) 对任意 $$x$$，由 (i) 的后一式（取 $$y=F(x)$$）得 $$F(G(F(x)))\ge F(x)$$；又由 (i) 的前一式 $$x\le G(F(x))$$，两边作用反序的 $$F$$ 得 $$F(x)\ge F(G(F(x)))$$。两式合起来给出 $$F(G(F(x)))=F(x)$$，即 $$F\circ G\circ F=F$$。同法（把 $$x,y$$ 互换）得 $$G\circ F\circ G=G$$。

(iii) 先算 $$P_0$$。若 $$x\in P_0$$，即 $$x=G(F(x))$$，则 $$x\in G(Q)$$。反之设 $$x=G(y)$$，由 (ii) 得
$$G(F(x))=G(F(G(y)))=G(y)=x,$$
故 $$x\in P_0$$。于是 $$P_0=G(Q)$$；同理可得 $$Q_0=F(P)$$。
再证互逆。对 $$x\in P_0$$，$$G(F(x))=x$$ 正是 $$P_0$$ 的定义，故 $$G\circ F$$ 在 $$P_0$$ 上是恒等映射；对 $$y\in Q_0$$，$$F(G(y))=y$$ 正是 $$Q_0$$ 的定义。于是 $$F\vert_{P_0}$$ 与 $$G\vert_{Q_0}$$ 互为逆映射，特别地 $$F(P_0)=Q_0$$。$$\blacksquare$$

**注 3.4（Galois 对应与覆叠对应是同一台机器）** 把定理 3.4 的两副输入填上，就得到全书最后两章与最早拓扑章的核心定理。

- **Galois 理论**（第 38、39 章）。设 $$k\subseteq K$$ 是**有限** Galois 扩张。令 $$P$$ 为中间域 $$\{E:k\subseteq E\subseteq K\}$$ 按包含序，$$Q$$ 为子群 $$\{H:H\le\operatorname{Gal}(K/k)\}$$ 按**反**包含序，取
$$F(E)=\operatorname{Gal}(K/E),\qquad G(H)=K^H\ \text{（}H\ \text{的固定域）}.$$
$$F,G$$ 都反序：域越大，保持它不动的自同构越少。恒等式 $$G(F(E))=E$$ 与 $$F(G(H))=H$$ 由度数的乘法性与 $$\lvert\operatorname{Gal}(K/k)\rvert=[K:k]$$ 给出。定理 3.4 (iii) 于是成为：**中间域与子群的一一对应**。顺带解释了第 39 章那句"$$K/k$$ 是 Galois 的 $$\iff$$ 固定域恰为 $$k$$"：它说的是 $$H$$ 是闭元。
- **覆叠理论**（第 08、25 章）。把 $$P$$ 换成连通覆盖空间、$$Q$$ 换成基本群的子群（按反包含序），$$F$$ = 取覆盖对应的子群、$$G$$ = 由子群构造覆盖。完全相同的推理给出"子群的共轭类 ↔ 连通覆盖的同构类"，其中正规子群对应 Galois 覆盖。

一个证明，两门学科。**这正是本书把 Galois 理论放在最后的理由**：它不是一块新领地，而是那条从第 08 章就开始的"拓扑 ↔ 代数"对应线的终点站。

### 3.5 三角：几何、物理、代数在同一行公式里

**命题 3.5（$$dF=0$$ 就是齐次 Maxwell 方程组）** 在 $$\mathbb R^4$$ 上取坐标 $$(x^0,x^1,x^2,x^3)=(t,x,y,z)$$，设
$$F=\sum_{0\le i<j\le3}F_{ij}\,dx^i\wedge dx^j$$
是 2-形式，其系数按标准约定取自电场 $$\mathbf E=(E_x,E_y,E_z)$$ 与磁场 $$\mathbf B=(B_x,B_y,B_z)$$：
$$F_{0i}=E_i\quad(i=1,2,3),\qquad F_{ij}=-\varepsilon_{ijk}B_k\quad(1\le i<j\le3),$$
这里 $$\varepsilon_{ijk}$$ 是 Levi-Civita 符号。则 $$dF=0$$ 等价于
$$\operatorname{div}\mathbf B=0,\qquad \partial_t\mathbf B+\operatorname{curl}\mathbf E=0.$$

**证明**：由外微分的定义（第 07、12 章），$$d\big(f\,dx^i\wedge dx^j\big)=df\wedge dx^i\wedge dx^j$$，而 $$dx^k\wedge dx^i\wedge dx^j$$ 在每个下标出现两次时为零、交换两个下标时变号。把 $$dF=\sum_{i<j}\sum_k\partial_kF_{ij}\,dx^k\wedge dx^i\wedge dx^j$$ 按三元组 $$i<j<k$$ 归项，每个三元组恰有三项落进来：

$$dF=\sum_{i<j<k}\big(\partial_iF_{jk}+\partial_jF_{ki}+\partial_kF_{ij}\big)\,dx^i\wedge dx^j\wedge dx^k,$$

其中第二个括号里的 $$F_{ki}$$ 按 $$F_{ki}=-F_{ik}$$ 理解。$$\mathbb R^4$$ 中的 3-形式只有四个独立系数，逐个算。

**三元组 $$(1,2,3)$$：** $$\partial_1F_{23}+\partial_2F_{31}+\partial_3F_{12}=\partial_x(-B_x)+\partial_y(-B_y)+\partial_z(-B_z)=-(\partial_xB_x+\partial_yB_y+\partial_zB_z)$$。令其为零即 $$\operatorname{div}\mathbf B=0$$。

**三元组 $$(0,1,2)$$：** $$\partial_0F_{12}+\partial_1F_{20}+\partial_2F_{01}=\partial_t(-B_z)-\partial_xE_y+\partial_yE_x=-\big(\partial_tB_z+(\partial_xE_y-\partial_yE_x)\big)$$。令其为零即 Faraday 定律的 $$z$$ 分量
$$\partial_tB_z=-\,(\operatorname{curl}\mathbf E)_z.$$

**三元组 $$(0,1,3)$$：** $$\partial_0F_{13}+\partial_1F_{30}+\partial_3F_{01}=\partial_tB_y-\partial_xE_z+\partial_zE_x=\partial_tB_y+(\operatorname{curl}\mathbf E)_y$$。令其为零即 $$y$$ 分量。

**三元组 $$(0,2,3)$$：** $$\partial_0F_{23}+\partial_2F_{30}+\partial_3F_{02}=\partial_t(-B_x)-\partial_yE_z+\partial_zE_y=-\big(\partial_tB_x+(\operatorname{curl}\mathbf E)_x\big)$$。令其为零即 $$x$$ 分量。

四式合起来正是 $$\operatorname{div}\mathbf B=0$$ 与 $$\partial_t\mathbf B+\operatorname{curl}\mathbf E=0$$。$$\blacksquare$$

**例 3.5（同一个 $$\Lambda^\bullet$$，三个学科）** 命题 3.5 里的 $$d$$ 是第 07 章的外微分；把 $$\Lambda^\bullet$$ 整体当作链复形、取它的同调，就是第 14 章的 de Rham 上同调（而 $$H^2_{dR}(\mathbb R^4)=0$$ 恰好说明"闭的 2-形式必是恰当的"，即齐次方程组的解都来自势 $$A$$，$$F=dA$$）；而第 29 章告诉我们，把外代数"$$q$$-变形"$$\Lambda^\bullet\rightsquigarrow \operatorname{Cl}(V,q)$$，同一个 $$d$$ 就变成 Dirac 算子的平方。物理（Maxwell）、几何（形式与 Stokes）、代数（分次代数与其导子）在同一行公式里会齐——这就是本课程反复出现的那条三角线。

## 四、几何与物理直觉 (Intuition)

### 4.1 这张图长什么样

六卷是从"具体到抽象"铺的一条台阶：复数（卷一）$$\to$$ 流形与积分（卷二）$$\to$$ 分析与量子（卷三）$$\to$$ 群与对称（卷四）$$\to$$ 范畴与同调（卷五）$$\to$$ 数论与 Galois（卷六）。台阶是给读者的路线图；真正的结构是**竖着穿过这六级台阶的四条线**。下面逐条把它们排出来。

### 4.2 地图一：对偶与反变

| 章 | 对象 | 反变发生在哪里 |
|---|---|---|
| 03 | 对偶空间 $$V^*=\operatorname{Hom}_k(V,k)$$ | 线性映射 $$f:V\to W$$ 掉头成 $$f^*:W^*\to V^*$$；$$\lvert V\rvert=\lvert W\rvert$$ 时才有同构，且要选基 |
| 15 | Riesz 表示 $$H\cong H^*$$ | $$x\mapsto\langle x,-\rangle$$ 是**反线性**等距；不选基，因此是"自然"的 |
| 20 | Gelfand 谱 $$\widehat A=\operatorname{Hom}_{\text{alg}}(A,\mathbb C)$$ | 代数同态 $$\varphi:A\to B$$ 掉头成 $$\widehat B\to\widehat A$$；这正是赋值的拉回 |
| 31 | 对偶范畴 $$\mathcal C^{\mathrm{op}}$$ | 把每个箭头掉头，公理逐字成立（定理 3.1） |
| 36 | $$\operatorname{Spec} A$$ | 环同态掉头成连续映射；Zariski 闭集 $$V(\mathfrak a)$$ 与理想 $$\mathfrak a$$ 反序对应 |
| 37 | Čech 上同调 $$\check H^\bullet(\mathfrak U;\mathbb Z)$$ | 开集的包含 $$\iota:U\hookrightarrow V$$ 给出反向的限制映射 $$\iota^*:\mathcal F(V)\to\mathcal F(U)$$ |

**几何直觉**：对偶是"从函数看空间"。给一个空间 $$X$$，我们实际上只能通过它上面的函数（$$C(X)$$、$$\mathcal O_X$$）去了解它；而"函数"天然是反变的——空间之间的映射，把函数拉回来。第 20 章与第 36 章把这件事推到极致：**空间可以由它的函数代数完全重建**（Gelfand–Naimark 与仿射概形）。这也是为什么 $$\operatorname{Spec}$$ 必须反变：它不是一个"几何实现"，而是一个**等价**——两个范畴反向相等。

**物理直觉**：第 03 章的"逆变/协变"在物理里就是**坐标变换下的两类量**：切向量按 $$\partial/\partial x^i$$ 变，余切向量（如梯度 $$\partial f/\partial x^i$$）按相反的方向变。物理定律必须把这两类指标配成一对才写出不变量，这就是"上下指标求和"的真正内容。

### 4.3 地图二：同一个构造的两副面孔

**面孔对 1：$$v^2=0$$ 与 $$v^2=q(v)$$。**
第 07 章的外代数 $$\Lambda^\bullet V$$ 满足 $$v\wedge v=0$$；第 29 章的 Clifford 代数 $$\operatorname{Cl}(V,q)$$ 满足 $$v^2=q(v)\cdot1$$。把它们写成同一句话：

$$\operatorname{Cl}(V,q)=T(V)\ /\ \langle\ v\otimes v-q(v)\ \rangle,\qquad \Lambda^\bullet V=T(V)\ /\ \langle\ v\otimes v\ \rangle=\operatorname{Cl}(V,0).$$

取 $$q\equiv0$$ 就退回外代数。这不是类比，是同一条商构造的两个参数值（见精讲 2）。物理上这对应**费米子与玻色子**：$$q=0$$ 的反对易关系给出外代数（Pauli 不相容），$$q\ne0$$ 的 Clifford 关系给出 Dirac 代数（相对论性电子）。

**面孔对 2：三个"平方为零"。**
第 07 章的 $$d^2=0$$、第 09 章的 $$\partial^2=0$$、第 35 章导出函子里的 $$\delta^2=0$$——它们各自的第一条定理都是定理 3.2，差别只在"$$D$$ 是谁"。物理上 $$d^2=0$$ 还有一层含义：$$F=dA$$ 自动满足 $$dF=0$$，所以**齐次 Maxwell 方程组不是物理假设，而是 $$d^2=0$$ 的推论**（命题 3.5）。

**面孔对 3：对称与反对称的同一个来源。**
第 04 章的辛形式 $$\omega$$ 反对称，第 11 章的度量 $$g$$ 对称；两者都是 $$V\otimes V\to k$$ 的双线性型，只差一个符号。第 22 章的正则对易关系 $$[p,q]=\mathrm i\hbar$$ 与第 29 章 Clifford 的 $$v^2=q(v)$$ 是同一支"量子化"的两个版本：**对称化给出玻色子（对易），反对称化给出费米子（反对易）**。

### 4.4 地图三：谱、特征值、表示

| 章 | 那里"谱"是什么 |
|---|---|
| 02 | $$SO(2)$$ 的特征值 $$e^{\pm i\theta}$$；求导给出 $$\mathfrak{so}(2)$$——**无穷小版本** |
| 16 | 可观测量 = 自伴算子；测量值 = 谱——**物理版本** |
| 18–19 | 有界算子的谱、预解式、投影算子值测度——**分析版本**（定理 3.3） |
| 22 | Stone–von Neumann：正则对易关系的表示在同构意义下唯一——**唯一性版本** |
| 28 | 复半单 Lie 代数的权与根：$$K$$ 的格点被 Weyl 群作用——**离散/组合版本** |
| 30 | 双重覆叠与射影表示：$$SU(2)\to SO(3)$$ 的 $$\mathbb Z/2$$ 障碍——**拓扑版本** |

**直觉**：一条线上的六个站点说的是同一件事——"**把算子变成数**"。特征值是第一步（有限维、能算出来），谱是全平面上的闭集（无穷维、靠 Liouville 保证非空，定理 3.3），投影算子值测度是"把算子按谱切成可数无穷多块"的精确说法，而表示论则是"当算子来自对称群时，谱本身可以被组合地分类"。

### 4.5 地图四：几何 ↔ 物理 ↔ 代数 的三角

| 章 | 几何 | 物理 | 代数 |
|---|---|---|---|
| 04 | 辛形式、辛流形 | 相空间与 Hamilton 力学 | 反对称双线性型、辛群 |
| 06 | 纤维丛、余切丛 | 场（每点一个自由度的场量） | 模、自由模上的转移函数 |
| 13 | 定向流形与带边流形 | 守恒量与通量 | 边缘算子 $$\partial$$ 与其对偶 $$d$$ |
| 24 | 变换群、Lie 群 | 对称性与守恒律（Noether） | Lie 代数、括号 |
| 36 | 概形、Zariski 拓扑 | ——（算术的"几何化"） | 交换环、素理想谱、层 |

三角的读法是这样的：**几何提出问题**（"两个子簇交几次""这个丛有没有整体截面"），**代数提供工具**（理想、模、导出函子、同调群），**物理提供直觉与检验**（守恒律、变分原理、对称性决定相互作用）。每一章的入口题几乎都是"一个几何问题"，而解答几乎都落在"一个代数不变量"上；中间那一步的动机，往往来自物理。

第 36 章是这张三角最极端的一次实验：它把**算术本身**（$$\mathbb Z$$、$$\mathbb F_q$$ 上的方程）也画进几何这一格，于是"数论问题"和"几何问题"从此是同一门学科的两半。第 38、39 章立刻给出了第一次回报：数域扩张的 Galois 群，和黎曼面的覆叠变换群，服从同一套定理（注 3.4）。

### 4.6 三段历史注脚

- **1832 年，Galois**。据通行说法，他在决斗前夜写下的遗稿里反复出现"群"这个词，却始终用"置换"称呼它——他手里已有定理 3.4，却还没有"子群"的语言。他关心的是一元方程的根式可解性，得到的却是整个代数的骨架。
- **1920–1930 年代，Noether 与 van der Waerden**。Emmy Noether 把"理想"当成对象来研究，交换代数与代数几何由此合流：零点集与理想是同一个东西的两副面孔。第 36 章的字典就是这次合流的产物。
- **1957 年，Grothendieck 的 Tôhoku 论文**。他把"同调"从具体对象里解放出来，写成"右导出函子的普遍定义"。第 35 章的导出函子、第 31–33 章的范畴语言，都来自这一次抽象——**抽象得越彻底，能装下的例子越多**，这正是本章四条主线能贯穿六卷的原因。

## 五、经典问题精讲 (Classical Problems)

### 精讲 1（余积是什么：把对偶原理用一次）

**考点**：定义 3.1 与定理 3.1。**在本章结构里的位置**：地图一的第一格（第 03、31 章）。

**(i)** 写出积 $$X\times Y$$ 的万有性质；
**(ii)** 把 (i) 的每个箭头掉头，写出得到的陈述，并指出它就是余积的万有性质；
**(iii)** 证明：若 $$(P,\pi_X,\pi_Y)$$ 与 $$(P',\pi'_X,\pi'_Y)$$ 都是 $$X$$ 与 $$Y$$ 的积，则存在唯一同构 $$u:P\to P'$$ 使 $$\pi'_Xu=\pi_X$$、$$\pi'_Yu=\pi_Y$$；
**(iv)** 在 $$\mathbf{Vect}_k$$ 里认出余积的具体形态并验证它的万有性质。

**解**：

**(i)** $$P$$ 连同一对态射 $$\pi_X:P\to X$$、$$\pi_Y:P\to Y$$，使得**对任意**对象 $$Z$$ 与任意一对态射 $$f:Z\to X$$、$$g:Z\to Y$$，存在**唯一**的 $$h:Z\to P$$ 使
$$\pi_Xh=f,\qquad \pi_Yh=g.$$

**(ii)** 把 (i) 中每个箭头的方向掉头：$$\pi_X:P\to X$$ 变成 $$\iota_X:X\to P$$，$$\pi_Y$$ 变成 $$\iota_Y:Y\to P$$，条件里的 $$f:Z\to X$$、$$g:Z\to Y$$、$$h:Z\to P$$ 变成 $$f:X\to Z$$、$$g:Y\to Z$$、$$h:P\to Z$$。得到的陈述是：

> $$P$$ 连同一对态射 $$\iota_X:X\to P$$、$$\iota_Y:Y\to P$$，使得对任意对象 $$Z$$ 与任意一对态射 $$f:X\to Z$$、$$g:Y\to Z$$，存在唯一的 $$h:P\to Z$$ 使 $$h\iota_X=f$$、$$h\iota_Y=g$$。

这正是余积 $$X\sqcup Y$$ 的万有性质。这一步不需要"证明"——它就是定义的逐字对偶化；由定理 3.1，凡对一切范畴成立的积的结论，自动对余积成立。

**(iii)** 把 $$(P',\pi'_X,\pi'_Y)$$ 当作积、把 $$Z=P$$、$$f=\pi_X$$、$$g=\pi_Y$$ 代入 (i)，得**唯一**的 $$u:P\to P'$$ 使
$$\pi'_Xu=\pi_X,\qquad \pi'_Yu=\pi_Y.$$
对称地，把 $$(P,\pi_X,\pi_Y)$$ 当作积、代入 $$Z=P'$$、$$f=\pi'_X$$、$$g=\pi'_Y$$，得唯一的 $$v:P'\to P$$ 使
$$\pi_Xv=\pi'_X,\qquad \pi_Yv=\pi'_Y.$$
现在看 $$vu:P\to P$$。用复合的结合律：
$$\pi_X(vu)=(\pi_Xv)u=\pi'_Xu=\pi_X,\qquad \pi_Y(vu)=(\pi_Yv)u=\pi'_Yu=\pi_Y.$$
在 (i) 中取 $$Z=P$$、$$f=\pi_X$$、$$g=\pi_Y$$：满足同样条件的 $$h$$ 是**唯一**的，而 $$h=\mathrm{id}_P$$ 满足这两式（$$\pi_X\mathrm{id}_P=\pi_X$$、$$\pi_Y\mathrm{id}_P=\pi_Y$$），故 $$vu=\mathrm{id}_P$$。同法 $$uv=\mathrm{id}_{P'}$$。于是 $$u$$ 是同构，且由万有性质的唯一性，这样的 $$u$$ 只有一个。

**(iv)** 取 $$P=X\oplus Y$$（直和），
$$\iota_X(x)=(x,0),\qquad \iota_Y(y)=(0,y).$$
给定 $$f:X\to Z$$、$$g:Y\to Z$$，定义
$$h(x,y)=f(x)+g(y);$$
$$h$$ 是线性的（$$f,g$$ 线性，加法与数乘逐分量）。验证：
$$h\iota_X(x)=h(x,0)=f(x),\qquad h\iota_Y(y)=h(0,y)=g(y).$$
唯一性：任一满足条件的 $$h'$$ 都必须有
$$h'(x,y)=h'\big(\iota_Xx+\iota_Yy\big)=h'\iota_Xx+h'\iota_Yy=f(x)+g(y)=h(x,y),$$
这里用了 $$(x,y)=\iota_Xx+\iota_Yy$$ 与 $$h'$$ 的线性。故 $$h'=h$$。所以 $$\mathbf{Vect}_k$$ 中余积就是直和。$$\blacksquare$$

> 注意最后一步用到的正是直和的定义性质"每个元素唯一地写成两个分量之和"——万有性质里的"存在唯一"不是白来的。

### 精讲 2（两副面孔：$$q=0$$ 的 Clifford 就是外代数）

**考点**：第 07 章与第 29 章的同一个商构造（注 3.2）。**位置**：地图二的面孔对 1。

**题目**：设 $$V$$ 是特征不等于 $$2$$ 的域上的向量空间。证明 $$\operatorname{Cl}(V,0)\cong\Lambda^\bullet V$$ 作为结合代数。

**解**：先写下两边的泛性质（这是第 07、29 章各自的核心定理）。

- **外代数的泛性质**：设 $$\iota:V\to\Lambda^\bullet V$$ 是到一次部分的包含。对任意结合 $$k$$-代数 $$A$$ 与任意线性映射 $$\psi:V\to A$$，若 $$\psi(v)^2=0$$ 对一切 $$v\in V$$，则存在**唯一**代数同态 $$\widetilde\psi:\Lambda^\bullet V\to A$$ 使 $$\widetilde\psi\circ\iota=\psi$$。
- **Clifford 代数的泛性质**：$$\operatorname{Cl}(V,q)=T(V)/\langle v\otimes v-q(v)\cdot1\rangle$$，结构映射 $$j:V\to\operatorname{Cl}(V,q)$$ 满足 $$j(v)^2=q(v)\cdot1$$。对任意结合 $$k$$-代数 $$A$$ 与任意线性映射 $$\phi:V\to A$$，若 $$\phi(v)^2=q(v)\cdot1$$ 对一切 $$v$$ 成立，则存在**唯一**代数同态 $$\widetilde\phi:\operatorname{Cl}(V,q)\to A$$ 使 $$\widetilde\phi\circ j=\phi$$。

在 $$\Lambda^\bullet V$$ 中，对 $$v\in V$$ 有 $$v\wedge v=0$$：因为 $$\wedge$$ 反交换（第 07 章），$$v\wedge v=-v\wedge v$$，即 $$2(v\wedge v)=0$$，而特征不为 $$2$$，故 $$v\wedge v=0$$。

**第一步**，取 $$q=0$$：$$j:V\to\operatorname{Cl}(V,0)$$ 满足 $$j(v)^2=0\cdot1=0$$。把它当作外代数泛性质中的 $$\psi$$（目标代数 $$A=\operatorname{Cl}(V,0)$$），得唯一同态
$$\Psi:\Lambda^\bullet V\to\operatorname{Cl}(V,0),\qquad \Psi\circ\iota=j.$$

**第二步**，$$\iota:V\to\Lambda^\bullet V$$ 满足 $$\iota(v)^2=v\wedge v=0=0\cdot1$$。把它当作 Clifford 泛性质中的 $$\phi$$（目标代数 $$A=\Lambda^\bullet V$$，$$q=0$$），得唯一同态
$$\Phi:\operatorname{Cl}(V,0)\to\Lambda^\bullet V,\qquad \Phi\circ j=\iota.$$

**第三步**，看复合 $$\Psi\Phi:\operatorname{Cl}(V,0)\to\operatorname{Cl}(V,0)$$。它是代数同态，且
$$(\Psi\Phi)\circ j=\Psi\circ(\Phi\circ j)=\Psi\circ\iota=j=\mathrm{id}\circ j.$$
在 Clifford 泛性质中取 $$A=\operatorname{Cl}(V,0)$$、$$\phi=j$$，"延拓同态唯一"这一条说的正是：满足 $$\widetilde\phi\circ j=j$$ 的同态只有 $$\mathrm{id}$$。故 $$\Psi\Phi=\mathrm{id}$$。

**第四步**，同理看 $$\Phi\Psi:\Lambda^\bullet V\to\Lambda^\bullet V$$：
$$(\Phi\Psi)\circ\iota=\Phi\circ(\Psi\circ\iota)=\Phi\circ j=\iota=\mathrm{id}\circ\iota,$$
由外代数泛性质的唯一性得 $$\Phi\Psi=\mathrm{id}$$。

于是 $$\Phi$$、$$\Psi$$ 互为逆同态，$$\operatorname{Cl}(V,0)\cong\Lambda^\bullet V$$。$$\blacksquare$$

> 这道题说明：两副面孔之间不是"类比"，而是**同一个泛性质在 $$q=0$$ 处的取值**。$$q$$ 就是那个旋钮：拧到 $$0$$ 得外代数（费米子），拧到正定得 Dirac 代数。

### 精讲 3（谱的第一个非平凡例：$$C(S^1)$$ 上的乘法算子）

**考点**：定义 3.3 与定理 3.3。**位置**：地图三的第 18–20 章一格，也是例 3.3(b) 的完整化。

**题目**：设 $$A=C(S^1)$$（$$S^1$$ 上连续复值函数，取上确界范数），$$z:S^1\to\mathbb C$$ 是恒等映射，$$M_z\in\mathcal B(A)$$ 是乘 $$z$$ 的算子：$$(M_zf)(\zeta)=\zeta f(\zeta)$$。求 $$\sigma(M_z)$$。

**解**：

**第一步：$$M_f$$ 可逆的判据。** 对 $$f\in A$$ 记 $$M_f$$ 为乘 $$f$$。两个事实：(a) $$M_fM_g=M_{fg}$$（逐点乘法结合）；(b) $$\lVert M_f\rVert=\sup_{\zeta\in S^1}\lvert f(\zeta)\rvert=\lVert f\rVert_\infty$$，上界由 $$\lvert f(\zeta)g(\zeta)\rvert\le\lVert f\rVert_\infty\lvert g(\zeta)\rvert$$ 得，下界取 $$g\equiv1$$ 得。

断言：$$M_f$$ 可逆 $$\iff$$ $$f$$ 在 $$S^1$$ 上无处为零。
若 $$f$$ 无零点，则 $$\lvert f\rvert$$ 在紧集 $$S^1$$ 上取到正的最小值 $$m>0$$，故 $$1/f$$ 连续、$$\lVert1/f\rVert_\infty=1/m$$，且 $$M_fM_{1/f}=M_1=\mathrm{id}$$，可逆。
反之设 $$f(\zeta_0)=0$$。取 $$g_n\in A$$ 满足 $$0\le g_n\le1$$、$$g_n(\zeta_0)=1$$、且在 $$\lvert\zeta-\zeta_0\rvert\ge1/n$$ 处为 $$0$$（例如按距离线性过渡）。则 $$\lVert g_n\rVert_\infty=1$$，而
$$\lVert M_fg_n\rVert_\infty=\sup_{\lvert\zeta-\zeta_0\rvert<1/n}\lvert f(\zeta)g_n(\zeta)\rvert\le\sup_{\lvert\zeta-\zeta_0\rvert<1/n}\lvert f(\zeta)\rvert\longrightarrow0\quad(n\to\infty),$$
最后一步是 $$f(\zeta_0)=0$$ 与 $$f$$ 连续。若 $$M_f$$ 可逆，则对一切 $$g$$，
$$\lVert g\rVert_\infty=\lVert M_f^{-1}M_fg\rVert_\infty\le\lVert M_f^{-1}\rVert\,\lVert M_fg\rVert_\infty,$$
即 $$\lVert M_fg_n\rVert_\infty\ge\lVert M_f^{-1}\rVert^{-1}>0$$，与上式矛盾。

**第二步：确定谱。** 注意 $$M_z-\lambda I=M_{z-\lambda}$$（$$\lambda I=M_{\lambda}$$，常数函数）。由第一步，$$M_{z-\lambda}$$ 可逆 $$\iff$$ 函数 $$\zeta\mapsto\zeta-\lambda$$ 在 $$S^1$$ 上无零点 $$\iff$$ $$\lvert\lambda\rvert\ne1$$。故
$$\sigma(M_z)=\{\lambda\in\mathbb C:\lvert\lambda\rvert=1\}=S^1.$$

**第三步：与定理 3.3 对照。** $$S^1$$ 是非空紧集，与定理 3.3 一致；$$\lvert\lambda\rvert>1$$ 时第一步给出的逆正是定理 3.3 证明里的 Neumann 级数（此时 $$\lVert\lambda^{-1}M_z\rVert=1/\lvert\lambda\rvert<1$$）。$$\lvert\lambda\rvert=1$$ 时算子不可逆，而 $$\lVert M_z-\lambda I\rVert=2$$ 有限——这说明 $$\lVert T\rVert$$ **只给出谱半径的上界，不给下界**：谱的非空性是分析的味道（Liouville），不是估计的味道。$$\blacksquare$$

### 精讲 4（Galois 连接的一次完整运行：$$\mathbb Q(\sqrt2,\sqrt3)/\mathbb Q$$）

**考点**：定义 3.4 与定理 3.4。**位置**：地图一的第四格（第 39 章），也是注 3.4 里 Galois 侧的例子。

**题目**：设 $$K=\mathbb Q(\sqrt2,\sqrt3)$$。求出 $$\operatorname{Gal}(K/\mathbb Q)$$、它的全部子群、以及全部中间域，并造出对应表。

**解**：

**第一步：次数与基底。** 先证 $$\mathbb Q(\sqrt2)\cap\mathbb Q(\sqrt3)=\mathbb Q$$。设 $$\sqrt3=a+b\sqrt2$$（$$a,b\in\mathbb Q$$），平方得
$$3=a^2+2b^2+2ab\sqrt2.$$
若 $$ab\ne0$$，则 $$\sqrt2=(3-a^2-2b^2)/(2ab)\in\mathbb Q$$，矛盾；故 $$ab=0$$。若 $$b=0$$，则 $$\sqrt3=a\in\mathbb Q$$，矛盾；若 $$a=0$$，则 $$\sqrt3=b\sqrt2$$，平方得 $$3=2b^2$$——写 $$b=p/q$$ 既约，则 $$3q^2=2p^2$$，故质数 $$3\mid p$$，从而 $$3\mid q$$，与既约矛盾。所以交为 $$\mathbb Q$$。
于是 $$\sqrt2\notin\mathbb Q(\sqrt3)$$，多项式 $$x^2-2$$ 在 $$\mathbb Q(\sqrt3)$$ 上不可约，$$[K:\mathbb Q]=2\cdot2=4$$，且 $$\{1,\sqrt2,\sqrt3,\sqrt6\}$$ 是基（两个二次扩张的基相乘）。

**第二步：Galois 群。** $$K$$ 是 $$(x^2-2)(x^2-3)$$ 的分裂域，故 $$K/\mathbb Q$$ 是 Galois 扩张。$$\mathbb Q$$-自同构 $$\sigma$$ 由 $$\sigma(\sqrt2)$$、$$\sigma(\sqrt3)$$ 决定，而它们只能取 $$\pm\sqrt2$$、$$\pm\sqrt3$$（自同构把多项式的根送到根），所以 $$\lvert\operatorname{Gal}(K/\mathbb Q)\rvert\le4$$；又 $$\lvert\operatorname{Gal}(K/\mathbb Q)\rvert=[K:\mathbb Q]=4$$，故恰有 4 个自同构：
$$G=\{\mathrm{id},\ \sigma,\ \tau,\ \sigma\tau\},\qquad \sigma(\sqrt2)=-\sqrt2,\ \sigma(\sqrt3)=\sqrt3;\quad \tau(\sqrt2)=\sqrt2,\ \tau(\sqrt3)=-\sqrt3.$$
每个非恒等元的阶为 2，且 $$\sigma\tau=\tau\sigma$$，故 $$G\cong\mathbb Z/2\times\mathbb Z/2$$。

**第三步：全部子群。** $$\mathbb Z/2\times\mathbb Z/2$$ 的子群恰有 5 个：
$$G,\quad\langle\sigma\rangle=\{\mathrm{id},\sigma\},\quad\langle\tau\rangle,\quad\langle\sigma\tau\rangle,\quad\{1\},$$
其中三个 2 阶子群各由一个非恒等元生成。

**第四步：固定域。** 由定理 3.4 (iii)，中间域与子群一一对应且反序。对 2 阶子群 $$H$$，$$[K^H:\mathbb Q]=[G:H]=2$$，故 $$K^H$$ 是二次子域；只要找被 $$H$$ 固定的那个平方根。

- $$H=\langle\sigma\rangle$$：$$\sigma(\sqrt3)=\sqrt3$$ 而 $$\sigma(\sqrt2)=-\sqrt2$$，故 $$K^{\langle\sigma\rangle}=\mathbb Q(\sqrt3)$$。
- $$H=\langle\tau\rangle$$：同理 $$K^{\langle\tau\rangle}=\mathbb Q(\sqrt2)$$。
- $$H=\langle\sigma\tau\rangle$$：$$(\sigma\tau)(\sqrt2)=-\sqrt2$$、$$(\sigma\tau)(\sqrt3)=-\sqrt3$$，故 $$(\sigma\tau)(\sqrt6)=(-\sqrt2)(-\sqrt3)=\sqrt6$$，即 $$\sqrt6$$ 被固定，而 $$\sqrt2$$ 不被固定，故 $$K^{\langle\sigma\tau\rangle}=\mathbb Q(\sqrt6)$$。

对应表：

| 子群 $$H$$（按反包含序） | 固定域 $$K^H$$（按包含序） | $$[K^H:\mathbb Q]$$ |
|---|---|---|
| $$\{1\}$$ | $$K=\mathbb Q(\sqrt2,\sqrt3)$$ | 4 |
| $$\langle\sigma\rangle$$ | $$\mathbb Q(\sqrt3)$$ | 2 |
| $$\langle\tau\rangle$$ | $$\mathbb Q(\sqrt2)$$ | 2 |
| $$\langle\sigma\tau\rangle$$ | $$\mathbb Q(\sqrt6)$$ | 2 |
| $$G$$ | $$\mathbb Q$$ | 1 |

**第五步：核对反序。** $$H$$ 越大，固定域 $$K^H$$ 越小——这正是定义 3.4 中 $$F$$、$$G$$ 都反序的含义。定理 3.4 (i) 的两个不等号在这里分别是：$$H\supseteq\{1\}$$ 给出 $$K^H\subseteq K^{\{1\}}=K$$；$$H\subseteq G$$ 给出 $$K^H\supseteq K^G=\mathbb Q$$。$$\blacksquare$$

## 六、练习 (Exercises)

### 基础（巩固定义）

**基1.** 写出对偶范畴 $$\mathcal C^{\mathrm{op}}$$ 的定义（对象、态射、复合、恒等四条），并逐条验证
$$(\mathcal C^{\mathrm{op}})^{\mathrm{op}}=\mathcal C.$$
再用定理 3.1 说明：为什么"积的对偶是余积"这句话不需要重新证明？

**基2.** 判断下列哪些是链复形，并算出是链复形的那些的同调：
(a) $$0\to\mathbb Z\xrightarrow{\ \times2\ }\mathbb Z\xrightarrow{\ \pi\ }\mathbb Z/2\to0$$（$$\pi$$ 是模 2 归约）；
(b) $$0\to\mathbb Z\xrightarrow{\ \times2\ }\mathbb Z\xrightarrow{\ \pi_4\ }\mathbb Z/4\to0$$（$$\pi_4$$ 是模 4 归约）；
(c) $$\Lambda^0(\mathbb R^2)\xrightarrow{\ d\ }\Lambda^1(\mathbb R^2)\xrightarrow{\ d\ }\Lambda^2(\mathbb R^2)\xrightarrow{\ d\ }0$$，其中 $$d$$ 是外微分。

**基3.** 求 $$2\times2$$ 实矩阵
$$A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$$
的谱（看作 $$\mathbb C^2$$ 上的算子），并说明它与例 3.3(a) 是同一件事。

### 竞赛（本课目标难度）

**竞1.** （入口题 (iii) 的完整解）设 $$\varphi:A\to B$$ 是交换环同态，$$\mathfrak p\subseteq A$$ 是素理想。
(i) 证明 $$\varphi^{-1}(\mathfrak p)$$ 是 $$B$$ 的素理想；
(ii) 证明 $$\operatorname{Spec}\varphi:\operatorname{Spec} B\to\operatorname{Spec} A,\ \mathfrak p\mapsto\varphi^{-1}(\mathfrak p)$$ 关于 Zariski 拓扑连续；
(iii) 举出一个具体例子说明"同向映射 $$\mathfrak p\mapsto\varphi(\mathfrak p)$$"行不通。

**竞2.** 设 $$C=(C_n,\partial)$$ 是 $$A$$-模链复形，$$M$$ 是 $$A$$-模。令 $$C^n=\operatorname{Hom}_A(C_n,M)$$，
$$(\delta^nf)(c)=f(\partial_{n+1}c)\qquad(f\in C^n,\ c\in C_{n+1}).$$
(i) 证明 $$\delta^{n+1}\delta^n=0$$，故可定义 $$H^n(C;M)=\ker\delta^n/\operatorname{im}\delta^{n-1}$$；
(ii) 证明：链映射 $$g:C\to D$$ 诱导出**反向**的 $$H^n(g):H^n(D;M)\to H^n(C;M)$$，且 $$H^n$$ 是反变函子。

**竞3.** 设 $$\zeta_5=e^{2\pi\mathrm i/5}$$，$$K=\mathbb Q(\zeta_5)$$。求出 $$\operatorname{Gal}(K/\mathbb Q)$$、它的全部子群与全部中间域，并指出唯一的二次中间域。

**竞4.** 设 $$S$$ 是 $$\ell^2(\mathbb Z)$$ 上的**双边移位**：$$(Sx)_n=x_{n-1}$$。证明 $$\sigma(S)=\{\lambda\in\mathbb C:\lvert\lambda\rvert=1\}$$。

### 研究（通向新的方向）

**研1.** 把地图一的六步写成一张交换图并验证它交换。定义函子上的"对偶化"运算 $$(-)^{\mathrm{op}}$$，证明下面的方块交换：
$$\begin{array}{ccc}\mathcal C & \xrightarrow{\ F\ } & \mathcal D\\ \downarrow & & \downarrow\\ \mathcal C^{\mathrm{op}} & \xrightarrow{\ F^{\mathrm{op}}\ } & \mathcal D^{\mathrm{op}}\end{array}$$
并说明 $$(-)^{\mathrm{op}}\circ(-)^{\mathrm{op}}=\mathrm{id}$$。再用它解释两件事：(a) 为什么 $$V\mapsto V^{**}$$ 是自然同构，而 $$V\mapsto V^{*}$$ 不是；(b) 地图一里哪几步是"反变等价"（Spec、Gelfand），哪一步只是"自然的同构"（Riesz）。

**研2.** 用"两副面孔"造一个新例子：在 $$A=\Lambda^\bullet\mathbb R$$（基 $$1,dx$$）上定义两个线性算子
$$\varepsilon(\omega)=\omega\wedge dx,\qquad \iota(a+b\,dx)=b.$$
(i) 证明 $$\varepsilon^2=0$$、$$\iota^2=0$$、$$\varepsilon\iota+\iota\varepsilon=\mathrm{id}$$；
(ii) 由此证明 $$(\varepsilon+\iota)^2=\mathrm{id}$$，即 $$\varepsilon+\iota$$ 是一个"平方等于 1"的元素；
(iii) 说明这里同时出现了第 07 章的 $$v^2=0$$ 与第 29 章的 $$v^2=q(v)$$，并指出它与第 22 章正则对易关系的同异。

### 解答 (Solutions)

**解 基1.** 定义（定义 3.1）：(1) $$\operatorname{Ob}(\mathcal C^{\mathrm{op}})=\operatorname{Ob}(\mathcal C)$$；(2) $$\operatorname{Hom}_{\mathcal C^{\mathrm{op}}}(X,Y)=\operatorname{Hom}_{\mathcal C}(Y,X)$$；(3) 若 $$f\in\operatorname{Hom}_{\mathcal C^{\mathrm{op}}}(X,Y)$$、$$g\in\operatorname{Hom}_{\mathcal C^{\mathrm{op}}}(Y,Z)$$，则 $$g\circ^{\mathrm{op}}f=f\circ g$$；(4) $$1_X^{\mathrm{op}}=1_X$$。

验证 $$(\mathcal C^{\mathrm{op}})^{\mathrm{op}}=\mathcal C$$，逐条来：
(1) $$\operatorname{Ob}((\mathcal C^{\mathrm{op}})^{\mathrm{op}})=\operatorname{Ob}(\mathcal C^{\mathrm{op}})=\operatorname{Ob}(\mathcal C)$$。
(2) $$\operatorname{Hom}_{(\mathcal C^{\mathrm{op}})^{\mathrm{op}}}(X,Y)=\operatorname{Hom}_{\mathcal C^{\mathrm{op}}}(Y,X)=\operatorname{Hom}_{\mathcal C}(X,Y)$$——掉了两次头，回到原方向。
(3) 设 $$f\in\operatorname{Hom}_{\mathcal C}(X,Y)$$、$$g\in\operatorname{Hom}_{\mathcal C}(Y,Z)$$。在 $$(\mathcal C^{\mathrm{op}})^{\mathrm{op}}$$ 中的复合是 $$\mathcal C^{\mathrm{op}}$$ 中复合的镜像，即
$$g\circ^{\mathrm{op,op}}f=f\circ^{\mathrm{op}}g=g\circ f$$
（最后一步用 $$\mathcal C^{\mathrm{op}}$$ 中 $$f\circ^{\mathrm{op}}g$$ 的定义）。
(4) 恒等始终不变。
四条逐一相等，故两个范畴**逐字相同**（不只是同构）。

定理 3.1 说：对任何陈述 $$S$$，"$$S$$ 在 $$\mathcal C$$ 中成立 $$\iff$$ $$S^{\mathrm{op}}$$ 在 $$\mathcal C^{\mathrm{op}}$$ 中成立"。取 $$S$$ = "$$\mathcal C$$ 中存在 $$X,Y$$ 的积"，则 $$S^{\mathrm{op}}$$ 就是"$$\mathcal C^{\mathrm{op}}$$ 中存在 $$X,Y$$ 的余积"。于是"存在 $$\mathcal C$$ 的积"这一结论对所有范畴成立时，"存在余积"也自动对所有范畴成立——因为 $$S$$ 的证明掉头后就是 $$S^{\mathrm{op}}$$ 的证明，而"$$\mathcal C$$ 任取"与"$$\mathcal C^{\mathrm{op}}$$ 任取"是同一件事。所以不必重证。$$\blacksquare$$

**解 基2.**
(a) **是链复形**。检验复合为零：$$\pi\circ(\times2)(n)=\pi(2n)=0\pmod 2$$，故 $$\partial^2=0$$。同调：记下标使 $$C_1=\mathbb Z\xrightarrow{\times2}C_0=\mathbb Z\xrightarrow{\pi}C_{-1}=\mathbb Z/2$$，
$$H_1=\ker(\times2)/\operatorname{im}(0\to\mathbb Z)=0/0=0,\qquad H_0=\ker\pi/\operatorname{im}(\times2)=2\mathbb Z/2\mathbb Z=0,$$
$$H_{-1}=\ker(\mathbb Z/2\to0)/\operatorname{im}\pi=(\mathbb Z/2)/(\mathbb Z/2)=0,\qquad H_2=0.$$
全部为零：这个复形**正合**。（它的正合性正是 $$0\to\mathbb Z\to\mathbb Z\to\mathbb Z/2\to0$$ 是短正合列的意思。）

(b) **不是链复形**。要检验的是 $$\pi_4\circ(\times2)=0$$：取 $$n=1$$，$$\pi_4(2\cdot1)=\pi_4(2)=2\not\equiv0\pmod4$$。故复合不为零，谈不上同调。

(c) **是链复形**。外微分满足 $$d^2=0$$（第 07、12 章）。这是**上链复形**（$$d$$ 升次），把下标反号即化为链复形（例 3.1(2)）。同调即 de Rham 上同调：
$$H^0=\ker(d:\Lambda^0\to\Lambda^1)=\{\text{常函数}\}\cong\mathbb R;$$
$$H^1=\ker(d:\Lambda^1\to\Lambda^2)/\operatorname{im}(d:\Lambda^0\to\Lambda^1)$$。在 $$\mathbb R^2$$ 上，$$\alpha=P\,dx+Q\,dy$$ 闭（$$d\alpha=0$$）等价于 $$\partial_yP=\partial_xQ$$，而 $$\mathbb R^2$$ 单连通：由
$$f(x,y)=\int_0^xP(t,0)\,dt+\int_0^yQ(x,s)\,ds$$
可验 $$\partial_xf=P$$、$$\partial_yf=Q$$（第二个等式用 $$\partial_xQ=\partial_yP$$ 交换求导次序），故每个闭 1-形式都恰当，$$H^1=0$$；
$$H^2=\ker(d:\Lambda^2\to0)/\operatorname{im}(d:\Lambda^1)=\Lambda^2(\mathbb R^2)/\Lambda^2(\mathbb R^2)=0.$$ $$\blacksquare$$

**解 基3.** 特征多项式
$$\det(\lambda I-A)=\det\begin{pmatrix}\lambda&1\\-1&\lambda\end{pmatrix}=\lambda^2+1,$$
故特征值为 $$\pm\mathrm i$$，即 $$\sigma(A)=\{\mathrm i,-\mathrm i\}$$（$$\mathbb C^2$$ 上的算子）。

与例 3.3(a) 的关系：把 $$\mathbb R^2$$ 与 $$\mathbb C$$ 等同（$$(x,y)\leftrightarrow x+\mathrm iy$$），则 $$A$$ 就是"乘 $$\mathrm i$$"。更明确地，指数映射给出
$$\exp(\theta A)=\sum_{k\ge0}\frac{\theta^kA^k}{k!}=\cos\theta\cdot I+\sin\theta\cdot A=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}=R_\theta,$$
（用了 $$A^2=-I$$，从而 $$A^{2k}=(-1)^kI$$、$$A^{2k+1}=(-1)^kA$$），两端取 $$\theta=0$$ 的导数得 $$\frac{d}{d\theta}\Big\vert_{\theta=0}R_\theta=A$$。所以 $$A$$ 是 $$SO(2)$$ 的 Lie 代数生成元，而 $$R_\theta$$ 的特征值 $$e^{\pm\mathrm i\theta}$$ 就是 $$\exp(\theta\{\pm\mathrm i\})$$——**"求导"把乘 $$\mathrm i$$ 的特征值变成旋转的特征值**。定理 3.3 在此给出 $$\sigma(A)\ne\varnothing$$（有限维情形由代数基本定理保证，与定理 3.3 一致）。$$\blacksquare$$

**解 竞1.**
(i) 记 $$\mathfrak q=\varphi^{-1}(\mathfrak p)$$。先证它是理想：$$0\in\mathfrak q$$ 因为 $$\varphi(0)=0\in\mathfrak p$$；若 $$x,y\in\mathfrak q$$ 则 $$\varphi(x-y)=\varphi(x)-\varphi(y)\in\mathfrak p$$，故 $$x-y\in\mathfrak q$$；若 $$x\in\mathfrak q$$、$$a\in A$$ 则 $$\varphi(ax)=\varphi(a)\varphi(x)\in\mathfrak p$$（$$\mathfrak p$$ 吸收乘法），故 $$ax\in\mathfrak q$$。再证素：$$\mathfrak q\ne A$$（因为 $$1\notin\mathfrak q$$，否则 $$1=\varphi(1)\in\mathfrak p$$）；若 $$xy\in\mathfrak q$$，则
$$\varphi(x)\varphi(y)=\varphi(xy)\in\mathfrak p,$$
由 $$\mathfrak p$$ 素得 $$\varphi(x)\in\mathfrak p$$ 或 $$\varphi(y)\in\mathfrak p$$，即 $$x\in\mathfrak q$$ 或 $$y\in\mathfrak q$$。所以 $$\mathfrak q$$ 是素理想，映射在点集上良定义。

(ii) Zariski 拓扑的闭集是 $$V(\mathfrak a)=\{\mathfrak p\in\operatorname{Spec} A:\mathfrak a\subseteq\mathfrak p\}$$（$$\mathfrak a$$ 取遍 $$A$$ 的理想）。要证连续，只需证每个 $$V(\mathfrak a)$$ 的原像是闭集。计算：
$$(\operatorname{Spec}\varphi)^{-1}\big(V(\mathfrak a)\big)=\{\mathfrak q\in\operatorname{Spec} B:\varphi^{-1}(\mathfrak q)\supseteq\mathfrak a\}=\{\mathfrak q:\varphi(\mathfrak a)\subseteq\mathfrak q\}=V\big(\varphi(\mathfrak a)\cdot B\big).$$
中间那一步是纯逻辑：$$\varphi^{-1}(\mathfrak q)\supseteq\mathfrak a$$ 等价于"对一切 $$x\in\mathfrak a$$，$$\varphi(x)\in\mathfrak q$$"，即 $$\varphi(\mathfrak a)\subseteq\mathfrak q$$。右端是 $$\operatorname{Spec} B$$ 的 Zariski 闭集，故原像闭，$$\operatorname{Spec}\varphi$$ 连续。

(iii) 反例：取 $$\varphi:\mathbb Z\to\mathbb Z[\mathrm i]$$ 为包含，$$\mathfrak p=(2)\subset\mathbb Z$$ 是素理想（$$\mathbb Z/(2)$$ 是域）。同向映射给 $$\varphi((2))=2\mathbb Z[\mathrm i]$$。但
$$2=(1+\mathrm i)(1-\mathrm i),$$
两个因子都不在 $$2\mathbb Z[\mathrm i]$$ 中（$$1+\mathrm i$$ 的实部为 1，不是偶数；也不可能写成 $$2z$$ 的形式），所以 $$2\mathbb Z[\mathrm i]$$ 不是素理想：$$2\mathbb Z[\mathrm i]$$ 的同向像是 $$(1+\mathrm i)^2$$，被平方"退化"了。故 $$\mathfrak p\mapsto\varphi(\mathfrak p)$$ 不能给出从 $$\operatorname{Spec} A$$ 到 $$\operatorname{Spec} B$$ 的映射。

**箭头的方向为什么必须反向**：代数几何的第一字典里，$$A$$ 的元素是 $$\operatorname{Spec} A$$ 上的"函数"。要有函数从 $$\operatorname{Spec} B$$ 到 $$\operatorname{Spec} A$$，就必须把 $$A$$ 的函数**拉回**成 $$B$$ 的函数，而拉回的方式只能是"复合 $$\varphi$$"。所以空间的方向与环的方向天然相反。同样一句话也解释了 (iii) 为什么失败：$$\varphi$$ 只保证"$$A$$ 的函数能拉回"，不能保证"$$A$$ 的素理想能推过去"。$$\blacksquare$$

**解 竞2.**
(i) 对 $$f\in C^n$$ 与 $$c\in C_{n+2}$$，
$$(\delta^{n+1}\delta^nf)(c)=(\delta^nf)(\partial_{n+2}c)=f\big(\partial_{n+1}(\partial_{n+2}c)\big)=f\big((\partial_{n+1}\partial_{n+2})c\big)=f(0)=0,$$
最后一步用了链复形公理 $$\partial^2=0$$。因这对一切 $$c$$ 成立，$$\delta^{n+1}\delta^nf=0$$，即 $$\delta^2=0$$。于是 $$\operatorname{im}\delta^{n-1}\subseteq\ker\delta^n$$，$$H^n(C;M)=\ker\delta^n/\operatorname{im}\delta^{n-1}$$ 有意义。

(ii) 给定链映射 $$g:C\to D$$，即 $$g_n:C_n\to D_n$$ 且 $$d_ng_n=g_{n-1}\partial_n$$。定义
$$g^n:D^n\to C^n,\qquad g^n(\psi)=\psi\circ g_n\quad(\psi\in\operatorname{Hom}_A(D_n,M)).$$
$$g^n$$ 是线性的（复合对第一个变量线性）。它是**上链映射**，即 $$\delta^n_C\circ g^n=g^{n+1}\circ\delta^n_D$$：对 $$\psi\in D^n$$、$$c\in C_{n+1}$$，
$$(\delta^n_Cg^n\psi)(c)=(g^n\psi)(\partial_{n+1}c)=\psi\big(g_n\partial_{n+1}c\big)=\psi\big(d_{n+1}g_{n+1}c\big)=(\delta^n_D\psi)(g_{n+1}c)=(g^{n+1}\delta^n_D\psi)(c),$$
第二步是 $$g^n$$ 的定义，第三步是 $$g$$ 是链映射。故两边的上链映射相等。

把定理 3.2 的证明"逐字掉头"（这正是定理 3.1 的用法）：上链映射 $$g^n:D^\bullet\to C^\bullet$$ 诱导出良定义的
$$H^n(g):H^n(D;M)\to H^n(C;M),\qquad[\psi]\mapsto[g^n\psi].$$
注意方向的翻转：$$g$$ 从 $$C$$ 到 $$D$$，而 $$H^n(g)$$ 从 $$H^n(D)$$ 到 $$H^n(C)$$。函子性同样掉头：若 $$g:C\to D$$、$$h:D\to E$$ 是链映射，则 $$\operatorname{Hom}$$ 上的复合次序反转，
$$H^n(h\circ g)=H^n(g)\circ H^n(h).$$
所以 $$H^n(-;M)$$ 是反变函子。$$\blacksquare$$

> 这就是例 3.1(2) 的内容：**同调协变、上同调反变**，差别只在作用了一次 $$\operatorname{Hom}_A(-,M)$$。

**解 竞3.** 记 $$\zeta=\zeta_5$$。

**第一步：不可约性与次数。** 五次分圆多项式
$$\Phi_5(x)=x^4+x^3+x^2+x+1.$$
作代换 $$x\mapsto x+1$$：由 $$\Phi_5(x)(x-1)=x^5-1$$ 得 $$\Phi_5(x+1)=\frac{(x+1)^5-1}{x}=x^4+5x^3+10x^2+10x+5$$。它的所有非常数系数都被质数 5 整除，常数项 5 不被 25 整除，故由 Eisenstein 判别法（取 $$p=5$$）$$\Phi_5(x+1)$$ 不可约，从而 $$\Phi_5$$ 不可约。于是
$$[K:\mathbb Q]=\deg\Phi_5=4.$$

**第二步：Galois 群。** $$K$$ 是 $$\Phi_5$$ 的分裂域（$$\Phi_5$$ 的根是 $$\zeta,\zeta^2,\zeta^3,\zeta^4$$，都在 $$K$$ 中），故 $$K/\mathbb Q$$ 是 Galois 扩张。$$\mathbb Q$$-自同构由 $$\zeta\mapsto\zeta^k$$ 决定，$$k\in(\mathbb Z/5)^\times=\{1,2,3,4\}$$（自同构把根送到根）。记 $$\sigma_k(\zeta)=\zeta^k$$，则 $$\sigma_k\sigma_l=\sigma_{kl}$$，故
$$G=\operatorname{Gal}(K/\mathbb Q)\cong(\mathbb Z/5)^\times\cong\mathbb Z/4,$$
生成元取 $$\sigma=\sigma_2:\zeta\mapsto\zeta^2$$（模 5 中 $$2$$ 的阶为 $$4$$：$$2,4,3,1$$）。

**第三步：子群。** $$\mathbb Z/4$$ 的子群恰有 3 个：
$$\{1\},\qquad \langle\sigma^2\rangle=\{\mathrm{id},\sigma^2\},\qquad G.$$

**第四步：固定域。** 由定理 3.4 (iii)（反序一一对应），中间域恰有 3 个，且 $$[K^H:\mathbb Q]=[G:H]$$：
- $$H=G$$：$$K^G=\mathbb Q$$；
- $$H=\langle\sigma^2\rangle$$，$$[G:H]=2$$，故 $$[K^H:\mathbb Q]=2$$；
- $$H=\{1\}$$：$$K^{\{1\}}=K$$。

定出 $$K^{\langle\sigma^2\rangle}$$：$$\sigma^2(\zeta)=\zeta^{4}=\zeta^{-1}=\overline{\zeta}$$，即 $$\sigma^2$$ 就是复共轭，故
$$K^{\langle\sigma^2\rangle}=K\cap\mathbb R=\mathbb Q(\zeta+\zeta^{-1}).$$
令 $$u=\zeta+\zeta^{-1}=2\cos\frac{2\pi}{5}$$。由 $$\Phi_5(\zeta)=0$$ 除以 $$\zeta^2$$：
$$\zeta^2+\zeta+1+\zeta^{-1}+\zeta^{-2}=0.$$
用 $$\zeta^2+\zeta^{-2}=u^2-2$$ 代入得
$$(u^2-2)+u+1=0,\qquad\text{即}\qquad u^2+u-1=0.$$
故 $$u=\dfrac{-1\pm\sqrt5}{2}$$；因 $$u=2\cos72^\circ>0$$，取 $$u=\dfrac{\sqrt5-1}{2}$$，于是
$$K^{\langle\sigma^2\rangle}=\mathbb Q(\sqrt5).$$
这正是唯一的二次中间域（$$\mathbb Q(\sqrt5)$$ 由判别式为 5 的二次域给出，与二次域理论一致）。

**对应表：**

| 子群 $$H$$ | 固定域 $$K^H$$ | 扩张次数 |
|---|---|---|
| $$\{1\}$$ | $$\mathbb Q(\zeta_5)=K$$ | 4 |
| $$\langle\sigma^2\rangle$$ | $$\mathbb Q(\sqrt5)$$ | 2 |
| $$G$$ | $$\mathbb Q$$ | 1 |

**一处呼应**：$$\mathbb Q(\zeta_5)$$ 的 Galois 群是 $$\mathbb Z/4$$，它**唯一**的二次商对应唯一的二次子域 $$\mathbb Q(\sqrt5)$$——这不是巧合，而是二次域理论与分圆域理论交接处最早的一条定理（也是类域论的入口，见第 7 节）。$$\blacksquare$$

**解 竞4.** 记 $$S^*=S^{-1}$$：由
$$\langle Sx,y\rangle=\sum_n(Sx)_ny_n=\sum_nx_{n-1}y_n=\sum_mx_my_{m+1}=\langle x,S^{-1}y\rangle$$
得 $$S^*=S^{-1}$$。故 $$S$$ 是酉算子（$$S^*S=SS^*=I$$），$$\lVert S\rVert=\lVert S^{-1}\rVert=1$$。

**第一步：$$\lvert\lambda\rvert\ne1$$ 时 $$\lambda I-S$$ 可逆。**
- 若 $$\lvert\lambda\rvert>1$$：$$\lambda I-S=\lambda\big(I-\lambda^{-1}S\big)$$，而 $$\lVert\lambda^{-1}S\rVert=\lvert\lambda\rvert^{-1}<1$$。Neumann 级数 $$\sum_{k\ge0}(\lambda^{-1}S)^k$$ 绝对收敛，其和为 $$(I-\lambda^{-1}S)^{-1}$$，故
$$(\lambda I-S)^{-1}=\lambda^{-1}\sum_{k\ge0}\lambda^{-k}S^k,\qquad \lVert(\lambda I-S)^{-1}\rVert\le\frac{1}{\lvert\lambda\rvert-1}.$$
- 若 $$\lvert\lambda\rvert<1$$：用法与上面不同，要借 $$S^*=S^{-1}$$：
$$\lambda I-S=-S\big(I-\lambda S^{-1}\big)=-S\big(I-\lambda S^{*}\big),$$
而 $$\lVert\lambda S^*\rVert=\lvert\lambda\rvert<1$$，故 $$\big(I-\lambda S^*\big)^{-1}=\sum_{k\ge0}\lambda^kS^{*k}$$ 收敛，从而
$$(\lambda I-S)^{-1}=-\Big(\sum_{k\ge0}\lambda^kS^{*k}\Big)S^{-1}=-\sum_{k\ge0}\lambda^kS^{-k-1}.$$
（直接代入验证：$$(\lambda I-S)\big(-\sum_{k\ge0}\lambda^kS^{-k-1}\big)=-\sum_{k\ge0}\lambda^{k+1}S^{-k-1}+\sum_{k\ge0}\lambda^kS^{-k}=I$$，因为前一个级数是后一个去掉 $$k=0$$ 项。）
所以 $$\sigma(S)\subseteq\{\lvert\lambda\rvert=1\}$$。

**第二步：$$\lvert\lambda\rvert=1$$ 时不可逆。** 取 $$\lambda$$ 使 $$\lvert\lambda\rvert=1$$，对 $$N\ge1$$ 令
$$x_N=N^{-1/2}\sum_{k=1}^{N}\lambda^{-k}e_k.$$
则 $$\{e_k\}$$ 两两正交，$$\lVert x_N\rVert^2=N^{-1}\cdot N=1$$。注意 $$Se_k=e_{k+1}$$，故
$$\lambda x_N-Sx_N=N^{-1/2}\sum_{k=1}^{N}\lambda^{1-k}e_k-N^{-1/2}\sum_{k=1}^{N}\lambda^{-k}e_{k+1}.$$
右端第二个和是 $$\sum_{j=2}^{N+1}\lambda^{1-j}e_j$$；逐下标相减，$$2\le j\le N$$ 时两个系数恰好相同而抵消，只剩
$$\lambda x_N-Sx_N=N^{-1/2}\big(e_1-\lambda^{-N}e_{N+1}\big),\qquad\lVert\lambda x_N-Sx_N\rVert=N^{-1/2}\sqrt2\longrightarrow0.$$
若 $$\lambda I-S$$ 可逆，则由
$$\lVert x_N\rVert\le\lVert(\lambda I-S)^{-1}\rVert\,\lVert(\lambda I-S)x_N\rVert$$
得 $$\lVert(\lambda I-S)x_N\rVert\ge\lVert(\lambda I-S)^{-1}\rVert^{-1}>0$$，与上式矛盾。故 $$\lambda\notin\rho(S)$$。

**结论**：$$\sigma(S)=\{\lambda\in\mathbb C:\lvert\lambda\rvert=1\}$$。

**三点补充**：(1) 这与定理 3.3 一致（谱非空，且是紧集）；(2) 谱半径恰为 $$1=\lVert S\rVert$$，因为 $$S$$ 酉；(3) 与精讲 3 对照：**同一个答案（单位圆）、两种机制**——精讲 3 靠"函数有无零点"，这里靠"平移不变性与近似特征向量"。$$\blacksquare$$

**解 研1.** **第一步：定义对偶化。** 设 $$F:\mathcal C\to\mathcal D$$ 是协变函子。定义 $$F^{\mathrm{op}}:\mathcal C^{\mathrm{op}}\to\mathcal D^{\mathrm{op}}$$ 如下：对象上 $$F^{\mathrm{op}}(X)=F(X)$$；态射上，若 $$\tilde f\in\operatorname{Hom}_{\mathcal C^{\mathrm{op}}}(X,Y)$$ 对应 $$\mathcal C$$ 中的 $$f:Y\to X$$，则令
$$F^{\mathrm{op}}(\tilde f)=\widetilde{F(f)}\in\operatorname{Hom}_{\mathcal D^{\mathrm{op}}}(FX,FY),$$
即 $$\mathcal D$$ 中的 $$F(f):FY\to FX$$ 所对应的那个态射。验证 $$F^{\mathrm{op}}$$ 是函子：恒等对应恒等；复合方面，$$\mathcal C^{\mathrm{op}}$$ 中 $$\tilde g\circ\tilde f$$ 对应 $$\mathcal C$$ 中的 $$f\circ g$$，而
$$F^{\mathrm{op}}(\tilde g\circ\tilde f)=\widetilde{F(f\circ g)}=\widetilde{F(f)\circ F(g)}=\widetilde{F(g)}\circ^{\mathrm{op}}\widetilde{F(f)}=F^{\mathrm{op}}(\tilde g)\circ^{\mathrm{op}}F^{\mathrm{op}}(\tilde f),$$
（在 $$\mathcal D^{\mathrm{op}}$$ 中 $$\widetilde{\alpha\circ\beta}=\tilde\beta\circ^{\mathrm{op}}\tilde\alpha$$，此处正好用上）。故 $$F^{\mathrm{op}}$$ 是函子。

**第二步：方块交换。** 要验证的图是

$$\begin{array}{ccc}\mathcal C & \xrightarrow{\ F\ } & \mathcal D\\ \downarrow & & \downarrow\\ \mathcal C^{\mathrm{op}} & \xrightarrow{\ F^{\mathrm{op}}\ } & \mathcal D^{\mathrm{op}}\end{array}$$

其中四条边是：上边 $$F$$，左右两边是"取对偶范畴"的恒等函子（对象不动、态射掉头），下边 $$F^{\mathrm{op}}$$。按定义，从左上角走"先下、再右"：对象 $$X\mapsto X\mapsto F(X)$$；态射 $$f\mapsto\tilde f\mapsto F^{\mathrm{op}}(\tilde f)=\widetilde{F(f)}$$。走"先右、再下"：对象 $$X\mapsto F(X)\mapsto F(X)$$；态射 $$f\mapsto F(f)\mapsto\widetilde{F(f)}$$。两条路径在对象与态射上**逐字相同**，故方块严格交换（不需要自然同构）。

**第三步：平方等于恒等。** 对 $$F:\mathcal C\to\mathcal D$$，把上述构造用两次：$$(F^{\mathrm{op}})^{\mathrm{op}}:\mathcal C\to\mathcal D$$，对象 $$X\mapsto F(X)$$，态射 $$f\mapsto F(f)$$——就是 $$F$$ 本身。故 $$(-)^{\mathrm{op}}\circ(-)^{\mathrm{op}}=\mathrm{id}$$。

**第四步：用它解释六步。**

**(a) 为什么 $$V\mapsto V^{**}$$ 自然、$$V\mapsto V^*$$ 不自然。** 取 $$\mathcal C=\mathcal D=\mathbf{Vect}_k^{\mathrm{fin}}$$，$$F=\operatorname{Hom}_k(-,k)$$。注意 $$F$$ 本身就是**反变**的，即它是 $$(\mathbf{Vect}^{\mathrm{fin}})^{\mathrm{op}}\to\mathbf{Vect}^{\mathrm{fin}}$$ 的协变函子；把它写成 $$F:\mathcal D^{\mathrm{op}}\to\mathcal D$$ 的形式，再由第二步的方块，**再作用一次就是回到原方向**——这就是 $$V^{**}=F^{\mathrm{op}}(F(V))$$ 协变的原因。具体验证自然性：定义 $$\iota_V:V\to V^{**}$$，$$(\iota_Vv)(\varphi)=\varphi(v)$$。对任意线性映射 $$f:V\to W$$、$$\varphi\in W^*$$、$$v\in V$$，
$$\big(f^{**}\iota_Vv\big)(\varphi)=(\iota_Vv)(f^*\varphi)=(f^*\varphi)(v)=\varphi\big(f(v)\big)=\big(\iota_Wf(v)\big)(\varphi),$$
故 $$f^{**}\circ\iota_V=\iota_W\circ f$$：方块交换，$$\iota$$ 是自然变换；$$\dim V<\infty$$ 时它还是同构（$$\dim V^{**}=\dim V$$，且核为零：若 $$\iota_Vv=0$$ 则对一切 $$\varphi$$ 有 $$\varphi(v)=0$$，Hahn–Banach 给出 $$v=0$$）。

反过来，若 $$\{\alpha_V:V\to V^*\}$$ 是自然同构，取 $$V=k^2$$、$$f=\mathrm{diag}(1,2)$$。自然性给出 $$\alpha_Vf=(f^{*})^{-1}\alpha_V$$，即 $$\alpha_Vf\alpha_V^{-1}=(f^*)^{-1}=\mathrm{diag}(1,\tfrac12)$$（$$f$$ 对称，故 $$f^*=f$$，其逆为 $$\mathrm{diag}(1,\tfrac12)$$）。相似矩阵有相同的特征值集合，于是 $$\{1,2\}=\{1,\tfrac12\}$$，矛盾。故不存在自然同构 $$V\cong V^*$$——**这正是入口题 (ii) 的答案**。

**(b) 六步里各步的性质。**
- $$\operatorname{Spec}$$：它给出范畴**反等价** $$(\mathbf{AffSch})^{\mathrm{op}}\simeq\mathbf{CRing}$$——是等价，不只是函子；
- Gelfand 谱：给出范畴**反等价** $$(\text{紧 Hausdorff 空间})^{\mathrm{op}}\simeq(\text{交换单位 }C^*\text{-代数})$$；
- Riesz：给出**自然同构** $$H\cong H^*$$（反线性），是同一个函子与自身的自然同构，不是范畴等价；
- $$V\mapsto V^*$$、$$\mathcal C\mapsto\mathcal C^{\mathrm{op}}$$、$$\check H^\bullet$$ 三步只是反变函子，没有逆。

所以"六步是同一个构造"的精确含义是：**它们都是 $$(\mathcal C)^{\mathrm{op}}$$ 这一个构造的实例**，其中 Spec 与 Gelfand 两步更进一步，升格为反等价。**新的方向**：把"反等价"当研究对象，就得到 Gelfand 对偶与概形理论背后的统一语言——**拓扑斯与层论的对偶**，那是代数几何与数论在现代的交汇处。$$\blacksquare$$

**解 研2.**
(i) $$\Lambda^\bullet\mathbb R$$ 只有两部分：$$\Lambda^0=\mathbb R\cdot1$$、$$\Lambda^1=\mathbb R\cdot dx$$。取 $$\omega=a+b\,dx$$（$$a,b\in\mathbb R$$）。
**$$\varepsilon^2=0$$**：$$\varepsilon(\omega)=\omega\wedge dx=(a+b\,dx)\wedge dx=a\,dx+b\,dx\wedge dx=adx$$（用 $$dx\wedge dx=0$$，即第 07 章的反对称）。再作用一次：$$\varepsilon(adx)=a\,dx\wedge dx=0$$。
**$$\iota^2=0$$**：由定义 $$\iota(a+b\,dx)=b\in\Lambda^0$$，再作用 $$\iota(b)=0$$（$$\iota$$ 把常值部分送到 $$0$$）。
**$$\varepsilon\iota+\iota\varepsilon=\mathrm{id}$$**：
$$\varepsilon\iota(\omega)=\varepsilon(b)=b\,dx,\qquad\iota\varepsilon(\omega)=\iota(a\,dx)=a,$$
相加得 $$a+b\,dx=\omega$$。

(ii) 直接展开，并用 $$\varepsilon^2=\iota^2=0$$：
$$(\varepsilon+\iota)^2=\varepsilon^2+\varepsilon\iota+\iota\varepsilon+\iota^2=0+(\varepsilon\iota+\iota\varepsilon)+0=\mathrm{id}.$$
（复合是线性的，故可以这样展开。）于是 $$\varepsilon+\iota\in\operatorname{End}(\Lambda^\bullet\mathbb R)$$ 满足 "$$v^2=1$$"。

(iii) **两副面孔在同一空间上同时出现。**
- **第 07 章的那一副**：$$\varepsilon^2=0$$，而 $$\varepsilon$$ 就是"乘 $$dx$$"。子代数 $$\mathbb R[\varepsilon]/(\varepsilon^2)$$ 是外代数 $$\Lambda^\bullet(\mathbb R)$$ 里"生成元平方为零"的完整写照：$$v\wedge v=0$$。
- **第 29 章的那一副**：令 $$v=\varepsilon+\iota$$，则 $$v^2=\mathrm{id}=q(v)\cdot1$$，其中 $$q$$ 取"标准"二次型 $$q(t)=t^2$$。所以 $$v$$ 是 $$\operatorname{Cl}(\mathbb R,1)$$ 的生成元，而 $$v=\varepsilon+\iota$$ 是把这个 Clifford 代数**实现**在 $$\Lambda^\bullet\mathbb R$$ 上的方式（这就是"用外代数构造旋量表示"的最小模型）。
- **与第 22 章的同异**：第 22 章的正则对易关系是 $$[p,q]=\mathrm i\hbar$$——两个算子的**对易子**是单位；这里的 $$\varepsilon,\iota$$ 满足**反对易**关系 $$\varepsilon\iota+\iota\varepsilon=\mathrm{id}$$。两者都是"两个算子给出单位"，差别只在符号：**对易 = 玻色子（对称代数）**，**反对易 = 费米子（外代数 / Clifford 代数）**。把符号改成 $$q$$-变形，二者被同一条公式统一：$$vw\pm wv=(\cdots)$$。

**接着往哪走**：把"奇算子 + 偶算子 + 反对易"当成公理，就得到**超代数 (superalgebra)** 与超对称的数学框架；把上面这个 $$\mathbb R^2$$ 换成一般流形上的 $$\Omega^\bullet(M)$$，$$d=\varepsilon+\iota$$ 型的分解就是 Hodge 理论与指标定理的起点。这正是下一站：第 7 节说的"拓扑/K 理论入口"。$$\blacksquare$$

## 七、Takeaway 与延伸 (Takeaways)

### 给读者的一封信

你已经走完了 40 章。

第 01 章开始时，你手里只有 $$\mathbb C$$ 和 Euler 公式。第 39 章结束时，你手里有：流形与层、同调与上同调、Hilbert 空间与谱定理、Lie 代数与根系、范畴与导出函子、Galois 对应。这些不是"读过"的东西，而是**四十次从一道具体问题里把它长出来**的东西——这就是这本书与一般教材最大的不同：你没有先背定义，你是先被一道题卡住，才被迫发明定义。

**这本书教了四件事。**

1. **一套语言，而不是一堆定理。** 全书真正反复使用的词只有几个：对偶、函子、正合、谱、表示、度。定理会忘，语言不会——将来你读到任何一门数学，第一件事都是问"它的对象是什么、态射是什么、不变量是哪个函子"。
2. **找不变量的条件反射。** 遇到一个新对象，先问"什么在变形下不变"。同调度量"闭链不等于边界"，谱度量"算子可不可逆"，Chern 类度量"丛扭不扭得过来"，类数度量"理想分解离主理想有多远"。**同一个动作，四十个化身。**
3. **一个换算准则：先算最小的非平凡例子。** 全书每一条主线都能在 $$S^1$$、$$\mathbb C[x]/(x^2)$$、$$\mathbb Q(\sqrt2,\sqrt3)$$ 这种最小的例子上完整跑一遍（第 4、5 节就是这么做的）。以后你遇到不认识的构造，先找它的 $$S^1$$。
4. **一张地图（本章第 4 节）。** 四条主线——对偶与反变、$$D^2=0$$ 的两副面孔、谱与表示、几何—物理—代数三角——比任何单条定理都值得记住。它们是这门课真正的"知识"。

**你现在能做什么。** 你能读懂研究生教材的第一章；能把"某某不变量是什么"翻译成"哪个函子的什么性质"；能在遇到一个陌生结构时，先在 $$\mathbb Q$$、$$k[x]$$、$$S^1$$ 上把它算一遍；能自己判断一条定理的证明是否"跳步"。这些比记住多少定理重要得多。

**下一步读什么。** 不要从最厚的书开始。走完本书的路，自然的下一站是"一门具体的现代学科，从头到尾读一本"——下面四个入口，选一个你看着最顺眼的，把它读到底。

### 下一站：四个入口

**一、代数几何：概形上同调、层论、$$\ell$$-进上同调。**
你已经有了两件工具：层的语言（第 36 章）与导出函子（第 35 章）。把它们合起来就是**概形上同调** $$H^i(X,\mathcal F)$$——整体截面函子的右导出函子，第 37 章那台"粘合障碍计量器"的一般版本。它的第一组定理（Serre 对偶、Riemann–Roch）就把曲线论的全部古典结果收成推论；而为了给有限域上的概形配上"正确的"上同调（让它带上 Galois 作用），Grothendieck 造出了 $$\ell$$-进上同调——**这就是 Weil 猜想的证明路线，也是第 38、39 章的 Galois 群第一次真正用上同调的方式出场。**

**二、数论：类域论、模形式、Langlands 纲领。**
第 38 章已经让你见过数域的算术：范围是 $$K/\mathbb Q$$ 的扩张被 Galois 群控制。**类域论**说：$$\mathbb Q$$ 的**阿贝尔**扩张全都被"模某个整数"描述——你在竞赛 3 里算出的 $$\mathbb Q(\sqrt5)\subset\mathbb Q(\zeta_5)$$ 就是这条定理最小的例子。**模形式**是把这件事搬进分析：上半平面上的全纯函数、Hecke 算子、L 函数，它们把算术信息编码成解析对象（第 38、39 章的知识在这里与解析数论的 zeta、L 函数接上）。**Langlands 纲领**猜想：一切 Galois 表示都来自自守表示——即"算术"与"分析"这两个世界是同一件事的两副面孔。这是当代数学最大的未解纲领之一，而它的语言你已经具备。

**三、表示论：最高权分类、Kazhdan–Lusztig。**
第 28 章的根系已经把复半单 Lie 代数的不可约表示**组合地**分类完（最高权）。下一步是把这个分类做成范畴：BGG 范畴 $$\mathcal O$$ 里的对象（Verma 模及其合成因子）有精确的**对偶性**，Kazhdan–Lusztig 猜想把它的基与 Hecke 代数的基联系起来——它同时用到了第 28 章的根系、第 30 章的射影表示、第 35 章的导出函子，以及第 39 章的 Galois 味思想（Dynkin 图的自同构）。**这是本书四条主线最后汇聚得最密的一处。**

**四、拓扑与 K 理论：特征类、指标定理。**
第 37 章结束时你手上有一个"用向量丛做的广义上同调理论"的雏形：Grothendieck 群 $$K(X)$$、Bott 周期、Chern 特征标。往下走一步就是**特征类**——给每个丛配一个上同调类，度量它的"扭"，并由此得到 Poincaré–Hopf、Gauss–Bonnet 这类"局部的曲率积出整体的拓扑数"的定理。顶点是 **Atiyah–Singer 指标定理**：椭圆算子的解析指标（解空间的维数差）等于纯拓扑的指标（用 Chern 特征标与 Todd 类算出）。**这是"分析 ↔ 拓扑"的最强定理，也是本书"几何 ↔ 物理 ↔ 代数三角"的最后一个榜样。**

### 延伸阅读（按入口分组，每条只给一本起点）

- **代数几何**：Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*（自由讲义，最接近本书的口吻：从问题里长出定义）；工具书用 Hartshorne, *Algebraic Geometry*, GTM 52。
- **数论**：J. S. Milne, *Algebraic Number Theory*（自由讲义）；要直接看纲领，读 S. Gelbart, *An Elementary Introduction to the Langlands Program*（BAMS 10 (1984)）。
- **表示论**：J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, GTM 9；进阶读 Humphreys, *Representations of Semisimple Lie Algebras in the BGG Category O*, GSM 94。
- **拓扑与 K 理论**：Allen Hatcher, *Vector Bundles and K-Theory*（自由 PDF，与本课程第 37 章同一来源）；指标定理读 M. Atiyah, *K-Theory* 或 N. Berline, E. Getzler, M. Vergne, *Heat Kernels and Dirac Operators*。
- **回来读的一本**：Michael Atiyah, *The Geometry and Physics of Knots*（用物理直觉讲拓扑不变量，是本课程"三角"精神的最好示范）。

### 最后一段

本书从 $$\mathbb C$$ 走到 Galois，中间绕过四十个弯。**没有哪一步是必需的**——它们只是同一个冲动在四十个场合的四十次表现：**把看不见的东西，换成一个能算的东西。** 你在第 01 章学会把旋转换成乘法，在第 09 章学会把"洞"换成商群，在第 36 章学会把几何换成环，在第 39 章学会把扩张换成群。这条线索不会在第 40 章结束，它只是换了一本书继续。

祝你在下一本书里，还能听见问题被卡住的那一声脆响。

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch39_Galois群与Galois对应.md">← 第39章 Galois 群与 Galois 对应</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div></div>
</div>
