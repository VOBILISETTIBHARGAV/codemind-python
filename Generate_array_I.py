a=int(input())
b=list(map(int,input().split()))
for i in range(0,a,2):
    c=0
    while c<b[i+1] and b[i+1]!=0:
        print(b[i],end=' ')
        c+=1