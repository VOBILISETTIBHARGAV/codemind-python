x=int(input())
for i in range(x):
    x=input()
    if x=="".join(reversed(x)):
        if len(x)%2==0:
            print('YES','EVEN')
        else:
            print('YES','ODD')
    else:
        print('NO')