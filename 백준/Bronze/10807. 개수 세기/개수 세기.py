ans=0

N = int(input())
numlist = list(input().split())
# print (numlist) #numlist 보여주는 역할
V = input()


for i in range(N):
    if V == numlist[i]:
        ans +=1
print(ans)