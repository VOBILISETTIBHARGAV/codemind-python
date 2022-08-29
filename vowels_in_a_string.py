a=input()
b=input()
count=0
for i in range(len(a)):
    if a[i]==b:
        print(True)
        print(i)
        count+=1
        break
if count==0:
    print(False)