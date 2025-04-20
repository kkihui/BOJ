# stick 길이가 10^9이어도 2^30 이내이므로 30번 안에 다 찾기 ㄱㄴ
import collections

T = int(input())

for _ in range(T):
    n = int(input())
    sticks = list(map(int,input().split()))
    s_dict_li = []
    answer, answer_set = 0,0
    
    for i in range(n):
        stick = sticks[i]
        candi = [(0,stick)]
        deque = collections.deque([(0,stick)])
        visited = set()
        s_dict = {}

        while deque:
            cnt,length = deque.popleft()
            if length >= 2:
                if length//2 not in visited:
                    deque.append((cnt+1,length//2))
                    candi.append((cnt+1,length//2))
                    visited.add(length//2)
                
                if length % 2 == 1:
                    if length-length//2 not in visited:
                        deque.append((cnt+1,length - length//2))
                        candi.append((cnt+1,length - length//2))
                        visited.add(length - length//2)
        
        for num,length in candi:
            s_dict[length] = num
		
        s_dict_li.append(s_dict)
    
    for i in range(n):
        if not answer_set:
            answer_set = set(s_dict_li[i].keys())
        else:
            answer_set = answer_set.intersection(set(s_dict_li[i].keys()))
        
    answer_key = max(answer_set)
    
    for i in range(n):
        answer += s_dict_li[i][answer_key]
    
    print(answer)