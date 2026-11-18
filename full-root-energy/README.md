# Candidate bound for the full-root energy

**Status:** Candidate proof, 17 November 2026. Independent review is pending.

The estimate concerns the signed off-diagonal sum for the capped full-root model used in the twin-prime research. The argument below gives
$$
E_H(K,y),\ |R_{\mathrm{far}}(K,y)|
 \ll (1+\log K)^{4/3}\bigl(1+\log(1+\log K)\bigr)^{14/3}
 =o((1+\log K)^2)
$$
uniformly for $y\leq\sqrt{6K}$. The result concerns the model and the masks defined below. The scope of this note ends at the energy estimate.

The [variance transfer](variance-transfer.md) derives the conditional primorial-window variance limit from this energy bound.

## Energy and notation

Let
$$
\ell=1+\log K,\quad m=1+\log\ell,\quad H=\lceil\ell^{13}\rceil,\quad
Q=\min(K,\exp(\ell^{1/4})),\quad A=\min(K,\sqrt{6K}\ell^{128}).
$$
All arithmetic variables carrying weights are squarefree divisors of the product $P_y$ of primes $7\le p\le y$. For these divisors set
$$
\alpha_j(d)=\prod_{p\mid d}\frac{j}{p-4},\qquad
\rho(d)=2^{\omega(d)},\qquad
D_y=\prod_{p\mid P_y}\frac{p(p-4)}{(p-2)^2}.
$$
The weights are zero outside that support. Write $e_q(w)=\exp(2\pi i w/q)$, $e(w)=\exp(2\pi i w)$ and use a bar for the inverse modulo the denominator in question. Let $c_s(r)$ denote the Ramanujan sum and set
$$
F_N(\theta)=\sum_{j\in\mathbb Z}(1-|j|/N)_+ e(j\theta),
\qquad v_j=3(1+\cos(2\pi j/5)).
$$
Write $x_{a,s}=0$ unless $Q<a\le A$, $s>Q$, $(a,s)=1$, and $K/\ell^2<as\le K\ell^{11}$. On that support define
$$
\begin{aligned}
B_s(r,a) &=
 \sum_{\substack{\xi\bmod s\\ \xi^2=1}} e_s(r\xi\overline{15a})
 -\rho(s)c_s(r)/\varphi(s),\\
x_{a,s} &= D_y\frac{\alpha_1(s)}s
 \sum_{0<|r|\le\min(H,(5s-1)/2)}
 v_{r\overline{as}\bmod 5}\,F_{K/a}(r/(5s)) B_s(r,a).
\end{aligned}
$$
Each $x_{a,s}$ is real. Set $S_0=\sqrt{K/6}\,\ell^{-130}$ and
$$
E_H=\sum_a\alpha_2(a)\Big|\sum_s x_{a,s}\Big|^2,\qquad
R_{\mathrm{far}}=\sum_a\alpha_2(a)
 \sum_{\substack{|s-t|>S_0/\ell^6\\(s,t)\le\ell^{10}}}x_{a,s}x_{a,t}.
$$
The inner sum is over ordered pairs. The support implies $s>S_0$.

## Weight and mask estimates

