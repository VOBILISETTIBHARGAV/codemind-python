a,b=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
k=[]
c=0
c=0
for i in range(a):
    if l[i] in m:
        k.append(l[i])
print(len(set(k)))