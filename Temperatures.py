a=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    x=l[i]
    m=i
    c=0
    for i in range(m+1,len(l)):
        if l[i]>x:
            print(i-m,end=" ")
            c+=1
            break
    if c==0:
        print(0,end=" ")