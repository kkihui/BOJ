import sys

def make_graph(list):
    for i in range(16):
        for j in range(16):
            if i != j:
                num1,num2,dist,step = i,j,0,8
                while step != 0:
                    if (num1<step and num2 >=step) or (num1>=step and num2 <step): # 글자 다르면
                        dist += 1
                    num1 %= step
                    num2 %= step
                    step //= 2
                list[i][j] = dist    

class Graph:
    def __init__(self,dist):
        self.mbti = [0]*16
        self.distance = dist
        
    def find_min(self):
        if max(self.mbti) >= 3: # 같은거 3개 이상이면 끝
            return 0
        else: # 해봤자 32개 밖에 안 됨 (32c3의 경우의 수)
            candinate = []
            for _ in range(16):
                if self.mbti[_] == 1:
                    candinate.append(_)
                elif self.mbti[_] == 2:
                    candinate.append(_)
                    candinate.append(_)
            length,minlength = len(candinate), 12
            for i in range(length):
                for j in range(length):
                    for k in range(length):
                        if i != j and  j != k and i != k:
                            a,b,c = candinate[i],candinate[j],candinate[k]
                            now = 0
                            now += self.distance[a][b]
                            now += self.distance[b][c]
                            now += self.distance[a][c]
                            minlength = min(minlength,now)
            return minlength
                
def main():
    distance = [[0]*16 for _ in range(16)]
    make_graph(distance)
    
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        g = Graph(distance)
        g.input = list(map(str,sys.stdin.readline().split()))
        
        if N > 32: # 비둘기집 원리
            print(0)
        else:    
            for mbti in g.input:
                cnt = 0
                if mbti[0] == 'E':
                    cnt += 8
                if mbti[1] == 'N':
                    cnt += 4
                if mbti[2] == 'F':
                    cnt += 2
                if mbti[3] == 'P':
                    cnt += 1
                g.mbti[cnt] += 1
            
            ans = g.find_min()
            print(ans)
        
if __name__ == '__main__':
    main()
