myset = set()
for i in range(10):
    myset.add(int(input())%42) # 나머지를 저장하는데 집합은 중복 안 되서 알아서 들어옴
# print(myset) # myset 확인용
print(len(myset))