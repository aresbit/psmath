# 范畴论与普适性质 (Category Theory & Universal Properties)

> **整理自**：Emily Riehl《Category Theory in Context》、Saunders Mac Lane《Categories for the Working Mathematician》(GTM 5)、Tom Leinster《Basic Category Theory》(arXiv:1612.09375)、Bartosz Milewski《Category Theory for Programmers》
> **适用触发词**：范畴、函子、自然变换、自然同构、对偶、始对象、终对象、积、余积、万有性质、极限、余极限、锥、等化子、拉回、推出、完备、伴随、单位、余单位、三角恒等式、自由遗忘、张量-Hom、Yoneda、可表函子、万有元、子对象分类器、幺半范畴

## 0. 一句话定位

范畴论是关于"结构保持的映射"与"映射之间的映射"的抽象语言：对象连同态射打包成范畴，结构保持的构造抽象成函子，构造之间的等价抽象成自然变换。极限是万有构造的一种，伴随是"最接近互逆"的一对函子，Yoneda 引理断言"对象完全由它与其它对象的关系决定"。**理解一个代数对象，不要孤立看它，而要看它与所有对象的态射。**

## 1. 范畴与函子（ch01）

- **范畴** = 对象类 + 态射集 + 满足结合律与单位律的复合。**同构** = 有逆的态射（范畴论里真正算数的相等是同构，不是字面相等）。
- **函子** $$F:\mathcal{C}\to\mathcal{D}$$：映对象、映态射，保持恒等与复合。
- **对偶范畴** $$\mathcal{C}^{\mathrm{op}}$$：反转所有箭头。命题与对偶命题"买一送一"。
- 典型范畴：$$\mathbf{Set}$$、$$\mathbf{Grp}$$、$$\mathbf{Ab}$$、$$\mathbf{Ring}$$、$$R\text{-}\mathbf{Mod}$$、$$\mathbf{Vect}_k$$、$$\mathbf{Pos}$$、$$\mathbf{Top}$$。
- **反变函子** = 到 $$\mathcal{C}^{\mathrm{op}}$$ 的协变函子（如谓词 $$a\to\mathbf{Bool}$$）。**Hom 函子** $$\mathcal{C}(a,-)$$ 协变、$$\mathcal{C}(-,a)$$ 反变，是范畴论的"心脏"（Yoneda、可表函子、伴随全建立在它上面）。

## 2. 自然变换（ch02）

- **自然变换** $$\alpha:F\Rightarrow G$$：一族态射 $$\alpha_c:Fc\to Gc$$ 满足自然性 $$\alpha_d\circ Ff=Gf\circ\alpha_c$$。
- **自然同构**才是范畴论里真正的"相同"：$$V\cong V^{**}$$ 自然，但 $$V\cong V^*$$ 不自然（依赖选基）。
- 函子范畴 $$[\mathcal{C},\mathcal{D}]$$ 的对象是函子、态射是自然变换；自然变换有垂直复合与水平复合。

## 3. 万有性质、极限与余极限（ch03）

- **锥**：到图 $$D:J\to\mathcal{C}$$ 的态射族，满足三角图交换。**极限** = 万有锥（任何其它锥唯一穿过它）；**余极限** = 万有锥的对偶。万有构造在"同构意义下唯一"自动成立。
- **极限特例**：终对象（空图）、**积** $$\prod_j X_j$$、**等化子** $$E=\{x:f(x)=g(x)\}$$、**拉回** $$X\times_ZY=\{(a,b):f(a)=g(b)\}$$（纤维积）。
- **余极限特例**：始对象、**余积**（不相交并 / 直和 / 自由积）、**余等化子**（商 / 轨道集）、**推出**（粘合空间 / 粘合并）。
- **万有性质的三步读法**：先保证任何锥能唯一穿过极限，再保证分解唯一——"存在性 + 唯一性"。
- **完备性**：有所有积与等化子 $$\Rightarrow$$ 有所有极限；对偶地有余积与余等化子 $$\Rightarrow$$ 有所有余极限。$$\mathbf{Set},\mathbf{Grp},\mathbf{Ab},R\text{-}\mathbf{Mod},\mathbf{Top},\mathbf{Pos}$$ 既完备又余完备。
- **Hom 保极限**：$$\mathcal{C}(C,\lim D)\cong\lim_j\mathcal{C}(C,D_j)$$；反变 Hom 把余极限映为极限。这是"极限 = 万有锥"与"右伴随保极限"之间的桥梁。

## 4. 伴随函子（ch04）

