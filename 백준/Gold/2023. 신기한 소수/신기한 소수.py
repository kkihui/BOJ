# n이 커질수록 이전 숫자에 1,3,7,9 붙힌 것 중에서 되는 것만 가능해짐.

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
    n = int(sys.stdin.readline())
    
    # n <= 5 이하면 엄청 빨리 가능 (6부터는 n 뒤에 숫자 붙혀서 판단)
    if n <= 5:
        for num in range(10**(n-1),10**n):
            if is_prime(num):
                done = 1
                for i in range(n-1,0,-1):
                    if not is_prime(num // (10**i)):
                        done = 0
                        break
                if done:
                    print(num)
    
    else:
        prime_5678 = [[] for _ in range(4)]
        candidate = (1,3,7,9)
        
        for num in range(10**4,10**5):
            if is_prime(num):
                done = 1
                for i in range(4,0,-1):
                    if not is_prime(num // (10**i)):
                        done = 0
                        break
                if done:
                    prime_5678[0].append(num)

        # 뒤에 (1,3,7,9 붙혀서 판단)
        for i in range(n-5):
            for num in prime_5678[i]:
                for first in candidate:
                    if is_prime(num*10+first):
                        prime_5678[i+1].append(num*10+first)
                    
        for num in prime_5678[n-5]:
            print(num)

if __name__ == "__main__":
    main()