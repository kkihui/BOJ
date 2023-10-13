import sys
            
def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    S = sys.stdin.readline().rstrip()
    length,conti,cnt = 2*N+1,0,0
    
    if S[0] == 'I':
        conti = 1

    for _ in range(1,M):
        if conti == 0:
            if S[_] == 'I':
                conti = 1
                
        else:
            if S[_] != S[_-1]:
                conti += 1
            else:
                if S[_] == 'I':
                    conti = 1
                else:
                    conti = 0
        
        if conti >= length:
            if conti == length:
                cnt += 1
            elif (conti-length)%2 == 0:
                cnt += 1
                
    print(cnt)

if __name__ == "__main__":
    main()