# include <stdio.h>
# include <string.h>

int main() 
{
    int N,cmp,cmp2,idx,max=0;
    int cnt[1000]={0};
    char book[1000][51], best[1000][51];
    
    scanf("%d",&N);

    for (int i=0;i<N;i++) scanf("%s",book[i]);
    for (int i=0;i<N;i++)
    {
        for (int j=0;j<N;j++)
        {
            cmp = strcmp(book[i],best[j]);
            if (cmp == 0)
            {
                cnt[j] += 1;
                break;
            }


            cmp2 = strcmp(best[j],"");
            if (best[j][0] == '\0')
            {
                strcpy(best[j],book[i]);
                cnt[j] += 1;
                break;
            }
        }
    }

    for (int i=0;i<N;i++)
    {
        if (cnt[i] > max)
        {
            max = cnt[i];
            idx = i;
        }

        if (cnt[i] == max && max != 0)if (strcmp(best[i],best[idx]) < 0) idx = i; // 같은 빈도면 사전 순으로 제일 앞서는 것
    }
    printf("%s",best[idx]);
    return 0;
}