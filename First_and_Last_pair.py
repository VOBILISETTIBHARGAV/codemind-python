x=int(input())
l=list(map(int,input().split()))
z=[0]
for i in range(len(l)//2):
    print(l[i],l[len(l)-i-1],end=" ")
if len(l)%2!=0:
    print(l[len(l)//2],"0")