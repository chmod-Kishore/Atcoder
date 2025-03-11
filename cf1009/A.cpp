#include <bits/stdc++.h>
using namespace std;
bool check(int x, int y, int z) {
    return (x+y>z) && (y+z>x) && (x+z>y);
}

bool isPowerOfTwo(int n) {
    return (n > 0) && ((n & (n - 1)) == 0);
}

int process(int i) {
    if((i&(i-1)) == 0){
        return -1;
    }
    for (int j = 1; j < i; j++) {
    if (isPowerOfTwo(j)) {
        continue;
    }
    int k = i ^ j;
    if (check(i, j, k)) {
        return j;
    }
}
    return -1;
}

/* Main() function */
void solve() {
    int n;
    cin >> n;
    int result = process(n);
    cout << result << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}