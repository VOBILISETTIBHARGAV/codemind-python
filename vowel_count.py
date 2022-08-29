a=input()
count=0
for i in range(len(a)):
    if(a[i]=='a'or a[i]=='i'or a[i]=='e'or a[i]=='o'or a[i]=='u')or(a[i]=='A'or a[i]=='I'or a[i]=='E' or a[i]=='O' or a[i]=='U'):
        count+=1
if count==0:
    print('0')
else:
    print(count)