a=int(input())
l1=list(map(int,input().split()))
x=set(l1)
y=list(x)
b=int(input())
l2=list(map(int,input().split()))
m=set(l2)
n=list(m)
c=0
for i in range(len(y)):
    if y[i] in n:
        c+=1
if c==len(y)==len(n):
    print(True)
else:
    print(False)