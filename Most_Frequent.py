x=int(input())
l=list(map(int,input().split()))
c=0
m=0
for i in range(x):
    for j in range(x):
        if(l[i]==l[j]):
            c+=1
    if c>m:
        m=c
        y=l[i]
    elif c==m:
        if y<l[i]:
            y
        else:
            y=l[i]
    c=0
print(y)