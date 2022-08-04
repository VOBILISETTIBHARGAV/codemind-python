b=int(input())
l=list(map(str,input().split()))
ml=0
for i in l:
    if len(i)>ml:
        ml=len(i)
for i in l:
    if len(i)==ml:
        print(i,end=" ")