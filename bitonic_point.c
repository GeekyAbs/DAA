#include <stdio.h>
#include <stdlib.h>
int bitonic_point(int arr[], int n) {
  int l = 1;
  int r = n - 2;
  while (l <= r) {
    int m = l + (r - l) / 2;
    if (arr[m - 1] < arr[m] && arr[m + 1] < arr[m])
      return m;
    else if (arr[m - 1] < arr[m])
      l = m + 1;
    else
      r = m - 1;
  }
  return -1;
}

int main() {
  int n;
  printf("Number of Elements: \n");
  scanf("%d", &n);
  int *arr = malloc(n * sizeof(int));
  printf("Enter Elements: \n");
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }
  int point = bitonic_point(arr, n);
  printf("Bitonic Point Found at index: %d\n", point);
  free(arr);
  return 0;
}
