import sys

def permutation(n,m):
    temp = [1]*m
    res = [tuple(temp)]
    end_cnt = 0
    while not end_cnt:
        for change in range(m-1,-1,-1):
            if temp[change]+1 <= n:
                temp[change] += 1
                for i in range(change+1,m):
                    temp[i] = 1
                res.append(tuple(temp))
                end_cnt = 0
                break
            else:
                end_cnt = 1
    return res   

def main():
    n,m = map(int,sys.stdin.readline().split())
    permu = permutation(n,m)
    for i in range(len(permu)):
        print(*permu[i])

if __name__ == '__main__':
    main()