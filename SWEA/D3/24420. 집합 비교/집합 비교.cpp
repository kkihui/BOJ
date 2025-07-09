#include<iostream>
#include<algorithm>
 
using namespace std;
 
int arr1[50], arr2[50];
 
bool IsSame(int n)
{
    for (int i=0; i<n; i++)
    {
        if (arr1[i] != arr2[i])
            return 0;
    }
    return 1;
}
 
bool IsPartial(int a,int b)
{
    if (a<b)
    {
        for (int i=0; i<a; i++)
        {
            bool exists = 0;
            for (int j=0; j<b; j++)
            {
                if (arr1[i] == arr2[j])
                {
                    exists = 1;
                    break;
                }
            }
            if (!exists)
                return 0;
        }
        return 1;
         
    }
    else
    {
        for (int i=0; i<b; i++)
        {
            bool exists = 0;
            for (int j=0; j<a; j++)
            {
                if (arr2[i] == arr1[j])
                {
                    exists = 1;
                    break;
                }
            }
            if (!exists)
                return 0;
        }
        return 1;
    }
}
 
int main(int argc, char** argv)
{
    int test_case;
     
    int T;
    cin >> T;
 
    for(test_case = 1; test_case <= T; ++test_case)
    {
        int a,b;
        cin >> a >> b;
         
        char ans;
         
        for (int i=0; i<a; i++)
            cin >> arr1[i];
        for (int i=0; i<b; i++)
            cin >> arr2[i];
         
        sort(arr1, arr1+a);
        sort(arr2, arr2+b);
         
        if (a==b)
        {
            if (IsSame(a))
                ans = '=';
            else
                ans = '?';
        }
        else
        {
            if (IsPartial(a,b))
            {
                if (a>b)
                    ans = '>';
                else
                    ans = '<';
            }
            else
                ans = '?';
        }
         
        cout << ans << endl;
    }
    return 0;
}