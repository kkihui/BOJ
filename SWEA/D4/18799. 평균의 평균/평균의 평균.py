def refine(num):
    s = str(num)
    decimal = []
    
    for i in range(len(s)):
        if s[i] == '.':
            point = i
            break
    
    for j in range(point+1,len(s)):
        decimal.append(s[j])
    
    if len(decimal) == 1:
        if decimal[0] == '0':
            return s[:i]
    return s

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    num_li = list(map(int,input().split()))
    avg = sum(num_li) / n
    avg = refine(avg)
    
    print(f'#{t} {avg}')