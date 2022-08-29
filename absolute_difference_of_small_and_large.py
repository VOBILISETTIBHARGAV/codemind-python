a=input()
a=a.split()
count=0
su=0
for i in range(len(a)):
    count=0
    su=0
    count+=ord(max(a[i]))
    su+=ord(min(a[i]))
    print(count-su,end=' ')