x=input()
x=x.lower()
a=set(x)
l=sorted(a)
for i in range(len(l)):
    if ord(l[i])!=32:
        print(l[i],end='')