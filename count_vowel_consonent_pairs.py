x=input()
x=x.lower()
count=0
for i in range(len(x)):
    if ord(x[i])!=32:
        if (x[i] in 'aeiou' and x[len(x)-i-1] not in 'aeiou') or  (x[i] not in 'aeiou' and x[len(x)-i-1]  in 'aeiou'):
            count+=1
print(count//2)