#include<iostream>
#include<vector>

using namespace std;

int n;
int boxes[501];

bool IsNotSorted()
{
	for (int i = 0; i < n; i++)
	{
		if (boxes[i] > boxes[i + 1])
		{
			return true;
		}
	}
	return false;
}

int main(int argc, char** argv)
{
	int T;
	cin >> T;

	while (T--)
	{
		// 입력
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> boxes[i];
		}
		
		// 변수 선언
		vector<int> path;
		int idx_space = n, cnt = 0;
		boxes[idx_space] = 501;

		// 정렬 실시 및 기록
		while (idx_space != n || IsNotSorted())
		{
			// 빈 공간이 제일 뒤에 있을 때 (앞에서 자기 위치에 없는 제일 큰 것과 바꾸기)
			if (idx_space == n)
			{
				int idx = -1, value_max = 0;
				for (int i = 0; i < n; i++)
				{
					if (boxes[i] != i + 1 && boxes[i] > value_max)
					{
						value_max = boxes[i];
						idx = i;
					}
				}
				path.push_back(idx + 1);
				boxes[idx_space] = value_max;
				idx_space = idx;
				boxes[idx_space] = 501;
			}
			// 현재 위치에 해당하는 것과 바꾸기
			else
			{
				for (int i = 0; i < n + 1; i++)
				{
					if (boxes[i] == idx_space + 1)
					{
						path.push_back(i + 1);
						boxes[idx_space] = boxes[i];
						idx_space = i;
						boxes[idx_space] = 501;
						break;
					}
				}
			}
			cnt++;
		}

		// 출력
		cout << cnt << '\n';
		for (int i = 0; i < path.size(); i++)
		{
			cout << path[i] << ' ';
		}
		cout << '\n';
	}
	return 0;
}