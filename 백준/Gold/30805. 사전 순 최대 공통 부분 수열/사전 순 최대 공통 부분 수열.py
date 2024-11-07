# 겹치는 숫자 중에 제일 큰 거 먼저 찾고, 거기서 부터 뒤 중에 제일 큰거 찾고 느낌으로 하기.

import sys

def main():
    n = int(sys.stdin.readline())
    an = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    bn = list(map(int,sys.stdin.readline().split())) 
    
    a_real_idx = 0
    b_real_idx = 0
    ans = []
    
    while a_real_idx < len(an) and b_real_idx < len(bn):
        an_nums = sorted(list(set(an[a_real_idx:])))
        bn_nums = sorted(list(set(bn[b_real_idx:]))) 
        a_idx, b_idx = 0,0
        common_max = 0
    
        # 공통된 것 중 제일 큰 것 있는 idx 찾기    
        while a_idx < len(an_nums) and b_idx < len(bn_nums):
            if an_nums[a_idx] == bn_nums[b_idx]:
                if an_nums[a_idx] > common_max:
                    common_max = an_nums[a_idx]
                    a_real_idx_candi = a_real_idx + an[a_real_idx:].index(common_max) +1
                    b_real_idx_candi = b_real_idx + bn[b_real_idx:].index(common_max) +1
                
                if a_idx +1 < len(an_nums) and b_idx+1 < len(bn_nums):
                    if an_nums[a_idx+1] >= bn_nums[b_idx+1]:
                        b_idx += 1
                    else:
                        a_idx += 1
                else:
                    break
            elif an_nums[a_idx] < bn_nums[b_idx]:
                a_idx += 1
            else:
                b_idx += 1
        
        if common_max == 0:
            break
        else:
            ans.append(common_max)
            a_real_idx = a_real_idx_candi
            b_real_idx = b_real_idx_candi
    
    if ans:
        print(len(ans))
        print(*ans)
    else:
        print(0)
            
    
if __name__ == "__main__":
    main()