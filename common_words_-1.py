a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split()
b=b.split()
count=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            count+=1
print(count)