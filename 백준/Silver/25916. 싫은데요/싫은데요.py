N,M = map(int,input().split())
Ali = list(map(int,input().split()))
sumli = []

if sum(Ali) <= M: # sum이 M보다 작으면 굳이 루프 돌릴 필요 X
    print(sum(Ali))
else:
    for _ in range(N): # 시작을 1~N 사이로 해봄
        sum = Ali[_]
        i = _
        while i <= N-2: # N-2보다는 작거나 같아야함
            if sum > M:
                sum -= Ali[i]
                break
            elif sum == M: # M되면 최댓값이라 그냥 끝내면 됨
                break
            else:
                i +=1
                sum += Ali[i]
        if sum == M:
            sumli.append(sum)
            break
        elif sum < M:
            sumli.append(sum)
    if sumli == []:
        print(0)
    else:
        print(max(sumli))