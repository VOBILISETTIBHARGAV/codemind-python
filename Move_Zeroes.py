x=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(x):
    if l[i]==0:
        a.append(l[i])
    else:
        b.append(l[i])
print(*(b+a))
        