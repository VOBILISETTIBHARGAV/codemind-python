n=int(input())
a=0
count=0
b=1
while b>0:
    c=a+b
    a=b
    b=c
    if b==n:
        count+=1
        break
    elif b>n:
        break
    else:
        continue
if count>0:
    print(True)
else:
    print(False)