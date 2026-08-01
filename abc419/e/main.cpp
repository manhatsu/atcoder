#include <bits/stdc++.h>

using namespace std;

const long long INF = (1LL << 60);

int main() {

    int N, M, L;
    cin >> N >> M >> L;

    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        A[i] %= M;
    }

    vector<vector<long long>> C(L, vector<long long>(M, 0));
    for (int j = 0; j < M; j++) {
        for (int i = 0; i < L; i++) {
            for (int idx = i; idx < N; idx += L) {
                C[i][j] += (j - A[idx] + M) % M;
            }
        }
    }

    vector<vector<long long>> dp(L + 1, vector<long long>(M, INF));
    dp[0][0] = 0;

    for (int i = 1; i <= L; i++) {
        for (int j = 0; j < M; j++) {
            for (int k = 0; k < M; k++) {
                int prev = (j - k + M) % M;
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + C[i - 1][prev]);
            }
        }
    }

    long long ans = dp[L][0];
    cout << ans << "\n";

    return 0;
}
