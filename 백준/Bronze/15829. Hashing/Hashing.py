import sys
L = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
hash = 0
for _ in range(L):
    hash += ((ord(s[_])-96) * (31**_)) % 1234567891
print(hash)