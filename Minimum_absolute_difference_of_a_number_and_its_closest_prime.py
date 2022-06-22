def palindrome(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return 1
    else:
        return 0
a=int(input())
i=1
while a>0:
    if palindrome(a):
        print(0)
        break
    elif palindrome(a+i) and palindrome(a-i):
        print(a-(a-i))
        break
    elif palindrome(a+i):
        print((a+i)-a)
        break
    elif palindrome(a-i):
        print(a-(a-i))
        break
    i+=1