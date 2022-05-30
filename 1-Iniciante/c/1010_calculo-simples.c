#include <stdio.h>
 
int main() 
{
    char nome[20][2];
    double a, b;
    scanf("%s", &nome);
    scanf("%lf", &a);
    scanf("%lf", &b);
    printf("TOTAL = R$ %.2lf\n", a + (b*0.15));
    return 0;
}