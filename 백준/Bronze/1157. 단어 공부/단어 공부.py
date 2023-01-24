W = input()
W = W.upper() # 대문자로 수정
Wlist = list(W)
anslist = [0]*92
for i in range(len(W)):
    for k in range(65,91):
        if Wlist[i] == chr(k): # Wlist의 글자가 그 알파벳과 같다면 anslist에서 그 index에 해당하는 숫자를 올림
            anslist[k] += 1
if anslist.count(max(anslist)) == 1: #제일 많이 나온 숫자가 1개이면
    print(chr(anslist.index(max(anslist)))) # 제일 많이 나온 숫자의 index를 아스키 코드로 변환
else: # 제일 많이 나온 숫자가 1개가 아니면
    print('?')