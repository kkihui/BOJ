#include<stdio.h>
// 5로 나눈 나머지를 통해서 계산

int main() 
{
    int ea;
    int n;
    
    scanf("%d",&n);
    
    
    if(n%5==0)
    {
        ea=n/5;
        printf("%d",ea);
    }

    else if (n%5==1)
    {
        ea=(n/5)+1; // 나머지가 1이면 5kg 하나 빼고 3kg 2개 넣으면 됨
        printf("%d",ea); 
    }

    else if (n%5==2)
    {
        if(n==7)
        {
            printf("-1"); //다른 거는 ㄱㅊ 한데 7은 계산 안 됨
        }
        else
        {
            ea=(n/5)+2; // 나머지가 2이면 5kg 2개 빼고 3kg 4개 넣으면 됨
            printf("%d",ea);
        }
        
    }

    else if (n%5==3)
    {
        ea=(n/5)+1; // 나머지가 3이면 5kg로 채우고 3kg 1개 넣으면 됨
        printf("%d",ea);
    }

    else if (n%5==4)
    {
        if(n==4)
        {
            printf("-1"); //다른 거는 ㄱㅊ 한데 4는 계산 안 됨
        }
        else
        {
            ea=(n/5)+2; // 나머지가 4이면 5kg 1개 뺴고 3kg 3개 넣으면 됨
            printf("%d",ea);
        }
    }

    return 0;
}