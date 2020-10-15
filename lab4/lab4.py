# Welcome to lab4
# Primitive Root
# say $g$ is primitive root for some number $p$, means that 
#    for all $x$ != 0, exists $n$ such that g**n==x(mod p)
from AITMCLab.libnum import gcd, invmod, s2n
from Crypto.Util.number import isPrime

# Define Euler function
def phi(n):
    ps = []
    x = n
    for i in range(2, n + 1):
        if x % i == 0:
            ps.append(i)
            while x % i == 0:
                x //= i
    ret = n
    for i in ps:
        ret = ret / i * (i - 1)
    return ret
assert phi(41) == 40
assert phi(100) == 40

p = 89
phi_p = phi(p) # Euler function
# find a primitive root for $p$
g = None
for i in range(1, p):
    ls = []
    for j in range(phi_p):
        i_exp_j = pow(i, j, p)
        if i_exp_j in ls:
            break
        ls.append(i_exp_j)
    if len(ls) == phi_p:
        g = i
        break
print g    # 3
# which means $Z^*_p$ can be presented as {3**1, 3**2, 3**3, ..., 3**40}

# Then we can find all primitive root easily! ( Why? )
all_g = []
for i in range(phi_p + 1):
    if gcd(i, phi_p) == 1:
        all_g.append(pow(g, i, p))
print all_g

# Then we can solve x**n==1(mod p) easily! ( Why? )
def solve_x_exp_n_equal_1_mod_p(n):
    res1 = []
    for i in range(p):
        if pow(i, n, p) == 1:
            res1.append(i)
    res2 = []
    for i in range(phi_p):
        if i * n % phi_p == 0:    # why?
            res2.append(pow(g, i, p))
    res2.sort()
    return res1, res2
r1, r2 = solve_x_exp_n_equal_1_mod_p(12)
print r1, r2
r1, r2 = solve_x_exp_n_equal_1_mod_p(33)
print r1, r2

# Something Special with Euler Function
n = 41 * 43 * 47
phi_n = phi(n)
e = 37
assert gcd(e, phi_n) == 1
d = invmod(e, phi_n)
from random import randint  # randint(l, r): return random integer in [l, r]
m = randint(0, n - 1)
c = pow(m, e, n)   # encryption
mm = pow(c, d, n)  # decryption
assert mm == m     # why?

# Question
p = 104879397075344024438671231239628115011303349344697797964879592144922079000957 
q = 104879397075344024438671231239628115011303349344697797964879592144922079001013
assert isPrime(p) and isPrime(q)
n = p * q
flag = s2n('flag{can_you_find_me??}')
r = randint(1, n)
c = (pow(n + 1, flag, n * n) * pow(r, n, n * n)) % (n * n)
print c
# 13134489820394613222282607681686272081419875146946401883172682167011759113388373349180457979897848113275982219264879081189886853062717764580364698888338032141434053832247476010400449272010082460437747190468766740274587999336359171283098137261396013153130265440425676242061845667887640808895666325466803989428