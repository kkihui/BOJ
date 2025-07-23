/* i번째에 arr[i]라는 숫자 이전에 0 ~ i-1 idx에서 arr[i] - 1이 나왔다면 연산 횟수가 1회 줄어든다. */
#include<iostream>

const int kmaxN = 200001;

using namespace std;

int n;
int arr[kmaxN] = { 0, };

// 한 번만 탐색하면서 O(n)으로 계산하기.
int CalcAns()
{
	bool record[kmaxN] = { 0, }; // arr[i] 기록 및 arr[i] - 1이 앞에 나왔는지 확인.
	int ret = n; // 최대 n번 해야함. (역순 배열)
	for (int i = 0; i < n; i++)
	{
		// arr[i] - 1이 앞에 나왔다면
		if (record[arr[i]-1])
		{
			ret--;
		}
		record[arr[i]] = 1;
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

		for (int i = 0; i < n; i++)
		{
			cin >> arr[i];
		}

		int ans = CalcAns();

		cout << '#' << test_case << ' ' << ans << '\n';
	}

	return 0;
}