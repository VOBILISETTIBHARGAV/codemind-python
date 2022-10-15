a=input()
a=a.split()
y=min(a[len(a)-1])
if y.lower() in a[len(a)-1] and y.upper() in a[len(a)-1]:
    print(y.lower())
else:
    print(y)