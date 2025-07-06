#include<iostream>
#include<queue>
#include<vector>

using namespace std;

const int kMaxSize = 100001;

class DP
{
public:
	int time;
	int before;

	DP(int time = kMaxSize + 1, int before = -1)
	{
		this->time = time;
		this->before = before; // 직전 위치를 기록
	}
};

bool InRange(int num)
{
	return (0 <= num && num < kMaxSize);
}

int n, k, fastest_time = kMaxSize + 1;
DP dp[kMaxSize];

int main()
{
	cin >> n >> k;

	dp[n].time = 0;

	int ans_time;
	vector<int> ans_ways;

	if (n == k)
	{
		ans_time = 0;
		ans_ways.push_back(n);
	}
	else
	{
		queue<int> q;
		q.push(n);
		while (!q.empty())
		{
			int cur_idx = q.front();
			q.pop();

			int next_idx[3] = { cur_idx + 1,cur_idx - 1,cur_idx * 2 };
			for (int i = 0; i < 3; i++)
			{
				if (InRange(next_idx[i]))
				{
					// 더 빠르게 도달한 방법만 기록
					if (dp[next_idx[i]].time > dp[cur_idx].time + 1)
					{
						dp[next_idx[i]].time = dp[cur_idx].time + 1;
						// 직전에 도착한 위치 기록
						dp[next_idx[i]].before = cur_idx;
						
						// k에 도착한 제일 빠른 시간 이후는 확인할 필요x
						if (dp[next_idx[i]].time + 1 <= fastest_time)
						{
							q.push(next_idx[i]);
						}

						// k에 도달하면 fastest time 기록
						if (next_idx[i] == k && dp[next_idx[i]].time <= fastest_time)
						{
							fastest_time = dp[next_idx[i]].time;
						}
					}
				}
			}
		}

		ans_time = dp[k].time;
		int cur_idx = k;
		while (cur_idx != n)
		{
			ans_ways.push_back(cur_idx);
			cur_idx = dp[cur_idx].before;
		}
		ans_ways.push_back(n);
	}

	cout << ans_time << endl;
	
	for (int i = ans_ways.size() - 1; i >= 0; i--)
	{
		cout << ans_ways[i] << " ";
	}

	return 0;
}