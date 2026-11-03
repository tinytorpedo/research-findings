# Source transcription

Complete 66-line extracted text of REPORT(20260922-203312).md, read from the supplied research files on 3 November 2026. Line endings are normalized. This is a text transcription, not a byte-identical source copy. Historical verification claims have not been independently rerun; the current inspection status of supporting records is documented in SOURCE_COVERAGE.md.

# I109 — explicit source weights and the bound they require

**Independent reconstruction audit: PASS.** A new smooth source cover and
its P/U/O ownership are fully defined. The unknown legacy production
weights and theorem-complement owner have not been recovered.

The cover is a normalized compact-bump grid with denominator
**D(u)>=exp(-4/3)** at every point. It has a complete tensor cover and
derivative bounds C_r R^r. All children of an owned history are retained,
so each of the four sibling responses reconstructs that source owner exactly.
The general-scale packet convention is explicitly new; at R=126 it agrees
with I106–I108. These weights have exact analytic definitions and support
certificates; no floating-point zero or opaque weight is used.

Verified 6,672 existing ordered histories with 427,008
bound tensor children, 4,350 exact coordinate certificates,
63 complete small HB sources and 5,920 histories.
The small check uses independent prime allocations and U^j*Lambda
convolution, retaining 9 higher prime powers, both small-prime
exceptions and 186 Gram entries. Native owner counts: {'PACKET': 3266, 'POST_PACKET': 3406}.
No new cancellation slice was measured.

Actual hits and weight differences survive in the general formula:

    T = K*S + sum_s K_s*(S_s-S).

The controls include 17 cases with actual divisibility hits,
33 cases where replacing the four responses by one is wrong,
and 16 endpoint-asymmetry cases. The tested no-hit constant
multiplier from I108 has not been extended to all production data.

For the full ordered HB2 family the exact reduction is

    T_X = sum_(a,n) A_Q(a) mu(a) sum_d chi6(d) lambda(d) G_(a,n)(d).

Here G keeps factor-split multiplicities, the distinguished log role,
actual hits, endpoints and the actual supplied sibling weights. Discrete
partial summation proves the uniform bound

    |T_X| <= sum_(a,n) |A_Q(a)| M6(I_t) V(G_(a,n)),

where M6 is the maximum absolute projected Liouville prefix on the precise
d interval and V(G)=|G(U)|+sum_d |G(d+1)-G(d)|. The coefficient identity
passed 576 checks across 16 declared rational kernels.
This inequality is exact and uniform, but it supplies **no small-o saving**.
Smooth source bumps do not remove the arithmetic jumps in G.

Domain clarification: the outer ordered n pairs satisfy gcd(n1*n2,6)=1,
as specified in WEIGHT_BINDING.md. Empty d intervals contribute zero.

An unrestricted sign-selecting two-owner control has selected sums
14 and -33, total variation 47. Both owners are bounded and
recombine exactly, yet each has no internal sign cancellation. Thus
partition-of-unity and boundedness alone cannot justify the needed saving.
This is an adversarial control, not the actual production ownership.

**Remaining bridge:** transport the published-removal and rough-source
organization into this explicit cover, identify its actual retained-child
selector q_(s,c), and bound the resulting weighted discrepancy/variation.
No legacy production fields were filled with these new choices. No full
growing population, separated W_D/F estimate, or prime-count bound is claimed.

WEIGHT_BINDING.md gives definitions and proofs; PRETEST.md and
EXECUTION_SEAL.json predate execution; REPRODUCE.md gives commands.
Machine records preserve all supports, histories, signed controls and checks.
174 sealed files remained unchanged. Audit completed 2026-09-22T20:12:18.544214+00:00.

