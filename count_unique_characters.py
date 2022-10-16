n=input()
n=n.lower()
c=0
q=""
for i in n:
    if n.count(i)==1 and i!=' ':
        c+=1
print(c)