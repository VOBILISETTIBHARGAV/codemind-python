a=input()
a=a.lower()
a=a.split()
count=0
for i in range(len(a)):
    x=str(a[i])
    for i in range(len(x)):
        if (x[i] in 'aeiou' and x[len(x)-i-1] not in 'aeiou') or (x[i] not in 'aeiou' and x[len(x)-i-1]  in 'aeiou'):
            count+=1
print(count//2)