z=int(input())
l=list(map(int,input().split()))
c=0
s=0
x=[]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]==l[j]:
            c+=1
    if c>=2 and l[i] not in x:
        s+=c//2
        x.append(l[i])
print(s)