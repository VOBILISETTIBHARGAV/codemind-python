def prime(n):
    count=0
    if(n<2):
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return 0
        return 1
def palindrome(n):
    su=0
    k=n
    while n>0:
        temp=n%10
        su=su*10+temp
        n=n//10
    if su==k:
        return 1
    else:
        return 0
a=int(input())
for i in range(a+1,100000000):
    if prime(i) and palindrome(i):
        print(i)
        break