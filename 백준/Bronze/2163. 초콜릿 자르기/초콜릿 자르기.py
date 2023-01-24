def cut(a,b):
    s = 0
    while a != 1 or b != 1: # 둘다 1이어야 끝나야함
        if a >= b:
            if a%2==0: # 짝수면 깔끔하게 반 쪼개짐
                # print('짝수에서 원래 a값은',a) # 아래의 print들은 다 확인용
                s+=1
                # print('짝수를 한 번 쪼개서 더해진 s값',s)
                a = a//2
                # print('짝수에서 바뀐 a값은',a)
                s+=cut(a,b)+cut(a,b)
                # print('짝수를 쪼갠 조각에서 더해진 s값',s)
                break # 남은 애가 다시 돌지 않도록 멈춰줌
            else: # 홀수면 a=2k+1일때 k,k+1로 쪼개짐
                # print('홀수에서 원래 a값은',a)
                s+=1
                # print('홀수를 한 번 쪼개서 더해진 s값',s)
                a = a//2
                # print('홀수에서 바뀐 a값은',a)
                s+=cut(a,b)+cut(a+1,b)
                # print('홀수를 한 번 쪼개서 더해진 s값',s)
                break
        else: # a가 더 작으면 a랑 b랑 바꿔줌
            olda = a
            oldb = b
            a = oldb
            b = olda
    return s
            

N,M = map(int,input().split())
print(cut(N,M))