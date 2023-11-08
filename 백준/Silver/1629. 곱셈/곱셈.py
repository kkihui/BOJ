import sys
import math
# B를 2^n꼴의 합들로 분해해서 그것의 나머지의 곱으로 계산하기.

def decomposition_by2(X:int):
    exp2 = 1
    basis = []
    while X != 0:
        if exp2 >= X:
            if exp2 > X:
                exp2 = exp2//2
            basis.append(int(math.log2(exp2)))
            X -= exp2
            exp2 = 1
        else:
            exp2 *= 2
    return basis

def calculate_mod(a:int,b:int,c:int):
    basis = decomposition_by2(b)
    max_num = max(basis)
    numli_exp2 = [0] * (max_num+1)
    numli_exp2[0] = a%c # a^(2^0)%c
    for i in range(1,max_num+1): # a^(2^1~2^max)%X
        numli_exp2[i] = (numli_exp2[i-1]**2)%c
    
    res = numli_exp2[basis[0]]
    for i in range(1,len(basis)):
        res *= numli_exp2[basis[i]]
        res %= c

    return res
    
def main():
    A,B,C = map(int,sys.stdin.readline().split())
    ans = calculate_mod(A,B,C)
    print(ans)
    
if __name__ == "__main__":
    main()