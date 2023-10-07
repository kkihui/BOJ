import sys

def main():
    N,r,c = map(int,sys.stdin.readline().split())
    size = 2**N
    num = 0
    row,col = size,size
    
    while True:
        if row == r+1 and col == c+1:
            print(num+size**2-1)
            exit()
        
        if row-size//2 < r+1 <= row: # 2,3 사분면에 해당
            down = True
        else:
            down = False
            row = row-size//2
            
        if col-size//2 < c+1 <= col: # 1,2 사분면에 해당
            right = True
        else:
            right = False
            col = col-size//2
        
        if down and right: # 2사분면이면 4등분 중 3개 더해줌
            num += size*size//4*3
        elif down and not right:
            num += size*size//4*2
        elif right and not down:
            num += size*size//4*1

        size = size //2
    
    
if __name__ == "__main__":
    main()