Mertens' estimate gives $\sum_d\alpha_j(d)\ll_j\ell^j$ and $\alpha_1(d)\ll\ell^4/d$. Two useful interval bounds for $1\le U<V$ are
$$
\begin{aligned}
\sum_{U<d\le V}\alpha_1(d)&\ll 1+\log(V/U),\\
\sum_{U<d\le V}\alpha_2(d)&\ll (1+\log V)(1+\log(V/U)).
\end{aligned}
$$
For the first, majorize $\alpha_1$ by the convolution of $1/d$ with the nonnegative squarefree weight of prime values $1/(p-4)-1/p$ at the eligible primes. For the second, use $\tau(d)/d$ and prime corrections $2/(p-4)-2/p$. Both correction weights are summable. Sum $\tau(d)/d$ by writing $d=ij$ and applying the harmonic interval bound to the $j$ sum. The same bounds hold for positive $U<1$ with $V\ge1$. [Mertens' prime reciprocal estimate](https://doi.org/10.1515/crll.1874.78.46)

The kernel $F_N$ is nonnegative for $N\ge1$ as a convex combination of the Fejér kernels at consecutive integer parameters. For $L=5s$, aliasing gives
$$
\frac1L\sum_{r\bmod L}F_N(r/L)=f(N/L),\qquad
F_N(0)=f(N),\qquad
f(z)=z+\frac{\{z\}(1-\{z\})}{z}.
$$
Thus the nonzero residue sum is bounded by $L$. The weighted mass $\sum_r v_{r\overline{as}\bmod5}F_N(r/(5s))/s$ over the admitted nonzero modes is at most 30. In particular, $|x_{a,s}|\le60\alpha_2(s)$.

Each opposite root pair corresponds to a unique coprime split $s=bc$, $b<c$. Choose the root $\xi\equiv1\bmod b$, $\xi\equiv-1\bmod c$. With $A_a=15a$, let $J_b\equiv1\bmod A_a$ and $J_b\equiv2\bmod b$. Additive reciprocity gives
$$
e_{bc}(r\xi\overline{A_a})=
 e_{A_a b}(rJ_b\bar c)\,e(-r/(A_a bc)).
$$
The pair gives twice the real part and has matched centering $2c_s(r)/\varphi(s)$. Squarefreeness gives $|c_s(r)|\le(r,s)\le H$ for the admitted nonzero modes. Since $\varphi(s)\gg s/\ell$, the phase correction and centering can be removed at cost $K^{-1/2}\ell^{O(1)}$ per row, uniformly on any subset of root pairs. Here each centered root-pair contribution has absolute value at most $120\alpha_1(b)\alpha_1(c)$.

For the oscillatory estimates, use dyadic intervals $(B,2B]$ and $(C,2C]$. For fixed $a,b,r$, the product and frequency masks define an interval in $c$. Restricting an arbitrary matrix by a row-dependent interval costs $O(1+\log K)$ in operator norm when the columns lie in the ranges here. To see this, write an interval as a difference of prefixes, decompose each prefix into disjoint dyadic pieces, and group those pieces by level. At a fixed level the distinct pieces have disjoint column sets and disjoint assigned row sets. Each block is a projection of the original matrix. A separate prefix mask in a different column ordering costs the same factor. Split $b,c$ into their residue classes modulo 5 to fix the multiplier $v$. For a nonempty box in the product window, $N/(BC)\ll\ell^2$ with $N=K/a$. The weight $F_N(r/(5x))/x$ has supremum plus variation
$$
\ll \frac N{BC}+|r|\Big(\frac N{BC}\Big)^2
$$
on $BC\le x\le4BC$, by differentiating its finite Fourier sum. Partial summation in $x=bc$ introduces another interval mask in each row. These bounds allow the use of an unweighted matrix norm with the original windows and coefficients.

## Small root factors

Use $T=\ell^{80P}$ with $P$ a sufficiently large absolute constant. First remove the root pairs with $c>yT^2$ and $c>15abT$. Write $c=de$ with $d$ the shortest descending-prime prefix exceeding $T$. Then $d\le yT$ and $e>T$. This decomposition is unique. Its masks are the independent condition $d/P_{\min}(d)\le T$, the prime-order prefix $P_{\max}(e)<P_{\min}(d)$, and product intervals in $e$ for fixed $d$.

At fixed $a,b,r$, use the matrix $e_q(rJ_b\bar d\bar e)$ on units modulo $q=15ab$, in dyadic boxes of lengths $D,F$. The full matrix on residues before restriction and inverse permutations has norm $\sqrt{q(r,q)}$. Repeated residues in the intervals cost factors $O(\sqrt{1+D/q}\sqrt{1+F/q})$. After dividing the norm by $\sqrt{DF}$ the bound is
$$
\ll\sqrt{|r|}\left(q^{-1/2}+D^{-1/2}+F^{-1/2}+\sqrt{q/(DF)}\right).
$$
On a contributing box all four terms in parentheses are $O(T^{-1/2})$. The weight norms are $\ll\ell^4/\sqrt D$ and $\ll\ell^4/\sqrt F$. Apply the interval and prime-order mask bounds and partial summation in $x=bde$. Summing the boxes, frequencies and $\alpha_1(b)$ costs a fixed power of $\ell$, so the removed rows have negligible weighted norm.

In a remaining box with $B<T$, we have $b\le2T$, which implies $a\gg\sqrt K/(\ell^2 T^3)$. Indeed $abc>K/\ell^2$, while $c\le\max(yT^2,15abT)$. The resulting $a$ interval has $\alpha_2$-mass $O(\ell m)$. For fixed $a$ the small-$b$ mass is $O(m)$, and for fixed $a,b$ the $c$-mass is $O(m)$ by its product-window ratio $\ell^{13}$. Thus the small-$b$ component has energy $O(\ell m^5)$. The subsequent estimates concern the boxes with $B\ge T$.

## A correlation estimate with two independent shifts

Restrict the oscillatory calculation to $\omega(a),\omega(b)\le100\log\ell$. The omitted weights have mass $\ll_j\ell^{2j-100\log 2}$ under $\alpha_j$, by weighting the Euler product with $2^{\omega}$. Combined with the root-pair bound, this gives a negligible weighted norm for the excluded $a$ and $b$ tails.

Use rows $b$ coprime to $a$ and the unweighted dyadic column interval $I=(C,2C]\cap\mathbb Z$. Set $M_{b,c}=e_{15ab}(rJ_b\bar c)$ when $(c,15ab)=1$ and set it to zero otherwise. The physical weights and row-dependent interval masks are applied after estimating this matrix. The row correlation for distinct $b=gu$ and $b'=gv$, $g=(b,b')$, is an interval sum of $e_L(n\bar c)$ on units, where
$$
L=15aguv,\qquad n=r(J_bv-J_{b'}u).
$$
The factors $15ag,u,v$ are pairwise coprime and squarefree, and
$$
(n,uv)=(r,uv),\qquad (n,15ag)=(r(v-u),15ag).
$$
### The two shift inequalities

Let $z(c)=e_L(n\bar c)$ when $c\in I$ and $(c,L)=1$, with $z(c)=0$ elsewhere. Put $S=\sum_c z(c)$. For a function $f$ of modulus at most 1 supported on an integer interval of length $O(C)$, write $S_f=\sum_c f(c)$. If the shift step is $d_0$ and $Jd_0\ll C$, then
$$
J S_f=\sum_c\sum_{i=1}^{J} f(c+i d_0).
$$
The outer support has size $O(C)$. Cauchy–Schwarz bounds $J^2|S_f|^2$ by $O(C)$ times the sum of squares of the inner sums. Expanding those squares gives
$$
\frac{|S_f|^2}{C^2}\ll
 \frac1J+\frac1J\sum_{j=1}^{J-1}
 \frac{\left|\sum_c f(c+j d_0)\overline{f(c)}\right|}{C}.
$$
The diagonal contributes $J\sum_c |f(c)|^2\ll JC$. The correlation at shift $j d_0$ occurs with multiplicity $J-j$ before taking absolute values.

Take $q_1\mid u$, $q_2\mid v$, and write $Q_0=q_1q_2$ and $q=L/Q_0$. Assume $J\max(q_1,q_2)\ll C$, with $J=\lfloor\ell^{16P}\rfloor$. Apply the inequality first with $f=z$ and $d_0=q_1$. For $h_1=j_1q_1$, the first correlation is the sum of
$$
z_{h_1}(c)=z(c+h_1)\overline{z(c)}
$$
over $I\cap(I-h_1)$. Apply the inequality again to $z_{h_1}$ with $d_0=q_2$, using the same ambient scale $C$ even if the intersection is short. For $h_2=j_2q_2$ the second correlation is
$$
S_2(j_1,j_2)=\sum_c z_{h_1}(c+h_2)\overline{z_{h_1}(c)}.
$$
Its interval is $I\cap(I-h_1)\cap(I-h_2)\cap(I-h_1-h_2)$. The term is supported where all four shifted arguments are units modulo $L$. If $|S_2(j_1,j_2)|\ll C\varepsilon$ throughout, the second inequality bounds the normalized first correlations by $O((J^{-1}+\varepsilon)^{1/2})$. Substituting that result into the first inequality gives $|S|/C\ll J^{-1/4}+\varepsilon^{1/4}$. [Arithmetic differencing](https://arxiv.org/html/1403.8031)

### Completion on the remaining modulus

Write $\mathcal H=\{0,h_1,h_2,h_1+h_2\}$ for the offsets in the unit conditions. The second correlation has positive reciprocal terms at $0$ and $h_1+h_2$ and negative terms at $h_1$ and $h_2$, with multiplicities included. The component at $q_1$ vanishes because $h_1$ is a multiple of $q_1$. The component at $q_2$ vanishes because $h_2$ is a multiple of $q_2$. By CRT the exponential on the remaining modulus is $e_q(n\overline{Q_0}\Delta_q(c))$, where
$$
\Delta_q(c)=\overline{c+h_1+h_2}-\overline{c+h_1}
-\overline{c+h_2}+\bar c\pmod q
$$
on the four $q$-unit arguments.

For each $p\mid Q_0$ the four unit conditions exclude the classes $\{-h\bmod p:h\in\mathcal H\}$, at most two distinct classes because one shift is zero modulo $p$. Expanding the product of the allowed-class indicators gives at most $3^{\omega(Q_0)}$ signed progressions $c=c_0+dt$ with $d\mid Q_0$ and $(d,q)=1$. On each such progression define the $q$-periodic function $\Phi(t)=e_q(n\overline{Q_0}\Delta_q(c_0+dt))$ on the four $q$-unit arguments and set it to zero elsewhere. Let $I_d$ denote the integer interval in $t$ cut out by the four original intervals. Then $|I_d|=O(C/d+1)$. With
$$
\widehat\Phi(k)=\sum_{t\bmod q}\Phi(t)e_q(-kt),
$$
the sum on this progression is exactly
$$
\frac1q\sum_{k\bmod q}\widehat\Phi(k)\sum_{t\in I_d}e_q(kt).
$$
The zero Fourier mode contributes $|I_d|/q$ to the normalized sum of the absolute interval coefficients. For $0<k<q$, geometric summation bounds the interval coefficient by $O(q/\min(k,q-k))$. Hence the normalized sum over all modes is $O(C/(dq)+\log(2q))$.

Because $q$ is squarefree, CRT factors $\widehat\Phi(k)$ into prime-modulus sums. At $p\mid q$ with $p\nmid nj_1j_2$, both shifts are nonzero modulo $p$. If $h_1+h_2\ne0\bmod p$, the unshifted reciprocal has a unique pole. If $h_1+h_2=0\bmod p$, the two nonzero shifts give distinct poles since $p$ is odd. This simple pole persists under the invertible affine change $c=c_0+dt$ and the linear Fourier twist. It verifies the nondegeneracy condition for the rational-function Weil bound. There are at most four simple finite poles and at most a simple pole at infinity, so the local bound is $O(\sqrt p)$ with an absolute constant. Any additional points excluded by the unit conditions cost at most four terms. At a prime dividing $nj_1j_2$ use the trivial bound $p$. Thus for an absolute $C_0$,
$$
|\widehat\Phi(k)|\ll C_0^{\omega(q)}\sqrt{q(q,nj_1j_2)}
$$
uniformly in $k$. [Rational-function Weil bound, Theorem 1.1](https://www.math.ksu.edu/~cochrane/research/stepmix.pdf)

Summing the progression bounds and using $d\ge1$ gives
$$
|S_2(j_1,j_2)|\ll
\ell^P\sqrt{(q,nj_1j_2)}
\left(\frac C{\sqrt q}+\sqrt q\right).
$$
The fixed power $\ell^P$ absorbs the factors $3^{\omega(Q_0)}C_0^{\omega(q)}\log(2q)$ because $\omega(L)\le300\log\ell+2$ and $\log(2L)\ll\ell$. This choice is independent of the exponents in the shift and length thresholds.

### From correlations to the matrix norm

Set $G=\ell^{16P}$. For fixed $b$, the number of rows with $g>G$ or $(15ag,n)>G$ is $O(\ell^P(BH/G+1))$. The first count uses multiples in $(B,2B]$ of each divisor of $b$ exceeding $G$. For the second count, fix $g\mid b$ and a divisor $d>G$ of $15ag$. The condition $d\mid r(v-u)$ restricts $v$ to one class modulo $d/(d,r)>G/H$. There are at most $O(BH/(gG)+1)$ possibilities in the interval for $v$. The number of divisor choices is bounded by a fixed power of $\ell$ using the restrictions on $\omega(a)$ and $\omega(b)$.

Bound the exceptional correlations and the diagonal by $O(C)$. If the other rows satisfy $|S_2|\ll C\varepsilon$, the absolute row sums of $MM^*$ give
$$
\frac{\|M\|_{\mathrm{op}}^2}{BC}
\ll \frac1B+\ell^P\left(\frac HG+\frac1B\right)
     +J^{-1/4}+\varepsilon^{1/4}.
$$
With $B\ge T=\ell^{80P}$ and $\varepsilon=\ell^{-16P}$, this yields $\|M\|_{\mathrm{op}}\ll\sqrt{BC}\,\ell^{-2P}$. Apply the original masks and the $\ell^2$ norms of the weights, bounded by $O(\ell^4/\sqrt B)$ and $O(\ell^4/\sqrt C)$. The mask decomposition, variation, frequencies and dyadic summation cost fixed powers of $\ell$ independent of $P$. Taking $P$ sufficiently large gives a row estimate of $O(\ell^{-P})$.

## The two applications of the correlation estimate

First use $q_1=u$, $q_2=v$, hence $q=15ag$. This applies to boxes with $C\ge T\max(B,\sqrt a)$. Apart from the counted exceptions, the twice-shifted bound divided by $C$ is
$$
\ll \ell^P J\left(\sqrt{G/a}+G\frac{\sqrt a}{C}\right)\ll\ell^{-16P}.
$$
For those pairs, $(q,nj_1j_2)\le GJ^2$ and $15a\le q\le15aG$, giving the two displayed terms. The first is smaller than any fixed inverse power of $\ell$ since $a>Q$. The second is $O(\ell^P JG/T)=O(\ell^{-47P})$. The shift lengths are $O(JB)$ and fit in $O(C)$.

In all remaining boxes $c/b\ll T^2\ell^{258}$. If $C<TB$, use $c\le2C$ and $b>B$. If $C<T\sqrt a$, then $c/b=ac^2/(abc)\ll T^2 a^2\ell^2/K\ll T^2\ell^{258}$. For fixed $a$, this and the product window place $b$ in an interval within factors $\ell^{O(1)}$ of $\sqrt{K/a}$. There are $O(m)$ dyadic $b$ intervals, and the product window gives $O(m)$ mass for $c$ per $b$. Thus the remaining rows are $O(m^2)$.

Put $L_*=(\ell m^2)^{1/3}$. The strip $a>\sqrt K e^{-L_*}$ has $\alpha_2$-mass $O(\ell L_*)$, so its energy in the remaining boxes is $O(\ell L_*m^4)$.

For $a\le\sqrt K e^{-L_*}$, select one prime $p_b\mid b$ in $[\ell^{32P},e^{L_*/4}]$ whenever possible. The choice depends only on $b$. For nonexceptional pairs with both selected primes, take $q_1=u/p_b$, $q_2=v/p_{b'}$. Since the selected primes exceed $G$, neither is in $g$, and they are distinct. They exceed $H$ as well, so the congruences for $n$ show $(q,n)=(15ag,n)$ with $q=15agp_bp_{b'}$. The earlier exceptional-row count therefore applies. A box with $b<c$ has $C\ge B$, so the shorter shifts fit because $J\max(q_1,q_2)\ll JB/\ell^{32P}$. An active box has $C^2>K/(4a\ell^2)$, giving
$$
\frac{\sqrt q}{C}\ll \ell\sqrt G\,\frac a{\sqrt K}e^{L_*/4}
 \le\ell\sqrt G\,e^{-3L_*/4}.
$$
Again $(q,nj_1j_2)\le GJ^2$. After division by $C$, the part from $C/\sqrt q$ is $O(\ell^PJ\sqrt{G/a})$, which is smaller than any fixed inverse power of $\ell$. The part from $\sqrt q$ is $O(\ell^{33P+1}e^{-3L_*/4})$. Thus the shortened shifts give the same $O(C\ell^{-16P})$ bound for the twice-shifted sum and negligible weighted norm.

## Sifted factors and recombination

The remaining $b$ have no prime divisor in $[\ell^{32P},e^{L_*/4}]$. Their dyadic intervals have size at least $K^{1/5}/2$ eventually, from the comparable-factor restriction and the cap on $a$. The ordinary upper-bound sieve gives density $O(m/L_*)$ on each such interval. Specifically, truncate inclusion–exclusion at an even $k=O(\log\ell)$ with a sufficiently large fixed constant. The omitted reciprocal sums are $O(\ell^{-100})$ because the prime reciprocal mass is $O(\log\ell)$ and the $j$th elementary symmetric sum is bounded by that mass to the $j$th power divided by $j!$. The number of rounding errors is $\exp(O(L_*\log\ell))=K^{o(1)}$. Mertens' estimate gives the sieve product $O(m/L_*)$. [Mertens' prime reciprocal estimate](https://doi.org/10.1515/crll.1874.78.46)

This also bounds the $\alpha_1$-mass by $O(m/L_*)$ per box. Use the convolution with $1/d$ above, whose correction has finite moment of order $1/2$. Correction divisors at most the square root of the box size leave intervals large enough for the same rounding-error bound. Larger correction divisors cost a power-saving tail by the finite moment. The product window and comparable-factor restriction now give $O(m^3/L_*)$ per row. This component has energy $O(\ell^2m^6/L_*^2)$.

Combine the components with the triangle inequality in the weighted row norm $\|f\|^2=\sum_a\alpha_2(a)|f(a)|^2$. This pays all cross terms. The result is
$$
E_H\ll\ell m^5+\ell L_*m^4+\frac{\ell^2m^6}{L_*^2}
 \ll\ell^{4/3}m^{14/3}.
$$

For the comparison to $R_{\mathrm{far}}$, the positive tail bound
$$
\sum_{s>Z}\alpha_2(s)^2\ll\frac{(1+\log Z)^3}{Z}
$$
follows by majorizing $s^2\alpha_2(s)^2$ by $\tau_4$ convolved with a nonnegative correction of prime values $4p^2/(p-4)^2-4$ and using partial summation. By $|x_{a,s}|\le60\alpha_2(s)$, the conductor diagonal has size $O(\ell^5/S_0)$. For pairs with $0<|s-t|\le S_0/\ell^6$, the inequality $2|xy|\le |x|^2+|y|^2$ and the number of neighbors give $O(\ell^{-1})$. Finally, sum over common divisors $g>\ell^{10}$, using $\alpha_2(gd)=\alpha_2(g)\alpha_2(d)$ for coprime supported factors. The absolute bound is $O(\ell^6\sum_{g>\ell^{10}}\alpha_2(g)^2)=O(\ell^{-4}m^3)$. Thus $R_{\mathrm{far}}=E_H+O(\ell^{-1})$, as claimed.
