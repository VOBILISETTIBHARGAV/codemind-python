a=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
for i in range(len(l)//2):
    x.append(l[i])
for i in range(len(l)//2,len(l)):
    y.append(l[i])
for i in range(a//2):
    print(x[i],y[i],end=" ")