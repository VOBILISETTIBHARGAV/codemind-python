x=int(input())
for i in range(x):
    y=int(input())
    l=list(map(int,input().split()))
    z=sorted(l)
    if z==l:
        print('0')
    else:
        print(max(z)-min(z))