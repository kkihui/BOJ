year = int(input())
if(year%4 == 0): # 4의 배수일 경우
  if(year%100 == 0): # 100의 배수일 경우
    if(year%400 == 0): # 400의 배수일 경우
      print(1)
    else: # 400의 배수가 아닌 100의 배수일 경우
      print(0)
  else: #100의 배수가 아닌 4의 배수일 경우
    print(1)
else: # 4의 배수가 아닐 경우
  print(0)