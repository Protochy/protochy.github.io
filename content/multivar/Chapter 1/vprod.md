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
{{< box "white" "lime" "transparent" >}}
Formula 1. Scalar (Dot) Product
$$\c{lime} \Large \vec{a} \x \vec{b} = \c{pink} \left|\vec{a}\right| \x \left|\vec{b}\right| \x \cos(\theta) = \c{turquoise} \sum_{i=1}^{n} a_i b_i$$

{{< toggle showText="Show proof" hideText="Hide proof" >}}
hi reeshav, figure it out yourself (kidding itll come soon)
{{< /toggle >}}
{{</ box >}}
{{</ centr >}}

where $\Large \c{tan} \left|\vec{a}\right|$ represents the **magnitude** of $\c{tan} \vec{a}$,

$\Large \c{pink} \theta$ represents the angle between $ \c{tan} \vec{a}$ and $ \c{tan} \vec{b}$, 

and $\Large \c{magenta} a_i$ represents the i<sup>th</sup> component of $\c{tan} \vec{a}$

It should now be clear why the dot product of two *perpendicular* vectors is 0. If two vectors are *perpendicular* then the angle between them must be a right angle (definitions!), so $\color{orchid} \Large \theta = 90^{\circ}$ and $\color{orchid} \Large \cos(\theta) = 0$
{{< divide >}}

Suppose I asked you to find the angle between $\c{yellow} \vecD{1}{1}$ and $\c{turquoise} \vecD{3}{-1}$.
The dot product helps here.


 <img src="/anim/im/vec1dp.png" alt="Dot Product Example" width="1280" height="720"> 
 {{< toggle showText="Show answer" hideText="Hide answer" >}}
We know the magnitudes of both vectors, so we can just use the formula in reverse!
$$\Large \color{yellow} \vecD{1}{1} \color{pink} \x \color{turquoise} \vecD{3}{-1} = \color{yellow} \sqrt{2} \color{pink} \x \color{turquoise} \sqrt{10} \color{orchid} \x \cos(\theta) \implies$$
$$\Large \color{orchid} \arccos\left(\f{\color{yellow} \vecD{1}{1} \color{pink} \x \color{turquoise} \vecD{3}{-1}}{\color{yellow} \sqrt{2} \color{pink} \x \color{turquoise} \sqrt{10}}\right) = \color{orchid} \theta$$
{{< /toggle >}}

{{< divide >}}
Let's go over projections now. Suppose I asked you to find the projection of $\c{yellow} \vec{a} := \vecD{2}{1}$ onto $\c{turquoise} \vec{b} := \vecD{3}{-1}$, denoted by $\c{orange} \Large \tu{proj}_{\c{turquoise} \vec{b}} \c{yellow} \vec{a}$, in terms of the dot product.

 <img src="/anim/im/proj1.png" alt="Projection Example" width="1280" height="720"> 
 {{< toggle showText="You're projecting so hard right now" hideText="Stop projecting" >}}
  Let's just do this the good ol' trigonometric way. **Observe** that we have a right triangle with $\c{yellow} \vec{a}$ as the hypotenuse and $\c{orange} \tu{proj}_{\vec{b}} \vec{a}$ as one of the legs. So let's use **TRIGGERNOMETRY**.
  
  $$
  \begin{align*}
  \Large \c{pink} \cos(\theta) = \f{ \c{orange} | \tu{proj}\_{\vec{b}} \vec{a}|}{\c{yellow} | \vec{a} |} \\\
  \Large \c{yellow} | \vec{a} | \c{pink} \cos(\theta) = \c{orange} | \tu{proj}_{\vec{b}} \vec{a}|
  \end{align*}
  $$
  
 now... NOW! we shall employ a SECRET technique, one hidden in the lost pages of the AOPS forums... Multiplying by 1
  $$
  \begin{align*}
  \Large \c{yellow} | \vec{a} | \c{pink} \cos(\theta) \c{turquoise} \x \f{| \vec{b} |}{| \vec{b} |} = \c{orange} | \tu{proj}_{\vec{b}} \vec{a}|
  \end{align*}
  $$

  get it?? because $\c{turquoise} \Large \f{| \vec{b} |}{| \vec{b} |} \normalsize = 1$! (unless $\c{turquoise} \vec{b} = \vec{0}$, but why the FUCK would we try to project onto the 0 vector?), anyway

  $$
  \begin{align*}
  \Large \c{turquoise} \f{\c{yellow} | \vec{a} | \c{turquoise} | \vec{b} | \c{pink} \cos(\theta)}{\c{turquoise} | \vec{b} | } = \c{orange} | \tu{proj}_{\vec{b}} \vec{a}|
  \end{align*}
  $$
  hey now doesn't that look familiar...

  $$\Large \c{lime} \f{ \vec{a} \x \vec{b}}{\c{turquoise} | \vec{b} |} =\c{orange} | \tu{proj}_{\vec{b}} \vec{a}|$$ 


 {{< tip >}}
