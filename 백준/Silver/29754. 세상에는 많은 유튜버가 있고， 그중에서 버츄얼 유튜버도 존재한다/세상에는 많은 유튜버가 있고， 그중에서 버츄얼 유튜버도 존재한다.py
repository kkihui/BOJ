import sys

def main():
    N,M = map(int,sys.stdin.readline().split())
    youtuber = dict()
    real_list = list()
    # 받으면서 방송 날짜랑 시간 기록
    for _ in range(N):
        name,day,start,end = map(str,sys.stdin.readline().split())
        day = int(day)
        time = (int(end[:2]) - int(start[:2])) * 60 + int(end[3:]) - int(start[3:])
        
        if not name in youtuber:
            youtuber[name] = [[0]*(M//7),[0]*(M//7)]
        youtuber[name][0][(day-1)//7] += 1
        youtuber[name][1][(day-1)//7] += time
        
    
    for name in youtuber.keys():
        real = 1
        for i in range(M//7):
            if youtuber[name][0][i] < 5 or youtuber[name][1][i] < 3600:
                real = 0
                break
        if real:
            real_list.append(name)    
    
    if real_list:
        real_list.sort()
        for ans in real_list:
            print(ans)
    else:
        print(-1)
    
if __name__ == '__main__':
    main()