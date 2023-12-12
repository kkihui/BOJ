import sys

def permutation(n,m):
    temp = [0]*m
    res = [tuple(temp)]
    end_cnt = 0
    while not end_cnt:
        for change in range(m-1,-1,-1):
            if temp[change]+1 <= n-1:
                temp[change] += 1
                for i in range(change+1,m):
                    temp[i] = 0
                res.append(tuple(temp))
                end_cnt = 0
                break
            else:
                end_cnt = 1
    return res
    
def main():
    n,m = map(int,sys.stdin.readline().split())
    numli = list(map(int,sys.stdin.readline().split()))
    numli.sort()
    permu = permutation(n,m)
    for i in range(len(permu)):
        for j in range(m):
            if j != m-1:
                print(numli[permu[i][j]],end=' ')
            else:
                print(numli[permu[i][j]],end='')
        print()
    

if __name__ == '__main__':
    main()