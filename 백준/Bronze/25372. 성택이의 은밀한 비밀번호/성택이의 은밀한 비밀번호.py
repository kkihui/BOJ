n = int(input())
for _ in range(n):
    m = input()
    if len(m) >= 6 and len(m) <= 9:
        print('yes')
    else:
        print('no')