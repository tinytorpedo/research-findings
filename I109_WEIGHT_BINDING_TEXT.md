# Source transcription

Complete original WEIGHT_BINDING.md text, read from the research project on 3 November 2026. No personal absolute paths occurred in this text, so no substantive redactions were needed. This is a message-transmitted text transcription with normalized line endings, not a byte-identical file copy. The original byte hash is recorded in SOURCE_COVERAGE.md. The source's historical verification is not rerun here.

# I109 — an explicit smooth source cover and its exact analytic burden

This is a NEW definition, not recovery of the missing legacy production
weights. It completes the smoothing and P/U/O ownership of the I106–I108
source family for every macroblock scale. It does not identify that family
with the full theorem-complement residual in frontier Eq. (41).

## 1. A complete cover with a uniform positive denominator

Let X=25*4^k, k>=0, R=floor(log2 X)=2k+4, and

    b(t)=exp(-1/(1-t^2)) for |t|<1; b(t)=0 otherwise,
    D(u)=sum_{j in Z} b(u-j),
    theta_j(x)=b(R*x-j)/D(R*x).

At most two summands are positive at any point. Some integer lies within
1/2 of u, so D(u)>=exp(-4/3)>0 everywhere. Thus sum_j theta_j(x)=1 exactly,
0<=theta_j<=1, and the cover includes its outer neighboring cells. No
truncated edge denominator or unspecified normalization remains.

D is positive, smooth and 1-periodic. For every fixed derivative order r,
the derivatives of theta_j obey |theta_j^(r)(x)|<=C_r R^r uniformly in
x,j,X. The constants exist by compactness on the support and D's lower
bound; they are not numerical constants supplied to a published theorem.

For h=(j,m_1,...,m_j,n_1,...,n_j), N=product of its roles, define

    x(a,h)=(log(a), log(N), log(m_1),...,log(m_j),
                            log(n_1),...,log(n_j))/log(X),
    Omega_c(a,h)=product_l theta_{c_l}(x_l(a,h)).

This is an explicit locally finite smooth tensor, with sum_c Omega_c=1,
nonnegative weights, and at most 2^(2j+2) active children. Integer power
comparisons locate the supports exactly: floor(R log(v)/log(X))=z iff
X^z<=v^R<X^(z+1). At equality only child z has positive weight.
The complete tensor is defined on all factor, modulus and N coordinates;
hard endpoint indicators are retained separately in K below. In particular,
we do not multiply an endpoint cutoff into the coefficient twice.

## 2. Explicit raw-source ownership at every scale

Keep the I106 source predicate F_X(h). It requires j=2 and, for B=X and N,

    B^123 < m_i^500,   m_i^125 < B^31,
    B^63  < n_i^250,   n_i^500 < B^127.

The Mobius roles remain separately squarefree in the HB coefficient. No
source-source coprimality restriction is added. Put

    z_m=floor(R*(1/4-log(m)/log(N))+1/2),
    z_n=floor(R*(log(n)/log(N)-1/4)+1/2),
    z_*(R)=floor(R/500-1/2)+1.

The declared growing source family U consists of F_X histories outside
the single packet z=(z_*,z_*,z_*,z_*). Define P as that packet and O=1-F_X.
For R=126 this is exactly the existing I79/I106 P/U/O rule. Choosing the
least clipped diagonal packet at other scales is an EXPLICIT new extension;
no quantitative estimate for that packet or its complement is assumed.

Give every child (a,h,s,c) its parent's one owner b in {P,U,O}. Retain ALL
smoothing children of that owned history on every sibling. With chi6(N)
applied upstream, the owned response is

    rho_{s,c,b}(a,h)=chi6(N) * 1[owner(h)=b] * Omega_c(a,h).

Hence sum_c rho_{s,c,b}=chi6*1[owner=b] for EACH sibling. This deliberately
defines a common completed source response; it is not evidence that the
unknown legacy residual selector keeps the same children on all siblings.

Retain the full j=1,2,3 HB expansion with M=floor((128X)^(1/3)). Attach the
negative higher-prime-power correction to O as a separate, explicitly
tagged source term, with the same chi6, endpoints and its own (a,N) cover.
Then P+U+O reconstructs chi6*(Lambda/log-PP), hence the prime indicator for
N>3. The primes 2 and 3 require their explicit exception terms. Individual
selected P or U responses are not asserted to vanish.

## 3. The four siblings and actual hits

