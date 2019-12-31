#include <math.h>
#include <stdio.h>

#define MAX_N 10000
static int primes[MAX_N];

int is_prime(int n) {
  if (n == 1)
    return 0;
  else if (n < 4)
    return 1;
  else if (n % 2 == 0)
    return 0;
  else if (n < 9)
    return 1;
  else if (n % 3 == 0)
    return 0;
  else {
    int r = floor(sqrt(n));
    int f = 5;

    while (f <= r){
      if (n % f == 0)
        return 0;
      if (n % (f + 2) == 0)
        return 0;
      f += 6;
    }
  }

  return 1;
}

int main(){
  int t; 
  scanf("%d", &t);

  int pcnt = 1;
  primes[0] = 2;
  for (int i = 3; pcnt < MAX_N; i += 2)
    if (is_prime(i))
      *(primes + pcnt++) = i;

  for (int i = 0; i < t; i++) {
    int n; 
    scanf("%d", &n);
    printf("%d\n", *(primes + n - 1));
  }

  return 0;
}

