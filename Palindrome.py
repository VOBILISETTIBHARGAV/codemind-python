a=int(input())
m=a
rev=0
while a>0:
    temp=a%10
    rev=rev*10+temp
    a=a//10
if m==rev:
    print('True')
else:
    print('False')