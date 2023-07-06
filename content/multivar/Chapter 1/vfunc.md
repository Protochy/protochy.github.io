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
{{< box "white" "pink" "transparent" >}}
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
$$\Large \c{pink} r(t) =  \vecD{\cos(t)}{\sin(t)}$$
notice how those values are bundled up in a vector? that's the {{<col "magenta" >}} key! {{</ col>}}
It's **not** returning $\cos$ and $\sin$ seperately, it's returning them *together*. They are one. (well technically, them squared make 1 {{< kekw >}})

{{< divide >}}
ok, now let's investigate what happens as we range $\c{pink} t$ from $\c{pink} 0$ to $\c{pink} 2\pi$

nice, a circle! anyway, we associate each t value with a corresponding *2D vector*, which is why the whole thing still works. 
INSERT manimVIDEO
{{< divide >}}

let's end with a formal-ish definition:

{{< centr >}}
{{< box "orchid" "turquoise" "transparent" >}}
Definition 2. Vector valued Fucktion

Let $\c{orchid} r: \mbb{R} \to \mbb{R}^n$, then
$$\Large \c{orchid} r(t) =\begin{bmatrix} r_1(t) \\\\[1.1ex\] r_2(t) \\\\[1.1ex\] \vdots \\\\[1.1ex\] r_n(t) \end{bmatrix}$$
{{</ box >}}
{{</ centr >}}
### Differentiation
Now, let's look at differentiating this function. 

{{< centr >}}
{{< box "white" "orchid" "transparent" >}}
Definition 3. Derivative of a vector function
$$\Large \c{orchid} r'(t) = \lim_{h \to 0} \frac{r(t+h) - r(t)}{h}$$
{{</ box >}}
{{</ centr >}}
pretty bloody obvious, right? it's the exact same thing for scalar functions. Let's investigate it a bit further though...
$$
\Large \\begin{equation*}
\\begin{split}   \c{orchid}  r'(t) &\c{orchid} = \lim_{h \to 0} \frac{r(t+h) - r(t)}{h}\\\\[1.3ex\]
       & \c{lime} =
 \c{lime} \lim_{h \to 0} \f{1}{h} \left(\begin{bmatrix} r_1(t+h) \\\ r_2(t+h) \\\ \vdots \\\ r_n(t+h) \end{bmatrix} - \begin{bmatrix} r_1(t) \\\ r_2(t) \\\ \vdots \\\ r_n(t) \end{bmatrix}\right) \\\\[5ex\]
       & \c{lime} =
 \c{lime} \lim_{h \to 0}  \begin{bmatrix} \f{r_1(t+h) - r_1(t)}{h} \\\\[1.3ex\] \f{r_2(t+h) - r_2(t)}{h} \\\\[1.3ex\] \vdots \\\\[1.3ex\] \f{r_n(t+h) - r_n(t)}{h} \end{bmatrix} \\\\[5ex\]
       & \c{orange} = \begin{bmatrix} r_1'(t) \\\\[1.1ex\] r_2'(t) \\\\[1.1ex\] \vdots \\\\[1.1ex\] r_n'(t) \end{bmatrix} \\\\[5ex\]
\\end{split}
\\end{equation*}
$$
wowzers, looks like it's as simple as taking the derivative of each component of the vector function. 
