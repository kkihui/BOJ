import copy
import numbers #deep copy를 위해 import
def d(N): # d(N)이라는 함수 정의
    answer = copy.deepcopy(N) # N 값을 복사
    
    while(N>0): # N의 일의 자리 부터 떼서 각 자리수를 다 answer에 더해줌
        answer+=(N%10)
        N=N//10
    
    return answer # answer에 d(N) 연산 값 저장됨
 
s1=set(range(1,10001)) #1부터 10,000까지 s1이라는 set로 만듦
s2=set() # 1부터 10,000까지 d(N) 연산한 것을 s2라는 set로 만듦
for i in range(1,100001):
   s2.add(d(i))
   
prlist = list(s1-s2) # s1과 s2의 차집합을 list로 만듦 (생성자가 있는 숫자를 다 뺐으므로 셀프넘버만 남는다.)
prlist.sort() #set로 연산했기 때문에 뒤죽박죽이라 정렬해줌

for i in prlist: #최종적으로 정렬된 self number 출력
    print(i)