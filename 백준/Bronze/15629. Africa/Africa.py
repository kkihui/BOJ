import sys

N = int(input())
dosi = [0]*N
money = {'botswana': 0,'south-africa':0,'ethiopia':50,'kenya':50,'tanzania':50,'zambia':50,'zimbabwe':30,'namibia':140}
sum = 0
for _ in range(N):
    dosi[_] = input()
    sum += money[dosi[_]]

if 'namibia' in dosi and 'south-africa' in dosi:
    if dosi.index('namibia') > dosi.index('south-africa'):
        sum -= 100
if 'zimbabwe' in dosi and 'zambia' in dosi:
    if abs(dosi.index('zimbabwe') - dosi.index('zambia')) == 1:
        sum -= 30
print(sum)