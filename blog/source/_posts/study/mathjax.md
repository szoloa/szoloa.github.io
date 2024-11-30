---
title: Mathjax使用
tags:
  - mathjax
categories: 工具
cover: >-
  https://image.baidu.com/search/down?url=https://wx2.sinaimg.cn/mw690/00817ymegy1he8b39xrcwj32o01o0apu.jpg
top_img: >-
  https://image.baidu.com/search/down?url=https://wx2.sinaimg.cn/mw2000/00817ymegy1he8b39xrcwj32o01o0apu.jpg
description: Mathjax使用
mathjax: true
abbrlink: 18629
---

- 行内公式:使用` $ … $ `定义，此时公式在一行内显示 

## 希腊字母 

| 显示	|命令	|显示	|命令    | 
|----|----|----|----| 
|α | \alpha	|  β	| \beta | 
|γ  | \gamma	| δ |  \delta |
|ϵ |	\epsilon	| ζ |	\zeta |
|η | 	\eta	| θ |	\theta |
|ι  |	\iota|	κ  |	\kappa|
|λ | \lambda |	μ |	\mu|
|ν |	\nu	|ξ |	\xi|
|π |\pi |	ρ |	\rho|
|σ |	\sigma	| τ |	\tau|
|υ |\upsilon |	ϕ |	\phi|
|χ |\chi|	ψ |	\psi|
|ω |	\omega|	—	|—| 

- 如果要大写希腊字母，则首字母大写即可，如\Gamma显示为 $\Gamma$
- 如果要使希腊字母显示为斜体，则前面添加var即可，如\varGamma显示为 $\varGamma$

## 字母修饰
### 上下标
- 上标: ^
- 下标: _

### 矢量
- 单字母向量: 

`\vec a` 显示为 $\vec a$ 
 
`\overrightarrow a` 显示为 $\overrightarrow a$
 
- 多字母向量: 

`\vec {ab}` 显示为 $\vec {ab}$
 
`\overrightarrow {ab}` 显示为 $\overrightarrow {ab}$ 
 
### 特殊修饰
- 字母上^： 

`\hat a` 显示为 $\hat a$
 
- 平均数(上划线): 

`\overline a` 显示为$\overline a$
 
- 下划线: 

`\underline a` 显示为 $\underline a$​
 
### 字体
- TypeWriter: 

	`\mathtt {A}` 显示为 
	
	$\mathtt {ABCDEFGHIJKLMNOPQRSTUVWXYZ}$

- Blackboard blod: 

	`\mathbb {A}` 显示为 
	
	$\mathbb {ABCDEFGHIJKLMNOPQRSTUVWXYZ}$

- Sans Serif: 

	`\mathsf {A}` 显示为 
	
	$\mathsf {ABCDEFGHIJKLMNOPQRSTUVWXYZ}$

### 空格
小空格:a\ b显示为 $a\ b$ 

4格空格:`a\quad b` 显示为 $a\quad b$

### 分组
使用{}将同一级的括在一起，成组处理 

举例: `x_i^2` 显示为 $x_i^2x$​ ，而 `x_{i^2}` 显示为 $x_{i^2}x$ 
 
### 括号
- 小括号: `(...)` 显示为 $( . . . )$ 

- 中括号: `[...]` 显示为 $[ . . . ]$  

- 大括号:`\{...\}` 显示为 $\{...\}$ 

- 尖括号: `\langle ...  \rangle` 显示为 $\langle ...\rangle$ 

- 绝对值: `\vert ... \vert` 显示为 $\vert ... \vert$ 

- 双竖线: `\Vert ... \Vert` 显示为 $\Vert ... \Vert$ 

- 使用`\lvert`和`\rvert`显示绝对值 
例如： 

`\{\frac{(x+y)}{[\alpha+\beta]}\}`显示为 $\{\frac{(x+y)}{[\alpha+\beta]}\}$ 

`lvert\{\frac{(x+y)}{[\alpha+\beta]}\rvert\}` 显示为$\lvert\{\frac{(x+y)}{[\alpha+\beta]}\rvert\}$ 

## 常用数学运算符

