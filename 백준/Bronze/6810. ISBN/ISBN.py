nli = [9,7,8,0,9,2,1,4,1,8]
sum = 0
for _ in range(3):
  nli.append(int(input()))
for _ in range(13):
  sum += nli[_] * (_%2*2+1) # _가 홀수 일때는 3 짝수 일때는 1을 곱함
print ('The 1-3-sum is',sum)