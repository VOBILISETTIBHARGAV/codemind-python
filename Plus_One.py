a=int(input())
l=list(map(int,input().split()))
t=0
z=0
y=[]
n=[]
count=0
for i in range(a-1,-1,-1):
    t=(t*10)+l[i]
while t>0:
    z=(z*10)+(t%10)
    t=t//10
z=z+1
while z>0:
    y.append(z%10)
    z=z//10
    count+=1
for i in range(count-1,-1,-1):
    n.append(y[i])
print(*n)