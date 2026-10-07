# Numerical checks of Lemmas 4.2, 4.3, 4.4 (Gauss sums, quadratic phase, sextic reciprocity)
# Elements of O = Z[w], w = exp(2 pi i/3), are pairs (a, b) = a + b w.
import cmath, math, random, itertools
from math import gcd
W = cmath.exp(2j*math.pi/3)
def mul(x, y): a,b = x; c,d = y; return (a*c - b*d, a*d + b*c - b*d)
def conj(x): a,b = x; return (a - b, -b)
def norm(x): a,b = x; return a*a - a*b + b*b
def cx(x): return x[0] + x[1]*W
def sub(x, y): return (x[0]-y[0], x[1]-y[1])
def divides(m, z):
    u, v = mul(z, conj(m)); n = norm(m); return u % n == 0 and v % n == 0
def reduce(z, m):
    u, v = mul(z, conj(m)); n = norm(m)
    q = (round(u/n), round(v/n)); return sub(z, mul(q, m))
def powmod(z, e, m):
    r = (1, 0); z = reduce(z, m)
    while e:
        if e & 1: r = reduce(mul(r, z), m)
        z = reduce(mul(z, z), m); e >>= 1
    return r
UNITS = {(1,0):1, (1,1):cmath.exp(1j*math.pi/3), (0,1):W, (-1,0):-1, (-1,-1):W**2, (0,-1):-W}
def is_primary(x): return x[0] % 3 == 1 and x[1] % 3 == 0
def primary(x):
    for u in UNITS:
        y = mul(u, x)
        if is_primary(y): return y
    raise ValueError
