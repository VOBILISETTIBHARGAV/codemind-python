def pretty(a):
    if a%10==2 or a%10==3 or a%10==9:
        return 1
n=int(input())
for i in range(n):
    count=0
    m,a=map(int,input().split())
    for i in range(m,a+1):
        if pretty(i):
            count+=1
    print(count)