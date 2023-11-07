# include <stdio.h>

void combiPrint(int* combination,int* candiarr,int len)
{
    printf("%d",candiarr[combination[1]]);
    for (int k=2; k<=len; k++) printf(" %d",candiarr[combination[k]]);
    printf("\n");
}

void bubleSort(int* arr,int len)
{
    int temp;
    for (int i=1;i<=len;i++)
    {
        for (int j=1;j<len;j++)
        {
            if(arr[j] > arr[j+1])
            {
                temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() 
{
    int N,M,i,ending=0;
    int combi[9]={0,} , candinate[9]={0,};
    
    scanf("%d %d",&N,&M);
    for (i=1; i<=N; i++) scanf("%d",&candinate[i]);
    bubleSort(candinate,N);
    
    for (i=1; i<=M; i++) combi[i] = 1; // 초기 값
    int change = M;
    while (1)
    {
        if (ending) break; // 다 돌았으면 탈출
        combiPrint(combi,candinate,M);
        if (combi[change] == N) // change 번째 자리에 둘 수 있는 최대값은 N
        {
            while (combi[change] == N)
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
            for (i=change+1; i<=M; i++) combi[i] = combi[change];
            change = M;
        }
        else combi[change] += 1;
    }
    return 0;
}