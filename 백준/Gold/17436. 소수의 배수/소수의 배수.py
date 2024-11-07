# 1개의 소수는 그냥 나눈 몫.
# 2개의 소수는 2c1 한 것들 나눈 몫 합 - 둘 다 곱한 것으로 나눈 몫
# 3개의 소수는 3c1 한 것들 나눈 몫 합 - 3c2하여 곱한 것들 나눈 몫 합 + 셋 다 곱한 것으로 나눈 몫
# 4개는 4c1 - 4c2 + 4c3 - 4c4
# 10개의 소수가 있으면 10c1 = 10, 10c2 = 45, 10c3 = 120, 10c4 = 210, 10c5 = 252... 다 더하면 1022번

import sys
import itertools
   
def main():
    n,m = map(int,sys.stdin.readline().split())
    prime = list(map(int,sys.stdin.readline().split()))
    ans = 0
    
    for i in range(1,n+1):
        candidate = itertools.combinations(prime,i)
        for nums in candidate:
            multiple = 1
            for num in nums:
                multiple *= num
            # 홀수개 고르면 다 곱해서 더함.
            if i % 2 == 1:
                ans += m // multiple
            # 짝수개 고르면 다 곱해서 뺌.
            else:
                ans -= m // multiple
        
    print(ans)
    
    
if __name__ == "__main__":
    main()