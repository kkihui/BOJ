a = input()
if a[0]== 'A':
    ans = 4.0
elif a[0]== 'B':
    ans = 3.0
elif a[0]== 'C':
    ans = 2.0
elif a[0]== 'D':
    ans = 1.0
elif a[0]== 'F':
    ans = 0.0
    a ='F0'

if a[1] == '+':
    ans += 0.3
elif a[1] == '-':
    ans -= 0.3

print(ans)