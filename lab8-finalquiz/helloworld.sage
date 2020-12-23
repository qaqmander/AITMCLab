# Assign list to variable as python2
A = [
    [1/2, 2/3, 3/4],
    [12/13, 11/10, 5/6],
    [15/14, 9/10, 7/8]
]
# Matrix over rational number
A = Matrix(QQ, A)    
print 'A:'
print A
print 'A.inverse():'
print A.inverse()
print ''

B = [
    [0, 1, 1],
    [1, 1, 0],
    [0, 0, 1]
]
# Matrix over Finite Field with order 2
B = Matrix(GF(2), B) 
print 'B:'
print B
print 'B.inverse():'
print B.inverse()
print ''

P.<x> = GF(2)[]
irreducible_polys = []
for i in range(1 << 8, 1 << 9):
    now_poly = P(list(reversed(map(int, bin(i)[2:]))))
    if now_poly.is_irreducible():
        irreducible_polys.append(now_poly)
print 'number of irreducible poly with deg 8 in GF(2)[x]:', len(irreducible_polys)
for i in range(5):
    print irreducible_polys[i]
