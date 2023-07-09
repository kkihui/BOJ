import sys

equ = sys.stdin.readline().rstrip()
li = list(equ)
num = 0
baseli = []
afterplus = []
res = 0

for _ in range(len(li)): #숫자와 +,- 기호로 분리해서 리스트 만들기 
    if li[_] == '+' or li[_]=='-':
        baseli.append(num)
        baseli.append(li[_])
        num=0
    else:
        if _ == len(li)-1:
            num = num*10+int(li[_])
            baseli.append(num)
        else:
            num = num*10+int(li[_])

for _ in range(len(baseli)): # + 있으면 먼저 계산
    if baseli[_] == '+':
        sum = afterplus[-1]+baseli[_+1]
        afterplus.pop()
        afterplus.append(sum)
    elif baseli[_-1] == '+':
        pass
    else:
        afterplus.append(baseli[_])
  
for _ in range(len(afterplus)):
    if afterplus[_] == '-':
        res -= afterplus[_+1]
    elif afterplus[_-1] == '-':
        pass
    else:
        res += afterplus[_]

print(res)