#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        int n;
        scanf("%d", &n);
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }
        int seen = 0;
        int m = 0;
        while (seen != (1<<10)-1) {
            m += n;
            int temp = m;
            while (temp > 0) {
                seen |= 1<<temp%10;
                temp /= 10;
            }
        }
        printf("Case #%d: %d\n", t, m);
    }
}