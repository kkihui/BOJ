import sys

# 두 점 사이의 거리 구하기 (제곱 형태)
def calDist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(int,sys.stdin.readline().split())
        distance = calDist(x1,y1,x2,y2)
        
        # 두 원이 일치하는 경우 (무수히 많이 만남)
        if x1 == x2 and y1 == y2 and r1 == r2:
            ans = -1  
        # 포함 관계이거나 두 원 중심 사이의 거리보다 반지름 합이 작은 경우 (안 만남)
        elif distance < (r1-r2)**2 or (r1+r2)**2 < distance:
            ans = 0
        # 접하는 경우 (한 점)
        elif distance == (r1-r2)**2 or (r1+r2)**2 == distance:
            ans = 1
        # 두 점에서 만나는 경우
        else:
            ans = 2
        
        print(ans)
    
if __name__ == "__main__":
    main()