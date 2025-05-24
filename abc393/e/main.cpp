#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAX_A = 1000000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;
    vector<int> A(N);
    vector<int> div_count(MAX_A + 1, 0); 

    // 入力
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        div_count[A[i]]++;
    }

    for (int d = 1; d <= MAX_A; ++d) {
        for (int multiple = 2 * d; multiple <= MAX_A; multiple += d) {
            div_count[d] += div_count[multiple];
        }
    }

    for (int g = MAX_A; g >= 1; --g) {
        if (div_count[g] >= K) {
            cout << g << '\n';
            return 0;
        }
    }

    return 0;
}
