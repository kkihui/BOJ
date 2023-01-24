import statistics #list 평균 구하는 함수인 stastics.mean 이용 위해서 import

N = int(input())
score_list = list(map(int,input().split()))
score_list.sort()

# print(score_list) # 처음에 받은 점수
for i in range(N): # score_list[0]~score_list[N-1] 까지 반복함.
    score_list[i] = score_list[i]/score_list[N-1]*100 # 작은 것 부터 점수 고쳐나가기 N-1이 제일 큰 점수
# print(score_list) # 고친 점수
mean = statistics.mean(score_list) # score_list의 평균 구함
print(mean) #새로 나온 평균