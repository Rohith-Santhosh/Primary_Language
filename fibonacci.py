n=int(input('enter range :'))
s=0
r=1
r=int(r)
s=str(s)
n1=0
n2=1
n3=n1+n2
print(n1,n2,n3,end='')
for i in range(0,n):
    for i in range(len(str(n3))):
        n3=int(n3)
        r=int(r)
        r=r//n3
        r=str(r)
        s=s+r
        print(n3,end='')
    n1=n2
    n2=n3
    n3=n1+n2