想要表达非的概念只需前加`\not`，会添加删除斜线，如: `\not=`显示$\not= ​$,`\not\in`显示$\not\in$

|运算符	|说明	|应用举例	|命令|
|----|---|----|----|
|+	|加	|$x + y$|	x+y|
|-	|减|	$x − y$ |	x-y|
|\times|	叉乘|	$x \times y$ |x \times y|
|\cdot|	点乘|	$x \cdot y$|	x \cdot y|
|\ast(\*)|	星乘|	 $x \ast y$ |x \ast y (x \* y)|
|\div	|除|	$x \div y$ |	x \div y|
|\pm	|加减|	$x \pm y$ |	x \pm y|
|\mp	|减加| $x \mp y$ |	x \mp y|
|=	|等于|	$x=y$|	x=y |
|\leq	|小于等于|	$x \leq y	$|x \leq y|
|\geq	|大于等于|	$x \geq y$	|x \geq y|
|\approx|	约等于|	x ≈ y $x \approx y$	|x \approx y|
|\equiv	|恒等于|	x ≡ y $x \equiv y$	|x \equiv y\
|\bigodot|	定义运算符	x ⨀ y | $x \bigodot y$	|x \bigodot y|
|\bigtimes|	定义运算符	x ⨂ y| $x \bigotimes y$ |x \bigotimes| 

### 集合符号 
|运算符	|说明	|应用举例	|命令|
|-----|-----|-----|------|
|\in	|属于	|$x \in y$ |	x \in y|
|\subset|	子集	|$x \subset y$|x \subset y|
|\subseteq|	真子集	|$x \subseteq y$	|x \subseteq y|
|\supset|	超集	| $x \supset y$	|x \supset y|
|\supseteq	|超集	|$x \supseteq y$	|x \supseteq y|
|\varnothing|	空集	| $\varnothing$	|\varnothing|
|\cup	|并	|$x \cup y$	|x \cup y|
|\cap|	交|	$x \cap y$	|x \cap y|

### 字母修饰
|运算符	|说明	|应用举例	|命令|
|----|-----|-----|-----|
|\overline|平均数(上划线)	|$\overline a$|	\overline a|
|\underline|	下划线|	$\underline a$| 	\underline a|
|\overbrace|	上大括号|	$\overbrace{a+\underbrace{b+c}_{1.0}+d}^{2.0}$|	\overbrace{a+\underbrace{b+c}_{1.0}+d}^{2.0}|
|\underbrace|	下大括号|$\underbrace{a+d}_3$ | 	\underbrace{a+d}_3 |

### 杂项 
|运算符	|说明	|应用举例	|命令|
|----|-----|-----|-----|
|\partial|	偏导数|	$\frac{\partial z}{\partial x}$  |\frac{\partial z}{\partial x}|
|\ldots|	底端对齐的省略号|	$1,2,\ldots,n$ |1,2,\ldots,n|
|\cdots|	中线对齐的省略号|	$1,2,\cdots,n$ | 1,2,\cdots,n|
|\uparrow|	上箭头|	$\uparrow$	|\uparrow|
|\Uparrow|	双上箭头|	$\Uparrow$	|\Uparrow|
|\downarrow|	下箭头|	$\downarrow$	|\downarrow|
|\Downarrow|	双下箭头|	$\Downarrow$	|\Downarrow|
|\leftarrow|	左箭头| $\leftarrow$	|\leftarrow|
|\Leftarrow|	双左箭头|	$\Leftarrow$	|\Leftarrow|
|\rightarrow|	右箭头|	$\rightarrow$	|\rightarrow|
|\Rightarrow|	双右箭头|	$\Rightarrow$	|\Rightarrow |

### 求和、极限与积分
#### 求和
求和符号`\sum`显示为 $\sum$ 

举例: `\sum_{i=0}^n`显示为$\sum_{i=0}^n$ 

举例: `\displaystyle\sum_{i=0}^n2`显示为$\displaystyle\sum_{i=0}^n2$ 
 
#### 极限
极限符号`\lim`显示为 $\lim$ 

