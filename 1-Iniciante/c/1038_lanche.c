#include <stdio.h>

int main () {
    double codigos_precos[5] = {4.00, 4.50, 5.00, 2.00, 1.50};
    int cod, qtd;
    scanf("%d %d", &cod, &qtd);
    printf("Total: R$ %.2lf\n", codigos_precos[cod-1]*qtd);
    
    return 0;
}