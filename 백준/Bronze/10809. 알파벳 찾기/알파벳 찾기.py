word = input()
wordlist = list(word)
anslist = []
for i in range(97,123): #a~z까지 반복
    for k in range(len(word)): #단어에서 찾기
        if (wordlist[k] == chr(i)): # k번째 글자가 i번째 알파벳과 같다면
            ans = k
            break
        else:
            ans = -1
    anslist.append(ans)
print(*anslist) # *을 붙혀서 괄호랑 쉼표 없이 리스트 출력