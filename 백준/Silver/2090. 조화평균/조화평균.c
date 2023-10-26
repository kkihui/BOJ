# include <stdio.h>

int main() 
{
    int n,i,num[9] = {0},conti;
    long long numerator=0,denominator=1;
    scanf("%d",&n);
    for (i=0;i<n;i++)
    {
        scanf("%d",&num[i]);
        denominator *= num[i];
    }
    for (i=0;i<n;i++) numerator += denominator/num[i];

    while (1)
    {
        conti = 0;
        for (i=2;i<100;i++)
        {
            if ((denominator%i == 0) && (numerator%i ==0))
            {
                denominator /= i;
                numerator /= i;
                conti = 1;
                break;
            }
        }
        if (conti == 0) break;
    }
    printf("%lld/%lld",denominator,numerator);

    return 0;
}