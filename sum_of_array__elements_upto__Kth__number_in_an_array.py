a=int(input())
l=list(map(int,input().split()))
k=int(input())
x=0
count=0
for i in range(a):
    if l[i]==k:
        x=x+i
        break
for i in range(a):
    if i<=x:
        count=count+l[i]
print(count)