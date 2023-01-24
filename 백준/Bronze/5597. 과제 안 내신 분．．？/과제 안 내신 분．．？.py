stset= set()
for i in range(28):
    stset.add(int(input()))
aset = set(range(1,31))
bset = aset - stset
alist = list(bset)
alist.sort()

print(alist[0])
print(alist[1])