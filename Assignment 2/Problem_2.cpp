#include <bits/stdc++.h>
using namespace std;

// std::to_string didn't work - http://stackoverflow.com/a/20861692/4905313
namespace patch
{
    template < typename T > string to_string( const T& n )
    {
        ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

long long SUM[105][105];

bool isbad(int i, int j, int x, int y, vector<string> bad) {
    string a1 = patch::to_string(i) + " " + patch::to_string(j) + " " + patch::to_string(x) + " " + patch::to_string(y);
    string a2 = patch::to_string(x) + " " + patch::to_string(y) + " " + patch::to_string(i) + " " + patch::to_string(j);
    for (auto p: bad) {
        if (a1 == p) {
            return true;
        }
        if (a2 == p) {
            return true;
        }
    }
    return false;
}

long long calc(int i, int j, vector<string> bad) {
    if (SUM[i][j] != -1)
        return SUM[i][j];
    long long sum = 0;
    if (i-1 >= 0 && !isbad(i, j, i-1, j, bad)) {
        if(i == 1 && j == 0) {
            sum += 1;
        } else {
            sum += calc(i-1, j, bad);
        }
    }
    if (j-1 >= 0 && !isbad(i, j, i, j-1, bad)) {
        if(i == 0 && j == 1) {
            sum += 1;
        } else {
            sum += calc(i, j-1, bad);
        }
    }
    SUM[i][j] = sum;
    return SUM[i][j];
}

long long pnc(int w, int l, vector<string> bad) {
    for(int i = 0; i <= w; i++) {
        for(int j = 0; j <= l; j++) {
            SUM[i][j] = -1;
        }
    }
    return calc(w, l, bad);
}

int main() {
    cout << pnc(6, 6, {"0 0 0 1","6 6 5 6"}) << endl;
    cout << pnc(1, 1, {}) << endl;
    cout << pnc(35, 31, {}) << endl;
    cout << pnc(2, 2, {"0 0 1 0", "1 2 2 2", "1 1 2 1"}) << endl;
    return 0;
}
