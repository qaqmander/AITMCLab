# Welcome to lab2, let's go through some grammars in python2
# We use keyword 'assert' to check something
assert 1 == 1    # Nothing happened
# assert 1 == 2  # program will exits when executing this line

# You have a string, remember to use '\' to escape special character
a = 'I\'m a string'    # or a = "I'm a string"

# Apply function 'len' to get length of string
print len(a) # 12

# Use '[' ']' to slice a string
print a[0]       # 'I'
print a[-1]      # 'g'
print a[-3]      # 'i'
print a[4:7]     # 'a s'
print a[:3]      # "I'm"
print a[-5:]     # 'tring'
print a[4:10:2]  # 'asr'
print a[::-1]    # What's this???

# Tip! How to judge Palindrome string? 
# Notice: Here we define our own function with keyword 'def'
#         and control return value with keyword 'return'
def judge_palindrome(s):
    if s[::-1] == s:
        return True
    else:
        return False
assert judge_palindrome('ababa') == True
assert judge_palindrome('abcab') == False

# Concatenate string as you like
a = a + '!!!!!'
print a   # I'm a string!!!!!


# You have a list: A list is a list of things (like array in C-language)
a = [1, 2, 3, 4]
print len(a)    # 4

# Use 'for' to go through all element of a list
for i in range(len(a)):
    print a[i]
# 1
# 2
# 3
# 4

# Use 'append' to add new element to the end of a list
a.append(5)
a.append(6)

# Use '+' to add another list to a list
a = a + [7, 8, 9, 10]

# You can print a list directly!
print a # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Lab2

a, b = 5, 12
x = 7
y = (a * x + b) % 26        # encryption
print x, y    # 7 21

from AITMCLab.libnum import invmod
a_1 = invmod(a, 26)
assert a * a_1 % 26 == 1    # a_1 is a^{-1} % 26!!!
xx = a_1 * (y - b) % 26     # decryption
assert x == xx
print x, y, xx    # 7 21 7

# Affine cryptography
def affine(message, a, b):    # y = ax + b (mod 26)
    cipher = ''
    for char in message:
        if 'a' <= char <= 'z':
            now_cipher = (a * (ord(char) - ord('a')) + b) % 26
            cipher += chr(now_cipher + ord('a'))
        elif 'A' <= char <= 'Z':
            now_cipher = (a * (ord(char) - ord('A')) + b) % 26
            cipher += chr(now_cipher + ord('A'))
        else:
            cipher += char 
    return cipher

# Affine cryptography - 1: 
#    Try to findout what happen and message!
message = 'flag{**********}'
a, b = 7, 12
cipher = affine(message, a, b)
print cipher
# vlmc{ko_lgdo_MQPSALmt_doby_swaj!!}

# Affine cryptography - 2: 
#    Try to findout what happen and message without a & b!!
message = 'flag{**********}'
a, b = ??, ??    # We don't have a & b now !!!! hahahaha
cipher = affine(message, a, b)
print cipher
# kyhv{pz_mzhyyl_yfez_HRIJDYhs_ezml_jtdg!!}

# Hill cryptography (optional)
# May be difficult! Try to findout what happen and message
message = 'flag{************}'

# 2-dimentional matrix
A = [[1, 2, 3, 4], [0, 3, 4, 5], [1, 5, 8, 10], [2, 10, 15, 8]]
B = [6, 9, 12, 15]

# A_1 = [[21, 2, 2, 15], [21, 4, 1, 15], [6, 6, 8, 19], [19, 19, 19, 7]]

#             / 157 104 104 130 \      / 1  0  0  0 \
#            |  182 131 130 156  |    |  0  1  0  0  |
# A * A_1 =  |  364 260 261 312  | == |  0  0  1  0  | (mod 26)
#             \ 494 286 286 521 /      \ 0  0  0  1 /

buf = '' 
cipher = ''
for char in message:
    if 'a' <= char <= 'z':
        buf += char
    else:
        cipher += char
    if len(buf) == 4:
        X = []
        for ch in buf:
            X.append(ord(ch) - ord('a'))
        Y = [0, 0, 0, 0]
        for i in range(4):
            for j in range(4):
                Y[i] = Y[i] + A[i][j] * X[j]
            Y[i] = Y[i] + B[i]
            Y[i] = Y[i] % 26
        for i in range(4):
            cipher += chr(Y[i] + ord('a'))
        buf = ''
print cipher
# fucb{uzpexfrygluh}