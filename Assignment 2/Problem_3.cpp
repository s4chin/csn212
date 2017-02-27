// https://www.codechef.com/viewsolution/12945923

#include <bits/stdc++.h>
using namespace std;

int lisc(int index, int n, int *a) {
    int lis[n]; int res = 0;
    for(int i = 0; i < n; i++) {
            int m = 1;
            for(int j = i-1; j >= 0; j--) {
                if(a[j+index] < a[i+index])
                    m = lis[j] < m ? m : lis[j]+1;
            }
            lis[i] = m;
            if(lis[i] > res) res = lis[i];
        }
        return res;
   }

int main() {
    int t, n;
    int m, res;
    int a[100000];
    cin >> t;
    while(t--) {
        cin >> n;
        vector<pair<int,int> > s(n);
        res = 1;
        for(int i = 0; i < n; i++) {
            cin >> a[i];
            a[i+n] = a[i];
            s[i].first = a[i];
            s[i].second = i;
        }
        sort(s.begin(),s.end());
        int ans = 0;
        for(int i = 0; i < min(36, n); i++) {
            ans = max(ans, lisc(s[i].second, n, a));
        }
        cout << ans << "\n";
    }
    return 0;
}
