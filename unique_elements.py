x=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]==l[j]:
            if l[i] not in a:
                a.append(l[i])
print(*a)