n = int(input())
num_li = []
for _ in range(n):
    num_li.append(float(input()))
ans = str(sorted(num_li)[1])
dollar,cent = ans.split('.')

if len(cent) == 1:
    ans += '0'

print(ans)