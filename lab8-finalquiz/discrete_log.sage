from itertools import count

# random_prime, is_prime from SageMath
getPrime = lambda n: random_prime(2^n-1, proof=False, lbound=2^(n-1))
isPrime = is_prime

def Pohlig_Hellman_keygen():
    while True:
        ps = [2]
        n = 2
        while True:
            p = getPrime(randint(8, 14))
            ps.append(p)
            n = n * p
            # n.nbits: find how many bits in binary form of `n`
            if n.nbits() > 1024 and isPrime(n + 1):
                break
            if n.nbits() > 2048:
                break
        if isPrime(n + 1):
            break
    n += 1
    g = primitive_root(n)
    assert Mod(g, n).multiplicative_order() == n - 1
    x = randint(1, Mod(g, n).multiplicative_order())  # Mod from SageMath
    y = power_mod(g, x, n)  # power_mod from SageMath
    return n, g, x, y

def Pohlig_Hellman_attack(n, g, y):
    # discrete_log from SageMath
    #   which calculates discrete logarithm with many methods, including Pohlig_Hellman attack
    x = discrete_log(Mod(y, n), Mod(g, n)) 
    return x

n, g, x, y = Pohlig_Hellman_keygen()
attack_x = Pohlig_Hellman_attack(n, g, y)
assert x == attack_x

print 'n\t=', n
print 'g\t=', g
print 'y\t=', y

print 'x\t=', x
print 'atk_x\t=', attack_x
