def solution(array, commands):
    answer = []
    for i,j,k in commands:
        arr = array[i-1:j]
        arr.sort()
        num = arr[k-1]
        answer.append(num)
    return answer