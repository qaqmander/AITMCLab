# Welcome to py2! First let's go through some basic grammars! 
# Feel free to use '#' to lead a one-line comment

# Output something as you like
print 'Hello XinXiSafetyShuXueBasic'

# You have variables like C-language, and you can assign values to them
a = 1 # int
b = 'Don\'t play microphone in class!!!' # str
c = [1, 2, 3] # list

# You can do some operating on variables
a = a + 1
print a  # 2
print b[0] + b[1]  # 'Do'
print len(c)  # 3

# Use if & for to construct complicated control flow
s = 0
for i in range(10):  # 0, 1, 2, 3, ..., 9
    if i % 2 == 0:
        s += i
print s  # 20

# You can program easier with built-in function, such as 'ord' and 'chr'
#   ord: str(length=1) -> int    Transfer character into ascii number
#   chr: int -> str(length=1)    Transfer ascii number into character
# Want to know more? 
#   https://www.runoob.com/python/python-func-ord.html
#   https://www.runoob.com/python/python-func-chr.html
print ord('a') # 97
print chr(97) # 'a'


# Use keyword 'import' to import other function from ctflab
from AITMCLab.libnum import n2s, s2n
print s2n('Happy Hacking')  # 5734583677810927947475323547239
print n2s(5734583677810927947475323547239) # 'Happy Hacking'
# Want to know more about AITMCLab.libnum? https://github.com/hellman/libnum

# Explore more grammars, use baidu

# Lab1
# Here is an encoding procedure, try to understand 
#     what happened and findout the message
message = 'flag{*************}'   # You can't see the message here!! hahaha
cipher = ''
key = 3
for char in message:
    if 'a' <= char <= 'z':
        now_cipher = (ord(char) - ord('a') + key) % 26
        cipher += chr(now_cipher + ord('a'))
    else:
        cipher += char
print cipher
# cipher = 'iodj{ece_lv_kdqgvrph}'
# Try to findout message!
# You DO NOT need to submit this lab
