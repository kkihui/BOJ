# p1p2를 이은 직선을 기준으로 그 위에 점이 있으면 일직선, 아래(우측)에 있으면 시계, 위(좌측)에 있으면 반시계
# p2가 p1 보다 좌측 이거나 하단에 있으면 반대가 됨.
# 부동 소수점 오류 발생하므로, 오차율 반영해줘야 함.

import sys

def main():
    point = []
    ans = 0
    for _ in range(3):
        x,y = map(int,sys.stdin.readline().split())
        point.append((x,y))
    
    x1,y1 = point[0]
    x2,y2 = point[1]
    x3,y3 = point[2]
    
    # p1p2 세로선 아닌 경우
    if x1 != x2:
        # p1p2 가로선 아닌 경우
        if y1 != y2:
            y = (y2-y1)/(x2-x1) *x3 + y2-x2*(y2-y1)/(x2-x1) 
            
            # p1p2 직선 위에 y3가 있으면 일직선
            if abs(y3-y) < 1e-9:
                ans = 0
            # p1p2 직선 위의 x3 좌표에 해당하는 y보다 위측이면 ccw (p2가 p1보다 왼쪽이면 반대)
            elif y3 > y:
                if x1 < x2: ans = 1
                else: ans = -1
            # p1p2 직선 위의 x3 좌표에 해당하는 y보다 아래쪽이면 cw (p2가 p1보다 왼쪽이면 반대)
            else:
                if x1 < x2: ans = -1
                else: ans = 1
        
        # p1p2 가로선인 경우
        else:
            # p3의 y 좌표도 같으면 가로 일직선
            if y3 == y2:
                ans = 0
            # p3의 y 좌표 작으면 하단에 있으므로 cw (p2가 p1보다 왼쪽이면 반대)
            elif y3 < y2:
                if x1 < x2: ans = -1
                else: ans = 1
            # p3의 y 좌표 크면 상단에 있으므로 ccw (p2가 p1보다 왼쪽이면 반대)
            else:
                if x1 < x2: ans = 1
                else: ans = -1            
    
    # p1p2 세로선인 경우    
    else:
        # p3의 x 좌표도 같으면 세로 일직선
        if x3 == x2: ans = 0
        
        # p3의 x 좌표 작으면 좌측에 있으므로 ccw (p2가 p1보다 아래면 반대)
        elif x3 < x2:
            if y1 < y2: ans = 1
            else: ans = -1
        
        # p3의 x 좌표 크면 우측에 있으므로 cw (p2가 p1보다 아래면 반대)
        else:
            if y1 < y2: ans = -1
            else: ans = 1
    
    print(ans)
        
if __name__ == "__main__":
    main()