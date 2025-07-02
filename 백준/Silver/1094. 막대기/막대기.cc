// 막대는 결국 2의 제곱의 합으로 표현되기 때문에 2진수로 변환해서 몇개의 1이 있는지 판단하면 됨.
#include <iostream>
#include <string>

using namespace std;

string ToBinary(int num)
{
	int arr[7] = { 0, }, idx = 0;
	string ret = "";
	while (num > 0)
	{
		if (num % 2 == 0)
		{
			arr[idx] = 0;
		}
		else
		{
			arr[idx] = 1;
		}
		num /= 2;
		idx++;

	}

	for (int i = 6; i >= 0; i--)
	{
		ret += arr[i]+'0';
	}

	return ret;
}

int GetAns(int num)
{
	string s = ToBinary(num);
	int cnt = 0;
	
	for (int i = 0; i < s.length(); i++)
	{
		if (s[i] == '1')
		{
			cnt++;
		}
	}
	
	return cnt;
}

int main()
{
	int x;
	cin >> x;

	int ans = GetAns(x);

	cout << ans << endl;

	return 0;
}