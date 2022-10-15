x=int(input())
m=[]
l=[]
c=0
temp=3
while x>0:
    m=[]
    semp=x%10
    while c<temp:
        remp=semp%2
        m.append(remp)
        semp=semp//2
        c+=1
    l+=m
    x=x//10
    c=0
c=0
for i in range(len(l)-1,-1,-1):
    if l[i]==0 and c==0:
        continue
    else:
        print(l[i],end="")
        c+=1