def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n=int(input())
a=n
su=0
while n>0:
    temp=n%10
    su=su+fact(temp)
    n=n//10
if su==a:
    print('The number',end=' ')
    print(a,end=' ')
    print('is a strong number')
else:
    print('The number',end=' ')
    print(a,end=' ')
    print('is not a strong number')