import sys

def main():
    s = sys.stdin.readline().rstrip()
    bomb = sys.stdin.readline().rstrip()
    
    while True:
        stack = []
        
        if len(s) < len(bomb):
            print(''.join(s))
            break
        
        for i in range(len(s)):
            stack.append(s[i])
            
            if stack[-1] == bomb[-1]: # 끝이랑 같을 경우를 이용해서 즉각적으로 폭발 시키기 (여러번 돌면 시간 초과 남)
                if len(bomb) <= len(stack):
                    bombcnt = 0
                    for j in range(len(bomb)):
                        if stack[-1-j] != bomb[-1-j]:
                            bombcnt = 1
                            break
                    if bombcnt == 0:
                        for _ in range(len(bomb)):
                            stack.pop()
                            
        if len(stack) == 0:
            print('FRULA')
            break
        elif len(stack) == len(s):
            print(''.join(stack))
            break
        else:
            s = stack

if __name__ == '__main__':
    main()