a=input()
count=0
x=[]
for j in range(len(a)):
    if(a[j]=='a'or a[j]=='i'or a[j]=='e'or a[j]=='o'or a[j]=='u')or(a[j]=='A'or a[j]=='I'or a[j]=='E'or a[j]=='O'or a[j]=='U'):
        if a[j] not in x:
            print(a[j],end=' ')
        x.append(a[j])
        count+=1
if count==0:
    print(-1)