New skill unlocked! You can now **project** your deepest insecurities on others.
{{</ tip >}}
 {{</ toggle >}}

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

now onto the more painful one, famously unintuitive with the crazy determinant formula (what the fuck is the determinant?)

Just like the dot product, there is an analagous 3b1b video \[insert\] that excellently addresses the motivation and intuition of the cross product.

{{< centr >}}
{{< box "white" "orange" "transparent" >}}
Formula 2a. Vector (Cross) Product
$$\c{orange} \Large \vec{a} \times \vec{b} = \c{orange} \det\left(\begin{bmatrix} \vec{i} & \vec{j} & \vec{k} \\\ \c{lime} \vec{a}_1 & \c{lime} \vec{a}_2 & \c{lime} \vec{a}_3 \\\ \c{pink} \vec{b}_1 & \c{pink} \vec{b}_2 & \c{pink} \vec{b}_3 \\\ \end{bmatrix} \c{orange}\right) = \vecT{\c{lime} a_2 \c{pink} b_3 - \c{lime} a_3 \c{pink} b_2}{\c{lime} a_3 \c{pink} b_1 - \c{lime} a_1 \c{pink} b_3}{\c{lime} a_1 \c{pink} b_2 - \c{lime} a_2 \c{pink} b_1}$$

{{< toggle showText="Show proof" hideText="Hide proof" >}}
hi reeshav, figure it out yourself (kidding itll come soon)
{{< /toggle >}}
{{</ box >}}


<br>
<br>
{{< box "white" "orange" "transparent" >}}
Formula 2b. *Magnitude* of Vector (Cross) Product
$$\Large \c{orange} \left| \vec{a} \times \vec{b}\right| = \c{lime} \left|\vec{a}\right| \x \c{pink} \left|\vec{b}\right| \c{orange} \x \sin(\theta)$$

{{< toggle showText="Show proof" hideText="Hide proof" >}}
A Geometrical Intuition:
{{< /toggle >}}
{{</ box >}}
{{</ centr >}}

 <img src="/anim/im/crossprod1.png" alt="Cross Product Example" width="1280" height="720"> 
okay, lots to unpack here.
TODO: finish problems, add more examples, clean up, do cross product stuff, make manim anims for problems, ok bye
<br>
<br>

### Problems

{{<prob "easy">}}
1. Prove that 
$$ \Large \c{orange} (\vec{a} \times \vec{b}) \x \vec{a} = (\vec{a} \times \vec{b}) \x \vec{b} = 0$$
{{</ prob >}}
<br>
{{<prob "med">}}
2. Given three vectors $\Large \c{lime} \vec{a},\vec{b},\vec{c} \in \mbb{R}^3$, show that $$\Large \c{orange} (\vec{a} \times \vec{b}) \c{lime} \x \vec{c} = \c{cyan} \det\left(\begin{bmatrix} a_1 & b_1 & c_1 \\\ a_2 & b_2 & c_2 \\\ a_3 & b_3 & c_3 \end{bmatrix}\right)$$
{{< col "cyan">}} or in other words, the {{< col "red" >}} volume {{</ col >}} of the *parallelepiped* spanned by the three vectors. {{</ col >}}
{{</ prob >}}
<br>
{{<prob "hard">}}
3. Prove that the area of a *simple* polygon is given by
$$\Large \c{lime} \f{1}{2} \x \sum_{i=0}^{n-1} \\left|\vec{v_i} \times \vec{v_{i+1}}\\right|$$
{{</ prob >}}  


