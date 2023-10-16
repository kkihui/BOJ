import sys
import heapq

def main():
    heap = []
    N = int(sys.stdin.readline())
    for _ in range(N):
        num = int(sys.stdin.readline())
        if num != 0:
            heapq.heappush(heap,(abs(num),num))
                                        
        else:
            if heap == []:
                print(0)
            else:
                print(heapq.heappop(heap)[1])    
    
if __name__ == '__main__':
    main()