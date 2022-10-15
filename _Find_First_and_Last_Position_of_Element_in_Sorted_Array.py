a=int(input())
l=list(map(int,input().split()))
k=int(input())
x=[]
m=0
for i in range(len(l)):
    if l[i]==k:
        x.append(i)
        break
for i in range(len(l)):
    if l[i]==k:
        m=i
x.append(m)
if k not in l:
    print(-1,-1)
else:
    print(*x)