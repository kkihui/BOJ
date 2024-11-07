# 1의 자리와 제일 앞이 자리는 1,3,7,9만 가능.
# 최대값은 1억 (99,999,999) 까지 판단 8자리

import sys

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
   
def main():
    a,b = map(int,sys.stdin.readline().split())
    
    # 100 이하는 5,7,11 밖에 없음.
    prime_palin = [5,7,11]
    
    # 제일 앞이랑 1의 자리 가능한 숫자는 1,3,7,9
    candidate = (1,3,7,9)
    
    # 3의 자리 ~ 8의 자리 계산
    for n in range(3,9):
        for i in range(4):
            first_last = candidate[i]
            num = first_last * 10**(n-1) + first_last
            # 자리 수가 홀수일 경우 (3,5,7) 가운데는 10^(1,2,3)
            if n%2 == 1:
                for mid in range(10):
                    judge = num + mid * 10**(n//2)
                    if n >= 5:
                        for mid2 in range(10):
                            judge_5 = judge + mid2*10 + mid2*10**(n-2)
                            if n == 7:
                                for mid3 in range(10):
                                    judge_7 = judge_5 + mid3*10**2 + mid3*10**4
                                    if is_prime(judge_7):
                                        prime_palin.append(judge_7)
                            elif is_prime(judge_5):
                                prime_palin.append(judge_5)
                    elif is_prime(judge):
                        prime_palin.append(judge)
            # 자리 수가 짝수일 경우 (4,6,8)
            else:
                for mid in range(10):
                    judge = num + mid*10 + mid*10**(n-2)
                    if n >= 6:
                        for mid2 in range(10):
                            judge_6 = judge + mid2*10**2 + mid2*10**(n-3)
                            if n == 8:
                                for mid3 in range(10):
                                    judge_8 = judge_6 + mid3*10**3 + mid3*10**(n-4)
                                    if is_prime(judge_8):
                                        prime_palin.append(judge_8)
                            elif is_prime(judge_6):
                                prime_palin.append(judge_6)        
                    elif is_prime(judge):
                        prime_palin.append(judge)
    
    prime_palin.sort()
    
    for ans in prime_palin:
        if a <= ans <= b:
            print(ans)
    
    print(-1)                 
    
if __name__ == "__main__":
    main()