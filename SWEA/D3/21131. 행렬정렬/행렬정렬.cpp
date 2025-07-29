#include<iostream>

const int kmaxN = 64;

using namespace std;

int n, temp;
int first_raw[kmaxN] = {0,};

int CalcAns()
{
	int cnt = 0;
	bool transpose = false;

	// i행과 i열을 전치할지 말지 판단해서 연산 횟수 추가
	for (int i = n - 1; i >= 1; i--)
	{
		if (first_raw[i] != i + 1 && !transpose)
		{
			cnt++;
			transpose = true;
		}
		else if (first_raw[i] == i + 1 && transpose)
		{
			cnt++;
			transpose = false;
		}
	}

	return cnt;
}

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0); 
	cout.tie(0);

	int T;
	cin >> T;

	while (T--)
	{
		cin >> n;

		// 1행으로 풀이 가능
		for (int i = 0; i < n; i++)
		{
			cin >> first_raw[i];
		}

		// 2 ~ n 행은 무시.
		for (int i = 1; i < n; i++)
			for (int j = 0; j < n; j++)
			{
				cin >> temp;
			}
		
		int ans = CalcAns();
		cout << ans << '\n';
	}

	return 0;
}