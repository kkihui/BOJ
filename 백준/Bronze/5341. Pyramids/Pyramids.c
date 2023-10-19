# include <stdio.h>

int main()
{
    int num;
    while(1)
    {
        scanf("%d",&num);
        if (num == 0) break;
        else printf("%d\n",num*(num+1)/2);
    }
    return 0;
}