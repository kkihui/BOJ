#include <iostream>
#include <string>

using namespace std;

int main()
{
	int n, m, sx, sy, ex, ey;
	string ans;

	cin >> n >> m >> sx >> sy >> ex >> ey;

	if ((sx + sy) % 2 == (ex + ey) % 2)
		ans = "YES";
	else
		ans = "NO";

	cout << ans << endl;

	return 0;
}