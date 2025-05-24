#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

int main() {
    int N;
    long long M;
    cin >> N >> M;

    vector<vector<int>> A(N, vector<int>(N));
    for (auto& row : A)
        for (auto& cell : row)
            cin >> cell;

    long long ans = 0;
    queue<tuple<int, int, long long>> q;
    q.emplace(0, 0, A[0][0] % M);

    while (!q.empty()) {
        auto [h, w, val] = q.front(); q.pop();

        if (h == N - 1 && w == N - 1) {
            ans = max(ans, val);
            continue;
        }

        if (h + 1 < N)
            q.emplace(h + 1, w, (val * 10 + A[h + 1][w]) % M);
        if (w + 1 < N)
            q.emplace(h, w + 1, (val * 10 + A[h][w + 1]) % M);
    }

    cout << ans << '\n';
    return 0;
}
