import copy
import sys

def main():
    n = int(sys.stdin.readline())
    triangle = []
    
    for _ in range(n):
        triangle.append(list(map(int,sys.stdin.readline().split())))
    
    
    tri = copy.deepcopy(triangle)
    height = 0
    while height < len(triangle)-1:
        for idx in range(height+1):
            tri[height+1][idx] = max(tri[height+1][idx],triangle[height+1][idx]+tri[height][idx])
            tri[height+1][idx+1] = max(tri[height+1][idx+1],triangle[height+1][idx+1]+tri[height][idx])
        height += 1
    
    print(max(tri[-1]))

if __name__ == "__main__":
    main()