#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		int n, m;
		cin  >> n >> m;

		vector<int> warrior_n;
		vector<int> warrior_m;

		for (int j = 0; j < n; j++)
		{
			int a;
			cin >> a;
			warrior_n.push_back(a);
		}

		for (int j = 0; j < m; j++)
		{
			int b;
			cin >> b;
			warrior_m.push_back(b);
		}

		sort(warrior_n.begin(), warrior_n.end(), greater<int>());
		sort(warrior_m.begin(), warrior_m.end(), greater<int>());

		while (!warrior_n.empty() && !warrior_m.empty())
		{
			if (warrior_n[warrior_n.size()-1] >= warrior_m[warrior_m.size()-1])
			{
				warrior_m.pop_back();
			}
			else
			{
				warrior_n.pop_back();
			}
		}

		if (warrior_n.empty())
		{
			cout << 'B' << endl;
		}
		else
		{
			cout << 'S' << endl;
		}

	}

	return 0;
}