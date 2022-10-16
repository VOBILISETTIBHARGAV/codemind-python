n=input()
n=n.lower()
s=input()
s=s.lower()
q=""
for i in n:
    if i in s and i not in q and i!=' ':
        q+=i
print(len(q))