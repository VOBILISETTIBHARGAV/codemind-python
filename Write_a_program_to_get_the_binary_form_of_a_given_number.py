x=int(input())
c=0
for i in range(x):
    y=int(input())
    m=[]
    while y>0:
        temp=y%2
        m.append(temp)
        y=y//2
    for i in range(len(m)-1,-1,-1):
        print(m[i],end="")
    print()