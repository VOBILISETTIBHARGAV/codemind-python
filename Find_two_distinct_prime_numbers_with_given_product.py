def prime(n):
    su=0
    for i in range(1,n+1):
        if n%i==0:
            su+=1
    if su==2:
        return 1
    else:
        return 0
n=int(input())
count=0
for i in range(1,n):
    for j in range(1,n):
        if i*j==n:
            if count>0:
                break
            if prime(i) and prime(j):
                print(i,j,end=' ')
                count+=1
if count==0:
    print('-1')