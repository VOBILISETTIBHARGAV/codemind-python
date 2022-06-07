a=int(input())
import math
m=a
k=m
su=0
count=0
while a>0:
    a=a//10
    count+=1
while m>0:
    temp=m%10
    su=su+math.pow(temp,count)
    m=m//10
    count-=1;
if(su==k):
    print(True)
else:
    print(False)