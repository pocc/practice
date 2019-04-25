/* This program prints the sum and differences of ints and floats
 * Input (I=int, F=float):
 * I I
 * F F
 * hasontehusan
 * Output:
 * I_sum I_diff
 * F_sum F_diff
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int MAX_DIGITS = 21;  // For 64bit int, with -
const int BASE10 = 10;

void print_int_sum_diff(const int *var1, const int *var2) {
  printf("%d %d\n", *var1 + *var2, *var1 - *var2);
}

void print_flt_sum_diff(const float *var1, const float *var2) {
  printf("%.1f %.1f\n", *var1 + *var2, *var1 - *var2);
}

int main() {
  char buffer1[MAX_DIGITS];
  char buffer2[MAX_DIGITS];
  char *_ptr;

  int int1;
  int int2;
  float flt1;
  float flt2;

  scanf("%s %s", buffer1, buffer2);
  int1 = (int)strtol(buffer1, &_ptr, BASE10);
  int2 = (int)strtol(buffer2, &_ptr, BASE10);

  scanf("%s %s", buffer1, buffer2);
  flt1 = strtof(buffer1, &_ptr);
  flt2 = strtof(buffer2, &_ptr);

  print_int_sum_diff(&int1, &int2);
  print_flt_sum_diff(&flt1, &flt2);

  return 0;
}
