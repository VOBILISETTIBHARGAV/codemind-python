a=int(input())
b=(2**a)
for i in range(0,b):
    c=0
    x=i
    m=[]
    while c<a:
        temp=x%2
        m.append(temp)
        x=x//2
        c+=1
    for i in range(len(m)-1,-1,-1):
        print(m[i],end="")
    print()