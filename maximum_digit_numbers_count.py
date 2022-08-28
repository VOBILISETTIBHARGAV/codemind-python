a=int(input())
l=list(map(str,input().split()))
c=0
for i in l:
    if len(i)>c:
        c=len(i)
for i in l:
    if len(i)==c:
        print(i,end=' ')