举例:`\lim_{x\to\infty}`显示为$\lim_{x\to\infty}$ 
​
举例:`\displaystyle\lim_{x\to\infty}`显示为 $\displaystyle\lim_{x\to\infty}$ 
​
#### 积分
|命令|	显示|
|----|-----|
|\int	|$\int$| 
|\iint	 |$\iint$| 
|\iiint	 |$\iiint$|
|\oint |$\oint$| 

举例: `\int_0^\infty{fxdx}`显示为$\int_0^\infty{fxdx}$ 
​
#### 分式与根式
##### 分式
`\frac{公式1}{公式2}`显示为 $\frac{公式1}{公式2}$ ​
 
举例: $\frac{b_i^2}{a_i^2}$ 
 
##### 根式
`\sqrt[x]{y}`显示为$\sqrt[x]{y}$ 
​
#### 特殊函数
##### \函数名 
举例:\sin x,\ln x,\log_n^2 5,\max(A,B,C)显示为$\sin x$, $\ln x$, $\log_n^2 5$, $\max(A,B,C)$
#### 特殊符号
|命令|	显示|	命令	|显示|
|-----|-----|-----|-----|
|\infty	| ∞	|\partial	|∂|
|\nabla	|∇	|\triangle	|△|
|\forall	|∀	|\exists	|∃|
|\lnot	 | ¬		| --- | --- |

### 矩阵
#### 基本语法
起始标记:`\begin{matrix}`,结束标记:`\end{matrix}` 

每一行末尾标记`\\`，行间元素之间以`&`分隔 

举例:
$$\begin{matrix}
1&0&0\\
0&1&0\\
0&0&1\\
\end{matrix}$$


#### 矩阵边框
在起始、结束标记处用下列词替换matrix 

|类型	|命令	|
|-----|------|
|小括号边框|	pmatrix| 
|中括号边框|	bmatrix| 
|大括号边框|	Bmatrix| 
|单竖线边框|	vmatrix|
|双竖线边框|	Vmatrix| 

### 省略元素
横省略号：`\cdots`
竖省略号：`\vdots`
斜省略号：`\ddots`
举例: 
	$$\begin{bmatrix}
	{a_{11}}&{a_{12}}&{\cdots}&{a_{1n}}\\
	{a_{21}}&{a_{22}}&{\cdots}&{a_{2n}}\\
	{\vdots}&{\vdots}&{\ddots}&{\vdots}\\
	{a_{m1}}&{a_{m2}}&{\cdots}&{a_{mn}}\\
	\end{bmatrix}$$

显示为：

$$\begin{bmatrix}
{a_{11}}&{a_{12}}&{\cdots}&{a_{1n}}\\
{a_{21}}&{a_{22}}&{\cdots}&{a_{2n}}\\
{\vdots}&{\vdots}&{\ddots}&{\vdots}\\
{a_{m1}}&{a_{m2}}&{\cdots}&{a_{mn}}\\
\end{bmatrix}$$

### 阵列
需要`array`环境:起始、结束处以`{array}`声明
对齐方式:在{array}后以{}逐行统一声明
左对齐:l；居中：c；右对齐：r
竖直线:在声明对齐方式时，插入|建立竖直线
插入水平线:`\hline`
举例: 

	$$\begin{array}{c|lll}
	{↓}&{a}&{b}&{c}\\
	\hline
	{R_1}&{c}&{b}&{a}\\
	{R_2}&{b}&{c}&{c}\\
	\end{array}$$

显示为： 

$$\begin{array}{c|lll}
{↓}&{a}&{b}&{c}\\
\hline
{R_1}&{c}&{b}&{a}\\
{R_2}&{b}&{c}&{c}\\
\end{array}$$

### 方程组
需要`cases`环境:起始、结束处以`{cases}`声明
举例:

	$$\begin{cases}
	a_1x+b_1y+c_1z=d_1\\
	a_2x+b_2y+c_2z=d_2\\
	a_3x+b_3y+c_3z=d_3\\
	\end{cases}$$

显示为： 

$$\begin{cases}
a_1x+b_1y+c_1z=d_1\\
a_2x+b_2y+c_2z=d_2\\
a_3x+b_3y+c_3z=d_3\\
\end{cases}$$
