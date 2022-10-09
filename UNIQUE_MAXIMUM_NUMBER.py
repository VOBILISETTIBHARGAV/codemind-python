x=int(input())
l=list(map(int,input().split()))
a=set(l)
b=list(l)
s=0
z=[]
c=0
for i in range(len(b)):
    for j in range(len(l)):
        if b[i]==l[j]:
            c+=1
    if c==1:
        z.append(b[i])
        s+=1
    c=0
if s==0:
    print('-1')
else:
    print(max(z))
    