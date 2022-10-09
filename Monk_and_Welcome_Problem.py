x=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
for i in range(x):
    s+=a[i]+b[i]
    print(s,end=' ')
    s=0