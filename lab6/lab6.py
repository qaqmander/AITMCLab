# Welcome to lab6
from AITMCLab.Crypto.Util.number import getPrime, isPrime
from AITMCLab.libnum import invmod, gcd, n2s, s2n
from random import randint

# For all cryptographic scheme later, we use following common parameters
p = 1439
g = 7
assert isPrime(p) and isPrime((p - 1) // 2)  # strong prime
assert pow(g, 2, p) != 1 and pow(g, (p - 1) // 2, p) != 1  # primitive root

# Elgamal Encryption Scheme
def elgamal_keygen(p, g):
    x = randint(1, p - 1)
    y = pow(g, x, p)
    return y, x

def elgamal_encrypt(m, p, g, y):
    assert 0 <= m and m < p
    r = randint(1, p - 1)
    s = pow(y, r, p)
    c1 = pow(g, r, p)
    c2 = m * s % p
    return c1, c2

def elgamal_decrypt(c1, c2, p, g, x):
    return None

# Elgamal test:
def elgamal_test():
    y, x = elgamal_keygen(p, g)
    for _ in range(10):
        for m in range(p):
            c1, c2 = elgamal_encrypt(m, p, g, y)
            mm = elgamal_decrypt(c1, c2, p, g, x)
            if mm != m:
                return False
    return True

# Elgamal Signature Scheme, without hash function
def elgamal_sig_keygen(p, g):
    # same as elgamal_keygen
    x = randint(1, p - 1)
    y = pow(g, x, p)
    return y, x

def elgamal_sig_signify(m, p, g, x):
    assert 0 <= m and m < p - 1
    k = randint(2, p - 2)
    while gcd(k, p - 1) != 1:
        k = randint(2, p - 2)
    r = pow(g, k, p)
    # without hash function here
    s = (m - x * r) * invmod(k, p - 1) % (p - 1)
    return r, s

def elgamal_sig_verify(m, r, s, p, g, y):
    return None

def elgamal_sig_test():
    y, x = elgamal_sig_keygen(p, g)
    for _ in range(10):
        for m in range(p - 1):
            r, s = elgamal_sig_signify(m, p, g, x)
            if not elgamal_sig_verify(m, r, s, p, g, y):
                return False
    return True

# lab6
def elgamal_enc_lab(large_m):
    f = open('enc', 'wb')
    y, x = elgamal_keygen(p, g)
    f.write('y, x = {}, {}\n'.format(y, x))
    for i in range(large_m.bit_length() // 10 + 1):
        now_p = getPrime(10)
        f.write('now_p = {}\n'.format(now_p))
        now_m = large_m % now_p
        c1, c2 = elgamal_encrypt(now_m, p, g, y)
        f.write('c1, c2 = {}, {}\n'.format(c1, c2))
    f.close()

def elgamal_sig_lab(large_m):
    f = open('sig', 'wb')
    y, x = elgamal_sig_keygen(p, g)
    f.write('y = {}\n'.format(y))
    for i in range(large_m.bit_length()):
        now_m = (large_m >> i) & 1
        r, s = elgamal_sig_signify(1024, p, g, x)
        if now_m == 1:
            f.write('r, s = {}, {}\n'.format(r, s))
        else:
            f.write('r, s = {}, {}\n'.format(r, randint(0, p - 2)))
    f.close()

if __name__ == '__main__':
    print 'elgamal_test()', elgamal_test()
    print 'elgamal_sig_test()', elgamal_sig_test()
    from secret import flag
    assert flag.startswith('flag{') and flag.endswith('}')
    flag = flag[5:-1]
    f1, f2 = s2n(flag[:len(flag) // 2]), s2n(flag[len(flag) // 2:])

    elgamal_enc_lab(f1)
    elgamal_sig_lab(f2)
