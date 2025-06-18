#include <iostream>

using namespace std;

int woods[5];

bool isNotDone()
{
	for (int i = 0; i < 5; i++)
	{
		if (woods[i] != i + 1)
			return true;
	}
	return false;
}

void printWoods()
{
	for (int i = 0; i < 5; i++)
		cout << woods[i] << ' ';
	cout << endl;
}

void sortWoods()
{
	int idx = 0;
	while (isNotDone())
	{
		if (woods[idx] > woods[idx + 1])
		{
			int temp = woods[idx];
			woods[idx] = woods[idx + 1];
			woods[idx + 1] = temp;
			printWoods();
		}
		idx++;
		if (idx == 4)
			idx = 0;
	}
}

int main()
{
	for (int i = 0; i < 5; i++)
		cin >> woods[i];

	sortWoods();

	return 0;
}