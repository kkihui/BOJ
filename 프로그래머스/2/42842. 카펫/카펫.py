def solution(brown, yellow):
    area = brown+yellow
    length = brown//2+2
    
    for height in range(1,length):
        width = length-height
        if height*(width) == area:
            return [width,height]