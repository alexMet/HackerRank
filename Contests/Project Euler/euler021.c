#include <stdio.h>
#include <stdlib.h>

int factor(int num) {
  int dvsr;
  int sum = 1;

  for (dvsr = 2; dvsr * dvsr < num; dvsr++) {
    if (num % dvsr != 0) continue;
    sum += dvsr;
    sum += num / dvsr;
  }

  return sum;
}

int main(int argc, char *argv[]) {
  int i, j, n, max;
  scanf("%d", &n);
  int num[n];

  max = -1;
  for (i = 0; i < n; i++) {
    scanf("%d", &num[i]);
    if (num[i] > max) max = num[i];
  }

  int fact2[max + 1], max2 = -1;
  for (i = 0; i <= max; i++) {
    if ((fact2[i] = factor(i)) > max2)
      max2 = fact2[i];
  }

  int fact[max2+1];
  for (i = 0; i <= max; i++) fact[i] = fact2[i];
  for (i = max+1; i <= max2; i++) fact[i] = -1;

  for (i = 0; i < n; i++) {
    int cnt = 0;
      
    for (j = 0; j < num[i]; j++) {
      if (fact[j] > num[i] && fact[fact[j]] == -1)
        fact[i] = factor(i);
        
      if (fact[j] != j && j == fact[fact[j]])
        cnt += j;
    }

    printf("%d\n", cnt);
  }
  
  return 0;
}

