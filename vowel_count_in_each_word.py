a=input()
a=a.split()
count=0
for i in range(len(a)):
    count=0
    x=str(a[i])
    for i in range(len(x)):
        if x[i] in 'aieou':
            count+=1
    print(count,end=' ')