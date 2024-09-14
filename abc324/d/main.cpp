#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

const long long MOD = 998244353;
const double INF = numeric_limits<double>::infinity();
const double MINF = -numeric_limits<double>::infinity();

int main() {
    int N;
    cin >> N;  // Nを入力
    string S;
    cin >> S;  // 文字列Sを入力

    // Sを降順にソート
    sort(S.begin(), S.end(), greater<char>());

    // 1から10^7までの平方数を事前に計算
    vector<long long> sq_num_set;
    for (long long i = 0; i  <= 10000000; ++i) {
        sq_num_set.push_back(i * i);
    }

    int ans = 0;
    for (long long sq : sq_num_set) {
        string T = to_string(sq);  // 平方数を文字列に変換
        sort(T.begin(), T.end(), greater<char>());  // 平方数も降順にソート

        // Sの長さが平方数より短い場合はスキップ
        if (S.size() < T.size()) {
            continue;
        }

        // SとTを比較
        bool isSame = true;
        for (int i = 0; i < T.size(); i++) {
            if (T[i] != S[i]) {
                isSame = false;
                break;
            }
        }

        // Sの残り部分が'0'以外のとき
        if (T.size() < S.size()) {
            for (int i = T.size(); i < S.size(); i++) {
                if (S[i] != '0') {
                    isSame = false;
                    break;
                }
            }
        }

        // 一致していれば答えをカウント
        if (isSame) {
            ans++;
        }
    }

    cout << ans << endl;  // 結果を出力
    return 0;
}
