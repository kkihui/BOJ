# 부동 소수점 오류 발생하므로, 오차율 반영해줘야 함.

import sys

def is_between(a,b,c):
    return min(a,b) - 1e-8 <= c <= max(a,b) + 1e-8

def vertical_2_judge(y1,y2,y3,y4):
    L1_min = min(y1,y2)
    L1_max = max(y1,y2)
    L2_min = min(y3,y4)
    L2_max = max(y3,y4)
    # 세로선이 안 만나면
    if L1_max < L2_min or L2_max < L1_min:
        return 0
    # 세로선이 만나면
    else:
        return 1

def vertical_1_judge(y,y1,y2,y3,y4):
    # y가 [y1,y2]와 [y3,y4] 위에 있으면
    if is_between(y1,y2,y) and is_between(y3,y4,y): 
        return 1
    else:
        return 0

def judge(x,y,x1,x2,x3,x4,y1,y2,y3,y4):
    # 구한 교점이 L1과 L2 범위 안에 있으면
    if is_between(x1,x2,x) and is_between(x3,x4,x) and is_between(y1,y2,y) and is_between(y3,y4,y):  
        return 1
    else:
        return 0

def parallel_one_point_judge(x1,y1,x2,y2,x3,y3,x4,y4):
    # L1에서 어떤 점이 더 왼쪽에 있나
    if min(x1,x2) == x1:
        L1_min = (x1,y1)
        L1_max = (x2,y2)
    else:
        L1_min = (x2,y2)
        L1_max = (x1,y1)
    # L2에서 어떤 점이 더 왼쪽에 있나
    if min(x3,x4) == x3:
        L2_min = (x3,y3)
        L2_max = (x4,y4)
    else:
        L2_min = (x4,y4)
        L2_max = (x3,y3)
    # 끝 점이 일치하나
    if L1_max == L2_min:
        return L1_max
    elif L2_max == L1_min:
        return L2_max
    else:
        return 0
    

def main():
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    x3,y3,x4,y4 = map(int,sys.stdin.readline().split())
    point = 0
    
    # L1이 세로선인 경우
    if x1 == x2:
        L1_vertical = 1 # x = x1 (y1 <= y <= y2)
    # L1이 가로선이거나 기울기가 있을 경우
    else:
        L1_vertical = 0 # y = (y2-y1)/(x2-x1)*x + y2 - {(y2-y1)*x2/(x2-x1)}
    
    # L2가 세로선인 경우
    if x3 == x4:
        L2_vertical = 1 # x = x3 (y3 <= y <= y4)
    # L2가 가로선이거나 기울기가 있을 경우
    else:
        L2_vertical = 0 # y = (y4-y3)/(x4-x3)*x + y4 - {(y4-y3)*x4/(x4-x3)}
    
    # 둘 다 세로선일 경우
    if L1_vertical and L2_vertical:
        # x좌표 동일하고 y 좌표가 그 범위
        if x1 == x3 and vertical_2_judge(y1,y2,y3,y4):
            ans = 1
            # onepoint에서 만나는지 판단
            if min(y1,y2) == max(y3,y4):
                point = (x1, min(y1,y2))
            elif min(y3,y4) == max(y1,y2):
                point = (x3, min(y3,y4))
            
        else:
            ans = 0
    
    # L1만 세로선일 경우    
    elif L1_vertical:
        y = (y4-y3)/(x4-x3)*x1 + y4 - ((y4-y3)*x4/(x4-x3))
        # x1=x2가 [x3,x4] 범위 안에 있고 x좌표에 해당하는 y값이 범위 안에 있을 때
        if is_between(x3,x4,x1) and vertical_1_judge(y,y1,y2,y3,y4):
            ans = 1
            point = (x1, y)
        else:
            ans = 0
        
    # L2만 세로선일 경우    
    elif L2_vertical:
        y = (y2-y1)/(x2-x1)*x3 + y2 - ((y2-y1)*x2/(x2-x1))
        # x3=x4가 [x1,x2] 범위 안에 있고 x좌표에 해당하는 y값이 그 안에 있을 때
        if is_between(x1,x2,x3) and vertical_1_judge(y,y1,y2,y3,y4):
            ans = 1
            point = (x3, y)
        else:
            ans = 0
    
    # L1,L2 둘 다 대각선일 경우
    else:
        # 기울기가 일치한다면 (평행)
        if abs((y2-y1)/(x2-x1)-(y4-y3)/(x4-x3)) < 1e-8:
            L1_intercept = y2 - ((y2-y1)*x2/(x2-x1))
            L2_intercept = y4 - ((y4-y3)*x4/(x4-x3))
            # 절편 동일하고 범위도 일치할 때
            if abs(L1_intercept-L2_intercept) < 1e-8 and vertical_2_judge(x1,x2,x3,x4) and vertical_2_judge(y1,y2,y3,y4):
                ans = 1
                # 일치하는 직선인데 끝점만 같을 때
                point = parallel_one_point_judge(x1,y1,x2,y2,x3,y3,x4,y4)
            else:
                ans = 0 
                
        # 기울기가 다르다면
        else:
        # y를 일치한다고 두면 (y2-y1)/(x2-x1)*x + y2 - {(y2-y1)*x2/(x2-x1)} = (y4-y3)/(x4-x3)*x + y4 - {(y4-y3)*x4/(x4-x3)}
        # -> {(y2-y1)/(x2-x1)-(y4-y3)/(x4-x3)}*x = y4-y2 + {(y2-y1)*x2/(x2-x1)} - {(y4-y3)*x4/(x4-x3)}
        # -> x = [y4-y2 + {(y2-y1)*x2/(x2-x1)} - {(y4-y3)*x4/(x4-x3)}] / {(y2-y1)/(x2-x1)-(y4-y3)/(x4-x3)}
            x = (y4-y2 + ((y2-y1)*x2/(x2-x1)) - ((y4-y3)*x4/(x4-x3))) / ((y2-y1)/(x2-x1)-(y4-y3)/(x4-x3))
            y = (y4-y3)/(x4-x3)*x + y4 - ((y4-y3)*x4/(x4-x3))
            if judge(x,y,x1,x2,x3,x4,y1,y2,y3,y4):
                ans = 1
                point = (x, y)
            else:
                ans = 0
        
    print(ans)
    if point:
        print(*point)
        
if __name__ == "__main__":
    main()