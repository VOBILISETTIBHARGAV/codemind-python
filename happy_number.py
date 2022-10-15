def su(n):
    c=0
    while n>0:
        temp=n%10
        c+=temp**2
        n=n//10
    return c
x=int(input())
c=0
while x>0:
    if su(x)==1 or su(x)==7:
        c+=1
        break
    elif su(x)%10==su(x):
        break
    else:
        x=su(x)
if c==1:
    print(True)
else:
    print(False)