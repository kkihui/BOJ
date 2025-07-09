#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		int n;
		cin >> n;

		int arr[50];
		for (int i = 0; i < n; i++)
		{
			cin >> arr[i];
		}

		int distance_min = 10000;
		// 방문하지 않을 CheckPoint 별로 계산
		for (int i = 1; i < n-1; i++)
		{
			int distance = 0;
			for (int j = 1; j < n; j++)
			{
				if (j == i)
				{
					continue;
				}
				else if (j - 1 == i)
				{
					distance += abs(arr[j] - arr[j - 2]);
				}
				else
				{
					distance += abs(arr[j] - arr[j - 1]);
				}
			}
			distance_min = min(distance_min, distance);
		}

		cout << distance_min << endl;

	}
	return 0;
}