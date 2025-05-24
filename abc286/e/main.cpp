#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <limits>
using namespace std;

const long long INF = numeric_limits<long long>::max();

int main() {
    int N;
    cin >> N;

    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    vector<string> S(N);
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }

    vector<vector<long long>> d(N, vector<long long>(N, INF));
    vector<vector<long long>> val(N, vector<long long>(N, 0));

    // 初期化
    for (int i = 0; i < N; ++i) {
        d[i][i] = 0;
        for (int j = 0; j < N; ++j) {
            val[i][j] = A[i];
            if (S[i][j] == 'Y') {
                d[i][j] = 1;
                val[i][j] += A[j];
            }
        }
    }

    // 最短距離更新 (ワーシャル–フロイド法)
    for (int k = 0; k < N; ++k) { // 経由する点
        for (int i = 0; i < N; ++i) { // 始点
            for (int j = 0; j < N; ++j) { // 終点
                if (d[i][k] == INF || d[k][j] == INF) continue; // 無限大の場合はスキップ
                if (d[i][j] > d[i][k] + d[k][j]) {
                    d[i][j] = d[i][k] + d[k][j];
                    val[i][j] = val[i][k] + val[k][j] - A[k];
                } else if (d[i][j] == d[i][k] + d[k][j]) {
                    val[i][j] = max(val[i][j], val[i][k] + val[k][j] - A[k]);
                }
            }
        }
    }

    int Q;
    cin >> Q;
    while (Q--) {
        int u, v;
        cin >> u >> v;
        --u, --v; // 0-indexedに変換
        if (d[u][v] == INF) {
            cout << "Impossible" << endl;
        } else {
            cout << d[u][v] << " " << val[u][v] << endl;
        }
    }

    return 0;
}
