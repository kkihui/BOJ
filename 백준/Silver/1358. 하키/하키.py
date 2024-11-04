import sys
              
def main():
    w,h,x,y,p = map(int,sys.stdin.readline().split())
    ans = 0
    square = (x,y,x+w,y+h)
    # 왼쪽 반원 (p_x-x)^2 + (p_y-(y+h/2))^2 = h^2/4 -> p_y = y+h/2 +- sqrt(h^2/4-(p_x-x)^2)
    # 우측 반원 (p_x-(x+w))^2 + (p_y-(y+h/2))^2 = h^2/4 -> p_y = y+h/2 +- sqrt(H^2/4 - (p_x-(x+w))^2)
    
    for _ in range(p):
        p_x,p_y = map(int,sys.stdin.readline().split())
        # 사각형 위에 있는지 판단
        if square[0]<= p_x <= square[2] and square[1]<= p_y <= square[3]:
            ans += 1
        
        # 왼쪽 반원에 있는지 판단
        elif x - h/2 <= p_x <= x:
            conjugate = (h**2/4 - (p_x-x)**2)**0.5
            circle_y = (y+h/2-conjugate,y+h/2+conjugate)
            if circle_y[0] <= p_y <= circle_y[1]:
                ans += 1
            
        # 오른쪽 반원에 있는지 판단
        elif x+w <= p_x <= x+w+h/2:
            conjugate = (h**2/4 - (p_x-(x+w))**2)**0.5
            circle_y = (y+h/2-conjugate,y+h/2+conjugate)
            if circle_y[0] <= p_y <= circle_y[1]:
                ans += 1
        
    print(ans)
        
if __name__ == "__main__":
    main()