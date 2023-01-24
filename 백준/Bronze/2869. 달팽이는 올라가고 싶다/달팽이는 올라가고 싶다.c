#include<stdio.h>
#include <math.h> 

int main()
// (a-b)*day+a >= v 가 되야 하므로 day >= (v-a)/(a-b) 임. 
{
    int a,b,v;
    int k,i;
    int day;
    double x;
    
    scanf("%d %d %d",&a,&b,&v);
    
    k=v-a;
    i=a-b;

    x = (double)k/i; //간단한 방정식 계산 
    day = ceil(x)+1; //소숫점 올려주는 함수 사용 10->11, 10.1234->12
    
    // printf("%lf \n",x); //확인용
    printf("%d",day);


    return 0;
}