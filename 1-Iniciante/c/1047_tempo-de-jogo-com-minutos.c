#include <stdio.h>

int main () {
    int hi, mi, hf, mf, hora, minuto;
    scanf("%d %d %d %d", &hi, &mi, &hf, &mf);
    hora = hf - hi;
    minuto = mf -mi;
    if (hi == hf) {
        if (mi == mf) {
            hora = 24;
            minuto = 0;
        } else if (mi > mf) {
            hora = 24;
            hora -= 1;
            minuto += 60;
        } else {}
    } else if (hi > hf) {
        hora += 24;
        if (mi > mf) {
            minuto += 60;
            hora -= 1;
        } else {}
    } else {
        if (mi >= mf) {
            hora -= 1;
            minuto += 60;
        } else {}
    }

    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", hora, minuto);

    return 0;
}