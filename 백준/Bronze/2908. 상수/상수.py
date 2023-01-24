a,b = (input().split())#공백으로 나눠 받아 리스트에 저장
ali = list(a)
bli = list(b)
ali.reverse() # 뒤집어주기
bli.reverse()
a = ''.join(ali) #list를 다시 문자열로
b = ''.join(bli)
if a>b :
    print(a)
else:
    print(b)