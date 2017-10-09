#include <stdio.h>
#include <string.h>

static int A[5001], B[5001], c[5001][5001];
int L, R;

int compute(int n, int m) {
	int i, j;

	for (i = 1; i < m; i++) c[i][0] = 0;
	for (i = 0; i < n; i++) c[0][i] = 0;

	for (i = 1; i < m; i++) {
		for (j = 1; j < n; j++) {
			if (A[i] == B[j]) {
				c[i][j] = c[i-1][j-1] + 1;
			}
			else if (c[i-1][j] >= c[i][j-1]) {
				c[i][j] = c[i-1][j];
			}
			else {
				c[i][j] = c[i][j-1];
			}
		}
	}

	return c[m-1][n-1];
}

int main() {
    int m, n, i;
    char E[5001], D[5001];
    
	gets(E);
    gets(D);
    n = strlen(E);
    m = strlen(D);
    
    
    for (i = 0; i < n; i++)
        A[i+1] = E[i];
    for (i = 0; i < m; i++)
        B[i+1] = D[i];
        
	printf("%d\n", compute(n+1, m+1));
	
	return 0;
}
