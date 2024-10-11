def solution(citations):
    cit_min = 0
    cit_max = max(citations)
    answer = 0
    
    for h in range(0,cit_max):
        cnt_cited = 0
        cnt_none = 0
        
        for citation in citations:
            if citation >= h:
                cnt_cited += 1
            else:
                cnt_none += 1
            
            if cnt_none > h:
                break
        
        if cnt_cited >= h and cnt_none <= h:
            answer = h
    
    return answer