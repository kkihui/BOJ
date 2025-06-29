#include <iostream>
#include <string>

using namespace std;

int main()
{
	int k, s;
	cin >> k >> s;
	cin.ignore();

	string line;
	getline(cin, line);

	k = k % 26;

	for (int i = 0; i < s; i++)
	{
		if (line[i] == '.' || line[i] == ',' || line[i] == ' ')
		{
			cout << line[i];
		}
		// 소문자
		else if (line[i] >= 'a')
		{
			if ((int)line[i] + k > 122)
			{
				cout << (char)((int)line[i] + k - 26);
			}
			else
			{
				cout << (char)((int)line[i] + k);
			}
			
		}
		// 대문자
		else
		{
			if ((int)line[i] + k > 90)
			{
				cout << (char)((int)line[i] + k - 26);
			}
			else
			{
				cout << (char)((int)line[i] + k);
			}
		}
	}

	return 0;
}