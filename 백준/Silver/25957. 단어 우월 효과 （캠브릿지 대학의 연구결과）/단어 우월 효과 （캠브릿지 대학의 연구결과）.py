import sys

def anagram(a,b):
    c = [0] * 26
    for _ in a:
        c[ord(_)-ord('a')] += 1
    for _ in b:
        c[ord(_)-ord('a')] -= 1
    if c == [0]*26:
        return True
    else:
        return False
  
N = int(sys.stdin.readline())
ansli = []
wordli = [[[] for i in range(26)] for _ in range(26)]

for _ in range(N):
    s = sys.stdin.readline().rstrip()
    if len(s)==1 or len(s)==2:
        pass
    else:
        init = ord(s[0])-ord('a')
        final = ord(s[-1])-ord('a')
        wordli[init][final].append(s[1:-1])

M = int(sys.stdin.readline())

camwli = list(map(str,sys.stdin.readline().split()))

for _ in camwli:
    if len(_) == 1 or len(_)==2:
        print(_,'',end='')
    else:
        for i in wordli[ord(_[0])-ord('a')][ord(_[-1])-ord('a')]:
            if anagram(i,_[1:-1]):
                word = _[0]+ i +_[-1]
                print(word,'',end='')
                break