For s=(epsilon,kappa), epsilon=+-1, kappa=1 or 3, retain

    K_s(a,N)=1[N in J_epsilon(a)] * sign_kappa *
        (1[kappa*a | N-2epsilon]-1[gcd(N,kappa*a)=1]/phi(kappa*a)),
    sign_1=+1, sign_3=-1.

The endpoint is the existing ordinary interval: lower bound is the smallest
integer congruent to epsilon modulo 6 at least max(p^2+5+epsilon,a+2epsilon),
and upper bound is q^2-1+epsilon. The congruence adjusts that lower bound;
it does NOT impose a residue mask on every N inside the interval.

For this completed new source cover, T_b=(sum_s K_s) S_b exactly. Every
divisibility hit and endpoint is retained. On the both-lane, wheel-coprime,
chi6-admitted interior, sum_s K_s=H_a(N)-1/phi(a). I108's further H_a=0
simplification holds only on its checked data, not on the growing family.

For an actual residual selector q_{s,c}(a,h), the required response instead is

    W_s(a,h)=sum_c Omega_c(a,h) q_{s,c}(a,h),
    S_s=sum_h c(h) chi6(N) W_s(a,h),
    T=sum_s K_s S_s = K*S + sum_s K_s*(S_s-S).

This retains any difference between sibling responses. It also retains n
ordering: log(n1) and log(n2) cannot be averaged unless their weights have
the required permutation symmetry. Common smoothing alone does not prove
either ownership symmetry or equality of the completed responses.

## 4. A uniform, exact reduction to a weighted Liouville bound

For one band, let its full endpoint union be contained in [A,B]. Sum over
every admitted wheel a and ALL ordered n1,n2 in the declared source windows,
not offsets about sample centers. Put t=n1*n2 and I_t=[ceil(A/t),floor(B/t)].
For any supplied responses (including their source support and ownership),
define on this full d interval

    G_{a,n}(d) = -3*log(n1)/log(dt)
        * sum_{m1*m2=d; m_i squarefree, m_i<=M}
            sum_s K_s(a,dt) W_s(a,m1,m2,n1,n2).

Set invalid source weights to zero. Because mu(m1)mu(m2)=lambda(d), the
projected HB2 sum is exactly

    T_X = sum_{a,n; gcd(t,6)=1} A_Q(a)mu(a)
               * sum_{d in I_t; gcd(d,6)=1} lambda(d) G_{a,n}(d).

This identity permits shared primes between m1,m2. For the explicit family
above, W_s=1[owner=U] after the complete cover is summed. For a residual
family W_s must include its actual owned-child selector. The same identity
holds, but those W_s are not inferred from a count of factor splits.

Write I_t=[L,U],

    L6(v)=sum_{L<=d<=v; gcd(d,6)=1} lambda(d),
    M6(I_t)=max_{L<=v<=U}|L6(v)|,
    V(G)=|G(U)|+sum_{d=L}^{U-1}|G(d+1)-G(d)|.

Exact discrete partial summation gives

    sum lambda(d)chi6(d)G(d)
      = L6(U)G(U)+sum_{d=L}^{U-1} L6(d)*(G(d)-G(d+1)).

Consequently, uniformly for every finite band, wheel and supplied kernel,

    |T_X| <= sum_{a,n; gcd(t,6)=1} |A_Q(a)| M6(I_t) V(G_{a,n}).

This is a proven variation bound, NOT an o(M_k) estimate. Its right side
can be as large as the original absolute sum or larger. Smoothness of Omega
does not control the jumps from factor-split counts, ownership, endpoints
or actual divisibility hits inside G. Nor does an estimate on long ordinary
Liouville sums automatically control these short shifted intervals.
The signed outer sum may permit stronger estimates than this triangle bound.

Positivity, boundedness and reconstruction alone cannot supply cancellation:
q_+(d)=1[lambda(d)=+1], q_-=1-q_+ are a complete two-owner partition, but
the q_+ selected sum has only positive terms. This is an adversarial
unrestricted-owner example, not a claim about the real production selector.

## What this binds

Closed by definition/proof: a uniformly normalized smooth source tensor,
its complete P/U/O ownership, all signed siblings, exact reconstruction,
and a uniform variation inequality with actual hits retained.

Still open: transport of the frontier's full-source removals and rough
expansion into this new cover; the actual theorem-complement q_{s,c};
any separated W_D/F norm/representation required by an analytic estimate;
and a bound on the displayed quantity strong enough for the required growing
residual. No legacy production field is overwritten and no prime-count
bound, asymptotic saving or production cancellation is claimed.

