a,b,c=map(int,input().split())
s=(a+b+c)/2
import math
x=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(format(x,".2f"))