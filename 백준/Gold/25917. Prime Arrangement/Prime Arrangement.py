import sys
import math

R,C = map(int,sys.stdin.readline().split())
Ali = list(map(int,sys.stdin.readline().split()))
Pli = list(map(int,sys.stdin.readline().split()))
case = math.factorial(R*C)//math.factorial(R) # R*C!은 배열을 채우는 모든 경우,  R!을 나눠줘야 가중치 순서를 만족하는 경우

print(case%998244353)