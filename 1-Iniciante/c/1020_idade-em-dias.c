#include <stdio.h>

int main() 
{
    int ano = 0, mes = 0, dia = 0, A;
    scanf("%d", &A);
    while (A > 0) {
        if (A >= 365) {
            A -= 365;
            ano++; 
        } else if (A >= 30) {
            A -= 30;
            mes++;
        } else {
            A -= 1;
            dia++;
        }
    } 
    printf("%d ano(s)\n", ano);
    printf("%d mes(es)\n", mes);
    printf("%d dia(s)\n", dia);
    return 0;
}