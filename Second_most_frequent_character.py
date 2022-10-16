n=input()
arr=[]
for i in n:
    if i not in arr:
        arr.append(i)
arr2=[]
for i in arr:
    c=0
    for j in n:
        if i==j:
            c+=1
    arr2.append(c)
m1=max(arr2)
if len(arr2)==1:
     print(-1)
else:
    s_max=0
    for i in arr2:
        if i>s_max and i<m1:
            s_max=i
    if s_max==0:
        print(-1)
    else:
        for i in range(len(arr)):
            if arr2[i]==s_max:
                print(arr[i])
                break