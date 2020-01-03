#include <stdio.h>

int main(){
  int t; 
  scanf("%d", &t);

  for (int i = 0; i < t; i++){
    long int n; 
    scanf("%ld", &n);

    long int sum = n * (n + 1) / 2;
    long int sum_sq = n * (n + 1) * (2 * n + 1) / 6;
    printf("%ld\n", sum * sum - sum_sq);
  }

  return 0;
}

