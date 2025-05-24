#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <tuple>

using namespace std;

const int MOD = 998244353;
const long long INF = numeric_limits<long long>::max();

int main() {
    int N, M, X;
    cin >> N >> M >> X;
    
    vector<vector<int>> G(N), INVG(N);
    
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        G[u].push_back(v);
        INVG[v].push_back(u);
    }
    
    vector<vector<long long>> dist(N, vector<long long>(2, INF));

    using T = tuple<long long, int, int>;
    auto cmp = [](const T& a, const T& b) { return get<0>(a) > get<0>(b); };
    priority_queue<T, vector<T>, decltype(cmp)> pq(cmp);
    
    pq.emplace(0, 0, 0);
    dist[0][0] = 0;
    
    while (!pq.empty()) {
        long long c;
        int v, state;
        tie(c, v, state) = pq.top();
        pq.pop();
        
        if (dist[v][state] < c) continue;
        
        if (state == 0) {
            for (int lv : G[v]) {
                if (dist[lv][state] > c + 1) {
                    dist[lv][state] = c + 1;
                    pq.emplace(c + 1, lv, state);
                }
            }
        } else {
            for (int lv : INVG[v]) {
                if (dist[lv][state] > c + 1) {
                    dist[lv][state] = c + 1;
                    pq.emplace(c + 1, lv, state);
                }
            }
        }
        
        if (dist[v][1 - state] > c + X) {
            dist[v][1 - state] = c + X;
            pq.emplace(c + X, v, 1 - state);
        }
    }
    
    long long ans = min(dist[N - 1][0], dist[N - 1][1]);
    cout << (ans == INF ? -1 : ans) << endl;
    
    return 0;
}
