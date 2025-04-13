T = int(input())

for _ in range(T):
    heights = list(map(int,input().split()))
    h_max = max(heights)
    h_sum = sum(heights)
    
    for i in range(1,8):
        if (h_max+i+h_sum) % 7 == 0: print(h_max+i)