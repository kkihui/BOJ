import sys

def set_Pn(num):
    a = []
    for i in range(num):
        if i % 2: # odd
            a.append("O")
        else: # even
            a.append("I")
    return a
            
def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    S = list(sys.stdin.readline().rstrip())
    length,cnt = 2*N+1,0
    Pn = set_Pn(length)

    for _ in range(M-length+1):
        if S[_:length+_] == Pn:
            cnt +=1
        
    print(cnt)

if __name__ == "__main__":
    main()
