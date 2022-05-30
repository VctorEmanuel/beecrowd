#include <stdio.h>

int main ()
{
    int notas[6] = {0, 0, 0, 0, 0, 0}, moedas[6] = {0, 0, 0, 0, 0, 0};
    int valor, valor2;
    double informado, valor2_0;

    scanf("%lf", &informado);

    valor = informado;
    valor2 = informado;
    notas[0] = valor/100;
    valor = valor%100;
    notas[1] = valor/50;
    valor = valor%50;
    notas[2] = valor/20;           // notas
    valor = valor%20;
    notas[3] = valor/10;
    valor = valor%10;
    notas[4] = valor/5;
    valor = valor%5;
    notas[5] = valor/2;
    moedas[0] = valor%2;

    valor2_0 = informado*100; // multiplica o que sobrou pra virar um inteiro
    valor2 = (int)valor2_0; // transforma em inteiro

    valor2 = valor2%100;
    moedas[1] = valor2/50;
    valor2 = valor2%50;
    moedas[2] = valor2/25;           // moedas
    valor2 = valor2%25;
    moedas[3] = valor2/10;
    valor2 = valor2%10;
    moedas[4] = valor2/5;
    moedas[5] = valor2%5;

    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100.00\n", notas[0]);
    printf("%d nota(s) de R$ 50.00\n", notas[1]);
    printf("%d nota(s) de R$ 20.00\n", notas[2]);
    printf("%d nota(s) de R$ 10.00\n", notas[3]);
    printf("%d nota(s) de R$ 5.00\n", notas[4]);
    printf("%d nota(s) de R$ 2.00\n", notas[5]);
    printf("MOEDAS:\n");
    printf("%d moeda(s) de R$ 1.00\n", moedas[0]);
    printf("%d moeda(s) de R$ 0.50\n", moedas[1]);
    printf("%d moeda(s) de R$ 0.25\n", moedas[2]);
    printf("%d moeda(s) de R$ 0.10\n", moedas[3]);
    printf("%d moeda(s) de R$ 0.05\n", moedas[4]);
    printf("%d moeda(s) de R$ 0.01\n", moedas[5]);

   return 0; 
}