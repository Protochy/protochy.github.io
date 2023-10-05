---
title: Norm Sequences
weight: 4005
description: >
  An sequence of norms!
---
coolio. now we move onto sequences of norms. You remember sequences from {{<col "cyan">}} Analysis I {{</col>}} right? {{<kekw>}}  
### Sequence Space
{{<centr>}}
{{<box "#00ffc0">}}
We define the **SEQUENCE** space $\c{lime} \ell^p$ as follows:  
Let $\c{pink} 1 \geqslant p < \infty$, then 
$$\Large \begin{align*}
\c{lime} \ell^p \c{orchid} &\c{orchid} = \left\\{(x_i)_{i=1}^{\infty} \Biggm\vert \left(\sum\_{i=1}^{\infty} |x_i|^p \right)^{\large \f{1}{p}} < \infty \right\\} \\\
\c{lime} \ell^{\infty} &\c{orchid} = \left\\{(x\_i)\_{i=1}^{\infty} \Biggm\vert \sup_i x\_i  \right\\}
\end{align*}
$$
or in other words, the set of all *infinite sequences* with convergent norms. You can think of an *infinite sequence* as an infinite dimensional vector like this:
$$\Large \c{#088F8F} \vec{x} = (x_i)\_{i=1}^{\infty} = \begin{bmatrix} x_1 \\\ x_2 \\\ x_3 \\\ \vdots \end{bmatrix}$$
then apply the standard $\c{lime} \ell^p$ norm to it, and {{< plink href="../norm-families/#normlp" text="we know what that looks like!" >}}
{{<tip>}}
The sequence space $\c{lime} \ell^{\infty}$ is exactly the same as the $\c{lime} \ell^{\infty}$ norm we saw previously, it's just the max over an infinite sequence which has the more precise name of $\sup$remum
{{</tip>}}
{{</box>}}
{{</centr>}}
ok nice, let's get to {{<col "red">}} analysing. {{</col>}}  
<br>
{{<prob 6>}}
Show that $\c{lime} \ell^p$ is a {{<rcol>}} vector space, {{</rcol>}} i.e. it satisfies
* Abelian group under addition {{<col "#00A36C">}} (I'm too lazy to outline the actual axioms so I'll just use non-elementary shorthand) {{</col>}} {{<kekw>}}
* Associativity of scalar multiplication $(\c{violet} a,b \in \mbb{F}, \c{lime} v \in V, \c{violet} (ab) \x \c{lime} v \c{violet} = a(b \x \c{lime} v \c{violet})$\$)$
* Distributivity of scalar multiplication over scalar addition
* Distributivity of scalar multiplication over vector addition
{{<tip>}}
ngl i hate the vector space axioms, even though they make sense. It's just bloody awful showing they hold because half of them reduce to the properties of the fundamental arithmetic operators
{{</tip>}}
{{<toggle "Partial solution" "Hide solution">}}
This is the proof of vector addition being closed (one of the properties of abelian additive groups):

{{<tip>}}
You could also do this with Minkowski's Inequality if you want to!
{{</tip>}}
{{</toggle>}}
{{</prob>}}
ok that was arduous, let's see a very nice result that literally follows from what we already know (my favourite type of result):
{{<centr>}}
{{<box "indigo">}}
{{< plink href="../norm-families/#normminkowski" text="The Minkowski Inequality" >}} for $\c{lime} \ell^p$ sequence spaces:  

It's literally the exact same thing as for regular $\c{lime} \ell^p$ norms  
(but limits are involved as we aren't dealing with finite vector spaces).
$$\Large \c{orchid} \boxed{|\vec{x} + \vec{y}|\_{\c{lime} \ell^p} \leqslant |\vec{x}|\_{\c{lime} \ell^p} + |\vec{y}|\_{\c{lime} \ell^p}}$$
{{<toggle "Quick proof" "Hide proof">}}
Let $\c{lime} x,y \in V$  
We'll split this into two cases, one where $\c{pink} p = \infty$ and $\c{pink} p \in [1,\infty)$:
1. $\c{pink} p = \infty$
$$\large \begin{align*}
\c{lime} |x+y|\_{\ell^{\infty}} &= \c{pink} \max_{i}(|x_i + y_i|) \\\
 &\leqslant \c{pink} \max_{i}(|x_i|) + \max_{j}(|y_j|) \c{lime} \\\
 &\leqslant \c{lime} |x|\_{\ell^{\infty}} + |y|\_{\ell^{\infty}}
\end{align*}$$
2. $\c{pink} p \in [1,\infty)$
boring, will fill out l8er
{{</toggle>}}
{{</box>}}
{{</centr>}}
### <span style="color:rgba(90,160,255,1)">Subspaces</span>
Remember how we talked about {{< plink href="../norm/#normnormedspace" text="normed spaces?" >}} $\c{pink} (V,|\x|)$  

Yep, they come back. Anyway, we see they have the vector space $\c{pink} V$ in them, so it probably will not surprise you in the {{<col "orange">}} fucking slightest {{</col>}} that you can define a subspace for them.
{{<centr>}}
{{<box "magenta">}}
Let $\c{#5AA0FF} W$ be a subspace of $\c{pink} V$, then $\c{#5AA0FF} (W,|\x|)$ is a normed space.  

Some examples!  

* $\c{#FA8072} c_0$, the set of all sequences that converge to $0$, is a *subspace* of $\c{lime} \ell^{\infty}$
* $\c{pink} c_{00}$, the set of all sequences with finitely many nonzero terms (so infinitely many zero terms, a more restrictive version of $\c{#FA8072} c_0$), is a *subspace* of $\c{lime} \ell^{p}$ for all $\c{gold} p \in [1,\infty]$  

kinda boring to prove but whatever
{{</box>}}
{{</centr>}}

### <span style="color:rgba(90,255,160,1)">Continuous spaces</span>
So, you've actually already seen a bit of this before if you tried {{< plink href="../norm-families/#nfctsspace" text="Problem 3." >}}

Anyway let's make it a bit more formal (ew).
{{<centr>}}
{{<cbox>}}
We denote $\c{tan} C([a,b])$ as the space of (real-valued) *continuous* functions on the interval $\c{tan} [a,b]$.  
Pretty simple.  

Anyway, the most common norm ( and the one seen in {{< plink href="../norm-families/#nf4" text="Problem 4." >}}) is the **supremum** (maximum) norm.  
The reason such a norm even works is because continuous functions on a bounded closed interval always have a max (Extreme Value Theorem!)
{{</cbox>}}
{{</centr>}}

### Problems
{{<prob 3>}}
1. Let $\c{pink} (V,|\x|)$ be a normed space. We say that a sequence $\c{lime} (x_n) \in \c{pink} V$ converges in the norm $\c{pink} |\x|$ to $\c{pink} x \in V$ if $$\large \c{gold} \lim_{n \to \infty} |x_n - x| = 0$$
Suppose that $\c{lime} x_n$ converges in the norm $\c{pink} |\x|$ to $\c{pink} x \in V$. Show that $$
\large \c{gold} \lim_{n \to \infty} |x_n| = |x|$$

{{<tip>}}
This is a pretty troll question ngl. {{<kekwait>}}  
It's more of an analysis recap. 
{{</tip>}}
{{<toggle "Hint" "Hide hint">}}
ytilauqenI $\c{pink} \Delta$ esreveR
{{</toggle>}}
{{</prob>}}
<br>
{{<prob 7>}}
2. Show that if $\c{orchid} 1 \leqslant p \leqslant q \leqslant \infty$ then $\c{lime} \ell^p \subseteq \ell^q$ and 
$$\large \c{cyan} |x|\_{\c{lime} \ell^q} \leqslant \c{cyan} |x|\_{\c{lime} \ell^p}$$
for every $\c{cyan} x \in \c{lime} \ell^p$
{{<toggle "Hint" "Hide hint">}}
This one's a doozy. Start simple and assume $\large \c{cyan} x \in \c{lime} \ell^p$ with $\large \c{cyan} |x|\_{\c{lime} \ell^p} \c{cyan} = 1$
{{</toggle>}}
{{</prob>}}
add MORE exercises later, i'm tired {{<kekw>}}