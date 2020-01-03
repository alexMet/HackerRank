#include <stdio.h>

#define MAX_N 5000001
static int a[MAX_N];

int count_chain(long int n) {
  if (n < MAX_N && a[n] != 0)
    return a[n];

  int cnt = 0;
  long int k = n;
  while (k != 1) {
    if (k % 2 == 0) {
      k = k >> 1;
      cnt++;
    }
    else {
      k = (3 * k + 1) >> 1;
      cnt += 2;
    }
    
    if (n < MAX_N && k < MAX_N && a[k] != 0) {
      a[n] = a[k] + cnt;
      break;
    }
  }
  
  if (a[n] == 0) a[n] = cnt;
  return cnt;
}

int main(void) {
  int t, longest_chain;
  long int cnt, n, answer;

  for (int i = 0; i < MAX_N; i++)
    a[i] = 0;
  a[1] = 1;
 
  for (int i = 3; i < MAX_N; i++)
    count_chain(i);

  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    scanf("%ld", &n);
    longest_chain = 0;
    answer = 0;
    for (int j = n / 2; j <= n; j++) {
      if (a[j] >= longest_chain) {
        answer = j;
        longest_chain = a[j];
      }
    }

    printf("%ld\n", answer);
  }

  return 0;
}

