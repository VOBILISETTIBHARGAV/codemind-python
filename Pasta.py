x,y=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=[]
c=0
for i in range(len(l2)):
        if l2[i] in l1 :
            if l2[i] not in a:
                c+=1
                a.append(l2[i])
if c==len(l2):
    print("Yes")
else:
    print("No")