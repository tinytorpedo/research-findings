# Transfer from the full-root energy to the primorial-window variance

**Status:** Companion proof for review, 17 November 2026. The conclusion uses the [candidate full-root energy bound](README.md) and the limiting conductor law in the pinned variance note.

Let $L=x\#$ for primes $x\to\infty$, let $y$ be the largest prime at most $\sqrt L$, and put $K=L/6$, $\ell=1+\log K$, $m=1+\log\ell$. Consider the two-house comb of §7 of the variance note. Its survivor set consists of the residues $11,17\bmod 30$ whose two legs are coprime to the eligible primes $7\le p\le y$. Let $N_L$ count these survivors in a window of length $L$ with a uniform starting point modulo the sieve period. The candidate energy bound implies the conditional limit
$$
\lim_{x\to\infty}\frac{\operatorname{Var}N_L}{\mathbb E N_L}
=1-e^{-2\gamma}\Big(\frac92-4\log 2\Big)=0.45545648\ldots .
$$
The argument below bounds the full mixed error and connects it to the exact variance decomposition. [Pinned variance note, §§7–10](https://github.com/solveathome/twin-primes/blob/c8fced6cac7008c4a5d06295db2b7dca1ed5eef3/paper/variance-note.md)

## Exact mixed discrepancy

Use $\alpha_j$, $D_y$, $F_N$, $B_s$, $A$, $Q$ and $H$ as defined in the energy note. In compressed lag coordinates $d=6h$, write $V(h)=15$ on $0\bmod5$, $15/2$ on $\pm1\bmod5$, and zero elsewhere. For a function $F$ on compressed lags put
$$
\mathcal L_K(F)=\sum_{|h|<K}(1-|h|/K)F(h)-K\langle F\rangle,
$$
where the brackets denote the complete CRT mean. The exact normalized correlation kernel of the comb is zero on lags outside $6\mathbb Z$, and on $6h$ it is
$$
W(6h)=D_y V(h)\prod_{7\le p\le y}
\left(1+\frac{2\,1_{p\mid h}+1_{p\mid 3h-1}+1_{p\mid 3h+1}}{p-4}\right).
$$
Indeed the small-prime comb gives the displayed $V$, and $p\mid 6h\pm2$ is equivalent to $p\mid 3h\pm1$ for eligible primes. The mean of $W(6h)$ is $6D_y\prod_p(1+4/[p(p-4)])=6$. Consequently the exact discrepancy $X(L)$ of the variance note equals $\mathcal L_K(W(6\cdot))$.

An assignment has pairwise coprime role products $(a,b,c)$ and $n=abc$. Its weight before the factor $D_y$ is $\lambda=\alpha_2(a)\alpha_1(b)\alpha_1(c)$. It selects $a\mid h$, $b\mid3h-1$, and $c\mid3h+1$. Its centered contribution is
$$
e_{a,b,c}=D_y\lambda\,\mathcal L_K\big(V\,1_{a\mid h,\,b\mid3h-1,\,c\mid3h+1}\big).
$$
Here the mean inside $\mathcal L_K$ is $6/n$, by CRT and the three comb weights. Let $E_{\rm mix}$ sum the assignments with at least two nonunit role products. This includes both nonempty shifted roles with $a=1$. The empty assignment belongs to the central group. With this convention $X=X_{\rm cen}+X_{\rm shift}+E_{\rm mix}$ exactly.

## From the full mixed sum to the capped spectrum

**Product window and small factors.** For a class $t$ modulo $d$, write $K=kd+r$, $0\le r<d$, and let $I=\{0,\dots,r-1\}$ modulo $d$. Counting differences of two indices in $\{0,\dots,K-1\}$ gives
$$
\mathcal L_K(1_{h\equiv t\bmod d})
=\frac{|I\cap(I+t)|-r^2/d}{K}.
$$
In particular its absolute value is at most $\min(1,d/(4K))$. Apply this at modulus $5n$ to the three comb classes. Then $|e_{a,b,c}|\ll\lambda\min(1,n/K)$.

For fixed $j$, $\sum_{d\le U}d\alpha_j(d)\ll_j U(1+\log U)^{j-1}$ and $\sum_{d>U}\alpha_j(d)/d\ll_j(1+\log U)^{j-1}/U$ for $U\ge1$. The first estimate follows from convolution with $\tau_j$. At an eligible prime the nonnegative squarefree correction has value $j p/(p-4)-j=O_j(1/p)$, whose reciprocal-weighted Euler product converges. The second estimate is partial summation. At fixed $n$, the total allocation weight is at most $\alpha_4(n)$. Thus $n\le K/\ell^2$ costs $O(\ell)$ in absolute centered mass.

For $n>K\ell^{11}$, the reference mass costs $O(\ell^{-8})$. To bound the actual mass, insert a factor $n/(K\ell^{11})$. At $h\ne0$, the sum of $n\lambda$ over compatible assignments is bounded by $F_2^*(|h|)F_1^*(|3h-1|)F_1^*(|3h+1|)$, where
$$
F_j^*(t)=\prod_{p\ge7,\,p\mid t}(1+j p/(p-4)).
$$
The mean bounds for $(F_2^*)^2$ and $(F_1^*)^4$ are $O((1+\log U)^8)$ and $O((1+\log U)^{15})$ through $U$. To verify these, a prime-factor product of local values $\gamma_p=k+O(1/p)$ has mean $O((1+\log U)^{k-1})$ by convolution with $\tau_k$. The correction has local polynomial $(1+(\gamma_p-1)z)(1-z)^{k-1}$, so its reciprocal-weighted absolute coefficients are summable. Apply this with $k=9,16$. Hölder with exponents $2,4,4$ bounds the product sum through $K$ by $O(K\ell^{23/2})$. Mixed assignments vanish at zero. The actual high-product mass is therefore $O(\ell^{1/2})$.

Within $K/\ell^2<n\le K\ell^{11}$, put $s=bc$. The allocation weight at fixed $a,s$ is bounded by $\alpha_2(a)\alpha_2(s)$. For fixed $a$, the allowed $s$ lie in an interval of ratio $\ell^{13}$ with upper endpoint at most $K\ell^{11}$, so their $\alpha_2$-mass is $O(\ell m)$ by the interval estimate in the energy note. The same bound holds for the $a$-mass at fixed $s$. Since $\sum_{d\le Q}\alpha_2(d)\ll(1+\log Q)^2\ll\ell^{1/2}$, the union $a\le Q$ or $s\le Q$ costs $O(\ell^{3/2}m)$. The case $a>K$ has only its reference term since no nonzero $h$ is divisible by $a$ in the window. Its reference mass is $O(\ell)$ by the $\alpha_2(d)/d$ tail and the bounded sum of $\alpha_2(s)/s$.

**Exact spectrum.** The retained pairs have $Q<a\le K$, $Q<s$, $(a,s)=1$ and the product window above. Summing all shifted assignments at fixed $a,s$ gives exactly the roots $(3h)^2=1\bmod s$. Indeed each eligible prime dividing $s$ chooses one of the two distinct roots. Write $h=at$ and take the discrete Fourier transform modulo $5s$ of $V(at)1_{(3at)^2=1\bmod s}$. CRT gives its coefficient at $r$ as
$$
\frac{v_{r\overline{as}\bmod 5}}s\sum_{\xi^2=1\bmod s}e_s(r\xi\overline{15a}).
$$
The $5$-component uses the three comb weights, and the $s$-component contributes the factor $\overline{15a}$. Both sets are even, which absorbs the sign in the Fourier convention. At zero the coefficient is $6\rho(s)/s$. After triangular smoothing, the difference of its contribution from the mean is $6\rho(s)(F_{K/a}(0)-K/a)/s$. Since $F_N(0)-N\le1/(4N)$, the total weighted error is $O(\ell)$ by $\sum_{a\le K}a\alpha_2(a)\ll K\ell$ and the convergence of $\sum_s\alpha_2(s)/s$.

For the nonzero modes, $F_N(r/(5s))\ll s^2/(N r^2)$ for $0<|r|\le(5s-1)/2$, from the geometric-series formula for the Fejér kernel. The error from $|r|>H$ is at most a constant times
$$
\frac{1}{KH}\sum_{\substack{as\le K\ell^{11}\\(a,s)=1}} as\,\alpha_2(a)\alpha_2(s)
\ll \frac{\ell^{14}}H=O(\ell),
$$
using $\alpha_4(n)$ on the positive regrouping by $n=as$. Finally, inserting the matched Ramanujan term in $B_s$ costs $O(\ell^5 H/Q)$ in absolute sum, by the weighted nonzero Fejér mass bound of 30, $|c_s(r)|\le |r|$, and $\varphi(s)\gg s/\ell$. These errors apply on every subpopulation of the retained pairs.

**Central cap.** Write $A_*=\sqrt{6K}\ell^{128}$ and $T=\ell^{64}$. On the remaining tail $a>A_*$, one has $a>yT^2$ and $a/s>6\ell^{245}$. Factor $a=de$ using its shortest descending-prime prefix $d>T$. Then $d,e>T$. For fixed $s,r$ and root $\xi$ use the matrix $e_s(r\xi\overline{15}\bar d\bar e)$ on units, with $d,e$ in dyadic intervals of sizes $D,F$. Permuting inverse residues and bounding repetitions by $O(1+D/s)$ and $O(1+F/s)$ gives the following norm divided by $\sqrt{DF}$:
$$
\ll \sqrt{(r,s)}
  \left(s^{-1/2}+D^{-1/2}+F^{-1/2}+\sqrt{s/(DF)}\right).
$$
The bracket is $O(T^{-1/2})$ since $s>Q\gg T$, $D,F\ge T/2$ and $DF> sT/4$. The unique prefix condition is a restriction on $d$, together with the row-dependent prime-order prefix $P^+(e)<P^-(d)$. The product window and central cap give a second row-dependent interval. The prefix decomposition from the energy note pays $O(\ell^2)$ for the two masks. Residue classes modulo 5 fix $v$. For each $r$, the supremum plus variation of $F_{K/z}(r/(5s))/s$ on $DF\le z\le4DF$ is $O(K/(DFs))=O(\ell^2)$ on a contributing box. This follows by summing the variations of the individual coefficients $(1-z|j|/K)_+$, which are decreasing in $z$. Partial summation therefore uses the same product-interval bound.

The squared-weight estimate $\sum_{U<d\le 2U}\alpha_2(d)^2\ll\ell^3/U$ follows from the $\tau_4$ convolution in the energy note. Thus the two weight norms cost $O(\ell^3)$ after multiplying by $\sqrt{DF}$. Summing both dyadic indices costs $O(\ell^2)$, summing $s$ and its roots costs at most $\sum_s\alpha_1(s)\rho(s)\ll\ell^2$, and summing the nonzero $r$ costs $O(H^{3/2})$. The central tail of the spectral sum is at most $O(\ell^{11}H^{3/2}T^{-1/2})=O(\ell^{-3/2})$. The absolute Fourier and centering errors above also cover this tail.

The remaining spectrum is exactly the one defining $x_{a,s}$ in the energy note, with $A=\min(K,A_*)$. In total this proves the signed transfer
$$
E_{\rm mix}=\sum_a\alpha_2(a)\sum_s x_{a,s}+O(\ell^{3/2}m).
$$
Assuming the candidate bound $E_H\ll\ell^{4/3}m^{14/3}$, weighted Cauchy–Schwarz and $\sum_a\alpha_2(a)\ll\ell^2$ now give
$$
E_{\rm mix}=O(\ell^{5/3}m^{7/3})=o(\ell^2).
$$

## From the discrepancy to the limit

The combined pure shifted contribution is $O(\ell)$. There are two pure shifted allocations for each nonunit support, each with weight $\alpha_1$ and bounded centered CRT kernel.

To handle the central contribution, replace $V$ by $\bar V=15/4+(45/4)1_{5\mid h}$. The difference is $(15/4)\chi_5(h)$ with the quadratic character modulo 5. On $h=at$, complete blocks of five in $t$ contribute zero to the linear weight, by the zero zeroth and first moments of $\chi_5$. The last block costs $O(a/K)$ for $a\le K$. Both the mean and the actual term vanish for $a>K$. Thus replacing the comb in the central contribution costs $O(K^{-1}\sum_{a\le K}a\alpha_2(a))=O(\ell)$.

Let $\delta=1/15\prod_{7\le p\le y}(1-2/p)$ be the density of survivors and set $g_L(n)=\{L/n\}(1-\{L/n\})n/L$. The exact triangular identity at class zero gives $\mathcal L_K(1_{d\mid h})=g_L(6d)$. Since $15\delta D_y\sum_a\alpha_2(a)=1$, multiplying the central contribution with the replaced comb by $\delta$ gives exactly $\mathbb E g_L(n_{\rm cen})$. Here $n_{\rm cen}$ includes 2 and 3, includes 5 with probability $3/4$, and includes each prime $7\le p\le y$ with probability $2/(p-2)$, independently.

Use the same uniform random number for each prime to couple this law with the model conductor $n_{\rm dec}$ of the variance note. The model uses the same small primes and inclusion probabilities $2/(p-1)$ at $p\ge7$. The expected difference of the two log conductors is bounded by
$$
\sum_{p\ge7}\frac{2\log p}{(p-2)(p-1)}<\infty.
$$
After division by $\log y$, the difference tends to zero in probability. The pinned model law gives $\log n_{\rm dec}/\log y\Rightarrow GD(2)$ with continuous distribution. Hence the same weak limit holds for $n_{\rm cen}$. By Bertrand's postulate, the prime cutoff has $\log L/\log y\to2$ on the primorial diagonal. For $n/L<y^{-\varepsilon}$, $g_L(n)\le y^{-\varepsilon}/4$, and for $n/L>y^\varepsilon$, $g_L(n)=1-L/n$. Letting $\varepsilon\downarrow0$ shows that $\mathbb E g_L(n_{\rm cen})\to\Pr[GD(2)>2]$. [Pinned variance note, Theorems 7–8 and the constant](https://github.com/solveathome/twin-primes/blob/c8fced6cac7008c4a5d06295db2b7dca1ed5eef3/paper/variance-note.md#9-a-decoupled-model-and-its-limit-theorem)

Mertens' estimate gives $\delta\ll\ell^{-2}$ on this diagonal. Thus the pure shifted groups and comb correction vanish after multiplication by $\delta$, while the normalized mixed term is $O(\ell^{-1/3}m^{7/3})$. The exact identity $\operatorname{Var}N_L/\mathbb E N_L=\delta X(L)$ yields the stated conditional limit. The mixed-term rate applies to that component alone.

## Review checkpoints

- Check the shortened shifts and exceptional correlations in the candidate energy proof. The transfer here uses the bound for the original capped spectrum with its comb and matched centering.
- Check the high-product moment and the central-cap estimate above. These are the two range reductions that use more than the pointwise CRT kernel.
- At $L=210$, exact rational evaluation of the physical kernel and a separate enumeration of all role assignments agree on $X=11417/2475$. The centered pieces are $509162/81675$ for the central group, $-832/1485$ for the two pure shifts together, and $-86641/81675$ for the mixed group. This fixture checks the normalization and partition.
