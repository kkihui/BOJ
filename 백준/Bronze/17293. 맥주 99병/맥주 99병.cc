#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;

	int left = n;
	while (left > 1)
	{
		cout << left << " bottles of beer on the wall, " << left << " bottles of beer." << endl;
		if (left != 2)
		{
			cout << "Take one down and pass it around, " << --left << " bottles of beer on the wall." << endl << endl;
		}
		else
		{
			cout << "Take one down and pass it around, " << --left << " bottle of beer on the wall." << endl << endl;
		}
	}

	cout << "1 bottle of beer on the wall, 1 bottle of beer." << endl;
	cout << "Take one down and pass it around, no more bottles of beer on the wall." << endl << endl;

	cout << "No more bottles of beer on the wall, no more bottles of beer." << endl;
	if (n != 1)
	{
		cout << "Go to the store and buy some more, " << n << " bottles of beer on the wall." << endl;
	}
	else
	{
		cout << "Go to the store and buy some more, " << n << " bottle of beer on the wall." << endl;
	}	

	return 0;
}