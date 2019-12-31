#include <stdio.h>

unsigned long long int sum_divisible_by(int n, int target) {
  unsigned long long int p = target / n;
  return n * p * (p + 1) / 2;;
}

int main(int argc, char *argv[]) {
  int t, n;
  scanf("%d", &t);

  for (int i = 0; i < t; i++) {
    scanf("%d", &n);
    unsigned long long int sum = 0;
    sum += sum_divisible_by(3, n - 1);
    sum += sum_divisible_by(5, n - 1);
    sum -= sum_divisible_by(15, n - 1);
    printf("%lld\n", sum);
  }

  return 0;
}

