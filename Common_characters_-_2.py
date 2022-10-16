s1=input().lower()
s1=s1.split()
r=s1[0]
res=[]
c=0
for i in r:
    for j in s1:
        if i not in j:
            break
    else:
        c+=1
print(c)