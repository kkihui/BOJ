#include <iostream>
#include <string>
#include <deque>

using namespace std;

/* 2가지 방식 다 가능 (메모리와 시간 측면에서 차이 x)
bool IsNotPalindrome(deque<char> str)
{
    while (str.size() >= 2)
    {
        if (str.front() != str.back())
        {
            return true;
        }
        else
        {
            str.pop_front();
            str.pop_back();
        }
    }
         
    return false;
}
*/

bool IsNotPalindrome(const deque<char>& str)
{
	auto left = str.begin();
	auto right = str.end() - 1;

	while (left < right)
	{
		if (*left != *right)
		{
			return true;
		}
		left++;
		right--;
	}

	return false;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin >> T;

	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		string s;
		cin >> s;

		deque<char> dq;
		for (int i = 0; i < s.length(); i++)
		{
			dq.push_back(s[i]);
		}

		int cnt = 0;

		while (dq.size() >= 2 && (dq.front() == 'x' || dq.back() == 'x' || dq.front() == dq.back()))
		{
			if (dq.front() == dq.back())
			{
				dq.pop_front();
				dq.pop_back();
			}
			else if (dq.front() == 'x')
			{
				dq.push_back('x');
				cnt++;
			}
			else if (dq.back() == 'x')
			{
				dq.push_front('x');
				cnt++;
			}
		}

		if (dq.size() >= 2 && IsNotPalindrome(dq))
		{
			cnt = -1;
		}

		cout << cnt << endl;
	}
	return 0;
}