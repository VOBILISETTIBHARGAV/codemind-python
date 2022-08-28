a=input()
a=a.split()
for i in range(len(a)):
    if i%2==0:
        a[i]="".join(reversed(a[i]))
print(*a)