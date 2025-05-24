#include <iostream>
#include <vector>
#include <deque>
#include <set>

using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        A[i]--;  // 0インデックスに調整
    }

    // 隣接リストを作成
    vector<vector<int>> F(N);
    for (int i = 0; i < N; i++) {
        F[A[i]].push_back(i);
    }

    vector<int> seen(N, 0);
    long long ans = 0;

    for (int i = 0; i < N; i++) {
        if (seen[i]) continue;

        vector<int> stack;
        int now = i;
        seen[i] = 1;
        stack.push_back(i);

        // サイクルを検出
        while (true) {
            now = A[now];
            if (seen[now]) break;
            seen[now] = 1;
            stack.push_back(now);
        }

        // サイクルを保存
        vector<int> cycle = {now};
        while (true) {
            int v = stack.back();
            stack.pop_back();
            if (v == now) break;
            cycle.push_back(v);
        }

        ans += (long long)cycle.size() * cycle.size();

        vector<int> toadd(N, 0);

        set<int> set_cycle(cycle.begin(), cycle.end());
        for (int v : cycle) {
            deque<int> Q;
            Q.push_back(v);
            while (!Q.empty()) {
                int q = Q.front();
                Q.pop_front();
                for (int lq : F[q]) {
                    if (set_cycle.count(lq)) continue;
                    seen[lq] = 1;
                    toadd[lq] = toadd[q] + 1;
                    ans += (long long)cycle.size() + toadd[lq];
                    Q.push_back(lq);
                }
            }
        }
    }

    cout << ans << endl;
    return 0;
}
