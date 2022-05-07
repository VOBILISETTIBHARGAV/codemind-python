a=int(input())
s=0
for i in range(1,a):
    for j in range(a,1,-1):
        if i*i+j*j==a:
            s+=1
if s==1:
    print(False)
else:
    print(True)
        
        
