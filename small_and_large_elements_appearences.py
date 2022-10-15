a=input()
c=0
sum=0
mi=122
for i in range(len(a)):
    if ord(a[i])!=32 and ord(a[i])<mi:
        mi=ord(a[i])
x=chr(mi)
y=max(a)
for i in range(len(a)):
    if x==a[i]:
        c+=1
for i in range(len(a)):
    if y==a[i]:
        sum+=1
print(x,c,y,sum)