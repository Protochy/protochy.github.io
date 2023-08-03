---
title: "Arc length"
weight: 12
description: >
 How long a curve is... and more!
---

Okay, let's talk about how we can find the length of a curve. As always, let's start simple. VERY simple. The circumference of a circle. We all know this, right? $\c{cyan} 2\pi r$  

Nice, now let's jump up a few levels and talk about a general curve given by $$\Large \c{orange} \vec{r}(t) = \vecD{r_x(t)}{r_y(t)}$$

{{< centr >}}
{{< cbox >}}

Definition 1a. Arc length of a 2D curve 

Let $\c{pink} \vec{r} : I \to \mbb{R}^2$ be a *continuous* vector valued function, where $\c{orange} I = [a,b]$ is a **finite** interval. Then, the length of the arc subtended from $\c{magenta} a$ to $\c{magenta} b$ is given by the definite integral
$$\Huge \c{lime} \int_a^b \Large \c{cyan} \\sqrt{\left(\f{\tu{d}r_x}{\tu{d}t}\right)^2 + \left(\f{\tu{d}r_y}{\tu{d}t}\right)^2} \\; \c{red} \tu{d}t$$
{{<toggle "Show proof" "Hide proof">}}
insert details
{{<toggle "Show geometric intuition" "Hide geometric intuition">}}
<video width=100% controls> <source src="/anim/mvchap1/ArcLengthFormula.mp4" type="video/mp4">

still needs work, video is too fast (pause at beg)
{{</toggle>}}
{{</toggle>}}
{{</ cbox >}}
{{</ centr >}}


