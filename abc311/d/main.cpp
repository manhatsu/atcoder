#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<string> F(N);
    for (int i = 0; i < N; ++i) {
        cin >> F[i];
    }

    // スタート地点
    int sh = 1, sw = 1;
    int dh[] = {0, 1, 0, -1}; // 移動方向（上下左右の4方向）
    int dw[] = {1, 0, -1, 0};

    // seen配列を3次元ベクトルで初期化
    vector<vector<vector<int>>> seen(N, vector<vector<int>>(M, vector<int>(4, 0)));

    // キューを作成 (h, w, d) を持つ
    queue<pair<pair<int, int>, int>> Q;
    for (int i = 0; i < 4; ++i) {
        Q.push({{sh, sw}, i});
    }

    while (!Q.empty()) {
        auto current = Q.front();
        Q.pop();
        int nh = current.first.first;
        int nw = current.first.second;
        int d = current.second;
        seen[nh][nw][d] = 1;

        int nexh = nh + dh[d];
        int nexw = nw + dw[d];

        // 範囲外チェック
        if (nexh < 0 || nexh >= N || nexw < 0 || nexw >= M) {
            continue;
        }

        if (F[nexh][nexw] == '#') {
            // 壁にぶつかった場合、他の方向を試す
            for (int k = 0; k < 4; ++k) {
                if (!seen[nh][nw][k]) {
                    Q.push({{nh, nw}, k});
                }
            }
        } else {
            // 壁でない場合、現在の方向で進む
            if (!seen[nexh][nexw][d]) {
                Q.push({{nexh, nexw}, d});
            }
        }
    }

    int ans = 0;
    for (int h = 0; h < N; ++h) {
        for (int w = 0; w < M; ++w) {
            for (int i = 0; i < 4; ++i) {
                if (seen[h][w][i] == 1) {
                    ans++;
                    break;
                }
            }
        }
    }

    cout << ans << endl;
    return 0;
}
