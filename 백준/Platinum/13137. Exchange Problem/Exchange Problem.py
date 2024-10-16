# 동전끼리 배수 관계이면 무조건 됨
# 배수 관계 아니면, 모든 동전합 까지 그리디와 dp의 결과 비교

import sys

inf = 100000

def main():
    n = int(sys.stdin.readline())
    coin_list = list(map(int,sys.stdin.readline().split()))
    coin_set = set(coin_list)
    
    dp = [inf] * (coin_list[-1]*2+1)
    dp[0] = 0
    yes = 1
    
    for i in range(1,n):
        if coin_list[i] % coin_list[i-1] != 0:
            yes = 0
            break
    # 모든 동전이 배수 관계이면 무조건 됨
    if yes:
        print('Yes')
    
    # 배수 관계 아니면 판단해봐야 함
    else:
        yes = 1
        # dp로 전체 계산해보기
        for coin in coin_list:
            dp[coin] = 1
        
        for i in range(1,coin_list[-1]*2+1):
            if dp[i] == 1:
                continue
            else:
                for j in range(n):
                    if i - coin_list[j] >= 0:
                        if dp[i - coin_list[j]] != inf:
                            dp[i] = min(dp[i],dp[i-coin_list[j]]+1)
                    else:
                        break
        
        # greedy로 주어진 동전의 n배인 값들 계산해보기
        guess_list = []
        for i in range(1,n):
            for j in range(i,n):
                if coin_list[i] + coin_list[j] <= 2*coin_list[-1]:
                    guess_list.append(coin_list[i]+coin_list[j])
            for j in range(3,5):
                if coin_list[i]*j <= 2*coin_list[-1]:
                    guess_list.append(coin_list[i]*j)
            
        for guess in set(guess_list):
            cnt = 0
            num = guess
            while num != 0:
                idx = n-1
                while idx >= 0:
                    if coin_list[idx] <= num:
                        cnt += 1
                        num -= coin_list[idx]
                    else:
                        idx -= 1
                
                for j in range(n-1,-1,-1):
                    if coin_list[j] <= num:
                        cnt += 1
                        num -= coin_list[j]
                        break
            
            if dp[guess] != cnt:
                yes = 0
                break
    
        if yes:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()