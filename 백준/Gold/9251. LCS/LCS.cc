// s1이나 s2의 길이가 0이면 LCS(s1,s2) = 0
// s1과 s2의 끝글자가 같으면 LCS(s1,s2) = 1 + LCS(s1[:-2],s2[:-2]
// s1과 s2의 끝글자가 다름녀 LCS(s1,s2) = max(LCS(s1,s2[:-2]),LCS(s1[:-2],s2))

#include <iostream>
#include <string>

using namespace std;

string s1, s2;
int dp[1000][1000] = {0, };

bool InRange(int x, int y)
{
	return 0 <= x && x < s1.length() && 0 <= y && y < s2.length();
}

int LCS()
{
	int dx[2] = { 0,-1};
	int dy[2] = { -1,0};
	for (int i = 0 ; i < s1.length(); i++)
		for (int j = 0; j < s2.length(); j++)
		{
			int value;
			if (s1[i] == s2[j])
			{
				value = 1;
				if (InRange(i - 1, j - 1))
				{
					value += dp[i - 1][j - 1];
				}
			}
			else
			{
				value = 0;
				int prev_max = 0;
				for (int k = 0; k < 2; k++)
				{
					if (InRange(i + dx[k], j + dy[k]))
					{
						prev_max = max(prev_max, dp[i + dx[k]][j + dy[k]]);
					}
				}
				value += prev_max;
			}
			dp[i][j] = value;
		}

	return dp[s1.length() - 1][s2.length() - 1];
}

int main()
{
	cin >> s1 >> s2;

	cout << LCS() << endl;

	return 0;
}