a,b,c = map(int,input().split())
if b<c:
    print('Bus')
elif b==c:
    if a <= c:
        print('Anything')
    else:
        print('Bus')
else:
    if a<=c:
        print('Subway')
    else:
        print('Bus')
    
    