import sys

xli = []
yli = []
count = 0
s = sys.stdin.readline().rstrip()
sli = list(s)

for _ in range(len(sli)-1):
    if sli[_] == sli[_+1]:
        if sli[_] == '(':
            xli.append(_+1)
        else:
            yli.append(_+1)

for _ in yli:
    for i in xli:
        if i < _:
            count += 1
        else:
            break
print(count)