from ast import Try
import sys

n = int(sys.stdin.readline())
nli = list(range(n,0,-1))
seq = [int(sys.stdin.readline()) for _ in range(n)]
stack,plmili = [],[]
try:
    for _ in seq:
        while True:
            if stack == []:
                stack.append(nli.pop())
                plmili.append('+')
            elif stack[len(stack)-1] == _:
                stack.pop()
                plmili.append('-')
                break
            else:
                stack.append(nli.pop())
                plmili.append('+')

    for _ in plmili:
        print(_)

except IndexError: # 불가능하면 error 발생
    print("NO")