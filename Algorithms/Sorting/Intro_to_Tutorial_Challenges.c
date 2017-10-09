#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
   
   int _ar_size, N, k;
    scanf("%d", &N);
    scanf("%d", &_ar_size);
        

    int _ar[_ar_size], _ar_i;
    for(_ar_i = 0; _ar_i < _ar_size; _ar_i++) { 
       scanf("%d", &_ar[_ar_i]);
        if (_ar[_ar_i] == N) {
            k = _ar_i;
            break;
        }
    }

    printf("%d\n", k);
   
   return 0;
}
