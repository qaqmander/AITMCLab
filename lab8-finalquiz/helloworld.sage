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

