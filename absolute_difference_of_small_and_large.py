x=input()
x=x.split()
c=0
s=0
for i in range(len(x)):
    c=0
    s=0
    c+=ord(max(x[i]))
    s+=ord(min(x[i]))
    print(c-s,end=' ')