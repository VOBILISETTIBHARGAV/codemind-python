def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return 1
    else:
        return 0
n=int(input())
k=n
count=0
su=0
while k>0:
    k=k//10
    su+=1
if prime(n):
    while n>0:
        temp=n%10
        if prime(temp):
            count+=1
        n=n//10
if count==su:
    print('Mega Prime')
else:
    print('Not Mega Prime')