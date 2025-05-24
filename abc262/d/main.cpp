#include <iostream>
#include <vector>
using namespace std;

const int MOD = 998244353;
const int INF = 1e9;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    vector<vector<vector<vector<int>>>> dp(
        N + 1, vector<vector<vector<int>>>(N + 1, vector<vector<int>>(N + 1, vector<int>(N + 1, 0))));
    
    for (int i = 0; i <= N; i++) {
        dp[0][0][i][0] = 1;
    }

    int ans = 0;
    for (int i = 1; i <= N; i++) { // i個目まで見る
        for (int j = 0; j <= N; j++) { // j個選ぶ
            for (int k = 1; k <= N; k++) { // kで割る
                for (int l = 0; l < k; l++) { // あまり
                    dp[i][j][k][l] = dp[i - 1][j][k][l];
                    dp[i][j][k][l] %= MOD;
                    if (j > 0) {
                        dp[i][j][k][l] += dp[i - 1][j - 1][k][(l - A[i - 1] % k + k) % k];
                        dp[i][j][k][l] %= MOD;
                    }
                }
            }
        }
    }

    for (int i = 0; i <= N; i++) {
        ans += dp[N][i][i][0];
        ans %= MOD;
    }

    cout << ans << endl;
    return 0;
}