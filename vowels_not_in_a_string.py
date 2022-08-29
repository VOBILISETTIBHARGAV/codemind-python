a=input()
x=[]
y=[]
count=0
for i in range(len(a)):
    if(a[i]=='a'or a[i]=='i'or a[i]=='e'or a[i]=='o'or a[i]=='u'):
        x.append(a[i])
if 'a' not in x:
    y.append('a')
    count+=1
if 'i' not in x:
    y.append('i')
    count+=1
if 'e' not in x:
    y.append('e')
    count+=1
if 'o' not in x:
    y.append('o')
    count+=1
if 'u' not in x:
    y.append('u')
    count+=1
if count>0:
    print(*y)
else:
    print('0')