x=int(input())
l=list(map(int,input().split()))
y=1
for i in range(x):
    y*=l[i]
for i in range(l[x-1],y+1):
    m=i
    c=0
    for i in range(len(l)):
        if m%l[i]==0:
            c+=1
    if c==len(l):
        print(m)
        break