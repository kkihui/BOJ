import sys
N,K,R,Q=map(int,sys.stdin.readline().split())
typung = []
for _ in range(K):
    typung.append(list(map(int,sys.stdin.readline().split())))
for _ in range(1,K):
    l = typung[_][0] - typung[_-1][0] # 진행하는 날짜
    if typung[_][2] == typung[_-1][2]: # y좌표 같으니 x축으로 진행하는 경우
        if typung[_][1] < typung[_-1][1]: # 음의 방향으로 진행
            for i in range(1,l):
                typung.append([typung[_][0]-i,typung[_][1]+i,typung[_][2]])
        else:
            for i in range(1,l):
                typung.append([typung[_][0]-i,typung[_][1]-i,typung[_][2]])
    else: # y축으로 진행하는 경우
        if typung[_][2] < typung[_-1][2]: # 음의 방향으로 진행
            for i in range(1,l):
                typung.append([typung[_][0]-i,typung[_][1],typung[_][2]+i])
        else:
            for i in range(1,l):
                typung.append([typung[_][0]-i,typung[_][1],typung[_][2]-i])
typung.sort()

for _ in range(Q):
    i,x,y = map(int,sys.stdin.readline().split())
    infor = typung[i-1] # 그날 태풍의 정보 (j,x,y)
    equ = (x-infor[1])**2 + (y-infor[2])**2 #원의 방정식
    if equ > R**2: #반지름 제곱보다 크면 원 밖임
        print('gori')
    else:
        if i == N: # index error 방지 
            if infor[2] == typung[i-2][2]: #y좌표 같으니 x축으로 진행
                if typung[i-2][1] < infor[1]:#양의 방향 진행
                    if y-infor[2] > 0:
                        print('safe')
                    elif y-infor[2] == 0:
                        print('gori')
                    else:
                        print('unsafe')
                else:#음의 방향 진행
                    if y-infor[2] < 0:
                        print('safe')
                    elif y-infor[2] == 0:
                        print('gori')
                    else:
                        print('unsafe')
                
            else: #y축으로 진행
                if typung[i-2][2] < infor[2]:#양의 방향 진행
                    if x-infor[1] < 0:
                        print('safe')
                    elif x-infor[1] == 0:
                        print('gori')
                    else:
                        print('unsafe')
                else: #음의 방향 진행
                    if x-infor[1] > 0:
                        print('safe')
                    elif x-infor[1] == 0:
                        print('gori')
                    else:
                        print('unsafe')
        else:
            if infor[2] == typung[i][2]:#y좌표 같으니 x축으로 진행
                if  infor[1] < typung[i][1]:#양의 방향 진행
                    if y-infor[2] > 0:
                        print('safe')
                    elif y-infor[2] == 0:
                        print('gori')
                    else:
                        print('unsafe')
                else:#음의 방향 진행
                    if y-infor[2] < 0:
                        print('safe')
                    elif y-infor[2] == 0:
                        print('gori')
                    else:
                        print('unsafe')
            else: #y축으로 진행
                if infor[2]< typung[i][2]:#양의 방향 진행
                    if x-infor[1] < 0:
                        print('safe')
                    elif x-infor[1] == 0:
                        print('gori')
                    else:
                        print('unsafe')
                else: #음의 방향 진행
                    if x-infor[1] > 0:
                        print('safe')
                    elif x-infor[1] == 0:
                        print('gori')
                    else:
                        print('unsafe')