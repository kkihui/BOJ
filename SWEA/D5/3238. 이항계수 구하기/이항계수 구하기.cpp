/* 뤼카 정리 활용 */
// nCk (mod p)를 구하기 위해 n과 k를 p 진수로 나타냄.
// n = n_q * p^q + .... n_1 * p + n_0 * p^0 (0 <= n_i < p)
// k = k_q * p^q + .... k_1 * p + k_0 * p^0 (0 <= k_i < p)
// 이때, nCk (mod p) = n_0 C k_0 (mod p) * n_1 C k_1 (mod p) *... * n_q C k_q (mod p)가 된다.

#include <iostream>

using namespace std;

long long int n, r, p;

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
		return (base * Pow(base, exp - 1)) % p;
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
	if (n == r || r == 0)
	{
		return 1;
	}
	else if (r == 1)
	{
		return n % p;
	}
	else if (r > n)
	{
		return 0;
	}

	long long int numerator = Factorial(n);
	long long int denominator = Factorial(r) * Factorial(n - r) % p;
	long long int ret = (numerator * Pow(denominator, p - 2)) % p;

	return ret;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> n >> r >> p;
		
		// 1C1, 2C1, 2C2, ....pCp는 페르마 소정리로 구하기
		// nCr -> 뤼카 정리 -> 페르마 소정리
		long long int ans = 1;
		while (n || r)
		{
			long long int n_q = n % p;
			long long int r_q = r % p;

			ans = ans * CalnCr(n_q, r_q) %p;
			n /= p;
			r /= p;
		}
		
		cout << '#' << test_case << ' ' << ans << endl;
	}

	return 0;
}