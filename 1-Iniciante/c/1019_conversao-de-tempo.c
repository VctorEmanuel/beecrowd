#include <stdio.h>

int main()
{
    int n, horas = 0, minutos = 0, segundos = 0;
    scanf("%d", &n);
    while (n > 0) {
        if (n > 3600) {
            horas++;
            n -= 3600;
        } else if (n > 60) {
            minutos++;
            n -= 60;
        } else {
            segundos = n;
            n = 0;
        }
    }
    printf("%d:%d:%d\n", horas, minutos, segundos);
    return 0;
}