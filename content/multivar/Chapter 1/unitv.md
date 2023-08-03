---
title: "Special unit vectors"
weight: 9
description: >
  Your tangent, unit tangent, normal, and principal unit normal vectors.
---

ok. bugga. now we talk about {{< rcol >}} SPECIAL {{</ rcol >}} types of arrows, those that lie *TANGENT* and *PERPENDICULAR* to our curve.

## Tangent vectors
First, we discuss *tangent* vectors. It's actually really simple. Just like how the derivative of a standard one variable fuction lies tangent to it, a derivative of a {{< col "orange" >}} vector {{</col>}} function lies tangent to it. 

{{< centr >}}
{{< box "purple" "transparent" >}}
Definition 1. Tangent vector

If $\c{pink} \vec{r}(t)$ is a parameterisation of a curve $\c{lime} \mathcal{C}$ and if the derivative exists at $\c{orange} t_0$ and is non-zero, i.e. $$\Large \c{pink} \vec{r}'(t_0) \neq \vec{0}$$, then the vector $\c{pink} \vec{r}'(t_0)$ lies {{< col "pink" >}} tangent {{</col>}} to $\c{lime} \mathcal{C}$ at $\c{orange} \vec{r}(t_0)$

{{< toggle showText="Show proof" hideText="Hide proof" >}}

It goes quite similarly to the \"proof\" of the derivative of a function being tangent to it. 

TODO: Add animation showing dy/dx as dx -> 0 and how that approaches tan line
{{< /toggle >}}
{{</ box >}}
{{</ centr >}}


<video width=100% controls> <source src="/anim/mvchap1/TangentVectorParametric.mp4" type="video/mp4">

pretteh simple, amirite?
{{< divide >}}
<h3> Unit tangent vectors </h3>  

for once in methmatics, the names are actually quite self explanatory. it's a vector that is tangent to the curve, but it's *unit* length. 

{{< centr >}}
{{< box "indigo" "transparent" >}}
Definition 2. Unit tangent vector  

Let $\c{pink} \vec{r'}(t)$ be a tangent vector of a curve $\c{lime} \mathcal{C}$, then the unit tangent vector $\c{orange} \vec{T}(t)$ is given by 
$$\Large \c{orange} \vec{T}(t) = \c{lime} \f{\vec{r'}(t)}{\left|\vec{r'}(t)\right|}$$
or in other words, literally the tangent vector divided by its magnitude to make it have a length of 1.
{{</ box >}}
{{</ centr >}}
aint it nice when the names actually make sense?  
<br>

### Normal vectors
Don't be fooled by the ordinary sounding name, these sneaky fucks are not normal. They're perpendicular though, so they point exactly $90^{\circ}$ away from the tangent vector.  

It turns out that it's much easier to calculate *unit normal vectors* (i know, truly mystical), so that's what we'll do. 

<h4> Unit normal vectors </h4>  

This is probably the first result that is kinda counter intuitive to most people (at least it was to me):

{{< centr >}}
{{< box "blue" "transparent" >}}
Definition 3. Unit normal vector  

Let $\c{orange} \vec{T}(t)$ be the unit tangent vector to a curve $\c{lime} \mathcal{C}$, then we define the *principal unit normal vector* as 
$$\c{magenta} \Large \vec{N}(t) = \c{orange} \f{\vec{T'}(t)}{\left|\vec{T'}(t)\right|}$$
yep, the derivative of the unit tangent vector, normalised (that just means make the vector a unit vector, another typical example of maths' flair for unhelpful nomenclature, `like seriously why the FUCK call it normalising when A NORMAL VECTOR MEANS PERPENDICULAR AND NOTHING TO DO WITH UNIT?` but oh well, that's maths)

{{<tip >}}
for those curious, the "normal" used in *normalising* a vector comes from the mathematical word for distance, **norm**.  

the "normal" used in *normal vector* comes from the latin *normalis* which means right-angled in Latin, go figure.
{{</tip>}}
{{</ box >}}
{{</ centr >}}

okay, let's first prove that the name isn't just a troll, i.e.
{{<prob "med">}} 
Show that the principal unit normal vector and the unit tangent vector really are perpendicular.  

If you don't know where to start:
{{<toggle showText="Show hint" hideText="Hide hint">}}
Prove that $$\Large \c{orange} \vec{T}(t) \x \c{magenta} \vec{N}(t)  \c{lime} = 0$$
given that you know $\c{orange} \vec{T}(t) \x \vec{T}(t) \c{lime} = 1$
{{</toggle>}}  

{{<toggle showText="Show proof" hideText="Hide proof">}}
So, we start with 
$$
\Large \\begin{equation*}
\\begin{split}  \c{orange} \vec{T}(t) \x \vec{T}(t) &\c{lime} = 1 \\\
\c{cyan} \deriv{t}\left(\underbrace{\c{orange} \vec{T}(t) \x \vec{T}(t)}_{\tu{Product rule $(\ast)$}} \c{cyan}\right) &\c{lime} = \c{cyan} \deriv{t} \left(\c{lime} 1 \c{cyan} \right) \\\\[5ex\]
\c{turquoise} 2 \c{orange} \vec{T}(t) \x \c{magenta} \vec{T'}(t) &\c{turquoise} = \c{lime} 0 \\\
\normalsize \tu{multiply by } \c{violet} \f{1}{2\left|\vec{T'}(t)\right|} \tu{ on both sides} \\\
\c{orange} \vec{T}(t) \x \c{magenta} \vec{N}(t) &\c{turquoise} = \c{lime} 0 \\\
\\end{split}
\\end{equation*}
$$  
$\c{cyan} \ast:$ [Problem 3](../vfunc/#problems) of [Vector Functions](../vfunc).  

and note that we assumed $\c{magenta} \vec{T'}(t) \neq 0$ in the first place, so we can divide by it. 

{{</toggle>}}
{{</prob>}}
but is this really satisfying? it's still pretty unintuitive to me, so let's actually look under the hood and see what's going on. 

<video width=100% controls> <source src="/anim/mvchap1/NormalVecPerpendicular.mp4" type="video/mp4">
(maybe remove music, use the 1.5 mb file lol)
c
{{<tip "warn">}}
In the animation, I'm representing $\c{cyan} \vec{N}(t)$ as $\c{orange} \vec{T'}(t)$, not the **normalised** (unit vector) version of it. This doesn't affect the validity of the proof, but it does make it easier to understand.  

In practice, you would take the normalised version of what I put there for $\c{cyan} \vec{N}(t)$
{{</tip>}}

The vector $\c{cyan} h \x \vec{N}(t)$ connecting $\c{orange} \vec{T}(t)$ and $\c{lime} \vec{T}(t+h)$ is quite literally $$\Large \c{cyan} h \x \vec{N}(t) = \c{lime} \vec{T}(t+h) - \c{orange} \vec{T}(t)$$ the change in the unit tangent vector as $\c{lime} h$ changes. (Rearrange it for $\c{cyan} \vec{N}(t)$ and out pops the derivative formula).

This vector is usually called the rejection, and as $\c{orange} h \to 0$, it becomes perpendicular to the unit tangent vector. 
{{< divide >}}

### Problems
TODO, lotta computational shit... yuck











