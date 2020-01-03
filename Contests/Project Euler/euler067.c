#include <stdio.h>
#include <stdlib.h>

#define N 100
static int m[N][N], a[N][N];

int max (int a, int b) {
    return (a > b) ? a : b;
}

void read_triangle(int n) {
  for (int slice = 0; slice < n; ++slice) {
    int z = slice < n ? 0 : slice - n + 1;
    for (int j = z; j <= slice - z; ++j)
      scanf("%d", &a[j][slice - j]);
  }
}

void calculate_paths(int n) {
  m[0][0] = a[0][0];
  for (int slice = 1; slice < n; ++slice) {
    int z = slice < n ? 0 : slice - n + 1;
    for (int j = z; j <= slice - z; ++j) {
      if (slice - j == 0)
        m[j][slice - j] = m[j-1][slice-j] + a[j][slice-j];
      else if (j == 0) 
        m[j][slice - j] = m[j][slice-j-1] + a[j][slice-j];
      else
        m[j][slice-j] = max(m[j-1][slice-j] + a[j][slice-j], m[j][slice-j-1] + a[j][slice-j]);
    }
  }
}

int get_solution(int n) {
  int sol = m[0][n-1];
  
  for (int i = 1; i < n; i++) 
    if (m[i][n-i-1] > sol) 
      sol = m[i][n-i-1];
  
  return sol;
}

int main(int argc, char **argv) {
  int t, n;

  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    scanf("%d", &n);
    read_triangle(n);
    calculate_paths(n);
    int answer = get_solution(n);
    printf("%d\n", answer);
  }

  return 0;
}

