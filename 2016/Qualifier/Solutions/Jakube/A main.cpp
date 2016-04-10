#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        long long int N;
        cin >> N;

        if (!N)
        {
            cout << "Case #" << t + 1 << ": INSOMNIA" << endl;
            continue;
        }

        int digits = 0;
        int i = 0;

        while (digits != (1<<10) - 1) {
            i++;
            long long int M = N * i;
            while (M) {
                digits |= 1 << (M % 10);
                M /= 10;
            }
        }

        cout << "Case #" << t + 1 << ": " << N * i << endl;
    }
    return 0;
}