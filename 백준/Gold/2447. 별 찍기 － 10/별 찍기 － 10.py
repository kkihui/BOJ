import sys
def draw(li,n):
    if n==3:
        li[1][1] = 0
        return li
    a=n//3
    for _ in li[a:2*a]:
        _[a:2*a]=[0]*a
    tri1 = li[0:a]
    tri2 = li[a:2*a]
    tri3 = li[2*a:3*a]
    n1,n2,n3,n4,n5,n6,n7,n8 = [],[],[],[],[],[],[],[]
    for _ in tri1:
        n1.append(_[0:a])
        n2.append(_[a:2*a])
        n3.append(_[2*a:3*a])
    for _ in tri2:
        n4.append(_[0:a])
        n5.append(_[2*a:3*a])
    for _ in tri3:
        n6.append(_[0:a])
        n7.append(_[a:2*a])
        n8.append(_[2*a:3*a])    
    n1 = draw(n1,a)
    n2 = draw(n2,a)
    n3 = draw(n3,a)
    n4 = draw(n4,a)
    n5 = draw(n5,a)
    n6 = draw(n6,a)
    n7 = draw(n7,a)
    n8 = draw(n8,a)
    
    for _ in range(a):
        tri1[_] = n1[_]+n2[_]+n3[_]
        tri2[_] = n4[_]+[0]*a+n5[_]
        tri3[_] = n6[_]+n7[_]+n8[_]
    li = tri1 + tri2 + tri3
    return li

N = int(sys.stdin.readline())
nli = [['*']*N for _ in range(N)]
for _ in draw(nli,N):
    for i in _:
        if i == '*':
            sys.stdout.write('*')
        else:
            sys.stdout.write(' ')
    print('')