x=int(input())
for i in range(x,0,-1):
    y=chr(64+i)
    for j in range(1,i+1):
        print(y,end=" ")
    print()