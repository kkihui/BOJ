import sys

T = int(sys.stdin.readline())
for _ in range(T):
    s = sys.stdin.readline().rstrip()
    if s.count('(') != s.count(')'): # 괄호 개수 다르면 NO
        print('NO')
    else: 
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count +=1
            else:
                count -=1
            if count < 0 : # 괄호 갯수 같지만 ')'가 먼저 나오면 NO
                print('NO')
                break
        if count == 0 :
            print('YES')