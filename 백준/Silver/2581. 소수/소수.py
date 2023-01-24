M = int(input())
N = int(input())
declist = list() # 소수만 정리할 목록
comlist = list() # 합성수 목록
allist = list(range(M,N+1)) # 전체 목록

for i in range(M,N+1): # M~N 까지 반복함.
    if i == 2 : # 2일 경우 패스
        pass
    
    elif i == 1 : # 1일 경우 아무것도 안 한다
        comlist.append(i)
    
    else: # 3이상일 경우
        mylist = list(range(2,i)) #2부터i-1까지의 수로 나눠줄 거임
        #print(mylist) # 잘 나오나 확인 용
        for k in range(i-2):
            if (i % mylist[k] == 0): # k번째 수로 나눠 떨어지면 소수 아니니까 탈출
                comlist.append(i)
                break
            
         # 3이상인데 2~3까지 나눠서 안 나누어 떨어지면 소수니까 소수 목록에 추가
# print(allist) #전체 목록 확인용
# print(comlist) #합성수 목록 확인용
declist = [x for x in allist if x not in comlist] # 리스트 컴프리핸드를 통해 차집합 구하기 전체-합성수 = 소수
# print(declist) #소수 목록 확인용

if declist == []: # 소수가 없으면 -1 출력
    print(-1)
else:
    print(sum(declist)) # 합계
    print(declist[0]) # 제일 작은 소수    