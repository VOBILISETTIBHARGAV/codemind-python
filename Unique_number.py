x=int(input())
k=x
l=[]
c=0
flag=0
while x>0:
    temp=x%10
    l.append(temp)
    x=x//10
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]==l[j] and i!=j:
            c+=1
    if c==1:
        flag+=1
        break
    c=0
if flag==1:
    print('Not Unique Number')
else:
    print('Unique Number')