- **Hom 集伴随** $$F\dashv G$$：自然同构 $$\mathcal{D}(Fc,d)\cong\mathcal{C}(c,Gd)$$（对 $$c,d$$ 都自然）。
- **单位与余单位**：$$\eta_c:c\to GFc$$，$$\varepsilon_d:FGd\to d$$，满足**三角恒等式** $$(\varepsilon F)\circ(F\eta)=1_F$$、$$(G\varepsilon)\circ(\eta G)=1_G$$。
- **经典伴随对**：

  | 左伴随 $$F$$ | 右伴随 $$G$$ |
  |---|---|
  | 自由 | 遗忘 |
  | 张量积 $$-\otimes_A M$$ | Hom $$\operatorname{Hom}_A(M,-)$$ |
  | 对角 $$\Delta$$ | 极限 $$\lim$$ |
  | 余极限 $$\operatorname{colim}$$ | 对角 $$\Delta$$ |
  | 诱导/标量扩张 | 限制 |

  - **张量-Hom 伴随**：$$\operatorname{Hom}(M\otimes N,P)\cong\operatorname{Hom}(N,\operatorname{Hom}(M,P))$$。
  - **极限作为伴随**：$$\lim\dashv\Delta\dashv\operatorname{colim}$$（极限 = 对角函子的右伴随）。
- **左伴随保余极限、右伴随保极限**：$$F(\operatorname{colim}D)\cong\operatorname{colim}F(D)$$，$$G(\lim D)\cong\lim G(D)$$。推论（判定非伴随）：不保（余）极限的函子不能是左（右）伴随。
- **范畴等价** $$\mathcal{C}\simeq\mathcal{D}$$：存在 $$G$$ 使 $$GF\cong1$$、$$FG\cong1$$（只要求自然同构，不要求严格相等）。例：$$\mathbf{FinVect}_k\simeq\mathbf{Mat}_k$$。

## 5. Yoneda 引理（ch05）

- **可表函子** $$F\cong\mathcal{C}(C,-)$$；$$(C,\eta)$$ 是表示。
- **Yoneda 引理**：$$\operatorname{Nat}(\mathcal{C}(C,-),F)\cong F(C)$$，双射由 $$\alpha\mapsto\alpha_C(1_C)$$ 给出。
- **推论 1（Yoneda 嵌入）**：$$Y:\mathcal{C}^{\mathrm{op}}\to[\mathcal{C},\mathbf{Set}]$$，$$C\mapsto\mathcal{C}(C,-)$$ 是**全忠实**嵌入。
- **推论 2**：$$C\cong D\iff\mathcal{C}(C,-)\cong\mathcal{C}(D,-)$$（**对象由可表函子决定**）。
- **推论 3**：可表函子的表示在同构意义下唯一。
- **推论 4（万有元）**：自然变换 $$\mathcal{C}(C,-)\Rightarrow F$$ 与 $$F(C)$$ 的元素一一对应；是自然同构 $$\iff$$ 对应元素 $$x$$ 满足"对每个 $$y\in F(X)$$ 存在唯一 $$f:C\to X$$ 使 $$Ff(x)=y$$"——**万有元**是最通用元素的精确化。
- **哲学**：**"一个对象完全由它到所有其它对象的态射决定"**。任何局部小范畴都能全忠实嵌入一个完备余完备的预层范畴（完备化标准手段，层论与拓扑斯的起点）。
- **可表视角重解**：$$\mathcal{C}(c,G-)$$ 可表给出右伴随；图的极限可表（表示对象即 $$\lim D$$）；子集函子由**子对象分类器** $$\Omega=\{0,1\}$$ 表示（特征函数 $$\chi_S:X\to\Omega$$）。

## 6. 幺半范畴（ch06，进阶）

- **幺半范畴**：带张量积 $$\otimes$$ 与单位对象 $$I$$，结合与单位只"融贯地"成立（五边形公理 + 三角形公理）。
- **幺半对象**统一了群、环、代数、Hopf 代数等一切"带乘法的结构"。
- **对称 / 辫子幺半范畴**：带交换同构（辫子满足六边形公理）；**融贯定理**保证"一切合理的图都交换"。

## 7. 代数大师的解题清单（范畴侧）

1. **把问题搬到范畴里看普适性质**：不要问"这个对象是什么"，而问"它满足什么万有性质"——凡满足同一万有性质的对象必同构。
2. **构造先试极限/余极限**：积、拉回、等化子（极限）；余积、推出、余等化子（余极限）。要"最通用"用极限，要"最省/最粘合"用余极限。
3. **成对出现的构造先找伴随**：自由-遗忘、张量-Hom、诱导-限制、极限-对角都是伴随对；伴随自动保（余）极限，是最强的结构搬运定理。
4. **要"元素"就用可表函子 + 万有元**：可表函子的表示对象唯一，万有元把"最通用"变成可验证条件。
5. **要证明同构就证明可表函子自然同构**（Yoneda），比直接构造同构往往更省。
6. **同构关不上就看等价**：范畴论里"等价 $\simeq$"而非"同构"才是正确的相同。
