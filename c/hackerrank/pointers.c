/* Reads two integers as argument and prints
 *   - the sum of
 *   - the absolute difference
 * Must pass values to functions via pointers
 *
 * https://www.hackerrank.com/challenges/pointer-in-c/problem
 */
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int MAX_DIGITS = 21;  // For 64bit int, with -
const int BASE10 = 10;

// Get the sum of 2 ints
int get_sum(int int_ary[]) { return int_ary[0] + int_ary[1]; }

// Get the absolute difference of 2 ints
int get_absdiff(int int_ary[]) { return abs(int_ary[0] - int_ary[1]); }

int main() {
  char buffer1[MAX_DIGITS];
  char buffer2[MAX_DIGITS];
  char *_ptr;
  scanf("%s %s", buffer1, buffer2);
  int result[] = {(int)strtol(buffer1, &_ptr, BASE10),
                  (int)strtol(buffer2, &_ptr, BASE10)};
  printf("%d\n%d\n", get_sum(result), get_absdiff(result));
  return 0;
}
