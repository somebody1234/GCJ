/* 
 
Google Code Jam Qualification Round
April 8, 2016

Jesse Pritchard
Public contact: chaserdevelopment@gmail.com
 
Problem D

*/

#include "stdio.h"
#include "stdlib.h"
#include "math.h"

typedef unsigned long long ubig;
typedef long long big;

ubig bpow(ubig val, ubig exponent) {
    if (exponent == 1) {
        return val;
    }
    else if (exponent == 0) {
        return 1;
    }
    
    ubig inc = val;
    
    exponent--;
    while (exponent--) {
        inc *= val;
    }
    return inc;
}

ubig getsubsetindex( ubig K, ubig C, ubig* sublist, int num ) {
    int i;
    ubig result = 0;
    for (i = 0; i < num; i++) {
        result += sublist[i] * bpow(K, C - i - 1);
    }
    return result;
}

int main() {
    int num, iii;
    scanf(" %d", &num);
    for (iii = 0; iii < num; iii++) {
        
        ubig K, C, S;
        scanf(" %llu %llu %llu", &K, &C, &S);
        if (S * C < K) {
            printf("Case #%d: IMPOSSIBLE\n", iii + 1);
            continue;
        }
        
        
        ubig* sub = malloc(C * sizeof(ubig));
        
        printf("Case #%d: ", iii + 1);
        ubig i = 0, j;
        while (i < K) {
            ubig orig_i = i;
            for (j = i; j < orig_i + C; j++, i++) {
                sub[j - orig_i] = j;
            }
            
            ubig index = getsubsetindex(K, C, sub, i > K ? (int)C - (int)(i - K) : (int)C);
            
            printf("%llu ", index + 1);
        }
        printf("\n");
        
        free(sub);
    }
    return 0;
}


