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

def gen_keystream(K, length):
    j = 0
    S = k = []
    K = list(K)
    for i in range(len(K)):
        K[i] = ord(K[i])
    for i in range(256):
        S.append(i)
        k.append(K[i % len(K)])
    for i in range(256):
        j = (j + S[i] + k[i]) % 256
        S[i], S[j] = S[j], S[i]

    k1 = k2 = 0
    keystream = []
    for i in range(length):
        k1 = (k1 + 1) % 256
        k2 = (k2 + S[k1]) % 256
        S[k1], S[k2] = S[k2], S[k1]
        keystream.append(S[(S[k1] + S[k2]) % 256])
    return keystream


def Encrypt(key, D):
    keystream = gen_keystream(key, len(D))
    result = ''

    for i in range(len(D)):
        a = ord(D[i])
        k = chr(a ^ keystream[i])
        result += k
    return result


def Decrypt(key, D):
    keystream = gen_keystream(key, len(D))
    result = ''

    for i in range(len(D)):
        a = ord(D[i])
        k = chr(a ^ keystream[i])
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
# c1 = 5120829596353532760839054347975234579355835073413768618360492980516438193909447500996222328143719619379838946544412967584025416378147246422705451415437468
# c2 = 17985907282297772406857113433926323639543183645704827789984971602150950301590677893419082
