a=input()
x=[]
count=0
for i in range(len(a)):
    if a[i]=='a' or a[i]=='i' or a[i]=='e' or a[i]=='o' or a[i]=='u':
        x.append(a[i])
if 'a' in x:
    count+=1
if 'i' in x:
    count+=1
if 'e' in x:
    count+=1
if 'o' in x:
    count+=1
if 'u' in x:
    count+=1
if count==5:
    print(True)
else:
    print(False)