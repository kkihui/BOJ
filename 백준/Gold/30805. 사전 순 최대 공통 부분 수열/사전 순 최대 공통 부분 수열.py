# 겹치는 숫자 중에 제일 큰 거 먼저 찾고, 거기서 부터 뒤 중에 제일 큰거 찾고 느낌으로 하기.

import sys
import itertools

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

''' 앞에서 부터 긴 공통된 수열 찾으려고 하면 제일 큰 거 위치가 다르면 문제 발생
import sys
import itertools

# 100 * 100 = 100000

def main():
    n = int(sys.stdin.readline())
    an = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    bn = list(map(int,sys.stdin.readline().split())) 
    
    a_idx, b_idx = 0,0
    common = []
    real_end = 0
    
    while not real_end:
        end = 0
        for i in range(a_idx,n):
            end = 0
            for j in range(b_idx,m):
                if an[i] == bn[j]:
                    common.append(an[i])
                    a_idx = i+1
                    b_idx = j+1
                    end = 1
                    break
            if end:
                break
        if not end:
            real_end = 1
            break
    
    print(common)
    idx = 0
    ans = []
    while idx != len(common):
        maxi = max(common[idx:])
        end = 1
        for i in range(idx,len(common)):
            if common[i] == maxi:
                ans.append(common[i])
                idx = i+1
                end = 0
                break
        if end:
            break
    
    if ans:
        print(len(ans))
        print(*ans)
    else:
        print(0)
    
if __name__ == "__main__":
    main()
'''