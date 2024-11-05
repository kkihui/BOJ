n = list(map(int,input().split()))
n.sort()
if n[0] == n[1] == n[2]:
    print(2)
elif n[0]**2+n[1]**2 == n[2]**2:
    print(1)
else:
    print(0)