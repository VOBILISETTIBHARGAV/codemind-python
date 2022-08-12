a=int(input())
l=list(map(int,input().split()))
c=0
b=0
for i in range(a//2):
    c=c+l[i]
for i in range(a//2,a):
    b=b+l[i]
print(b-c)