a=int(input())
l=list(map(int,input().split()))
c=0
sum=0
l1=set(l)
l2=list(l1)
for i in range(len(l2)):
    c=0
    for j in range(len(l)):
        if l2[i]==l[j]:
            c+=1
    if c==l2[i]:
        sum+=1
print(sum)