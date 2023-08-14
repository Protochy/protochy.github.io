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