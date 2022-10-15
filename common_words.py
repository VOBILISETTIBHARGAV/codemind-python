x=input()
y=input()
x=x.lower()
y=y.lower()
x=x.split()
y=y.split()
for i in range(len(y)):
    for j in range(len(x)):
        if y[i]==x[j]:
            print(y[i],end=' ')