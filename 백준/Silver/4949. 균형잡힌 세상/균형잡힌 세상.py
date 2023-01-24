import sys

def harmony(a):
    scount,lcount = 0,0
    openli = []
    for _ in a:
        if _ == '(':
            scount += 1
            openli.append(_)
        elif _ == ')':
            scount -= 1
            if scount < 0 or lcount < 0: #오른쪽 괄호가 먼저 나오면
                return 'no'
            
            if openli.pop() != '(': # 괄호 서순 안 맞으면
                return 'no'
        elif _ == '[':
            lcount += 1
            openli.append(_)
        elif _ == ']':
            lcount -= 1
            
            if scount < 0 or lcount < 0:
                return 'no'
            
            if openli.pop() != '[':
                return 'no'
        
    if scount != 0 or lcount != 0: #괄호 갯수가 다르면
        return 'no'      
    else:
        return 'yes'    

while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break
    print(harmony(s))