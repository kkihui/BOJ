#include<iostream>

using namespace std;

int n, cnt;
int ans_arr[50] = { 0, };

void Recursion(int num)
{
	if (cnt <= n && cnt != 50)
	{
		if (num <= n)
		{
			ans_arr[cnt++] = num;
			for (int i = 0; i < 10; i++)
			{
				Recursion(num * 10 + i);
			}
		}
	}
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
		cnt = 0;

		int num = 1;
		for (int num = 1; num < 10; num++)
		{
			Recursion(num);
		}

		cout << '#' << test_case;
		for (int i = 0; i < min(n,50); i++)
			cout << ' ' << ans_arr[i] << ".png";
		cout << '\n';

	}

	return 0;
}