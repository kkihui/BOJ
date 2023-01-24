import sys
sta = []
N = int(sys.stdin.readline())
for _ in range(N):
    order = sys.stdin.readline().rstrip()
    
    if order[:4] == 'push':
        sta.append(order[5:])
    
    if order == 'pop':
        if sta == []:
            print('-1')
        else:
            print(sta.pop())
    
    if order == 'size':
        print(len(sta))
    
    if order == 'empty':
        if sta == []:
            print('1')
        else:
            print('0')
    
    if order == 'top':
        if sta == []:
            print('-1')
        else:
            a = sta.pop()
            sta.append(a)
            print(a)