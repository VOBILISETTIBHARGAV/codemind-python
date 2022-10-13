x=input()
x=x.split()
for i in range(len(x)):
    print(min(x[i]),max(x[i]),end=' ')