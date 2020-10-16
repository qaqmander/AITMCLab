from libnum import invmod,n2s
c=3808740243451829078210724960912929301578515217667342177748504822876637487457955515274108053834689975926677363518389793704175328503134131135222019673109070160582400165248020145405704970220361687652902588280756668081550609197401147259204898810928417434170277979905559815094009996366760441244275219995751156342
n=10999687930887680707038926445934606154952916940968581490041059775550485116500433363190163190149269018664612556276327671880157597616757778207737495630969441
c = 13134489820394613222282607681686272081419875146946401883172682167011759113388373349180457979897848113275982219264879081189886853062717764580364698888338032141434053832247476010400449272010082460437747190468766740274587999336359171283098137261396013153130265440425676242061845667887640808895666325466803989428

from math import sqrt
l,r=0,n
while l<r-1:
    mid=(l+r)/2
    if mid*mid<=n:
        l=mid
    else:
        r=mid
a=l
i=0
while True:
    i+=1
    if i%100000==0:
        print i
    if n%a==0:
        print a,n//a
        break 
    a-=1

p=104879397075344024438671231239628115011303349344697797964879592144922079000957 
assert n%p==0
q=n/p
print p,q

phi=(p-1)*(q-1)
t=pow(c,phi,n*n)-1
t1=t//n
phi_=invmod(phi,n)
aa = t1 * phi_ % n
print aa
print n2s(aa)
# flag = s2n('flag{can_you_find_me??}')