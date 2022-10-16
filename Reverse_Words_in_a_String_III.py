def rev(s):
    s=s[::-1]
    return s
s=input()
x=list(s.split())
for i in x:
    print(rev(i),end=" ")