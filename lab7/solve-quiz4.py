from AITMCLab.libnum import n2s, s2n, invmod
from AITMCLab.Crypto.Util.number import getPrime, isPrime
from random import randint

with open('enc', 'rb') as fr:
    n = int(fr.readline().strip().split()[-1])
    g = int(fr.readline().strip().split()[-1])
    y = int(fr.readline().strip().split()[-1])

ps = []
gs = []
ys = []
N = n - 1
for p in range(2, 1 << 12):
    if N % p == 0:
        ps.append(p)
        gs.append(pow(g, (n - 1) / p, n))
        ys.append(pow(y, (n - 1) / p, n))
        N //= p

xs = []
for i in range(len(ps)):
    now = 1
    for x in range(ps[i] + 1):
        if now == ys[i]:
            xs.append(x)
            break
        now = now * gs[i] % n
print xs
print ps

Ms = []
m = 1
for p in ps:
    m *= p
for i in range(len(ps)):
    now_m = m // ps[i]
    now_m = now_m * invmod(now_m, ps[i]) % n
    Ms.append(now_m)

res = 0
for i in range(len(ps)):
    res = (res + xs[i] * Ms[i]) % m
print(n2s(res))
