#include <iostream>

#define ARR_MAX 1001

using namespace std;

class DP
{
public:
	int idx;
	int value;

	DP(int idx = 0, int value = 0)
	{
		this->idx = idx;
		this->value = value;
	}
};

DP dp[ARR_MAX];
int arr[ARR_MAX];

int main()
{
	int n;
	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	// 증가하는 부분 DP로 계산
	for (int i = 0; i < n; i++)
	{
		int smaller = 0;
		// 앞에서 더 적은 숫자가 몇 개 있었는지 체크.
		for (int j = 0; j < arr[i]; j++)
		{
			if (dp[j].value > smaller)
				smaller = dp[j].value;
		}
		if (dp[arr[i]].value < smaller + 1)
		{
			dp[arr[i]].value = smaller + 1;
			dp[arr[i]].idx = i;
		}
	}

	int ans = 0;

	for (int i = 0; i < ARR_MAX; i++)
		ans = max(ans, dp[i].value);

	cout << ans << endl;

	return 0;
}