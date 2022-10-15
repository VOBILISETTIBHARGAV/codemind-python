a=str(input())
a=a.split()
ma=100
for i in range(len(a)):
    if len(a[i])<ma:
        ma=len(a[i])
for i in range(len(a)):
    if len(a[i])==ma:
        print(len(a[i]))
        break