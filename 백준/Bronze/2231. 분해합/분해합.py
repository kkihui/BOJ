n = int(input())
for _ in range(1,n+1):
    k,i = _,_
    while i != 0:
        k += i%10
        i = i//10
    if k == n:
        print(_)
        break
    elif _ == n:
        print(0)