import sys

num2 = 0
num5 = 0

n = int(sys.stdin.readline())
for _ in range(1,n+1):
    if _%2 != 0 and _%5 != 0: # 2의 배수도 5의 배수도 아니면 pass
        pass
    else:
        k = _
        while True:
            if k%2 != 0 and k%5 != 0:
                break
            else:
                if k%2 == 0:
                    num2 += 1
                    k = k//2
                if k%5 == 0:
                    num5 += 1
                    k = k//5
print(min(num2,num5))