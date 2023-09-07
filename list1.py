n=input("enter:")
l=[]
for i in range (len(n)):
    l.append(n[i])
print(l[0],end="")
c1=l[1]
print(c1,end='')
c1=int(c1)
c2=l[2]
c2=int(c1)
for i in range (3,len(l)):
    print(c1*c2,end='')
    c1=c2
    c2=l[i]
    