def su(n):
    count=0
    while n>0:
        temp=n%10
        count=count+temp
        n=n//10
    return count
a=int(input())
while a>0:
    if su(a)%10==su(a):
        print(su(a))
        break
    else:
        a=su(a)