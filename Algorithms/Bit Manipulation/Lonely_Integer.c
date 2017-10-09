#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

int f[101];
int lonelyinteger(int a_size, int* a) {
    for (int i = 0; i < 101; i++)
        if (f[i] == 1) return i;

    return 0;
}

int main() {
    int res, max = -1;
    
    int _a_size, _a_i;
    scanf("%d", &_a_size);
    int _a[_a_size];
    
    for (_a_i = 0; _a_i < 101; _a_i++) f[_a_i] = 0;
    for(_a_i = 0; _a_i < _a_size; _a_i++) { 
        int _a_item;
        scanf("%d", &_a_item);
        
        _a[_a_i] = _a_item;
        f[_a_item]++;
    }
    
    res = lonelyinteger(_a_size, _a);
    printf("%d", res);
    
    return 0;
}

