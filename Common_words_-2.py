a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split()
b=b.split()
x=[]
y=[]
c=0
su=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if a[i]==a[j]:
            c+=1
    if c==1:
        x.append(a[i])
for i in range(len(b)):
    c=0
    for j in range(len(b)):
        if b[i]==b[j]:
            c+=1
    if c==1:
        y.append(b[i])
for i in range(len(x)):
    if x[i] in y:
        su+=1
print(su)