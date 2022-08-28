a=input()
a=a.split()
for i in range(len(a)):
    a[i]="".join(reversed(a[i]))
    print(a[i],end=" ")