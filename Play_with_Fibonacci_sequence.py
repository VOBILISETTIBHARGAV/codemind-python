n=int(input())
a=0 
b=1
print(a,end=' ')
print(b,end=' ')
for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    print(b,end=' ')