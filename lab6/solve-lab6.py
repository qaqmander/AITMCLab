from AITMCLab.libnum import invmod

def elgamal_decrypt(c1, c2, p, g, x):
    return invmod(pow(c1, x, p), p) * c2 % p

def elgamal_sig_verify(m, r, s, p, g, y):
    return pow(g, m, p) == pow(y, r, p) * pow(r, s, p) % p

p = 1439
g = 7

def solve_enc():
    ls = []
    with open('enc', 'rb') as f:
        line = f.readline().strip().split()
        y, x = int(line[-2][:-1]), int(line[-1])
        print y, x
        for i in range(10):
            line = f.readline().strip().split('=')[-1]
            nowp = int(line)
            line = f.readline().strip().split('=')[-1].strip().split(',')
            c1, c2 = int(line[0]), int(line[1])
            ls.append((nowp, c1, c2))
    print ls
    res = []
    for i in range(10):
        res.append(elgamal_decrypt(ls[i][1], ls[i][2], p, g, x))
    print(res)
    # f1 = 20870207792577095536753079401
    N = 1
    for i in range(10):
        N *= ls[i][0]
    M = []
    for i in range(10):
        nowm = N // ls[i][0]
        nowm = nowm * invmod(nowm, ls[i][0]) % N
        M.append(nowm)
    r = 0
    for i in range(10):
        r += M[i] * res[i]
    r = r % N
    # print r
    return r

def solve_sig():
    ls = []
    with open('sig', 'rb') as f:
        line = f.readline().split('=')[-1]
        y = int(line)
        for i in range(95):
            line = f.readline().split('=')[-1].strip().split(',')
            ls.append((int(line[0]), int(line[1])))
    res = []
    for i in range(95):
        r, s = ls[i]
        res.append(1 if elgamal_sig_verify(1024, r, s, p, g, y) else 0)
    r = int(''.join(map(str, res[::-1])), 2)
    # print r
    return r

f1 = solve_enc()
f2 = solve_sig()
from AITMCLab.libnum import n2s
f = n2s(f1) + n2s(f2)
print 'flag{' + f + '}'