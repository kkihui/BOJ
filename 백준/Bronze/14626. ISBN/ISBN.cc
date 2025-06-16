#include <iostream>
#include <string>

using namespace std;

int CalIsbn(string s, int m)
{
    int sum=0, idx;

    // 나머지의 합과 훼손된 숫자의 index 계산
    for (int i=0; i<12; i++)
    {
        if (s[i] != '*')
        {
            if (i%2 == 0)
                sum += s[i] - '0';
            else
                sum += 3 * (s[i] - '0');
        }
        else
            idx = i;
    }
    
    // 훼손된 숫자 도출
    for (int i=0; i<10; i++)
    {
        if (idx%2 == 0)
        {
            if ((10 - ((sum + i)%10))%10 == m)
                return i;
        }
        else
        {
            if ((10 - ((sum + 3*i)%10))%10 == m)
                return i;
        }
    }
}

int main() 
{
    string isbn;
    cin >> isbn;

    int check = isbn[12] - '0';

    cout << CalIsbn(isbn,check);

    return 0;
}