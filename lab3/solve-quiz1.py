import math
from AITMCLab.Crypto.Util.number import long_to_bytes
from AITMCLab.Crypto.Util.number import bytes_to_long
from AITMCLab.Crypto.Util.number import getRandomNBitInteger
from AITMCLab.Crypto.Util.number import getPrime
from AITMCLab.Crypto.Util.number import isPrime
from AITMCLab.Crypto.Util.number import inverse
from AITMCLab.libnum import n2s, s2n

flag = 'flag{Congratulation!_quiz1_passed!!!}'

def nextPrime(n):
    n += 2 if n & 1 else 1
    while not isPrime(n):
        n += 2
    return n

e = 11248112333656902878308992204660514716130692202019193081806766887380465145401754698746718075268681481388695805324253817155823465013590321091178897918430457
c1 = 5120829596353532760839054347975234579355835073413768618360492980516438193909447500996222328143719619379838946544412967584025416378147246422705451415437468
c2 = 17985907282297772406857113433926323639543183645704827789984971602150950301590677893419082
c1, c2 = n2s(c1), n2s(c2)
E = nextPrime(e)

f = 1
for i in range(E - 2, e, -1):
    f = f * inverse(i ,E) % E
print f
f = n2s(f)

def xor(s1, s2):
    length = min(len(s1), len(s2))
    res = ''
    for i in range(length):
        res = res + chr(ord(s1[i]) ^ ord(s2[i]))
    return res

key = xor(f, c1)
m = xor(key, c2)
print m  # flag{Congratulation!_quiz1_passed!!!}
