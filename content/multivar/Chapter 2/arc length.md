---
title: "Arc length"
weight: 1011
description: >
 How long a curve is... and more!
---

Okay, let's talk about how we can find the length of a curve. As always, let's start simple. VERY simple. The circumference of a circle. We all know this, right? $\c{cyan} 2\pi r$  

Nice, now let's jump up a few levels and talk about a general 2D curve given by $$\Large \c{orange} \vec{r}(t) = \vecD{r_x(t)}{r_y(t)}$$

{{< centr >}}
{{< cbox >}}

Definition 1a. Arc length of a 2D curve 

Let $\c{pink} \vec{r} : I \to \mbb{R}^2$ be a *continuous* vector valued function, where $\c{orange} I = [a,b]$ is a **finite** interval. Then, the length of the arc subtended from $\c{lime} a$ to $\c{lime} b$ is given by the definite integral
$$\Huge \c{lime} \int_a^b \Large \c{cyan} \\sqrt{\left(\f{\tu{d}r_x}{\tu{d}t}\right)^2 + \left(\f{\tu{d}r_y}{\tu{d}t}\right)^2} \\; \c{red} \tu{d}t$$
{{<toggle "Show proof" "Hide proof">}}
<video width=100% controls> <source src="/anim/mvchap1/ArcLengthFormula.mp4" type="video/mp4">

Formal writeup coming soon...
{{</toggle>}}
{{</ cbox >}}
{{</ centr >}}

Unsurprisingly, this result generalises for an $\c{orange} n$-D curve.

{{< centr >}}
{{< cbox >}}

Definition 1. Arc length of a $\c{orange} n$-D curve 

Let $\c{pink} \vec{r} : I \to \mbb{R}^n$ be a *continuous* vector valued function, where $\c{orange} I = [a,b]$ is a **finite** interval. Then, the length of the arc subtended from $\c{lime} a$ to $\c{lime} b$ is given by the definite integral
$$\Large \c{lime} \int_a^b \c{cyan} \left| r'(t) \right| \\; \c{red} \tu{d}t$$
since $$\Huge \c{cyan} | r'(t) | = \Large \c{violet} \sqrt{\sum_{i=1}^n \left(\f{\tu{d}r_i}{\tu{d}t}\right)^2}$$
{{</ cbox >}}
{{</ centr >}}

ok sick, we got a way of calculating the literal length of a curve given two reference points (that's the $\c{lime} a$ and $\c{lime} b$ in the integral). A natural (natural to mathematicians, that is) question to ask is,  

<h4> {{<col "turquoise">}} Can we get a coordinate point from how far we've travelled along the curve?{{</col>}} </h4>
{{<divide>}}

### <span style="color: #da6d2b;">Arc length parameterisation</span>
okay okay, let's make the question posed above clear:
{{<centr>}}
{{<box "teal" "transparent" "orchid">}}
<h3> Can we find a coordinate point $\c{lime} \vec{r}(b)$ given the arc length from a reference point $\c{lime} \vec{r}(a)$? </h3>
{{</box>}}
{{</centr>}}


too many fucking words we need more numbers.
here's an actual PROBLEM:
{{<centr>}}
{{<prob 4>}}
Let $$\Large \c{chartreuse} f(x) = \f{2}{3} \sqrt{x^3}$$
What $\c{orange} (x,y)$ pair is exactly {{<arcol>}}**2**{{</arcol>}} units along the curve from the origin?

<img src="/anim/mvchap1/chap2/al56.png" alt="Arc Length Visual" width="1280" height="720"> 
{{</prob>}}
{{</centr>}}

{{<divide>}}
### Problems
{{<centr>}}
{{<prob 4>}}
{{<tip "warn">}}<h4> {{<rcol>}}  Computationally heavy! {{</rcol>}} </h4> {{</tip>}}
1. Let $$\Large \c{chartreuse} f(x) = \f{4}{15} (\sqrt{1 + x} - 1)^{\frac{3}{2}} (3 \sqrt{1 + x} + 2)$$
What $\c{orange} (x,y)$ pair is exactly {{<arcol>}}**5.6**{{</arcol>}} units along the curve from the origin?
{{</prob>}}
{{</centr>}}
yes, there's a reason the numbers are so goddamn FUcking ugly.