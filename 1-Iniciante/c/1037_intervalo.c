#include <stdio.h>

int main() {
    double informado;
    scanf("%lf", &informado);
    if (0 <= informado && informado <= 25) {
        printf("Intervalo [0,25]\n");
    } else if (25 < informado && informado <= 50) {
        printf("Intervalo (25,50]\n");
    } else if (50 < informado && informado <= 75) {
        printf("Intervalo (50,75]\n");
    } else if (75 < informado && informado <= 100) {
        printf("Intervalo (75,100]\n");
    } else {
        printf("Fora de intervalo\n");
    }
    return 0;
}