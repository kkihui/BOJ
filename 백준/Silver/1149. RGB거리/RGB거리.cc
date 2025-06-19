#include <iostream>

using namespace std;

int Min(int a, int b)
{
	if (a < b)
		return a;
	return b;
}

int main()
{
	int n, rgb_info[1000][3], dp[1000][3];
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < 3; j++)
			cin >> rgb_info[i][j];
	}

	dp[0][0] = rgb_info[0][0];
	dp[0][1] = rgb_info[0][1];
	dp[0][2] = rgb_info[0][2];

	for (int i = 1; i < n; i++)
	{
		dp[i][0] = Min(dp[i - 1][1], dp[i - 1][2]) + rgb_info[i][0];
		dp[i][1] = Min(dp[i - 1][0], dp[i - 1][2]) + rgb_info[i][1];
		dp[i][2] = Min(dp[i - 1][0], dp[i - 1][1]) + rgb_info[i][2];
	}

	cout << Min(Min(dp[n - 1][0], dp[n - 1][1]), dp[n - 1][2]);

	return 0;
}