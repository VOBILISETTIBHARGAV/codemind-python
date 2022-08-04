n=int(input())
l1=list(map(int,input().split()))
l2=set(l1)
l3=list(l2)
count=0
for i in range(len(l3)):
    count+=l3[i]
print(count)