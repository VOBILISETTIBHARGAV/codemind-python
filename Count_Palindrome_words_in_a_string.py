a=input()
a=a.lower()
a=a.split()
count=0
for i in range(len(a)):
    if a[i]=="".join(reversed(a[i])):
        count+=1
print(count)