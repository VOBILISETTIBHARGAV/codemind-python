a=input()
a=a.lower()
count=0
su=0
x=[]
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count+=1
    if count==1:
        x.append(a[i])
        su+=1
if su==0:
    print("-1")
else:
    print(x[0])