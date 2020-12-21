from secret import flag
from AITMCLab.libnum import n2s, s2n
from AITMCLab.Crypto.Util.number import getPrime, isPrime
from random import randint

assert flag.startswith('flag{') and flag.endswith('}')
flag = s2n(flag[5:-1])

n = 2
ps = [2]
while True:
    p = getPrime(randint(9, 11))
    ps.append(p)
    n = n * p
    if n + 1 > flag and isPrime(n + 1):
        break
n += 1

for g in range(2, ps[-1] ** 2 - 1):
    is_primitive_root = True
    for p in ps:
        if pow(g, (n - 1) / p, n) == 1:
            is_primitive_root = False
            break
    if is_primitive_root:
        break

with open('enc', 'wb') as fw:
    fw.write('n = {}\n'.format(n))
    fw.write('g = {}\n'.format(g))
    fw.write('c = {}\n'.format(pow(g, flag, n)))
