a=input()
a=a.split()
count=0
for i in range(len(a)-1,len(a)):
    x=str(a[i])
    for i in range(len(x)):
        print(x[i])
        break