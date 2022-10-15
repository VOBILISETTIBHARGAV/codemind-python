a=int(input())
for i in range(a):
    x=int(input())
    l=list(map(int,input().split()))
    m=[]
    n=[]
    su=0
    for i in range(len(l)):
        m=[]
        n=[]
        z=i
        for i in range(0,z):
            m.append(l[i])
        for i in range(z+1,len(l)):
            n.append(l[i])
        if sum(m)==sum(n):
            print("YES")
            su+=1
            break
    if su==0:
        print("NO")