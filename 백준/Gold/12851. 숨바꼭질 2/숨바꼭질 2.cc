#include<iostream>
#include<queue>
#include<climits>

using namespace std;

const int kMaxSize = 100001;

class DP
{
public:
	int time;
	int ways;
	bool cur_way[3];

	DP(int time = INT_MAX,int ways = 0)
	{
		this->time = time;
		this->ways = ways; // 현재까지의 총 방법 수
		this->cur_way[3] = {false,}; // 현재 숫자에 도달한 방법 수 (idx 0은 -1, 1은 +1, 2는 *2로 도달)
	}
};

bool InRange(int num)
{
	return (0 <= num && num < kMaxSize);
}

int n, k, fastest_time = INT_MAX;
DP dp[kMaxSize];

int main()
{
	cin >> n >> k;

	dp[n].time = 0;
	dp[n].ways = 1;

	int ans_time, ans_ways;

	if (n == k)
	{
		ans_time = 0;
		ans_ways = 1;
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
					if (dp[next_idx[i]].time >= dp[cur_idx].time + 1)
					{
						// 해당 시간에 새로운 방법으로 도달하면 + 현재까지 도달한 ways
						if (dp[next_idx[i]].time == dp[cur_idx].time + 1)
						{
							if (dp[next_idx[i]].cur_way[i] != 1)
							{
								dp[next_idx[i]].ways += dp[cur_idx].ways;
								dp[next_idx[i]].cur_way[i] = 1;
							}
						}
						// 처음 도달하면 똑같은 ways와 현재 도달한 방법에 방문 처리
						else
						{
							dp[next_idx[i]].ways = dp[cur_idx].ways;
							dp[next_idx[i]].cur_way[i] = 1;
						}
						dp[next_idx[i]].time = dp[cur_idx].time + 1;

						// k에 도착한 제일 빠른 시간 이후는 확인할 필요x
						if (dp[next_idx[i]].time + 1 <= fastest_time)
						{
							q.push(next_idx[i]);
						}

						if (next_idx[i] == k && dp[next_idx[i]].time <= fastest_time)
						{
							fastest_time = dp[next_idx[i]].time;
						}
					}
				}
			}
		}

		ans_time = dp[k].time;
		ans_ways = dp[k].ways;
	}

	cout << ans_time << endl << ans_ways << endl;

	return 0;
}