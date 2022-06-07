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
count=0
su=0
for i in range(1,a+1):
    if a%i==0:
        su+=1
for i in range(1,a+1):
    if a%i==0:
        if prime(i):
            count+=1
print(su-count)