#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n, t;
    scanf("%d %d", &n, &t);
    int num[n], in, out, i, j, min;
    
    for (i = 0; i < n; i++)
        scanf("%d", &num[i]);
    
    for (i = 0; i < t; i++) {
        scanf("%d %d", &in, &out);
        min = 4;
        for (j = in; j <= out; j++)
            if (num[j] < min) min = num[j];
        printf("%d\n", min);
    }
        
    return 0;
}

