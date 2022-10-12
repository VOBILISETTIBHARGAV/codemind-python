a=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
su=0
x=[]
l1=set(l)
l2=list(l1)
for i in range(len(l2)):
    c=0
    for j in range(len(l)):
        if l2[i]==l[j]:
            c+=1
    if c==k:
        x.append(l2[i])
        su+=1
if su==0:
    print('-1')
else:
    print(*x)