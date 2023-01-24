import sys

x = int(sys.stdin.readline())
den,num,k,sum = 1,1,1,1

# 분자는 1, 1-2, 3-2-1, 1-2-3-4, 5-4-3-2-1 순으로 진행 됨
# 분모는 1, 2-1, 1-2-3, 4-3-2-1, 1-2-3-4-5 순으로 진행됨

while sum < x: # 천만 까지 계산해도 4472면 끝남, x가 포함된 k번째 대각선과 그 때의 합 찾기
    k += 1
    sum = k*(k+1)//2

for _ in range(1,k+1): # k번째 대각선에서의 분수 찾기, k-1번째 까지의 sum과 반복한 횟수의 합이 x가 되면 종료
    if k%2 == 0: 
            num = _
            den = k+1-_
    else:
            num = k+1-_
            den = _
            
    if k*(k-1)//2 + _ == x:
        break
    
print('%d/%d'%(num,den))