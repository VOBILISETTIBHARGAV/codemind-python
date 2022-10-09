x=int(input())
c=0
l=[]
while x>0:
    temp=x%10
    l.append(temp)
    x=x//10
for i in range(len(l)-1,-1,-1):
    if l[i]==6:
        l[i]=9
        break
for i in range(len(l)-1,-1,-1):
    print(l[i],end='')