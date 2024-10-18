import sys

word_list = []

for _ in range(5):
    word = list(sys.stdin.readline().rstrip())
    word_list.append(word)

for i in range(16):
    for j in range(5):
        if i < len(word_list[j]):
            print(word_list[j][i],end='')