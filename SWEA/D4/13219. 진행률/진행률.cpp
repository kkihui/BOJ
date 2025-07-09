#include <iostream>
#include <cmath>

using namespace std;

const double PI = 3.141592653589793238;

double ToRadian(double deg)
{
	double rad = deg * PI / 180;

	return rad;
}

// Circle : (x-x1)^2 + (y-y1)^2 = r^2
bool OutofCircle(int x, int y)
{
	int distance = (x-50) * (x-50) + (y-50) * (y-50); // 거리 제곱
	if (distance > 2500)
		return true;
	else
		return false;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		int p, x, y;
		cin >> p >> x >> y;

		int color = 0;
		// 원밖인 부분은 무조건 흰색
		if (!OutofCircle(x, y))
		{
			// 중심 기준 1사분면
			if (x > 50 && y > 50)
			{
				// 싹다 흰색
				if (p == 0)
				{
					color = 0;
				}
				// 싹다 검은색
				else if (p >= 25)
				{
					color = 1;
				}
				// 흑백 혼재 (y = tan(rad)*(x-50)+50 직선과 점의 위치 비교)
				else
				{
					// (50,50)을 지나고 기울기가 tan(90 - 3.6*p deg)인 직선과의 위치 비교
					double degree = 90 - 3.6 * p;
					double radian = ToRadian(degree);
					// 직선과 겹치거나 위에 있으면 검정색.
					if (y >= tan(radian) * (x - 50) + 50)
					{
						color = 1;
					}
					// 직선보다 아래에 있으면 흰색.
					else
					{
						color = 0;
					}
				}
			}
			// 2사분면
			else if (x > 50 && y < 50)
			{
				// 싹다 흰색
				if (p <= 25)
				{
					color = 0;
				}
				// 싹다 검은색
				else if (p >= 50)
				{
					color = 1;
				}
				// 흑백 혼재
				else
				{
					// (50,50)을 지나고 기울기가 tan(90 - 3.6*p deg)인 직선과의 위치 비교
					double degree = 90 - 3.6 * p;
					double radian = ToRadian(degree);
					// 직선과 겹치거나 위에 있으면 검정색.
					if (y >= tan(radian) * (x - 50) + 50)
					{
						color = 1;
					}
					// 직선보다 아래에 있으면 흰색.
					else
					{
						color = 0;
					}
				}
			}
			// 3사분면
			else if (x < 50 && y < 50)
			{
				// 싹다 흰색
				if (p <= 50)
				{
					color = 0;
				}
				// 싹다 검은색
				else if (p >= 75)
				{
					color = 1;
				}
				// 흑백 혼재
				else
				{
					// (50,50)을 지나고 기울기가 tan(270 - 3.6*p deg)인 직선과의 위치 비교
					double degree = 270 - 3.6 * p;
					double radian = ToRadian(degree);
					// 직선과 겹치거나 아래에 있으면 검정색.
					if (y <= tan(radian) * (x - 50) + 50)
					{
						color = 1;
					}
					// 직선보다 위에 있으면 흰색.
					else
					{
						color = 0;
					}
				}
			}
			// 4사분면
			else if (x < 50 && y > 50)
			{
				// 싹다 흰색
				if (p <= 75)
				{
					color = 0;
				}
				// 싹다 검은색
				else if (p == 100)
				{
					color = 1;
				}
				// 흑백 혼재
				else
				{
					// (50,50)을 지나고 기울기가 tan(270 - 3.6*p deg)인 직선과의 위치 비교
					double degree = 270 - 3.6 * p;
					double radian = ToRadian(degree);
					// 직선과 겹치거나 아래에 있으면 검정색.
					if (y <= tan(radian) * (x - 50) + 50)
					{
						color = 1;
					}
					// 직선보다 위에 있으면 흰색.
					else
					{
						color = 0;
					}
				}
			}
			// 경계선 (x = 50 or y = 50)
			else
			{
				// 중심은 1펀센트라도 차면 무조건 검정색
				if (x == y)
				{
					if (p)
						color = 1;
					else
						color = 0;
				}
				// x = 50 (위쪽은 1퍼센트, 아래는 50퍼센트 이상 차야함)
				else if (x == 50)
				{
					if (y > 50)
					{
						if (p)
							color = 1;
						else
							color = 0;
					}
					else
					{
						if (p >= 50)
							color = 1;
						else
							color = 0;
					}
				}
				// y = 50 (오른쪽은 25퍼센트, 왼쪽은 75퍼센트 이상 차야함)
				else if (y == 50)
				{
					if (x > 50)
					{
						if (p >= 25)
							color = 1;
						else
							color = 0;
					}
					else
					{
						if (p >= 75)
							color = 1;
						else
							color = 0;
					}
				}
			}
		}

		cout << '#' << test_case << ' ' << color << endl;
	}
	return 0;
}