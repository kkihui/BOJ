import sys
            
def main():
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    x3,y3,x4,y4 = map(int,sys.stdin.readline().split())
    point_P = [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]
    point_Q = [(x3,y3),(x3,y4),(x4,y3),(x4,y4)]
    point_PQ = [(x1,y3),(x1,y4),(x2,y3),(x2,y4),(x3,y1),(x3,y2),(x4,y1),(x4,y2)]
    
    common = set()
    inner = set()
    line = set()
    
    # P의 네 꼭짓점 확인
    for x,y in point_P:
        if x in (x3,x4) or y in (y3,y4):
            if x3 <= x and x <= x4 and y3 <= y and y <= y4:
                common.add((x,y))
        elif x3 < x and x < x4 and y3 < y and y < y4:
            inner.add((x,y))
    
    # Q의 네 꼭짓점 확인
    for x,y in point_Q:
        if x in (x1,x2) or y in (y1,y2):
            if x1 <= x and x <= x2 and y1 <= y and y <= y2:
                common.add((x,y))
        elif x1 < x and x < x2 and y1 < y and y < y2:
            inner.add((x,y))
    
    # P와 Q를 합친 8개의 좌표 추가로 확인
    for x,y in point_PQ:
        if x1 <= x and x <= x2 and y1 <= y and y <= y2:
            if x3 <= x and x <= x4 and y3 <= y and y <= y4:
                inner.add((x,y))
    
    for pt in common:
        if pt in inner:
            inner.remove(pt)    
    
    if inner:
        print('FACE')
    elif common:
        if len(common) == 1:
            print('POINT')
        else:
            print('LINE')
    else:
        print('NULL')
        
    
if __name__ == "__main__":
    main()