#include <iostream>
#include <vector>

using namespace std;

long long int to_base(vector<int> &v, int base)
{
    long long int n = 0;
    for (auto it = v.begin(); it != v.end(); ++it)
    {
        n = (n * base) + *it;
    }
    return n;
}

void to_base_2(vector<int> &v, long long int number)
{
    for (auto rit = v.rbegin(); rit != v.rend(); ++rit)
    {
        *rit = number % 2;
        number /= 2;
    }
}

bool is_divisible(vector<int> &v, int base, int divisor)
{
    int rest = 0;
    for (auto it = v.begin(); it != v.end(); ++it)
    {
        rest = ((rest * base) + *it) % divisor;
    }
    return rest == 0;
}

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++)
    {
        int N, J;
        cin >> N >> J;
        cout << "Case #" << t << ": " << endl;

        vector<int> v(N, 0);
        v[0] = 1;
        v[N-1] = 1;

        long long int value = to_base(v, 2);

        vector<int> divisors(9);
        divisors[0] = 3;

        while (J)
        {
            value += 6;
            to_base_2(v, value);

            bool found_total = true;
            for (int base = 3; base <= 10; base++)
            {
                bool found = false;


                for (int divisor = 3; divisor < 1000; divisor+=2)
                {
                    if (is_divisible(v, base, divisor))
                    {
                        found = true;
                        divisors[base - 2] = divisor;
                        break;
                    }
                }

                if (!found)
                {
                    found_total = false;
                    break;
                }
            }

            if (found_total)
            {
                for (auto tmp : v)
                    cout << tmp;
                for (auto tmp : divisors)
                    cout << " " << tmp;
                cout << endl;
                J--;
            }

        }
    }
}