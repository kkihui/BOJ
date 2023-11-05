# include <stdio.h>

void combiPrint(int* combination,int len)
{
    printf("%d",combination[1]);
    for (int k=2; k<=len; k++) printf(" %d",combination[k]);
    printf("\n");
}

int main() 
{
    int N,M,i,ending=0;
    int combi[9]={0,};
    
    scanf("%d %d",&N,&M);
    
    for (i=1; i<=M; i++) combi[i] = i;
    int change = M;
    while (1)
    {
        if (ending) break; // 다 돌았으면 탈출
        combiPrint(combi,M);
        if (combi[change] == N-M+change) // change 번째 자리에 둘 수 있는 최대값은 N-M+change
        // ex) N=8 M=6 이면 5번째 자리 (change=5)에 둘 수 있는게 7이 최대임 (오름차순이라)
        {
            while (combi[change] == N-M+change)
            {
                change -= 1; // 만족하는 범위를 지나 최대한 앞으로 감.
                if (change == 0) // 끝났으면 탈출
                {
                    ending = 1;
                    break; 
                }
            }
            if (ending) break;
            
            combi[change] += 1;
            for (i=change+1; i<=M; i++) combi[i] = combi[change] + (i-change);
            change = M;
        }
        else combi[change] += 1;
    }

    return 0;
}