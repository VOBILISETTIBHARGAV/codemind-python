x=input()
y=input()
c=0
for i in range(len(x)):
    if x[i]==y:
        c+=1
if c==0:
    print('-1')
else:
    print(c)