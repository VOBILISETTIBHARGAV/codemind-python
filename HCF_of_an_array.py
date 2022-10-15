a=int(input())
l=list(map(int,input().split()))
m=[]
n=[]
for i in range(len(l)):
    x=l[i]
    for i in range(1,l[i]+1):
        if x%i==0:
            m.append(i)
for i in range(len(m)):
    c=0
    for j in range(len(m)):
        if m[i]==m[j]:
            c+=1
    if c==a:
        n.append(m[i])
print(max(n))