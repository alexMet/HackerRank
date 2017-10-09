#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n, c[100], i;
    
    for (i = 0; i < 100; i++) c[i] = 0;
    scanf("%d ", &n);
    int a[n], b[n+1];
    
    for (i = 0; i < n; i++) {
        b[i] = 0;
        scanf("%d", &a[i]);
        //printf("%d\n", a[i]);
        c[a[i]]++;
    }
    
    for (i = 1; i < 100; i++) {
        //printf("%d %d\n", i, c[i]);
        c[i] += c[i-1];
        //printf("%d = %d\n", i, c[i]);
    }
    
    for (i = n-1; i > -1; i--) {
        //printf("%d\n", i);
        b[c[a[i]]] = a[i];
        c[a[i]]--;
    }
    
    for (i = 1; i < n; i++) {
        printf("%d ", b[i]);
    }
    printf("%d", b[n]);    
    return 0;
}

