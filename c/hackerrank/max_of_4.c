/* max_of_4.c
 * Function that finds the max of 4 numbers
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int MAX_DIGITS = 21;  // For 64bit uint
const int BASE10 = 10;

// Find the max of 4 ints and return it
int max_of_4(int int1, int int2, int int3, int int4) {
  int max_num = int1;
  int int_ary[4] = {int1, int2, int3, int4};
  const int ary_size = 4;
  for (int i = 0; i < ary_size; i++) {
    if (int_ary[i] > max_num) {
      max_num = int_ary[i];
    }
  }
  return max_num;
}

int main() {
  char buffer1[MAX_DIGITS];
  char buffer2[MAX_DIGITS];
  char buffer3[MAX_DIGITS];
  char buffer4[MAX_DIGITS];
  char *_ptr;

  scanf("%s %s %s %s", buffer1, buffer2, buffer3, buffer4);
  int int1 = (int)strtol(buffer1, &_ptr, BASE10);
  int int2 = (int)strtol(buffer2, &_ptr, BASE10);
  int int3 = (int)strtol(buffer3, &_ptr, BASE10);
  int int4 = (int)strtol(buffer4, &_ptr, BASE10);

  int result = max_of_4(int1, int2, int3, int4);
  printf("%d\n", result);
}
