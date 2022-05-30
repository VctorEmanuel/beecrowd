#include <stdio.h>

int main() {
    char meses[12][11] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
    int informado;
    scanf("%d", &informado);
    printf("%s\n", meses[informado-1]);
    
    return 0;
}