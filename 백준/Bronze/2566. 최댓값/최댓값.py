alist = [0]*9
max = 0
row = 0
col = 0
for i in range(9):
    alist[i] = list(input().split())

for i in range(9):
    for k in range(9):
        if (max <= int(alist[i][k])):
            max = int(alist[i][k])
            row = i+1
            col = k+1
# print(alist) #행렬 잘 나오는지 확인
print(max)
print(row,col)