a=int(input())
l=list(map(int,input().split()))
count=0
for i in range(a):
    if l[i]%2==0:
        count=count+l[i]
    else:
        break
print(count)