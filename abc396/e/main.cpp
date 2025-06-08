#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const long long INF = 1LL << 60;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<tuple<int, int, int>> L;
    for (int i = 0; i < M; ++i) {
        int x, y, z;
        cin >> x >> y >> z;
        --x; --y; // 0-indexed
        L.emplace_back(x, y, z);
    }

    vector<vector<int>> ans(30, vector<int>(N, -1));

    for (int i = 0; i < 30; ++i) {
        vector<vector<pair<int, int>>> G(N);
        for (auto &[x, y, z] : L) {
            int bit = (z >> i) & 1;
            G[x].emplace_back(y, bit);
            G[y].emplace_back(x, bit);
        }

        vector<bool> seen(N, false);
        vector<pair<set<int>, set<int>>> group_lists;

        for (int j = 0; j < N; ++j) {
            if (seen[j]) continue;

            set<int> groups[2];
            queue<pair<int, int>> Q;
            Q.emplace(j, 0);
            groups[0].insert(j);
            seen[j] = true;

            while (!Q.empty()) {
                auto [v, g] = Q.front(); Q.pop();
                for (auto &[u, w] : G[v]) {
                    if (w == 0) {
                        if (groups[1 - g].count(u)) {
                            cout << -1 << '\n';
                            return 0;
                        }
                        if (!seen[u]) {
                            groups[g].insert(u);
                            seen[u] = true;
                            Q.emplace(u, g);
                        }
                    } else {
                        if (groups[g].count(u)) {
                            cout << -1 << '\n';
                            return 0;
                        }
                        if (!seen[u]) {
                            groups[1 - g].insert(u);
                            seen[u] = true;
                            Q.emplace(u, 1 - g);
                        }
                    }
                }
            }

            // swap if needed
            if (groups[0].size() < groups[1].size())
                swap(groups[0], groups[1]);

            group_lists.emplace_back(groups[0], groups[1]);
        }

        for (auto &[group0, group1] : group_lists) {
            for (int v : group0) ans[i][v] = 0;
            for (int v : group1) ans[i][v] = 1;
        }
    }

    vector<int> ret(N, 0);
    for (int i = 0; i < 30; ++i) {
        for (int j = 0; j < N; ++j) {
            if (ans[i][j] == 1)
                ret[j] |= (1 << i);
        }
    }

    for (int i = 0; i < N; ++i) {
        cout << ret[i] << (i == N - 1 ? '\n' : ' ');
    }

    return 0;
}
