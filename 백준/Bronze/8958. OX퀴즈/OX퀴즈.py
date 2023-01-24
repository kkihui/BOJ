N = int(input())
for i in range(N):
    score = 0
    A = input()
    mylist = list(A) # 받은 string을 list로 쪼개기
    # print(mylist) # mylist 확인용
    for k in range(len(mylist)):
        if mylist[k] == 'O' :
            score += 1
            for j in range(1,k+1): # 연속 될 경우 추가 점수
                if mylist[k-j] == 'X' : #X가 있으면 바로 끝
                    break
                else: # O이면 점수 추가
                    score += 1
        # print('%d번째 글자까지의 점수 : %d'%(k+1,score)) #점수 확인용
    print(score)