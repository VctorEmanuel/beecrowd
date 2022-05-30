#include <stdio.h>
#include <math.h>
 
int main() 
{
    double n = 3.14159, raio;
    scanf("%lf", &raio);    // lf recebe o tipo double
    printf("A=%.4lf\n", n * raio * raio);
    return 0;
}