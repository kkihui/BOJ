import sys
wordli = []

while True: # 단어 목록 (글자 개수로 list화)
    letterli = [0]*26
    s = list(sys.stdin.readline().rstrip())
    if s == ['-']:
        break
    for _ in s:
        letterli[ord(_)-ord('A')] += 1
    wordli.append(letterli)
    
while True: # 퍼즐판 받아서 결과 출력
    pli = [0]*26
    useli = []
    alphali = [0]*26
    pdict = {}
    ansli = []
    
    p = list(sys.stdin.readline().rstrip())
    if p == ['#']:
        break
    
    for _ in p:
        pli[ord(_)-ord('A')] += 1
    
    for _ in wordli: # 만들 수 있는 단어 목록 제작
        use = True
        for x,y in zip(pli,_):
            if x < y:
                use = False
                break
        if use:
            useli.append(_)
    
    for _ in useli: # 만들 수 있는 단어에서 알파벳 사용 횟수 출력
        for i in range(26):
            if _[i]:
                alphali[i] += 1
    
    for _ in p:
        pdict[_] = alphali[ord(_)-ord('A')]
    pdict = dict(sorted(pdict.items()))
    
    n = min(pdict.values())
    x = max(pdict.values())
    
    for _ in pdict:
        if pdict[_] == n:
            ansli.append(_)
    ansli.append(str(n))
    for _ in pdict:
        if pdict[_] == x:
            ansli.append(_)
    ansli.append(str(x))
    
    for _ in ansli: # 결과 출력
        if _.isdigit():
            print('',_,'',end='')
        else:
            print(_,end='')
    print()