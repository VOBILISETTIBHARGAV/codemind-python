a=int(input())
rev=0
su=0
count=0
for i in range(1,a+1):
    if a%i==0:
        count+=1
while a>0:
    temp=a%10
    rev=rev*10+temp
    a=a//10
for i in range(1,rev+1):
    if rev%i==0:
        su+=1
if su==2 and count==2:
    print('circular prime')
elif count==2 and su!=2:
    print('prime but not a circular prime')
else:
    print('not prime')