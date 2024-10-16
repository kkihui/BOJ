'''
피보나치 행렬 사용 F_i+1 = F_i + F_i-1 & F_i = F_i+0
[F_i+1] = [1  1] [F_i  ]  = [1  1]^i [F_1] = [1  1]^i [1]
[F_i  ] = [1  0] [F_i-1]  = [1  0]   [F_0] = [1  0]   [0]
n <= 100해 이므로 O(logN) 이하로 연산 안 하면 무조건 시간 초과
'''
div = 1000000007

import sys

# 분할정복을 활용한 행렬 거듭제곱 사용
def matrix_fpow(matrix,n):
    if n==1:
        return matrix
    else:
        small_matrix = matrix_fpow(matrix,n//2)
        # 모듈러 덧셈, 뺄셈, 곱셈 연산 (A+B) mod C = (A mod C + B mod C) mod C
        a1 = ((small_matrix[0][0] * small_matrix[0][0]) % div + (small_matrix[0][1] * small_matrix[1][0]) % div) % div
        a2 = ((small_matrix[0][0] * small_matrix[0][1]) % div + (small_matrix[0][1] * small_matrix[1][1]) % div) % div
        a3 = ((small_matrix[1][0] * small_matrix[0][0]) % div + (small_matrix[1][1] * small_matrix[1][0]) % div) % div
        a4 = ((small_matrix[1][0] * small_matrix[0][1]) % div + (small_matrix[1][1] * small_matrix[1][1]) % div) % div
            
        if n%2 == 0:
            return [[a1,a2],[a3,a4]]
        else:
            return [[(a1+a2)%div,a1],[(a3+a4)%div,a3]]

def main():
    n = int(sys.stdin.readline())
    fibonacci_matrix = [[1,1],[1,0]]
    ans = matrix_fpow(fibonacci_matrix,n)
    
    print(ans[1][0])
            
if __name__ == "__main__":
    main()

''' 일반항을 이용한 연산은 오차가 많아서 포기, 행렬을 이용한 연산으로 시도

# 피보나치 수열 일반항 F_n = [(1+루트5)^n - (1-루트5)^n]/ (2^n*루트5)
# 증명 : F_n+2 = F_n+1 + F_n 이므로 F_n+2 -a*F_n+1 = b(F_n+1 - a*F_n)으로 두고 풀면, a+b = 1 ab=-1 이므로 x^2-x-1=0의 두 근이 된다.
# n <= 100해 이므로 O(logN) 이하로 연산 안 하면 무조건 시간 초과

div = 1000000007

import sys

# 분할정복을 활용한 거듭제곱 사용
def fpow(C,n):
    if n==1:
        return C
    else:
        x = fpow(C,n//2)
        # 모듈러 제곱근 연산 A^B mod C = ((A mod C)^B) mod C
        if n%2 == 0:
            return (x*x) % div
        else:
            return (x*x*C) % div

def main():
    n = int(sys.stdin.readline())
    # 모듈러 나눗셈은 역원 b^M-2 사용
    term1 = fpow((1+5**0.5)/2,n) % div
    term2 = fpow((1-5**0.5)/2,n) % div
    denominator = fpow(5**0.5,div-2) % div
    
    # 모듈러 덧셈, 뺄셈 연산 (A+B) mod C = (A mod C + B mod C) mod C
    # fibonacci = (term1 - term2) % div
    fibonacci = ((term1 - term2)%div * denominator)%div
    
    print(fibonacci)
    print(5**0.5)
            
if __name__ == "__main__":
    main()

'''