#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;
const int INF = INT_MAX;
const int MINF = INT_MIN;

int H, W;
vector<vector<int>> F;
vector<vector<int>> seen;
int ans = 0;
int dh[2] = {0, 1}; // 右・下
int dw[2] = {1, 0};

// XORを計算する関数
int calc_xor(const vector<vector<int>>& seen) {
    int ret = 0;
    for (int h = 0; h < H; ++h) {
        for (int w = 0; w < W; ++w) {
            if (seen[h][w] == 0) {
                ret ^= F[h][w];
            }
        }
    }
    return ret;
}

void dfs(vector<vector<int>>& seen) {
    ans = max(ans, calc_xor(seen));

    for (int h = 0; h < H; ++h) {
        for (int w = 0; w < W; ++w) {
            if (seen[h][w] > 0) continue;

            seen[h][w] = 1;

            for (int k = 0; k < 2; ++k) {
                int nh = h + dh[k];
                int nw = w + dw[k];
                if (0 <= nh && nh < H && 0 <= nw && nw < W && seen[nh][nw] == 0) {
                    seen[nh][nw] = 1;
                    dfs(seen);
                    seen[nh][nw] = 0;
                }
            }

            seen[h][w] = 0;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> H >> W;
    F.assign(H, vector<int>(W));
    seen.assign(H, vector<int>(W, 0));

    for (int h = 0; h < H; ++h) {
        for (int w = 0; w < W; ++w) {
            cin >> F[h][w];
        }
    }

    ans = calc_xor(seen);
    dfs(seen);

    cout << ans << '\n';
    return 0;
}
