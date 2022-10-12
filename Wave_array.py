a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(1,a-1):
    if (b[i]>b[i-1] and b[i]<b[i+1]) or (b[i]<b[i-1] and b[i]<b[i+1]):
        c+=1
if c==(a//2)-1:
    print('yes')
else:
    print('no')