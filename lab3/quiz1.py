import math
from AITMCLab.Crypto.Util.number import long_to_bytes
from AITMCLab.Crypto.Util.number import bytes_to_long
from AITMCLab.Crypto.Util.number import getRandomNBitInteger
from AITMCLab.Crypto.Util.number import getPrime
from AITMCLab.Crypto.Util.number import isPrime
from AITMCLab.Crypto.Util.number import inverse

flag = 'flag{**********}'

def nextPrime(n):
    n += 2 if n & 1 else 1
    while not isPrime(n):
        n += 2
    return n

def init(S, K):
    j = 0
    k = []
    K = list(K)
    for i in range(len(K)):
        K[i] = ord(K[i])
    for i in range(256):
        S.append(i)
        k.append(K[i % len(K)])
    for i in range(256):
        j = (j + S[i] + k[i]) % 256
        S[i], S[j] = S[j], S[i]

def Encrypt(key, D):
    S=[]
    init(S, key)
    i = j = 0
    result = ''

    for a in D:
        a = ord(a)
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = chr(a ^ S[(S[i] + S[j]) % 256])
        result += k
    return result


def Decrypt(key, D):
    S = []
    init(S, key)
    i = j = 0
    result = ''
    for a in D:
        a = ord(a)
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = chr(a ^ S[(S[i] + S[j]) % 256])
        result += k
    return result

if __name__ == "__main__":
    key = long_to_bytes(getRandomNBitInteger(100))
    print 'key =', bytes_to_long(key)
    e = getPrime(512)
    print 'e =', e

    E = nextPrime(e)
    f = math.factorial(e) % E   # f = e! mod E and you CANNOT calculate it directly!! hahaha

    d = long_to_bytes(f)

    c1 = bytes_to_long(Encrypt(key, d))
    print 'c1 =', c1

    c2 = bytes_to_long(Encrypt(key, flag))
    print 'c2 =', c2

# e = 11248112333656902878308992204660514716130692202019193081806766887380465145401754698746718075268681481388695805324253817155823465013590321091178897918430457
# c1 = 11792816667683654209610238149228683194178884298019505853565076663183883681365400495420305428570416004628438524072440231323696408946395141935772862600031614
# c2 = 81946333492800053045881242964212560642046177081574600318494251620269838444004879162713842
