/* 
 
Google Code Jam Qualification Round
April 8, 2016

Jesse Pritchard
Public contact: chaserdevelopment@gmail.com
 
Problem A

*/

#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "math.h"

/* (See below for definitions) */
void toString(long val, char* buf);
long fromString(char* s);
void strreverse(char* s, char* o);
long reverseint(long N);


long min(long x, long y) {
    return x < y ? x : y;
}

void calculate_seen(long num, int* test) {
    char buf[100];
    snprintf(buf, 100, "%ld", num);
    int i;
    for (i = 0; i < strlen(buf); i++) {
        test[buf[i] - 48] = 1;
    }
}

int all_seen(int* test) {
    int i;
    for (i = 0; i < 10; i++) {
        if (!test[i]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    long num, iii;
    scanf(" %ld", &num);
    for (iii = 0; iii < num; iii++) {
        
        int test[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        
        long N;
        scanf(" %ld", &N);
        
        if (N == 0) {
            printf("Case #%ld: INSOMNIA\n", iii + 1);
            continue;
        }
        
        long incremented = N;
        calculate_seen(incremented, test);
        while (!all_seen(test)) {
            incremented += N;
            calculate_seen(incremented, test);
        }
        
        printf("Case #%ld: %ld\n", iii + 1, incremented);
    }
    return 0;
}
































































/* 
 
 STRING/INT MANIPULATION:
 
 */



void toString(long val, char* buf){
    char comp[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    
    int negative = 0;
    if (val < 0) {
        negative = 1;
        val *= -1;
    }
    
    long digtest = val;
    int digits = 1;
    while (digtest >= 10) {
        digtest /= 10;
        digits++;
    }
    if (val == 0) {
        digits = 1;
    }
    else if (negative) {
        digits++;
        buf[0] = '-';
    }
    
    long iii, k;
    for (iii = negative; iii < digits; iii++) {
        k = val / 10;
        buf[digits - (iii + (!negative))] = comp[val - (k * 10)];
        val /= 10;
    }
    
    buf[digits] = '\0';
    return;
}

long fromString(char* s){
    long val = 0;
    while (*s){
        val *= 10;
        val += *s++ - 48;
    }
    return val;
}

void strreverse(char* s, char* o){
    char* c = s;
    int len = 1;
    while (*c++) {
        len++;
    }
    int i;
    for (i = 0; i < len - 1; i++) {
        o[i] = s[len - 2 - i];
    }
    o[len - 1] = 0;
}

long reverseint(long N){
    char buf[100];
    char rev[100];
    toString(N, buf);
    strreverse(buf, rev);
    long t = fromString(rev);
    return t;
}