#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> make_divisors(int n)
{
    vector<int> lower_divisors, upper_divisors;
    int i = 1;
    while (i * i <= n)
    {
        if (n % i == 0)
        {
            lower_divisors.push_back(i);
            if (i != n / i)
            {
                upper_divisors.push_back(n / i);
            }
        }
        i++;
    }
    lower_divisors.insert(lower_divisors.end(), upper_divisors.rbegin(), upper_divisors.rend());
    return lower_divisors;
}

int main()
{
    int N;
    cin >> N;

    vector<int> L = make_divisors(N);

    for (int X : L)
    {
        if ((N - X * X * X) % (3 * X) != 0)
        {
            continue;
        }
        int Y = (N - X * X * X) / (3 * X);
        vector<int> M = make_divisors(Y);

        for (int y : M)
        {
            int x = Y / y;
            if (x - y == X)
            {
                cout << x << " " << y << endl;
                return 0;
            }
        }
    }

    cout << -1 << endl;
    return 0;
}
