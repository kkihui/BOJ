#include <iostream>
#include <string>

using namespace std;

int main()
{
	while (1)
	{
		string line;
		getline(cin, line);

		if (line == "#")
		{
			break;
		}
		else
		{
			string word = "";
			for (int i = 0; i < line.length()+1; i++)
			{
				if (line[i] != ' ' && line[i] != '\0')
				{
					word += line[i];
				}
				else
				{
					for (int j = word.length() - 1; j >= 0; j--)
					{
						cout << word[j];
					}
					cout << " ";
					word = "";
				}
			}
			cout << endl;
		}
	}
	return 0;
}