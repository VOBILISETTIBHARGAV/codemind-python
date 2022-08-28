a=input()
a=a.lower()
if a=="".join(reversed(a)):
    print(True)
else:
    print(False)