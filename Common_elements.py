a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
x=[]
for i in range(len(l1)):
    if l1[i] in l2 and l1[i] not in x:
        x.append(l1[i])
print(*x)