#include <iostream>

using namespace std;

const long long int p = 1000000007; // 10^9 + 7 은 소수

// Factorial mod p 계산 (모듈러 연산 결합 법칙 사용) -> (a*b) mod c = (a mod c) * (b mod c) mod c 
long long int Factorial(int num)
{
	long long int ret = 1;
	for (int i = 2; i <= num; i++)
	{
		ret = (ret % p) * (i % p) % p;
	}
	return ret;
}

// 거듭제곱의 분할정복 활용 + 모듈러 연산
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

	long long int half = Pow(base, exp / 2) % p;
	// 나머지가 있을 때
	if (exp % 2)
	{
		return half * half % p * base % p;
	}
	else
	{
		return half * half % p;
	}
}

// 이항계수 nCk = n! / k! (n-k)!이 됨.
// 페르마 소정리 a^p (mod p) = a (mod p) 활용 -> a^(p-2) (mod p) = 1/a (mod p)
// {n! / k! (n-k)!} (mod p) = [n! * {k! (n-k)! ^ (p-2)} (mod p)] (mod p)
int CalnCk(int n, int k)
{
	long long int numerator = Factorial(n);
	long long int denominator = (Factorial(k) % p) * (Factorial(n - k) % p) %p;
	long long int ret = numerator * (Pow(denominator, p - 2) % p) % p;

	return ret;
}

int main()
{
	int n, k;

	cin >> n >> k;

	cout << CalnCk(n,k) << endl;

	return 0;
}
