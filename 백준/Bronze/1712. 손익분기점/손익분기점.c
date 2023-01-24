#include<stdio.h>
#include <math.h> 

int main()
// a+ma*b <= ma*c 가 되야 하므로 a <= ma*(c-b) 이며 a/(c-b) <= ma 임. 
{
    int a,b,c,d;
    int ma;
    double x;
    
    scanf("%d %d %d",&a,&b,&c);
    d = c-b;
    
    if(b>=c)
    {
        printf("-1");
    }

    else
    {
        x = (double)a/d; //간단한 방정식 계산 
        ma = floor(x)+1; //소숫점 내려주는 함수 사용 10->11, 10.1234->11
        //printf("%lf",x); 확인용
        printf("%d",ma);
    }

    return 0;
}

//아래 코드는 되기는 하는데 반복문이 21억번 돌고 하면서 시간 초과 됨 반복문 없이 해보기
/*
int main()
{
    long a,b,c;
    long ma=0;
    long cost,income;

    scanf("%d %d %d",&a,&b,&c);
    
    if(b>=c)
    {
        printf("-1");
    }

    else
    {
    while(1)
    {
        cost = a+ ma*b;
        income = ma*c;
        ma = ma+1;
        if(income >= cost)
        {
            break;
        }
    }
    printf("%d",ma);
    }

    
    
    return 0;
}
*/