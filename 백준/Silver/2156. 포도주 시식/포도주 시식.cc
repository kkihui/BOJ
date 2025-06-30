#include <iostream>
#include <algorithm>

using namespace std;

class Dp
{
public:
	int value; // 해당 idx의 값
	int conti_none_max; // 현재 idx를 안 먹었을 때의 최대값
	int conti_one_max; // 2칸 이전의 idx와 현재 idx를 먹었을 때의 최대값
	int conti_two_max; // 직전 idx와 현재 idx를 먹었을 때의 최대값

	Dp(int value = -1)
	{
		this->value = value;
		conti_none_max = value;
		conti_one_max = value;
		conti_two_max = value;
	}
};

Dp dp[10000];

int main()
{
	int n;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		int num;
		cin >> num;
		dp[i].value = num;
	}

	for (int idx = 0; idx < n; idx++)
	{
		if (idx == 0)
		{
			dp[idx].conti_one_max = dp[idx].value;
		}
		else if (idx == 1)
		{
			dp[idx].conti_none_max = dp[idx-1].value;
			dp[idx].conti_one_max = dp[idx].value;
			dp[idx].conti_two_max = dp[idx].value + dp[idx - 1].value;
		}
		else
		{
			dp[idx].conti_none_max = max(dp[idx - 1].conti_none_max, max(dp[idx - 1].conti_one_max, dp[idx - 1].conti_two_max));
			dp[idx].conti_one_max = dp[idx].value + max(dp[idx - 2].conti_none_max, max(dp[idx - 2].conti_one_max, dp[idx - 2].conti_two_max));
			dp[idx].conti_two_max = dp[idx].value + max(dp[idx - 1].conti_none_max, dp[idx - 1].conti_one_max);
		}
	}

	int ans = max(dp[n-1].conti_none_max, max(dp[n - 1].conti_one_max, dp[n - 1].conti_two_max));
	cout << ans << endl;

	return 0;
}