# 무게별로 dp를 만들어서 최대 값 찾기
# 최대 10만 길이의 dp에 대해 최대 100개의 N에 대해 계산하면 1천만으로 연산 가능.
import sys
          
def main():
    N,K = map(int,sys.stdin.readline().split())
    dp = [0]*(K+1)
    stuff_set = set()
    total_weight = 0
    ans = 0
    
    for idx in range(N):
        w, v = map(int,sys.stdin.readline().split())
        stuff_set.add((idx,w,v))
        total_weight += w
    
    # 무게 다 합쳐도 K 보다 작으면 가치의 합이 정답
    if total_weight <= K:
        while stuff_set:
            idx,w,v = stuff_set.pop()
            ans += v
        print(ans)
    # 아니면 DP로 연산
    else:
        for stuff in stuff_set:
            idx,w,v = stuff
            if w <= K:
                if dp[w] == 0:
                    dp[w] = [set([idx]),v]
                else:
                    if dp[w][1] < v:
                        dp[w] = [set([idx]),v]
        for i in range(K):
            if dp[i] != 0:
                for stuff in stuff_set:
                    idx,w,v = stuff
                    if not idx in dp[i][0]:
                        if i + w <= K:
                            if dp[i+w] == 0:
                                dp[i+w] = [dp[i][0].union(set([idx])),dp[i][1]+v]
                            elif dp[i+w][1] < dp[i][1] + v:
                                dp[i+w] = [dp[i][0].union(set([idx])),dp[i][1]+v]

        maximum = 0
        for i in range(K+1):
            if dp[i] != 0:
                maximum = max(maximum,dp[i][1])
        print(maximum)
            
if __name__ == "__main__":
    main()