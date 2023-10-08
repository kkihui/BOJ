import sys
import math

primelist = []

def prime():
    for i in range(2,100000):
        prime = True
        for _ in range(2,int(math.sqrt(i))+1):
            if i%_ == 0:
                prime = False
                break
        if prime:
            primelist.append(i)

def factorization(num):
    n = num
    ans,res = {},[]
    while n != 1:
        for _ in primelist:
            if n % _ == 0:
                res.append(_)
                n //= _
    li = list(set(res))
    li.sort()
    
    for _ in li:
        ans[_] = 0
    for _ in res:
        ans[_] += 1
    for key,value in ans.items():
        print(key,value)           
        
def main():
    prime()
    T = int(sys.stdin.readline())
    for _ in range(T):
        a = int(sys.stdin.readline())
        factorization(a)

if __name__ == "__main__":
    main()        
                
