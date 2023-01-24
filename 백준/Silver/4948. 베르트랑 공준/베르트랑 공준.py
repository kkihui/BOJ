import sys
import math
def decimal(a):
    for i in range(2,int(math.sqrt(a))+1): # 1부터 루트a 까지 확인하여 소수 판별
        if a%i == 0:
            return False
    return True


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        count = 0
        for _ in range(n+1,2*n+1):
            if decimal(_) == True:
                count += 1
    print(count)
        