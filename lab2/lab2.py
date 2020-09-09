# Welcome to lab2, let's go through some grammars in python2
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
a, b = ??, ??
cipher = affine(message, a, b)
print cipher
# kyhv{pz_mzhyyl_yfez_HRIJDYhs_ezml_jtdg!!}

# Hill cryptography TODO