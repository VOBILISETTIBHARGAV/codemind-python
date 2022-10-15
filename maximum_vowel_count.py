x=input()
x=x.split()
c=0
max=0
for i in range(len(x)):
    c=0
    a=str(x[i])
    for i in range(len(a)):
        if a[i] in 'aeiou':
            c+=1
    if c>max:
        max=c
print(max)