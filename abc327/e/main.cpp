#include <iostream>
#include <vector>
#include <cmath>
#include <limits>
#include <algorithm>

using namespace std;

const int MOD = 998244353;
const double INF = numeric_limits<double>::infinity();
const double MINF = -numeric_limits<double>::infinity();

int main() {
    int N;
    cin >> N;
    
    vector<double> P(N);
    for (int i = 0; i < N; i++) {
        cin >> P[i];
    }
    
    reverse(P.begin(), P.end());

    vector<vector<vector<double>>> dp(N + 1, vector<vector<double>>(N + 1, vector<double>(2, 0.0)));

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= i; j++) {
            if (j == 1) {
                dp[i][j][0] = P[i - 1];
                dp[i][j][1] = 1.0;
            } else {
                double offset = -1200.0 / sqrt(j);
                double cand_rate0 = (dp[i - 1][j][1] == 0) ? MINF : (dp[i - 1][j][0] / dp[i - 1][j][1] + offset);
                double cand_rate1 = (dp[i - 1][j - 1][1] == 0) ? MINF : ((dp[i - 1][j - 1][0] + pow(0.9, j - 1) * P[i - 1]) / (dp[i - 1][j - 1][1] + pow(0.9, j - 1)) + offset);

                if (cand_rate0 == MINF && cand_rate1 == MINF) {
                    continue;
                } else {
                    if (cand_rate0 > cand_rate1) {
                        dp[i][j][0] = dp[i - 1][j][0];
                        dp[i][j][1] = dp[i - 1][j][1];
                    } else {
                        dp[i][j][0] = dp[i - 1][j - 1][0] + pow(0.9, j - 1) * P[i - 1];
                        dp[i][j][1] = dp[i - 1][j - 1][1] + pow(0.9, j - 1);
                    }
                }
            }
        }
    }

    double ans = MINF;
    for (int j = 1; j <= N; j++) {
        double temp = dp[N][j][0] / dp[N][j][1] - 1200.0 / sqrt(j);
        ans = max(ans, temp);
    }

    cout << ans << endl;

    return 0;
}
