def solution(answers):
    question_num = len(answers)
    res = [[] for _ in range(3)]
    cnt = [0]*3
    
    # 수포자들의 정답
    for i in range(question_num):
        # 1번 수포자
        res[0].append(i%5+1)
        
        # 2번 수포자
        if i%2 == 0:
            res[1].append(2)
        else:
            if i%8 == 1 or i%8 == 3:
                res[1].append(i%8)
            else:
                if i%8 == 5:
                    res[1].append(4)
                if i%8 == 7:
                    res[1].append(5)
        
        # 3번 수포자
        if i % 10 < 2: 
            res[2].append(3)
        elif i % 10 < 4:
            res[2].append(1)
        elif i % 10 < 6:
            res[2].append(2)
        elif i % 10 < 8:
            res[2].append(4)
        else:
            res[2].append(5)
        
        # 문제 맞췄는지 판단
        for num in range(3):
            if res[num][i] == answers[i]:
                cnt[num] += 1
    
    # 등수 결정
    answer = []
    for num in range(3):
        if cnt[num] == max(cnt):
            answer.append(num+1)        
    return answer