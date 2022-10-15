a=input()
x=[]
c=0
for i in range(len(a)):
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
        x.append(a[i])
if 'a' in x:
    c+=1
if 'e' in x:
    c+=1
if 'i' in x:
    c+=1
if 'o' in x:
    c+=1
if 'u' in x:
    c+=1
if c==5:
    print(True)
else:
    print(False)