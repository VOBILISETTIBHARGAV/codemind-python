a=input()
count=0
for i in range(len(a)):
    if (ord(a[i])>=48 and ord(a[i])<=57) or (ord(a[i])>=65 and ord(a[i])<=90) or (ord(a[i])>=97 and ord(a[i])<=122) or ord(a[i])==32:
        count+=1
print(len(a)-count)