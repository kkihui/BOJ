def solution(participant, completion):
    comple = dict()
    for name in completion:
        if name in comple:
            comple[name] += 1
        else:
            comple[name] = 1
    
    for name in participant:
        if name not in comple:
            answer = name
            break
        else:
            comple[name] -= 1
            if comple[name] == -1:
                answer = name
                break
    return answer