#include <stdio.h>

int main () {
    int x;
    for (x = 1; x < 101; x++) {
        if (x % 2 == 0){
            printf("%d\n", x);
        } 
    }
    return 0;
}