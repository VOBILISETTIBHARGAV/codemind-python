x=str(input())
x=x.split()
ma=0
for i in range(len(x)):
    if len(x[i])>ma:
        ma=len(x[i])
for i in range(len(x)):
    if len(x[i])==ma:
        print(len(x[i]))
        break