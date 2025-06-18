#include <iostream>

using namespace std;

int x1, yi, r1, x2, y2, r2;
int distSquare;

bool isSame()
{
	if (x1 == x2 && yi == y2 && r1 == r2)
		return true;
	return false;
}

bool isNotMeet()
{
	if (distSquare < (r1-r2)*(r1-r2) || (r1+r2) * (r1 + r2) < distSquare)
		return true;
	return false;
}

bool isTouch()
{
	if (distSquare == (r1 - r2) * (r1 - r2) || (r1 + r2) * (r1 + r2) == distSquare)
		return true;
	return false;
}

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		int ans;

		cin >> x1 >> yi >> r1 >> x2 >> y2 >> r2;

		distSquare = (y2 - yi) * (y2 - yi) + (x2 - x1) * (x2 - x1);

		// 두 원이 겹칠 때 (일치)
		if (isSame())
			ans = -1;

		// 두 원이 안 만날 경우 (멀거나 포함 관계)
		else if (isNotMeet())
			ans = 0;

		// 한 점에서 만날 경우 (접하는 경우)
		else if (isTouch())
			ans = 1;

		// 그 외의 경우 (두 점에서 만날 때)
		else
			ans = 2;

		cout << ans << endl;
	}
		
	return 0;
}