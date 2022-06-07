a=int(input())
m=a*a
rev=0
su=0
while a>0:
    temp=a%10
    rev=rev*10+temp
    a=a//10
k=rev*rev
pu=0
while k>0:
    semp=k%10
    pu=pu*10+semp
    k=k//10
if pu==m:
    print(True)
else:
    print(False)