x=int(input())
l=list(map(int,input().split()))
c=0
for i in range(x):
    for j in range(x):
        if l[i]==l[j]:
            c+=1
    if c>=((x//2)+1):
        print(l[i])
        break
    c=0