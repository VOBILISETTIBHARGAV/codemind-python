x=input()
x=x.lower()
c=0
for i in range(len(x)):
    if ord(x[i])!=32:
        if (x[i] in 'aeiou' and x[len(x)-i-1] not in 'aeiou') or  (x[i] not in 'aeiou' and x[len(x)-i-1]  in 'aeiou'):
            c+=1
print(c//2)