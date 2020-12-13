from AITMCLab import libnum
import random

N = 21950613536281390486175757463951027643556662621824579929664918617520636813458994325720569579695736856079459340474316751889021883755540017377473409564797843019125596929359598746535191841338208989879009508321774759757392464348925062704618198548398309908878380041795632951630513476281083426748653263731919122841901104123145297521411331174923397782111024006706017326210374498919922250769088886696170966869394222786903527353128540253585182758832324462426318387914150570168191590734053846371944717431858873198597415498765665035309188308408227521317670668417094970551798085092238594309838065757300622761550073415879726501051
e = 0x10001
"""
m = number.bytes_to_long(key)

with open('key.enc', 'w') as f:
    while m:
        p = getPrime(8)
        padding = random.randint(0, 2**1000) ** 2
        message = padding << m**(p-1) % p + m % 2
        cipher = pow(message, e, N)
        f.write(hex(cipher)+'\n')
        m /= 2"""
p = 23  
m = 5      
#(2 * pad * pad + 0) ** e + kn = enc
#
#(2 * pad * pad + 0) + (kn) % e = enc % e
#(2 * pad * pad + 1) ** e + kn = enc
i = 0
m = 0 

with open("./key.enc","r") as f:
	info = f.readlines()
	f.close()
for i in range(len(info)):
	x = int(info[i].strip()[:-1],16)
	#print libnum.jacobi(x,N)
	#print x,hex(x)
	#raw_input()
	if libnum.jacobi(x,N) == 1:
		m += (1 << i)
	else:
		m += 0
n = N
temp = random.randint(0, 2**1000) ** 2
print libnum.jacobi(pow(2*temp,e,n),n)
print libnum.jacobi(pow(4*temp,e,n),n)
print libnum.n2s(m)