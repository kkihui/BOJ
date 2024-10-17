#include<stdio.h>

int main()
{
    char str[5];
    scanf("%s",str);
    for (int i=2 ; i>=0 ; --i)
    {
        printf("%c",str[i]);
    }
    
    return 0;
}