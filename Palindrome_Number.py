def palindrome(n):
    su=0
    k=n
    while n>0:
        temp=n%10
        su=su*10+temp
        n=n//10
    if k==su:
        return 1
    else:
        return 0
n=int(input())
for i in range(1,n+1):
    a=int(input())
    if palindrome(a):
        print(True)
    else:
        print(False)