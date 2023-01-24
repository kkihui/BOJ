A = int(input())
B = int(input())
C = int(input())
res = list(str(A*B*C))
# print(res) # res 잘 나오나 확인
for i in range(10):
    count = 0
    for k in range(len(res)):
        if res[k] == str(i):
            count +=1
    print(count)