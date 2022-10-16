x=int(input())
c=1
for i in range(1,x+1):
    for j in range(1,x+1):
        if(j==x or j==1 or j==c):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    c+=1