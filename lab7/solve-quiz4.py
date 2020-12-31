from AITMCLab.libnum import n2s, s2n, invmod
from AITMCLab.Crypto.Util.number import getPrime, isPrime
from random import randint

with open('enc', 'rb') as fr:
    n = int(fr.readline().strip().split()[-1])
    g = int(fr.readline().strip().split()[-1])
    y = int(fr.readline().strip().split()[-1])

ps = []
rs = []
gs = []
ys = []
N = n - 1
for p in range(2, 1 << 12):
    if N % p == 0:
        ps.append(p)
        r = 0
        while N % p == 0:
            r += 1 
            N //= p
        rs.append(r)
        gs.append(pow(g, (n - 1) / (p ** r), n))
        ys.append(pow(y, (n - 1) / (p ** r), n))

print ps
print rs

xs = []
for idx in range(len(ps)):
    p, r = ps[idx], rs[idx]
    g, y = gs[idx], ys[idx]
    a = [0] * r
    now_x = 0
    for i in range(r):
        now_g = pow(g, pow(p, r - 1 - i), n)
        now_y = pow(y, pow(p, r - 1 - i), n)
        now = pow(now_g, now_x, n)
        for now_a in range(p + 1):
            if now == now_y:
                a[i] = now_a
                break
            now = now * pow(now_g, pow(p, i), n) % n
        now_x += a[i] * pow(p, i)
    xs.append(now_x)
print xs

for i in range(len(ps)):
    ps[i] = pow(ps[i], rs[i])

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
