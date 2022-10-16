n=input()
n=n.lower()
s=input()
s=s.lower()
q=""
c=0
for i in n:
    if i not in s and i not in q and i!=' ':
        q+=i
        c+=1
for i in s:
    if i not in n and i not in q and i!=' ':
        q+=i
        c+=1
print(len(q))