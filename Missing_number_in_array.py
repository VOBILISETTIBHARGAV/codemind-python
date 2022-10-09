x=int(input())
for i in range(x):
    y=int(input())
    l=list(map(int,input().split()))
    for i in range(1,y+1):
        if i not in l:
            print(i)