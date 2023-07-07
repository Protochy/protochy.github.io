---
title: "Curves and parameterisations"
weight: 8
description: >
  What is a curve/path and how do you parameterise it?
---
### Curves
ooh you sniff turkey fat. okay, what is a curve? well, it's a bunch of points that are connected together. more formally, it's

{{< centr >}}
{{< box "cyan" "transparent" >}}
Definition 1. Curves

Let $\c{pink} \vec{r} : I \to \mbb{R}^n$ be a *continuous* vector valued function, where $\c{orange} I \subseteq \mbb{R}$ is an interval. Then, the set of points
$$\c{lime} \Large \mathcal{C} = \\{ \vec{r}(t) \mid t \in I \\}$$
is a curve. The function $\c{pink} \vec{r}$ is called a *parameterisation* of the curve.
{{</ box >}}
{{</ centr >}}
literally just a collection of points. all of your favourite functions are in there, like $\c{pink} y = x^2$ or $\c{orchid} y = e^x$ 
{{<tip >}}
{{<prob "easy">}}
Question for the initiated. How would you define $\c{pink} y = x^2$ or $\c{orchid} y = e^x$ as **vector functions**?
{{</prob>}}
{{</ tip >}}
{{< divide >}}

### Parameterisations

okay, let's talk parameterisations. what are they? well, they're just a way of representing a curve. for example, $\c{pink} \vec{r}(t) = \vecD{t}{t^2}$ is a parameterisation of $\c{pink} y = x^2$. 

{{< tip "warn" >}}
Parameterisations need not be unique! For example, $\c{pink} \vec{r}(t) = \vecD{t}{t^2}$ and $\c{pink} \vec{r}(t) = \vecD{t^2}{t^4}$ are both parameterisations of $\c{pink} y = x^2$.
{{</tip>}}

For a visual example, take $$\Large \c{red} \vec{r_1}(t) = \vecD{\cos(t)}{\sin(t)} \c{white} \tu{ and  } \\; \c{lime} \vec{r_2}(t) = \vecD{\cos(2t)}{\sin(2t)}$$
<video width=100% controls> <source src="/anim/mvchap1/ParameterisedCurve1.mp4" type="video/mp4">

Notice how they both draw out the unit circle but at different speeds? That's because they're parameterisations of the same curve, but with different *speeds*.

### Problems
  

{{< prob "med" >}}
{{<tip "warn" >}} Do [Problem 4](../vfunc/#problems) of [Vector Functions](../vfunc) first. {{</tip>}}

1. Let $\c{orchid} \vec{r}(t) = \vecD{t}{t^2}$ be a parameterisation of a curve $\c{lime} \mathcal{C} \in \mbb{R}^3$ such that $\c{pink} \vec{r}(0) = (R,-R,R)$, where $\c{pink} R > 0$.  
Suppose $\c{pink} \vec{r}(t) \neq 0$ and $\c{lime} \vec{r}(t) \x \vec{r'}(t) = 0$ for all points on $\c{lime} \mathcal{C}$. Show that $\c{lime} \mathcal{C}$ lies on the surface of a sphere and determine the centre and radius of the sphere.
{{< /prob >}}