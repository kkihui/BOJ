def solve(a): #리스트를 받아서 합을 return하는 함수 solve() 정의
    ans = 0
    for i in range(len(a)):
         ans += a[i]
    return ans

'''
함수 구현만 하면 됨.
mylist = list(map(int,input().split()))
print(mylist)
print(solve(mylist))
'''