def solution(participant, completion):
    parti_dict = {}
    
    for human in participant:
        if human in parti_dict:
            parti_dict[human] += 1
        else:
            parti_dict[human] = 1
    
    for done in completion:
        parti_dict[done] -= 1
        
        if parti_dict[done] == 0:
            del parti_dict[done]
    
    answer = list(parti_dict.keys())[0]
    return answer