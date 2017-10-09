#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n, i;
    unsigned int num;
    
    scanf("%d", &n);
    
    for (i = 0; i < n; i++) {
        scanf("%ud", &num);
        printf("%u\n", ~num);
    }
        
    return 0;
}

