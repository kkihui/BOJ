#include<stdio.h>

int gcd(int a, int b) // 유클리드 호제법 + 재귀 활용해서 최대공약수 찾기
{
    if (b==0) return a;
    else return gcd(b, a%b);
}

long long lcm(int a, int b) // 최소공배수는 (두 수의 곱) / (최대공약수)
{
    long long c = (long long)a*((long long)b/(long long)gcd(a,b));
    return c; // a*b먼저 계산하면 overflow 발생
}

int main()
{
    int Great,Least,i,min,num1,num2,cnt=0;
    int Opt[800]={0}, ans[2]={0}; // 1억 이하에서 약수 제일 많은게 768개임.
    scanf("%d %d",&Great,&Least);
    i = Great;
    min = 2*Least;

    if (Great == Least)
    {
        printf("%d %d",Great,Least);
        return 0;
    }

    while (i<=Least) // 최대공약수의 배수이면서 최소공배수의 약수인 수의 목록 만들기
    {
        if (Least % i == 0)
        {
            Opt[cnt] = i;
            // printf("%d\n",Opt[cnt]);
            cnt += 1;
        }
        i += Great;
    }

    for (i=0; i<cnt; i++) 
    {
        num1 = Opt[i];
        for (int j=i+1; j<cnt; j++) // Opt는 크기가 800보다 작으므로 O(n^2)으로 연산해도 괜찮음.
        {
            num2 = Opt[j];
            // printf("%d %d %d %llu\n",num1,num2,gcd(num1,num2),(long long)lcm(num1,num2));

            if (gcd(num1,num2) == Great && lcm(num1,num2) == Least) // Opt의 두 수가 최대공약수랑 최소공배수 일치
            {
                if (num1+num2 < min) // 여러개 쌍 중에서 최소인 것만 갱신하면서 저장
                {
                    ans[0] = num1;
                    ans[1] = num2;
                    min = num1 + num2;
                }
            }
        }
    }
    
    printf("%d %d",ans[0],ans[1]);

    return 0;
}