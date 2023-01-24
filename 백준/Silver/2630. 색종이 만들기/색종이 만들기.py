import sys
def slicecheck(li,n):
    wbli = [0,0]
    hap = 0
    
    for _ in li: # 종이 완성되면 return하고 끝
        hap += sum(_)
    
    if hap == 0:
        wbli[0] = 1
        return wbli
        
    if hap == n**2:
        wbli[1] = 1
        return wbli
    
    halfli1 = li[0:n//2]
    halfli2 = li[n//2:n]
    quadli1,quadli2,quadli3,quadli4 = [],[],[],[]
    for _ in halfli1: # 4등분
        quadli1.append(_[0:n//2])
        quadli2.append(_[n//2:n])
    for _ in halfli2:
        quadli3.append(_[0:n//2])
        quadli4.append(_[n//2:n])
    wbli[0] = slicecheck(quadli1,n//2)[0]+slicecheck(quadli2,n//2)[0]+slicecheck(quadli3,n//2)[0]+slicecheck(quadli4,n//2)[0]
    wbli[1] = slicecheck(quadli1,n//2)[1]+slicecheck(quadli2,n//2)[1]+slicecheck(quadli3,n//2)[1]+slicecheck(quadli4,n//2)[1]
    
    return wbli


N = int(sys.stdin.readline())
nli = [[] for _ in range(N)]
for _ in range(N):
    nli[_] = list(map(int,sys.stdin.readline().split()))
a =slicecheck(nli,N)
for _ in a:
    print(_)