import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

if N%2 == 1:
    print(-1)
    exit()

if S.count('(') != S.count(')'): # 괄호개수 안 맞으면 -1 출력
    print(-1)

else:
    stack = []
    maxconti = 0
    
    for _ in range(N):
        if stack == []:
            stack.append(S[_])
        else:
            stack.append(S[_])
            if stack[-1] != stack[-2]:
                stack.pop()
                stack.pop() 
        
        if len(stack) > maxconti:
            maxconti = len(stack)

    if stack != []:
        print(-1)
    else:
        print(maxconti)