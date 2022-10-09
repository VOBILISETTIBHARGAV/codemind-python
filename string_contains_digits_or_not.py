x=int(input())
for i in range(x):
    a=input()
    c=0
    for i in range(len(a)):
        if ord(a[i])>=48 and ord(a[i])<=57:
            c+=1
    if c>0:
        print('Yes')
    else:
        print('No')