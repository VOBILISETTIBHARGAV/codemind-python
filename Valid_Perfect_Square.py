x=int(input())
for i in range(x):
    y=int(input())
    c=0
    for i in range(1,y):
        if i*i==y:
            c+=1
    if c>=1:
        print('True')
    else:
        print('False')