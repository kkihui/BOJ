#include <iostream>
#include <string>

using namespace std;

int main()
{
	int n, m, sx, sy, ex, ey;
	string ans;

	cin >> n >> m >> sx >> sy >> ex >> ey;

	if (n == 1)
	{
		if (sy == ey)
			ans = "YES";
		else
			ans = "NO";
	}
	else if (m == 1)
	{
		if (sx == ex)
			ans = "YES";
		else
			ans = "NO";
	}
	else
	{
		if ((sx + sy) % 2 == (ex + ey) % 2)
			ans = "YES";
		else
			ans = "NO";
	}
	cout << ans << endl;

	return 0;
}