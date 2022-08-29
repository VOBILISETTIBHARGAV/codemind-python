a=input()
a=a.lower()
a=a.split()
count=0
for i in range(len(a)):
    x=str(a[i])
    for i in range(len(x)):
        if x[0] in 'aieou' and x[len(x)-1] not in 'aieou':
            count+=1
            break
print(count)