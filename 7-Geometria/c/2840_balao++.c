#include <stdio.h>
#include <math.h>

int main () {
    int n, r;
    float pi = 3.1415, v;

    scanf("%d %d", &n, &r);

    v = 1.333333 * pi*pow(n, 3);
    printf("%d\n", (int)floor(r/v));

    return 0;
}