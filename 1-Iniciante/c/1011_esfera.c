#include <stdio.h>
#include <math.h>

int main()
{
    double a;
    scanf("%lf", &a);
    printf("VOLUME = %.3lf\n", (4/3.0) * 3.14159 * pow(a, 3));
    return 0;
}