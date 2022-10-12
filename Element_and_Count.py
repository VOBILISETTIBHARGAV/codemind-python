a=int(input())
l=list(map(int,input().split()))
x=[]
c=0
for i in range(a):
    c=0
    for j in range(a):
        if l[i]==l[j]:
            c+=1
    if l[i] not in x:
        print(l[i],c,end=' ')
        x.append(l[i])