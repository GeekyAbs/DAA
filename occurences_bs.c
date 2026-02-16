// given a sorted array, find the first_occ and last_occ of an element. Time
// Complexity: O(log n)

#include <stdio.h>
#include <stdlib.h>

int first_occ(int arr[], int n, int x) {
  int l = 0, r = n - 1;
  int first = -1;
  while (l <= r) {
    int m = l + (r - l) / 2;
    if (arr[m] == x) {
      first = m;
      r = m - 1;
    } else if (arr[m] > x) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }
  return first;
}

int last_occ(int arr[], int n, int x) {
  int l = 0, r = n - 1;
  int last = -1;
  while (l <= r) {
    int m = l + (r - l) / 2;
    if (arr[m] == x) {
      last = m;
      l = m + 1;
    } else if (arr[m] > x) {
      r = m - 1;
    } else {
      l = m + 1;
    }
  }
  return last;
}

int main() {
  int n;
  printf("Number of elements: \n");
  scanf("%d", &n);
  int *arr = malloc(n * sizeof(int));
  printf("Enter array elements: \n");
  for (int i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }
  int x;
  printf("Target element for occurence: ");
  scanf("%d", &x);
  int first = first_occ(arr, n, x);
  int last = last_occ(arr, n, x);
  printf("\nFirst Occurence: %d\nLast Occurence: %d\n", first, last);
  free(arr);
  return 1;
}
