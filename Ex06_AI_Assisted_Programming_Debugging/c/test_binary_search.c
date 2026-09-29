#include <stdio.h>
#include <stdlib.h>
int binary_search(const int *arr, int n, int target);

#define CHECK(cond) do { if (!(cond)) { printf("FAIL line %d: %s\n", __LINE__, #cond); return 1; } } while (0)

int main(void) {
    int a[] = {1, 3, 5, 7, 9};
    CHECK(binary_search(a, 0, 1) == -1);
    CHECK(binary_search(a, 5, 1) == 0);
    CHECK(binary_search(a, 5, 9) == 4);
    CHECK(binary_search(a, 5, 4) == -1);
    int one[] = {5};
    CHECK(binary_search(one, 1, 5) == 0);
    CHECK(binary_search(one, 1, 4) == -1);
    printf("All C tests passed\n");
    return 0;
}
