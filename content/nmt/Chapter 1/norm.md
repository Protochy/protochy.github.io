---
title: "Norm"
weight: 2003
description: >
  Generalised length. 
---
<style>
    .inline-header {
        font-size: 1.8em;
        display: inline;
    }
</style>

okOKOK so how do we go about generalising something like the length? well, to recap, the traditional *length* of a vector is usually denoted by $\c{cyan} \large |\vec{x}| = \sqrt{x^2_1 + x^2_2 + \dotsc + x^2_n}$, just good ol' {{<col "cyan">}} Pythagoras {{</col>}}  

cool. now let's define some VERY obvious facts about length.

{{< centr >}}
{{< cbox >}}
<h4> Very obvious facts about length: </h4>


Let's denote the "length" of some vector $\large \c{cyan} \vec{x}$ as $\c{cyan} \large |\vec{x}|$  

1. $\c{orchid} |\vec{x}| \geqslant 0$
obvious, right? How could length be negative. We're realists here! (for now)
    * Actually, $\c{orchid} \vec{x} = \vec{0} \iff | \vec{x} | = 0$, so only the zero vector has magnitude 0.
2. $\c{violet}| \lambda \vec{x} | = \lambda \x | \vec{x} |$ for $\c{violet} \lambda$ a scalar, so we can just pull out any scalar. This also makes sense right? It's just scaling the vector!

3. Choose two arbitrary vectors $\c{magenta} \vec{x}, \vec{y}$, then $\c{magenta} |\vec{x} + \vec{y}| \leqslant |\vec{x}| + |\vec{y}|$ (Triangle Inequality)   
This one is a bit of a pain in the ass but oh well you take the good with the bad.   

Anyway, if a "length" satisfies all these axioms then it's a &nbsp;<span class="inline-header">{{<arcol>}} **norm!** {{</arcol>}}</span>
{{</cbox>}}
{{</centr>}}
<br>
{{<prob 3>}}
Show that the "traditional" length is a norm.
$$\c{cyan} \Large |\vec{x}| = \left(\sum_{i=1}^n x^2_i\right)^{\Large \frac{1}{2}}$$
{{<tip>}}
The "traditional" length is called a Euclidean norm and is represented as $\c{turquoise} \ell^2$
{{</tip>}}
{{<toggle "Show solution" "Hide solution">}}
First two are easy to show so I'll just show tringle inequality. 

show picture for R^2, literally a triangle

Let $\c{lime} \vec{x}, \vec{y}$ be two vectors in $\c{cyan} \mbb{R}^n$, then we have
$$
\large \begin{align*}
 \c{lime} | \vec{x} + \vec{y}| &= \c{orchid} \sqrt{(x_1 + y_1)^2 + (x_2 + y_2)^2 + \dotsc + (x_n + y_n)^2} \\\
 \c{lime} | \vec{x} + \vec{y}|^2 &= \c{orchid} (x_1 + y_1)^2 + (x_2 + y_2)^2 + \dotsc + (x_n + y_n)^2 \\\
  &= \c{orchid} x^2_1 + \dotsc + x^2_n + y^2_1 + \dotsc + y^2_n \c{orange} + 2x_1 y_1 + \dotsc 2x_2 y_2 + \dotsc + 2x_n y_n \\\
  &= \c{orchid} |\vec{x}|^2 + |\vec{y}|^2 \c{orange} + 2 (\vec{x} \x \vec{y})
\end{align*}$$
It's at this point, we acknowledge {{<rcol>}} Cauchy-(Bunyakovsky)-Schwarz {{</rcol>}} exists, i.e.
$$\Large \c{orange} \vec{x} \x \vec{y}  \leqslant \c{orchid} |\vec{x}| |\vec{y}|$$
{{<toggle "Show proof + more info" "Hide proof">}}
You may have seen it as
$$\Large \c{lime} \left(\sum_{i=1}^n a_i b_i \right)^2 \leqslant \c{turquoise} \left(\sum_{i=1}^n x^2_i\right) \left(\sum_{i=1}^n y^2_i\right)$$
later bro
{{</toggle>}}
it's literally a deus ex machina, drops out of the sky to give us exactly what we need. just watch

$$
\large \begin{align*}
\c{lime} | \vec{x} + \vec{y}|^2 &= \c{orchid} |\vec{x}|^2 + |\vec{y}|^2 \c{orange} + 2 (\vec{x} \x \vec{y}) \\\
&\geqslant \c{orchid} |\vec{x}|^2 + |\vec{y}|^2 + 2 |\vec{x}| |\vec{y}| \\\
&\geqslant \c{orchid} \left(|\vec{x}| + |\vec{y}|\right)^2 \\\
\c{lime} | \vec{x} + \vec{y}| &\geqslant  \c{orchid} |\vec{x}| + |\vec{y}|
\end{align*}
$$
<img style="width: 200px" src="https://media.tenor.com/9XyRPn8GZr8AAAAC/quod-erat-demonstrandum-unbelievable.gif">
{{</toggle>}}
{{</prob>}}
{{<divide>}}
### Unit ball
blah blah fill in CONVEXITY gaming shit
{{<divide>}}
### Problems
{{<prob 1>}}
1. Let's define a new notion of length for some vector $\c{cyan} \vec{v} \in \mbb{R}^n$, namely
$$\Large \c{cyan} |\vec{v}| = \sum_{i=1}^n v_i$$
Show that this is **not** a norm.
{{</prob>}}
<br>
{{<prob 2>}}
2. Ok cool, let's try
$$\Large \c{cyan} |\vec{v}| = \sum_{i=1}^n |v_i|$$
Show that this **is** a norm.
{{</prob>}}
<br>
{{<prob 7>}}
3a. Given a sequence of $\c{orange} n$ positive reals $\c{pink} x_1,x_2,\dotsc,x_n$, show that $$\large \c{lime} \left(\sum_{i=1}^n x^m_i\right)^{\large \frac{1}{m}} \to \max(x_1,x_2,\dotsc,x_n) \tu{ as } \c{orange} m \to \infty$$
{{</prob>}}
<br>
{{<prob 3>}}
{{<tip "warn">}}
{{<col "red">}} Problem 3a {{</col>}} must be done first!
{{</tip>}}
3b. Let's define the following as a candidate norm for some vector $\c{cyan} x \in \mbb{R}^n$:
$$\Large \c{cyan} |\vec{x}| = \c{lime} \lim_{m \to \infty} \left(\sum_{i=1}^n x^m_i\right)^{\large \frac{1}{m}}$$
&emsp; &nbsp;Show that this **is** a norm.
{{</prob>}}