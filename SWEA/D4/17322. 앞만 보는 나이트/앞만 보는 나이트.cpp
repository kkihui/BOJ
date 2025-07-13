#include <iostream>

using namespace std;

const long long int p = 1000000007; // 10^9 + 7

// 모듈러 적용한 Factorial ( a*b (mod p) = {a (mod p) * b (mod p)} (mod p) )
long long int Factorial(long long int num)
{
	long long int ret = 1;
	for (long long int i = 1; i < num; i++)
	{
		ret = ret * (i + 1) % p;
	}

	return ret % p;
}

// 모듈러 적용한 거듭제곱 분할정복 
long long int Pow(long long int base, long long int exp)
{
	base %= p;
	if (exp == 0)
	{
		return 1;
	}
	else if (exp == 1)
	{
		return base % p;
	}

	if (exp % 2)
	{
		return (base * Pow(base,exp - 1)) % p;
	}
	else
	{
		long long int half = Pow(base, exp / 2) % p; // base^(exp/2) (mod p)
		return (half * half) % p;
	}
}

// 이항정리 (조합) (n! / r!(n-r)!)
// 페르마 소정리: a^p (mod p) = a (mod p) -> 양변 a^2 나누면,  a^(p-2) (mod p) = 1/a (mod p)
// 이항계수의 mod 연산 nCr % p = n! * {(n-r)! * r!)}^-1 % p = n! * {(n-r)! * r!}^(p-2) % p
long long int CalnCr(long long int n, long long int r)
{

	long long int numerator = Factorial(n);
	long long int denominator = Factorial(r) * Factorial(n - r) % p;
	long long int ret = (numerator * Pow(denominator, p - 2)) % p;

	return ret;
}

bool Inrange(long long int n, long long int r)
{
	return 0 <= r && r <= n;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		long long int x, y;
		cin >> x >> y;

		// 파스칼 삼각형 모양 
		long long int ans = 0;
		if ((x + y) % 3 == 0)
		{
			long long int n = (x + y) / 3; // 파스칼 삼각형의 깊이 (0부터 시작)
			long long int r = x - n; // 거기서 몇 번째에 해당하는가 (0부터 시작)

			if (Inrange(n, r))
			{
				ans = CalnCr(n, r);
			}
		}

		cout << '#' << test_case << ' ' << ans << endl;
	}
	return 0;
}