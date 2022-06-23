def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return 1
    else:
        return 0
a=int(input())
b=int(input())
x=1
while a>0:
    k=a+b+x
    if prime(k):
        print(x)
        break
    else:
        k=a+b
        x+=1