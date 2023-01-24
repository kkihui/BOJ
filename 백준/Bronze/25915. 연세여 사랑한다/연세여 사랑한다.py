s = input()
if ord(s) >= ord('I'):
    f = ord(s) - ord('I')
else:
    f = ord('I') - ord(s)
print(f+84) # 시작만 이동하면 나머지는 다 같음