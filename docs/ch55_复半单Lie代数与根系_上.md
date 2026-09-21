---
layout: default
---

# 第55章: 复半单 Lie 代数与根系·上：预备与直觉 (Complex Semisimple Lie Algebras and Root Systems · Part I: Warm-up and Intuition)

> 配套深化: 见 第56章 复半单 Lie 代数与根系·下（完整推导），本章是它的具体铺垫，建议先读本章
> 对应原专栏: MP73
> 专家依据: `_experts/algebra/lie-algebra-root-systems.md`（主，主场）+ `_experts/algebra/_SKILL.md`
> 知识库依据: `opc2/knowledge/math/李代数/`（15 篇）
> 深度锚: 对标俄罗斯物理数学高中（СУНЦ МГУ 级）

## 一、本章概要 (Overview)

本章要为第56章里四个"跳步"最凶的地方做准备。第一处：$$\mathfrak{sl}(2,\mathbb C)$$ 有限维不可约表示由一个非负整数决定这件事，第56章只用几行抽象记号 $$v_k=F^kv$$ 完成，本章先在一个具体的三维表示里把每一步拆开手算。第二处：Killing 型 $$\kappa(x,y)=\operatorname{tr}(\operatorname{ad}x\operatorname{ad}y)$$ 与 Cartan 判据看起来像凭空冒出的定义，本章先在两个最小的例子（$$\mathfrak{sl}(2,\mathbb C)$$ 与一个二维可解代数）里把 $$2\times2$$ 的 $$\operatorname{ad}$$ 矩阵乘出来、算出行列式，让读者亲眼看到"半单 $$\iff\kappa$$ 非退化"这句话背后是什么。第三处：根空间分解 $$L=H\oplus\bigoplus_\alpha L_\alpha$$ 第一次出现时是一句抽象陈述，本章直接在 $$\mathfrak{sl}(3,\mathbb C)$$ 里对角化两个具体的 $$\operatorname{ad}h$$，把"根"从符号变成一对具体数字。第四处：第56章 定理 3.29 里"夹角只有七种"用到一对 Cartan 整数 $$\langle\beta,\alpha\rangle,\langle\alpha,\beta\rangle$$，长根短根到底谁配到哪个数值，是全书最容易记反符号的地方之一，本章用一对不等长的平面向量把公式代入算一遍，把这件事钉死。

读完本章，你应该已经能：徒手算出 $$\mathfrak{sl}(2,\mathbb C)$$ 小维数表示的权链、徒手判定一个小代数是否半单、徒手写出 $$\mathfrak{sl}(3,\mathbb C)$$ 的全部根、徒手算对一对不等长根的 Cartan 整数。第56章要做的，只是把这四件事从"算过的例子"升级为"对任意半单 Lie 代数、任意维数都成立"的一般定理。

## 二、入口：一道具体的问题 (Entry Problem)

**(i) 热身：把 $$2\times2$$ 矩阵的换位子算一遍。** 取

$$E=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad F=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad H=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

直接算 $$[H,E]$$、$$[H,F]$$、$$[E,F]$$（三次 $$2\times2$$ 矩阵乘法即可，不需要任何理论）。

**(ii) 猜规律：一个三维的例子。** 假设有另一组作用在三维空间 $$V=\operatorname{span}\{v_0,v_1,v_2\}$$ 上的算子 $$E,F,H$$（同一套记号，不同的表示），满足

$$Hv_0=2v_0,\quad Fv_0=v_1,\quad Fv_1=v_2,\quad Fv_2=0,\quad Ev_0=0 .$$

只用 $$[H,F]=-2F$$（(i) 里已经算出）与上面五条关系，能不能不做任何一般证明，就**算出** $$Hv_1,\ Hv_2,\ Ev_1,\ Ev_2$$ 具体是多少？（提示：$$H(Fv_0)=(HF)v_0=(FH-2F)v_0$$。）先猜出数字，答案与验证在 三.1 节给出。

**(iii) 猜形状：$$\mathfrak{sl}(3,\mathbb C)$$ 里的六个数。** 取 $$3\times3$$ 迹零矩阵构成的空间 $$L=\mathfrak{sl}(3,\mathbb C)$$，取对角矩阵 $$h_1=\operatorname{diag}(1,0,-1)$$，取矩阵单位 $$E_{12},E_{13},E_{23},E_{21},E_{31},E_{32}$$（即第 $$i$$ 行第 $$j$$ 列为 $$1$$、其余为 $$0$$ 的矩阵）。直接算 $$[h_1,E_{ij}]$$（$$6$$ 次矩阵乘法），把结果写成 $$[h_1,E_{ij}]=c_{ij}E_{ij}$$ 的形式，列出六个数 $$c_{ij}$$。你会发现有些 $$c_{ij}$$ 重复——这说明只用一个 $$h_1$$ 分不清六个方向。三.3 节会加入第二个对角矩阵 $$h_2$$，把六个方向**完全**分开。

**本题的地位**：(i) 是全部计算的起点；(ii) 预演第56章 入口题(iii) 的权链公式；(iii) 预演第56章 定理 3.22 的根空间分解——本章结束时你会亲手算出这两件事的答案，第56章只是把"算过的例子"写成对任意维数都成立的定理。

## 三、结构：定义与完整推导 (Structure & Proof)

（待填：这是本章主体。用 2–3 个具体数字例子先手算一遍，再抽象出一般定义；把第56章里压缩的推导步骤拆开、补齐中间步骤，讲清楚"为什么会这样想"。不跳步、不手挥。）

## 四、几何与物理直觉 (Intuition)

（待填：更简单、更贴近日常经验的类比；为第56章的几何/物理直觉做准备。）

## 五、经典问题精讲 (Classical Problems)

（待填：2–4 道比第56章更基础的例题，逐题给完整解，为下一章的经典题打地基。）

## 六、练习 (Exercises)
### 基础（巩固定义）


### 竞赛（本课目标难度）


### 研究（通向下一章）


### 解答 (Solutions)


## 七、Takeaway 与延伸 (Takeaways)

（待填：3–5 条核心洞察；明确交棒给第56章——"现在你已经有了直觉和具体计算经验，下一章把它变成严格陈述和证明"。）

---

<!-- chapter-nav -->
<div style="display:flex; justify-content:space-between; align-items:center; padding:1em 0;">
  <div><a href="ch54_Lie代数与指数映射_下.md">← 第54章 Lie 代数与指数映射·下</a></div>
  <div><a href="index.md">↑ 目录</a></div>
  <div><a href="ch56_复半单Lie代数与根系_下.md">第56章 复半单 Lie 代数与根系·下 →</a></div>
</div>
