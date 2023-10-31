import sys
import copy

def GaussElimination(size,matrix:list,coefficient:list,constant):
    r,c = size+1,size+2
    A = copy.deepcopy(matrix)
    B = copy.deepcopy(coefficient)
    
    # Forward elimination
    for row in range(r): # matrix랑 coefficient 결합하기
        A[row].append(B[row])
    
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
        x[row] = A[row][c-1] / A[row][row]
    
    if constant-10**-3 <= x[r-1] <= constant+10**-3:
        return True

    return False
    
    

def main():
    while True:
        d = int(sys.stdin.readline())
        coefficient,candinate = [],[]
        matrix = [[0]*(d+1) for _ in range(d+3)]
        if d == 0:
            break
        
        for i in range(d+3):
            for j in range(d+1):
                matrix[i][j] = i ** (d-j)
            input = float(sys.stdin.readline())
            coefficient.append(input)
        
        wrongnum = 0
        for i in range(1,d+3): # 첫번째 식 빼고 d+2개의 식 중에서 하나씩 제외해서 테스트
            testMatrix = []
            testCoefficient = []
            for j in range(1,d+3):
                if i != j: 
                    testMatrix.append(matrix[j])
                    testCoefficient.append(coefficient[j])
            result = GaussElimination(d,testMatrix,testCoefficient,coefficient[0])
            if result:
                wrongnum = i
                break  
        
        print(wrongnum)

if __name__ == '__main__':
    main()