---
author: Joseph Bendy
date: 2023-07-08
title: Hmm
image: boy.jpg
---

# The problem
<br>
{{<centr>}}
{{<prob "hard">}}
Find the least value of $\c{pink} n \in \mbb{N}$ such that the decimal representation of $$\Large \c{lime} \frac{1}{9 - \tfrac{1}{n}}$$
only contains the digits $\c{orange} 1$ and $\c{orange} 2$ *after* the decimal point.
{{</prob>}}
{{</centr>}}

<br>

Okay, this isn't the easiest thing to parse. Let's break it down. 
SOOOO let's gather some data
{{< block "grid-2">}}
{{< column >}}
 | $$\Large \c{red} \frac{1}{9 - \tfrac{1}{n}}$$  | $$\Huge \c{purple} n$$ |
| ----------- | ----------- |
| $\Large 0.125$      | $\Large 1$       |
| $\Large 0.11235955056179775280898\dotsc$   | $\Large 10$       |
| $\Large 0.11129032258064516129032\dotsc$   | $\Large 69$       |
| $\Large 0.11111825192802056555269\dotsc$  | $\Large 1829$        |
{{< /column >}}

{{< column >}}
<br>
 Okay well that's not very helpful. Let's try something else.  

 When we're faced with a problem regarding decimal expansions of fractions, it's best to recall everything we know about decimal expansions of fractions.

 Here's a good warmup problem:
{{<prob "easy">}}
Prove that every fraction's decimal expansion repeats.
<br>
Examples:
| $$\Large \c{red} \frac{1}{n}$$  | $$\Huge \c{purple} n$$ |
| ----------- | ----------- |
| $ 1.\overline{0}$      | $$ 1$$       |
|  $ 0.5\overline{0}$    | $$ 2$$       |
| $ 0.\overline{3}$      | $$ 3$$       |
| $ 0.25\overline{0}$    | $$ 4$$       |
| $ 0.2\overline{0}$     | $$ 5$$       |
| $ 0.1\overline{6}$     | $$ 6$$       |
| $ 0.\overline{142857}$| $$ 7$$       |
| $ 0.125\overline{0}$   | $$ 8$$       |
| $ 0.1\overline{1}$     | $$ 9$$       |
| $ 0.1\overline{0}$     | $$10$$      |
| $ 0.\overline{09}$     | $$ 11$$      |
{{<toggle showText="Show hint" hideText="Hide hint">}}
Use the long division algorithm. Show that you eventually get a remainder that you've already seen before.
{{</toggle>}}

{{<toggle showText="Show proof" hideText="Hide proof">}}
ok
{{</toggle>}}
{{</prob>}}
{{< /column >}}

{{</block>}}

$$\begin{array}{rrrrrr}{cccccc}
        &          & 1 & + & x & + & 2x^2 & + & 3x^3 & + & 5x^4 & + & \dots  \\\
\overline{2-13}
1-x-x^2 &  1 &   &   &   &      &   &      &   &      &   &        \\\
        &          & 1 & - & x & - &  x^2 &   &      &   &      &   &        \\\
\cline{3-7}
        &          &   &   & x & + &  x^2 &   &      &   &      &   &        \\\
        &          &   &   & x & - &  x^2 & - &  x^3 &   &      &   &        \\\
\overline{5-9}
        &          &   &   &   &   & 2x^2 & - &  x^3 &   &      &   &        \\\
        &          &   &   &   &   & 2x^2 & - & 2x^3 & - & 2x^4 &   &        \\\
\overline{7-11}
        &          &   &   &   &   &      &   & 3x^3 & + & 2x^4 &   &        \\\
        &          &   &   &   &   &      &   & 3x^3 & - & 3x^4 & - & 3x^5   \\
\overline{9-13}
        &          &   &   &   &   &      &   &      &   & 5x^4 & + & 3x^5   \\
        &          &   &   &   &   &      &   &      &   &      &   & \vdots \\
\end{array}$$


{{<prob "easy">}}
Hi lolol i am easy!! easy easy easy easy easy easy easy 
{{</prob>}}