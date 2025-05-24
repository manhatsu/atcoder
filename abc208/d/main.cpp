#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

const long long INF = LLONG_MAX;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<vector<long long>>> F(N + 1, vector<vector<long long>>(N + 1, vector<long long>(N + 1, INF)));
    
    for (int i = 1; i <= N; i++) {
        for (int j = 0; j <= N; j++) {
            F[i][i][j] = 0;
        }
    }

    for (int i = 0; i < M; i++) {
        int a, b;
        long long c;
        cin >> a >> b >> c;
        F[a][b][0] = c;
    }

    for (int k = 1; k <= N; k++) {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (F[i][k][k - 1] != INF && F[k][j][k - 1] != INF) {
                    F[i][j][k] = min(F[i][j][k - 1], F[i][k][k - 1] + F[k][j][k - 1]);
                } else {
                    F[i][j][k] = F[i][j][k - 1];
                }
            }
        }
    }

    long long ans = 0;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            for (int k = 1; k <= N; k++) {
                if (F[i][j][k] != INF) {
                    ans += F[i][j][k];
                }
            }
        }
    }

    cout << ans << endl;

    return 0;
}
