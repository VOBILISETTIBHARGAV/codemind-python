n=input()
q="aeiou"
x=0
c=1
for i in range(len(n)):
    c=1
    for j in range(i,len(n)-1):
        if n[j] in q and n[j+1] in q:
            c+=1
            if x<c :
                x=c
        else:
            if x<c :
                x=c
            c=0
print(x)