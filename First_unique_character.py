x=input()
for i in x:
    if x.count(i)==1:
        print(i)
        break
else:
    print(-1)