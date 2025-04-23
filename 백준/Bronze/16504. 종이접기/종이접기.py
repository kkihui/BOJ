import sys
n = int(sys.stdin.readline())
ans = 0
for i in range(n): ans += sum(map(int,sys.stdin.readline().split()))
print(ans)