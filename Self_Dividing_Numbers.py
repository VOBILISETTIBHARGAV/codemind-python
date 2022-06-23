def count(n):
    su=0
    while n>0:
        n=n//10
        su+=1
    return su
def dividing(n):
    k=n
    su=0
    while n>0:
        temp=n%10
        if temp>0:
            if k%temp==0:
                su+=1
        n=n//10
    return su
a=int(input())
b=int(input())
for i in range(a,b+1):
    if dividing(i)==count(i):
        print(i,end=' ')