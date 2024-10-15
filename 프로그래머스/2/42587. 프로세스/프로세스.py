import collections

def solution(priorities, location):
    queue = collections.deque()
    maxi = []
    answer = 0
    
    for i in range(len(priorities)):
        if i != location:
            queue.append((0,priorities[i]))
        else:
            queue.append((1,priorities[i]))
        maxi.append(priorities[i])
    maxi.sort()
    
    while len(queue) != 0:
        temp = queue.popleft()
        
        if temp[1] >= maxi[-1]:
            maxi.pop()
            answer += 1
            if temp[0]:
                return answer
        else:
            queue.append(temp)
    