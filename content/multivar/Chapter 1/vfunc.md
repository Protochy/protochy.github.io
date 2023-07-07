---
title: "Vector functions"
weight: 7
description: >
  Functions of vectors. Yep. That's it.
---

very cool. now we've graduated from vectors to vector functions. 

So what exactly ISSSSS a vector function? Well to fully answer that, we need to talk about the baby version of vector functions, {{< col "pink">}} scalar functions {{< /col >}}

### Scalar functions

{{< centr >}}
{{< box "white" "transparent" "pink" >}}
Definition 1. Scalar Fucking Function  

Literally just every function you've seen before:
$$\Large \c{pink} y = f(x)$$
Spits out ONE and only ONE value.
{{</ box >}}
{{</ centr >}}

Now ofc, I'm simplifying a lot here, but who gives a shit (for now). Anyway, the alternative is that we return MORE than 1 value. 

### Vector valued functions
{{< tip "warn" >}}
BUT ISNT THE DEFINITION OF A FUNCTION EVERY INPUT HAS ONE AND ONLY ONE OUTPUT, for example, you can't have $\c{cyan} 4 \to \begin{cases} 2 \\\ -2 \end{cases}$
{{</ tip >}}
and you'd be right! but the nice thing is, the definition of a vector function is a bit cleverer than that. let's say we return 2 values, i.e.
$$\Large \c{pink} \vec{r}(t) =  \vecD{\cos(t)}{\sin(t)}$$
notice how those values are bundled up in a vector? that's the {{<col "magenta" >}} key! {{</ col>}}
It's **not** returning $\cos$ and $\sin$ seperately, it's returning them *together*. They are one. (well technically, them squared make 1 {{< kekw >}})

{{< divide >}}
ok, now let's investigate what happens as we range $\c{pink} t$ from $\c{pink} 0$ to $\c{pink} 2\pi$

<video width=100% controls> <source src="/anim/pathCircle1.mp4" type="video/mp4"> Your browser does not support the video tag.</video> ADD FUCKING ARROW TO R LOL (del this line later)

nice, a circle! anyway, we associate each t value with a corresponding *2D vector*, which is why the whole thing still works. 
{{< tip >}}
We'll see more of this when we cover *curves*, but essentially what the {{< rcol >}} rainbow {{</ rcol >}} thing drew out was a **path**. 
{{</ tip >}}
{{< divide >}}

let's end with a formal-ish definition:

{{< centr >}}
{{< box "orchid" "transparent" "turquoise" >}}
Definition 2. Vector valued Fucktion

Let $\c{orchid} \vec{r}: \mbb{R} \to \mbb{R}^n$, then
$$\Large \c{orchid} \vec{r}(t) =\begin{bmatrix} r_1(t) \\\\[1.1ex\] r_2(t) \\\\[1.1ex\] \vdots \\\\[1.1ex\] r_n(t) \end{bmatrix}$$
{{</ box >}}
{{</ centr >}}
{{< tip >}}
You may also see a different notation: 
$$\Large \c{orchid} \vec{r}(t) = \langle r_1(t), r_2(t), \dotsc, r_n(t) \rangle$$
They're the same thing so worry not!
{{</ tip >}}
### Differentiation
Now, let's look at differentiating this function. 

{{< centr >}}
{{< box "white" "transparent" "orchid" >}}
Definition 3. Derivative of a vector function

$$\Large \c{orchid} \vec{r'}(t) = \lim_{h \to 0} \frac{\vec{r}(t+h) - \vec{r}(t)}{h}$$
{{</ box >}}
{{</ centr >}}

pretty bloody obvious, right? it's the exact same thing for scalar functions. Let's investigate it a bit further though...
$$
\Large \\begin{equation*}
\\begin{split}   \c{orchid}  \vec{r'}(t) &\c{orchid} = \lim_{h \to 0} \frac{\vec{r}(t+h) - \vec{r}(t)}{h}\\\\[1.3ex\]
       & \c{lime} =
 \c{lime} \lim_{h \to 0} \f{1}{h} \left(\begin{bmatrix} r_1(t+h) \\\ r_2(t+h) \\\ \vdots \\\ r_n(t+h) \end{bmatrix} - \begin{bmatrix} r_1(t) \\\ r_2(t) \\\ \vdots \\\ r_n(t) \end{bmatrix}\right) \\\\[5ex\]
       & \c{lime} =
 \c{lime} \lim_{h \to 0}  \begin{bmatrix} \f{r_1(t+h) - r_1(t)}{h} \\\\[1.3ex\] \f{r_2(t+h) - r_2(t)}{h} \\\\[1.3ex\] \vdots \\\\[1.3ex\] \f{r_n(t+h) - r_n(t)}{h} \end{bmatrix} \\\\[5ex\]
       & \c{orange} = \begin{bmatrix} r_1'(t) \\\\[1.1ex\] r_2'(t) \\\\[1.1ex\] \vdots \\\\[1.1ex\] r_n'(t) \end{bmatrix} \\\\[5ex\]
\\end{split}
\\end{equation*}
$$
wowzers, looks like it's as simple as taking the derivative of each component of the vector function. 

### Problems

{{< prob "med" >}}
1. If you know about the Riemann integral, you can probably guess what the integral of a vector function is. 
Prove that $$\Large \c{pink} \int_a^b \vec{r}(t) \\: \tu{d}t = \begin{bmatrix} \int_a^b r_1(t) \\: \tu{d}t \\\\[1.1ex\] \int_a^b r_2(t) \\: \tu{d}t \\\\[1.1ex\] \vdots \\\\[1.1ex\] \int_a^b r_n(t) \\: \tu{d}t \end{bmatrix}$$
{{< /prob >}}
<br>
{{< prob "easy" >}}
2. Differentiate $$\Large \c{cyan} \vec{r}(t) = \vecD{t^2}{t^3}$$
{{< /prob >}}
<br>
{{< prob "med" >}}
3. Prove that
$$\Large \c{magenta} \deriv{x} (\vec{a} \x \vec{b}) = \f{\tu{d} \vec{a}}{\tu{d}x} \vec{b} + \f{\tu{d} \vec{b}}{\tu{d}x} \vec{a}$$
{{< /prob >}}
<br>
{{< prob "hard" >}}
4. If $\c{lime} \vec{r}(t)$ is a vector function satisfying the following property that $\c{lime} \vec{r}(t) \x \vec{r'}(t) = 0 \\; \forall t$ 

(for all $t$), then prove that $\c{orchid} |\vec{r}(t)|$ is constant. 

<br>
{{< toggle showText="Hint 1" hideText="Hide hint" >}}
What's $\c{lime} \Large \displaystyle \int f(x) f'(x) \\: \tu{d}x$?
{{< /toggle >}}
{{< /prob >}}