#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i, x, n;
    
    fscanf(stdin, "%d", &n);
    for (i = 0; i < n; i++) {
        fscanf(stdin, "%d", &x);
        printf("%d\n", x+1);
    }
        
    return 0;
}

