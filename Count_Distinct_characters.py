a=input()
a=a.lower()
x=set(a)
l=sorted(x)
count=0
for i in range(len(l)):
    if ord(l[i])!=32:
        count+=1
print(count)
