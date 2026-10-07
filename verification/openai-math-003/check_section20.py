# Exact checks of the exponent bookkeeping in Section 20 of
# "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8" (OpenAI, 30 Sep 2026)
from sympy import Rational as Q, symbols, expand, simplify, together, factor
import sympy as sp
ok = []
def check(name, cond):
    ok.append((name, bool(cond))); print(("PASS " if cond else "FAIL ") + name)

h, l, lx, ly = Q(13,16), Q(1,6), Q(17,48), Q(23,48)
alpha = Q(5,6); C0 = Q(-1,48)
check("h = 1 - lx + l", h == 1 - lx + l)
check("C(7/8) = 7/8 - 11/16 = 3/16", Q(7,8) - Q(11,16) == Q(3,16))
check("C_I(11/12) = 11/12 - 2/3 = 1/4", Q(11,12) - Q(2,3) == Q(1,4))
check("m_w = ly/20 = 23/960", ly/20 == Q(23,960))
check("m_z = h/600 = 13/9600", h/600 == Q(13,9600))
check("B0 = lx/2 + 1 + ly = 53/32", lx/2 + 1 + ly == Q(53,32))
check("kappa = 3/4 + 2*Delta <= 5/6 for Delta <= 1/24", Q(3,4) + 2*Q(1,24) == Q(5,6))

d, delta, q, R, x, y, Delta = symbols('d delta q R x y Delta', real=True)
a = (1 + delta)/2
# Eq (20.4), first line
E1 = a - Q(7,8) + h*(Q(17,50) - Q(1,6)) - a*ly - (1-a)*l - (delta/2 - q)*l + d*(R + delta/2 - Q(17,50))
# Eq (20.4), second line
E2 = C0 + Q(2,3)*delta + q/6 - h*(1-R) + (d-h)*(R + delta/2 - Q(17,50))
check("(20.4) first line == second line", simplify(expand(E1 - E2)) == 0)
E = E2
# (20.5) floor bin
d0 = Q(1,50)
check("(20.5) E(h) at floor = -7/1200", E.subs({d:h, R:1, q:d0/2, delta:d0}) == Q(-7,1200))
# (20.6)
check("(20.6) h(17/50-1/6) - ly/2 = -79/800", h*(Q(17,50)-Q(1,6)) - ly/2 == Q(-79,800))
check("small rows: -79/800 + 2*dmin = -63/800", Q(-79,800) + 2*Q(1,100) == Q(-63,800))
# (20.7) endpoint delta = alpha, R = 1 - delta, q <= delta/2
check("(20.7) E(h) with R=1-delta, q=delta/2 equals -1/48 - delta/16",
      simplify(E.subs({d:h, R:1-delta, q:delta/2}) - (-Q(1,48) - delta/16)) == 0)
