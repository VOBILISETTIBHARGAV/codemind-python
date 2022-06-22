def count(n):
    su=0
    while n>0:
        n=n//10
        su+=1
    return su
a,b=map(int,input().split())
import math
x=count(a)-b
y=math.pow(10,x)
z=math.pow(10,b)
m=int(a//y)
n=int(a%z)
if m>n:
    print(m-n)
else:
    print(n-m)