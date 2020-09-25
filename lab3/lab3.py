# Welcome to lab3, I am going to introduct some interesting functions to you!
# We need to import what we want
from AITMCLab.libnum import n2s, s2n, invmod
from AITMCLab.Crypto.Util.number import long_to_bytes, bytes_to_long
from AITMCLab.Crypto.Util.number import getPrime, isPrime

# Use s2n(acronym for 'string to number') to convert string to number
#    and use n2s to revert
s = 'I love algorithm design'
n = s2n(s)    # int
print 'n =',n
new_s = n2s(n)
assert new_s == s

# Feel free to replace n2s with long_to_bytes, or replace s2n with bytes_to_long
#    They are equavalant!!
assert long_to_bytes(bytes_to_long('hahaha')) == 'hahaha'
assert n2s(bytes_to_long('heiheihei')) == 'heiheihei'
assert long_to_bytes(s2n('xixixi')) == 'xixixi'

# x * invmod(x, n) % n == 1, as you suppose
n = 23
for x in range(1, n):
    assert x * invmod(x, n) % n == 1
    assert invmod(x, n) * x % n == 1

# Use function 'getPrime' to generate a prime RANDOMLY
#    namely, you will get different result every time you execute this program
p = getPrime(5)
q = getPrime(5)
print p, q
assert p.bit_length() == 5

# With arg=1024, you can generate a very big prime!! ( It can be a little slow )
big_p = getPrime(1024)
print big_p
assert big_p.bit_length() == 1024

# Use function 'isPrime' to judge a number: whether it is prime or not?
#     It is very efficient, feel free to apply it to very BIG number
print 'Is p prime? : ', isPrime(p)
print 'Is q prime? : ', isPrime(q)
print 'Is p*q prime? : ', isPrime(p*q)
print 'Is big_p prime? : ', isPrime(big_p)
print 'Is p*big_p prime? : ', isPrime(p*big_p)


# Lab3
# Here we introduce an insecure encryption scheme
n = getPrime(800)
# NOTICE: Every time you execute 'getPrime', different prime is returned
#         Please pay attention to the number in comment: it is the prime I generated
#         And I use this notion to tell you how I generate this prime
#         You should not be suprised to find that your execution result is different from mine
#             ( And you can believe it is a truely random prime )
print 'n =', n    # n = 3914224287795636809861368015178301501372188634077669936495180785846977608060045377653931855350462641602739528638098085015546367841148708574573569280349292403464473463818042817457266362325488737681832840764568002910598017717058689969512296099
# uncomment next line to use original value of n for following execution
# n = 3914224287795636809861368015178301501372188634077669936495180785846977608060045377653931855350462641602739528638098085015546367841148708574573569280349292403464473463818042817457266362325488737681832840764568002910598017717058689969512296099
e = 0x10001    # hexadecimal presentation!!
assert e == 65537
flag = 'flag{**********}'
m = s2n(flag)    # convert string to number
c = pow(m, e, n)    # pow(a, b, c) == a**b % c
print 'c =', c    # c = 3678716732847973069496233717035619410810008982881832778108057662379358563168669345659610269104838531535596938088040391434969949131327247362326079375825722973572861874365364217648459622237827463731017181656549460372354778250000173854890274241
# HINT: find d such that e * d % (n - 1) == 1, and try pow(c, d, n)~~