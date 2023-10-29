import sys
import heapq
                      
class DualPriorQueue:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.cnt = dict()
        
    def insert(self,input):
        if input in self.cnt:
            self.cnt[input] += 1
        else:
            self.cnt[input] = 1
        heapq.heappush(self.minheap,input)
        heapq.heappush(self.maxheap,(-input,input))
        
    def delete(self,MaxOrMin):
        if MaxOrMin == 1:
            while self.maxheap != []:
                ans = heapq.heappop(self.maxheap)[1]
                if self.cnt[ans] != 0:
                    self.cnt[ans] -= 1
                    return ans
            return None
        else:
            while self.minheap != []:
                ans = heapq.heappop(self.minheap)
                if self.cnt[ans] != 0:
                    self.cnt[ans] -= 1
                    return ans
            return None
            
    
def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        K = int(sys.stdin.readline())
        dpqueue = DualPriorQueue()
        for _ in range(K):
            command,num = map(str,sys.stdin.readline().split())
            num = int(num)
            
            if command == 'D':
                if dpqueue.maxheap != [] and dpqueue.minheap != []: # 비어 있지 않을 경우만 실행
                    dpqueue.delete(num)
                    
            if command == 'I':
                dpqueue.insert(num)
        
        if dpqueue.maxheap == [] or dpqueue.minheap == []:
            print("EMPTY")
        else:
            max = dpqueue.delete(1)
            min = dpqueue.delete(-1)
            if max == None and min == None:
                print("EMPTY")
            else:
                if max != None and min == None:
                    min = max
                elif max == None and min != None:
                    max = min 
                print("%d %d"%(max,min))
            
            
if __name__ == "__main__":
    main()