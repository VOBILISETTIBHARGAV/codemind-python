x=int(input())
l=list(map(int,input().split()))
y=int(input())
a=max(l)
for i in range(x):
    if l[i]+y<a:
        print(False,end=' ')
    else:
        print(True,end=' ')