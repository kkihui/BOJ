# include <stdio.h>

int main() 
{
    int N,cnt;
    int li[11] = {0};
    int ans[11] = {0};
    
    scanf("%d",&N);

    for (int i=0;i<N;i++) scanf("%d",&li[i]);
    for (int i=0;i<N;i++)
    {
        cnt = 0;
        for (int j=0;j<N;j++)
        {
            if (cnt == li[i] && ans[j] == 0)
            {
                ans[j] = i+1;
                break;
            }
            if (ans[j] == 0) cnt += 1;
        }
    }
    for (int i=0;i<N;i++) printf("%d ",ans[i]);
    return 0;
}