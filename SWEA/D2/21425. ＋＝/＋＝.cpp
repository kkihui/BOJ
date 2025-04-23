#include<iostream>
 
using namespace std;
 
int main() {
 
    int T;
    cin >> T;
 
    for (int tc = 1;tc <= T;tc++) {
 
        long long x, y;
        long long Target;
        long long cnt = 0;
         
        cin >> x >> y >> Target;
 
        while (x <= Target && y <= Target) {
            if (x > y) {
                y += x;
                cnt++;
            }
            else {
                x += y;
                cnt++;
            }
        }
 
        cout << cnt << "\n";
    }
 
}