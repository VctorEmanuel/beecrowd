#include <stdio.h>

int main()
{
    int a, b;
    float c;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%f", &c);
    printf("NUMBER = %d\nSALARY = U$ %.2f\n", a, b*c);
    return 0;
}