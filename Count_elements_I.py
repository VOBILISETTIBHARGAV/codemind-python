a,b=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
k=[]
for i in range(a):
    if l[i] in m:
        k.append(l[i])
print(len(set(k)))