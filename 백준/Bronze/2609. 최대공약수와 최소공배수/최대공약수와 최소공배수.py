def gcd(x,y):
    while x%y != 0: #나머지가 0이면 무조건 최대공약수임(y가 더 크면 나머지 0 안 됨)
        oldx = x
        oldy = y    
        x = oldy
        y = oldx%oldy
    return y

def lcm(x,y): # 최소공배수는 두 수의 곱에다가 최대 공약수를 나누면 된다.
    return x*y//gcd(x,y)

a,b = map(int,input().split())
print(gcd(a,b))
print(lcm(a,b))