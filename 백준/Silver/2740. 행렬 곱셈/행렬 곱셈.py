import sys
        
def matprint(matrix):
    for _ in range(len(matrix)):
        print(*matrix[_])
    
def multiplication(matA,matB,n,m,k):
    multiple_result = [[0]*k for _ in range(n)]
    for i in range(n):
        for j in range(k):
            component = 0
            for t in range(m):
                component += matA[i][t] * matB[t][j]
            multiple_result[i][j] = component
    return multiple_result

def main():
    N,M = map(int,sys.stdin.readline().split())
    matrixA = [[0]*M for _ in range(N)]
    for i in range(N):
        matrixA[i] = list(map(int,sys.stdin.readline().split()))
    
    M,K = map(int,sys.stdin.readline().split())
    matrixB = [[0]*K for _ in range(M)]
    for i in range(M):
        matrixB[i] = list(map(int,sys.stdin.readline().split()))
    
    result = multiplication(matrixA,matrixB,N,M,K)
    matprint(result)
    
    
if __name__ == "__main__":
    main()