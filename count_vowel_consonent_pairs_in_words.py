a=input()
a=a.lower()
a=a.split()
c=0
for i in range(len(a)):
    x=str(a[i])
    for i in range(len(x)):
        if (x[i] in 'aeiou' and x[len(x)-i-1] not in 'aeiou') or (x[i] not in 'aeiou' and x[len(x)-i-1]  in 'aeiou'):
            c+=1
print(c//2)