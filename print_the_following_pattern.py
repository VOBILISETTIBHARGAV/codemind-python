a=int(input())
for i in range(1,a+1):
    for j in  range(1,a+1):
        if j<=i:
            print(j,end='')
    print()