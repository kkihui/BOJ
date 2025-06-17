#include<iostream>

#define MAX_SIZE 10000000

using namespace std;

int matrix[4][4];
int dx[4] = {0,0,1,-1}, dy[4] = {1,-1,0,0};
bool arr[MAX_SIZE] = {false, };

void getNum(int row, int col, int time, int num)
{
    if (time == 7)
    {
        arr[num] = true;
        return;
    }

    int x, y;
    
    for (int i = 0; i < 4; i++)
    {
        x = row + dx[i];
        y = col + dy[i];
        if (0 <= x && x < 4 && 0 <= y && y < 4)
        {
            getNum(x, y, time + 1, num * 10 + matrix[x][y]);
        }
    }
}

int getAns()
{
    int ans = 0;
    for (int i = 0; i < MAX_SIZE; i++)
    {
        if (arr[i])
            ans++;
    }
    return ans;
}

int main(int argc, char** argv)
{
    int test_case;
    int T;
    cin >> T;

    for (test_case = 1; test_case <= T; ++test_case)
    {
        // 배열 초기화
        for (int i = 0; i < MAX_SIZE; i++)
            arr[i] = false;

        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
                cin >> matrix[i][j];
        }

        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
                getNum(i, j, 1, matrix[i][j]);
        }
        
        cout << '#' << test_case << ' ' << getAns() << endl;

    }
    return 0;
}