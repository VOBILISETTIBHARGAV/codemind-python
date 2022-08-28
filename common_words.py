a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split()
b=b.split()
for j in range(len(b)):
    for i in range(len(a)):
        if a[i]==b[j]:
            print(b[j],end=' ')