z=int(input())
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if a>=z and b>=z and a==b:
        print('ACCEPTED')
    elif a>=z and b>=z and a!=b:
        print('CROP IT')
    elif a<z or b<z:
        print('UPLOAD ANOTHER')