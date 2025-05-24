#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <tuple>

using namespace std;

const int INF = numeric_limits<int>::max();
const int MOD = 998244353;
const int dh[4] = {0, 1, 0, -1};
const int dw[4] = {1, 0, -1, 0};

int main() {
    int N;
    cin >> N;
    vector<string> F(N);
    for (int i = 0; i < N; i++) {
        cin >> F[i];
    }
    
    int p0h = -1, p0w = -1, p1h = -1, p1w = -1;
    for (int h = 0; h < N; h++) {
        for (int w = 0; w < N; w++) {
            if (F[h][w] == 'P') {
                if (p0h == -1) {
                    p0h = h; p0w = w;
                } else {
                    p1h = h; p1w = w;
                }
            }
        }
    }
    
    vector<vector<vector<vector<int>>>> dist(N, vector<vector<vector<int>>>(N, vector<vector<int>>(N, vector<int>(N, INF))));
    queue<tuple<int, int, int, int, int>> Q;
    dist[p0h][p0w][p1h][p1w] = 0;
    Q.push(make_tuple(p0h, p0w, p1h, p1w, 0));
    
    int ans = INF;
    while (!Q.empty()) {
        auto [n0h, n0w, n1h, n1w, v] = Q.front(); Q.pop();
        
        for (int i = 0; i < 4; i++) {
            int nn0h = n0h + dh[i];
            int nn0w = n0w + dw[i];
            int nn1h = n1h + dh[i];
            int nn1w = n1w + dw[i];
            
            bool flag0 = (nn0h >= 0 && nn0h < N && nn0w >= 0 && nn0w < N && F[nn0h][nn0w] != '#');
            bool flag1 = (nn1h >= 0 && nn1h < N && nn1w >= 0 && nn1w < N && F[nn1h][nn1w] != '#');
            
            if (!flag0 && !flag1) continue;
            if (!flag0 && flag1) { nn0h = n0h; nn0w = n0w; }
            if (flag0 && !flag1) { nn1h = n1h; nn1w = n1w; }
            
            if (dist[nn0h][nn0w][nn1h][nn1w] != INF) continue;
            
            dist[nn0h][nn0w][nn1h][nn1w] = v + 1;
            Q.push(make_tuple(nn0h, nn0w, nn1h, nn1w, v + 1));
        }
    }
    
    for (int h = 0; h < N; h++) {
        for (int w = 0; w < N; w++) {
            if (dist[h][w][h][w] == INF) continue;
            ans = min(ans, dist[h][w][h][w]);
        }
    }
    
    cout << (ans == INF ? -1 : ans) << endl;
    return 0;
}
