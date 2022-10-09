x=int(input())
for i in range(x):
    a,b=list(map(int,input().split()))
    y=list(map(int,input().split()))
    z=list(map(int,input().split()))
    print(*(sorted(y+z)))