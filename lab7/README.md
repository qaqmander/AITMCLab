# AITMCLab6

## Content

* Pohlig-Hellman algorithm

## Lecture Note

Assume cyclic group $G=Z^*_n$ with prime $n$, where $n-1=\prod_{i=1}^rp_i^{e_i}$. Given generator $g$ and $ y\in G$, compute $x\in Z $ such that $g^x\equiv y\pmod n$.

1. For each $i \in \{1,2,...,r\}$
2. ​    Calculate $g_i\equiv g^{(n-1)/p_i^{e_i}}\pmod n$, obviously $ord(g_i)=p_i^{e_i}$; let $x_i:=x\mod p_i^{e_i}$
3. ​    Calculate $y_i\equiv y^{(n-1)/p_i^{e_i}}\equiv g^{x(n-1)/p_i^{e_i}}\equiv g_i^{x}\equiv g_i^{x\mod p_i^{e_i}}\equiv g_i^{x_i}\pmod n$
4. ​    Find out $x_i$ by iteration if $p_i^{e_i}$ is small. (or with some other method)
5. Calculate $x$ by Chinese Remainder Theorem

## Changelog

* 2020.12.13 First version
* 2020.12.14 Fix typo, from fyh

