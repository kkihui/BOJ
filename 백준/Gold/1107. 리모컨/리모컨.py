# 1. 100에서 +로 이동 2. 100에서 -로 이동 3. 목표 채널에서 ++ 4. 목표 채널에서 --
import sys

def only_plus(init,final):
    cnt = 0
    while init != final:
        init += 1
        cnt += 1
        if init == 500001:
            return 500001
    if cnt == 0:
        print(cnt)
        exit()
    return cnt

def only_minus(init,final):
    cnt = 0
    while init != final:
        init -= 1
        cnt += 1
        if init == -1:
            return 500001
    if cnt == 0:
        print(cnt)
        exit()
    return cnt

def target2plus(init,button):
    cnt = 0
    while True:
        numli = set(str(init))
        if numli <= button:
            return cnt + len(str(init))
        init += 1
        cnt += 1
        if init == 1000000: # 50만 보다 더 가서 내려 가는 것도 생각
            return 500001

def target2minus(init,button):
    cnt = 0
    while True:
        numli = set(str(init))
        if numli <= button:
            return cnt + len(str(init))
        init -= 1
        cnt += 1
        if init == -1:
            return 500001
              
def main():
    target = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    canuse = ['0','1','2','3','4','5','6','7','8','9']
    canuse = set(canuse)
    
    if M > 0: # 쓸 수 있는 숫자의 set을 만듦
        broken = list(map(str,sys.stdin.readline().split()))
        for _ in broken:
            canuse.remove(_)
    a = only_plus(100,target)
    b = only_minus(100,target)
    c = target2plus(target,canuse)
    d = target2minus(target,canuse)
    print(min(a,b,c,d))
    
if __name__ == "__main__":
    main()