s1=input().lower()
s2=input().lower()
res=""
for i in s1:
    if i in s2 and i not in res and i!=' ':
        res+=i
res=list(res)
res.sort()
res=''.join(res)
if len(res)!=0:
    print(res)
else:
    print(-1)