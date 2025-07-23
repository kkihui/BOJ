/* 오름차순으로 위치 정렬해서 DP 실시 */
 
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<climits>
#include<vector>
 
const int kmaxN = 50;
 
using namespace std;
 
struct Dp
{
    int r, c;
    int dist;
};
 
int n, k;
vector<Dp> dp[kmaxN * kmaxN + 1]; // [value][point index] = (r, c)
 
void DpClear()
{
    for (int i = 1; i <= kmaxN * kmaxN; i++)
        dp[i].clear();
}
 
int CalcAns()
{
    // k까지 다 있는지 판단 (최대 2500회 연산)
    for (int i = 1; i <= k; i++)
    {
        if (dp[i].empty())
        {
            DpClear();
            return -1;
        }
    }
     
    // value 별로 1 작은 value와의 최소 거리 계산 (최대 1250^2 = 1,562,500회 연산)
    for (int idx = 2; idx <= k; idx++)
    {
        for (int i = 0; i < dp[idx].size(); i++)
            for (int j = 0; j < dp[idx - 1].size(); j++)
            {
                int dist = abs(dp[idx][i].r - dp[idx - 1][j].r) + abs(dp[idx][i].c - dp[idx - 1][j].c) + dp[idx-1][j].dist;
                if (dp[idx][i].dist)
                    dp[idx][i].dist = min(dp[idx][i].dist, dist);
                else
                    dp[idx][i].dist = dist;
            }
    }
 
    // 최종 위치 k인 곳에서 최소값 구하기 (최대 2499회 연산)
    int ans = INT_MAX;
    for (int i = 0; i < dp[k].size(); i++)
        ans = min(ans, dp[k][i].dist);
         
    // dp 벡터 초기화 (2500회 연산)
    DpClear();
 
    return ans;
}
 
int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    int T;
    cin >> T;
 
    for (int test_case = 1; test_case <= T; ++test_case)
    {
        cin >> n >> k;
         
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
            {
                int value;
                cin >> value;
                dp[value].push_back({i, j, 0}); // value에 따라 좌표 저장
            }
 
        int ans = CalcAns();
 
        cout << '#' << test_case << ' ' << ans << '\n';
    }
    
    return 0;
}