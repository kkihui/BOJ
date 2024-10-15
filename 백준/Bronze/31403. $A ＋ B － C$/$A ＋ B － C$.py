import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

print(A+B-C)
print(A*10**(len(str(B)))+B-C)