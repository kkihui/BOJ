import sys

dr = (0,0,-1,1)
dc = (1,-1,0,0)

def greedy(r,c,N,M,first,maxnum,map):
    candinate = []
    visit = set()
    visit.add((r,c))
    maxg = 0
    
    for _ in range(3): # 3개 더 찾기
        for k in range(4): # 4방향 탐색
            nr = r+dr[k]
            nc = c+dc[k]
            if 0 <= nr < N and 0 <= nc < M and (nr,nc) not in visit:
                candinate.append((map[nr][nc],nr,nc))
                visit.add((nr,nc))                
        candinate.sort()
        greed,r,c = candinate.pop() # 후보 중에 제일 큰 값 가진 애를 다음으로 삼음
        first += greed
    
    if first > maxg:
        maxg = first
        if maxg == 4*maxnum: #최대값 4배 있으면 바로 탈출, 계산량 줄임.
            print(maxg)
            exit()
    return maxg  
    
def search_4way(r,c,N,M,indexli,map,visit):  # 4방향 탐색
    for k in range(4):
        nr = r+dr[k]
        nc = c+dc[k]
        if 0 <= nr < N and 0 <= nc < M and (nr,nc) not in visit:
            indexli.append((map[nr][nc],nr,nc))
            visit.add((nr,nc))
          
def main():
    N,M = map(int,sys.stdin.readline().split())
    tetromap = [[0]*M for _ in range(N)]
    ans,entire,maxnum,start = 0,0,0,[]
    
    for i in range(N):
        row_input = list(map(int,sys.stdin.readline().split()))
        tetromap[i] = row_input
        entire += sum(row_input)
        
        for j in range(M):
            if tetromap[i][j] > maxnum:
                maxnum = tetromap[i][j]
        
    entire /= N*M
        
    for i in range(N):
        for j in range(M):
            if tetromap[i][j] >= entire: # 평균 보다 크거나 같으면 start 후보로 선점, 계산량 많이 줄임. # 평균이상의 수가 적힌 블록이 포함되어야 하지만, 반드시 말단 블록은 아님.
                start.append((i,j))
    
    while start != []: # 갈 수 있는데 다 가보기 + 평균 이상이 가운데 끼면 greedy 사용
        r,c = start.pop()
        firstnum = tetromap[r][c]
        second,third,last = [],[],[]
        visited = set()
        visited.add((r,c))
        a = greedy(r,c,N,M,firstnum,maxnum,tetromap)
        if a > ans:
            ans = a
        
        search_4way(r,c,N,M,second,tetromap,visited)
        first_visited = visited
        
        while second != []:
            secondnum,r,c = second.pop() # 후보 한번 씩 다 봄
            visited = first_visited
            search_4way(r,c,N,M,third,tetromap,visited) # 2번째 후보에서 4방향 탐색
            second_visited = visited
            
            while third != []:
                thirdnum,r,c = third.pop() # 후보 한번 씩 다 봄
                visited = second_visited
                search_4way(r,c,N,M,last,tetromap,visited) # 3번째 후보에서 4방향 탐색
                
                while last != []:
                    lastnum,r,c = last.pop()
                    maxtetro = firstnum+secondnum+thirdnum+lastnum
                    if maxtetro > ans:
                        ans = maxtetro
                        if ans == 4*maxnum: #최대값 4배 있으면 바로 탈출, 계산량 줄임.
                            print(ans)
                            exit()
                            
    print(ans)
    
    
if __name__ == "__main__":
    main()