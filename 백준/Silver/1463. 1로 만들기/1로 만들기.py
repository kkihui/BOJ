import sys

n = int(sys.stdin.readline())
count = 0
countli = [0]*(n+1)
for _ in range(2,n+1):
    count = _
    a,b = _,_
    if _%3 == 0:
        a = countli[_//3] + 1
    if _%2 == 0:
        b = countli[_//2] + 1
    c = countli[_-1] + 1
    count = min(count,a,b,c)
    countli[_] = count
print(countli[n])