# AITMCLab6

## Content

* Elgamal Encryption Scheme

* Definition: Digital Signature

* Elgamal Signature Scheme

## Lecture Note

### Elgamal Encryption Scheme

Key Generation, assume we have prime $p$ and generator $g$ of multiplicative group $Z^*_p$:

$(p, g) \rightarrow \{PUB\_KEY: y, PRI\_KEY: x\}$ 

2. choose $x$ randomly from $\{1,2,...,p-1\}$
3. compute $ y:=g^x\mod p$
4. return $\{PUB\_KEY:y, PRI\_KEY: x\}$

Encryption:

$(M\in \{0,1,2,...,p-1\},p,g,y)\rightarrow (c_1,c_2)$

1. choose $r$ randomly from $\{1,2,..., p-1\}$
2. compute $s:=y^r \mod p$
3. compute $c_1:=g^r\mod p$
4. compute $c_2:=m\cdot s\mod p$
5. return $(c_1, c_2)$

Decryption:

$(c_1,c_2, p,g, x)\rightarrow M$

NOTHING HERE

### Digital Signature

Including key generation, signify and verify; 

key generation: $keygen()=(PUB\_KEY, PRI\_KEY)$

signify: $signify(M,PRI\_KEY)=SIG$

verify: $verify(M, SIG, PUB\_KEY)=RES\in \{TRUE,FALSE\}$

Required:

$verify(M, signify(M, PRI\_KEY), PUB\_KEY)==TRUE$

hard to forge fake signature without $PRI\_KEY$

#### Why Digital Signature?

for message receiver, to verify message is sended by the trusted sender

for message sender, to let everyone know the message is TRUELY sended by him

The reason we use digital signature is almost the reason we use hand signature.

### Elgamal Signature Scheme

Key Generation, assume we have prime $p$ and generator $g$ of multiplicative group $Z^*_p$:

$(p,g)\rightarrow \{PUB\_KEY: y, PRI\_KEY: x\}$

1. choose $x$ randomly from $\{1,2,..., p-1\}$
2. compute $y:=g^x\mod p$
3. return $\{PUB\_KEY: y, PRI\_KEY:x\}$

Signify:

$(M, p, g, x)\rightarrow (r, s)$

1. choose $k$ randomly from $\{2,...,p-2\}$, satisfying $(k,p-1)=1$
2. compute $r:=g^k\mod p$
3. compute $s:=(H(M)-xr)k^{-1}\mod (p-1)$, where $H$ is a hash function
4. return $(r, s)$

Verify:

$(M,r,s,p,g, y)\rightarrow RES\in\{TRUE,FALSE\}$

1. return $TRUE$ if and only if $g^{H(m)}\equiv y^rr^s\pmod p$

## TIP

Encryption procedure and signifying procedure are both RANDOM

## Changelog

* 2020.12.13 First version

