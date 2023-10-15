# include <stdio.h>

int gcd(int a,int b) // 유클리드 호제법 + 재귀 활용해서 최대공약수 찾기
{
    if (b==0) return a;
    else return gcd(b, a%b);
}

int lcm(int a,int b) // 최소공배수는 (두 수의 곱) / (최대공약수)
{
    return a*(b/gcd(a,b));
}

int main() 
{
    int T,M,N,x,y;
    int num,max,ans,zero_x,zero_y;
    
    scanf("%d",&T);

    for (int i=0;i<T;i++)
    {
        scanf("%d %d %d %d",&M,&N,&x,&y);
        max = lcm(M,N);
        ans = -1, zero_x=0, zero_y=0;
        if (x==M && y==N)
        {
            printf("%d\n",max);
            continue;
        }
        
        if (x==M) x=0;
        if (y==N) y=0;

        if (M <= N)
        {
            num = x;
            while (num <= max)
            {
                if (num % N == y)
                {
                    ans = num;
                    break;
                }
                num += M;
            }
        }
        else
        {
            num = y;
            while (num <= max)
            {
                if (num % M == x)
                {
                    ans = num;
                    break;
                }
                num += N;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}