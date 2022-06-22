a=int(input())
b=int(input())
for i in range(a,b):
    rev=0
    m=i
    while i>0:
        temp=i%10
        rev=rev*10+temp
        i=i//10
    if rev==m:
        print(rev,end=' ')