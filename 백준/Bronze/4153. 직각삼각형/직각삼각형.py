import sys
end = False
while end != True:
    ali = list(map(int,sys.stdin.readline().split()))
    
    if ali[0] == ali[1] == ali[2] == 0:
        end = True
        break
    ali.sort()
    
    if ali[2]**2 == ali[1]**2 + ali[0]**2:
        print('right')
    else:
        print('wrong')