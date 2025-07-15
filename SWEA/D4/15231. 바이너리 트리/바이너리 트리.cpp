/* 
	N이 10억 미만이므로 2 ^ 29 = 5억3천이기에 트리의 최대 깊이는 29까지.
	2^0 = 1 (depth 0), 2^1: 2~3 (depth 1) 2^2: 4~7 (depth 2) 2^3: 8~15 (depth 3)... 2^29: 536870912 ~ 1073741823 (depth 29)
	case 당 70번 이내 연산
*/

#include<iostream>

using namespace std;

int pow_2[31] = { 1, };

int CalcDepth(int num)
{
	int depth = 0;
	while (num >= pow_2[depth])
	{
		depth++;
	}
	return depth - 1;
}

int Solve(int n, int v)
{
	int depth_max = CalcDepth(n);
	int depth_cur = CalcDepth(v);

	// 루트에서 시작하면 최대 깊이와 동일.
	if (depth_cur == 0)
	{
		return depth_max;
	}
	// 그 외의 위치에선 올라갔다 루트 찍고 내려가는 것이 최대 (좌우 균형 판단)
	else
	{
		int ret = depth_cur; // root 까지 올라가는 거리.
		// 현재 루트 노드에서 왼쪽에 있을 경우 (depth_max가 오른쪽에 없을 수도 있음)
		if (v < pow_2[depth_cur] + pow_2[depth_cur - 1])
		{
			// depth_max가 왼쪽에만 있다면
			if (n < pow_2[depth_max] + pow_2[depth_max - 1])
			{
				ret += depth_max - 1;
			}
			// depth_max가 오른쪽에도 있다면
			else
			{
				ret += depth_max;
			}
		}
		// 현재 루트 노드에서 오른쪽에 있을 경우 (depth_max는 무조건 왼쪽에는 있음)
		else
		{
			ret += depth_max;
		}

		return ret;
	}
}

int main(int argc, char** argv)
{
	// c++ 입출력 속도 높이기 (c와 c+ 사이 stream 동기화 끔 / c의 표준 입출력 혼용 x)
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	// 2의 거듭제곱 목록 제작 (전처리)
	for (int i = 1; i < 31; i++)
	{
		pow_2[i] = pow_2[i - 1] * 2;
	}

	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		int n, v;
		cin >> n >> v;

		cout << '#' << test_case << ' ' << Solve(n,v) << '\n'; // 개행 시, std::endl 대신 '\n'이 시간 줄임.
	}
	return 0;
}