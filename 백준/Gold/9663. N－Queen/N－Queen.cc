#include <iostream>

using namespace std;

int n, cnt;

struct Point
{
	int r;
	int c;
};

class Board
{
public: 
	Point cur_pt;

	bool record_row[15];  // 각 행에 Queen이 있는지
	bool record_diag1[29]; // ↘ 방향 대각선 (row - col + n) 이 true인지로 판단 
	bool record_diag2[29]; // ↙ 방향 대각선 (row + col)이 true인지로 판단

	// 생성자: record arr를 받지 않는 경우
	Board(const Point pt)
	{
		this->cur_pt = pt;
		for (int i = 0; i < 2*n - 1; i++)
		{
			if (i < n)
			{
				record_row[i] = 0;
			}
			record_diag1[i] = 0;
			record_diag2[i] = 0;
		}
	}


	// 생성자: record arr을 받는 경우
	Board(const Point pt, const bool r_row[], const bool r_diag1[], const bool r_diag2[])
	{
		this->cur_pt = pt;
		for (int i = 0; i < 2 * n - 1; i++)
		{
			if (i < n)
			{
				record_row[i] = r_row[i];
			}
			record_diag1[i] = r_diag1[i];
			record_diag2[i] = r_diag2[i];
		}
	}
};

// 해당 좌표에 Queen 놓을 수 있는지 판단. (record 주어질 경우)
bool CanPutQueen(Point pt, bool r_row[], bool r_diag1[], bool r_diag2[])
{
	// Record 활용하여 이미 있는지 판단
	// row 판단
	if (r_row[pt.r])
	{
		return false;
	}
	
	// 대각선 판단, ↘ 방향 대각선 (row - col + n) 과 ↙ 방향 대각선 (row + col - n)
	if (r_diag1[pt.r - pt.c + n] || r_diag2[pt.r + pt.c])
	{
		return false;
	}
	
	return true; // 위에서 안 걸리면 놓을 수 있음.
}

void Bfs(Board bd)
{
	// 끝까지 왔으면 cnt 하나 올림
	if (bd.cur_pt.c == n - 1)
	{
		cnt++;
	}
	// 끝까지 안 왔으면 다음 column에 Queen 놓을 수 있는지 탐색.
	else
	{
		// 기록 활용하여 가능하면 BFS 실행.
		for (int i = 0; i < n; i++)
		{
			Point pt = {i, bd.cur_pt.c + 1};
			
			// pt 위치에 Queen 놓을 수 있으면 Bfs 실행.
			if (CanPutQueen(pt, bd.record_row, bd.record_diag1, bd.record_diag2))
			{
				Board next(pt, bd.record_row, bd.record_diag1, bd.record_diag2);
				next.record_row[pt.r] = 1;
				next.record_diag1[pt.r - pt.c + n] = 1;
				next.record_diag2[pt.r + pt.c] = 1;
				Bfs(next);
			}
		}
	}
}

int CountCase()
{
	for (int i = 0; i < n; i++)
	{
		Point pt = { i, 0 };

		Board board(pt);
		board.record_row[i] = 1;
		board.record_diag1[pt.r - pt.c + n] = 1;
		board.record_diag2[pt.r + pt.c] = 1; 

		Bfs(board);
	}

	return cnt;
}

int main()
{
	cin >> n;

	cout << CountCase() << endl;

	return 0;
}