#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

const int MOD = 998244353;
const int INF = numeric_limits<int>::max();

int main() {
    int N, X;
    cin >> N >> X;
    
    vector<pair<int, int>> V1, V2, V3;
    
    for (int i = 0; i < N; i++) {
        int v, a, c;
        cin >> v >> a >> c;
        if (v == 1) {
            V1.emplace_back(a, c);
        } else if (v == 2) {
            V2.emplace_back(a, c);
        } else {
            V3.emplace_back(a, c);
        }
    }
    
    vector<vector<int>> dp1(V1.size() + 1, vector<int>(X + 1, 0));
    vector<vector<int>> dp2(V2.size() + 1, vector<int>(X + 1, 0));
    vector<vector<int>> dp3(V3.size() + 1, vector<int>(X + 1, 0));
    
    for (size_t i = 0; i < V1.size(); i++) {
        for (int j = 0; j <= X; j++) {
            int a = V1[i].first, c = V1[i].second;
            dp1[i + 1][j] = max(dp1[i + 1][j], dp1[i][j]);
            if (j + c <= X) {
                dp1[i + 1][j + c] = max(dp1[i + 1][j + c], dp1[i][j] + a);
            }
        }
    }
    
    for (size_t i = 0; i < V2.size(); i++) {
        for (int j = 0; j <= X; j++) {
            int a = V2[i].first, c = V2[i].second;
            dp2[i + 1][j] = max(dp2[i + 1][j], dp2[i][j]);
            if (j + c <= X) {
                dp2[i + 1][j + c] = max(dp2[i + 1][j + c], dp2[i][j] + a);
            }
        }
    }
    
    for (size_t i = 0; i < V3.size(); i++) {
        for (int j = 0; j <= X; j++) {
            int a = V3[i].first, c = V3[i].second;
            dp3[i + 1][j] = max(dp3[i + 1][j], dp3[i][j]);
            if (j + c <= X) {
                dp3[i + 1][j + c] = max(dp3[i + 1][j + c], dp3[i][j] + a);
            }
        }
    }
    
    int ans = 0;
    for (int i = 0; i <= X; i++) {
        for (int j = 0; j <= X - i; j++) {
            int min_w = min({dp1[V1.size()][i], dp2[V2.size()][j], dp3[V3.size()][X - i - j]});
            ans = max(ans, min_w);
        }
    }
    
    cout << ans << endl;
    return 0;
}
