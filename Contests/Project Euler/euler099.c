#include <stdio.h>
#include <math.h>

#define MAX_N 100000

struct expo {
  int b, e;
  long double x;
};

static struct expo num[MAX_N];

void quick_sort(struct expo *a, int n) {
  if (n < 2)  return;

  long double p = a[n / 2].x;
  struct expo *l = a;
  struct expo *r = a + n - 1;
 
  while (l <= r) {
    if (l->x < p) {
      l++;
      continue;
    }
    if (r->x > p) {
      r--;
      continue;
    }
    struct expo t = *l;
    *l++ = *r;
    *r-- = t;
  }

  quick_sort(a, r - a + 1);
  quick_sort(l, a + n - l);
}

int main(void) {
  int t, k;
  scanf("%d", &t);

  for (int i = 0; i < t; i++) {
    int b, e;
    scanf("%d %d", &b, &e);

    num[i].b = b;
    num[i].e = e;
    num[i].x = e * log10l(b);
  }

  scanf("%d", &k);
  quick_sort(num, t);
  printf("%d %d\n", num[k - 1].b, num[k - 1].e);

  return 0;
}
