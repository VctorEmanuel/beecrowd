#include <stdio.h>

int main () {
    float y;
    int x, ns = 0;
    for (x = 0; x < 6; x++) {
        scanf("%f", &y);
        if (y > 0) {
            ns++;
        }
    }
    printf("%d valores positivos\n", ns);
    return 0;
}