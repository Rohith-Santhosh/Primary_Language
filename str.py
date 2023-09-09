l1=[]
l2=[]
l3=[]
n1=int(input("enter the size of list 1:"))
n2=int(input("enter the size of list 2:"))
for i in range(n1):
    e=input("enter 1:")
    l1.append(e)
for j in range(n2):
    t=input("enter 2:")
    l2.append(t)
l2.extend(l1)
print(l2)