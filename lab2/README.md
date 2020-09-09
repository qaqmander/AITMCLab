# AITMCLab2

## Content

* Introduction to py2

  list, string operations

* Affine cryptography

  "from AITMCLab.libnum import invmod"

* Hill cryptography (%26) (optional)

  A good review of Linear Algebra

## Quick View

* Affine cryptography

  Encryption: $y = a  x + b (mod\ p)$

  Decryption: $x = a^{-1}(y-b)(mod\ p)$

  More about $a^{-1}(mod\ p)$: https://blog.csdn.net/qq_41897386/article/details/82289975

* Hill cryptography (optional)

  Encryption: $Y=AX+B(mod\ p)$

  Decryption: $X=A^{-1}(Y-B)(mod\ p)$

  Here we encrypt multi-char in one round.