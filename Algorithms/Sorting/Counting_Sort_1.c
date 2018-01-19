#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n, c[100], i;
    
    for (i = 0; i < 100; i++) c[i] = 0;
    scanf("%d", &n);
    int a[n];
    
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        c[a[i]]++;
    }
    
    for (i = 0; i < 100; i++)
        printf("%d ", c[i]);
        
    return 0;
}

