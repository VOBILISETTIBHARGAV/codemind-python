def palindrome(n):
    c=0
    while n>0:
        temp=n%10
        c=c*10+temp
        n=n//10
    return c
a=int(input())
while a>0:
    x=a+palindrome(a)
    if palindrome(x)==x:
        print(x)
        break
    else:
        a=x