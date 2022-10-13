a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split()
b=b.split()
x=[]
y=[]
count=0
su=0
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count+=1
    if count==1:
        x.append(a[i])
for i in range(len(b)):
    count=0
    for j in range(len(b)):
        if b[i]==b[j]:
            count+=1
    if count==1:
        y.append(b[i])
for i in range(len(x)):
    if x[i] in y:
        su+=1
print(su)