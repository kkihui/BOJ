import sys
import copy

def GaussElimination(size,matrix:list):
    r,c = size,size+1
    A = copy.deepcopy(matrix)
    
    # Forward elimination
    for stRow in range(r): # 위의 행 이용해서 밑의 행의 앞부분들 제거
        pivot = A[stRow][stRow]
        for tgRow in range(stRow+1,r):
            m = A[tgRow][stRow]/pivot
            if m != 0: # targetRow의 pivot이 0이 아니라면
                for col in range(c): # 행끼리 빼서 0 만들어줌
                    A[tgRow][col] -= A[stRow][col] * m
            
    for stRow in range(r-1,-1,-1): # 아래 행 이용해서 위의 행의 뒷부분들 제거 (Gauss-jordan)
        pivot = A[stRow][stRow]
        for tgRow in range(stRow-1,-1,-1):
            m = A[tgRow][stRow]/pivot
            if m != 0: # targetRow의 pivot이 0이 아니라면
                for col in range(c): # 행끼리 빼서 0 만들어줌
                    A[tgRow][col] -= A[stRow][col] * m
     
    # Backward substitution
    x = [0]*r
    for row in range(r):
        x[row] = round(A[row][c-1] / A[row][row])
    
    return x
    

def main():
    N = int(sys.stdin.readline())
    matrix = []
    for _ in range(N):
        input = list(map(int,sys.stdin.readline().split()))
        matrix.append(input)
    result = GaussElimination(N,matrix)
    
    print(*result)
    

if __name__ == '__main__':
    main()