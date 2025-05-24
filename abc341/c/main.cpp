#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main() {
    int H, W, N;
    cin >> H >> W >> N;

    string T;
    cin >> T;

    vector<string> F(H);
    for (int i = 0; i < H; i++) {
        cin >> F[i];
    }

    map<char, int> D = {{'L', 0}, {'R', 1}, {'U', 2}, {'D', 3}};
    vector<int> dh = {0, 0, -1, 1};
    vector<int> dw = {-1, 1, 0, 0};

    int ans = 0;
    for (int h = 1; h < H - 1; h++) {
        for (int w = 1; w < W - 1; w++) {
            if (F[h][w] == '#') {
                continue;
            }
            int nh = h;
            int nw = w;
            bool ret = true;
            for (char t : T) {
                nh += dh[D[t]];
                nw += dw[D[t]];
                if (nh < 0 || nw < 0 || nh >= H || nw >= W) {
                    ret = false;
                    break;
                }
                if (F[nh][nw] == '#') {
                    ret = false;
                    break;
                }
            }
            if (ret) {
                ans++;
            }
        }
    }

    cout << ans << endl;

    return 0;
}
