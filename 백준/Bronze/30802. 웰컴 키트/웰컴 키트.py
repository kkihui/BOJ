import sys

N = int(sys.stdin.readline())
T_size = list(map(int,sys.stdin.readline().split()))
T,P = map(int,sys.stdin.readline().split())

total_T = 0

for tshirt in T_size:
    total_T += tshirt//T
    if tshirt % T != 0:
        total_T += 1


print(total_T)
print(N//P, N%P)