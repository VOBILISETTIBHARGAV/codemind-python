a=input()
a=a.split()
c=0
mini=10
su=0
for i in range(len(a)):
    c=0
    x=str(a[i])
    for i in range(len(x)):
        if x[i] in 'aeiou':
            c+=1
    if c<mini:
        mini=c
print(mini)