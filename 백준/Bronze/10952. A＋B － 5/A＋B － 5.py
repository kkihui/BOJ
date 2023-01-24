import sys

while True:
  a,b = map(int,sys.stdin.readline().split()) #input보다 빠름
  if (a == b == 0):
    break
  else:
    print(a+b)
  