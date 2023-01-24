import sys

T = int(input())
for _ in range(T):
    cateli = []
    entireli = []
    n = int(sys.stdin.readline())
    for i in range(n):
        name,cate = map(str,sys.stdin.readline().split())
        if cate not in cateli:
            cateli.append(cate)
            entireli.append([cate,name])
        else:
            for j in entireli:
                if j[0] == cate:
                    j.append(name)
                    break
    ans = 1
    for i in entireli:
        ans *= len(i) # 옷개수 +1 (안 입는 경우)
    print(ans-1) # 아예 안 입는 경우 뺌