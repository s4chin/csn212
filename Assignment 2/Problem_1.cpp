#include <bits/stdc++.h>
using namespace std;

int main() {
    int zzi[55], zzd[55];
    // int a[] = { 1, 7, 4, 9, 2, 5 };
    /* int a[] = { 374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
                600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
                67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
                477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
                249, 22, 176, 279, 23, 22, 617, 462, 459, 244 };
                */
    int a[] = { 70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32 };
    int n = sizeof(a)/sizeof(a[0]);
    for(int i = 0; i < 55; i++) {
        zzi[i] = 1;
        zzd[i] = 1;
    }
    int res = 1;
    for(int i = 0; i < n; i++) {
        for(int j = i-1; j >= 0; j--) {
            if (zzi[i] < zzd[j] + 1 && a[j] < a[i])
                zzi[i] = zzd[j] + 1;
            if (zzd[i] < zzi[j] + 1 && a[j] > a[i])
                zzd[i] = zzi[j] + 1;
        }
        res = max(zzd[i], zzi[i]);
    }
    cout << res;
    return 0;
}
