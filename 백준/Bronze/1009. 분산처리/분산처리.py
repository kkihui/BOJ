import sys
# 연산을 줄이기 위해 제곱을 직접 계산 안 하고 일의 자리수 규칙으로 나머지결정
N = int(input())
for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    c = a%10
    d = b%4
    if (c==1 or c==5 or c==6):
        print(c)
    elif (c==0) :
        print(10)
    elif (c == 4 or c == 9):
        if(b%2 == 1):
            print(c)
        else:
            print((c**2)%10)
    else:
        if(d == 0):
            print((c**4)%10)
        else:
            print((c**d)%10)