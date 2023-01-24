import sys

warmli = []

def warm(li,num,a): #재귀로 계속 연결 찾아줌
    warmli.append(num)
    for _ in li[num]:
        if _ in warmli:
            pass
        else:
            warm(li,_,N)
    for _ in range(a):
         if num in li[_]:
             if _ in warmli:
                 pass
             else:
                 warmli.append(_)
                 warm(li,_,N)
    return warmli
        

N=int(sys.stdin.readline())
c=int(sys.stdin.readline())
connectli = [[] for _ in range(N+1)]

for _ in range(c): # 연결된 컴퓨터 목록을 2차원 list로
    a,b = map(int,sys.stdin.readline().split())
    connectli[a].append(b)

res = set(warm(connectli,1,N))
print(len(res)-1)