#include <bits/stdc++.h>
using namespace std;

double compute_probability(vector<int> &die1, vector<int> &die2) {
    unordered_map<int, long long> freq;
    for (int num : die1) {
        freq[num]++;
    }
    long long total_outcomes = (long long)die1.size() * die2.size();
    long long favorable = 0;
    for (int num : die2) {
        if (freq.find(num) != freq.end()) {
            favorable += freq[num];
        }
    }
    return (double)favorable / total_outcomes;
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("inputf.in", "r", stdin);
    #endif
    long long N;
    cin >> N;
    vector<vector<int>> dice(N);
    for (long long i = 0; i < N; ++i) {
        long long K;
        cin >> K;
        dice[i].resize(K);
        for (long long j = 0; j < K; ++j) {
            cin >> dice[i][j];
        }
    }
    double max_probability = 0.0;
    for (long long i = 0; i < N; ++i) {
        for (long long j = i + 1; j < N; ++j) {
            double prob = compute_probability(dice[i], dice[j]);
            max_probability = max(max_probability, prob);
        }
    }
    cout << fixed << setprecision(15) << max_probability << endl;
    return 0;
}