def chi_p(a, p):
    """sextic symbol (a/p)_6 for a primary prime p (outside 6): complex sixth root of unity, 0 if p | a"""
    if divides(p, a): return 0
    t = powmod(a, (norm(p) - 1)//6, p)
    for u, val in UNITS.items():
        if divides(p, sub(t, u)): return val
    raise RuntimeError("no unit matched")
def chi(a, factors):
    r = 1
    for p in factors: r *= chi_p(a, p)
    return r
def residues(c):
    a, b = c; n = norm(c); B = gcd(abs(b), abs(a - b)); A = n // B
    for xx in range(A):
        for yy in range(B): yield (xx, yy)
def e_of(v, c):
    s, t = mul(v, conj(c)); n = norm(c); return cmath.exp(2j*math.pi*(t % n)/n)
def prod(fs):
    r = (1, 0)
    for f in fs: r = mul(r, f)
    return r
def gamma_j(j, factors):
    c = prod(factors); n = norm(c); tot = 0
    for v in residues(c):
        ch = chi(v, factors)
        if ch == 0: continue
        tot += ch**(j % 6) * e_of(v, c)
    return tot / math.sqrt(n)
def Gamma(c):
    n = norm(c); tot = sum(e_of(mul(x, x), c) for x in residues(c))
    return tot / math.sqrt(n)
def Gamma_formula(c):
    a, b = c; i = 1j; return (1 + i**(-b) + i**a + i**(b - a))/2
def alpha(c): z = cx(c); return z/abs(z)
# primes
def split_primes(limit):
    out = []
    for p in range(7, limit):
        if all(p % q for q in range(2, int(p**0.5)+1)) and p % 3 == 1:
            for a in range(-p, p+1):
                found = False
                for b in range(-p, p+1):
                    if a*a - a*b + b*b == p:
                        pi = primary((a, b)); out += [pi, primary(conj(pi))]; found = True; break
                if found: break
    return out
def inert_primes(limit):
    return [primary((p, 0)) for p in range(5, limit) if all(p % q for q in range(2, int(p**0.5)+1)) and p % 3 == 2]
results = {}
def check(name, cond):
    results.setdefault(name, [0, 0]); results[name][0 if cond else 1] += 1
TOL = 1e-8
primes = split_primes(140) + inert_primes(40)
print("primes tested:", len(primes), "norms up to", max(norm(p) for p in primes))
four = (4, 0)
for p in primes:
    g = {j: gamma_j(j, [p]) for j in range(1, 6)}
    H4 = chi_p(four, p)
    check("L4.2  |gamma_j(p)| = 1, j=1..5", all(abs(abs(g[j]) - 1) < TOL for j in g))
    check("L4.2  gamma_2(p)^3 = -alpha(p)", abs(g[2]**3 + alpha(p)) < TOL)
    check("L4.2  gamma_1 gamma_2 = conj(H(4)) gamma_3 gamma_2^3", abs(g[1]*g[2] - H4.conjugate()*g[3]*g[2]**3) < TOL)
    check("L4.4  R(p,p) = gamma_3(p)^2 = chi_p(-1)",
          abs(g[3]**2 - chi_p((-1, 0), p)) < TOL and abs(Gamma(mul(p, p))/(Gamma(p)**2) - g[3]**2) < TOL)
    G_p3 = complex(chi(four, [p, p, p])).conjugate() * Gamma(prod([p, p, p])) if norm(p) < 200 else None
    if G_p3 is not None:
        check("L4.4  G(p^3) = gamma_3(p)", abs(G_p3 - g[3]) < TOL)
    Gv2 = complex(chi(four, [p, p])).conjugate() * Gamma(mul(p, p))
    check("L4.4  G(v^2) = chi_v(4)  (v = p)", abs(Gv2 - H4) < TOL)
# Lemma 4.3 on random odd elements (not necessarily primary or squarefree)
random.seed(1)
cnt = 0
while cnt < 300:
    c = (random.randint(-25, 25), random.randint(-25, 25))
    if c == (0, 0) or (c[0] % 2 == 0 and c[1] % 2 == 0) or norm(c) > 900: continue
    cnt += 1
    check("L4.3  Gamma(c) four-term formula (random odd c)", abs(Gamma(c) - Gamma_formula(c)) < TOL)
    v = (random.randint(-5, 5), random.randint(-5, 5))
    if (v[0] % 2 or v[1] % 2) and norm(mul(c, mul(v, v))) < 4000:
        check("L4.3  Gamma(c v^2) = Gamma(c)", abs(Gamma(mul(c, mul(v, v))) - Gamma(c)) < TOL)
lam = (1, 2)
check("L4.3  table Gamma(1)=1, Gamma(-1)=1, Gamma(lambda)=i, Gamma(-lambda)=-i",
      abs(Gamma((1,0)) - 1) < TOL and abs(Gamma((-1,0)) - 1) < TOL and abs(Gamma(lam) - 1j) < TOL and abs(Gamma((-1,-2)) + 1j) < TOL)
def r(a, b): return Gamma(mul(a, b))/(Gamma(a)*Gamma(b))
for e_, f_, g_, h_ in itertools.product([0,1], repeat=4):
    A = mul(((-1)**e_, 0), (1,0) if f_ == 0 else lam); B = mul(((-1)**g_, 0), (1,0) if h_ == 0 else lam)
    check("L4.3  r((-1)^e l^f, (-1)^g l^h) = (-1)^(eh+fg+fh)", abs(r(A, B) - (-1)**(e_*h_ + f_*g_ + f_*h_)) < TOL)
# Lemma 4.4: sextic reciprocity and G multiplicativity, on primes and squarefree composites
small = [p for p in primes if norm(p) < 120]
for p, q in itertools.combinations(small, 2):
    if norm(p) == norm(q) and p == conj(q): pass
    lhs = chi_p(p, q); rhs = r(p, q) * chi_p(q, p)
    check("L4.4  sextic reciprocity chi_q(p) = r(p,q) chi_p(q)  (prime pairs)", abs(lhs - rhs) < TOL)
    G = lambda fs: complex(chi(four, fs)).conjugate() * Gamma(prod(fs))
    check("L4.4  G(pq) = G(p) G(q) R(p,q)", abs(G([p, q]) - G([p])*G([q])*r(p, q)) < TOL)
# composite reciprocity and (4.7) for squarefree c = p q with N(pq) small
pairs = [(p, q) for p, q in itertools.combinations(small, 2) if norm(p)*norm(q) <= 3000][:40]
for p, q in pairs:
    c = mul(p, q)
    g = {j: gamma_j(j, [p, q]) for j in (1, 2, 3)}
    mu = 1  # two distinct primes
    Gc = complex(chi(four, [p, q])).conjugate() * Gamma(c)
    check("(4.7) gamma_2(c)^3 = mu(c) alpha(c), c = pq", abs(g[2]**3 - mu*alpha(c)) < TOL)
    check("(4.7) gamma_1 gamma_2 = mu alpha G, c = pq", abs(g[1]*g[2] - mu*alpha(c)*Gc) < TOL)
    check("(4.7) G(c) = conj(chi_c(4)) gamma_3(c), |G(c)| = 1", abs(Gc - complex(chi(four, [p, q])).conjugate()*g[3]) < TOL and abs(abs(Gc) - 1) < TOL)
    for t in small[:6]:
        if t in (p, q): continue
        check("L4.4  sextic reciprocity, composite: chi_c(t) = r(t,c) chi_t(c)", abs(chi(t, [p, q]) - r(t, c)*chi_p(c, t)) < TOL)
print()
allok = True
for k, (good, bad) in results.items():
    print(f"{'PASS' if bad == 0 else 'FAIL'}  {k}:  {good} ok, {bad} failed"); allok &= bad == 0
print("\nALL PASS" if allok else "\nSOME FAILURES")
