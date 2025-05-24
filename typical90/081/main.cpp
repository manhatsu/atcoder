#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 5000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    vector<vector<int>> F(MAX + 1, vector<int>(MAX + 1, 0));
    
    // (a, b) の位置に1を加算
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        F[a][b]++;
    }

    // 累積和の計算
    vector<vector<int>> S(MAX + 1, vector<int>(MAX + 1, 0));

    for (int i = 1; i <= MAX; i++) {
        for (int j = 1; j <= MAX; j++) {
            S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + F[i][j];
        }
    }

    // 最大値を求める
    int ans = 0;
    for (int i = 0; i <= MAX; i++) {
        for (int j = 0; j <= MAX; j++) {
            if (i + K + 1 <= MAX && j + K + 1 <= MAX) {
                int sum = S[i + K + 1][j + K + 1] - S[i][j + K + 1] - S[i + K + 1][j] + S[i][j];
                ans = max(ans, sum);
            }
        }
    }

    cout << ans << "\n";

    return 0;
}
