x=int(input())
y=list(map(int,input().split()))
for i in range(0,x,2):
    count=0
    while count<y[i+1] and y[i+1]!=0:
        print(y[i],end=' ')
        count+=1