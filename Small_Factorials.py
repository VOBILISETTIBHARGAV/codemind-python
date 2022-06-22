def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
a=int(input())
for i in range(0,a):
    n=int(input())
    print(fact(n))