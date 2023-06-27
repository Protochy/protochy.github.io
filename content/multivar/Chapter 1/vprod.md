---
title: "Vector products"
weight: 6
description: >
  Dot product and cross product and their use
---
okay sugga, so you know how you can multiply two numbers together? well, its kinda nice having that also be defined for *vectors*, so let's go ahead and do that!

but how...?

well, mathematicians decided to do this in two ways, the {{< col "lime" >}} scalar product (dot product) {{</ col >}} and the {{< col "orange" >}} vector product (cross product). {{</ col >}}

Unsurprisingly, the {{< col "lime" >}} dot product {{</ col >}} takes in two vectors and spits out a **number** (yes, a NUMBER, a laymans term for scalar) while the {{< col "orange" >}} cross product {{</ col >}} takes in two vectors and spits out another vector with special properties (as we shall see)

### <span style="color: lime;">Dot product</span>
okay, so in the spirit of not reinventing the wheel, I leave this excellent video explaining how and why anyone could come up with the idea of the dot product in the first place.
(LEAVE 3b1b VIDEO)

TL;DW dot product is just a measure of how "close" two vectors are. if they point in similar directions, the dot product will be larger, if they point in opposite directions, it will be very small (negative)
{{< tip >}}
**The dot product of two vectors is 0 if they are perpendicular.**
{{</ tip >}}

So with that in mind, let's dive into the formula of the dot product.

{{< centr >}}
{{< box color="cyan" background="transparent" >}}

$$\c{lime} \Large \vec{a} \x \vec{b} = \c{pink} \left|\vec{a}\right| \x \left|\vec{b}\right| \x \cos(\theta) = \c{turquoise} \sum_{i=1}^{n} a_i b_i$$
{{< toggle showText="Show proof" hideText="Hide proof" >}}
hi reeshav, figure it out yourself (kidding itll come soon)
{{< /toggle >}}
{{</ box >}}
{{</ centr >}}

where $\Large \c{tan} \left|\vec{a}\right|$ represents the **magnitude** of $\c{tan} \vec{a}$,

$\Large \c{pink} \theta$ represents the angle between $\Large \c{tan} \vec{a}$ and $\Large \c{tan} \vec{b}$, 

and $\Large \c{magenta} a_i$ represents the i<sup>th</sup> component of $\c{tan} \vec{a}$

It should now be clear why the dot product of two *perpendicular* vectors is 0. If two vectors are *perpendicular* then the angle between them must be a right angle (definitions!), so $\color{orchid} \Large \theta = 90^{\circ}$ and $\color{orchid} \Large \cos(\theta) = 0$
{{< divide >}}

Suppose I asked you to find the angle between $\c{yellow} \vecD{1}{1}$ and $\c{turquoise} \vecD{3}{-1}$.
The dot product helps here.


 <img src="/anim/im/vec1.png" alt="Newton's Notes" width="1280" height="720"> 
 {{< toggle showText="Show answer" hideText="Hide answer" >}}
We know the magnitudes of both vectors, so we can just use the formula in reverse!
$$\Large \color{yellow} \vecD{1}{1} \color{pink} \x \color{turquoise} \vecD{3}{-1} = \color{yellow} \sqrt{2} \color{pink} \x \color{turquoise} \sqrt{10} \color{orchid} \x \cos(\theta) \implies$$
$$\Large \color{orchid} \arccos\left(\f{\color{yellow} \vecD{1}{1} \color{pink} \x \color{turquoise} \vecD{3}{-1}}{\color{yellow} \sqrt{2} \color{pink} \x \color{turquoise} \sqrt{10}}\right) = \color{orchid} \theta$$
{{< /toggle >}}

A short list of a few properties of the dot product:
Distributes, scalar mult,yadda yadad
| Properties      | Description |
| ----------- | ----------- |
| Scalar multiplication      | $\c{pink} \vec{a} \x (c\vec{b}) = c(\vec{a} \x \vec{b})$ for some scalar (NOOOOOMBER) $\c{pink} c$ {{< toggle showText="Show proof" hideText="Hide proof" >}}
hi reeshav, figure it out yourself (kidding itll come soon)
{{< /toggle >}}      |
| Distributivity (over addition)  | $\c{violet} \vec{a} \x (\vec{b} + \vec{c}) = \vec{a} \x \vec{b} + \vec{a} \x \vec{c}$ mmmm very nice{{< toggle showText="Show proof" hideText="Hide proof" >}}
hi reeshav, figure it out yourself (kidding itll come soon)
{{< /toggle >}}        |
| Commutativity  | $\c{magenta} \vec{a} \x \vec{b} = \vec{b} \x \vec{a}${{< toggle showText="Show proof" hideText="Die proof" >}}
hi reeshav, figure it out yourself (kidding itll come soon)
{{< /toggle >}}        |

note that Scalar mult and Commutativity are pretty visually intuitive to prove.

we'll see a lot more of the dot product so get REAL comfortable with it

<br>
<br>

### <span style="color: orange;">Cross product</span>
