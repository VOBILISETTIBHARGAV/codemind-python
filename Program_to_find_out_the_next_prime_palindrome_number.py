def prime(n):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
    if c==0:
        return 1
    else:
        return 0
def palindrome(n):
    c=0
    k=n
    while n>0:
        temp=n%10
        c=c*10+temp
        n=n//10
    if c==k:
        return 1
    else:
        return 0
a=int(input())
for i in range(a+1,10000000):
    if prime(i) and palindrome(i):
        print(i)
        break