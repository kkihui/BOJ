# x,y 범위가 10억인데 3^19이면 10억정도고 3^20이면 30억임.3^20이 더해지고 빼지는 순간 무조건 범위 넘어가니 3^19까지 +-로 계산 가능한지 확인하면 됨.
# 모든 숫자는 3의 제곱들의 합과 차로 표현 가능. 숫자를 분해 해서 순서 찾기.
# 1을 한 번 쓰니까 둘 중 하나는 3의 배수 아니고 둘 중 하나는 3의 배수여야 함.

# 제곱수 리스트 만들기
square3 = []
for i in range(20):
    square3.append(3 ** i)


# 3의 제곱수로 분해
def Decompose3(num):
    li = [0] * 20

    while num != 0:
        for i in range(20):
            if abs(num) < square3[i]:
                if abs(num) <= sum(square3[:i]) and not li[i-1]:
                    li[i - 1] = 1
                    if num < 0:
                        num += square3[i - 1]
                    else:
                        num -= square3[i - 1]
                elif abs(num) > sum(square3[:i]) and not li[i]:
                    li[i] = 1
                    if num < 0:
                        num += square3[i]
                    else:
                        num -= square3[i]
                break
            elif abs(num) == square3[i] and not li[i]:
                li[i] = 1
                num = 0
                break
            elif li[i] == 1:
                break

    return li


T = int(input())

for t in range(1, T + 1):
    x, y = map(int, input().split())
    x_li = Decompose3(x)
    y_li = Decompose3(y)
    conti = 1
    state = 'yes'
    
    for i in range(20):
        total = x_li[i] + y_li[i]
        if total > 1:
            state = 'no'
            break
        elif total == 1:
            if not conti:
                state = 'no'
                break
        else:
            conti = 0

    print(f'#{t} {state}')