#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; t++)
    {
        string s;
        cin >> s;

        int count = 0;
        for (int i = 0; i < s.size() - 1; i++)
        {
            if (s[i] != s[i+1])
                count++;
        }
        if (s.back() == '-')
            count++;

        cout << "Case #" << t << ": " << count << endl;
    }
}