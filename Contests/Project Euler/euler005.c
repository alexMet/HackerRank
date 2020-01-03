#include <math.h>
#include <stdio.h>
#include <string.h>

#define MAX_N 41
static int prime[MAX_N];

void sieve(int n) { 
  int temp[n + 1];
  memset(temp, 1, sizeof(temp));

  for (int p = 2; p <= sqrt(n); p++) {
    if (temp[p]) {
      for (int i = p * p; i <= n; i += p)
        temp[i] = 0;
    }
  }

  for (int p = 2, i = 0; p <= n; p++)
    if (temp[p])
      prime[i++] = p;
}

int main(void) {
  int t, n; 
  scanf("%d", &t);
  sieve(MAX_N);

  for (int i = 0; i < t; i++) {
    scanf("%d", &n);

    int res = 1, flag = 1, limit = sqrt(n);
    for (int j = 0; prime[j] <= n; j++) {
      int a = 1;

      if (flag) {
        if (prime[j] <= limit)
          a = log(n) / log(prime[j]);
        else
          flag = 0;
      }

      res *= pow(prime[j], a);
    }

    printf("%d\n", res);
  }

  return 0;
}

