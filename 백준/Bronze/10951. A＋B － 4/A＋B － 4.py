import sys

while True:
    try:
        a,b = map(int,sys.stdin.readline().rstrip().split()) # sys.stdin.readlin()은 input()보다 빠름 rstrip()으로 공백 제거
        print(a+b)
    except ValueError: #VallueError 발생해도 종료
        break
    except EOFError: #EOF 발생하면 종료
        break