n = int(input())

for i in range(2*n-1):
    if i >= n-1:
        num = 2*n-2-i
    else:
        num = i
    print(' '*(n-1-num),end='')
    print('*'*(2*num+1))