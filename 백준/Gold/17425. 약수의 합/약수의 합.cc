#include <iostream>

using namespace std;

const long long kMaxSize = 1e+6 + 1;

long long g[kMaxSize] = { 0, };

int main()
{
	// 1 ~ 100만의 배수 다 더해주기 (f(A) 계산)
	for (long long i = 1; i < kMaxSize; i++)
	{
		long long num = i;
		while (num < kMaxSize)
		{
			g[num] += i;
			num += i;
		}
	}

	// 1 ~ 100만까지 f(a) 더해주기 (g(X)) 계산)
	for (long long i = 2; i < kMaxSize; i++)
	{
		g[i] += g[i - 1];
	}

	// 입출력 속도 높이기
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// 입력 받아서 출력
	int t;
	cin >> t;

	while (t--)
	{
		int n;
		cin >> n;

		cout << g[n] << '\n';
	}

	return 0;
}