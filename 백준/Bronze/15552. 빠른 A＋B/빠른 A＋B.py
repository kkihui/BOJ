import sys

t = int(input())
for i in range(t):
  a,b = map(int,sys.stdin.readline().split()) #input보다 빠름
  print(a+b)