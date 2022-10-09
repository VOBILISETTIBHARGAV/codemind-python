x=int(input())
l=list(map(int,input().split()))
a=set(l)
b=sorted(list(a))
if x<=2:
    print(l[-1])
else:
    print(b[-3])