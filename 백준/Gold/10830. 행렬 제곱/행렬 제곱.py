import sys
import math
import copy
# log2(천억)은 36.~~이므로 제곱한걸 이용해서 행렬 계산을 한다.

class Matrix():
    def __init__(self,size):
        self.matrix = [[0]*size for _ in range(size)]
        self.size = size
        self.basis = []
        self.max = 0
    
    def matprint(self,matrix):
        for _ in range(self.size):
            print(*matrix[_])
    
    def square(self,matrix):
        square_result = [[0]*self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                component = 0
                for k in range(self.size):
                    component += matrix[i][k] * matrix[k][j]
                square_result[i][j] = component%1000
        return square_result
    
    def multiplication(self,matA,matB):
        multiple_result = [[0]*self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                component = 0
                for k in range(self.size):
                    component += matA[i][k] * matB[k][j]
                multiple_result[i][j] = component%1000
        return multiple_result
    
    def decomposition(self,num):
        exp2 = 1
        while num != 0:
            if exp2 >= num:
                if exp2 > num:
                    exp2 = exp2//2
                if exp2 > self.max:
                    self.max = exp2
                self.basis.append(int(math.log2(exp2)))
                num -= exp2
                exp2 = 1
            else:
                exp2 *= 2
        
    def exponent(self):
        self.max = int(math.log2(self.max))
        self.matrix_exp2 = [0] * (self.max+1)
        self.matrix_exp2[0] = self.matrix
        for i in range(self.max):
            self.matrix_exp2[i+1] = self.square(self.matrix_exp2[i])
    
    def calculate(self,num):
        self.decomposition(num)
        self.exponent()
        ans = copy.deepcopy(self.matrix_exp2[self.max])
        for i in self.basis:
            if i == self.max:
                continue
            ans = self.multiplication(ans,self.matrix_exp2[i])
        for i in range(self.size): # 1제곱하는 경우 대비
            for j in range(self.size):
                ans[i][j] = ans[i][j]%1000
        self.matprint(ans) 

def main():
    N,B = map(int,sys.stdin.readline().split())
    m = Matrix(N)
    for i in range(N):
        m.matrix[i] = list(map(int,sys.stdin.readline().split()))
    m.calculate(B)
    
if __name__ == "__main__":
    main()