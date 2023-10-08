import sys

def sum_2darr(arr,r1,c1,r2,c2):
    newarr = arr[r1:r2]
    res = 0
    for _ in newarr:
        res += sum(_[c1:c2])
    return res

def main():
    N,M = map(int,sys.stdin.readline().split())
    li = [[0]*M for _ in range(N)]
    for _ in range(N):
        row = list(map(int,sys.stdin.readline().split()))
        li[_] = row
    K = int(sys.stdin.readline())
    for _ in range(K):
        i,j,x,y = map(int,sys.stdin.readline().split())
        print(sum_2darr(li,i-1,j-1,x,y))
        

if __name__=='__main__':
    main()

