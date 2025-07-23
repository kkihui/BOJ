// DP로 에라스토스테네스의 체 처럼 계산

#include<iostream>
#include<algorithm>

const int kmaxN = 1e+5;
const int kmaxRange = 1e+6 + 1;

using namespace std;

int n;
int arr[kmaxN] = { 0, };
int dp[kmaxRange] = { 0, };
bool exist_num[kmaxRange] = { 0, };

int CalcAns(int max_value)
{
	// 배열 초기화
	for (int i = 0; i < kmaxRange; i++)
	{
		dp[i] = 0;
		exist_num[i] = 0;
	}

	// 수열에 존재하는 숫자들 업데이트
	for (int i = 0; i < n; i++)
	{
		exist_num[arr[i]] = 1;
	}

	int ret = 0;
	sort(arr, arr + n);

	// 작은 값 부터 dp 업데이트
	for (int i = 0; i < n; i++)
	{
		int num = arr[i];
		dp[num] += 1; // 자기자신 포함
		ret = max(ret, dp[num]);

		num += arr[i];
		while (num <= max_value)
		{
			if (exist_num[num])
			{
				dp[num] = max(dp[num], dp[arr[i]]); // 이전 값과 비교해서 더 큰 값으로 업데이트.
			}
			ret = max(ret, dp[num]);
			num += arr[i];
		}
	}

	return ret;
}

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int test_case;
	int T;

	cin >> T;


	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> n;

		int arr_max = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> arr[i];
			arr_max = max(arr_max, arr[i]);
		}

		int ans = CalcAns(arr_max);
		cout << '#' << test_case << ' ' << ans << '\n';

	}

	return 0;
}