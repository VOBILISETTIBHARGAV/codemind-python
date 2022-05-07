a,b=map(int,input().split())
for i in range(1,b+1):
    if a%i==0 and b%i==0:
        gcd=i
print(int(a*b/gcd))