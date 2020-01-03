#include <math.h>
#include <stdio.h>

int main(int argc,char **argv) {
  int i, t;
  long double sum = 0, num;
  
  scanf("%d", &t);
  for (i = 0; i < t; i++) {
    scanf("%llf", &num);
    sum += num;
  }

  while (sum > 10000000000)
    sum = truncl(sum / 10);

  printf("%.0llf\n", sum);
  return 0;

