n=int(input())
count=0
while n>0:
    n=n//10
    count+=1
if  count==10:
    print('Valid')
else:
    print('Invalid')