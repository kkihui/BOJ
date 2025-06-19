#include <iostream>

using namespace std;

int main()
{
	int n; 
	char arr[100];

	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	for (int i = 0; i < n; i++)
	{
		int cnt_s = 0, cnt_t = 0;
		for (int j = i; j < n; j++)
		{
			if (arr[j] == 's')
				cnt_s++;
			else
				cnt_t++;
		}

		if (cnt_s == cnt_t)
		{
			for (int idx = i; idx < n; idx++)
				cout << arr[idx];
			break;
		}
	}

	return 0;
}