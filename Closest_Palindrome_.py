def palindrome(n):
    count=0
    k=n
    while n>0:
        temp=n%10
        count=count*10+temp
        n=n//10
    if k==count:
        return 1
    else:
        return 0
a=int(input())
i=1
while a>0:
    if palindrome(a+i) and palindrome(a-i):
        print(a-i,a+i)
        break
    elif palindrome(a+i):
        print(a+i)
        break
    elif palindrome(a-i):
        print(a-i)
        break
    i+=1