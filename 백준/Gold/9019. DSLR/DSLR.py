import sys
from collections import deque
# 방문한 곳 기록하게 해보하면 최대 1만번만 반복할 수 있음

character = ('D','S','L','R')
class DSLR:
    def __init__(self,init,final):
        self.final = final
        self.queue = deque()
        self.queue.append((init,''))
        self.visit = set()
        self.visit.add(init)
        
    def bfs(self):
        while len(self.queue) != 0 :
            temp,route = self.queue.popleft()
            for i in range(4):
                if i == 0:
                    num = (temp*2)%10000
                elif i == 1:
                    if temp == 0:
                        num = 9999
                    else:
                        num = temp - 1
                elif i == 2:
                    num = (temp//100%10)*1000 + (temp//10%10)*100 + (temp%10)*10+ temp//1000
                else:
                    num = (temp%10)*1000 + (temp//1000)*100 + (temp//100%10)*10 + temp//10%10
                
                if num == self.final:
                    res = ''.join((route,character[i]))
                    return res
                else:
                    if num not in self.visit:
                        self.visit.add(num)
                        new = (num,''.join((route,character[i])))
                        self.queue.append(new)
            
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        A,B = map(int,sys.stdin.readline().split())
        dslr = DSLR(A,B)
        ans = dslr.bfs()
        print(ans)

if __name__ == "__main__":
    main()