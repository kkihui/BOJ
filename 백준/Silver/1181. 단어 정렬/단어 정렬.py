import sys
N= int(sys.stdin.readline().rstrip())
wordli,newli,ali,bli = [],[],[],[]

for _ in range(N): # 중복되는거 빼고 단어 받기
    word = sys.stdin.readline().rstrip()
    if word in wordli:
        pass
    else:
        wordli.append(word)

for _ in wordli: # 글자수 붙히고 정렬해서 글자수 및 알파벳 순서대로 나오게 함
    newli.append(str(len(_))+_)

for _ in newli: #10글자가 넘어가는거랑 아닌거 따로 정렬해서 합침
    if (len(_)) > 10 :
        ali.append(_)
    else:
        bli.append(_)   

ali.sort()
bli.sort()
newli = bli+ali

for _ in range(len(newli)): # 슬라이싱으로 숫자 지우고 하나씩 출력 (10보다 크면 넘어가면 2개 잘라야함)
    if len(newli[_]) < 11:
        newli[_] = newli[_][1:]
        print(newli[_])    
    else:
        newli[_] = newli[_][2:]
        print(newli[_])