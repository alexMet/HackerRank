#include <stdio.h>

int reverse(int n) {
  int reversed;

  for (reversed = 0; n > 0; n /= 10)
    reversed = 10 * reversed + n % 10;

  return reversed;
}

int is_palindrome(int n) {
  return n == reverse(n);
}

int find_palindrome(int n) {
  int largest_palindrome = 0;

  for (int a = 999; a >= 100; a--) {
    int b, db;

    if (a % 11 == 0) {
      b = 999;
      db = 1;
    }
    else {
      b = 990;
      db = 11;
    }

    for (; b >= a; b -= db) {
      int ab = a * b;

      if (ab >= n)
        continue;

      if (ab <= largest_palindrome)
        break;

      if (is_palindrome(ab))
        largest_palindrome = ab;
    }
  }

  return largest_palindrome;
}

int main(){
  int t; 
  scanf("%d", &t);

  for (int i = 0; i < t; i++){
    int n; 
    scanf("%d", &n);
    printf("%d\n", find_palindrome(n));
  }

  return 0;
}

