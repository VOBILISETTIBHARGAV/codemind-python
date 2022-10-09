x=str(input())
c=0
for i in x:
    if ord(i)>=48 and ord(i)<=57:
        c+=1
if c>0:
    print('Contains ',end='')
    print(c ,end='')
    print(' digit')
else:
    print("Doesn't contain ",end='')
    print('digit')