#include <stdio.h>
#include <stdlib.h>
#define MAX 2147483647

int main() {
    char n1[500];
    char n2[500];
    char operation;
    while (scanf("%s %c %s", n1, &operation, n2) != EOF) {
        double x;
        double y;
        printf("%s %c %s\n", n1, operation, n2);
        x = atof(n1);
        y = atof(n2);

        if (x > MAX) {
            printf("first number too big\n");
        }
            
        if (y > MAX) {
            printf("second number too big\n");
        }

        if (operation == '+' && x + y > MAX) {
            printf("result too big\n");
        }
            
        if (operation == '*' && x * y > MAX) {
            printf("result too big\n");
        }
    }
    return 0;
}