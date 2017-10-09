#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

void quick_sort (int *a, int na) {
    if (na < 2)
        return;
    
    int p = a[na / 2];
    int *l = a;
    int *r = a + na - 1;
    
    while (l <= r) {
        if (*l < p) {
        	l++;
            continue;
        }
        if (*r > p) {
            r--;
            continue; // we need to check the condition (l <= r) every time we change the value of l or r
        }
        
        int t = *l;
        *l++ = *r;
        *r-- = t;
    }
    
    quick_sort(a, r - a + 1);
    quick_sort(l, a + na - l);
}

int main(){
    int n, k, cnt, min, cur; 
    
    scanf("%d %d", &n, &k);
    int *x = malloc(sizeof(int) * n);
    
    for (int i = 0; i < n; i++)
       scanf("%d", &x[i]);
    
    quick_sort(x, n);
    
    cnt = 1;
    cur = min = x[0];
    for (int i = 1; i < n; i++) {
        if (x[i] - min <= k) {
            cur = x[i];
        }
        
        if (x[i] - cur > k) {
            cur = min =  x[i];
            cnt++;
        }
    }
        
    printf("%d\n", cnt);
    
    return 0;
}

