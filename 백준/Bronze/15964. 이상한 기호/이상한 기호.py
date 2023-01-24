def gol(n,k):
    ans = (n+k)*(n-k)
    return ans
a,b = map(int,input().split())
print(gol(a,b))