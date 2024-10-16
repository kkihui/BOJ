import sys
import math

def main():
    ans = 0
    n = int(sys.stdin.readline())
    numlist = []
    while n > 0:
        num = math.floor(math.log2(n))
        numlist.append(num)
        n -= 2**num
        if num == 0:
            break
    
    for num in numlist:
        ans += 3**num
    
    print(ans)

if __name__ == '__main__':
    main()