#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int n, sequence[100000], dp[100000];
	int max_num = -1000;
	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> sequence[i];

	dp[0] = sequence[0];
	max_num = max(max_num,dp[0]);

	for (int i = 1; i < n; i++)
	{
		dp[i] = sequence[i] + max(dp[i - 1], 0);
		max_num = max(max_num, dp[i]);
	}

	cout << max_num;

	return 0;
}