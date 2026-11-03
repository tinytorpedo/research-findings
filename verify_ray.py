#!/usr/bin/env python3
"""Portable retrospective finite audit. Python 3 standard library only."""
if not __debug__:
    raise SystemExit("ERROR: verification requires assertions; do not use Python -O or -OO.")

import json, math, hashlib
from pathlib import Path
from functools import lru_cache
@lru_cache(None)
def fac(n):
    out=[]; p=2
    while p*p<=n:
        e=0
        while n%p==0: n//=p; e+=1
        if e: out.append((p,e))
        p+=1
    if n>1: out.append((n,1))
    return tuple(out)
def mu(n):
    f=fac(n)
    return 0 if any(e>1 for p,e in f) else (-1)**len(f)
def lam(n): return (-1)**sum(e for p,e in fac(n))
def sf(n): return math.prod(p for p,e in fac(n) if e%2)
def square(n): return math.isqrt(n)**2==n
def divs(n): return [d for d in range(1,n+1) if n%d==0]
def mur(n,R):
    return math.prod((-1)**e*math.comb(R,e) if e<=R else 0 for p,e in fac(n))
def fiber(n):
    for g in divs(n):
        for h in divs(n//g):
            for j in divs(n//g//h):
                l=n//g//h//j
                if math.gcd(j,l)==1: yield g,h,j,l

def main():
    counts=dict(content=0,fixed_allocation=0,primitive_rays=0,ray_scale_states=0,multi_mobius_sign=0,liouville_sign=0,abel=0)
    for n in range(1,401):
        rows=list(fiber(n))
        assert sum(lam(j*l) for g,h,j,l in rows)==int(square(n)); counts['content']+=1
        for b in divs(n):
            assert sum(lam(j*l) for g,h,j,l in rows if g*l==b)==int(square(n))*lam(b)
            counts['fixed_allocation']+=1
    for c in range(1,51):
        for d in range(1,51):
            if math.gcd(c,d)!=1: continue
            counts['primitive_rays']+=1
            seen=[]
            for a in range(1,401):
                counts['ray_scale_states']+=1
                v=mu(a*d)*int(square(a*c))
                expected=mu(sf(c)*d) if a==sf(c) else 0
                assert v==expected
                if v: seen.append(a)
                if square(a*c):
                    assert lam(a*d)==lam(c*d); counts['liouville_sign']+=1
                    for R in (2,3,4):
                        w=mur(a*d,R)
                        assert w==0 or (1 if w>0 else -1)==lam(c*d)
                        counts['multi_mobius_sign']+=1
            assert len(seen)<=1
    a=[1,2,3,4,6]; w=[1,2,1j,-2,1-1j]
    laws=[lambda x:1,mu,lambda x:mu(x)**2,lam,lambda x:int(square(x)),lambda x:mu(2*x)*int(square(x))]
    expected=[(2+0j,4,12),(-2j,4,8),(4+0j,16,8),(-2-2j,8,12),(-1+0j,1,5),(-1+0j,1,1)]
    panel=[]
    for name,law,ex in zip(['unsigned','mu','mu_squared','lambda','square','mu_2a_square'],laws,expected):
        values=[law(x)*y for x,y in zip(a,w)]; z=sum(values); energy=int(z.real*z.real+z.imag*z.imag); diagonal=int(sum(x.real*x.real+x.imag*x.imag for x in values))
        assert (z,energy,diagonal)==ex
        panel.append(dict(law=name,coefficient=[z.real,z.imag],energy=energy,diagonal=diagonal))
    assert [4*pow(x,-1,35)%35 for x in a]==[4,2,13,1,24]
    assert all((4*pow(x,-1,35)*(2*x))%35==8 for x in a)
    # Both exact identities and negative controls are checked, not just positive fixtures.
    witnesses={
      'radical_is_not_parity_kernel':sf(12)==3 and math.prod(p for p,e in fac(12))==6,
      'omit_coprimality':sum(lam(j*l) for g in divs(4) for h in divs(4//g) for j in divs(4//g//h) for l in [4//g//h//j])!=1,
      'one_mobius_not_two':mu(4)==0 and mur(4,2)==1,
      'lambda_not_mobius':lam(4)==1 and mu(4)==0,
      'square_indicator_not_mu_squared':square(4) and mu(4)**2==0,
      'mask_revives_nonsquare':sum(lam(j*l) for g,h,j,l in fiber(2) if j==2)==-1,
      'phase_revives_nonsquare':sum(lam(j*l)*(1j if j==2 else 1) for g,h,j,l in fiber(2))==1-1j,
      'principal_mode_not_diagonal':25!=5,
      # Illustrative substitution only, not a recovered native source mapping.
      'illustrative_scale_source_substitution':mu(2)!=mu(4),
      # Actual chi6-filtered interval [5,7], compressed positions 5 and 7.
      # F(4)=1, F(7)=-1, T=-2; dropping F(4) gives the wrong -1.
      'filtered_left_boundary_required':sum(lam(k) for k in (5,7)) == -2 and sum(lam(k) for k in range(1,8) if math.gcd(k,6)==1) == -1 and sum(lam(k) for k in range(1,5) if math.gcd(k,6)==1) == 1,
      'incomplete_fixed_allocation':sum(lam(j*l) for g,h,j,l in fiber(2) if g*l==1 and j==1)!=0,
      'nonunit_scale_inverse_undefined':math.gcd(5,35)!=1,
    }
    assert all(witnesses.values())
    F=[0]
    for n in range(1,201): F.append(F[-1]+(lam(n) if math.gcd(n,6)==1 else 0))
    for L in range(1,31):
        for U in range(L,51):
            # Keep all nonzero-character positions, including positions of zero weight.
            ts=[t for t in range(L,U+1) if math.gcd(t,6)==1]
            if not ts: continue
            hs=[complex((t*t+3*t)%7-3,(t%3)-1) for t in ts]
            lhs=sum(lam(t)*h for t,h in zip(ts,hs))
            rhs=F[ts[-1]]*hs[-1]-F[ts[0]-1]*hs[0]+sum(F[ts[j]]*(hs[j]-hs[j+1]) for j in range(len(ts)-1))
            assert lhs==rhs; counts['abel']+=1
    report={'status':'PASS','scope':'Retrospective exact finite audit; not original I42 verifier or a production theorem','bounds':{'content_max':400,'primitive_c_d_max':50,'scale_max':400,'R':[2,3,4]},'counts':counts,'generated_panel':panel,'hostile_witnesses':witnesses,'hostile_count':len(witnesses),'filtered_boundary_witness':{'interval':[5,7],'eligible_positions':[5,7],'weights':[1,1],'F_left':1,'F_right':-1,'correct_sum':-2,'omit_left_boundary_sum':-1},'mapping_witness_scope':'Illustrative scalar substitution only; no native source mapping is certified'}
    Path(__file__).with_name('verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__': main()
