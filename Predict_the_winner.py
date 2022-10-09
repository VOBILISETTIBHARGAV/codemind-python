x=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in range(x):
    if i%2==0:
        c+=l[i]
    else:
        s+=l[i]
if (c-s)%4==0:
    print('X')
else:
    print('Y')