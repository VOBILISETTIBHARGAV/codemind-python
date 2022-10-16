z=input()
z=z.lower()
c=0
q=""
for i in z:
    if i not in q and z.count(i)==1 and i!=' ':
        q+=i
x="".join(sorted(q))
print(x)