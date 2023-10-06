#include<stdio.h>

int main()
{
    int Fibonacci[20] = {0}, num=0, n;
    Fibonacci[0] = 1;

    for (int i=1;i<20;i++)
    {
        Fibonacci[i] = Fibonacci[i-1]+num;
        num = Fibonacci[i-1];
    }
    
    scanf("%d",&n);
    printf("%d",Fibonacci[n-1]);

    return 0;
}
