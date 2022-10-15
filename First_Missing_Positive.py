x=input()
l=list(map(int,input().split()))
c=0
for i in range(1,max(l)):
    if i not in l:
        print(i)
        c+=1
        break
if c==0:
    print(max(l)+1)