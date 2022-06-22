n=int(input())
m=n
s=0
while n>0:
    n=n//10
    s+=1
ec=0
oc=0
while m>0:
    temp=m%10
    if temp%2==0:
        ec+=1
    else:
        oc+=1
    m=m//10
if oc==s and ec==0:
    print('Odd')
elif ec==s and oc==0:
    print('Even')
else:
    print('Mixed')