/* 뤼카 정리 활용 */
// nCk (mod m)을 구하기 위해 n과 k를 m 진수로 나타냄.
// n = n_q * m^q + .... n_1 * m + n_0 * m^0 (0 <= n_i < m)
// k = k_q * m^q + .... k_1 * m + k_0 * m^0 (0 <= k_i < m)
// 이때, nCk (mod m) = n_0 C k_0 (mod m) * n_1 C k_1 (mod m) *... * n_q C k_q (mod m)이 된다.
#include <iostream>

using namespace std;

long long n, k, m;

// Factorial mod p 계산 (모듈러 연산 결합 법칙 사용) -> (a*b) mod c = (a mod c) * (b mod c) mod c 
long long Factorial(long long num)
{
	long long ret = 1;
	for (int i = 2; i <= num; i++)
	{
		ret = (ret % m) * (i % m) % m;
	}
	return ret % m;
}

// 거듭제곱의 분할정복 활용 + 모듈러 연산
long long Pow(long long base, long long exp)
{
	base %= m;
	if (exp == 0)
	{
		return 1;
	}
	else if (exp == 1)
	{
		return base;
	}

	long long half = Pow(base, exp / 2);
	// 나머지가 있을 때
	if (exp % 2)
	{
		return half * half % m * base % m;
	}
	else
	{
		return half * half % m;
	}
}

// 이항계수 nCk = n! / k! (n-k)!이 됨.
// 페르마 소정리 a^m (mod m) = a (mod m) 활용 -> a^(m-2) (mod m) = 1/a (mod m)
// {n! / k! (n-k)!} (mod m) = [n! * {k! (n-k)! ^ (m-2)} (mod m)] (mod m)
long long CalnCk(long long n, long long k)
{	
	if (n == k || k == 0)
	{
		return 1;
	}
	else if (k > n)
	{
		return 0;
	}

	long long numerator = Factorial(n);
	long long denominator = Factorial(k) * Factorial(n - k) % m;
	long long ret = numerator * Pow(denominator, m - 2) % m;

	return ret;
}

int main()
{
	cin >> n >> k >> m;

	// 1C1, 2C1, 2C2, ....mCm은 페르마 소정리로 구하기
	// nCk -> 뤼카 정리 -> 페르마 소정리
	long long ans = 1;
	while (n || k)
	{
		long long n_q = n % m;
		long long k_q = k % m;

		ans = ans * CalnCk(n_q, k_q) % m;
		n /= m;
		k /= m;
	}

	cout << ans << endl;

	return 0;
}