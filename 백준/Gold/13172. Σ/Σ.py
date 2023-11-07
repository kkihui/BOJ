import sys
import math

def GCD(a:int,b:int):
    while b > 0:
        a,b = b,a%b
    return a

def decomposition(X:int):
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

def modular(a:int,b:int,X:int):
    basis = decomposition(X-2)
    max_num = max(basis)
    numli_exp2 = [0] * (max_num+1)
    numli_exp2[0] = b%X # b^(2^0)%X
    for i in range(1,max_num+1): # b^(2^1~2^29)%X
        numli_exp2[i] = (numli_exp2[i-1]**2)%X
    
    invb = numli_exp2[basis[0]]
    for i in range(1,len(basis)):
        invb = (invb *numli_exp2[basis[i]]) % X
    
    return (a*invb) % X
    
def main():
    M = int(sys.stdin.readline())
    ans = 0
    
    for _ in range(M):
        Ni,Si = map(int,sys.stdin.readline().split())
        gcd = GCD(Ni,Si)
        Ni //= gcd
        Si //= gcd
        ans += modular(Si,Ni,1000000007)
        ans %= 1000000007
    
    print(ans)
    
if __name__ == "__main__":
    main()