a = input()
alist = []
for i in range(len(a)):
    if ord(a[i]) <= ord('z') and ord(a[i]) >= ord('a'):
        alist.append(a[i].upper())
    else:
        alist.append(a[i].lower())
a = ''.join(alist)
print(a)