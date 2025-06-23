#include <iostream>

const int kArrMax = 1001;

using namespace std;

class DP
{
public:
	int asc;
	int des;
	
	DP(int a = 0, int d = 0)
	{
		this->asc = a;
		this->des = d;
	}
};

class NumArray
{
public:
	int value;
	int asc_cnt;
	int des_cnt;
	
	NumArray(int v = 0, int a = 0, int d = 0)
	{
		this->value = v;
		this->asc_cnt = a;
		this->des_cnt = d;
	}
};

DP dp[kArrMax];
NumArray arr[kArrMax];

int main()
{
	int n;
	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> arr[i].value;
	
	// 1~idx까지 증가하는 부분 DP로 계산
	for (int i = 0; i < n; i++)
	{	
		int asc = 0;
		for (int j = 0; j < arr[i].value; j++)
			asc = max(asc, dp[j].asc);

		dp[arr[i].value].asc = asc+1;
		
		for (int j = 0; j <= arr[i].value; j++)
			arr[i].asc_cnt = max(arr[i].asc_cnt,dp[j].asc);

		for (int j = 0; j < i; j++)
			arr[i].asc_cnt = max(arr[i].asc_cnt, arr[j].asc_cnt);

	}

	// idx~n까지 감소하는 부분 DP로 계산 (거꾸로 오름차순)
	for (int i = n - 1; i >= 0; i--)
	{
		int des = 0;
		for (int j = 0; j < arr[i].value; j++)
			des = max(des, dp[j].des);
		dp[arr[i].value].des = des+1;

		for (int j = 0; j <= arr[i].value; j++)
			arr[i].des_cnt = max(arr[i].des_cnt, dp[j].des);

		for (int j = n-1; j > i; j--)
			arr[i].des_cnt = max(arr[i].des_cnt, arr[j].des_cnt);
	}

	// ASC와 DES 합 제일 큰 것 도출 (수열의 i 번째 부분이 2번 반영 되므로 마지막에 1 빼줌).
	int ans = 0;
	for (int i = 0; i < n; i++)
		ans = max(ans, arr[i].des_cnt + arr[i].asc_cnt);

	cout << ans-1 << endl;

	return 0;
}