import collections

def solution(progresses, speeds):
    deque = collections.deque()
    answer = []
    
    for i in range(len(progresses)):
        deque.append([progresses[i],speeds[i]])
    
    while len(deque) != 0:
        done = 0
        deque_li = list(deque)
        
        for i in range(len(deque_li)):
            deque_li[i][0] += deque_li[i][1]
        
        deque = collections.deque(deque_li)
        
        if deque_li[0][0] >= 100:
            end = 0
            while not end and len(deque) != 0:
                temp = deque.popleft()
                if temp[0] >= 100:
                    done += 1
                else:
                    deque.appendleft(temp)
                    end = 1

        if done != 0:
            answer.append(done)
    
    return answer