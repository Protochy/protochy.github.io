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

### What is it?
okOKOK so how do we go about generalising something like the length/magnitude? well, to recap, the traditional *length* of a vector is usually denoted by $\c{cyan} \large |\vec{x}| = \sqrt{x^2_1 + x^2_2 + \dotsc + x^2_n}$, just good ol' {{<col "cyan">}} Pythagoras {{</col>}}  

cool. now let's define some VERY obvious facts about length.

{{< centr >}}
{{< cbox >}}
<h4> Very obvious facts about length: </h4>


Let's denote the "length" of some vector $\large \c{cyan} \vec{x}$ as $\c{cyan} \large |\vec{x}|$  

1. {{<col "red">}} *Always nonnegative*: {{</col>}} $\c{orchid} |\vec{x}| \geqslant 0$
obvious, right? How could length be negative. We're realists here! (for now)
    * Actually, $\c{orchid} \vec{x} = \vec{0} \iff | \vec{x} | = 0$, so only the zero vector has magnitude 0.
2. {{<col "red">}} *Scalar pullout*: {{</col>}} $\c{violet}| \lambda \vec{x} | = \lambda \x | \vec{x} |$ for $\c{violet} \lambda$ a scalar, so we can just pull out any scalar. This also makes sense right? It's just scaling the vector!

3. {{<col "red">}} *$\c{pink} \Delta$ inequality*: {{</col>}} Choose two arbitrary vectors $\c{magenta} \vec{x}, \vec{y}$, then $\c{magenta} |\vec{x} + \vec{y}| \leqslant |\vec{x}| + |\vec{y}|$ (Triangle Inequality)   
This one is a bit of a pain in the ass but oh well you take the good with the bad.
<img src="/anim/nmt/ch1/trineq.png" alt="Triangle Inequality Example" width="1280" height="720"> 
{{<tip>}}
the way I intuitively understand the tringle inequality is that it's an effort to make any norm more relatable to the traditional length we are used to, and also maybe because if it doesn't hold some very weird stuff happens {{<kekwait>}}
{{</tip>}}

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
Just to be crystal clear. A {{<arcol>}} norm {{</arcol>}} $\c{orchid}  |\x|$ is a mapping from a vector space $\c{orange} V \c{lime} \to \mbb{R}^+$, as in it takes any vector to a positive real {{<kekw>}} as one would expect length to do.   

we're gonna see a pretty nifty proof soon, but first let's go through one more definition {{<kekwait>}} *<h4> Ahem  </h4>* 

