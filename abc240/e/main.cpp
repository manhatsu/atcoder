#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;
const int INF = 1e9;
const int MINF = -1e9;

int N;
vector<vector<int>> G;
vector<int> L, R;
int num = 1;

void dfs(int v, int p) {
    if (G[v].size() == 1) { // 葉ノード
        L[v] = num;
        R[v] = num;
        num++;
        return;
    }
    for (int lv : G[v]) {
        if (lv == p) continue;
        dfs(lv, v);
        if (L[v] == -1) L[v] = L[lv];
        else L[v] = min(L[v], L[lv]);
        if (R[v] == -1) R[v] = R[lv];
        else R[v] = max(R[v], R[lv]);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    G.resize(N);
    L.assign(N, -1);
    R.assign(N, -1);

    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        u--, v--; // 0-based index に変換
        G[u].push_back(v);
        G[v].push_back(u);
    }

    G[0].push_back(-1); // ダミーノードを追加（Pythonのリストとは異なり無視される）

    dfs(0, -1);

    for (int i = 0; i < N; i++) {
        cout << L[i] << " " << R[i] << "\n";
    }

    return 0;
}
