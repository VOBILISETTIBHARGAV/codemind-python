a=int(input())
l=list(map(int,input().split()))
b=int(input())
count=0
for i in range(a):
        if(l[i]==b):
            print(i)
            count+=1
            break
if count==0:
    print(-1)