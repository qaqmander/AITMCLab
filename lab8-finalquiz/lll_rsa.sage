# random_prime from SageMath
getPrime = lambda n: random_prime(2^n-1, proof=False, lbound=2^(n-1)) 

PRIME_BITLENGTH = 512

def common_private_key_rsa_keygen():
    d = getPrime(2 * PRIME_BITLENGTH // 3)
    pubs = []
    for i in range(10):
        p, q = getPrime(PRIME_BITLENGTH), getPrime(PRIME_BITLENGTH)
        phi = (p - 1) * (q - 1)
        while gcd(d, phi) > 1:
            p, q = getPrime(PRIME_BITLENGTH), getPrime(PRIME_BITLENGTH)
            phi = (p - 1) * (q - 1)
        n = p * q
        e = inverse_mod(d, phi)
        pubs.append((n, e))
    return pubs, d

def common_private_key_rsa_attack(pubs):
    pubs = sorted(pubs, key=lambda x: x[0])
    M = int(sqrt(pubs[-1][0]))
    a = [[0] * (len(pubs) + 1) for _ in range(len(pubs) + 1)]
    a[0][0] = M
    for i in range(len(pubs)):
        n, e = pubs[i]
        a[i + 1][i + 1] = -n
        a[0][i + 1] = e
    a = Matrix(ZZ, a)
    dM = abs(a.LLL()[0][0])
    assert dM % M == 0
    return dM // M

pubs, d = common_private_key_rsa_keygen()
attack_d = common_private_key_rsa_attack(pubs)
assert attack_d == d

for i in range(len(pubs)):
    n, e = pubs[i]
    for _ in range(10):
        now_m = randint(0, n - 1)
        assert power_mod(now_m, e * attack_d, n) == now_m

print 'd\t=', d
print 'atk_d\t=', attack_d
