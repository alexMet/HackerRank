#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n, x, tree, i, j;
    
    fscanf(stdin, "%d", &n);
    for (i = 0; i < n; i++) {
        fscanf(stdin, "%d", &x);
        
        if (x == 0) tree = 1;
        else {
            tree = 2;
            for (j = 1; j < x; j++) {
                if (j % 2 == 0) tree *= 2;
                else tree += 1;
            }
        }
        printf("%d\n", tree);
    }
   
    return 0;
}

