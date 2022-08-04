a=int(input())
l1=list(map(int,input().split()))
if a%2==0:
    print(*l1)
else:
    print(*l1,end=' 0')