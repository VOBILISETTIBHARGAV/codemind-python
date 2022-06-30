a,b=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
c=set(l)
d=set(m)
e=list(c)
f=list(d)
k=[]
n=[]
for i in range(len(e)):
    if e[i] not in f:
        k.append(e[i])
for i in range(len(f)):
    if f[i] not in e:
        n.append(f[i])
print(len(k)+len(n))