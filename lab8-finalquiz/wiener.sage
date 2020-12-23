# random_prime from SageMath
getPrime = lambda n: random_prime(2^n-1, proof=False, lbound=2^(n-1))  

def wiener_keygen():
    p, q = getPrime(1024), getPrime(1024)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    d = getPrime(400)
    while gcd(d, phi) > 1:
        d = getPrime(400)
    e = inverse_mod(d, phi)  # inverse_mod from SageMath

    for _ in range(10):
        test_m = randint(100, n - 100)  # randint from SageMath
        assert pow(test_m, e * d, n) == test_m
    return n, e, d

def wiener_attack(n, e):
    fracs = (e / n).continued_fraction()
    assert isinstance(fracs, sage.rings.continued_fraction.ContinuedFraction_periodic)
    for i in range(len(fracs)):
        assert isinstance(fracs[:i], sage.rings.continued_fraction.ContinuedFraction_periodic)
        now_frac = fracs[:i].value()
        d = now_frac.denominator()
        flag = True
        for _ in range(10):
            test_m = randint(100, n - 100)
            if pow(test_m, e * d, n) != test_m:
                flag = False
                break
        if flag:
            return d
    return None
    
n, e, d = wiener_keygen()
attack_d = wiener_attack(n, e)
assert d == attack_d

print 'n\t=', n
print 'e\t=', e
print 'd\t=', d
print 'atk_d\t=', attack_d
