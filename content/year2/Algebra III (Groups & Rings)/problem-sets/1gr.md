---
title: "1"
weight: 29002
hide: true
description: >
  Problem Set 1.
---
rn it'll just be the interesting problems because god i suck ass at getting stuff done.

{{<prob 4>}}
3. Let $\c{pink} x,y,z \in$ group $\c{pink}G$. Suppose $\c{pink} xyz = \c{cyan} 1$.
<br>  
a) Does it follow that $\c{orange} yzx = \c{cyan} 1$? <br>
b) Does it follow that $\c{lime} yxz = \c{cyan} 1$?
{{<toggle "Hint a" "Hide hint">}}
For the first part, try using inverses to equate the two statements together (yes, it's true {{<kekw>}})
{{</toggle>}}
{{<toggle "Hint b" "Hide hint">}}
Use the same idea in a) to deduce that the only way $\c{lime} yxz = \c{cyan} 1$ holds is if $\c{pink} G$ is **abelian**. To find a somewhat simple counterexample, consider $\c{yellow} GL_2(\mbb{R})$
{{</toggle>}}

{{<toggle "Solution" "Hide solution">}}
a) $$\large \begin{align*}
\c{lime} xyz &\c{lime}= \c{cyan}1 \\\
\c{lime} yz &\c{lime}= \c{cyan}x^{-1} \\\
\c{lime} yzx &\c{lime}= \c{cyan}x^{-1}x \\\
\c{lime} yzx &\c{lime}= \c{cyan}1
\end{align*}$$
b) Let $\c{pink} G = GL_2(\mbb{R})$, and
$$\large \c{#5aa0ff} \begin{align*}
x &= \begin{bmatrix} 0 & 1 \\\ 1 & 0 \end{bmatrix} \\\
y &= \begin{bmatrix} 0 & -1 \\\ 1 & 0 \end{bmatrix} \\\
z &= \begin{bmatrix} 1 & 0 \\\ 0 & -1 \end{bmatrix}
\end{align*}$$
then $\c{#5aa0ff} xyz = I$ but $\c{orange} yxz = -I$
{{</toggle>}}
{{</prob>}}
<br>
{{<prob 4>}}
6. Let $\c{pink} G$ be a group and $\c{lime} x \in G$. Suppose that $\c{lime} x^2 \neq 1_G$ and $\c{lime} x^6 = 1_G$.   
Prove that $\c{violet} x^4 \neq 1_G$ and $\c{#5AFFA0} x^5 \neq 1_G$.
What are the possible values for $\c{lime} |x|$?
{{<tip "warn">}}
Closely related to {{<centr>}} <h3> {{<col "orchid">}}  Lagrange's Theorem {{</col>}} </h3>  {{</centr>}}
{{</tip>}}
{{<toggle "Hint 1" "Hide hint">}}
Try a proof by contradiction. Suppose $\c{violet} x^4 = 1_G$. Use the fact that $\c{lime} x^2 \neq 1_G$ to show that $\c{lime} x^6 = 1_G$ cannot possibly hold given our assumption.
{{</toggle>}}
{{<toggle "Solution" "Hide solution">}}
Suppose $\c{violet} x^4 = 1_G$, then we have $$\large \c{violet} x^4 \x x^2 = \c{lime} x^6 = 1_G$$
Since we assumed $\c{violet} x^4 = 1_G$, we get
$$\large \c{violet} 1 \x x^2 = \c{lime} 1_G$$ Contradiction!   

Suppose $\c{violet} x^5 = 1_G$, then $$\large \c{violet} x^5 \x x = \c{lime} x^6 = 1_G$$
Since we assumed $\c{violet} x^5 = 1_G$, we get
$$\large \c{violet} 1 \x x = \c{lime} 1_G$$
This implies $\c{violet} x$ is the identity, but if it was, then clearly $\c{lime} x^2 = 1_G$. But it's not. 
Contradiction!   

By process of elimination, the only candidate order remaining is $\c{lime} |x| = 3$. It turns out this is possible, take 
$\c{pink} G = \mbb{Z}_6$ with the binary operation of addition, and let $\c{violet} x = 2$.
{{</toggle>}}
{{</prob>}}
<br>
{{<prob 7>}}
7. Let $\c{pink} G$ be a group and $\c{#5AFFA0} g \in \c{pink} G \setminus \\{1_G\\}$. Prove the following statements.  

a) Let $\c{#5AFFA0} g \in \c{pink} G \setminus \\{1_G\\}$. Then $\c{#5AFFA0} g = g^{-1}$ iff $\c{#5AFFA0} |g| = 2$. $\left(\tu{Difficulty: }\textcolor{lime} {\boxed{3}}\right)$

b) $\c{#5AFFA0} |g^{-1}| = |g| \\;\forall g \in \c{pink} G$
$\left(\tu{Difficulty: }\textcolor{#c8ff00} {\boxed{4}} \right)$  

c) If $\c{pink} G$ is finite and $\c{pink} |G|$ even, then $\c{pink} G$ contains an element of order $2$.
$\left(\tu{Difficulty: }\textcolor{orange} {\boxed{7}}\right)$

{{<toggle "Solution a" "Hide soln a">}}
First let's tackle the $\c{#5AFFA0} \implies$ direction. Clearly $\c{#5AFFA0} |g| \neq 1$ since $\c{#5AFFA0} g$ is not the identity.  
<img src="https://i.imgur.com/S4TM2zH.gif" alt="Mmm...  monke" style="width:300px;height:200px;">  

So if $\c{#5AFFA0} g = g^{-1}$, then $\c{#5AFFA0} g^2 = g \x g^{-1} = 1$. Easy, right? Now the other direction...  

If $\c{#5AFFA0} |g| = 2$, then we have $\c{#5AFFA0} g^2 = 1 \implies g^2 g^{-1} = g^{-1}$   
I trust you see where this is going!
{{</toggle>}}
{{<toggle "Solution b" "Hide soln b">}}
Let's focus on an arbitrary element $\c{#5AFFA0} g \in \c{pink} G$. Suppose $\c{#5AFFA0} |g| = n$. Then, we have $$\c{#5AFFA0} \Large g^n = 1$$  

Now, we can apply $\c{#5AFFA0} g^{-1}$, $\c{lime} n$ times to both sides
$$\c{#5AFFA0} \large g^n \x (g^{-1})^{n} = (g^{-1})^{n} \implies 1 = (g^{-1})^{n}$$ 
But wait! We're not done yet. We haven't excluded the possibility that there exists some smaller integer $\c{orange} k$ such that $\c{orange} 1 = (g^{-1})^{k}$  
We can resolve this nagging doubt. Let's assume for the sake of contradiction that there was such a $\c{orange} k$. Then, we can use the exact same line of reasoning above to show that $\c{#5AFFA0} g^k = 1$. But this contradicts the fact that the order of $\c{#5AFFA0} g = n$.
{{</toggle>}}

{{<toggle "Solution c" "Hide soln c">}}
This is a special case of{{<arcol>}} Lagrange's Theorem  {{</arcol>}}. Okay, let's start categorising elements of this group by their order. We'll place them into $\c{cyan} 3$ buckets.  

- Order $\c{lime} 1$
- Order $\c{yellow} 2$
- Order $\c{#fb8b23} \geqslant 3$  

Note that the existence of even just ONE element in Order $\c{yellow} 2$ gets us the W.  

There's only one element in bucket Order $\c{lime} 1$, namely the *identity*.  

Let's skip Order $\c{yellow} 2$ for now.   

We can now use part b). Every element in Order $\c{#fb8b23} \geqslant 3$ has a corresponding inverse element which IS ALSO in Order $\c{#fb8b23} \geqslant 3$
which means the size of the set of Order $\c{#fb8b23} \geqslant 3$ elements must be even! Not so fast though! If an element happens to equal its inverse, this completely ruins our scheme.  
Why? Because the evenness of Order $\c{#fb8b23} \geqslant 3$ is stringent upon the fact that an element and its inverse come bundled in **pairs**. If an element equals its inverse, we aren't adding 2 elements to Order $\c{#fb8b23} \geqslant 3$, we're just adding 1.  

Shit. But wait, part a)! This cannot happen since the order is greater than 3. This means we'll never run into this issue!  

Now, the {{<col "tan">}} fun part. {{</col>}}  

Let's count up all the elements we've seen so far. There's $1$ in Order $\c{lime} 1$. There's an even number in Order $\c{#fb8b23} \geqslant 3$. This means our total tally right now must be odd.  

But, our group has an **even** number of elements. So, what gives? There must be at least one 
Order $\c{yellow} 2$ element. There just has to be! Isn't that slick?
{{</toggle>}}
{{</prob>}}