#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const int MOD = 998244353;
const int INF = numeric_limits<int>::max();
const int MINF = numeric_limits<int>::min();
const int LIMIT = 1000000;

int N, M;
vector<vector<int>> G;
vector<int> seen;
int K = 0;

void dfs(int v) {
    if (K >= LIMIT) return;
    K++;
    seen[v] = 1;
    for (int lv : G[v]) {
        if (seen[lv]) continue;
        dfs(lv);
    }
    seen[v] = 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    G.resize(N);
    seen.assign(N, 0);
    
    if (M == 0) {
        cout << 1 << "\n";
        return 0;
    }

    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    
    dfs(0);
    cout << (K < LIMIT ? K : LIMIT) << "\n";
    
    return 0;
}