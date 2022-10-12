a=int(input())
l=list(map(int,input().split()))
x=[]
c=0
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]==l[j]:
            c+=1
    if c==l[i]:
        if l[i] not in x:
            x.append(l[i])
if len(x)==0:
    print("-1")
else:
    print(*x)