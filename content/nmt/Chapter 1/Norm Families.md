---
title: Norm families
weight: 2004
description: >
  An entire infinite class of norms!
---
<style>
    #a-r-t {
        background-image: repeating-linear-gradient(to right, red, orange, yellow, lime, cyan, violet);
        display: inline-block;
        background-size: 800% 800%;
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        animation: rainbow 8s ease infinite;
    }
    @keyframes rainbow { 
        0%{background-position:0% 50%}
        50%{background-position:100% 25%}
        100%{background-position:0% 50%}
    }
</style>

okay SO we've seen a few example of norms, but every single one you've seen up till now is actually part of something more *general*   
### <span id="a-r-t" style="color:rgba(0,255,0,1)">$\ell^p$ norms</span>
{{<centr>}}
{{<box "lime" "transparent" "pink">}}
We define the $\c{lime} \ell^p$ norms on $\c{cyan} \mbb{R}^n$ as follows:  
Let $\c{pink} p \geqslant 1$, then 
$$\Large \c{orchid} |\vec{x}| = \left(\sum_{i=1}^n |x_i|^p \right)^{\large \f{1}{p}}$$
{{</box>}}
{{</centr>}}

The traditional $\c{lime} \ell^2$ is a member of this infinite family. Christmas must be painful. {{<kekw>}}   

