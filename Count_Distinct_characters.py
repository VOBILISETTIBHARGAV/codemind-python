x=input()
x=x.lower()
a=set(x)
l=sorted(a)
c=0
for i in range(len(l)):
    if ord(l[i])!=32:
        c+=1
print(c)