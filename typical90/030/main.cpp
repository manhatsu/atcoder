#include <iostream>
#include <vector>

using namespace std;

// 素数を求める関数
vector<int> getPrimes(int n) {
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = false;
    is_prime[1] = false;
    for (int i = 2; i * i <= n; i++) {
        if (!is_prime[i]) continue;
        for (int j = i * 2; j <= n; j += i) {
            is_prime[j] = false;
        }
    }

    vector<int> primes;
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) primes.push_back(i);
    }
    return primes;
}

int main() {
    int N, K;
    cin >> N >> K;

    vector<int> primes = getPrimes(N);
    vector<int> S(N + 1, 0);

    for (int p : primes) {
        for (int bp = p; bp <= N; bp += p) {
            S[bp]++;
        }
    }

    int ans = 0;
    for (int s : S) {
        if (s >= K) {
            ans++;
        }
    }

    cout << ans << endl;
    return 0;
}
