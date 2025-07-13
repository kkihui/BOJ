#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

long long CalBlockCell(long long x1, long long x2, long long y1, long long y2, long long k)
{
	long long block = 0;
	// 최대 2*10^6번 반복.
	for (int x = x1; x <= x2; x++)
	{
		// 각 x에 대해서 y > 0의 최대값은 k-|x|, 이 중에서 장애물이 있는 부분, 돌아가서 갈 수 있는 부분 계산
		int y_max = k - abs(x);
		// y1 보다 작으면 장애물에 닿지 않음.
		if (y_max < y1)
		{
			continue;
		}
		// y1 ~ y2 사이면 y_max에서 y1까지 장애물인 부분 빼주기.
		else if (y_max <= y2)
		{
			block += y_max - y1 + 1;
		}
		// y2 보다 크면 y2에서 y1까지 장애물인 부분 빼주고 돌아가는 거리 계산
		else
		{
			block += y2 - y1 + 1;
			int x_dist = min(abs(x1) + abs(x - x1) + 2, x2 + abs(x - x2) + 2); // 우회하는데 필요한 거리
			int real_y_max = k - x_dist; // x1이나 x2 끝까지 갔다가 다시 와야 갈 수 있음.
			// 장애물 우회하고 갈 수 있는 값이 있으면
			if (real_y_max > y2)
			{
				block += (y_max - real_y_max); // y_max ~ real_y_max 사이는 못 감.
			}
			// 장애물 우회 못하면
			else
			{
				block += (y_max - y2); // y_max ~ y2 사이 못 감.
			}
		}
	}

	return block;
}

// num이 1 일때, 1+3+1 = 5 / 2일 때, 1+3+5+3+1 = 13 / 3일 때, 1+3+5+7+5+3+1 = 25 
// 전반부 등차 수열 최고항 (1,3,5,7..2n+1) n+1개
// 후반부 등차 수열 최고항 (2n-1, 2n-3,....1) n개
long long CalTotalCell(long long  num)
{
	// 첫째항이 a, 공차가 d인 등차수열의 합은 n{2a+(n-1)d} / 2 -> a=1, d=1이면 n(n+1)/2
	// 첫째항이 1, 공차가 2인 등차수열의 합은 n*n임.
	long long bigger_sum = (num + 1) * (num + 1);
	long long smaller_sum = (num) * (num);
	
	return bigger_sum + smaller_sum;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		long long  x1, x2, y1, y2, k;
		cin >> x1 >> x2 >> y1 >> y2 >> k;

		long long cell_nonblock = CalTotalCell(k) - CalBlockCell(x1, x2, y1, y2, k);

		cout << cell_nonblock << endl;
	}

	return 0;
}