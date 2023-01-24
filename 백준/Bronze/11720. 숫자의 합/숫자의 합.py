N=int(input())
a=list(input()) #리스트로 받아서 다 잘림
sum = 0
# print(a) # a 잘 나왔는지 판단용
for i in range(N):
    sum += int(a[i])
print(sum)