def reverse(v):
    #print(s)
    temp=""
    f=0
    for i in range(len(v)):
        if v[i] >= 'a' and v[i] <= 'z' or v[i] >= 'A' and v[i] <= 'Z':
            temp+=v[i]
            f=1
    temp=temp[::-1]
    q=list(v)
    #print(q)
    x=0
    for i in range(len(q)):
        if q[i] >= 'a' and q[i] <= 'z' or q[i] >= 'A' and q[i] <= 'Z':
            q[i]=temp[x]
            x+=1
    u=""
    for i in range(len(q)):
        u+=q[i]
    return u
s=input()
print(reverse(s))