<h3> A normed space is $\c{turquoise} (V,|\x|)$ </h3> 
Yeah, that's all LMAO.
{{<tip>}}
Honestly, I think of {{<col "violet">}} *spaces* {{</col>}} in maths like objects in programming:
```java
NormedSpace normedSpace = new NormedSpace(new RealVectorSpace(dim: n),new EuclideanNorm(dim: n));
{{</tip>}}

In any case we'll be working in a `normed space` pretty much ALWAYS {{<kekw>}}
{{<divide>}}
### Unit ball
Okay so this is actually real simple, imagine the unit circle (and its interior). What is it really?
$$\Large \c{chartreuse} x^2 + y^2 \leqslant 1$$
notice that we are using the "traditional" $\c{cyan} \ell^2$ norm.  

okay thats the equation (or rather inequality), so what's so interesting about it? Well, it has the peculiar property that whenever you draw a line connecting two points on the exterior, that line will always be contained **inside** the circle.   

too many words here's an animation explaining it:
<video width=100% controls> <source src="/anim/nmt/ch1/l2convex.mp4" type="video/mp4">

nice! Now why is this important? {{<col "pink">}} WELL I'm glad you asked {{</col>}} because it turns out

{{<centr>}}
{{<box "teal">}}
<h4> {{<rcol>}}  ALL VALID NORMS preserve this property! {{</rcol>}} </h4> 
{{<tip>}}
This property is called {{<arcol>}} convexity. {{</arcol>}}
{{</tip>}}
Do you believe me?   
<video width=100% controls> <source src="/anim/nmt/ch1/Lp.mp4" type="video/mp4">
{{</box>}}
{{</centr>}}

well tbh it doesn't matter if you don't believe me because we're gonna prove it.
$$\Large \c{violet} \mathfrak{B} = \\{\vec{x} \in X \Biggm\vert |\vec{x}| \leqslant 1\\}$$
i.e. the set of all vectors $\c{orchid} \vec{x}$ that have "length" (i should just start using the word norm) $\c{magenta} \leqslant 1$   

What does it mean to represent a line between two vectors? Well, the idea of {{<rcol>}} linear interpolation {{</rcol>}} comes to mind.  

Say we have two vectors $\c{lime} \vec{x},\vec{y} \in \c{violet} \mathfrak{B}$, then the line segment between $\c{lime} \vec{x}$ and $\c{lime} \vec{y}$ can be represented as 
$$\Large \c{yellow} t\vec{x} + (1-t)\vec{y}$$ for $\c{yellow} t \in [0,1]$  

See for yourself! (few very minor design errors in both videos, fix l8er!)
<video width=100% controls> <source src="/anim/nmt/ch1/LpLI.mp4" type="video/mp4">   

With that out of the way, we proceed to do the thing and show that it works. 
What is it that we want to do? 
{{<prob 5>}}
Show that
$$\Large \c{yellow} t\vec{x} + (1-t)\vec{y} \in \c{orchid} \mathfrak{B}$$
for $\c{lime} \vec{x}, \vec{y} \in \c{orchid} \mathfrak{B}$
{{<tip>}}
Remember that the ONLY criteria to be in $\c{orchid} \mathfrak{B}$ is for the {{<arcol>}} norm {{</arcol>}} $\c{violet} \leqslant 1$!
{{</tip>}}
{{<toggle "Hint" "Hide hint">}}
Use the $\c{pink} \Delta$ {{<col "pink">}} Triangle Inequality! {{</col>}}
Namely, let $\c{orange} \vec{a} := t\vec{x}$ and $\c{orange} \vec{b} := (1-t)\vec{y}$ and use the fact that $$\c{orange} \Large |\vec{a} + \vec{b}| \leqslant |\vec{a}| + |\vec{b}|$$
{{</toggle>}}
{{<toggle "Solution" "Hide solution">}}
Using the hint above, we note that
$$\large \begin{align*}
\c{orange}  |\vec{a} + \vec{b}| &\leqslant \c{orange}  |\vec{a}| + |\vec{b}| \\\
\c{yellow}  |t\vec{x} + (1-t)\vec{y}| &\leqslant \c{yellow} |t|\vec{x}| + |(1-t)\vec{y}| \\\
&= \c{yellow} t|\vec{x}| + (1-t)|\vec{y}| \normalsize\tu{&nbsp;&nbsp;&nbsp;(Using scalar pullout)} \large \\\
&\leqslant \c{lime} t \x 1 + (1-t) \x 1  \normalsize\tu{&nbsp;&nbsp;&nbsp;(Using properties of } \c{orchid} \mathfrak{B} \c{lime} \tu{)}\large\\\
&= \c{cyan} 1
\end{align*}$$
{{</toggle>}}
Remember, wherever we see a $\c{cyan} ||$, that's {{<arcol>}} norm {{</arcol>}} and so our "norm" axioms apply!  
{{</prob>}}

ok, so what? We showed that if a map $\c{pink} ||: V \to \mbb{R}^+$ satisfies the three {{<arcol>}} norm {{</arcol>}} axioms, its unit ball is **convex**. Here's the slick thing: It also holds the *other* way.
{{<centr>}}
{{<box "pink">}}
*Lemma 69.* If a map $\c{pink} ||: V \to \mbb{R}^+$ satisfies the first two {{<arcol>}} norm {{</arcol>}} axioms **AND** its unit ball is **convex**, then it satisfies the triangle inequality and is a norm!  

okay let's get into it. Let's take two arbitrary vectors $\c{lime} \vec{x},\vec{y} \in V$ and consider THIS:  
$$\Large \c{#F49EC4} \begin{align*}
\vec{U}_x &= \f{\vec{x}}{|\vec{x}|}  \\\
\vec{U}_y &= \f{\vec{y}}{|\vec{y}|} 
\end{align*}$$
Exactly what you're thinking, they are **unit vectors**.
Here's a quickie: 
{{< prob 2>}}
Prove that $\c{#F49EC4} |\vec{U}_x| = 1$ and $\c{#F49EC4} |\vec{U}_y| = 1$
{{<toggle "Hint" "Hide hint">}}
Use scalar pullout!
{{</toggle>}}
{{</prob>}}
Anyway, since they are unit vectors, that means they are in $\c{orchid} \mathfrak{B}$.  
That's what we like to see, so now let's try and wrestle it into the $\c{pink} \Delta$ inequality. 
imo this part is a little bit of an asspull but it works:  

Let's use convexity with $\c{#F49EC4} \vec{U}_x$ and $\c{#F49EC4} \vec{U}_y$ as follows:
$$\large \begin{align*}
\c{yellow} t\c{#F49EC4} \vec{U}_x + \c{yellow} (1-t)\c{#F49EC4} \vec{U}_y &\in \c{orchid} \mathfrak{B} \\\
\c{yellow} t\c{#F49EC4} \f{\vec{x}}{|\vec{x}|} + \c{yellow} (1-t)\c{#F49EC4} \f{\vec{y}}{|\vec{y}|} &\in \c{orchid} \mathfrak{B}&nbsp;&nbsp;&nbsp;\c{white}\tu{ (1)}
\end{align*}
$$
with some specially chosen $\c{yellow} t$. Well, if we can wrestle it into this form:
$$\large \begin{align*}
\to \c{orchid} \f{\vec{x} + \vec{y}}{|\vec{x}| + |\vec{y}|} \in \mathfrak{B}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\c{white}\tu{ (2)}
\end{align*}
$$
Then we'll have it! (If it's not clear yet, don't worry. All you need to do is trust me.)
So if we equate $(1)$ and $(2)$ together and solve for $\c{yellow} t$, we get:
$$\large \begin{align*}
\c{yellow} t\c{#F49EC4} \f{\vec{x}}{|\vec{x}|} + \c{yellow} (1-t)\c{#F49EC4} \f{\vec{y}}{|\vec{y}|} &= \c{orchid} \f{\vec{x} + \vec{y}}{|\vec{x}| + |\vec{y}|} \\\
\c{yellow} t &= \c{yellow} \f{|\vec{x}|}{|\vec{x}| + |\vec{y}|}
\end{align*}$$
This is looking promising! That value of $\c{yellow} t \in [0,1]$ and plugging it in does indeed get us to the holy land.  
Well, we did it boyo.  

$$\Large \begin{align*}
\c{orchid} \f{\vec{x} + \vec{y}}{|\vec{x}| + |\vec{y}|} &\c{orchid} \in \mathfrak{B} \implies \\\\[3ex]
\c{orchid} \left|\f{\vec{x} + \vec{y}}{|\vec{x}| + |\vec{y}|}\right| &\c{cyan} \leqslant 1 \implies \\\\[3ex]
\c{orchid} \f{|\vec{x} + \vec{y}|}{|\vec{x}| + |\vec{y}|} &\c{cyan} \leqslant 1 \implies
\end{align*}
$$
$$\Large \c{red} \boxed{\c{orchid} \|\vec{x} + \vec{y}\| \c{orchid} \leqslant \|\vec{x}\| + \|\vec{y}\|}$$
{{</box>}}
{{</centr>}}
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
3a. Given a sequence of $\c{orange} n$ reals $\c{pink} x_1,x_2,\dotsc,x_n$, show that $$\large \c{lime} \left(\sum_{i=1}^n |x_i|^m\right)^{\large \frac{1}{m}} \to \max(|x_1|,|x_2|,\dotsc,|x_n|) \tu{ as } \c{orange} m \to \infty$$  
{{<toggle "Hint 1" "Hide hint">}}
Try bounding it from above and below, then use the {{<col "cyan">}} Squeeze/Sandwich Theorem {{</col>}}
{{</toggle>}}
{{<toggle "Hint 2" "Hide hint">}}
Let $\c{cyan} \mathcal{M} = \max(|x_1|,|x_2|,\dotsc,|x_n|)$, then the lower bound can simply be
$$\large \c{cyan} \mathcal{M} \leqslant \c{lime} \left(\sum_{i=1}^n |x_i|^m\right)^{\large \frac{1}{m}}$$ 
since $\c{cyan} \mathcal{M}$ is clearly in the sum and the sum contains *nonnegative* reals only.  
{{</toggle>}}
{{<toggle "Hint 3" "Hide hint">}}
The upper bound isn't too much worse. Consider the following sum:
$$\large \c{chartreuse} \left(\sum_{i=1}^n \mathcal{M}^m\right)^{\large \frac{1}{m}}$$
Then it's clear that
$$
\large \begin{align*}
\c{lime} \left(\sum_{i=1}^n \|x\_i\|^m\right)^{\large \frac{1}{m}} &\leqslant \c{chartreuse} \left(\sum_{i=1}^n \mathcal{M}^m\right)^{\large \frac{1}{m}} \\\
&= \c{chartreuse} \left(n\mathcal{M}^m\right)^{\large \frac{1}{m}} \\\
&= \c{chartreuse} n^{\large \frac{1}{m}} \mathcal{M}
\end{align*}$$ 
and as $\c{orange} m \to \infty$, we have $\c{chartreuse} n^{\large \frac{1}{m}} \to 1$, since $\c{lime} n$ is constant (in the $\c{orange} m$-world).
{{</toggle>}}
{{</prob>}}
<br>
{{<prob 3>}}
{{<tip "warn">}}
{{<col "red">}} Problem 3a {{</col>}} must be done first!
{{</tip>}}
3b. Let's define the following as a candidate norm for some vector $\c{cyan} x \in \mbb{R}^n$:
$$\Large \c{cyan} |\vec{x}| = \c{lime} \lim_{m \to \infty} \left(\sum_{i=1}^n |x_i|^m\right)^{\large \frac{1}{m}}$$
&emsp;&nbsp;&nbsp;&nbsp;Show that this **is** a norm.
{{</prob>}}