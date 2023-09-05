n=input("enter a string ")
m=input("enter a string ")
l1=len(n)
l2=len(m)
if(l1==l2):
    for i in range(l1):
        if(n[i]==m[i]):
            print(n[i],"=",m[i])
        else:
            print('not same')
else:
    print('not same')