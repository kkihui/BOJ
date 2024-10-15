import copy

def solution(triangle):
    tri = copy.deepcopy(triangle)
    height = 0
    while height < len(triangle)-1:
        for idx in range(height+1):
            tri[height+1][idx] = max(tri[height+1][idx],triangle[height+1][idx]+tri[height][idx])
            tri[height+1][idx+1] = max(tri[height+1][idx+1],triangle[height+1][idx+1]+tri[height][idx])
        height += 1
    
    return max(tri[-1])
    