OKAY but you really shouldn't believe me this easily :P We need to show it's a norm! Easy enough for $\c{magenta} p \in \\{1,2,\infty\\}$, [we showed that already!](../norm/#problems)  

Showing positive definiteness (i.e. *always nonnegative*) and homogeneity (*scalar pullout*) ain't too bad, so let's just assume it using {{<col "orange">}} Proof by Can't Be Arsed {{</col>}} (but feel free to prove it for yourself!)  

The real kicker is the $\c{pink} \Delta$ inequality, and oh boy is it a nasty one. **However**, we pretty much did all the heavy lifting when we covered the convex ball $\iff$ $\c{pink} \Delta$ inequality thing.  

First, we need to tackle
### <span>{{<arcol>}}Convexity{{</arcol>}}</span>
but for *functions*.
{{<centr>}}
{{<box "cyan">}}
*Definition* {{<arcol>}} (*Convex function*) {{</arcol>}}:  

Let $\c{pink} I$ be a $\c{lime} \mbb{R}$ interval and $\c{lime} f: X \to \mbb{R}$ be a function, then
it's convex if and only if 
$$\c{gold} \large f(tx + (1-t)y) \leqslant t \x f(x) + (1-t) \x f(y)$$
for $\c{yellow} t \in [0,1]$ and $\c{lime} x,y \in \c{pink} I$  

hmmm... We see the idea of {{<rcol>}} linear interpolation {{</rcol>}} in there again and some weird inequality version of scalar pullout...  
Well it sure SHOULD be similar to a convex polygon/set where we had that line is contained in the interior of the shape rule. So the line connecting two points on the curve are contained INSIDE the curve?  
{{<col "#87CEEB">}} FFS too many words again, {{</col>}} Let's look at an `animation`!
<video width=100% controls> <source src="/anim/nmt/ch1/ConvexityLI.mp4" type="video/mp4"> 

You can see how the straight {{<rcol>}} linear interpolation {{</rcol>}} line lies within the curve!

Let's meddle with the definition to get it in a more user-friendly form.  
$$\large \c{gold} \f{f(x_2) - f(x_1)}{x_2 - x_1} \leqslant \f{f(x_3) - f(x_2)}{x_3 - x_2}$$
for $\c{yellow} x_1 < x_2 < x_3 \in \c{pink} I$  

This should make sense right? The slope of the secant line increases as $\c{yellow} x$ gets larger.{{<toggle "Show meddling" "Hide meddling">}}
god it's quite annoying, go in depth later  
if you wanna see it rn: [Click Here!](https://proofwiki.org/wiki/Equivalence_of_Definitions_of_Convex_Real_Function)
{{</toggle>}}
{{</box>}}
{{</centr>}}  

Here's a useful problem:  
{{<prob 6>}}
Show that if $\c{gold} f$ is twice differentiable and $\c{gold} f''(x) > 0 \\; \forall \\, x \in [a,b]$, then $\c{gold} f$ is {{<arcol>}} convex {{</arcol>}}  
{{<toggle "Hint" "Hide hint">}}
Use the mean value theorem and the second definition of convexity! (The meddled one)
{{</toggle>}} 
{{</prob>}}
okay so why did we go on a {{<arcol>}} convexity {{</arcol>}} detour? Because it's about to show why $\c{lime} \ell^p$ is a norm!  

What's the **Game Plan**? We're gonna use [Lemma 69](../norm/#unit-ball) (make it scroll exactly there, add js fiddly func later)  

But first we need to show the {{<col "red">}} unit ball {{</col>}} of $\c{lime} \ell^p$ is {{<arcol>}} convex {{</arcol>}}, remember that it's a candidate norm at this point, we DON'T KNOW whether it's a valid norm and we need to {{<col "pink">}} prove {{</col>}} that.

Let's just take it step by step. Say we have two vectors $\c{lime} \vec{x}, \vec{y} \in \c{orchid} \mathfrak{B}$, then we want to show
$$\Large \c{yellow} |t\vec{x} + (1-t)\vec{y}| \in \c{orchid} \mathfrak{B}$$ for all $\c{yellow} t \in [0,1]$ where 
$$\Large \c{orchid} \mathfrak{B} = \\{\vec{x} \in \mbb{R}^n \biggm\vert |\vec{x}|_{\c{lime} \ell^p} \c{orchid} \leqslant 1\\}$$

Okay, so we'll start with just the norm of 
$$\Large \begin{align*} \c{yellow} |t\c{pink} \vec{x}\c{yellow} + (1-t)\c{pink} \vec{y}\c{yellow}| &= \c{chartreuse} \left(\sum_{i=1}^n \c{yellow} |t\c{pink} x_i \c{yellow} + (1-t)\c{pink} y_i \c{yellow}|^p \c{lime} \right)^{\large \f{1}{p}} \\\
\c{yellow} |t\c{pink} \vec{x}\c{yellow} + (1-t)\c{pink} \vec{y}\c{yellow}|^p &= \c{chartreuse} \sum_{i=1}^n \c{yellow} |t\c{pink} x_i \c{yellow} + (1-t)\c{pink} y_i \c{yellow}|^p \c{white}\tu{&nbsp;&nbsp;&nbsp;(1)}
\end{align*}$$
If we let $\c{orange} f(t) = |t|^p$, it can be shown that $\c{orange} f$ is {{<arcol>}} convex {{</arcol>}}  

Actually, why don't YOU show it {{<kekw>}}
{{<prob 3>}}
Show that $\c{orange} f(t) = |t|^p$ is convex.
{{<toggle "Hint" "Hide hint">}}
$\huge \c{cyan} \f{\tu{d}}{\tu{d}t}$
{{</toggle>}}
{{</prob>}}
Cool, so we can use it on $$\Large \c{yellow} |t\c{pink}x_i \c{yellow} + (1-t)\c{pink}y_i \c{yellow}|^p \leqslant t \c{pink} |x_i|^p \c{yellow} + (1-t) \c{pink} |y_i|^p$$
If we sub that back in to our **Norm**an conquest $(1)$, then we can close it out:
$$\Large \begin{align*} \c{yellow} |t\c{pink} \vec{x}\c{yellow} + (1-t)\c{pink} \vec{y}\c{yellow}|^p &= \c{chartreuse} \sum_{i=1}^n \c{yellow} |t\c{pink} x_i \c{yellow} + (1-t)\c{pink} y_i \c{yellow}|^p \c{white}\tu{&nbsp;&nbsp;&nbsp;(1)} \\\
&\leqslant \c{chartreuse} \sum_{i=1}^n \c{yellow} t \c{pink} |x_i|^p \c{yellow} + (1-t) \c{pink} |y_i|^p \\\
&= \c{chartreuse} \sum_{i=1}^n \c{yellow} t \c{pink} |x_i|^p \c{yellow} + \c{chartreuse} \sum_{i=1}^n \c{yellow} (1-t) \c{pink} |y_i|^p \\\
&= \c{yellow} t \c{chartreuse} \sum_{i=1}^n  \c{pink} |x_i|^p \c{yellow} + \c{yellow} (1-t) \c{chartreuse} \sum_{i=1}^n  \c{pink} |y_i|^p \\\\[3ex]
&= \c{yellow} t  \c{pink} |\vec{x}|^p \c{yellow} + \c{yellow} (1-t)  \c{pink} |\vec{y}|^p \c{white}\tu{&nbsp;&nbsp;&nbsp;}(\star)\\\\[1.4ex]
&\leqslant \c{yellow} t \x \c{pink} 1 \c{yellow} + \c{yellow} (1-t) \x  \c{pink} 1 \\\\[1.4ex]
&= \c{cyan} 1
\end{align*}$$
{{<toggle "$(\star)$" "Hide">}}
$$\Large \begin{align*} 
\c{pink} |\vec{x}| &= \c{pink} \left(\c{lime} \sum_{i=1}^n \c{pink} |x_i|^p\right)^{\large \f{1}{p}} \implies \\\
\c{pink} |\vec{x}|^p &= \c{lime} \sum_{i=1}^n \c{pink} |x_i|^p
\end{align*}
$$
{{</toggle>}}
And so that means
$$\Large \begin{align*}
\c{yellow} |t\c{pink} \vec{x}\c{yellow} + (1-t)\c{pink} \vec{y}\c{yellow}|^p &\leqslant \c{cyan} 1 \\\
\c{yellow} |t\c{pink} \vec{x}\c{yellow} + (1-t)\c{pink} \vec{y}\c{yellow}| &\leqslant \c{cyan} 1  \\\
\c{yellow} |t\c{pink} \vec{x}\c{yellow} + (1-t)\c{pink} \vec{y}\c{yellow}| &\in \c{orchid} \mathfrak{B}
\end{align*}$$
<img style="width: 200px" src="https://media.tenor.com/9XyRPn8GZr8AAAAC/quod-erat-demonstrandum-unbelievable.gif">

### Equivalency
Didn't think norms could be equivalent did ya? Well I sure didn't. Anyway, the definition is kinda reasonable-ish. It's like Big-$\theta$'s definition, and by that I mean pretty much exactly it but for norms.
{{<centr>}}
{{<box "indigo">}}
*Equivalency of two* {{<arcol>}} *norms*: {{</arcol>}} 

Two norms on *the same* vector space $\c{lime} X$, $\c{pink} ||\_{1}$ and $\c{orange} ||\_{2}$ are **equivalent** iff one of the conditions hold (since then the other one will also):

1.  $\c{cyan} \exists \\, 0 < c_1 \leqslant c_2$ such that 
$$\Large \c{magenta} \boxed{\c{orchid} c_1 |\vec{x}|_{1} \leqslant |\vec{x}|_2 \leqslant c_2 |\vec{x}|_1} \c{lime} \tu{&nbsp;&nbsp;&nbsp;} \\; \forall \\, \vec{x} \in X$$
Basically if you can squeeze one of the norms in between the others for ALL $\c{lime} \vec{x} \in X$  

2.  $\c{cyan} \exists \\, 0 < c_1 \leqslant c_2$ such that 
$$\Large \c{magenta} \boxed{\c{orchid} c_1 \mathfrak{B}\_{1} \subseteq \mathfrak{B}\_{2} \subseteq c_2 \mathfrak{B}\_{1}}$$
where $\c{orchid} \mathfrak{B}\_i$ is the unit ball of norm $\c{pink} ||\_{i}$  
Basically the same thing as condition 1 but with unit balls instead.
{{<centr>}} <img style="width: 200px" src="https://pbs.twimg.com/profile_images/1284223274109501447/5p0AbGeq_400x400.jpg"> {{</centr>}}
{{</box>}}
{{</centr>}}
### Problems
Everyone's favourite section woooo...
{{<prob 4>}}
1. Show that if $\c{pink} ||$ is a {{<arcol>}} norm {{</arcol>}} on $\c{lime} X$, then 
$$\Large \begin{array}{lr}
 \c{gold} \left| |\vec{x}-\vec{y}| \right| \leqslant |\vec{x}-\vec{y}| & \tu{for any } \c{lime} \vec{x},\vec{y} \in X
\end{array}$$
{{<toggle "Hint (Basically answer)" "Hide answer">}}
{{<rcol>}} Reverse Triangle Inequality! {{</rcol>}}
{{</toggle>}}
{{</prob>}} <br>
{{<prob 4>}}
2a. Show that the {{<arcol>}} norm {{</arcol>}} equivalency definition is actually an `equivalence relation` on $\large \c{lime} \mathcal{N}(X)$, the set of all {{<arcol>}} norms {{</arcol>}} on $\c{lime} \large X$
{{<toggle "Hint" "Hide hint">}}
Show {{<col "turquoise">}} reflexivity, symmetry, and transitivity {{</col>}}
{{</toggle>}}
{{</prob>}} <br>
{{<prob 7>}}
2b. Show that all the $\c{lime} \large \ell^p$ {{<arcol>}} norms {{</arcol>}} are equivalent.
{{<toggle "Hint" "Hide hint">}}
Use the fact that {{<arcol>}} norm {{</arcol>}} equivalency is an `equivalence relation`, and so if you show $\large \c{lime} \ell^p \sim \ell^{\c{magenta} K}$ for varying $\c{lime} p$ and fixed $\c{magenta} K$, then that does it!  

(If you're confused on why, showing the above shows that all the $\c{lime} \ell^p$ norms fall under the same `equivalence class` and so must be equivalent.)
{{</toggle>}}
{{<toggle "Hint 2" "Hide hint">}}
Let $\large \c{magenta} K = \infty$
{{</toggle>}}
{{</prob>}} <br>
{{<prob 6>}}
3. Show that the following is a {{<arcol>}} norm: {{</arcol>}}
$$\Large \c{silver} |f|_{L^p} = \left(\int_a^b |f(x)|^p \\: \tu{d}x \right)^{\Large \f{1}{p}} \tu{ for } p \in [1,\infty)$$
given that $\c{silver} f(x)$ is {{<col "#87CEEB">}} continuous {{</col>}} on $\c{pink} [a,b]$
{{<toggle "Hint" "Hide hint">}}
Use [Lemma 69](../norm/#unit-ball) to prove the $\c{pink} \Delta$ inequality.
{{</toggle>}}
{{</prob>}} <br>
{{<prob 9>}}
{{<tip "warn">}}
Similar to [Problem 3a.](../norm/#problems)
{{</tip>}}
4. Let $\c{#B9F2FF} f$ be {{<col "#87CEEB">}} continuous {{</col>}} on $\c{pink} [a,b]$, then show that $$\Large \c{orange} \lim_{n \to \infty} \left(\int_a^b |f(x)|^n \\: \tu{d}x \right)^{\Large \f{1}{n}} = \c{red} \max_{x \in [a,b]} f(x)$$
or in other words, the *maximal* value attained by $\c{#B9F2FF} f$ in $\c{pink} [a,b]$
{{<tip "warn">}}
Might require you to dust off those old {{<col "cyan">}} Analysis II {{</col>}} notes :P
{{</tip>}}
{{</prob>}}

