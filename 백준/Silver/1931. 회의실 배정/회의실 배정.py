import sys
N = int(sys.stdin.readline())
meetli = [[0,0] for _ in range(N)]
usemeetli = []
for _ in range(N):
    meetli[_] = list(map(int,sys.stdin.readline().split()))
meetli.sort(key = lambda x: (x[0],x[1])) #오름차순 정리
for _ in meetli:
    if usemeetli == []:
        usemeetli.append(_)
    else:
        if usemeetli[-1][0] == _[0]: #시작 시간 동일한 경우 but 같거나 더 늦게 끝남
            if _[0] == _[1]: # 시작과 끝이 같은 경우
                usemeetli.append(_)
            elif usemeetli[-1][0] == usemeetli[-1][1]: #앞선 회의가 시작과 동시에 끝나면
                usemeetli.append(_)

        else: # 시작 시간 늦은 경우,
            if usemeetli[-1][0] == usemeetli[-1][1]: #앞선 회의가 시작과 동시에 끝나면
                usemeetli.append(_)    
            elif usemeetli[-1][1] > _[1]: # 더 빨리 끝나는 경우
                usemeetli.pop()
                usemeetli.append(_)
            elif usemeetli[-1][1] == _[1] and _[0] != _[1]: # 같이 끝나지만 동시에 끝나는 경우 아님 (공존 불가)
                usemeetli.pop()
                usemeetli.append(_)
            elif usemeetli[-1][1] == _[1] and _[0] == _[1]: # 같이 끝나지만 동시에 끝나는 경우 (공존 가능)
                usemeetli.append(_)
            elif usemeetli[-1][1] <= _[0]: # 앞 회의의 끝나는 시간보다 시작 시간이 늦을 때
                usemeetli.append(_)
print(len(usemeetli))