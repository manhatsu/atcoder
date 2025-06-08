#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const long long INF = 1LL << 60;

int N, M;
vector<vector<pair<int, int>>> G;

bool is_ok(int val) {
    vector<long long> dist(N, INF);
    dist[0] = 0;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    pq.emplace(0, 0);

    while (!pq.empty()) {
        auto [nd, nv] = pq.top(); pq.pop();
        if (nd > dist[nv]) continue;

        for (auto [lv, cost] : G[nv]) {
            if ((dist[nv] | cost) < dist[lv]) {
                if ((cost & val) == cost) {
                    dist[lv] = dist[nv] | cost;
                    pq.emplace(dist[lv], lv);
                }
            }
        }
    }
    return dist[N - 1] != INF;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    G.resize(N);

    for (int i = 0; i < M; ++i) {
        int u, v, d;
        cin >> u >> v >> d;
        u--, v--;
        G[u].emplace_back(v, d);
        G[v].emplace_back(u, d);
    }

    string ans(30, '1');
    for (int i = 0; i < 30; ++i) {
        ans[i] = '0';
        int val = stoi(ans, nullptr, 2);
        if (is_ok(val)) {
            continue;
        } else {
            ans[i] = '1';
        }
    }

    cout << stoi(ans, nullptr, 2) << '\n';
    return 0;
}
