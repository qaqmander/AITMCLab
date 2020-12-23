x = []
y = None
with open('data', 'rb') as fr:
    for i in range(64):
        x.append(int(fr.readline().strip().split()[-1]))
    y = int(fr.readline().strip().split()[-1])

with open('enc', 'rb') as fr:
    enc = list(map(int, fr.readline().strip().split()))

M = [[0] * 65 for _ in range(65)]
for i in range(64):
    M[i][i] = 1
    M[64][i] = x[i]
M[64][64] = -y
M = Matrix(ZZ, M).transpose()

solve = M.LLL()[0]

flag = []
for i in range(64):
    flag.append(chr(enc[i] ^^ solve[i]))
print 'flag{' + ''.join(flag) + '}'
