import sys
import copy

class Matrix():
    def __init__(self):
        self.matrix = [[0]*4 for _ in range(3)]
   
    def determinant(self,matrix):
        a = matrix
        det = a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1]) - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0]) + a[0][2]* (a[1][0]*a[2][1]-a[1][1]*a[2][0])
        return det
    
    def determinant_4case(self):
        det = self.determinant(self.matrix)
        matrix1 = copy.deepcopy(self.matrix)
        matrix2 = copy.deepcopy(self.matrix)
        matrix3 = copy.deepcopy(self.matrix)
        for i in range(3):
            matrix1[i][0] = matrix1[i][3]
            matrix2[i][1] = matrix1[i][3]
            matrix3[i][2] = matrix1[i][3]
        det1 = self.determinant(matrix1)
        det2 = self.determinant(matrix2)
        det3 = self.determinant(matrix3)
        return det,det1,det2,det3

def main():
    T = int(sys.stdin.readline())
    for j in range(T):
        m = Matrix()
        for i in range(3):
            m.matrix[i] = list(map(int,sys.stdin.readline().split()))
        
        det,det1,det2,det3 = m.determinant_4case()
        print("%d %d %d %d"%(det1,det2,det3,det))
        if det == 0:
            print("No unique solution")
        else:
            sol = [det1/det,det2/det,det3/det]
            for _ in range(3):
                if -0.0005< sol[_] < 0.0005:
                    sol[_] = 0.000
            print("Unique solution: %.3f %.3f %.3f"%(sol[0],sol[1],sol[2]))
        print()
        
if __name__ == "__main__":
    main()