#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void insertionSort(int ar_size, int *  ar) {
    int j, key, i, k = 0;
    
    for (j = 1; j < ar_size; j++) {
        key = *(ar+j);
        i = j - 1;
        while (i >= 0 && ar[i] > key) {
            *(ar+i+1) = *(ar+i);
            i--;
            k++;
        }
        *(ar+i+1) = key;
    }
    printf("%d\n", k);
}

int main(void) {
    int _ar_size;
    
    scanf("%d", &_ar_size);
    int _ar[_ar_size], _ar_i;
    for(_ar_i = 0; _ar_i < _ar_size; _ar_i++) { 
        scanf("%d", &_ar[_ar_i]); 
    }

    insertionSort(_ar_size, _ar);

    return 0;
}


