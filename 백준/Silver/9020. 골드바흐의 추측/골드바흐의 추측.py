import sys
import math

def prime(a): # 그 수가 소수인지 찾는 함수
    if a == 1:
        return False
    
    for i in range(2,int(math.sqrt(a))+1): # 1부터 루트a 까지 확인하여 소수 판별
        if a%i == 0: # 나눠 떨어지면 소수 아님
            return False
    return True

def primeli(b): # 2부터 b까지 소수의 list를 에라토스테네스의 채로 찾는 함수 
    numberli = [True]*(b)
    for _ in range(2,int(math.sqrt(b))+1):
        if numberli[_] == True:
            for i in range(_+_,b,_):
                numberli[i] = False
    
    return [k for k in range(2,b) if numberli[k]==True]

T = int(sys.stdin.readline())
for _ in range(T):
    a = int(sys.stdin.readline()) 
    numli = primeli(a)
    sumli = []
    
    for _ in numli: # 주어진 짝수보다 작은 소수 목록에서 합이 같은 경우를 겹치는거 빼고 다 추가
        if prime(a-_) == True and not a-_ in sumli:
            sumli.append(_)
    k = len(sumli)
    print(sumli[k-1],a-sumli[k-1]) # 마지막이 차가 제일 적음