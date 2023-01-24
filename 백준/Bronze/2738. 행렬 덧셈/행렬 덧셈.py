N,M = map(int,input().split())
alist =[]
blist = []
anslist = [[0]*M for _ in range(N)]
for i in range(N):
    alist.append(input().split())
# print(alist) #alist 잘 나오나 확인
# print(anslist) #비어있는 list 잘 나오나 확인

for i in range(N):
    blist.append(input().split())
# print(blist) #blist 잘 나오나 확인

for i in range(N):
    for k in range(M):
        anslist[i][k] = int(alist[i][k])+int(blist[i][k])
for i in range(N):
    print(*anslist[i])