# Lemma 20.2
Dx = (37 + 34*y)/18; py = 7 + 18*y + 8*y**2; Px = py/9
jy = 185 + 170*y + (-138 + 12*y + 96*y**2)*delta
J = (alpha - delta)*Dx + delta*Px
check("J = jy/108", simplify(J - jy/108) == 0)
check("Dx - Px = 1 + x - 8x^2/9 with y = 1/2 - x", simplify((Dx - Px).subs(y, Q(1,2)-x) - (1 + x - Q(8,9)*x**2)) == 0)
Rstar = 1 - delta + (alpha - delta)*delta*Px/(2*J)
Estar = E.subs({d:h, R:Rstar, q:(Q(1,2)-y)*delta})
negE_claim = (1 + (3 + 8*y)*delta)/48 - Q(13,32)*(Q(5,6) - delta)*delta*Px/J
check("-E* formula in proof of Lemma 20.2", simplify(-Estar - negE_claim) == 0)
lhs = expand(sp.cancel(10368*J*(-Estar)))
rhs1 = expand(2*jy*(1 + (3+8*y)*delta) - 468*(Q(5,6) - delta)*delta*py)
rhs2 = expand(10*(37+34*y) - 8*(237 + 377*y + 26*y**2)*delta + 48*(51 + 131*y + 94*y**2 + 32*y**3)*delta**2)
check("10368 J (-E*) = 2 jy[...] - 468(...)", simplify(lhs - rhs1) == 0)
check("... = explicit quadratic in delta", simplify(rhs1 - rhs2) == 0)
v = 51 + 41*y
rhs920 = (3 + 5*y)*((4*v*delta - 79)**2 + 49) + 4*y*(4*v*delta*((1 + 3*y)*(15 + 32*y)*delta + 9 - 13*y) + 265 + 3485*y)
check("(20.9) completion of the square identity", simplify(expand(v*rhs2 - rhs920)) == 0)
check("176256 * 5/2 = 440640", 176256*Q(5,2) == 440640)
check("10368 * 17 = 176256 (49(3+5y)/(10368 v J) >= 49/(10368*17*J))", 10368*17 == 176256)
# numeric scan of -E* and J over the ranges, independent of the algebra
import itertools
mn = None; mnJ = (None, None)
for i in range(0, 41):
    for k in range(0, 41):
        yy = Q(i, 80); dd = Q(5,6)*Q(k,40)
        Jv = J.subs({y:yy, delta:dd}); 
        val = (-Estar).subs({y:yy, delta:dd})
        mn = val if mn is None or val < mn else mn
        mnJ = (Jv if mnJ[0] is None or Jv < mnJ[0] else mnJ[0], Jv if mnJ[1] is None or Jv > mnJ[1] else mnJ[1])
print("grid min of -E* =", mn, "=", float(mn), "  claimed lower bound 49/440640 =", float(Q(49,440640)))
check("grid: -E* >= 49/440640 everywhere", mn >= Q(49,440640))
print("grid range of J =", mnJ, [float(t) for t in mnJ])
check("grid: 35/54 <= J <= 5/2", mnJ[0] >= Q(35,54) and mnJ[1] <= Q(5,2))
# (20.11)
E11 = E.subs({d:Q(1,2), R:Q(76,75) - Q(2,3)*delta, q:delta/2})
check("(20.11) E(1/2) = -529/2400 + 25 delta/96", simplify(E11 - (Q(-529,2400) + Q(25,96)*delta)) == 0)
check("(20.11) at delta=5/6: -529/2400 + 125/576 = -49/14400", Q(-529,2400) + Q(25,96)*Q(5,6) == Q(-49,14400))
check("76/75 - 2/3*(1/50) = 1", Q(76,75) - Q(2,3)*Q(1,50) == 1)
check("slope R + delta/2 - 17/50 = 101/150 - delta/6", simplify((Q(76,75) - Q(2,3)*delta) + delta/2 - Q(17,50) - (Q(101,150) - delta/6)) == 0)
# 20.5 frequency ranges
check("l/h = 8/39", l/h == Q(8,39))
check("8/39 > 1/5 > 7/37", Q(8,39) > Q(1,5) > Q(7,37))
check("5l - h = 1/48", 5*l - h == Q(1,48))
check("1/5 - 7/37 = 2/185 ; 8/39 - 7/37 = 23/1443", Q(1,5)-Q(7,37) == Q(2,185) and Q(8,39)-Q(7,37) == Q(23,1443))
check("33/50 - delta/2 >= 4/25 at delta = 5/6", Q(33,50) - Q(5,12) >= Q(4,25))
check("139/96 + 1/2 - 17/50 < 2", Q(139,96) + Q(1,2) - Q(17,50) < 2)
check("m_hi = (1 - h/4) Delta = 51/64 Delta", 1 - h/4 == Q(51,64))
check("kappa_P = 7/16 * l/K = 7/(96K), and < 7/8 * l/K = 7/(48K)", Q(7,16)*l == Q(7,96) and Q(7,8)*l == Q(7,48))
print()
print(f"{sum(c for _,c in ok)}/{len(ok)} checks passed")
