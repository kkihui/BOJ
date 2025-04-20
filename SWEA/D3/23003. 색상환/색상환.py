T = int(input())
color = {'red':1, 'purple':2,'blue':3, 'green':4,'yellow':5, 'orange':6}
 
for _ in range(T):
    s1,s2 = map(str,input().split())
    c1,c2 = color[s1],color[s2]
     
    if c1 == c2:
        print('E')
    elif abs(c1-c2) == 1 or abs(c1-c2) == 5:
        print('A')
    elif abs(c1-c2) == 3:
        print('C')
    else:
        print('X')