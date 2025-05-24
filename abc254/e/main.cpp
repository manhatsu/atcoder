#include <bits/stdc++.h>
using namespace std;

constexpr int MOD = 998244353;
constexpr int INF = numeric_limits<int>::max();
constexpr int MINF = numeric_limits<int>::min();

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<vector<int>> G(N);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        --a; --b;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    vector<vector<int>> A(N, vector<int>(4, 0));
    for (int i = 0; i < N; ++i) {
        A[i][0] = i + 1;
    }

    for (int i = 0; i < N; ++i) {
        vector<bool> seen(N, false);
        queue<pair<int, int>> Q;
        seen[i] = true;
        Q.emplace(i, 0);

        while (!Q.empty()) {
            auto [v, d] = Q.front(); Q.pop();
            for (int lv : G[v]) {
                if (seen[lv]) continue;
                seen[lv] = true;
                if (d + 1 <= 3)
                    A[i][d + 1] += lv + 1;
                if (d + 1 == 3) continue;
                Q.emplace(lv, d + 1);
            }
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 1; j < 4; ++j) {
            A[i][j] += A[i][j - 1];
        }
    }

    int R;
    cin >> R;
    for (int i = 0; i < R; ++i) {
        int x, k;
        cin >> x >> k;
        cout << A[x - 1][k] << '\n';
    }

    return 0;
}
