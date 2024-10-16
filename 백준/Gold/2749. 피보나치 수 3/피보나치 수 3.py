'''
피보나치 행렬 사용 F_i+1 = F_i + F_i-1 & F_i = F_i+0
[F_i+1] = [1  1] [F_i  ]  = [1  1]^i [F_1] = [1  1]^i [1]
[F_i  ] = [1  0] [F_i-1]  = [1  0]   [F_0] = [1  0]   [0]
n <= 100해 이므로 O(logN) 이하로 연산 안 하면 무조건 시간 초과
'''
div = 1000000

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