def palindrome(n):
    su=0
    k=n
    c=0
    while n>0:
        temp=n%10
        su=su*10+temp
        n=n//10
    if n<0:
        n=n*(-1)
        c+=1
    while n>0:
        temp=n%10
        su=su*10+temp
        n=n//10
    if c>0:
        su=su*(-1)
    return su
n=int(input())
print(palindrome(n))