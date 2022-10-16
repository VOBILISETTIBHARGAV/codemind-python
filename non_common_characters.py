n=input()
n=n.lower()
s=input()
s=s.lower()
q=""
for i in n:
    if i not in s and i not in q and i!=' ':
        q+=i
for i in s:
    if i not in n and i not in q and i!=' ':
        q+=i
x="".join(sorted(q))
print(x)