# 최대 20이므로 20!번 계산하게 되면 거의 100해개의 숫자가 나옴.
# 일일히 하는 것이 아니라, 그 자리수에 해당하는 factorial 활용해서 수를 결정해야함. (O(N) 되면 100해가 되기 때문.)

import sys
import math

def main():
    n = int(sys.stdin.readline())
    num_li = list(map(int,sys.stdin.readline().split()))
    candinate = list(range(1,n+1))
    length = 1
    
    # 1번 문제
    if num_li[0] == 1:
        num = num_li[1]-1
        ans = []
        
        while len(ans) != n:
            if num != 0:
                cal = math.factorial(n-length) 
                ans.append(candinate.pop(num//cal))
                num -= num//cal * cal
            else:
                ans.append(candinate.pop(0))
            length += 1
        
        print(*ans)
    
    # 2번 문제
    if num_li[0] == 2:
        ans = 1
        num_li.pop(0)
        while len(num_li) != 0:
            if num_li[0] != candinate[0]:
                for idx in range(len(candinate)):
                    if num_li[0] == candinate[idx]:
                        ans += math.factorial(n-length) * idx
                        num_li.pop(0)
                        candinate.pop(idx)
                        break
            else:
                num_li.pop(0)
                candinate.pop(0)
            length += 1
    
        print(ans)
        
if __name__ == "__main__":
    main()