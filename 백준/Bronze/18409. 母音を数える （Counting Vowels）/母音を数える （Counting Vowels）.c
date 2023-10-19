# include <stdio.h>

int main()
{
    int n,cnt=0;
    char word[51] = {0}, list[5] = {'a','e','i','o','u'};
    scanf("%d",&n);
    scanf("%s",word);
    
    for (n;n>=0;n--)
    {
        for(int i=0;i<5;i++)
        {
            if (word[n] == list[i]) cnt +=1;
        }
    }
    printf("%d",cnt);
    return 0;
}