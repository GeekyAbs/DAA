// counting sort in O(n+k)
#include <stdio.h>
#include <stdlib.h>

void count_sort(int arr[], int n) {
  int max = -1;
  for (int i = 0; i < n; i++) {
    max = arr[i] > max ? arr[i] : max;
  }
  int *count = calloc(max + 1, sizeof(int));
  for (int i = 0; i < n; i++) {
    count[i]++;
  }
  int j = 0;
  for (int i = 0; i < sizeof(count); i++) {
    if (count[i] != 0) {
      arr[j] = i;
      j++;
    }
  }
  free(count);
}

int main() {
  int n;
  printf("Number of elements: ");
  scanf("%d", &n);

  int *arr = malloc(n * sizeof(int));
  printf("Enter elements of the array: \n");
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }
  count_sort(arr, n);
  printf("\nSorted Array: \n");
  for (int i = 0; i < n; i++) {
    printf("%d, ", arr[i]);
  }
  free(arr);
  return 1;
}
