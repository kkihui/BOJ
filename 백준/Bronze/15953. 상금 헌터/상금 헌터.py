import sys

T = int(input())
for i in range(T):
    A,B = map(int,sys.stdin.readline().split())
    if (A==0): # A의 등수 판별하여 상금 결정
        cashA = 0
    elif (A==1): 
        cashA = 5000000
    elif (A <= 3):
        cashA = 3000000
    elif (A <= 6):
        cashA = 2000000
    elif (A <= 10):
        cashA = 500000
    elif (A <= 15):
        cashA = 300000
    elif (A <= 21):
        cashA = 100000
    else:
        cashA = 0
    
    if (B==0): # B의 등수 판별하여 상금 결정
        cashB=0
    elif (B==1): 
        cashB = 5120000
    elif (B <= 3):
        cashB = 2560000
    elif (B <= 7):
        cashB = 1280000
    elif (B <= 15):
        cashB = 640000
    elif (B <= 31):
        cashB = 320000
    else:
        cashB = 0
    
    print(cashA+cashB)