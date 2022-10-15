a=input()
a=a.split()
c=0
min=10
su=0
for i in range(len(a)):
    c=0
    x=str(a[i])
    for i in range(len(x)):
        if x[i] in 'aeiou':
            c+=1
    if c<min:
        min=c
for i in range(len(a)):
    c=0
    x=str(a[i])
    for i in range(len(x)):
        if x[i] in 'aeiou':
            c+=1
    if min==c:
        su+=1
print(su)