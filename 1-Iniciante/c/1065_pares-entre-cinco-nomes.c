#include <stdio.h>

int main () {
    int ns = 0; 
    float numero;
    for (int x = 0; x < 5; x++) {
        scanf("%f", &numero);
        if (numero % 2 == 0) {
            ns++;
        }
    }
    printf("%d valores pares\n", ns);
    return 0;
}