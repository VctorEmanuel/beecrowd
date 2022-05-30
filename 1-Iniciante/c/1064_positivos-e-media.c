#include <stdio.h>

int main () {
    float y, positivos = 0;
    int ns = 0;
    for (int x = 0; x < 6; x++) {
        scanf("%f", &y);
        if (y > 0) {
            ns++;
            positivos =+ y;
        }
    }
    printf("%d valores positivos\n%.1f\n", ns, positivos/ns);
    return 0;
}