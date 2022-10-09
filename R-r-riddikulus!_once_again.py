x,y=list(map(int,input().split()))
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(y):
    a.append(l[i])
for i in range(y,x):
    b.append(l[i])
print(*(b+a))