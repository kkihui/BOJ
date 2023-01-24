A = int(input())
B = int(input()) # 3자리수 2개 입력 받음
print(A*(B%10)) # A* B의 일의 자리수 
print(A*((B//10)%10)) # A* B의 10의 자리수
print(A*(B//100)) # A* B의 100의 자리수
print(A*B)