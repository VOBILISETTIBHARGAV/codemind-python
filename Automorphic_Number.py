def amicable(n):
    k=n*n
    su=0
    while k>0:
        k=k//10
        su+=1
    return (su//2)
a=int(input())
k=a*a
import math
x=math.pow(10,amicable(a))
if k%x==a:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')