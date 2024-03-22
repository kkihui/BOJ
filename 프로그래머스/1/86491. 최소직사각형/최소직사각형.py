def solution(sizes):
    hmax = 0
    wmax = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
        if wmax < sizes[i][0]:
            wmax = sizes[i][0]
        if hmax < sizes[i][1]:
            hmax = sizes[i][1]
    answer = wmax * hmax
    return answer