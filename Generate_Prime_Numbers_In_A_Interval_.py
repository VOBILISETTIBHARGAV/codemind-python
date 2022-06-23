def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1;
    if count==2:
        return 1
    else:
        return 0
a=int(input())
b=int(input())
count=0
for i in range(a+1,b):
    if prime(i):
        print(i)