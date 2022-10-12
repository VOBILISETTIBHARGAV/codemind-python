a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(1,a-1):
    if (b[i]>b[i-1] and b[i]>b[i+1]):
        c+=1
if c==(a-1)//2:
    print(c)
else:
    print('-1')